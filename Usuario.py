class Usuario:

    # Lugar para definir variable no existe

    # Pero si tienen (nombre_usuario) (clave) Nombre - Apellido - Ubicacion | en comun

    def __init__(self, nombre_usuario , clave , nombre , apellido , ubicacion):

        self.nombre_usuario    = nombre_usuario
        self.clave_ingreso     = clave
        self.nombre            = nombre
        self.apellido          = apellido
        self.ubicacion_usuario = ubicacion


class Doctor(Usuario):

    # Clase de Doctor: Carnet - Precio Cobra / consulta - Especialidad

    def __init__(self, nombre_usuario, clave, nombre, apellido, ubicacion, carnet, precio , especialidad):
        super().__init__(nombre_usuario, clave, nombre, apellido, ubicacion)

        self.carnet_doctor       = carnet
        self.precio_consulta     = precio
        self.especialidad_doctor = especialidad

    def recaudar_datos_doctor(self):
        return self.nombre_usuario + "," + self.clave_ingreso + "," + self.nombre+ "," + self.apellido + "," + self.ubicacion_usuario + "," + self.carnet_doctor + "," + self.precio_consulta + "," + self.especialidad_doctor + "\n"

class Paciente(Usuario):

    # Clase de paciente: Edad - Presupuesto - Estatura - Peso (Kg) - Sintomas

    def __init__(self, nombre_usuario, clave, nombre, apellido, ubicacion, edad, presupuesto, estatura, peso, sintoma):
        super().__init__(nombre_usuario, clave, nombre, apellido, ubicacion)

        self.edad_paciente        = edad
        self.presupuesto_paciente = presupuesto
        self.estatura_paciente    = estatura
        self.peso_paciente        = peso
        self.sintoma_paciente     = sintoma

    def recaudar_datos_paciente(self):
        return self.nombre_usuario + "," + self.clave_ingreso + "," + self.nombre + "," + self.apellido+ "," + self.ubicacion_usuario  + "," + self.edad_paciente  + "," + self.presupuesto_paciente  + "," + self.estatura_paciente  + "," + self.peso_paciente  + "," + self.sintoma_paciente + "\n"
    
class Calificaciones(Usuario):
    
    #Clase de reseñas: carnet - reseña
    
    def __init__(self, carnet, calificacion):
        
        self.carnet_d_doctor       = carnet
        self.calificacion_d_doctor = calificacion