# 
# This module will control the application for Will's Summer Service
# @author Arthur Zuliani
# @since 20211014
# First try using OO programming in Python

from job import Job

print("---------------------------------\r\n- Welcome to Will's Summer Services\r\n---------------------------------")
print("")

job1 = Job()
job1.getInformation()
job1.calculations()
print(job1.toString())

