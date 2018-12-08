import templates as templates
import time

# Create a blank output file
output = templates.output

def addEvent(name, data=0):
	output["events"].append({"name":name, "timestamp":str(time.time()), "packet":data})

def addGSM(message):
	output["match"]["GSM"].append({"message":str(message), "timestamp":str(time.time())})

def addReplay(number):
	output["match"]["replay"].append({"number":number, "timestamp":str(time.time())})

def addAlliance(alliance):
	output["match"]["alliance"].append({"alliance":alliance, "timestamp":str(time.time())})

def setName(name):
	output["match"]["event_name"] = name

def addStation(station):
	output["match"]["station"].append({"station":station, "timestamp":str(time.time())})

def add(data,name):
	output["match"][name].append({name:data, "timestamp":str(time.time())})

def write():
	with open("./output/"+str(time.time()) +".gamedump.json", "w") as f:
		f.writelines(str(output).replace("'", '"'))
		f.close()