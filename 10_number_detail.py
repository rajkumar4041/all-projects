import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("enter your number with +__: ")
time=timezone.time_zone_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)