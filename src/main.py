from robot import Robot  # Importa a classe Robot do arquivo robot.py
import inquirer  # Importa a biblioteca para criar interfaces interativas de linha de comando

# Instancia um objeto Robot para controlar o robô
robo = Robot()

# Função para executar comandos com base na ação especificada
def execute_command(action, direction=None, distance=None, filenames=None):
    # Executa a ação com base no comando fornecido
    if action == "mover":
        # Mapeia as direções para os métodos de movimento do robô
        movements = {
            'x': lambda: robo.moveX(float(distance)),
            'y': lambda: robo.moveY(float(distance)),
            'z': lambda: robo.moveZ(float(distance)),
            'r': lambda: robo.moveR(float(distance))
        }
        # Executa o movimento na direção especificada
        if direction in movements:
            movements[direction]()
        else:
            print("Direção inválida")
    elif action == "moveToFilePosition":
        # Move o robô para as posições especificadas em arquivos
        if filenames:
            robo.moveToPositionFromFiles(filenames)
        else:
            print("Filenames não especificados.")
    elif action == "ligar":
        # Liga o atuador do robô
        robo.actuatorOn()
    elif action == "desligar":
        # Desliga o atuador do robô
        robo.actuatorOff()
    elif action == "atual":
        # Imprime a posição atual do robô
        robo.current()
    elif action == "savePosition":
        # Salva a posição atual do robô em um arquivo
        if filenames:
            for filename in filenames:
                robo.setposition(filename)
        else:
            print("Filename não especificado.")
    else:
        print("Comando desconhecido")

# Função para solicitar ao usuário que escolha uma ação
def ask_for_action():
    # Cria uma lista suspensa para escolha da ação
    questions = [
        inquirer.List('action',
                      message="Escolha um comando",
                      choices=['executeTask', 'moveToFilePosition', 'ligar', 'desligar', 'mover', 'atual', 'savePosition']),
    ]
    # Pede ao usuário que escolha uma ação
    answers = inquirer.prompt(questions)
    return answers['action']

# Função para solicitar ao usuário as informações de movimento (direção e distância)
def ask_for_movement_args():
    # Cria perguntas para obter a direção e a distância do movimento
    questions = [
        inquirer.List('direction', message="Escolha uma direção", choices=['x', 'y', 'z', 'r']),
        inquirer.Text('distance', message="Insira a distância"),
    ]
    # Pede ao usuário que insira a direção e a distância do movimento
    answers = inquirer.prompt(questions)
    return answers['direction'], answers['distance']

# Função para solicitar ao usuário os nomes dos arquivos
def ask_for_filenames():
    # Cria uma pergunta para obter os nomes dos arquivos
    question = [
        inquirer.Text('filenames', message="Digite o nome do arquivo"),
    ]
    # Pede ao usuário que insira os nomes dos arquivos
    answer = inquirer.prompt(question)
    # Divide os nomes dos arquivos e remove espaços em branco extras
    filenames = answer['filenames'].split(',')
    filenames = [filename.strip() for filename in filenames if filename.strip()]
    return filenames

# Função principal que executa continuamente até que o usuário decida sair
def main():
    while True:
        # Solicita ao usuário que escolha uma ação
        action = ask_for_action()
        # Executa a ação com base na escolha do usuário
        if action == 'executeTask':
            task_name = input("Digite o nome da tarefa (diretório): ")
            robo.executeTask(task_name)
        elif action == 'mover':
            direction, distance = ask_for_movement_args()
            execute_command(action, direction=direction, distance=distance)
        elif action == 'moveToFilePosition':
            filenames = ask_for_filenames()
            execute_command(action, filenames=filenames)
        elif action in ['ligar', 'desligar', 'atual']:
            execute_command(action)
        elif action == 'savePosition':
            filename = ask_for_filenames()
            execute_command(action, filenames=filename)
        else:
            print("Comando desconhecido.")

# Executa a função principal se este arquivo for o arquivo principal
if __name__ == "__main__":
    main()
