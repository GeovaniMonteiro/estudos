# Desenvolvendo um Projeto Completo Python com Estrutura de Dados - Fundação Bradesco

## Configurando o Ambiente Virtual

1. Instale o virtualenv

``~$ pip install virtualenv``

2. Para começar a utilizar o ambiente utilize o comando:

``~$ python3 -m venv venv``

3. Agora, seu projeto tem seu próprio ambientevirtual. Geralmente, antes de começar a usá-lo,você primeiro ativará o ambiente executandoum script que acompanha a instalação:

``~$ source venv/scripts/activate`` 

# Pronto! Agora que criou e ativou seu ambiente virtual, com ele você pode instalar quaisquer dependências externas necessárias para seu projeto:

Para instalar pacotes externos do Python com pip, utilize o comando padrão:

``(venv) $ python -m pip install <nome do pacote>``

Como você primeiro criou e ativou o ambiente virtual, pip instalará os pacotes em um local isolado.

Desde que você não feche seu terminal, cada pacote Python que instalar terminará neste ambiente isolado em vez de seus pacotes Python globais.

Isso significa que agora você pode trabalhar em seu projeto Python sem se preocupar com conflitos de dependência.

**Quando terminar de trabalhar com esse ambiente virtual, você pode desativá-lo utilizando o comando:**

``(venv) $ deactivate``

## Projeto Cadastro Simples

O projeto consiste em um programa para cadastro de pessoas(Nome, Sobrenome, Email, CPF) em um banco de dados
atrvés de uma interface.

![InterfaceMain.png](..%2Fimgs%2FCurso02%2FInterfaceMain.png)


Foi utilizado a biblioteca TKinter para a criação da interface e sqlite3 para gerar o banco de dados

Pode visualizar os testes no Banco de dados através do JupyterNotebook :
[testesDB.ipynb](MainProject%2FtestesDB.ipynb)





