from multiprocessing.resource_sharer import stop
from urllib import robotparser
from RobotArm import RobotArm



robotArm = RobotArm('exercise 12')
robotArm.speed = 5
# Jouw python instructies zet je vanaf hier:
for x in range(25):
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan()=="red":
        for x in range(25):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(25):
            robotArm.moveLeft()




    else:
        robotArm.drop()
        robotArm.moveRight()





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()