class JSONFixture:
    @staticmethod
    def for_get_data(ids):
        json = {"ids": [ids]}
        return json

    @staticmethod
    def for_put_game_server(put_id, server_id, title, game, platform, application_id, url, env):
        json = {
            "data": {
                "id": put_id,
                "type": "game-servers",
                "attributes": {
                    "server_id_in_old_game_admin": server_id,
                    "title": title,
                    "game": game,
                    "platform": platform,
                    "application_id": application_id,
                    "url": url,
                    "env": env,
                },
            }
        }

        return json

    @staticmethod
    def for_post_player(nickname, club, name):
        json = {"nickname": nickname, "club": club, "name": name}

        return json

    @staticmethod
    def for_post_clubs(city, club_name):
        json = {"city": city, "club_name": club_name}

        return json

    @staticmethod
    def for_get_clubs(city, club_name):
        json = {"city": city, "club_name": club_name}
        return json
