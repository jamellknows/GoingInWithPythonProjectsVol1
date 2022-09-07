import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def phonetracer():
    number = input("Enter your No.: with the area code\n")
    phone=phonenumbers.parse(number)
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone,"en")
    reg=geocoder.description_for_number(phone,"en")
    print("For the phone: "+ str(phone) + "\n")
    print("The time is: " + str(time) +"\n")
    print("The carrier is: " + str(car) + "\n")
    print("The region is: " + str(reg) + "\n")
