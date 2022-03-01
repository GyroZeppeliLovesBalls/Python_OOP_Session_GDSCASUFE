class Person:
    def __init__(self, name, age, location, faculty):
        self.Name = name
        self.Age = age
        self.Location = location
        self.Faculty = faculty

    def wakeUp(self):
        print("Hello World!")


Waseem = Person("Waseem Faheem", 20, "Shoubra", "ASUFE")
Waseem.wakeUp()
print(Waseem.Age)
