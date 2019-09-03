from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Alex Dyer'

doc = """
Es un juego para evaluar la cantidad de ocntribucion en competencia con otros
"""


class Constants(BaseConstants):
    name_in_url = 'my_simple_survey2'
    players_per_group =3
    num_rounds = 1
    endowment = c(1000)
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label="How much will you contribute?"
    )
