from networktables import NetworkTables
import sys
import requests
import time
import logging
import listeners as lstn
import file as file

logging.basicConfig(level=50)
if len(sys.argv) <2:
	team = "5024"
else:
	team = sys.argv[1]

# - match name
# - match type
# - match legnth
# - match events
# - match GSM
# - control word
# - alliance
# - station

# An event:
# any initalization
# Mode changes


# listen for fms
# Establish networktables connection
# Check if bot is publishing data
# start recording









## main ##

#listen for nt connection
print("Waiting for NetworkTables connection...")

# This should be a listener
# while True:
# 	requests.get('http://roborio-'+str(team)+'-frc.local')
# 	break

print("RoboRIO found. Connecting")
NetworkTables.initialize(server='roborio-'+str(team)+'-frc.local')

# FMS listener
print("Connecting to FMSinfo")
fms = NetworkTables.getTable("FMSInfo")
fms.addEntryListener(lstn.fmsListen)

# GameDump event listener
print("Connecting to GameDump")
gd =  NetworkTables.getTable("GameDump")
gd.addEntryListener(lstn.gdListen)


# Do something useless while listening
print("Fetching data")
try:
	while True:
		time.sleep(1)
except:
	print("\rSaving...")

file.write()