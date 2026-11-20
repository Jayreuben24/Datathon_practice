## CASE 3 — Logical Programming and Resistor Color Coding 
## imports
import pandas as pd
import math as ma
## resistor color coding list

resistorColorCoding = [[ "black", 0 , 1 , "-"], 
                       ["brown", 1 , 10 , 0.01] , 
                       ["red" , 2 , 100 ,0.02],
                       ["orange", 3 , 1000, "-"],
                       ["yellow", 4, 10000, "-"],
                       ["green", 5, 100000, 0.005],
                       ["blue", 6, 1000000, 0.0025],
                       ["violet", 7, 10000000, 0.001],
                       ["gray", 8 , 100000000 , 0.0005],
                       ["white" , 9 , 1000000000 , "-"],
                       ["gold" , "-" , 0.1 , 0.05],
                       ["silver" , "-" , 0.01 , 0.10]
                       ]

## resistor color coding dataframe
resistorColorCodes = pd.DataFrame(resistorColorCoding, columns= ("Color","Digit","Multiplier","Tolerance"))
print (resistorColorCodes)

## inputs: colors
## input validations

def get_color(text):
    while True:
        try: 
            value = str(input(text)).strip().lower()
        except ValueError:
            print("Please input valid color")
            continue
        if value not in resistorColorCodes["Color"].values:
            print(f'{value} is not a color or not belong to the resistor color coding')
            continue
        break
    return(value)

## enter first digit
while True:
    firstColor = get_color("Please input the first color: ")
    if firstColor == "gold" or firstColor == "silver":
        print("Silver and Gold cannot be the first color.")
        continue
    break

firstDigit= resistorColorCodes.loc[resistorColorCodes["Color"]==firstColor,"Digit"].values[0]

## enter second digit
while True:
    secondColor = get_color("Please input the second color: ")
    if secondColor == "gold" or secondColor == "silver":
        print("Silver and Gold cannot be the second color.")
        continue
    break
secondDigit = resistorColorCodes.loc[resistorColorCodes["Color"]==secondColor,"Digit"].values[0]

## enter 3rd color
thirdColor = get_color("Please input the third color: ")

multiplier = resistorColorCodes.loc[resistorColorCodes["Color"]==thirdColor, "Multiplier"].values[0] 

## enter 4th color
while True:
    fourthColor = get_color("Please input the fourth color: ")
    if fourthColor == "black" or fourthColor == "orange" or fourthColor == "yellow" or fourthColor == "white":
        print("Please enter correct tolerance, check again the color.")
        continue
    break

tolerance = resistorColorCodes.loc[resistorColorCodes["Color"]==fourthColor, "Tolerance"].values[0]

print(f'Your resistor color coding is {firstColor} , {secondColor} , {thirdColor} , {fourthColor}')

## calculate the resistance with tolerance
firstSecondColor = int(str(firstDigit) + str(secondDigit))
resistance = firstSecondColor * multiplier
resistorTolerance = resistance * tolerance
upperTolerance = resistance + resistorTolerance
lowertolerance = resistance - resistorTolerance
print(f'Resistance= {resistance} ohms')
print(f'Tolerance range ({lowertolerance:.2f} - {upperTolerance:.2f})')

      
      


        
            
        
        