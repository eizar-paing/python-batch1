import re

township_list = ["Rangoon", "Mandalay", "Nay Pyi Taw","Kyaukse", "Hpa-An",
"Maungdaw",
"Taunggyi",
"Mahlaing",
"Mudon",
"Myebon",
"Pyay",
"Mogaung",
"Yenangyaung",
"Taungoo",
"Namhkam",
"Pyinmana",
"Sagaing",
"Hakha",
"Amarapura",
"Loikaw",
]

township_str = "Rangoon, Mandalay, Nay Pyi Taw, Kyaukse, Hpa-An, Maungdaw, Taunggyi, Magway, Myeik, Bago, Mawlamyine, Natogyi, Myitkyina, Pathein"


def searchTownship():
  search_character = input("Enter First letter: ")
  town_format = r"\b" + search_character + "\w+"

  result = re.findall(town_format, township_str)
  print(result)

searchTownship()