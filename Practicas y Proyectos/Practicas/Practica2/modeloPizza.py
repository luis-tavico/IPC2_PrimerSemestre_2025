class Pizza:
    def __init__(self, especialidad, tiempo):
        self.especialidad = especialidad
        self.tiempo = tiempo
    
    def getEspecialidad(self):
        return self.especialidad

    def getTiempo(self):
        return self.tiempo

    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad

    def setTiempo(self, tiempo):
        self.tiempo = tiempo