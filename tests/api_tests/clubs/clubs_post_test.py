import allure
import pytest

from tests.conftest import random_string
from utils.api.api import Api
from requests import Response
from utils.db_connector import DbConnector


@allure.feature("POST")
class TestClubPostApi:
    @allure.story("Создание нового клуба")
    def test_post_club(self):
        # Arrange
        club_name = random_string(10)
        # Act
        result: Response = Api.post_new_club(city="Moscow", club_name=club_name)
        response_json = result.json()
        id_club = response_json["id"]
        # Arrange
        with allure.step("Проверяем, что код ответа 201"):
            assert 201 == result.status_code
        with allure.step(f"Проверяем что в ответе параметр id={id_club}"):
            assert response_json["id"] == id_club

        Api.delete_clubs(id_club=id_club)  # удаляем созданный клуб после теста

    @allure.story("Создание нового клуба с уже существующим названием")
    def test_post_exist_club_name(self):
        # Arrange
        db = DbConnector()
        exist_club_name = db.get_first_club()
        # Act
        result: Response = Api.post_new_club(city="Moscow", club_name=exist_club_name)
        response_json = result.json()
        # Assert
        with allure.step("Проверяем, что код ответа 400"):
            assert 400 == result.status_code
        with allure.step("Проверяем что в ответе сообщение об ошибке создания клуба"):
            assert response_json["error"] == "Club with this name already exists"

    @allure.story("Создание нового клуба с некорректными параметрами")
    @pytest.mark.parametrize(
        "club_name, city, error",
        [
            ("", "Moscow", "Club name is required"),  # пустой клабнейм валидный город
            ("TT", "", "City is required"),  # валидный клуб пустой город
            (random_string(31), "Moscow", "Club name must be max 30 characters"),
            # невалидный клуб (длина строки) валидный город
            ("ТЗТЗ", random_string(31), "City must be max 30 characters")
            # валидный клуб невалидный город (длина строки)
        ],
    )
    def test_post_negative_clubs(self, club_name, city, error):
        # Act
        result: Response = Api.post_new_club(city=city, club_name=club_name)
        response_json = result.json()
        # Assert
        with allure.step("Проверяем, что код ответа 400"):
            assert 400 == result.status_code
        with allure.step("Проверяем что в ответе актуальная ошибка"):
            assert response_json["error"] == error
