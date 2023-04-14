import allure
from requests import Response
import pytest
from utils.api.api import Api

#  ЭТО ВСЕ ПРОСТО ПРИМЕР ИЗ ДРУГОГО ПРОЕКТА


@allure.feature("GET")
class TestClubsApi:
    @allure.story("Получение списка клубов")
    def test_get_clubs(self):
        result: Response = Api.get_clubs()
        response_json = result.json()
        with allure.step("Проверяем, что код ответа 200"):
            print(result.request.url)
            assert 200 == result.status_code
        with allure.step("Проверяем что в ответе параметр id=1"):
            assert response_json["clubs"][0]["id"] == 1
