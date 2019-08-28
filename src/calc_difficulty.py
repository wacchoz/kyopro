from sklearn import linear_model
import urllib.request
import os
import json
import matplotlib.pyplot as plt
import matplotlib
import time
import math
from scipy.special import expit
import datetime



contestlist = [
    ["abc042", "arc058"], 
    ["tenka1-2016-quala"],
    ["agc002"],
    ["tkppc2"],
    ["abc043", "arc059"],
    ["agc003"],
    ["tenka1-2016-qualb"],
    ["abc044", "arc060"],
    ["jag2016autumn"],
    ["agc004"],
    ["tenka1-2016-final", "tenka1-2016-final-open"],
    ["abc045", "arc061"],
    ["code-festival-2016-quala"],
    ["agc005"],
    ["kupc2016"],
    ["code-festival-2016-qualb"],
    ["abc046", "arc062"],
    ["code-festival-2016-qualc"],
    ["agc006"],
#    ["chokudai002"],
    ["ddcc2016-qual"],
    ["abc047", "arc063"],
    ["agc007"],
    ["s8pc-3"],
    ["cf16-final", "cf16-final-open"],
    ["cf16-exhibition", "cf16-exhibition-open"],
    ["cf16-tournament-round1-open"],
    ["cf16-tournament-round2-open"],
    ["cf16-tournament-round3-open"],
    ["cf16-relay-open"],
    ["cf16-exhibition-final", "cf16-exhibition-final-open"],
    ["ddcc2016-final"],
    ["abc048", "arc064"],
    ["abc049", "arc065"],
    ["dwacon2017-prelims"],
    ["abc050", "arc066"],
    ["xmascon16noon","xmascon16","xmascon16midnight"],
    ["agc008"],
#    ["joi2017ho"],
#    ["joi2017yo"],
#    ["joisc2017"],
    ["abc051"],
    ["dwacon2017-honsen"],
    ["abc052", "arc067"],
    ["agc009","jrex2017"],
    ["abc053", "arc068"],
    ["njpc2017"],
    ["agc010"],
    ["abc054"],
    ["abc055", "arc069"],
#    ["chokudai003"],
    ["mujin-pc-2017"],
#    ["rco-contest-2017-qual"],
    ["yahoo-procon2017-qual"],
    ["bcu30"],
    ["agc011"],
    ["abc056", "arc070"],
#    ["rco-contest-2017-final", "rco-contest-2017-final-open"],
    ["yahoo-procon2017-final", "yahoo-procon2017-final-open"],
    ["abc057"],
    ["agc012"],
    ["abc058", "arc071"],
    ["s8pc-4"],
    ["agc013"],
    ["abc059", "arc072"],
    ["abc060", "arc073"],
    ["agc014"],
    ["abc061"],
    ["abc062", "arc074"],
    ["agc015"],
    ["abc063", "arc075"],
    ["abc064"],
    ["agc016"],
    ["abc065", "arc076"],
    ["abc066", "arc077"],
    ["agc017"],
    ["abc067", "arc078"],
    ["agc018"],
    ["chokudai_S001"],
    ["abc068", "arc079"],
    ["abc069", "arc080"],
    ["abc070"],
    ["abc071", "arc081"],
    ["agc019"],
    ["abc072", "arc082"],
    ["abc073"],
    ["abc074", "arc083"],
    ["jag2017summer-day1"],
    ["code-festival-2017-quala"],
    ["jag2017summer-day3"],
    ["tenka1-2017", "tenka1-2017-beginner"],
    ["kupc2017"],
    ["ddcc2017-qual"],
    ["code-festival-2017-qualb"],
    ["abc075"],
    ["code-festival-2017-qualc"],
    ["abc076"],
    ["ddcc2017-final"],
    ["abc077", "arc084"],
    ["abc078", "arc085"],
    ["abc079"],
    ["jag2017autumn"],
    ["cf17-final", "cf17-final-open"],
    ["cf17-exhibition-open"],
    ["cf17-tournament-round1-open"],
    ["cf17-tournament-round2-open"],
    ["cf17-tournament-round3-open"],
    ["cf17-relay-open"],
#    ["hokudai-hitachi2017-1"],
    ["code-thanks-festival-2017", "code-thanks-festival-2017-open"],
    ["abc080"],
    ["colopl2018-qual"],
#    ["joi2018yo"],
    ["abc081", "arc086"],
#    ["hokudai-hitachi2017-2"],
    ["abc082", "arc087"],
    ["abc083", "arc088"],
    ["xmascon17"],
    ["abc084"],
#    ["joi2018ho"],
#    ["joisc2018"],
    ["abc085"],
    ["dwacon2018-prelims"],
    ["agc020"],
#    ["wn2017_1"],
    ["colopl2018-final", "colopl2018-final-open"],
    ["abc086", "arc089"],
    ["soundhound2018"],
    ["abc087", "arc090"],
    ["dwacon2018-final", "dwacon2018-final-open"],
    ["apc001"],
    ["yahoo-procon2018-qual"],
#    ["rco-contest-2018-qual"],
#    ["future-contest-2018-qual"],
    ["abc088"],
    ["yahoo-procon2018-final", "yahoo-procon2018-final-open"],
    ["agc021"],
#    ["future-contest-2018-final", "future-contest-2018-final-open"],
    ["abc089"],
#    ["rco-contest-2018-final", "rco-contest-2018-final-open"],
    ["abc090", "arc091"],
    ["abc091", "arc092"],
    ["abc092", "arc093"],
    ["agc022"],
    ["maximum-cup-2018"],
    ["abc093", "arc094"],
    ["abc094", "arc095"],
    ["s8pc-5"],
    ["bcu30-2018-qual"],
    ["bcu30-2018"],
    ["abc095", "arc096"],
    ["agc023"],
    ["abc096"],
    ["abc097", "arc097"],
    ["agc024"],
    ["abc098", "arc098"],
    ["bitflyer2018-qual"],
    ["agc025"],
    ["abc099"],
    ["abc100"],
    ["abc101", "arc099"],
    ["bitflyer2018-final", "bitflyer2018-final-open"],
    ["abc102", "arc100"],
    ["soundhound2018-summer-qual"],
    ["tkppc3"],
    ["agc026"],
    ["abc103"],
    ["soundhound2018-summer-final", "soundhound2018-summer-final-open"],
    ["mujin-pc-2018"],
    ["abc104"],
    ["abc105"],
    ["abc106"],
    ["abc107", "arc101"],
    ["abc108", "arc102"],
    ["abc109"],
    ["agc027"],
    ["jag2018summer-day2"],
    ["code-festival-2018-quala"],
    ["abc110"],
#    ["future-meets-you-contest-2018-open","future-meets-you-contest-2018"],
    ["abc111", "arc103"],
    ["kupc2018"],
    ["abc112"],
    ["agc028"],
    ["code-festival-2018-qualb"],
    ["qupc2018"],
    ["tenka1-2018-beginner", "tenka1-2018"],
    ["abc113"],
#    ["future-contest-2019-qual"],
    ["code-festival-2018-final", "code-festival-2018-final-open"],
    ["cf18-relay-open"],
    ["ddcc2019-qual"],
    ["dwacon5th-prelims"],
    ["code-thanks-festival-2018", "code-thanks-festival-2018-open"],
#    ["future-contest-2019-final-open","future-contest-2019-final"],
    ["abc114"],
    ["abc115"],
    ["joi2019yo"],
    ["agc029"],
    ["caddi2018b", "caddi2018"],
    ["dwacon5th-final", "dwacon5th-final-open"],
    ["pakencamp-2018-day2"],
    ["xmascon18"],
    ["pakencamp-2018-day3"],
    ["agc030"],
#    ["joi2019ho"],
#    ["joisc2019"],
#    ["asprocon2"],
    ["dp"],
    ["aising2019"],
    ["keyence2019"],
    ["ddcc2019-final"],
    ["abc116"],
    ["nikkei2019-qual"],
    ["abc117"],
    ["yahoo-procon2019-qual"],
#    ["rco-contest-2019-qual"],
    ["abc118"],
    ["nikkei2019-final"],
#    ["nikkei2019-ex"],
    ["yahoo-procon2019-final", "yahoo-procon2019-final-open"],
    ["wtf19-open", "wtf19"],
    ["abc119"],
#    ["hokudai-hitachi2018"],
#    ["rco-contest-2019-final", "rco-contest-2019-final-open"],
    ["abc120"],
    ["abc121"],
    ["wupc2019"],
    ["agc031"],
#    ["caddi2019"],
    ["agc032"],
    ["abc122"],
    ["exawizards2019"],
    ["abc123"],
    ["abc124"],
    ["s8pc-6"],
    ["tenka1-2019-beginner", "tenka1-2019"],
    ["abc125"],
    ["iroha2019-day1"],
    ["iroha2019-day2"],
    ["iroha2019-day3"],
    ["iroha2019-day4"],
    ["cpsco2019-s1"],
    ["agc033"],
    ["cpsco2019-s2"],
    ["cpsco2019-s3"],
    ["cpsco2019-s4"],
#    ["asprocon3"],
    ["diverta2019"],
    ["abc126"],
    ["chokudai_S002"],
    ["abc127"],
    ["abc128"],
    ["m-solutions2019"],
    ["agc034"],
    ["abc129"],
    ["diverta2019-2"],
    ["abc130"],
    ["abc131"],
    ["abc132"],
    ["bcu30-2019-qual"],
    ["bcu30-2019"],
    ["abc133"],
    ["agc035"],
    ["abc134"],
    ["agc036"],
    ["tkppc4-1"],
    ["abc135"],
    ["tkppc4-2"],
    ["otemae2019"],
#    ["kuronekoyamato-contest2019"]
    ["abc136"],
    ["abc137"],
    ["agc037"],
    ["abc138"],
    ["jsc2019-qual"]
    ]


