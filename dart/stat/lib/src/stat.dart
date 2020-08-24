import 'dart:math';

class Stat {
  Stat() {}

  num sum(var list) {
    num sum_value = 0;
    for (num value in list) {
      sum_value += value;
    }
    return sum_value;
  }

  num max(var list) {
    int max = list[0];
    for (num value in list) {
      if (value > max) {
        max = value;
      }
    }
    return max;
  }

  num min(var list) {
    int min = list[0];
    for (num value in list) {
      if (value < min) {
        min = value;
      }
    }
    return min;
  }
  
  num mean(var list) {
    num mean_value = this.sum(list) / list.length;
    return mean_value;
  }

  num median(var list) {
    final length = list.length;
    num median;

    if (length % 2 == 1) {
      median = list[(length / 2 + 0.5).toInt()];
    } else {
      median = ((list[length ~/ 2] + list[length ~/ 2 + 1]) ~/ 2);
    }
    return median;
  }
  
}

