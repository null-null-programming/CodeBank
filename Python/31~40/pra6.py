try:
    print(a)
except NameError:
    print("NameError!")

try:
    a + 1
except (NameError, TypeError):
    print("Error!")

a = 2

try:
    a + 1
except:
    print("Error")
else:
    print(a)
finally:
    print("end")