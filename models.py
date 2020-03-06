from datetime import datetime
from mongoengine import Document, EmbeddedDocument, ValidationError
from mongoengine.fields import (
    DateTimeField,
    EmbeddedDocumentField,
    ListField,
    ReferenceField,
    StringField,
    BooleanField,
    IntField,
    FloatField
)

class Booking(Document):
    meta = {"collection": "booking"}
    meta = {'db_alias': 'db1'}
    start_time = DateTimeField(default=datetime.utcnow)
    end_time = DateTimeField(default=datetime.utcnow)
    booking_price = FloatField()


def _vehicle_type_validation(val):
    if val not in ["small car", "full-size car", "truck", "luxury car"]:
        raise ValidationError('value can not be empty')

class Vehicle(Document):
    meta = {"collection": "vehicle"}
    meta = {'db_alias': 'db1'}
    type = StringField(validation=_vehicle_type_validation)
    default_hourly_rate = FloatField()
    make = StringField()
    model = StringField()
    year = IntField()
    registration_tag = StringField()
    current_mileage = FloatField()
    condition = StringField()
    capacity = IntField()
    last_service_time = DateTimeField(default=datetime.utcnow)
    is_available = BooleanField()
    booking = ListField(ReferenceField(Booking))