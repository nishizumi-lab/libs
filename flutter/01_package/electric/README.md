# electric

It is an electric calculation package
[Documment](https://nishizumi-lab.github.io/libs/flutter/01_package/electric/docs/html/index.html)


# 参考資料


## 電気主任技術者関連

[地上設置型太陽光発電システムの設計ガイドライン2019年版](https://www.nedo.go.jp/activities/ZZJP2_100060.html#guideline)

[経済産業省 法令｜電力の安全](https://www.meti.go.jp/policy/safety_security/industrial_safety/law/index.html)

[電気事業法　告示・内規等](https://www.meti.go.jp/policy/safety_security/industrial_safety/law/denjikokuji.html)

[JIS C 8955（太陽電池アレイ用支持物の設計用荷重算出方法）の改定内容](https://www.safety-chugoku.meti.go.jp/denki/hatsuden/taiyoukou/file/seminarshiryou2.pdf)

# Sample code

```
    // 速度圧qp
    print(wp.calcQp(34, 1.194, 1.0)); // 828.1583999999998

    // 風圧荷重W
    print(wp.calcW(828, 1.25, 1.0)); // 1035.0
```


