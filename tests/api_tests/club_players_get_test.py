import allure
from requests import Response
import pytest

from tests.conftest import random_string
from utils.api.api import Api


@allure.feature("GET")
class TestPlayersApi:
    @allure.story("Получение списка игроков")
    def test_get_club_players(self):
        # Arrange
        nickname = random_string(10)
        result: Response = Api.post_new_player(nickname=nickname, club="Domus", name="Olga Naumova")
        response_post_json = result.json()
        id_player = response_post_json["id"]
        # Act
        result: Response = Api.get_club_players(club_name="Domus")
        response_json = result.json()
        # Assert
        with allure.step("Проверяем, что код ответа 200"):
            assert 200 == result.status_code
        with allure.step(f"Проверяем что в ответе поле nickname={nickname}"):
            assert response_json["players"][-1]["nickname"] == nickname

        Api.delete_players(id_player=id_player)  # удаляем созданного пользователя после теста
