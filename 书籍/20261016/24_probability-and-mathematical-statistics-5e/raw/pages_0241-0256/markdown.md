$$
\frac {\sum_ {i = 1} ^ {n _ {j}} (X _ {i j} - \overline {{X}} _ {. j}) ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n _ {j} - 1).
$$

因各 $X_{ij}$ 相互独立，故(1.11)式中各平方和相互独立.由 $\chi^2$ 分布的可加性知

$$
\frac {S _ {E}}{\sigma^ {2}} \sim \chi^ {2} \Big (\sum_ {j = 1} ^ {s} (n _ {j} - 1) \Big),
$$

即 $\frac{S_E}{\sigma^2} \sim \chi^2 (n - s),$ (1.12)

这里 $n = \sum_{j=1}^{s} n_j$. 由(1.12)式还可知, $S_E$ 的自由度为 $n - s$, 且有

$$
E (S _ {E}) = (n - s) \sigma^ {2}. \tag {1.13}
$$

下面讨论  $S_{A}$  的统计特性, 我们看到  $S_{A}$  是 s 个变量  $\sqrt{n_{j}}(\overline{X}_{.j}-\overline{X})$  (j=1,  $2,\cdots,s$ ) 的平方和, 它们之间仅有一个线性约束条件

$$
\sum_ {j = 1} ^ {s} \sqrt {n _ {j}} \big [ \sqrt {n _ {j}} (\overline {{X}} _ {. j} - \overline {{X}}) \big ] = \sum_ {j = 1} ^ {s} n _ {j} (\overline {{X}} _ {. j} - \overline {{X}}) = \sum_ {j = 1} ^ {s} \sum_ {i = 1} ^ {n _ {j}} X _ {i j} - n \overline {{X}} = 0,
$$

故知  $S_{A}$  的自由度是 s-1.

再由(1.3)，(1.6)式及 $X_{ij}$ 的独立性，知

$$
\overline {{X}} \sim N \Big (\mu , \frac {\sigma^ {2}}{n} \Big). \tag {1.14}
$$

即得

$$
\begin{array}{l} E (S _ {A}) = E \left[ \sum_ {j = 1} ^ {s} n _ {j} \overline {{X}} _ {. j} ^ {2} - n \overline {{X}} ^ {2} \right] = \sum_ {j = 1} ^ {s} n _ {j} E (\overline {{X}} _ {. j} ^ {2}) - n E (\overline {{X}} ^ {2}) \\ = \sum_ {j = 1} ^ {s} n _ {j} \left[ \frac {\sigma^ {2}}{n _ {j}} + (\mu + \delta_ {j}) ^ {2} \right] - n \left(\frac {\sigma^ {2}}{n} + \mu^ {2}\right) \\ = (s - 1) \sigma^ {2} + 2 \mu \sum_ {j = 1} ^ {s} n _ {j} \delta_ {j} + n \mu^ {2} + \sum_ {j = 1} ^ {s} n _ {j} \delta_ {j} ^ {2} - n \mu^ {2}. \\ \end{array}
$$

由(1.1) $^{\prime}$ 式 $\sum_{j=1}^{s}n_{j}\delta_{j}=0$ ，故有

$$
E (S _ {A}) = (s - 1) \sigma^ {2} + \sum_ {j = 1} ^ {s} n _ {j} \delta_ {j} ^ {2}. \tag {1.15}
$$

进一步还可以证明 $S_A$ 与 $S_E$ 独立，且当 $H_0$ 为真时

$$
\frac {S _ {A}}{\sigma^ {2}} \sim \chi^ {2} (s - 1). \tag {1.16}
$$

(证略.)

## （四）假设检验问题的拒绝域

现在我们可以来确定假设检验问题(1.2)'的拒绝域了.

由(1.15)式知, 当  $H_{0}$  为真时

$$
E \left(\frac {S _ {A}}{s - 1}\right) = \sigma^ {2}, \tag {1.17}
$$

即 $\frac{S_A}{s - 1}$ 是 $\sigma^2$ 的无偏估计. 而当 $H_{1}$ 为真时, $\sum_{j=1}^{s} n_j \delta_j^2 > 0$, 此时

$$
E \left(\frac {S _ {A}}{s - 1}\right) = \sigma^ {2} + \frac {1}{s - 1} \sum_ {j = 1} ^ {s} n _ {j} \delta_ {j} ^ {2} > \sigma^ {2}. \tag {1.18}
$$

又由(1.13)知，

$$
E \left(\frac {S _ {E}}{n - s}\right) = \sigma^ {2}, \tag {1.19}
$$

即不管 $H_0$ 是否为真，$\frac{S_E}{n - s}$ 都是 $\sigma^2$ 的无偏估计.

综上所述，分式 $F = \frac{S_A / (s - 1)}{S_E / (n - s)}$ 的分子与分母独立，分母 $\frac{S_E}{n - s}$ 不论 $H_0$ 是否为真，其数学期望总是 $\sigma^2$。当 $H_0$ 为真时，分子的数学期望为 $\sigma^2$，当 $H_0$ 不真时，由(1.18)式分子的取值有偏大的趋势。故知检验问题(1.2)'的拒绝域具有形式

$$
F = \frac {S _ {A} / (s - 1)}{S _ {E} / (n - s)} \geqslant k,
$$

其中 $k$ 由预先给定的显著性水平 $\alpha$ 确定. 由(1.12)，(1.16)式及 $S_{E}$ 与 $S_{A}$ 的独立性知，当 $H_0$ 为真时，

$$
\frac {S _ {A} / (s - 1)}{S _ {E} / (n - s)} = \frac {S _ {A} / \sigma^ {2}}{s - 1} \Big / \frac {S _ {E} / \sigma^ {2}}{n - s} \sim F (s - 1, n - s).
$$

