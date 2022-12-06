from config import db


class Users(db.Model):
    """
    Модель класса Users для таблицы БД с названием users
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50))
    role = db.Column(db.String(50))
    phone = db.Column(db.String(20))


class Offer(db.Model):
    """
    Модель класса Offer для таблицы БД с названием offer
    """
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Order(db.Model):
    """
    Модель класса Order для таблицы БД с названием order
    """
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))


def create_database():
    """
    Очистка БД и создание таблиц согласно описанным моделям
    :return:
    """
    db.drop_all()
    db.create_all()


