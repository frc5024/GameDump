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

event_template = {
	"type":"",
	"timestamp":0,
	"name":"",
	"data":[]
}

output_template = {
	"match":{
		"name":"",
		"type":"",
		"legnth":0,
		"GSM":"",
		"control_word":""
	},
	"events":[
		
		],
	"alliance":"",
	"station":""
}