由此得检验问题(1.2) $^{'}$ 的拒绝域为

$$
F = \frac {S _ {A} / (s - 1)}{S _ {E} / (n - s)} \geqslant F _ {\alpha} (s - 1, n - s). \tag {1.20}
$$

上述分析的结果可排成表 9-5 的形式, 称为方差分析表.

表 9-5 单因素试验的方差分析表

| 方差来源 | 平方和 | 自由度 | 均方 | F比 |
| --- | --- | --- | --- | --- |
| 因素A | $S_A$ | s-1 | $\overline{S}_A = \frac{S_A}{s-1}$ | $F = \frac{\overline{S}_A}{\overline{S}_E}$ |
| 误差 | $S_E$ | n-s | $\overline{S}_E = \frac{S_E}{n-s}$ |  |
| 总和 | $S_T$ | n-1 |  |  |

表中 $\overline{S}_A = S_A / (s - 1),\overline{S}_E = S_E / (n - s)$ 分别称为 $S_{A},S_{E}$ 的均方.另外，因在$S_{T}$ 中 $n$ 个变量 $X_{ij} - \overline{X}$ 之间仅满足一个约束条件(1.6)，故 $S_{T}$ 的自由度为 $n - 1$

在实际中,我们可以按以下较简便的公式来计算  $S_{T}, S_{A}$  和  $S_{E}$ .

记 $T_{.j} = \sum_{i=1}^{n_j} X_{ij}, j = 1,2,\cdots,s,\quad T_{..} = \sum_{j=1}^{s} \sum_{i=1}^{n_j} X_{ij},$

即有

$$
\begin{array}{l} S _ {T} = \sum_ {j = 1} ^ {s} \sum_ {i = 1} ^ {n _ {j}} X _ {i j} ^ {2} - n \overline {{X}} ^ {2} = \sum_ {j = 1} ^ {s} \sum_ {i = 1} ^ {n _ {j}} X _ {i j} ^ {2} - \frac {T _ {\cdot \cdot} ^ {2}}{n}, \\ S _ {A} = \sum_ {j = 1} ^ {s} n _ {j} \overline {{X}} _ {\cdot j} ^ {2} - n \overline {{X}} ^ {2} = \sum_ {j = 1} ^ {s} \frac {T _ {\cdot j} ^ {2}}{n _ {j}} - \frac {T _ {\cdot \cdot} ^ {2}}{n}, \\ S _ {E} = S _ {T} - S _ {A}. \end{array} \tag {1.21}
$$

例 4 设在例 1 中符合模型(1.1) 条件, 检验假设( $\alpha = 0.05$ ):

$$
H _ {0}: \mu_ {1} = \mu_ {2} = \mu_ {3},
$$

$H_{1}:\mu_{1},\mu_{2},\mu_{3}$ 不全相等.

解 现在 $s = 3, n_1 = n_2 = n_3 = 5, n = 15,$

$$
\begin{array}{l} S _ {T} = \sum_ {j = 1} ^ {3} \sum_ {i = 1} ^ {5} X _ {i j} ^ {2} - \frac {T _ {. .} ^ {2}}{1 5} = 0. 9 6 3 9 1 2 - \frac {3 . 8 ^ {2}}{1 5} = 0. 0 0 1 2 4 5 3 3, \\ S _ {A} = \sum_ {j = 1} ^ {3} \frac {T _ {. j} ^ {2}}{n _ {j}} - \frac {T _ {. .} ^ {2}}{n} = \frac {1}{5} (1. 2 1 ^ {2} + 1. 2 8 ^ {2} + 1. 3 1 ^ {2}) - \frac {3 . 8 ^ {2}}{1 5} \\ = 0. 0 0 1 0 5 3 3 3, \\ S _ {E} ^ {\cdot} = S _ {T} - S _ {A} = 0. 0 0 0 1 9 2. \\ \end{array}
$$

$S_{T}, S_{A}, S_{E}$ 的自由度依次为 $n - 1 = 14, s - 1 = 2, n - s = 12$，得方差分析表如表9-6所示:

表 9-6 例 4 的方差分析表

| 方差来源 | 平方和 | 自由度 | 均方 | F比 |
| --- | --- | --- | --- | --- |
| 因素 | 0.001 053 33 | 2 | 0.000 526 67 | 32.92 |
| 误差 | 0.000 192 | 12 | 0.000 016 |  |
| 总和 | 0.001 245 33 | 14 |  |  |

因 $F_{0.05}(2,12) = 3.89 < 32.92$ ，故在显著性水平0.05下拒绝 $H_0$ ，认为各台机器生产的薄板厚度有显著的差异. □

## (五) 未知参数的估计

上面已讲到过,不管  $H_{0}$  是否为真,

$$
\hat {\sigma} ^ {2} = \frac {S _ {E}}{n - s}
$$

是  $\sigma^{2}$  的无偏估计.

又由(1.14)，(1.7)式知

$$
E (\overline {{X}}) = \mu ,   E (\overline {{X}} _ {. j}) = \frac {1}{n _ {j}} \sum_ {i = 1} ^ {n _ {j}} E (X _ {i j}) = \mu_ {j}, \quad j = 1, 2, \dots , s.
$$

故 $\hat{\mu} = \overline{X}$, $\hat{\mu}_j = \overline{X}_{.j}$ 分别是 $\mu, \mu_j$ 的无偏估计.

又若拒绝  $H_{0}$ ，这意味着效应  $\delta_{1}, \delta_{2}, \cdots, \delta_{s}$  不全为零。由于

$$
\delta_ {j} = \mu_ {j} - \mu , \quad j = 1, 2, \dots , s,
$$

知 $\hat{\delta}_j = \overline{X}_{.j} - \overline{X}$ 是 $\delta_j$ 的无偏估计.此时还有关系式

$$
\sum_ {j = 1} ^ {s} n _ {j} \hat {\delta} _ {j} = \sum_ {j = 1} ^ {s} n _ {j} \overline {{X}} _ {. j} - n \overline {{X}} = 0.
$$

当拒绝 $H_0$ 时，常需要作出两总体 $N(\mu_j, \sigma^2)$ 和 $N(\mu_k, \sigma^2), j \neq k$ 的均值差 $\mu_j - \mu_k = \delta_j - \delta_k$ 的区间估计. 其做法如下.

由于 $E(\overline{X}_{.j} - \overline{X}_{.k}) = \mu_j - \mu_k,$

$$
D (\overline {{X}} _ {. j} - \overline {{X}} _ {. k}) = \sigma^ {2} \left(\frac {1}{n _ {j}} + \frac {1}{n _ {k}}\right),
$$

由第六章末所附“§3定理3的证明及其推广”知 $\overline{X}_{.j}-\overline{X}_{.k}$ 与 $\hat{\sigma}^{2}=S_{E}/(n-s)$ 独立.于是

$$
\begin{array}{l} \frac {(\overline {{X}} _ {. j} - \overline {{X}} _ {. k}) - (\mu_ {j} - \mu_ {k})}{\sqrt {\overline {{S}} _ {E} \left(\frac {1}{n _ {j}} + \frac {1}{n _ {k}}\right)}} \\ = \frac {(\overline {{X}} _ {. j} - \overline {{X}} _ {. k}) - (\mu_ {j} - \mu_ {k})}{\sigma \sqrt {1 / n _ {j} + 1 / n _ {k}}} \left| \sqrt {\frac {S _ {E}}{\sigma^ {2}}} \right| (n - s) \sim t (n - s). \\ \end{array}
$$

据此得均值差 $\mu_{j} - \mu_{k} = \delta_{j} - \delta_{k}$ 的置信水平为 $1 - \alpha$ 的置信区间为

$$
\left(\overline {{X}} _ {. j} - \overline {{X}} _ {. k} \pm t _ {\alpha / 2} (n - s) \sqrt {\overline {{S}} _ {E} \left(\frac {1}{n _ {j}} + \frac {1}{n _ {k}}\right)}\right). \tag {1.22}
$$

例5 求例4中的未知参数 $\sigma^2, \mu_j, \delta_j (j = 1,2,3)$ 的点估计及均值差的置信水平为0.95的置信区间.

解 $\hat{\sigma}^2 = S_E / (n - s) = 0.000016,$

$$
\hat {\mu} _ {1} = \overline {{x}} _ {. 1} = 0. 2 4 2, \hat {\mu} _ {2} = \overline {{x}} _ {. 2} = 0. 2 5 6, \hat {\mu} _ {3} = \overline {{x}} _ {. 3} = 0. 2 6 2, \hat {\mu} = \overline {{x}} = 0. 2 5 3,
$$

$$
\hat {\delta} _ {1} = \overline {{x}} _ {. 1} - \overline {{x}} = - 0. 0 1 1, \hat {\delta} _ {2} = \overline {{x}} _ {. 2} - \overline {{x}} = 0. 0 0 3, \hat {\delta} _ {3} = \overline {{x}} _ {. 3} - \overline {{x}} = 0. 0 0 9.
$$

均值差的区间估计如下:

由 $t_{0.025}(n - s) = t_{0.025}(12) = 2.1788$ 得

$$
t _ {0. 0 2 5} (1 2) \sqrt {\overline {{S}} _ {E} \left(\frac {1}{n _ {j}} + \frac {1}{n _ {k}}\right)} = 2. 1 7 8 8 \sqrt {1 6 \times 1 0 ^ {- 6} \times \frac {2}{5}} = 0. 0 0 6,
$$

故 $\mu_{1} - \mu_{2},\mu_{1} - \mu_{3}$ 及 $\mu_{2} - \mu_{3}$ 的置信水平为0.95的置信区间分别为

$$
\begin{array}{l} (0. 2 4 2 - 0. 2 5 6 \pm 0. 0 0 6) = (- 0. 0 2 0, - 0. 0 0 8), \\ (0. 2 4 2 - 0. 2 6 2 \pm 0. 0 0 6) = (- 0. 0 2 6, - 0. 0 1 4), \\ (0. 2 5 6 - 0. 2 6 2 \pm 0. 0 0 6) = (- 0. 0 1 2, 0). \\ \end{array}
$$

例6 设在例2中的四种类型电路的响应时间的总体均为正态, 且各总体的方差相同, 但参数均未知. 又设各样本相互独立. 试取显著性水平 $\alpha = 0.05$ 检验各类型电路的响应时间是否有显著差异.

解 分别以  $\mu_{1}, \mu_{2}, \mu_{3}, \mu_{4}$  记类型 I, II, III, IV 四种电路响应时间总体的均值. 我们需检验假设 ( $\alpha = 0.05$ )

$$
H _ {0}: \mu_ {1} = \mu_ {2} = \mu_ {3} = \mu_ {4},
$$

$H_{1}:\mu_{1},\mu_{2},\mu_{3},\mu_{4}$  不全相等.

现在 $n = 18, s = 4, n_1 = n_2 = n_3 = 5, n_4 = 3,$

$$
S _ {T} = \sum_ {j = 1} ^ {4} \sum_ {i = 1} ^ {n _ {j}} x _ {i j} ^ {2} - \frac {T _ {\cdot \cdot} ^ {2}}{1 8} = 8 9 9 2 - 3 8 6 ^ {2} / 1 8 = 7 1 4. 4 4,
$$

$$
\begin{array}{l} S _ {A} = \sum_ {j = 1} ^ {4} \frac {T _ {. j} ^ {2}}{n _ {j}} - \frac {T _ {. .} ^ {2}}{1 8} \\ = \left[ \frac {1}{5} (9 4 ^ {2} + 1 4 1 ^ {2} + 9 2 ^ {2}) + \frac {5 9 ^ {2}}{3} \right] - \frac {3 8 6 ^ {2}}{1 8} = 3 1 8. 9 8, \\ \end{array}
$$

$$
\begin{array}{l} S _ {A} = \sum_ {j = 1} ^ {4} \frac {T _ {. j} ^ {2}}{n _ {j}} - \frac {T _ {. .} ^ {2}}{1 8} \\ = \left[ \frac {1}{5} (9 4 ^ {2} + 1 4 1 ^ {2} + 9 2 ^ {2}) + \frac {5 9 ^ {2}}{3} \right] - \frac {3 8 6 ^ {2}}{1 8} = 3 1 8. 9 8, \\ S _ {E} = S _ {T} - S _ {A} = 3 9 5. 4 6. \\ \end{array}
$$

$S_{T}, S_{A}, S_{E}$  的自由度依次为 17, 3, 14, 结果载于表 9-7.

表 9-7 例 6 的方差分析表

| 方差来源 | 平方和 | 自由度 | 均方 | F比 |
| --- | --- | --- | --- | --- |
| 因素 | 318.98 | 3 | 106.33 | 3.76 |
| 误差 | 395.46 | 14 | 28.25 |  |
| 总和 | 714.44 | 17 |  |  |

因 $F_{0.05}(3,14) = 3.34 < 3.76$ ，故在显著性水平0.05下拒绝 $H_0$ ，认为各类型电路的响应时间有显著差异. □

## § 2 双因素试验的方差分析

本节介绍双因素试验的方差分析.

## (一) 双因素等重复试验的方差分析

设有两个因素 A, B 作用于试验指标. 因素 A 有 r 个水平  $A_{1}, A_{2}, \cdots, A_{r}$ ，因素 B 有 s 个水平  $B_{1}, B_{2}, \cdots, B_{s}$ . 现对因素 A, B 的水平的每对组合  $(A_{i}, B_{j}), i = 1, 2, \cdots, r; j = 1, 2, \cdots, s$  都作  $t (t \geqslant 2)$  次试验（称为等重复试验），得到如表 9-8 的结果:

表9-8

| 因素A\\因素B | $B_1$ | $B_2$ | ... | $B_s$ |
| --- | --- | --- | --- | --- |
| $A_1$ | $X_{111},X_{112},$$\cdots,X_{11t}$ | $X_{121},X_{122},$$\cdots,X_{12t}$ | ... | $X_{1s1},X_{1s2},$$\cdots,X_{1st}$ |
| $A_2$ | $X_{211},X_{212},$$\cdots,X_{21t}$ | $X_{221},X_{222},$$\cdots,X_{22t}$ | ... | $X_{2s1},X_{2s2},$$\cdots,X_{2st}$ |
| ⋮ | ⋮ | ⋮ |  | ⋮ |
| $A_r$ | $X_{r11},X_{r12},$$\cdots,X_{r1t}$ | $X_{r21},X_{r22},$$\cdots,X_{r2t}$ | ... | $X_{rs1},X_{rs2},$$\cdots,X_{rst}$ |

并设

$$
X _ {i j k} \sim N (\mu_ {i j}, \sigma^ {2}), \quad i = 1, 2, \dots , r; j = 1, 2, \dots , s; k = 1, 2, \dots , t,
$$

各 $X_{ijk}$ 独立.这里， $\mu_{ij},\sigma^2$ 均为未知参数.或写成

$$
\left. \begin{array}{l} {{X _ {i j k} = \mu_ {i j} + \varepsilon_ {i j k},}} \\ {{\varepsilon_ {i j k} \sim N (0, \sigma^ {2}), \text {各} \varepsilon_ {i j k} \text {独立},}} \\ {{i = 1, 2, \dots , r; j = 1, 2, \dots , s;}} \\ {{k = 1, 2, \dots , t.}} \end{array} \right\} \tag {2.1}
$$

