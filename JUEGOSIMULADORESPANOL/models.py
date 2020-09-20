from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Alex Dyer'

doc = """
Simulador de planeamiento 
"""


class Constants(BaseConstants):
    name_in_url = 'JUEGOSIMULADORESPANOL'
    players_per_group = None

    Capacidad = 2200
    Capacidad2 = 2200

    SETUP = 0
    SETUP2 = 0

    CostoProducto1 = 4
    CostoProducto2 = 4

    CostoInventario1 = 3
    CostoInventario2 = 3

    CostoBackorder1 = 18
    CostoBackorder2 = 18

    num_rounds = 1
    inventario_inicial = 100
    inventario_inicialR = 100

    inventario_inicial2 = 100
    inventario_inicialR2 = 100

    inventario_inicial3 = 100
    inventario_inicialR3 = 100

    inventario_inicial4 = 100
    inventario_inicialR4 = 100

    LimaDemanda1 = 1100
    LimaDemanda2 = 1500
    LimaDemanda3 = 1800
    LimaDemanda4 = 1800
    LimaDemanda5 = 1500
    LimaDemanda6 = 1600
    rojoLimaDemanda1 = 500
    rojoLimaDemanda2 = 700
    rojoLimaDemanda3 = 800
    rojoLimaDemanda4 = 400
    rojoLimaDemanda5 = 500
    rojoLimaDemanda6 = 500

    LimaDemanda7 = 1300
    LimaDemanda8 = 1200
    LimaDemanda9 = 1800
    LimaDemanda10 = 1500
    LimaDemanda11 = 1400
    LimaDemanda12 = 1600
    rojoLimaDemanda7 = 300
    rojoLimaDemanda8 = 500
    rojoLimaDemanda9 = 400
    rojoLimaDemanda10 = 700
    rojoLimaDemanda11 = 500
    rojoLimaDemanda12 = 300

    JaponDemanda1 = 1300
    JaponDemanda2 = 1600
    JaponDemanda3 = 1600
    JaponDemanda4 = 1700
    JaponDemanda5 = 1800
    JaponDemanda6 = 1500
    rojoJaponDemanda1 = 800
    rojoJaponDemanda2 = 500
    rojoJaponDemanda3 = 500
    rojoJaponDemanda4 = 600
    rojoJaponDemanda5 = 400
    rojoJaponDemanda6 = 600

    JaponDemanda7 = 1200
    JaponDemanda8 = 1100
    JaponDemanda9 = 1900
    JaponDemanda10 = 1700
    JaponDemanda11 = 1500
    JaponDemanda12 = 1500
    rojoJaponDemanda7 = 200
    rojoJaponDemanda8 = 600
    rojoJaponDemanda9 = 500
    rojoJaponDemanda10 = 400
    rojoJaponDemanda11 = 700
    rojoJaponDemanda12 = 400


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass




class Player(BasePlayer):

    ProduccionLima1 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionLima2 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionLima3 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionLima4 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionLima5 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionLima6 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionLima7 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionLima8 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionLima9 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionLima10 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionLima11 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionLima12 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima1 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima2 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima3 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima4 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima5 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima6 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima7 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima8 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima9 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima10 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima11 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionLima12 = models.IntegerField(initial=0, min=0, max=5500, label="")

    tabla1 = models.BooleanField(label="¿Deseas calcular tus costos antes de pasar de periodo? - Si elige SI y apreta next se actualizaran los costos con la produccion que propuso")

    ProduccionJapon1 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionJapon2 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionJapon3 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionJapon4 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionJapon5 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionJapon6 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionJapon7 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionJapon8 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionJapon9 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionJapon10 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionJapon11 = models.IntegerField(initial=0, min=0, max=5500, label="")
    ProduccionJapon12 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon1 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon2 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon3 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon4 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon5 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon6 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon7 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon8 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon9 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon10 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon11 = models.IntegerField(initial=0, min=0, max=5500, label="")
    RojoProduccionJapon12 = models.IntegerField(initial=0, min=0, max=5500, label="")


    Pregunta1 = models.FloatField(initial=0)
    Pregunta2 = models.IntegerField(initial=0)
    Pregunta3 = models.IntegerField(initial=0)
    Pregunta4 = models.IntegerField(initial=0)

    Manipulation1 = models.StringField()
    Manipulation2 = models.StringField()
    Manipulation3 = models.StringField()
    Manipulation4 = models.StringField()
    Manipulation5 = models.StringField()


