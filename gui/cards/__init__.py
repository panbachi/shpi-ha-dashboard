# -*- coding: utf-8 -*-

import importlib

'''
    Autoload the apporpriate module and returns a new card instance.
    A card is defined as class <Cardtype> (capitalized) in <cardtype>.py (all lower)
    (e. g. cardtype: weather is defined as class Weather in weather.py).

    The card receives the config via its first (and only) constructor argument.
    The field nav_icon defines which icon should be showen in navigation item.
'''
def createCard(card):
    module = importlib.import_module("." + card['type'].lower(), __name__)
    card_type = getattr(module, card['type'].capitalize())
    return card_type(card)