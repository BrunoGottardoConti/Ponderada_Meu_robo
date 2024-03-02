import json  # Importa o módulo para lidar com JSON

# Função para criar um arquivo JSON com os parâmetros especificados
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
    # Escreve os dados em um arquivo JSON
    with open(f'{name}.json', 'w') as file:
        json.dump(data, file, indent=4)
    print(f'JSON file "{name}.json" created.')

# Função para ler um arquivo JSON e retornar seus dados
def readJson(name):
    # Adiciona a extensão '.json' se não estiver presente no nome do arquivo
    filename = f"{name}" if name.endswith('.json') else f"{name}.json"
    try:
        # Tenta abrir e ler o arquivo JSON
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        # Lida com o erro caso o arquivo não seja encontrado
        print(f'Error: File "{filename}" not found.')
        return {}


