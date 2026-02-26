from inventario.inventario import Inventario

def test_registrar_producto():
    inventario = Inventario()
    inventario.registrar_producto("001", "Shampoo", 25)

    producto = inventario.consultar_producto("001")

    assert producto["nombre"] == "Shampoo"
    assert producto["cantidad"] == 25