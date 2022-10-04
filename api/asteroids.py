from sqlalchemy import or_, func
from flask_sqlalchemy import SQLAlchemy
from api_settings import *

db = SQLAlchemy(app)


# the class Asteroids will inherit the db.Model of SQLAlchemy
class Asteroids(db.Model):
    __tablename__ = 'asteroids'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    sizekg = db.Column(db.BigInteger, nullable=False)
    hazard = db.Column(db.String(2), nullable=False)
    diameterkm = db.Column(db.Numeric, nullable=False)
    rotationh = db.Column(db.Numeric, nullable=False)
    spectraltype = db.Column(db.String(3), nullable=False)
    au = db.Column(db.Numeric, nullable=False)


    def json(self):
        return {'id': self.id, 'name': self.name, 'sizekg': self.sizekg,
                'hazard': self.hazard, 'diameterkm': self.diameterkm,
                'rotationh': self.rotationh, 'spectraltype': self.spectraltype,
                'au': self.au}
        # this method we are defining will convert our output to json

    def add_asteroid(_name, _sizekg, _hazard, _diameterkm, _rotationh, _spectraltype, _au):
        '''function to add asteroid to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our asteroid constructor
        new_asteroid = Asteroids(name=_name, sizekg=_sizekg, hazard=_hazard, diameterkm=_diameterkm, rotationh=_rotationh, spectraltype=_spectraltype, au=_au)
        db.session.add(new_asteroid)  # add new asteroid to database session
        db.session.commit()  # commit changes to session

    def get_all_asteroids():
        '''function to get all Asteroids in our database'''
        return [Asteroids.json(asteroid) for asteroid in Asteroids.query.filter(db.and_(Asteroids.au > .00200,Asteroids.au < .00330)).all()]

    def get_asteroid(_id):
        '''function to get asteroid using the id of the asteroid as parameter'''
        return [Asteroids.json(Asteroids.query.filter_by(id=_id).first())]
        # Asteroids.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_asteroid(_id, _name, _sizekg, _hazard, _diameterkm, _rotationh, _spectraltype, _au):
        '''function to update the details of a asteroid using the id'''
        asteroid_to_update = Asteroids.query.filter_by(id=_id).first()
        asteroid_to_update.name = _name
        asteroid_to_update.sizekg = _sizekg
        asteroid_to_update.hazard = _hazard
        asteroid_to_update.diameterkm = _diameterkm
        asteroid_to_update.rotationh = _rotationh
        asteroid_to_update.spectraltype = _spectraltype
        asteroid_to_update.au = _au
        db.session.commit()

    # def delete_asteroid(_id):
    #     '''function to delete a asteroid from our database using
    #        the id of the asteroid as a parameter'''
    #     print(_id)
    #     Asteroids.query.filter_by(id=_id).delete()
    #     # filter by id and delete
    #     db.session.commit()  # commiting the new change to our database
    
    def search_all_asteroids(_search):
        search = "%{}%".format(_search)

        # return [Asteroids.json(asteroid) for asteroid in Asteroids.query.filter(or_(Asteroids.name.like(search),Asteroids.hazard.like(search))).all()]
        return [Asteroids.json(asteroid) for asteroid in Asteroids.query.filter(Asteroids.name.like(search)).all()]

    def analyze_asteroids():
        '''function to analyze all Asteroids in our database'''
        
        avg_hp_row = db.session.query(func.avg(Asteroids.spectraltype)).all()

        avg_hp_decimal = [x[0] for x in avg_hp_row]

        # color_count = Asteroids.query.count(Asteroids.rotationh).all()
        color_count_row = db.session.query(Asteroids.spectraltype, func.count(Asteroids.spectraltype)).group_by(Asteroids.spectraltype).order_by(func.count(Asteroids.spectraltype).desc()).all()

        color_count_dict = {}

        for row in color_count_row:
            color_count_dict[row[0]] = row[1]


        payload = {
            'count' : Asteroids.query.count(),
            'avg_hp' : int(avg_hp_decimal[0]),
            'color_count' : color_count_dict
        }
        
        return payload