from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = ''

doc = """
Simulador de planeamiento 2
"""

class Constants(BaseConstants):
    name_in_url = 'JUEGOSIMULADOR2'
    players_per_group = None
    num_rounds = 1
    inventario_inicial = 1000
    inventario_inicialR = 1000

    inventario_inicial2 = 1000
    inventario_inicialR2 = 500

    inventario_inicial3 = 1000
    inventario_inicialR3 = 1000

    inventario_inicial4 = 1000
    inventario_inicialR4 = 500

    LimaDemanda1 = 1700
    LimaDemanda2 = 1400
    LimaDemanda3 = 1400
    LimaDemanda4 = 1700
    LimaDemanda5 = 300
    LimaDemanda6 = 1100
    rojoLimaDemanda1 = 300
    rojoLimaDemanda2 = 600
    rojoLimaDemanda3 = 500
    rojoLimaDemanda4 = 1000
    rojoLimaDemanda5 = 700
    rojoLimaDemanda6 = 800
    LimaDemanda7 = 900
    LimaDemanda8 = 300
    LimaDemanda9 = 1200
    LimaDemanda10 = 400
    LimaDemanda11 = 1700
    LimaDemanda12 = 800
    rojoLimaDemanda7 = 400
    rojoLimaDemanda8 = 1400
    rojoLimaDemanda9 = 100
    rojoLimaDemanda10 = 1100
    rojoLimaDemanda11 = 1400
    rojoLimaDemanda12 = 800

    JaponDemanda1 = 800
    JaponDemanda2 = 3000
    JaponDemanda3 = 1800
    JaponDemanda4 = 1500
    JaponDemanda5 = 1000
    JaponDemanda6 = 2000
    rojoJaponDemanda1 = 1300
    rojoJaponDemanda2 = 200
    rojoJaponDemanda3 = 600
    rojoJaponDemanda4 = 600
    rojoJaponDemanda5 = 1100
    rojoJaponDemanda6 = 200
    JaponDemanda7 = 1300
    JaponDemanda8 = 1100
    JaponDemanda9 = 100
    JaponDemanda10 = 1700
    JaponDemanda11 = 1500
    JaponDemanda12 = 900
    rojoJaponDemanda7 = 100
    rojoJaponDemanda8 = 600
    rojoJaponDemanda9 = 500
    rojoJaponDemanda10 = 600
    rojoJaponDemanda11 = 800
    rojoJaponDemanda12 = 700

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    ProduccionLima1 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima2 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima3 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima4 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima5 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima6 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima7 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima8 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima9 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima10 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima11 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionLima12 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima1 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima2 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima3 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima4 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima5 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima6 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima7 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima8 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima9 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima10 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima11 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionLima12 = models.IntegerField(initial=0, min=0, max=1500, label="")

    tabla1 = models.BooleanField(label="¿Deseas calcular tus costos antes de pasar de periodo? - Si elige SI y apreta next se actualizaran los costos con la produccion que propuso")

    ProduccionJapon1 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionJapon2 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionJapon3 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionJapon4 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionJapon5 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionJapon6 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionJapon7 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionJapon8 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionJapon9 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionJapon10 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionJapon11 = models.IntegerField(initial=0, min=0, max=1500, label="")
    ProduccionJapon12 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon1 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon2 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon3 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon4 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon5 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon6 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon7 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon8 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon9 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon10 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon11 = models.IntegerField(initial=0, min=0, max=1500, label="")
    RojoProduccionJapon12 = models.IntegerField(initial=0, min=0, max=1500, label="")

