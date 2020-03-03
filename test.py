from mongoengine import connect, disconnect, Document, EmbeddedDocument, ValidationError
from mongoengine.fields import StringField, FloatField, DateTimeField, IntField, BooleanField, EmbeddedDocumentField, ListField
import datetime

connect(host='mongodb://localhost/mongoengine_test', alias='db1')

class Booking1(EmbeddedDocument):
    start_time = DateTimeField(default=datetime.datetime.utcnow)
    end_time = DateTimeField(default=datetime.datetime.utcnow)
    booking_price = FloatField()

def _vehicle_type_validation(val):
    if val not in ["small car", "full-size car", "truck", "luxury car"]:
        raise ValidationError('value can not be empty')

class Vehicle1(Document):
    type = StringField(validation=_vehicle_type_validation)
    default_hourly_rate = FloatField()
    make = StringField()
    model = StringField()
    year = IntField()
    registration_tag = StringField()
    current_mileage = FloatField()
    condition = StringField()
    capacity = IntField()
    last_service_time = DateTimeField(default=datetime.datetime.utcnow)
    is_available = BooleanField()
    booking = ListField(EmbeddedDocumentField(Booking1))
    meta = {'db_alias': 'db1'}



booking1 = Booking1(booking_price=66.6, start_time=datetime.datetime(2020, 3, 1, 0, 0 ,0), end_time=datetime.datetime(2020, 3, 4, 0, 0 ,0))
vehicle1 = Vehicle1(type="small car", make="Honda", model="Civic R", year=2020, registration_tag="A12345", current_mileage=123.12, condition="like new", capacity=4, is_available=True, booking=[booking1])
vehicle1.save()

disconnect(alias='db1')