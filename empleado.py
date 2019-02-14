class Empleado:
    def__init__(self, nombre, salario, tasa):
        self.__nombre = nombre
        self.__salario = salario
        self.__tasa = tasa
    def CalculoImpuestos(self):
        self.__impuestos = self.__salario*self.__tasa
        print(("El empleado {name} debe pagar {tax:.2f}".format(name=self.__nombre,tax=self.__impuestos)))
        return self.__impuestos

class Directivo(Empleado):
    def__init__(self, nombre, salario, tasa, bonus):
    	self.__bonus = bonus

emp1 = Empleado("Pepe", 20000, 0.35)
emp1.CalculoImpuestos()
dir1 = Directivo("Ana", 30000, 0.30)
dir1.CalculoImpuestos()
