# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:30:11 2024

@author: Usuario
"""

# %% 1, Importamción de módulos
# Importamos las clases necesarias
from gestion_erp import Empleado_Hora, Empleado_Asalariado, Empresa

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
