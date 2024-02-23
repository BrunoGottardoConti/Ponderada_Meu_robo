from serial.tools import list_ports
import inquirer

def scanport():
    available_ports = list_ports.comports()
    porta_escolhida = inquirer.prompt([
        inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])
    ])["porta"]
    return porta_escolhida