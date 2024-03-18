# Nama: Hanzel Oclihar Tjiam
# NIM: 221402064

# Soal 3
class Person:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        bmi = float((self.weight / (self.height)**2))
        return bmi
        
x = Person(65, 1.65)
print(x.BMI_Value())