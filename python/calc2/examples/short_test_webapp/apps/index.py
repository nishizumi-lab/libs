from flask import Flask, render_template, url_for, request, redirect, Blueprint
import os

# Blueprintオブジェクトを生成
app = Blueprint('index', __name__)

# index にアクセスされた場合の処理
@app.route('/', methods=['GET', 'POST'])
def index():
    HTML_PATH = 'index.html'
    PAGE_TITLE = "分析ツール集（試作中）"
    # messageとtitleをindex.htmlに変数展開
    return render_template(HTML_PATH,
    page_title=PAGE_TITLE,
    )
