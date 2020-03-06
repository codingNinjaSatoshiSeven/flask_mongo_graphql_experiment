import json
from datetime import datetime
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

def addBooking(_, info, vehicle_id, booking_price, start_time, end_time):
    newbooking = Booking(
        booking_price=booking_price,
        start_time=datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S'),
        end_time=datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    )
    newbooking.save()
    vehicle = Vehicle.objects(id=vehicle_id).first()
    vehicle.booking.append(newbooking)
    vehicle.save()
    return vehicle
