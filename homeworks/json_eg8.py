import json
json_sample = {
	"items":
		{
			"item":
				[
					{
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
					},

				]
		}
}

items = json_sample["items"]
item = items["item"]
all_item = item[0]
topping = all_item["topping"]
batters = all_item["batters"]
batter_list = batters["batter"]

for batter_item in batter_list:
	print(batter_item["id"] + " & " + batter_item["type"])

# print(topping)
# print(all_item)

# for i in item:
# 	topping_list = i["topping"]
# 	print(topping_list[0]["id"])

    
        
# json_4 = json_3["topping"]
# print(json_4)

# for i in json_4:
     
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True, separators=(".", "=")))