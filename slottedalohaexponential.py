
def findaspot(node, currentslot, highestslot, allslots):
    #exponential backoff
    #start with 2**1 max 2**9
    generated = 0
    keepgoing = True
    delay = 0
    exponent = 1
    currentslot = currentslot
    
    #forgot to do a random slot
    while (keepgoing):
        adder = 2**exponent
        adder = random.randint(1,adder+1)
        generated = generated + 1
        delay = generateframe.delaycounter(currentslot,currentslot+adder) + delay       
        
        if (node not in allslots[currentslot+adder]):
            return currentslot+adder, generated, delay
        
        elif (currentslot+adder>highestslot):
            return 0, generated, delay
        
        else:
            if (exponent<9):
                exponent = exponent + 1
                
        currentslot = currentslot + adder
        

def instancetrial(sysargv, seed):
    
    numberslots = int(sysargv[4])
    generatedframe = 0
    successfullytransmitted = 0
    throughput = 0
    totaldelay = 0
    #generation till succesffuly submitted
    
    Allslots = []
    #make slots to be available (initialize nothing in them)
    for iterslot in range(0, int(sysargv[4])+1):
        emptyslot = []
        Allslots.append(list(emptyslot))
    
    
        
    #iterate through each slots    
    for iterslot in range(1,int(sysargv[4])+1):
        nodesinslot = []
        
        #within each slot we generate frame for each slot
        for iternode in range(1,int(sysargv[2])+1):
            #print("generate stuff")
            boolgenerate = generateframe.generateframe(sysargv[3],seed)
            
            if (boolgenerate==True):
                #print("if pass append to nodeinslot")                
                nodesinslot.append(iternode)
                #print("count number of generated")
                generatedframe = generatedframe + 1
                
            
            #check if we have a collision: collision if more that one frame in a slot
        if (len(nodesinslot) > 1):
            #print(collision)
            
            for collidednodeiter in nodesinslot:
                #print("find a new spot for each collided part")
                slotnumber, createdframes, delay = findaspot(collidednodeiter, iterslot, int(sysargv[4]), allslots)
                Allslots[slotnumber].append(collidednodeiter)
                generatedframe = generatedframe + createdframes
                totaldelay = totaldelay + delay
                successfullytransmitted = successfullytransmitted + 1
                
                #print("if its already in that spot try again")
                
        elif(len(nodesinslot)==1):
            #successfully transmitted in 1 slot
            successfullytransmitted = successfullytransmitted + 1
            totaldelay = totaldelay+1
            #count success 
        
        else:
            continue
        
            
    delayinstance = totaldelay/successfullytransmitted
    throughputinstance = successfullytransmitted/numberslots
    return delay_instance, thoroughput_instance, seed
            
        
            
        
    