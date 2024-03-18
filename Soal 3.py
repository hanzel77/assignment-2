# Nama: Hanzel Oclihar Tjiam
# NIM: 221402064

# Soal 3
class Person:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def bmi(self):
        BMI_Value = float((self.weight / (self.height)**2))
        return BMI_Value
        
x = Person(65, 1.65)
print(x.bmi())