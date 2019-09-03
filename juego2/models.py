from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Alex Dyer'

doc = """
juego2
"""


class Constants(BaseConstants):
    name_in_url = 'juego2'
    players_per_group = 2
    num_rounds = 1
    endowment = 10
    multiplication_factor = 3



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        label="How much do you want to send to participant B?"
    )
    sent_back_amount = models.CurrencyField(
        label="How much do you want to send back?"
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Player(BasePlayer):
    sent_amount = models.CurrencyField()
    sent_back_amount = models.CurrencyField()
