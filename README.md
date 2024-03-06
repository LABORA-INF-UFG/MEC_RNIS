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
# Resumo

A Agricultura 4.0 tem evoluído à medida que novas oportunidades e benefícios surgem com a aplicação de diversas tecnologias no setor agropecuário. O Multi-access Edge Computing - (MEC) destaca-se como uma tecnologia fundamental, possibilitando o desenvolvimento de novas aplicações e serviços que agregam benefícios tanto para a geração atual quanto para as futuras. No âmbito do MEC, o Radio Network Information Service - (RNIS) assume um papel crucial, sendo um dos principais serviços relacionados à obtenção de informações da Radio Access Network - (RAN). No cenário Fifth generation of mobile networks - (5G), o RNIS necessitará de aprimoramentos para lidar com as informações de RAN das novas gerações. Nesse contexto, o aprimoramento do serviço RNIS é essencial para potencializar diversas aplicações agrícolas. Este trabalho propõe o serviço RNIS as a service to the MEC framework in 5G Networks - (RaM-5G) implementando o RNIS e destacando a importância da integração destas tecnologias como MEC, Internet of Things - (IoT), 5G e RNIS, impulsionando o setor agropecuário. Além disso, busca otimizar aplicações que dependem de informações provenientes da RAN.

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
