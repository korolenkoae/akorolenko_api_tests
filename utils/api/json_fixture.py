class JSONFixture:
    @staticmethod
    def for_post_player(nickname, club, name):
        json = {"nickname": nickname, "club": club, "name": name}

        return json

    @staticmethod
    def for_post_clubs(city, club_name):
        json = {"city": city, "club_name": club_name}

        return json

    @staticmethod
    def for_put_clubs(put_id, club_name, city):
        json = {"id": put_id, "club_name": club_name, "city": city}
        return json

    @staticmethod
    def for_put_players(put_id_player, nickname, club, name):
        json = {"id": put_id_player, "nickname": nickname, "club": club, "name": name}
        return json
