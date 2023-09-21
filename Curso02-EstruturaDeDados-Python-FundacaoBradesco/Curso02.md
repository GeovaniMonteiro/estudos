# Desenvolvendo um Projeto Completo Python com Estrutura de Dados - Fundação Bradesco

Acesse o Projeto Completo: [MainProject](MainProject)

As Anotações de testes estão no diretório: [PandasSQLite notebook](PandasSQLite%20notebook)

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

## Foi utilizado o Conceito de POO no desenvolvimento e separação das classes

# Backend
Arquivo:
[Backend.py](MainProject%2FBackend.py)
![FuncoesBackProj.png](..%2Fimgs%2FCurso02%2FFuncoesBackProj.png)
Separado especificamente para as funções de BackEnd
* Remoção de dados

![FuncDelete.png](..%2Fimgs%2FCurso02%2FFuncDelete.png)

* Atualização de dados

![FuncUpdate.png](..%2Fimgs%2FCurso02%2FFuncUpdate.png)

* Visualização de dados

![FuncView.png](..%2Fimgs%2FCurso02%2FFuncView.png)

* Inserção de dados

![FuncInsert.png](..%2Fimgs%2FCurso02%2FFuncInsert.png)

* Procura de dados

![FuncSearch.png](..%2Fimgs%2FCurso02%2FFuncSearch.png)


# FrontEnd
Arquivo: [GUI.py](MainProject%2FGUI.py)
![InterfaceMainCode.png](..%2Fimgs%2FCurso02%2FInterfaceMainCode.png)
Separado especificamente para a criação da Interface FrontEnd

* Criação dos objetos da janela

 ![ObjetosJanela.png](..%2Fimgs%2FCurso02%2FObjetosJanela.png)

* Associando os objetos

![AssociandoOBJETOS.png](..%2Fimgs%2FCurso02%2FAssociandoOBJETOS.png)

* Interface SWAG

![InterfaceSWAG.png](..%2Fimgs%2FCurso02%2FInterfaceSWAG.png)
