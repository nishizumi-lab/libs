import 'package:flutter_test/flutter_test.dart';
import 'package:electric/taigi/taigi4_wind_pressure.dart';
import 'package:electric/taigi/taigi4_allowable_stress.dart';

void main() {
  test('adds one to input values', () {
    final wp = WindPressure();
    final as = AllowableStress();

    // @param Zb 地表面粗度区分で定まる値(JIS C 8955 表4) 5
    // @param Zg 地表面粗度区分で定まる値(JIS C 8955 表4) 450
    // @param alpha 地表面粗度区分で定まる値(JIS C 8955 表4) 0.20
    // @param H アレイ面の平均地上高(m)(アレイの最大高さと最小高さの中間で架台構造により決まる) 1.789
    // @retval 平均風速の高さ方向の分布を表す係数Er
    print(wp.calcEr(5, 450, 0.20, 1.789)); // 0.6911947320312629

    // @brief 平均風速の高さ方向の分布を表す係数Er、ガスト影響係数Gfから環境係数Eを計算します。
    // @param Er 平均風速の高さ方向の分布を表す係数(calcErで計算) 0.691
    // @param Gf ガスト影響係数（※突風の影響を示す）(JIS C 8955 表3) 2.5
    // @retval 環境係数E
    print(wp.calcE(0.691, 2.5)); // 1.1937024999999999

    // @brief 設計用基準風速V0、環境係数E、用途係数Iwから設計用速度圧qを計算します。
    // @param V0 設計用基準風速V0(m/s)(JIS C 8955 表2より地域で決まる) 34
    // @param E 環境係数E(calcEで計算) 1.194
    // @param Iw 用途係数Iw(JIS C 8955 表5より利用用途で決まる) 1.0
    // @retval 設計用速度圧q 828.1583999999998
    print(wp.calcQp(34, 1.194, 1.0)); // 828.1583999999998

    // @fn calcCa
    // @brief 太陽電池アレイの傾斜角度もしくは相対角度と設置形態から風圧係数Caを計算します。
    // @param theta 太陽電池アレイの傾斜角度もしくは相対角度(架台構造と地盤傾斜により決まる)[deg]
    // @param type 設置形態。1:地上設置(正圧)、2:地上設置(負圧)、3:勾配屋根設置(正圧)、4:勾配屋根設置(負圧)、5:陸屋根設置(正圧、端部アレイ)、6:陸屋根設置(正圧、中央部アレイ)、7:陸屋根設置(負圧、端部アレイ)、8:陸屋根設置(負圧、中央部アレイ) ※ 正圧は順風、負圧は逆風ともいいます。
    // @retval アレイの風圧係数Ca
    print(wp.calcCa(20, "地上設置(正圧)")); // 1.25  傾斜角度(相対角)20degで地上設置(正圧)の場合
    print(wp.calcCa(20, "地上設置(負圧)")); // 1.61  傾斜角度(相対角)20degで地上設置(負圧)の場合
    print(wp.calcCa(0, "地上設置(正圧)")); // 0.35  傾斜角度(相対角)20degで地上設置(正圧)の場合
    print(wp.calcCa(0, "地上設置(負圧)")); // 0.85  傾斜角度(相対角)20degで地上設置(負圧)の場合

    // @brief 風力係数C、設計用速度圧q、受風面積Aから風圧荷重を計算します。
    // @param C アレイ面，支持物構成材の風力係数(アレイ面についてはcalcCa、支持物についてはJIS C 8955 表もしくは風洞実験等により計算) 1.25
    // @param q 設計用速度圧q(calcQpで計算) 828
    // @param A アレイ面の受風面積，支持物構成材の鉛直投影面積A（m2）(架台構造から計算、単位平方面積で考えるなら1) 1.0
    // @retval アレイ，支持物構成材に作用する風圧荷重W（N） 1035.0
    print(wp.calcW(828, 1.25, 1.0)); // 1035.0 傾斜角(相対角)20degで地上設置(正圧)の場合
    print(wp.calcW(828, -1.61, 1.0)); // -1333.08 傾斜角(相対角)20degで地上設置(負圧)の場合(※正圧方向を正として、風圧係数は負の値にしている)
    print(wp.calcW(828, 0.35, 1.0)); // 289.79 傾斜角(相対角)0degで地上設置(正圧)の場合
    print(wp.calcW(828, -0.85, 1.0)); // -703.8 傾斜角(相対角)0degで地上設置(負圧)の場合(※正圧方向を正として、風圧係数は負の値にしている)

    // @brief 降伏点強度Fから長期許容引張応力度Ftを計算します。
    // @param F 降伏点強度=降伏点=基準強度=引張強さF[N/mm2] : SS400の場合、「F=235」と鋼構造設計指針や告示2464号に規定されている。
    // @param material 材質。steel:鋼材、
    // @retval 長期許容引張応力度Ft[N/mm2]
    print(as.calcFt(235, "steel")); // 156.66666666666666

    // @brief 降伏点強度Fから長期許容せん断応力度Fsを計算します。
    // @param F 降伏点強度=降伏点=基準強度=引張強さF[N/mm2] 235 : SS400の場合、「F=235」と鋼構造設計指針や告示2464号に規定されている。
    // @param material 材質。steel:鋼材、
    // @retval 長期許容せん断応力度Fs[N/mm2]
    print(as.calcFs(235, "steel")); // 90.45154217304137

    // @brief 座屈長さLkと断面二次半径iから細長比λを計算します。
    // @param Lk 座屈長さLk[mm] 1245.2(x, y軸回りで同じ)
    // @param i 断面二次半径i[mm] 30(x軸回り), 16.9(y軸回り)
    // @retval 細長比λ
    print(as.calcLamda(1245.2, 30)); // 41.50666666666667
    print(as.calcLamda(1245.2, 16.9)); // 73.68047337278108
    // 細長比 λ = max( λx , λy ) = max( 41.5 ,73.7 ) = 73.7を採用

  });
}
