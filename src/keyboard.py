from src.item import Item


class MixinLang:
    lang = 'EN'

    def __init__(self):
        self.__language = self.lang

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, MixinLang):
    pass
