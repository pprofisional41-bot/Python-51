dtc = dict()
dtc["key"] = "value"
dtc["sex"] = True
dtc["salary"] = 10.5
print(dtc)
print(dtc["key"])

print(list(dtc.keys()))

print("_________________________________")
for key in dtc:
    print(f"{key} = {dtc[key]}")

print("_________________________________")

for key, value in dtc.items():
    print(f"{key} = {value}")
print("_________________________________")
print(list(dtc.values())[2][1])

