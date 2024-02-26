# from robot import robot
# import inquirer

# robo = robot()

# def execute_command(action, direction=None, distance=None):
#     movements = {
#         'x': lambda: robo.moveX(float(distance)),
#         'y': lambda: robo.moveY(float(distance)),
#         'z': lambda: robo.moveZ(float(distance)),
#         'r': lambda: robo.moveR(float(distance))
#     }

#     commands = {
#         "home": lambda: robo.moveHome(),
#         "ligar": lambda: robo.actuatorOn(),
#         "desligar": lambda: robo.actuatorOff(),
#         "mover": lambda: movements[direction]() if direction in movements else print("Sentido inválido desconhecido."),
#         "atual": lambda: robo.current(),
#         "setHome": lambda: robo.setHome()
#     }

#     if action in commands:
#         commands[action]()
#     else:
#         print("Comando desconhecido.")

# def ask_for_command():
#     questions = [
#         inquirer.List('action',
#                       message="Escolha um comando",
#                       choices=['home', 'ligar', 'desligar', 'mover', 'atual', 'setHome']),
#     ]
#     answers = inquirer.prompt(questions)
#     return answers['action']

# def ask_for_movement_args():
#     questions = [
#         inquirer.List('direction', message="Qual direção?", choices=['x', 'y', 'z', 'r']),
#         inquirer.Text('distance', message="Qual a distância?"),
#     ]
#     answers = inquirer.prompt(questions)
#     return answers['direction'], answers['distance']

# def main():
#     while True:
#         action = ask_for_command()
#         if action == 'mover':
#             direction, distance = ask_for_movement_args()
#             execute_command(action, direction, distance)
#         else:
#             execute_command(action)

# if __name__ == "__main__":
#     main()

from robot import Robot
import inquirer

robo = Robot()

def execute_command(action, direction=None, distance=None):
    # Define movement functions for each direction
    movements = {
        'x': lambda: robo.moveX(float(distance)),
        'y': lambda: robo.moveY(float(distance)),
        'z': lambda: robo.moveZ(float(distance)),
        'r': lambda: robo.moveR(float(distance))
    }

    # Define commands for home position, actuator control, and movements
    commands = {
        "home": lambda: robo.moveHome(),
        "ligar": lambda: robo.actuatorOn(),
        "desligar": lambda: robo.actuatorOff(),
        "mover": lambda: movements[direction]() if direction in movements else print("Invalid direction."),
        "atual": lambda: robo.current(),
        "setHome": lambda: robo.setHome()
    }

    # Execute the given command
    if action in commands:
        commands[action]()
    else:
        print("Unknown command.")

def ask_for_command():
    # Prompt the user to select a command
    questions = [
        inquirer.List('action',
                      message="Choose a command",
                      choices=['home', 'ligar', 'desligar', 'mover', 'atual', 'setHome']),
    ]
    answers = inquirer.prompt(questions)
    return answers['action']

def ask_for_movement_args():
    # Prompt the user for movement direction and distance if the action is 'mover'
    questions = [
        inquirer.List('direction', message="Which direction?", choices=['x', 'y', 'z', 'r']),
        inquirer.Text('distance', message="What distance?"),
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
