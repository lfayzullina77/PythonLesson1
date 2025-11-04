from smartphone import Smartphone

catalog = [
  Smartphone("iPhone", "16Pro", "+79161234567"),
  Smartphone("Samsung", "A35", "+79104567890"),
  Smartphone("Xiaomi", "Note9", "+79999999999"),
  Smartphone("Techno", "SPARK 30C", "79011111111"),
  Smartphone("Poco", "M7", "+79035678901")]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} . {smartphone.number}")
