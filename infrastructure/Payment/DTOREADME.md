# stdlib solutions
dataclasses
added to Python 3.7 (and later backported to Python 3.6)

created using a @dataclass decorator

by default add automatically generated dunder methods __init__, __repr__ and __eq__

__init__ method takes all fields as method parameters and sets their values to instance attributes with the same names:
from dataclasses import dataclass

@dataclass
class ItemDto:
    name: str
    location: Location
    description: str = ""


# support both positional and keyword args
itemdto = ItemDto(
    name="Old Rod",
    location=Location("Vermillion City"),
    description="Fish for low-level Pokemon",
)
generated __repr__ method returns a string containing class name, field names and field representation
>>> print(itemdto)
ItemDto(name='Old Rod', location=Location(name=Vermillion City), description='Fish for low-level Pokemon')
generated __eq__ method compares the class tuples containing field values of the current and the other instance
itemdto2 = ItemDto(
    name="Old Rod",
    location=Location("Vermillion City"),
    description="Fish for low-level Pokemon",
)

>>> itemdto == itemdto2
True
__eq__ method works the same as if we would explicitly declare it this way:
def __eq__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.location, self.description) == (other.name, other.location, other.description)
    return NotImplemented
it might be a good idea to make DTO instances immutable. It is possible by setting the argument frozen to True:
@dataclass(frozen=True)
class ItemDto:
    name: str
    location: Location
    description: str = ""
not iterable:
...: for field in itemdto:
...:     print(field)
...: 
TypeError: 'ItemDto' object is not iterable