引入记号

$$
\begin{array}{l} \mu = \frac {1}{r s} \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} \mu_ {i j}, \\ \mu_ {i.} = \frac {1}{s} \sum_ {j = 1} ^ {s} \mu_ {i j}, \quad i = 1, 2, \dots , r, \\ \mu_ {. j} = \frac {1}{r} \sum_ {i = 1} ^ {r} \mu_ {i j}, \quad j = 1, 2, \dots , s, \\ \alpha_ {i} = \mu_ {i}. - \mu , \quad i = 1, 2, \dots , r, \\ \beta_ {j} = \mu_ {\cdot j} - \mu , \quad j = 1, 2, \dots , s. \\ \end{array}
$$

易见

$$
\sum_ {i = 1} ^ {r} \alpha_ {i} = 0, \quad \sum_ {j = 1} ^ {s} \beta_ {j} = 0.
$$

称 $\mu$ 为总平均，称 $\alpha_{i}$ 为水平 $A_{i}$ 的效应，称 $\beta_{j}$ 为水平 $B_{j}$ 的效应.这样可将 $\mu_{ij}$ 表示成

$$
\mu_ {i j} = \mu + \alpha_ {i} + \beta_ {j} + (\mu_ {i j} - \mu_ {i}. - \mu_ {. j} + \mu), \tag {2.2}
$$

