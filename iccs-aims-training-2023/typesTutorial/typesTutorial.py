
def greeting(name : str) -> None:
  print ("Hello " + name)

# Here are problems
greeting("AIMS Rwanda")
# greeting(1)

# Example with signatures
flag : bool = True

def plus(x : int, y : int) -> int:
   return x + y

def greet_all(names: list[str]) -> None:
    names2 = names + names # note no need for a type signature
    for name in names2:
        print('Hello ' + name)

names = ["Alice", "Brijesh", "Chenxi"]
# reveal_type(names) # Uncomment and ask mypy what the type is.

greet_all(names)   # Ok!

from typing import Iterable

def greet_all_again(names: Iterable[str]) -> None:
    for name in names:
        print('Jambo ' + name)

greet_all_again(names)   # Ok!
greet_all_again(("Dave", "Ali", "Medhi"))

# # Some more examples

some_data : tuple[int, bool, str] = (42, True, "Kigali")

x: dict[str, float] = {"field1": 2.0, "field2": 3.0}

# #from typing import TypeVar, Generic, reveal_type
# # T = TypeVar('T')
