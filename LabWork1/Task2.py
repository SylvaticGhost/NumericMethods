import json

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Convert the 2D array to a JSON string
json_str = json.dumps(array)

print("JSON string representation of the array: ", json_str)