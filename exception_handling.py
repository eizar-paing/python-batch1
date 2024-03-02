try:
  age = 0
  if age <= 0:
    raise Exception("No age below zero")
except:
  print("No age below zero")
else:
  print("Nothing went wrong")
finally:
  print("Exception handling is finished")