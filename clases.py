class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        self.saldo -= cantidad

    def mostrar_saldo(self):
        return self.saldo

class Estudiante:
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Matrícula: {self.matricula}, Carrera: {self.carrera}"

    def mostrar_carrera(self):
        return self.carrera

    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera