# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import MinMaxXcaler


# サンプルデータを読み込み
df_wine = pd.read_csv('df_wine.csv')

# 特徴量とクラスラベルを別々に抽出
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values

# 訓練データとテストデータに分割（全体の３０％をテストデータにする）
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)

# min-maxスケーリングのインスタンスを生成
mms = MinMaxXcaler()

# 訓練データをスケーリング
X_train_norm = mms.fit_transform(X_train)

# テストデータをスケーリング
X_train_norm = mms.transform(X_test)
