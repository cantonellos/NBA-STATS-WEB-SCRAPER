from urllib.request import urlopen
import urllib.request
import pymongo
from html_table_parser.parser import HTMLTableParser

import time

#update team's stats
#for the first time you have to insert the records first
#records.insert_one({'name': f'{name}'})

def update_teams():
    client = pymongo.MongoClient( {your pymongo link to your database with write privileges} )
    db = client.get_database('Teams_db')
    records = db.Teams_records
    url = "https://www.basketball-reference.com/leagues/NBA_2022.html"
    print("request")
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    xhtml = f.read().decode('utf-8')
    p = HTMLTableParser()
    p.feed(xhtml)
    j = 0
    for n in range(12, 14):
        matches = p.tables[len(p.tables) - n]
        rows = []
        count = 0
        global icon
        for row in matches:
            rows.append(row)

        for x in range(15):
            count = count + 1
            name = rows[x + 1][0].replace(f"({count})", "")
            wins = rows[x + 1][1]
            loses = rows[x + 1][2]
            percentage = rows[x + 1][3]
            ps = rows[x + 1][5]
            pg = rows[x + 1][6]
            j = j + 3.3
            records.update_one({'name': f'{name}'}, {'$set': {"position": count}})
            records.update_one({'name': f'{name}'}, {'$set': {"wins": f"{wins}"}})
            records.update_one({'name': f'{name}'}, {'$set': {"loses": f"{loses}"}})
            records.update_one({'name': f'{name}'}, {'$set': {"winpercentage": f"{percentage}"}})
            records.update_one({'name': f'{name}'}, {'$set': {"pointsscore": f"{ps}"}})
            records.update_one({'name': f'{name}'}, {'$set': {"pointsgets": f"{pg}"}})
            k = "{:.1f}".format(j)
            print(f"Updating:{k}%")
    print('Teams Updated')

#update players stats
def fill_players(url, threecharacter, update):
    client = pymongo.MongoClient( {your pymongo link to your database with write privileges} )
    db = client.get_database('Players_db')
    records = db.Player
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    xhtml = f.read().decode('utf-8')
    p = HTMLTableParser()
    p.feed(xhtml)
    print("request to open teams")
    time.sleep(10)
    matches = p.tables[len(p.tables) - 4]

    rows = []
    count = 0
    show_update = 0
    for row in matches:
        rows.append(row)

    for x in range(len(rows) - 1):
        name = rows[x + 1][1]
        uniformnumber = rows[x + 1][0]
   #for the first time only
   #    records.insert_one({'name': f'{name}'})
        records.update_one({'name': f'{name}'}, {'$set': {"uniformnumber": f"{uniformnumber}"}})
        onlyname = name[0] + name[1]
        count = 0
        final = ''
        for x in range(len(name)):
            if name[x] == " ":
                if (len(name) - (x + 1)) >= 5:
                    final = (name[x + 1] + name[x + 2] + name[x + 3] + name[x + 4] + name[x + 5])

                else:
                    for s in range(len(name) - (x + 1)):
                        final = final + name[x + 1]
                        x = x + 1

                final = (((final + onlyname + "01").lower()).strip("")).replace(" ", "")
                break
        if final == "capelcl01":
            final = "capelca01"
        if final == "willilo01":
            final = "willilo02"
        if final == "thomaca01":
            final = "thomaca02"
        if final == "edwarke01":
            final = "edwarke02"
        if final == "paytoga01":
            final = 'paytoga02'
        if final == "leeda01":
            final = "leeda03"
        if final == "millspa01":
            final = "millspa02"
        if final == "johnsca01":
            final = "johnsca02"
        if final == "smithja01":
            final = "smithja04"
        if final == "johnsja01":
            final = "johnsja05"
        if final == "williro01":
            final = "williro04"
        if final == "brownja01":
            final = "brownja02"
        if final == "freeden01":
            final = "kanteen01"
        if final == "bridgmi01":
            final = "bridgmi02"
        if final == "waship.01":
            final = "washipj01"
        if final == "schröde01":
            final = "schrode01"
        if final == "šarićda01":
            final = "saricda"
        if final == "matthwe01":
            final = "matthwe02"
        if final == "tuckep.01":
            final = "tuckepj01"
        if final == "martica01":
            final = "martica02"
        if final == "morrima01":
            final = "morrima02"
        if final == "guy(ky01":
            final = "guyky01"
        if final == "greenja01":
            final = "greenja02"
        if final == "thomama01":
            final = "thomama02"
        if final == "jonesde01":
            final = "jonesde02"
        if final == "vučevni01":
            final = "vucevni01"
        if final == "harrito01":
            final = "harrito02"
        if final == "greenda01":
            final = "greenda02"
        if final == "brownch01":
            final = "brownch02"
        if final == "osmance01":
            final = "osmande01"
        if final =="thomais01":
            final ="thomais02"
        if final =="trentga01":
            final = "trentga02"
        if final =="johnsda01":
            final ="johnsda08"
        if final =="walkeke01":
            final ="walkeke02"
        if final =="barneha01":
            final= "barneha02"
        if final =="jonesda01":
            final ="jonesda03"
        if final =="daviste01":
            final ="daviste02"
        if final =="jacksjo01":
            final ="jacksjo02"

        print(final)
        if uniformnumber != "":
            url = f"https://www.basketball-reference.com/players/{final[0]}/{final}/gamelog/2022"
            req = urllib.request.Request(url=url)
            f = urllib.request.urlopen(req)
            xhtml = f.read().decode('utf-8')
            p = HTMLTableParser()
            p.feed(xhtml)
            print("request")
            matchestable = p.tables[len(p.tables) - 1]
            playersrows = []
            count1 = 0
            totalpoints = 0
            totalrebounds = 0
            totalassists = 0
            matchplayed = 0

            for playersrow in matchestable:
                playersrows.append(playersrow)

            for x in range(len(playersrows) - 1):
                count1 = count1 + 1
                if len(playersrows[x + 1]) > 9:
                    if playersrows[x + 1][27] != 'PTS':
                        points = playersrows[x + 1][27]
                        rebounds = playersrows[x + 1][21]
                        assists = playersrows[x + 1][22]

                        totalpoints = totalpoints + int(points)
                        totalassists = totalassists + int(assists)
                        totalrebounds = totalrebounds + int(rebounds)
                        matchplayed = matchplayed + 1



                    else:
                        count1 = count1 - 1
            averagepoints = "{:.1f}".format(totalpoints / matchplayed)
            averagerebounds = "{:.1f}".format(totalrebounds / matchplayed)
            averageassists = "{:.1f}".format(totalassists / matchplayed)
            averagepra = "{:.1f}".format((totalpoints + totalrebounds + totalassists) / matchplayed)
            titlename = name.replace("(TW)", "")
            records.update_one({'name': f'{name}'}, {'$set': {"averagepoints": f"{averagepoints}"}})
            records.update_one({'name': f'{name}'}, {'$set': {"averagerebounds": f"{averagerebounds}"}})
            records.update_one({'name': f'{name}'}, {'$set': {"averageassists": f"{averageassists}"}})
            records.update_one({'name': f'{name}'}, {'$set': {"averagepra": f"{averagepra}"}})
            records.update_one({'name': f'{name}'}, {'$set': {"titlename": f"{titlename}"}})
            records.update_one({'name': f'{name}'}, {'$set': {"team": f"{threecharacter}"}})
            show_update = show_update + (100 / (len(rows) - 1))
            print(f"Updating part {update}:{show_update}%")
            time.sleep(4)
        else:
            titlename = name.replace("(TW)", "")
            records.update_one({'name': f'{name}'}, {'$set': {"titlename": f"{titlename}"}})
            records.update_one({'name': f'{name}'}, {'$set': {"team": f"{threecharacter}"}})




