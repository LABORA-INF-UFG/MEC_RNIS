# Master

# MEC_RNIS

---
O repositório contém todo o desenvolvimento relacionado à dissertação de mestrado intitulada "Serviço de Informações de Rádio (RNIS) para o framework MEC usando Redes 5G". Sendo desenvolvido através do Curso de Mestrado Acadêmico em Ciência da Computação - Presencial - Goiânia, pelo Instituto de Informática (INF) da Universidade Federal de Goiás (UFG). Este projeto contou com o apoio da Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES) e do Conselho Superior da Fundação de Amparo à Pesquisa do Estado de Goiás (FAPEG).

O processo de ingresso no mestrado foi realizado por meio do [edital 1988959](https://files.cercomp.ufg.br/weby/up/85/o/SEI_UFG_-_1988959_-_Edital_-_Retificado.pdf), PROGRAMA DE DESENVOLVIMENTO DA PÓS-GRADUAÇÃO - APOIO AOS PROGRAMAS DE PÓS-GRADUAÇÃO EM CONSOLIDAÇÃO EM ÁREAS PRIORITÁRIAS NOS ESTADOS - 03/2021, que tornou público o Processo Seletivo 03/2021 para o preenchimento de vagas no segundo semestre letivo de 2021, nos níveis de Mestrado, Doutorado e Pós-Doutorado, em conformidade com as exigências da Chamada Pública CAPES No 18/2020.

---

Aluno responsável:
* [Kaíque Matheus](http://lattes.cnpq.br/9539570966327546)
* kaiquematheus@discente.ufg.br / ufgkaique@gmail.com 



---
# Descrição

A estrutura da API está sendo feita com base nas especificações do ETSI GS MEC 012 V2.1.1 (2019-12).

---
# Instalando o python 3

sudo apt-get install python3

sudo apt-get install python3-pip

# Ambiente virtual

sudo pip3 install virtualenv  --user

 ## ou

sudo apt install python3-virtualenv

## criando o ambiente:

 virtualenv nome_Do_ambiente  --python=python3.10         

## para acessar o ambiente use o comando:

source nome_Do_ambiente/bin/activate

## para desativar o ambiente

deactivate

# Bibliotecas

pip3 install Flask

pip3 install Flask-Restful

pip3 install connexion

pip3 install pika

# Detalhes

Detalhe o __init__.py dizer que esta pasta no qual esta inserido e um modulo/pacote. Para que possamos utilizar como se fosse uma blibloteca da mesma forma que importamos um Flask

# Running on 

python3 app.py

- Running on http://127.0.0.1:5000/rni/v2/queries/rab_info
