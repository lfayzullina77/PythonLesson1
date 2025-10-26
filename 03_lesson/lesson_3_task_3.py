from address import Address
from mailing import Mailing


to_address = Address(141002, "Мытищи", "Матросова", 4, 28)
from_address = Address(141014, "Мытищи", "Семашко", 32, 180)
track = ("Отправление")
cost = (2856)

mailing = Mailing(to_address, from_address, cost, track)

print(mailing)
