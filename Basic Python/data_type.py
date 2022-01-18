# 1. None (Python using None)

# 2. Numberic (int, float, complex, bool)
num = 2
print(type(num))
num = 2.5
print(type(num))
a = 2.5
b = int(a)
print(b)
k = float(b)
print(k)
k = 7
#   complex
c = complex(b, k)
print(c)
num = 6 + 9j
print(type(num))
#   bool
bool = b < k
print(bool)
print(int(bool))
print(int(b > k))


# List, Tuple, Set, String, Range,


ls = [34, 56, 67, 89]
print(type(ls))
s = {34, 56, 67, 89}
print(type(s))
t = (5, 6, 8, 0)
print(type(t))
str = "kay"
print(type(str))
ranges = range(10)
print(ranges)
lsRange = list(ranges)
print(lsRange)
event_number = list(range(2,10,2))
print(event_number)

# Dictionary
dic = {'a':'Hil','b':'Hook','c':'Hellow'}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.get('a'))
