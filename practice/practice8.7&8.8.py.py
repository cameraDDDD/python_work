def make_album(x,y,z=None):
    dictx={'name':x,'singer':y,}
    if z:
        dictx['songs_num']=z
    return dictx
a=make_album('Help','The beatles')
b=make_album("pet sounds",'The beach boys')
c=make_album('now and than',"The beatles",2)
print('input p to esc')

while True:
    a=input("album's name:")
    if a=='p':
        break
    b=input("singer's name:")
    if b=='p':
        break
    print(make_album(a,b))