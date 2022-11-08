#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel, Base
from models.review import Review
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """
    Database vs File Storage Method for Place
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBTN_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity',
                                 secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """Send reviews to file storage"""
            reviews_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """ getter for amenity table
            """
            from models import storage
            from models.amenity import Amenity
            amenity_list = []
            amenity_dict = storage.all(Amenity)

            for amenity_inst in amenity_dict.values():
                if amenity_inst.id == self.amenity_id:
                    amenity_list.append(amenity_inst)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity_list):
            """Setter for amenities"""
            from models.amenity import Amenity
            for amenity_inst in amenity_list:
                if type(amenity_inst) == Amenity:
                    self.amenity_ids.append(amenity_inst)
