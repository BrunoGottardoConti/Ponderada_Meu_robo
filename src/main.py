from robot import robot
import inquirer

roboti = robot()

def execute_command(action, direction=None, distance=None):
    movements = {
        'x': lambda: roboti.moveX(float(distance)),
        'y': lambda: roboti.moveY(float(distance)),
        'z': lambda: roboti.moveZ(float(distance)),
        'r': lambda: roboti.moveR(float(distance))
    }

    commands = {
        "home": lambda: roboti.moveHome(),
        "ligar": lambda: roboti.actuatorOn(),
        "desligar": lambda: roboti.actuatorOff(),
        "mover": lambda: movements[direction]() if direction in movements else print("Sentido inválido desconhecido."),
        "atual": lambda: roboti.current(),
        "setHome": lambda: roboti.setHome()
    }

    if action in commands:
        commands[action]()
    else:
        print("Comando desconhecido.")

def ask_for_command():
    questions = [
        inquirer.List('action',
                      message="Escolha um comando",
                      choices=['home', 'ligar', 'desligar', 'mover', 'atual', 'setHome']),
    ]
    answers = inquirer.prompt(questions)
    return answers['action']

def ask_for_movement_args():
    questions = [
        inquirer.List('direction', message="Qual direção?", choices=['x', 'y', 'z', 'r']),
        inquirer.Text('distance', message="Qual a distância?"),
    ]
    answers = inquirer.prompt(questions)
    return answers['direction'], answers['distance']

def main():
    while True:
        action = ask_for_command()
        if action == 'mover':
            direction, distance = ask_for_movement_args()
            execute_command(action, direction, distance)
        else:
            execute_command(action)

if __name__ == "__main__":
    main()