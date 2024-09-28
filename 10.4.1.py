from pathlib import Path
import json

"""numbers=[2,3,5,7,9,88,444,666]
path=Path('numbers.json')
contents=json.dumps(numbers)
path.write_text(contents)"""



path=Path('numbers.json')
content=path.read_text()
print(type(content))
num=json.loads(content)
print(type(num))
