from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Thing(Base):
    __tablename__ = 'Thing'

    code = Column(String, primary_key=True)
    name = Column(String)
    parent_code = Column(String, ForeignKey('Thing.code'))
    parent = relationship('Thing', uselist=False)

    def __init__(self, code, name, parent=None):
        self.code = code
        self.name = name
        if parent is not None:
            self.parent = parent  # TODO: work out one-to-one relationships

    def move_to(self, new_parent):
        self.parent = new_parent
