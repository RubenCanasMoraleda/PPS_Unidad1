def isInList(value, list1):
    try:
        if (isinstance(list1, list) or isinstance(list1, str)):
            return value in list1
        else:
            raise RuntimeError("El segundo parámetro introducido no corresponde a una lista")
    except TypeError:
        raise RuntimeError("Estas intentando comparar tipos de datos diferentes")
    
def isInRange(num, min, max):
    try:
        int(num)
        int(min)
        int(max)
        if (min<max):
            return not(num < min or num > max)
        else:
            raise RuntimeError("El mínimo siempre debe ser menor que el máximo")
    except ValueError:
        raise RuntimeError("Todos los valores deben ser números enteros")

try:
    num1 = int(input())
    list1 = "adsadasda"
    print(isInList(num1, list1))
    num2 = input("Introduce un número para ver si se encuentra dentro del rango: ")
    min = input("Introduce el valor mínimo del rango: ")
    max = input("Introduce el valor máximo del rango: ")
    print(isInRange(num2, min, max))
except RuntimeError as e:
    print(e)