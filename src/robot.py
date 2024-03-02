import scanport  # Importa o módulo para escanear a porta de conexão
import dobotJson  # Importa o módulo para lidar com arquivos JSON para o Dobot
import pydobot  # Importa o módulo principal para controlar o Dobot
import os  # Importa o módulo para interagir com o sistema operacional
from time import sleep  # Importa a função sleep para adicionar pausas no código
import re  # Importa o módulo para lidar com expressões regulares

# Função auxiliar para converter texto em números inteiros, se possível
def atoi(text):
    return int(text) if text.isdigit() else text

# Função auxiliar para classificar uma lista mista de strings e números
def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

# Classe principal para controlar o robô
class Robot:
    # Método de inicialização para conectar-se ao Dobot e obter a posição atual
    def __init__(self):
        self.device = pydobot.Dobot(port=scanport.scanport())
        self._update_pose()

    # Método interno para atualizar a posição atual do Dobot
    def _update_pose(self):
        self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4 = self.device.pose()

    # Métodos para mover o robô em cada eixo
    def moveX(self, x):
        self._update_pose()
        self.device.move_to(self.x + x, self.y, self.z, self.r, wait=True)
        self._update_pose()

    def moveY(self, y):
        self._update_pose()
        self.device.move_to(self.x, self.y + y, self.z, self.r, wait=True)
        self._update_pose()

    def moveZ(self, z):
        self._update_pose()
        self.device.move_to(self.x, self.y, self.z + z, self.r, wait=True)
        self._update_pose()

    def moveR(self, r):
        self._update_pose()
        self.device.move_to(self.x, self.y, self.z, self.r + r, wait=True)
        self._update_pose()

    # Move o robô para posições definidas em arquivos JSON
    def moveToPositionFromFiles(self, filenames):
        self._update_pose()
        for filename in filenames:
            json_data = dobotJson.readJson(filename)
            if json_data:
                self.device.move_to(json_data['x'], json_data['y'], json_data['z'], json_data['r'], wait=True)
                self._update_pose()
                if json_data.get('actuator') == 'on':
                    self.actuatorOn()
                elif json_data.get('actuator') == 'off':
                    self.actuatorOff()
                else:
                    self.actuatorOff()
            else:
                print(f"Failed to move to: file {filename} not found.")

    # Executa uma série de movimentos especificados em um diretório
    def executeTask(self, task_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        task_directory = os.path.join(script_dir, task_name)
        
        if os.path.exists(task_directory) and os.path.isdir(task_directory):
            filenames = [f for f in os.listdir(task_directory) if f.endswith('.json')]
            filenames.sort(key=natural_keys)
            filepaths = [os.path.join(task_directory, filename) for filename in filenames]
            self.moveToPositionFromFiles(filepaths)
        else:
            print(f"Task directory {task_directory} not found.")

    # Salva a posição atual do robô em um arquivo JSON
    def setposition(self, filename='home'):
        self._update_pose()
        dobotJson.makeJson(filename, self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4, "linear", "off")

    # Liga o atuador
    def actuatorOn(self):
        self.device.suck(True)
        sleep(0.2)

    # Desliga o atuador
    def actuatorOff(self):
        self.device.suck(False)

    # Imprime a posição atual do robô
    def current(self):
        self._update_pose() 
        print(f"Current position: x={self.x}, y={self.y}, z={self.z}, r={self.r}")
