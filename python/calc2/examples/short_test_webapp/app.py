from flask import Flask, render_template, url_for, request, redirect, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import numpy as np
import pandas as pd
from calc2.electricity.short_test import ShortTest
from apps import index, short_test, short_test_ini

app = Flask(__name__)


# 分割先のコントローラー(Blueprint)を登録
app.register_blueprint(index.app)
app.register_blueprint(short_test.app)
app.register_blueprint(short_test_ini.app)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.debug = True  # デバッグモード有効化
    app.run(host="0.0.0.0", port=port)
