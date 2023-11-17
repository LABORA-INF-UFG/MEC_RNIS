import psutil
import os
import subprocess

def find_and_terminate_process(port):
    try:
        # Tenta encontrar o processo usando a porta
        for conn in psutil.net_connections():
            if conn.laddr.port == port:
                print(f"Porta {port} está sendo usada pelo processo com PID {conn.pid}.")
                
                # Tenta encerrar o processo
                process = psutil.Process(conn.pid)
                process.terminate()
                print(f"Processo com PID {conn.pid} encerrado.")
                
                # Aguarda um curto período de tempo para o processo encerrar completamente
                process.wait(timeout=5)
                
                # Se o processo ainda estiver em execução, force o encerramento
                if process.is_running():
                    process.kill()
                    print(f"Processo com PID {conn.pid} forçadamente encerrado.")

    except Exception as e:
        print(f"Erro ao tentar encerrar o processo: {e}")


def stop_and_remove_containers():
    # Obtém uma lista de IDs de todos os containers em execução
    running_containers = subprocess.check_output(["docker", "ps", "-q"]).decode("utf-8").splitlines()

    if not running_containers:
        print("Nenhum container em execução encontrado.")
        return

    # Para e remove cada container em execução
    for container_id in running_containers:
        # Para o container
        subprocess.run(["docker", "stop", container_id])
        print(f"Container {container_id} parado.")

        # Remove o container
        subprocess.run(["docker", "rm", container_id])
        print(f"Container {container_id} removido.")

    print("Todos os containers em execução foram parados e removidos com sucesso.")


if __name__ == "__main__":
    # Portas a serem verificadas e liberadas
    ports_to_check = [5000, 8002, 8009]

    for port in ports_to_check:
        find_and_terminate_process(port)
        
    stop_and_remove_containers()

    print("Processos encerrados e portas liberadas.")