import sys

from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivy.uix.screenmanager import FadeTransition
import gui.cards

class RoomNavigation(MDBottomNavigation):
    def __init__(self, config, **kwargs):
        super(RoomNavigation, self).__init__(**kwargs)
        self.height = '80dp'
        self.ids.bottom_panel.height = '80dp'
        self.ids.tab_bar.height = '80dp'
        self.ids.tab_manager.transition.duration = 0.0

        for card in config:
            content = gui.cards.createCard(card)

            if content:
                item = MDBottomNavigationItem(name=card['name'], text=card['name'], icon=content.nav_icon)
                item.add_widget(content)
                self.add_widget(item)

        for i in self.ids.tab_bar.children:
            i.ids._label_icon.font_size = '48sp'


class Room(FloatLayout):
    def __init__(self, config, **kwargs):
        super(Room, self).__init__(**kwargs)
        self.config = config

        self.content = MDLabel(text=self.config['name'], halign="center", theme_text_color="Primary", font_style="H6")
        self.navigation = RoomNavigation(config['cards'])

        self.add_widget(self.content)
        self.add_widget(self.navigation)
