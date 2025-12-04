# Question 2:
# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their swim lane position in the list.

# Assume that the first item in the list is swim lane position 1.
#####################################################
swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
              30.4, 32.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]
# Answer for Question 2 here
fastest_time = swim_times[0]
slowest_time = swim_times[0]

for i in range(len(swim_times)):
    if swim_times[i] < fastest_time:
        fastest_time = swim_times[i]
        fastest_lane = i + 1
    if swim_times[i] > slowest_time:
        slowest_time = swim_times[i]
        slowest_lane = i + 1
print(f"The fastest time is {fastest_time} at lane {fastest_lane}")
print(f"The slowest time is {slowest_time} at lane {slowest_lane}")

