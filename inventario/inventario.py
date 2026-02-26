class Inventario:

    def __init__(self):
        self.productos = {}

    def registrar_producto(self, codigo, nombre, cantidad):
        if codigo in self.productos: # Refactor: Si el código ya existe, no hacemos nada (evitamos duplicados)
            return False
        self.productos[codigo] = {"nombre": nombre, "cantidad": cantidad}
        return True

    def consultar_producto(self, codigo):
        return self.productos.get(codigo) # Refactor: .get() busca el código y si no existe, devuelve None
    
    def actualizar_cantidad(self, codigo, cantidad): 
        if codigo in self.productos: # Refactor: Solo sumamos si el producto existe para evitar errores
            self.productos[codigo]["cantidad"] += cantidad
            return True
        return False
    
    def listar_productos(self):
        return list(self.productos.values())
    
    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            return True
        return False
    