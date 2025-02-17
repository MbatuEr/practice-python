from collections import deque
from enum import Enum
from dataclasses import dataclass

class AnimalType(Enum):
    DOG = "dog"
    CAT = "cat"

@dataclass
class Animal:
    animal_type: AnimalType
    order: int

class AnimalShelter:
    def __init__(self):
        self.dogs: deque[Animal] = deque()
        self.cats: deque[Animal] = deque()
        self.order: int = 1

    def enqueue(self, animal_type: str) -> None:
        try:
            animal_enum = AnimalType(animal_type.lower())
        except ValueError:
            raise ValueError(f"Invalid animal type: {animal_type}. Allowed types: {', '.join(t.value for t in AnimalType)}")

        animal = Animal(animal_enum, self.order)
        self.order += 1

        if animal_enum == AnimalType.DOG:
            self.dogs.append(animal)
        else:
            self.cats.append(animal)

    def dequeue_any(self) -> Animal:
        if not self.dogs and not self.cats:
            raise RuntimeError("No animals available for adoption.")

        if not self.dogs:
            return self._dequeue(self.cats, "No cats available for adoption.")
        if not self.cats:
            return self._dequeue(self.dogs, "No dogs available for adoption.")

        return self.dequeue_dog() if self.dogs[0].order < self.cats[0].order else self.dequeue_cat()

    def dequeue_dog(self) -> Animal:
        return self._dequeue(self.dogs, "No dogs available for adoption.")

    def dequeue_cat(self) -> Animal:
        return self._dequeue(self.cats, "No cats available for adoption.")

    def _dequeue(self, queue: deque[Animal], error_message: str) -> Animal:
        if not queue:
            raise RuntimeError(error_message)
        return queue.popleft()

