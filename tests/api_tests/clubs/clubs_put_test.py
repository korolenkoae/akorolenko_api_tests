import allure

from tests.conftest import random_string
from utils.api.api import Api
from requests import Response


@allure.feature("PUT")
class TestClubPutApi:
    @allure.story("Редактирование клубов")
    def test_put_clubs(self):
        # Arrange
        club_name = random_string(10)
        result: Response = Api.post_new_club(city="Moscow", club_name=club_name)
        with allure.step("Проверяем, что код ответа 201"):
            assert 201 == result.status_code
        response_json = result.json()
        put_id = response_json["id"]
        put_city = random_string(10)
        put_club_name = random_string(10)
        # Act
        result: Response = Api.put_clubs(put_id=put_id, city=put_city, club_name=put_club_name)
        # Assert
        with allure.step("Проверяем, что код ответа 200"):
            assert 200 == result.status_code
        response_json_put = result.json()
        with allure.step("Проверяем что в ответе сообщение об обновлении клуба с put_id"):
            assert response_json_put["message"] == f"Club with ID {put_id} updated successfully"

        Api.delete_clubs(id_club=put_id)  # удаляем созданный клуб после теста
