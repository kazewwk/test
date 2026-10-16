## 目录

## 第十六章 多元函数的积分学 1

16.1 二重 Riemann 积分 2

16.2 多重积分及其基本性质 7

16.3 重积分化为累次积分计算 12

16.4 重积分的变量替换 21

16.4.1 仿射变换 21

16.4.2 一般的变量替换 23

16.4.3 极坐标变换 27

16.5 重积分的应用和推广 33

## 第十七章 曲线积分与曲面积分 41

17.1 第一型曲线积分 42

17.2 第二型曲线积分 50

17.3 第一型曲面积分 54

17.4 第二型曲面积分 61

## 第十八章 微分形式简介 67

18.1 各类积分之间的联系 68

18.1.1 Gauss-Green 公式 68

18.1.2 Stokes 公式 76

18.2 外代数和微分形式 80

18.3 拉回映射和外微分运算 87

18.4 Brouwer 不动点定理 91

## 第十九章 场论初步 97

19.1 梯度场和保守场 98

19.2 散度和 Laplace 算子 102

19.3 旋度场 108

## 第二十章 含参变量积分 111

20.1 含参变量常义积分及其性质 112

20.2 含参变量广义积分及其一致收敛性 117

20.3 含参变量广义积分的基本性质 122

20.4 Euler 积分 135

## 第二十一章 Fourier 级数 149

21.1 三角级数与 Fourier 级数 150

21.2 Fourier级数的收敛性 156

21.2.1 Fourier 级数部分和的收敛性,
Dirichlet 积分 156

21.2.2 Fourier 级数的 Cesáro 和的
收敛性, Fejér 积分 160

21.2.3 Fourier级数的逐项可积性 162

21.2.4 Fourier级数的逐项可微性 164

21.2.5 Fourier级数的一致收敛性 167

21.2.6 Gibbs 现象 170

21.2.7 例题 172

21.3 平方可积周期函数的 Fourier 级数 174

21.4 Fourier变换 184

21.5 Fourier级数的唯一性 193

## 参考文献 202

## 常用符号 206

## 索引 208

## 第十六章

## 多元函数的积分学

在第九章中, 我们讨论了一元函数的 Riemann 积分. 本章讨论多元函数的 Riemann 积分 (重积分). 我们遵循的理论框架和第九章类似, 区别在于一元函数的积分区域是区间, 而多元函数的积分区域就要复杂得多. 另外, 多元函数的积分还有积分次序的交换问题, 多元函数的积分变量替换公式的证明也比一元情形复杂得多. 由于两个变量的函数和更多变量的函数的积分理论并无本质差别, 因此我们从 $\mathbb{R}^2$ 上的积分开始讨论.

## 16.1 二重 Riemann 积分

设 $[a, b]$, $[c, d]$ 分别为 $\mathbb{R}$ 中的区间, 则 $I = [a, b] \times [c, d]$ 为 $\mathbb{R}^2$ 中的矩形, 其直径 $d(I)$ 和容积 (面积) $\nu(I)$ 分别为

$$
d (I) = \sqrt {(b - a) ^ {2} + (d - c) ^ {2}}, \nu (I) = (b - a) (d - c).
$$

设这两个区间分别有分割

$$
\mathrm{P} _ {1}: a = x _ {0} <   x _ {1} <   \dots <   x _ {m} = b, \quad \mathrm{P} _ {2}: c = y _ {0} <   y _ {1} <   \dots <   y _ {n} = d,
$$

则直线 $x = x_{i}$ $(0\leqslant i\leqslant m)$ 和 $y = y_{j}$ $(0\leqslant j\leqslant n)$ 将 $I$ 分成 $mn$ 个小矩形(图16.1)

$$
I _ {i j} = [ x _ {i - 1}, x _ {i} ] \times [ y _ {j - 1}, y _ {j} ], 1 \leqslant i \leqslant m, 1 \leqslant j \leqslant n.
$$

这些小矩形称为 $I$ 的一个分割, 记为 $\mathrm{P} = \mathrm{P}_1 \times \mathrm{P}_2$. 分割 $\mathrm{P}$ 的模定义为 $\| \mathrm{P} \| = \max_{i,j} d(I_{ij})$.

![](images/page_643_image_11.jpg)

<details>
<summary>text_image</summary>

y
d
c
O a b x
</details>

图 16.1 矩形的分割

定义 16.1.1 (矩形中的 Riemann 积分) 设  $f: I \rightarrow R$  是定义在矩形 I 上的函数 (图 16.2), 如果存在实数  $\alpha$ , 使得任给  $\varepsilon > 0$ , 均存在  $\delta > 0$ , 当  $\|P\| < \delta$  时, 有

$$
\left| \sum_ {i, j} f (\pmb {\xi} _ {i j}) \nu (I _ {i j}) - \alpha \right| <   \varepsilon , \forall \pmb {\xi} _ {i j} \in I _ {i j},
$$

则称 $f$ 在 $I$ 上Riemann可积，简称可积，记为 $f\in R(I)$ . $\alpha$ 称为 $f$ 在 $I$ 上的积分，记为

$$
\alpha = \int_ {I} f = \iint_ {I} f (x, y)   \mathrm{d} x   \mathrm{d} y.
$$

![](images/page_644_image_4.jpg)

<details>
<summary>text_image</summary>

f
I
</details>

图 16.2 二重积分

注16.1.1 (1) 我们将 $\sum_{i,j} f(\pmb{\xi}_{ij}) \nu(I_{ij})$ 称为 $f$ 关于分割 $\mathrm{P}$ 的一个Riemann和, 也记为 $S(f, \mathrm{P}, \pmb{\xi})$. 如果 $f$ 可积, 则积分可用极限表示为

