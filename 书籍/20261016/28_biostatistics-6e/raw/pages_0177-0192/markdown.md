查 q 值表（附表 12），当 $df_{e}=16,\ M=2 、 3 、$ 4 时，将 $q_{0.05} 、 q_{0.01}$ 的值列于表 7-9，由式（7-25）计算出相应的最小显著极差 LSR:

$$
L S R _ {0. 0 5} = q _ {0. 0 5} \cdot s _ {\bar {x}}
$$

$$
L S R _ {0. 0 1} = q _ {0. 0 1} \cdot s _ {\overline {{x}}}
$$

计算结果列于表 7-9 中。

表 7-9 例 7-1 不同营养土培养芦荟株高多重比较的 LSR 值 $( q$ 法）

| M | 2 | 3 | 4 |
| --- | --- | --- | --- |
| $q_{0.05}$ | 3.00 | 3.65 | 4.05 |
| $q_{0.01}$ | 4.13 | 4.78 | 5.19 |
| $LSR_{0.05}$ | 0.879 | 1.069 | 1.187 |
| $LSR_{0.01}$ | 1.210 | 1.401 | 1.521 |

根据表 7-9，用 $q$ 检验法对例 7-1 数据进行差异显著性检验，结果列于表 7-10。

表 7-10 例 7-1 不同营养土培养芦荟株高差异显著性（q 法）

<table><tr><td rowspan="2">营养土</td><td rowspan="2">平均数 $(\bar{x}_i)$ </td><td colspan="2">差异显著性</td></tr><tr><td> $\alpha=0.05$ </td><td> $\alpha=0.01$ </td></tr><tr><td> $A_1$ </td><td>18.52</td><td>a</td><td>A</td></tr><tr><td> $A_3$ </td><td>17.42</td><td>b</td><td>A</td></tr><tr><td> $A_2$ </td><td>17.28</td><td>b</td><td>A</td></tr><tr><td> $A_4$ </td><td>16.04</td><td>c</td><td>B</td></tr></table>

由表 7-7 和表 7-9 可知，当 $M { \geq } 2$ 时，由于 $q$ 法的 $L S R _ { \alpha }$ 更大，所以对于例 7-1 的数据进行多重比较时， $q$ 法检验结果（表 7-10）与 SSR 法检验结果（表 7-8）存在一定的差异。

对比以上所介绍的这三种多重比较检验方法可以发现，在样本数（处理数）k=2 时，LSD法、SSR 法和 $q$ 法的显著尺度是相同的。当 $k { \ngeq } 3$ 时，3 种检验的显著尺度便不相同。LSD 法最低、SSR 法次之、 $q$ 法最高，即这三种检验方法的检验尺度关系为 LSD 法≤SSR 法≤q 法。用 LSD 法检验显著的差数，用 SSR 法或 $q$ 法检验则未必显著；而用 $q$ 法检验显著的差数，

用 LSD 法进行检验差异必然显著。在实际研究工作中，对于精度要求高的试验应用 $q$ 法，一般试验可用 SSR 法，试验中各处理都与对照相比的试验数据可用LSD 法。

多重比较的方法还有很多。应当注意，无论采用何种方法表示多重比较结果，都应注明采用的是哪一种多重比较方法。

![](images/page_176_image_15.jpg)

不同多重

比较方法

的比较

综上所述，方差分析的基本步骤是:①将样本数据的总平方和与总自由度分解为各变异因素的平方和与自由度；②列方差分析表进行 F 检验，分析各变异因素在总变异中的重要程度；③计算处理间平方和与处理内平方和之间的关系强度；④若 F 检验结果显著，对各处理平均数进行多重比较。

## 第二节 单因素方差分析

根据试验因素的多少，方差分析可以分为单因素方差分析、二因素方差分析和多因素方差分析。单因素试验（single factor experiment）数据的方差分析称为单因素方差分析（one-way analysis of variance，one-way ANOVA），它是方差分析中最基本、最简单的一种，目的在于正确判断该试验因素各水平的相对效果。在单因素方差分析中，根据组内观测数目（重复数）是否相同，又分为组内观测次数相等的方差

![](images/page_177_image_2.jpg)

方差分析与

试验设计

分析和组内观测次数不相等的方差分析。如果考虑到非试验因素的差异，需要使用局部控制手段通过试验设计的区组技术，进行包含分解区组效应的方差分析方法，以提高试验的精度。

## 一、组内观测次数相等的方差分析

k 组数据，每一处理组皆含有 n 个观测值，其方差分析方法在本章第一节已做介绍，这里以方差分析表形式给出有关计算公式（表 7-11）。

表 7-11 组内观测次数相等（k 个处理 n 次重复）的单因素方差分析

| 变异来源 | df | SS | $s^{2}$ | F |
| --- | --- | --- | --- | --- |
| 处理间 | k-1 | $SS_{t}=\frac{\sum T_{i.}^{2}}{n}-C$ | $s_{t}^{2}$ | $\frac{s_{t}^{2}}{s_{e}^{2}}$ |
| 处理内 | k(n-1) | $SS_{e}=SS_{T}-SS_{t}$ | $s_{e}^{2}$ |  |
| 总变异 | nk-1 | $SS_{T}=\sum x^{2}-C$ |  |  |

例 **7-2** 测定东北、内蒙古、河北、安徽、贵州 5 个地区黄鼬冬季针毛的长度，每个地区随机抽取 4 个样本，测定的结果列于表 7-12。试比较各地区黄鼬针毛长度的差异显著性。

表 7-12 不同地区黄鼬冬季针毛长（mm）

| 地区 | 东北 | 内蒙古 | 河北 | 安徽 | 贵州 | 合计 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 32.0 | 29.2 | 25.5 | 23.3 | 22.3 |  |
| 2 | 32.8 | 27.4 | 26.1 | 25.1 | 22.5 |  |
| 3 | 31.2 | 26.3 | 25.8 | 25.1 | 22.9 |  |
| 4 | 30.4 | 26.7 | 26.7 | 25.5 | 23.7 |  |
| $\sum x$ | 126.4 | 109.6 | 104.1 | 99.0 | 91.4 | 530.5 |
| n | 4 | 4 | 4 | 4 | 4 | 20 |
| $\bar{x}$ | 31.60 | 27.40 | 26.03 | 24.75 | 22.85 | 26.53 |
| $\sum x^{2}$ | 3997.44 | 3007.98 | 2709.99 | 2453.16 | 2089.64 | 14258.21 |

在本例中，k=5， $n { = } 4$

（1）整理数据:计算 $\sum$ x、 x 和 $\sum x ^ { 2 }$ ，并列入表 7-12 中。
（2）计算平方和与自由度:

$$
C = \frac {T ^ {2}}{n k} = \frac {5 3 0 . 5 ^ {2}}{4 \times 5} = 1 4 0 7 1. 5 1
$$

$$
S S _ {T} = \sum x ^ {2} - C = 1 4 2 5 8. 2 1 - 1 4 0 7 1. 5 1 = 1 8 6. 7 0
$$

$$
S S _ {t} = \frac {\sum T _ {i .} ^ {2}}{n} - C = \frac {(1 2 6 . 4 ^ {2} + 1 0 9 . 6 ^ {2} + \cdots + 9 1 . 4 ^ {2})}{4} - 1 4 0 7 1. 5 1 = 1 7 3. 7 1
$$

$$
S S _ {e} = S S _ {T} - S S _ {t} = 1 8 6. 7 0 - 1 7 3. 7 1 = 1 2. 9 9
$$

$$
d f _ {T} = n k - 1 = 2 0 - 1 = 1 9
$$

$$
d f _ {t} = k - 1 = 5 - 1 = 4
$$

$$
d f _ {e} = k (n - 1) = 5 \times (4 - 1) = 1 5
$$

（3）计算方差:

$$
s _ {t} ^ {2} = \frac {S S _ {t}}{d f _ {t}} = \frac {1 7 3 . 7 1}{4} = 4 3. 4 2 8
$$

$$
s _ {e} ^ {2} = \frac {S S _ {e}}{d f _ {e}} = \frac {1 2 . 9 9}{1 5} = 0. 8 6 6
$$

（4）进行 F 检验:

$$
F = \frac {s _ {t} ^ {2}}{s _ {e} ^ {2}} = \frac {4 3 . 4 2 8}{0 . 8 6 6} = 5 0. 1 4 7 8
$$

查附表 5，得 $F_{0.05(4,15)} = 3.06$ $F_{0.01(4,15)} = 4.89$ ，故 $F > F_{0.01}, \quad P < 0.01$ ，说明 5 个地区黄鼬冬季针毛长度差异极显著，并将结果记入方差分析表（表 7-13）。

表 7-13 不同地区黄鼬冬季针毛长度方差分析表

| 变异来源 | df | SS | $s^2$ | F | $F_{0.05(4,15)}$ | $F_{0.01(4,15)}$ |
| --- | --- | --- | --- | --- | --- | --- |
| 处理间 | 4 | 173.71 | 43.428 | 50.15** | 3.06 | 4.89 |
| 处理内 | 15 | 12.99 | 0.866 |  |  |  |
| 总变异 | 19 | 186.70 |  |  |  |  |

知道了 5 个地区之间存在极显著性差异，要确定哪些地区之间的差异达到显著或极显著水平，需要进一步进行关系强度的测量和多重比较。

（5）关系强度的测量:由式（7-17）可知，本例中 $R ^ { 2 }$ 为

$$
R^2 = \frac{SS_t}{SS_T} = \frac{173.71}{186.70} = 93.04\%
$$

这表明不同地区（处理效应）对黄鼬冬季针毛长度的影响占总效应的 93.04%，而误差效应仅占 6.96%，说明地区间的差异达到了统计意义上极显著的程度。而其平方根 R 为 96.46%，说明不同地区黄鼬冬季针毛长度之间关系极强。

（6）多重比较:这里用 LSD 法进行检验。平均数差数标准误 $S _ { \overline { { x } } _ { 1 } - \overline { { x } } _ { 2 } }$ 为

$$
s _ {\bar {x} _ {1} - \bar {x} _ {2}} = \sqrt {\frac {2 s _ {e} ^ {2}}{n}} = \sqrt {\frac {2 \times 0 . 8 6 6}{4}} = 0. 6 5 8 (\mathrm{mm})
$$

查 t 值表，当误差自由度 $df_{e}=15$ 时， $t_{0.05} = 2.131, \quad t_{0.01} = 2.947$ ，则

$$
L S D _ {0. 0 5} = t _ {0. 0 5} \cdot s _ {\overline {{x}} _ {1} - \overline {{x}} _ {2}} = 2. 1 3 1 \times 0. 6 5 8 = 1. 4 0 2 (\mathrm{mm})
$$

$$
L S D _ {0. 0 1} = t _ {0. 0 1} \cdot s _ {\overline {{x}} _ {1} - \overline {{x}} _ {2}} = 2. 9 4 7 \times 0. 6 5 8 = 1. 9 3 9 (\mathrm{mm})
$$

将两组平均数的差值与 $L S D _ { 0 . 0 5 }$ 及 $L S D _ { 0 . 0 1 }$ 比较，若差数 $\text{> } LSD_{0.01}$ ，说明两地间黄鼬冬季针毛长度差异极显著，标以不同的大写字母；若差数 $\text{> } LSD_{0.05}$ ，说明两地黄鼬冬季针毛长度差异显著，标以不同的小写字母。多重比较的结果列于表 7-14。

表 7-14 不同地区黄鼬冬季针毛长度的差异显著性（LSD 法）

<table><tr><td rowspan="2">地区</td><td rowspan="2">平均数 $(\bar{x}_i)$ </td><td colspan="2">差异显著性</td></tr><tr><td> $\alpha=0.05$ </td><td> $\alpha=0.01$ </td></tr><tr><td>东北</td><td>31.60</td><td>a</td><td>A</td></tr><tr><td>内蒙古</td><td>27.40</td><td>b</td><td>B</td></tr><tr><td>河北</td><td>26.03</td><td>bc</td><td>BC</td></tr><tr><td>安徽</td><td>24.75</td><td>c</td><td>CD</td></tr><tr><td>贵州</td><td>22.85</td><td>d</td><td>D</td></tr></table>

检验结果表明，东北与其他地区，内蒙古与安徽、贵州，河北与贵州，黄鼬冬季针毛长度差异达极显著水平，安徽与贵州差异达到显著水平，而内蒙古与河北、河北与安徽差异不显著。

## 二、组内观测次数不相等的方差分析

由于试验情况的不同，有时会出现不同处理间观测次数（重复数）不同的情况。对于 k个处理的观测次数依次是 $n_{1} 、 n_{2} 、 \cdots 、 n_{k}$ 的单因素数据，上面所述的方差分析方法仍然可用，但由于总观测次数不是 nk，而是 $\sum _ { i = 1 } ^ { k } n _ { i }$ ，计算平方和的公式稍有不同（表 7-15）。

表 7-15 组内观测次数不等的方差分析

| 变异来源 | df | SS | $s^{2}$ | F |
| --- | --- | --- | --- | --- |
| 处理间(组间) | k-1 | $\sum \frac{T_{i}^{2}}{n_{i}} - C$ | $\frac{SS_{t}}{df_{t}}$ | $\frac{S_{t}^{2}}{S_{e}^{2}}$ |
| 处理内(组内) | $\sum n_{i} - k$ | $SS_{T} - SS_{t}$ | $\frac{SS_{e}}{df_{e}}$ |  |
| 总变异 | $\sum n_{i} - 1$ | $\sum x_{ij}^{2} - C$ |  |  |

在进行多重比较时，首先应计算平均数（或平均数差数）的标准误。由于各组内观测次数不等，无法直接套用式（7-22）或式（7-23），需先算得各 $n _ { i }$ 的平均数 $n _ { 0 } ;$

$$
n _ {0} = \frac {\left(\sum n _ {i}\right) ^ {2} - \sum n _ {i} ^ {2}}{\left(\sum n _ {i}\right) (k - 1)} \tag {7-26}
$$

然后有 $s _ { \overline { { x } } _ { 1 } - \overline { { x } } _ { 2 } } { = } \sqrt { \frac { 2 s _ { e } ^ { 2 } } { n _ { 0 } } } ,$ ，或 $s _ { \overline { { x } } }   =   \sqrt { \frac { S _ { e } ^ { 2 } } { n _ { 0 } } }   \mathrm { { _ { \circ } } }$

例 **7-3** 园艺研究所调查了 3 个品种草莓的维生素 C 含量（mg/100g），测定结果列于表 7-16。试分析不同品种草莓之间维生素 C 含量是否有显著差异。

表 7-16 不同品种草莓维生素 C 含量（mg/100g）

<table><tr><td rowspan="2">处理</td><td colspan="10">维生素C含量</td><td rowspan="2">合计</td><td rowspan="2">平均数</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>I</td><td>117</td><td>99</td><td>107</td><td>112</td><td>113</td><td>106</td><td></td><td></td><td></td><td></td><td>654</td><td>109.0</td></tr><tr><td>II</td><td>81</td><td>77</td><td>79</td><td>76</td><td>85</td><td>87</td><td>74</td><td>69</td><td>72</td><td>80</td><td>780</td><td>78.0</td></tr><tr><td>III</td><td>80</td><td>82</td><td>78</td><td>84</td><td>89</td><td>73</td><td>86</td><td>88</td><td></td><td></td><td>660</td><td>82.5</td></tr></table>

（1）平方和计算:

$$
C = \frac {\left(\sum T _ {i}\right) ^ {2}}{\sum n _ {i}} = \frac {(6 5 4 + 7 8 0 + 6 6 0) ^ {2}}{6 + 1 0 + 8} = 1 8 2 7 0 1. 5
$$

$$
S S _ {T} = \sum x ^ {2} - C = 1 1 7 ^ {2} + 9 9 ^ {2} + \dots + 8 8 ^ {2} - 1 8 2 7 0 1. 5 = 4 5 6 2. 5
$$

$$
S S _ {t} = \sum \frac {T _ {i .} ^ {2}}{n _ {i}} - C = \frac {6 5 4 ^ {2}}{6} + \frac {7 8 0 ^ {2}}{1 0} + \frac {6 6 0 ^ {2}}{8} - 1 8 2 7 0 1. 5 = 3 8 7 4. 5
$$

$$
S S _ {e} = S S _ {T} - S S _ {t} = 4 5 6 2. 5 - 3 8 7 4. 5 = 6 8 8. 0
$$

（2）自由度计算:

$$
d f _ {T} = \sum n _ {i} - 1 = 6 + 1 0 + 8 - 1 = 2 3
$$

$$
d f _ {t} = k - 1 = 3 - 1 = 2
$$

$$
d f _ {e} = d f _ {T} - d f _ {t} = 2 1
$$

（3）列方差分析表（表 7-17）。

表 7-17 不同品种草莓维生素 C 含量方差分析表

| 变异来源 | df | SS | $s^2$ | F | $F_{0.05(2,21)}$ | $F_{0.01(2,21)}$ |
| --- | --- | --- | --- | --- | --- | --- |
| 品种间 | 2 | 3874.5 | 1937.25 | 59.13** | 3.47 | 5.28 |
| 品种内 | 21 | 688.0 | 32.76 |  |  |  |
| 总变异 | 23 | 4562.5 |  |  |  |  |

从表 7-17 方差分析结果可知， $F { \geq } F _ { 0 . 0 1 }$ ，表明 3 个品种草莓维生素 C 含量差异达极显著水平，需要测量关系强度，做进一步的多重比较。

（4）关系强度的测量:

$$
R^2 = \frac{SS_t}{SS_T} = \frac{3874.5}{4562.5} = 84.92\%
$$

表明不同的草莓品种对维生素 C 含量的影响占总效应的 84.92%，而误差效应占 15.08%，其平方根 R 为 92.15%，说明草莓品种与维生素 C 含量间关系极强。

（5）多重比较:进行多重比较时，需要计算 $n _ { 0 } ,$ 并求得 $S _ { \overline { { x } } _ { 1 } - \overline { { x } } _ { 2 } }$ （用于 LSD 检验）或 $s _ { \overline { { x } } }$ （用于 LSR 检验），即

$$
n _ {0} = \frac {\left(\sum n _ {i}\right) ^ {2} - \sum n _ {i} ^ {2}}{\left(\sum n _ {i}\right) (k - 1)} = \frac {2 4 ^ {2} - (6 ^ {2} + 1 0 ^ {2} + 8 ^ {2})}{2 4 \times 2} = 7. 8 \approx 8
$$

本题以 LSD 检验法为例进行多重比较（表 7-18）。

$$
s _ {\overline {{x}} _ {1} - \overline {{x}} _ {2}} = \sqrt {\frac {2 s _ {e} ^ {2}}{n}} = \sqrt {\frac {2 \times 3 2 . 7 6}{8}} = 2. 8 6 2 (\mathrm{mg/100g})
$$

查 t 值表，当误差自由度 $df_{e} = 21$ 时， $t_{0.05} = 2.080,\ t_{0.01} = 2.831$ ，则

$$
L S D _ {0. 0 5} = t _ {0. 0 5} \cdot s _ {\bar {x} _ {1} - \bar {x} _ {2}} = 2. 0 8 0 \times 2. 8 6 2 = 5. 9 5 3 (\mathrm{mg/100g})
$$

$$
L S D _ {0. 0 1} = t _ {0. 0 1} \cdot s _ {\bar {x} _ {1} - \bar {x} _ {2}} = 2. 8 3 1 \times 2. 8 6 2 = 8. 1 0 2 (\mathrm{mg/100g})
$$

表 7-18 不同品种草莓维生素 C 含量的差异显著性（LSD 法）

<table><tr><td rowspan="2">品种</td><td rowspan="2">平均数 $(\bar{x}_i)$ </td><td colspan="2">差异显著性</td></tr><tr><td> $\alpha=0.05$ </td><td> $\alpha=0.01$ </td></tr><tr><td>I</td><td>109.0</td><td>a</td><td>A</td></tr><tr><td>III</td><td>82.5</td><td>b</td><td>B</td></tr><tr><td>II</td><td>78.0</td><td>b</td><td>B</td></tr></table>

多重比较结果表明，品种Ⅰ与品种Ⅲ、品种Ⅱ维生素 C 含量的差异达到极显著水平。品种Ⅲ与品种Ⅱ之间维生素 C 含量差异不显著。

要注意的是，组内不等观测次数的试验要尽量避免，因为这样的试验数据不仅计算麻烦，而且降低了分析的灵敏度。

## 第三节 二因素方差分析

在试验实施中，经常会遇到两个因素共同影响试验结果的情况。二因素试验（two-factor experiment）的方差分析，因素的主效应和因素间的互作都需要考虑。因素间的交互作用显著与否关系到主效应的利用价值，有时互作效应相当大，甚至可以忽略主效应。两个因素间是否存在交互作用可以根据专门的统计方法或专业知识进行判断。

## 一、无重复观测值的二因素方差分析

有些试验，如果依据经验或专业知识能够判断两个因素间无互作时，每个处理可不设重复。假定 A 因素有 a 个水平，B 因素有 b 个水平，每个处理组合只有一个观测值。这种无重复观测值的二因素分组数据模式如表 7-19 所示。

表 7-19 无重复观测值的二因素数据构成

<table><tr><td rowspan="2">因素A</td><td colspan="4">因素B</td><td rowspan="2">总和 $T_{i.}$ </td><td rowspan="2">平均数 $\overline{x}_{i.}$ </td></tr><tr><td> $B_1$ </td><td> $B_2$ </td><td>...</td><td> $B_b$ </td></tr><tr><td> $A_1$ </td><td> $x_{11}$ </td><td> $x_{12}$ </td><td>...</td><td> $x_{1b}$ </td><td> $T_1.$ </td><td> $\overline{x}_1.$ </td></tr><tr><td> $A_2$ </td><td> $x_{21}$ </td><td> $x_{22}$ </td><td>...</td><td> $x_{2b}$ </td><td> $T_2.$ </td><td> $\overline{x}_2.$ </td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td></td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td> $A_a$ </td><td> $x_{a1}$ </td><td> $x_{a2}$ </td><td>...</td><td> $x_{ab}$ </td><td> $T_a.$ </td><td> $\overline{x}_{a.}$ </td></tr><tr><td>总和 $T_{.j}$ </td><td> $T_{.1}$ </td><td> $T_{.2}$ </td><td>...</td><td> $T_{.b}$ </td><td>T</td><td></td></tr><tr><td>平均数 $\overline{x}_{.j}$ </td><td> $\overline{x}_{.1}$ </td><td> $\overline{x}_{.2}$ </td><td>...</td><td> $\overline{x}_{.b}$ </td><td></td><td> $\overline{x}_{..}$ </td></tr></table>

在无重复观测值的二因素试验数据中，A 因素的每一个水平可看成有 b 个重复，B 因素的每一个水平可看成有 $a$ 个重复。每个观测值既受到 A 因素的影响，又受到 B 因素的影响。二因素方差分析的线性模型可以以单因素模型为基础导出。若因素间不存在互作，则二因素方差分析观测值的线性模型为

$$
x _ {i j} = \mu + \alpha_ {i} + \beta_ {j} + \varepsilon_ {i j} \tag {7-27}
$$

式中， $\alpha _ { i }  、  \beta _ { j }$ 分别是 A 因素、B 因素的效应 $(i = 1, 2, \cdots, a; j = 1, 2, \cdots, b)$ ，可以是固定因素，也可以是随机因素，且 $\sum \alpha_{i} = \sum \beta_{j} = 0$ $\varepsilon _ { i j }$ 是随机误差，彼此独立并且服从正态分布 $N \left( 0 , \sigma ^ { 2 } \right)$ 。

（1）平方和分解:

$$
C = \frac {T ^ {2}}{a b}
$$

$$
\left\{ \begin{array}{l} S S _ {T} = \sum \sum (x _ {i j} - \bar {x}) ^ {2} = \sum x _ {i j} ^ {2} - C \\ S S _ {A} = b \sum (\bar {x} _ {i.} - \bar {x}) ^ {2} = \frac {\sum T _ {i .} ^ {2}}{b} - C \\ S S _ {B} = a \sum (\bar {x} _ {. j} - \bar {x}) ^ {2} = \frac {\sum T _ {. j} ^ {2}}{a} - C \\ S S _ {e} = \sum \sum (\bar {x} _ {i j} - \bar {x} _ {i.} - \bar {x} _ {. j} + \bar {x}) ^ {2} = S S _ {T} - S S _ {A} - S S _ {B} \end{array} \right. \tag {7-28}
$$

（2）自由度分解:

$$
\left\{ \begin{array}{l} d f _ {T} = a b - 1 \\ d f _ {A} = a - 1 \\ d f _ {B} = b - 1 \\ d f _ {e} = (a - 1) (b - 1) \end{array} \right. \tag {7-29}
$$

（3）各项方差的计算:

$$
\left\{ \begin{array}{l} s _ {A} ^ {2} = \frac {S S _ {A}}{d f _ {A}} \\ s _ {B} ^ {2} = \frac {S S _ {B}}{d f _ {B}} \\ s _ {e} ^ {2} = \frac {S S _ {e}}{d f _ {e}} \end{array} \right. \tag {7-30}
$$

（4）将以上结果及期望方差列入方差分析表（表 7-20）中。

表 7-20 无重复观测值的二因素方差分析

<table><tr><td rowspan="2">变异来源</td><td rowspan="2">df</td><td rowspan="2">SS</td><td rowspan="2"> $s^2$ </td><td rowspan="2">F</td><td colspan="3">期望方差E( $s^2$ )</td></tr><tr><td>固定模型</td><td>随机模型</td><td>混合模型*</td></tr><tr><td>A因素</td><td>a-1</td><td> $SS_A$ </td><td> $s_A^2$ </td><td> $\frac{s_A^2}{s_e^2}$ </td><td> $\sigma^2 + b\eta_\alpha^2$ </td><td> $\sigma^2 + b\sigma_\alpha^2$ </td><td> $\sigma^2 + b\eta_\alpha^2$ </td></tr><tr><td>B因素</td><td>b-1</td><td> $SS_B$ </td><td> $s_B^2$ </td><td> $\frac{s_B^2}{s_e^2}$ </td><td> $\sigma^2 + a\eta_\beta^2$ </td><td> $\sigma^2 + a\sigma_\beta^2$ </td><td> $\sigma^2 + a\sigma_\beta^2$ </td></tr><tr><td>误差</td><td>(a-1)(b-1)</td><td> $SS_e$ </td><td> $s_e^2$ </td><td></td><td> $\sigma^2$ </td><td> $\sigma^2$ </td><td> $\sigma^2$ </td></tr><tr><td>总变异</td><td>ab-1</td><td> $SS_T$ </td><td></td><td></td><td></td><td></td><td></td></tr></table>

\*A 为固定，B 为随机

例 **7-4** 将一种生长激素配成 $M _ { 1 }$ 、 $M _ { 2 }$ $M _ { 3 }$ $M _ { 4 }$ $M _ { 5 }$ 5 种浓度，并用 $H _ { 1 }$ 、 $H _ { 2 }$ 、 $H _ { 3 }$ 3 种时间浸渍某大豆品种的种子，出苗 45d 后得各处理每一植株的平均干物质重量 $( \mathbf { g } )$ ，结果列于表 7-21。试做方差分析并进行多重比较。

表 7-21 生长激素及浸渍时间对大豆干物质重量（g）的影响

<table><tr><td rowspan="2">浓度(A)</td><td colspan="3">时间(B)</td><td rowspan="2"> $T_{i.}$ </td><td rowspan="2"> $\overline{x}_{i.}$ </td></tr><tr><td> $H_1$ </td><td> $H_2$ </td><td> $H_3$ </td></tr><tr><td> $M_1$ </td><td>13</td><td>14</td><td>14</td><td>41</td><td>13.67</td></tr><tr><td> $M_2$ </td><td>12</td><td>12</td><td>13</td><td>37</td><td>12.33</td></tr><tr><td> $M_3$ </td><td>3</td><td>3</td><td>3</td><td>9</td><td>3.00</td></tr><tr><td> $M_4$ </td><td>10</td><td>9</td><td>10</td><td>29</td><td>9.67</td></tr><tr><td> $M_5$ </td><td>2</td><td>5</td><td>4</td><td>11</td><td>3.67</td></tr><tr><td> $T_{\cdot j}$ </td><td>40</td><td>43</td><td>44</td><td>127</td><td></td></tr><tr><td> $\overline{x}_{\cdot j}$ </td><td>8.0</td><td>8.6</td><td>8.8</td><td></td><td>8.47</td></tr></table>

本例主要研究生长激素和时间的效应，这两个因素均为固定因素，因而 $\alpha _ { i }$ 和 $\beta _ { j }$ 均为固定效应，适应于固定模型。

（1）平方和计算:

$$
C = \frac {T ^ {2}}{a b} = \frac {1 2 7 ^ {2}}{5 \times 3} = 1 0 7 5. 2 7
$$

$$
S S _ {T} = \sum x ^ {2} - C = 1 3 ^ {2} + 1 4 ^ {2} + \dots + 4 ^ {2} - 1 0 7 5. 2 7 = 2 9 5. 7 3
$$

$$
S S _ {A} = \frac {\sum T _ {i .} ^ {2}}{b} - C = \frac {4 1 ^ {2} + 3 7 ^ {2} + \cdots + 1 1 ^ {2}}{3} - 1 0 7 5. 2 7 = 2 8 9. 0 7
$$

$$
S S _ {B} = \frac {\sum T _ {. j} ^ {2}}{a} - C = \frac {4 0 ^ {2} + 4 3 ^ {2} + 4 4 ^ {2}}{5} - 1 0 7 5. 2 7 = 1. 7 3
$$

$$
S S _ {e} = S S _ {T} - S S _ {A} - S S _ {B} = 2 9 5. 7 3 - 2 8 9. 0 7 - 1. 7 3 = 4. 9 3
$$

（2）自由度计算:

$$
d f _ {T} = a b - 1 = 5 \times 3 - 1 = 1 4
$$

$$
d f _ {A} = a - 1 = 5 - 1 = 4
$$

$$
d f _ {B} = b - 1 = 3 - 1 = 2
$$

$$
d f _ {e} = (a - 1) (b - 1) = (5 - 1) \times (3 - 1) = 8
$$

（3）列方差分析表（表 7-22），并进行 $F$ 检验。

表 7-22 例 7-4 生长激素处理对大豆干物质重量影响的方差分析表

| 变异来源 | df | SS | $s^2$ | F | $F_{0.05}$ | $F_{0.01}$ |
| --- | --- | --- | --- | --- | --- | --- |
| 浓度间(A) | 4 | 289.07 | 72.27 | 116.56** | 3.84 | 7.01 |
| 时间间(B) | 2 | 1.73 | 0.87 | 1.40 | 4.46 | 8.65 |
| 误差 | 8 | 4.93 | 0.62 |  |  |  |
| 总变异 | 14 | 295.73 |  |  |  |  |

F 检验结果表明，生长激素处理浓度之间的 F 值大于 $F _ { 0 . 0 1 }$ ，生长激素处理时间之间的 F值未达到显著水平，表明不同生长激素浓度对大豆干物质重量有极显著的影响。

（4）关系强度的测量:例 7-4 的方差分析结果显示，不同浓度处理对大豆干物质重量有极显著影响，这意味着浓度（A 因素）与大豆干物质重量之间的关系是显著的。而浸泡时间（B 因素）与大豆干物质重量之间的关系不显著。那么，两个因素合起来与大豆干物质重量之

间的关系强度是怎样的呢？

表 7-22 给出 $了  A$ A 因素激素浓度的平方和 $( S S _ { A } )$ ）、B 因素浸泡时间的平方和 $( S S _ { B } )$ 、误差平方和 $( S S _ { e } )$ 。将两个因素平方和相加，就度量了两个因素对大豆干物质重量的联合效应；联合效应与总平方和的比值为 $R ^ { 2 }$ ，其平方根 R 值可反映其关系强度:

$$
R ^ {2} = \frac {\text {联合效应}}{\text {总效应}} = \frac {S S _ {A} + S S _ {B}}{S S _ {T}} \tag {7-31}
$$

根据表 7-22 的数据，得

$$
R^{2} = \frac{SS_{A} + SS_{B}}{SS_{T}} = \frac{289.07 + 1.73}{295.73} = 0.9833 = 98.33\%
$$

这表明，激素浓度和浸泡时间两个因素合起来一共解释了大豆干物质增重差异的 98.33%，而误差效应只占了干物质重量差异的1.67%。 $R = 99.16\%$ ，表明两个因素之和与大豆干物质重量之间有极强的关系。

（5）多重比较（SSR 检验）:生长激素处理浓度之间的效应达到了极显著差异，生长激素处理时间之间的效应未达到显著水平，只需对 5 种浸渍浓度进行多重比较。根据式（7-23）可计算出浓度之间的平均数标准误为

$$
s _ {\bar {x}} = \sqrt {\frac {s _ {e} ^ {2}}{b}} = \sqrt {\frac {0 . 6 2}{3}} = 0. 4 5 5 (\mathrm{g})
$$

这里需注意:上式的 $b { = } 3$ 是每一浓度水平下的观测值数目。如果要比较时间之间的效应，则由于每一时间水平下有 $a { = } 5$ 个观测值，其平均数的标准误为 $s_{\bar{x}} = \sqrt{\frac{s_{e}^{2}}{a}} = \sqrt{\frac{0.62}{5}} = 0.352$ $( \mathbf { g } )$ 。查附表 11，当 $d f _ { e } { = } 8$ ，M 为 2、3、4、5 时的 SSR 值及由此计算的 LSR 值列于表 7-23，多重比较结果列于表 7-24。

表 7-23 例 7-4 不同生长激素浓度大豆干物质重量多重比较的 SSR 值和 LSR 值

| M | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- |
| $SSR_{0.05}$ | 3.26 | 3.40 | 3.48 | 3.52 |
| $SSR_{0.01}$ | 4.75 | 4.94 | 5.06 | 5.14 |
| $LSR_{0.05}$ | 1.48 | 1.55 | 1.58 | 1.60 |
| $LSR_{0.01}$ | 2.16 | 2.25 | 2.30 | 2.34 |

表 7-24 例 7-4 不同生长激素浓度大豆干物质重量平均数差异显著性（SSR 法）

<table><tr><td rowspan="2">浓度</td><td rowspan="2">平均数 $(\overline{x}_i)$ </td><td colspan="2">差异显著性</td></tr><tr><td> $\alpha=0.05$ </td><td> $\alpha=0.01$ </td></tr><tr><td> $M_1$ </td><td>13.67</td><td>a</td><td>A</td></tr><tr><td> $M_2$ </td><td>12.33</td><td>a</td><td>A</td></tr><tr><td> $M_4$ </td><td>9.67</td><td>b</td><td>B</td></tr><tr><td> $M_5$ </td><td>3.67</td><td>c</td><td>C</td></tr><tr><td> $M_3$ </td><td>3.00</td><td>c</td><td>C</td></tr></table>

多重比较结果表明:5 种生长激素浓度对大豆干物质重量的影响达到了极显著水平，除

$M _ { 1 }$ 与 M<sub>2</sub>、 $M _ { 5 }$ 与 $M _ { 3 }$ 之间差异不显著外，其他生长激素浓度之间的大豆干物质重量均达到极显著差异。5 种生长激素浓度中，以 $M _ { 1 }$ 和 $M _ { 2 }$ 的处理效果较好。

## 二、具有重复观测值的二因素方差分析

没有重复观测值的二因素试验，估计的误差实际上是这两个因素的相互作用，这是在两个因素不存在互作或互作效应非常小的前提下估计的。但是，如果两个因素间存在互作，在进行方差分析时，就需要将互作项和误差项的平方和与自由度分别解析。因此，进行二因素或多因素试验时，一般应设置重复。

具有重复观测值的二因素试验的典型设计是:假定 A 因素有 $a$ 个水平，B 因素有 b 个水平，则每一次重复都包括 $a b$ 次试验，设试验重复 n 次，则试验总观测次数为 abn 次。具有重复观测值的二因素试验数据模式如表 7-25 所示。

表 7-25 具有重复观测值的二因素数据构成

<table><tr><td rowspan="2">因素A</td><td colspan="4">因素B</td><td rowspan="2"> $T_{i.}$ </td><td rowspan="2"> $\overline{x}_{i.}$ </td></tr><tr><td> $B_1$ </td><td> $B_2$ </td><td>...</td><td> $B_b$ </td></tr><tr><td rowspan="4"> $A_1$ </td><td> $x_{111}$ </td><td> $x_{121}$ </td><td>...</td><td> $x_{1b1}$ </td><td rowspan="4"> $T_1.$ </td><td rowspan="4"> $\overline{x}_{1.}$ </td></tr><tr><td> $x_{112}$ </td><td> $x_{122}$ </td><td>...</td><td> $x_{1b2}$ </td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td></td><td> $\vdots$ </td></tr><tr><td> $x_{11n}$ </td><td> $x_{12n}$ </td><td>...</td><td> $x_{1bn}$ </td></tr><tr><td rowspan="4"> $A_2$ </td><td> $x_{211}$ </td><td> $x_{221}$ </td><td>...</td><td> $x_{2b1}$ </td><td rowspan="4"> $T_2.$ </td><td rowspan="4"> $\overline{x}_{2.}$ </td></tr><tr><td> $x_{212}$ </td><td> $x_{222}$ </td><td>...</td><td> $x_{2b2}$ </td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td></td><td> $\vdots$ </td></tr><tr><td> $x_{21n}$ </td><td> $x_{22n}$ </td><td>...</td><td> $x_{2bn}$ </td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td></td><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td rowspan="4"> $A_a$ </td><td> $x_{a11}$ </td><td> $x_{a21}$ </td><td>...</td><td> $x_{ab1}$ </td><td rowspan="4"> $T_a.$ </td><td rowspan="4"> $\overline{x}_{a.}$ </td></tr><tr><td> $x_{a12}$ </td><td> $x_{a22}$ </td><td>...</td><td> $x_{ab2}$ </td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td></td><td> $\vdots$ </td></tr><tr><td> $x_{a1n}$ </td><td> $x_{a2n}$ </td><td>...</td><td> $x_{abn}$ </td></tr><tr><td> $T_{,j}$ </td><td> $T_{,1}$ </td><td> $T_{,2}$ </td><td>...</td><td> $T_{,b}$ </td><td>T</td><td></td></tr><tr><td> $\overline{x}_{,j}$ </td><td> $\overline{x}_{,1}$ </td><td> $\overline{x}_{,2}$ </td><td>...</td><td> $\overline{x}_{,b}$ </td><td></td><td> $\overline{x}.$ </td></tr></table>

具有重复观测值的二因素方差分析可用下面的线性模型来描述:

$$
x _ {i j k} = \mu + \alpha_ {i} + \beta_ {j} + (\alpha \beta) _ {i j} + \varepsilon_ {i j k} \tag {7-32}
$$

式中， $x _ { i j k }$ 为 $A$ 因素第 i 水平、B 因素第 $j$ 水平的第 k 次重复观测值 $(i = 1,2,\cdots,a;j = 1,2,\cdots,$ $b; k = 1, 2, \cdots, n$ ； $\mu$ 为总体平均值； $a _ { i }$ 为 A 因素第 i 水平的效应， $\beta _ { j }$ 为 $B$ 因素第 j 水平的效应； $( \alpha \beta ) _ { i j }$ 为 $a _ { i }$ 和 $\beta _ { j }$ 的交互作用，且有 $\sum \alpha_{i}=\sum \beta_{j}=\sum(\alpha \beta)_{ij}=0;$ ； $\varepsilon _ { i j k }$ 为随机误差，彼此独立且服从 $N \left( 0 , \sigma ^ { 2 } \right)$ 。

具有重复观测值的二因素方差分析，步骤和前面介绍的类似，不同的是 F 检验的方法。

（1）平方和计算:

$$
C = \frac {T ^ {2}}{a b n}
$$

$$
\left\{ \begin{array}{l} S S _ {T} = \sum \sum \sum (x _ {i j k} - \bar {x}) ^ {2} = \sum x ^ {2} - C \\ S S _ {A} = b n \sum (\bar {x} _ {i.} - \bar {x}) ^ {2} = \frac {\sum T _ {i .} ^ {2}}{b n} - C \\ S S _ {B} = a n \sum (\bar {x}. _ {j} - \bar {x}) ^ {2} = \frac {\sum T _ {. j} ^ {2}}{a n} - C \\ S S _ {A B} = n \sum \sum (\bar {x} _ {i j} - \bar {x} _ {i.} - \bar {x}. _ {j} + \bar {x}) ^ {2} \\ = \frac {\sum T _ {i j} ^ {2}}{n} - C - S S _ {A} - S S _ {B} \\ S S _ {e} = S S _ {T} - S S _ {A} - S S _ {B} - S S _ {A B} \end{array} \right. \tag {7-33}
$$

（2）自由度计算:

$$
\left\{ \begin{array}{l} d f _ {T} = a b n - 1 \\ d f _ {A} = a - 1 \\ d f _ {B} = b - 1 \\ d f _ {A B} = (a - 1) (b - 1) \\ d f _ {e} = a b (n - 1) \end{array} \right. \tag {7-34}
$$

（3）各项方差的计算:

$$
\left\{ \begin{array}{l} s _ {A} ^ {2} = \frac {S S _ {A}}{d f _ {A}} \\ s _ {B} ^ {2} = \frac {S S _ {B}}{d f _ {B}} \\ s _ {A B} ^ {2} = \frac {S S _ {A B}}{d f _ {A B}} \\ s _ {e} ^ {2} = \frac {S S _ {e}}{d f _ {e}} \end{array} \right. \tag {7-35}
$$

（4）F 检验。

A.固定模型:在固定模型中， $\alpha _ { i }  、  \beta _ { j }$ 及 $( \alpha \beta ) _ { i j }$ 均为固定效应。在 F 检验时，检验 A 因素、B 因素和 $A   \times   B$ 互作项均以 $s _ { e } ^ { 2 }$ 作为分母。
B.随机模型:对于随机模型， $\alpha _ { i } , \beta _ { j } , ( \alpha \beta ) _ { i j }$ 和 $\varepsilon _ { i j k }$ 是相互独立的随机变量，都服从正态分布。做 F 检验，检验 $A   \times   B$ 互作时，F 值为

$$
F _ {A B} = \frac {s _ {A B} ^ {2}}{s _ {e} ^ {2}} \tag {7-36}
$$

检验 A 因素、B 因素时，F 值为

$$
\left\{ \begin{array}{l} F _ {A} = \frac {s _ {A} ^ {2}}{s _ {A B} ^ {2}} \\ F _ {B} = \frac {s _ {B} ^ {2}}{s _ {A B} ^ {2}} \end{array} \right. \tag {7-37}
$$

C.混合模型（以 A 为固定因素、B 为随机因素为例）:在混合模型中，A 和 B 的效应为非可加性， $a _ { i }$ 为固定效应， $\beta _ { j }$ 及 $( \alpha \beta ) _ { i j }$ 为随机效应。对固定因素（A）做检验时同随机模型，对随机因素 $(B, A \times B)$ 做检验时同固定模型，即

$$
\left\{ \begin{array}{l} F _ {A} = \frac {s _ {A} ^ {2}}{s _ {A B} ^ {2}} \\ F _ {B} = \frac {s _ {B} ^ {2}}{s _ {e} ^ {2}} \\ F _ {A B} = \frac {s _ {A B} ^ {2}}{s _ {e} ^ {2}} \end{array} \right. \tag {7-38}
$$

为了便于比较，将 3 种模型的方差分析列于表 7-26。

表 7-26 有重复观测值的二因素资料方差分析表

<table><tr><td colspan="2">变异来源</td><td colspan="2">SS</td><td colspan="2">df</td><td colspan="2"> $s^2$ </td></tr><tr><td colspan="2">因素A</td><td colspan="2"> $SS_A$ </td><td colspan="2">a-1</td><td colspan="2"> $s_A^2$ </td></tr><tr><td colspan="2">因素B</td><td colspan="2"> $SS_B$ </td><td colspan="2">b-1</td><td colspan="2"> $s_B^2$ </td></tr><tr><td colspan="2">A×B</td><td colspan="2"> $SS_{AB}$ </td><td colspan="2">(a-1)(b-1)</td><td colspan="2"> $s_{AB}^2$ </td></tr><tr><td colspan="2">误差</td><td colspan="2"> $SS_e$ </td><td colspan="2">ab(n-1)</td><td colspan="2"> $s_e^2$ </td></tr><tr><td colspan="2">总变异</td><td colspan="2"> $SS_T$ </td><td colspan="2">abn-1</td><td colspan="2"></td></tr><tr><td rowspan="2">变异来源</td><td colspan="2">固定模型</td><td colspan="2">随机模型</td><td colspan="3">混合模型(A固定,B随机)</td></tr><tr><td>F</td><td>期望方差</td><td>F</td><td>期望方差</td><td>F</td><td colspan="2">期望方差</td></tr><tr><td>因素A</td><td> $\frac{s_A^2}{s_e^2}$ </td><td> $\sigma^2 + bnn_\alpha^2$ </td><td> $\frac{s_A^2}{s_{AB}^2}$ </td><td> $\sigma^2 + n\sigma_{\alpha\beta}^2 + bn\sigma_\alpha^2$ </td><td> $\frac{s_A^2}{s_{AB}^2}$ </td><td colspan="2"> $\sigma^2 + n\sigma_{\alpha\beta}^2 + bnn_\alpha^2$ </td></tr><tr><td>因素B</td><td> $\frac{s_B^2}{s_e^2}$ </td><td> $\sigma^2 + ann_\beta^2$ </td><td> $\frac{s_B^2}{s_{AB}^2}$ </td><td> $\sigma^2 + n\sigma_{\alpha\beta}^2 + an\sigma_\beta^2$ </td><td> $\frac{s_B^2}{s_e^2}$ </td><td colspan="2"> $\sigma^2 + an\sigma_\beta^2$ </td></tr><tr><td>A×B</td><td> $\frac{s_{AB}^2}{s_e^2}$ </td><td> $\sigma^2 + nn_\alpha\beta^2$ </td><td> $\frac{s_{AB}^2}{s_e^2}$ </td><td> $\sigma^2 + n\sigma_{\alpha\beta}^2$ </td><td> $\frac{s_{AB}^2}{s_e^2}$ </td><td colspan="2"> $\sigma^2 + n\sigma_{\alpha\beta}^2$ </td></tr><tr><td>误差</td><td></td><td> $\sigma^2$ </td><td></td><td> $\sigma^2$ </td><td></td><td colspan="2"> $\sigma^2$ </td></tr></table>

在生物学及其相关学科实际应用中，固定模型应用最多，随机模型和混合模型相对较少。

例 **7-5** 为了研究某种昆虫滞育期长短与环境的关系，在给定的温度和光照条件下进行实验室培养，每一处理记录 4 只昆虫的滞育天数，结果列于表 7-27。试对该数据进行方差分析。

表 7-27 不同温度及光照条件下某种昆虫滞育天数（d）

<table><tr><td rowspan="2">光照(A)</td><td colspan="3">温度(B)</td></tr><tr><td>25°C</td><td>30°C</td><td>35°C</td></tr><tr><td rowspan="4">5h/d</td><td>143</td><td>101</td><td>89</td></tr><tr><td>138</td><td>100</td><td>93</td></tr><tr><td>120</td><td>80</td><td>101</td></tr><tr><td>107</td><td>83</td><td>76</td></tr><tr><td rowspan="4">10h/d</td><td>96</td><td>79</td><td>80</td></tr><tr><td>103</td><td>61</td><td>76</td></tr><tr><td>78</td><td>83</td><td>61</td></tr><tr><td>91</td><td>59</td><td>67</td></tr><tr><td rowspan="4">15h/d</td><td>79</td><td>60</td><td>67</td></tr><tr><td>83</td><td>71</td><td>58</td></tr><tr><td>96</td><td>78</td><td>71</td></tr><tr><td>98</td><td>64</td><td>83</td></tr></table>

本例中，由于温度和光照条件都是人为控制的，均为固定因素，可依固定模型分析。为便于展示，将表 7-27 中的数字均减去 80，并整理于表 7-28 中。

表 7-28 例 7-5 昆虫滞育天数数据整理表（d）

<table><tr><td rowspan="2">光照(A)</td><td rowspan="2">标本</td><td colspan="3">温度(B)</td><td rowspan="2"> $T_{i.}$ </td></tr><tr><td>25°C</td><td>30°C</td><td>35°C</td></tr><tr><td rowspan="5">5h/d</td><td>1</td><td>63</td><td>21</td><td>9</td><td rowspan="5">271</td></tr><tr><td>2</td><td>58</td><td>20</td><td>13</td></tr><tr><td>3</td><td>40</td><td>0</td><td>21</td></tr><tr><td>4</td><td>27</td><td>3</td><td>-4</td></tr><tr><td> $T_{ij}$ </td><td>188</td><td>44</td><td>39</td></tr><tr><td rowspan="5">10h/d</td><td>1</td><td>16</td><td>-1</td><td>0</td><td rowspan="5">-26</td></tr><tr><td>2</td><td>23</td><td>-19</td><td>-4</td></tr><tr><td>3</td><td>-2</td><td>3</td><td>-19</td></tr><tr><td>4</td><td>11</td><td>-21</td><td>-13</td></tr><tr><td> $T_{ij}$ </td><td>48</td><td>-38</td><td>-36</td></tr><tr><td rowspan="5">15h/d</td><td>1</td><td>-1</td><td>-20</td><td>-13</td><td rowspan="5">-52</td></tr><tr><td>2</td><td>3</td><td>-9</td><td>-22</td></tr><tr><td>3</td><td>16</td><td>-2</td><td>-9</td></tr><tr><td>4</td><td>18</td><td>-16</td><td>3</td></tr><tr><td> $T_{ij}$ </td><td>36</td><td>-47</td><td>-41</td></tr><tr><td colspan="2"> $T_{j}$ </td><td>272</td><td>-41</td><td>-38</td><td>T=193</td></tr></table>

平方和与自由度的分解:

$$
C = \frac {T ^ {2}}{a b n} = \frac {1 9 3 ^ {2}}{3 \times 3 \times 4} = 1 0 3 4. 6 9
$$

$$
S S _ {T} = \sum x ^ {2} - C = (6 3 ^ {2} + 5 8 ^ {2} + \dots + 3 ^ {2}) - 1 0 3 4. 6 9 = 1 4 5 2 6. 3 1
$$

$$
S S _ {A} = \frac {\sum T _ {i .} ^ {2}}{b n} - C = \frac {2 7 1 ^ {2} + (- 2 6) ^ {2} + (- 5 2) ^ {2}}{3 \times 4} - 1 0 3 4. 6 9 = 5 3 6 7. 0 6
$$

$$
S S _ {B} = \frac {\sum T _ {. j} ^ {2}}{a n} - C = \frac {2 7 2 ^ {2} + (- 4 1) ^ {2} + (- 3 8) ^ {2}}{3 \times 4} - 1 0 3 4. 6 9 = 5 3 9 1. 0 6
$$

$$
\begin{array}{l} S S _ {A B} = \frac {\sum T _ {i j} ^ {2}}{n} - C - S S _ {A} - S S _ {B} \\ = \frac {1 8 8 ^ {2} + 4 4 ^ {2} + \cdots + (- 4 1) ^ {2}}{4} - 1 0 3 4. 6 9 - 5 3 6 7. 0 6 - 5 3 9 1. 0 6 = 4 6 4. 9 4 \\ \end{array}
$$

$$
\begin{array}{l} S S _ {e} = S S _ {T} - S S _ {A} - S S _ {B} - S S _ {A B} \\ = 1 4 5 2 6. 3 1 - 5 3 6 7. 0 6 - 5 3 9 1. 0 6 - 4 6 4. 9 4 = 3 3 0 3. 2 5 \\ d f _ {T} = a b n - 1 = 3 \times 3 \times 4 - 1 = 3 5 \\ d f _ {A} = a - 1 = 3 - 1 = 2 \\ d f _ {B} = b - 1 = 3 - 1 = 2 \\ d f _ {A B} = (a - 1) (b - 1) = (3 - 1) \times (3 - 1) = 4 \\ d f _ {e} = a b (n - 1) = 3 \times 3 \times (4 - 1) = 2 7 \\ \end{array}
$$

将上述结果列入方差分析表（表 7-29）。从表 7-29 可以看出，不同光照和温度间的差异均达到了极显著，即昆虫滞育期长短主要取决于光照和温度，而与两者之间互作关系不大。

表 7-29 例 7-4 昆虫滞育天数数据方差分析表

| 变异来源 | df | SS | $s^2$ | F | $F_{0.05}$ | $F_{0.01}$ |
| --- | --- | --- | --- | --- | --- | --- |
| 光照间 | 2 | 5367.06 | 2683.53 | 21.93** | 3.35 | 5.49 |
| 温度间 | 2 | 5391.06 | 2695.53 | 22.03** | 3.35 | 5.49 |
| 光照×温度 | 4 | 464.94 | 116.24 | 0.95 | 2.73 | 4.11 |
| 误差 | 27 | 3303.25 | 122.34 |  |  |  |
| 总变异 | 35 | 14526.31 |  |  |  |  |

要了解各种光照时间及温度对滞育期的影响，需进行不同光照之间及不同温度之间的多重比较，其方法可参照前面例子进行。其平均数标准误的计算为:光照（A）间平均数标准误 $s _ { \overline { { x } } } { = } \sqrt { \frac { S _ { e } ^ { 2 } } { b n } }$ ；温度（B）间平均数标准误 $s _ { \overline { { x } } } { = } \sqrt { \frac { S _ { e } ^ { 2 } } { a n } }$

例 **7-6** 用大麦生产啤酒过程中，需要研究烘烤方式（A）与大麦水分（B）对糖化时间的影响，选择 2 种烘烤方式、4 种大麦水分，共 8 种处理，每一处理重复 3 次，结果列于表 7-30。

表 7-30 不同烘烤方式及大麦水分对糖化时间（h）的影响

<table><tr><td rowspan="2">烘烤方式(A)</td><td colspan="4">水分(B)</td></tr><tr><td> $B_1$ </td><td> $B_2$ </td><td> $B_3$ </td><td> $B_4$ </td></tr><tr><td rowspan="3"> $A_1$ </td><td>12.0</td><td>9.5</td><td>16.0</td><td>18.0</td></tr><tr><td>13.0</td><td>10.0</td><td>15.5</td><td>19.0</td></tr><tr><td>14.5</td><td>12.5</td><td>14.0</td><td>17.0</td></tr><tr><td rowspan="3"> $A_2$ </td><td>5.0</td><td>13.0</td><td>17.5</td><td>15.0</td></tr><tr><td>6.5</td><td>14.0</td><td>18.5</td><td>16.0</td></tr><tr><td>5.5</td><td>15.0</td><td>16.0</td><td>17.5</td></tr></table>

本例中，烘烤方式这一因素是固定因素，大麦水分是不均匀的，又不易控制，所以该因素是随机因素，其效应也是随机的。由此可见，本题应采用混合模型进行方差分析。将表 7-30中各观测值都减去 10，整理后的数据列于表 7-31。

表 7-31 糖化时间数据整理表

<table><tr><td rowspan="2">烘烤方式(A)</td><td rowspan="2">标本号</td><td colspan="4">温度(B)</td><td rowspan="2"> $T_{i.}$ </td></tr><tr><td> $B_1$ </td><td> $B_2$ </td><td> $B_3$ </td><td> $B_4$ </td></tr><tr><td rowspan="4"> $A_1$ </td><td>1</td><td>2.0</td><td>-0.5</td><td>6.0</td><td>8.0</td><td rowspan="4">51.0</td></tr><tr><td>2</td><td>3.0</td><td>0.0</td><td>5.5</td><td>9.0</td></tr><tr><td>3</td><td>4.5</td><td>2.5</td><td>4.0</td><td>7.0</td></tr><tr><td> $T_{ij}$ </td><td>9.5</td><td>2.0</td><td>15.5</td><td>24.0</td></tr><tr><td rowspan="4"> $A_2$ </td><td>1</td><td>-5.0</td><td>3.0</td><td>7.5</td><td>5.0</td><td rowspan="4">39.5</td></tr><tr><td>2</td><td>-3.5</td><td>4.0</td><td>8.5</td><td>6.0</td></tr><tr><td>3</td><td>-4.5</td><td>5.0</td><td>6.0</td><td>7.5</td></tr><tr><td> $T_{ij}$ </td><td>-13.0</td><td>12.0</td><td>22.0</td><td>18.5</td></tr><tr><td colspan="2"> $T_{.j}$ </td><td>-3.5</td><td>14.0</td><td>37.5</td><td>42.5</td><td>T=90.5</td></tr></table>

（1）平方和与自由度的分解:

$$
C = \frac {T ^ {2}}{a b n} = \frac {9 0 . 5 ^ {2}}{2 \times 4 \times 3} = 3 4 1. 2 6
$$

$$
S S _ {T} = \sum x ^ {2} - C = 2. 0 ^ {2} + (- 0. 5) ^ {2} + \dots + 7. 5 ^ {2} - 3 4 1. 2 6 = 3 6 3. 9 9
$$

$$
S S _ {A} = \frac {\sum T _ {i .} ^ {2}}{b n} - C = \frac {5 1 . 0 ^ {2} + 3 9 . 5 ^ {2}}{4 \times 3} - 3 4 1. 2 6 = 5. 5 1 1
$$

$$
S S _ {B} = \frac {\sum T _ {. j} ^ {2}}{a n} - C = \frac {(- 3 . 5) ^ {2} + 1 4 ^ {2} + \cdots + 4 2 . 5 ^ {2}}{2 \times 3} - 3 4 1. 2 6 = 2 2 8. 8 6 5
$$

$$
S S _ {A B} = \frac {\sum T _ {i j} ^ {2}}{n} - C - S S _ {A} - S S _ {B}
$$

$$
= \frac {9 . 5 ^ {2} + 2 . 0 ^ {2} + \cdots + 1 8 . 5 ^ {2}}{3} - 3 4 1. 2 6 - 5. 5 1 1 - 2 2 8. 8 6 5 = 1 0 7. 6 1 4
$$

$$
S S _ {e} = S S _ {T} - S S _ {A} - S S _ {B} - S S _ {A B}
$$

$$
= 3 6 3. 9 9 - 5. 5 1 1 - 2 2 8. 8 6 5 - 1 0 7. 6 1 4 = 2 2. 0 0 0
$$

$$
d f _ {T} = a b n - 1 = 2 \times 4 \times 3 - 1 = 2 3
$$

$$
d f _ {A} = a - 1 = 2 - 1 = 1
$$

$$
d f _ {B} = b - 1 = 4 - 1 = 3
$$

$$
d f _ {A B} = (a - 1) (b - 1) = (2 - 1) \times (4 - 1) = 3
$$

$$
d f _ {e} = a b (n - 1) = 2 \times 4 \times (3 - 1) = 1 6
$$

（2）计算 F 值:

$$
F _ {A} = \frac {s _ {A} ^ {2}}{s _ {A B} ^ {2}} = \frac {5 . 5 1 1}{3 5 . 8 7 2} = 0. 1 5 4
$$

$$
F _ {B} = \frac {s _ {B} ^ {2}}{s _ {e} ^ {2}} = \frac {7 6 . 2 8 8}{1 . 3 7 5} = 5 5. 4 8 2
$$

$$
F _ {A B} = \frac {s _ {A B} ^ {2}}{s _ {e} ^ {2}} = \frac {3 5 . 8 7 2}{1 . 3 7 5} = 2 6. 0 8 9
$$

## （3）列出方差分析表并进行 F 检验（表 7-32）。

表 7-32 糖化时间方差分析表

| 变异来源 | df | SS | $s^2$ | F | $F_{0.05}$ | $F_{0.01}$ |
| --- | --- | --- | --- | --- | --- | --- |
| 烘烤方式(A) | 1 | 5.511 | 5.511 | 0.154 | 10.13 | 34.12 |
| 水分(B) | 3 | 228.865 | 76.288 | 55.482** | 3.24 | 5.29 |
| A×B | 3 | 107.614 | 35.872 | 26.089** | 3.24 | 5.29 |
| 误差 | 16 | 22.000 | 1.375 |  |  |  |
| 总变异 | 23 | 363.990 |  |  |  |  |

由表 7-32 可以看出，大麦中的水分及水分与烘烤方式之间的互作对糖化时间的影响达到了极显著水平，而烘烤方式对糖化时间的作用则不显著。在生产中应注意大麦的含水量及根据含水量来选择合适的烘烤方式。

由本例可以看出，由于 $S S _ { A B }$ 一般要大于 $S S _ { e }$ ，尤其是在互作存在时 $S S _ { A B }$ 更是显著地偏大，因此若不注意区分是随机因素还是固定因素，就有可能错用统计量，导致错误的结论。因此在两个以上因素的方差分析中，区分因素类型更为重要。

在随机模型和混合模型中，如果不设重复，同样无法把 $S S _ { A B }$ 与 $S S _ { e }$ 分开，此时随机模型仍可对主效应进行检验，混合模型中也可以对固定因素的主效应进行检验。如果互作存在，仅检验主效应是没有太大意义的，因为很可能是互作在起主要作用。因此只要条件许可，无论哪一类模型都应尽可能设置重复，除非有可靠的证据证明互作不存在。

## 第四节 多因素方差分析

科研工作中，往往需要考察三个或多个因素的效应。这相当于把二因素方差分析扩展到一般情况。多因素方差分析的方法，本节仅对三因素的情况进行分析。设 A 因素有 a 个水平、B 因素有 b 个水平、C 因素有 c 个水平，假设每一处理都有 n 次重复，那么总观测次数为 abcn次。对观测值 $x _ { i j k l }$ ，这个三因素方差分析的线性数学模型为

$$
x _ {i j k l} = \mu + \alpha_ {i} + \beta_ {j} + \gamma_ {k} + (\alpha \beta) _ {i j} + (\alpha \gamma) _ {i k} + (\beta \gamma) _ {j k} + (\alpha \beta \gamma) _ {i j k} + \varepsilon_ {i j k l} \tag {7-39}
$$

式中， $x _ { i j k l }$ 为 A 因素第 i 水平、B 因素第 j 水平、C 因素第 k 水平的第 l 次重复观测值（其中 $i = 1, 2, \cdots, a; j = 1, 2, \cdots, b; k = 1, 2, \cdots, c; l = 1, 2, \cdots, n)$ ； $\mu$ 为总体平均值； $\alpha _ { i }$ 为 A 因素第 i 水平的效应； $\beta _ { j }$ 为 B 因素第 j 水平的效应， $\gamma _ { k }$ 为 $C$ 因素第 k 水平的效应； $( \alpha \beta ) _ { i j } , ( \alpha \gamma ) _ { i k }$ 和 $( \beta \gamma ) _ { \textit { j k } }$ 分别为 $A \times B 、 A \times C$ 和 $B   \times   C$ 的交互效应， $(   \alpha \beta \gamma   ) _ { \; i j k }$ 为 $A \times$ $B   \times   C$ 的交互效应； $\varepsilon _ { i j k l }$ 为随机误差。同时，应满足以下条件:① $\sum \alpha_{i} = \sum \beta_{j} = \sum \gamma_{k} = 0;$ $\sum \left( \alpha \beta \right)_{ij} = \sum \left( \alpha \gamma \right)_{ik} = \sum \left( \beta \gamma \right)_{jk} = 0; \quad \textcircled{s} \sum \left( \alpha \beta \gamma \right)_{ijkl} = 0; \quad \textcircled{4} \varepsilon_{ijkl}$ 为随机误差，彼此独立且服从$N \left( 0 , \sigma ^ { 2 } \right)$

实际分析时，可将三因素方差分析转化成 3 个二因素方差分析，列出 3 个两向表。例如，把 A、B 条件下的全部结果列成一个两向表，如表 7-33 所示。