basedir = "D:/python/atcoder_result"


# 順位表のjsonファイルを取得する
def download_standing_json(contest, dirname):
    os.makedirs(dirname, exist_ok=True)
    savename = dirname + "/" + contest

    # ファイルがすでにあればダウンロードしない
    if not os.path.isfile(savename) or os.path.getsize(savename)==0:
        url = "https://atcoder.jp/contests/" + contest + "/standings/json"
        print(url)
        jsontext = urllib.request.urlopen(url).read()
        with open(savename, mode="wb") as f:
            f.write(jsontext)
    else:            
        with open(savename, mode="r", encoding='utf-8') as f:
            jsontext = f.read()
        
    jsondata = json.loads(jsontext, encoding='utf-8')
    return jsondata


# ユーザのコンテスト成績表を取得
# requestの文字列がなければdownloadする
def download_user_json(user, request, dirname):
    os.makedirs(dirname, exist_ok=True)
    savename = dirname + "/" + user

    download = True
    if os.path.isfile(savename):
        with open(savename, mode="r", encoding='utf-8') as f:
            jsontext = f.read()
        if request in jsontext:
            download = False

    if download:            
        time.sleep(0.200)
        url = "https://atcoder.jp/users/" + user + "/history/json"
        print(user)
        jsontext = urllib.request.urlopen(url).read()
        with open(savename, mode="wb") as f:
            f.write(jsontext)
    
    jsondata = json.loads(jsontext, encoding='utf-8')
    return jsondata


