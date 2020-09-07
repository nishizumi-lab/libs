from flask import Flask, render_template, url_for, request, redirect, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import datetime
import os
import numpy as np
import pandas as pd
from calc2.electricity.short_test import ShortTest
import io
import base64
import configparser

# Blueprintオブジェクトを生成
app = Blueprint('short_test_ini', __name__)

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
@app.route('/short_test_ini', methods=['GET', 'POST'])
def short_test_ini():
    PAGE_TITLE = "外部短絡試験計算機 ver0.1.0"
    INPUT_NAME = 'file1'
    HTML_PATH = 'short_test_ini.html'
    if request.method == 'POST':
        message = "hello!"
        target_voltage = 0
        target_current = 0
        power_module_num = 0
        power_module_max_voltage = 0
        power_module_min_voltage = 0
        power_module_resistance = 0
        test_resistance = 0
        line_resistance = 0
        external_resistances = ['']

        if request.method == 'POST':
            filebuf = request.files[INPUT_NAME].read()
            int_texts = filebuf.decode('utf-8')
            config = configparser.ConfigParser()
            try:
                config.read_string(int_texts)
                message = "Loaded ini file"
                target_voltage = string_to_float(config.get('settings', 'target_voltage'))
                target_current = string_to_float(config.get('settings', 'target_current'))
                power_module_num = string_to_int(
                    config.get('settings', 'power_module_num'))
                power_module_max_voltage = string_to_float(
                    config.get('settings', 'power_module_max_voltage'))
                power_module_min_voltage = string_to_float(
                    config.get('settings', 'power_module_min_voltage'))
                power_module_resistance = string_to_float(
                    config.get('settings', 'power_module_resistance'))
                test_resistance = string_to_float(
                    config.get('settings', 'test_resistance'))
                line_resistance = string_to_float(
                    config.get('settings', 'line_resistance'))
                external_resistances = config.get(
                    'settings', 'external_resistances').split(',')

            except:
                message = "not ini file"
                target_voltage = 0
                target_current = 0
                power_module_num = 0
                power_module_max_voltage = 0
                power_module_min_voltage = 0
                power_module_resistance = 0
                test_resistance = 0
                line_resistance = 0
                external_resistances = ['']

        #print("external_resistances:", external_resistances)
        if external_resistances == ['']:
            external_resistances = [0]
        else:
            external_resistances = list(map(int, external_resistances))

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
            return render_template(HTML_PATH,
                                   page_title = PAGE_TITLE,
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
                                   error_min_result_index=st.df_error_min_result.index.tolist(),)
        else:
            return render_template(HTML_PATH,
                                   page_title=PAGE_TITLE,
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
                                   error_min_result_index=0)
    else:
        # エラーなどでリダイレクトしたい場合
        return render_template(HTML_PATH,
                               page_title=PAGE_TITLE)
