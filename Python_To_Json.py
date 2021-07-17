import json
a={"name": "David",
     "class":"I",
     "age": 6  
 }
# file=open("hellow.json","w")
# json.dump(a,file,indent=4)
# d=json.dumps(file)
# print(d)
# file.close()
file=open("shu.json","w")
json.dump(a,file,indent=4)
d=json.dumps(file)
print(d)
file.close()
