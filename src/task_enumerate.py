# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urljoin
import json
import os, urllib
import time


root = "https://atcoder.jp/"    
basedir = "D:/python/atcoder_result"


# コンテストトップページURLとコンテスト名
def get_contest_info(max_page=13):
    
    info_all = {}

    for page in range(1,max_page+1):
        url = "https://atcoder.jp/contests/archive?lang=ja&page=%d" % page
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        table = soup.find_all("table")
        if len(table)==0:
            break

        rows = table[0].find_all("tr")    
        for row in rows:        
            items = row.find_all(['td'])
            if len(items)==0:
                continue
    
            info = {}
            info["url"] = urljoin(root, items[1].find('a').get('href'))
            info["title"] = items[1].get_text()
            info["start"] = items[0].get_text()
            info["duration"] = items[2].get_text()
            info["rated_range"] = items[3].get_text()
            info["contest_screenname"] = info["url"].split('/')[-1]

            info_all[info["contest_screenname"]] = info
                        
    return info_all


# 順位表をダウンロード
def download_standing_json(contest_screenname, dirname):
    
    os.makedirs(dirname, exist_ok=True)
    savename = dirname + "/" + contest_screenname

    # ファイルがすでにあればダウンロードしない
    if not os.path.isfile(savename):
        url = "https://atcoder.jp/contests/" + contest_screenname + "/standings/json"
        print(url)
        try:
            jsontext = urllib.request.urlopen(url).read()
        except urllib.error.URLError as e:
            if e.code == 404:
                return None      
            else:
                raise
        else:
            with open(savename, mode="wb") as f:
                f.write(jsontext)
    else:            
        with open(savename, mode="r", encoding='utf-8') as f:
            jsontext = f.read()
        
    jsondata = json.loads(jsontext, encoding='utf-8')
    return jsondata


# 配点を取得
def get_score(url, savename):
    # ファイルが存在しない場合のみダウンロードする
    if not os.path.isfile(savename) or os.path.getsize(savename)==0:
        r = requests.get(url)
        time.sleep(0.20)

        r.encoding = "utf-8"
        r = r.text
        os.makedirs(os.path.dirname(savename), exist_ok=True)
        with open(savename, mode="w", encoding="utf-8") as f:
            f.write(r)
    else:
        with open(savename, mode="r", encoding="utf-8") as f:
            r = f.read()
            
    soup = BeautifulSoup(r, 'lxml')

    for p in soup.find_all('p'):
        if "配点" in p.get_text():
            match = re.match('.*?(\d+).*', p.get_text())
            if match is not None:
                score = match.group(1)
                return score
    return None


# コンテストページのurlから問題のURLと問題名などを取得
def get_task_info(contest_screenname):
    url = "https://atcoder.jp/contests/" + contest_screenname + '/tasks?lang=ja'
    print(url)

    savename = basedir + "/task/" + contest_screenname + "/top"
    if not os.path.isfile(savename) or os.path.getsize(savename)==0:    
        r = requests.get(url)
        r.encoding = "utf-8"
        r = r.text
        os.makedirs(os.path.dirname(savename), exist_ok=True)
        with open(savename, mode="w", encoding="utf-8") as f:
            f.write(r)
    else:
        with open(savename, mode="r", encoding="utf-8") as f:
            r = f.read()
        
        
        
    soup = BeautifulSoup(r, 'lxml')

    task_info = {}

    # 開始時間、終了時間を取得
    time_tags = soup.find_all('time')
    if len(time_tags)==0:
        pass
    else:
        duration = sorted([time_tags[0].get_text(), time_tags[1].get_text()])

    # 問題情報を取得
    table = soup.find_all("table")
