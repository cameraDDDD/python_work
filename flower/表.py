
import pyecharts
from pyecharts.charts import Bar
bar=Bar()
bar.add_yaxis("胡凯闻",[105,128,106,76,82,79])
#pyecharts.charts.basic_charts.bar.Bar object at 0x0000010D05B163F0>
bar.add_xaxis(["语文","英语","数学","物理","生物","化学"])
#<pyecharts.charts.basic_charts.bar.Bar object at 0x0000010D05B163F0>
print(repr(bar))#oh no
#<bound method Base.render of <pyecharts.charts.basic_charts.bar.Bar object at 0x0000010D05B163F0>>