$$
i = 1, 2, \dots , r; \quad j = 1, 2, \dots , s.
$$

记  $\gamma_{ij}=\mu_{ij}-\mu_{i\cdot}-\mu_{\cdot j}+\mu,\quad i=1,2,\cdots,r;\quad j=1,2,\cdots,s,$  (2.3)

此时

$$
\mu_ {i j} = \mu + \alpha_ {i} + \beta_ {j} + \gamma_ {i j}. \tag {2.4}
$$

$\gamma_{ij}$  称为水平  $A_{i}$  和水平  $B_{j}$  的交互效应, 这是由  $A_{i}, B_{j}$  搭配起来联合起作用而引起的. 易见

$$
\begin{array}{l} \sum_ {i = 1} ^ {r} \gamma_ {i j} = 0, \quad j = 1, 2, \dots , s, \\ \sum_ {j = 1} ^ {s} \gamma_ {i j} = 0, \quad i = 1, 2, \dots , r. \\ \end{array}
$$

这样，(2.1) 可写成

$$
\left. \begin{array}{l} X _ {i j k} = \mu + \alpha_ {i} + \beta_ {j} + \gamma_ {i j} + \varepsilon_ {i j k}, \\ \varepsilon_ {i j k} \sim N (0, \sigma^ {2}), \text {各} \varepsilon_ {i j k} \text {独立}, \\ i = 1, 2, \dots , r; j = 1, 2, \dots , s; k = 1, 2, \dots , t, \\ \sum_ {i = 1} ^ {r} \alpha_ {i} = 0, \sum_ {j = 1} ^ {s} \beta_ {j} = 0, \sum_ {i = 1} ^ {r} \gamma_ {i j} = 0, \sum_ {j = 1} ^ {s} \gamma_ {i j} = 0, \end{array} \right\} \tag {2.5}
$$

其中  $\mu,\alpha_{i},\beta_{j},\gamma_{ij}$  及  $\sigma^{2}$  都是未知参数.

(2.5) 式就是我们所要研究的双因素试验方差分析的数学模型. 对于这一模型我们要检验以下三个假设:

$$
\left\{ \begin{array}{l l} H _ {0 1}: & \alpha_ {1} = \alpha_ {2} = \dots = \alpha_ {r} = 0, \\ H _ {1 1}: & \alpha_ {1}, \alpha_ {2}, \dots , \alpha_ {r} \text {不全为零}, \end{array} \right. \tag {2.6}
$$

$$
\left\{ \begin{array}{l l} H _ {0 2}: & \beta_ {1} = \beta_ {2} = \dots = \beta_ {s} = 0, \\ H _ {1 2}: & \beta_ {1}, \beta_ {2}, \dots , \beta_ {s} \text {不全为零}, \end{array} \right. \tag {2.7}
$$

$$
\left\{ \begin{array}{l l} H _ {0 3}: & \gamma_ {1 1} = \gamma_ {1 2} = \dots = \gamma_ {r s} = 0, \\ H _ {1 3}: & \gamma_ {1 1}, \gamma_ {1 2}, \dots , \gamma_ {r s} \text {不全为零}. \end{array} \right. \tag {2.8}
$$

与单因素情况类似,对这些问题的检验方法也是建立在平方和的分解上的.先引入以下的记号:

$$
\overline {{X}} = \frac {1}{r s t} \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} \sum_ {k = 1} ^ {t} X _ {i j k},
$$

$$
\overline {{X}} _ {i j.} = \frac {1}{t} \sum_ {k = 1} ^ {t} X _ {i j k}, \quad i = 1, 2, \dots , r; j = 1, 2, \dots , s,
$$

$$
\overline {{X}} _ {i..} = \frac {1}{s t} \sum_ {j = 1} ^ {s} \sum_ {k = 1} ^ {t} X _ {i j k}, \quad i = 1, 2, \dots , r,
$$

$$
\overline {{X}} _ {. j.} = \frac {1}{r t} \sum_ {i = 1} ^ {r} \sum_ {k = 1} ^ {t} X _ {i j k}, \quad j = 1, 2, \dots , s.
$$

再引入总偏差平方和(称为总变差)

$$
S _ {T} = \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} \sum_ {k = 1} ^ {t} (X _ {i j k} - \overline {{X}}) ^ {2}.
$$

我们可将 $S_{T}$ 写成

$$
\begin{array}{l} S _ {T} = \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} \sum_ {k = 1} ^ {t} (X _ {i j k} - \overline {{X}}) ^ {2} \\ = \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} \sum_ {k = 1} ^ {t} \left[ (X _ {i j k} - \overline {{X}} _ {i j.}) + (\overline {{X}} _ {i..} - \overline {{X}}) + (\overline {{X}} _ {. j.} - \overline {{X}}) \right. \\ \left. + (\overline {{X}} _ {i j}. - \overline {{X}} _ {i..} - \overline {{X}} _ {. j.} + \overline {{X}}) \right] ^ {2} \\ = \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} \sum_ {k = 1} ^ {t} (X _ {i j k} - \overline {{X}} _ {i j.}) ^ {2} + s t \sum_ {i = 1} ^ {r} (\overline {{X}} _ {i..} - \overline {{X}}) ^ {2} \\ + r t \sum_ {j = 1} ^ {s} (\overline {{X}} _ {. j.} - \overline {{X}}) ^ {2} + t \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} (\overline {{X}} _ {i j.} - \overline {{X}} _ {i..} - \overline {{X}} _ {. j.} + \overline {{X}}) ^ {2}, \\ \end{array}
$$

即得平方和的分解式

$$
S _ {T} = S _ {E} + S _ {A} + S _ {B} + S _ {A \times B}, \tag {2.9}
$$

其中 $S_{E} = \sum_{i=1}^{r}\sum_{j=1}^{s}\sum_{k=1}^{t}(X_{ijk}-\overline{X}_{ij.})^{2},$ (2.10)

$$
S _ {A} = s t \sum_ {i = 1} ^ {r} (\overline {{X}} _ {i..} - \overline {{X}}) ^ {2}, \tag {2.11}
$$

$$
S _ {B} = r t \sum_ {j = 1} ^ {s} (\overline {{X}} _ {. j.} - \overline {{X}}) ^ {2}, \tag {2.12}
$$

$$
S _ {A \times B} = t \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} (\overline {{X}} _ {i j.} - \overline {{X}} _ {i..} - \overline {{X}} _ {. j.} + \overline {{X}}) ^ {2}. \tag {2.13}
$$

$S_{E}$ 称为误差平方和， $S_{A}, S_{B}$ 分别称为因素 $A$ 、因素 $B$ 的效应平方和， $S_{A \times B}$ 称为 $A, B$ 交互效应平方和.

可以证明 $S_{T}, S_{E}, S_{A}, S_{B}, S_{A \times B}$ 的自由度依次为 $rst - 1, rs(t - 1), r - 1, s - 1, (r - 1)(s - 1)$，且有

$$
E \left(\frac {S _ {E}}{r s (t - 1)}\right) = \sigma^ {2}, \tag {2.14}
$$

$$
E \Big (\frac {S _ {A}}{r - 1} \Big) = \sigma^ {2} + \frac {s t \sum_ {i = 1} ^ {r} \alpha_ {i} ^ {2}}{r - 1}, \tag {2.15}
$$

$$
E \Big (\frac {S _ {B}}{s - 1} \Big) = \sigma^ {2} + \frac {r t \sum_ {j = 1} ^ {s} \beta_ {j} ^ {2}}{s - 1}, \tag {2.16}
$$

$$
E \Big (\frac {S _ {A \times B}}{(r - 1) (s - 1)} \Big) = \sigma^ {2} + \frac {t \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} \gamma_ {i j} ^ {2}}{(r - 1) (s - 1)}. \tag {2.17}
$$

当 $H_{01}:\alpha_1 = \alpha_2 = \dots = \alpha_r = 0$ 为真时，可以证明

$$
F _ {A} = \frac {S _ {A} / (r - 1)}{S _ {E} / [ r s (t - 1) ]} \sim F (r - 1, r s (t - 1)). \tag {2.18}
$$

取显著性水平为 $\alpha$ ，得假设 $H_{01}$ 的拒绝域为

$$
F _ {A} = \frac {S _ {A} / (r - 1)}{S _ {E} / [ r s (t - 1) ]} \geqslant F _ {a} (r - 1, r s (t - 1)). \tag {2.19}
$$

类似地，在显著性水平  $\alpha$  下，假设  $H_{02}$  的拒绝域为

$$
F _ {B} = \frac {S _ {B} / (s - 1)}{S _ {E} / [ r s (t - 1) ]} \geqslant F _ {\alpha} (s - 1, r s (t - 1)). \tag {2.20}
$$

在显著性水平  $\alpha$  下, 假设  $H_{03}$  的拒绝域为

$$
\begin{array}{l} F _ {A \times B} = \frac {S _ {A \times B} / [ (r - 1) (s - 1) ]}{S _ {E} / [ r s (t - 1) ]} \\ \geqslant F _ {\alpha} ((r - 1) (s - 1), r s (t - 1)). \tag {2.21} \\ \end{array}
$$

上述结果可汇总成下列的方差分析表(表9-9):

表 9-9 双因素试验的方差分析表

| 方差来源 | 平方和 | 自由度 | 均方 | F比 |
| --- | --- | --- | --- | --- |
| 因素A | $S_A$ | r-1 | $\overline{S}_A = \frac{S_A}{r-1}$ | $F_A = \frac{\overline{S}_A}{\overline{S}_E}$ |
| 因素B | $S_B$ | s-1 | $\overline{S}_B = \frac{S_B}{s-1}$ | $F_B = \frac{\overline{S}_B}{\overline{S}_E}$ |
| 交互作用 | $S_{A \times B}$ | (r-1)(s-1) | $\overline{S}_{A \times B} = \frac{S_{A \times B}}{(r-1)(s-1)}$ | $F_{A \times B} = \frac{\overline{S}_{A \times B}}{\overline{S}_E}$ |
| 误差 | $S_E$ | rs(t-1) | $\overline{S}_E = \frac{S_E}{rs(t-1)}$ |  |
| 总和 | $S_T$ | rst-1 |  |  |

