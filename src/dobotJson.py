import json

def makeJson(name, x, y, z, r, j1, j2, j3, j4, mode, actuator):
    data = {
        'x': x,
        'y': y,
        'z': z,
        'r': r,
        'j1': j1,
        'j2': j2,
        'j3': j3,
        'j4': j4,
        'mode': mode,
        'actuator': actuator
    }
    with open(f'{name}.json', 'w') as file:
        json.dump(data, file, indent=4)
    print(f'JSON file "{name}.json" criada.')

def readJson(name):
    try:
        with open(f'{name}.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f'Error: File "{name}.json" not found.')
        return {}

