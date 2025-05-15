# Class initialisation with default __init__
class Pet:
    def speak(self):
        print("sound made")
        # return ("pet spoke")

Rasmus = Pet()
Rasmus.name = "Rasmus"
print(Rasmus.name)
print(Rasmus.speak())        


# A simple class to represent a dog modified __init__    
class Dog:
    def __init__(self,name,breed,age="N/A"):
        self.name = name
        self.breed = breed
        self.age = age
    def speak(self):
        return f"1  "        
    

class Cat:
    pass

class Rat:
    pass        