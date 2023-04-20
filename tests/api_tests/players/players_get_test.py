import allure
from requests import Response
import pytest
from utils.api.api import Api


@allure.feature("GET")
class TestPlayersApi:
    @allure.story("Получение списка игроков")
    def test_get_players(self):
        # Act
        result: Response = Api.get_players()
        # Assert
        response_json = result.json()
        with allure.step("Проверяем, что код ответа 200"):
            assert 200 == result.status_code
        with allure.step("Проверяем что в ответе параметр id=1"):
            assert response_json["players"][0]["id"] == 1

