from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
import random




author = 'Alex Dyer'

doc = """
Simulador de planeamiento 
"""


class Constants(BaseConstants):
    name_in_url = 'JUEGOSIMULADOR_High_Different'
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

    HanoiDemanda1 = 1300
    HanoiDemanda2 = 800
    HanoiDemanda3 = 800
    HanoiDemanda4 = 800
    HanoiDemanda5 = 700
    HanoiDemanda6 = 1000
    rojoHanoiDemanda1 = 900
    rojoHanoiDemanda2 = 600
    rojoHanoiDemanda3 = 600
    rojoHanoiDemanda4 = 800
    rojoHanoiDemanda5 = 800
    rojoHanoiDemanda6 = 800

    HanoiDemanda7 = 900
    HanoiDemanda8 = 800
    HanoiDemanda9 = 900
    HanoiDemanda10 = 1200
    HanoiDemanda11 = 800
    HanoiDemanda12 = 700
    rojoHanoiDemanda7 = 1000
    rojoHanoiDemanda8 = 900
    rojoHanoiDemanda9 = 800
    rojoHanoiDemanda10 = 1000
    rojoHanoiDemanda11 = 900
    rojoHanoiDemanda12 = 700

    MexicoDemanda1 = 1100
    MexicoDemanda2 = 1000
    MexicoDemanda3 = 800
    MexicoDemanda4 = 1400
    MexicoDemanda5 = 1300
    MexicoDemanda6 = 1200
    rojoMexicoDemanda1 = 500
    rojoMexicoDemanda2 = 500
    rojoMexicoDemanda3 = 600
    rojoMexicoDemanda4 = 600
    rojoMexicoDemanda5 = 500
    rojoMexicoDemanda6 = 500

    MexicoDemanda7 = 1200
    MexicoDemanda8 = 900
    MexicoDemanda9 = 1000
    MexicoDemanda10 = 1200
    MexicoDemanda11 = 1700
    MexicoDemanda12 = 1100
    rojoMexicoDemanda7 = 600
    rojoMexicoDemanda8 = 400
    rojoMexicoDemanda9 = 700
    rojoMexicoDemanda10 = 600
    rojoMexicoDemanda11 = 400
    rojoMexicoDemanda12 = 700


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


    ProduccionHanoi1 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi2 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi3 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi4 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi5 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi6 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi7 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi8 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi9 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi10 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi11 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionHanoi12 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi1 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi2 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi3 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi4 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi5 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi6 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi7 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi8 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi9 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi10 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi11 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionHanoi12 = models.IntegerField(initial=0, min=0, max=1500)

    ProduccionMexico1 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico2 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico3 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico4 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico5 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico6 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico7 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico8 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico9 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico10 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico11 = models.IntegerField(initial=0, min=0, max=1500)
    ProduccionMexico12 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico1 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico2 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico3 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico4 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico5 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico6 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico7 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico8 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico9 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico10 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico11 = models.IntegerField(initial=0, min=0, max=1500)
    RojoProduccionMexico12 = models.IntegerField(initial=0, min=0, max=1500)


    Pregunta1 = models.FloatField(initial=0)
    Pregunta2 = models.IntegerField(initial=0)
    Pregunta3 = models.IntegerField(initial=0)
    Pregunta4 = models.IntegerField(initial=0)

    Question1 = models.IntegerField(initial=0, min = 1, max = 5)
    Question2 = models.IntegerField(initial=0, min = 1, max = 5)
    Question3 = models.IntegerField(initial=0, min = 1, max = 5)
    Question4 = models.IntegerField(initial=0, min = 1, max = 5)
    Question5 = models.IntegerField(initial=0, min = 1, max = 5)
    Question6 = models.IntegerField(initial=0, min = 1, max = 5)

    Age = models.IntegerField(label="What age are you?", min=0, max = 120)
    Sex = models.StringField(label="What is your gender?", choices=["Male", "Female", "Other"])
    Nationality = models.StringField(label="What is your nationality",
    choices=["american","argentinean","australian","belgian","brazilian","british","canadian","chilean","chinese",
             "colombian","cuban","croatian","danish","dominican","dutch","ecuadorean","finnish","french","german",
             "hungarian","icelander","indian","italian","japanese","mexican","peruvian","russian","scottish","spanish","swedish",
             "swiss","turkish","venezuelan"])
    Profession = models.StringField(label="What is your profession?", choices =["Engineering related", "Life Sciences related",
                                                                                "Business related","Other"])
    Instruction = models.StringField(label="What is the highest degree or level of school you have completed?",
    choices=["High School Graduate", "Currently Undergraduate", "Bachelor Graduate", "Master", "Doctor", ])
    Experience = models.StringField(label="Do You have any experience in production or supply chain planning?", choices=["Yes","No"])
    Code = models.IntegerField(label = "Write here the code")

    AttentionQuestion1 = models.StringField(label="Which of the following is what you need to decide?",choices=["Profit of the company",
                        "Cost of production","Production lot size of two products","Production Capacity","Level of sales"])
    AttentionQuestion2 = models.StringField(label=" Which cost needs to be minized?     a)Cost of backorders  b)Marketing  c)Purchasing costs  d)Inventory costs  e)set-up costs",
    choices=["A,B,C","A,B,D","A,B,E","A,C,D","A,C,E","A,D,E","B,C,D","B,C,E","B,D,E","C,D,E"])
    AttentionQuestion3 = models.StringField(label=" Which of the following is True ",
    choices=["The lot sizes need to be decided before the demand of the period is revealed",
                        "The lot sizes need to be decided after the demand of the period is revealed",
                        "The price is decided before the demand and lot size is revealed",
                                            "The price is decided after the demand and lot size is revealed"])



