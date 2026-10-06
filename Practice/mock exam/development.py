weather_data = [
    [30.0, 8.0, "No Rain"],
    [29.0, 12.0, "No Rain"],
    [27.0, 18.0, "Rain"],
    [25.0, 22.0, "Rain"],
    [32.0, 6.0, "No Rain"],
    [26.0, 16.0, "Rain"],
    [31.0, 10.0, "No Rain"],
    [28.0, 20.0, "Rain"]
]
def calculate_distance(temperature1,wind_speed1,temperature2,wind_speed2):    #Defining function
    distance = (((temperature1 - temperature2)**2)+ ((wind_speed1-wind_speed2)**2)) ** 0.5   #Uses euclidean distance formula to calculate distance between two points
    return distance  #Returns euclidean distance as output
def find_nearest(distance_list):   #Defining function 
    smallest_distance =  distance_list[0]
    smallest_index = 0
    for distance in distance_list:     #Loops through every distance in the distance
        if distance < smallest_distance:   #Checks for the smallest distance in list
            smallest_distance = distance_list    #Brings smaller distance as the one to compare
            smallest_index = distance_list.index(distance)    #Takes the index of the current smallest distance
    return smallest_index   #Returns the index of the smallest distance

def predict_rain(current_temperature,current_wind_speed, weather_data):    #Defining function
    distance_list = []   #Stores all euclidean distances in a list for later comparison
    for data in weather_data:  #Loops through every data set in the weather data
        comp_temp = data[0]   #Takes temperature for comparison
        comp_speed = data[1]   #Takes wind speed for comparison
        euclidean_distance = calculate_distance(current_temperature,current_wind_speed, comp_temp,comp_speed)   #Calls o=upon previous function to calculate euclidean distancex
        distance_list.append(euclidean_distance)  #Adds euclidean distance to the list
    smallest_index = find_nearest(distance_list)   #calls upon previous function to find index of the smallest distance
    nearest_data_set = weather_data[smallest_index]    #Uses smallest index to find the closest data set
    prediction = nearest_data_set[2]   #Takes the prediction of the nearest neighbour
    return prediction   #Returns prediction
prediction_records = []
while True:   #loops until broken
    prediction_str = ""
    current_temperature = float(input("What is the current temperaure?: "))
    current_speed = float(input("What is the current wind speed?: "))
    prediction = predict_rain(current_temperature,current_speed,weather_data)   #Uses user input to get prediction
    print(f"Prediction today will have {prediction}")   #Outputs the prediction in a suitable message
    prediction_str = f"{current_temperature},{current_speed},{prediction}"   #Links user temperature, wind speed and prediction as a string
    prediction_records.append(prediction_str)   #Adds string to list
    user_repeat = input("Do you want another prediction?: (Y or N)").upper()  #Checks if user wants to do another prediction
    if user_repeat == "N":
        break   #Ends loop if user decides to stop
with open("weather_predictions.txt", "w") as file:   #opening a file
    for prediction in prediction_records:   #Outputs every prediction in the prediction list
        file.write(f"prediction\n")


