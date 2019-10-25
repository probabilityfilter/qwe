import sys

var_list = [3, 5, 7, "odd", True, 10.123]
var_tuple = (3, 5, 7, "odd", True, 10.123)
print(
    "List occupies",
    sys.getsizeof(var_list),
    ". Tuple occupies",
    sys.getsizeof(var_tuple),
)