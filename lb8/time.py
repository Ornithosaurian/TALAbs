import random
import names
import sys
import time
import time
from Person import Person as man
from main import add, search

start_time = time.time()

start_time = time.time()
sys.setrecursionlimit(1000000000)
name = names.get_first_name()
city_list = ["kyiv", "odesa", "kharkiv", "lviv", "dnipro"]
city = random.choice(city_list)
zip = random.randint(0, 200000)
Person2 = man(name, city, zip)

with open('file.txt', 'w') as f:
    people = [man(name, city, zip) for i in range(200000)]
    for i in range(200000):
        f.write(str(people[i]) + "\n")
        #add(people[i])
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
for i in range(1000):
    search(people[i])
print("--- %s seconds ---" % (time.time() - start_time))
