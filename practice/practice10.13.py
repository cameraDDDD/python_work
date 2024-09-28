from pathlib import Path
import json
path=Path("dick.json")
dick={}
dick['name']=input("Your name:")
dick["sex"]=input("Your sex:")
dick["birth"]=input("Your birthday:")
d=json.dumps(dick)
path.write_text(d)
b=path.read_text()
print(b)

