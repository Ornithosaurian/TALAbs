class Person():
    name: str
    city: str
    zip: int

    def __init__(self, name, city, zip):
        self.name = name
        self.city = city
        self.zip = zip

    @property
    def flet(self):
        return ord(self.city[0]) - 97

    def __hash__(self):
        sum = 0

        for b in self.name:
            sum = 102 * sum + ord(b) + self.zip * 47
        for b in self.city:
            sum = 143 * sum + ord(b) - self.zip * 14

        return sum


