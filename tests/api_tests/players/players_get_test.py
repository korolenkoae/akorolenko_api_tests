import allure
from requests import Response
import pytest
from utils.api.api import Api

#  ЭТО ВСЕ ПРОСТО ПРИМЕР ИЗ ДРУГОГО ПРОЕКТА


@allure.feature("GET")
class TestGameServersApi:
    @allure.story("Получение списка game servers")
    def test_get_servers(self):
        result: Response = Api.get_game_servers()
        response_json = result.json()
        with allure.step("Проверяем, что код ответа 200"):
            assert 200 == result.status_code
        with allure.step("Проверяем что в ответе параметр type=game-servers, id=1"):
            assert response_json["data"][0]["type"] == "game-servers"
            assert response_json["data"][0]["id"] == "1"
