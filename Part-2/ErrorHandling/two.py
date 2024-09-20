try:
    fp=open("one.txt",'r')
except:
    fp=open("data.txt",'r')

data = fp.read()
print(data)
print("GM")
print("GA")
print("GN")