$$
\int_ {I} f = \lim _ {\| \mathrm{P} \| \to 0} S (f, \mathrm{P}, \boldsymbol {\xi}).
$$

(2) 与一元函数类似, $f$ 在 $I$ 上 Riemann 可积的必要条件是 $f$ 为 $I$ 上的有界函数.

下面假设 $f$ 为 $I$ 上的有界函数. 我们像对一元函数所做过的那样来讨论 $f$ 可积的充要条件. 记 $M_{ij} = \sup_{p \in I_{ij}} f(p), m_{ij} = \inf_{p \in I_{ij}} f(p)$, 并令

$$
S (\mathrm{P}) = S (\mathrm{P}, f) = \sum_ {i, j} M _ {i j} \nu (I _ {i j}), \quad s (\mathrm{P}) = s (\mathrm{P}, f) = \sum_ {i, j} m _ {i j} \nu (I _ {i j}),
$$

$S(P)$  和  $s(P)$  分别是 f 关于分割 P 的 Darboux 上和与 Darboux 下和. 与一元函数一样, 称

$$
\omega_ {i j} = M _ {i j} - m _ {i j} = \sup _ {p \in I _ {i j}} f (p) - \inf _ {p \in I _ {i j}} f (p)
$$

为 $f$ 在小矩形 ${I}_{ij}$ 上的振幅. $f$ 的上和与下和之差可以表示为

$$
S (\mathrm{P}) - s (\mathrm{P}) = \sum_ {i, j} \omega_ {i j} \nu (I _ {i j}).
$$

如果 $[a, b]$ 的分割 $\mathrm{P}_1'$ 是由 $\mathrm{P}_1$ 通过添加分点得到, $[c, d]$ 的分割 $\mathrm{P}_2'$ 是由 $\mathrm{P}_2$ 通过添加分点得到, 则称 $[a, b] \times [c, d]$ 的分割 $\mathrm{P}' = \mathrm{P}_1' \times \mathrm{P}_2'$ 是 $\mathrm{P} = \mathrm{P}_1 \times \mathrm{P}_2$ 的一个加细. 对于加细分割, 下面命题的证明和一元函数完全类似.

命题 16.1.1 如果  $P'$  是 P 的加细, 则

$$
s (\mathrm{P}) \leqslant s (\mathrm{P} ^ {\prime}) \leqslant S (\mathrm{P} ^ {\prime}) \leqslant S (\mathrm{P}),
$$

即分割加细后下和不减，上和不增.

推论 16.1.2 对于 I 的任何两个分割  $P^{1}, P^{2}$ ，均有  $s(P^{1}) \leqslant S(P^{2})$ .

证明 设 $\mathrm{P}^1 = \mathrm{P}_1\times \mathrm{P}_2,\mathrm{P}^2 = \mathrm{P}_1'\times \mathrm{P}_2'$ ，令

$$
\mathrm{P} = \mathrm{P} ^ {1} \cup \mathrm{P} ^ {2} = (\mathrm{P} _ {1} \cup \mathrm{P} _ {1} ^ {\prime}) \times (\mathrm{P} _ {2} \cup \mathrm{P} _ {2} ^ {\prime}),
$$

则 P 既是  $P^{1}$  的加细, 又是  $P^{2}$  的加细, 因此

$$
s (\mathrm{P} ^ {1}) \leqslant s (\mathrm{P}) \leqslant S (\mathrm{P}) \leqslant S (\mathrm{P} ^ {2}),
$$

这说明下和总是不超过上和.

□

对于有界函数, 它的上和与下和也都是有界的. 因此可以考虑

$$
S (f) = \inf _ {\mathrm{P}} S (\mathrm{P}), \quad s (f) = \sup _ {\mathrm{P}} s (\mathrm{P}).
$$

分别称  $S(f)$ ,  $s(f)$  为 f 的上积分与下积分.

例 16.1.1 求常值函数的积分.

解 如果 $f \equiv c$, 则它在矩形 $I$ 上的任何 Riemann 和均为 $c\nu(I)$, 因此常值函数可积. 同时, 常值函数的上积分和下积分与其积分也相等. $\square$

如果 k 为常数, 则易见  $f + k$  可积当且仅当 f 可积, 且

$$
S (f + k) = S (f) + k \nu (I), s (f + k) = s (f) + k \nu (I).
$$

设 $I = [a,b]\times [c,d],\delta$ 是充分小的正数，记

$$
I ^ {\delta} = (a + \delta , b - \delta) \times (c + \delta , d - \delta),
$$

显然 $0 < \nu(I) - \nu(I^{\delta}) < 2(b - a)\delta + 2(d - c)\delta$.

定理 16.1.3 (Darboux 定理) 设 f 为矩形 I 上的有界函数, 则

$$
\lim _ {\| \mathrm{P} \| \to 0} S (\mathrm{P}) = S (f), \quad \lim _ {\| \mathrm{P} \| \to 0} s (\mathrm{P}) = s (f).
$$

证明 我们以上和为例证明第一个等式. 因为 $f$ 有界, 根据刚才的讨论, 不妨设 $0 \leqslant f \leqslant M$. 任给 $\varepsilon > 0$, 存在分割 $\mathrm{P}' = \{I_{ij}\}$, 使得 $S(\mathrm{P}') < S(f) + \frac{\varepsilon}{2}$. 设 $\delta$ 是充分小的正数, 记 $J_{\delta} = I \setminus \bigcup_{ij} I_{ij}^{\delta}$, 我们要求 $\nu(J_{\delta}) < \varepsilon (2M + 1)^{-1}$. 现在设 $\| \mathrm{P} \| < \delta$, 对于分割

