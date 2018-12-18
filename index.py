#Author: Nhlonipho Sonke Gumede
#email: ns.gumede2@gmail.com


import sys
sys.path.insert(0, '.') #current path
from rovers import Rovers

rover = Rovers() #Rovers

class Index:

    def __init__(self):
        self.coord = list()
        self.commands = ""
        self.RoversTotal = 0

    def GetInput(self):
        #Get Input from console

        self.GetNumberOfRobots()
        print "\n" #Print empty line
        robots = [] #Empty array

        #loop through number of rovers/robots entered
        for x in range(self.RoversTotal):
            index = x + 1 #Robot index

            #Validate Inputs
            self.ValidateCoord(index)
            self.ValidateCmd(index)
            
            print "\n" #Print empty line
            #append to array

            list_of_dictionaries = {
                "Number": index,
                "Points": [int(self.coord[0]), int(self.coord[1]), str(self.coord[2]).upper()], #Make an array from coord input
                "Commands": self.commands.upper() #Change commands to upper case
            }

            robots.append(list_of_dictionaries) #append to an array


        for obj in robots:

            print "Moving Robot #",obj["Number"]

            rover.SetValues(obj["Points"],obj["Commands"])
            rover.MakeAmove()
            
            print "............................"



    def ValidateCoord(self,index):
        #get input
        self.coord = list(raw_input("Enter coordinates for Robot #"+ str(index) + " [ e.g: 5 4 E ]: ").replace(" ","")) #remove white spaces

        #First element
        try:
            int(self.coord[0])
            pass
        except ValueError:
            print "First value must be numeric, please try again"
            self.ValidateCoord(index)

        #Second element
        try:
            int(self.coord[1])
            pass
        except ValueError:
            print "Second value must be numeric, please try again"
            self.ValidateCoord(index)

        #Last element
        try:
            int(self.coord[2])
            print "Last value must be a string, please try again"
            self.ValidateCoord(index)
        except ValueError:
            if self.coord[2].upper() !="S" or self.coord[2].upper() !="N" or self.coord[2].upper() !="W" or self.coord[2].upper() !="E":
                print "Last value must only be E,W,S or N"
                self.ValidateCoord(index)
            else:
                pass

        
            
        if len(self.coord) !=3:
            print "Coordinates must be 3 charector long"
            self.ValidateCoord(index)



    def ValidateCmd(self,index):
        commands = list(raw_input("Enter commands for Robot #"+str(index) +" [e.g: MMMRML ]: ").replace(" ",""))

        #serach for charectors
        for letter in commands:
            if letter !="M" or letter !="R" or letter !="L":
                print "Command string must only contain letter M,R or L"
                self.ValidateCmd(index)

        self.commands = commands 

    def GetNumberOfRobots(self):
        try:
            self.RoversTotal = int(raw_input("Please Enter Number of Robots to control: "))
        except ValueError:
            print "Value must be numeric, try again"
            self.GetNumberOfRobots()
        

#Initialize 
index = Index()
index.GetInput()
