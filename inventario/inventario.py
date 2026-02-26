class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, codigo, nombre, cantidad):
        self.productos[codigo] = {
            "nombre": nombre,
            "cantidad": cantidad
        }

    def consultar_producto(self, codigo):
        return self.productos[codigo]