from flask import Flask, render_template, url_for, request, redirect, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import datetime
import os
import numpy as np
import pandas as pd
from calc2.electricity.short_test import ShortTest

# Blueprintオブジェクトを生成
app = Blueprint('short_test', __name__)

def string_to_float(string_value):
    string_value = string_value.replace('"', '')

    if string_value == "":
        float_value = 0
        
    else:
        float_value = float(string_value)

    return float_value


def string_to_int(string_value):
    string_value = string_value.replace('"', '')
    if string_value == "":
        int_value = 0
    else:
        int_value = int(string_value)

    return int_value


def delete_files(top):
  for root, dirs, files in os.walk(top, topdown=False):
      for name in files:
          os.remove(os.path.join(root, name))
      for name in dirs:
          os.rmdir(os.path.join(root, name))
  
  #os.rmdir(top) #トップディレクトリを残す場合はいらない


# short_testにアクセスされた場合の処理
@app.route('/short_test', methods=['GET', 'POST'])
def short_test():
    title = "いらっしゃい"
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得
        input_datas = request.form.getlist('input')
        target_voltage = string_to_float(input_datas[0])
        target_current = string_to_float(input_datas[1])
        power_module_num = string_to_int(input_datas[2])
        power_module_max_voltage = string_to_float(input_datas[3])
        power_module_min_voltage = string_to_float(input_datas[4])
        power_module_resistance = string_to_float(input_datas[5])
        test_resistance = string_to_float(input_datas[6])
        external_resistances = input_datas[7].split(',')
        print("external_resistances:", external_resistances)
        if external_resistances == ['']:
            external_resistances = [0]
        else:
            external_resistances = list(map(int, external_resistances))
        line_resistance = string_to_float(input_datas[8])

        st = ShortTest()
        # 一覧表を作成・保存
        st.make_table(power_module_num=power_module_num,
                      power_module_resistance=power_module_resistance,
                      test_resistance=test_resistance,
                      external_resistances=external_resistances,
                      line_resistance=line_resistance,
                      power_module_max_voltage=power_module_max_voltage,
                      power_module_min_voltage=power_module_min_voltage)

        # 試験条件を満たす電源・外部短絡抵抗の組合せを探索
        search_result = st.search_pattern(
            target_current, target_voltage, round_num=2)


        now = datetime.datetime.now()

        delete_files("static/images/")
        save_graph_path = "static/images/graph_" + \
            now.strftime('%Y%m%d_%H%M%S') + ".png"

        # I-V領域グラフをプロット
        st.save_graph(save_graph_path,
                  fig_size_x=30,
                  fig_size_y=15,
                  lim_font_size=30,
                  loc=1,
                  bbox_to_anchor=(1.05, 1),
                  borderaxespad=0)

        if search_result != -1:
            # nameとtitleをindex.htmlに変数展開
            return render_template('short_test.html',
                                   save_graph_path=save_graph_path,
                                   target_voltage=str(target_voltage),
                                   target_current=str(target_current),
                                   power_module_num=str(power_module_num),
                                   power_module_max_voltage=str(
                                       power_module_max_voltage),
                                   power_module_min_voltage=str(
                                       power_module_min_voltage),
                                   power_module_resistance=str(
                                       power_module_resistance),
                                   test_resistance=str(test_resistance),
                                   external_resistances=','.join(
                                       map(str, external_resistances)),
                                   line_resistance=str(line_resistance),
                                   search_result=search_result,
                                   result_columns=st.df_result.columns.tolist(),
                                   result_values=st.df_result.values.tolist(),
                                   error_min_result_columns=st.df_error_min_result.columns.tolist(),
                                   error_min_result_values=st.df_error_min_result.values.tolist(),
                                   error_min_result_index=st.df_error_min_result.index.tolist(),
                                   title=title)
        else:
            return render_template('short_test.html',
                                   save_graph_path=save_graph_path,
                                   target_voltage=str(target_voltage),
                                   target_current=str(target_current),
                                   power_module_num=str(power_module_num),
                                   power_module_max_voltage=str(
                                       power_module_max_voltage),
                                   power_module_min_voltage=str(
                                       power_module_min_voltage),
                                   power_module_resistance=str(
                                       power_module_resistance),
                                   test_resistance=str(test_resistance),
                                   external_resistances=','.join(
                                       map(str, external_resistances)),
                                   line_resistance=str(line_resistance),
                                   search_result=-1,
                                   result_columns=0,
                                   result_values=0,
                                   error_min_result_columns=0,
                                   error_min_result_values=0,
                                   error_min_result_index=0,
                                   title=title)
    else:
        # エラーなどでリダイレクトしたい場合
        return render_template('short_test.html',
                               title=title)
