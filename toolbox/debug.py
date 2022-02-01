class Person:
    def __init__(self, name, year_born, city):
        self.name = name
        self.year_born = year_born
        self.city = city

class PersonSlotted:
    __slot__ = 'name', 'year_born', 'city'
    def __init__(self, name, year_born, city):
        self.name = name
        self.year_born = year_born
        self.city = city

from tracemalloc import start, take_snapshot
from sys import getsizeof

print(__file__)
start()

before = take_snapshot()
person = Person('Marek', 1961, 'Krakow')
after = take_snapshot()
print([name for name in dir(before) if not name.startswith('_')])
print(__file__)
for stat in after.compare_to(before, 'lineno'):
    if stat.traceback[0].filename.startswith(__file__):
        print(stat)
print(f'person instance size: {getsizeof(person)}')
print(f"{hasattr(person, '__dict__') = }")


before = take_snapshot()
person = PersonSlotted('Marek', 1961, 'Krakow')
after = take_snapshot()
print([name for name in dir(before) if not name.startswith('_')])

for stat in after.compare_to(before, 'lineno'):
    if stat.traceback[0].filename.startswith(__file__):
        print(stat)
print(f'person on slot instance size: {getsizeof(person)}')

