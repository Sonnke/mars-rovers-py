#Author: Nhlonipho Sonke Gumede
#email: ns.gumede2@gmail.com


import sys
sys.path.insert(0, '.')
from rovers import Rovers

rover = Rovers() #Rovers




#Get Input from console
rovers_total = int(raw_input("Please Enter Number of Robots to control: "))
print "\n" #Print empty line
robots = [] #Empty array

#loop through number of rovers/robots entered
for x in range(rovers_total):
    index = x + 1 #Robot index

    coord = list(raw_input("Enter coordinates for Robot #"+ str(index) + " [ e.g: 5 4 E ] ").replace(" ","")) #remove white spaces
    #coord = rover.ValidateInputPoints(validateCoord,num)

    commands = raw_input("Enter commands for Robot #"+str(index) +" [e.g: MMMRML ] ")
    print "\n" #Print empty line
    #append to array

    list_of_dictionaries = {
        "Number": index,
        "Points": [int(coord[0]), int(coord[1]), str(coord[2]).upper()], #Make an array from coord input
        "Commands": commands.upper() #Change commands to upper case
    }

    robots.append(list_of_dictionaries) #append to an array


for obj in robots:

    print "Moving Robot #",obj["Number"]

    rover.SetValues(obj["Points"],obj["Commands"])
    rover.MakeAmove()
    
    print "............................"