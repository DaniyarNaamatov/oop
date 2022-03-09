class Haikyu_1_season:
    def __init__(self, country, genre, kind_of_sport, team_name, official_color):
        self.country = country
        self.genre = genre
        self.kind_of_sport = kind_of_sport
        self.team_name = team_name
        self.official_color = official_color

    def winnings(self):
        return f"{self.team_name} has 3 wins in the first season"

    def __str__(self):
        return f"Country: {self.country}\n" \
               f"Genre: {self.genre}\n" \
               f"Kind of sport: {self.kind_of_sport}\n" \
               f"Team name: {self.team_name}\n" \
               f"Official color: {self.official_color}\n"


season1 = Haikyu_1_season(country="Japan", genre="sport, comedy", kind_of_sport="volleybal",
                          team_name="KARASUNO", official_color="black")

print(season1)
print(season1.winnings())
print("~" * 39)


class Haikyu_2_season(Haikyu_1_season):
    def __init__(self, country, genre, kind_of_sport, team_name, official_color, opposing_team, leader):
        super(Haikyu_2_season, self).__init__(country, genre, kind_of_sport, team_name, official_color)
        self.opposing_team = opposing_team
        self.leader = leader

    def winnings(self):
        return f"In the second season {self.team_name} defeated {self.opposing_team}"

    def __str__(self):
        return super(Haikyu_2_season, self).__str__() + f"Opposing team: {self.opposing_team}\n" \
                                                        f"Leader: {self.leader}\n"


season2 = Haikyu_2_season(country="Japan", genre="sport, comedy", kind_of_sport="volleybal",
                          team_name="KARASUNO", official_color="black",
                          opposing_team="Aobajohsai", leader="Sawamura Daichi")

print(season2)
print(season2.winnings())
print("~" * 49)


class Haikyu_3_season(Haikyu_2_season):
    def __init__(self, country, genre, kind_of_sport, team_name, official_color, opposing_team, leader,
                 friendly_match, new_manager):
        super(Haikyu_3_season, self).__init__(country, genre, kind_of_sport, team_name,
                                              official_color, opposing_team, leader)
        self.friendly_match = friendly_match
        self.new_manager = new_manager

    def winnings(self):
        return f"In the third season {self.team_name} won the {self.opposing_team}," \
               f"but lost to {self.friendly_match} in a friendly match"

    def __str__(self):
        return super(Haikyu_3_season, self).__str__() + f"Friendly match: {self.friendly_match}\n" \
                                                        f"New manager: {self.new_manager}\n"


season3 = Haikyu_3_season(country="Japan", genre="sport, comedy", kind_of_sport="volleybal",
                          team_name="KARASUNO", official_color="black",
                          opposing_team="Dateko", leader="Sawamura Daichi",
                          friendly_match="Nekoma high school", new_manager="Hitoka Yachi")

print(season3)
print(season3.winnings())
print("~" * 94)