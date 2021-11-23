library electric;
import 'dart:math';

class WindPressure {
  WindPressure() {}

  // @fn calcW
  // @brief 風力係数C、設計用速度圧q、受風面積Aから風圧荷重を計算します。
  // @param C ：アレイ面，支持物構成材の風力係数
  // @param q 設計用速度圧q（N・mିଶ）
  // @param A アレイ面の受風面積，支持物構成材の鉛直投影面積A（mଶ）
  // @retval アレイ，支持物構成材に作用する風圧荷重W（N）

  double calcW(double C, double q, double A) {
    return C * q * A;
  }

  // @fn calcQp
  // @brief 設計用基準風速V0、環境係数E、用途係数Iwから設計用速度圧qを計算します。
  // @param V0 ：設計用基準風速V0 ms^-1
  // @param E 環境係数E
  // @param Iw 用途係数Iw
  // @retval 設計用速度圧q（N・mିଶ）
  double calcQp(double V0, double E, double Iw) {
    return 0.6 * V0 * V0 * E * Iw;
  }

  // @fn calcE
  // @brief 平均風速の高さ方向の分布を表す係数Er、ガスト影響係数Gfから環境係数Eを計算します。
  // @param Er 平均風速の高さ方向の分布を表す係数
  // @param Gf ガスト影響係数（※突風の影響を示す）
  // @retval 環境係数E
  double calcE(double Er, double Gf) {
    return Er * Er * Gf;
  }

  // @fn calcEr
  // @brief 地表面粗度区分に応じて決まる数値Zb, Zg, alphaと、アレイ面の平均地上高H(m)から平均風速の高さ方向の分布を表す係数Erを計算します。
  // @param Zb 地表面粗度区分に応じて決まる数値
  // @param Zg 地表面粗度区分に応じて決まる数値
  // @param H アレイ面の平均地上高(m)
  // @param alpha 地表面粗度区分に応じて決まる数値
  // @retval 平均風速の高さ方向の分布を表す係数Er
  double calcEr(double Zb, double Zg, double H, double alpha) {
    if(Zb > H){
      return 1.7 * pow(Zb/Zg, alpha);
    } else{
      return 1.7 * pow(H/Zg, alpha);
    }
  }
}