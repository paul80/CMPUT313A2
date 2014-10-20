def standard_dev(lists):
    
    if len(lists) == 0:
        return 0
    
    x = len(lists)
    if(x == 0):
        x = 1
    avg = float(sum(lists))/x
    #print(avg)
    dev = []
    for x in lists:
        dev.append(x - avg)
        #print(dev)
    sqr = []
    
    for x in dev:
        sqr.append(x * x)
        
    #print(sqr)
    mean = sum(sqr)/len(sqr)
    #print(mean)
    standard_deviation = math.sqrt(sum(sqr)/(len(sqr)-1))    
    return standard_deviation


def getandprintstats(averageframecounter,array_of_thoroughput, array_of_seeds, array_of_input ):

    T = int(array_of_input[5])

    
    Framestddev=standard_dev(averageframecounter)
    Thoroughputstddev = standard_dev(array_of_thoroughput)

        #Framesum = Framesum+numofframes
    if (averageframecounter==0):
        averageframecounter=1
    Frameavg=sum(averageframecounter)/(len(averageframecounter))


    Thoroughputsum = 0
    for athoroughput in (array_of_thoroughput):
        Thoroughputsum = Thoroughputsum + athoroughput
    
    Thoroughputavg = Thoroughputsum/(len(array_of_thoroughput))

    Framec1 = float((Frameavg)-(2.776*(Framestddev/(math.sqrt(T)))))
    Framec2 = float((Frameavg)+(2.776*(Framestddev/(math.sqrt(T)))))

    Thoroughc1 = float((Thoroughputavg)-(2.776*(Thoroughputstddev/(math.sqrt(T)))))
    Thoroughc2 = float((Thoroughputavg)+(2.776*(Thoroughputstddev/(math.sqrt(T)))))
    

    
    contain = ""
    for x in array_of_input:
        contain = contain + x + " "
    print(contain)

    print("Frame stats:"+str(Frameavg)+" "+"("+ str(Framec1)+ "," + str(Framec2)+")")
    print("Thoroughput stats: "+str(Thoroughputavg)+" "+"("+ str(Thoroughc1)+ "," + str(Thoroughc2)+")")