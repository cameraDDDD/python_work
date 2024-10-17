import re
phoneNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')#相当于\d{3}-\d{3}-\d{3}
mm = phoneNum.findall("my phone number is 157-9778-9836 just like \n157-977-8983-6 or 181-790-8565-9")
#print(type(mo))

for i in mm:
    print("my phone number is not "+i )