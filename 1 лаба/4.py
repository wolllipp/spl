my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
arr = sorted (my_dict, key=my_dict.get) [:3]
print(arr)