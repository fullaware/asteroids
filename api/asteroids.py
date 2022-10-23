from sqlalchemy import or_, func
from flask_sqlalchemy import SQLAlchemy
from api_settings import *

db = SQLAlchemy(app)


# the class AsteroidsModel will inherit the db.Model of SQLAlchemy
class AsteroidsModel(db.Model):
    __tablename__ = 'asteroids'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(80), nullable=False)
    owner = db.Column(db.Integer, nullable=True)
    # nullable is false so the column can't be empty
    sizekg = db.Column(db.BigInteger, nullable=False)
    minedsizekg = db.Column(db.BigInteger, nullable=False)
    diameterkm = db.Column(db.Numeric, nullable=False)
    rotationh = db.Column(db.Numeric, nullable=False)
    spectralgroup = db.Column(db.String(3), nullable=False)
    au = db.Column(db.Numeric, nullable=False)
    hazard = db.Column(db.String(2), nullable=False)


    def json(self):
        return {'id': self.id, 
                'name': self.name,
                'owner': self.owner, 
                'sizekg': self.sizekg,
                'minedsizekg': self.minedsizekg,
                'diameterkm': self.diameterkm,
                'rotationh': self.rotationh, 
                'spectralgroup': self.spectralgroup,
                'au': self.au,
                'hazard': self.hazard}
        # this method we are defining will convert our output to json

    def add_asteroid_json(_json_payload):
        '''function to add asteroid to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our asteroid constructor
        print(f"TESTING _json_payload\n{_json_payload}")

        new_asteroid = AsteroidsModel(   name=_json_payload["name"], 
                                    owner=_json_payload["owner"],
                                    sizekg=_json_payload["sizekg"], 
                                    minedsizekg=_json_payload["minedsizekg"], 
                                    diameterkm=_json_payload["diameterkm"], 
                                    rotationh=_json_payload["rotationh"], 
                                    spectralgroup=_json_payload["spectralgroup"], 
                                    au=_json_payload["au"],
                                    hazard=_json_payload["hazard"])
        db.session.add(new_asteroid)  # add new asteroid to database session
        db.session.commit()  # commit changes to session

    def get_all_asteroids():
        '''function to get all AsteroidsModel in our database'''
        return [AsteroidsModel.json(asteroid) for asteroid in AsteroidsModel.query.all()]
    
    def scanrange_asteroids(_range, _location):
        ''' function to get all Asteroids between 
            min and max _range in au
            _range = 100
            _location = .00200

            Returns all between .00100 - .00300
            '''

        minau = float(_location - (_range/100000))
        maxau = float(_location + (_range/100000))
        print(minau, maxau)
        return [AsteroidsModel.json(asteroid) for asteroid in AsteroidsModel.query.filter(db.and_(AsteroidsModel.au > minau,AsteroidsModel.au < maxau)).all()]

    def get_asteroid(_id):
        '''function to get asteroid using the id of the asteroid as parameter'''
        return [AsteroidsModel.json(AsteroidsModel.query.filter_by(id=_id).first())]
        # AsteroidsModel.json() coverts our output to json
        # the filter_by method filters the query by the id
        # the .first() method displays the first value

    def update_asteroid_json(_id, _json_payload):
        '''function to update the details of a asteroid using the id'''
        asteroid_to_update = AsteroidsModel.query.filter_by(id=_id).first()
        asteroid_to_update.name = _json_payload["name"]
        asteroid_to_update.owner = _json_payload["owner"]
        asteroid_to_update.sizekg = _json_payload["sizekg"]
        asteroid_to_update.minedsizekg = _json_payload["minedsizekg"]
        asteroid_to_update.diameterkm = _json_payload["diameterkm"]
        asteroid_to_update.rotationh = _json_payload["rotationh"]
        asteroid_to_update.spectralgroup = _json_payload["spectralgroup"]
        asteroid_to_update.au = _json_payload["au"]
        asteroid_to_update.hazard = _json_payload["hazard"]
        db.session.commit()


    # def delete_asteroid(_id):
    #     '''function to delete a asteroid from our database using
    #        the id of the asteroid as a parameter'''
    #     print(_id)
    #     AsteroidsModel.query.filter_by(id=_id).delete()
    #     # filter by id and delete
    #     db.session.commit()  # commiting the new change to our database
    
    def search_all_asteroids(_search):
        search = "%{}%".format(_search)

        # return [AsteroidsModel.json(asteroid) for asteroid in AsteroidsModel.query.filter(or_(AsteroidsModel.name.like(search),AsteroidsModel.hazard.like(search))).all()]
        return [AsteroidsModel.json(asteroid) for asteroid in AsteroidsModel.query.filter(AsteroidsModel.name.like(search)).all()]

    def analyze_asteroids():
        '''function to analyze all AsteroidsModel in our database'''
        
        avg_au = db.session.query(func.avg(AsteroidsModel.au)).all()

        avg_au_decimal = [x[0] for x in avg_au]

        # color_count = AsteroidsModel.query.count(AsteroidsModel.rotationh).all()
        spectralgroup_row = db.session.query(AsteroidsModel.spectralgroup, func.count(AsteroidsModel.spectralgroup)).group_by(AsteroidsModel.spectralgroup).order_by(func.count(AsteroidsModel.spectralgroup).desc()).all()

        result2 = []

        for row in spectralgroup_row:
            result2.append({row[0] : row[1]})


        payload = {
            'count' : AsteroidsModel.query.count(),
            'avg_au' : int(avg_au_decimal[0]),
            'spectral_groups' : result2
        }
        
        return payload