#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from calc2.electricity.ac3 import AcPhase3

ac3 = AcPhase3()

print("■Input...El, P3p, Cos, delta or star wire")
result1 = ac3.El_P3p_Cos(El=480., P3p=2000000., Cos=1., wire="delta")
ac3.show_result(result1)

result2 = ac3.El_P3p_Cos(El=480., P3p=2000000., Cos=1., wire="star")
ac3.show_result(result2)

print("■Input...El, Rp, Xp, delta or star wire")
result3 = ac3.El_Rp_Xp(El=480., Rp=0.345, Xp=0., wire="delta")
ac3.show_result(result3)

result4 = ac3.El_Rp_Xp(El=480., Rp=0.1152, Xp=0., wire="star")
ac3.show_result(result4)

print("■Input...Il, Zp, Cos, delta or star wire")
result5 = ac3.Il_Zp_Cos(Il=2405.3, Zp=0.346, Cos=1., wire="delta")
ac3.show_result(result5)

result6 = ac3.Il_Zp_Cos(Il=2405.3, Zp=0.1152, Cos=1., wire="star")
ac3.show_result(result6)

print("■Input...Il, Rp, Xp, delta or star wire")
result7 = ac3.Il_Rp_Xp(Il=2405.5, Rp=0.3456, Xp=0., wire="delta")
ac3.show_result(result7)

result8 = ac3.Il_Rp_Xp(Il=2405.5, Rp=0.1152, Xp=0., wire="star")
ac3.show_result(result8)

print("■Input...Il, El, Cos, delta or star wire")
result9 = ac3.El_Il_Cos(Il=2405.6, El=480., Cos=1., wire="delta")
ac3.show_result(result9)

result10 = ac3.El_Il_Cos(Il=2405.6, El=480., Cos=1., wire="star")
ac3.show_result(result10)

print("■Input...Il, P3p, Cos, delta or star wire")
result11 = ac3.Il_P3p_Cos(Il=2405.6, P3p=2000000., Cos=1., wire="delta")
ac3.show_result(result11)

result12 = ac3.Il_P3p_Cos(Il=2405.6, P3p=2000000., Cos=1., wire="star")
ac3.show_result(result12)


"""
■Input...El, P3p, Cos, delta or star wire
Il[A] = 2405.626121623441
El[V] = 480.0
P3p（W） = 2000000.0
Pp（W） = 666666.6666666666
Cosθ[rad] = 1.0
Ep[V] = 480.0
Ip[A] = 1388.8888888888891
Zp[Ω] = 0.34559999999999996
Rp[Ω] = 0.34559999999999996
Xp[Ω] = 0.0
------------------------------------
Il[A] = 2405.626121623441
El[V] = 480.0
P3p（W） = 2000000.0
Pp（W） = 666666.6666666666
Cosθ[rad] = 1.0
Ep[V] = 277.1281292110204
Ip[A] = 2405.626121623441
Zp[Ω] = 0.1152
Rp[Ω] = 0.1152
Xp[Ω] = 0.0
------------------------------------
■Input...El, Rp, Xp, delta or star wire
Il[A] = 2409.8098192262646
El[V] = 480.0
P3p（W） = 2003478.2608695654
Pp（W） = 667826.0869565218
Cosθ[rad] = 1.0
Ep[V] = 480.0
Ip[A] = 2409.8098192262646
Zp[Ω] = 0.345
Rp[Ω] = 0.345
Xp[Ω] = 0.0
------------------------------------
Il[A] = 2405.6261216234416
El[V] = 480.0
P3p（W） = 2000000.0000000005
Pp（W） = 666666.6666666669
Cosθ[rad] = 1.0
Ep[V] = 277.1281292110204
Ip[A] = 2405.6261216234416
Zp[Ω] = 0.1152
Rp[Ω] = 0.1152
Xp[Ω] = 0.0
------------------------------------
■Input...Il, Zp, Cos, delta or star wire
Il[A] = 2405.3
El[V] = 480.4904084587052
P3p（W） = 2001771.9591400002
Pp（W） = 667257.3197133334
Cosθ[rad] = 1.0
Ep[V] = 480.4904084587052
Ip[A] = 1388.700602481807
Zp[Ω] = 0.346
Rp[Ω] = 0.346
Xp[Ω] = 0.0
------------------------------------
Il[A] = 2405.3
El[V] = 479.93492821771247
P3p（W） = 1999457.7719040003
Pp（W） = 666485.9239680001
Cosθ[rad] = 1.0
Ep[V] = 277.09056000000004
Ip[A] = 2405.3
Zp[Ω] = 0.1152
Rp[Ω] = 0.1152
Xp[Ω] = 0.0
------------------------------------
■Input...Il, Rp, Xp, delta or star wire
Il[A] = 2405.5
El[V] = 479.9748346683189
P3p（W） = 1999790.2944000005
Pp（W） = 666596.7648000001
Cosθ[rad] = 1.0
Ep[V] = 479.9748346683189
Ip[A] = 1388.816072535645
Zp[Ω] = 0.3456
Rp[Ω] = 0.3456
Xp[Ω] = 0.0
------------------------------------
Il[A] = 2405.5
El[V] = 479.97483466831886
P3p（W） = 1999790.2944
Pp（W） = 666596.7648
Cosθ[rad] = 1.0
Ep[V] = 277.1136
Ip[A] = 2405.5
Zp[Ω] = 0.1152
Rp[Ω] = 0.1152
Xp[Ω] = 0.0
------------------------------------
■Input...Il, El, Cos, delta or star wire
Il[A] = 2405.6
El[V] = 480.0
P3p（W） = 1999978.2828900917
Pp（W） = 666659.4276300306
Cosθ[rad] = 1.0
Ep[V] = 480.0
Ip[A] = 1388.8738075625638
Zp[Ω] = 0.3456037527573416
Rp[Ω] = 0.3456037527573416
Xp[Ω] = 0.0
------------------------------------
Il[A] = 2405.6
El[V] = 480.0
P3p（W） = 1999978.2828900917
Pp（W） = 666659.4276300306
Cosθ[rad] = 1.0
Ep[V] = 277.1281292110204
Ip[A] = 2405.6
Zp[Ω] = 0.1152012509191139
Rp[Ω] = 0.1152012509191139
Xp[Ω] = 0.0
------------------------------------
■Input...Il, P3p, Cos, delta or star wire
Il[A] = 2405.6
El[V] = 480.0052121629745
P3p（W） = 2000000.0
Pp（W） = 666666.6666666666
Cosθ[rad] = 1.0
Ep[V] = 480.0052121629745
Ip[A] = 1388.8738075625638
Zp[Ω] = 0.34560750555543324
Rp[Ω] = 0.34560750555543324
Xp[Ω] = 0.0
------------------------------------
Il[A] = 2405.6
El[V] = 480.00521216297454
P3p（W） = 2000000.0
Pp（W） = 666666.6666666666
Cosθ[rad] = 1.0
Ep[V] = 277.1311384547168
Ip[A] = 2405.6
Zp[Ω] = 0.1152025018518111
Rp[Ω] = 0.1152025018518111
Xp[Ω] = 0.0
------------------------------------
"""
