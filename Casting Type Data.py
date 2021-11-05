#Casting Type Data

'''
Text Type       : str
Numeric Type    : int, float, complex
Sequence Type   : list, tuple, range
Mapping Type    : dict
Set Type        : set, frozenset
Boolean Type    : bool
Binary Type     : bytes, bytearray, memoryview
'''

str_data = "11"
print("data :", str_data)
print("-bertipe :", type(str_data))

int_data = 11
print("data :", int_data)
print("-bertipe :", type(int_data))

float_data = 11.1
print("data :", float_data)
print("-bertipe :", type(float_data))

complex_data = 23+1j
print("data :", complex_data)
print("-bertipe :", type(complex_data))

list_data = ["apple", "banana", "cherry"]
print("data :", list_data)
print("-bertipe :", type(list_data))

tuple_data = ("apple", "banana", "cherry")
print("data :", tuple_data)
print("-bertipe :", type(tuple_data))

range_data = range(10)
print("data :", range_data)
print("-bertipe :", type(range_data))

dict_data = {"name" : "Banana", "Age :":17}
print("data :", dict_data)
print("-bertipe :", type(dict_data))

set_data = {"name","age","gender"}
print("data :", set_data)
print("-bertipe :", type(set_data))

frozenset_data = ({"name","age","gender"})
print("data :", frozenset_data)
print("-bertipe :", type(frozenset_data))

bool_data1 = True
print("data :", bool_data1)
print("-bertipe :", type(bool_data1))

bool_data2 = False
print("data :", bool_data2)
print("-bertipe :", type(bool_data2))