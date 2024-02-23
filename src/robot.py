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
        self.device.move_to(self.x+x, self.y, self.z, self.r, wait=True)
        self._update_pose()
        print("Moving x")
        print(self.device.pose())

    def moveY(self, y):
        self.device.move_to(self.x, self.y+y, self.z, self.r, wait=True)
        self._update_pose()
        print("Moving y")
        print(self.device.pose())

    def moveZ(self, z):
        self.device.move_to(self.x, self.y, z, self.r, wait=True)
        self._update_pose()
        print("Moving z")
        print(self.device.pose())

    def moveR(self, r):
        self.device.move_to(self.x, self.y, self.z, r, wait=True)
        self._update_pose()
        print("Moving r")
        print(self.device.pose())

    def moveHome(self):
        json = dobotJson.readJson("home")
        self.device.move_to(json['x'], json['y'], json['z'], json['r'], wait=True)
        self._update_pose()
        print("Moving to home")
        print(self.device.pose())

    def setHome(self):
        dobotJson.makeJson('home', self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4, "linear", "on")

    def actuatorOn(self):
        self.device.suck(True)
        print("Actuator on")

    def actuatorOff(self):
        self.device.suck(False)
        print("Actuator off")

    def current(self):
        print(f"Posição atual: x={self.x}, y={self.y}, z={self.z}, r={self.r}")