记 $T\ldots = \sum_{i=1}^{r}\sum_{j=1}^{s}\sum_{k=1}^{t}X_{ijk},$

$$
T _ {i j.} = \sum_ {k = 1} ^ {t} X _ {i j k}, \quad i = 1, 2, \dots , r; j = 1, 2, \dots , s,
$$

$$
T _ {i..} = \sum_ {j = 1} ^ {s} \sum_ {k = 1} ^ {t} X _ {i j k}, \quad i = 1, 2, \dots , r,
$$

$$
T _ {. j.} = \sum_ {i = 1} ^ {r} \sum_ {k = 1} ^ {t} X _ {i j k}, \quad j = 1, 2, \dots , s.
$$

我们可以按照下述(2.22)式来计算上表中的各个平方和.

$$
\left. \begin{array}{l} S _ {T} = \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} \sum_ {k = 1} ^ {t} X _ {i j k} ^ {2} - \frac {T _ {\cdots} ^ {2}}{r s t}, \\ S _ {A} = \frac {1}{s t} \sum_ {i = 1} ^ {r} T _ {i..} ^ {2} - \frac {T _ {\cdots} ^ {2}}{r s t}, \\ S _ {B} = \frac {1}{r t} \sum_ {j = 1} ^ {s} T _ {. j.} ^ {2}. - \frac {T _ {\cdots} ^ {2}}{r s t}, \\ S _ {A \times B} = \left(\frac {1}{t} \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} T _ {i j.} ^ {2}. - \frac {T _ {\cdots} ^ {2}}{r s t}\right) - S _ {A} - S _ {B}, \\ S _ {E} = S _ {T} - S _ {A} - S _ {B} - S _ {A \times B}. \end{array} \right\} \tag {2.22}
$$

例 1 在上一节例 3 中, 假设符合双因素方差分析模型所需的条件. 试在显著性水平  $\alpha = 0.05$  下, 检验不同燃料(因素 A)、不同推进器(因素 B)下的射程是否有显著差异? 交互作用是否显著?

解 需检验假设 $H_{01}, H_{02}, H_{03}$ （见(2.6)—(2.8)). $T\ldots, T_{ij}$, $T_{i\ldots}, T_{j\cdot}$ 的计算如表9-10.

表9-10

| A\\B | $B_1$ | $B_2$ | $B_3$ | $T_{i..}$ |
| --- | --- | --- | --- | --- |
| $A_1$ | 58.2(110.8)52.6 | 56.2(97.4)41.2 | 65.3(126.1)60.8 | 334.3 |
| $A_2$ | 49.1(91.9)42.8 | 54.1(104.6)50.5 | 51.6(100)48.4 | 296.5 |
| $A_3$ | 60.1(118.4)58.3 | 70.9(144.1)73.2 | 39.2(79.9)40.7 | 342.4 |
| $A_4$ | 75.8(147.3)71.5 | 58.2(109.2)51.0 | 48.7(90.1)41.4 | 346.6 |
| T.j. | 468.4 | 455.3 | 396.1 | 1 319.8 |

表中括弧内的数是 $T_{ij}$ ..现在 $r = 4,s = 3,t = 2$ ，故有

$$
S _ {T} = (5 8. 2 ^ {2} + 5 2. 6 ^ {2} + \dots + 4 1. 4 ^ {2}) - \frac {1 3 1 9 . 8 ^ {2}}{2 4} = 2 6 3 8. 2 9 8 3 3,
$$

$$
S _ {A} = \frac {1}{6} (3 3 4. 3 ^ {2} + 2 9 6. 5 ^ {2} + 3 4 2. 4 ^ {2} + 3 4 6. 6 ^ {2}) - \frac {1 3 1 9 . 8 ^ {2}}{2 4} = 2 6 1. 6 7 5 0 0,
$$

$$
S _ {B} = \frac {1}{8} (4 6 8. 4 ^ {2} + 4 5 5. 3 ^ {2} + 3 9 6. 1 ^ {2}) - \frac {1 3 1 9 . 8 ^ {2}}{2 4} = 3 7 0. 9 8 0 8 3,
$$

$$
S _ {A \times B} = \frac {1}{2} (1 1 0. 8 ^ {2} + 9 1. 9 ^ {2} + \dots + 9 0. 1 ^ {2}) - \frac {1 3 1 9 . 8 ^ {2}}{2 4} - S _ {A} - S _ {B} = 1 7 6 8. 6 9 2 5 0,
$$

$$
S _ {E} = S _ {T} - S _ {A} - S _ {B} - S _ {A \times B} = 2 3 6. 9 5 0 0 0.
$$

得方差分析表如表 9-11 所示:

表 9-11 例 1 的方差分析表

| 方差来源 | 平方和 | 自由度 | 均方 | F比 |
| --- | --- | --- | --- | --- |
| 因素A(燃料) | 261.675 00 | 3 | 87.225 0 | $F_A = 4.42$ |
| 因素B(推进器) | 370.980 83 | 2 | 185.490 4 | $F_B = 9.39$ |
| 交互作用A×B | 1 768.692 50 | 6 | 294.782 1 | $F_{A \times B} = 14.9$ |
| 误差 | 236.950 00 | 12 | 19.745 8 |  |
| 总和 | 2 638.298 33 | 23 |  |  |

由于 $F_{0.05}(3,12) = 3.49 < F_A, F_{0.05}(2,12) = 3.89 < F_B$，所以在显著性水平 $\alpha = 0.05$ 下，我们拒绝假设 $H_{01}, H_{02}$，即认为不同燃料或不同推进器下的射程有显著差异。也就是说，燃料和推进器这两个因素对射程的影响都是显著的。又，$F_{0.05}(6,12) = 3.00 < F_{A \times B}$，故拒绝 $H_{03}$。值得注意的是，$F_{0.001}(6,12) = 8.38$ 也远小于 $F_{A \times B} = 14.9$。故交互作用效应是高度显著的。从表9-10可以看出，$A_4$ 与 $B_1$ 或 $A_3$ 与 $B_2$ 的搭配都使火箭射程较之其他水平的搭配要远得多。在实际中我们就选最优的搭配方式来实施。

例 2 在某种金属材料的生产过程中, 对热处理温度(因素 B)与时间(因素 A)各取两个水平, 产品强度的测定结果(相对值)如表 9-12 所示. 在同一条件下每个试验重复两次. 设各水平搭配下强度的总体服从正态分布且方差相同. 各样本独立. 问热处理温度、时间以及这两者的交互作用对产品强度是否有显著的影响(取  $\alpha = 0.05$ )?

表9-12

