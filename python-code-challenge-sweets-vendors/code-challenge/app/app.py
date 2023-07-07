#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Vendor, Sweet, VendorSweet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

@app.route('/')
def home():
    return 'THE CANDY SHOP'

class VendorResource(Resource):
    def get(self):

        vendor = Vendor.query.all()
        vend_list = [item.to_dict() for item in vendor]
        return make_response(jsonify(vend_list), 200)
    
   
api.add_resource(VendorResource, "/vendor")


class VendorResourceID(Resource):
    def get(self, id):

       vendor = Vendor.query.filter_by(id=id).first()

       return make_response(jsonify(vendor), 200) 
       
    
api.add_resource(VendorResourceID, "/vendor/<int:id>")

class SweetResource(Resource):
    def get (self):

        sweet = Sweet.query.all()

        sweet_list = [item.to_dict() for item in sweet]

        return make_response(jsonify(sweet_list), 200)

api.add_resource(SweetResource, "/sweet")

class SweetResourceById(Resource):
    def get (self, id):

        sweet = Sweet.query.filter_by(id = id).first()

        return make_response(jsonify(sweet), 200)

api.add_resource(SweetResourceById, "/sweet/<int:id>")


class VendorSweetResource(Resource):
    def post(self):

        new_vendorsweet = VendorSweet(
            price = vendorsweet["price"],
            vendor_id = vendorsweet["vendor_id"],
            sweet_id = vendorsweet['sweet_id']
        )

        db.session.add(new_vendorsweet)
        db.session.commit()

        vendorsweet = new_vendorsweet.to_dict()

        return make_response(jsonify(vendorsweet), 201)


    def delete(self, id):
        record = (Vendor.query.filter_by(id=id)).first()

        db.session.delete(record)
        db.session.commit()
        
        response = {
            "message":"message is deleted"
        }


        return make_response(jsonify(response), 200)

        
api.add_resource(VendorSweetResource, "/vendor_sweet/<int:id>")

if __name__ == '__main__':
    app.run(port=5555)
