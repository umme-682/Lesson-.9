class Dog:
    species = "dog"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
fluffy = Dog("Fluffy", 3)
coco = Dog("Cocc", 4)

print("Fluffy is a {}".format(fluffy.species))
print("Coco is also a {}".format(coco.species))

print("{} is {} years old".format(fluffy.name, fluffy.age))
print("{} is {} years old".format(coco.name, coco.age))