library electric;
import 'dart:math';

class AllowableStress {
  AllowableStress() {}

  // @fn calcFt
  // @brief 降伏点強度Fから長期許容引張応力度Ftを計算します。
  // @param F 降伏点強度=降伏点=基準強度=引張強さF[N/mm2]
  // @param material 材質。steel:鋼材、
  // @retval 長期許容引張応力度Ft[N/mm2]
  double calcFt(double F, String material) {
    if(material == "steel") {
      return F / 1.5;
    }
    return 0;
  }

  // @fn calcFs
  // @brief 降伏点強度Fから長期許容せん断応力度Fsを計算します。
  // @param F 降伏点強度=降伏点=基準強度=引張強さF[N/mm2]
  // @param material 材質。steel:鋼材、
  // @retval 長期許容せん断応力度Fs[N/mm2]
  double calcFs(double F, String material) {
    if(material == "steel") {
      return F /sqrt(3)/ 1.5;
    }
    return 0;
  }

  // @fn calcLamda
  // @brief 座屈長さLkと断面二次半径iから細長比λを計算します。
  // @param Lk 座屈長さLk[mm]
  // @param i 断面二次半径i[mm]
  // @retval 細長比λ
  double calcLamda(double Lk, double i) {
    return Lk/i;
  }
}