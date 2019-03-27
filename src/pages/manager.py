from kivy.uix.screenmanager import ScreenManager

from pages.splash import SplashPage, LoginPage
from pages.menu import MenuPage

pages = {
    'splash': SplashPage,
    'menu': MenuPage,
    'login': LoginPage
}


class PageManager(ScreenManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, page in pages.items():
            self.add_widget(page(name=name))

        self.current = 'splash'
