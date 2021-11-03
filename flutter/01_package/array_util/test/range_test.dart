import 'package:flutter_test/flutter_test.dart';
import 'package:array_util/range.dart';

void main() {
  test('adds one to input values', () {
    var listItem = new List.from(range(10, 20, 1));
    print(listItem);    // [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
  });
}