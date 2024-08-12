"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User ,Planetas, Personas, Vehiculos , Favoritos

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    users = User.query.all()
    users_serialized = list(map(lambda item:item.serialize(), users))
    print(users_serialized)


    response_body = {
        "msg": "Ok",
        "data": users_serialized
    
    }
    return jsonify(response_body), 200

@app.route('/user/<int:id>', methods=['GET'])
def get_people_by_id(id):
    user = User.query.filter_by(id=id).first()
    user_serialize = user.serialize()

    response_body = {
        "msg": "Ok",
        "data": user_serialize
    }

    return jsonify(response_body), 200


@app.route('/user', methods=['POST'])
def create_user():
    body = request.json
    me = User(email=body["email"], password=body["password"], is_active=body["is_active"])
    db.session.add(me)
    db.session.commit()

    response_body = {
        "msg": "Ok",
        "id": me.id
    }

    return jsonify(response_body), 200

@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user=User.query.get(user_id)

    if not user:
        return jsonify({"msj":"usuario no encontrado"}), 404
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({"msj":"usuario eliminado"}), 200



@app.route('/planetas', methods=['GET'])
def handle_planetas():

    planetas = Planetas.query.all()
    planetas_serialized = list(map(lambda item:item.serialize(), planetas))
    print(planetas_serialized)


    response_body = {
        "msg": "ok",
        "data": planetas_serialized
    
    }
    return jsonify(response_body), 200


@app.route('/planetas/<int:id>', methods=['GET'])
def get_planetas_by_id(id):
    planetas = Planetas.query.filter_by(id=id).first()
    planetas_serialize = planetas.serialize()

    response_body = {
        "msg": "Ok",
        "data": planetas_serialize
    }

    return jsonify(response_body), 200


@app.route('/planetas', methods=['POST'])
def create_planetas():
    body = request.json
    me = Planetas(nombre_planeta=body["nombre_planeta"], periodo_rotacion=body["periodo_rotacion"], diametro=body["diametro"], clima=body["clima"], terreno=body ["terreno"],)
    db.session.add(me)
    db.session.commit()

    response_body = {
        "msg": "Ok",
        "id": me.id
    }

    return jsonify(response_body), 200

@app.route("/planetas/<int:planetas_id>", methods=["DELETE"])
def delete_planetas(planetas_id):
    planetas=Planetas.query.get(planetas_id)

    if not planetas:
        return jsonify({"msj":"planeta no encontrado"}), 404
    
    db.session.delete(planetas)
    db.session.commit()

    return jsonify({"msj":"planeta eliminado"}), 200



@app.route('/personas', methods=['GET'])
def handle_personas():

    personas = Personas.query.all()
    personas_serialized = list(map(lambda item:item.serialize(), personas))
    print(personas_serialized)


    response_body = {
        "msg": "ok",
        "data": personas_serialized
    
    }
    return jsonify(response_body), 200


@app.route('/personas/<int:id>', methods=['GET'])
def get_personas_by_id(id):
    personas = Personas.query.filter_by(id_persona=id).first()
    personas_serialize = personas.serialize()

    response_body = {
        "msg": "Ok",
        "data": personas_serialize
    }

    return jsonify(response_body), 200


@app.route('/personas', methods=['POST'])
def create_personas():
    body = request.json
    me = Personas(nombre_persona=body["nombre_persona"], peso=body["peso"], color_de_piel=body["color_de_piel"], color_de_pelo=body["color_de_pelo"], genero=body ["genero"], birth_year=body ["birth_year"])
    db.session.add(me)
    db.session.commit()

    response_body = {
        "msg": "Ok",
        "id": me.id
    }

    return jsonify(response_body), 200

@app.route("/personas/<int:personas_id>", methods=["DELETE"])
def delete_personas(personas_id):
    personas=Personas.query.get(personas_id)

    if not personas:
        return jsonify({"msj":"persona no encontrado"}), 404
    
    db.session.delete(personas)
    db.session.commit()

    return jsonify({"msj":"persona eliminado"}), 200




@app.route('/vehiculos', methods=['GET'])
def handle_vehiculos():

    vehiculos = Vehiculos.query.all()
    vehiculos_serialized = list(map(lambda item:item.serialize(), vehiculos))
    print(vehiculos_serialized)


    response_body = {
        "msg": "ok",
        "data": vehiculos_serialized
    
    }
    return jsonify(response_body), 200


@app.route('/vehiculos/<int:id>', methods=['GET'])
def get_vehiculos_by_id(id):
    vehiculos = Vehiculos.query.filter_by(id_vehiculos=id).first()
    vehiculos_serialize = vehiculos.serialize()

    response_body = {
        "msg": "Ok",
        "data": vehiculos_serialize
    }

    return jsonify(response_body), 200



@app.route('/vehiculos', methods=['POST'])
def create_vehiculos():
    body = request.json
    me = Vehiculos(nombre_vehiculos=body["nombre_vehiculos"], modelo=body["modelo"], longitud=body["longitud"], tripulacion=body["tripulacion"])
    db.session.add(me)
    db.session.commit()

    response_body = {
        "msg": "Ok",
        "id": me.id
    }

    return jsonify(response_body), 200

@app.route("/vehiculos/<int:vehiculos_id>", methods=["DELETE"])
def delete_vehiculos(vehiculos_id):
    vehiculos=Vehiculos.query.get(vehiculos_id)

    if not vehiculos:
        return jsonify({"msj":"vehiculo no encontrado"}), 404
    
    db.session.delete(vehiculos)
    db.session.commit()

    return jsonify({"msj":"vehiculo eliminado"}), 200



@app.route('/favoritos', methods=['GET'])
def handle_favoritos():

    favoritos = Favoritos.query.all()
    favoritos_serialized = list(map(lambda item:item.serialize(), favoritos))
    print(favoritos_serialized)


    response_body = {
        "msg": "ok",
        "data": favoritos_serialized
    
    }
    return jsonify(response_body), 200


@app.route('/favoritos/<int:id>', methods=['GET'])
def get_favoritos_by_id(id):
    favoritos = Favoritos.query.filter_by(id=id).first()
    favoritos_serialize = favoritos.serialize()

    response_body = {
        "msg": "Ok",
        "data": favoritos_serialize
    }

    return jsonify(response_body), 200


@app.route('/favoritos', methods=['POST'])
def create_favoritos():
    body = request.json
    me = Favoritos(usuario_id=body["usuario_id"], planeta_id=body["planeta_id"], vehiculo_id=body["vehiculo_id"], nombre_id=body["nombre_id"])
    db.session.add(me)
    db.session.commit()

    response_body = {
        "msg": "Ok",
        "id": me.id
    }

    return jsonify(response_body), 200

@app.route("/favoritos/<int:favoritos_id>", methods=["DELETE"])
def delete_favoritos(favoritos_id):
    favoritos=Favoritos.query.get(favoritos_id)

    if not favoritos:
        return jsonify({"msj":"favortio no encontrado"}), 404
    
    db.session.delete(favoritos)
    db.session.commit()

    return jsonify({"msj":"usuario eliminado"}), 200





# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
