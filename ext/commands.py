from ext.database import db
from models.User import User
from models.Product import Product, Type, producttypes
from werkzeug.security import generate_password_hash


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [User(id=1, username='yago', email='yaduri16@gmail.com', password=generate_password_hash('190201')),
            Product(id=1, name='Camisa Teste', price=10.99),
            Type(id=1, name='Camisetas'),
            Type(id=2, name='Calças'),
            Type(id=3, name='Sapatos'),
            ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    values = 1, 2
    relacao = producttypes.insert(values)
    db.session.execute(relacao)
    db.session.commit()
    return User.query.all()
