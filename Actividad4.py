class Geometria:
    def area(self, ancho, alto=None):
        """Calcula el área de una figura. Si solo se da un lado, calcula el área de un cuadrado."""
        if alto is None:
            alto = ancho  # Si solo se proporciona un lado, se asume que es un cuadrado.
        return ancho * alto

    def perimetro(self, ancho, alto=None):
        """Calcula el perímetro de una figura. Si solo se da un lado, calcula el perímetro de un cuadrado."""
        if alto is None:
            alto = ancho  # Si solo se proporciona un lado, se asume que es un cuadrado.
        return 2 * (ancho + alto)

# Crear una instancia de la clase Geometria
geometria = Geometria()

# Pedir al usuario que ingrese el ancho y opcionalmente el alto
ancho = float(input("Introduce el ancho: "))
alto = input("Introduce el alto (presiona Enter si es un cuadrado): ")

# Verificar si el alto ha sido introducido o no
if alto == '':
    alto = None
else:
    alto = float(alto)

# Mostrar los resultados
print("Área:", geometria.area(ancho, alto))  # Calcular el área
print("Perímetro:", geometria.perimetro(ancho, alto))  # Calcular el perímetro
