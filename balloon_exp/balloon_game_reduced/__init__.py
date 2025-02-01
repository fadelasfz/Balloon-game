import random
import time
import csv

from otree.api import *

doc = """Jeu: Devine le point de rupture du ballon"""


class C(BaseConstants):
    NAME_IN_URL = 'balloon_experiment_reduced'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 100
    TIMER_TEXT = "Il vous reste : "
    PAYMENT_PER_CORRECT_ANSWER = cu(1000)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# class Product(ExtraModel):
#     nom_complet_2 = models.StringField()
#     # price = models.FloatField()
#     # is_organic = models.BooleanField()


class Player(BasePlayer):
    ball = models.IntegerField(
        label='',
        blank=True,
        # widget=widgets.RadioSelectHorizontal,
        # choices=range(1, 21, 1),
        # help_text='Vous pouvez directement entrer un nombre entre 1 et 20 ici',
    )
    ball_practice = models.IntegerField(
        label='',
        blank=True
    )
    nb_failed_attempts = models.IntegerField(initial=0)
    solution_to_find = models.IntegerField()
    solution_to_find_practice = models.IntegerField()
    found_solution = models.BooleanField(initial=False)
    found_solution_practice = models.BooleanField(initial=False)
    is_finished = models.BooleanField(initial=False)
    is_finished_practice = models.BooleanField(initial=False)
    combined_payoff_currency = models.IntegerField()
    end_game = models.BooleanField(initial=False)


def get_timeout_seconds1(player: Player):
    participant = player.participant
    import time
    return participant.expiry - time.time()


# PAGES

## Introduction
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return (player.round_number == 1)



## Baloon pages
class PracticeBalloon(Page):
    form_model = 'player'
    form_fields = ['ball_practice']

    @staticmethod
    def js_vars(player: Player):
        return dict(
            round_number_practice=player.round_number,
        )

    @staticmethod
    def live_method(player, data):
        player.solution_to_find_practice = data['solution_to_find_practice']
        player.found_solution_practice = data['found_solution_practice']

    @staticmethod
    def is_displayed(player: Player):
        return (player.round_number == 1)


## Baloon pages
class Balloon(Page):
    form_model = 'player'
    form_fields = ['ball']

    timer_text = C.TIMER_TEXT

    @staticmethod
    def vars_for_template(player: Player):
        if 'round_start_time' not in player.participant.vars:
            player.participant.vars['round_start_time'] = time.time()
            player.participant.vars['current_time_limit'] = 120

        current_time = time.time()
        elapsed_time = current_time - player.participant.vars['round_start_time']
        remaining_time = player.participant.vars['current_time_limit'] - elapsed_time
        return dict(remaining_time=remaining_time, elapsed_time=elapsed_time, current_time=current_time)

    @staticmethod
    def get_timeout_seconds(player: Player):
        current_time = time.time()
        elapsed_time = current_time - player.participant.vars['round_start_time']
        remaining_time = player.participant.vars['current_time_limit'] - elapsed_time
        return max(remaining_time, 0)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time

        participant.expiry = time.time() + 120
        if (timeout_happened):
            player.is_finished = True
        if (player.round_number == C.NUM_ROUNDS):
            player.is_finished = True

    @staticmethod
    def js_vars(player: Player):
        return dict(
            round_number=player.round_number,
        )

    @staticmethod
    def live_method(player, data):
        player.nb_failed_attempts = data['count']
        player.solution_to_find = data['solution_to_find']
        player.found_solution = data['found_solution']

        if (data['found_solution']):
            player.payoff = 1

        # Update remaining time after submission
        current_time = time.time()
        elapsed_time = current_time - player.participant.vars['round_start_time']
        remaining_time = player.participant.vars['current_time_limit'] - elapsed_time
        return remaining_time

    @staticmethod
    def is_displayed1(player: Player):
        """only returns True if there is time left."""
        return get_timeout_seconds1(player) > 0

    # @staticmethod
    # def is_displayed(player: Player):
    #     return (not player.end_game)


class CombinedResults(Page):
    @staticmethod
    def is_displayed(player: Player):
        return (player.is_finished)

    @staticmethod
    def vars_for_template(player: Player):
        all_players = player.in_all_rounds()
        combined_payoff = 0
        for temp_player in all_players:
            combined_payoff += temp_player.payoff
        player.combined_payoff_currency = int(combined_payoff) * 500
        return {
            "combined_payoff": combined_payoff
        }


class PracticeFeedback(Page):
    @staticmethod
    def is_displayed(player: Player):
        return (player.round_number == 1)


# class EndGame(Page):
#     @staticmethod
#     def is_displayed(player: Player):
#         return (player.end_game)


page_sequence = [Introduction]