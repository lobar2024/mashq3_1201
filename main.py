# 29. JSON BILAN ISHLASH (eng sodda)
import json

data = {"Ali":90, "Vali":85}

# saqlash
with open("students.json", "w") as f:
    json.dump(data, f)

# o‘qish
with open("students.json") as f:
    d = json.load(f)

print(d)
