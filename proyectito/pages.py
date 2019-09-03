from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass

class pagina1(Page):
    pass






page_sequence = [
    pagina1,
    MyPage,
    ResultsWaitPage,
    Results
]
