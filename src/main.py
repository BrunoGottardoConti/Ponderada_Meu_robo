from robot import Robot
import inquirer

# Initialize the Robot instance
robo = Robot()

def execute_command(action, direction=None, distance=None, filename=None):
    if action == "mover":
        movements = {
            'x': lambda: robo.moveX(float(distance)),
            'y': lambda: robo.moveY(float(distance)),
            'z': lambda: robo.moveZ(float(distance)),
            'r': lambda: robo.moveR(float(distance))
        }
        if direction in movements:
            movements[direction]()
        else:
            print("direção invalida")
    elif action == "moveToFilePosition":
        if filename:
            robo.moveToPositionFromFile(filename)
        else:
            print("Nome não especificado.")
    elif action == "ligar":
        robo.actuatorOn()
    elif action == "desligar":
        robo.actuatorOff()
    elif action == "atual":
        robo.current()
    elif action == "savePosition":
        if filename:
            robo.setposition(filename)
        else:
            print("Nome não especificado.")
    else:
        print("Comando desconhecido")

def ask_for_action():
    questions = [
        inquirer.List('action',
                      message="Choose a command",
                      choices=['moveToFilePosition', 'ligar', 'desligar', 'mover', 'atual', 'savePosition']),
    ]
    answers = inquirer.prompt(questions)
    return answers['action']

def ask_for_movement_args():
    questions = [
        inquirer.List('direction', message="Escolha uma direção", choices=['x', 'y', 'z', 'r']),
        inquirer.Text('distance', message="Digite a distancia"),
    ]
    answers = inquirer.prompt(questions)
    return answers['direction'], answers['distance']

def ask_for_filename():
    question = [
        inquirer.Text('filename', message="Enter filename"),
    ]
    answer = inquirer.prompt(question)
    return answer['filename']

def main():
    while True:
        action = ask_for_action()
        if action == 'mover':
            direction, distance = ask_for_movement_args()
            execute_command(action, direction=direction, distance=distance)
        elif action in ['moveToFilePosition', 'savePosition']:
            filename = ask_for_filename()
            execute_command(action, filename=filename)
        else:
            execute_command(action)

if __name__ == "__main__":
    main()
