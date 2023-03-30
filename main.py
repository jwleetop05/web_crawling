a = 1 # int
b = "1"
c = 1.0
d = [1,2,3]
e = [{"key":"value"}]
#print(type(a),type(b),type(c),type(d),type(e))

# for i in range(1,11):
#    print(i)


for i in e:
    print(i['key'])

def print_hi():
    print("재원이 성이 뭐였지?")

print_hi()
