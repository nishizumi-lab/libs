import 'package:calender_jp/base.dart';

void main() {
  var calender = Calendar();

  // 西暦　→　干支
  String eto = calender.yearToEto(1992);
  print(eto); // 申

  // 西暦　→　和暦
  String wareki = calender.yearToWareki(1992, 7, 23);
  print(wareki); // 平成4

  // 和暦　→　西暦
  num year = calender.warekiToYear("平成", 4);
  print(year); // 1992

  // 西暦 →　年齢
  num age = calender.yearToAge(1992, 7, 23);
  print(age); // 26
}