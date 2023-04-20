# akorolenko_api_tests

Необходимо клонировать репозиторий с небольшим api сервисом на джанго (писала не я) https://github.com/Elvisred/mafia_test
Необходимая версия Python - 3.9 (pip install python)
Настроить интерпретатор
Создать venv (в папке env, так как она находится в .gitignore) командой python -m venv  
Активировать виртуальное окружение командой source env\Scripts\activate
Установить зависимости из файла requirements.txt командой pip install -r requirements.txt
Запустить проект в докере. Для этого устанавливаем docker desktop
Из директории проекта выполнить команды: docker compose build, docker compose up 

Склонировать этот репозиторий с тестами 
Настроить интерпретатор
Создать venv (в папке env, так как она находится в .gitignore) командой python -m venv  
Активировать виртуальное окружение командой source env\Scripts\activate
Установить зависимости из файла requirements.txt командой pip install -r requirements.txt

Тесты запускаются командой python -m pytest tests/дальнейший путь до директории/файла
Отдельный тест можно запустить с ключом -k, например, python -m pytest tests/api_tests/clubs/ -k имя теста
