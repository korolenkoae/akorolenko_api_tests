import allure

from tests.conftest import random_string
from utils.api.api import Api
from requests import Response
from utils.db_connector import DbConnector


@allure.feature("POST")
class TestPlayerPostApi:
    @allure.story("Создание нового игрока")
    def test_post_player(self):
        # Arrange
        nickname = random_string(10)
        # Act
        result: Response = Api.post_new_player(nickname, "Red Testing Mafia", "Alina Korolenko")
        response_json = result.json()
        id_player = response_json["id"]
        # Assert
        with allure.step("Проверяем, что код ответа 201"):
            assert 201 == result.status_code
        with allure.step(f"Проверяем что в ответе параметр id={id_player}"):
            assert response_json["id"] == id_player

        Api.delete_players(id_player=id_player)  # удаляем созданного пользователя после теста

    @allure.story("Создание нового пользователя с уже существующим никнеймом")
    def test_post_exist_nickname(self):
        # Arrange
        db = DbConnector()
        exist_nickname = db.get_first_player()
        # Act
        result: Response = Api.post_new_player(nickname=exist_nickname, club="Red Testing Mafia", name="Alina Korolenko")
        response_json = result.json()
        # Assert
        with allure.step("Проверяем, что код ответа 400"):
            assert 400 == result.status_code
        with allure.step("Проверяем что в ответе сообщение об ошибке создания клуба"):
            assert response_json["error"] == "Player with this nickname already exists"
