from games.mario_saving_the_princess import MarioSavingThePrincess
from datetime import datetime
from models.utilities.utilities import DateTimeEncoder
from db import db
import json


class MarioSavingThePrincessModel(MarioSavingThePrincess, db.Model):
    """
    Definition of database tables and convinient saving method to use with SQLAlchemy
    """

    __tablename__ = 'mario_results'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True))
    size = db.Column(db.Integer)
    # grid = db.Column(db.String(120))
    grid = db.Column(db.JSON)

    def __init__(self, size, grid):
        super().__init__(size, grid)
        self.size = size
        self.grid = grid
        self.date_created = datetime.utcnow()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        """
        Method for serialization of response data.

        Another way of serialization  datetime object would be to just convert to string (str(datetime.utcnow()))
        and then deserialize with this: datetime.datetime.strptime(sDate, '%Y-%m-%d %H:%M:%S.%f')

        :return: Return serialized data of date_created, size and grid values.
        """
        return {'date_created': json.dumps(self.date_created, cls=DateTimeEncoder), 'N': self.size, 'Grid': self.grid}
