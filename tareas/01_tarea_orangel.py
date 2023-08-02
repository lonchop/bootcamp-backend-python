# Crea un decorador que valide si las entradas de la siguiente función son enteros, si no lo son retornar un TypeError.

def integer_validator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(
                    "Todos los argumentos deben ser numeros enteros")
        print(f"La suma de {args[0]} + {args[1]}")
        return func(*args, **kwargs)

    return wrapper


@integer_validator
def add(a, b):
    return a + b


try:
    result = add(7, 3)
    print(f"es {result}")
except TypeError as error:
    print(f"Error: {error}")
