"""
t90.py - 本示例程序演示如何用程序在天勤的行情图上绘图
"""

import numpy as np
from tqsdk import TqApi

api = TqApi()

# 获取 cu1905 和 cu1906 的日线数据
klines = api.get_kline_serial("SHFE.cu1905", 86400)
klines2 = api.get_kline_serial("SHFE.cu1906", 86400)

df = klines.to_dataframe()
df2 = klines2.to_dataframe()

# 算出 cu1906 - cu1905 的价差，并以折线型态显示在副图
dif = df2["close"] - df["close"]
klines.draw_serial(dif, id="dif", board="DIF", color=0xFF00FF00, width=3)

# 在附图画出 cu1906 的K线
klines.draw_kserial(df2, id="cu1906", board="B2")

# 给主图最后5根K线加一个方框
last_id = klines.last_id()
klines.draw_box(x1=-5, y1=klines[-5]["close"], x2=-1, y2=klines[-1]["close"], width=1, color=0xFF0000FF, bg_color=0x8000FF00)

# 在主图最近K线的最低处标一个"最低"文字
indic = np.where(df["low"] == df["low"].min())[0]
value = df["low"].min()
klines.draw_text("测试413423", x=indic, y=value, color=0xFF00FF00)

api.close()
