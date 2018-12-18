#Author: Nhlonipho Sonke Gumede
#email: ns.gumede2@gmail.com


import time

class Rovers:
    def __init__(self):
        self.Points = []
        self.Commands = ""
       

    
    #Set Values
    def SetValues(self,Points,Commands):
        self.Points = Points
        self.Commands = Commands



    #Make Movements
    def Movements(self,pole,axis):
        NewCoorDinates = {
            "N": [axis[0], (axis[1] + 1),"N"], #Move upward Y axis 
            "S": [axis[0], (axis[1] - 1),"S"], #Move move downward Y axis
            "W": [(axis[0] - 1),axis[1], "W"], #Move to the left, X axis
            "E": [(axis[0] + 1),axis[1],"E"] #Move to the Right, X axis
        }

        return NewCoorDinates.get(pole,axis)


    #Make A turn
    def MakeAturn(self,pole,orientation):
        position = pole+orientation

        angle = {
            "NR": 90 - 90, #From 90 , Turn 90 degrees right
            "NL": 90 + 90, #From 90, Turn 90 degrees left
            "SR": 270 - 90, #From angle 270, turn 90 degress right
            "SL": 270 + 90, #From angle 270, turn 90 degress left
            "WR": 180 + 90, #From angle 180, turn 90 degress right
            "WL": 180 + 90, #From angle 180, turn 90 degrees left
            "ER": 360 - 90, #From angle 360, turn 90 degrees right
            "EL": 0 + 90 #From angle 0, turn 90 degrees left 
        }

        return angle.get(position,90)



    
    def GetPoleByAngle(self,angle):
        pole = {
            90: "N", #North pole
            180:"W", #West Pole
            270:"S", #South Pole
            360:"E" #East Pole
        }

        return pole.get(angle,"E")

    #Update Points
    def UpdatePoints(self,Pole,Points):
        return [Points[0], Points[1], Pole]

    
    #Make Movements
    def MakeAmove(self):

        Points = self.Points
        Pole = self.Points[2]
        Commands = list(self.Commands) #string to array
        Angle = 0

        for Cmd in Commands:
            if Cmd == "M": #Move one grid point
                time.sleep(1) #delay output for 1 second
                Points = self.Movements(Pole,Points)
                print "".join(str(x)+" " for x in Points) #format array to string

            else: #make a turn
                time.sleep(1) #delay output for 1 second
                Angle = self.MakeAturn(Pole,Cmd) #Make a turn
                Pole = self.GetPoleByAngle(Angle) #Get an angle
                Points = self.UpdatePoints(Pole,Points) #return new points
                print "".join(str(i)+" " for i in Points) #format array to string



