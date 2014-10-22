'''
This simulation takes in 5 parameters: protocol, N, p, R, T (and seeds)
First is protocol name, N is number of stations (20), p is frame generation probability for each node (<=0.04), R is total number of slots that need to be simulated (50000), T is number of trials (5)
'''
import random

'''
#This function is to get frame generation, it takes in probability
and if the random number is <= probability of frame generation, generate a frame (1)
else, don't generate a frame (0)
'''

def generate_frame(p):
    x = random.random()
    if x > p:
        return 0
    else:
        return 1 

def time_division_multiplexing(stations,slots,probability,seed):
    delay_time=0
    frames_transmitted=0
    total_delay=0
    frames_generated=0
    
    '''
    Transmission occurs in cycles of N(meaning stations) 
    Every station has its own frame queue (aka a list) and frame delay queue
    Must also record data for each station/node (throughput, average delay for frames of the node)
    
    Important: READ BELOW
    First value in each node list is: Frames generated, frames transmitted, then total frame delays
    '''
    
    frame_queues=[]
    frame_queues_delay=[]
    node_data=[]
    
    for i in range(stations):
        queue=[]
        frame_queues.append(queue)
        frame_queues_delay.append(queue)
    cycle_index=stations
    cycle_number=0
    
    for i in range(stations):
        node=[0,0,0,0]
        node_data.append(node)
    
    
    #Run this function as long as you need to (the slot time) 
    for length in range(1,slots+1):
        
        if length>cycle_index:
            cycle_number+=1
            cycle_index=cycle_index+stations
            
        #Generate frames for stations
        for j in range(stations):
            frame_generation= generate_frame(probability)
            
            # If a frame is generated, add it to the frame queue for the jth station and add 1 to its frame delay
            if frame_generation==1:
                frames_generated+=1
                #Add to the station data list
                node_data[j][0]+=1
                
                frame_queues[j].append(1)
                frame_queues_delay[j].append(1)
        
        #Check if a station has frames to transmit
        for station in range(stations):
            if (len(frame_queues[station])==0):
                continue
            
         
#If the frame queue of a station isn't empty, check to see
#if you can transmit the frame or not
#according to this rule:
#A station i is only allowed to transmit in a slot with number mN + i where m = 0, 1, 2, ... is the cycle number
  
            else:
                #if station has something to transmit: its queue isnt empty
                #get the slot that the station is allowed to transmit in, use 1+station since station has 
                #range of 0, stations-1 
                slot_allowed=(cycle_number*stations)+ (1+station)
                
                if (length==slot_allowed):
                    frame_queues[station].pop(0)
                    delay_to_add=frame_queues_delay[station].pop(0)
                    total_delay+=delay_to_add
                    frames_transmitted+=1
                    
                    node_data[station][1]+=1
                    node_data[station][2]+= delay_to_add
                    
                    '''
                    count=0
                    #With this data becomes more skewed 
                    #if station queue isn't empty, increment delay for all frames in its queue
                    
                    while count<stations:
                        delay_queue= frame_queues_delay[count]
                        for i in range(len(delay_queue)):
                            delay_queue[i]=delay_queue[i]+1
                        #frame_queues_delay[count]=delay_queue[i]
                        frame_queues_delay[count]=delay_queue
                        
                        #node_data[count][2]+=sum(delay_queue)
                        
                        count+=1                    
                
                '''
      
                '''
                else:
                    #if the station can't transmit and its queue isn't empty, increase delay for all frames in queue
                    count=0
                    while count<stations:
                        delay_queue= frame_queues_delay[count]
                        for i in range(len(delay_queue)):
                            delay_queue[i]=delay_queue[i]+1
                        #frame_queues_delay[count]=delay_queue[i]
                        frame_queues_delay[count]=delay_queue
                        
                        #node_data[count][2]+=sum(delay_queue)
                        
                        count+=1
                '''
        #Increment the delay for all frames in a stations frame queue after checking if they can transmit or not
        count=0
        while count<stations:
            delay_queue= frame_queues_delay[count]
            for i in range(len(delay_queue)):
                delay_queue[i]=delay_queue[i]+1
            frame_queues_delay[count]=delay_queue       
            count+=1  
            
    average_delay= total_delay/frames_transmitted 
    throughput=frames_transmitted/slots
    '''
    #Calculate station data
    station_stats=[]
    for i in range(station):
        node=[]
        station_stats.append(node)
        
    for i in range(station):
        station_stats[i].append(node_data[i][0])   #Get total frames generated
        station_stats[i].append(node_data[i][1])   #Get total frames transmitted
        station_stats[i].append(node_data[i][2])   #Get total delay for successful frames of the station
      '''  
    return average_delay,throughput,seed


'''
num_stations=20
num_slots=50000
num_prob=0.04


throughput,delay,frame_trans,total_delay= time_division_multiplexing(num_stations,num_slots,num_prob)
print(throughput)
print(delay)
print(frame_trans)
print(total_delay)
'''
        

        