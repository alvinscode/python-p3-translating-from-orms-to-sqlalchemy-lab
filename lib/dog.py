from models import Dog
from sqlalchemy import create_engine


def create_table(Base, engine):
    engine = create_engine('sqlite:///lib/dogs.db')
    Base.metadata.create_all(engine)
    
def save(session, dog):
    session.add(dog)
    session.commit()
    session.close()

def get_all(session):
    dogs = session.query(Dog).all()
    session.close()
    return dogs

def find_by_name(session, name):
    dog = session.query(Dog).filter_by(name=name).first()
    session.close()
    return dog

def find_by_id(session, id):
    dog = session.query(Dog).get(id)
    session.close()
    return dog

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter_by(name=name, breed=breed).first()
    session.close()
    return dog

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    session.close()