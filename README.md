Проект 6 спринта Page Object. Автотесты для сервиса «Яндекс.Самокат».

Перед работой с репозиторием требуется установить зависимости

pip install -r requirements.txt
Запустить все тесты из директории tests

pytest tests --alluredir=allure_results
Посмотреть отчет в веб версии пройденного прогона

allure serve allure_results
