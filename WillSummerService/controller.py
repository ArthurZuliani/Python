# 
# This module will control the application for Will's Summer Service
# @author Arthur Zuliani
# @since 20211014
#
COST_PER_SQUARE_METERS = 0.016
COST_PER_CAR_WASHED = 20

print("---------------------------------\r\n- Welcome to Will's Summer Services\r\n---------------------------------\r\n")
print("")

client_name = input("Client's name?\r\n")
length_of_lawn = int(input("What is the length of the lawn(meters)?\r\n"))
width_of_lawn = int(input("What is the width of the lawn(meters)?\r\n"))
number_of_vehicles = int(input("How many vehicles to wash?\r\n"))
print("---------------------------------")

square_meters = length_of_lawn * width_of_lawn
cost_of_grassCutting = square_meters * COST_PER_SQUARE_METERS
cost_for_washing = number_of_vehicles * COST_PER_CAR_WASHED
total_cost = cost_for_washing + cost_of_grassCutting

print("- Summary for " + client_name)
print("- Size of lawn: " + str(square_meters) + " square meters")
print("- Cost for grass cutting: $" + str(cost_of_grassCutting))
print("- Vehicles to wash: " + str(number_of_vehicles))
print("- Cost for washing: $" + str(cost_for_washing))
print("- Total cost: $" + str(total_cost))
print("---------------------------------")
