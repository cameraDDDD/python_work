import locale
locale.setlocale(locale.LC_COLLTE,'zh_CN.UTF')





writer=['村上春树','赫尔曼·黑塞','加缪']
writer=sorted(writer,key=locale.strxfrm)
print(writer)