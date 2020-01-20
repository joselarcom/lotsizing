from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import decimal




class MyPage(Page):
    pass
class Inicio1(Page):
    pass
class Inicio2(Page):
    pass
class Inicio3(Page):
    pass
class Inicio4(Page):
    pass
class Inicio6(Page):
    pass

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
            setup1= Constants.SETUP
        else:
            setup1=0

        if values["RojoProduccionLima1"]>0:
            rojosetup1=Constants.SETUP
        else:
            rojosetup1=0

        if values["ProduccionLima1"] + values["RojoProduccionLima1"] > Constants.Capacidad:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return{
            'InvAzul':inventariofinal1,
            'InvRojo':rojoinventariofinal1,
            'VentaPerdidaAzul':ventasperdidas1,
            'VentaPerdidaRojo':rojoventasperdidas1,
            'AlmacenamientoAzul':inventariofinal1*Constants.CostoInventario1,
            'AlmacenamientoRojo':rojoinventariofinal1*Constants.CostoInventario1,
            'CostoPerdidasAzul':ventasperdidas1*Constants.CostoBackorder1,
            'CostoPerdidasRojo':rojoventasperdidas1*Constants.CostoBackorder1,
            'SetupAzul':setup1,
            'SetupRojo':rojosetup1,
            'TotalesAzul':inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'TotalesRojo':rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,
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
            setup2 = Constants.SETUP
        else:
            setup2 = 0

        if values["RojoProduccionLima2"] > 0:
            rojosetup2 = Constants.SETUP
        else:
            rojosetup2 = 0

        if values["ProduccionLima2"] + values["RojoProduccionLima2"] > Constants.Capacidad:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal2,
            'InvRojo': rojoinventariofinal2,
            'VentaPerdidaAzul': ventasperdidas2,
            'VentaPerdidaRojo': rojoventasperdidas2,
            'AlmacenamientoAzul': inventariofinal2 * Constants.CostoInventario1,
            'AlmacenamientoRojo': rojoinventariofinal2 * Constants.CostoInventario1,
            'CostoPerdidasAzul': ventasperdidas2 * Constants.CostoBackorder1,
            'CostoPerdidasRojo': rojoventasperdidas2 * Constants.CostoBackorder1,
            'SetupAzul': setup2,
            'SetupRojo': rojosetup2,
            'TotalesAzul': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'TotalesRojo': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

            'inventario2': inventariofinal1,
            'Rojoinventario2': rojoinventariofinal1,

            'ventasperdidas1':ventasperdidas1,
            'rojoventasperdidas1':rojoventasperdidas1,
            'costoalmacenamiento1':inventariofinal1*Constants.CostoInventario1,
            'rojocostoalmacenamiento1':rojoinventariofinal1*Constants.CostoInventario1,
            'costoventasperdidas1':ventasperdidas1*Constants.CostoBackorder1,
            'rojocostoventasperdidas1':rojoventasperdidas1*Constants.CostoBackorder1,
            'setup1':setup1,
            'rojosetup1':rojosetup1,
            'totales1':inventariofinal1*Constants.CostoInventario1+ventasperdidas1*Constants.CostoBackorder1+setup1,
            'rojototales1':rojoinventariofinal1*Constants.CostoInventario1+rojoventasperdidas1*Constants.CostoBackorder1+rojosetup1
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
            setup3 = Constants.SETUP
        else:
            setup3 = 0

        if values["RojoProduccionLima3"] > 0:
            rojosetup3 = Constants.SETUP
        else:
            rojosetup3 = 0
        
        if values["ProduccionLima3"] + values["RojoProduccionLima3"] > Constants.Capacidad:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal3,
            'InvRojo': rojoinventariofinal3,
            'VentaPerdidaAzul': ventasperdidas3,
            'VentaPerdidaRojo': rojoventasperdidas3,
            'AlmacenamientoAzul': inventariofinal3 * Constants.CostoInventario1,
            'AlmacenamientoRojo': rojoinventariofinal3 * Constants.CostoInventario1,
            'CostoPerdidasAzul': ventasperdidas3 * Constants.CostoBackorder1,
            'CostoPerdidasRojo': rojoventasperdidas3 * Constants.CostoBackorder1,
            'SetupAzul': setup3,
            'SetupRojo': rojosetup3,
            'TotalesAzul': inventariofinal3 * Constants.CostoInventario1 + ventasperdidas3 * Constants.CostoBackorder1 + setup3,
            'TotalesRojo': rojoinventariofinal3 * Constants.CostoInventario1 + rojoventasperdidas3 * Constants.CostoBackorder1 + rojosetup3,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario1,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario1,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder1,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder1,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

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
            setup4 = Constants.SETUP
        else:
            setup4 = 0

        if values["RojoProduccionLima4"] > 0:
            rojosetup4 = Constants.SETUP
        else:
            rojosetup4 = 0

        if values["ProduccionLima4"] + values["RojoProduccionLima4"] > Constants.Capacidad:
            return ' La produccion no debe pasar de la capacidad'


    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal4,
            'InvRojo': rojoinventariofinal4,
            'VentaPerdidaAzul': ventasperdidas4,
            'VentaPerdidaRojo': rojoventasperdidas4,
            'AlmacenamientoAzul': inventariofinal4 * Constants.CostoInventario1,
            'AlmacenamientoRojo': rojoinventariofinal4 * Constants.CostoInventario1,
            'CostoPerdidasAzul': ventasperdidas4 * Constants.CostoBackorder1,
            'CostoPerdidasRojo': rojoventasperdidas4 * Constants.CostoBackorder1,
            'SetupAzul': setup4,
            'SetupRojo': rojosetup4,
            'TotalesAzul': inventariofinal4 * Constants.CostoInventario1 + ventasperdidas4 * Constants.CostoBackorder1 + setup4,
            'TotalesRojo': rojoinventariofinal4 * Constants.CostoInventario1 + rojoventasperdidas4 * Constants.CostoBackorder1 + rojosetup4,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario1,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario1,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder1,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder1,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario1,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario1,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder1,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder1,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario1 + ventasperdidas3 * Constants.CostoBackorder1 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario1 + rojoventasperdidas3 * Constants.CostoBackorder1 + rojosetup3,
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
            setup5 = Constants.SETUP
        else:
            setup5 = 0

        if values["RojoProduccionLima5"] > 0:
            rojosetup5 = Constants.SETUP
        else:
            rojosetup5 = 0

        if values["ProduccionLima5"] + values["RojoProduccionLima5"] > Constants.Capacidad:
            return ' La produccion no debe pasar de la capacidad'


    def vars_for_template(self):

        return{
            'InvAzul': inventariofinal5,
            'InvRojo': rojoinventariofinal5,
            'VentaPerdidaAzul': ventasperdidas5,
            'VentaPerdidaRojo': rojoventasperdidas5,
            'AlmacenamientoAzul': inventariofinal5 * Constants.CostoInventario1,
            'AlmacenamientoRojo': rojoinventariofinal5 * Constants.CostoInventario1,
            'CostoPerdidasAzul': ventasperdidas5 * Constants.CostoBackorder1,
            'CostoPerdidasRojo': rojoventasperdidas5 * Constants.CostoBackorder1,
            'SetupAzul': setup5,
            'SetupRojo': rojosetup5,
            'TotalesAzul': inventariofinal5 * Constants.CostoInventario1 + ventasperdidas5 * Constants.CostoBackorder1 + setup5,
            'TotalesRojo': rojoinventariofinal5 * Constants.CostoInventario1 + rojoventasperdidas5 * Constants.CostoBackorder1 + rojosetup5,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario1,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario1,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder1,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder1,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario1,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario1,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder1,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder1,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario1 + ventasperdidas3 * Constants.CostoBackorder1 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario1 + rojoventasperdidas3 * Constants.CostoBackorder1 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario1,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario1,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder1,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder1,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario1 + ventasperdidas4 * Constants.CostoBackorder1 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario1 + rojoventasperdidas4 * Constants.CostoBackorder1 + rojosetup4,
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
            setup6 = Constants.SETUP
        else:
            setup6 = 0

        if values["RojoProduccionLima6"] > 0:
            rojosetup6 = Constants.SETUP
        else:
            rojosetup6= 0

        global TotalinventarioLima, TotalsetupLima, TotalventasLima, TotalTotalesLima

        TotalinventarioLima = (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6) * Constants.CostoInventario1
        TotalinventarioLima = TotalinventarioLima + (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6) * Constants.CostoInventario1
        TotalsetupLima = setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6
        TotalventasLima = (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6) * Constants.CostoBackorder1
        TotalventasLima = TotalventasLima + (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6) * Constants.CostoBackorder1
        TotalTotalesLima = TotalinventarioLima + TotalventasLima + TotalsetupLima

        if values["ProduccionLima6"] + values["RojoProduccionLima6"] > Constants.Capacidad:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):

        return{
            'InvAzul': inventariofinal6,
            'InvRojo': rojoinventariofinal6,
            'VentaPerdidaAzul': ventasperdidas6,
            'VentaPerdidaRojo': rojoventasperdidas6,
            'AlmacenamientoAzul': inventariofinal6 * Constants.CostoInventario1,
            'AlmacenamientoRojo': rojoinventariofinal6 * Constants.CostoInventario1,
            'CostoPerdidasAzul': ventasperdidas6 * Constants.CostoBackorder1,
            'CostoPerdidasRojo': rojoventasperdidas6 * Constants.CostoBackorder1,
            'SetupAzul': setup6,
            'SetupRojo': rojosetup6,
            'TotalesAzul': inventariofinal6 * Constants.CostoInventario1 + ventasperdidas6 * Constants.CostoBackorder1 + setup6,
            'TotalesRojo': rojoinventariofinal6 * Constants.CostoInventario1 + rojoventasperdidas6 * Constants.CostoBackorder1 + rojosetup6,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario1,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario1,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder1,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder1,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario1,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario1,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder1,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder1,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario1 + ventasperdidas3 * Constants.CostoBackorder1 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario1 + rojoventasperdidas3 * Constants.CostoBackorder1 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario1,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario1,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder1,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder1,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario1 + ventasperdidas4 * Constants.CostoBackorder1 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario1 + rojoventasperdidas4 * Constants.CostoBackorder1 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario1,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario1,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder1,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder1,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario1 + ventasperdidas5 * Constants.CostoBackorder1 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario1 + rojoventasperdidas5 * Constants.CostoBackorder1 + rojosetup5,
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
            setup7 = Constants.SETUP
        else:
            setup7 = 0

        if values["RojoProduccionLima7"] > 0:
            rojosetup7 = Constants.SETUP
        else:
            rojosetup7 = 0

        if values["ProduccionLima7"] + values["RojoProduccionLima7"] > Constants.Capacidad:
            return 'La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal7,
            'InvRojo': rojoinventariofinal7,
            'VentaPerdidaAzul': ventasperdidas7,
            'VentaPerdidaRojo': rojoventasperdidas7,
            'AlmacenamientoAzul': inventariofinal7 * Constants.CostoInventario1,
            'AlmacenamientoRojo': rojoinventariofinal7 * Constants.CostoInventario1,
            'CostoPerdidasAzul': ventasperdidas7 * Constants.CostoBackorder1,
            'CostoPerdidasRojo': rojoventasperdidas7 * Constants.CostoBackorder1,
            'SetupAzul': setup7,
            'SetupRojo': rojosetup7,
            'TotalesAzul': inventariofinal7 * Constants.CostoInventario1 + ventasperdidas7 * Constants.CostoBackorder1 + setup7,
            'TotalesRojo': rojoinventariofinal7 * Constants.CostoInventario1 + rojoventasperdidas7 * Constants.CostoBackorder1 + rojosetup7,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario1,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario1,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder1,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder1,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario1,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario1,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder1,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder1,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario1 + ventasperdidas3 * Constants.CostoBackorder1 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario1 + rojoventasperdidas3 * Constants.CostoBackorder1 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario1,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario1,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder1,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder1,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario1 + ventasperdidas4 * Constants.CostoBackorder1 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario1 + rojoventasperdidas4 * Constants.CostoBackorder1 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario1,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario1,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder1,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder1,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario1 + ventasperdidas5 * Constants.CostoBackorder1 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario1 + rojoventasperdidas5 * Constants.CostoBackorder1 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario1,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario1,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder1,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder1,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario1 + ventasperdidas6 * Constants.CostoBackorder1 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario1 + rojoventasperdidas6 * Constants.CostoBackorder1 + rojosetup6,
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
            setup8 = Constants.SETUP
        else:
            setup8 = 0

        if values["RojoProduccionLima8"] > 0:
            rojosetup8 = Constants.SETUP
        else:
            rojosetup8 = 0

        if values["ProduccionLima8"] + values["RojoProduccionLima8"] > Constants.Capacidad:
            return 'La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal8,
            'InvRojo': rojoinventariofinal8,
            'VentaPerdidaAzul': ventasperdidas8,
            'VentaPerdidaRojo': rojoventasperdidas8,
            'AlmacenamientoAzul': inventariofinal8 * Constants.CostoInventario1,
            'AlmacenamientoRojo': rojoinventariofinal8 * Constants.CostoInventario1,
            'CostoPerdidasAzul': ventasperdidas8 * Constants.CostoBackorder1,
            'CostoPerdidasRojo': rojoventasperdidas8 * Constants.CostoBackorder1,
            'SetupAzul': setup8,
            'SetupRojo': rojosetup8,
            'TotalesAzul': inventariofinal8 * Constants.CostoInventario1 + ventasperdidas8 * Constants.CostoBackorder1 + setup8,
            'TotalesRojo': rojoinventariofinal8 * Constants.CostoInventario1 + rojoventasperdidas8 * Constants.CostoBackorder1 + rojosetup8,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario1,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario1,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder1,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder1,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario1,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario1,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder1,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder1,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario1 + ventasperdidas3 * Constants.CostoBackorder1 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario1 + rojoventasperdidas3 * Constants.CostoBackorder1 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario1,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario1,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder1,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder1,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario1 + ventasperdidas4 * Constants.CostoBackorder1 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario1 + rojoventasperdidas4 * Constants.CostoBackorder1 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario1,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario1,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder1,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder1,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario1 + ventasperdidas5 * Constants.CostoBackorder1 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario1 + rojoventasperdidas5 * Constants.CostoBackorder1 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario1,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario1,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder1,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder1,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario1 + ventasperdidas6 * Constants.CostoBackorder1 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario1 + rojoventasperdidas6 * Constants.CostoBackorder1 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario1,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario1,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder1,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder1,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario1 + ventasperdidas7 * Constants.CostoBackorder1 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario1 + rojoventasperdidas7 * Constants.CostoBackorder1 + rojosetup7,
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
            setup9 = Constants.SETUP
        else:
            setup9 = 0

        if values["RojoProduccionLima9"] > 0:
            rojosetup9 = Constants.SETUP
        else:
            rojosetup9 = 0

        if values["ProduccionLima9"] + values["RojoProduccionLima9"] > Constants.Capacidad:
            return 'La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal9,
            'InvRojo': rojoinventariofinal9,
            'VentaPerdidaAzul': ventasperdidas9,
            'VentaPerdidaRojo': rojoventasperdidas9,
            'AlmacenamientoAzul': inventariofinal9 * Constants.CostoInventario1,
            'AlmacenamientoRojo': rojoinventariofinal9 * Constants.CostoInventario1,
            'CostoPerdidasAzul': ventasperdidas9 * Constants.CostoBackorder1,
            'CostoPerdidasRojo': rojoventasperdidas9 * Constants.CostoBackorder1,
            'SetupAzul': setup9,
            'SetupRojo': rojosetup9,
            'TotalesAzul': inventariofinal9 * Constants.CostoInventario1 + ventasperdidas9 * Constants.CostoBackorder1 + setup9,
            'TotalesRojo': rojoinventariofinal9 * Constants.CostoInventario1 + rojoventasperdidas9 * Constants.CostoBackorder1 + rojosetup9,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario1,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario1,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder1,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder1,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario1,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario1,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder1,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder1,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario1 + ventasperdidas3 * Constants.CostoBackorder1 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario1 + rojoventasperdidas3 * Constants.CostoBackorder1 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario1,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario1,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder1,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder1,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario1 + ventasperdidas4 * Constants.CostoBackorder1 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario1 + rojoventasperdidas4 * Constants.CostoBackorder1 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario1,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario1,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder1,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder1,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario1 + ventasperdidas5 * Constants.CostoBackorder1 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario1 + rojoventasperdidas5 * Constants.CostoBackorder1 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario1,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario1,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder1,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder1,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario1 + ventasperdidas6 * Constants.CostoBackorder1 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario1 + rojoventasperdidas6 * Constants.CostoBackorder1 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario1,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario1,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder1,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder1,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario1 + ventasperdidas7 * Constants.CostoBackorder1 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario1 + rojoventasperdidas7 * Constants.CostoBackorder1 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * Constants.CostoInventario1,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * Constants.CostoInventario1,
            'costoventasperdidas8': ventasperdidas8 * Constants.CostoBackorder1,
            'rojocostoventasperdidas8': rojoventasperdidas8 * Constants.CostoBackorder1,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * Constants.CostoInventario1 + ventasperdidas8 * Constants.CostoBackorder1 + setup8,
            'rojototales8': rojoinventariofinal8 * Constants.CostoInventario1 + rojoventasperdidas8 * Constants.CostoBackorder1 + rojosetup8,

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
            setup10 = Constants.SETUP
        else:
            setup10 = 0

        if values["RojoProduccionLima10"] > 0:
            rojosetup10 = Constants.SETUP
        else:
            rojosetup10 = 0

        if values["ProduccionLima10"] + values["RojoProduccionLima10"] > Constants.Capacidad:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal10,
            'InvRojo': rojoinventariofinal10,
            'VentaPerdidaAzul': ventasperdidas10,
            'VentaPerdidaRojo': rojoventasperdidas10,
            'AlmacenamientoAzul': inventariofinal10 * Constants.CostoInventario1,
            'AlmacenamientoRojo': rojoinventariofinal10 * Constants.CostoInventario1,
            'CostoPerdidasAzul': ventasperdidas10 * Constants.CostoBackorder1,
            'CostoPerdidasRojo': rojoventasperdidas10 * Constants.CostoBackorder1,
            'SetupAzul': setup10,
            'SetupRojo': rojosetup10,
            'TotalesAzul': inventariofinal10 * Constants.CostoInventario1 + ventasperdidas10 * Constants.CostoBackorder1 + setup10,
            'TotalesRojo': rojoinventariofinal10 * Constants.CostoInventario1 + rojoventasperdidas10 * Constants.CostoBackorder1 + rojosetup10,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario1,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario1,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder1,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder1,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario1,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario1,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder1,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder1,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario1 + ventasperdidas3 * Constants.CostoBackorder1 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario1 + rojoventasperdidas3 * Constants.CostoBackorder1 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario1,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario1,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder1,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder1,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario1 + ventasperdidas4 * Constants.CostoBackorder1 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario1 + rojoventasperdidas4 * Constants.CostoBackorder1 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario1,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario1,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder1,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder1,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario1 + ventasperdidas5 * Constants.CostoBackorder1 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario1 + rojoventasperdidas5 * Constants.CostoBackorder1 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario1,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario1,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder1,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder1,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario1 + ventasperdidas6 * Constants.CostoBackorder1 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario1 + rojoventasperdidas6 * Constants.CostoBackorder1 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario1,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario1,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder1,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder1,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario1 + ventasperdidas7 * Constants.CostoBackorder1 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario1 + rojoventasperdidas7 * Constants.CostoBackorder1 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * Constants.CostoInventario1,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * Constants.CostoInventario1,
            'costoventasperdidas8': ventasperdidas8 * Constants.CostoBackorder1,
            'rojocostoventasperdidas8': rojoventasperdidas8 * Constants.CostoBackorder1,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * Constants.CostoInventario1 + ventasperdidas8 * Constants.CostoBackorder1 + setup8,
            'rojototales8': rojoinventariofinal8 * Constants.CostoInventario1 + rojoventasperdidas8 * Constants.CostoBackorder1 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * Constants.CostoInventario1,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * Constants.CostoInventario1,
            'costoventasperdidas9': ventasperdidas9 * Constants.CostoBackorder1,
            'rojocostoventasperdidas9': rojoventasperdidas9 * Constants.CostoBackorder1,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * Constants.CostoInventario1 + ventasperdidas9 * Constants.CostoBackorder1 + setup9,
            'rojototales9': rojoinventariofinal9 * Constants.CostoInventario1 + rojoventasperdidas9 * Constants.CostoBackorder1 + rojosetup9,
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
            setup11 = Constants.SETUP
        else:
            setup11 = 0

        if values["RojoProduccionLima11"] > 0:
            rojosetup11 = Constants.SETUP
        else:
            rojosetup11 = 0

        if values["ProduccionLima11"] + values["RojoProduccionLima11"] > Constants.Capacidad:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):

        return {
            'InvAzul': inventariofinal11,
            'InvRojo': rojoinventariofinal11,
            'VentaPerdidaAzul': ventasperdidas11,
            'VentaPerdidaRojo': rojoventasperdidas11,
            'AlmacenamientoAzul': inventariofinal11 * Constants.CostoInventario1,
            'AlmacenamientoRojo': rojoinventariofinal11 * Constants.CostoInventario1,
            'CostoPerdidasAzul': ventasperdidas11 * Constants.CostoBackorder1,
            'CostoPerdidasRojo': rojoventasperdidas11 * Constants.CostoBackorder1,
            'SetupAzul': setup11,
            'SetupRojo': rojosetup11,
            'TotalesAzul': inventariofinal11 * Constants.CostoInventario1 + ventasperdidas11 * Constants.CostoBackorder1 + setup11,
            'TotalesRojo': rojoinventariofinal11 * Constants.CostoInventario1 + rojoventasperdidas11 * Constants.CostoBackorder1 + rojosetup11,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario1,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario1,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder1,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder1,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario1,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario1,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder1,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder1,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario1 + ventasperdidas3 * Constants.CostoBackorder1 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario1 + rojoventasperdidas3 * Constants.CostoBackorder1 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario1,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario1,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder1,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder1,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario1 + ventasperdidas4 * Constants.CostoBackorder1 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario1 + rojoventasperdidas4 * Constants.CostoBackorder1 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario1,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario1,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder1,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder1,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario1 + ventasperdidas5 * Constants.CostoBackorder1 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario1 + rojoventasperdidas5 * Constants.CostoBackorder1 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario1,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario1,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder1,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder1,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario1 + ventasperdidas6 * Constants.CostoBackorder1 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario1 + rojoventasperdidas6 * Constants.CostoBackorder1 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario1,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario1,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder1,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder1,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario1 + ventasperdidas7 * Constants.CostoBackorder1 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario1 + rojoventasperdidas7 * Constants.CostoBackorder1 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * Constants.CostoInventario1,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * Constants.CostoInventario1,
            'costoventasperdidas8': ventasperdidas8 * Constants.CostoBackorder1,
            'rojocostoventasperdidas8': rojoventasperdidas8 * Constants.CostoBackorder1,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * Constants.CostoInventario1 + ventasperdidas8 * Constants.CostoBackorder1 + setup8,
            'rojototales8': rojoinventariofinal8 * Constants.CostoInventario1 + rojoventasperdidas8 * Constants.CostoBackorder1 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * Constants.CostoInventario1,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * Constants.CostoInventario1,
            'costoventasperdidas9': ventasperdidas9 * Constants.CostoBackorder1,
            'rojocostoventasperdidas9': rojoventasperdidas9 * Constants.CostoBackorder1,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * Constants.CostoInventario1 + ventasperdidas9 * Constants.CostoBackorder1 + setup9,
            'rojototales9': rojoinventariofinal9 * Constants.CostoInventario1 + rojoventasperdidas9 * Constants.CostoBackorder1 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * Constants.CostoInventario1,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * Constants.CostoInventario1,
            'costoventasperdidas10': ventasperdidas10 * Constants.CostoBackorder1,
            'rojocostoventasperdidas10': rojoventasperdidas10 * Constants.CostoBackorder1,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * Constants.CostoInventario1 + ventasperdidas10 * Constants.CostoBackorder1 + setup10,
            'rojototales10': rojoinventariofinal10 * Constants.CostoInventario1 + rojoventasperdidas10 * Constants.CostoBackorder1 + rojosetup10,
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
            setup12 = Constants.SETUP
        else:
            setup12 = 0

        if values["RojoProduccionLima12"] > 0:
            rojosetup12 = Constants.SETUP
        else:
            rojosetup12 = 0

        TotalinventarioLima = (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6 + inventariofinal7 + inventariofinal8 + inventariofinal9 + inventariofinal10 + inventariofinal11 + inventariofinal12) * Constants.CostoInventario1
        TotalinventarioLima = (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6 + rojoinventariofinal7 + rojoinventariofinal8 + rojoinventariofinal9 + rojoinventariofinal10 + rojoinventariofinal11 + rojoinventariofinal12) * Constants.CostoInventario1
        TotalsetupLima = setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + setup7 + setup8 + setup9 + setup10 + setup11 + setup12 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6 + rojosetup7 + rojosetup8 + rojosetup9 + rojosetup10 + rojosetup11 + rojosetup12
        TotalventasLima = (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6 + ventasperdidas7 + ventasperdidas8 + ventasperdidas9 + ventasperdidas10 + ventasperdidas11 + ventasperdidas12) * Constants.CostoBackorder1
        TotalventasLima = (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6 + rojoventasperdidas7 + rojoventasperdidas8 + rojoventasperdidas9 + rojoventasperdidas10 + rojoventasperdidas11 + rojoventasperdidas12) * Constants.CostoBackorder1
        TotalTotalesLima = TotalinventarioLima + TotalventasLima + TotalsetupLima

        if values["ProduccionLima12"] + values["RojoProduccionLima12"] > Constants.Capacidad:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal12,
            'InvRojo': rojoinventariofinal12,
            'VentaPerdidaAzul': ventasperdidas12,
            'VentaPerdidaRojo': rojoventasperdidas12,
            'AlmacenamientoAzul': inventariofinal12 * Constants.CostoInventario1,
            'AlmacenamientoRojo': rojoinventariofinal12 * Constants.CostoInventario1,
            'CostoPerdidasAzul': ventasperdidas12 * Constants.CostoBackorder1,
            'CostoPerdidasRojo': rojoventasperdidas12 * Constants.CostoBackorder1,
            'SetupAzul': setup12,
            'SetupRojo': rojosetup12,
            'TotalesAzul': inventariofinal12 * Constants.CostoInventario1 + ventasperdidas12 * Constants.CostoBackorder1 + setup12,
            'TotalesRojo': rojoinventariofinal12 * Constants.CostoInventario1 + rojoventasperdidas12 * Constants.CostoBackorder1 + rojosetup12,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario1,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario1,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder1,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder1,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario1,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario1,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder1,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder1,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario1 + ventasperdidas3 * Constants.CostoBackorder1 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario1 + rojoventasperdidas3 * Constants.CostoBackorder1 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario1,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario1,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder1,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder1,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario1 + ventasperdidas4 * Constants.CostoBackorder1 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario1 + rojoventasperdidas4 * Constants.CostoBackorder1 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario1,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario1,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder1,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder1,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario1 + ventasperdidas5 * Constants.CostoBackorder1 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario1 + rojoventasperdidas5 * Constants.CostoBackorder1 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario1,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario1,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder1,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder1,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario1 + ventasperdidas6 * Constants.CostoBackorder1 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario1 + rojoventasperdidas6 * Constants.CostoBackorder1 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario1,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario1,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder1,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder1,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario1 + ventasperdidas7 * Constants.CostoBackorder1 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario1 + rojoventasperdidas7 * Constants.CostoBackorder1 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * Constants.CostoInventario1,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * Constants.CostoInventario1,
            'costoventasperdidas8': ventasperdidas8 * Constants.CostoBackorder1,
            'rojocostoventasperdidas8': rojoventasperdidas8 * Constants.CostoBackorder1,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * Constants.CostoInventario1 + ventasperdidas8 * Constants.CostoBackorder1 + setup8,
            'rojototales8': rojoinventariofinal8 * Constants.CostoInventario1 + rojoventasperdidas8 * Constants.CostoBackorder1 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * Constants.CostoInventario1,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * Constants.CostoInventario1,
            'costoventasperdidas9': ventasperdidas9 * Constants.CostoBackorder1,
            'rojocostoventasperdidas9': rojoventasperdidas9 * Constants.CostoBackorder1,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * Constants.CostoInventario1 + ventasperdidas9 * Constants.CostoBackorder1 + setup9,
            'rojototales9': rojoinventariofinal9 * Constants.CostoInventario1 + rojoventasperdidas9 * Constants.CostoBackorder1 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * Constants.CostoInventario1,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * Constants.CostoInventario1,
            'costoventasperdidas10': ventasperdidas10 * Constants.CostoBackorder1,
            'rojocostoventasperdidas10': rojoventasperdidas10 * Constants.CostoBackorder1,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * Constants.CostoInventario1 + ventasperdidas10 * Constants.CostoBackorder1 + setup10,
            'rojototales10': rojoinventariofinal10 * Constants.CostoInventario1 + rojoventasperdidas10 * Constants.CostoBackorder1 + rojosetup4,

            'ventasperdidas11': ventasperdidas11,
            'rojoventasperdidas11': rojoventasperdidas11,
            'costoalmacenamiento11': inventariofinal11 * Constants.CostoInventario1,
            'rojocostoalmacenamiento11': rojoinventariofinal11 * Constants.CostoInventario1,
            'costoventasperdidas11': ventasperdidas11 * Constants.CostoBackorder1,
            'rojocostoventasperdidas11': rojoventasperdidas11 * Constants.CostoBackorder1,
            'setup11': setup11,
            'rojosetup11': rojosetup11,
            'totales11': inventariofinal11 * Constants.CostoInventario1 + ventasperdidas11 * Constants.CostoBackorder1 + setup11,
            'rojototales11': rojoinventariofinal11 * Constants.CostoInventario1 + rojoventasperdidas11 * Constants.CostoBackorder1 + rojosetup11,
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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario1,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario1,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder1,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder1,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario1 + ventasperdidas1 * Constants.CostoBackorder1 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario1 + rojoventasperdidas1 * Constants.CostoBackorder1 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario1,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario1,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder1,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder1,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario1 + ventasperdidas2 * Constants.CostoBackorder1 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario1 + rojoventasperdidas2 * Constants.CostoBackorder1 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario1,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario1,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder1,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder1,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario1 + ventasperdidas3 * Constants.CostoBackorder1 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario1 + rojoventasperdidas3 * Constants.CostoBackorder1 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario1,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario1,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder1,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder1,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario1 + ventasperdidas4 * Constants.CostoBackorder1 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario1 + rojoventasperdidas4 * Constants.CostoBackorder1 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario1,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario1,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder1,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder1,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario1 + ventasperdidas5 * Constants.CostoBackorder1 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario1 + rojoventasperdidas5 * Constants.CostoBackorder1 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario1,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario1,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder1,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder1,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario1 + ventasperdidas6 * Constants.CostoBackorder1 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario1 + rojoventasperdidas6 * Constants.CostoBackorder1 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario1,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario1,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder1,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder1,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario1 + ventasperdidas7 * Constants.CostoBackorder1 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario1 + rojoventasperdidas7 * Constants.CostoBackorder1 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * Constants.CostoInventario1,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * Constants.CostoInventario1,
            'costoventasperdidas8': ventasperdidas8 * Constants.CostoBackorder1,
            'rojocostoventasperdidas8': rojoventasperdidas8 * Constants.CostoBackorder1,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * Constants.CostoInventario1 + ventasperdidas8 * Constants.CostoBackorder1 + setup8,
            'rojototales8': rojoinventariofinal8 * Constants.CostoInventario1 + rojoventasperdidas8 * Constants.CostoBackorder1 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * Constants.CostoInventario1,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * Constants.CostoInventario1,
            'costoventasperdidas9': ventasperdidas9 * Constants.CostoBackorder1,
            'rojocostoventasperdidas9': rojoventasperdidas9 * Constants.CostoBackorder1,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * Constants.CostoInventario1 + ventasperdidas9 * Constants.CostoBackorder1 + setup9,
            'rojototales9': rojoinventariofinal9 * Constants.CostoInventario1 + rojoventasperdidas9 * Constants.CostoBackorder1 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * Constants.CostoInventario1,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * Constants.CostoInventario1,
            'costoventasperdidas10': ventasperdidas10 * Constants.CostoBackorder1,
            'rojocostoventasperdidas10': rojoventasperdidas10 * Constants.CostoBackorder1,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * Constants.CostoInventario1 + ventasperdidas10 * Constants.CostoBackorder1 + setup10,
            'rojototales10': rojoinventariofinal10 * Constants.CostoInventario1 + rojoventasperdidas10 * Constants.CostoBackorder1 + rojosetup4,

            'ventasperdidas11': ventasperdidas11,
            'rojoventasperdidas11': rojoventasperdidas11,
            'costoalmacenamiento11': inventariofinal11 * Constants.CostoInventario1,
            'rojocostoalmacenamiento11': rojoinventariofinal11 * Constants.CostoInventario1,
            'costoventasperdidas11': ventasperdidas11 * Constants.CostoBackorder1,
            'rojocostoventasperdidas11': rojoventasperdidas11 * Constants.CostoBackorder1,
            'setup11': setup11,
            'rojosetup11': rojosetup11,
            'totales11': inventariofinal11 * Constants.CostoInventario1 + ventasperdidas11 * Constants.CostoBackorder1 + setup11,
            'rojototales11': rojoinventariofinal11 * Constants.CostoInventario1 + rojoventasperdidas11 * Constants.CostoBackorder1 + rojosetup11,

            'ventasperdidas12': ventasperdidas12,
            'rojoventasperdidas12': rojoventasperdidas12,
            'costoalmacenamiento12': inventariofinal12 * Constants.CostoInventario1,
            'rojocostoalmacenamiento12': rojoinventariofinal12 * Constants.CostoInventario1,
            'costoventasperdidas12': ventasperdidas12 * Constants.CostoBackorder1,
            'rojocostoventasperdidas12': rojoventasperdidas12 * Constants.CostoBackorder1,
            'setup12': setup12,
            'rojosetup12': rojosetup12,
            'totales12': inventariofinal12 * Constants.CostoInventario1 + ventasperdidas12 * Constants.CostoBackorder1 + setup12,
            'rojototales12': rojoinventariofinal12 * Constants.CostoInventario1 + rojoventasperdidas12 * Constants.CostoBackorder1 + rojosetup12,
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
            setup1=Constants.SETUP2
        else:
            setup1=0

        if values["RojoProduccionJapon1"]>0:
            rojosetup1=Constants.SETUP2
        else:
            rojosetup1=0

        if values["ProduccionJapon1"] + values["RojoProduccionJapon1"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal1,
            'InvRojo': rojoinventariofinal1,
            'VentaPerdidaAzul': ventasperdidas1,
            'VentaPerdidaRojo': rojoventasperdidas1,
            'AlmacenamientoAzul': inventariofinal1 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal1 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas1 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas1 * Constants.CostoBackorder2,
            'SetupAzul': setup1,
            'SetupRojo': rojosetup1,
            'TotalesAzul': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'TotalesRojo': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,
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
            setup2 = Constants.SETUP2
        else:
            setup2 = 0

        if values["RojoProduccionJapon2"] > 0:
            rojosetup2 = Constants.SETUP2
        else:
            rojosetup2 = 0

        if values["ProduccionJapon2"] + values["RojoProduccionJapon2"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal2,
            'InvRojo': rojoinventariofinal2,
            'VentaPerdidaAzul': ventasperdidas2,
            'VentaPerdidaRojo': rojoventasperdidas2,
            'AlmacenamientoAzul': inventariofinal2 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal2 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas2 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas2 * Constants.CostoBackorder2,
            'SetupAzul': setup2,
            'SetupRojo': rojosetup2,
            'TotalesAzul': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'TotalesRojo': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

            'inventario2': inventariofinal1,
            'Rojoinventario2': rojoinventariofinal1,
            
            'ventasperdidas1':ventasperdidas1,
            'rojoventasperdidas1':rojoventasperdidas1,
            'costoalmacenamiento1':inventariofinal1*Constants.CostoInventario2,
            'rojocostoalmacenamiento1':rojoinventariofinal1*Constants.CostoInventario2,
            'costoventasperdidas1':ventasperdidas1*Constants.CostoBackorder2,
            'rojocostoventasperdidas1':rojoventasperdidas1*Constants.CostoBackorder2,
            'setup1':setup1,
            'rojosetup1':rojosetup1,
            'totales1':inventariofinal1*Constants.CostoInventario2+ventasperdidas1*Constants.CostoBackorder2+setup1,
            'rojototales1':rojoinventariofinal1*Constants.CostoInventario2+rojoventasperdidas1*Constants.CostoBackorder2+rojosetup1
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
            setup3 = Constants.SETUP2
        else:
            setup3 = 0

        if values["RojoProduccionJapon3"] > 0:
            rojosetup3 = Constants.SETUP2
        else:
            rojosetup3 = 0

        if values["ProduccionJapon3"] + values["RojoProduccionJapon3"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'


    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal3,
            'InvRojo': rojoinventariofinal3,
            'VentaPerdidaAzul': ventasperdidas3,
            'VentaPerdidaRojo': rojoventasperdidas3,
            'AlmacenamientoAzul': inventariofinal3 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal3 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas3 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas3 * Constants.CostoBackorder2,
            'SetupAzul': setup3,
            'SetupRojo': rojosetup3,
            'TotalesAzul': inventariofinal3 * Constants.CostoInventario2 + ventasperdidas3 * Constants.CostoBackorder2 + setup3,
            'TotalesRojo': rojoinventariofinal3 * Constants.CostoInventario2 + rojoventasperdidas3 * Constants.CostoBackorder2 + rojosetup3,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            
            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario2,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario2,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder2,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder2,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

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
            setup4 = Constants.SETUP2
        else:
            setup4 = 0

        if values["RojoProduccionJapon4"] > 0:
            rojosetup4 = Constants.SETUP2
        else:
            rojosetup4 = 0

        if values["ProduccionJapon4"] + values["RojoProduccionJapon4"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal4,
            'InvRojo': rojoinventariofinal4,
            'VentaPerdidaAzul': ventasperdidas4,
            'VentaPerdidaRojo': rojoventasperdidas4,
            'AlmacenamientoAzul': inventariofinal4 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal4 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas4 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas4 * Constants.CostoBackorder2,
            'SetupAzul': setup4,
            'SetupRojo': rojosetup4,
            'TotalesAzul': inventariofinal4 * Constants.CostoInventario2 + ventasperdidas4 * Constants.CostoBackorder2 + setup4,
            'TotalesRojo': rojoinventariofinal4 * Constants.CostoInventario2 + rojoventasperdidas4 * Constants.CostoBackorder2 + rojosetup4,

            'inventario2': inventariofinal1,
            'inventario3': inventariofinal2,
            'inventario4': inventariofinal3,
            'Rojoinventario2': rojoinventariofinal1,
            'Rojoinventario3': rojoinventariofinal2,
            'Rojoinventario4': rojoinventariofinal3,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario2,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario2,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder2,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder2,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario2,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario2,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder2,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder2,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario2 + ventasperdidas3 * Constants.CostoBackorder2 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario2 + rojoventasperdidas3 * Constants.CostoBackorder2 + rojosetup3,
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
            setup5 = Constants.SETUP2
        else:
            setup5 = 0

        if values["RojoProduccionJapon5"] > 0:
            rojosetup5 = Constants.SETUP2
        else:
            rojosetup5 = 0

        if values["ProduccionJapon5"] + values["RojoProduccionJapon5"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):

        return{
            'InvAzul': inventariofinal5,
            'InvRojo': rojoinventariofinal5,
            'VentaPerdidaAzul': ventasperdidas5,
            'VentaPerdidaRojo': rojoventasperdidas5,
            'AlmacenamientoAzul': inventariofinal5 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal5 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas5 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas5 * Constants.CostoBackorder2,
            'SetupAzul': setup5,
            'SetupRojo': rojosetup5,
            'TotalesAzul': inventariofinal5 * Constants.CostoInventario2 + ventasperdidas5 * Constants.CostoBackorder2 + setup5,
            'TotalesRojo': rojoinventariofinal5 * Constants.CostoInventario2 + rojoventasperdidas5 * Constants.CostoBackorder2 + rojosetup5,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario2,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario2,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder2,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder2,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario2,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario2,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder2,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder2,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario2 + ventasperdidas3 * Constants.CostoBackorder2 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario2 + rojoventasperdidas3 * Constants.CostoBackorder2 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario2,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario2,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder2,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder2,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario2 + ventasperdidas4 * Constants.CostoBackorder2 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario2 + rojoventasperdidas4 * Constants.CostoBackorder2 + rojosetup4,
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

        if values["ProduccionJapon6"] + values["RojoProduccionJapon6"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'

        inventariofinal6 = max(values['ProduccionJapon6'] + inventariofinal5 - Constants.JaponDemanda6, 0)
        rojoinventariofinal6 = max(values['RojoProduccionJapon6'] + rojoinventariofinal5 - Constants.rojoJaponDemanda6, 0)
        ventasperdidas6 = max(Constants.JaponDemanda6 - values['ProduccionJapon6'] - inventariofinal5, 0)
        rojoventasperdidas6 = max(Constants.rojoJaponDemanda6 - values['RojoProduccionJapon6'] - rojoinventariofinal5, 0)

        if values["ProduccionJapon6"] > 0:
            setup6 = Constants.SETUP2
        else:
            setup6 = 0

        if values["RojoProduccionJapon6"] > 0:
            rojosetup6 = Constants.SETUP2
        else:
            rojosetup6= 0

        global TotalinventarioJapon, TotalsetupJapon, TotalventasJapon, TotalTotalesJapon

        TotalinventarioJapon = (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6) * Constants.CostoInventario2
        TotalinventarioJapon = TotalinventarioJapon + (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6) * Constants.CostoInventario2
        TotalsetupJapon = setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6
        TotalventasJapon = (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6) * Constants.CostoBackorder2
        TotalventasJapon = TotalventasJapon + (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6) * Constants.CostoBackorder2
        TotalTotalesJapon = TotalinventarioJapon + TotalventasJapon + TotalsetupJapon

        if values["ProduccionJapon6"] + values["RojoProduccionJapon6"] > Constants.Capacidad2:
            return 'La produccion no debe pasar de la capacidad'

    def vars_for_template(self):

        return{
            'InvAzul': inventariofinal6,
            'InvRojo': rojoinventariofinal6,
            'VentaPerdidaAzul': ventasperdidas6,
            'VentaPerdidaRojo': rojoventasperdidas6,
            'AlmacenamientoAzul': inventariofinal6 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal6 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas6 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas6 * Constants.CostoBackorder2,
            'SetupAzul': setup6,
            'SetupRojo': rojosetup6,
            'TotalesAzul': inventariofinal6 * Constants.CostoInventario2 + ventasperdidas6 * Constants.CostoBackorder2 + setup6,
            'TotalesRojo': rojoinventariofinal6 * Constants.CostoInventario2 + rojoventasperdidas6 * Constants.CostoBackorder2 + rojosetup6,


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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario2,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario2,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder2,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder2,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario2,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario2,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder2,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder2,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario2 + ventasperdidas3 * Constants.CostoBackorder2 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario2 + rojoventasperdidas3 * Constants.CostoBackorder2 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario2,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario2,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder2,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder2,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario2 + ventasperdidas4 * Constants.CostoBackorder2 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario2 + rojoventasperdidas4 * Constants.CostoBackorder2 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario2,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario2,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder2,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder2,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario2 + ventasperdidas5 * Constants.CostoBackorder2 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario2 + rojoventasperdidas5 * Constants.CostoBackorder2 + rojosetup5,
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
            setup7 = Constants.SETUP2
        else:
            setup7 = 0

        if values["RojoProduccionJapon7"] > 0:
            rojosetup7 = Constants.SETUP2
        else:
            rojosetup7 = 0

        if values["ProduccionJapon7"] + values["RojoProduccionJapon7"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return{
            'InvAzul': inventariofinal7,
            'InvRojo': rojoinventariofinal7,
            'VentaPerdidaAzul': ventasperdidas7,
            'VentaPerdidaRojo': rojoventasperdidas7,
            'AlmacenamientoAzul': inventariofinal7 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal7 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas7 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas7 * Constants.CostoBackorder2,
            'SetupAzul': setup7,
            'SetupRojo': rojosetup7,
            'TotalesAzul': inventariofinal7 * Constants.CostoInventario2 + ventasperdidas7 * Constants.CostoBackorder2 + setup7,
            'TotalesRojo': rojoinventariofinal7 * Constants.CostoInventario2 + rojoventasperdidas7 * Constants.CostoBackorder2 + rojosetup7,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario2,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario2,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder2,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder2,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario2,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario2,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder2,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder2,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario2 + ventasperdidas3 * Constants.CostoBackorder2 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario2 + rojoventasperdidas3 * Constants.CostoBackorder2 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario2,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario2,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder2,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder2,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario2 + ventasperdidas4 * Constants.CostoBackorder2 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario2 + rojoventasperdidas4 * Constants.CostoBackorder2 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario2,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario2,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder2,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder2,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario2 + ventasperdidas5 * Constants.CostoBackorder2 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario2 + rojoventasperdidas5 * Constants.CostoBackorder2 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario2,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario2,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder2,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder2,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario2 + ventasperdidas6 * Constants.CostoBackorder2 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario2 + rojoventasperdidas6 * Constants.CostoBackorder2 + rojosetup6,
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
            setup8 = Constants.SETUP2
        else:
            setup8 = 0

        if values["RojoProduccionJapon8"] > 0:
            rojosetup8 = Constants.SETUP2
        else:
            rojosetup8 = 0

        if values["ProduccionJapon8"] + values["RojoProduccionJapon8"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'


    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal8,
            'InvRojo': rojoinventariofinal8,
            'VentaPerdidaAzul': ventasperdidas8,
            'VentaPerdidaRojo': rojoventasperdidas8,
            'AlmacenamientoAzul': inventariofinal8 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal8 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas8 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas8 * Constants.CostoBackorder2,
            'SetupAzul': setup8,
            'SetupRojo': rojosetup8,
            'TotalesAzul': inventariofinal8 * Constants.CostoInventario2 + ventasperdidas8 * Constants.CostoBackorder2 + setup8,
            'TotalesRojo': rojoinventariofinal8 * Constants.CostoInventario2 + rojoventasperdidas8 * Constants.CostoBackorder2 + rojosetup8,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario2,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario2,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder2,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder2,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario2,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario2,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder2,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder2,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario2 + ventasperdidas3 * Constants.CostoBackorder2 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario2 + rojoventasperdidas3 * Constants.CostoBackorder2 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario2,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario2,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder2,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder2,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario2 + ventasperdidas4 * Constants.CostoBackorder2 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario2 + rojoventasperdidas4 * Constants.CostoBackorder2 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario2,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario2,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder2,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder2,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario2 + ventasperdidas5 * Constants.CostoBackorder2 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario2 + rojoventasperdidas5 * Constants.CostoBackorder2 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario2,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario2,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder2,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder2,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario2 + ventasperdidas6 * Constants.CostoBackorder2 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario2 + rojoventasperdidas6 * Constants.CostoBackorder2 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario2,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario2,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder2,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder2,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario2 + ventasperdidas7 * Constants.CostoBackorder2 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario2 + rojoventasperdidas7 * Constants.CostoBackorder2 + rojosetup7,
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
            setup9 = Constants.SETUP2
        else:
            setup9 = 0

        if values["RojoProduccionJapon9"] > 0:
            rojosetup9 = Constants.SETUP2
        else:
            rojosetup9 = 0

        if values["ProduccionJapon9"] + values["RojoProduccionJapon9"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'


    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal9,
            'InvRojo': rojoinventariofinal9,
            'VentaPerdidaAzul': ventasperdidas9,
            'VentaPerdidaRojo': rojoventasperdidas9,
            'AlmacenamientoAzul': inventariofinal9 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal9 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas9 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas9 * Constants.CostoBackorder2,
            'SetupAzul': setup9,
            'SetupRojo': rojosetup9,
            'TotalesAzul': inventariofinal9 * Constants.CostoInventario2 + ventasperdidas9 * Constants.CostoBackorder2 + setup9,
            'TotalesRojo': rojoinventariofinal9 * Constants.CostoInventario2 + rojoventasperdidas9 * Constants.CostoBackorder2 + rojosetup9,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario2,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario2,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder2,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder2,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario2,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario2,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder2,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder2,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario2 + ventasperdidas3 * Constants.CostoBackorder2 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario2 + rojoventasperdidas3 * Constants.CostoBackorder2 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario2,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario2,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder2,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder2,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario2 + ventasperdidas4 * Constants.CostoBackorder2 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario2 + rojoventasperdidas4 * Constants.CostoBackorder2 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario2,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario2,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder2,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder2,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario2 + ventasperdidas5 * Constants.CostoBackorder2 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario2 + rojoventasperdidas5 * Constants.CostoBackorder2 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario2,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario2,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder2,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder2,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario2 + ventasperdidas6 * Constants.CostoBackorder2 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario2 + rojoventasperdidas6 * Constants.CostoBackorder2 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario2,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario2,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder2,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder2,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario2 + ventasperdidas7 * Constants.CostoBackorder2 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario2 + rojoventasperdidas7 * Constants.CostoBackorder2 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * Constants.CostoInventario2,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * Constants.CostoInventario2,
            'costoventasperdidas8': ventasperdidas8 * Constants.CostoBackorder2,
            'rojocostoventasperdidas8': rojoventasperdidas8 * Constants.CostoBackorder2,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * Constants.CostoInventario2 + ventasperdidas8 * Constants.CostoBackorder2 + setup8,
            'rojototales8': rojoinventariofinal8 * Constants.CostoInventario2 + rojoventasperdidas8 * Constants.CostoBackorder2 + rojosetup8,

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
            setup10 = Constants.SETUP2
        else:
            setup10 = 0

        if values["RojoProduccionJapon10"] > 0:
            rojosetup10 = Constants.SETUP2
        else:
            rojosetup10 = 0

        if values["ProduccionJapon10"] + values["RojoProduccionJapon10"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal10,
            'InvRojo': rojoinventariofinal10,
            'VentaPerdidaAzul': ventasperdidas10,
            'VentaPerdidaRojo': rojoventasperdidas10,
            'AlmacenamientoAzul': inventariofinal10 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal10 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas10 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas10 * Constants.CostoBackorder2,
            'SetupAzul': setup10,
            'SetupRojo': rojosetup10,
            'TotalesAzul': inventariofinal10 * Constants.CostoInventario2 + ventasperdidas10 * Constants.CostoBackorder2 + setup10,
            'TotalesRojo': rojoinventariofinal10 * Constants.CostoInventario2 + rojoventasperdidas10 * Constants.CostoBackorder2 + rojosetup10,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario2,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario2,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder2,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder2,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario2,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario2,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder2,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder2,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario2 + ventasperdidas3 * Constants.CostoBackorder2 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario2 + rojoventasperdidas3 * Constants.CostoBackorder2 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario2,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario2,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder2,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder2,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario2 + ventasperdidas4 * Constants.CostoBackorder2 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario2 + rojoventasperdidas4 * Constants.CostoBackorder2 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario2,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario2,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder2,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder2,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario2 + ventasperdidas5 * Constants.CostoBackorder2 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario2 + rojoventasperdidas5 * Constants.CostoBackorder2 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario2,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario2,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder2,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder2,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario2 + ventasperdidas6 * Constants.CostoBackorder2 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario2 + rojoventasperdidas6 * Constants.CostoBackorder2 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario2,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario2,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder2,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder2,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario2 + ventasperdidas7 * Constants.CostoBackorder2 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario2 + rojoventasperdidas7 * Constants.CostoBackorder2 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * Constants.CostoInventario2,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * Constants.CostoInventario2,
            'costoventasperdidas8': ventasperdidas8 * Constants.CostoBackorder2,
            'rojocostoventasperdidas8': rojoventasperdidas8 * Constants.CostoBackorder2,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * Constants.CostoInventario2 + ventasperdidas8 * Constants.CostoBackorder2 + setup8,
            'rojototales8': rojoinventariofinal8 * Constants.CostoInventario2 + rojoventasperdidas8 * Constants.CostoBackorder2 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * Constants.CostoInventario2,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * Constants.CostoInventario2,
            'costoventasperdidas9': ventasperdidas9 * Constants.CostoBackorder2,
            'rojocostoventasperdidas9': rojoventasperdidas9 * Constants.CostoBackorder2,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * Constants.CostoInventario2 + ventasperdidas9 * Constants.CostoBackorder2 + setup9,
            'rojototales9': rojoinventariofinal9 * Constants.CostoInventario2 + rojoventasperdidas9 * Constants.CostoBackorder2 + rojosetup9,
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
            setup11 = Constants.SETUP2
        else:
            setup11 = 0

        if values["RojoProduccionJapon11"] > 0:
            rojosetup11 = Constants.SETUP2
        else:
            rojosetup11 = 0

        if values["ProduccionJapon11"] + values["RojoProduccionJapon11"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):

        return {
            'InvAzul': inventariofinal11,
            'InvRojo': rojoinventariofinal11,
            'VentaPerdidaAzul': ventasperdidas11,
            'VentaPerdidaRojo': rojoventasperdidas11,
            'AlmacenamientoAzul': inventariofinal11 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal11 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas11 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas11 * Constants.CostoBackorder2,
            'SetupAzul': setup11,
            'SetupRojo': rojosetup11,
            'TotalesAzul': inventariofinal11 * Constants.CostoInventario2 + ventasperdidas11 * Constants.CostoBackorder2 + setup11,
            'TotalesRojo': rojoinventariofinal11 * Constants.CostoInventario2 + rojoventasperdidas11 * Constants.CostoBackorder2 + rojosetup11,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario2,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario2,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder2,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder2,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario2,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario2,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder2,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder2,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario2 + ventasperdidas3 * Constants.CostoBackorder2 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario2 + rojoventasperdidas3 * Constants.CostoBackorder2 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario2,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario2,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder2,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder2,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario2 + ventasperdidas4 * Constants.CostoBackorder2 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario2 + rojoventasperdidas4 * Constants.CostoBackorder2 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario2,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario2,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder2,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder2,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario2 + ventasperdidas5 * Constants.CostoBackorder2 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario2 + rojoventasperdidas5 * Constants.CostoBackorder2 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario2,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario2,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder2,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder2,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario2 + ventasperdidas6 * Constants.CostoBackorder2 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario2 + rojoventasperdidas6 * Constants.CostoBackorder2 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario2,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario2,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder2,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder2,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario2 + ventasperdidas7 * Constants.CostoBackorder2 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario2 + rojoventasperdidas7 * Constants.CostoBackorder2 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * Constants.CostoInventario2,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * Constants.CostoInventario2,
            'costoventasperdidas8': ventasperdidas8 * Constants.CostoBackorder2,
            'rojocostoventasperdidas8': rojoventasperdidas8 * Constants.CostoBackorder2,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * Constants.CostoInventario2 + ventasperdidas8 * Constants.CostoBackorder2 + setup8,
            'rojototales8': rojoinventariofinal8 * Constants.CostoInventario2 + rojoventasperdidas8 * Constants.CostoBackorder2 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * Constants.CostoInventario2,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * Constants.CostoInventario2,
            'costoventasperdidas9': ventasperdidas9 * Constants.CostoBackorder2,
            'rojocostoventasperdidas9': rojoventasperdidas9 * Constants.CostoBackorder2,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * Constants.CostoInventario2 + ventasperdidas9 * Constants.CostoBackorder2 + setup9,
            'rojototales9': rojoinventariofinal9 * Constants.CostoInventario2 + rojoventasperdidas9 * Constants.CostoBackorder2 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * Constants.CostoInventario2,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * Constants.CostoInventario2,
            'costoventasperdidas10': ventasperdidas10 * Constants.CostoBackorder2,
            'rojocostoventasperdidas10': rojoventasperdidas10 * Constants.CostoBackorder2,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * Constants.CostoInventario2 + ventasperdidas10 * Constants.CostoBackorder2 + setup10,
            'rojototales10': rojoinventariofinal10 * Constants.CostoInventario2 + rojoventasperdidas10 * Constants.CostoBackorder2 + rojosetup10,
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
            setup12 = Constants.SETUP2
        else:
            setup12 = 0

        if values["RojoProduccionJapon12"] > 0:
            rojosetup12 = Constants.SETUP2
        else:
            rojosetup12 = 0

        TotalinventarioJapon = (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6 + inventariofinal7 + inventariofinal8 + inventariofinal9 + inventariofinal10 + inventariofinal11 + inventariofinal12) * Constants.CostoInventario2
        TotalinventarioJapon = (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6 + rojoinventariofinal7 + rojoinventariofinal8 + rojoinventariofinal9 + rojoinventariofinal10 + rojoinventariofinal11 + rojoinventariofinal12) * Constants.CostoInventario2
        TotalsetupJapon = setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + setup7 + setup8 + setup9 + setup10 + setup11 + setup12 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6 + rojosetup7 + rojosetup8 + rojosetup9 + rojosetup10 + rojosetup11 + rojosetup12
        TotalventasJapon = (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6 + ventasperdidas7 + ventasperdidas8 + ventasperdidas9 + ventasperdidas10 + ventasperdidas11 + ventasperdidas12) * Constants.CostoBackorder2
        TotalventasJapon = (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6 + rojoventasperdidas7 + rojoventasperdidas8 + rojoventasperdidas9 + rojoventasperdidas10 + rojoventasperdidas11 + rojoventasperdidas12) * Constants.CostoBackorder2
        TotalTotalesJapon = TotalinventarioJapon + TotalventasJapon + TotalsetupJapon

        if values["ProduccionJapon12"] + values["RojoProduccionJapon12"] > Constants.Capacidad2:
            return ' La produccion no debe pasar de la capacidad'

    def vars_for_template(self):
        return {
            'InvAzul': inventariofinal12,
            'InvRojo': rojoinventariofinal12,
            'VentaPerdidaAzul': ventasperdidas12,
            'VentaPerdidaRojo': rojoventasperdidas12,
            'AlmacenamientoAzul': inventariofinal12 * Constants.CostoInventario2,
            'AlmacenamientoRojo': rojoinventariofinal12 * Constants.CostoInventario2,
            'CostoPerdidasAzul': ventasperdidas12 * Constants.CostoBackorder2,
            'CostoPerdidasRojo': rojoventasperdidas12 * Constants.CostoBackorder2,
            'SetupAzul': setup12,
            'SetupRojo': rojosetup12,
            'TotalesAzul': inventariofinal12 * Constants.CostoInventario2 + ventasperdidas12 * Constants.CostoBackorder2 + setup12,
            'TotalesRojo': rojoinventariofinal12 * Constants.CostoInventario2 + rojoventasperdidas12 * Constants.CostoBackorder2 + rojosetup12,

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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas1': ventasperdidas1,
            'rojoventasperdidas1': rojoventasperdidas1,
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario2,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario2,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder2,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder2,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario2,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario2,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder2,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder2,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario2 + ventasperdidas3 * Constants.CostoBackorder2 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario2 + rojoventasperdidas3 * Constants.CostoBackorder2 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario2,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario2,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder2,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder2,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario2 + ventasperdidas4 * Constants.CostoBackorder2 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario2 + rojoventasperdidas4 * Constants.CostoBackorder2 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario2,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario2,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder2,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder2,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario2 + ventasperdidas5 * Constants.CostoBackorder2 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario2 + rojoventasperdidas5 * Constants.CostoBackorder2 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario2,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario2,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder2,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder2,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario2 + ventasperdidas6 * Constants.CostoBackorder2 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario2 + rojoventasperdidas6 * Constants.CostoBackorder2 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario2,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario2,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder2,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder2,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario2 + ventasperdidas7 * Constants.CostoBackorder2 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario2 + rojoventasperdidas7 * Constants.CostoBackorder2 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * Constants.CostoInventario2,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * Constants.CostoInventario2,
            'costoventasperdidas8': ventasperdidas8 * Constants.CostoBackorder2,
            'rojocostoventasperdidas8': rojoventasperdidas8 * Constants.CostoBackorder2,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * Constants.CostoInventario2 + ventasperdidas8 * Constants.CostoBackorder2 + setup8,
            'rojototales8': rojoinventariofinal8 * Constants.CostoInventario2 + rojoventasperdidas8 * Constants.CostoBackorder2 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * Constants.CostoInventario2,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * Constants.CostoInventario2,
            'costoventasperdidas9': ventasperdidas9 * Constants.CostoBackorder2,
            'rojocostoventasperdidas9': rojoventasperdidas9 * Constants.CostoBackorder2,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * Constants.CostoInventario2 + ventasperdidas9 * Constants.CostoBackorder2 + setup9,
            'rojototales9': rojoinventariofinal9 * Constants.CostoInventario2 + rojoventasperdidas9 * Constants.CostoBackorder2 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * Constants.CostoInventario2,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * Constants.CostoInventario2,
            'costoventasperdidas10': ventasperdidas10 * Constants.CostoBackorder2,
            'rojocostoventasperdidas10': rojoventasperdidas10 * Constants.CostoBackorder2,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * Constants.CostoInventario2 + ventasperdidas10 * Constants.CostoBackorder2 + setup10,
            'rojototales10': rojoinventariofinal10 * Constants.CostoInventario2 + rojoventasperdidas10 * Constants.CostoBackorder2 + rojosetup4,

            'ventasperdidas11': ventasperdidas11,
            'rojoventasperdidas11': rojoventasperdidas11,
            'costoalmacenamiento11': inventariofinal11 * Constants.CostoInventario2,
            'rojocostoalmacenamiento11': rojoinventariofinal11 * Constants.CostoInventario2,
            'costoventasperdidas11': ventasperdidas11 * Constants.CostoBackorder2,
            'rojocostoventasperdidas11': rojoventasperdidas11 * Constants.CostoBackorder2,
            'setup11': setup11,
            'rojosetup11': rojosetup11,
            'totales11': inventariofinal11 * Constants.CostoInventario2 + ventasperdidas11 * Constants.CostoBackorder2 + setup11,
            'rojototales11': rojoinventariofinal11 * Constants.CostoInventario2 + rojoventasperdidas11 * Constants.CostoBackorder2 + rojosetup11,
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
            'costoalmacenamiento1': inventariofinal1 * Constants.CostoInventario2,
            'rojocostoalmacenamiento1': rojoinventariofinal1 * Constants.CostoInventario2,
            'costoventasperdidas1': ventasperdidas1 * Constants.CostoBackorder2,
            'rojocostoventasperdidas1': rojoventasperdidas1 * Constants.CostoBackorder2,
            'setup1': setup1,
            'rojosetup1': rojosetup1,
            'totales1': inventariofinal1 * Constants.CostoInventario2 + ventasperdidas1 * Constants.CostoBackorder2 + setup1,
            'rojototales1': rojoinventariofinal1 * Constants.CostoInventario2 + rojoventasperdidas1 * Constants.CostoBackorder2 + rojosetup1,

            'ventasperdidas2': ventasperdidas2,
            'rojoventasperdidas2': rojoventasperdidas2,
            'costoalmacenamiento2': inventariofinal2 * Constants.CostoInventario2,
            'rojocostoalmacenamiento2': rojoinventariofinal2 * Constants.CostoInventario2,
            'costoventasperdidas2': ventasperdidas2 * Constants.CostoBackorder2,
            'rojocostoventasperdidas2': rojoventasperdidas2 * Constants.CostoBackorder2,
            'setup2': setup2,
            'rojosetup2': rojosetup2,
            'totales2': inventariofinal2 * Constants.CostoInventario2 + ventasperdidas2 * Constants.CostoBackorder2 + setup2,
            'rojototales2': rojoinventariofinal2 * Constants.CostoInventario2 + rojoventasperdidas2 * Constants.CostoBackorder2 + rojosetup2,

            'ventasperdidas3': ventasperdidas3,
            'rojoventasperdidas3': rojoventasperdidas3,
            'costoalmacenamiento3': inventariofinal3 * Constants.CostoInventario2,
            'rojocostoalmacenamiento3': rojoinventariofinal3 * Constants.CostoInventario2,
            'costoventasperdidas3': ventasperdidas3 * Constants.CostoBackorder2,
            'rojocostoventasperdidas3': rojoventasperdidas3 * Constants.CostoBackorder2,
            'setup3': setup3,
            'rojosetup3': rojosetup3,
            'totales3': inventariofinal3 * Constants.CostoInventario2 + ventasperdidas3 * Constants.CostoBackorder2 + setup3,
            'rojototales3': rojoinventariofinal3 * Constants.CostoInventario2 + rojoventasperdidas3 * Constants.CostoBackorder2 + rojosetup3,

            'ventasperdidas4': ventasperdidas4,
            'rojoventasperdidas4': rojoventasperdidas4,
            'costoalmacenamiento4': inventariofinal4 * Constants.CostoInventario2,
            'rojocostoalmacenamiento4': rojoinventariofinal4 * Constants.CostoInventario2,
            'costoventasperdidas4': ventasperdidas4 * Constants.CostoBackorder2,
            'rojocostoventasperdidas4': rojoventasperdidas4 * Constants.CostoBackorder2,
            'setup4': setup4,
            'rojosetup4': rojosetup4,
            'totales4': inventariofinal4 * Constants.CostoInventario2 + ventasperdidas4 * Constants.CostoBackorder2 + setup4,
            'rojototales4': rojoinventariofinal4 * Constants.CostoInventario2 + rojoventasperdidas4 * Constants.CostoBackorder2 + rojosetup4,

            'ventasperdidas5': ventasperdidas5,
            'rojoventasperdidas5': rojoventasperdidas5,
            'costoalmacenamiento5': inventariofinal5 * Constants.CostoInventario2,
            'rojocostoalmacenamiento5': rojoinventariofinal5 * Constants.CostoInventario2,
            'costoventasperdidas5': ventasperdidas5 * Constants.CostoBackorder2,
            'rojocostoventasperdidas5': rojoventasperdidas5 * Constants.CostoBackorder2,
            'setup5': setup5,
            'rojosetup5': rojosetup5,
            'totales5': inventariofinal5 * Constants.CostoInventario2 + ventasperdidas5 * Constants.CostoBackorder2 + setup5,
            'rojototales5': rojoinventariofinal5 * Constants.CostoInventario2 + rojoventasperdidas5 * Constants.CostoBackorder2 + rojosetup5,

            'ventasperdidas6': ventasperdidas6,
            'rojoventasperdidas6': rojoventasperdidas6,
            'costoalmacenamiento6': inventariofinal6 * Constants.CostoInventario2,
            'rojocostoalmacenamiento6': rojoinventariofinal6 * Constants.CostoInventario2,
            'costoventasperdidas6': ventasperdidas6 * Constants.CostoBackorder2,
            'rojocostoventasperdidas6': rojoventasperdidas6 * Constants.CostoBackorder2,
            'setup6': setup6,
            'rojosetup6': rojosetup6,
            'totales6': inventariofinal6 * Constants.CostoInventario2 + ventasperdidas6 * Constants.CostoBackorder2 + setup6,
            'rojototales6': rojoinventariofinal6 * Constants.CostoInventario2 + rojoventasperdidas6 * Constants.CostoBackorder2 + rojosetup6,

            'ventasperdidas7': ventasperdidas7,
            'rojoventasperdidas7': rojoventasperdidas7,
            'costoalmacenamiento7': inventariofinal7 * Constants.CostoInventario2,
            'rojocostoalmacenamiento7': rojoinventariofinal7 * Constants.CostoInventario2,
            'costoventasperdidas7': ventasperdidas7 * Constants.CostoBackorder2,
            'rojocostoventasperdidas7': rojoventasperdidas7 * Constants.CostoBackorder2,
            'setup7': setup7,
            'rojosetup7': rojosetup7,
            'totales7': inventariofinal7 * Constants.CostoInventario2 + ventasperdidas7 * Constants.CostoBackorder2 + setup7,
            'rojototales7': rojoinventariofinal7 * Constants.CostoInventario2 + rojoventasperdidas7 * Constants.CostoBackorder2 + rojosetup7,

            'ventasperdidas8': ventasperdidas8,
            'rojoventasperdidas8': rojoventasperdidas8,
            'costoalmacenamiento8': inventariofinal8 * Constants.CostoInventario2,
            'rojocostoalmacenamiento8': rojoinventariofinal8 * Constants.CostoInventario2,
            'costoventasperdidas8': ventasperdidas8 * Constants.CostoBackorder2,
            'rojocostoventasperdidas8': rojoventasperdidas8 * Constants.CostoBackorder2,
            'setup8': setup8,
            'rojosetup8': rojosetup8,
            'totales8': inventariofinal8 * Constants.CostoInventario2 + ventasperdidas8 * Constants.CostoBackorder2 + setup8,
            'rojototales8': rojoinventariofinal8 * Constants.CostoInventario2 + rojoventasperdidas8 * Constants.CostoBackorder2 + rojosetup8,

            'ventasperdidas9': ventasperdidas9,
            'rojoventasperdidas9': rojoventasperdidas9,
            'costoalmacenamiento9': inventariofinal9 * Constants.CostoInventario2,
            'rojocostoalmacenamiento9': rojoinventariofinal9 * Constants.CostoInventario2,
            'costoventasperdidas9': ventasperdidas9 * Constants.CostoBackorder2,
            'rojocostoventasperdidas9': rojoventasperdidas9 * Constants.CostoBackorder2,
            'setup9': setup9,
            'rojosetup9': rojosetup9,
            'totales9': inventariofinal9 * Constants.CostoInventario2 + ventasperdidas9 * Constants.CostoBackorder2 + setup9,
            'rojototales9': rojoinventariofinal9 * Constants.CostoInventario2 + rojoventasperdidas9 * Constants.CostoBackorder2 + rojosetup9,

            'ventasperdidas10': ventasperdidas10,
            'rojoventasperdidas10': rojoventasperdidas10,
            'costoalmacenamiento10': inventariofinal10 * Constants.CostoInventario2,
            'rojocostoalmacenamiento10': rojoinventariofinal10 * Constants.CostoInventario2,
            'costoventasperdidas10': ventasperdidas10 * Constants.CostoBackorder2,
            'rojocostoventasperdidas10': rojoventasperdidas10 * Constants.CostoBackorder2,
            'setup10': setup10,
            'rojosetup10': rojosetup10,
            'totales10': inventariofinal10 * Constants.CostoInventario2 + ventasperdidas10 * Constants.CostoBackorder2 + setup10,
            'rojototales10': rojoinventariofinal10 * Constants.CostoInventario2 + rojoventasperdidas10 * Constants.CostoBackorder2 + rojosetup4,

            'ventasperdidas11': ventasperdidas11,
            'rojoventasperdidas11': rojoventasperdidas11,
            'costoalmacenamiento11': inventariofinal11 * Constants.CostoInventario2,
            'rojocostoalmacenamiento11': rojoinventariofinal11 * Constants.CostoInventario2,
            'costoventasperdidas11': ventasperdidas11 * Constants.CostoBackorder2,
            'rojocostoventasperdidas11': rojoventasperdidas11 * Constants.CostoBackorder2,
            'setup11': setup11,
            'rojosetup11': rojosetup11,
            'totales11': inventariofinal11 * Constants.CostoInventario2 + ventasperdidas11 * Constants.CostoBackorder2 + setup11,
            'rojototales11': rojoinventariofinal11 * Constants.CostoInventario2 + rojoventasperdidas11 * Constants.CostoBackorder2 + rojosetup11,

            'ventasperdidas12': ventasperdidas12,
            'rojoventasperdidas12': rojoventasperdidas12,
            'costoalmacenamiento12': inventariofinal12 * Constants.CostoInventario2,
            'rojocostoalmacenamiento12': rojoinventariofinal12 * Constants.CostoInventario2,
            'costoventasperdidas12': ventasperdidas12 * Constants.CostoBackorder2,
            'rojocostoventasperdidas12': rojoventasperdidas12 * Constants.CostoBackorder2,
            'setup12': setup12,
            'rojosetup12': rojosetup12,
            'totales12': inventariofinal12 * Constants.CostoInventario2 + ventasperdidas12 * Constants.CostoBackorder2 + setup12,
            'rojototales12': rojoinventariofinal12 * Constants.CostoInventario2 + rojoventasperdidas12 * Constants.CostoBackorder2 + rojosetup12,
        }


class InicioHanoi (Page):
    pass

class Hanoi1(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi1','RojoProduccionHanoi1']
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
        global inventariofinal1, rojoinventariofinal1,ventasperdidas1,rojoventasperdidas1,setup1,rojosetup1

        inventariofinal1 = max(values['ProduccionHanoi1']+Constants.inventario_inicial3-Constants.HanoiDemanda1, 0)
        rojoinventariofinal1 = max(values['RojoProduccionHanoi1']+Constants.inventario_inicialR3-Constants.rojoHanoiDemanda1, 0)
        ventasperdidas1 = max(Constants.HanoiDemanda1-values['ProduccionHanoi1']-Constants.inventario_inicial3, 0)
        rojoventasperdidas1 = max(Constants.rojoHanoiDemanda1-values['RojoProduccionHanoi1']-Constants.inventario_inicialR3, 0)


        if values["ProduccionHanoi1"]>0:
            setup1=1500
        else:
            setup1=0

        if values["RojoProduccionHanoi1"]>0:
            rojosetup1=1500
        else:
            rojosetup1=0

        if values["ProduccionHanoi1"] + values["RojoProduccionHanoi1"] > 1500:
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


class Hanoi2(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi2','RojoProduccionHanoi2']
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

        if values["ProduccionHanoi2"] + values["RojoProduccionHanoi2"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal2 = max(values['ProduccionHanoi2'] + inventariofinal1 - Constants.HanoiDemanda2, 0)
        rojoinventariofinal2 = max(values['RojoProduccionHanoi2'] + rojoinventariofinal1 - Constants.rojoHanoiDemanda2, 0)
        ventasperdidas2 = max(Constants.HanoiDemanda2 - values['ProduccionHanoi2'] - inventariofinal1, 0)
        rojoventasperdidas2 = max(Constants.rojoHanoiDemanda2 - values['RojoProduccionHanoi2'] - rojoinventariofinal1, 0)

        if values["ProduccionHanoi2"] > 0:
            setup2 = 1500
        else:
            setup2 = 0

        if values["RojoProduccionHanoi2"] > 0:
            rojosetup2 = 1500
        else:
            rojosetup2 = 0


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


class Hanoi3(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi3','RojoProduccionHanoi3']
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

        if values["ProduccionHanoi3"] + values["RojoProduccionHanoi3"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal3 = max(values['ProduccionHanoi3'] + inventariofinal2 - Constants.HanoiDemanda3, 0)
        rojoinventariofinal3 = max(values['RojoProduccionHanoi3'] + rojoinventariofinal2 - Constants.rojoHanoiDemanda3, 0)
        ventasperdidas3 = max(Constants.HanoiDemanda3 - values['ProduccionHanoi3'] - inventariofinal2, 0)
        rojoventasperdidas3 = max(Constants.rojoHanoiDemanda3 - values['RojoProduccionHanoi3'] - rojoinventariofinal2, 0)

        if values["ProduccionHanoi3"] > 0:
            setup3 = 1500
        else:
            setup3 = 0

        if values["RojoProduccionHanoi3"] > 0:
            rojosetup3 = 1500
        else:
            rojosetup3 = 0


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

class Hanoi4(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi4','RojoProduccionHanoi4']
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

        if values["ProduccionHanoi4"] + values["RojoProduccionHanoi4"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal4 = max(values['ProduccionHanoi4'] + inventariofinal3 - Constants.HanoiDemanda4, 0)
        rojoinventariofinal4 = max(values['RojoProduccionHanoi4'] + rojoinventariofinal3 - Constants.rojoHanoiDemanda4, 0)
        ventasperdidas4 = max(Constants.HanoiDemanda4 - values['ProduccionHanoi4'] - inventariofinal3, 0)
        rojoventasperdidas4 = max(Constants.rojoHanoiDemanda4 - values['RojoProduccionHanoi4'] - rojoinventariofinal3, 0)

        if values["ProduccionHanoi4"] > 0:
            setup4 = 1500
        else:
            setup4 = 0

        if values["RojoProduccionHanoi4"] > 0:
            rojosetup4 = 1500
        else:
            rojosetup4 = 0

        if values["ProduccionHanoi4"] + values["RojoProduccionHanoi4"] > 1500:
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

class Hanoi5(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi5','RojoProduccionHanoi5']
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

        if values["ProduccionHanoi5"] + values["RojoProduccionHanoi5"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal5 = max(values['ProduccionHanoi5'] + inventariofinal4 - Constants.HanoiDemanda5, 0)
        rojoinventariofinal5 = max(values['RojoProduccionHanoi5'] + rojoinventariofinal4 - Constants.rojoHanoiDemanda5, 0)
        ventasperdidas5 = max(Constants.HanoiDemanda5 - values['ProduccionHanoi5'] - inventariofinal4, 0)
        rojoventasperdidas5 = max(Constants.rojoHanoiDemanda5 - values['RojoProduccionHanoi5'] - rojoinventariofinal4, 0)

        if values["ProduccionHanoi5"] > 0:
            setup5 = 1500
        else:
            setup5 = 0

        if values["RojoProduccionHanoi5"] > 0:
            rojosetup5 = 1500
        else:
            rojosetup5 = 0

        if values["ProduccionHanoi5"] + values["RojoProduccionHanoi5"] > 1500:
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

class Hanoi6(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi6','RojoProduccionHanoi6']
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
        global inventariofinal6, rojoinventariofinal6, ventasperdidas6, rojoventasperdidas6,setup6,rojosetup6

        if values["ProduccionHanoi6"] + values["RojoProduccionHanoi6"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal6 = max(values['ProduccionHanoi6'] + inventariofinal5 - Constants.HanoiDemanda6, 0)
        rojoinventariofinal6 = max(values['RojoProduccionHanoi6'] + rojoinventariofinal5 - Constants.rojoHanoiDemanda6, 0)
        ventasperdidas6 = max(Constants.HanoiDemanda6 - values['ProduccionHanoi6'] - inventariofinal5, 0)
        rojoventasperdidas6 = max(Constants.rojoHanoiDemanda6 - values['RojoProduccionHanoi6'] - rojoinventariofinal5, 0)

        if values["ProduccionHanoi6"] > 0:
            setup6 = 1500
        else:
            setup6 = 0

        if values["RojoProduccionHanoi6"] > 0:
            rojosetup6 = 1500
        else:
            rojosetup6= 0

        global TotalinventarioHanoi, TotalsetupHanoi, TotalventasHanoi, TotalTotalesHanoi

        TotalinventarioHanoi = (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6) * 5
        TotalinventarioHanoi = TotalinventarioHanoi + (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6) * 5
        TotalsetupHanoi = setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6
        TotalventasHanoi = (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6) * 10
        TotalventasHanoi = TotalventasHanoi + (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6) * 10
        TotalTotalesHanoi = TotalinventarioHanoi + TotalventasHanoi + TotalsetupHanoi

        if values["ProduccionHanoi6"] + values["RojoProduccionHanoi6"] > 1500:
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







class Hanoi7(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi7', 'RojoProduccionHanoi7']
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

        if values["ProduccionHanoi7"] + values["RojoProduccionHanoi7"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal1 = max(values['ProduccionHanoi7'] + inventariofinal6 - Constants.HanoiDemanda7, 0)
        rojoinventariofinal1 = max(values['RojoProduccionHanoi7'] + rojoinventariofinal6 - Constants.rojoHanoiDemanda7, 0)
        ventasperdidas1 = max(Constants.HanoiDemanda7 - values['ProduccionHanoi7'] - inventariofinal6, 0)
        rojoventasperdidas1 = max(Constants.rojoHanoiDemanda7 - values['RojoProduccionHanoi7'] - rojoinventariofinal6, 0)

        if values["ProduccionHanoi7"] > 0:
            setup1 = 1500
        else:
            setup1 = 0

        if values["RojoProduccionHanoi7"] > 0:
            rojosetup1 = 1500
        else:
            rojosetup1 = 0

        if values["ProduccionHanoi7"] + values["RojoProduccionHanoi7"] > 1500:
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

            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
        }


class Hanoi8(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi8', 'RojoProduccionHanoi8']
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
        global inventariofinal2, rojoinventariofinal2, ventasperdidas2, rojoventasperdidas2, setup2, rojosetup2
        if values["ProduccionHanoi8"] + values["RojoProduccionHanoi8"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal2 = max(values['ProduccionHanoi8'] + inventariofinal1 - Constants.HanoiDemanda8, 0)
        rojoinventariofinal2 = max(values['RojoProduccionHanoi8'] + rojoinventariofinal1 - Constants.rojoHanoiDemanda8, 0)
        ventasperdidas2 = max(Constants.HanoiDemanda8 - values['ProduccionHanoi8'] - inventariofinal1, 0)
        rojoventasperdidas2 = max(Constants.rojoHanoiDemanda8 - values['RojoProduccionHanoi8'] - rojoinventariofinal1, 0)

        if values["ProduccionHanoi8"] > 0:
            setup2 = 1500
        else:
            setup2 = 0

        if values["RojoProduccionHanoi8"] > 0:
            rojosetup2 = 1500
        else:
            rojosetup2 = 0


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

            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
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

class Hanoi9(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi9', 'RojoProduccionHanoi9']
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
        global inventariofinal3, rojoinventariofinal3, ventasperdidas3, rojoventasperdidas3, setup3, rojosetup3
        if values["ProduccionHanoi9"] + values["RojoProduccionHanoi9"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal3 = max(values['ProduccionHanoi9'] + inventariofinal2 - Constants.HanoiDemanda9, 0)
        rojoinventariofinal3 = max(values['RojoProduccionHanoi9'] + rojoinventariofinal2 - Constants.rojoHanoiDemanda9, 0)
        ventasperdidas3 = max(Constants.HanoiDemanda9 - values['ProduccionHanoi9'] - inventariofinal2, 0)
        rojoventasperdidas3 = max(Constants.rojoHanoiDemanda9 - values['RojoProduccionHanoi9'] - rojoinventariofinal2, 0)

        if values["ProduccionHanoi9"] > 0:
            setup3 = 1500
        else:
            setup3 = 0

        if values["RojoProduccionHanoi9"] > 0:
            rojosetup3 = 1500
        else:
            rojosetup3 = 0


    def vars_for_template(self):
        return {
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


            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
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


class Hanoi10(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi10', 'RojoProduccionHanoi10']
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
        global inventariofinal4, rojoinventariofinal4, ventasperdidas4, rojoventasperdidas4, setup4, rojosetup4
        if values["ProduccionHanoi10"] + values["RojoProduccionHanoi10"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal4 = max(values['ProduccionHanoi10'] + inventariofinal3 - Constants.HanoiDemanda10, 0)
        rojoinventariofinal4 = max(values['RojoProduccionHanoi10'] + rojoinventariofinal3 - Constants.rojoHanoiDemanda10, 0)
        ventasperdidas4 = max(Constants.HanoiDemanda10 - values['ProduccionHanoi10'] - inventariofinal3, 0)
        rojoventasperdidas4 = max(Constants.rojoHanoiDemanda10 - values['RojoProduccionHanoi10'] - rojoinventariofinal3, 0)

        if values["ProduccionHanoi10"] > 0:
            setup4 = 1500
        else:
            setup4 = 0

        if values["RojoProduccionHanoi10"] > 0:
            rojosetup4 = 1500
        else:
            rojosetup4 = 0

        if values["ProduccionHanoi10"] + values["RojoProduccionHanoi10"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return {
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


            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
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


class Hanoi11(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi11', 'RojoProduccionHanoi11']
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
        global inventariofinal5, rojoinventariofinal5, ventasperdidas5, rojoventasperdidas5, setup5, rojosetup5
        if values["ProduccionHanoi11"] + values["RojoProduccionHanoi11"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal5 = max(values['ProduccionHanoi11'] + inventariofinal4 - Constants.HanoiDemanda11, 0)
        rojoinventariofinal5 = max(values['RojoProduccionHanoi11'] + rojoinventariofinal4 - Constants.rojoHanoiDemanda11, 0)
        ventasperdidas5 = max(Constants.HanoiDemanda11 - values['ProduccionHanoi11'] - inventariofinal4, 0)
        rojoventasperdidas5 = max(Constants.rojoHanoiDemanda11 - values['RojoProduccionHanoi11'] - rojoinventariofinal4, 0)

        if values["ProduccionHanoi11"] > 0:
            setup5 = 1500
        else:
            setup5 = 0

        if values["RojoProduccionHanoi11"] > 0:
            rojosetup5 = 1500
        else:
            rojosetup5 = 0

        if values["ProduccionHanoi11"] + values["RojoProduccionHanoi11"] > 1500:
            return ' La produccion no debe pasar de 1500'


    def vars_for_template(self):

        return {
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


            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
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


class Hanoi12(Page):
    form_model = 'player'
    form_fields = ['ProduccionHanoi12', 'RojoProduccionHanoi12']
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

        global inventariofinal6, rojoinventariofinal6, ventasperdidas6, rojoventasperdidas6, setup6, rojosetup6
        global TotalinventarioHanoi,TotalsetupHanoi,TotalventasHanoi,TotalTotalesHanoi

        if values["ProduccionHanoi12"] + values["RojoProduccionHanoi12"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal6 = max(values['ProduccionHanoi12'] + inventariofinal5 - Constants.HanoiDemanda12, 0)
        rojoinventariofinal6 = max(values['RojoProduccionHanoi12'] + rojoinventariofinal5 - Constants.rojoHanoiDemanda12, 0)
        ventasperdidas6 = max(Constants.HanoiDemanda12 - values['ProduccionHanoi12'] - inventariofinal5, 0)
        rojoventasperdidas6 = max(Constants.rojoHanoiDemanda12 - values['RojoProduccionHanoi12'] - rojoinventariofinal5, 0)

        if values["ProduccionHanoi12"] > 0:
            setup6 = 1500
        else:
            setup6 = 0

        if values["RojoProduccionHanoi12"] > 0:
            rojosetup6 = 1500
        else:
            rojosetup6 = 0

        TotalinventarioHanoi = TotalinventarioHanoi + (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6) * 5
        TotalinventarioHanoi = TotalinventarioHanoi + (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6) * 5
        TotalsetupHanoi = TotalsetupHanoi + setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6
        TotalventasHanoi = TotalventasHanoi + (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6) * 10
        TotalventasHanoi = TotalventasHanoi + (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6) * 10
        TotalTotalesHanoi = TotalinventarioHanoi + TotalventasHanoi + TotalsetupHanoi


        if values["ProduccionHanoi12"] + values["RojoProduccionHanoi12"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):


        return {
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


            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
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

class ResumenHanoi(Page):
    def vars_for_template(self):
        return{
            'TotalTotales': TotalTotalesHanoi
        }




class InicioMexico (Page):
    pass

class Mexico1(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico1','RojoProduccionMexico1']
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
        global inventariofinal1, rojoinventariofinal1,ventasperdidas1,rojoventasperdidas1,setup1,rojosetup1

        inventariofinal1 = max(values['ProduccionMexico1']+Constants.inventario_inicial4-Constants.MexicoDemanda1, 0)
        rojoinventariofinal1 = max(values['RojoProduccionMexico1']+Constants.inventario_inicialR4-Constants.rojoMexicoDemanda1, 0)
        ventasperdidas1 = max(Constants.MexicoDemanda1-values['ProduccionMexico1']-Constants.inventario_inicial4, 0)
        rojoventasperdidas1 = max(Constants.rojoMexicoDemanda1-values['RojoProduccionMexico1']-Constants.inventario_inicialR4, 0)


        if values["ProduccionMexico1"]>0:
            setup1=1500
        else:
            setup1=0

        if values["RojoProduccionMexico1"]>0:
            rojosetup1=1500
        else:
            rojosetup1=0

        if values["ProduccionMexico1"] + values["RojoProduccionMexico1"] > 1500:
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


class Mexico2(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico2','RojoProduccionMexico2']
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

        if values["ProduccionMexico2"] + values["RojoProduccionMexico2"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal2 = max(values['ProduccionMexico2'] + inventariofinal1 - Constants.MexicoDemanda2, 0)
        rojoinventariofinal2 = max(values['RojoProduccionMexico2'] + rojoinventariofinal1 - Constants.rojoMexicoDemanda2, 0)
        ventasperdidas2 = max(Constants.MexicoDemanda2 - values['ProduccionMexico2'] - inventariofinal1, 0)
        rojoventasperdidas2 = max(Constants.rojoMexicoDemanda2 - values['RojoProduccionMexico2'] - rojoinventariofinal1, 0)

        if values["ProduccionMexico2"] > 0:
            setup2 = 1500
        else:
            setup2 = 0

        if values["RojoProduccionMexico2"] > 0:
            rojosetup2 = 1500
        else:
            rojosetup2 = 0


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


class Mexico3(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico3','RojoProduccionMexico3']
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

        if values["ProduccionMexico3"] + values["RojoProduccionMexico3"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal3 = max(values['ProduccionMexico3'] + inventariofinal2 - Constants.MexicoDemanda3, 0)
        rojoinventariofinal3 = max(values['RojoProduccionMexico3'] + rojoinventariofinal2 - Constants.rojoMexicoDemanda3, 0)
        ventasperdidas3 = max(Constants.MexicoDemanda3 - values['ProduccionMexico3'] - inventariofinal2, 0)
        rojoventasperdidas3 = max(Constants.rojoMexicoDemanda3 - values['RojoProduccionMexico3'] - rojoinventariofinal2, 0)

        if values["ProduccionMexico3"] > 0:
            setup3 = 1500
        else:
            setup3 = 0

        if values["RojoProduccionMexico3"] > 0:
            rojosetup3 = 1500
        else:
            rojosetup3 = 0


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

class Mexico4(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico4','RojoProduccionMexico4']
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

        if values["ProduccionMexico4"] + values["RojoProduccionMexico4"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal4 = max(values['ProduccionMexico4'] + inventariofinal3 - Constants.MexicoDemanda4, 0)
        rojoinventariofinal4 = max(values['RojoProduccionMexico4'] + rojoinventariofinal3 - Constants.rojoMexicoDemanda4, 0)
        ventasperdidas4 = max(Constants.MexicoDemanda4 - values['ProduccionMexico4'] - inventariofinal3, 0)
        rojoventasperdidas4 = max(Constants.rojoMexicoDemanda4 - values['RojoProduccionMexico4'] - rojoinventariofinal3, 0)

        if values["ProduccionMexico4"] > 0:
            setup4 = 1500
        else:
            setup4 = 0

        if values["RojoProduccionMexico4"] > 0:
            rojosetup4 = 1500
        else:
            rojosetup4 = 0

        if values["ProduccionMexico4"] + values["RojoProduccionMexico4"] > 1500:
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

class Mexico5(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico5','RojoProduccionMexico5']
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

        if values["ProduccionMexico5"] + values["RojoProduccionMexico5"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal5 = max(values['ProduccionMexico5'] + inventariofinal4 - Constants.MexicoDemanda5, 0)
        rojoinventariofinal5 = max(values['RojoProduccionMexico5'] + rojoinventariofinal4 - Constants.rojoMexicoDemanda5, 0)
        ventasperdidas5 = max(Constants.MexicoDemanda5 - values['ProduccionMexico5'] - inventariofinal4, 0)
        rojoventasperdidas5 = max(Constants.rojoMexicoDemanda5 - values['RojoProduccionMexico5'] - rojoinventariofinal4, 0)

        if values["ProduccionMexico5"] > 0:
            setup5 = 1500
        else:
            setup5 = 0

        if values["RojoProduccionMexico5"] > 0:
            rojosetup5 = 1500
        else:
            rojosetup5 = 0

        if values["ProduccionMexico5"] + values["RojoProduccionMexico5"] > 1500:
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

class Mexico6(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico6','RojoProduccionMexico6']
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
        global inventariofinal6, rojoinventariofinal6, ventasperdidas6, rojoventasperdidas6,setup6,rojosetup6

        if values["ProduccionMexico6"] + values["RojoProduccionMexico6"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal6 = max(values['ProduccionMexico6'] + inventariofinal5 - Constants.MexicoDemanda6, 0)
        rojoinventariofinal6 = max(values['RojoProduccionMexico6'] + rojoinventariofinal5 - Constants.rojoMexicoDemanda6, 0)
        ventasperdidas6 = max(Constants.MexicoDemanda6 - values['ProduccionMexico6'] - inventariofinal5, 0)
        rojoventasperdidas6 = max(Constants.rojoMexicoDemanda6 - values['RojoProduccionMexico6'] - rojoinventariofinal5, 0)

        if values["ProduccionMexico6"] > 0:
            setup6 = 1500
        else:
            setup6 = 0

        if values["RojoProduccionMexico6"] > 0:
            rojosetup6 = 1500
        else:
            rojosetup6= 0

        global TotalinventarioMexico, TotalsetupMexico, TotalventasMexico, TotalTotalesMexico

        TotalinventarioMexico = (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6) * 5
        TotalinventarioMexico = TotalinventarioMexico + (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6) * 5
        TotalsetupMexico = setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6
        TotalventasMexico = (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6) * 10
        TotalventasMexico = TotalventasMexico + (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6) * 10
        TotalTotalesMexico = TotalinventarioMexico + TotalventasMexico + TotalsetupMexico

        if values["ProduccionMexico6"] + values["RojoProduccionMexico6"] > 1500:
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







class Mexico7(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico7', 'RojoProduccionMexico7']
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

        if values["ProduccionMexico7"] + values["RojoProduccionMexico7"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal1 = max(values['ProduccionMexico7'] + inventariofinal6 - Constants.MexicoDemanda7, 0)
        rojoinventariofinal1 = max(values['RojoProduccionMexico7'] + rojoinventariofinal6 - Constants.rojoMexicoDemanda7, 0)
        ventasperdidas1 = max(Constants.MexicoDemanda7 - values['ProduccionMexico7'] - inventariofinal6, 0)
        rojoventasperdidas1 = max(Constants.rojoMexicoDemanda7 - values['RojoProduccionMexico7'] - rojoinventariofinal6, 0)

        if values["ProduccionMexico7"] > 0:
            setup1 = 1500
        else:
            setup1 = 0

        if values["RojoProduccionMexico7"] > 0:
            rojosetup1 = 1500
        else:
            rojosetup1 = 0

        if values["ProduccionMexico7"] + values["RojoProduccionMexico7"] > 1500:
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


            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
        }


class Mexico8(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico8', 'RojoProduccionMexico8']
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
        global inventariofinal2, rojoinventariofinal2, ventasperdidas2, rojoventasperdidas2, setup2, rojosetup2
        if values["ProduccionMexico8"] + values["RojoProduccionMexico8"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal2 = max(values['ProduccionMexico8'] + inventariofinal1 - Constants.MexicoDemanda8, 0)
        rojoinventariofinal2 = max(values['RojoProduccionMexico8'] + rojoinventariofinal1 - Constants.rojoMexicoDemanda8, 0)
        ventasperdidas2 = max(Constants.MexicoDemanda8 - values['ProduccionMexico8'] - inventariofinal1, 0)
        rojoventasperdidas2 = max(Constants.rojoMexicoDemanda8 - values['RojoProduccionMexico8'] - rojoinventariofinal1, 0)

        if values["ProduccionMexico8"] > 0:
            setup2 = 1500
        else:
            setup2 = 0

        if values["RojoProduccionMexico8"] > 0:
            rojosetup2 = 1500
        else:
            rojosetup2 = 0


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


            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
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

class Mexico9(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico9', 'RojoProduccionMexico9']
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
        global inventariofinal3, rojoinventariofinal3, ventasperdidas3, rojoventasperdidas3, setup3, rojosetup3
        if values["ProduccionMexico9"] + values["RojoProduccionMexico9"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal3 = max(values['ProduccionMexico9'] + inventariofinal2 - Constants.MexicoDemanda9, 0)
        rojoinventariofinal3 = max(values['RojoProduccionMexico9'] + rojoinventariofinal2 - Constants.rojoMexicoDemanda9, 0)
        ventasperdidas3 = max(Constants.MexicoDemanda9 - values['ProduccionMexico9'] - inventariofinal2, 0)
        rojoventasperdidas3 = max(Constants.rojoMexicoDemanda9 - values['RojoProduccionMexico9'] - rojoinventariofinal2, 0)

        if values["ProduccionMexico9"] > 0:
            setup3 = 1500
        else:
            setup3 = 0

        if values["RojoProduccionMexico9"] > 0:
            rojosetup3 = 1500
        else:
            rojosetup3 = 0


    def vars_for_template(self):
        return {
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


            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
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


class Mexico10(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico10', 'RojoProduccionMexico10']
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
        global inventariofinal4, rojoinventariofinal4, ventasperdidas4, rojoventasperdidas4, setup4, rojosetup4
        if values["ProduccionMexico10"] + values["RojoProduccionMexico10"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal4 = max(values['ProduccionMexico10'] + inventariofinal3 - Constants.MexicoDemanda10, 0)
        rojoinventariofinal4 = max(values['RojoProduccionMexico10'] + rojoinventariofinal3 - Constants.rojoMexicoDemanda10, 0)
        ventasperdidas4 = max(Constants.MexicoDemanda10 - values['ProduccionMexico10'] - inventariofinal3, 0)
        rojoventasperdidas4 = max(Constants.rojoMexicoDemanda10 - values['RojoProduccionMexico10'] - rojoinventariofinal3, 0)

        if values["ProduccionMexico10"] > 0:
            setup4 = 1500
        else:
            setup4 = 0

        if values["RojoProduccionMexico10"] > 0:
            rojosetup4 = 1500
        else:
            rojosetup4 = 0

        if values["ProduccionMexico10"] + values["RojoProduccionMexico10"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):
        return {
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


            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
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


class Mexico11(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico11', 'RojoProduccionMexico11']
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
        global inventariofinal5, rojoinventariofinal5, ventasperdidas5, rojoventasperdidas5, setup5, rojosetup5
        if values["ProduccionMexico11"] + values["RojoProduccionMexico11"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal5 = max(values['ProduccionMexico11'] + inventariofinal4 - Constants.MexicoDemanda11, 0)
        rojoinventariofinal5 = max(values['RojoProduccionMexico11'] + rojoinventariofinal4 - Constants.rojoMexicoDemanda11, 0)
        ventasperdidas5 = max(Constants.MexicoDemanda11 - values['ProduccionMexico11'] - inventariofinal4, 0)
        rojoventasperdidas5 = max(Constants.rojoMexicoDemanda11 - values['RojoProduccionMexico11'] - rojoinventariofinal4, 0)

        if values["ProduccionMexico11"] > 0:
            setup5 = 1500
        else:
            setup5 = 0

        if values["RojoProduccionMexico11"] > 0:
            rojosetup5 = 1500
        else:
            rojosetup5 = 0

        if values["ProduccionMexico11"] + values["RojoProduccionMexico11"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):

        return {
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


            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
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


class Mexico12(Page):
    form_model = 'player'
    form_fields = ['ProduccionMexico12', 'RojoProduccionMexico12']

    def error_message(self, values):

        global inventariofinal6, rojoinventariofinal6, ventasperdidas6, rojoventasperdidas6, setup6, rojosetup6
        global TotalinventarioMexico,TotalsetupMexico,TotalventasMexico,TotalTotalesMexico

        if values["ProduccionMexico12"] + values["RojoProduccionMexico12"] > 1500:
            return ' La produccion no debe pasar de 1500'

        inventariofinal6 = max(values['ProduccionMexico12'] + inventariofinal5 - Constants.MexicoDemanda12, 0)
        rojoinventariofinal6 = max(values['RojoProduccionMexico12'] + rojoinventariofinal5 - Constants.rojoMexicoDemanda12, 0)
        ventasperdidas6 = max(Constants.MexicoDemanda12 - values['ProduccionMexico12'] - inventariofinal5, 0)
        rojoventasperdidas6 = max(Constants.rojoMexicoDemanda12 - values['RojoProduccionMexico12'] - rojoinventariofinal5, 0)

        if values["ProduccionMexico12"] > 0:
            setup6 = 1500
        else:
            setup6 = 0

        if values["RojoProduccionMexico12"] > 0:
            rojosetup6 = 1500
        else:
            rojosetup6 = 0

        TotalinventarioMexico = TotalinventarioMexico + (inventariofinal1 + inventariofinal2 + inventariofinal3 + inventariofinal4 + inventariofinal5 + inventariofinal6) * 5
        TotalinventarioMexico = TotalinventarioMexico + (rojoinventariofinal1 + rojoinventariofinal2 + rojoinventariofinal3 + rojoinventariofinal4 + rojoinventariofinal5 + rojoinventariofinal6) * 5
        TotalsetupMexico = TotalsetupMexico + setup1 + setup2 + setup3 + setup4 + setup5 + setup6 + rojosetup1 + rojosetup2 + rojosetup3 + rojosetup4 + rojosetup5 + rojosetup6
        TotalventasMexico = TotalventasMexico + (ventasperdidas1 + ventasperdidas2 + ventasperdidas3 + ventasperdidas4 + ventasperdidas5 + ventasperdidas6) * 10
        TotalventasMexico = TotalventasMexico + (rojoventasperdidas1 + rojoventasperdidas2 + rojoventasperdidas3 + rojoventasperdidas4 + rojoventasperdidas5 + rojoventasperdidas6) * 10
        TotalTotalesMexico = TotalinventarioMexico + TotalventasMexico + TotalsetupMexico


        if values["ProduccionMexico12"] + values["RojoProduccionMexico12"] > 1500:
            return ' La produccion no debe pasar de 1500'

    def vars_for_template(self):


        return {
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


            'inventario1': inventariofinal6,
            'rojoinventario1': rojoinventariofinal6,
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

class ResumenMexico(Page):
    def vars_for_template(self):
        return{
            'TotalTotales': TotalTotalesMexico
        }



class ResumenTotal(Page):
    def vars_for_template(self):
        return{
            'TotalTotales1': TotalTotalesLima,
            'TotalTotales2': TotalTotalesJapon,
            'TotalTotales3': TotalTotalesHanoi,
            'TotalTotales4': TotalTotalesMexico,
            'TotalTotales5': TotalTotalesLima+TotalTotalesJapon+TotalTotalesHanoi+TotalTotalesMexico
        }


class ResultsWaitPage(WaitPage):
    pass




class Results(Page):
    pass


page_sequence = [
# Inicio1,
#     Inicio2,
#     Inicio3,
#     Inicio6,
#     Inicio4,
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

# InicioHanoi,
#     Hanoi1,
#     Hanoi2,
#     Hanoi3,
#     Hanoi4,
#     Hanoi5,
#     Hanoi6,
#     Hanoi7,
#     Hanoi8,
#     Hanoi9,
#     Hanoi10,
#     Hanoi11,
#     Hanoi12,
#     ResumenHanoi,

# InicioMexico,
#     Mexico1,
#     Mexico2,
#     Mexico3,
#     Mexico4,
#     Mexico5,
#     Mexico6,
#     Mexico7,
#     Mexico8,
#     Mexico9,
#     Mexico10,
#     Mexico11,
#     Mexico12,
#     ResumenMexico,

    # ResumenTotal,














]
