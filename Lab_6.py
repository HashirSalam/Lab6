number_of_lines = 3
number_of_stations = 4  #Each line has 4 stations
 

#a = time_spent
#t = switch_time
#e = entry_time
#x = exit_time


def Assembly(time_spent, switch_time,entry_time,exit_time):

    T1 = [0,0,0,0] #4 stations 
    T2 = [0,0,0,0] #4 stations 
    T3 = [0,0,0,0] #4 stations 
  
    #Base Case 
    T1[0] = entry_time[0] + time_spent[0][0]  # time taken to leave first station istationn line 1
    T2[0] = entry_time[1] + time_spent[1][0]  #time taken to leave first  in line 2
    T3[0] = exit_time[2] + time_spent[2][0]  #time taken to leave first station in line 3
    
    #Fill tables T1[] and T2[] using the above given recursive relations
     
    for i in range(number_of_stations):
        T1[i] = min(T1[i] + time_spent[0][i],    T2[i] + switch_time[1][i] + time_spent[0][i] ,T3[i] + switch_time[2][i] + time_spent[0][i])  #Each Lane minimum time
        T2[i] = min(T2[i] + time_spent[1][i],    T1[i] + switch_time[0][i] + time_spent[1][i] ,T3[i] + switch_time[2][i] + time_spent[1][i])
        T3[i] = min(T3[i] + time_spent[2][i],    T1[i] + switch_time[0][i] + time_spent[2][i] ,T2[i] + switch_time[1][i] + time_spent[0][i] )

    #Consider exit times and retutn minimum
    return min(T1[number_of_stations-1] + exit_time[0], T2[number_of_stations-1] + exit_time[1],T3[number_of_stations-1] + exit_time[2])
    

# Creates a list containing 5 lists, each of 8 items, all set to 0
width, height = number_of_stations, number_of_lines 
time_spent = [[0 for x in range(width)] for y in range(height)] 
switch_time = [[0 for x in range(width)] for y in range(height)] 

#print time_spent
#print switch_time

time_spent = [[4, 5, 3, 2] ,[2, 10, 1, 4],[100,100,100 ,100]]
switch_time = [[0, 7, 4, 5],[0, 9, 2, 8], [100, 100 , 100 , 100]]

print "Time Spent" ,time_spent
print "Switch Time" ,switch_time

entry_time = [1, 12 ,5] #each value for each line
exit_time = [18, 7 ,6]   #each value for each line   
 
print "Shortest Time :" ,(Assembly(time_spent,switch_time,entry_time,exit_time));
 
