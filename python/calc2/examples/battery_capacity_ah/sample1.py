# -*- coding: uTf-8 -*-
from calc2.electricity.battery_test import BatteryTest
import pandas as pd

# インスタンス生成
battery = BatteryTest()

# 読み込むCSVファイルのパス
csv_path = "C:/github/libs/python/calc2/examples/datasets/capacity_measurement_kwh/battery_capacity_measurement.csv"

# 保存先のディレクトリパス
save_dir_path = "C:/github/libs/python/calc2/examples/result/battery_test/"

# 空のデータフレームを作成
df = pd.DataFrame({})

# CSVファイルのロードし、データフレームへ格納
df = pd.read_csv(csv_path, encoding="SHIFT-JIS", skiprows=0)

# 時刻の列データを取り出し
date = df.loc[:, "時刻"]
df["date"] = pd.to_datetime(date, format='%Y年%m月%d日%H時%M分%S秒')

# 経過時間[sec]を計算し、カラムに追加
df["time"] = time = df["date"] - df.loc[0, "date"]
df["time"] = df['time'].dt.total_seconds()

# 重複した経過時間があれば、重複行を削除
df = df[~df["time"].duplicated()]

# 経過時間をインデックスラベルに設定
df.set_index("time", inplace=True)

# ラベル名のリネーム
df = df.rename(columns={'電力': 'kw'})

# 蓄電池の容量測定（kwh単位）
param, dst, df = battery.capacity_measurement_kwh(
    time=df.index, kw=df["kw"], save_dir_path=save_dir_path, graph_time_unit="h")
