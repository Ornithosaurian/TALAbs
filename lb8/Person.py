class Person():
    name:str
    city:str
    zip:int

    def __init__(self, name, city, zip):
        self.name = name
        self.city = city
        self.zip = zip

    def __hash__(self):
        sum  = 0

        for b in range(len(self.name)-1):
            sum += ord(self.name[b])

        for b in range(len(self.city)-1):
            sum += ord(self.name[b])

        return sum + self.zip    