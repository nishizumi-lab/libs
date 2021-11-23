import 'package:flutter_test/flutter_test.dart';
import 'package:electric/taigi/taigi4_wind_pressure.dart';

void main() {
  test('adds one to input values', () {
    final wp = WindPressure();

    // 風圧荷重W
    print(wp.calcW(828, 1.25, 1.0)); // 1035.0

    // 速度圧qp
    print(wp.calcQp(34, 1.194, 1.0)); // 828.1583999999998


  });
}
