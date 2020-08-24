#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from calc2.electricity.short_test import ShortTest

def main():
    # 試験条件
    TARGET_CURRENT = 2500  # 目標電流値[A]
    TARGET_VOLTAGE = 40  # 目標電圧値[V]
    TEST_RESISTANCE = 0  # 試験体の抵抗[mΩ]
    OTHER_RESISTANCE = 0  # その他の抵抗値（端子台など）
    LINE_RESISTANCE = 5  # 配線抵抗[mΩ]
    POWER_MODULE_RESISTANCE = 3  # 電源1つ(1直1並)あたりの内部抵抗[mΩ]
    POWER_MODULE_NUM = 4  # 電源の最大個数
    POWER_MODULE_MIN_VOLTAGE = 10.4  # 電源1つ(1直1並)あたりの最小電圧[V]
    POWER_MODULE_MAX_VOLTAGE = 21.6  # 電源1つ(1直1並)あたりの最大電圧[V]
    # 外部短絡装置の可変抵抗組み合わせパターン(昇順に並べる)
    EXTERNAL_RESISTANCES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 計算結果の保存先パス
    PATH = "C:/github/libs/python/calc2/examples/short_test/"
    ROUND_NUM = 2  # 小数点の桁数
    st = ShortTest()

    # 一覧表を作成・保存
    st.make_table(power_module_num=POWER_MODULE_NUM,
                  power_module_resistance=POWER_MODULE_RESISTANCE,
                  test_resistance=TEST_RESISTANCE + OTHER_RESISTANCE,
                  external_resistances=EXTERNAL_RESISTANCES,
                  line_resistance=LINE_RESISTANCE,
                  power_module_max_voltage=POWER_MODULE_MAX_VOLTAGE,
                  power_module_min_voltage=POWER_MODULE_MIN_VOLTAGE)

    # 試験条件を満たす電源・外部短絡抵抗の組合せを探索
    search_result = st.search_pattern(
        TARGET_CURRENT,  TARGET_VOLTAGE, round_num=ROUND_NUM)
    if search_result == -1:
        print("試験条件を満たす構成は存在しません。")

    else:
        print("試験条件を満たす構成は存在したので記録します")
        # 結果保存
        st.save_excel(PATH)

    # I-V領域グラフをプロット
    st.save_graph(save_file_path=PATH + "graph.png",
                  #x_lim=(0, 20000, 1000),
                  #y_lim=(0, 1000, 100),
                  fig_size_x=30,
                  fig_size_y=15,
                  lim_font_size=30,
                  loc=1,
                  bbox_to_anchor=(1.05, 1),
                  borderaxespad=0)


if __name__ == "__main__":
    main()

"""
----------------------------------------
●Error between the target current or voltage and the theoretical current is minimum     
                  Min current error Min voltage error
Pattern                   2s1p-ext5         2s1p-ext5
Min current[A]                 1300              1300
Max current[A]                 2700              2700
Min voltage[V]                 43.2              43.2
Max voltage[V]                 20.8              20.8
Current[A](40V)                2500              2500
Voltage[V](2500A)                40                40
Current error                     0                 0
Voltage error                     0                 0
----------------------------------------
●List of pattern match test conditions
               Pattern  Min current[A]  ...  Current error  Voltage error
2s1p-ext1    2s1p-ext1         1733.33  ...         833.33           10.0
2s1p-ext2    2s1p-ext2         1600.00  ...         576.92            7.5
2s1p-ext3    2s1p-ext3         1485.71  ...         357.14            5.0
2s1p-ext4    2s1p-ext4         1386.67  ...         166.67            2.5
2s1p-ext5    2s1p-ext5         1300.00  ...           0.00            0.0
2s1p-ext6    2s1p-ext6         1223.53  ...         147.06            2.5
2s2p-ext1    2s2p-ext1         2311.11  ...        1944.44           17.5
2s2p-ext2    2s2p-ext2         2080.00  ...        1500.00           15.0
2s2p-ext3    2s2p-ext3         1890.91  ...        1136.36           12.5
2s2p-ext4    2s2p-ext4         1733.33  ...         833.33           10.0
2s2p-ext5    2s2p-ext5         1600.00  ...         576.92            7.5
2s2p-ext6    2s2p-ext6         1485.71  ...         357.14            5.0
2s2p-ext7    2s2p-ext7         1386.67  ...         166.67            2.5
2s2p-ext8    2s2p-ext8         1300.00  ...           0.00            0.0
2s2p-ext9    2s2p-ext9         1223.53  ...         147.06            2.5
3s1p-ext1    3s1p-ext1         2080.00  ...         166.67            2.5
3s1p-ext2    3s1p-ext2         1950.00  ...           0.00            0.0
3s1p-ext3    3s1p-ext3         1835.29  ...         147.06            2.5
3s1p-ext4    3s1p-ext4         1733.33  ...         277.78            5.0
3s1p-ext5    3s1p-ext5         1642.11  ...         394.74            7.5
3s1p-ext6    3s1p-ext6         1560.00  ...         500.00           10.0
3s1p-ext7    3s1p-ext7         1485.71  ...         595.24           12.5
3s1p-ext8    3s1p-ext8         1418.18  ...         681.82           15.0
3s1p-ext9    3s1p-ext9         1356.52  ...         760.87           17.5
3s1p-ext10  3s1p-ext10         1300.00  ...         833.33           20.0

[25 rows x 9 columns]
試験条件を満たす構成は存在したので記録します
min_voltage_max_currents: Pattern
1s1p    1155.555556
1s2p    1386.666667
1s3p    1485.714286
1s4p    1540.740741
2s1p    1733.333333
2s2p    2311.111111
3s1p    2080.000000
4s1p    2311.111111
Name: min_current_ext1, dtype: float64
-----------
max_voltages_min_currents: Pattern
1s1p    1200.000000
1s2p    1309.090909
1s3p    1350.000000
1s4p    1371.428571
2s1p    2057.142857
2s2p    2400.000000
3s1p    2700.000000
4s1p    3200.000000
Name: max_current_ext10, dtype: float64
-----------
min_voltages_min_ccurrents: Pattern
1s1p     577.777778
1s2p     630.303030
1s3p     650.000000
1s4p     660.317460
2s1p     990.476190
2s2p    1155.555556
3s1p    1300.000000
4s1p    1540.740741
Name: min_current_ext10, dtype: float64
-----------
"""
