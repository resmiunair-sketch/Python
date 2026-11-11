d={"name":"sneha","age":23}
d["grade"]="A"
d["age"]=12
d.update({"place":"chennai","blood":"AB+"})
print(d.get("age"))
print(d.keys())
# # print(d.values())
# # print(d.items())

# # del d["age"]
# # age=d.pop("age")
# last_item=d.popitem()
# print(d)
# # print(d)
# d.clear()
for key,value in d.items():
 print(f"{key}-->{value}")