# 個別のuser_jsonから内部レーティングを取得
# Ratingが無い場合Noneを返す
def get_inner_rating(user_json_ind, contest_screenname, task_info_all):

    rating = None
    inner_rating = None

    for k,v in task_info_all[contest_screenname]["task"].items():
        contest_start = datetime.datetime.strptime(v["start"].replace("T", " "),"%Y-%m-%d %H:%M:%S%z")
        break
    # コンテスト開始前のRated参加回数
    cnt_rated = 0
    for c in user_json_ind:
        t = datetime.datetime.strptime(c["EndTime"].replace("T", " "),"%Y-%m-%d %H:%M:%S%z")
        if t < contest_start:
            if c["IsRated"]:
                rating = c["NewRating"]
                cnt_rated += 1
        else:
            break
                

    # Rating補正を戻す
    if rating is not None and rating!=0:
        if rating <= 400:
            rating = 400 * (1-math.log(400/rating))
        corr = (math.sqrt(1-0.81**cnt_rated) / (1-0.9**cnt_rated) - 1) / (math.sqrt(19)-1) * 1200
    
        inner_rating = rating + corr

    return rating, inner_rating  


# 全参加者のACかどうか、スコアなどの情報取得
def get_AC_info(contest_screenname, task_info_all, X, Y, USER, Score, Score_all):
                    
    print("------------",contest_screenname)
    
    # 順位表を取得
    standing_js = download_standing_json(contest_screenname, dirname=basedir + "/contest")

    if len(standing_js["StandingsData"]) == 0:
        return

    user_json = {}   

    for data in standing_js["StandingsData"]:

        # unratedは集計から除外
