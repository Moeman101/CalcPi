import random
import statistics as stat #needed for mean function
import matplotlib.pyplot as plt 

def random_coords(NumRanCo): #possible for graphical display
    set = []
    for pair in range(NumRanCo):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        Circle = bool ((x**2+y**2)**0.5 <= 1) #Checks if in circle
        set.append([x,y,Circle])
    return set #returns list with tuples of: (x,y,within circle or not)

def GraphChart():
    pass

#Program start
Volume = [10,50,100,500,1000,5000,10000]#modify these numbers for darts thrown
monty= 10 #how often a given number of darts are thrown
for RandomDarts in Volume:
    NCircle = []
    xCoordin = []
    xCoordout = []
    yCoordin = []
    yCoordout = []
    for freq in range(monty): #monty carlo of random_coords
        DartData = random_coords(RandomDarts)
        InCircle = 0
        for Dart in DartData:
            if Dart.pop(2):
                InCircle+=1
                xCoordin.append(Dart.pop())
                yCoordin.append(Dart.pop())  
            else:
                xCoordout.append(Dart.pop())
                yCoordout.append(Dart.pop())  
            
        NCircle.append(InCircle)
    plt.plot(xCoordin,yCoordin,'ro')
    plt.plot(xCoordout,yCoordout,'bo')
    plt.axis([-1,1,-1,1])
    plt.title(str(RandomDarts))
    plt.show()
    
    AveCircle = stat.mean(NCircle)
    pi = (AveCircle/RandomDarts)*4
    print(AveCircle)
    print("Pi is approximatly " + str(pi))