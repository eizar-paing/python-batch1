def getNonNumeric_Value(dict_val):
  non_numeric_dict = {}
  for key, val in dict_val.items():
    if not isinstance(val, (int, float)):
      non_numeric_dict[key] = val
  return non_numeric_dict

my_dict = {"a": 1, "b": "Hello", "c": [1, 2, 3]}
result_dict = getNonNumeric_Value(my_dict)
print(result_dict)
