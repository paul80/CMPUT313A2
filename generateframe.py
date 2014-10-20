def generateframe(probability,Seed):
    #random.seed(Seed)
    generated = random.random()
    
    if (generated<probability):
        return True
    else:
        return False

def delaycounter(firstslot,nextslot):
    return (nextslot - firstslot + 1)
