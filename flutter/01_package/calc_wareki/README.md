# calc_wareki

calc for wareki

## Getting Started

This project is a starting point for a Dart
[package](https://flutter.dev/developing-packages/),
a library module containing code that can be shared easily across
multiple Flutter or Dart projects.

For help getting started with Flutter, view our 
[online documentation](https://flutter.dev/docs), which offers tutorials, 
samples, guidance on mobile development, and a full API reference.

## Sample Code

'''
    final calender = Calendar();

    // 西暦　→　干支(十二支)
    String eto = calender.yearToEto(2022);
    print(eto); // 寅

    // 西暦　→　干支(十二支 ローマ字)
    String eto2 = calender.yearToEto2(2022);
    print(eto2); // tora

    // 西暦　→　干支(十干)
    String eto10 = calender.yearToEto10(2022);
    print(eto10); // 壬

    // 西暦　→　和暦
    String wareki = calender.yearToWareki(1992, 7, 23);
    print(wareki); // 平成4

    // 和暦　→　西暦
    num year = calender.warekiToYear("平成", 4);
    print(year); // 1992

    // 西暦 →　年齢
    num age = calender.yearToAge(1992, 7, 23);
    print(age); // 26
'''
