from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int = 12
    species: str = "Homo sapiens"


# Пример использования:
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(p1.species)  # Homo sapiens
print(p2.species)  # Homo sapiens
