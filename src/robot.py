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
        self.device.move_to(self.x + x, self.y, self.z, self.r, wait=True)
        self._update_pose()
        print("Moved X to:", self.x)

    def moveY(self, y):
        self.device.move_to(self.x, self.y + y, self.z, self.r, wait=True)
        self._update_pose()
        print("Moved Y to:", self.y)

    def moveZ(self, z):
        self.device.move_to(self.x, self.y, self.z + z, self.r, wait=True)
        self._update_pose()
        print("Moved Z to:", self.z)

    def moveR(self, r):
        self.device.move_to(self.x, self.y, self.z, self.r + r, wait=True)
        self._update_pose()
        print("Rotated R to:", self.r)

    def moveHome(self):
        json = dobotJson.readJson("home")
        self.device.move_to(json['x'], json['y'], json['z'], json['r'], wait=True)
        self._update_pose()
        print("Moved to home position")

    def setHome(self):
        dobotJson.makeJson('home', self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4, "linear", "on")
        print("Home position set")

    def actuatorOn(self):
        self.device.suck(True)
        print("Actuator turned on")

    def actuatorOff(self):
        self.device.suck(False)
        print("Actuator turned off")

    def current(self):
        print(f"Current Position: x={self.x}, y={self.y}, z={self.z}, r={self.r}")