#            if not data["IsRated"]:
#                continue

        # nosubは集計から除外
        if data["TotalResult"]["Count"]==0:
            continue

        username = data["UserScreenName"]

        # userデータ取得
        # ratedコンのときは取得
        if task_info_all[contest_screenname]["rated"] is True:
            if username not in user_json.keys():
                user_json[username] = download_user_json(username, request=contest_screenname, dirname=basedir + "/user")
        else:
        # unratedコンのときは取得しない（最新で保存されているratedコン結果を使う）
            if username not in user_json.keys():
                user_json[username] = download_user_json(username, request="", dirname=basedir + "/user")
            

        # jsonからcontestを探す
        # contest開始前までのRating取得と、Rated参加回数をカウント
        rating, inner_rating = get_inner_rating(user_json[username], contest_screenname, task_info_all)

  
        
        for task_screenname in task_info_all[contest_screenname]["task"]:

            if task_screenname not in X.keys():        
                X[task_screenname] = []
                Score[task_screenname] = []
                USER[task_screenname] = []
                Score_all[task_screenname] = {}

                                
            try:
                score = data["TaskResults"][task_screenname]["Score"]
            except:
                score = 0
            
            # レーティングがある人だけ集計
            if inner_rating is not None:                
                X[task_screenname].append([inner_rating])
                Score[task_screenname].append(score)   
                USER[task_screenname].append(username)

            # こっちは全員集計
            Score_all[task_screenname][username] = score
    


def calc_Y_totalACratio(X, Score_all):
    # ABC/ARC同時開催はまとめて処理するように、再度ループする
    total_ac_ratio = {}
    Y = {}
    for task_screenname in X.keys():
        # 集計対象が一人もいなければ飛ばす
