from domain.pago import Pago

class PagoService:
    def __init__(self):
        self.pagos = []

    def crear(self, pago: Pago):
        self.pagos.append(pago)
        return pago

    def listar(self):
        return self.pagos

    def obtener(self, id: int):
        for p in self.pagos:
            if p.id == id:
                return p
        return None

    def actualizar(self, id: int, pago: Pago):
        for i, p in enumerate(self.pagos):
            if p.id == id:
                self.pagos[i] = pago
                return pago
        return None

    def eliminar(self, id: int):
        for p in self.pagos:
            if p.id == id:
                self.pagos.remove(p)
                return True
        return False