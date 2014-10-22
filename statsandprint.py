import math
import start
import sys 


def standard_dev(lists):
    
    if len(lists) == 0:
        return 0
    
    x = len(lists)
    
    if(x == 0):
        x = 1
    avg = float(sum(lists))/x
    dev = []
    
    for x in lists:
        dev.append(x - avg)

    sqr = []    
    for x in dev:
        sqr.append(x * x)
        
    mean = sum(sqr)/len(sqr)
    standard_deviation = math.sqrt(sum(sqr)/(len(sqr)-1))    

    return standard_deviation


def getandprintstats(arrayofdelay,array_of_thoroughput, array_of_seeds, array_of_input ):

    T = int(array_of_input[4])

    
    Delaystddev=standard_dev(arrayofdelay)
    Thoroughputstddev = standard_dev(array_of_thoroughput)

    Delaysum = 0
    for adelay in (arrayofdelay):
        Delaysum = Delaysum + adelay
    
    Delayavg = Delaysum/(len(array_of_thoroughput))


    if ((sum(arrayofdelay) or len(arrayofdelay))==0):
        arrayofdelay=1
        
    Delayavg=sum(arrayofdelay)/(len(arrayofdelay))


    Thoroughputsum = 0
    for athoroughput in (array_of_thoroughput):
        Thoroughputsum = Thoroughputsum + athoroughput
    
    Thoroughputavg = Thoroughputsum/(len(array_of_thoroughput))

    Delayc1 = float((Delayavg)-(2.776*(Delaystddev/(math.sqrt(T)))))
    Delayc2 = float((Delayavg)+(2.776*(Delaystddev/(math.sqrt(T)))))

    Thoroughc1 = float((Thoroughputavg)-(2.776*(Thoroughputstddev/(math.sqrt(T)))))
    Thoroughc2 = float((Thoroughputavg)+(2.776*(Thoroughputstddev/(math.sqrt(T)))))
    
    
    contain = ""
    for x in array_of_input:
        contain = contain + x + " "
    print(contain)

    print("Delay Avg stats:"+str(Delayavg)+" "+"("+ str(Delayc1)+ "," + str(Delayc2)+")")
    print("Thoroughput stats: "+str(Thoroughputavg)+" "+"("+ str(Thoroughc1)+ "," + str(Thoroughc2)+")")