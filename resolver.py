import json
from models import Booking, Vehicle

def getBookings(_, info, id):
    booking = Booking.objects(id=id).first()
    if (booking == None):
        raise Exception("Booking not found")
    return booking

def getVehicles(_, info, id):
    vehicle = Vehicle.objects(id=id).first()
    if (vehicle == None):
        raise Exception("Vehicle not found")
    return vehicle
