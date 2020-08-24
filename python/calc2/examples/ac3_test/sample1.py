#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from calc2.electricity.short_test import ShortTest

st = ShortTest()

# 試験条件
I_target = 200  # 目標電流値[A]
E_target = 50  # 目標電圧値[V]
R_test = 0  # 試験体の抵抗[mΩ]
R_other = 0  # その他の抵抗値（端子台など）

# 計算結果の保存先パス
path = "C:/prog/python/pandas"

# 配線抵抗[mΩ]
R_line = 5

# 電源のパラメータ
Rm = 5  # 電源1つ(1直1並)あたりの内部抵抗[mΩ]
power_num = 4  # 電源の最大個数
E1_min = 20.0  # 電源1つ(1直1並)あたりの最小電圧[V]
E1_max = 30.0  # 電源1つ(1直1並)あたりの最大電圧[V]

# 外部短絡装置の可変抵抗組み合わせパターン(昇順に並べる)
R_exts = [100, 200]

# 一覧表を作成・保存
st.make_table(power_num, Rm, R_test + R_other, R_exts, R_line, E1_max, E1_min)

# 試験条件を満たす電源・外部短絡抵抗の組合せを探索
st.search_pattern(I_target, E_target)

# 結果表示
st.show_result()


"""
----------------------------------------
●List of pattern match test conditions
              Imin   Imax  Emin  Emax  I[A](50V)  E[V](200A)  Ierror  Eerror
Pattern
2s1p-ext200 186.05 279.07 60.00 40.00     232.56       43.00   32.56    7.00
2s2p-ext200 190.48 285.71 60.00 40.00     238.10       42.00   38.10    8.00
↑試験条件を満たす装置構成一覧。「電源が2S1P、外部短絡抵抗値が200mΩ」もしくは「電源が2S2P、外部短絡抵抗値が200mΩ」の2通りとなります。
----------------------------------------
●Error between the target current and the theoretical current is minimum
Imin         186.05
Imax         279.07
Emin          60.00
Emax          40.00
I[A](50V)    232.56
E[V](200A)    43.00
Ierror        32.56
Eerror         7.00
Name: 2s1p-ext200, dtype: float64
↑電源電圧を試験条件と一致させた場合、電源の出力電流が目標電流に最も近いときの装置構成は、「電源が2S1Pで外部短絡抵抗が200mΩ」だとわかります。
----------------------------------------
●Error between the target voltage and the theoretical voltage is minimum
Imin         186.05
Imax         279.07
Emin          60.00
Emax          40.00
I[A](50V)    232.56
E[V](200A)    43.00
Ierror        32.56
Eerror         7.00
Name: 2s1p-ext200, dtype: float64
↑電源の出力電流を試験条件と一致させた場合、電源電圧が目標電圧に最も近いときの装置構成は、「電源が2S1Pで外部短絡抵抗が200mΩ」だとわかります。
"""
