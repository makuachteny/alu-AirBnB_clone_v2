#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value(city_id="fsdfk34-4543-234-4543")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value(user_id="fsdfk34-4543-234-4543")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value(name="kigali")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value(description="wow")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value(number_rooms=2)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value(number_bathrooms=2)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value(max_guest=4)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value(price_by_night=200)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value(latitude=0.9)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value(latitude=2.4)
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value(amenity_ids=[])
        self.assertEqual(type(new.amenity_ids), list)