from sql_models.utils import init_tables
from config import app
from api.view import api_blueprint


#Регистрация блюпринта для обработки представлений
app.register_blueprint(api_blueprint)


@app.errorhandler(500)
def error_page_500(err):
    """
    Обработка ошибки 500
    :param err:
    :return:
    """
    return f"Ошибка обработки запрса сервером, проверьте правильность указания данных в эндпоинте: {err}"


@app.errorhandler(404)
def error_page_404(err):
    """
    Обработка ошибки 404
    :param err:
    :return:
    """
    return f"Запрошенная страница не существует: {err}"


if __name__ == "__main__":

    # Создание таблиц БД и наполнение их данными
    init_tables()
    app.run()