| A\\B | $B_1$ | $B_2$ | $T_{i..}$ |
| --- | --- | --- | --- |
| $A_1$ | 38.0(76.6)38.6 | 47.0(91.8)44.8 | 168.4 |
| $A_2$ | 45.0(88.8)43.8 | 42.4(83.2)40.8 | 172 |
| $T_{.j.}$ | 165.4 | 175 | 340.4 |

解 按题意需检验假设(2.6)—(2.8)，作计算如下:

$$
S _ {T} = (3 8. 0 ^ {2} + 3 8. 6 ^ {2} + \dots + 4 0. 8 ^ {2}) - \frac {3 4 0 . 4 ^ {2}}{8} = 7 1. 8 2,
$$

$$
S _ {A} = \frac {1}{4} (1 6 8. 4 ^ {2} + 1 7 2 ^ {2}) - \frac {3 4 0 . 4 ^ {2}}{8} = 1. 6 2,
$$

$$
S _ {B} = \frac {1}{4} (1 6 5. 4 ^ {2} + 1 7 5 ^ {2}) - \frac {3 4 0 . 4 ^ {2}}{8} = 1 1. 5 2,
$$

$$
S _ {A \times B} = 1 4 5 5 1. 2 4 - 1 4 4 8 4. 0 2 - 1. 6 2 - 1 1. 5 2 = 5 4. 0 8,
$$

$$
\begin{array}{l} S _ {E} = S _ {T} - S _ {A} - S _ {B} - S _ {A \times B} \\ = 7 1. 8 2 - 1. 6 2 - 1 1. 5 2 - 5 4. 0 8 = 4. 6. \\ \end{array}
$$

得方差分析表如表 9-13 所示:

表 9-13 例 2 的方差分析表①

| 方差来源 | 平方和 | 自由度 | 均方 | F比 |
| --- | --- | --- | --- | --- |
| 因素A | 1.62 | 1 | 1.62 | $F_A = 1.4$ |
| 因素B | 11.52 | 1 | 11.52 | $F_B = 10.0$ |
| 交互作用A×B | 54.08 | 1 | 54.08 | $F_{A \times B} = 47.0$ |
| 误差 | 4.6 | 4 | 1.15 |  |
| 总和 | 71.82 | 7 |  |  |

由于

$$
F _ {0. 0 5} (1, 4) = 7. 7 1,
$$

所以认为时间对产品强度的影响不显著,而热处理温度的影响显著,且交互作用的影响显著.

## (二) 双因素无重复试验的方差分析

在以上的讨论中,我们考虑了双因素试验中两个因素的交互作用.为检验交互作用的效应是否显著,对于两个因素的每一组合 $(A_{i},B_{j})$ 至少要做2次试验.这是因为在模型(2.5)中,若 $k=1,\gamma_{ij}+\varepsilon_{ijk}$ 总以结合在一起的形式出现,这样就不能将交互作用与误差分离开来.如果在处理实际问题时,我们已经知道不存在交互作用,或已知交互作用对试验的指标影响很小,则可以不考虑交互作用.此时,即使k=1,也能对因素A、因素B的效应进行分析.现设对于两个因素的每一组合 $(A_{i},B_{j})$ 只做一次试验,所得结果如表9-14所示:

表9-14

| 因素A\\因素B | $B_1$ | $B_2$ | ... | $B_s$ |
| --- | --- | --- | --- | --- |
| $A_1$ | $X_{11}$ | $X_{12}$ | ... | $X_{1s}$ |
| $A_2$ | $X_{21}$ | $X_{22}$ | ... | $X_{2s}$ |
| $\vdots$ | $\vdots$ | $\vdots$ |  | $\vdots$ |
| $A_r$ | $X_{r1}$ | $X_{r2}$ | ... | $X_{rs}$ |

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 在实际应用中，总是先计算 $F_{A \times B}$，对交互作用进行检验。如果交互作用不显著，则将 $A \times B$ 一栏的平方和与自由度分别加到误差这一栏中去，重新计算 $F_A, F_B$，用新的 $F_A, F_B$ 对因素 $A$，因素 $B$ 进行检验。</span></small>

并设

$$
X _ {i j} \sim N (\mu_ {i j}, \sigma^ {2}),
$$

各  $X_{ij}$  独立， $i=1,2,\cdots,r;j=1,2,\cdots,s,$

其中 $\mu_{ij},\sigma^2$ 均为未知参数.或写成

$$
\left. \begin{array}{l} {{X _ {i j} = \mu_ {i j} + \varepsilon_ {i j},}} \\ {{\varepsilon_ {i j} \sim N (0, \sigma^ {2}),}} \\ {{\text {各} \varepsilon_ {i j} \text {独立},}} \\ {{i = 1, 2, \dots , r; j = 1, 2, \dots , s.}} \end{array} \right\} \tag {2.23}
$$

沿用(一)中的记号, 注意到现在假设不存在交互作用, 此时  $\gamma_{ij}=0, i=1, 2,\cdots,r; j=1,2,\cdots,s.$  故由(2.4)式知  $\mu_{ij}=\mu+\alpha_{i}+\beta_{j}.$  于是(2.23)可写成

$$
\left. \begin{array}{l} {X _ {i j} = \mu + \alpha_ {i} + \beta_ {j} + \varepsilon_ {i j},} \\ {\varepsilon_ {i j} \sim N (0, \sigma^ {2}), \text {各} \varepsilon_ {i j} \text {独立},} \\ {i = 1, 2, \dots , r; j = 1, 2, \dots , s,} \\ {\sum_ {i = 1} ^ {r} \alpha_ {i} = 0, \sum_ {j = 1} ^ {s} \beta_ {j} = 0.} \end{array} \right\} \tag {2.24}
$$

这就是现在要研究的方差分析的模型. 对这个模型我们所要检验的假设有以下两个:

