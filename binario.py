def esBinario(arg):
    try:
        intArg = int(arg, 2)
        return intArg
    except ValueError:
        raise RuntimeError("No has introducido un número binario")

arg = input("Introduce un número binario: ")
try:
    print(f"El número binario {arg} en decimal es {esBinario(arg)}")
except RuntimeError as e:
    print(e)