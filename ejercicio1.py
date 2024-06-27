#-----Ejercicio 1-----
from datetime import date, timedelta

class Fecha():
    def __init__(self, dd=None, mm=None, aaaa=None):
        if dd is None or mm is None or aaaa is None:
            fecha_actual = date.today()
            self.dia = fecha_actual.day
            self.mes = fecha_actual.month
            self.anio = fecha_actual.year
        else:
            self.dia = dd
            self.mes = mm
            self.anio = aaaa
        
    def convertir_fecha(self):
        return date(self.anio, self.mes, self.dia)
    
    def calcular_dif_fecha(self, nuevafecha):
        fecha_1 = self.convertir_fecha()
        fecha_2 = nuevafecha.convertir_fecha()
        return abs ((fecha_2 - fecha_1).days)
    
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anio}"
    def __add__(self, dd):
        otrafecha = self.convertir_fecha() + timedelta(days=dd)
        return Fecha(otrafecha.day, otrafecha.month, otrafecha.year)
    def __eq__(self, nuevafecha):
        return self.dia == nuevafecha.dia and self.mes == nuevafecha.mes and self.anio == nuevafecha.anio
    
#-----Ejercicio 2-----
from datetime import datetime
class Alumno:
    def __init__(self, nombre, dni, fechaingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fechaingreso,
            "Carrera": carrera
        }
    def cambiar_dato(self, clave, nuevovalor):
            self.datos[clave] = nuevovalor
        
    def cambiar_varios_datos(self, nuevosvalores):
        for clave, valor in nuevosvalores.items():
                self.datos[clave] = valor
                
    def antiguedad(self):
        fecha_ingreso = datetime.strptime(self.datos["FechaIngreso"], "%Y-%m-%d")
        fecha_actual = datetime.now()
        antiguedad_alumno = fecha_actual - fecha_ingreso
        return antiguedad_alumno
                
    def __str__(self):
        #return f"Alumno(Nombre: {self.nombre}, DNI: {self.dni}, Fecha de ingreso: {self.fechaingreso}, Carrera: {self.carrera})"
        datos_str = ', '.join(f"{llave}: {valor}" for llave, valor in self.datos.items())
        return f"Alumno({datos_str})"
    
    def __eq__(self, otroalumno):
        if isinstance(otroalumno, Alumno):
            return self.datos == otroalumno.datos
        return False

#-----Ejercicio 3-----
import random
import string
class Nodo:
    def __init__(self, alumno=None, siguiente=None, anterior=None):
        self.alumno = alumno
        self.siguiente = siguiente
        self.anterior = anterior
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0
        
    def esta_vacia(self):
        return self.size == 0
    
    def insertar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
            self.size += 1
            
    def __iter__(self):
        current = self.cabeza
        while current:
            yield current.alumno
            current = current.siguiente
            
    def lista_ejemplo(self, cantidad_alumnos):
        for _ in range(cantidad_alumnos):
            nombre = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = datetime.now().strftime("%Y-%m-%d")
            carrera = random.choice(["Ingeniería Informática", "Matemáticas", "Física", "Ciencias Sociales"])
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
        self.insertar_al_final(alumno)

#----Ejercicio 4-----


#-----Ejercicio 5-----

