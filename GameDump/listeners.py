import fms as fms

def fmsListen(table, key, value, isNew):
	
	if key in fms.keys:
		fms.keysKeys[key](value)
	else:
		print(f"Unknown: {key}: {value}")

def gdListen(table, key, value, isNew):
	if key == "robot_mode":
		print("Robot Mode: "+ value)