import file as file

def ctlData(data):
	if str(data) == "893665.0":
		print("Robot Enabled")
		file.addEvent("Robot enabled",data)
	elif str(data) == "893664.0":
		print("Robot Disabled")
		file.addEvent("Robot disabled",data)
	elif str(data) == "893666.0":
		print("Auto mode")
		file.addEvent("Auto mode",data)
	elif str(data) == "893668.0":
		print("Test mode")
		file.addEvent("Test mode",data)
	else:
		print("FMS control data:"+ str(data))
		file.addEvent("Unknown packet", data)

def gsm(data):
	print(f"GSM sent from FMS: {data}")
	file.add(data, "GSM")

def replay(data):
	print(f"Match replay number: "+ str(data).split(".")[0])
	file.add(int(str(data).split(".")[0]), "replay")

def alliance(data):
	if str(data) == "True":
		print("Robot assigned to RED alliance")
		file.add("red", "alliance")
	else:
		print("Robot assigned to BLUE alliance")
		file.add("blue", "alliance")

def eventName(data):
	file.setName(data)

def station(data):
	file.add(int(str(data).split(".")[0]), "station")

def number(data):
	file.add(int(str(data).split(".")[0]), "number")

def matchType(data):
	file.add(data, "type")


# GameSpecificMessage
# FMSControlData
# enable 893665.0
# disable 893664.0

#auto 893666.0
#test 893668.0


keys = {
	"FMSControlData":ctlData,
	"GameSpecificMessage":gsm,
	"ReplayNumber":replay,
	"IsRedAlliance":alliance,
	"EventName":eventName,
	"StationNumber":station,
	"MatchNumber":number,
	"MatchType":matchType
}

# ctlData(893665.0)
# alliance("True")
# alliance("False")