from config import db
from sql_models.models import Users, Offer, Order, create_database
from default_data.data import users, offers, orders


def init_tables():
    """
    Создание таблиц БД и наполнение данными
    :return:
    """
    create_database()
    for user in users:
        add_users(user)
    for offer in offers:
        add_offers(offer)
    for order in orders:
        add_orders(order)


def commit_data(object_):
    """
    Подтверждение изменений в БД, выполнение коммита
    :param object_:
    :return:
    """
    db.session.add(object_)
    db.session.commit()


def add_users(user):
    """
    Создание объекта на основе модели класса Users
    :param user:
    :return:
    """
    new_user = Users(
        id=user['id'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        age=user['age'],
        email=user['email'],
        role=user['role'],
        phone=user['phone']
    )
    commit_data(new_user)



def add_offers(offer):
    """
    Создание объекта на основе модели класса Offer
    :param offer:
    :return:
    """
    new_offer = Offer(
        id=offer["id"],
        order_id=offer["order_id"],
        executor_id=offer["executor_id"]
    )
    commit_data(new_offer)


def add_orders(order):
    """
    Создание объекта на основе модели класса Order
    :param order:
    :return:
    """
    new_order = Order(
        id=order["id"],
        name=order["name"],
        description=order["description"],
        start_date=order["start_date"],
        end_date=order["end_date"],
        address=order["address"],
        price=order["price"],
        customer_id=order["customer_id"],
        executor_id=order["executor_id"]
    )
    commit_data(new_order)


def update_users(user, user_data):
    """
    Внесение изменений в значения данных выбранного объекта класса Users
    :param user:
    :param user_data:
    :return:
    """
    user.first_name = user_data['first_name']
    user.last_name = user_data['last_name']
    user.age = user_data['age']
    user.email = user_data['email']
    user.role = user_data['role']
    user.phone = user_data['phone']
    commit_data(user)


def update_offers(offer, offer_data):
    """
    Внесение изменений в значения данных выбранного объекта класса Offer
    :param offer:
    :param offer_data:
    :return:
    """
    offer.order_id = offer_data['order_id']
    offer.executor_id = offer_data['executor_id']
    commit_data(offer)


def update_orders(order, order_data):
    """
    Внесение изменений в значения данных выбранного объекта класса Order
    :param order:
    :param order_data:
    :return:
    """
    order.name = order_data['name']
    order.description = order_data['description']
    order.start_date = order_data['start_date']
    order.end_date = order_data['end_date']
    order.address = order_data['address']
    order.price = order_data['price']
    order.customer_id = order_data['customer_id']
    order.executor_id = order_data['executor_id']
    commit_data(order)


def convert_dict_users(user):
    """
    Преобразование значений объекта класса User в словарь данных
    :param user:
    :return:
    """
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
        "email": user.email,
        "role": user.role,
        "phone": user.phone
    }


def convert_dict_offers(offer):
    """
    Преобразование значений объекта класса Offer в словарь данных
    :param offer:
    :return:
    """
    return {
        "id": offer.id,
        "order_id": offer.order_id,
        "executor_id": offer.executor_id
    }


def convert_dict_orders(order):
    """
    Преобразование значений объекта класса Order в словарь данных
    :param order:
    :return:
    """
    return {
        "id": order.id,
        "name": order.name,
        "description": order.description,
        "start_date": order.start_date,
        "end_date": order.end_date,
        "address": order.address,
        "price": order.price,
        "customer_id": order.customer_id,
        "executor_id": order.executor_id
    }
