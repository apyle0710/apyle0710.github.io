import pandas as pd

columns = ["RANK","PLAYER","PLAYER_PAGE","TEAM","TEAM_PAGE","AGE","POS","G","GS","W","L","T","WIN %","COMP.","ATT","COMP.%","YDS","TD","TD%","INT","INT%","LONG","YDS/ATT","YDS/COMP.","YDS/G","RATING","QBR","SKD","SKD_YDS","SKD%","4QC","GWD"]
stats_passing_2018 = pd.read_csv('nfl_passing_stats_2018.csv', names=columns)

rank = list(stats_passing_2018["RANK"])
player = list(stats_passing_2018["PLAYER"])
player_page = list(stats_passing_2018["PLAYER_PAGE"])
team = list(stats_passing_2018["TEAM"])
team_page = list(stats_passing_2018["TEAM_PAGE"])
age = list(stats_passing_2018["AGE"])
pos = list(stats_passing_2018["POS"])
games = list(stats_passing_2018["G"])
gamesstarted = list(stats_passing_2018["GS"])
wins = list(stats_passing_2018["W"])
wins_formatted = [ '%.0f' % elem for elem in wins]
losses = list(stats_passing_2018["L"])
losses_formatted = [ '%.0f' % elem for elem in losses]
ties = list(stats_passing_2018["T"])
ties_formatted = [ '%.0f' % elem for elem in ties]
win_perct = list(stats_passing_2018["WIN %"])
win_perct_formatted = [ '%.3f' % elem for elem in win_perct]
completions = list(stats_passing_2018["COMP."])
attempts = list(stats_passing_2018["ATT"])
comp_perct = list(stats_passing_2018["COMP.%"])
comp_perct_formatted = [ '%.1f' % elem for elem in comp_perct]
yards = list(stats_passing_2018["YDS"])
tds = list(stats_passing_2018["TD"])
td_perct = list(stats_passing_2018["TD%"])
td_perct_formatted = [ '%.1f' % elem for elem in td_perct]
interceptions = list(stats_passing_2018["INT"])
int_perct = list(stats_passing_2018["INT%"])
int_perct_formatted = [ '%.1f' % elem for elem in int_perct]
long = list(stats_passing_2018["LONG"])
yds_att = list(stats_passing_2018["YDS/ATT"])
yds_att_formatted = [ '%.1f' % elem for elem in yds_att]
yds_comp = list(stats_passing_2018["YDS/COMP."])
yds_comp_formatted = [ '%.1f' % elem for elem in yds_comp]
yds_game = list(stats_passing_2018["YDS/G"])
yds_game_formatted = [ '%.1f' % elem for elem in yds_game]
rating = list(stats_passing_2018["RATING"])
rating_formatted = [ '%.1f' % elem for elem in rating]
qbr = list(stats_passing_2018["QBR"])
qbr_formatted = [ '%.1f' % elem for elem in qbr]
skd = list(stats_passing_2018["SKD"])
skd_yds = list(stats_passing_2018["SKD_YDS"])
skd_perct = list(stats_passing_2018["SKD%"])
skd_perct_formatted = [ '%.1f' % elem for elem in skd_perct]
fourthqtr = list(stats_passing_2018["4QC"])
fourthqtr_perct_formatted = [ '%.0f' % elem for elem in fourthqtr]
gwd = list(stats_passing_2018["GWD"])
gwd_perct_formatted = [ '%.0f' % elem for elem in gwd]


stats_passing_2018_zipped = zip(rank,player,player_page,team,team_page,age,pos,games,gamesstarted,wins_formatted,losses_formatted,ties_formatted,win_perct_formatted,completions,attempts,comp_perct_formatted,yards,tds,td_perct_formatted,interceptions,int_perct_formatted,long,yds_att_formatted,yds_comp_formatted,yds_game_formatted,rating_formatted,qbr_formatted,skd,skd_yds,skd_perct_formatted,fourthqtr_perct_formatted,gwd_perct_formatted)

print("  <div class='horizontal'>")
print("    <div class='table'>")
print("      <article>")
print("        <table>")
print("          <tbody id='standingstable'>")
print("            <tr id='statsheader'>")
print("              <th class='stats30'>RK</th>")
print("              <th class='stats125'>PLAYER</th>")
print("              <th class='stats35'>TEAM</th>")
print("              <th class='stats30'>AGE</th>")
print("              <th class='stats30'>POS</th>")
print("              <th class='stats30'>G</th>")
print("              <th class='stats30'>GS</th>")
print("              <th class='stats30'>W</th>")
print("              <th class='stats30'>L</th>")
print("              <th class='stats30'>T</th>")
print("              <th class='stats40'>WIN%</th>")
print("              <th class='stats40'>COMP</th>")
print("              <th class='stats40'>ATT</th>")
print("              <th class='stats40'>COMP%</th>")
print("              <th class='stats40'>YDS</th>")
print("              <th class='stats30'>TD</th>")
print("              <th class='stats30'>TD%</th>")
print("              <th class='stats30'>INT</th>")
print("              <th class='stats30'>INT%</th>")
print("              <th class='stats40'>LONG</th>")
print("              <th class='stats40'>YDS/ATT</th>")
print("              <th class='stats40'>YDS/COMP</th>")
print("              <th class='stats40'>YDS/G</th>")
print("              <th class='stats40'>RATING</th>")
print("              <th class='stats40'>QBR</th>")
print("              <th class='stats40'>SKD</th>")
print("              <th class='stats40'>SKD_YDS</th>")
print("              <th class='stats40'>SKD%</th>")
print("              <th class='stats40'>4QC</th>")
print("              <th class='stats40'>GWD</th>")
print("            </tr>")


yds_rank=0
for a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af in stats_passing_2018_zipped:
    yds_rank+=1
    print("          <tr>")
    print("            <td>" + str(yds_rank) + "</td>")
    print("            <td id='pagelink'><a href='https://football-stats-and-data.com/" + str(c) + "'>" + str(b) + "</a></td>")
    print("            <td id='pagelink'><a href='https://football-stats-and-data.com/" + str(e) + "'>" + str(d) + "</a></td>")
    print("            <td>" + str(f) + "</td>")
    print("            <td>" + str(g) + "</td>")
    print("            <td>" + str(h) + "</td>")
    print("            <td>" + str(i) + "</td>")
    print("            <td>" + str(j) + "</td>")
    print("            <td>" + str(k) + "</td>")
    print("            <td>" + str(l) + "</td>")
    print("            <td>" + str(m) + "</td>")
    print("            <td>" + str(n) + "</td>")
    print("            <td>" + str(o) + "</td>")
    print("            <td>" + str(p) + "</td>")
    print("            <td>" + str(q) + "</td>")
    print("            <td>" + str(r) + "</td>")
    print("            <td>" + str(s) + "</td>")
    print("            <td>" + str(t) + "</td>")
    print("            <td>" + str(u) + "</td>")
    print("            <td>" + str(v) + "</td>")
    print("            <td>" + str(w) + "</td>")
    print("            <td>" + str(x) + "</td>")
    print("            <td>" + str(y) + "</td>")
    print("            <td>" + str(z) + "</td>")
    print("            <td>" + str(aa) + "</td>")
    print("            <td>" + str(ab) + "</td>")
    print("            <td>" + str(ac) + "</td>")
    print("            <td>" + str(ad) + "</td>")
    print("            <td>" + str(ae) + "</td>")
    print("            <td>" + str(af) + "</td>")
    print("          </tr>")
