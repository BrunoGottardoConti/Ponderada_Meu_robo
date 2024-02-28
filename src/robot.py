import scanport
import dobotJson
import pydobot

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

    def moveToPositionFromFile(self, filename):
        self._update_pose()
        json = dobotJson.readJson(filename)
        if json:
            self.device.move_to(json['x'], json['y'], json['z'], json['r'], wait=True)
            self._update_pose()
            print(f"Moveu para a posição de nome: {filename}.json")
        else:
            print(f"Falha ao mover para: file {filename}.json not found.")


    def setposition(self, filename='home'):
        self._update_pose()
        dobotJson.makeJson(filename, self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4, "linear", "off")
        print(f"Posição salva como {filename}")

    def actuatorOn(self):
        self.device.suck(True)
        print("Atuador ligado")

    def actuatorOff(self):
        self.device.suck(False)
        print("Atuador desligado")

    def current(self):
        self._update_pose() 
        print(f"Posição atual: x={self.x}, y={self.y}, z={self.z}, r={self.r}")
