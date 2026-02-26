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
    
    def actualizar_cantidad(self, codigo, cantidad):
        self.productos[codigo]["cantidad"] += cantidad
    
    def listar_productos(self):
        return list(self.productos.values())