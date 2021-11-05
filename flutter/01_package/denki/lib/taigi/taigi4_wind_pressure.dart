/*
@brief Analyzes various parameters of pulse signals.
@details Analyzes various parameters of pulse signals.
*/
library denki;

class WindPressure {
  WindPressure() {}

  //
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
}