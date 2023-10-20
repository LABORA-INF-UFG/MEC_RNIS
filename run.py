
import threading
import subprocess
import time

# Função para executar uma API em uma thread
def run_api(api_file, port):
    subprocess.call(['python3', api_file, '--port', str(port)])

if __name__ == '__main__':
    # Especifique os arquivos Python de suas APIs e as portas em que deseja executá-las
    api1_file = 'api_1.py'
    api2_file = 'api_2.py'
    port_api1 = 5000
    port_api2 = 8085

    # Crie threads para executar cada API
    thread1 = threading.Thread(target=run_api, args=(api1_file, port_api1))
    thread2 = threading.Thread(target=run_api, args=(api2_file, port_api2))

    # Inicie as threads
    thread1.start()
    time.sleep(5)
    thread2.start()

    # Aguarde até que ambas as threads terminem
    thread1.join()
    thread2.join()