P 的每一个小矩形来说 (图 16.3), 不难看出, 要么它完全含于 $J_{\delta}$, 要么它完全含于分割 $\mathrm{P}^{\prime}$ 的某个 (开) 矩形之内, 二者必居其一 (也可同时成立). 因此, P 的上和有如下估计:

$$
\begin{array}{l} S (f) \leqslant S (\mathrm{P}) \leqslant M \nu (J _ {\delta}) + S (\mathrm{P} ^ {\prime}) \\ \leqslant M \frac {\varepsilon}{2 M + 1} + S (f) + \frac {\varepsilon}{2} <   S (f) + \varepsilon . \\ \end{array}
$$

这说明  $\lim_{\|P\|\to0}S(P)=S(f).$

![](images/page_646_image_5.jpg)

<details>
<summary>natural_image</summary>

Grid of 12 empty squares with dashed borders, no text or symbols present
</details>

图16.3 矩形的内缩

有了 Darboux 定理, 下面判断有界函数可积性定理的证明和一元函数就没什么不同了.

定理 16.1.4（可积的充要条件） 设 f 为 I 上的有界函数, 则下列条件等价:

(1)  $f \in R(I)$ ;
(2) f 的上积分和下积分相等;
(3) $\lim_{\| P\| \to 0}\sum_{i,j}\omega_{ij}\nu (I_{ij}) = 0.$

(4) 任给 $\varepsilon > 0$, 存在 $I$ 的某个分割 $\mathrm{P}$, 使得

$$
S (\mathrm{P}) - s (\mathrm{P}) = \sum_ {i, j} \omega_ {i j} \nu (I _ {i j}) <   \varepsilon .
$$

对于二元函数, 下面的结果也是成立的.

定理 16.1.5 (Riemann 定理) 设 f 为 I 上的有界函数, 则  $f \in R(I)$  当且仅当任给  $\varepsilon, \eta > 0$ , 存在 I 的分割 P, 使得

$$
\sum_ {\{(i, j) | \omega_ {i j} \geqslant \eta \}} \nu (I _ {i j}) <   \varepsilon .
$$

因为闭矩形上的连续函数具有一致连续性, 我们立即得到

推论 16.1.6 设 f 为矩形 I 上的连续函数, 则  $f \in R(I)$ .

和一元函数一样, 我们可以用零测集来刻画可积函数. 设 $f$ 是定义在矩形 $I$ 上的有界函数, $x \in  I$. $f$ 在 $x$ 处的振幅定义为

$$
\omega (f, \boldsymbol {x}) = \lim _ {r \to 0 ^ {+}} \sup \{| f (\boldsymbol {x} _ {1}) - f (\boldsymbol {x} _ {2}) |: \boldsymbol {x} _ {1}, \boldsymbol {x} _ {2} \in B _ {r} (\boldsymbol {x}) \cap I \}.
$$

易见, $f$ 在 $\pmb{x}$ 处连续当且仅当 $\omega (f,\pmb {x}) = 0.$ 设 $\delta >0$ ，记

$$
D _ {f} (\delta) = \{\boldsymbol {x} \in I \mid \omega (f, \boldsymbol {x}) \geqslant \delta \},
$$

则 $f$ 的间断点 (不连续点) 全体为 $D_{f} = \bigcup_{n=1}^{\infty} D_{f}(1/n)$.

定理 16.1.7 (Lebesgue 定理) 设 f 为矩形 I 上的有界函数, 则 f 可积  $\Longleftrightarrow f$  的间断点集  $D_{f}$  为零测集.

证明 “$\Longrightarrow$” 只要证明对每一个 $\eta > 0, D_f(\eta)$ 均为零测集即可. 任给 $\varepsilon > 0$, 根据 Riemann 定理, 可取 $I$ 的分割 $\{I_{ij}\}$, 使得振幅满足 $\omega_{ij} \geqslant \eta$ 的小矩形的面积之和小于 $\frac{\varepsilon}{2}$.

设 $\delta > 0$, 记 $J_{\delta} = I \setminus \bigcup_{ij} I_{ij}^{\delta}$, 我们要求 $\nu(J_{\delta}) < \frac{\varepsilon}{2}$. 注意到当 $I_{ij}^{\delta} \cap D_f(\eta) \neq \varnothing$ 时, $\omega_{ij} \geqslant \eta$. 这说明 $D_f(\eta)$ 包含在 $J_{\delta}$ 和 $\{I_{ij} \mid I_{ij}^{\delta} \cap D_f(\eta) \neq \varnothing\}$ 的并集之中, 且它们的面积之和小于 $\varepsilon$. 由零测集的定义即知 $D_f(\eta)$ 为零测集.

“$\Longleftarrow$”设 $D_{f}$ 为零测集. 任给 $\varepsilon, \eta > 0$, 存在至多可数个开矩形 $\{I_{k}\}$, 使得

$$
D _ {f} \subseteq \bigcup_ {k \geqslant 1} I _ {k}, \quad \sum_ {k \geqslant 1} \nu (I _ {k}) <   \varepsilon .
$$

任取 $\pmb{x} \in I \setminus D_f$, 由 $f$ 在 $\pmb{x}$ 处连续可知, 存在 $r > 0$, 使得 $f$ 在 $B_r(\pmb{x}) \cap I$ 中的振幅小于 $\eta$. 显然, $\{B_r(\pmb{x}) \mid \pmb{x} \in I \setminus D_f\}$ 和 $\{I_k\}$ 形成了 $I$ 的开覆盖, 设 $\lambda$ 是它的 Lebesgue 数. 设 $\{I_{ij}\}$ 是 $I$ 的分割, 当它的模小于 $\lambda$ 时, 每一个小矩形要么完全包含于某一个 $B_r(\pmb{x})$ 中, 此时 $f$ 在此小矩形中的振幅小于 $\eta$; 要么小矩形完全包含于某一个 $I_k$ 中. 这说明

