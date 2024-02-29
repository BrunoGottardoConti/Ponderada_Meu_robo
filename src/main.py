from robot import Robot
import inquirer

robo = Robot()

def execute_command(action, direction=None, distance=None, filenames=None):
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
            print("Direção invalida")
    elif action == "moveToFilePosition":
        if filenames:
            robo.moveToPositionFromFiles(filenames)
        else:
            print("Filenames not specified.")
    elif action == "ligar":
        robo.actuatorOn()
    elif action == "desligar":
        robo.actuatorOff()
    elif action == "atual":
        robo.current()
    elif action == "savePosition":
        if filenames:
            for filename in filenames:
                robo.setposition(filename)
        else:
            print("Filename not specified.")
    else:
        print("Comando desconhecido")

def ask_for_action():
    questions = [
        inquirer.List('action',
                      message="Escolha um comando",
                      choices=['moveToFilePosition', 'ligar', 'desligar', 'mover', 'atual', 'savePosition']),
    ]
    answers = inquirer.prompt(questions)
    return answers['action']

def ask_for_movement_args():
    questions = [
        inquirer.List('direction', message="Choose a direction", choices=['x', 'y', 'z', 'r']),
        inquirer.Text('distance', message="Enter the distance"),
    ]
    answers = inquirer.prompt(questions)
    return answers['direction'], answers['distance']

def ask_for_filenames():
    question = [
        inquirer.Text('filenames', message="Diga o ou os arquivos separados por vírgula (,)"),
    ]
    answer = inquirer.prompt(question)
    filenames = answer['filenames'].split(',')
    filenames = [filename.strip() for filename in filenames if filename.strip()]
    return filenames

def main():
    while True:
        action = ask_for_action()
        if action == 'mover':
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

if __name__ == "__main__":
    main()