from flask import Flask
from flask_restful import Api
from resources.product import Product, ProductList
from models.product import ProductModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'sdflkdnldcndcldcndkccnk'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()



api.add_resource(Product, '/product/<string:name>')
api.add_resource(ProductList, '/products')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)