$$
\left\{ \begin{array}{l l} H _ {0 1}: & \alpha_ {1} = \alpha_ {2} = \dots = \alpha_ {r} = 0, \\ H _ {1 1}: & \alpha_ {1}, \alpha_ {2}, \dots , \alpha_ {r} \text {不全为零}. \end{array} \right. \tag {2.25}
$$

$$
\left\{ \begin{array}{l l} H _ {0 2}: & \beta_ {1} = \beta_ {2} = \dots = \beta_ {s} = 0, \\ H _ {1 2}: & \beta_ {1}, \beta_ {2}, \dots , \beta_ {s} \text {不全为零}. \end{array} \right. \tag {2.26}
$$

与在(一)中同样的讨论可得方差分析表如表9-15所示:

表9-15

| 方差来源 | 平方和 | 自由度 | 均方 | F比 |
| --- | --- | --- | --- | --- |
| 因素A | $S_A$ | r-1 | $\overline{S}_A = \frac{S_A}{r-1}$ | $F_A = \overline{S}_A / \overline{S}_E$ |
| 因素B | $S_B$ | s-1 | $\overline{S}_B = \frac{S_B}{s-1}$ | $F_B = \overline{S}_B / \overline{S}_E$ |
| 误差 | $S_E$ | (r-1)(s-1) | $\overline{S}_E = \frac{S_E}{(r-1)(s-1)}$ |  |
| 总和 | $S_T$ | rs-1 |  |  |

取显著性水平为  $\alpha$ ，得假设  $H_{01}:\alpha_{1}=\alpha_{2}=\cdots=\alpha_{r}=0$  的拒绝域为

$$
F _ {A} = \frac {\overline {{S}} _ {A}}{\overline {{S}} _ {E}} \geqslant F _ {\alpha} (r - 1, (r - 1) (s - 1)).
$$

假设  $H_{02}:\beta_{1}=\beta_{2}=\cdots=\beta_{s}=0$  的拒绝域为

$$
F _ {B} = \frac {\overline {{S}} _ {B}}{\overline {{S}} _ {E}} \geqslant F _ {\alpha} (s - 1, (r - 1) (s - 1)).
$$

表 9-15 中的平方和可按下述式子来计算:

$$
\left. \begin{array}{l} S _ {T} = \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} X _ {i j} ^ {2} - \frac {T _ {\cdot \cdot} ^ {2}}{r s}, \\ S _ {A} = \frac {1}{s} \sum_ {i = 1} ^ {r} T _ {i \cdot} ^ {2} - \frac {T _ {\cdot \cdot} ^ {2}}{r s}, \\ S _ {B} = \frac {1}{r} \sum_ {j = 1} ^ {s} T _ {\cdot j} ^ {2} - \frac {T _ {\cdot \cdot} ^ {2}}{r s}, \\ S _ {E} = S _ {T} - S _ {A} - S _ {B}, \end{array} \right\} \tag {2.27}
$$

其中 $T_{..} = \sum_{i=1}^{r} \sum_{j=1}^{s} X_{ij}, \quad T_{i..} = \sum_{j=1}^{s} X_{ij}, \quad i = 1,2,\cdots,r,$

$$
T _ {. j} = \sum_ {i = 1} ^ {r} X _ {i j}, \quad j = 1, 2, \dots , s.
$$

例3 下面给出了在某5个不同地点、不同时间空气中的颗粒状物（以 $\mathrm{mg / m^3}$ 计）的含量的数据:

<table><tr><td rowspan="2">因素A(时间)</td><td colspan="5">因素B(地点)</td><td rowspan="2"> $T_{i.}$ </td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1995年10月</td><td>76</td><td>67</td><td>81</td><td>56</td><td>51</td><td>331</td></tr><tr><td>1996年1月</td><td>82</td><td>69</td><td>96</td><td>59</td><td>70</td><td>376</td></tr><tr><td>1996年5月</td><td>68</td><td>59</td><td>67</td><td>54</td><td>42</td><td>290</td></tr><tr><td>1996年8月</td><td>63</td><td>56</td><td>64</td><td>58</td><td>37</td><td>278</td></tr><tr><td> $T_{.j}$ </td><td>289</td><td>251</td><td>308</td><td>227</td><td>200</td><td>1 275</td></tr></table>

设本题符合模型(2.24)中的条件.试在显著性水平  $\alpha = 0.05$  下检验:在不同时间下颗粒状物含量的均值有无显著差异,在不同地点下颗粒状物含量的均值有无显著差异.

解 按题意需检验假设(2.25)、(2.26). $T_{i}$, $T_{j}$ 的值已算出载于上表. 现在 $r = 4, s = 5$. 由(2.27)得到

$$
\begin{array}{l} S _ {T} = 7 6 ^ {2} + 6 7 ^ {2} + \dots + 3 7 ^ {2} - \frac {1 2 7 5 ^ {2}}{2 0} = 3 5 7 1. 7 5, \\ S _ {A} = \frac {1}{5} (3 3 1 ^ {2} + 3 7 6 ^ {2} + 2 9 0 ^ {2} + 2 7 8 ^ {2}) - \frac {1 2 7 5 ^ {2}}{2 0} = 1 1 8 2. 9 5, \\ S _ {B} = \frac {1}{4} (2 8 9 ^ {2} + 2 5 1 ^ {2} + \dots + 2 0 0 ^ {2}) - \frac {1 2 7 5 ^ {2}}{2 0} = 1 9 4 7. 5 0, \\ S _ {E} = 3 5 7 1. 7 5 - (1 1 8 2. 9 5 + 1 9 4 7. 5 0) = 4 4 1. 3 0. \\ \end{array}
$$

得方差分析表如表 9-16 所示:

表 9-16 例 3 的方差分析表

| 方差来源 | 平方和 | 自由度 | 均方 | F比 |
| --- | --- | --- | --- | --- |
| 因素A | $S_A = 1\ 182.95$ | 3 | 394.32 | $F_A = 10.72$ |
| 因素B | $S_B = 1\ 947.50$ | 4 | 486.88 | $F_B = 13.24$ |
| 误差 | $S_E = 441.30$ | 12 | 36.78 |  |
| 总和 | $S_T = 3\ 571.75$ | 19 |  |  |

由于 $F_{0.05}(3,12) = 3.49 < 10.72, F_{0.05}(4,12) = 3.26 < 13.24$，故拒绝 $H_{01}$ 及 $H_{02}$，即认为不同时间下颗粒状物含量的均值有显著差异，也认为不同地点下颗粒状物含量的均值有显著差异。即认为在本题中，时间和地点对颗粒状物的含量的影响均为显著。

## § 3 一元线性回归

在客观世界中普遍存在着变量之间的关系. 变量之间的关系一般来说可分为确定性的与非确定性的两种. 确定性关系是指变量之间的关系可以用函数关系来表达的. 另一种非确定性的关系即所谓相关关系. 例如人的身高与体重之间存在着关系, 一般来说, 人高一些, 体重要重一些, 但同样高度的人, 体重往往不相同. 人的血压与年龄之间也存在着关系, 但同年龄的人的血压往往不相同. 气象中的温度与湿度之间的关系也是这样. 这是因为我们涉及的变量 (如体重、血压、湿度) 是随机变量, 上面所说的变量关系是非确定性的. 回归分析是研究相关关系的一种数学工具, 它能帮助我们从一个变量取得的值去估计另一变量所取的值.