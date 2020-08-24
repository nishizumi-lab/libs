class Calendar {
  Calendar() {}
  // 年齢 → 干支
  String yearToEto(num year) {
    var arr = ["申", "酉", "戌", "亥", "子", "丑", "寅", "卯", "辰", "巳", "午", "未"];
    return arr[year % 12];
  }

  // 西暦 → 和暦
  String yearToWareki(num year, num month, num day) {
    var wareki = "エラー";

    if ((year == 2019) && (month < 5)) {
      wareki = "平成31";
    } else if ((year == 1989) && (month < 2) && (day < 8)) {
      wareki = "昭和64";
    } else if ((year == 1926) && (month < 13) && (day < 26)) {
      wareki = "大正15";
    } else if ((year == 1926) && (month < 12)) {
      wareki = "大正15";
    } else if ((year == 1868) && (month < 8) && (day < 31)) {
      wareki = "明治45";
    } else if ((year == 1868) && (month < 7)) {
      wareki = "明治45";
    } else if (year > 2018)
      wareki = "令和" + (year - 2018).toString();
    else if (year > 1988)
      wareki = "平成" + (year - 1988).toString();
    else if (year > 1925)
      wareki = "昭和" + (year - 1925).toString();
    else if (year > 1911)
      wareki = "大正" + (year - 1911).toString();
    else
      wareki = "明治" + (year - 1867).toString();

    return wareki;
  }

  // 和暦 →　西暦
  num warekiToYear(String nengo, num yearWareki) {
    if ((nengo == "令和") && (yearWareki > 0)) {
      return yearWareki + 2018;
    } else if ((nengo == "平成") && (yearWareki > 0)) {
      return yearWareki + 1988;
    } else if ((nengo == "昭和") && (yearWareki > 0) && (yearWareki <= 64)) {
      return yearWareki + 1925;
    } else if ((nengo == "大正") && (yearWareki > 0) && (yearWareki <= 15)) {
      return yearWareki + 1911;
    } else if ((nengo == "明治") && (yearWareki > 0) && (yearWareki <= 45)) {
      return yearWareki + 1867;
    } else {}

    return -1;
  }

  // 西暦 → 年齢
  num yearToAge(num year, num month, num day) {
    //今日
    var now = new DateTime.now();

    // 生年月日
    var birthday = new DateTime(year, month, day);

    // 今年の誕生日
    var thisYearBirthday = new DateTime(now.year, month, day);

    //今年-誕生年
    var age = now.year - birthday.year;

    //今年の誕生日を迎えていなければage-1を返す
    if (thisYearBirthday.isAfter(now)) {
      age = age - 1;
    }
    return age;
  }
}
