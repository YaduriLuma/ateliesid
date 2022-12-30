from ext.database import db

producttypes = db.Table('producttypes',
                        db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
                        db.Column('type_id', db.Integer, db.ForeignKey('type.id'), primary_key=True)
                        )


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, unique=True, nullable=False)
    producttypes = db.relationship('Type', secondary=producttypes, lazy='subquery',
                                   backref=db.backref('products', lazy=True))


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
