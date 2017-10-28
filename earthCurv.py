#EarthCurvature Calculator

from math import cos, acos, pi, radians, degrees
def calcDrop(paramDistance,Perimetre,earthRadius):
    Angle = (paramDistance * 360)/Perimetre
    adjacent = cos(radians(Angle)) * earthRadius
    hiddenDrop = earthRadius - adjacent
    hiddenHeight = earthRadius * ( ((adjacent + hiddenDrop)/adjacent) -1 )
    
    
    print ("Earth Circumference is:",Perimetre)
    print ("Earth Angle for a Distance of 1KM: ",AngleFor1K)
    print ("Angle of the Object Distance: ",Angle)
    print ("Distance Adjacent to the Object Angle: ",adjacent)
    print ("Hidden Drop(in meter): ",hiddenDrop*1000)
    print ("Hidden Objects Max Height from the Surface(in meter): ",hiddenHeight * 1000)

def calcEyeDrop(paramDistance,Perimetre,earthRadius,eyeHeight):
    Angle = (paramDistance * 360)/Perimetre
    cosine_alpha1 = earthRadius/(earthRadius+(eyeHeight/1000))
    alpha1 = degrees(acos(cosine_alpha1))
    alpha2 = Angle - alpha1
    hiddenHeight = (earthRadius / (cos(radians(alpha2)))) - earthRadius
    
    
    print ("Earth Circumference is:",Perimetre)
    print ("Earth Angle for a Distance of 1KM: ",AngleFor1K)
    print ("Angle of the Object Distance: ",Angle)
    print ("Eye/Lens Height in KM: ", eyeHeight/1000)
    print ("Cosine of Alpha1 angle i: ", cosine_alpha1)
    print ("Alpha1 Angle is: ",alpha1)
    print ("Alpha2 Angle is: ",alpha2)
    print ("Hidden Objects Max Height from the Surface(in meter): ",hiddenHeight * 1000)

print ("Welcome to the Slaycken Earth Curve Calc")

earthRad = 6371#km
Per = 2 * pi * earthRad #Earth Circumference
AngleFor1K = 360 / Per

Distance = input("What is the Distance of the Object in KM ") #Distance Parameter
Eye = input("What is the Height from the ground to the Observer Lens in meters ") #Distance Parameter

if (Eye>0):
    calcEyeDrop(Distance,Per,earthRad,Eye)    
else: 
    calcDrop(Distance,Per,earthRad)
