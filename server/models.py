from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from flask import Flask

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)
app = Flask(__name__)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String)
    magnitude = db.Column(db.Float)
    year = db.Column(db.Integer)

def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"


if __name__ == '__main__':
    app.run(port=5555, debug=True)