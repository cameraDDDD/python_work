import re
phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d\d)')
mo=phoneNumRegex.search('My numjksjfkj is aD D559()(415)-5556-4242')
print(mo.group())