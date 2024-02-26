import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y)
print(y["name"])
print(y["age"])
print(y["city"])

x_json_val = { 
  "name":"John", 
  "age":30, 
  "city":"New York"
  }

y_json_string = json.dumps(x_json_val)
print(y_json_string)
print(type(y_json_string))

json_sample = {
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
}

batters = json_sample["batters"]
print(batters)
batter = batters["batter"]

print(batter)
# first_obj = batter[0]
# print(first_obj)
# print(first_obj["id"])
# print(first_obj["type"])

# [
# 					{ "id": "1001", "type": "Regular" },
# 					{ "id": "1002", "type": "Chocolate" },
# 					{ "id": "1003", "type": "Blueberry" },
# 					{ "id": "1004", "type": "Devil's Food" }
# 				]
for item in batter:
  print(item["id"] + ", " + item["type"]) # {'id': '1001', 'type': 'Regular'}



