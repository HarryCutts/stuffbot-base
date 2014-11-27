from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from thing import Thing, Base

engine = create_engine('sqlite:///stuffbot.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

new_thing = Thing('001', "18L Really Useful Box")
session.add(new_thing)

the_banner = Thing('000', "The banner", parent=new_thing)
session.add(the_banner)

session.commit()
