from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Vendor(db.Model, SerializerMixin):
    __tablename__ = 'vendors'

    serialize_rules = ("-vendor_sweets.vendor",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    vendor_sweets = db.relationship("VendorSweet", backref="vendor")

    def __repr__(self):
        return f'<Vendor {self.name} >'


class Sweet(db.Model, SerializerMixin):  
    __tablename__ = "sweets"

    serialize_rules = ("-vendor_sweets.sweet",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now()) 
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    vendor_sweets= db.relationship('VendorSweet', backref='sweet')
    

class VendorSweet(db.Model, SerializerMixin):
    __tablename__= "vendor_sweets"

    serialize_rules = ("-vendor.vendor_sweets","-sweet.vendor_sweets",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

#relationships
    sweet_id = db.Column(db.Integer, db.ForeignKey("sweets.id"))
    vendor_id = db.Column(db.Integer,db.ForeignKey("vendors.id"))

    def __repr__(self):
        return f'<VendorSweet ({self.id})>'
