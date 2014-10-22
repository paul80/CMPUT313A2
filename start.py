import sys
import argparse
import statsandprint
import slottedalohaexponential
import generateframe
import time_division
import slottedALOHAprob
'''
This simulation takes in 5 parameters: protocol, N, p, R, T (and seeds)
First is protocol name, N is number of stations (20), p is frame generation probability for each node (<=0.04), R is total number of slots that need to be simulated (50000), T is number of trials (5)
'''

def main():
   
    #like this
    #start.py T 20 0.04 50000 5 seed1 seed2 seed3 seed4 seed5
    
    print("The program may take a while to be finished, please be patient")
    print ("enter Protocol N p R T seed1 seed2 ... SeedT respectively without commas separated by spaces +\n")
    print("The first item is the protocol name 'T, P, I, or B'")
    print("Second parameter is the number of stations \n")
    print("The third parameter is the frame generation probbability \n")
    print("The fourth parameter is the number of slots for each simulation \n")
    print("T is the number of trials +\n")
    print("Last input is T number of seeds")
    

    command_arguments=[]
    numarguments = len(sys.argv)  
        
    if ((numarguments==int(sys.argv[5])+ 6)):
        #print("shere")
        for arg in sys.argv:
            command_arguments.append(arg)                        

        #frame_counter_container=[]
        #successful_frame_container = []
        thoroughput_container=[]
        delay_container=[]
        seed_instance_container=[]
        #averageframecounter=[]
        

        for testinstance in range(0, int(sys.argv[5])):
            seed = int(sys.argv[4+testinstance+1])

            print("Loading,please be patient")
            if (sys.argv[1] == 'T'):
                delay_instance, thoroughput_instance, seed = time_division.time_division_multiplexing(int(sys.argv[2]),int(sys.argv[4]),float(sys.argv[3]),seed)
                
                #print("T")
                
            
            elif (sys.argv[1] == 'P'):
                delay_instance, thoroughput_instance, seed = slottedALOHAprob.slotted_ALOHA_prob_backoff(int(sys.argv[2]),int(sys.argv[4]),float(sys.argv[3]),seed)
                
                #print("P")
                

            elif (sys.argv[1] == 'I'):
                delay_instance, thoroughput_instance, seed = slottedintervalbased.instancetrial(sys.argv, seed)

            elif (sys.argv[1] == 'B'):
                delay_instance, thoroughput_instance, seed = slottedalohaexponential.instancetrial(sys.argv, seed)
                
            
            else:
                print("Something went wrong")
                return
            #averageframecounter.append(averageframes)
            delay_container.append(delay_instance)            
            thoroughput_container.append(thoroughput_instance)
            seed_instance_container.append(seed)

        statsandprint.getandprintstats(delay_container, thoroughput_container, seed_instance_container, sys.argv[1:])
        
        #stats.getandprintstats(averageframecounter, thoroughput_container, seed_instance_container, sys.argv[1:])
        



if __name__ == "__main__":
    main()