if __name__ == "__main__":
    print("Type 1 to update Teams\nType 2 to update Players\nType 3 to update both")
    x = input()
    if x == '1':
        update_teams()
    elif x=='2':
        print('s')
        url = f"https://www.basketball-reference.com/teams/SAC/2022.html"
        fill_players(url, "SAC", 14)

     #url = f"https://www.basketball-reference.com/teams/MIA/2022.html"
     #fill_players(url,"MIA",1)

     #url = f"https://www.basketball-reference.com/teams/CHI/2022.html"
     #fill_players(url,"CHI",2)

     #url = f"https://www.basketball-reference.com/teams/PHI/2022.html"
     #fill_players(url,"PHI",3)

     #url = f"https://www.basketball-reference.com/teams/CLE/2022.html"
     #fill_players(url, "CLE", 4)

     #url = f"https://www.basketball-reference.com/teams/MIL/2022.html"
     #fill_players(url, "MIL", 5)

     #url = f"https://www.basketball-reference.com/teams/GSW/2022.html"
     #fill_players(url,"GSW",6)

     #url = f"https://www.basketball-reference.com/teams/PHO/2022.html"
     #fill_players(url,"PHO",7)

     #url = f"https://www.basketball-reference.com/teams/CHO/2022.html"
     #fill_players(url,"CHO",8)

     #url = f"https://www.basketball-reference.com/teams/BOS/2022.html"
     #fill_players(url,"BOS",9)

     #url = f"https://www.basketball-reference.com/teams/ATL/2022.html"
     #fill_players(url,"ATL",10)

     #url = f"https://www.basketball-reference.com/teams/TOR/2022.html"
     #fill_players(url,"TOR",11)

     #url = f"https://www.basketball-reference.com/teams/BRK/2022.html"
     #fill_players(url, "BRK", 12)

     #url = f"https://www.basketball-reference.com/teams/NYK/2022.html"
     #fill_players(url, "NYK", 13)














    else:
        print("Unknown value")
