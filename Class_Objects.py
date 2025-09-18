class Student():
    def __init__(self, Name, Age):  # Fixed: __init__ with double underscores
        self.name = Name            # Fixed: self with lowercase 's'
        self.age = Age
    
    def introduce(self):
        print(f"My Name is {self.name} and I am {self.age} years old")