# PUZZEL.py
#   by Lut99
#
# Dit bestand is waar je de puzzel in maakt. Vul de functies hieronder in, en
#   verander alleen tussen "VANAF HIER" en "TOT HIER".


def Level1(robot):
    # VANAF HIER

    for i in range(7):
        robot.stap()

    robot.draai("rechts")

    for i in range(5):
        robot.stap()

    # TOT HIER


def Level2(robot):
    # VANAF HIER

    for i in range(6):
        robot.stap()
    robot.draai("rechts")

    while True:
        obj = robot.kijk()
        if obj == "Vlag":
            robot.stap()
            break
        robot.stap()

    # TOT HIER

def Level3(robot):
    x, y = robot.kijk_vlag()

    # VANAF HIER

    for i in range(x - 2):
        robot.stap()
    robot.draai("rechts")
    for i in range(y - 2):
        robot.stap()

    # TOT HIER
