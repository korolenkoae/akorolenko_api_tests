import allure
from requests import Response
from utils.api.api import Api


@allure.feature("GET")
class TestClubsApi:
    @allure.story("Получение списка клубов")
    def test_get_clubs(self):
        # Act
        result: Response = Api.get_clubs()
        # Assert
        response_json = result.json()
        with allure.step("Проверяем, что код ответа 200"):
            assert 200 == result.status_code
        with allure.step("Проверяем что в ответе параметр id=1"):
            assert response_json["clubs"][0]["id"] == 1
