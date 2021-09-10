import json
import string
import time
from random import choice

from browser import Browser


class TestePage(Browser):
    def get_login(self):
        tamanho = 10
        valores = string.ascii_letters
        login = ''
        for i in range(tamanho):
            login += choice(valores)
        return login

    def cadastrar(self, login, senhaPadrao, nome, sobrenome, email):
        self.driver.find_element_by_xpath('//a[text()="Cadastre-se"]').click()
        self.driver.find_element_by_xpath('//input[@id="user_login"]').send_keys(login)
        self.driver.find_element_by_xpath('//input[@id="user_password"]').send_keys(senhaPadrao)
        self.driver.find_element_by_xpath('//input[@id="user_password_confirmation"]').send_keys(senhaPadrao)
        self.driver.find_element_by_xpath('//input[@id="user_firstname"]').send_keys(nome)
        self.driver.find_element_by_xpath('//input[@id="user_lastname"]').send_keys(sobrenome)
        self.driver.find_element_by_xpath('//input[@id="user_mail"]').send_keys(email)
        self.driver.find_element_by_xpath('//input[@value="Enviar"]').click()


    def click_menu_projeto(self):
        self.driver.find_element_by_xpath('//a[text()="Projetos"]').click()


    def cria_projeto(self, nomeProjeto):

        self.driver.find_element_by_xpath('//a[text()="Novo projeto"]').click()
        self.driver.find_element_by_xpath('//input[@id="project_name"]').send_keys(nomeProjeto)
        self.driver.find_element_by_xpath('//input[@value="2"]').click()
        self.driver.find_element_by_xpath('//input[@value="3"]').click()
        self.driver.find_element_by_xpath('//input[@value="Criar"]').click()


    def acessar_projeto(self, nomeProjeto):
        self.driver.find_element_by_xpath(f"//a[text()='{nomeProjeto}']").click()


    def click_nova_tarefa(self):
        self.driver.find_element_by_xpath('//a[text()="Nova tarefa"]').click()


    def cria_jason(self):
            tarefas = {"titulo": "tarefa-" + self.get_login(), "descricao": "Tarefa criada automaticamente",
                       "situacao": "New", "prioridade": "Normal"}
            cadastro_tarefas = json.dumps(tarefas)
            return cadastro_tarefas


    def lista_json(self):
        lista_tarefas = []
        i = 0
        while i < 30:
            tarefa = self.cria_jason()
            lista_tarefas.insert(i, tarefa)
            i = i + 1
        return lista_tarefas


    def insere_tarefas(self, lista_tarefa):
        z = 0
        while z < 30:
            tarefa = json.loads(str(lista_tarefa[z]))
            self.driver.find_element_by_xpath('//input[@id="issue_subject"]').send_keys(tarefa["titulo"])
            self.driver.find_element_by_xpath('//textarea[@id="issue_description"]').send_keys(tarefa["descricao"])
            self.driver.find_element_by_xpath('//input[@value="Criar e continuar"]').click()
            time.sleep(1)
            z = z + 1


    def paginar(self):
        self.driver.find_element_by_xpath('//a[text()="Próximo »"]').click()


    def retorna_item_tabela(self,linha: int, coluna: int):
        return self.driver.find_element_by_xpath(f"//table[@class='list issues sort-by-id sort-desc']/descendant::tbody/tr[{linha}]/td[{coluna}]").text


    def click_aba_tarefa(self):
        self.driver.find_element_by_xpath('//a[text()="Tarefas"]').click()


    def retorna_json(self, lista_tarefa, num):
        return json.loads(str(lista_tarefa[num]))