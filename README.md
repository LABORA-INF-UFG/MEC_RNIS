# Develop
# MEC_RNIS

O repositório contém todo o desenvolvimento relacionado à dissertação de mestrado intitulada "Serviço de Informações de Rádio (RNIS) para o framework MEC usando Redes 5G". Sendo desenvolvido através do Curso de Mestrado Acadêmico em Ciência da Computação - Presencial - Goiânia, pelo Instituto de Informática (INF) da Universidade Federal de Goiás (UFG). Este projeto contou com o apoio da Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES) e do Conselho Superior da Fundação de Amparo à Pesquisa do Estado de Goiás (FAPEG).

O processo de ingresso no mestrado foi realizado por meio do [edital 1988959](https://files.cercomp.ufg.br/weby/up/85/o/SEI_UFG_-_1988959_-_Edital_-_Retificado.pdf), PROGRAMA DE DESENVOLVIMENTO DA PÓS-GRADUAÇÃO - APOIO AOS PROGRAMAS DE PÓS-GRADUAÇÃO EM CONSOLIDAÇÃO EM ÁREAS PRIORITÁRIAS NOS ESTADOS - 03/2021, que tornou público o Processo Seletivo 03/2021 para o preenchimento de vagas no segundo semestre letivo de 2021, nos níveis de Mestrado, Doutorado e Pós-Doutorado, em conformidade com as exigências da Chamada Pública CAPES No 18/2020.

---

Aluno responsável:
* [Kaíque Matheus](http://lattes.cnpq.br/9539570966327546)
* kaiquematheus@discente.ufg.br / ufgkaique@gmail.com 

---
# Descrição

A estrutura da API está sendo feita com base nas especificações do ETSI GS MEC 012 V2.

---

# Ambiente virtual

  comando:

    sudo pip3 install virtualenv  --user 
 
  ou:

    sudo apt install python3-virtualenv


# Criando o ambiente:

  comando:

    virtualenv amb --python=python3.8

# Para acessar o ambiente use o comando:

  comando:
    
    source amb/bin/activate

# Para desativar o ambiente

  comando:
    
    deactivate

# Bibliotecas

  comando:

    pip3 install Flask

    pip3 install Flask-Restful

    pip3 install connexion

pip3 install pika

# Para criar um requirements e simples

  comando:

    pip3 freeze > requirements.txt

# Para instalar as dependências de um “requirements.txt” usamos o seguinte comando

  comando:

    pip3 install -r requirements.txt

# Passo a passo

# Instalar o docker no linux ubuntu/mint

Iniciando o docker:
    
    sudo apt-get update
    
      sudo apt-get install \
      ca-certificates \
      curl \
      gnupg \
      lsb-release
      
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

      echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

      sudo apt-get update

      sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

      apt-cache madison docker-ce

      sudo docker run hello-world

      sudo usermod -aG docker $USER

      sudo reboot

      docker run hello-world

# Instalando o docker-compose no linux ubuntu/mint

  comando:

    sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

    sudo chmod +x /usr/local/bin/docker-compose

    sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# RabbitMQ

Iniciar o RabbitMQ:
 
    cd MEC_RNIS/docker-compose
  
    docker-compose up -d

    Para acessar o rabbitmq no browser podemos utilizar http://localhost:15672/

# Running on 

  comando:

    source nome_Do_ambiente/bin/activate

    python3 app.py

  - Running on http://127.0.0.1:5000/rni/v2/queries/rab_info


# Locust
  ## locustfile.py para teste
  
  Instalando o locust:

      pip3 install locust
      locust -V
  
  Entre na pasta
  
    cd locust/

  Execute o comando locust:

      locust locust_test.py  
      
  ou:
  
    locust -f locustfile.py -H http://127.0.0.1:5000

  ou

    locust -f locustfile2.py -H http://127.0.0.1:5000 --autostart --run-time 5m -u 100 -r 100 --csv=/home/kaique/Documentos/ufg/MEC_RNIS/locust/exemplo/exemplo.csv --html=/home/kaique/Documentos/ufg/MEC_RNIS/locust/exemplo/exemplo.html

  ou

    locust -f locustfile2.py --host=http://127.0.0.1:5000 --web-host=0.0.0.0 --autostart --run-time 5m -u 100 -r 100
    locust -f locustfile_2.py --host=http://127.0.0.1:5000 --web-host=0.0.0.0 --autostart --run-time 10m -u 800 -r 800 --html=/l/disk0/mcunha/Documentos/ufg/MEC_RNIS/Dataset_flexran/Teste_10m_800_2.html


  ou 

    locust -f locustfile2.py --host=http://127.0.0.1:5000 --web-host=0.0.0.0 --autostart --run-time 35m -u 500 -r 500 --csv=/l/disk0/mcunha/Documentos/ufg/MEC_RNIS/locust/pc_32gb_ram/60_minutos_500_users_limpei_o_script/60_minutos_500_users_limpei_o_script.csv --html=/l/disk0/mcunha/Documentos/ufg/MEC_RNIS/locust/pc_32gb_ram/60_minutos_500_users_limpei_o_script/60_minutos_500_users_limpei_o_script.html


  -f LOCUSTFILE, --locustfile LOCUSTFILE
                        Python module to import, e.g. '../other_test.py'. Either a .py file, multiple comma-separated .py
                        files or a package directory. Defaults to 'locustfile'.

  -H HOST, --host HOST  Host to load test in the following format: http://10.21.32.33                      
    
  -t RUN_TIME, --run-time RUN_TIME
                        Stop after the specified amount of time, e.g. (300s, 20m, 3h, 1h30m, etc.). Only used together with
                        --headless or --autostart. Defaults to run forever.

  -u NUM_USERS, --users NUM_USERS
                        Peak number of concurrent Locust users. Primarily used together with --headless or --autostart. Can
                        be changed during a test by keyboard inputs w, W (spawn 1, 10 users) and s, S (stop 1, 10 users)

  -r SPAWN_RATE, --spawn-rate SPAWN_RATE
                        Rate to spawn users at (users per second). Primarily used together with --headless or --autostart

                        
  Caso tenha problema com o pandas:

    pip install --upgrade numpy

    pip install --upgrade pandas


  - https://cursos.alura.com.br/forum/topico-modulenotfounderror-no-module-named-pandas-198292
  
  Para acessar o locusst 
  - http://localhost:8089
   
  ## Documentos de referência
  Crirar um arquivo chamado locustfile.py onde vamos iniciar as configurações para executar testes na api
   - https://locust.io
   - https://docs.locust.io/en/stable/installation.html
   - https://docs.locust.io/en/stable/quickstart.html
   
# Detalhes

Detalhe o __init__.py dizer que esta pasta no qual esta inserido e um modulo/pacote. Para que possamos utilizar como se fosse uma blibloteca da mesma forma que mportamos um Flask

# Comando rápido para executar o RNIS.

  Comando:

      virtualenv amb --python=python3.8 && source amb/bin/activate && pip3 install -r requirements.txt && python3 api.py
      
