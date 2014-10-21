'''
This simulation takes in 5 parameters: protocol, N, p, R, T (and seeds)
First is protocol name, N is number of stations (20), p is frame generation probability for each node (<=0.04), R is total number of slots that need to be simulated (50000), T is number of trials (5)
'''
import random
#This function is to get frame generation, it takes in probability
# and if the random number is <= probability of frame generation, generate a frame (1)
# else, don't generate a frame (0)

def generate_frame(p):
    x = random.random()
    if x > p:
        return 0
    else:
        return 1 

#This function is to determine if a station can transmit or not after a collision
#If x generated is greater than 1/number of stations, then it isn't allowed to transmit

def transmit_frame(N):
    x=random.random()
    chance=1/N
    if x>chance:
        return 0
    else:
        return 1
    
def slotted_ALOHA_prob_backoff(stations,slots,probability,seed):
    frames_transmitted=0
    frames_generated=0
    
    backoff_stations=[]
    stations_allowed=[]
    
    total_delay=0
    frames_transmitted=0
    
    #Every station has its own frame queue (aka a list)
    
    stations_transmitting=[]
    frame_queues=[]
    frame_queues_delay=[]
    
    for i in range(stations):
        queue=[]
        frame_queues.append(queue)
        frame_queues_delay.append(queue)
        
    #Run this function as long as slots is 
    for length in range(1,slots+1):
        
        #If there were collisions in the previous slot, determine in this slot if the 
        #stations are allowed to transmit by probability 1/N
        #If allowed, add it to the stations transmitting list
        
        if len(backoff_stations)>=1:
            for station in backoff_stations:
                result= transmit_frame(stations)
                if result==1:
                    #stations_transmitting.append(station)
                    stations_allowed.append(station)
                else:
                    continue
        
        #If the station is allowed to transmit (by 1/N rule) remove it from the backoff stations list so it can transmit
        if len(stations_allowed)>0:
            for station in stations_allowed:
                backoff_stations.remove(station)
            stations_allowed=[]
            
        #Generate frames or not for stations depending on probability
        for j in range(stations):
            frame_generation= generate_frame(probability)
            # If a frame is generated, add it to the frame queue for the jth station and add 1 to its frame delay
            if frame_generation==1:
                frames_generated+=1
                frame_queues[j].append(1)
                frame_queues_delay[j].append(1)
        
        for station in range(stations):
            if (len(frame_queues[station])>=1 ) and (station not in backoff_stations):
                
                '''
                If the frame queue of a station is at least one and it isn't in 
                the backoff stations list, transmit the frame
                and append the station transmitting to the stations_transmitting list
                '''
                
                stations_transmitting.append(station)
         
         #If one station is transmitting, no collision, just transmit the frame
         #Pop the frame out of that station's frame queue and clear stations_transmitting list
        if (len(stations_transmitting)==1):
            frame_queues[stations_transmitting[0]].pop(0)
            
            #If the station that transmitted 
            '''
            if (len(backoff_stations>=1)):
                backoff_stations.remove(stations_transmitting[0])
            '''
            #Reset the stations transmitting list
            frames_transmitted+=1
            total_delay+=frame_queues_delay[stations_transmitting[0]].pop(0)
            stations_transmitting=[]
        
        #If more than one station is transmitting, there is gonna be a collision
        #Add the station to the backoff_stations list and don't pop the frames out
        else:
            for station in stations_transmitting:
                if station not in backoff_stations:
                    backoff_stations.append(station)
            #Reset the stations transmitting list
            stations_transmitting=[]
            
            #Additional code here
            
            count=0
            while count<stations:
                delay_queue= frame_queues_delay[count]
                for i in range(len(delay_queue)):
                    delay_queue[i]=delay_queue[i]+1
                frame_queues_delay[count]=delay_queue
                count+=1            
    
    
    average_delay= total_delay/frames_transmitted 
    throughput=frames_transmitted/slots
    #return throughput, average_delay,frames_transmitted,total_delay
    return average_delay,throughput,seed
    

'''
num_stations=20
num_slots=50000
num_prob=0.05

throughput,delay,transmissions,total_delay= slotted_ALOHA_prob_backoff(num_stations,num_slots,num_prob)
print(throughput)
print(delay)
print(transmissions)
print(total_delay)
'''