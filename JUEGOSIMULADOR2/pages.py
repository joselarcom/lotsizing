from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import decimal

class Inicio7LIMA(Page):
    def before_next_page(self):
        global inventariofinal1, rojoinventariofinal1, ventasperdidas1, rojoventasperdidas1, setup1, rojosetup1
        inventariofinal1 = 0
        rojoinventariofinal1 = 0
        ventasperdidas1 = 0
        rojoventasperdidas1 = 0
        setup1 = 0
        rojosetup1 = 0
    pass

##Crear una clase mensaje que la puedas llamar desde el html

class Lima1(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima1','RojoProduccionLima1']

    def error_message(self, values):

        global inventariofinal1, rojoinventariofinal1, ventasperdidas1, rojoventasperdidas1, setup1, rojosetup1

        inventariofinal1 = max(values['ProduccionLima1']+Constants.inventario_inicial-Constants.LimaDemanda1, 0)
        rojoinventariofinal1 = max(values['RojoProduccionLima1']+Constants.inventario_inicialR-Constants.rojoLimaDemanda1, 0)
        ventasperdidas1 = max(Constants.LimaDemanda1-values['ProduccionLima1']-Constants.inventario_inicial, 0)
        rojoventasperdidas1 = max(Constants.rojoLimaDemanda1-values['RojoProduccionLima1']-Constants.inventario_inicialR, 0)

        if values["ProduccionLima1"]>0:
            setup1=1500
        else:
            setup1=0

        if values["RojoProduccionLima1"]>0:
            rojosetup1=1500
        else:
            rojosetup1=0

        if values["ProduccionLima1"] + values["RojoProduccionLima1"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return{
            'InvAzul':inventariofinal1,
            'InvRojo':rojoinventariofinal1,
            'VentaPerdidaAzul':ventasperdidas1,
            'VentaPerdidaRojo':rojoventasperdidas1,
            'AlmacenamientoAzul':inventariofinal1*5,
            'AlmacenamientoRojo':rojoinventariofinal1*5,
            'CostoPerdidasAzul':ventasperdidas1*10,
            'CostoPerdidasRojo':rojoventasperdidas1*10,
            'SetupAzul':setup1,
            'SetupRojo':rojosetup1,
            'TotalesAzul':inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'TotalesRojo':rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,
}

class Lima2(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima2','RojoProduccionLima2']
    global inventariofinal2, rojoinventariofinal2, ventasperdidas2, rojoventasperdidas2, setup2, rojosetup2
    inventariofinal2 = 0
    rojoinventariofinal2 = 0
    ventasperdidas2 = 0
    rojoventasperdidas2 = 0
    setup2 = 0
    rojosetup2 = 0

    def error_message(self, values):
        global inventariofinal2,rojoinventariofinal2,ventasperdidas2,rojoventasperdidas2,setup2,rojosetup2

        inventariofinal2 = max(values['ProduccionLima2'] + inventariofinal1 - Constants.LimaDemanda2, 0)
        rojoinventariofinal2 = max(values['RojoProduccionLima2'] + rojoinventariofinal1 - Constants.rojoLimaDemanda2, 0)
        ventasperdidas2 = max(Constants.LimaDemanda2 - values['ProduccionLima2'] - inventariofinal1, 0)
        rojoventasperdidas2 = max(Constants.rojoLimaDemanda2 - values['RojoProduccionLima2'] - rojoinventariofinal1, 0)

        if values["ProduccionLima2"] > 0:
            setup2 = 1500
        else:
            setup2 = 0

        if values["RojoProduccionLima2"] > 0:
            rojosetup2 = 1500
        else:
            rojosetup2 = 0

        if values["ProduccionLima2"] + values["RojoProduccionLima2"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal2,
            'InvRojo': rojoinventariofinal2,
            'VentaPerdidaAzul': ventasperdidas2,
            'VentaPerdidaRojo': rojoventasperdidas2,
            'AlmacenamientoAzul': inventariofinal2 * 5,
            'AlmacenamientoRojo': rojoinventariofinal2 * 5,
            'CostoPerdidasAzul': ventasperdidas2 * 10,
            'CostoPerdidasRojo': rojoventasperdidas2 * 10,
            'SetupAzul': setup2,
            'SetupRojo': rojosetup2,
            'TotalesAzul': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'TotalesRojo': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'inventario2': inventariofinal1,
            'Rojoinventario2': rojoinventariofinal1,

            'ventasperdidas1':ventasperdidas1,
            'rojoventasperdidas1':rojoventasperdidas1,
            'costoalmacenamiento1':inventariofinal1*5,
            'rojocostoalmacenamiento1':rojoinventariofinal1*5,
            'costoventasperdidas1':ventasperdidas1*10,
            'rojocostoventasperdidas1':rojoventasperdidas1*10,
            'setup1':setup1,
            'rojosetup1':rojosetup1,
            'totales1':inventariofinal1*5+ventasperdidas1*10+setup1,
            'rojototales1':rojoinventariofinal1*5+rojoventasperdidas1*10+rojosetup1
        }


class Lima3(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima3','RojoProduccionLima3']
    global inventariofinal3, rojoinventariofinal3, ventasperdidas3, rojoventasperdidas3, setup3, rojosetup3
    inventariofinal3 = 0
    rojoinventariofinal3 = 0
    ventasperdidas3 = 0
    rojoventasperdidas3 = 0
    setup3 = 0
    rojosetup3 = 0

    def error_message(self, values):
        global inventariofinal3, rojoinventariofinal3, ventasperdidas3, rojoventasperdidas3,setup3,rojosetup3

        inventariofinal3 = max(values['ProduccionLima3'] + inventariofinal2 - Constants.LimaDemanda3, 0)
        rojoinventariofinal3 = max(values['RojoProduccionLima3'] + rojoinventariofinal2 - Constants.rojoLimaDemanda3, 0)
        ventasperdidas3 = max(Constants.LimaDemanda3 - values['ProduccionLima3'] - inventariofinal2, 0)
        rojoventasperdidas3 = max(Constants.rojoLimaDemanda3 - values['RojoProduccionLima3'] - rojoinventariofinal2, 0)

        if values["ProduccionLima3"] > 0:
            setup3 = 1500
        else:
            setup3 = 0

        if values["RojoProduccionLima3"] > 0:
            rojosetup3 = 1500
        else:
            rojosetup3 = 0
        
        if values["ProduccionLima3"] + values["RojoProduccionLima3"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal3,
            'InvRojo': rojoinventariofinal3,
            'VentaPerdidaAzul': ventasperdidas3,
            'VentaPerdidaRojo': rojoventasperdidas3,
            'AlmacenamientoAzul': inventariofinal3 * 5,
            'AlmacenamientoRojo': rojoinventariofinal3 * 5,
            'CostoPerdidasAzul': ventasperdidas3 * 10,
            'CostoPerdidasRojo': rojoventasperdidas3 * 10,
            'SetupAzul': setup3,
            'SetupRojo': rojosetup3,
            'TotalesAzul': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'TotalesRojo': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

        }

class Lima4(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima4','RojoProduccionLima4']
    global inventariofinal4, rojoinventariofinal4, ventasperdidas4, rojoventasperdidas4, setup4, rojosetup4
    inventariofinal4 = 0
    rojoinventariofinal4 = 0
    ventasperdidas4 = 0
    rojoventasperdidas4 = 0
    setup4 = 0
    rojosetup4 = 0

    def error_message(self, values):
        global inventariofinal4, rojoinventariofinal4, ventasperdidas4, rojoventasperdidas4,setup4,rojosetup4

        inventariofinal4 = max(values['ProduccionLima4'] + inventariofinal3 - Constants.LimaDemanda4, 0)
        rojoinventariofinal4 = max(values['RojoProduccionLima4'] + rojoinventariofinal3 - Constants.rojoLimaDemanda4, 0)
        ventasperdidas4 = max(Constants.LimaDemanda4 - values['ProduccionLima4'] - inventariofinal3, 0)
        rojoventasperdidas4 = max(Constants.rojoLimaDemanda4 - values['RojoProduccionLima4'] - rojoinventariofinal3, 0)

        if values["ProduccionLima4"] > 0:
            setup4 = 1500
        else:
            setup4 = 0

        if values["RojoProduccionLima4"] > 0:
            rojosetup4 = 1500
        else:
            rojosetup4 = 0

        if values["ProduccionLima4"] + values["RojoProduccionLima4"] > 1500:
            return ' La produccion no debe pasar de 1500'


    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal4,
            'InvRojo': rojoinventariofinal4,
            'VentaPerdidaAzul': ventasperdidas4,
            'VentaPerdidaRojo': rojoventasperdidas4,
            'AlmacenamientoAzul': inventariofinal4 * 5,
            'AlmacenamientoRojo': rojoinventariofinal4 * 5,
            'CostoPerdidasAzul': ventasperdidas4 * 10,
            'CostoPerdidasRojo': rojoventasperdidas4 * 10,
            'SetupAzul': setup4,
            'SetupRojo': rojosetup4,
            'TotalesAzul': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'TotalesRojo': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,
        }

class Lima5(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima5','RojoProduccionLima5']
    global inventariofinal5, rojoinventariofinal5, ventasperdidas5, rojoventasperdidas5, setup5, rojosetup5
    inventariofinal5 = 0
    rojoinventariofinal5 = 0
    ventasperdidas5 = 0
    rojoventasperdidas5 = 0
    setup5 = 0
    rojosetup5 = 0

    def error_message(self, values):
        global inventariofinal5, rojoinventariofinal5, ventasperdidas5, rojoventasperdidas5,setup5,rojosetup5

        inventariofinal5 = max(values['ProduccionLima5'] + inventariofinal4 - Constants.LimaDemanda5, 0)
        rojoinventariofinal5 = max(values['RojoProduccionLima5'] + rojoinventariofinal4 - Constants.rojoLimaDemanda5, 0)
        ventasperdidas5 = max(Constants.LimaDemanda5 - values['ProduccionLima5'] - inventariofinal4, 0)
        rojoventasperdidas5 = max(Constants.rojoLimaDemanda5 - values['RojoProduccionLima5'] - rojoinventariofinal4, 0)

        if values["ProduccionLima5"] > 0:
            setup5 = 1500
        else:
            setup5 = 0

        if values["RojoProduccionLima5"] > 0:
            rojosetup5 = 1500
        else:
            rojosetup5 = 0

        if values["ProduccionLima5"] + values["RojoProduccionLima5"] > 1500:
            return ' La produccion no debe pasar de 1500'


    def vars_for_template(self):

        return{
            'InvAzul': inventariofinal5,
            'InvRojo': rojoinventariofinal5,
            'VentaPerdidaAzul': ventasperdidas5,
            'VentaPerdidaRojo': rojoventasperdidas5,
            'AlmacenamientoAzul': inventariofinal5 * 5,
            'AlmacenamientoRojo': rojoinventariofinal5 * 5,
            'CostoPerdidasAzul': ventasperdidas5 * 10,
            'CostoPerdidasRojo': rojoventasperdidas5 * 10,
            'SetupAzul': setup5,
            'SetupRojo': rojosetup5,
            'TotalesAzul': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'TotalesRojo': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,
        }

class Lima6(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima6','RojoProduccionLima6']
    global inventariofinal6, rojoinventariofinal6, ventasperdidas6, rojoventasperdidas6, setup6, rojosetup6
    inventariofinal6 = 0
    rojoinventariofinal6 = 0
    ventasperdidas6 = 0
    rojoventasperdidas6 = 0
    setup6 = 0
    rojosetup6 = 0

    def error_message(self, values):
        global inventariofinal6, rojoinventariofinal6, ventasperdidas6, rojoventasperdidas6,setup6,rojosetup6

        inventariofinal6 = max(values['ProduccionLima6'] + inventariofinal5 - Constants.LimaDemanda6, 0)
        rojoinventariofinal6 = max(values['RojoProduccionLima6'] + rojoinventariofinal5 - Constants.rojoLimaDemanda6, 0)
        ventasperdidas6 = max(Constants.LimaDemanda6 - values['ProduccionLima6'] - inventariofinal5, 0)
        rojoventasperdidas6 = max(Constants.rojoLimaDemanda6 - values['RojoProduccionLima6'] - rojoinventariofinal5, 0)

        if values["ProduccionLima6"] > 0:
            setup6 = 1500
        else:
            setup6 = 0

        if values["RojoProduccionLima6"] > 0:
            rojosetup6 = 1500
        else:
            rojosetup6= 0

        global TotalinventarioLima, TotalsetupLima, TotalventasLima, TotalTotalesLima

        TotalinventarioLima = (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6) * 5
        TotalinventarioLima = TotalinventarioLima + (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6) * 5
        TotalsetupLima = setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6
        TotalventasLima = (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6) * 10
        TotalventasLima = TotalventasLima + (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6) * 10
        TotalTotalesLima = TotalinventarioLima + TotalventasLima + TotalsetupLima

        if values["ProduccionLima6"] + values["RojoProduccionLima6"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):

        return{
            'InvAzul': inventariofinal6,
            'InvRojo': rojoinventariofinal6,
            'VentaPerdidaAzul': ventasperdidas6,
            'VentaPerdidaRojo': rojoventasperdidas6,
            'AlmacenamientoAzul': inventariofinal6 * 5,
            'AlmacenamientoRojo': rojoinventariofinal6 * 5,
            'CostoPerdidasAzul': ventasperdidas6 * 10,
            'CostoPerdidasRojo': rojoventasperdidas6 * 10,
            'SetupAzul': setup6,
            'SetupRojo': rojosetup6,
            'TotalesAzul': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'TotalesRojo': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,
        }


class Lima7(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima7', 'RojoProduccionLima7']
    global inventariofinal7, rojoinventariofinal7, ventasperdidas7, rojoventasperdidas7, setup7, rojosetup7
    inventariofinal7 = 0
    rojoinventariofinal7 = 0
    ventasperdidas7 = 0
    rojoventasperdidas7 = 0
    setup7 = 0
    rojosetup7 = 0

    def error_message(self, values):
        global inventariofinal7, rojoinventariofinal7, ventasperdidas7, rojoventasperdidas7, setup7, rojosetup7

        inventariofinal7 = max(values['ProduccionLima7'] + inventariofinal6 - Constants.LimaDemanda7, 0)
        rojoinventariofinal7 = max(values['RojoProduccionLima7'] + rojoinventariofinal6 - Constants.rojoLimaDemanda7, 0)
        ventasperdidas7 = max(Constants.LimaDemanda7 - values['ProduccionLima7'] - inventariofinal6, 0)
        rojoventasperdidas7 = max(Constants.rojoLimaDemanda7 - values['RojoProduccionLima7'] - rojoinventariofinal6, 0)

        if values["ProduccionLima7"] > 0:
            setup7 = 1500
        else:
            setup7 = 0

        if values["RojoProduccionLima7"] > 0:
            rojosetup7 = 1500
        else:
            rojosetup7 = 0

        if values["ProduccionLima7"] + values["RojoProduccionLima7"] > 1500:
            return 'La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal7,
            'InvRojo': rojoinventariofinal7,
            'VentaPerdidaAzul': ventasperdidas7,
            'VentaPerdidaRojo': rojoventasperdidas7,
            'AlmacenamientoAzul': inventariofinal7 * 5,
            'AlmacenamientoRojo': rojoinventariofinal7 * 5,
            'CostoPerdidasAzul': ventasperdidas7 * 10,
            'CostoPerdidasRojo': rojoventasperdidas7 * 10,
            'SetupAzul': setup7,
            'SetupRojo': rojosetup7,
            'TotalesAzul': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'TotalesRojo': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,
        }


class Lima8(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima8', 'RojoProduccionLima8']
    global inventariofinal8, rojoinventariofinal8, ventasperdidas8, rojoventasperdidas8, setup8, rojosetup8
    inventariofinal8 = 0
    rojoinventariofinal8 = 0
    ventasperdidas8 = 0
    rojoventasperdidas8 = 0
    setup8 = 0
    rojosetup8 = 0

    def error_message(self, values):
        global inventariofinal8, rojoinventariofinal8, ventasperdidas8, rojoventasperdidas8, setup8, rojosetup8

        inventariofinal8 = max(values['ProduccionLima8'] + inventariofinal7 - Constants.LimaDemanda8, 0)
        rojoinventariofinal8 = max(values['RojoProduccionLima8'] + rojoinventariofinal7 - Constants.rojoLimaDemanda8, 0)
        ventasperdidas8 = max(Constants.LimaDemanda8 - values['ProduccionLima8'] - inventariofinal7, 0)
        rojoventasperdidas8 = max(Constants.rojoLimaDemanda8 - values['RojoProduccionLima8'] - rojoinventariofinal7, 0)

        if values["ProduccionLima8"] > 0:
            setup8 = 1500
        else:
            setup8 = 0

        if values["RojoProduccionLima8"] > 0:
            rojosetup8 = 1500
        else:
            rojosetup8 = 0

        if values["ProduccionLima8"] + values["RojoProduccionLima8"] > 1500:
            return 'La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal8,
            'InvRojo': rojoinventariofinal8,
            'VentaPerdidaAzul': ventasperdidas8,
            'VentaPerdidaRojo': rojoventasperdidas8,
            'AlmacenamientoAzul': inventariofinal8 * 5,
            'AlmacenamientoRojo': rojoinventariofinal8 * 5,
            'CostoPerdidasAzul': ventasperdidas8 * 10,
            'CostoPerdidasRojo': rojoventasperdidas8 * 10,
            'SetupAzul': setup8,
            'SetupRojo': rojosetup8,
            'TotalesAzul': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'TotalesRojo': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            
            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,
        }

class Lima9(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima9', 'RojoProduccionLima9']
    global inventariofinal9, rojoinventariofinal9, ventasperdidas9, rojoventasperdidas9, setup9, rojosetup9
    inventariofinal9 = 0
    rojoinventariofinal9 = 0
    ventasperdidas9 = 0
    rojoventasperdidas9 = 0
    setup9 = 0
    rojosetup9 = 0

    def error_message(self, values):
        global inventariofinal9, rojoinventariofinal9, ventasperdidas9, rojoventasperdidas9, setup9, rojosetup9

        inventariofinal9 = max(values['ProduccionLima9'] + inventariofinal8 - Constants.LimaDemanda9, 0)
        rojoinventariofinal9 = max(values['RojoProduccionLima9'] + rojoinventariofinal8 - Constants.rojoLimaDemanda9, 0)
        ventasperdidas9 = max(Constants.LimaDemanda9 - values['ProduccionLima9'] - inventariofinal8, 0)
        rojoventasperdidas9 = max(Constants.rojoLimaDemanda9 - values['RojoProduccionLima9'] - rojoinventariofinal8, 0)

        if values["ProduccionLima9"] > 0:
            setup9 = 1500
        else:
            setup9 = 0

        if values["RojoProduccionLima9"] > 0:
            rojosetup9 = 1500
        else:
            rojosetup9 = 0

        if values["ProduccionLima9"] + values["RojoProduccionLima9"] > 1500:
            return 'La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal9,
            'InvRojo': rojoinventariofinal9,
            'VentaPerdidaAzul': ventasperdidas9,
            'VentaPerdidaRojo': rojoventasperdidas9,
            'AlmacenamientoAzul': inventariofinal9 * 5,
            'AlmacenamientoRojo': rojoinventariofinal9 * 5,
            'CostoPerdidasAzul': ventasperdidas9 * 10,
            'CostoPerdidasRojo': rojoventasperdidas9 * 10,
            'SetupAzul': setup9,
            'SetupRojo': rojosetup9,
            'TotalesAzul': inventariofinal9 * 5 + ventasperdidas9 * 10 + setup9,
            'TotalesRojo': rojoinventariofinal9 * 5 + rojoventasperdidas9 * 10 + rojosetup9,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,
            'inventario9': inventariofinal8,            
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            'Rojoinventario9': rojoinventariofinal8,
            
            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * 5,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * 5,
            'costoventasperdidas8': ventasperdidas8 * 10,
            'rojocostoventasperdidas8': rojoventasperdidas8 * 10,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'rojototales8': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

        }


class Lima10(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima10', 'RojoProduccionLima10']
    global inventariofinal10, rojoinventariofinal10, ventasperdidas10, rojoventasperdidas10, setup10, rojosetup10
    inventariofinal10 = 0
    rojoinventariofinal10 = 0
    ventasperdidas10 = 0
    rojoventasperdidas10 = 0
    setup10 = 0
    rojosetup10 = 0

    def error_message(self, values):
        global inventariofinal10, rojoinventariofinal10, ventasperdidas10, rojoventasperdidas10, setup10, rojosetup10

        inventariofinal10 = max(values['ProduccionLima10'] + inventariofinal9 - Constants.LimaDemanda10, 0)
        rojoinventariofinal10 = max(values['RojoProduccionLima10'] + rojoinventariofinal9 - Constants.rojoLimaDemanda10, 0)
        ventasperdidas10 = max(Constants.LimaDemanda10 - values['ProduccionLima10'] - inventariofinal9, 0)
        rojoventasperdidas10 = max(Constants.rojoLimaDemanda10 - values['RojoProduccionLima10'] - rojoinventariofinal9, 0)

        if values["ProduccionLima10"] > 0:
            setup10 = 1500
        else:
            setup10 = 0

        if values["RojoProduccionLima10"] > 0:
            rojosetup10 = 1500
        else:
            rojosetup10 = 0

        if values["ProduccionLima10"] + values["RojoProduccionLima10"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal10,
            'InvRojo': rojoinventariofinal10,
            'VentaPerdidaAzul': ventasperdidas10,
            'VentaPerdidaRojo': rojoventasperdidas10,
            'AlmacenamientoAzul': inventariofinal10 * 5,
            'AlmacenamientoRojo': rojoinventariofinal10 * 5,
            'CostoPerdidasAzul': ventasperdidas10 * 10,
            'CostoPerdidasRojo': rojoventasperdidas10 * 10,
            'SetupAzul': setup10,
            'SetupRojo': rojosetup10,
            'TotalesAzul': inventariofinal10 * 5 + ventasperdidas10 * 10 + setup10,
            'TotalesRojo': rojoinventariofinal10 * 5 + rojoventasperdidas10 * 10 + rojosetup10,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,
            'inventario9': inventariofinal8,
            'inventario10': inventariofinal9,                      
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            'Rojoinventario9': rojoinventariofinal8,
            'Rojoinventario10': rojoinventariofinal9,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * 5,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * 5,
            'costoventasperdidas8': ventasperdidas8 * 10,
            'rojocostoventasperdidas8': rojoventasperdidas8 * 10,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'rojototales8': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * 5,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * 5,
            'costoventasperdidas9': ventasperdidas9 * 10,
            'rojocostoventasperdidas9': rojoventasperdidas9 * 10,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * 5 + ventasperdidas9 * 10 + setup9,
            'rojototales9': rojoinventariofinal9 * 5 + rojoventasperdidas9 * 10 + rojosetup9,
        }


class Lima11(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima11', 'RojoProduccionLima11']
    global inventariofinal11, rojoinventariofinal11, ventasperdidas11, rojoventasperdidas11, setup11, rojosetup11
    inventariofinal11 = 0
    rojoinventariofinal11 = 0
    ventasperdidas11 = 0
    rojoventasperdidas11 = 0
    setup11 = 0
    rojosetup11 = 0

    def error_message(self, values):
        global inventariofinal11, rojoinventariofinal11, ventasperdidas11, rojoventasperdidas11, setup11, rojosetup11

        inventariofinal11 = max(values['ProduccionLima11'] + inventariofinal10 - Constants.LimaDemanda11, 0)
        rojoinventariofinal11 = max(values['RojoProduccionLima11'] + rojoinventariofinal10 - Constants.rojoLimaDemanda11, 0)
        ventasperdidas11 = max(Constants.LimaDemanda11 - values['ProduccionLima11'] - inventariofinal10, 0)
        rojoventasperdidas11 = max(Constants.rojoLimaDemanda11 - values['RojoProduccionLima11'] - rojoinventariofinal10, 0)

        if values["ProduccionLima11"] > 0:
            setup11 = 1500
        else:
            setup11 = 0

        if values["RojoProduccionLima11"] > 0:
            rojosetup11 = 1500
        else:
            rojosetup11 = 0

        if values["ProduccionLima11"] + values["RojoProduccionLima11"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):

        return {
            'InvAzul': inventariofinal11,
            'InvRojo': rojoinventariofinal11,
            'VentaPerdidaAzul': ventasperdidas11,
            'VentaPerdidaRojo': rojoventasperdidas11,
            'AlmacenamientoAzul': inventariofinal11 * 5,
            'AlmacenamientoRojo': rojoinventariofinal11 * 5,
            'CostoPerdidasAzul': ventasperdidas11 * 10,
            'CostoPerdidasRojo': rojoventasperdidas11 * 10,
            'SetupAzul': setup11,
            'SetupRojo': rojosetup11,
            'TotalesAzul': inventariofinal11 * 5 + ventasperdidas11 * 10 + setup11,
            'TotalesRojo': rojoinventariofinal11 * 5 + rojoventasperdidas11 * 10 + rojosetup11,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,
            'inventario9': inventariofinal8,
            'inventario10': inventariofinal9,           
            'inventario11': inventariofinal10,                      
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            'Rojoinventario9': rojoinventariofinal8,
            'Rojoinventario10': rojoinventariofinal9,
            'Rojoinventario11': rojoinventariofinal10,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * 5,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * 5,
            'costoventasperdidas8': ventasperdidas8 * 10,
            'rojocostoventasperdidas8': rojoventasperdidas8 * 10,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'rojototales8': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * 5,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * 5,
            'costoventasperdidas9': ventasperdidas9 * 10,
            'rojocostoventasperdidas9': rojoventasperdidas9 * 10,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * 5 + ventasperdidas9 * 10 + setup9,
            'rojototales9': rojoinventariofinal9 * 5 + rojoventasperdidas9 * 10 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * 5,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * 5,
            'costoventasperdidas10': ventasperdidas10 * 10,
            'rojocostoventasperdidas10': rojoventasperdidas10 * 10,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * 5 + ventasperdidas10 * 10 + setup10,
            'rojototales10': rojoinventariofinal10 * 5 + rojoventasperdidas10 * 10 + rojosetup10,
        }


class Lima12(Page):
    form_model = 'player'
    form_fields = ['ProduccionLima12', 'RojoProduccionLima12']
    global inventariofinal12, rojoinventariofinal12, ventasperdidas12, rojoventasperdidas12, setup12, rojosetup12
    inventariofinal12 = 0
    rojoinventariofinal12 = 0
    ventasperdidas12 = 0
    rojoventasperdidas12 = 0
    setup12 = 0
    rojosetup12 = 0

    def error_message(self, values):

        global inventariofinal12, rojoinventariofinal12, ventasperdidas12, rojoventasperdidas12, setup12, rojosetup12
        global TotalinventarioLima, TotalsetupLima, TotalventasLima, TotalTotalesLima

        inventariofinal12 = max(values['ProduccionLima12'] + inventariofinal11 - Constants.LimaDemanda12, 0)
        rojoinventariofinal12 = max(values['RojoProduccionLima12'] + rojoinventariofinal11 - Constants.rojoLimaDemanda12, 0)
        ventasperdidas12 = max(Constants.LimaDemanda12 - values['ProduccionLima12'] - inventariofinal11, 0)
        rojoventasperdidas12 = max(Constants.rojoLimaDemanda12 - values['RojoProduccionLima12'] - rojoinventariofinal11, 0)

        if values["ProduccionLima12"] > 0:
            setup12 = 1500
        else:
            setup12 = 0

        if values["RojoProduccionLima12"] > 0:
            rojosetup12 = 1500
        else:
            rojosetup12 = 0

        TotalinventarioLima = (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6 + inventariofinal7 + inventariofinal8 + inventariofinal9 + inventariofinal10 + inventariofinal11 + inventariofinal12) * 5
        TotalinventarioLima = (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6 + rojoinventariofinal7 + rojoinventariofinal8 + rojoinventariofinal9 + rojoinventariofinal10 + rojoinventariofinal11 + rojoinventariofinal12) * 5
        TotalsetupLima = setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + setup7 + setup8 + setup9 + setup10 + setup11 + setup12 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6 + rojosetup7 + rojosetup8 + rojosetup9 + rojosetup10 + rojosetup11 + rojosetup12
        TotalventasLima = (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6 + ventasperdidas7 + ventasperdidas8 + ventasperdidas9 + ventasperdidas10 + ventasperdidas11 + ventasperdidas12) * 10
        TotalventasLima = (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6 + rojoventasperdidas7 + rojoventasperdidas8 + rojoventasperdidas9 + rojoventasperdidas10 + rojoventasperdidas11 + rojoventasperdidas12) * 10
        TotalTotalesLima = TotalinventarioLima + TotalventasLima + TotalsetupLima

        if values["ProduccionLima12"] + values["RojoProduccionLima12"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal12,
            'InvRojo': rojoinventariofinal12,
            'VentaPerdidaAzul': ventasperdidas12,
            'VentaPerdidaRojo': rojoventasperdidas12,
            'AlmacenamientoAzul': inventariofinal12 * 5,
            'AlmacenamientoRojo': rojoinventariofinal12 * 5,
            'CostoPerdidasAzul': ventasperdidas12 * 10,
            'CostoPerdidasRojo': rojoventasperdidas12 * 10,
            'SetupAzul': setup12,
            'SetupRojo': rojosetup12,
            'TotalesAzul': inventariofinal12 * 5 + ventasperdidas12 * 10 + setup12,
            'TotalesRojo': rojoinventariofinal12 * 5 + rojoventasperdidas12 * 10 + rojosetup12,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,
            'inventario9': inventariofinal8,
            'inventario10': inventariofinal9,           
            'inventario11': inventariofinal10,
            'inventario12': inventariofinal11,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            'Rojoinventario9': rojoinventariofinal8,
            'Rojoinventario10': rojoinventariofinal9,
            'Rojoinventario11': rojoinventariofinal10,
            'Rojoinventario12': rojoinventariofinal11,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * 5,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * 5,
            'costoventasperdidas8': ventasperdidas8 * 10,
            'rojocostoventasperdidas8': rojoventasperdidas8 * 10,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'rojototales8': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * 5,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * 5,
            'costoventasperdidas9': ventasperdidas9 * 10,
            'rojocostoventasperdidas9': rojoventasperdidas9 * 10,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * 5 + ventasperdidas9 * 10 + setup9,
            'rojototales9': rojoinventariofinal9 * 5 + rojoventasperdidas9 * 10 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * 5,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * 5,
            'costoventasperdidas10': ventasperdidas10 * 10,
            'rojocostoventasperdidas10': rojoventasperdidas10 * 10,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * 5 + ventasperdidas10 * 10 + setup10,
            'rojototales10': rojoinventariofinal10 * 5 + rojoventasperdidas10 * 10 + rojosetup4,

            'ventasperdidas11': ventasperdidas11,
            'rojoventasperdidas11': rojoventasperdidas11,
            'costoalmacenamiento11': inventariofinal11 * 5,
            'rojocostoalmacenamiento11': rojoinventariofinal11 * 5,
            'costoventasperdidas11': ventasperdidas11 * 10,
            'rojocostoventasperdidas11': rojoventasperdidas11 * 10,
            'setup11': setup11,
            'rojosetup11': rojosetup11,
            'totales11': inventariofinal11 * 5 + ventasperdidas11 * 10 + setup11,
            'rojototales11': rojoinventariofinal11 * 5 + rojoventasperdidas11 * 10 + rojosetup11,
        }

#Costos totales

class ResumenLima(Page):
    def vars_for_template(self):
        return{
            'TotalTotales': TotalTotalesLima,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,
            'inventario9': inventariofinal8,
            'inventario10': inventariofinal9,           
            'inventario11': inventariofinal10,
            'inventario12': inventariofinal11,
            'inventario12final': inventariofinal12,            
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            'Rojoinventario9': rojoinventariofinal8,
            'Rojoinventario10': rojoinventariofinal9,
            'Rojoinventario11': rojoinventariofinal10,
            'Rojoinventario12': rojoinventariofinal11,
            'Rojoinventario12final': rojoinventariofinal12,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * 5,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * 5,
            'costoventasperdidas8': ventasperdidas8 * 10,
            'rojocostoventasperdidas8': rojoventasperdidas8 * 10,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'rojototales8': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * 5,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * 5,
            'costoventasperdidas9': ventasperdidas9 * 10,
            'rojocostoventasperdidas9': rojoventasperdidas9 * 10,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * 5 + ventasperdidas9 * 10 + setup9,
            'rojototales9': rojoinventariofinal9 * 5 + rojoventasperdidas9 * 10 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * 5,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * 5,
            'costoventasperdidas10': ventasperdidas10 * 10,
            'rojocostoventasperdidas10': rojoventasperdidas10 * 10,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * 5 + ventasperdidas10 * 10 + setup10,
            'rojototales10': rojoinventariofinal10 * 5 + rojoventasperdidas10 * 10 + rojosetup4,

            'ventasperdidas11': ventasperdidas11,
            'rojoventasperdidas11': rojoventasperdidas11,
            'costoalmacenamiento11': inventariofinal11 * 5,
            'rojocostoalmacenamiento11': rojoinventariofinal11 * 5,
            'costoventasperdidas11': ventasperdidas11 * 10,
            'rojocostoventasperdidas11': rojoventasperdidas11 * 10,
            'setup11': setup11,
            'rojosetup11': rojosetup11,
            'totales11': inventariofinal11 * 5 + ventasperdidas11 * 10 + setup11,
            'rojototales11': rojoinventariofinal11 * 5 + rojoventasperdidas11 * 10 + rojosetup11,

            'ventasperdidas12': ventasperdidas12,
            'rojoventasperdidas12': rojoventasperdidas12,
            'costoalmacenamiento12': inventariofinal12 * 5,
            'rojocostoalmacenamiento12': rojoinventariofinal12 * 5,
            'costoventasperdidas12': ventasperdidas12 * 10,
            'rojocostoventasperdidas12': rojoventasperdidas12 * 10,
            'setup12': setup12,
            'rojosetup12': rojosetup12,
            'totales12': inventariofinal12 * 5 + ventasperdidas12 * 10 + setup12,
            'rojototales12': rojoinventariofinal12 * 5 + rojoventasperdidas12 * 10 + rojosetup12,
        }


class InicioJapon (Page):
    pass

class Japon1(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon1','RojoProduccionJapon1']

    def before_next_page(self):
        global inventariofinal2, rojoinventariofinal2, ventasperdidas2, rojoventasperdidas2, setup2, rojosetup2
        inventariofinal2 = 0
        rojoinventariofinal2 = 0
        ventasperdidas2 = 0
        rojoventasperdidas2 = 0
        setup2 = 0
        rojosetup2 = 0
    pass

    def error_message(self, values):
        global inventariofinal1, rojoinventariofinal1, ventasperdidas1, rojoventasperdidas1, setup1, rojosetup1

        inventariofinal1 = max(values['ProduccionJapon1']+Constants.inventario_inicial2-Constants.JaponDemanda1, 0)
        rojoinventariofinal1 = max(values['RojoProduccionJapon1']+Constants.inventario_inicialR2-Constants.rojoJaponDemanda1, 0)
        ventasperdidas1 = max(Constants.JaponDemanda1-values['ProduccionJapon1']-Constants.inventario_inicial2, 0)
        rojoventasperdidas1 = max(Constants.rojoJaponDemanda1-values['RojoProduccionJapon1']-Constants.inventario_inicialR2, 0)

        if values["ProduccionJapon1"]>0:
            setup1=1500
        else:
            setup1=0

        if values["RojoProduccionJapon1"]>0:
            rojosetup1=1500
        else:
            rojosetup1=0

        if values["ProduccionJapon1"] + values["RojoProduccionJapon1"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal1,
            'InvRojo': rojoinventariofinal1,
            'VentaPerdidaAzul': ventasperdidas1,
            'VentaPerdidaRojo': rojoventasperdidas1,
            'AlmacenamientoAzul': inventariofinal1 * 5,
            'AlmacenamientoRojo': rojoinventariofinal1 * 5,
            'CostoPerdidasAzul': ventasperdidas1 * 10,
            'CostoPerdidasRojo': rojoventasperdidas1 * 10,
            'SetupAzul': setup1,
            'SetupRojo': rojosetup1,
            'TotalesAzul': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'TotalesRojo': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,
        }


class Japon2(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon2','RojoProduccionJapon2']
    def before_next_page(self):
        global inventariofinal3, rojoinventariofinal3, ventasperdidas3, rojoventasperdidas3, setup3, rojosetup3
        inventariofinal3 = 0
        rojoinventariofinal3 = 0
        ventasperdidas3 = 0
        rojoventasperdidas3 = 0
        setup3 = 0
        rojosetup3 = 0
    pass

    def error_message(self, values):
        global inventariofinal2,rojoinventariofinal2,ventasperdidas2,rojoventasperdidas2,setup2,rojosetup2

        inventariofinal2 = max(values['ProduccionJapon2'] + inventariofinal1 - Constants.JaponDemanda2, 0)
        rojoinventariofinal2 = max(values['RojoProduccionJapon2'] + rojoinventariofinal1 - Constants.rojoJaponDemanda2, 0)
        ventasperdidas2 = max(Constants.JaponDemanda2 - values['ProduccionJapon2'] - inventariofinal1, 0)
        rojoventasperdidas2 = max(Constants.rojoJaponDemanda2 - values['RojoProduccionJapon2'] - rojoinventariofinal1, 0)

        if values["ProduccionJapon2"] > 0:
            setup2 = 1500
        else:
            setup2 = 0

        if values["RojoProduccionJapon2"] > 0:
            rojosetup2 = 1500
        else:
            rojosetup2 = 0

        if values["ProduccionJapon2"] + values["RojoProduccionJapon2"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal2,
            'InvRojo': rojoinventariofinal2,
            'VentaPerdidaAzul': ventasperdidas2,
            'VentaPerdidaRojo': rojoventasperdidas2,
            'AlmacenamientoAzul': inventariofinal2 * 5,
            'AlmacenamientoRojo': rojoinventariofinal2 * 5,
            'CostoPerdidasAzul': ventasperdidas2 * 10,
            'CostoPerdidasRojo': rojoventasperdidas2 * 10,
            'SetupAzul': setup2,
            'SetupRojo': rojosetup2,
            'TotalesAzul': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'TotalesRojo': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'inventario2': inventariofinal1,
            'Rojoinventario2': rojoinventariofinal1,
            
            'ventasperdidas1':ventasperdidas1,
            'rojoventasperdidas1':rojoventasperdidas1,
            'costoalmacenamiento1':inventariofinal1*5,
            'rojocostoalmacenamiento1':rojoinventariofinal1*5,
            'costoventasperdidas1':ventasperdidas1*10,
            'rojocostoventasperdidas1':rojoventasperdidas1*10,
            'setup1':setup1,
            'rojosetup1':rojosetup1,
            'totales1':inventariofinal1*5+ventasperdidas1*10+setup1,
            'rojototales1':rojoinventariofinal1*5+rojoventasperdidas1*10+rojosetup1
        }


class Japon3(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon3','RojoProduccionJapon3']
    def before_next_page(self):
        global inventariofinal4, rojoinventariofinal4, ventasperdidas4, rojoventasperdidas4, setup4, rojosetup4
        inventariofinal4 = 0
        rojoinventariofinal4 = 0
        ventasperdidas4 = 0
        rojoventasperdidas4 = 0
        setup4 = 0
        rojosetup4 = 0
    pass

    def error_message(self, values):
        global inventariofinal3, rojoinventariofinal3, ventasperdidas3, rojoventasperdidas3,setup3,rojosetup3

        inventariofinal3 = max(values['ProduccionJapon3'] + inventariofinal2 - Constants.JaponDemanda3, 0)
        rojoinventariofinal3 = max(values['RojoProduccionJapon3'] + rojoinventariofinal2 - Constants.rojoJaponDemanda3, 0)
        ventasperdidas3 = max(Constants.JaponDemanda3 - values['ProduccionJapon3'] - inventariofinal2, 0)
        rojoventasperdidas3 = max(Constants.rojoJaponDemanda3 - values['RojoProduccionJapon3'] - rojoinventariofinal2, 0)

        if values["ProduccionJapon3"] > 0:
            setup3 = 1500
        else:
            setup3 = 0

        if values["RojoProduccionJapon3"] > 0:
            rojosetup3 = 1500
        else:
            rojosetup3 = 0

        if values["ProduccionJapon3"] + values["RojoProduccionJapon3"] > 1500:
            return ' La produccion no debe pasar de 1500'


    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal3,
            'InvRojo': rojoinventariofinal3,
            'VentaPerdidaAzul': ventasperdidas3,
            'VentaPerdidaRojo': rojoventasperdidas3,
            'AlmacenamientoAzul': inventariofinal3 * 5,
            'AlmacenamientoRojo': rojoinventariofinal3 * 5,
            'CostoPerdidasAzul': ventasperdidas3 * 10,
            'CostoPerdidasRojo': rojoventasperdidas3 * 10,
            'SetupAzul': setup3,
            'SetupRojo': rojosetup3,
            'TotalesAzul': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'TotalesRojo': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            
            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

        }

class Japon4(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon4','RojoProduccionJapon4']
    def before_next_page(self):
        global inventariofinal5, rojoinventariofinal5, ventasperdidas5, rojoventasperdidas5, setup5, rojosetup5
        inventariofinal5 = 0
        rojoinventariofinal5 = 0
        ventasperdidas5 = 0
        rojoventasperdidas5 = 0
        setup5 = 0
        rojosetup5 = 0
    pass


    def error_message(self, values):
        global inventariofinal4, rojoinventariofinal4, ventasperdidas4, rojoventasperdidas4,setup4,rojosetup4

        inventariofinal4 = max(values['ProduccionJapon4'] + inventariofinal3 - Constants.JaponDemanda4, 0)
        rojoinventariofinal4 = max(values['RojoProduccionJapon4'] + rojoinventariofinal3 - Constants.rojoJaponDemanda4, 0)
        ventasperdidas4 = max(Constants.JaponDemanda4 - values['ProduccionJapon4'] - inventariofinal3, 0)
        rojoventasperdidas4 = max(Constants.rojoJaponDemanda4 - values['RojoProduccionJapon4'] - rojoinventariofinal3, 0)

        if values["ProduccionJapon4"] > 0:
            setup4 = 1500
        else:
            setup4 = 0

        if values["RojoProduccionJapon4"] > 0:
            rojosetup4 = 1500
        else:
            rojosetup4 = 0

        if values["ProduccionJapon4"] + values["RojoProduccionJapon4"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal4,
            'InvRojo': rojoinventariofinal4,
            'VentaPerdidaAzul': ventasperdidas4,
            'VentaPerdidaRojo': rojoventasperdidas4,
            'AlmacenamientoAzul': inventariofinal4 * 5,
            'AlmacenamientoRojo': rojoinventariofinal4 * 5,
            'CostoPerdidasAzul': ventasperdidas4 * 10,
            'CostoPerdidasRojo': rojoventasperdidas4 * 10,
            'SetupAzul': setup4,
            'SetupRojo': rojosetup4,
            'TotalesAzul': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'TotalesRojo': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,
        }

class Japon5(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon5','RojoProduccionJapon5']
    def before_next_page(self):
        global inventariofinal6, rojoinventariofinal6, ventasperdidas6, rojoventasperdidas6, setup6, rojosetup6
        inventariofinal6 = 0
        rojoinventariofinal6 = 0
        ventasperdidas6 = 0
        rojoventasperdidas6 = 0
        setup6 = 0
        rojosetup6 = 0
    pass

    def error_message(self, values):
        global inventariofinal5, rojoinventariofinal5, ventasperdidas5, rojoventasperdidas5,setup5,rojosetup5

        inventariofinal5 = max(values['ProduccionJapon5'] + inventariofinal4 - Constants.JaponDemanda5, 0)
        rojoinventariofinal5 = max(values['RojoProduccionJapon5'] + rojoinventariofinal4 - Constants.rojoJaponDemanda5, 0)
        ventasperdidas5 = max(Constants.JaponDemanda5 - values['ProduccionJapon5'] - inventariofinal4, 0)
        rojoventasperdidas5 = max(Constants.rojoJaponDemanda5 - values['RojoProduccionJapon5'] - rojoinventariofinal4, 0)

        if values["ProduccionJapon5"] > 0:
            setup5 = 1500
        else:
            setup5 = 0

        if values["RojoProduccionJapon5"] > 0:
            rojosetup5 = 1500
        else:
            rojosetup5 = 0

        if values["ProduccionJapon5"] + values["RojoProduccionJapon5"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):

        return{
            'InvAzul': inventariofinal5,
            'InvRojo': rojoinventariofinal5,
            'VentaPerdidaAzul': ventasperdidas5,
            'VentaPerdidaRojo': rojoventasperdidas5,
            'AlmacenamientoAzul': inventariofinal5 * 5,
            'AlmacenamientoRojo': rojoinventariofinal5 * 5,
            'CostoPerdidasAzul': ventasperdidas5 * 10,
            'CostoPerdidasRojo': rojoventasperdidas5 * 10,
            'SetupAzul': setup5,
            'SetupRojo': rojosetup5,
            'TotalesAzul': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'TotalesRojo': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,
        }

class Japon6(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon6','RojoProduccionJapon6']
    def before_next_page(self):
        global inventariofinal7, rojoinventariofinal7, ventasperdidas7, rojoventasperdidas7, setup7, rojosetup7
        inventariofinal7 = 0
        rojoinventariofinal7 = 0
        ventasperdidas7 = 0
        rojoventasperdidas7 = 0
        setup7 = 0
        rojosetup7 = 0
    pass

    def error_message(self, values):
        global inventariofinal6, rojoinventariofinal6, ventasperdidas6, rojoventasperdidas6,setup6,rojosetup6

        if values["ProduccionJapon6"] + values["RojoProduccionJapon6"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal6 = max(values['ProduccionJapon6'] + inventariofinal5 - Constants.JaponDemanda6, 0)
        rojoinventariofinal6 = max(values['RojoProduccionJapon6'] + rojoinventariofinal5 - Constants.rojoJaponDemanda6, 0)
        ventasperdidas6 = max(Constants.JaponDemanda6 - values['ProduccionJapon6'] - inventariofinal5, 0)
        rojoventasperdidas6 = max(Constants.rojoJaponDemanda6 - values['RojoProduccionJapon6'] - rojoinventariofinal5, 0)

        if values["ProduccionJapon6"] > 0:
            setup6 = 1500
        else:
            setup6 = 0

        if values["RojoProduccionJapon6"] > 0:
            rojosetup6 = 1500
        else:
            rojosetup6= 0

        global TotalinventarioJapon, TotalsetupJapon, TotalventasJapon, TotalTotalesJapon

        TotalinventarioJapon = (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6) * 5
        TotalinventarioJapon = TotalinventarioJapon + (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6) * 5
        TotalsetupJapon = setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6
        TotalventasJapon = (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6) * 10
        TotalventasJapon = TotalventasJapon + (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6) * 10
        TotalTotalesJapon = TotalinventarioJapon + TotalventasJapon + TotalsetupJapon

        if values["ProduccionJapon6"] + values["RojoProduccionJapon6"] > 1500:
            return 'La produccion no debe pasar de 1500'

    def vars_for_template(self):

        return{
            'InvAzul': inventariofinal6,
            'InvRojo': rojoinventariofinal6,
            'VentaPerdidaAzul': ventasperdidas6,
            'VentaPerdidaRojo': rojoventasperdidas6,
            'AlmacenamientoAzul': inventariofinal6 * 5,
            'AlmacenamientoRojo': rojoinventariofinal6 * 5,
            'CostoPerdidasAzul': ventasperdidas6 * 10,
            'CostoPerdidasRojo': rojoventasperdidas6 * 10,
            'SetupAzul': setup6,
            'SetupRojo': rojosetup6,
            'TotalesAzul': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'TotalesRojo': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,


            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,
        }

class Japon7(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon7', 'RojoProduccionJapon7']
    def before_next_page(self):
        global inventariofinal8, rojoinventariofinal8, ventasperdidas8, rojoventasperdidas8, setup8, rojosetup8
        inventariofinal8 = 0
        rojoinventariofinal8 = 0
        ventasperdidas8 = 0
        rojoventasperdidas8 = 0
        setup8 = 0
        rojosetup8 = 0
    pass

    def error_message(self, values):
        global inventariofinal7, rojoinventariofinal7, ventasperdidas7, rojoventasperdidas7, setup7, rojosetup7

        inventariofinal7 = max(values['ProduccionJapon7'] + inventariofinal6 - Constants.JaponDemanda7, 0)
        rojoinventariofinal7 = max(values['RojoProduccionJapon7'] + rojoinventariofinal6 - Constants.rojoJaponDemanda7, 0)
        ventasperdidas7 = max(Constants.JaponDemanda7 - values['ProduccionJapon7'] - inventariofinal6, 0)
        rojoventasperdidas7 = max(Constants.rojoJaponDemanda7 - values['RojoProduccionJapon7'] - rojoinventariofinal6, 0)

        if values["ProduccionJapon7"] > 0:
            setup7 = 1500
        else:
            setup7 = 0

        if values["RojoProduccionJapon7"] > 0:
            rojosetup7 = 1500
        else:
            rojosetup7 = 0

        if values["ProduccionJapon7"] + values["RojoProduccionJapon7"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal7,
            'InvRojo': rojoinventariofinal7,
            'VentaPerdidaAzul': ventasperdidas7,
            'VentaPerdidaRojo': rojoventasperdidas7,
            'AlmacenamientoAzul': inventariofinal7 * 5,
            'AlmacenamientoRojo': rojoinventariofinal7 * 5,
            'CostoPerdidasAzul': ventasperdidas7 * 10,
            'CostoPerdidasRojo': rojoventasperdidas7 * 10,
            'SetupAzul': setup7,
            'SetupRojo': rojosetup7,
            'TotalesAzul': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'TotalesRojo': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,
        }


class Japon8(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon8', 'RojoProduccionJapon8']
    def before_next_page(self):
        global inventariofinal9, rojoinventariofinal9, ventasperdidas9, rojoventasperdidas9, setup9, rojosetup9
        inventariofinal9 = 0
        rojoinventariofinal9 = 0
        ventasperdidas9 = 0
        rojoventasperdidas9 = 0
        setup9 = 0
        rojosetup9 = 0
    pass

    def error_message(self, values):
        global inventariofinal8, rojoinventariofinal8, ventasperdidas8, rojoventasperdidas8, setup8, rojosetup8

        inventariofinal8 = max(values['ProduccionJapon8'] + inventariofinal7 - Constants.JaponDemanda8, 0)
        rojoinventariofinal8 = max(values['RojoProduccionJapon8'] + rojoinventariofinal7 - Constants.rojoJaponDemanda8, 0)
        ventasperdidas8 = max(Constants.JaponDemanda8 - values['ProduccionJapon8'] - inventariofinal7, 0)
        rojoventasperdidas8 = max(Constants.rojoJaponDemanda8 - values['RojoProduccionJapon8'] - rojoinventariofinal7, 0)

        if values["ProduccionJapon8"] > 0:
            setup8 = 1500
        else:
            setup8 = 0

        if values["RojoProduccionJapon8"] > 0:
            rojosetup8 = 1500
        else:
            rojosetup8 = 0

        if values["ProduccionJapon8"] + values["RojoProduccionJapon8"] > 1500:
            return ' La produccion no debe pasar de 1500'


    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal8,
            'InvRojo': rojoinventariofinal8,
            'VentaPerdidaAzul': ventasperdidas8,
            'VentaPerdidaRojo': rojoventasperdidas8,
            'AlmacenamientoAzul': inventariofinal8 * 5,
            'AlmacenamientoRojo': rojoinventariofinal8 * 5,
            'CostoPerdidasAzul': ventasperdidas8 * 10,
            'CostoPerdidasRojo': rojoventasperdidas8 * 10,
            'SetupAzul': setup8,
            'SetupRojo': rojosetup8,
            'TotalesAzul': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'TotalesRojo': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,            
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            
            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,
        }

class Japon9(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon9', 'RojoProduccionJapon9']
    def before_next_page(self):
        global inventariofinal10, rojoinventariofinal10, ventasperdidas10, rojoventasperdidas10, setup10, rojosetup10
        inventariofinal10 = 0
        rojoinventariofinal10 = 0
        ventasperdidas10 = 0
        rojoventasperdidas10 = 0
        setup10 = 0
        rojosetup10 = 0
    pass

    def error_message(self, values):
        global inventariofinal9, rojoinventariofinal9, ventasperdidas9, rojoventasperdidas9, setup9, rojosetup9

        inventariofinal9 = max(values['ProduccionJapon9'] + inventariofinal8 - Constants.JaponDemanda9, 0)
        rojoinventariofinal9 = max(values['RojoProduccionJapon9'] + rojoinventariofinal8 - Constants.rojoJaponDemanda9, 0)
        ventasperdidas9 = max(Constants.JaponDemanda9 - values['ProduccionJapon9'] - inventariofinal8, 0)
        rojoventasperdidas9 = max(Constants.rojoJaponDemanda9 - values['RojoProduccionJapon9'] - rojoinventariofinal8, 0)

        if values["ProduccionJapon9"] > 0:
            setup9 = 1500
        else:
            setup9 = 0

        if values["RojoProduccionJapon9"] > 0:
            rojosetup9 = 1500
        else:
            rojosetup9 = 0

        if values["ProduccionJapon9"] + values["RojoProduccionJapon9"] > 1500:
            return ' La produccion no debe pasar de 1500'


    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal9,
            'InvRojo': rojoinventariofinal9,
            'VentaPerdidaAzul': ventasperdidas9,
            'VentaPerdidaRojo': rojoventasperdidas9,
            'AlmacenamientoAzul': inventariofinal9 * 5,
            'AlmacenamientoRojo': rojoinventariofinal9 * 5,
            'CostoPerdidasAzul': ventasperdidas9 * 10,
            'CostoPerdidasRojo': rojoventasperdidas9 * 10,
            'SetupAzul': setup9,
            'SetupRojo': rojosetup9,
            'TotalesAzul': inventariofinal9 * 5 + ventasperdidas9 * 10 + setup9,
            'TotalesRojo': rojoinventariofinal9 * 5 + rojoventasperdidas9 * 10 + rojosetup9,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,
            'inventario9': inventariofinal8,            
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            'Rojoinventario9': rojoinventariofinal8,
            
            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * 5,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * 5,
            'costoventasperdidas8': ventasperdidas8 * 10,
            'rojocostoventasperdidas8': rojoventasperdidas8 * 10,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'rojototales8': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

        }


class Japon10(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon10', 'RojoProduccionJapon10']
    def before_next_page(self):
        global inventariofinal11, rojoinventariofinal11, ventasperdidas11, rojoventasperdidas11, setup11, rojosetup11
        inventariofinal11 = 0
        rojoinventariofinal11 = 0
        ventasperdidas11 = 0
        rojoventasperdidas11 = 0
        setup11 = 0
        rojosetup11 = 0
    pass

    def error_message(self, values):
        global inventariofinal10, rojoinventariofinal10, ventasperdidas10, rojoventasperdidas10, setup10, rojosetup10
      
        inventariofinal10 = max(values['ProduccionJapon10'] + inventariofinal9 - Constants.JaponDemanda10, 0)
        rojoinventariofinal10 = max(values['RojoProduccionJapon10'] + rojoinventariofinal9 - Constants.rojoJaponDemanda10, 0)
        ventasperdidas10 = max(Constants.JaponDemanda10 - values['ProduccionJapon10'] - inventariofinal9, 0)
        rojoventasperdidas10 = max(Constants.rojoJaponDemanda10 - values['RojoProduccionJapon10'] - rojoinventariofinal9, 0)

        if values["ProduccionJapon10"] > 0:
            setup10 = 1500
        else:
            setup10 = 0

        if values["RojoProduccionJapon10"] > 0:
            rojosetup10 = 1500
        else:
            rojosetup10 = 0

        if values["ProduccionJapon10"] + values["RojoProduccionJapon10"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal10,
            'InvRojo': rojoinventariofinal10,
            'VentaPerdidaAzul': ventasperdidas10,
            'VentaPerdidaRojo': rojoventasperdidas10,
            'AlmacenamientoAzul': inventariofinal10 * 5,
            'AlmacenamientoRojo': rojoinventariofinal10 * 5,
            'CostoPerdidasAzul': ventasperdidas10 * 10,
            'CostoPerdidasRojo': rojoventasperdidas10 * 10,
            'SetupAzul': setup10,
            'SetupRojo': rojosetup10,
            'TotalesAzul': inventariofinal10 * 5 + ventasperdidas10 * 10 + setup10,
            'TotalesRojo': rojoinventariofinal10 * 5 + rojoventasperdidas10 * 10 + rojosetup10,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,
            'inventario9': inventariofinal8,
            'inventario10': inventariofinal9,                      
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            'Rojoinventario9': rojoinventariofinal8,
            'Rojoinventario10': rojoinventariofinal9,
            
            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * 5,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * 5,
            'costoventasperdidas8': ventasperdidas8 * 10,
            'rojocostoventasperdidas8': rojoventasperdidas8 * 10,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'rojototales8': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * 5,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * 5,
            'costoventasperdidas9': ventasperdidas9 * 10,
            'rojocostoventasperdidas9': rojoventasperdidas9 * 10,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * 5 + ventasperdidas9 * 10 + setup9,
            'rojototales9': rojoinventariofinal9 * 5 + rojoventasperdidas9 * 10 + rojosetup9,
        }


class Japon11(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon11', 'RojoProduccionJapon11']
    def before_next_page(self):
        global inventariofinal12, rojoinventariofinal12, ventasperdidas12, rojoventasperdidas12, setup12, rojosetup12
        inventariofinal12 = 0
        rojoinventariofinal12 = 0
        ventasperdidas12 = 0
        rojoventasperdidas12 = 0
        setup12 = 0
        rojosetup12 = 0
    pass

    def error_message(self, values):
        global inventariofinal11, rojoinventariofinal11, ventasperdidas11, rojoventasperdidas11, setup11, rojosetup11
    
        inventariofinal11 = max(values['ProduccionJapon11'] + inventariofinal10 - Constants.JaponDemanda11, 0)
        rojoinventariofinal11 = max(values['RojoProduccionJapon11'] + rojoinventariofinal10 - Constants.rojoJaponDemanda11, 0)
        ventasperdidas11 = max(Constants.JaponDemanda11 - values['ProduccionJapon11'] - inventariofinal10, 0)
        rojoventasperdidas11 = max(Constants.rojoJaponDemanda11 - values['RojoProduccionJapon11'] - rojoinventariofinal10, 0)

        if values["ProduccionJapon11"] > 0:
            setup11 = 1500
        else:
            setup11 = 0

        if values["RojoProduccionJapon11"] > 0:
            rojosetup11 = 1500
        else:
            rojosetup11 = 0

        if values["ProduccionJapon11"] + values["RojoProduccionJapon11"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):

        return {
            'InvAzul': inventariofinal11,
            'InvRojo': rojoinventariofinal11,
            'VentaPerdidaAzul': ventasperdidas11,
            'VentaPerdidaRojo': rojoventasperdidas11,
            'AlmacenamientoAzul': inventariofinal11 * 5,
            'AlmacenamientoRojo': rojoinventariofinal11 * 5,
            'CostoPerdidasAzul': ventasperdidas11 * 10,
            'CostoPerdidasRojo': rojoventasperdidas11 * 10,
            'SetupAzul': setup11,
            'SetupRojo': rojosetup11,
            'TotalesAzul': inventariofinal11 * 5 + ventasperdidas11 * 10 + setup11,
            'TotalesRojo': rojoinventariofinal11 * 5 + rojoventasperdidas11 * 10 + rojosetup11,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,
            'inventario9': inventariofinal8,
            'inventario10': inventariofinal9,           
            'inventario11': inventariofinal10,                      
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            'Rojoinventario9': rojoinventariofinal8,
            'Rojoinventario10': rojoinventariofinal9,
            'Rojoinventario11': rojoinventariofinal10,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * 5,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * 5,
            'costoventasperdidas8': ventasperdidas8 * 10,
            'rojocostoventasperdidas8': rojoventasperdidas8 * 10,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'rojototales8': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * 5,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * 5,
            'costoventasperdidas9': ventasperdidas9 * 10,
            'rojocostoventasperdidas9': rojoventasperdidas9 * 10,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * 5 + ventasperdidas9 * 10 + setup9,
            'rojototales9': rojoinventariofinal9 * 5 + rojoventasperdidas9 * 10 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * 5,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * 5,
            'costoventasperdidas10': ventasperdidas10 * 10,
            'rojocostoventasperdidas10': rojoventasperdidas10 * 10,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * 5 + ventasperdidas10 * 10 + setup10,
            'rojototales10': rojoinventariofinal10 * 5 + rojoventasperdidas10 * 10 + rojosetup10,
        }


class Japon12(Page):
    form_model = 'player'
    form_fields = ['ProduccionJapon12', 'RojoProduccionJapon12']
    def before_next_page(self):
        global inventariofinal1, rojoinventariofinal1, ventasperdidas1, rojoventasperdidas1, setup1, rojosetup1
        inventariofinal1 = 0
        rojoinventariofinal1 = 0
        ventasperdidas1 = 0
        rojoventasperdidas1 = 0
        setup1 = 0
        rojosetup1 = 0
    pass

    def error_message(self, values):

        global inventariofinal12, rojoinventariofinal12, ventasperdidas12, rojoventasperdidas12, setup12, rojosetup12
        global TotalinventarioJapon, TotalsetupJapon, TotalventasJapon, TotalTotalesJapon

        inventariofinal12 = max(values['ProduccionJapon12'] + inventariofinal11 - Constants.JaponDemanda12, 0)
        rojoinventariofinal12 = max(values['RojoProduccionJapon12'] + rojoinventariofinal11 - Constants.rojoJaponDemanda12, 0)
        ventasperdidas12 = max(Constants.JaponDemanda12 - values['ProduccionJapon12'] - inventariofinal11, 0)
        rojoventasperdidas12 = max(Constants.rojoJaponDemanda12 - values['RojoProduccionJapon12'] - rojoinventariofinal11, 0)

        if values["ProduccionJapon12"] > 0:
            setup12 = 1500
        else:
            setup12 = 0

        if values["RojoProduccionJapon12"] > 0:
            rojosetup12 = 1500
        else:
            rojosetup12 = 0

        TotalinventarioJapon = (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6 + inventariofinal7 + inventariofinal8 + inventariofinal9 + inventariofinal10 + inventariofinal11 + inventariofinal12) * 5
        TotalinventarioJapon = (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6 + rojoinventariofinal7 + rojoinventariofinal8 + rojoinventariofinal9 + rojoinventariofinal10 + rojoinventariofinal11 + rojoinventariofinal12) * 5
        TotalsetupJapon = setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + setup7 + setup8 + setup9 + setup10 + setup11 + setup12 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6 + rojosetup7 + rojosetup8 + rojosetup9 + rojosetup10 + rojosetup11 + rojosetup12
        TotalventasJapon = (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6 + ventasperdidas7 + ventasperdidas8 + ventasperdidas9 + ventasperdidas10 + ventasperdidas11 + ventasperdidas12) * 10
        TotalventasJapon = (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6 + rojoventasperdidas7 + rojoventasperdidas8 + rojoventasperdidas9 + rojoventasperdidas10 + rojoventasperdidas11 + rojoventasperdidas12) * 10
        TotalTotalesJapon = TotalinventarioJapon + TotalventasJapon + TotalsetupJapon

        if values["ProduccionJapon12"] + values["RojoProduccionJapon12"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal12,
            'InvRojo': rojoinventariofinal12,
            'VentaPerdidaAzul': ventasperdidas12,
            'VentaPerdidaRojo': rojoventasperdidas12,
            'AlmacenamientoAzul': inventariofinal12 * 5,
            'AlmacenamientoRojo': rojoinventariofinal12 * 5,
            'CostoPerdidasAzul': ventasperdidas12 * 10,
            'CostoPerdidasRojo': rojoventasperdidas12 * 10,
            'SetupAzul': setup12,
            'SetupRojo': rojosetup12,
            'TotalesAzul': inventariofinal12 * 5 + ventasperdidas12 * 10 + setup12,
            'TotalesRojo': rojoinventariofinal12 * 5 + rojoventasperdidas12 * 10 + rojosetup12,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,
            'inventario9': inventariofinal8,
            'inventario10': inventariofinal9,           
            'inventario11': inventariofinal10,
            'inventario12': inventariofinal11,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            'Rojoinventario9': rojoinventariofinal8,
            'Rojoinventario10': rojoinventariofinal9,
            'Rojoinventario11': rojoinventariofinal10,
            'Rojoinventario12': rojoinventariofinal11,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * 5,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * 5,
            'costoventasperdidas8': ventasperdidas8 * 10,
            'rojocostoventasperdidas8': rojoventasperdidas8 * 10,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'rojototales8': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * 5,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * 5,
            'costoventasperdidas9': ventasperdidas9 * 10,
            'rojocostoventasperdidas9': rojoventasperdidas9 * 10,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * 5 + ventasperdidas9 * 10 + setup9,
            'rojototales9': rojoinventariofinal9 * 5 + rojoventasperdidas9 * 10 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * 5,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * 5,
            'costoventasperdidas10': ventasperdidas10 * 10,
            'rojocostoventasperdidas10': rojoventasperdidas10 * 10,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * 5 + ventasperdidas10 * 10 + setup10,
            'rojototales10': rojoinventariofinal10 * 5 + rojoventasperdidas10 * 10 + rojosetup4,

            'ventasperdidas11': ventasperdidas11,
            'rojoventasperdidas11': rojoventasperdidas11,
            'costoalmacenamiento11': inventariofinal11 * 5,
            'rojocostoalmacenamiento11': rojoinventariofinal11 * 5,
            'costoventasperdidas11': ventasperdidas11 * 10,
            'rojocostoventasperdidas11': rojoventasperdidas11 * 10,
            'setup11': setup11,
            'rojosetup11': rojosetup11,
            'totales11': inventariofinal11 * 5 + ventasperdidas11 * 10 + setup11,
            'rojototales11': rojoinventariofinal11 * 5 + rojoventasperdidas11 * 10 + rojosetup11,
        }

class ResumenJapon(Page):
    def vars_for_template(self):
        return{
            'TotalTotales': TotalTotalesJapon,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'inventario5': inventariofinal4,
            'inventario6': inventariofinal5,
            'inventario7': inventariofinal6,
            'inventario8': inventariofinal7,
            'inventario9': inventariofinal8,
            'inventario10': inventariofinal9,           
            'inventario11': inventariofinal10,
            'inventario12': inventariofinal11,
            'inventario12final': inventariofinal12,            
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,
            'Rojoinventario5': rojoinventariofinal4,
            'Rojoinventario6': rojoinventariofinal5,
            'Rojoinventario7': rojoinventariofinal6,
            'Rojoinventario8': rojoinventariofinal7,
            'Rojoinventario9': rojoinventariofinal8,
            'Rojoinventario10': rojoinventariofinal9,
            'Rojoinventario11': rojoinventariofinal10,
            'Rojoinventario12': rojoinventariofinal11,
            'Rojoinventario12final': rojoinventariofinal12,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * 5,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * 5,
            'costoventasperdidas1': ventasperdidas1 * 10,
            'rojocostoventasperdidas1': rojoventasperdidas1 * 10,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * 5 + ventasperdidas1 * 10 + setup1,
            'rojototales1': rojoinventariofinal1 * 5 + rojoventasperdidas1 * 10 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * 5,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * 5,
            'costoventasperdidas2': ventasperdidas2 * 10,
            'rojocostoventasperdidas2': rojoventasperdidas2 * 10,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * 5 + ventasperdidas2 * 10 + setup2,
            'rojototales2': rojoinventariofinal2 * 5 + rojoventasperdidas2 * 10 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * 5,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * 5,
            'costoventasperdidas3': ventasperdidas3 * 10,
            'rojocostoventasperdidas3': rojoventasperdidas3 * 10,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * 5 + ventasperdidas3 * 10 + setup3,
            'rojototales3': rojoinventariofinal3 * 5 + rojoventasperdidas3 * 10 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * 5,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * 5,
            'costoventasperdidas4': ventasperdidas4 * 10,
            'rojocostoventasperdidas4': rojoventasperdidas4 * 10,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * 5 + ventasperdidas4 * 10 + setup4,
            'rojototales4': rojoinventariofinal4 * 5 + rojoventasperdidas4 * 10 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * 5,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * 5,
            'costoventasperdidas5': ventasperdidas5 * 10,
            'rojocostoventasperdidas5': rojoventasperdidas5 * 10,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * 5 + ventasperdidas5 * 10 + setup5,
            'rojototales5': rojoinventariofinal5 * 5 + rojoventasperdidas5 * 10 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * 5,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * 5,
            'costoventasperdidas6': ventasperdidas6 * 10,
            'rojocostoventasperdidas6': rojoventasperdidas6 * 10,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * 5 + ventasperdidas6 * 10 + setup6,
            'rojototales6': rojoinventariofinal6 * 5 + rojoventasperdidas6 * 10 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * 5,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * 5,
            'costoventasperdidas7': ventasperdidas7 * 10,
            'rojocostoventasperdidas7': rojoventasperdidas7 * 10,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * 5 + ventasperdidas7 * 10 + setup7,
            'rojototales7': rojoinventariofinal7 * 5 + rojoventasperdidas7 * 10 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * 5,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * 5,
            'costoventasperdidas8': ventasperdidas8 * 10,
            'rojocostoventasperdidas8': rojoventasperdidas8 * 10,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * 5 + ventasperdidas8 * 10 + setup8,
            'rojototales8': rojoinventariofinal8 * 5 + rojoventasperdidas8 * 10 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * 5,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * 5,
            'costoventasperdidas9': ventasperdidas9 * 10,
            'rojocostoventasperdidas9': rojoventasperdidas9 * 10,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * 5 + ventasperdidas9 * 10 + setup9,
            'rojototales9': rojoinventariofinal9 * 5 + rojoventasperdidas9 * 10 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * 5,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * 5,
            'costoventasperdidas10': ventasperdidas10 * 10,
            'rojocostoventasperdidas10': rojoventasperdidas10 * 10,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * 5 + ventasperdidas10 * 10 + setup10,
            'rojototales10': rojoinventariofinal10 * 5 + rojoventasperdidas10 * 10 + rojosetup4,

            'ventasperdidas11': ventasperdidas11,
            'rojoventasperdidas11': rojoventasperdidas11,
            'costoalmacenamiento11': inventariofinal11 * 5,
            'rojocostoalmacenamiento11': rojoinventariofinal11 * 5,
            'costoventasperdidas11': ventasperdidas11 * 10,
            'rojocostoventasperdidas11': rojoventasperdidas11 * 10,
            'setup11': setup11,
            'rojosetup11': rojosetup11,
            'totales11': inventariofinal11 * 5 + ventasperdidas11 * 10 + setup11,
            'rojototales11': rojoinventariofinal11 * 5 + rojoventasperdidas11 * 10 + rojosetup11,

            'ventasperdidas12': ventasperdidas12,
            'rojoventasperdidas12': rojoventasperdidas12,
            'costoalmacenamiento12': inventariofinal12 * 5,
            'rojocostoalmacenamiento12': rojoinventariofinal12 * 5,
            'costoventasperdidas12': ventasperdidas12 * 10,
            'rojocostoventasperdidas12': rojoventasperdidas12 * 10,
            'setup12': setup12,
            'rojosetup12': rojosetup12,
            'totales12': inventariofinal12 * 5 + ventasperdidas12 * 10 + setup12,
            'rojototales12': rojoinventariofinal12 * 5 + rojoventasperdidas12 * 10 + rojosetup12,
        }

class ResumenTotal(Page):
    def vars_for_template(self):
        return{
            'TotalTotales1': TotalTotalesLima,
            'TotalTotales2': TotalTotalesJapon,
            'TotalTotales5': TotalTotalesLima+TotalTotalesJapon
        }

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [
Inicio7LIMA,
    Lima1,
    Lima2,
    Lima3,
    Lima4,
    Lima5,
    Lima6,
    Lima7,
    Lima8,
    Lima9,
    Lima10,
    Lima11,
    Lima12,
    ResumenLima,

InicioJapon,
    Japon1,
    Japon2,
    Japon3,
    Japon4,
    Japon5,
    Japon6,
    Japon7,
    Japon8,
    Japon9,
    Japon10,
    Japon11,
    Japon12,
    ResumenJapon,

    ResumenTotal,
]
