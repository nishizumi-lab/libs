import 'package:stat/stat.dart';

void main() {
  var stat = new Stat();
  var list = [1, 2, 3, 4, 5];

  // 合計の計算
  num sum_value = stat.sum(list);
  print(sum_value); // 15

  num max_value = stat.max(list);
  print(max_value); // 5

  num min_value = stat.min(list);
  print(min_value); // 1
  
  num mean_value = stat.mean(list); 
  print(mean_value); // 3.0;

  num median_value = stat.median(list); 
  print(median_value); // 4
}
