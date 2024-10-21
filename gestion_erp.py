# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:30:34 2024

@author: Usuario
"""

# %% 1. Importación de módulos
from abc import ABC, abstractmethod

# %% 2. Creación de las clases necesarias
""" 1. Creamos la clase abstracta empleado (padre) y sus hijas: Empleado_hora 
       y Empleado_asalariado
"""


class Empleado(ABC):
    def __init__(self, nombre, edad, id_empleado):
        self.nombre = nombre
        self.edad = edad
        self.id = id_empleado

    # Método abstracto que deben implementar las subclases
    @abstractmethod
    def calcular_pago():
        pass  # pasamos este método a cada clase hija

    # Método concreto que heredan las subclases
    def mostrar_info(self):
        return f"El nombre del empleado es {self.nombre}, el cual tiene una edad de {self.edad} años y un id: {self.id}"

# clase hija de Empleado


class Empleado_Hora(Empleado):

    def __init__(self, nombre, edad, id_empleado, horas_trabajadas, tarifa_hora):
        super().__init__(nombre, edad, id_empleado)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_pago(self):
        pago = (self.horas_trabajadas * self.tarifa_hora)
        print(
            f"El pago del empleado {self.id} que es un empleado por hora es {pago} €")
        return pago

# clase hija de Empleado


class Empleado_Asalariado(Empleado):

    def __init__(self, nombre, edad, id_empleado, salario_mensual):
        super().__init__(nombre, edad, id_empleado)
        self.salario_mensual = salario_mensual

    def calcular_pago(self):
        pago = self.salario_mensual
        print(
            f"El pago del empleado {self.id} que es un empleado asalariado es {pago} €")
        return pago


""" Clase empresa """


class Empresa():
    def __init__(self, nombre_empresa):
        self.nombre_empresa = nombre_empresa
        self.empleados = []

    def Agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def Calculo_pago_empleado(self):
        for empleado in self.empleados:
            print(empleado.calcular_pago())
        return

    def Calculo_pago_total(self):
        pago_total = 0
        for empleado in self.empleados:
            pago_total += empleado.calcular_pago()
        return f"El coste total a la empresa por sus trabajadores es {pago_total}"

    def lista_empleados(self):
        for empleado in self.empleados:
            print(empleado.mostrar_info())


# %% 2. Código
if __name__ == "__main__":
    # Crear empresa
    mi_empresa = Empresa("IES Las Salinas")

    # Agregar empleados por hora
    empleado1 = Empleado_Hora(
        "Sebastian", 19, 101, horas_trabajadas=40, tarifa_hora=15)
    empleado2 = Empleado_Hora(
        "Javier", 19, 102, horas_trabajadas=30, tarifa_hora=18)

    # Agregar empleados asalariados
    empleado3 = Empleado_Asalariado("Manu", 26, 103, salario_mensual=6000)
    empleado4 = Empleado_Asalariado("Iván", 20, 104, salario_mensual=3500)

    # Agregar empleados a la empresa
    mi_empresa.Agregar_empleado(empleado1)
    mi_empresa.Agregar_empleado(empleado2)
    mi_empresa.Agregar_empleado(empleado3)
    mi_empresa.Agregar_empleado(empleado4)

    # Listar empleados
    print("Lista de empleados:")
    mi_empresa.lista_empleados()

    # Calcular pago por empleado
    print("Pagos individuales:")
    mi_empresa.Calculo_pago_empleado()

    # Calcular pago total
    print("Pago total:")
    print(mi_empresa.Calculo_pago_total())
