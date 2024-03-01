import scanport
import dobotJson
import pydobot
import os
from time import sleep
import re

def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

class Robot:
    def __init__(self):
        self.device = pydobot.Dobot(port=scanport.scanport())
        self._update_pose()

    def _update_pose(self):
        self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4 = self.device.pose()

    def moveX(self, x):
        self._update_pose()
        self.device.move_to(self.x + x, self.y, self.z, self.r, wait=True)
        self._update_pose()
        print("Moveu para X:", self.x)

    def moveY(self, y):
        self._update_pose()
        self.device.move_to(self.x, self.y + y, self.z, self.r, wait=True)
        self._update_pose()
        print("Moveu para Y:", self.y)

    def moveZ(self, z):
        self._update_pose()
        self.device.move_to(self.x, self.y, self.z + z, self.r, wait=True)
        self._update_pose()
        print("Moveu para Z:", self.z)

    def moveR(self, r):
        self._update_pose()
        self.device.move_to(self.x, self.y, self.z, self.r + r, wait=True)
        self._update_pose()
        print("Rotacionando para:", self.r)

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
                    print(f"Nenhum modo de atuador encontrado em {filename}, assumindo 'off'.")
                    self.actuatorOff()

                print(f"Moveu para: {filename}")
            else:
                print(f"Failha ao mover para: file {filename} not found.")

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


    def setposition(self, filename='home'):
        self._update_pose()
        dobotJson.makeJson(filename, self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4, "linear", "off")
        print(f"Posição salva como {filename}")

    def actuatorOn(self):
        self.device.suck(True)
        sleep(0.2)
        print("Atuador ligado")

    def actuatorOff(self):
        self.device.suck(False)
        print("Atuador desligado")

    def current(self):
        self._update_pose() 
        print(f"Posição atual: x={self.x}, y={self.y}, z={self.z}, r={self.r}")
