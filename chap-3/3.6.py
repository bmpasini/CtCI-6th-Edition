# An animal shelter holds only dogs and cats, and operates on a strictly "first in, first out"
# basis. People must adopt either the "oldest" (based on arrival time) of all animals at the
# shelter, or they can select whether they would prefer a dog or a cat (and will receive the
# oldest animal of that type). They cannot select which specific animal they would like. Create
# the data structures to maintain this system and implement operations such as enqueue,
# dequeueAny, dequeueDog and dequeueCat. You may use the built-in LinkedList data structure.

class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue(object):

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            raise Exception("Queue is empty.")
        else:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return data

    def peek(self):
        if self.head is None:
            raise Exception("Queue is empty.")
        else:
            return self.head.data        

    def is_empty(self):
        return self.head is None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            x = self.head
            while x.next:
                x = x.next
            x.next = Node(data)
        self.size += 1

    def remove(self):
        if self.head is None:
            raise Exception("LinkedList is empty.")
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data

    def peek(self):
        if self.head is None:
            raise Exception("LinkedList is empty.")
        else:
            return self.head.data

    def get_size(self):
        return self.size


class Animal(object):

    def __init__(self, species, id=None):
        self.species = species
        self.id = id

    def set_id(self, id):
        self.id = id

    def is_older_than(self, other):
        return self.id < other.id

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self, "Dog")


class Cat(Animal):

    def __init__(self):
        Animal.__init__(self, "Cat")


class AnimalQueue:

    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()
        self.id = 0

    def enqueue(self, animal):
        self.id += 1
        animal.set_id(self.id)
        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)
        else:
            raise Exception("This shelter only accepts dogs and cats.")
            
    def dequeueAny(self):
        if self.dogs.get_size() == 0 and self.cats.get_size() == 0:
            raise Exception("The shelter is empty :(")
        elif self.dogs.get_size() == 0:
            print("You got a happy cat!")
            return self.cats.remove()
        elif self.cats.get_size() == 0:
            print("You got a happy dog!")
            return self.dogs.remove()
        else:
            dog = self.dogs.peek()
            cat = self.cats.peek()
            if dog.is_older_than(cat):
                print("You got a happy dog!")
                return self.dogs.remove()
            else:
                print("You got a happy cat!")
                return self.cats.remove()

    def dequeueCat(self):
        if self.cats.get_size() == 0:
            raise Exception("All of our cats are gone :(")
        else:
            print("You got a happy cat!")
            return self.cats.remove()
    
    def dequeueDog(self):
        if self.dogs.get_size() == 0:
            raise Exception("All of our dogs are gone :(")
        else:
            print("You got a happy dog!")
            return self.dogs.remove()


if __name__ == "__main__":
    a = AnimalQueue()
    a.enqueue(Dog())
    a.enqueue(Cat())
    a.enqueue(Dog())
    a.enqueue(Dog())
    a.enqueue(Dog())
    a.enqueue(Cat())
    a.enqueue(Cat())
    a.enqueue(Dog())
    a.enqueue(Cat())
    a.dequeueAny()
    a.dequeueAny()
    a.dequeueAny()
    a.dequeueAny()
    a.dequeueDog()
    a.dequeueCat()
    a.dequeueAny()
    a.dequeueAny()
    a.dequeueAny()
    a.dequeueAny()
    a.dequeueDog()
    a.dequeueDog()




