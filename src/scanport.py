from serial.tools import list_ports  # Importa a função para listar as portas seriais disponíveis
import inquirer  # Importa a biblioteca para interação com o usuário

# Função para escanear e selecionar uma porta serial disponível
def scanport():
    # Lista todas as portas seriais disponíveis
    available_ports = list_ports.comports()
    # Obtém os nomes das portas disponíveis
    port_choices = [port.device for port in available_ports]
    if not port_choices: 
        print("Nenhuma porta serial encontrada.")
        return None
    # Cria uma pergunta para o usuário escolher a porta serial
    question = [
        inquirer.List("port", message="Escolha uma porta serial", choices=port_choices)
    ]
    # Pede ao usuário para selecionar uma porta serial
    selected_port = inquirer.prompt(question)["port"]
    return selected_port
