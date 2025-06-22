import os
import datetime

command= "uptime" #load avg
command="Date"  #date



def run_command(command):
    return os.system(command)

run_command("date") #calling a function
    

def show_date():
    return datetime.datetime.today()



