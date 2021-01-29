class animal:
    def __init__(self, name, typeOfAnimal):
        self.name = name
        self.typeOfAnimal = typeOfAnimal
    def sayName(self):
        print(self.name)
    def sayType(self):
        print(self.typeOfAnimal)
    def describeAnimal(self):
        self.sayType()
        self.sayName()

class fox(animal):
    def __init__(self, name):
        super().__init__(name, "fox")
    def sayType(self):
        print("fox")
    def bark(self):
        print("bark bark")

def main():
    a1 = animal("craig", "cat")
    a1.sayName()
    a1.sayType()
    a1.describeAnimal()

    foxInstance = fox("peppy")
    foxInstance.sayType()
    foxInstance.bark()
    
if __name__ == "__main__":
    main()