#    if len(table)==0:
#        return None
    task_shown = True
    if len(table)==0:
        task_shown = False
    
    standing_js = download_standing_json(contest_screenname, dirname=basedir + "/contest")
    
    if standing_js is None:
        return None, None

    
    # Ratedコンテストか否か
    rated = False
    for user_data in standing_js["StandingsData"]:
        if user_data["IsRated"]:
            rated = True
            break    

    # --------------------------------
    # 問題が表示されていないケース(wtf19とか)
    if not task_shown: 
        for item in standing_js["TaskInfo"]:
            info = {}
            info["url"] = ""
            info["number"] = item["Assignment"]
            info["title"] = ""
            info["timelimit"] = ""
            info["memorylimit"] = ""
            info["start"] = ""
            info["end"] = ""
            info["difficulty"] = None
            info["total_ac_ratio"] = None
            task_screenname = ""
            for item in standing_js["TaskInfo"]:
                if item["Assignment"] == info["number"]:
                    task_screenname = item["TaskScreenName"]
            info["taskscreenname"] = task_screenname
            
            info["score"] = ""
    
            task_info[task_screenname] = info
        return task_info, rated
    # --------------------------------


    rows = table[0].find_all("tr")    
    for row in rows:        
        items = row.find_all(['td'])
        if len(items)==0:
            continue

        info = {}
        info["url"] = urljoin(root,items[0].find('a').get('href'))
        info["number"] = items[0].get_text()
        info["title"] = items[1].get_text()
        info["timelimit"] = items[2].get_text()
        info["memorylimit"] = items[3].get_text()
        info["start"] = duration[0]
        info["end"] = duration[1]
        info["difficulty"] = None
        info["total_ac_ratio"] = None
        
        task_screenname = ""
        for item in standing_js["TaskInfo"]:
            if item["Assignment"] == info["number"]:
                task_screenname = item["TaskScreenName"]
        info["taskscreenname"] = task_screenname
        
        savename = basedir + "/task/" + contest_screenname + "/" + task_screenname
        info["score"] = get_score(info["url"], savename)

        task_info[task_screenname] = info
        

    
    return task_info, rated



if __name__ == '__main__':
    
    contest_info_map = get_contest_info()
    

    contest_map = {}
    task_dict = {}

    if os.path.isfile(basedir + '/problem.json'): 
        with open(basedir + '/problem.json','r') as f:
            task_dict = json.load(f)
    
    for contest_screenname, contest_info in contest_info_map.items():
        
        # すでに前回取得していれば飛ばす
        if contest_screenname in task_dict.keys():
            continue

        # 問題情報を取得            
        task_info, rated = get_task_info(contest_screenname)
        
        if task_info is None:
            continue

        # 開始日時を入れたいので、問題文から拾えない場合はコンテストページからの値を入れる
        for task_screenname in task_info.keys():
            if task_info[task_screenname]["start"] == "":
                task_info[task_screenname]["start"] = contest_info["start"]
        
        
        task_dict[contest_screenname] = {}
        
        task_dict[contest_screenname]["rated"] = rated
        task_dict[contest_screenname]["start"] = contest_info["start"]
        task_dict[contest_screenname]["task"] = {}
    
        for task_screenname, info in task_info.items():
            
            task_dict[contest_screenname]["task"][task_screenname] = info
            
            
    with open(basedir + '/problem.json','w') as f:
        json.dump(task_dict,f)

    # Excel保存
    if True:
        import win32com.client
        xlApp = win32com.client.Dispatch("Excel.Application")
        xlApp.Visible = 1
        wb = xlApp.Workbooks.Add()
        sheet = wb.Worksheets(1)
        row = 1
        
        task_info_sorted = sorted(task_dict.items(),\
                                 key = lambda x:contest_info_map[x[0]]["start"], reverse=True)

        for contest_screenname, task_info in task_info_sorted:
            for task_screenname, info in task_info["task"].items():

                sheet.Cells(row,1).Value = info["start"]
                sheet.Cells(row,2).Value = info["end"]
                sheet.Cells(row,3).Value = contest_info_map[contest_screenname]["duration"]
                sheet.Cells(row,4).Value = contest_info_map[contest_screenname]["rated_range"]
        
                sheet.Cells(row,5).Value = contest_screenname
                sheet.Cells(row,6).Value = task_screenname
                sheet.Cells(row,7).Value = info["url"]
                
                sheet.Cells(row,8).Value = contest_info_map[contest_screenname]["title"]
                sheet.Hyperlinks.Add(sheet.Cells(row,8), contest_info_map[contest_screenname]["url"])
                sheet.Cells(row,9).Value = info["number"]
                sheet.Cells(row,10).Value = info["title"]
                sheet.Cells(row,11).Value = info["score"]
                sheet.Cells(row,12).Value = info["timelimit"]
                sheet.Cells(row,13).Value = info["memorylimit"]
                sheet.Cells(row,14).Value = "Rated" if task_dict[contest_screenname]["rated"] else "Unrated"
    
                if info["url"] != "":
                    sheet.Hyperlinks.Add(sheet.Cells(row,9), info["url"])
                    sheet.Hyperlinks.Add(sheet.Cells(row,10), info["url"])
           
                row += 1
                
                if row%100==0:
                    print(row)

   