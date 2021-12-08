library electric;
import 'dart:math';

class WindPressure {
  WindPressure() {}

  // @fn calcCa
  // @brief 太陽電池アレイの傾斜角度もしくは相対角度と設置形態から風圧係数Caを計算します。
  // @param theta 太陽電池アレイの傾斜角度もしくは相対角度(架台構造と地盤傾斜により決まる)[deg]
  // @param type 設置形態。地上設置(正圧)、地上設置(負圧)、勾配屋根設置(正圧)、勾配屋根設置(負圧)、陸屋根設置(正圧、端部アレイ)、陸屋根設置(正圧、中央部アレイ)、陸屋根設置(負圧、端部アレイ)、陸屋根設置(負圧、中央部アレイ) ※ 正圧は順風、負圧は逆風ともいいます。
  // @retval アレイの風圧係数Ca
  double calcCa(double theta, String type){
    // 正圧は順風、負圧は逆風ともいいます。
    if(type == "地上設置(正圧)"){
      return 0.35 + 0.055 * theta - 0.0005 * pow(theta,2);
    }
    // 2:地上設置(負圧)
    else if(type == "地上設置(負圧)"){
      return 0.85 + 0.048 * theta - 0.0005 * pow(theta,2);
    }
    // 3:勾配屋根設置(正圧)
    else if(type == "勾配屋根設置(正圧)"){
      return 1.14;
    }
    // 4:勾配屋根設置(負圧)
    else if(type == "勾配屋根設置(負圧)"){
      return 1.5 - 0.015 * theta;
    }
    // 5:陸屋根設置(正圧、端部アレイ)
    else if(type == "陸屋根設置(正圧、端部アレイ)"){
      if(theta <= 10){
        return 0.75;
      }
      else if(theta <= 10  && theta <= 50){
        return 0.49 + 0.026 * theta;
      }
      else if(theta >= 50  && theta <= 60){
        return 1.8;
      }
      else{
        return 0;
      }
    }
    // 6:陸屋根設置(正圧、中央部アレイ)
    else if(type == "陸屋根設置(正圧、中央部アレイ)"){
      if(theta <= 10){
        return 0.6;
      }
      else if(theta <= 10  && theta <= 30){
        return 0.4 + 0.02 * theta;
      }
      else if(theta >= 30  && theta <= 60){
        return 1.0;
      }
      else{
        return 0;
      }
    }
    else if(type == "陸屋根設置(負圧、端部アレイ)"){
      if(theta <= 10){
        return 0.6;
      }
      else if(theta <= 10  && theta <= 35){
        return 0.04 + 0.056 * theta;
      }
      else if(theta >= 35  && theta <= 60){
        return 2.0;
      }
      else{
        return 0;
      }
    }
    else if(type == "陸屋根設置(負圧、中央部アレイ)"){
      if(theta <= 10){
        return 0.6;
      }
      else if(theta <= 10  && theta <= 30){
        return 0.4 + 0.02 * theta;
      }
      else if(theta >= 30  && theta <= 60){
        return 1.0;
      }
      else{
        return 0;
      }
    }
    return 0;
  }

  // @fn calcEr
  // @brief 地表面粗度区分に応じて決まる数値Zb, Zg, alphaと、アレイ面の平均地上高H(m)から平均風速の高さ方向の分布を表す係数Erを計算します。
  // @param Zb 地表面粗度区分で定まる値(JIS C 8955 表)
  // @param Zg 地表面粗度区分で定まる値(JIS C 8955 表)
  // @param alpha 地表面粗度区分に応じて決まる数値(JIS C 8955 表)
  // @param H アレイ面の平均地上高(アレイの最大高さと最小高さの中間)(m)
  // @retval 平均風速の高さ方向の分布を表す係数Er
  double calcEr(double Zb, double Zg, double alpha, double H) {
    if(Zb > H){
      return 1.7 * pow(Zb/Zg, alpha);
    } else{
      return 1.7 * pow(H/Zg, alpha);
    }
  }

  // @fn calcE
  // @brief 平均風速の高さ方向の分布を表す係数Er、ガスト影響係数Gfから環境係数Eを計算します。
  // @param Er 平均風速の高さ方向の分布を表す係数(別途計算)
  // @param Gf ガスト影響係数（※突風の影響を示す）(JIS C 8955 表)
  // @retval 環境係数E
  double calcE(double Er, double Gf) {
    return Er * Er * Gf;
  }

  // @fn calcQp
  // @brief 設計用基準風速V0、環境係数E、用途係数Iwから設計用速度圧qを計算します。
  // @param V0 設計用基準風速V0(m/s)
  // @param E 環境係数E
  // @param Iw 用途係数Iw
  // @retval 設計用速度圧q
  double calcQp(double V0, double E, double Iw) {
    return 0.6 * V0 * V0 * E * Iw;
  }

  // @fn calcW
  // @brief 風力係数C、設計用速度圧q、受風面積Aから風圧荷重を計算します。
  // @param C アレイ面，支持物構成材の風力係数(別途計算)
  // @param q 設計用速度圧q(別途計算)
  // @param A アレイ面の受風面積，支持物構成材の鉛直投影面積A（m2）
  // @retval アレイ，支持物構成材に作用する風圧荷重W（N）
  double calcW(double C, double q, double A) {
    return C * q * A;
  }

}