#        if len(X[task_screenname])==0:
#            continue

        Y[task_screenname] = []            

        # 簡易的に、全員の最高スコアを満点とみなす
        max_score = max(Score_all[task_screenname].values())

        # 全員0点なら仮で9999点としておく
        if max_score == 0:
            max_score = 9999
    
        for s in Score[task_screenname]:
            Y[task_screenname].append(s//max_score)

        # 除外なしの全員のAC率
        total_ac = 0
        for k,v in Score_all[task_screenname].items():
            if v//max_score == 1:
                total_ac += 1
        total_ac_ratio[task_screenname] = total_ac / len(Score_all[task_screenname])

    return Y, total_ac_ratio
            

# Rating100毎に正答率を集計
def calc_AC_ratio(X, Y, task_screenname):
    min_rate = int(min(X[task_screenname])[0])
    max_rate = int(max(X[task_screenname])[0])
    AC_cnt = {}; submit_cnt = {}
    AC_ratio = {}
    step = 100
    for i in range((min_rate//step-1)*step+step//2, (max_rate//step+1)*step+step//2, step):
        AC_cnt[i] = 0
        submit_cnt[i] = 0
    for x, y in zip(X[task_screenname], Y[task_screenname]):
        x0 = x[0]
        submit_cnt[x0//step * step + step//2] += 1
        if y>0:
            AC_cnt[x0//step * step + step//2] += 1
    for key, val in submit_cnt.items():
        if val > 0:
            AC_ratio[key] = AC_cnt[key] / submit_cnt[key]
            
    return AC_ratio, min_rate, max_rate



def calc_difficulty_and_make_graph(task_screenname, X, Y, savedir):
    # グラフ軸設定
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
#    ax = plt.gca()
    ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1000))
    ax.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(200))
    ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1.0))
    ax.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(0.25))
    ax.grid(which='major',color='gray',linestyle='-')
    ax.grid(which='minor',color='gray',linestyle=':')

    

    # 生データプロット
    ax.plot(X[task_screenname], Y[task_screenname], ".", color='black')
    # AC率プロット
    AC_ratio, min_rate, max_rate = calc_AC_ratio(X, Y, task_screenname)    
    ax.plot(list(AC_ratio.keys()), list(AC_ratio.values()), ls="--", color='blue')

    coef1 = None; coef2 = None
    try:
        # logistic回帰
        lr = linear_model.LogisticRegression(solver='lbfgs')
        lr.fit(X[task_screenname], Y[task_screenname])
    except:
        # ここでエラーになるのは全員正解か全員不正解
        # total_ac_ratioは除外なしとしているので、必ずしも1/0にならない
        if total_ac_ratio[task_screenname] > 0.9:
            difficulty = -1
        if total_ac_ratio[task_screenname] < 0.1:
            difficulty = 9999
    else:
        # 回帰プロット        
        loss = expit( [ i for i in range(min_rate,max_rate+1)] * lr.coef_ + lr.intercept_).ravel()
        ax.plot([ i for i in range(min_rate,max_rate+1)], loss, color='red', linewidth=1)
        # 難易度
        difficulty = -lr.intercept_[0] / lr.coef_[0][0]
        if difficulty <= 400:
            difficulty = 400 * math.exp(-(400-difficulty)/400)

        # 明らかにうまくいっていない場合は手で修正
        if total_ac_ratio[task_screenname] > 0.8 and difficulty > 2000:
            difficulty = 0
        if difficulty > 9999:
            difficulty = 9999

        coef1, coef2 = lr.intercept_[0], lr.coef_[0][0]


    plt.title(task_screenname + ("   (difficulty=%d)" % round(difficulty)))
    plt.xlabel('Inner Rating')
    
    ##########
    # ヒストグラム
    ac_X = []
    wa_X = []
    for x, y in zip(X[task_screenname], Y[task_screenname]):
        x0 = x[0]
        if y>0:
            ac_X.append(x0)
        else:
            wa_X.append(x0)
    ax2=ax.twinx()
    ax2.hist([ac_X, wa_X], bins=50, density=True, color=['green', 'orange'], alpha=0.4, stacked=True)
    ax1_y = ax.get_ylim()
    ax2_y = ax2.get_ylim()

    ax2.set_ylim([ax2_y[1]/ax1_y[1]*ax1_y[0]*1.1, ax2_y[1]*1.1])
    ax2.set_yticklabels([]) # y2軸ラベルを消す
    plt.tick_params(right=False)
    ##########

    # グラフ保存
    os.makedirs(savedir, exist_ok=True)
    plt.savefig(savedir + "/" + task_screenname)

    plt.show()

    task_info = task_info_all[contest_screenname]["task"][task_screenname]
    task_info["difficulty"] = difficulty
    task_info["total_ac_ratio"] = total_ac_ratio[task_screenname]

    print(task_screenname, "difficulty=%8.3f" % difficulty, "%5.2f%%" % (total_ac_ratio[task_screenname]*100))        

    return difficulty, coef1, coef2


