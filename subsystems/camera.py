__author__ = "nikolojedison"
from wpilib.command import Subsystem
import wpilib

class Camera(Subsystem):

    def __init__(self, robot):
        """Initialise the camera and the camera server"""

        #these are all actually really self explanatory. Wonder if they work.
        self.camera.setExposureManual(50)
        self.camera.setBrightness(80)
        self.camera.setFPS(10)
        self.camera.setSize(320, 240)
        self.camera.setWhiteBalanceAuto()
        self.camera.setQuality(30)
        self.camera.updateSettings() #update with the new settings so it actually does what we want it to

        server = wpilib.CameraServer.getInstance() #set up the camera server
        server.startAutomaticCapture(self.camera) #start the camera server

    def initDefaultCommand(self):
        #Camera don't need nothin'
        pass

    def log(self):
        #logging *could* be a thing, but meh
        pass
