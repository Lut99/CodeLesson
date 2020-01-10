# PUZZEL.py
#   by Lut99
#
# Dit bestand is waar je de puzzel in maakt. Vul de functies hieronder in, en
#   verander alleen tussen "VANAF HIER" en "TOT HIER".


def Level1(robot):
    while True:
        obj = robot.kijk()
        if obj == "Rand":
            robot.draai("rechts")
        else:
            robot.stap()
