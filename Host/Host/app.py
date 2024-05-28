from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chesse.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Создание объекта SQLAlchemy
db = SQLAlchemy(app)


# Определение модели (таблицы)
class Radio(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer(), default=0)
    quantity = db.Column(db.Integer(), default=0)

    def __repr__(self):
        return f'{self.name} - {self.year} - {self.quantity}'


with app.app_context():
    db.create_all()


@app.route('/add_chesse_product/', methods=['POST'])
def create_chesse_view():
    name = request.get_json()['name']
    year = request.get_json()['year']
    quantity = request.get_json()['quantity']
    product = Radio.query.filter_by(name=name).first()
    Radio.query.filter_by(quantity=quantity).first()
    if product:
        response = make_response(jsonify({'message': 'the database entry already exists'}))
        response.status_code = 400
        return response
    else:
        new_product = Radio(name=name, quantity=quantity, year=year)
        db.session.add(new_product)
        db.session.commit()
        response = make_response(jsonify({'message': 'created'}))
        response.status_code = 201
        return response


@app.route('/add_year/', methods=['POST'])
def add_year_view():
    name = request.get_json()['name']
    year = request.get_json()['year']
    quantity = request.get_json()['quantity']
    product = Radio.query.filter_by(name=name).first()
    Radio.query.filter_by(quantity=quantity).first()
    if product:
        product.year += year
        db.session.commit()
        response = make_response(jsonify({'message': 'success'}))
        response.status_code = 200
        return response
    else:
        response = make_response()
        response.status_code = 404
        return response






@app.route('/radio_get/<int:id>', methods=['GET'])
def detail_radio_view(id):
    product = Radio.query.filter_by(id=id).first()
    if product:
        response = make_response(jsonify({f'{product.name},quantity= {product.quantity}':product.year}))
        response.status_code = 200
        return response
    else:
        response = make_response()
        response.status_code = 404
        return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)