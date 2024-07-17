from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    fecha_de_subscripcion = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    favoritos = db.relationship('Favoritos', backref='usuario', lazy=True)

    def __repr__(self):
        return '<Usuario %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email
        }

class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_planeta = db.Column(db.String(100), nullable=False)
    periodo_rotacion = db.Column(db.Integer, nullable=False)
    diametro = db.Column(db.Float, nullable=False)
    clima = db.Column(db.String(50), nullable=False)
    terreno = db.Column(db.String(50), nullable=False)
    favoritos = db.relationship('Favoritos', backref='planeta', lazy=True)

    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre_planeta,
            "periodo_rotacion": self.periodo_rotacion,
            "diametro": self.diametro,
            "clima": self.clima,
            "terreno": self.terreno
        }

class Personas(db.Model):
    id_persona = db.Column(db.Integer, primary_key=True)
    nombre_persona = db.Column(db.String(200), nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    color_de_piel = db.Column(db.String(50), nullable=False)
    color_de_pelo = db.Column(db.String(50))
    genero = db.Column(db.String(50))
    birth_year = db.Column(db.Integer, nullable=False)
    favoritos = db.relationship('Favoritos', backref='persona', lazy=True)

    def __repr__(self):
        return '<Personas %r>' % self.id_persona

    def serialize(self):
        return {
            "id_persona": self.id_persona,
            "nombre_persona": self.nombre_persona,
            "peso": self.peso,
            "color_de_piel": self.color_de_piel,
            "color_de_pelo": self.color_de_pelo,
            "genero": self.genero,
            "birth_year": self.birth_year,
        }

class Vehiculos(db.Model):
    id_vehiculos = db.Column(db.Integer, primary_key=True)
    nombre_vehiculos = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(90), nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    tripulacion = db.Column(db.Integer, nullable=False)
    favoritos = db.relationship('Favoritos', backref='vehiculo', lazy=True)

    def __repr__(self):
        return '<Vehiculos %r>' % self.id_vehiculos

    def serialize(self):
        return {
            "id_vehiculos": self.id_vehiculos,
            "nombre_vehiculos": self.nombre_vehiculos,
            "modelo": self.modelo,
            "longitud": self.longitud,
            "tripulacion": self.tripulacion,
        }

class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    planeta_id = db.Column(db.Integer, db.ForeignKey('planetas.id'), nullable=True)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id_vehiculos'), nullable=True)
    nombre_id = db.Column(db.Integer, db.ForeignKey('personas.id_persona'), nullable=True)

    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id,
            "vehiculo_id": self.vehiculo_id,
            "nombre_id": self.nombre_id,
        }