$$
\sum_ {\{(i, j) | \omega_ {i j} \geqslant \eta \}} \nu (I _ {i j}) \leqslant \sum_ {k \geqslant 1} \nu (I _ {k}) <   \varepsilon ,
$$

由 Riemann 定理即知 f 可积.

下面的推论是显然的.

推论 16.1.8 (1) 设  $f \in R(I)$ ，矩形  $J \subseteq I$ ，则  $f \in R(J)$ ;

(2) 如果矩形 $I$ 被有限个矩形 $\{J_k\}$ 所覆盖, 且 $f$ 在每个 $J_k$ 上都是可积的, 则 $f \in R(I)$.

## 习题 16.1

1. 设 I 为矩形,  $f, g \in R(I)$ , 证明:  $fg \in R(I)$ .
2. 设 $f \in R[a, b]$, $g \in R[c, d]$, 记 $h(x, y) = f(x)g(y)$. 证明: $h$ 是矩形 $I = [a, b] \times [c, d]$

上的可积函数, 且

$$
\iint_ {I} h (x, y) \mathrm{d} x \mathrm{d} y = \left(\int_ {a} ^ {b} f (x) \mathrm{d} x\right) \left(\int_ {c} ^ {d} g (y) \mathrm{d} y\right).
$$

3. 计算积分  $\iint_{[0,1]^{2}}\sin(x+y)\mathrm{d}x\mathrm{d}y.$

4. 按照定义证明: 矩形上只有有限个间断点的有界函数是 Riemann 可积的.

5. 在矩形  $[0,1]^{2}$  上定义函数 f 如下:

