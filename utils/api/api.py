import logging
import allure

from utils.api.http_manager import HttpManager
from utils.api.json_fixture import JSONFixture


class Api:
    LOGGER = logging.getLogger(__name__)
    api_baseurl = "http://localhost:8000/"
    API_CLUBS = api_baseurl + "api/clubs"
    API_PLAYERS = api_baseurl + "api/players"

    @staticmethod
    @allure.step("Отправляем GET запрос списка игровых серверов")
    def get_game_servers():
        with allure.step("Получение списка игровых серверов"):
            result = HttpManager.get(Api.API_GAME_SERVERS)
            Api.LOGGER.info("TEST: Получение списка игровых серверов. Method: {0}, Data: {1}")
            with allure.step(f"Успешное получение списка игровых серверов {result.json()}"):
                pass
            return result

    @staticmethod
    def put_game_server(put_id, server_id, title, game, platform, application_id, url, env):
        with allure.step(f"Обновление сервера с {put_id, server_id, title, game, platform, application_id, url, env}"):
            result = HttpManager.put(
                Api.API_GAME_SERVERS + put_id,
                JSONFixture.for_put_game_server(put_id, server_id, title, game, platform, application_id, url, env),
            )
            Api.LOGGER.info(
                "TEST: Put News data. Method: {0}, Data: {1}".format(
                    "PUT",
                    JSONFixture.for_put_game_server(
                        put_id, server_id, title, game, platform, application_id, url, env
                    ),
                )
            )
            with allure.step(
                f"Успешное обновление сервера с "
                f"{put_id, server_id, title, game, platform, application_id, url} {result.json()}"
            ):
                pass
            return result

    @staticmethod
    @allure.step("Отправляем DELETE запрос Game Servers с учетом id_server")
    def delete_game_server(id_server):
        with allure.step(f"удаление сервера по параметру - {id_server}"):
            result = HttpManager.delete(Api.API_GAME_SERVERS + id_server)
            Api.LOGGER.info("TEST: Удаление Game server с учетом {id_server}. Method: {0}, Data: {1}")
            with allure.step("Успешное удаление Game Server с учетом id_server"):
                pass
            return result

    @staticmethod
    def post_new_player(nickname, club, name):
        with allure.step(f"Запроса на создание игрока{nickname, club, name}"):
            result = HttpManager.post(
                Api.API_PLAYERS,
                JSONFixture.for_post_player(nickname, club, name),
            )
            Api.LOGGER.info(
                "TEST: Post player data. Method: {0}, Data: {1}".format(
                    "POST", JSONFixture.for_post_player(nickname, club, name)
                )
            )
            with allure.step(f"Успешное создание player с {result.json()}"):
                pass
            return result

    @staticmethod
    def post_new_club(club_name, city):
        with allure.step(f"Запроса на создание клуба{city, club_name}"):
            result = HttpManager.post(
                Api.API_CLUBS,
                JSONFixture.for_post_clubs(city, club_name),
            )
            Api.LOGGER.info(
                "TEST: Post club data. Method: {0}, Data: {1}".format(
                    "POST", JSONFixture.for_post_clubs(city, club_name)
                )
            )
            with allure.step(f"Успешное создание club с {result.json()}"):
                pass
            return result

    @staticmethod
    @allure.step("Отправляем GET запрос списка клубов")
    def get_clubs():
        with allure.step("Получение списка клубов"):
            result = HttpManager.get(Api.API_CLUBS)
            Api.LOGGER.info("TEST: Получение списка клубов. Method: {0}, Data: {1}")
            with allure.step(f"Успешное получение списка клубов {result.json()}"):
                pass
            return result

    @staticmethod
    @allure.step("Отправляем GET запрос списка игроков")
    def get_players():
        with allure.step("Получение списка игроков"):
            result = HttpManager.get(Api.API_PLAYERS + "/")
            Api.LOGGER.info("TEST: Получение списка игроков. Method: {0}, Data: {1}")
            with allure.step(f"Успешное получение списка игроков {result.json()}"):
                pass
            return result

