import string
from datetime import datetime
from random import choice

from browser import Browser

class Utils(Browser):
    def navegar(self, url):
        self.driver.get(url)


    def get_datetime(self):
        return str(datetime.now().__format__('%d/%m/%Y %I:%M:%S'))


    def get_login(self):
        tamanho = 10
        valores = string.ascii_letters
        login = ''
        for i in range(tamanho):
            login += choice(valores)
        return login


    def get_senha(self):
        tamanho = 10
        valores = string.digits + string.punctuation
        senha = ''
        for i in range(tamanho):
            senha += choice(valores)
        return senha