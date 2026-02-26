from inventario.inventario import Inventario

def test_registrar_producto():
    inventario = Inventario()
    inventario.registrar_producto("001", "Shampoo", 25)

    producto = inventario.consultar_producto("001")

    assert producto["nombre"] == "Shampoo"
    assert producto["cantidad"] == 25

def test_actualizar_cantidad():
    inventario = Inventario()
    inventario.registrar_producto("001", "Shampoo", 10)

    inventario.actualizar_cantidad("001", 5)

    producto = inventario.consultar_producto("001")

    assert producto["cantidad"] == 15

def test_listar_productos():
    inventario = Inventario()
    inventario.registrar_producto("001", "Shampoo", 10)
    inventario.registrar_producto("002", "Jabon", 5)

    lista = inventario.listar_productos()

    assert len(lista) == 2

def test_eliminar_producto():
    inventario = Inventario()
    inventario.registrar_producto("004", "Teclado", 10)
    inventario.eliminar_producto("004")

    lista = inventario.listar_productos()

    assert len(lista) == 0

def test_consultar_producto_inexistente():
    inventario = Inventario()
    resultado = inventario.consultar_producto("999")
    
    assert resultado is None