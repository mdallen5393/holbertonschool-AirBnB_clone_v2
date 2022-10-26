#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel, Base
from models.review import Review
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

# place_amenity = Table('place_amenity', Base.metadata,
#                       Column('place_id',
#                              String(60),
#                              ForeignKey('places.id'),
#                              primary_key=True,
#                              nullable=False),
#                       Column('amenity_id',
#                              String(60),
#                              ForeignKey('amenities_id'),
#                              primary_key=True,
#                              nullable=False))


class Place(BaseModel, Base):
    """
    Database vs File Storage Method for Place
    """
    # if os.getenv('HBNB_TYPE_STORAGE') == 'db':  # db storage
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
    # amenity_ids = []

    if os.getenv('HBTN_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        # amenities = relationship('Amenity', secondary='place_amenity',
        #                          backref='place_amenities', viewonly=False)

    else:
        @property
        def reviews(self):
            """Send reviews to file storage"""
            reviews_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        # @property
        # def amenities(self):
        #     """
        #     Returns list of Amenity instances based on amenity_ids
        #     that contains all Amenity.d linked to the Place
        #     """
        #     from models.amenity import Amenity
        #     all_amenity = models.storage.all(Amenity)
        #     amenities = [obj for obj in all_amenity.values()
        #                  if obj.id == self.amenity_ids]

        # @amenities.setter
        # def amenities(self, obj):
        #     """
        #     Setter for amenities
        #     """
        #     from models.amenity import Amenity
        #     if isinstance(obj, Amenity):
        #         self.append(obj)
