#!/bin/bash

# Verifique se os parâmetros foram fornecidos
if [ $# -ne 2 ]; then
    echo "Uso: $0 <TEMPO_EXECUCAO_LOCUST> <users>"
    exit 1
fi

# Atribua os parâmetros de entrada às variáveis
TEMPO_EXECUCAO_LOCUST=$1
users=$2

# Convertendo minutos para segundos
segundos=$((TEMPO_EXECUCAO_LOCUST * 60))
# Acrescentando 60 segundos ao tempo total
segundos=$((segundos + 40))


# Número total de iterações
TOTAL_ITERACOES=10

diretorio_atual=$(pwd)

for ((iteracao=1; iteracao<=$TOTAL_ITERACOES; iteracao++)); do
    echo "Iniciando iteração $iteracao"

    # Verifica se há contêineres Docker em execução e os para e remove
    CONTAINER_ID=$(docker ps -q)
    if [ -n "$CONTAINER_ID" ]; then
        echo "Parando e removendo contêiner Docker em execução..."
        docker stop $CONTAINER_ID
        docker rm $CONTAINER_ID
    fi

    # Inicia a API em um terminal separado (background)
    gnome-terminal -- bash -c "python3 ${diretorio_atual}/receive.py $iteracao; exec bash"

    # Aguarda um breve momento antes de iniciar o cliente (ajuste conforme necessário)
    sleep 10

    # Inicia o cliente em um terminal separado (background)
    gnome-terminal -- bash -c "python3 ${diretorio_atual}/client_app/app_client3_client.py --n $iteracao; exec bash"

    # Aguarda um breve momento antes de iniciar o Locust (ajuste conforme necessário)
    sleep 1

     # Inicia o cliente em um terminal separado (background)
    gnome-terminal -- bash -c "python3 ${diretorio_atual}/client_app/app_client4_client.py --n $iteracao; exec bash"

    # Aguarda um breve momento antes de iniciar o Locust (ajuste conforme necessário)
    sleep 2

    # Inicia o Locust em um terminal separado (background)
    #gnome-terminal -- bash -c "locust -f ${diretorio_atual}/Dataset_flexran/locustfile_2.py --host=http://127.0.0.1:5000 --web-host=0.0.0.0 --autostart --run-time ${TEMPO_EXECUCAO_LOCUST}m -u ${users} -r ${users} --html=${diretorio_atual}/locust/${TEMPO_EXECUCAO_LOCUST}_minutos_client_${users}users_1s_2_mec_apps/time_${TEMPO_EXECUCAO_LOCUST}m_client_${iteracao}_${users}.html --autoquit ${TEMPO_EXECUCAO_LOCUST}; exec bash"
    # Inicia o Locust em um terminal separado (background)
    gnome-terminal -- bash -c "locust -f ${diretorio_atual}/Dataset_flexran/locustfile_2.py --host=http://127.0.0.1:5000 --web-host=0.0.0.0 --autostart --run-time ${TEMPO_EXECUCAO_LOCUST}m -u ${users} -r ${users} --html=${diretorio_atual}/locust/${TEMPO_EXECUCAO_LOCUST}_minutos_client_${users}users_1s_2_mec_apps/time_${TEMPO_EXECUCAO_LOCUST}m_client_${iteracao}_${users}.html --autoquit ${TEMPO_EXECUCAO_LOCUST} && sleep 2"

    # Aguardando o tempo em segundos
    sleep $segundos
    pkill -f "locust -f ${diretorio_atual}/Dataset_flexran/locustfile_2.py"
    #wait

    # Finaliza os processos da API e do Cliente (ajuste conforme necessário)
    pkill -f "python3 ${diretorio_atual}/receive.py"
    pkill -f "python3 ${diretorio_atual}/client_app/app_client3_client.py"
    pkill -f "python3 ${diretorio_atual}/client_app/app_client4_client.py"
    #pkill -f "locust -f ${diretorio_atual}/Dataset_flexran/locustfile_2.py --host=http://127.0.0.1:5000 --web-host=0.0.0.0 --autostart --run-time ${TEMPO_EXECUCAO_LOCUST}m -u ${users} -r ${users} --html=${diretorio_atual}/locust/${TEMPO_EXECUCAO_LOCUST}_minutos_client_${users}users_1s_2_mec_apps/time_${TEMPO_EXECUCAO_LOCUST}m_client_${iteracao}_${users}.html --autoquit ${TEMPO_EXECUCAO_LOCUST}"

    rm -f "/l/disk0/mcunha/Documentos/ufg/MEC_RNIS/applications.db"

    echo "Iteração $iteracao concluída. Aguardando próxima iteração."

    # Aguarda um intervalo entre as iterações (ajuste conforme necessário)
    sleep 10
done

echo "Todas as iterações concluídas."
