# -*- coding: utf-8 -*-
#
# AtCoderのパフォーマンスとレーティングをグラフに重ねてプロットする
#

import urllib.request
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import numpy as np
import datetime
import time


def download_json(user_list):
    jsondata={}
    for user in user_list:
        url = "https://atcoder.jp/users/" + user + "/history/json"
        jsontext = urllib.request.urlopen(url).read()
        jsondata[user] = json.loads(jsontext, encoding='utf-8')

        time.sleep(1)

    return jsondata

####
# 使用する際は以下の行のユーザ名を変更する
####
userlist = ["chokudai"]
jsondata = download_json(userlist)


range_color_list = [
	[5000, 3600, '#fcde5e'],
	[3600, 3200, '#e4e4e4'],
	[3200, 2800, '#ff9999'],
	[2800, 2400, '#ffcc99'],
	[2400, 2000, '#ffff99'],
	[2000, 1600, '#9999ff'],
	[1600, 1200, '#99ffff'],
	[1200, 800, '#99ff99'],
	[800, 400, '#d2b48c'],
	[400, -4000, '#bfbfbf']
]

alpha = 0.7

fig, ax = plt.subplots(figsize=(8,6))

def plot(username):
    # plot data(Rating)
    x=[]
    y=[]
    for data in jsondata[username]:
        if data["IsRated"]:
    #        x.append(datetime.date.fromisoformat(data["EndTime"].split("T")[0]))
            t = datetime.datetime.strptime(data["EndTime"].split("T")[0],"%Y-%m-%d")
            x.append(t.date())
            y.append(data["NewRating"])

    ax.plot(x, y, label="Rating", marker="o")

    # plot data(Performance)
    x=[]
    y=[]
    for data in jsondata[username]:
        if data["IsRated"]:
    #        x.append(datetime.date.fromisoformat(data["EndTime"].split("T")[0]))
            t = datetime.datetime.strptime(data["EndTime"].split("T")[0],"%Y-%m-%d")
            x.append(t.date())
            y.append(data["Performance"])

    ax.plot(x, y, label="Performance", marker="o")


    # update x limit
    margin = datetime.timedelta(7)
    ax.set_xlim(
        min(ax.get_xlim()[0],mdate.date2num(min(x)-margin)),
        max(ax.get_xlim()[1],mdate.date2num(min(x)+margin)))

    # update y limit
    i = next(i for i, ac in enumerate(range_color_list) if ac[1] <= max(y) < ac[0])
    user_ylim = range_color_list[max(i-1, 0)][0]
    max_ylim = max(ax.get_ylim()[1], user_ylim)
    min_ylim = min(
            ax.get_ylim()[0], 
            min(0, (np.floor(min(y) / 400 - 1) * 400))
    )
    plt.yticks([i*400 for i in range(-10,11)])
    ax.set_ylim(min_ylim, max_ylim)


for user in jsondata.keys():
    plot(user)

# style figure
plt.xlabel("date")
plt.ylabel("Rating")
plt.legend()
plt.grid()
plt.tight_layout()
fig.autofmt_xdate()

# color fill
x1 = ax.get_xlim()
for ac in range_color_list: 
    y_upper, y_lower = np.full(2, ac[0]), np.full(2, ac[1])	
    plt.fill_between(x1, y_upper, y_lower, facecolor=ac[2], alpha=alpha)


plt.show()
