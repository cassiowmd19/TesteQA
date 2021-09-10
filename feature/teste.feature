# language: pt

  Funcionalidade: Validação tarefa

  @teste
  Cenário: Cadastro e validação da 29ºtarefa
    Dado que acesso o site 'http://demo.redmine.org/'
    E cadastre um usuário
    E acesse a área de projetos
    E crie um novo projeto com somente 'Bug' selecionado
    E acesse o projeto pelo 'Menu->Projetos'
    E clique no projeto criado
    E entre na aba 'Nova Tarefa'
    E crie um json para cadastro de tarefas
    E através do json crie na sequência 30 tarefas
    E entre na aba de 'Tarefas'
    Quando paginar o grid de tarefas
    Então a 29ºtarefa deve conter os campos 'TIPO, SITUAÇÃO, PRIORIDADE E TÍTULO' equivalente ao seu registro no json