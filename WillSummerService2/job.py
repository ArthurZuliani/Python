# 
# This class will be used in Will's Summer Service application
# @author Arthur Zuliani
# @since 20211014
# First try using OO programming in Python

class Job:
    
    client_name = "none"
    length_of_lawn = 0
    width_of_lawn = 0
    number_of_vehicles = 0

    square_meters = 0
    cost_of_grassCutting = 0.0
    cost_for_washing = 0.0
    total_cost = 0.0

    def __init__(self) -> None:
        pass

    def getInformation(self):    
        global client_name
        global length_of_lawn
        global width_of_lawn
        global number_of_vehicles 

        client_name = input("Client's name?\r\n")
        length_of_lawn = int(input("What is the length of the lawn(meters)?\r\n"))
        width_of_lawn = int(input("What is the width of the lawn(meters)?\r\n"))
        number_of_vehicles = int(input("How many vehicles to wash?\r\n"))
        print("---------------------------------")

    def calculations(self):
        global square_meters
        global cost_of_grassCutting
        global cost_for_washing
        global total_cost

        square_meters = length_of_lawn * width_of_lawn
        cost_of_grassCutting = square_meters * 0.016
        cost_for_washing = number_of_vehicles * 20
        total_cost = cost_for_washing + cost_of_grassCutting
        return total_cost

    def toString(self):
        output_string = "- Summary for " + client_name + "\r\n- Size of lawn: " + str(square_meters) + " square meters" + \
                        "\r\n- Cost for grass cutting: $" + str(cost_of_grassCutting) + "\r\n- Vehicles to wash: " + str(number_of_vehicles) + \
                        "\r\n- Cost for washing: $" + str(cost_for_washing) + "\r\n- Total cost: $" + str(total_cost) + \
                        "\r\n---------------------------------"
        return output_string

   # def display():
   #     print(toString())

