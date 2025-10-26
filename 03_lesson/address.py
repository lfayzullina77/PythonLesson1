class Address:
    def __init__(self, postalcod, city, street, house, apartment):
        self.postalcod = postalcod
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return f"{self.postalcod}, {self.city}, {self.street}, \
{self.house}-{self.apartment}"
