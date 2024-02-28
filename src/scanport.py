from serial.tools import list_ports
import inquirer

def scanport():
    available_ports = list_ports.comports()
    port_choices = [port.device for port in available_ports]
    if not port_choices: 
        print("Nenhuma porta serial encontrada.")
        return None
    question = [
        inquirer.List("port", message = "Escolha uma porta serial", choices = port_choices)
    ]
    selected_port = inquirer.prompt(question)["port"]
    return selected_port