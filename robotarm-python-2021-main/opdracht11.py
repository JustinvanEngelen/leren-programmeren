from string import whitespace
from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 5


# Jouw python instructies zet je vanaf hier:
for x in range(11):
    robotArm.moveRight()
quit
for x in range (9):
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()

        




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()