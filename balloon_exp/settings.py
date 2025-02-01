from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. session.config['participation_fee']

DEBUG = False

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=500.00, participation_fee=0.00, doc=""
)

# ALLOWED_HOSTS = ['.localhost', '127.0.0.1']

SESSION_CONFIGS = [
    dict(
        name='balloon_game',
        display_name='Deviner le point de rupture de ballons',
        num_demo_participants=1,
        app_sequence=['balloon_game'],
    ),
    # dict(
    #     name='are_you_sure',
    #     display_name='Are you sure',
    #     num_demo_participants=1,
    #     app_sequence=['are_you_sure'],
    # ),
    # dict(
    #     name='balloon_game_reduced',
    #     display_name='Balloon reduced',
    #     num_demo_participants=1,
    #     app_sequence=['balloon_game_reduced'],
    # ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'fr'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'FCFA'
USE_POINTS = True

ROOMS = [
    dict(
        name='participant1',
        display_name='Participant 1',
        participant_label_file='_rooms/participant1.txt',
        use_secure_urls=True
    ),
    dict(
        name='participant2',
        display_name='Participant 2',
        participant_label_file='_rooms/participant2.txt',
        use_secure_urls=True
    ),
    dict(
        name='participant3',
        display_name='Participant 3',
        participant_label_file='_rooms/participant3.txt',
        use_secure_urls=True
    ),
    dict(
        name='participant4',
        display_name='Participant 4',
        participant_label_file='_rooms/participant4.txt',
        use_secure_urls=True
    ),
    dict(
        name='participant5',
        display_name='Participant 5',
        participant_label_file='_rooms/participant5.txt',
        use_secure_urls=True
    ),
    dict(
        name='participant6',
        display_name='Participant 6',
        participant_label_file='_rooms/participant6.txt',
        use_secure_urls=True
    ),
    dict(
        name='participant7',
        display_name='Participant 7',
        participant_label_file='_rooms/participant7.txt',
        use_secure_urls=True
    ),
    dict(
        name='participant8',
        display_name='Participant 8',
        participant_label_file='_rooms/participant8.txt',
        use_secure_urls=True
    ),
    dict(
        name='participant9',
        display_name='Participant 9',
        participant_label_file='_rooms/participant9.txt',
        use_secure_urls=True
    ),
    dict(
        name='participant10',
        display_name='Participant 10',
        participant_label_file='_rooms/participant10.txt',
        use_secure_urls=True
    ),
    dict(
        name='participant11',
        display_name='Participant 11',
        participant_label_file='_rooms/participant11.txt',
        use_secure_urls=True
    ),
    dict(
        name='participant12',
        display_name='Participant 12',
        participant_label_file='_rooms/participant12.txt',
        use_secure_urls=True
    ),
    # dict(
    #     name='participant13',
    #     display_name='Participant 13',
    #     participant_label_file='_rooms/participant13.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant14',
    #     display_name='Participant 14',
    #     participant_label_file='_rooms/participant14.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant15',
    #     display_name='Participant 15',
    #     participant_label_file='_rooms/participant15.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant16',
    #     display_name='Participant 16',
    #     participant_label_file='_rooms/participant16.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant17',
    #     display_name='Participant 17',
    #     participant_label_file='_rooms/participant17.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant18',
    #     display_name='Participant 18',
    #     participant_label_file='_rooms/participant18.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant19',
    #     display_name='Participant 19',
    #     participant_label_file='_rooms/participant19.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant20',
    #     display_name='Participant 20',
    #     participant_label_file='_rooms/participant20.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant21',
    #     display_name='Participant 21',
    #     participant_label_file='_rooms/participant21.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant22',
    #     display_name='Participant 22',
    #     participant_label_file='_rooms/participant22.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant23',
    #     display_name='Participant 23',
    #     participant_label_file='_rooms/participant23.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant24',
    #     display_name='Participant 24',
    #     participant_label_file='_rooms/participant24.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant25',
    #     display_name='Participant 25',
    #     participant_label_file='_rooms/participant25.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant26',
    #     display_name='Participant 26',
    #     participant_label_file='_rooms/participant26.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant27',
    #     display_name='Participant 27',
    #     participant_label_file='_rooms/participant27.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant28',
    #     display_name='Participant 28',
    #     participant_label_file='_rooms/participant28.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant29',
    #     display_name='Participant 29',
    #     participant_label_file='_rooms/participant29.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant30',
    #     display_name='Participant 30',
    #     participant_label_file='_rooms/participant30.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant31',
    #     display_name='Participant 31',
    #     participant_label_file='_rooms/participant31.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant32',
    #     display_name='Participant 32',
    #     participant_label_file='_rooms/participant32.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant33',
    #     display_name='Participant 33',
    #     participant_label_file='_rooms/participant33.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant34',
    #     display_name='Participant 34',
    #     participant_label_file='_rooms/participant34.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant35',
    #     display_name='Participant 35',
    #     participant_label_file='_rooms/participant35.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant36',
    #     display_name='Participant 36',
    #     participant_label_file='_rooms/participant36.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant37',
    #     display_name='Participant 37',
    #     participant_label_file='_rooms/participant37.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant38',
    #     display_name='Participant 38',
    #     participant_label_file='_rooms/participant38.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant39',
    #     display_name='Participant 39',
    #     participant_label_file='_rooms/participant39.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant40',
    #     display_name='Participant 40',
    #     participant_label_file='_rooms/participant40.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant41',
    #     display_name='Participant 41',
    #     participant_label_file='_rooms/participant41.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant42',
    #     display_name='Participant 42',
    #     participant_label_file='_rooms/participant42.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant39',
    #     display_name='Participant 39',
    #     participant_label_file='_rooms/participant39.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant43',
    #     display_name='Participant 43',
    #     participant_label_file='_rooms/participant43.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant44',
    #     display_name='Participant 44',
    #     participant_label_file='_rooms/participant44.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant45',
    #     display_name='Participant 45',
    #     participant_label_file='_rooms/participant45.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant46',
    #     display_name='Participant 46',
    #     participant_label_file='_rooms/participant46.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant47',
    #     display_name='Participant 47',
    #     participant_label_file='_rooms/participant47.txt',
    #     use_secure_urls=True
    # ),
    # dict(
    #     name='participant48',
    #     display_name='Participant 48',
    #     participant_label_file='_rooms/participant48.txt',
    #     use_secure_urls=True
    # ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin passwordInput in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')



DEMO_PAGE_TITLE = """
JOUEZ AUX BALLONS
"""

DEMO_PAGE_INTRO_HTML = """
BALLONS
"""


# don't share this with anybody.
SECRET_KEY = 'fnv*lfr%ghepfge1rg1a56t0sj+9d*p&1+&g%q@j!ju@zu^v@6'

SESSION_FIELDS = [
    'completions_by_treatment',
    'past_groups',
    'matrices',
    'wait_for_ids',
    'arrived_ids',
]

PARTICIPANT_FIELDS = [
    'app_payoffs',
    'expiry',
    'finished_rounds',
    'language',
    'num_rounds',
    'partner_history',
    'past_group_id',
    'progress',
    'quiz_num_correct',
    'selected_round',
    'task_rounds',
    'time_pressure',
    'wait_page_arrival',
]