if __name__ == '__main__':
    
    ## jsonファイルから問題情報を取得
    with open(basedir + "/problem.json", "r") as f:
        task_info_all = json.load(f)
    
            
    difficulty_dict = {}
    if os.path.isfile(basedir + '/difficulty.json'): 
        with open(basedir + "/difficulty.json", "r") as f:
            difficulty_dict = json.load(f)

   
    for clist in contestlist[::]:
    
        join_contestname = '+'.join(clist)
        
        if join_contestname in difficulty_dict.keys():
            continue


        X={}    # Inner Rating
        Y={}    # AC=1, otherwise 0 （ただしget_AC_info関数では計算されない）
        USER={} # ユーザ名
        Score = {}      # スコア（初参加者は集計から除外）
        Score_all = {}  # スコア（初参加も除外無し）

        for contest_screenname in clist:
            get_AC_info(contest_screenname, task_info_all, X, Y, USER, Score, Score_all)
        
    
        # 集計対象が無いコンテストならスキップ
        if len(X.keys()) == 0:
            continue
    

        total_ac_ratio = {} # トータルのAC率。初参加も除外無し。ABC/ARCは合算
        Y, total_ac_ratio = calc_Y_totalACratio(X, Score_all)      


    
        if join_contestname not in difficulty_dict.keys():
            difficulty_dict[join_contestname] = {}

        for contest_screenname in clist:

            for task_screenname in task_info_all[contest_screenname]["task"]:
                
                # 集計対象が一人もいなければ飛ばす
                if len(X[task_screenname])==0:
                    continue

                savedir=basedir + "/result/" + join_contestname

                # 難易度の計算とグラフ作成
                difficulty, coef1, coef2 = calc_difficulty_and_make_graph(task_screenname, X, Y, savedir)
                
                
                #---------------
                # debug用AC状況
                logfile = savedir + '/' + task_screenname + '.csv'
                with  open(logfile, mode='w') as f_log:
                    for x,y,u in zip(X[task_screenname], Y[task_screenname], USER[task_screenname]):
                        f_log.write("%s,%f,%d\n" % (u, x[0], y))
                #---------------

                
                difficulty_dict[join_contestname][task_screenname] = \
                         [ task_info_all[contest_screenname]["task"][task_screenname]["title"],\
                           task_info_all[contest_screenname]["task"][task_screenname]["url"],\
                           round(difficulty),\
                           total_ac_ratio[task_screenname]*100,\
                           coef1, coef2]
    

#    with open(basedir + "/difficulty.json", "w") as f:
#        json.dump(difficulty_dict, f)
#    
    
    markdown = basedir + "/README.md"
    with open(markdown, mode="w") as f:
        f.write("AtCoderの問題の難易度を推定してみた\n\n")
        f.write("詳しくはこちら ⇒ https://wacchoz.hatenablog.com/entry/2019/08/01/231719\n\n")
        f.write("[難易度順ソートはこちら](./difficulty_sorted.md)\n\n")
        f.write("データは自由に使ってね\n\n")
        f.write("|      |      |      | difficulty | AC ratio |\n")
        f.write("| ---- | ---- | ---- | ---- | ---- |\n")
        
        for contestname in sorted(difficulty_dict.keys(), key=lambda x: task_info_all[x.split("+")[0]]["start"], reverse=True):
            task_dict = difficulty_dict[contestname]
            for taskname, a in task_dict.items():
                f.write("| %s | %s | [%s](%s) | [%d](%s) | %5.2f |\n" \
                        % (contestname, taskname,a[0],a[1],a[2],"./result/"+contestname+"/"+taskname+".png",a[3]))
    
    markdown = basedir + "/difficulty_sorted.md"
    with open(markdown, mode="w") as f:
        f.write("AtCoderの問題の難易度を推定してみた（難易度順ソート）\n\n")
        f.write("詳しくはこちら ⇒ https://wacchoz.hatenablog.com/entry/2019/08/01/231719\n\n")
        f.write("[リスト順はこちら](./README.md)\n\n")
        f.write("データは自由に使ってね\n\n")
        f.write("|      |      |      | difficulty | AC ratio |\n")
        f.write("| ---- | ---- | ---- | ---- | ---- |\n")
        
        dlist = []
        for contestname, vdict in difficulty_dict.items():
            for taskname, info in vdict.items():
                dlist.append([contestname, taskname, info])

        for a in sorted(dlist, key=lambda x: x[2][2]):
            f.write("| %s | %s | [%s](%s) | [%d](%s) | %5.2f |\n" \
                    % (a[0], a[1], a[2][0],a[2][1],a[2][2],"./result/"+a[0]+"/"+a[1]+".png",a[2][3]))
    
    
