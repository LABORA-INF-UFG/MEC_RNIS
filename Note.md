#

# A flexRAN alimenta o RNIS com informações de RAN


# Vamos fazer uma alimentação sobre rab_info:  Atualmente usando o metodo post do postman

    Vamos alimentar o topico rab

    -> O rab_info já esta sendo alimentado com informações

# agora vamos criar um assinante no topico do rab_info para confiramar que a mensagem esta chegando

    Vamos iniciar um assinante sobre o topico rab

    -> o assinante recebe as informações enviadas para o topico rab

# O assinante tem que descerializar o json no caso o body

    Para pegar no body as informações que ele quer!

    -> O assinante consgue utilizar qualquer informação enviada pelo tópico

# Agora tenho que crirar uma Aplicação Exemplo que assina o tópico atraves do rnis

    criar o topico rab no rnis
    fazer com q minha Aplicação exemplo assine esse tópico

    A resposta pode ser no retorno do post! devolver a informação por lá



## Temos dois scripts para o cliente app_cliente_2.py e teste_reveiver.py
    -  Documentos/ufg/MEC_RNIS/client_app/app_cliente_2.py
    -  Documentos/ufg/MEC_RNIS/client_app/teste_reveiver.py

    O MEC APP deve consumir as funções do RNIS atravez do pondo de referencia MP1

    Vomos criar uma aplicação que simula o ponto de referencia mp1 e o mec app

