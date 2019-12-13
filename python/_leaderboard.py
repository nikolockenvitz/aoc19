from aoc import AOC
from datetime import datetime
from time import localtime
import json
import os

f = open("../leaderboard.txt", "r")
leaderboardConfig = f.read().splitlines()
f.close()

YEAR = int(leaderboardConfig[0])
LEADERBORD_ID = leaderboardConfig[1]

url = "https://adventofcode.com/{year}/leaderboard/private/view/{lb}.json".format(year=YEAR, lb=LEADERBORD_ID)
data = AOC.getWebsiteData(url)
j = json.loads(data)

def prnt(d, level=0):
    for k in d.keys():
        v = d[k]
        if(type(v) == dict):
            print(" "*2*level + str(k) + ":")
            prnt(v, level+1)
        else:
            print(" "*2*level + str(k) + ": " + str(v))
#prnt(j)

members = {}
names = []
for member in j["members"]:
    current = [None for i in range(53)]
    m = j["members"][member]
    name = str(member)
    names.append(name)
    current[0] = m["local_score"]
    current[1] = m["global_score"]
    current[2] = m["stars"]
    
    days = m["completion_day_level"]
    for day in days.keys():
        for part in days[day].keys():
            ts = int(days[day][part]["get_star_ts"])
            current[2*int(day) + int(part)] = ts

    members[name] = current

names.sort()

html = "<html>"
html += """<head><style>
table {
  border-collapse: collapse;
}
table, tr, td {
  border: 1px solid black;
}
</style></head>"""
html += "<body><table cellspacing=\"0\">"
html += "<tr>"
html += "<td>Name</td>"
for member in names:
    name = j["members"][member]["name"]
    if (name == None): name = member
    html += "<td>" + name + "</td>"
html += "</tr>"

h = 0
for attr in ["Local Score", "Global Score", "Stars"]:
    html += "<tr>"
    html += "<td>" + attr + "</td>"
    for member in names:
        html += "<td>" + str(members[member][h]) + "</td>"
    html += "</tr>"
    h += 1

html += "{WINS}"
wins = [0]*len(members)

for day in range(1,26):
    for part in [1,2]:
        html += "<tr><td>"
        html += "Day {}</td>".format(day) if part == 1 else "</td>" 

        refts = None
        for i in range(len(members)):
            cur = members[names[i]][2*day + part]
            if (cur != None):
                if (refts == None): refts = cur
                else: refts = min(refts, cur)

        for i in range(len(members)):
            member = names[i]
            ts = members[member][2*day + part]
            if(ts == None):
                html += "<td>-</td>"
            else:
                if(refts == None or refts == ts):
                    style = "background-color:#0f0;font-weight:bold;"
                    wins[i] += 1
                else:
                    style = "background-color:#f00;color:#fff;"
                html += "<td style=\"{}\">".format(style)
                ts = datetime.utcfromtimestamp(int(ts+3600)) # 3600: UTC -> UTC+1
                if(ts.day != day or ts.month != 12 or ts.year != YEAR):
                    html += ">18h ({}.{}.)".format(format(ts.day,"02d"),
                                                   format(ts.month,"02d"))
                else:
                    html += "{}:{}:{}".format(format(ts.hour,"02d"),
                                              format(ts.minute,"02d"),
                                              format(ts.second,"02d"))
            html += "</td>"
        html += "</tr>"

html += "</table></body></html>"

hw = "<tr><td>Wins</td>"
for w in wins:
    hw += "<td>" + str(w) + "</td>"
hw += "</tr>"
html = html.replace("{WINS}", hw)

filename = "_leaderboard.html"
f = open(filename,"w")
f.write(html)
f.close()

url = os.path.join(os.path.split(__file__)[0], filename)
os.system("start "+url)
