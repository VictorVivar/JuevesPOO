class Autor:
    def __init__(self,nom ,pseudo):
        self.__nombre = nom
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self, pseudo):
        self.__pseudonimo = pseudo

    def __str__(self):
        return f"Nombre: {self.__nombre} pseudonimo: {self.__pseudonimo}"

    def escribir(self):
        print(f"{self.__pseudonimo} está escribiendo su siguiente obra")

class Libro:
    def __init__(self,tit, aut, an, ed):
        self.__titulo = tit
        self.__autor = aut
        self.__año = an
        self.__editorial = ed

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def autor(self, tit):
        self.__titulo = tit


    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, aut):
        self.__autor = aut

    @property
    def año(self):
        return self.__año

    @año.setter
    def año(self, an):
        self.__año = an

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, ed):
        self.__editorial = ed

    def __str__(self):
        return f"""
             Título = {self.__titulo}
             Autor = {self.__autor}
             Año = {self.__año}
             Editorial = {self.__editorial}
           """

    @classmethod
    def libro_planeta(cls, titulo, autor, año):
        return cls(titulo, autor, año, "Planeta")

    def leer(self, minutos):
        print(f"Leyendo por {minutos} minutos")


class Persona:
    descripcion = "un ser humano común y corriente"

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, ed):
        self.__edad = ed

    def __str__(self):
        return f"Nombre: {self.__nombre} Edad: {self.__edad}"

    def dormir(self):
        print("ZzZzZzZzZzZz que calors.... zZzz")

    @classmethod
    def constructor_defecto(cls):
        return cls("", 0)


class Alumno(Persona):
    descripcion = "Una persona que dice que estudia pero se la pasa en el cel"

    def __init__(self, nombre, edad, nc, carrera):
        super().__init__(nombre, edad)
        self.__numero_cuenta = nc
        self.__carrera = carrera

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, nc):
        self.__numero_cuenta = nc

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    def __str__(self):
        return super().__str__() + f", Numero de cuenta: {self.__numero_cuenta}, Carrera: {self.__carrera}"

    def dormir(self):
        print(super().nombre, " está durmiendo como alumno")

    @classmethod
    def constructor_defecto(cls):
        return cls("", 0, "", "")


class Profesor(Persona):
    descripcion = "Una persona que dice que enseña pero se la pasa leyendo artículos de investigación"

    def __init__(self, nombre, edad, num_tra, area):
        super().__init__(nombre, edad)
        self.__numero_trabajador = num_tra
        self.__area = area

    @property
    def numero_trabajador(self):
        return self.__numero_trabajador

    @numero_trabajador.setter
    def numero_trabajador(self, num_tra):
        self.__numero_trabajador = num_tra

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    def __str__(self):
        return super().__str__() + f", Numero de trabajador: {self.__numero_trabajador}, Area: {self.__area}"

    def dormir(self):
        print(super().nombre, " está durmiendo como profesor")