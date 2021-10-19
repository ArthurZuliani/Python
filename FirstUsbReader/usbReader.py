# 
# This module is the first attempt to read information from sub and write it to a *.txt file
# @author Arthur Zuliani
# @since 20211018
#
import serial
from serial import Serial

# Path for the file that will be created/edited
writepath = 'P:\Python\FirstUsbReader\dataLogger.txt'

file_handler = open(writepath,'w')

serial1 = serial.Serial('COM3',9600)

readings_times = 0
file_handler.write('Datalogger test of serial transmission\r\n')

# Loop to control the amount of reading
while (readings_times < 10):
    data = serial1.readline(42)
    print(data)

    file_handler.write(str(data))   # Convert the data to string format and then write to the file
    readings_times += 1

# Close operation to save system resources    
file_handler.close()
