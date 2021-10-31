library calendarjp;

class Calendar {
  Calendar() {}
  // 年齢 → 干支
  String yearToEto2(int year) {
    var arr = ["saru", "tori", "inu", "i", "ne", "ushi", "tora", "u", "tatsu", "mi", "uma", "hitsuji"];
    return arr[year % 12];
  }

  String yearToEto(int year) {
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
    } else if ((year == 1912) && (month < 8) && (day < 31)) {
      wareki = "明治45";
    } else if ((year == 1912) && (month < 7)) {
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

  // 西暦 → 令和
  String yearToReiwa(num year, num month, num day) {
    return "令和" + (year - 2018).toString();
  }

  // 西暦 → 平成
  String yearToHeisei(num year, num month, num day) {
    return "平成" + (year - 1988).toString();
  }

  // 西暦 → 昭和
  String yearToShowa(num year, num month, num day) {
    return  "昭和" + (year - 1925).toString();
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
  num yearToAge(int year, int month, int day) {
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

  // 西暦を干支に変換
  String ageToEvent(num age) {
    var events = "";
    if(age == 0) {events = "今年";}
    else if(age == 7) {events = "小学入学";}
    else if(age == 13) {events = "中学入学";}
    else if(age == 16) {events = "高校入学";}
    else if(age == 19) {events = "大学入学";}
    else if(age == 20) {events = "成人";}
    else if(age == 24) {events = "厄年(男)";}
    else if(age == 27) {events = "アラサー";}
    else if(age == 30) {events = "而立";}
    else if(age == 32) {events = "厄年(女)";}
    else if(age == 36) {events = "厄年(女)";}
    else if(age == 40) {events = "初老,不惑";}
    else if(age == 41) {events = "厄年(男)";}
    else if(age == 50) {events = "中老,知命";}
    else if(age == 60) {events = "還暦,厄年";}
    else if(age == 64) {events = "破瓜";}
    else if(age == 65) {events = "定年退職";}
    else if(age == 70) {events = "杖国";}
    else if(age == 77) {events = "喜寿";}
    else if(age == 80) {events = "傘寿,杖朝";}
    else if(age == 88) {events = "米寿";}
    else if(age == 90) {events = "卒寿";}
    else if(age == 98) {events = "白寿";}
    else if(age == 100) {events = "百賀";}
    else if(age == 108) {events = "茶寿";}
    else if(age == 111) {events = "皇寿";}
    else if(age == 112) {events = "珍寿";}
    else if(age == 120) {events = "大還暦";}
    else{events = "";}
    return events;
  }
}

