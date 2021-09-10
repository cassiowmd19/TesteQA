import time
from random import choice

from selenium import webdriver
from datetime import datetime
import string
import json

from webdriver_manager.chrome import ChromeDriverManager

def get_datetime():
    return str(datetime.now().__format__('%d/%m/%Y %I:%M:%S'))

def get_login():
    tamanho = 10
    valores = string.ascii_letters
    login = ''
    for i in range(tamanho):
        login += choice(valores)
    return login

def get_senha():
    tamanho = 10
    valores = string.digits + string.punctuation
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)
    return senha

def cria_jason():
    tarefas = {"titulo":"tarefa-"+get_login(), "descricao":"Tarefa criada automaticamente", "situacao":"New", "prioridade":"Normal" }
    cadastro_tarefas = json.dumps(tarefas)
    return cadastro_tarefas

string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 0123456789
string.punctuation # <=>?@[\]^_`{|}~.


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


#DEFINIÇÃO DE CADASTROS LOGIN
login = get_login()
senhaPadrao = get_senha()
nome = "Teste"
sobrenome = "Automático"
email = login+"@hotmail.com.br"
nomeProjeto = "Automação - "+get_datetime()

# 1. ENTRAR NO AMBIENTE http://demo.redmine.org/
driver.get('http://demo.redmine.org')

# 2. CADASTRE O USUÁRIO;
driver.find_element_by_xpath('//a[text()="Cadastre-se"]').click()
driver.find_element_by_xpath('//input[@id="user_login"]').send_keys(login)
driver.find_element_by_xpath('//input[@id="user_password"]').send_keys(senhaPadrao)
driver.find_element_by_xpath('//input[@id="user_password_confirmation"]').send_keys(senhaPadrao)
driver.find_element_by_xpath('//input[@id="user_firstname"]').send_keys(nome)
driver.find_element_by_xpath('//input[@id="user_lastname"]').send_keys(sobrenome)
driver.find_element_by_xpath('//input[@id="user_mail"]').send_keys(email)
driver.find_element_by_xpath('//input[@value="Enviar"]').click()


# 3. ACESSE A ÁREA DE PROJETOS E CRIE UM NOVO PROJETO COM SOMENTE O TIPO (BUG) SELECIONADO;
driver.find_element_by_xpath('//a[text()="Projetos"]').click()
driver.find_element_by_xpath('//a[text()="Novo projeto"]').click()
driver.find_element_by_xpath('//input[@id="project_name"]').send_keys(nomeProjeto)
driver.find_element_by_xpath('//input[@value="2"]').click()
driver.find_element_by_xpath('//input[@value="3"]').click()
driver.find_element_by_xpath('//input[@value="Criar"]').click()


# 4. ACESSE O PROJETO PELO MENU->Projetos
driver.find_element_by_xpath('//a[text()="Projetos"]').click()


# 5. CLIQUE NO PROJETO CRIADO;
driver.find_element_by_xpath(f"//a[text()='{nomeProjeto}']").click()


# 6. ENTRE NA ABA DE "NOVA TAREFA";
driver.find_element_by_xpath('//a[text()="Nova tarefa"]').click()


# 7. CRIE UM JSON CADASTRO TAREFAS

lista_tarefas = []
i=0
while i < 30:
    tarefa = cria_jason()
    lista_tarefas.insert(i, tarefa)
    i = i+1

# 8. ATRAVÉS DO JSON CRIADADO DE DADOS DE CADASTRO DE TAREFAS, CRIE 30 TAREFAS COM DADOS QUE ESTÃO NA MASSA DE DADOS DO JSON;
z=0
while z < 30:
    tarefa = json.loads(str(lista_tarefas[z]))
    driver.find_element_by_xpath('//input[@id="issue_subject"]').send_keys(tarefa["titulo"])
    driver.find_element_by_xpath('//textarea[@id="issue_description"]').send_keys(tarefa["descricao"])
    driver.find_element_by_xpath('//input[@value="Criar e continuar"]').click()
    time.sleep(1)
    z = z+1

# 9. ENTRE NA ABA DE TAREFAS;
driver.find_element_by_xpath('//a[text()="Tarefas"]').click()


# 10. FAÇA A PAGINAÇÃO DO GRID DE TAREFAS E VALIDE SE A 29ª TAREFA POSSUI O TIPO, SITUAÇÃO, PRIORIDADE E TÍTULO CONFORME OUTRO JSON DE VALIDAÇÃO DE TAREFAS;

tarefa = json.loads(str(lista_tarefas[1]))
print(tarefa["titulo"])
driver.find_element_by_xpath('//a[text()="Próximo »"]').click()
assert driver.find_element_by_xpath('//table[@class="list issues sort-by-id sort-desc"]/descendant::tbody/tr[4]/td[3]').text == "Bug"
assert driver.find_element_by_xpath('//table[@class="list issues sort-by-id sort-desc"]/descendant::tbody/tr[4]/td[4]').text == tarefa["situacao"]
assert driver.find_element_by_xpath('//table[@class="list issues sort-by-id sort-desc"]/descendant::tbody/tr[4]/td[5]').text == tarefa["prioridade"]
assert driver.find_element_by_xpath('//table[@class="list issues sort-by-id sort-desc"]/descendant::tbody/tr[4]/td[6]').text == tarefa["titulo"]



