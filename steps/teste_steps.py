import time

from behave import given, when, then
from utils import Utils
from pages.teste_page import TestePage
from nose.tools import assert_equal


utils = Utils()
page = TestePage()


#DEFINIÇÃO DE CADASTROS LOGIN
login = utils.get_login()
senhaPadrao = utils.get_senha()
nome = "Teste"
sobrenome = "Automático"
email = login+"@hotmail.com.br"
nomeProjeto = "Automação - "+utils.get_datetime()


@given(u'que acesso o site \'http://demo.redmine.org/\'')
def step_impl(context):
   utils.navegar('http://demo.redmine.org/')


@given(u'cadastre um usuário')
def step_impl(context):
    page.cadastrar(login, senhaPadrao, nome, sobrenome, email)


@given(u'acesse a área de projetos')
def step_impl(context):
    page.click_menu_projeto()


@given(u'crie um novo projeto com somente \'Bug\' selecionado')
def step_impl(context):
    page.cria_projeto(nomeProjeto)


@given(u'acesse o projeto pelo \'Menu->Projetos\'')
def step_impl(context):
    page.click_menu_projeto()


@given(u'clique no projeto criado')
def step_impl(context):
    page.acessar_projeto(nomeProjeto)


@given(u'entre na aba \'Nova Tarefa\'')
def step_impl(context):
    page.click_nova_tarefa()


@given(u'crie um json para cadastro de tarefas')
def step_impl(context):
    global json
    json = page.lista_json()


@given(u'através do json crie na sequência 30 tarefas')
def step_impl(context):
   page.insere_tarefas(json)


@given(u'entre na aba de \'Tarefas\'')
def step_impl(context):
   page.click_aba_tarefa()


@when(u'paginar o grid de tarefas')
def step_impl(context):
    page.paginar()


@then(u'a 29ºtarefa deve conter os campos \'TIPO, SITUAÇÃO, PRIORIDADE E TÍTULO\' equivalente ao seu registro no json')
def step_impl(context):
    tarefa = page.retorna_json(json, 1)
    time.sleep(2)
    assert_equal(page.retorna_item_tabela(4, 3), 'Bug')
    assert_equal(page.retorna_item_tabela(4, 4), tarefa["situacao"])
    assert_equal(page.retorna_item_tabela(4, 5), tarefa["prioridade"])
    assert_equal(page.retorna_item_tabela(4, 6), tarefa["titulo"])


