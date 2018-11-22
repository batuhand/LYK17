import json
with open("jsonDeneme.json") as dosya:

    a = json.loads(dosya.read())
    print(a)
