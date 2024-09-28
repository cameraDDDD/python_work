from pathlib import Path
import json
a=input("What's your favorite number:")
b=Path("favorite_num.json")
c=json.dumps(a)
b.write_text(c)
