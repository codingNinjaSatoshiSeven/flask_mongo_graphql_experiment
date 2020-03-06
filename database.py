from mongoengine import connect
from datetime import datetime

from models import Vehicle, Booking

connect(host='mongodb://mongo:27017/mongoengine_ariadne_test', alias='db1')


def init_db():
    booking1 = Booking(
        booking_price=66.6,
        start_time=datetime(2020, 3, 1, 0, 0 ,0),
        end_time=datetime(2020, 3, 4, 0, 0 ,0)
    )
    booking1.save()

    booking2 = Booking(
        booking_price=55.5,
        start_time=datetime(2020, 3, 5, 0, 0 ,0),
        end_time=datetime(2020, 3, 7, 0, 0 ,0)
    )
    booking2.save()

    vehicle1 = Vehicle(
        type="small car",
        make="Honda",
        model="Civic R",
        year=2020,
        registration_tag="A12345",
        current_mileage=123.12,
        condition="like new",
        capacity=4,
        is_available=True,
        booking=[booking1, booking2]
    )
    vehicle1.save()