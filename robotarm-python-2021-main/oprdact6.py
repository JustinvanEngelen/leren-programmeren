from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
point = 0
point = int (point)


for x in range(7):
    robotArm.moveRight()
robotArm.drop()
robotArm.grab()

robotArm.moveRight()
robotArm.drop()
while point < 7:
    if point < 7:
        robotArm.moveLeft() 
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        point = point+1
    else:
        quit()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
