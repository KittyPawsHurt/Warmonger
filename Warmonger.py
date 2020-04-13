##########################
# Warmonger Army Creator #
#
#
#
##########################

# Imports #
import collections
import csv
import pandas as pd

# setup unit dictionaries #

unit1 =	{"name": "Unit One", "faction": "red", "cost": 100, "unique": "yes"}
unit2 =	{"name": "Unit Two","faction": "red","cost": 10,"unique": "no"}
unit3 =	{"name": "Unit Three","faction": "blue","cost": 100,"unique": "yes"}
unit4 =	{"name": "Unit Four","faction": "blue","cost":20,"unique": "no"}
unit5 =	{"name": "Unit Five","faction": "blue","cost":25,"unique": "no"}
unit6 =	{"name": "Unit Six","faction": "red","cost":15,"unique": "no"}
unit7 =	{"name": "Unit Seven","faction": "red","cost":15,"unique": "yes"}

UnitList = collections.ChainMap(unit1,unit2,unit3,unit4,unit5,unit6,unit7)

# setup input functions #

def SetArmyCost ():
    ArmyCost = input("How many points? ")
    if ArmyCost.isnumeric():
        print(ArmyCost)
    else:
        print("Needs to be a number.")
        SetArmyCost()

def SetArmyFaction():
    ArmyFaction = input("What Faction? (Red/Blue) ")
    if ArmyFaction.lower() == "red" or ArmyFaction.lower() == "blue":
        print(ArmyFaction.lower())
    else:
        print("Please enter supported faction.")
        SetArmyFaction()

# unit sorting test function #

def PrintFactionUnits():
    with open('UnitData.csv') as UnitData:
        reader = csv.DictReader(UnitData)
        for SetArmyFaction in csv.DictReader(UnitData):
            print (csv.DictReader("name"))

# Run Program #
with open('UnitData.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

SetArmyCost()
SetArmyFaction()
PrintFactionUnits()
