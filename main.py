import numpy as np
import pandas as pd


class Animal:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

    def makeSound(self):
        print("I don't know what animal I am!")


class Cat(Animal):
    def makeSound(self):
        print("Meow")

    def makeSound(self):
        print("Purr")


class Dog(Animal):
    def makeSound(self):
        print("Woof")


human = Animal("Skin", 2)
felix = Cat("ginger", 4)
mocha = Dog("Caramel", 4)
mocha.makeSound()
felix.makeSound()
human.makeSound()
