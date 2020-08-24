# -*- coding: uTf-8 -*-
from util2.file.searcher import FileSearcher

fsearch = FileSearcher()

# 検索対象のパス
LOAD_DIR_PATH = "./examples/file/sample_data"

# 検索結果の出力先
SAVE_FILE_PATH = "./examples/file/sample_data/result.csv"

# 検索対象内の全てのファイル・フォルダパスを取得
paths = fsearch.get_paths(LOAD_DIR_PATH)

for path in paths["file_abs_path"]:
    if path[-7:-4] == "001":
        print("ID:001")
        print("Date:", path[-12:-8])
        print("Path:", path)

for path in paths["file_abs_path"]:
    if path[-7:-4] == "002":
        print("ID:002")
        print("Date:", path[-12:-8])
        print("Path:", path)
"""
ID:001
Date: 1904
Path: C:/github/libs/python/filedit/examples/data\DATA_1904_001.txt
ID:001
Date: 1905
Path: C:/github/libs/python/filedit/examples/data\DATA_1905_001.txt
ID:001
Date: 1906
Path: C:/github/libs/python/filedit/examples/data\DATA_1906_001.txt
"""

"""
ID:002
Date: 1904
Path: C:/github/libs/python/filedit/examples/data\DATA_1904_002.txt
ID:002
Date: 1905
Path: C:/github/libs/python/filedit/examples/data\DATA_1905_002.txt
ID:002
Date: 1906
Path: C:/github/libs/python/filedit/examples/data\DATA_1906_002.txt
"""

