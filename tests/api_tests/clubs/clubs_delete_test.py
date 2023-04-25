import allure

from tests.conftest import random_string
from utils.api.api import Api
from requests import Response

from utils.db_connector import DbConnector


@allure.feature("DELETE")
class TestClubDeleteApi:
    @allure.story("Удаление клубов")
    def test_delete_clubs(self):
        # Arrange
        club_name = random_string(10)
        result: Response = Api.post_new_club(city="Moscow", club_name=club_name)
        with allure.step("Проверяем, что код ответа 201"):
            assert 201 == result.status_code
        response_json = result.json()
        id_club = response_json["id"]
        # Act
        result: Response = Api.delete_clubs(id_club=id_club)
        # Assert
        response_json_del = result.json()
        with allure.step("Проверяем, что код ответа 200"):
            assert 200 == result.status_code
        with allure.step("Проверяем что в ответе сообщение об удалении клуба с id_club"):
            assert response_json_del["message"] == f"Club with ID {id_club} deleted successfully"

    @allure.story("Удаление клуба с несуществующим id")
    def test_delete_negative_club(self):
        # Arrange
        db = DbConnector()
        new_id_club = db.get_new_id_club()
        # Act
        result: Response = Api.delete_clubs(id_club=new_id_club)
        response_json = result.json()
        # Assert
        with allure.step("Проверяем, что код ответа 400"):
            assert 400 == result.status_code
        with allure.step("Проверяем что в ответе сообщение об ошибке удаления клуба"):
            assert response_json["error"] == "No Club matches the given query."
