class Animal:
    def __init__(self, name: str, race: str, age: int, weight: int):
        self.name = name
        self.race = race
        self.age = age
        self.weight = weight

    def eat(self):
        print(f"{self.name} está comiendo")

    def walk(self):
        print(f"{self.name} está caminando")
    
    def sleep(self):
        print(f"{self.name} está durmiendo")

    def __str__(self):
        return f"Nombre: {self.name}, raza: {self.race}, edad: {self.age}, weight: {self.weight}"

dog = Animal("Brando", "San Bernardo", 3, 30)
cat = Animal("Roll", "Persa", 4, 3)
print(dog, cat, sep="\n")
