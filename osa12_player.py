#osa12-15
"""
Read player infomation from json file, implement the following requirements
- When user inputs 0, stop
- When user inputs 1, Output player info through player_name, format: player_name team_name goals + assists = ?
- When user inputs 2, Output all the team names
- When user inputs 3, Output all the nationalities
- When user inputs 4, Output player info through team_name, format: player_name team_name goals + assists = ?
- When user inputs 5, Output player info through nationality_name, format: player_name team_name goals + assists = ?
- When user inputs 6, Output the required number of players based on the ranking of goals + assists
- When user inputs 7, Output the required number of players based on the ranking of goals + assists

Take the osa.json file as an example:
yanjing@yanjingdeMacBook-Pro src % cd /Users/yanjing/Downloads/osa12/*/src;python3 *.py
tiedosto: osa.json
luettiin 14 pelaajan tiedot

komennot:
0 lopeta
1 hae pelaaja
2 joukkueet
3 maat
4 joukkueen pelaajat
5 maan pelaajat
6 eniten pisteitä
7 eniten maaleja

komento: 1
nimi: Andy Greene
Andy Greene          NYI   2 + 12 =  14

komento: 2
BUF
CGY
DAL
NJD
NYI
OTT
PIT
WPG
WSH

komento: 3
CAN
CHE
CZE
SWE
USA

komento: 4
joukkue: OTT
Drake Batherson      OTT   3 +  7 =  10
Jonathan Davidsson   OTT   0 +  1 =   1

komento: 5
maa: CAN
Jared McCann         PIT  14 + 21 =  35
Travis Zajac         NJD   9 + 16 =  25
Taylor Fedun         DAL   2 +  7 =   9
Mark Jankowski       CGY   5 +  2 =   7
Logan Shaw           WPG   3 +  2 =   5

komento: 6
kuinka monta: 3
Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
John Klingberg       DAL   6 + 26 =  32

komento: 7
kuinka monta: 5
Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
Conor Sheary         BUF  10 + 13 =  23
Travis Zajac         NJD   9 + 16 =  25
John Klingberg       DAL   6 + 26 =  32

komento: 0
"""
import json

class player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.name, self.nationality, self.assists, self.goals, self.penalties, self.team, self.games)

class player_set:
    def __init__(self):
        self.player_set = []
    
    def add_play(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.player_set.append(player(name, nationality, assists, goals, penalties, team, games))
    
    def playerset_list(self):
        return self.player_set

class player_ui:
    def __init__(self, content: list):
        self.content = content
        self.playerdb = player_set()
        for element in self.content:
            self.playerdb.add_play(element["name"], element["nationality"], element["assists"], element["goals"], element["penalties"], element["team"], element["games"])

    def get_player_set_from_file(self):
        return self.playerdb

    def ui_display(self):
        print("komennot:")
        print("0 lopeta")               # stop
        print("1 hae pelaaja")          # Output player info through player_name, format: player_name team_name goals + assists = ?
        print("2 joukkueet")            # Output all the team names
        print("3 maat")                 # Output all the nationalities
        print("4 joukkueen pelaajat")   # Output player info through team_name, format: player_name team_name goals + assists = ?
        print("5 maan pelaajat")        # Output player info through nationality_name, format: player_name team_name goals + assists = ?
        print("6 eniten pisteitä")      # Output the required number of players based on the ranking of goals + assists
        print("7 eniten maaleja")       # Output the required number of players based on the ranking of goals + assists
    
    def output_cmd_1(self, player_name: str):
        result = filter(lambda player: player.name == player_name, self.get_player_set_from_file().playerset_list())
        return list(map(lambda player: (player.name, player.team, player.goals, player.assists), result))
    
    def output_cmd_2(self):
        return sorted(set(list(map(lambda player: player.team, self.get_player_set_from_file().playerset_list()))))
        
    def output_cmd_3(self):
        return sorted(set(list(map(lambda player: player.nationality, self.get_player_set_from_file().playerset_list()))))
    
    def output_cmd_4(self, team_name: str):
        result1 = filter(lambda player: player.team == team_name, self.get_player_set_from_file().playerset_list())
        result2 = list(map(lambda player: (player.name, player.team, player.goals, player.assists), result1))
        return sorted(result2, key = lambda tuple_item: tuple_item[2] + tuple_item[3], reverse = True)

    def output_cmd_5(self, nationality_name: str):
        result1 = filter(lambda player: player.nationality == nationality_name, self.get_player_set_from_file().playerset_list())
        result2 = list(map(lambda player: (player.name, player.team, player.goals, player.assists), result1))
        return sorted(result2, key = lambda tuple_item: tuple_item[2] + tuple_item[3], reverse = True)
    
    def output_cmd_6(self):
        result1 = list(map(lambda player: (player.name, player.team, player.goals, player.assists), self.get_player_set_from_file().playerset_list()))
        result2 = sorted(result1, key = lambda tuple_item: tuple_item[2] + tuple_item[3], reverse = True)
        return result2
    
    def output_cmd_7(self):
        result1 = list(map(lambda player: (player.name, player.team, player.goals, player.assists, player.games), self.get_player_set_from_file().playerset_list()))
        result2 = sorted(result1, key = lambda tuple_item: (tuple_item[2], tuple_item[4]), reverse = True)
        return result2

    def user_interaction(self):
        self.ui_display()
        while True:
            print()
            cmd = int(input("komento: "))
            if cmd == 0:
                break
            elif cmd == 1:
                player_name = input("nimi: ")
                if self.output_cmd_1(player_name) != []:
                    player = self.output_cmd_1(player_name)[0]
                    print(f"{player[0]:21}{player[1]}{player[2]:>4}{'+':>2}{player[3]:>3}{'=':>2}{player[2]+player[3]:>4}")
            elif cmd == 2:
                for item in self.output_cmd_2():
                    print(item)
            elif cmd == 3:
                for item in self.output_cmd_3():
                    print(item)
            elif cmd == 4:
                team_name = input("joukkue: ")
                for player in self.output_cmd_4(team_name):
                    print(f"{player[0]:21}{player[1]}{player[2]:>4}{'+':>2}{player[3]:>3}{'=':>2}{player[2]+player[3]:>4}")
            elif cmd == 5:
                nationality_name = input("maa: ")
                for player in self.output_cmd_5(nationality_name):
                    print(f"{player[0]:21}{player[1]}{player[2]:>4}{'+':>2}{player[3]:>3}{'=':>2}{player[2]+player[3]:>4}")
            elif cmd == 6:
                num = int(input("kuinka monta: "))
                for player in self.output_cmd_6()[0:num]:
                    print(f"{player[0]:21}{player[1]}{player[2]:>4}{'+':>2}{player[3]:>3}{'=':>2}{player[2]+player[3]:>4}")
            elif cmd == 7:
                num = int(input("kuinka monta: "))
                play_list = self.output_cmd_7()[0:num]
                for i in range(0, len(play_list)-1):
                    if play_list[i][2] == play_list[i+1][2]:
                        if play_list[i][4] > play_list[i+1][4]:
                            tmp = play_list[i]
                            play_list[i] = play_list[i+1]
                            play_list[i+1] = tmp
                for player in play_list:
                    print(f"{player[0]:21}{player[1]}{player[2]:>4}{'+':>2}{player[3]:>3}{'=':>2}{player[2]+player[3]:>4}")
            else:
                self.ui_display()

filename = input("tiedosto: ")
with open(filename) as filename:
    data = filename.read()
content = json.loads(data)
print("luettiin {} pelaajan tiedot".format(len(content)))
print()
instance = player_ui(content)
instance.user_interaction()