#!/usr/bin/python3
"""
Database Storage Engine Module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    Database Storage Class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiate the DBStorage class
        """
        # Get environmental variables
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        # drop all tables if env is test
        if env == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """
        Query current database session for all objects of class
        """

        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}

        if cls in classes:
            class_dict = {}
            if isinstance(cls, str):
                cls = classes[cls]
            all_objects = self.__session.query(cls).all()
            for obj in all_objects:
                class_dict[f'{obj.id}'] = obj
            return(class_dict)

        else:
            all_dict = {}

            all_list = []
            all_list.append(self.all(User))
            all_list.append(self.all(Place))
            all_list.append(self.all(State))
            all_list.append(self.all(City))
            all_list.append(self.all(Amenity))
            all_list.append(self.all(Review))

            for list_item in all_list:
                all_dict.update(list_item)

            return(all_dict)

    def new(self, obj):
        """
        Adds the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Saves the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete object from current database if obj is not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database
        Create current database session
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """
        End attributes
        """
        self.__session.remove()
