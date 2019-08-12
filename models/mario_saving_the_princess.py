from games.mario_saving_the_princess import MarioSavingThePrincess
from datetime import datetime
from utilities.utilities import DateTimeEncoder
from db import db
import json


class MarioSavingThePrincessModel(MarioSavingThePrincess, db.Model):
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
        self.date = datetime.utcnow()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'date': json.dumps(self.date_created, cls=DateTimeEncoder), 'size': self.size, 'grid': self.grid}
