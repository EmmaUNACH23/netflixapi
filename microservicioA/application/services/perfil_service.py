from domain.perfil import Perfil

class PerfilService:
    def __init__(self):
        self.perfiles = []

    def crear(self, perfil: Perfil):
        self.perfiles.append(perfil)
        return perfil

    def listar(self):
        return self.perfiles

    def obtener(self, id: int):
        for p in self.perfiles:
            if p.id == id:
                return p
        return None

    def actualizar(self, id: int, perfil: Perfil):
        for i, p in enumerate(self.perfiles):
            if p.id == id:
                self.perfiles[i] = perfil
                return perfil
        return None

    def eliminar(self, id: int):
        for p in self.perfiles:
            if p.id == id:
                self.perfiles.remove(p)
                return True
        return False
