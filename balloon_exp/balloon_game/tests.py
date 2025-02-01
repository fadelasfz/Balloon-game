from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import requests

# BASE_URL='http://127.0.0.8000' <<< Url with port malformed
BASE_URL='http://172.20.10.3:8000'
ENDPOINT='api/'

class PlayerBot(Bot):
    def play_round(self):
        if (self.player.round_number == 1):
            yield Introduction
        yield Tabs
        if (self.player.round_number == 1):
            yield PracticeBalloon, dict(ball_practice=0)
        if is_displayed1(self.player):
            yield Balloon, dict(ball=0)
        if (self.player.is_finished):
            yield CombinedResults
        if (self.player.round_number == 1):
            yield PracticeFeedback

