# Nama: Hanzel Oclihar Tjiam
# NIM: 221402064

# Soal 1
import datetime as datetime

number = int(input("Enter a number: "))

x = datetime.datetime.now()

calc = x + datetime.timedelta(days = number)

result = calc.strftime("%A, %B %d, %Y")

print(result)