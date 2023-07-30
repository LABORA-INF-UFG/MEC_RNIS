# Develop
# MEC_RNIS

---
Repositório que contém todo o desenvolvimento relacionado à dissertação de mestrado "Integração da Computação de Borda Móvel e Sistema 5G para Internet das Coisas na Agricultura 4.0". 

Aluno responsável:
* [Kaíque Matheus](http://lattes.cnpq.br/9539570966327546)


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
  
    locust -f locust_test.py -H http://127.0.0.1:5000
  
  Para acessar o locusst 
  - http://localhost:8089
   
  ## Documentos de referência
  Crirar um arquivo chamado locustfile.py onde vamos iniciar as configurações para executar testes na api
   - https://locust.io
   - https://docs.locust.io/en/stable/installation.html
   - https://docs.locust.io/en/stable/quickstart.html
   
# Detalhes

Detalhe o __init__.py dizer que esta pasta no qual esta inserido e um modulo/pacote. Para que possamos utilizar como se fosse uma blibloteca da mesma forma que importamos um Flask

# Comando rápido para executar o RNIS.

  virtualenv amb --python=python3.8 && source amb/bin/activate && pip3 install -r requirements.txt && python3 api.py