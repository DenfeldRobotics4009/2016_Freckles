__author__ = "nikolojedison"

from wpilib.command import CommandGroup
from wpilib.command import WaitCommand

from commands.auto.spool import Spool
from commands.auto.roll import Roll

class Shoot(CommandGroup):
    """Command that runs the trigger back, spools, then fires."""

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        shoot_generator = [
        Roll(robot, 1, .5),
        WaitCommand(1),
        Spool(robot, 1, 1),
        WaitCommand(2),
        Roll(robot, -1, .25),
        WaitCommand(.5),
        Roll(robot, 0, .5),
        Spool(robot, 0, .5),
        ]
        for i in shoot_generator: self.addSequential(i)