$$
f (x, y) = \left\{ \begin{array}{l l} \sin \frac {1}{x y}, & x y > 0, \\ 0, & x y = 0. \end{array} \right.
$$

研究 f 在 I 上是否可积.

6. 设 $f$ 是定义在矩形 $I = [a, b] \times [c, d]$ 上的函数, 对于每一个固定的 $x \in [a, b]$, $f(x, y)$ 是关于 $y$ 的单调递增函数, 且对于每一个固定的 $y \in [c, d]$, $f(x, y)$ 是关于 $x$ 的单调递增函数. 证明: $f \in R(I)$.

7. 设非负函数 f 在矩形 I 上可积, 则  $\sqrt{f}$  在 I 上也可积.

8. 设 $f$ 是 $[a, b]$ 中的一元连续函数, $\varphi: I \to [a, b]$ 为矩形 $I$ 上的可积函数, 则复合函数 $f \circ \varphi$ 为矩形 $I$ 上的可积函数.

9. 设 $f \in R[-1,1]$, 当 $x, y \in [0,1]$ 时, 记 $g(x,y) = f(x - y)$. 证明: $g \in R([0,1]^2)$.

10. 设 I, J 为矩形, 且  $I \subseteq J$ . 证明:  $\chi_{I} \in R(J)$ , 且其积分等于 I 的面积.

11. 在矩形 $I = [a, b] \times [c, d]$ 上定义 Dirichlet 函数 $D$ 为: 当 $x, y$ 均为有理数时 $D(x, y) = 1$, 否则 $D(x, y) = 0$. 证明: $D$ 不是矩形 $I$ 上的可积函数.

12. 证明: 矩形不是平面上的零测集.

## 16.2 多重积分及其基本性质

前一节关于二元函数积分的理论可以直接推广至多元函数. 在 $n$ 维欧氏空间 $\mathbb{R}^n$ 中, 考虑定义在 $n$ 维矩形 $I$ 上的函数 $f$, 其中

$$
I = [ a _ {1}, b _ {1} ] \times [ a _ {2}, b _ {2} ] \times \dots \times [ a _ {n}, b _ {n} ],
$$

$I$ 的直径 $d(I)$ 和容积(体积) $\nu (I)$ 分别为

$$
d (I) = \sqrt {(b _ {1} - a _ {1}) ^ {2} + (b _ {2} - a _ {2}) ^ {2} + \cdots + (b _ {n} - a _ {n}) ^ {2}},
$$

$$
\nu (I) = (b _ {1} - a _ {1}) (b _ {2} - a _ {2}) \dots (b _ {n} - a _ {n}).
$$

设区间  $[a_{i}, b_{i}]$  ( $i = 1, 2, \cdots, n$ ) 有分割

$$
\mathrm{P} _ {i}: a _ {i} = x _ {0} ^ {i} <   x _ {1} ^ {i} <   \dots <   x _ {m _ {i}} ^ {i} = b _ {i},
$$

这时超平面  $x_{i}=x_{j}^{i}\left(i=1,2,\cdots,n;j=0,1,\cdots,m_{i}\right)$  将 I 分割成  $m_{1}m_{2}\cdots m_{n}$  个小 n 维矩形

$$
I _ {i _ {1} i _ {2} \dots i _ {n}} = [ x _ {i _ {1} - 1} ^ {1}, x _ {i _ {1}} ^ {1} ] \times [ x _ {i _ {2} - 1} ^ {2}, x _ {i _ {2}} ^ {2} ] \times \dots \times [ x _ {i _ {n} - 1} ^ {n}, x _ {i _ {n}} ^ {n} ],
$$

$$
1 \leqslant i _ {1} \leqslant m _ {1}, 1 \leqslant i _ {2} \leqslant m _ {2}, \dots , 1 \leqslant i _ {n} \leqslant m _ {n}.
$$

这些小矩形所形成的分割记为  $P = P_{1} \times P_{2} \times \cdots \times P_{n}$ ，定义

$$
\| \mathrm{P} \| = \max _ {i _ {1} i _ {2} \dots i _ {n}} d (I _ {i _ {1} i _ {2} \dots i _ {n}}),
$$

称为分割 P 的模.

定义 16.2.1 (n 维矩形上的 Riemann 积分) 设 f 是定义在 n 维矩形 I 上的函数. 如果存在实数  $\alpha$ ，使得任给  $\varepsilon > 0$ ，均存在  $\delta > 0$ ，当  $\|P\| < \delta$  时，有

$$
\left| \sum_ {i _ {1} i _ {2} \dots i _ {n}} f (\pmb {\xi} _ {i _ {1} i _ {2} \dots i _ {n}}) \nu (I _ {i _ {1} i _ {2} \dots i _ {n}}) - \alpha \right| <   \varepsilon , \forall \pmb {\xi} _ {i _ {1} i _ {2} \dots i _ {n}} \in I _ {i _ {1} i _ {2} \dots i _ {n}},
$$

则称 $f$ 在 $I$ 上Riemann可积，简称可积，记为 $f\in R(I)$ . $\alpha$ 称为 $f$ 在 $I$ 上的积分，记为

$$
\alpha = \int_ {I} f = \int_ {I} f (\boldsymbol {x}) \mathrm{d} \boldsymbol {x} = \int \dots \int_ {I} f (x _ {1}, x _ {2}, \dots , x _ {n}) \mathrm{d} x _ {1} \mathrm{d} x _ {2} \dots \mathrm{d} x _ {n}.
$$

矩形上的多元函数的可积性理论与二元函数的可积性理论是完全类似的, 我们不重复叙述. 下面我们将被积区域做一点推广.

定义 16.2.2 (Jordan $^{①}$ 可测集) 设 $A \subset R^{n}$ 为有界集合, I 为包含 A 的矩形. 如果 A 的特征函数 $\chi_{A}$ 在 I 上可积, 则称 A 为 Jordan 可测集, $\chi_{A}$ 在 I 上的积分称为 A 的 Jordan 测度或容积, 记为 $\nu(A)$.

不难看出, 有界集合 $A$ 是否为 Jordan 可测集以及 Jordan 测度的大小与定义中矩形 $I$ 的选取无关. 如果 $A$ 本身就是一个矩形, 则其 Jordan 测度等于矩形的容积.

命题 16.2.1 设  $A \subset R^{n}$  为有界集合, 则 A 为 Jordan 可测集当且仅当其边界  $\partial A$  为零测集.

证明 取矩形 $I \supseteq \bar{A}$, 且 $\bar{A}$ 与 $I$ 的边界不相交. 易见, 特征函数 $\chi_A$ 在 $I$ 中的间断点集恰为 $\partial A$. 由 Lebesgue 定理可知 $A$ 为 Jordan 可测集当且仅当 $\partial A$ 为零测集. □注16.2.1 由 $\partial \bar{A} \subseteq \partial A$ 可知, 当 $A$ 为 Jordan 可测集时, $\bar{A}$ 也为 Jordan 可测集, 并且 $\nu(\bar{A}) = \nu(A)$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Jordan, Marie Ennemond Camille, 1838 年 1 月 5 日—1922 年 1 月 22 日, 法国数学家.</span></small>

设 $A$ 为Jordan可测集, $f: A \to \mathbb{R}$ 为有界函数, 将 $f$ 零延拓为 $\mathbb{R}^n$ 上的函数 $f_A$ 如下:

$$
f _ {A} (\boldsymbol {x}) = \left\{ \begin{array}{l l} f (\boldsymbol {x}), & \boldsymbol {x} \in A, \\ 0, & \boldsymbol {x} \in \mathbb {R} ^ {n} \setminus A. \end{array} \right.
$$

定义 16.2.3 (Jordan 可测集上的积分) 设 A 和 f 如上, I 为包含 A 的矩形. 如果  $f_{A} \in R(I)$ , 则称 f 在 A 上可积, 记为  $f \in R(A)$ , 其积分定义为  $f_{A}$  在 I 上的积分, 即

$$
\int_ {A} f = \int_ {I} f _ {A}.
$$

这个定义也和矩形 $I$ 的选取无关. 当 $A$ 本身就是矩形时, 这个定义和矩形上积分的定义是一致的. 下面的定理给出了有界函数在 Jordan 可测集上可积的判别条件.

定理 16.2.2 设 $f: A \to \mathbb{R}$ 是定义在 Jordan 可测集 $A$ 上的有界函数. 则 $f \in R(A)$ 当且仅当 $f$ 在 $A$ 中的间断点集为零测集.

证明 取矩形 $I \supseteq \bar{A}$, 且 $\bar{A}$ 与 $I$ 的边界不相交. 由定义, $f \in R(A)$ 当且仅当 $f_{A} \in R(I)$. 根据 Lebesgue 定理, $f_{A} \in R(I)$ 当且仅当 $f_{A}$ 的间断点集为零测集. 因为在 $I \setminus \bar{A}$ 中 $f_{A}$ 为零, 因此 $f_{A}$ 的间断点都在 $\bar{A}$ 中. 又由于 $\partial A$ 为零测集, 故 $f_{A}$ 可积当且仅当 $f_{A}$ 在 $\operatorname{int} A = A \setminus \partial A$ 中的间断点集为零测集. 在 $\operatorname{int} A$ 上 $f_{A} = f$, 因此 $f_{A}$ 可积当且仅当 $f$ 在 $\operatorname{int} A$ 中的间断点集是零测集, 也就是说当且仅当 $f$ 在 $A$ 中的间断点集为零测集.

下面我们考虑积分的基本性质.

命题16.2.3 设 $A \subset \mathbb{R}^n$ 为Jordan可测集, $f, g \in R(A)$, 则 $fg, |f|, \lambda f + \mu g$ 均在 $A$ 上可积, 其中 $\lambda, \mu \in \mathbb{R}$, 且

$$
\int_ {A} (\lambda f + \mu g) = \lambda \int_ {A} f + \mu \int_ {A} g.
$$

当 $f\geqslant g$ 时， $\int_{A}f\geqslant \int_{A}g.$ 特别地，有

$$
\left| \int_ {A} f \right| \leqslant \int_ {A} | f |.
$$

证明 只需在矩形中考虑即可, 留作练习.

命题 16.2.4 设 A, B 均为 Jordan 可测集, 则  $A \cap B$ ,  $A \cup B$  也为 Jordan 可测集, 且

$$
\nu (A \cup B) = \nu (A) + \nu (B) - \nu (A \cap B). \tag {16.2.1}
$$

特别地, $\nu(A \cup B) \leqslant \nu(A) + \nu(B)$. 若 $A \subseteq B$, 则 $B \setminus A$ 也为 Jordan 可测集, 且

$$
\nu (B \setminus A) = \nu (B) - \nu (A). \tag {16.2.2}
$$

特别地, 此时  $\nu(A) \leqslant \nu(B)$ .

证明 由 $\chi_{A\cap B} = \chi_A\chi_B$ 可知 $A\cap B$ 为Jordan可测集.由

$$
\chi_ {A \cup B} = \chi_ {A} + \chi_ {B} - \chi_ {A \cap B}
$$

可知 $A \cup B$ 为 Jordan 可测集, 且 (16.2.1) 式成立. 同理, 当 $A \subseteq B$ 时, 由

$$
\chi_ {B \setminus A} = \chi_ {B} - \chi_ {A}
$$

可知  $B \setminus A$  为 Jordan 可测集, 且 (16.2.2) 式成立.

推论 16.2.5 矩形不是零测集.

证明 设 $\{I_i\}$ 为至多可数个矩形, 它们覆盖了矩形 $I$. 不妨设 $\{I_i\}$ 均为开矩形. 根据有限覆盖定理, 存在有限个 $I_i (i \leqslant k)$ 使得它们仍然覆盖 $I$. 由上述命题可知

$$
\sum_ {i \leqslant k} \nu (I _ {i}) \geqslant \nu \left(\bigcup_ {i \leqslant k} I _ {i}\right) \geqslant \nu (I) > 0,
$$

特别地, I 不可能为零测集.

命题 16.2.6 A 为 Jordan 可测集且 Jordan 测度为零当且仅当任给  $\varepsilon > 0$ ，存在有限个矩形  $\{I_{i}\}$ ，使得

$$
A \subseteq \bigcup_ {i} I _ {i}, \quad \sum_ {i} \nu (I _ {i}) <   \varepsilon . \tag {16.2.3}
$$

证明 设 $\nu(A) = 0$ 取包含 $A$ 的矩形 $I$, 由 $\chi_A$ 在 $I$ 上的积分为零可知, 任给 $\varepsilon > 0$, 存在 $I$ 的分割 $\{I_k\}$, 使得

$$
\sum_ {\{i | A \cap I _ {i} \neq \varnothing \}} \nu (I _ {i}) = \sum_ {k} \left(\sup _ {I _ {k}} \chi_ {A}\right) \nu (I _ {k}) <   \varepsilon ,
$$

这说明 (16.2.3) 式成立.

反之, 如果 (16.2.3) 式对 $A$ 成立, 则对 $\bar{A}$ 也成立, 这说明 $\bar{A}$ 为零测集. 特别地, $\partial A \subseteq \bar{A}$ 为零测集, 从而 $A$ 为 Jordan 可测集. 此时

$$
\nu (A) \leqslant \nu \left(\bigcup_ {i \leqslant k} I _ {i}\right) \leqslant \sum_ {i \leqslant k} \nu (I _ {i}) <   \varepsilon ,
$$

由  $\varepsilon$  的任意性可知  $\nu(A)=0$ .

□

定理 16.2.7 (积分中值定理) 设 A 为 Jordan 可测集, $f, g \in  R\left( A\right)$ . 如果 g 在 A 上不变号, 则存在 $\mu  \in  \mathbb{R}$ , 使得

$$
\int_ {A} f g = \mu \int_ {A} g,
$$

其中 $\inf_{A}f\leqslant \mu \leqslant \sup_{A}f.$

证明 不妨假设 $g \geqslant 0$, 则

$$
(\inf _ {A} f) g (x) \leqslant f (x) g (x) \leqslant (\sup _ {A} f) g (x), \forall x \in A.
$$

积分可得

$$
(\inf _ {A} f) \int_ {A} g \leqslant \int_ {A} f g \leqslant (\sup _ {A} f) \int_ {A} g,
$$

如果 $\int_{A} g = 0$，则上式表明 $fg$ 在 $A$ 上的积分也为零，此时 $\mu$ 可任意取值。设 $\int_{A} g > 0$ 则

$$
\inf _ {A} f \leqslant \left(\int_ {A} g\right) ^ {- 1} \int_ {A} f g \leqslant \sup _ {A} f,
$$

令

$$
\mu = \left(\int_ {A} g\right) ^ {- 1} \int_ {A} f g,
$$

则  $\mu$  满足定理的要求.

推论 16.2.8 设 A 为 Jordan 可测集,  $f \in C(A)$ ,  $g \in R(A)$  且不变号. 如果 A 为道路连通的闭集, 则存在  $\xi \in A$ , 使得

$$
\int_ {A} f g = f (\pmb {\xi}) \int_ {A} g,
$$

证明 利用积分中值定理和连续函数的介值定理即可.

## 习题16.2

1. 设 $I$ 为 $n$ 维矩形, $J \subseteq I$ 为子矩形. 证明: 当 $f \in R(I)$ 时, 也有 $f \in R(J)$.
2. 设 $A$ 为 Jordan 可测集且 Jordan 测度为零, 则任何有界函数在 $A$ 上均可积且积分为零.
3. 设 $A$ 为 Jordan 可测集, $f, g \in R(A)$, 则 $\max\{f, g\}$ 和 $\min\{f, g\}$ 也在 $A$ 上可积.
4. 设 $A$ 为 Jordan 可测集, $\pmb{b} \in \mathbb{R}^n$, 记 $A + \pmb{b} = \{\pmb{x} + \pmb{b} \mid \pmb{x} \in A\}$. 证明: $A + \pmb{b}$ 也为 Jordan 可测集, 且 $\nu(A + \pmb{b}) = \nu(A)$.
5. 设 $A$ 为 Jordan 可测集, 则 $\bar{A}$ 也为 Jordan 可测集且 $\nu(\bar{A}) = \nu(A)$.

6. 设 A, B 为 Jordan 可测集且  $\nu(A \cap B) = 0$ , f 为  $A \cup B$  上的可积函数, 证明:

$$
\int_ {A \cup B} f = \int_ {A} f + \int_ {B} f.
$$

7. 设  $A_{1}, A_{2}, \cdots, A_{k}$  为 Jordan 可测集, 则  $A_{1} \cup A_{2} \cup \cdots \cup A_{k}$  为 Jordan 可测集, 且

$$
\nu \big (A _ {1} \cup A _ {2} \cup \dots \cup A _ {k} \big) = \sum_ {i = 1} ^ {k} \sum_ {1 \leqslant j _ {1} <   j _ {2} <   \dots <   j _ {i} \leqslant k} (- 1) ^ {i - 1} \nu \big (A _ {j _ {1}} \cap A _ {j _ {2}} \cap \dots \cap A _ {j _ {i}} \big).
$$

8. 设开集 $U$ 为 Jordan 可测集, $f$ 是 $U$ 上的非负连续函数且不恒为零. 证明: $f$ 在 $U$ 上的积分大于零.

9. 设开区域 $\Omega$ 为 Jordan 可测集, $f$ 是 $\Omega$ 上的连续函数. 如果任给 Jordan 可测集 $A \subseteq \Omega$, $f$ 在 $A$ 上的积分均为零, 证明: $f$ 恒等于零.

10. 设开区域 $\Omega$ 为 Jordan 可测集, $f$ 是 $\overline{\Omega}$ 上的连续函数. 如果任给 $\overline{\Omega}$ 上连续而且在 $\partial \Omega$ 上取值为零的函数 $\phi$, 都有

$$
\int_ {\Omega} f \phi = 0,
$$

证明: $f$ 恒等于零.

11. 设 $I$ 为矩形, $f$ 在 $I$ 上可积且积分大于零. 证明: 存在子矩形 $J \subseteq I$, 使得 $f$ 在 $J$ 上处处大于零.

12. 设 $I$ 为矩形, $f$ 在 $I$ 上可积且处处大于零, 证明: $f$ 在 $I$ 上的积分大于零.

13. 利用积分中值定理证明:

$$
1. 9 6 \leqslant \iint_ {| x | + | y | \leqslant 1 0} \frac {\mathrm{d} x \mathrm{d} y}{1 0 0 + \cos^ {2} x + \cos^ {2} y} <   2.
$$

14. 设 $f$ 为连续函数, 求极限

$$
\lim _ {r \to 0 ^ {+}} \frac {1}{\pi r ^ {2}} \iint_ {x ^ {2} + y ^ {2} \leqslant r ^ {2}} f (x, y)   \mathrm{d} x   \mathrm{d} y.
$$

## 16.3 重积分化为累次积分计算

我们现在讨论重积分的一个常用的计算方法, 其特点是将 n 元函数的积分化为 m 元函数的积分, 其中 m < n. 我们先以二重积分化为一元函数的积分为例加以说明.

设 $f$ 为矩形 $I = [a,b]\times [c,d]$ 上的有界函数.对于每一个固定的 $x\in [a,b],f(x,y)$ 可以看成区间 $[c,d]$ 上关于 $y$ 的函数，它在 $[c,d]$ 上的下积分和上积分分别记为 $\varphi (x)$ 和$\psi (x)$ ，这样我们就得到了定义在 $[a,b]$ 上的两个有界函数

定理16.3.1 设 $f\in R(I)$ ，则 $\varphi ,\psi \in R[a,b]$ ，且

$$
\int_ {I} f = \int_ {a} ^ {b} \varphi (x)   \mathrm{d} x = \int_ {a} ^ {b} \psi (x)   \mathrm{d} x.
$$

证明 用记号 $\mathrm{P}_1, \mathrm{P}_2$ 分别表示 $[a, b]$ 和 $[c, d]$ 的分割:

$$
\mathrm{P} _ {1}: a = x _ {0} <   x _ {1} <   \dots <   x _ {m} = b, \mathrm{P} _ {2}: c = y _ {0} <   y _ {1} <   \dots <   y _ {n} = d,
$$

$I$ 的相应分割记为 $\mathrm{P} = \mathrm{P}_1\times \mathrm{P}_2$ 因为 $f\in R(I)$ ，故任给 $\varepsilon >0$ ，存在 $\delta >0$ ，当$\| \mathrm{P}_1\| ,\| \mathrm{P}_2\| <  \delta$ 时

$$
\int_ {I} f - \varepsilon <   \sum_ {i, j} f (\pmb {\xi} _ {i j}) \nu (I _ {i j}) <   \int_ {I} f + \varepsilon , \forall \pmb {\xi} _ {i j} \in I _ {i j}.
$$

特别地, 任取  $\xi_{i} \in [x_{i-1}, x_{i}] (i = 1, 2, \cdots, m)$ , 由上式可得

$$
\begin{array}{l} \int_ {I} f - \varepsilon \leqslant \sum_ {i, j} \inf _ {\eta \in [ y _ {j - 1}, y _ {j} ]} f (\xi_ {i}, \eta) \Delta x _ {i} \Delta y _ {j} \\ \leqslant \sum_ {i, j} \sup _ {\eta \in [ y _ {j - 1}, y _ {j} ]} f (\xi_ {i}, \eta) \Delta x _ {i} \Delta y _ {j} \leqslant \int_ {I} f + \varepsilon , \\ \end{array}
$$

因为 $\sum_{j=1}^{n}\inf_{\eta\in[y_{j-1},y_j]}f(\xi_i,\eta)\Delta y_j$ 是函数 $f(\xi_i,y)$ 在 $[c,d]$ 上的 Darboux 下和, 故

$$
\sum_ {j = 1} ^ {n} \inf _ {\eta \in [ y _ {j - 1}, y _ {j} ]} f (\xi_ {i}, \eta) \Delta y _ {j} \leqslant \varphi (\xi_ {i}).
$$

同理

$$
\sum_ {j = 1} ^ {n} \sup _ {\eta \in [ y _ {j - 1}, y _ {j} ]} f (\xi_ {i}, \eta) \Delta y _ {j} \geqslant \psi (\xi_ {i}).
$$

因此我们得到

$$
\int_ {I} f - \varepsilon \leqslant \sum_ {i = 1} ^ {m} \varphi (\xi_ {i}) \Delta x _ {i} \leqslant \sum_ {i = 1} ^ {m} \psi (\xi_ {i}) \Delta x _ {i} \leqslant \int_ {I} f + \varepsilon .
$$

这说明 $\varphi$ 和 $\psi$ 在 $[a, b]$ 上均可积, 且积分等于 $f$ 在 $I$ 上的积分.

推论 16.3.2 设  $f \in R(I)$ . 如果对于每一个  $x \in [a, b]$ ，以 y 为变量的函数  $f(x, y)$  在  $[c, d]$  上均可积，则

$$
\int_ {I} f = \int_ {a} ^ {b} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y.
$$

同理, 如果对于每一个 $y \in [c, d]$, 以 $x$ 为变量的函数 $f(x, y)$ 在 $[a, b]$ 上均可积, 则

$$
\int_ {I} f = \int_ {c} ^ {d} \mathrm{d} y \int_ {a} ^ {b} f (x, y) \mathrm{d} x.
$$

推论 16.3.3 设  $f \in C(I)$ ，则有

$$
\int_ {I} f = \int_ {a} ^ {b} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y = \int_ {c} ^ {d} \mathrm{d} y \int_ {a} ^ {b} f (x, y) \mathrm{d} x,
$$

为了区别起见, 上式最左边常称为重积分, 右边称为累次积分.

对于多重积分, 类似的结果也成立. 例如, 三重积分在一定条件下可以化为关于二重积分和一重积分的累次积分.

例 16.3.1 设  $I = [0,1] \times [0,1]$ ，计算积分

$$
\iint_ {I} \frac {y \mathrm{d} x \mathrm{d} y}{(1 + x ^ {2} + y ^ {2}) ^ {\frac {3}{2}}}.
$$

解 被积函数是连续函数, 因此重积分可以化为累次积分:

$$
\begin{array}{l} \iint_ {I} \frac {y \mathrm{d} x \mathrm{d} y}{(1 + x ^ {2} + y ^ {2}) ^ {\frac {3}{2}}} = \int_ {0} ^ {1} \mathrm{d} x \int_ {0} ^ {1} \frac {y \mathrm{d} y}{(1 + x ^ {2} + y ^ {2}) ^ {\frac {3}{2}}} \\ = \int_ {0} ^ {1} \left(\frac {1}{\sqrt {1 + x ^ {2}}} - \frac {1}{\sqrt {x ^ {2} + 2}}\right) \mathrm{d} x = \ln \frac {2 + \sqrt {2}}{1 + \sqrt {3}}. \\ \end{array}
$$

例16.3.2 设 $I = [0,1] \times [0,1]$, 计算积分 $\int_{I} f$, 其中

$$
f (x, y) = \left\{ \begin{array}{l l} 1 - x - y, & x + y \leqslant 1, \\ 0, & x + y > 1. \end{array} \right.
$$

解 被积函数是连续函数, 因此重积分可以化为累次积分:

$$
\begin{array}{l} \int_ {I} f = \int_ {0} ^ {1} \mathrm{d} x \int_ {0} ^ {1} f (x, y) \mathrm{d} y \\ = \int_ {0} ^ {1} \mathrm{d} x \int_ {0} ^ {1 - x} (1 - x - y) \mathrm{d} y \\ = \int_ {0} ^ {1} \frac {1}{2} (1 - x) ^ {2} \mathrm{d} x = \frac {1}{6}. \\ \end{array}
$$

例 16.3.3 设  $I = [0,1]^{3} = [0,1] \times [0,1] \times [0,1]$ ，计算积分

$$
\iiint_ {I} \frac {\mathrm{d} x \mathrm{d} y \mathrm{d} z}{(1 + x + y + z) ^ {3}}.
$$