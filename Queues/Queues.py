from collections import deque

class Animal:
    def __init__(self,animal_type, order):
        self.type = animal_type
        self.order = order

class AnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 1

    def enqueue(self, animal_type):
        if animal_type == "dog":
            self.dogs.append(Animal("dog", self.order))
            self.order += 1
        elif animal_type == "cat":
            self.cats.append(Animal("cat", self.order))
            self.order += 1
        else:
            print("Invalid animal type!")
        
    def dequeue_any(self):
        if not self.dogs and not self.cats:
            raise RuntimeError("No available for adoption.")
        if not self.dogs:
            return self.dequeue_cat()
        elif not self.cats:
            return self.dequeue_dog()
        
        if self.dogs[0].order < self.cats[0].order:
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()
        
    def dequeue_dog(self):
        if not self.dogs:
            raise RuntimeError("No dogs available for adoption.")
        return self.dogs.popleft()
    
    def dequeue_cat(self):
        if not self.cats:
            raise RuntimeError("No cats available for adoption.")
        return self.cats.popleft()
    