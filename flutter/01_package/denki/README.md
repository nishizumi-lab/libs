# denki

calc of electricity
電気技術者向けの計算パッケージです。

## Getting Started

This project is a starting point for a Dart
[package](https://flutter.dev/developing-packages/),
a library module containing code that can be shared easily across
multiple Flutter or Dart projects.

For help getting started with Flutter, view our 
[online documentation](https://flutter.dev/docs), which offers tutorials, 
samples, guidance on mobile development, and a full API reference.

## 参考資料


#### 電気主任技術者関連

[地上設置型太陽光発電システムの設計ガイドライン2019年版](https://www.nedo.go.jp/activities/ZZJP2_100060.html#guideline)

[経済産業省 法令｜電力の安全](https://www.meti.go.jp/policy/safety_security/industrial_safety/law/index.html)

[電気事業法　告示・内規等](https://www.meti.go.jp/policy/safety_security/industrial_safety/law/denjikokuji.html)


## Sample code

```
    final wp = WindPressure();

    // 風圧荷重W
    print(wp.calcW(1.0, 34, 2.0)); // 68.0
```