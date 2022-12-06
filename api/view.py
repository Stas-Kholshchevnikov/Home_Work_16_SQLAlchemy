from config import db
from flask import Blueprint, request, json, redirect
from sql_models.models import Users, Offer, Order
from sql_models.utils import convert_dict_users, convert_dict_offers, convert_dict_orders
from sql_models.utils import add_users, add_orders, add_offers
from sql_models.utils import update_users, update_offers, update_orders

#Создание блюпринта
api_blueprint = Blueprint("api_blueprint", __name__)


@api_blueprint.route("/")
def redirect_page():
    """
    Переадрессация на эндпоинт "/users", эндпоинт "/" не используем
    :return:
    """
    return redirect("http://127.0.0.1:5000/users", code=302)


@api_blueprint.route("/users", methods=["GET", "POST"])
def get_post_user():
    """
    Обработка энпоинта "/users", в зависимости от типа запроса
    :return:
    """
    if request.method == "GET":
        result = []
        for user in Users.query.all():
            result.append(convert_dict_users(user))
        return json.dumps(result)
    if request.method == "POST":
        user_data = json.loads(request.data)
        add_users(user_data)
        return f"Пользователь с данными {user_data} создан"


@api_blueprint.route("/users/<int:pk>", methods=["GET", "PUT", "DELETE"])
def get_put_del_user_by_id(pk):
    """
    Обработка энпоинта "/users/id", в зависимости от типа запроса
    :param pk:
    :return:
    """
    if request.method == "GET":
        user = Users.query.get(pk)
        result = convert_dict_users(user)
        return json.dumps(result)

    if request.method == "DELETE":
        user = Users.query.get(pk)
        db.session.delete(user)
        db.session.commit()
        return f"Пользователь с номером {pk} удален"

    if request.method == "PUT":
        user_data = json.loads(request.data)
        user = Users.query.get(pk)
        update_users(user, user_data)
        return f"Данные пользователя с номером {pk} обновлены"


@api_blueprint.route("/orders", methods=["GET", "POST"])
def get_post_orders():
    """
    Обработка энпоинта "/orders", в зависимости от типа запроса
    :return:
    """
    if request.method == "GET":
        result = []
        for order in Order.query.all():
            result.append(convert_dict_orders(order))
        return json.dumps(result)
    if request.method == "POST":
        order_data = json.loads(request.data)
        add_orders(order_data)
        return f"Заказ с данными {order_data} создан"


@api_blueprint.route("/orders/<int:pk>", methods=["GET", "PUT", "DELETE"])
def get_put_del_order_by_id(pk):
    """
    Обработка энпоинта "/order/id", в зависимости от типа запроса
    :param pk:
    :return:
    """
    if request.method == "GET":
        order = Order.query.get(pk)
        result = convert_dict_orders(order)
        return json.dumps(result)

    if request.method == "DELETE":
        order = Order.query.get(pk)
        db.session.delete(order)
        db.session.commit()
        return f"Заказ с номером {pk} удален"

    if request.method == "PUT":
        order_data = json.loads(request.data)
        order = Order.query.get(pk)
        update_orders(order, order_data)
        return f"Данные заказа с номером {pk} обновлены"


@api_blueprint.route("/offers", methods=["GET", "POST"])
def get_post_offers():
    """
    Обработка энпоинта "/offers", в зависимости от типа запроса
    :return:
    """
    if request.method == "GET":
        result = []
        for offer in Offer.query.all():
            result.append(convert_dict_offers(offer))
        return json.dumps(result)
    if request.method == "POST":
        offer_data = json.loads(request.data)
        add_offers(offer_data)
        return f"Договор с данными {offer_data} создан"


@api_blueprint.route("/offers/<int:pk>", methods=["GET", "PUT", "DELETE"])
def get_put_del_offer_by_id(pk):
    """
    Обработка энпоинта "/offers/id", в зависимости от типа запроса
    :param pk:
    :return:
    """
    if request.method == "GET":
        offer = Offer.query.get(pk)
        result = convert_dict_offers(offer)
        return json.dumps(result)

    if request.method == "DELETE":
        offer = Offer.query.get(pk)
        db.session.delete(offer)
        db.session.commit()
        return f"Договор с номером {pk} удален"

    if request.method == "PUT":
        offer_data = json.loads(request.data)
        offer = Offer.query.get(pk)
        update_offers(offer, offer_data)
        return f"Данные договора с номером {pk} обновлены"
