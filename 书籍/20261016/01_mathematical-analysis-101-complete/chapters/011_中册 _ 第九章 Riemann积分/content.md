# 中册 / 第九章 Riemann积分

原始 PDF 第 309–357 页。

## 第九章

## Riemann 积分

---

2

第九章 Riemann 积分

积分源于求弧长、面积、体积等几何问题. 物理学中求变速运动的位移问题, 求非均匀物质的质量问题等也可以转化为计算积分. 在微积分发明的早期, 人们一般认为积分是求导的逆运算, 积分本身没有独立的定义. 1821 年, Cauchy 给出了连续函数积分的定义. 1854 年, Riemann $^{①}$  在研究 Fourier $^{②}$  级数的一篇论文中给出了有界函数积分的定义. Darboux 和 Lebesgue 进一步研究了可积函数的刻画, 他们分别于 1875 年和 1904 年证明了可积函数就是 “几乎处处” 连续的有界函数.

## 9.1 Riemann 积分的定义与函数的可积性

设 $f$ 是定义在闭区间 $[a, b]$ 上的函数 (不一定连续), 考虑平面上由直线 $x = a, x = b, y = 0$ 及曲线 $y = f(x)$ 所围成的曲边梯形 (图9.1). 为了计算它的面积, 我们将曲边梯形分成若干部分, 每一部分可以近似地看成是小矩形, 这些小矩形的面积之和可以当作曲边梯形面积的近似值.

![](../../raw/pages_0305-0320/images/page_309_image_5.jpg)

<details>
<summary>text_image</summary>

y
y = f(x)
O a b x
</details>

图 9.1 曲边梯形的面积

具体说来, 我们在 $[a, b]$ 中取 $n + 1$ 个点, 依次记为 $a = x_0 < x_1 < \dots < x_n = b$, 它们将 $[a, b]$ 分成 $n$ 个小区间 $\Delta_i = [x_{i-1}, x_i] (1 \leqslant i \leqslant n)$, 这些小区间构成了 $[a, b]$ 的一个分割, 也称为分划, 记为

$$
\mathrm{P}: a = x _ {0} <   x _ {1} <   \dots <   x _ {n} = b.
$$

第 $i$ 个曲边小梯形的面积约等于 $f(\xi_i)\Delta x_i$ ，其中 $\xi_{i}\in [x_{i - 1},x_{i}],\Delta x_{i} = x_{i} - x_{i - 1}$ 整个曲边梯形的面积约等于

$$
\sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i},
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Riemann, Georg Friedrich Bernhard, 1826 年 9 月 17 日—1866 年 7 月 20 日, 德国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Fourier, Jean Baptiste Joseph, 1768 年 3 月 21 日—1830 年 5 月 16 日, 法国数学家、物理学家.</span></small>

---

9.1 Riemann 积分的定义与函数的可积性

3

上式称为 $f$ 的一个Riemann和或积分和(图9.2).

![](../../raw/pages_0305-0320/images/page_310_chart_3.jpg)

<details>
<summary>histogram</summary>

| X-axis | Frequency |
| --- | --- |
| a | \(f(\xi_i)\) |
| \(\xi_i\) | \(f(\xi_i)\) |
</details>

图9.2 Riemann和

我们期望当分割越来越细时, Riemann 和越来越接近曲边梯形的面积. 为了描述分割的精细程度, 记

$$
\| \mathrm{P} \| = \max _ {1 \leqslant i \leqslant n} \{\Delta x _ {i} \},
$$

称为分割 P 的模.

定义 9.1.1 (Riemann 积分) 设 f 是定义在区间  $[a, b]$  上的函数. 如果存在实数 I, 使得任给  $\varepsilon > 0$ , 均存在  $\delta > 0$ , 只要分割 P 满足  $\|P\| < \delta$ , 就有

$$
\left| \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} - I \right| <   \varepsilon , \forall \xi_ {i} \in [ x _ {i - 1}, x _ {i} ], i = 1, 2, \dots , n,
$$

则称 $f$ 在 $[a,b]$ 上Riemann可积(简称可积), $I$ 称为 $f$ 在 $[a,b]$ 上的（定）积分，记为

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = I = \lim _ {\| \mathrm{P} \| \to 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i}.
$$

注 9.1.1 在上述积分表达式中, $[a,b]$ 称为积分区间, a,b 分别为积分下限与积分上限, f 为被积函数, x 为积分变量. 注意, 定积分与变量 x 的表示方法无关, 即

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {b} f (t) \mathrm{d} t.
$$

例 9.1.1 设  $c \in R, f \equiv c,$  求 f 在  $[a, b]$  上的积分.

解 当 $f \equiv c$ 时, 其 Riemann 和形如

$$
\sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} = \sum_ {i = 1} ^ {n} c (x _ {i} - x _ {i - 1}) = c (x _ {n} - x _ {0}) = c (b - a),
$$

这说明

$$
\int_ {a} ^ {b} c \mathrm{d} x = c (b - a).
$$

□

---

4

第九章 Riemann积分

为了方便起见, 我们用  $f \in R[a, b]$  表示 f 在  $[a, b]$  上 Riemann 可积. 下面我们来研究什么样的函数是可积的.

定理 9.1.1（可积的必要条件） 设  $f \in R[a, b]$ ，则 f 在  $[a, b]$  上有界，反之不然.

证明 设 $f \in R[a, b]$, 记 $I$ 为其积分. 在积分的定义中, 取 $\varepsilon = 1$, 此时存在相应的 $\delta > 0$. 取定正整数 $n > \frac{b - a}{\delta}$, 对区间 $[a, b]$ 作 $n$ 等分, 则

$$
\left| \frac {b - a}{n} \sum_ {i = 1} ^ {n} f (\xi_ {i}) - I \right| <   1, \forall \xi_ {i} \in [ x _ {i - 1}, x _ {i} ], i = 1, 2, \dots , n.
$$

特别地, 当 $1 \leqslant i \leqslant n, j \neq i$ 时, 取 $\xi_{j} = x_{j}$, 则有

$$
| f (\xi_ {i}) | <   \sum_ {j \neq i} | f (x _ {j}) | + \frac {n}{b - a} (1 + | I |), \forall \xi_ {i} \in [ x _ {i - 1}, x _ {i} ].
$$

这说明 $f$ 在每一小区间 $[x_{i - 1},x_i]$ 上均有界，从而是 $[a,b]$ 上的有界函数

反之, 我们考虑在有理数上取值为 1, 在无理数上取值为 0 的 Dirichlet 函数 $D(x)$. 任给一个分割, 当 $\xi_{i}$ 都取 $[x_{i-1}, x_{i}]$ 中的无理数时, 积分和为 0; 当 $\xi_{i}$ 都取 $[x_{i-1}, x_{i}]$ 中的有理数时, 积分和为 1. 因此 $D(x)$ 的积分和没有极限. □

以下我们考虑有界函数可积的条件.如同研究有界数列的收敛性可以考虑上极限和下极限一样,我们考虑有界函数Riemann和的“最大”值和“最小”值.对于分割

$$
\mathrm{P}: a = x _ {0} <   x _ {1} <   \dots <   x _ {n} = b,
$$

记 $M_{i} = \sup_{x\in [x_{i - 1},x_{i}]}f(x),m_{i} = \inf_{x\in [x_{i - 1},x_{i}]}f(x)$ ，令

$$
S = \sum_ {i = 1} ^ {n} M _ {i} \Delta x _ {i}, s = \sum_ {i = 1} ^ {n} m _ {i} \Delta x _ {i},
$$

我们称 $S$ 为 $f$ 关于 $\mathrm{P}$ 的 Darboux 上和, 简称上和 (图 9.3(a)), 也记为 $S(\mathrm{P})$ 或 $S(\mathrm{P}, f)$; 而 $s$ 称为 Darboux 下和, 简称下和 (图 9.3(b)), 也记为 $s(\mathrm{P})$ 或 $s(\mathrm{P}, f)$.

![](../../raw/pages_0305-0320/images/page_311_image_15.jpg)

图 9.3 上和与下和

---

9.1 Riemann 积分的定义与函数的可积性

5

显然, 任何 Riemann 和总是介于下和与上和之间. 记

$$
\omega_ {i} = \omega_ {i} (f) = \sup _ {x \in [ x _ {i - 1}, x _ {i} ]} f (x) - \inf _ {x \in [ x _ {i - 1}, x _ {i} ]} f (x),
$$

称为 $f$ 在 $[x_{i - 1},x_i]$ 上的振幅.由定义，上和与下和之差可以表示为

$$
S - s = \sum_ {i = 1} ^ {n} \omega_ {i} \Delta x _ {i}.
$$

设 $f$ 为 $[a, b]$ 上的有界函数, 其上确界和下确界分别记为 $M, m$. 下面的引理给出了上和与下和关于分割的单调性质, 这与数列的情形类似.

引理 9.1.2 设分割 P' 是从 P 添加 k 个分点得到的, 则有

$$
S (\mathrm{P}) \geqslant S (\mathrm{P} ^ {\prime}) \geqslant S (\mathrm{P}) - (M - m) k \| \mathrm{P} \|,
$$

$$
s (\mathrm{P}) \leqslant s (\mathrm{P} ^ {\prime}) \leqslant s (\mathrm{P}) + (M - m) k \| \mathrm{P} \|.
$$

特别地, 往给定的分割增加新的分点时, 下和不减, 上和不增.

证明 以 $k = 1$ 的情形为例. 此时, 设新添加的分点为 $\bar{x}$, 则 $\bar{x}$ 必落在某个小区间 $(x_{j-1}, x_j)$ 内. 由上和的定义,

$$
S (\mathrm{P}) = \sum_ {i = 1} ^ {n} M _ {i} \Delta x _ {i} = M _ {j} \Delta x _ {j} + \sum_ {i \neq j} M _ {i} \Delta x _ {i},
$$

$$
S (\mathrm{P} ^ {\prime}) = M _ {j} ^ {\prime} (\bar {x} - x _ {j - 1}) + M _ {j} ^ {\prime \prime} (x _ {j} - \bar {x}) + \sum_ {i \neq j} M _ {i} \Delta x _ {i},
$$

这里 $M_j'$ 和 $M_j''$ 分别是 $f$ 在区间 $[x_{j-1},\bar{x}]$ 和 $[\bar{x},x_j]$ 上的上确界. 由 $M_j' \leqslant M_j, M_j'' \leqslant M_j$ 可得

$$
\begin{array}{l} 0 \leqslant S (\mathrm{P}) - S \left(\mathrm{P} ^ {\prime}\right) = \left(M _ {j} - M _ {j} ^ {\prime}\right) \left(\bar {x} - x _ {j - 1}\right) + \left(M _ {j} - M _ {j} ^ {\prime \prime}\right) \left(x _ {j} - \bar {x}\right) \\ \leqslant (M - m) (\bar {x} - x _ {j - 1}) + (M - m) (x _ {j} - \bar {x}) \\ = (M - m) \Delta x _ {j} \leqslant (M - m) \| \mathrm{P} \|. \\ \end{array}
$$

下和的情形可类似地证明.

推论 9.1.3 对于任意两个分割  $P_{1}$  及  $P_{2}$ ，均有  $s(\mathrm{P}_{1}) \leqslant S(\mathrm{P}_{2})$ .

证明 用 $\mathrm{P}_1 \cup \mathrm{P}_2$ 表示将 $\mathrm{P}_1$ 和 $\mathrm{P}_2$ 的所有分点合并后得到的分割 (重复的分点只取一次), 则 $\mathrm{P}_1 \cup \mathrm{P}_2$ 既可以看成由 $\mathrm{P}_1$ 添加分点, 又可以看作从 $\mathrm{P}_2$ 添加分点得到的分割. 由刚才的引理即得

$$
s (\mathrm{P} _ {1}) \leqslant s (\mathrm{P} _ {1} \cup \mathrm{P} _ {2}) \leqslant S (\mathrm{P} _ {1} \cup \mathrm{P} _ {2}) \leqslant S (\mathrm{P} _ {2}).
$$

下面的定理可以跟有界数列或有界函数的上、下极限的存在性作对比.

---

6

第九章 Riemann积分

定理 9.1.4 (Darboux)  $\lim_{\|P\|\to0}S(P)=\inf_{P}S(P),\quad\lim_{\|P\|\to0}s(P)=\sup_{P}s(P).$

证明 根据定义, 总有如下估计:

$$
m (b - a) \leqslant s (\mathrm{P}) \leqslant S (\mathrm{P}) \leqslant M (b - a),
$$

这说明  $\inf_{P} S(P)$  和  $\sup_{P} s(P)$  都存在.

根据确界的定义, 任给 $\varepsilon > 0$, 存在分割 $\mathrm{P}'$, 使得

$$
S (\mathrm{P} ^ {\prime}) <   \inf _ {\mathrm{P}} S (\mathrm{P}) + \frac {\varepsilon}{2}.
$$

设 $\mathrm{P}^{\prime}$ 由 $k$ 个分点构成. 对于任意另一分割 $\mathrm{P}, \mathrm{P} \cup \mathrm{P}^{\prime}$ 至多比 $\mathrm{P}$ 多 $k$ 个分点. 由引理9.1.2可得

$$
S (\mathrm{P}) - (M - m) k \| \mathrm{P} \| \leqslant S (\mathrm{P} \cup \mathrm{P} ^ {\prime}) \leqslant S (\mathrm{P} ^ {\prime}) <   \inf _ {\mathrm{P}} S (\mathrm{P}) + \frac {\varepsilon}{2}.
$$

于是, 当  $\|P\| < \delta = \frac{\varepsilon}{2(M - m + 1)k}$  时,

$$
\begin{array}{l} \inf _ {\mathrm{P}} S (\mathrm{P}) \leqslant S (\mathrm{P}) \leqslant \frac {(M - m) k \varepsilon}{2 (M - m + 1) k} + \inf _ {\mathrm{P}} S (\mathrm{P}) + \frac {\varepsilon}{2} \\ <   \inf _ {\mathrm{P}} S (\mathrm{P}) + \varepsilon , \\ \end{array}
$$

这就证明了上和的极限等式. 下和的极限同理可证.

我们称 $\inf_{\mathrm{P}}S(\mathrm{P})$ 为 $f$ 在 $[a,b]$ 上的上积分, $\sup_{\mathrm{P}}s(\mathrm{P})$ 为 $f$ 在 $[a,b]$ 上的下积分, 分别记为

$$
\int_ {a} ^ {\bar {b}} f (x) \mathrm{d} x = \inf _ {\mathrm{P}} S (\mathrm{P}), \quad \int_ {a} ^ {b} f (x) \mathrm{d} x = \sup _ {\mathrm{P}} s (\mathrm{P}).
$$

Riemann 和 Darboux 关于函数可积性的结果反映在下面的重要定理中.

定理 9.1.5 (可积的充要条件) 设 f 为  $[a, b]$  上的有界函数, 则以下命题等价:

(1) $f \in R[a, b]$.
(2) f 在  $[a, b]$  上的上积分和下积分相等.
(3) $\lim_{\| \mathrm{P}\| \to 0}\sum_{i = 1}^{n}\omega_{i}\Delta x_{i} = 0.$

(4) 任给 $\varepsilon > 0$, 存在 $[a, b]$ 的某个分割 $P$, 使得

$$
S (\mathrm{P}) - s (\mathrm{P}) = \sum_ {i = 1} ^ {n} \omega_ {i} \Delta x _ {i} <   \varepsilon .
$$

证明 (1) $\Longrightarrow$ (2): 设 $f \in R[a, b]$, 其积分记为 $I$. 于是任给 $\varepsilon > 0$, 存在 $\delta > 0$, 当 $\|P\| < \delta$ 时

$$
I - \varepsilon <   \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} <   I + \varepsilon .
$$

---

9.1 Riemann积分的定义与函数的可积性

7

特别地, 我们有

$$
\begin{array}{l} I - \varepsilon \leqslant \sum_ {i = 1} ^ {n} \inf _ {x \in [ x _ {i - 1}, x _ {i} ]} f (x) \Delta x _ {i} = s (\mathrm{P}) \\ \leqslant \sum_ {i = 1} ^ {n} \sup _ {x \in \left[ x _ {i - 1}, x _ {i} \right]} f (x) \Delta x _ {i} = S (\mathrm{P}) \\ \leqslant I + \varepsilon, \\ \end{array}
$$

这说明 $\lim_{\| \mathrm{P}\| \to 0}s(\mathrm{P}) = \lim_{\| \mathrm{P}\| \to 0}S(\mathrm{P}) = I.$ 由Darboux定理即知 $f$ 的上、下积分相等.

(2) $\Longrightarrow$ (1): 设 $\sup_{\mathrm{P}} s(\mathrm{P}) = \inf_{\mathrm{P}} S(\mathrm{P}) = I$. 由 Darboux 定理, 任给 $\varepsilon > 0$, 存在 $\delta > 0$, 当 $\| \mathrm{P} \| < \delta$ 时, 有

$$
I - \varepsilon <   s (\mathrm{P}) \leqslant \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} \leqslant S (\mathrm{P}) <   I + \varepsilon ,
$$

这说明 $\lim_{\| \mathrm{P}\| \to 0}\sum_{i = 1}^{n}f(\xi_i)\Delta x_i = I,$ 也就是说 $f$ 在 $[a,b]$ 上可积且积分为 $I$

(2)  $\Longleftrightarrow$  (3): 这可由 Darboux 定理及下式得到,

$$
\lim _ {\| \mathrm{P} \| \to 0} \sum_ {i = 1} ^ {n} \omega_ {i} \Delta x _ {i} = \lim _ {\| \mathrm{P} \| \to 0} (S (\mathrm{P}) - s (\mathrm{P})) = \inf _ {\mathrm{P}} S (\mathrm{P}) - \sup _ {\mathrm{P}} s (\mathrm{P}).
$$

(3) $\Longrightarrow$ (4): 这是显然的.
(4)  $\Longrightarrow$  (2): 如果存在分割 P, 使得  $S(\mathrm{P}) - s(\mathrm{P}) < \varepsilon$ , 则由

$$
s (\mathrm{P}) \leqslant \sup _ {\mathrm{P} ^ {\prime}} s (\mathrm{P} ^ {\prime}) \leqslant \inf _ {\mathrm{P} ^ {\prime}} S (\mathrm{P} ^ {\prime}) \leqslant S (\mathrm{P})
$$

可知

$$
0 \leqslant \inf _ {\mathrm{P} ^ {\prime}} S (\mathrm{P} ^ {\prime}) - \sup _ {\mathrm{P} ^ {\prime}} s (\mathrm{P} ^ {\prime}) \leqslant S (\mathrm{P}) - s (\mathrm{P}) <   \varepsilon .
$$

由 $\varepsilon$ 的任意性即知 $f$ 的上积分与下积分相等.

推论 9.1.6 (1) 设  $[\alpha, \beta] \subseteq [a, b]$ ，若  $f \in R[a, b]$ ，则  $f \in R[\alpha, \beta]$ .

(2) 设 $c \in (a, b)$, 若 $f \in R[a, c]$ 且 $f \in R[c, b]$, 则 $f \in R[a, b]$.

证明 (1) 由上述定理中的 (3), 任给 $\varepsilon > 0$, 存在 $\delta > 0$, 当 $[a, b]$ 的分割 $\mathbf{P}$ 满足 $\| \mathbf{P} \| < \delta$ 时, $\sum_{i=1}^{n} \omega_i \Delta x_i < \varepsilon$. 取 $[\alpha, \beta]$ 的一个分割 $\mathrm{P}'$, 使得 $\| \mathrm{P}' \| < \delta$. 显然, 可构造 $[a, b]$ 的分割 $\mathbf{P}$, 使得 $\mathbf{P}$ 是 $\mathrm{P}'$ 通过添加 $[a, b] \setminus [\alpha, \beta]$ 中的分点得到, 且 $\| \mathbf{P} \| < \delta$. 此时 $f$ 在 $[\alpha, \beta]$ 中的上和与下和之差不超过 $f$ 在 $[a, b]$ 中的上和与下和之差, 从而小于 $\varepsilon$. 由上述定理中的 (4) 即知 $f$ 在 $[\alpha, \beta]$ 上可积.

(2) 用上述定理中的 (4) 很容易证明, 略.

---

8

第九章 Riemann 积分

命题 9.1.7 (可积函数的运算性质) 设  $f, g \in R[a, b]$ ,  $\lambda, \mu \in R$ , 则有

(1) $\lambda f + \mu g \in R[a, b]$.
(2) $fg \in R[a, b]$.
(3) $|f|, |g| \in R[a, b]$. 如果 $|g|$ 有正下界, 则 $f / g \in R[a, b]$ 也成立.

证明 (1) 这可以从积分的定义直接得出.

(2) 根据定理 9.1.1, 存在 K > 0, 使得  $|f|, |g| \leqslant K$  处处成立. 由定理 9.1.5 (3), 任给  $\varepsilon > 0$ , 存在  $\delta > 0$ , 当  $\|P\| < \delta$  时,

$$
\sum_ {i = 1} ^ {n} \omega_ {i} (f) \Delta x _ {i} <   \frac {\varepsilon}{2 K + 1}, \quad \sum_ {i = 1} ^ {n} \omega_ {i} (g) \Delta x _ {i} <   \frac {\varepsilon}{2 K + 1}.
$$

当 $x, y \in [x_{i-1}, x_i]$ 时，

$$
\begin{array}{l} \left| f (x) g (x) - f (y) g (y) \right| \leqslant \left| f (x) (g (x) - g (y)) \right| + \left| (f (x) - f (y)) g (y) \right| \\ \leqslant K (\omega_ {i} (g) + \omega_ {i} (f)), \\ \end{array}
$$

这说明 $\omega_{i}(fg) \leqslant K(\omega_{i}(g) + \omega_{i}(f))$，从而有

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} \omega_ {i} (f g) \Delta x _ {i} \leqslant K \sum_ {i = 1} ^ {n} (\omega_ {i} (f) + \omega_ {i} (g)) \Delta x _ {i} \\ <   \frac {K \varepsilon}{2 K + 1} + \frac {K \varepsilon}{2 K + 1} <   \varepsilon . \\ \end{array}
$$

由定理 9.1.5 知 fg 可积.

(3) 由 $\omega_{i}(|f|) \leqslant \omega_{i}(f)$ 可知 $|f|$ 可积. 当 $|g|$ 有正下界时, 不妨设 $|g| \geqslant L > 0$. 此时, 由

$$
\left| \frac {1}{g (x)} - \frac {1}{g (y)} \right| = \frac {| g (x) - g (y) |}{| g (x) g (y) |}
$$

可得 $\omega_{i}(1 / g)\leqslant L^{-2}\omega_{i}(g)$ ，由此可知 $1 / g$ 可积.再由(2）即知 $f / g$ 可积

命题 9.1.8 (可积函数类) (1) 若有界函数 f 只在  $[a, b]$  上的有限个点处不连续，则 f 可积.

(2) 若 f 为  $[a, b]$  上的单调函数, 则 f 可积.

证明 (1) 我们用定理 9.1.5 (4) 来证明. 设  $\bar{x}_{k} (k=1,2,\cdots,N)$  为 f 的间断点. 任给  $\varepsilon>0$ , 取  $0<\rho<\frac{\varepsilon}{4(M-m+1)N}$ , 使得  $\{(\bar{x}_{k}-\rho,\bar{x}_{k}+\rho)\}$  互不相交. 去掉这些开区间后, [a,b] 剩下的部分由有限个闭区间组成, 且 f 在这些闭区间中连续. 根据一致连续性的 Cantor 定理, 可以取这些闭区间的分割, 使得 f 在每个闭区间上的振幅均小于  $\frac{\varepsilon}{2(b-a)}$ . 这些闭区间的分割连同  $\{[\bar{x}_{k}-\rho,\bar{x}_{k}+\rho]\cap[a,b]\}$  构成了 [a,b] 的分割, 记

---

9.1 Riemann积分的定义与函数的可积性

9

为 P. 对于此分割, 有

$$
\begin{array}{l} S (\mathrm{P}) - s (\mathrm{P}) \leqslant \frac {\varepsilon}{2 (b - a)} (b - a) + (M - m) \sum_ {i = 1} ^ {N} 2 \rho \\ \leqslant \frac {\varepsilon}{2} + (M - m) \frac {2 N \varepsilon}{4 (M - m + 1) N} <   \varepsilon . \\ \end{array}
$$

由定理 9.1.5 (4) 知 f 可积.

(2) 不妨设 $f$ 单调递增. 任给 $\varepsilon > 0$, 取 $[a, b]$ 的分割 $\mathrm{P}$, 使得 $\| \mathrm{P} \| < \frac{\varepsilon}{f(b) - f(a) + 1}$, 则

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} \omega_ {i} \Delta x _ {i} = \sum_ {i = 1} ^ {n} (f (x _ {i}) - f (x _ {i - 1})) \Delta x _ {i} \\ \leqslant \sum_ {i = 1} ^ {n} \left(f (x _ {i}) - f (x _ {i - 1})\right) \frac {\varepsilon}{f (b) - f (a) + 1} \\ = (f (x _ {n}) - f (x _ {0})) \frac {\varepsilon}{f (b) - f (a) + 1} \\ = (f (b) - f (a)) \frac {\varepsilon}{f (b) - f (a) + 1} <   \varepsilon , \\ \end{array}
$$

由定理 9.1.5 (4) 知 f 可积.

设 $f$ 为 $[a,b]$ 上定义的函数, 如果存在 $[a,b]$ 的分割

$$
\mathrm{P}: a = x _ {0} <   x _ {1} <   x _ {2} <   \dots <   x _ {n} = b,
$$

使得 $f$ 在每一个小区间 $(x_{i - 1},x_i)$ 内均为常数，则称 $f$ 为阶梯函数. 阶梯函数最多只有有限个间断点，因此是可积函数.

## 习题 9.1

1. 利用积分的几何含义写出下列积分的值:

(1) $\int_{a}^{b}\left|x - \frac{a + b}{2}\right|\mathrm{d}x;$

(2) $\int_{a}^{b}\sqrt{(x - a)(b - x)}\mathrm{d}x.$

2. 设 $f \in R[a, b]$, 证明:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \lim _ {n \to \infty} \frac {b - a}{n} \sum_ {k = 1} ^ {n} f \Big (a + \frac {k}{n} (b - a) \Big).
$$

3. 设 $b > a > 0, f \in R[a, b]$, 证明:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \lim _ {n \to \infty} \frac {\ln b - \ln a}{n} \sum_ {k = 1} ^ {n} a ^ {\frac {n - k}{n}} b ^ {\frac {k}{n}} f \big (a ^ {\frac {n - k}{n}} b ^ {\frac {k}{n}} \big).
$$

---

10

第九章 Riemann 积分

4. 设 b > a > 0, 用定义计算下列积分:

(1) $\int_{a}^{b} x \, \mathrm{d}x$;

(2) $\int_{a}^{b}\frac{1}{x^2}\mathrm{d}x.$

5. 判断下列函数在  $[0,1]$  上的可积性:

(1) $f(x) = \left\{ \begin{array}{ll} - 1, & x\in \mathbb{Q},\\ 1, & x\in \mathbb{R}\setminus \mathbb{Q}; \end{array} \right.$

(2) $f(x) = \left\{ \begin{array}{ll}x, & x\in \mathbb{Q},\\ 0, & x\in \mathbb{R}\setminus \mathbb{Q}; \end{array} \right.$

(3) $f(x) = \left\{ \begin{array}{ll}\operatorname {sgn}\Big(\sin \frac{\pi}{x}\Big), & x\neq 0,\\ 0, & x = 0; \end{array} \right.$

(4) $f(x) = \left\{ \begin{array}{ll}\frac{1}{x} -\left[\frac{1}{x}\right], & x\neq 0,\\ 0, & x = 0. \end{array} \right.$

6. 设 $f \in R[a, b], c \in \mathbb{R}$, 证明:

$$
\int_ {a - c} ^ {b - c} f (x + c) \mathrm{d} x = \int_ {a} ^ {b} f (x) \mathrm{d} x.
$$

7. 设 $f \in R[a, b]$, $g$ 与 $f$ 只在有限个点处取值不同, 证明: $g \in R[a, b]$, 且

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {b} g (x) \mathrm{d} x.
$$

8. 设 $f$ 是定义在 $[a, b]$ 上的函数，记 $f^{+} = \max\{f, 0\}$，$f^{-} = \max\{-f, 0\}$. 证明:$f \in R[a, b]$ 当且仅当 $f^{+}, f^{-} \in R[a, b]$.

9. 设 $f, g \in R[a, b]$, 证明: $\max \{f, g\}, \min \{f, g\} \in R[a, b]$.

10. 设 $f \in R[a, b]$, 证明: $\mathrm{e}^f \in R[a, b]$.

11. 设 $f \in R[a, b]$ 且 $f \geqslant c > 0$, 证明: $\ln f \in R[a, b]$.

12. 设 $f$ 为 $[a, b]$ 上的有界函数, 证明: 如果其间断点集 $D_f$ 只有有限个聚点, 则 $f \in R[a, b]$.

## 9.2 可积性的进一步刻画

从前一节中的讨论我们知道, 只有有限个间断点的有界函数必为可积函数. 在积分理论发展的早期, 人们认为这已经是关于可积性判断的最好的结果之一. 后来 Riemann 出人意料地用级数构造了一个具有可数个间断点的可积函数. 另一个具有类似特点的函数是 Riemann 函数 $R$, 它在 $[0,1]$ 上定义为

---

9.2 可积性的进一步刻画

11

$$
R (x) = \left\{ \begin{array}{l l} { \frac {1}{q},} & {x =  \frac {p}{q} \in (0, 1), p, q \text {为互素的正整数},} \\ {1,} & {x = 0, 1,} \\ {0,} & {x \in (0, 1) \text {为无理数}.} \end{array} \right.
$$

显然, $0 \leqslant R(x) \leqslant 1$. 任给 $\varepsilon > 0$, 当 $\frac{1}{q} \geqslant \frac{\varepsilon}{2}$, 即 $q \leqslant \frac{2}{\varepsilon}$ 时, $[0,1]$ 中形如 $\frac{p}{q}$ 的既约分数不超过 $N = N(\varepsilon)$ 个. 取 $\delta = \frac{\varepsilon}{4N}$, 对于 $\|P\| < \delta$ 的任意分割, 包含上述既约分数的小区间至多只有 $2N$ 个, 在其余的小区间上 $R(x)$ 的取值均小于 $\frac{\varepsilon}{2}$, 因此

$$
0 \leqslant \sum_ {i} R (\xi_ {i}) \Delta x _ {i} \leqslant 2 N \| \mathrm{P} \| + \frac {\varepsilon}{2} \sum_ {i} \Delta x _ {i} \leqslant \varepsilon ,
$$

这说明 $R$ 在 $[0,1]$ 上可积, 且积分为零. 注意, $R$ 具有可数个间断点, 事实上它在有理点处均不连续.

从上面的讨论中可以体会到, 要说明一个有界函数 $f$ 为可积函数, 我们只要找到某个分割, 使得要么 $f$ 在此分割中的小区间上的振幅很小, 要么振幅较大的那些小区间的总长度很小. 这可以总结为下面的结果.

定理 9.2.1 (Riemann) 设 f 为  $[a, b]$  上的有界函数, 则 f 可积当且仅当任给  $\varepsilon$ ,  $\eta > 0$ , 存在  $[a, b]$  的某个分割 P, 使得

$$
\sum_ {\{i | \omega_ {i} \geqslant \eta \}} \Delta x _ {i} <   \varepsilon .
$$

证明 (必要性) 设 $f$ 可积. 由定理9.1.5(4), 任给 $\varepsilon, \eta > 0$, 存在分割 $\mathrm{P}$, 使得

$$
\sum_ {i = 1} ^ {n} \omega_ {i} \Delta x _ {i} <   \varepsilon \eta .
$$

这说明

$$
\eta \sum_ {\{i | \omega_ {i} \geqslant \eta \}} \Delta x _ {i} \leqslant \sum_ {i = 1} ^ {n} \omega_ {i} \Delta x _ {i} <   \varepsilon \eta ,
$$

即有 $\sum_{\{i|\omega_i\geqslant \eta \}}\Delta x_i <   \varepsilon .$

(充分性) 由已知条件, 任给 $\varepsilon > 0$, 存在 $[a, b]$ 的分割 P, 使得

$$
\sum_ {\{i | \omega_ {i} \geqslant \frac {\varepsilon}{2 (b - a)} \}} \Delta x _ {i} <   \frac {\varepsilon}{2 (M - m + 1)}.
$$

对于这个分割, 有

$$
\sum_ {i = 1} ^ {n} \omega_ {i} \Delta x _ {i} = \sum_ {\{i | \omega_ {i} <   \frac {\epsilon}{2 (b - a)} \}} \omega_ {i} \Delta x _ {i} + \sum_ {\{i | \omega_ {i} \geqslant \frac {\epsilon}{2 (b - a)} \}} \omega_ {i} \Delta x _ {i}
$$

---

12

第九章 Riemann 积分

$$
\begin{array}{l} \leqslant \frac {\varepsilon}{2 (b - a)} \sum_ {\{i | \omega_ {i} <   \frac {\varepsilon}{2 (b - a)} \}} \Delta x _ {i} + (M - m) \sum_ {\{i | \omega_ {i} \geqslant \frac {\varepsilon}{2 (b - a)} \}} \Delta x _ {i} \\ \leqslant \frac {\varepsilon}{2 (b - a)} (b - a) + \frac {(M - m) \varepsilon}{2 (M - m + 1)} <   \varepsilon . \\ \end{array}
$$

由定理 9.1.5 (4) 知 f 可积.

例9.2.1 设 $f \in C[a, b]$, $\varphi \in R[\alpha, \beta]$ 且 $\varphi([\alpha, \beta]) \subseteq [a, b]$. 证明: $f \circ \varphi \in R[\alpha, \beta]$.

证明 由 Cantor 定理, 任给 $\varepsilon > 0$, 存在 $\delta > 0$, 当 $x, y \in [a, b]$ 且 $|x - y| < \delta$ 时, $|f(x) - f(y)| < \frac{\varepsilon}{2(\beta - \alpha)}$. 因为 $\varphi$ 在 $[\alpha, \beta]$ 上可积, 由定理 9.2.1, 存在 $[\alpha, \beta]$ 的分割

$$
\mathrm{P}: \alpha = t _ {0} <   t _ {1} <   \dots <   t _ {m} = \beta,
$$

使得 $\sum_{\{i|\omega_i(\varphi)\geqslant \delta \}}\Delta t_i <   \frac{\varepsilon}{4K + 1}$ ，其中 $K$ 是 $|f|$ 在 $[a,b]$ 上的最大值.于是

$$
\begin{array}{l} \sum_ {i = 1} ^ {m} \omega_ {i} (f \circ \varphi) \Delta t _ {i} = \sum_ {\{i | \omega_ {i} (\varphi) \geqslant \delta \}} \omega_ {i} (f \circ \varphi) \Delta t _ {i} + \sum_ {\{i | \omega_ {i} (\varphi) <   \delta \}} \omega_ {i} (f \circ \varphi) \Delta t _ {i} \\ \leqslant 2 K \sum_ {\{i | \omega_ {i} (\varphi) \geqslant \delta \}} \Delta t _ {i} + \frac {\varepsilon}{2 (\beta - \alpha)} \sum_ {\{i | \omega_ {i} (\varphi) <   \delta \}} \Delta t _ {i} \\ \leqslant 2 K \frac {\varepsilon}{4 K + 1} + \frac {\varepsilon}{2 (\beta - \alpha)} (\beta - \alpha) <   \varepsilon . \\ \end{array}
$$

由定理 9.1.5 (4) 可知  $f \circ \varphi$  在  $[\alpha, \beta]$  上可积.

我们知道, 函数在某一点处是否连续可以用它在这一点处的振幅是否为零来刻画. 上述 Riemann 定理提醒我们, 可积函数振幅较大的地方不会太多, 因此可积函数不会有太多的间断点. 为了准确地刻画这种现象, 我们引入如下定义.

定义 9.2.1 (零测集) 设  $A \subseteq R$ ，如果任给  $\varepsilon > 0$ ，均存在覆盖 A 的至多可数个开区间  $\{I_{i}\}$ ，使得

$$
\sum_ {i \geqslant 1} | I _ {i} | \leqslant \varepsilon ,
$$

则称 A 为零测集.

例 9.2.2 证明: (1) 有限集是零测集. (2) 可数集是零测集. (3) 零测集的子集仍为零测集. (4) 可数个零测集之并仍为零测集.

证明 (1) 设 $A = \{x_{i}\}_{i=1}^{n}$ 为有限点集, 任给 $\varepsilon > 0$, 记

$$
I _ {i} = \left(x _ {i} - \frac {\varepsilon}{2 n}, x _ {i} + \frac {\varepsilon}{2 n}\right), i = 1, 2, \dots , n.
$$

显然, $\{I_i\}$ 组成了 $A$ 的一个覆盖, 且这些开区间的长度之和为

$$
\sum_ {i = 1} ^ {n} | I _ {i} | = \sum_ {i = 1} ^ {n} 2 \frac {\varepsilon}{2 n} = \varepsilon ,
$$

---

9.2 可积性的进一步刻画

13

因此 A 为零测集.

(2) 设 $A = \{x_{i}\}_{i=1}^{\infty}$ 为可数点集, 任给 $\varepsilon > 0$, 记

$$
I _ {i} = \left(x _ {i} - \frac {\varepsilon}{2 ^ {i + 1}}, x _ {i} + \frac {\varepsilon}{2 ^ {i + 1}}\right), i = 1, 2, \dots .
$$

显然， $\{I_{i}\}$  组成了 A 的一个覆盖，且

$$
\sum_ {i = 1} ^ {\infty} | I _ {i} | = \sum_ {i = 1} ^ {\infty} 2 \frac {\varepsilon}{2 ^ {i + 1}} \leqslant \varepsilon ,
$$

因此 A 为零测集.

(3) 按定义, 这是显然的.

(4) 设 $A_{i} (i \geqslant 1)$ 为一列零测集. 于是任给 $\varepsilon > 0$, 对于每一个 $i$, 存在覆盖 $A_{i}$ 的开区间 $\{I_{ij}\}$, 使得 $\{I_{ij}\}$ 中任意有限个区间的长度之和均不超过 $\frac{\varepsilon}{2^{i}}$. 由于可数个可数集的并集仍是可数的, 故所有这些开区间 $\{I_{ij}\}$ 仍组成了 $\{A_{i}\}$ 的并集的覆盖, 且任意有限个开区间的长度和不超过

$$
\frac {\varepsilon}{2} + \frac {\varepsilon}{2 ^ {2}} + \frac {\varepsilon}{2 ^ {3}} + \dots \leqslant \varepsilon .
$$

因此  $\{A_{i}\}$  的并集仍为零测集.

设 $f$ 为 $[a,b]$ 上的有界函数, 它在 $x \in [a,b]$ 处的振幅为

$$
\omega (f, x) = \lim _ {r \to 0 ^ {+}} \sup \{| f (x _ {1}) - f (x _ {2}) | | x _ {1}, x _ {2} \in (x - r, x + r) \cap [ a, b ] \}.
$$

f 的间断点的全体记为  $D_{f}$ ，则

$$
D _ {f} = \{x \in [ a, b ] \mid \omega (f, x) > 0 \}.
$$

当 $\delta > 0$ 时, 记

$$
D _ {f} (\delta) = \{x \in [ a, b ] \mid \omega (f, x) \geqslant \delta \},
$$

则

$$
D _ {f} = \bigcup_ {n = 1} ^ {\infty} D _ {f} (1 / n). \tag {9.2.1}
$$

定理 9.2.2 (Lebesgue) 设 f 为  $[a, b]$  上的有界函数，则  $f \in R[a, b]$  当且仅当其间断点集  $D_{f}$  为零测集.

证明 (必要性) 设 $f \in R[a, b]$. 固定 $\delta > 0$. 根据 Riemann 定理, 任给 $\varepsilon > 0$, 存在 $[a, b]$ 的分割

$$
\mathrm{P}: a = x _ {0} <   x _ {1} <   \dots <   x _ {n} = b,
$$

---

14

第九章 Riemann 积分

使得

$$
\sum_ {i = 1} ^ {n} \omega_ {i} \Delta x _ {i} <   \varepsilon \frac {\delta}{2}.
$$

如果 $x \in D_f(\delta) \cap (x_{i-1}, x_i)$, 则显然 $\omega_i \geqslant \omega(f, x) \geqslant \delta$. 因此从上式可得

$$
\sum_ {\{i | D _ {f} (\delta) \cap (x _ {i - 1}, x _ {i}) \neq \varnothing \}} \Delta x _ {i} <   \frac {\varepsilon}{2}.
$$

显然

$$
D _ {f} (\delta) \subseteq \left(\bigcup_ {\{i | D _ {f} (\delta) \cap (x _ {i - 1}, x _ {i}) \neq \varnothing \}} (x _ {i - 1}, x _ {i})\right) \cup \left(\bigcup_ {i = 0} ^ {n} \left(x _ {i} - \frac {\varepsilon}{4 (n + 1)}, x _ {i} + \frac {\varepsilon}{4 (n + 1)}\right)\right),
$$

且

$$
\sum_ {\{i | D _ {f} (\delta) \cap (x _ {i - 1}, x _ {i}) \neq \varnothing \}} \Delta x _ {i} + \frac {2 \varepsilon}{4 (n + 1)} (n + 1) <   \frac {\varepsilon}{2} + \frac {\varepsilon}{2} = \varepsilon ,
$$

由定义即知 $D_{f}(\delta)$ 为零测集. 由(9.2.1)式可知 $D_{f}$ 为零测集

(充分性) 任给 $\varepsilon, \eta > 0$, 由 $D_{f}$ 为零测集可知, 存在开区间 $\{(\alpha_{j}, \beta_{j})\}_{j \geqslant 1}$, 使得

$$
D _ {f} \subseteq \bigcup_ {j \geqslant 1} (\alpha_ {j}, \beta_ {j}), \quad \sum_ {j \geqslant 1} (\beta_ {j} - \alpha_ {j}) <   \varepsilon .
$$

当 $x \in [a, b] \setminus \bigcup_{j \geqslant 1} (\alpha_j, \beta_j)$ 时, $f$ 在 $x$ 处连续, 故存在包含 $x$ 的开区间 $I_x$, 使得 $f$ 在 $I_x$ 上的振幅小于 $\eta$. 根据Lebesgue覆盖引理, 可取 $[a, b]$ 的分割

$$
\mathrm{P}: a = x _ {0} <   x _ {1} <   \dots <   x _ {n} = b,
$$

使得每一个小区间 $[x_{i - 1},x_i]$ 必含于某个 $(\alpha_{j},\beta_{j})$ 或某个 $I_{x}$ 之中.此时

$$
\sum_ {\{i | \omega_ {i} \geqslant \eta \}} \Delta x _ {i} \leqslant \sum_ {j \geqslant 1} (\beta_ {j} - \alpha_ {j}) <   \varepsilon ,
$$

由 Riemann 定理可知 $f \in R[a, b]$.

## 习题9.2

1. 请说明在零测集的定义中可以将“开区间”换成“闭区间”.
2. 利用 Lebesgue 定理重新证明命题 9.1.7 和例 9.2.1.
3. 设 $f$ 为定义在 $[a, b]$ 上的函数, 证明: 若 $f^2 \in R[a, b]$, 则 $|f| \in R[a, b]$.
4. 设 $f \in R[a, b]$, 如果 $f$ 处处大于零, 证明: $f$ 在 $[a, b]$ 上的积分也大于零.

---

9.3 微积分基本定理

15

5. 设 $A \subseteq \mathbb{R}$, 考虑 $A$ 的特征函数 $\chi_A: \mathbb{R} \to \mathbb{R}$:

$$
\chi_ {A} (x) = \left\{ \begin{array}{l l} 1, & x \in A, \\ 0, & x \in \mathbb {R} \setminus A. \end{array} \right.
$$

如果 $A$ 为闭的零测集, 证明: $\chi_A$ 在任何闭区间上均可积且积分等于零.

6. 设 $a, b \in \mathbb{R}, a < b$. 证明: 区间 $[a, b]$ 不是零测集.

7. 设 $f, g \in R[a, b]$, 如果 $f$ 与 $g$ 只在一个零测集上不相等, 证明: 它们的积分相等.

8. 设 $f \in R[a, b]$, $g$ 为有界函数且与 $f$ 只在一个闭的零测集上不相等, 证明: $g \in R[a, b]$.

9. 有理数的全体记为 $\{r_n\}_{n=1}^{\infty}$. 令

$$
U = \bigcup_ {n = 1} ^ {\infty} \left(r _ {n} - 2 ^ {- n}, r _ {n} + 2 ^ {- n}\right),
$$

问: $\mathbb{R} \setminus U$ 是否为零测集? 请说明理由.

## 9.3 微积分基本定理

从历史上来看, 积分概念的形成先于微分概念, 但积分的通用计算方法却直到 17 世纪中叶才由 Newton 和 Leibniz 所发现.

定理 9.3.1 (Newton-Leibniz 公式) 设 F 在  $[a, b]$  上可导且  $f = F' \in R[a, b]$ , 则

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = F (b) - F (a). \tag {9.3.1}
$$

证明 设 n 为正整数, 将  $[a, b]$  作 n 等分, 分点记为  $\{x_{i}\}_{i=0}^{n}$ . 当  $i = 1, 2, \cdots, n$  时, 由 Lagrange 微分中值定理可知, 存在  $\xi_{i} \in [x_{i-1}, x_{i}]$ , 使得

$$
F (x _ {i}) - F (x _ {i - 1}) = F ^ {\prime} (\xi_ {i}) (x _ {i} - x _ {i - 1}) = f (\xi_ {i}) \Delta x _ {i}.
$$

此时有

$$
\sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} = \sum_ {i = 1} ^ {n} (F (x _ {i}) - F (x _ {i - 1})) = F (x _ {n}) - F (x _ {0}) = F (b) - F (a).
$$

令 $n\to \infty$ ，由 $f\in R[a,b]$ 即得(9.3.1)式

---

16

第九章 Riemann积分

注 9.3.1 只要 F 连续, 至多在有限个点处不可导, 且  $F' \in R[a, b]$ , 则定理结论仍成立. 这只要将  $[a, b]$  分成有限个小区间, 然后在每一个小区间中运用 Newton-Leibniz 公式即可.

推论 9.3.2 设 $F \in  {C}^{1}\left\lbrack  {a,b}\right\rbrack$ ,则

$$
\int_ {a} ^ {b} F ^ {\prime} (x) \mathrm{d} x = F (b) - F (a). \tag {9.3.2}
$$

证明 当 $F \in C^{1}[a, b]$ 时 $F' \in C[a, b]$, 因此 $F' \in R[a, b]$, 由上述定理即得欲证结论. $\square$

注9.3.2 我们经常用记号 $F\big|_{a}^{b}$ 表示 $F(b) - F(a)$.

有了 Newton-Leibniz 公式, 要计算某个函数的积分, 只要能求出该函数的原函数即可. 为了研究原函数的存在性, 我们先来介绍积分的几个基本性质.

为了方便起见, 我们约定

当 $a = b$ 时， $\int_{a}^{b}f(x)\mathrm{d}x = 0;$ 当 $a <   b$ 时， $\int_{b}^{a}f(x)\mathrm{d}x = -\int_{a}^{b}f(x)\mathrm{d}x.$

定理 9.3.3 (1) 设 $f, g \in  R\left\lbrack  {a,b}\right\rbrack  ,\lambda ,\mu  \in  \mathbb{R}$ ,则

$$
\int_ {a} ^ {b} (\lambda f + \mu g) \mathrm{d} x = \lambda \int_ {a} ^ {b} f (x) \mathrm{d} x + \mu \int_ {a} ^ {b} g (x) \mathrm{d} x.
$$

(2) 设 $f \in R[a, b]$, $c \in (a, b)$, 则

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {c} f (x) \mathrm{d} x + \int_ {c} ^ {b} f (x) \mathrm{d} x.
$$

证明 (1) 任给 $\varepsilon > 0$, 由 $f, g$ 可积知, 存在 $\delta > 0$, 当 $[a, b]$ 的分割 $\mathrm{P}$ 满足 $\| \mathrm{P} \| < \delta$ 时,

$$
\left| \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} - \int_ {a} ^ {b} f (x) \mathrm{d} x \right| <   \varepsilon , \quad \left| \sum_ {i = 1} ^ {n} g (\xi_ {i}) \Delta x _ {i} - \int_ {a} ^ {b} g (x) \mathrm{d} x \right| <   \varepsilon .
$$

记

$$
h = \lambda f + \mu g, I = \lambda \int_ {a} ^ {b} f (x) \mathrm{d} x + \mu \int_ {a} ^ {b} g (x) \mathrm{d} x,
$$

由前式可得

$$
\left| \sum_ {i = 1} ^ {n} h (\xi_ {i}) \Delta x _ {i} - I \right| <   (| \lambda | + | \mu |) \varepsilon ,
$$

这说明 h 可积, 且积分等于 I.

---

9.3 微积分基本定理

17

(2) 由推论 9.1.6 可知 f 在  $[a, c]$  和  $[c, b]$  上均可积. 设  $P_{1}, P_{2}$  分别是  $[a, c]$  和  $[c, b]$  的分割, 当  $\|P_{1}\| \to 0, \|P_{2}\| \to 0$  时,  $P = P_{1} \cup P_{2}$  也满足条件  $\|P\| \to 0$ . 于是

$$
\begin{array}{l} \int_{a}^{b}f(x)\mathrm{d}x = \lim_{\substack{\| \mathrm{P}_{1}\| \to 0\\ \| \mathrm{P}_{2}\| \to 0}}\sum_{\mathrm{P}_{1}\cup \mathrm{P}_{2}}f(\xi_{i})\Delta x_{i} \\ = \int_ {a} ^ {c} f (x) \mathrm{d} x + \int_ {c} ^ {b} f (x) \mathrm{d} x. \\ \end{array}
$$

$$
= \lim _ {\| \mathrm{P} _ {1} \| \to 0} \sum_ {\mathrm{P} _ {1}} f (\xi_ {i}) \Delta x _ {i} + \lim _ {\| \mathrm{P} _ {2} \| \to 0} \sum_ {\mathrm{P} _ {2}} f (\xi_ {i}) \Delta x _ {i}
$$

![](../../raw/pages_0321-0336/images/page_324_image_5.jpg)

注9.3.3 根据之前的约定, 如果 $a, b, c$ 属于 $f$ 的某个可积区间, 则不论它们的相对位置如何, (2) 中等式仍成立, 这称为积分关于区间的可加性.

定理 9.3.4 (1) 设 f 为  $[a, b]$  上的非负可积函数，则其积分非负.

(2) 设 $f, g \in R[a, b]$, 且 $f(x) \geqslant g(x)$, 则

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x \geqslant \int_ {a} ^ {b} g (x) \mathrm{d} x.
$$

(3) 设 $f \in R[a, b]$, 则

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x \right| \leqslant \int_ {a} ^ {b} | f (x) | \mathrm{d} x.
$$

证明 (1) 如果 $f$ 非负可积, 则其积分和总是非负的, 从而积分非负.

(2) 由定理 9.3.3 可知 $f - g \in R[a, b]$, 由 (1) 可知

$$
0 \leqslant \int_ {a} ^ {b} (f - g) \mathrm{d} x = \int_ {a} ^ {b} f (x) \mathrm{d} x - \int_ {a} ^ {b} g (x) \mathrm{d} x.
$$

(3) 由命题 9.1.7 可知 $|f| \in R[a, b]$. 任给 $[a, b]$ 的分割 P, 均有

$$
\left| \sum_ {\mathrm{P}} f (\xi_ {i}) \Delta x _ {i} \right| \leqslant \sum_ {\mathrm{P}} | f (\xi_ {i}) | \Delta x _ {i},
$$

令  $\|P\|\rightarrow0$  即得欲证结论.

设 $f \in R[a, b]$, 我们想要寻找 $f$ 的原函数. 受 Newton-Leibniz 公式的启发, 考虑所谓变限积分

$$
F (x) = \int_ {a} ^ {x} f (t) \mathrm{d} t, x \in [ a, b ]. \tag {9.3.3}
$$

设 $|f| \leqslant M$，当 $x, y \in [a, b]$ 时，由积分的上述性质可得

$$
| F (x) - F (y) | = \left| \int_ {y} ^ {x} f (t) \mathrm{d} t \right| \leqslant M | x - y |,
$$

这说明 F 为 Lipschitz 函数. 进一步, 我们有

---

18

第九章 Riemann积分

定理9.3.5 设 $f \in R[a, b]$, $F$ 如 (9.3.3) 式所定义. 如果 $f$ 在 $x_0$ 处连续, 则 $F$ 在 $x_0$ 处可导, 且 $F'(x_0) = f(x_0)$.

证明 由积分的性质可得

$$
F (x) - F (x _ {0}) = \int_ {x _ {0}} ^ {x} f (t) \mathrm{d} t = f (x _ {0}) (x - x _ {0}) + E (x),
$$

其中

$$
E (x) = \int_ {x _ {0}} ^ {x} [ f (t) - f (x _ {0}) ]   \mathrm{d} t.
$$

由 $f$ 在 $x_0$ 处连续可知, 任给 $\varepsilon > 0$, 存在 $\delta > 0$, 当 $|x - x_0| < \delta$ 时 $|f(x) - f(x_0)| < \varepsilon$. 此时, 若 $t$ 介于 $x$ 和 $x_0$ 之间, 则 $|f(t) - f(x_0)| < \varepsilon$. 由积分的绝对值性质可得

$$
| E (x) | \leqslant \varepsilon | x - x _ {0} |.
$$

这说明 $F$ 在 $x_0$ 处可微 (可导), 且 $F'(x_0) = f(x_0)$.

![](../../raw/pages_0321-0336/images/page_325_image_10.jpg)

下面的重要结果和 Newton-Leibniz 公式一起常称为微积分基本定理:

定理 9.3.6 设  $f \in C[a, b]$ ，F 如 (9.3.3) 式所定义，则 F 为 f 的一个原函数.

证明 这是前一定理的直接推论.

![](../../raw/pages_0321-0336/images/page_325_image_14.jpg)

注 9.3.4 可积函数未必有原函数. 例如, 考虑如下阶梯函数:

$$
f (x) = - 1, \quad x \in [ 0, 1 ]; \quad f (x) = 1, \quad x \in (1, 2 ].
$$

显然, $f \in R[0,2]$ . 由关于导数的 Darboux 介值定理可知 f 不存在原函数.

推论 9.3.7 设  $f \in C[a, b]$ ,  $u, v : (c, d) \to [a, b]$  均为可导函数, 记

$$
G (x) = \int_ {v (x)} ^ {u (x)} f (t)   \mathrm{d} t, x \in [ c, d ],
$$

则 $G^{\prime}(x) = f(u(x))u^{\prime}(x) - f(v(x))v^{\prime}(x)$.

证明 设 $F$ 如 (9.3.3) 式所定义, 则 $G(x) = F(u(x)) - F(v(x))$. 由复合函数求导的链式法则可得

$$
G ^ {\prime} (x) = F ^ {\prime} (u (x)) u ^ {\prime} (x) - F ^ {\prime} (v (x)) v ^ {\prime} (x) = f (u (x)) u ^ {\prime} (x) - f (v (x)) v ^ {\prime} (x).
$$

![](../../raw/pages_0321-0336/images/page_325_image_23.jpg)

例 9.3.1 设  $F(x)=\int_{-x}^{2x}\frac{\sin t}{t}\mathrm{d}t,$  求  $F'(x)$  及  $F'(0).$

解 在 $t = 0$ 处规定 $\frac{\sin t}{t}$ 等于1, 此时 $\frac{\sin t}{t}$ 为 $\mathbb{R}$ 上的连续函数. 由上述推论可得

$$
F ^ {\prime} (x) = \frac {\sin (2 x)}{2 x} (2 x) ^ {\prime} - \frac {\sin (- x)}{- x} (- x) ^ {\prime} = \frac {1}{x} (\sin x + \sin 2 x),
$$

特别地, $F'(0)=3$ .

---

9.3 微积分基本定理

19

## 习题 9.3

1. 设 $f \in R[a, b]$, $F \in C[a, b]$. 如果 $F$ 在 $(a, b)$ 上可导且 $F' = f$, 证明:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = F (b) - F (a).
$$

2. 举例说明, 当 $F$ 在 $[a, b]$ 上可导时, $F'$ 在 $[a, b]$ 上未必可积.

3. 指出下列计算过程中的错误之处:

$$
\int_ {- 1} ^ {1} \frac {\mathrm{d} x}{1 + x ^ {2}} = - \arctan \frac {1}{x} \Big | _ {- 1} ^ {1} = - \frac {\pi}{2}.
$$

4. 利用 Newton-Leibniz 公式计算下列积分:

(1) $\int_0^1 x^2\mathrm{d}x;$

(2) $\int_{a}^{b}\sin x\mathrm{d}x;$

(3) $\int_{0}^{\pi}\cos^{2}x\mathrm{d}x.$

5. 利用积分求下列极限:

(1)  $\lim_{n\to\infty}\left(\frac{1}{n^{2}}+\frac{2}{n^{2}}+\cdots+\frac{n-1}{n^{2}}\right)$ ;
(2) $\lim_{n\to\infty}\frac{1}{n}\left(\sin\frac{\pi}{n}+\sin\frac{2\pi}{n}+\cdots+\sin\frac{n-1}{n}\pi\right);$
(3)  $\lim_{n\to\infty}\frac{1}{n^{4}}\left(1+2^{3}+\cdots+n^{3}\right).$

6. 设 $f \in C[a, b]$ 且 $\int_{a}^{b} f^{2}(x) \, \mathrm{d}x = 0$, 证明: $f \equiv 0$.

7. 设 $f, g \in R[a, b]$, 证明:

$$
\left| \int_ {a} ^ {b} f (x) g (x)   \mathrm{d} x \right| \leqslant \left(\int_ {a} ^ {b} f ^ {2} (x)   \mathrm{d} x\right) ^ {\frac {1}{2}} \left(\int_ {a} ^ {b} g ^ {2} (x)   \mathrm{d} x\right) ^ {\frac {1}{2}}.
$$

8. 设 $f \in C^{1}[a, b]$ 且 $f(a) = 0$, 证明:

$$
\int_ {a} ^ {b} f ^ {2} (x) \mathrm{d} x \leqslant \frac {(b - a) ^ {2}}{2} \int_ {a} ^ {b} [ f ^ {\prime} (x) ] ^ {2} \mathrm{d} x.
$$

9. 设 $f \in C^{1}[a, b]$, 证明:

$$
\max _ {a \leqslant x \leqslant b} | f (x) | \leqslant \frac {1}{b - a} \left| \int_ {a} ^ {b} f (x) \mathrm{d} x \right| + \int_ {a} ^ {b} | f ^ {\prime} (x) | \mathrm{d} x.
$$

10. 求下列函数的导数:

(1) $F(x) = \int_{0}^{\cos^{2}x}\sqrt{1 + t^{2}}\mathrm{d}t;$

(2) $F(x) = \int_{\sin x}^{x}\frac{\mathrm{d}t}{\sqrt{1 + \sin^2t}};$

(3) $F(x) = \int_{a}^{b}\sin (x + t)\mathrm{d}t.$

---

20

第九章 Riemann积分

11. 求下列极限:

(1) $\lim_{x\to 0}\frac{1}{x^4}\int_0^x\sin^3 t\mathrm{d}t;$

(2) $\lim_{x\to 0}\frac{1}{x}\int_0^x\cos t^2\mathrm{d}t;$

(3) $\lim_{x\to +\infty}\frac{\mathrm{e}^{-x^2}}{x}\int_0^x t^2\mathrm{e}^{t^2}\mathrm{d}t.$

12. 设 $f \in C(0, +\infty)$, 如果

$$
\int_ {0} ^ {x} f (t) \mathrm{d} t = \frac {1}{2} x f (x), \forall x > 0,
$$

证明: 存在常数 c, 使得  $f(x) = cx$ .

13. 设 f 为 n 次实系数多项式, 证明:

$$
\int_ {a} ^ {b} | f ^ {\prime} (x) | \mathrm{d} x \leqslant 2 n \max _ {a \leqslant x \leqslant b} | f (x) |.
$$

14. 设 $f$ 是 $[a, b]$ 上的凸函数, 证明: $f \in R[a, b]$ 且

$$
(b - a) f \Big (\frac {a + b}{2} \Big) \leqslant \int_ {a} ^ {b} f (x) \mathrm{d} x \leqslant (b - a) \frac {f (a) + f (b)}{2}.
$$

## 9.4 积分的计算

微积分基本定理将微分和积分统一在一个公式中, 是计算积分的有力工具. 下面我们来讨论微积分基本定理的变化形式, 由此得到计算积分的两个基本方法: 换元法和分部积分法.

定理 9.4.1（换元法） 设 f 在区间 I 上连续,  $\varphi$  在  $[\alpha, \beta]$  上可导且  $\varphi' \in R[\alpha, \beta]$ . 若  $\varphi([\alpha, \beta]) \subseteq I$ , 则

$$
\int_ {\varphi (\alpha)} ^ {\varphi (\beta)} f (x) \mathrm{d} x = \int_ {\alpha} ^ {\beta} f (\varphi (t)) \varphi^ {\prime} (t) \mathrm{d} t.
$$

证明 取 $a \in I$, 设 $F$ 由 (9.3.3) 式所定义. 由定理 9.3.6 可知 $F' = f$, 故

$$
\frac {\mathrm{d}}{\mathrm{d} t} F (\varphi (t)) = F ^ {\prime} (\varphi (t)) \varphi^ {\prime} (t) = f (\varphi (t)) \varphi^ {\prime} (t).
$$

由 Newton-Leibniz 公式可得

$$
\int_ {\alpha} ^ {\beta} f (\varphi (t)) \varphi^ {\prime} (t) \mathrm{d} t = F (\varphi (\beta)) - F (\varphi (\alpha)) = \int_ {\varphi (\alpha)} ^ {\varphi (\beta)} f (x) \mathrm{d} x.
$$

例 9.4.1 设 f 是周期函数, T 为其周期. 如果  $f \in R[0, T]$ , 证明: 任给  $a \in R$ , 均有

$$
\int_ {a} ^ {a + T} f (x) \mathrm{d} x = \int_ {0} ^ {T} f (x) \mathrm{d} x.
$$

---

9.4 积分的计算

21

证明 由题设可知 $f$ 在每一个闭区间上都是可积的. 由积分关于区间的可加性质可得

$$
\int_ {a} ^ {a + T} f (x) \mathrm{d} x = \int_ {a} ^ {0} f (x) \mathrm{d} x + \int_ {0} ^ {T} f (x) \mathrm{d} x + \int_ {T} ^ {a + T} f (x) \mathrm{d} x.
$$

利用变换 $x = t + T$ ，上式右边第三个积分成为

$$
\int_ {0} ^ {a} f (t + T) \mathrm{d} t = \int_ {0} ^ {a} f (t) \mathrm{d} t,
$$

代入前式就得到了等式的证明.

例 9.4.2 计算积分  $\int_{0}^{1}\frac{\sqrt{x}}{1+x}dx.$

解 令 $x = t^2, t \in [0,1]$, 则

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {\sqrt {x}}{1 + x} \mathrm{d} x = 2 \int_ {0} ^ {1} \frac {t ^ {2}}{1 + t ^ {2}} \mathrm{d} t = 2 - 2 \int_ {0} ^ {1} \frac {\mathrm{d} t}{1 + t ^ {2}} \\ = 2 - 2 (\arctan t) \big | _ {0} ^ {1} = 2 - \pi / 2. \\ \end{array}
$$

![](../../raw/pages_0321-0336/images/page_328_image_10.jpg)

例 9.4.3 计算积分  $\int_{0}^{1}\sqrt{1-x^{2}}\mathrm{d}x$ .

解 令 $x = \cos t, t \in \left[0, \frac{\pi}{2}\right]$, 则

$$
\begin{array}{l} \int_ {0} ^ {1} \sqrt {1 - x ^ {2}} \mathrm{d} x = \int_ {\frac {\pi}{2}} ^ {0} \sqrt {1 - \cos^ {2} t} (\cos t) ^ {\prime} \mathrm{d} t \\ = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} t \mathrm{d} t = \int_ {0} ^ {\frac {\pi}{2}} \frac {1}{2} (1 - \cos (2 t)) \mathrm{d} t \\ = \frac {1}{2} \left(x - \frac {1}{2} \sin (2 x)\right) \Big | _ {0} ^ {\frac {\pi}{2}} = \frac {\pi}{4}. \\ \end{array}
$$

![](../../raw/pages_0321-0336/images/page_328_image_14.jpg)

注 9.4.1 我们计算出来的是单位圆盘在平面第一象限中的面积, 因此整个单位圆盘的面积等于  $\pi$ .

定理 9.4.2（分部积分） 设 u, v 为 [a, b] 上的可导函数且  $u', v' \in R[a, b]$ ，则

$$
\int_ {a} ^ {b} u (x) v ^ {\prime} (x) \mathrm{d} x = u v \big | _ {a} ^ {b} - \int_ {a} ^ {b} u ^ {\prime} (x) v (x) \mathrm{d} x.
$$

证明 由题设可知, $uv'$ 和 $u'v$ 均为可积函数. 由 $(uv)' = u'v + uv'$ 和 Newton-Leibniz 公式可得

$$
u v \big | _ {a} ^ {b} = \int_ {a} ^ {b} (u v) ^ {\prime} (x)   \mathrm{d} x = \int_ {a} ^ {b} u (x) v ^ {\prime} (x)   \mathrm{d} x + \int_ {a} ^ {b} u ^ {\prime} (x) v (x)   \mathrm{d} x,
$$

移项即得欲证等式.

---

22

第九章 Riemann 积分

例 9.4.4 计算积分  $\int_{0}^{\pi} x^{2} \cos x \, dx$ .

解 利用分部积分可得

$$
\begin{array}{l} \int_ {0} ^ {\pi} x ^ {2} \cos x \mathrm{d} x = \int_ {0} ^ {\pi} x ^ {2} (\sin x) ^ {\prime} \mathrm{d} x = x ^ {2} \sin x | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} (x ^ {2}) ^ {\prime} \sin x \mathrm{d} x \\ = \int_ {0} ^ {\pi} 2 x (\cos x) ^ {\prime} \mathrm{d} x = 2 x \cos x \big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} 2 \cos x \mathrm{d} x \\ = - 2 \pi - 2 \sin x \big | _ {0} ^ {\pi} = - 2 \pi. \\ \end{array}
$$

注意这个例子中通过转移导数降低 x 的幂次, 最后消去 x 的幂次. 有时可以暂时升高 x 的幂次再通过分部积分进行化简.

例 9.4.5 计算积分  $\int_{1}^{3} x^{2} \ln x \, dx$ .

解 利用分部积分可得

$$
\begin{array}{l} \int_ {1} ^ {3} x ^ {2} \ln x \mathrm{d} x = \int_ {1} ^ {3} \left(\frac {1}{3} x ^ {3}\right) ^ {\prime} \ln x \mathrm{d} x \\ = \left(\frac {1}{3} x ^ {3}\right) \ln x \Big | _ {1} ^ {3} - \int_ {1} ^ {3} \left(\frac {1}{3} x ^ {3}\right) (\ln x) ^ {\prime} \mathrm{d} x \\ = 9 \ln 3 - \int_ {1} ^ {3} \frac {1}{3} x ^ {2} \mathrm{d} x = 9 \ln 3 - \left. \frac {1}{9} x ^ {3} \right| _ {1} ^ {3} \\ = 9 \ln 3 - \frac {2 6}{9}. \\ \end{array}
$$

例 9.4.6 当 m 为非负整数时, 计算积分

$$
I _ {m} = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {m} x \mathrm{d} x, J _ {m} = \int_ {0} ^ {\frac {\pi}{2}} \cos^ {m} x \mathrm{d} x.
$$

解 利用变换 $x = \frac{\pi}{2} - t$ 易见 $J_{m} = I_{m}$. 我们用递推的方法来计算 $I_{m}$. 显然, $I_{0} = \frac{\pi}{2}, I_{1} = 1$. 当 $m \geqslant 2$ 时, 利用分部积分可得

$$
\begin{array}{l} I _ {m} = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {m} x \mathrm{d} x = \int_ {0} ^ {\frac {\pi}{2}} (\sin^ {m - 1} x) (- \cos x) ^ {\prime} \mathrm{d} x \\ = (\sin^ {m - 1} x) (- \cos x) \big | _ {0} ^ {\frac {\pi}{2}} + \int_ {0} ^ {\frac {\pi}{2}} (m - 1) \sin^ {m - 2} x \cos^ {2} x \mathrm{d} x \\ = (m - 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {m - 2} x \left(1 - \sin^ {2} x\right) \mathrm{d} x \\ = (m - 1) I _ {m - 2} - (m - 1) I _ {m}, \\ \end{array}
$$

这就得到了递推公式 $I_{m} = \frac{m - 1}{m} I_{m - 2}$, 从而有

$$
I _ {2 n} = \frac {2 n - 1}{2 n} I _ {2 n - 2} = \frac {2 n - 1}{2 n} \frac {2 n - 3}{2 n - 2} I _ {2 n - 4} = \dots = \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {\pi}{2}. \tag {9.4.1}
$$

---

9.4 积分的计算

23

同理可得

$$
I _ {2 n + 1} = \frac {(2 n) ! !}{(2 n + 1) ! !}.
$$

注意到当 $0 < x < \frac{\pi}{2}$ 时, $\sin^{2n + 1}x < \sin^{2n}x < \sin^{2n - 1}x$, 由积分的性质可得

$$
I _ {2 n + 1} <   I _ {2 n} <   I _ {2 n - 1},
$$

即

$$
\frac {(2 n) ! !}{(2 n + 1) ! !} <   \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {\pi}{2} <   \frac {(2 n - 2) ! !}{(2 n - 1) ! !}.
$$

整理以后可得

$$
\frac {n \pi}{2 n + 1} <   \frac {1}{2 n + 1} \left(\frac {(2 n) ! !}{(2 n - 1) ! !}\right) ^ {2} <   \frac {\pi}{2}, \tag {9.4.2}
$$

由数列极限的夹逼准则可得

$$
\lim _ {n \to \infty} \frac {1}{2 n + 1} \left(\frac {(2 n) ! !}{(2 n - 1) ! !}\right) ^ {2} = \frac {\pi}{2}. \tag {9.4.3}
$$

上式称为 Wallis 公式.

分部积分还可以用来研究Taylor公式的余项.设 $f$ 为区间 $I$ 上的 $C^2$ 函数，当$x,x_0\in I$ 时，由分部积分可得

$$
\begin{array}{l} f (x) - f (x _ {0}) = \int_ {x _ {0}} ^ {x} f ^ {\prime} (t) \mathrm{d} t = \int_ {x _ {0}} ^ {x} f ^ {\prime} (t) (t - x) ^ {\prime} \mathrm{d} t \\ = f ^ {\prime} (t) (t - x) \big | _ {x _ {0}} ^ {x} - \int_ {x _ {0}} ^ {x} f ^ {\prime \prime} (t) (t - x) \mathrm{d} t \\ = f ^ {\prime} (x _ {0}) (x - x _ {0}) + \int_ {x _ {0}} ^ {x} f ^ {\prime \prime} (t) (x - t) \mathrm{d} t. \\ \end{array}
$$

若 $f$ 为 $C^3$ 函数, 则还可以继续做分部积分. 一般地, 我们有

定理 9.4.3 设 f 为区间 I 上的  $C^{n+1}$  函数,  $x, x_{0} \in I$ , 则

$$
f (x) = \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (x _ {0})}{k !} (x - x _ {0}) ^ {k} + R _ {n} (x),
$$

其中

$$
R _ {n} (x) = \frac {1}{n !} \int_ {x _ {0}} ^ {x} (x - t) ^ {n} f ^ {(n + 1)} (t) \mathrm{d} t. \tag {9.4.4}
$$

证明 我们对 $n$ 使用数学归纳法. $n = 0$ 的情形就是微积分基本定理. $n = 1$ 的情

---

24

第九章 Riemann积分

形上面已经讨论过. 设 $n = m - 1$ 时结论成立, 则 $n = m$ 时, 利用分部积分可得

$$
\begin{array}{l} R _ {m - 1} (x) = \int_ {x _ {0}} ^ {x} \left(\frac {- 1}{m !} (x - t) ^ {m}\right) ^ {\prime} f ^ {(m)} (t) \mathrm{d} t \\ = \left(\frac {- 1}{m !} (x - t) ^ {m}\right) ^ {\prime} f ^ {(m)} (t) \Big | _ {x _ {0}} ^ {x} + \int_ {x _ {0}} ^ {x} \frac {1}{m !} (x - t) ^ {m} f ^ {(m + 1)} (t) \mathrm{d} t \\ = \frac {f ^ {(m)} (x _ {0})}{m !} (x - x _ {0}) ^ {m} + R _ {m} (x), \\ \end{array}
$$

这说明 n = m 时结论也成立.

![](../../raw/pages_0321-0336/images/page_331_image_5.jpg)

## 习题 9.4

1. 计算下列积分:

(1) $\int_0^1\frac{x}{(1 + x)^3}\mathrm{d}x;$

(2) $\int_0^1\ln (1 + \sqrt{x})\mathrm{d}x;$

(3) $\int_0^1\sqrt{\frac{1 - x}{1 + x}}\mathrm{d}x;$

(4) $\int_{0}^{1}\arctan\sqrt{\frac{1-x}{1+x}}\mathrm{d}x;$

(5) $\int_0^1 x\sqrt{1 - x}\mathrm{d}x;$

(6) $\int_{1}x^{2}\sqrt{1 - x^{2}}\mathrm{d}x.$

2. 计算下列积分:

(1) $\int_0^1\ln (x + \sqrt{1 + x^2})\mathrm{d}x;$

(2) $\int_0^1 x (\arctan x)^2 \, \mathrm{d}x$;

(3) $\int_0^\pi x^2\sin (3x)\mathrm{d}x;$

(4) $\int_0^\pi \mathrm{e}^x\cos (2x)\mathrm{d}x;$

(5) $\int_{0}^{\pi}\sin^{3}x\mathrm{d}x;$

(6) $\int_{-\pi}^{\pi} x^{2} \cos x \, \mathrm{d}x$;

(7) $\int_0^1 x^2 (1 - x^3)^5\mathrm{d}x;$

(8) $\int_0^1 (1 - x)^2 x^3\mathrm{d}x;$

(9) $\int_0^1\frac{\mathrm{d}x}{(2 - x^2)^2};$

(10) $\int_{0}^{1}\frac{\sqrt{1 + x^2}}{x^2}\mathrm{d}x.$

3. 设 0 < r < 1, 证明:

$$
\int_ {0} ^ {2 \pi} \frac {1 - r ^ {2}}{1 - 2 r \cos x + r ^ {2}} \mathrm{d} x = 2 \pi .
$$

4. 设 n 为正整数, 证明:

$$
\int_ {0} ^ {1} \frac {\mathrm{d} x}{(1 + x ^ {n}) \sqrt [ n ]{1 + x ^ {n}}} = \frac {1}{\sqrt [ n ]{2}}.
$$

5. 设 m, n 为非零整数, 证明:

(1) $\int_{-\pi}^{\pi}\sin^{2}mx\mathrm{d}x = \int_{-\pi}^{\pi}\cos^{2}mx\mathrm{d}x = \pi;$

---

9.4 积分的计算

25

(2) $\int_{-\pi}^{\pi}\sin mx\sin nx\mathrm{d}x = \int_{-\pi}^{\pi}\cos mx\cos nx\mathrm{d}x = 0 (m\neq \pm n);$
(3) $\int_{-\pi}^{\pi}\sin mx\cos nx\mathrm{d}x = 0.$

6. 求下列积分的递推公式 (m, n 为非负整数):

(1) $\int_{0}^{1}\frac{x^n}{1 + x}\mathrm{d}x;$
(2) $\int_0^1\frac{x^n}{1 + x^2}\mathrm{d}x;$
(3) $\int_{0}^{1}(1 - x^2)^n\mathrm{d}x;$
(4) $\int_{0}^{\frac{\pi}{2}}\cos^{n}x\sin nx\mathrm{d}x;$
(5) $\int_{0}^{\frac{\pi}{2}}\cos^{n}x\cos nx\mathrm{d}x;$
(6) $\int_{0}^{\frac{\pi}{2}}\cos^{m}x\sin^{n}x\mathrm{d}x;$
(7) $\int_{0}^{\frac{\pi}{4}}\tan^{n}x\mathrm{d}x;$
(8) $\int_{0}^{\frac{\pi}{2}}\frac{\sin nx}{\sin x}\mathrm{d}x;$
(9) $\int_{0}^{\frac{\pi}{2}}\frac{\sin^{2}nx}{\sin^{2}x}\mathrm{d}x.$

7. 设  $f \in C[0,1]$ ，证明:

$$
\int_ {0} ^ {\pi} x f (\sin x) \mathrm{d} x = \frac {\pi}{2} \int_ {0} ^ {\pi} f (\sin x) \mathrm{d} x,
$$

并利用上式计算积分  $\int_{0}^{\pi}\frac{x\sin x}{1+\cos^{2}x}\mathrm{d}x.$

8. 设 $f$ 在 $(0, +\infty)$ 上单调递增, 记

$$
F (x) = \frac {1}{x} \int_ {0} ^ {x} f (t)   \mathrm{d} t, \forall x > 0,
$$

证明: $F$ 在 $(0, +\infty)$ 上单调递增.

9. 设 f 是周期为 T 且在  $[0, T]$  上可积的函数, 证明:

$$
\lim _ {\lambda \to + \infty} \frac {1}{\lambda} \int_ {0} ^ {\lambda} f (x)   \mathrm{d} x = \frac {1}{T} \int_ {0} ^ {T} f (x)   \mathrm{d} x.
$$

10. 设 $f \in C^{2}[a, b]$, 证明:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \frac {1}{2} \left(f (a) + f (b)\right) (b - a) + \frac {1}{2} \int_ {a} ^ {b} (x - a) (x - b) f ^ {\prime \prime} (x) \mathrm{d} x.
$$

11. 设 $f \in C[0,1]$, 证明:

$$
\lim _ {n \to + \infty} n \int_ {0} ^ {1} x ^ {n} f (x)   \mathrm{d} x = f (1).
$$

12. 设 $f \in R[0,1]$, 证明:

$$
\lim _ {n \to + \infty} \int_ {0} ^ {1} \sqrt [ n ]{x} f (x)   \mathrm{d} x = \int_ {0} ^ {1} f (x)   \mathrm{d} x.
$$

---

26

第九章 Riemann 积分

13. 证明:

$$
\int_ {0} ^ {1} \frac {\mathrm{d} x}{1 + x ^ {n}} = 1 - \frac {\ln 2}{n} + o \Big (\frac {1}{n} \Big) \quad (n \to + \infty).
$$

14. 设 $f \in C[-1, 1]$, 证明:

$$
\lim _ {h \to 0 ^ {+}} \int_ {- 1} ^ {1} \frac {h f (x)}{h ^ {2} + x ^ {2}}   \mathrm{d} x = \pi f (0).
$$

## 9.5 积分的进一步性质

Newton-Leibniz 公式虽然给出了计算积分的通用方法, 但由于不易获得原函数的解析表达式, 多数情况下只能对积分进行近似计算, 或利用积分中值定理对积分做粗略估计.

定理 9.5.1 (积分第一中值定理) 设 $f, g \in  R\left\lbrack  {a,b}\right\rbrack$ ,且 $g$ 不变号,则

$$
\int_ {a} ^ {b} f (x) g (x) \mathrm{d} x = \mu \int_ {a} ^ {b} g (x) \mathrm{d} x,
$$

其中 $\mu$ 介于 $f$ 的上下确界之间. 特别地, 当 $f$ 连续时, 存在 $\xi \in [a, b]$, 使得 $\mu = f(\xi)$.

证明 不失一般性, 可设 $g \geqslant 0$, 此时 $g$ 在 $[a, b]$ 上的积分大于或等于零. 分别记 $f$ 的上下确界为 $M, m$, 则 $mg \leqslant fg \leqslant Mg$. 由定理9.3.4可知

$$
m \int_ {a} ^ {b} g (x) \mathrm{d} x \leqslant \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x \leqslant M \int_ {a} ^ {b} g (x) \mathrm{d} x.
$$

上式说明, 若 $g$ 在 $[a, b]$ 上的积分为零, 则 $fg$ 在 $[a, b]$ 上的积分也为零, 此时欲证结论当然成立. 下设 $g$ 在 $[a, b]$ 上的积分大于零, 令

$$
\mu = \left(\int_ {a} ^ {b} g (x) \mathrm{d} x\right) ^ {- 1} \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x,
$$

则 $m \leqslant \mu \leqslant M$.

![](../../raw/pages_0321-0336/images/page_333_image_16.jpg)

注9.5.1 中值定理又称中值公式或平均值公式. 当 $g \equiv 1$ 时, 有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \mu (b - a),
$$

其中 $m \leqslant \mu \leqslant M$.

为了估计积分, 我们往往先用一些较为简单的函数去逼近被积函数.

---

9.5 积分的进一步性质

27

命题 9.5.2 (阶梯逼近) 设 $f \in  R\left\lbrack  {a,b}\right\rbrack$ ,则存在两列阶梯函数 $\left\{  {\varphi }_{n}\right\}$ , $\left\{  {\psi }_{n}\right\}$ ,使得

$$
\varphi_ {n} \leqslant f \leqslant \psi_ {n}, \quad \int_ {a} ^ {b} \left(\psi_ {n} (x) - \varphi_ {n} (x)\right) \mathrm{d} x <   \frac {1}{n}, \tag {9.5.1}
$$

且每一个 $\varphi_{n},\psi_{n}$ 均介于 $f$ 的上下确界之间.此外，任给 $g\in R[a,b]$ ，均有

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} \varphi_ {n} (x) g (x) \mathrm{d} x = \lim _ {n \to + \infty} \int_ {a} ^ {b} \psi_ {n} (x) g (x) \mathrm{d} x = \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x. \tag {9.5.2}
$$

证明 由题设可知, 任给 $n \geqslant 1$, 存在 $[a, b]$ 的分割

$$
\mathrm{P}: a = x _ {0} <   x _ {1} <   x _ {2} <   \dots <   x _ {m} = b,
$$

使得 $\sum_{i=1}^{m}(M_i - m_i)\Delta x_i < \frac{1}{n}$, 其中 $M_i, m_i$ 分别是 $f$ 在 $[x_{i-1}, x_i]$ 上的上确界和下确界.

在 $[a, b]$ 中定义阶梯函数 $\varphi_n, \psi_n$ 如下: 当 $x \in [x_{i-1}, x_i)$ 时 $\varphi_n(x) = m_i, \psi_n(x) = M_i$; 规定 $\varphi_n(b) = m_m, \psi_n(b) = M_m$. 显然, $\varphi_n, \psi_n$ 均介于 $f$ 的上下确界之间, 且满足 (9.5.1) 式.

当  $g \in R[a, b]$  时, 可设  $|g| \leqslant M$ . 此时

$$
| \varphi_ {n} g - f g | \leqslant M (\psi_ {n} - \varphi_ {n}), \quad | \psi_ {n} g - f g | \leqslant M (\psi_ {n} - \varphi_ {n}),
$$

这说明 (9.5.2) 式成立.

我们也可以用连续函数去逼近可积函数. 定义在 $[a, b]$ 中的函数称为是分段线性的, 是指存在 $[a, b]$ 的一个分割, 使得该函数在每一个小区间中都是一次函数.

命题 9.5.3 (分段线性逼近) 设  $f \in R[a, b]$ ，则存在一列连续的分段线性函数  $\{f_{n}\}$ ，使得  $f_{n}(a) = f(a)$ ， $f_{n}(b) = f(b)$ ，每一个  $f_{n}$  均介于 f 的上下确界之间，且

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} | f _ {n} (x) - f (x) | \mathrm{d} x = 0, \tag {9.5.3}
$$

此外, 任给 $g \in R[a, b]$, 均有

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} f _ {n} (x) g (x) \mathrm{d} x = \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x. \tag {9.5.4}
$$

证明 由题设, 任给 $n \geqslant 1$, 存在 $[a, b]$ 的分割 $\mathrm{P}: a = x_0 < x_1 < x_2 < \dots < x_m = b$, 使得

$$
\sum_ {i = 1} ^ {m} \omega_ {i} (f) \Delta x _ {i} <   \frac {1}{n}.
$$

在 $[a, b]$ 中定义分段线性函数 $f_n$, 使得

$$
f _ {n} (x) = \frac {x _ {i} - x}{\Delta x _ {i}} f (x _ {i - 1}) + \frac {x - x _ {i - 1}}{\Delta x _ {i}} f (x _ {i}), \forall x \in [ x _ {i - 1}, x _ {i} ], i = 1, 2, \dots , m.
$$

---

28

第九章 Riemann 积分

显然, $f_{n}$ 连续, 且 $f_{n}$ 在 $a, b$ 处的值与 $f$ 相同, 在其余地方的值介于 $f$ 的上下确界之间. 当 $x \in [x_{i-1}, x_{i}]$ 时, 还有

$$
\begin{array}{l} | f _ {n} (x) - f (x) | = | (x _ {i} - x) (f (x _ {i - 1}) - f (x)) + (x - x _ {i - 1}) (f (x _ {i}) - f (x)) | / \Delta x _ {i} \\ \leqslant ((x _ {i} - x) \omega_ {i} (f) + (x - x _ {i - 1}) \omega_ {i} (f)) / \Delta x _ {i} = \omega_ {i} (f). \\ \end{array}
$$

剩下的证明与上一命题类似, 略.

![](../../raw/pages_0321-0336/images/page_335_image_5.jpg)

下面我们来考虑几个应用.

例 9.5.1 设  $f \in R[a, b]$ ，证明:

$$
\int_ {a} ^ {b} | f (x) | \mathrm{d} x = \sup \biggl \{\int_ {a} ^ {b} f (x) \varphi (x) \mathrm{d} x \Big | \varphi \in R [ a, b ], | \varphi | \leqslant 1 \biggr \}. \tag {9.5.5}
$$

证明 (9.5.5) 式右端记为 $\alpha$, 由

$$
\int_ {a} ^ {b} f (x) \varphi (x) \mathrm{d} x \leqslant \int_ {a} ^ {b} | f (x) | \mathrm{d} x
$$

可知 $\alpha \leqslant \int_{a}^{b}|f(x)|\mathrm{d}x.$ 反之，任给 $\varepsilon >0$ ，存在阶梯函数 $g$ ，使得

$$
\int_ {a} ^ {b} | f (x) | \mathrm{d} x \leqslant \int_ {a} ^ {b} | g (x) | \mathrm{d} x + \int_ {a} ^ {b} | f (x) - g (x) | \mathrm{d} x <   \int_ {a} ^ {b} | g (x) | \mathrm{d} x + \varepsilon .
$$

由 g 为阶梯函数可知, 存在取值为  $\pm1$  的阶梯函数  $\varphi$ , 使得

$$
\int_ {a} ^ {b} g (x) \varphi (x) \mathrm{d} x = \int_ {a} ^ {b} | g (x) | \mathrm{d} x > \int_ {a} ^ {b} | f (x) | \mathrm{d} x - \varepsilon .
$$

此时有

$$
\begin{array}{l} \alpha \geqslant \int_ {a} ^ {b} f (x) \varphi (x)   \mathrm{d} x = \int_ {a} ^ {b} \left(f (x) - g (x)\right) \varphi (x)   \mathrm{d} x + \int_ {a} ^ {b} g (x) \varphi (x)   \mathrm{d} x \\ \geqslant - \int_ {a} ^ {b} | f (x) - g (x) | \mathrm{d} x + \int_ {a} ^ {b} | f (x) | \mathrm{d} x - \varepsilon \\ > \int_ {a} ^ {b} | f (x) | \mathrm{d} x - 2 \varepsilon , \\ \end{array}
$$

由  $\varepsilon$  的任意性即得欲证结论.

![](../../raw/pages_0321-0336/images/page_335_image_18.jpg)

例 9.5.2 (Riemann-Lebesgue 引理) 设  $f \in R[a, b]$ ，则

$$
\lim _ {\lambda \to + \infty} \int_ {a} ^ {b} f (x) \sin \lambda x   \mathrm{d} x = 0, \quad \lim _ {\lambda \to + \infty} \int_ {a} ^ {b} f (x) \cos \lambda x   \mathrm{d} x = 0. \tag {9.5.6}
$$

---

9.5 积分的进一步性质

29

证明 任给 $\varepsilon > 0$, 取阶梯函数 $g$, 使得

$$
\int_ {a} ^ {b} | f (x) - g (x) | \mathrm{d} x <   \frac {1}{2} \varepsilon .
$$

此时

$$
\left| \int_ {a} ^ {b} f (x) \sin \lambda x \mathrm{d} x - \int_ {a} ^ {b} g (x) \sin \lambda x \mathrm{d} x \right| \leqslant \int_ {a} ^ {b} | f (x) - g (x) | \mathrm{d} x <   \frac {1}{2} \varepsilon . \tag {9.5.7}
$$

设阶梯函数 $g$ 在 $(x_{i - 1},x_i)$ 中取值为 $c_{i}$ $(1\leqslant i\leqslant m)$ ，则

$$
\int_ {a} ^ {b} g (x) \sin \lambda x \mathrm{d} x = \sum_ {i = 1} ^ {m} \int_ {x _ {i - 1}} ^ {x _ {i}} c _ {i} \sin \lambda x \mathrm{d} x = \sum_ {i = 1} ^ {m} (\cos (\lambda x _ {i - 1}) - \cos (\lambda x _ {i})) c _ {i} / \lambda .
$$

记 $M = \max \{|c_i| \mid 1 \leqslant i \leqslant m\}$, 上式表明

$$
\left| \int_ {a} ^ {b} g (x) \sin \lambda x \mathrm{d} x \right| \leqslant 2 m M / \lambda . \tag {9.5.8}
$$

当 $\lambda > 4mM\varepsilon^{-1}$ 时, 就有

$$
\left| \int_ {a} ^ {b} f (x) \sin \lambda x \mathrm{d} x \right| \leqslant \frac {1}{2} \varepsilon + 2 m M / \lambda <   \varepsilon ,
$$

这说明 (9.5.6) 中第一式成立.

我们也可以用分段线性逼近来做, 以 (9.5.6) 中第二式为例. 任给 $\varepsilon > 0$, 取连续的分段线性函数 $h$, 使得

$$
\int_ {a} ^ {b} | f (x) - h (x) | \mathrm{d} x <   \frac {1}{2} \varepsilon .
$$

此时

$$
\left| \int_ {a} ^ {b} f (x) \cos \lambda x \mathrm{d} x - \int_ {a} ^ {b} h (x) \cos \lambda x \mathrm{d} x \right| \leqslant \int_ {a} ^ {b} | f (x) - h (x) | \mathrm{d} x <   \frac {1}{2} \varepsilon . \tag {9.5.9}
$$

利用分部积分可得

$$
\int_ {a} ^ {b} h (x) \cos \lambda x \mathrm{d} x = h (x) \frac {\sin \lambda x}{\lambda} \Big | _ {a} ^ {b} - \int_ {a} ^ {b} h ^ {\prime} (x) \frac {\sin \lambda x}{\lambda} \mathrm{d} x,
$$

当  $\lambda$  充分大时, 上式右端的绝对值小于  $\frac{1}{2}\varepsilon$ . 剩下的证明与前一段相同, 不再重复. □
其次, 利用分段线性逼近还可以将分部积分公式做一点推广.

定理 9.5.4（分部积分之二） 设  $f, g \in R[a, b]$ ,  $C_{1}, C_{2} \in R$ . 当  $x \in [a, b]$  时，记

$$
F (x) = \int_ {a} ^ {x} f (t) \mathrm{d} t + C _ {1}, G (x) = \int_ {a} ^ {x} g (t) \mathrm{d} t + C _ {2},
$$

则有

$$
\int_ {a} ^ {b} F (x) g (x) \mathrm{d} x = F G \Big | _ {a} ^ {b} - \int_ {a} ^ {b} f (x) G (x) \mathrm{d} x.
$$

---

30

第九章 Riemann 积分

证明 如果 $f, g \in C[a, b]$, 则 $F, G \in C^{1}[a, b]$, 欲证等式可从之前的分部积分公式直接得到. 一般地, 我们分别取 $f, g$ 的分段线性逼近 $\{f_{n}\}, \{g_{n}\}$, 使得

$$
\int_ {a} ^ {b} | f _ {n} (x) - f (x) | \mathrm{d} x <   \frac {1}{n}, \quad \int_ {a} ^ {b} | g _ {n} (x) - g (x) | \mathrm{d} x <   \frac {1}{n}.
$$

当 $x \in [a, b]$ 时, 记

$$
F _ {n} (x) = \int_ {a} ^ {x} f _ {n} (t) \mathrm{d} t + C _ {1}, G _ {n} (x) = \int_ {a} ^ {x} g _ {n} (t) \mathrm{d} t + C _ {2}.
$$

由 $f_{n}, g_{n}$ 连续可得

$$
\int_ {a} ^ {b} F _ {n} (x) g _ {n} (x) \mathrm{d} x = F _ {n} G _ {n} \Big | _ {a} ^ {b} - \int_ {a} ^ {b} f _ {n} (x) G _ {n} (x) \mathrm{d} x. \tag {9.5.10}
$$

当 $n \to +\infty$ 时, 我们来研究上式中的各项如何变化. 首先, 不妨设 $f, g, f_n, g_n, F_n, G_n$ 在 $[a, b]$ 上的绝对值均不超过 $M$. 此时有

$$
\begin{array}{l} \left| F _ {n} (x) G _ {n} (x) - F (x) G (x) \right| \leqslant \left| F _ {n} (x) \left(G _ {n} (x) - G (x)\right) \right| + \left| \left(F _ {n} (x) - F (x)\right) G (x) \right| \\ \leqslant M \left| \int_ {a} ^ {x} \left(g _ {n} (t) - g (t)\right) \mathrm{d} t \right| + M \left| \int_ {a} ^ {x} \left(f _ {n} (t) - f (t)\right) \mathrm{d} t \right| \\ \leqslant M \int_ {a} ^ {b} | g _ {n} (t) - g (t) | \mathrm{d} t + M \int_ {a} ^ {b} | f _ {n} (t) - f (t) | \mathrm{d} t \\ <   2 M / n. \\ \end{array}
$$

(9.5.10) 式中其余的项可以类似地做估计.令  $n \rightarrow +\infty$  就由 (9.5.10) 式得到了欲证等式. □

利用分部积分还可以得到积分中值定理的另一种表现形式. 先看一个例子.

例 9.5.3 设  $\beta \geqslant 0, b > a > 0,$  证明:

$$
\left| \int_ {a} ^ {b} \mathrm{e} ^ {- \beta x} \frac {\sin x}{x} \mathrm{d} x \right| \leqslant \frac {2}{a}.
$$

证明 记 $g(x) = \frac{1}{x}\mathrm{e}^{-\beta x}$，利用分部积分可得

$$
\int_ {a} ^ {b} \mathrm{e} ^ {- \beta x} \frac {\sin x}{x} \mathrm{d} x = g (x) (- \cos x) \Big | _ {a} ^ {b} + \int_ {a} ^ {b} g ^ {\prime} (x) \cos x \mathrm{d} x.
$$

注意到 $g$ 在 $[a,b]$ 上是单调递减函数, $g' \leqslant 0$. 由积分第一中值定理, 存在 $\theta \in [a,b]$, 使得

$$
\begin{array}{l} \int_ {a} ^ {b} \mathrm{e} ^ {- \beta x} \frac {\sin x}{x} \mathrm{d} x = g (a) \cos a - g (b) \cos b + \cos \theta \int_ {a} ^ {b} g ^ {\prime} (x) \mathrm{d} x \\ = g (a) \cos a - g (b) \cos b + \cos \theta (g (b) - g (a)) \\ = (g (a) - g (b)) (\cos a - \cos \theta) + g (b) (\cos a - \cos b), \\ \end{array}
$$

---

9.5 积分的进一步性质

31

这说明

$$
\left| \int_ {a} ^ {b} \mathrm{e} ^ {- \beta x} \frac {\sin x}{x} \mathrm{d} x \right| \leqslant 2 (g (a) - g (b)) + 2 g (b) = 2 g (a) \leqslant \frac {2}{a}.
$$

此例中的方法可以做如下推广.

定理 9.5.5 (Weierstrass) 设 $f \in R[a, b]$, $g$ 为 $[a, b]$ 上的单调函数, 则存在 $\xi \in [a, b]$, 使得

$$
\int_ {a} ^ {b} f (x) g (x) \mathrm{d} x = g (a) \int_ {a} ^ {\xi} f (x) \mathrm{d} x + g (b) \int_ {\xi} ^ {b} f (x) \mathrm{d} x. \tag {9.5.11}
$$

证明 设 $F$ 由 (9.3.3) 式所定义. 取 $g$ 的连续分段线性逼近 $\{g_n\}$, 由分部积分之二可得

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x = \lim _ {n \to + \infty} \int_ {a} ^ {b} f (x) g _ {n} (x) \mathrm{d} x \\ = \lim _ {n \to + \infty} \left(F g _ {n} \Big | _ {a} ^ {b} - \int_ {a} ^ {b} F (x) g _ {n} ^ {\prime} (x) \mathrm{d} x\right) \\ = \lim _ {n \to + \infty} \left(F (b) g (b) - F (a) g (a) - \int_ {a} ^ {b} F (x) g _ {n} ^ {\prime} (x)   \mathrm{d} x\right). \\ \end{array}
$$

根据 $g_{n}$ 的构造, 当 $g$ 为单调函数时, $g_{n}$ 也同样是单调函数. 此时, 由积分第一中值定理, 存在 $\xi_{n} \in [a, b]$, 使得

$$
\int_ {a} ^ {b} F (x) g _ {n} ^ {\prime} (x) \mathrm{d} x = F (\xi_ {n}) \int_ {a} ^ {b} g _ {n} ^ {\prime} (x) \mathrm{d} x = F (\xi_ {n}) (g _ {n} (b) - g _ {n} (a)) = F (\xi_ {n}) (g (b) - g (a)).
$$

根据 Bolzano 定理, $\{\xi_n\}$ 存在收敛子列, 不妨设它自身收敛于 $\xi \in [a, b]$, 则

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x = \lim _ {n \to + \infty} (F (b) g (b) - F (a) g (a) - F (\xi_ {n}) (g (b) - g (a))) \\ = F (b) g (b) - F (a) g (a) - F (\xi) (g (b) - g (a)) \\ = g (a) (F (\xi) - F (a)) + g (b) (F (b) - F (\xi)) \\ = g (a) \int_ {a} ^ {\xi} f (x) \mathrm{d} x + g (b) \int_ {\xi} ^ {b} f (x) \mathrm{d} x. \\ \end{array}
$$

推论 9.5.6 (Bonnet $^{①}$ ) 设  $f \in R[a, b]$ , g 为非负函数.

(1) 如果 $g$ 在 $[a, b]$ 上单调递减, 则存在 $\zeta \in [a, b]$ 使得

$$
\int_ {a} ^ {b} f (x) g (x) \mathrm{d} x = g (a) \int_ {a} ^ {\zeta} f (x) \mathrm{d} x. \tag {9.5.12}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Bonnet, Pierre Ossian, 1819 年 12 月 22 日—1892 年 6 月 22 日, 法国数学家.</span></small>

---

32

第九章 Riemann 积分

(2) 如果 $g$ 在 $[a, b]$ 上单调递增, 则存在 $\eta \in [a, b]$ 使得

$$
\int_ {a} ^ {b} f (x) g (x) \mathrm{d} x = g (b) \int_ {\eta} ^ {b} f (x) \mathrm{d} x. \tag {9.5.13}
$$

证明 (1) 由题设可知, 若强制规定 $g$ 在 $b$ 处的值为零, 则既不影响 $g$ 的单调性也不影响 $fg$ 的积分, 此时直接应用 Weierstrass 定理即得欲证结论.

(2) 留作练习.

![](../../raw/pages_0337-0352/images/page_339_image_6.jpg)

注 9.5.2 Weierstrass 定理和 Bonnet 定理统称为积分第二中值定理, 在对积分做估计的时候它们颇为有用.

## 习题9.5

1. 设 $f \in R[a, b]$, 证明: 存在 $\xi \in [a, b]$, 使得

$$
\int_ {a} ^ {\xi} f (x) \mathrm{d} x = \int_ {\xi} ^ {b} f (x) \mathrm{d} x.
$$

2. 设 $f \in R[a, b]$, 记

$$
F (x) = \int_ {a} ^ {x} f (t)   \mathrm{d} t, \forall x \in [ a, b ],
$$

证明:

$$
\int_ {a} ^ {b} F (x) \mathrm{d} x = \int_ {a} ^ {b} (b - x) f (x) \mathrm{d} x.
$$

3. 沿用上一题中的记号, 证明:

$$
\int_ {a} ^ {b} F ^ {2} (x) \mathrm{d} x = 2 \int_ {a} ^ {b} (b - x) f (x) F (x) \mathrm{d} x.
$$

4. 证明:

(1) $\lim_{n\to +\infty}\int_{0}^{\frac{\pi}{2}}\sin^n x\mathrm{d}x = 0;$

(2) $\lim_{n\to +\infty}\int_{n}^{n + p}\frac{\cos x}{x}\mathrm{d}x = 0 (p > 0).$

5. 设 $f$ 为 $[0, 2\pi]$ 上的单调递减函数, $n$ 为正整数, 证明:

$$
\int_ {0} ^ {2 \pi} f (x) \sin n x \mathrm{d} x \geqslant 0.
$$

6. 记

$$
f (x) = \int_ {x} ^ {x + 1} \sin t ^ {2}   \mathrm{d} t.
$$

证明: 当 x > 0 时  $|f(x)| < \frac{1}{x}$ .

---

9.6 积分的近似计算

33

7. 设 $f \in R[c, d], [a, b] \subset (c, d)$, 证明:

$$
\lim _ {h \to 0} \int_ {a} ^ {b} | f (x + h) - f (x) |   \mathrm{d} x = 0.
$$

8. 设 $f \in C[a, b]$, 证明:

$$
\lim _ {n \to + \infty} \left(\int_ {a} ^ {b} | f (x) | ^ {n}   \mathrm{d} x\right) ^ {\frac {1}{n}} = \max _ {a \leqslant x \leqslant b} | f (x) |.
$$

9. 设 $f \in R[a, b]$, $g$ 是以 $T$ 为周期的周期函数且 $g \in R[0, T]$, 证明:

$$
\lim _ {\lambda \to + \infty} \int_ {a} ^ {b} f (x) g (\lambda x)   \mathrm{d} x = \frac {1}{T} \left(\int_ {a} ^ {b} f (x)   \mathrm{d} x\right) \left(\int_ {0} ^ {T} g (x)   \mathrm{d} x\right).
$$

10. 设 $f$ 是定义在 $[a, b]$ 上的函数, 证明: $f \in R[a, b]$ 当且仅当任给 $\varepsilon > 0$, 存在 $g, h \in C[a, b]$, 使得 $g \leqslant f \leqslant h$, 且

$$
\int_ {a} ^ {b} (h (x) - g (x)) \mathrm{d} x <   \varepsilon .
$$

## 9.6 积分的近似计算

虽然利用 Newton-Leibniz 公式可以很方便地算出很多积分, 但如果被积函数的原函数缺乏显式表达式, 或者被积函数比较复杂, 人们往往使用近似计算方法来估计积分的值.

## 1. 矩形公式

设 $f \in R[a, b]$. 取 $c \in [a, b]$, 我们可以近似地用矩形的面积 $f(c)(b - a)$ 来估算 $f$ 在 $[a, b]$ 上的积分. 为了估计误差, 设 $f$ 可导, 且 $|f'(x)| \leqslant M_1, \forall x \in (a, b)$. 由微分中值定理可得

$$
\begin{array}{l} \left| \int_ {a} ^ {b} f (x) \mathrm{d} x - f (c) (b - a) \right| = \left| \int_ {a} ^ {b} (f (x) - f (c)) \mathrm{d} x \right| = \left| \int_ {a} ^ {b} f ^ {\prime} (\xi) (x - c) \mathrm{d} x \right| \\ \leqslant \int_ {a} ^ {b} | f ^ {\prime} (\xi) | | x - c | \mathrm{d} x \leqslant M _ {1} \int_ {a} ^ {b} | x - c | \mathrm{d} x \\ = \frac {1}{2} M _ {1} \left((c - a) ^ {2} + (b - c) ^ {2}\right). \\ \end{array}
$$

取 $c = \frac{1}{2} (a + b)$ 可得

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x - f \Big (\frac {a + b}{2} \Big) (b - a) \right| \leqslant \frac {1}{4} M _ {1} (b - a) ^ {2}. \tag {9.6.1}
$$

---

34

第九章 Riemann 积分

若 $f$ 为一次函数, 则上式左端为零 (即误差为零), 而右端并不能反映出这一点. 为此我们进一步设 $f$ 二阶可导, 且 $|f''(x)| \leqslant M_2, \forall x \in (a, b)$. 将 $f$ 在 $\frac{1}{2} (a + b)$ 处做Taylor展开可得

$$
f (x) = f \Big (\frac {a + b}{2} \Big) + f ^ {\prime} \Big (\frac {a + b}{2} \Big) \Big (x - \frac {a + b}{2} \Big) + \frac {1}{2} f ^ {\prime \prime} (\xi) \Big (x - \frac {a + b}{2} \Big) ^ {2},
$$

两边积分, 得

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = f \Big (\frac {a + b}{2} \Big) (b - a) + \frac {1}{2} \int_ {a} ^ {b} f ^ {\prime \prime} (\xi) \Big (x - \frac {a + b}{2} \Big) ^ {2} \mathrm{d} x,
$$

因此有

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x - f \left(\frac {a + b}{2}\right) (b - a) \right| \leqslant \frac {1}{2} M _ {2} \int_ {a} ^ {b} \left(x - \frac {a + b}{2}\right) ^ {2} \mathrm{d} x = \frac {1}{2 4} M _ {2} (b - a) ^ {3}. \tag {9.6.2}
$$

一般地, 我们将区间 $[a, b]$ 作 $n$ 等分, 在每一个小区间上均用矩形面积去逼近积分, 令

$$
R _ {n} = \sum_ {i = 1} ^ {n} f \left(\frac {x _ {i - 1} + x _ {i}}{2}\right) \frac {b - a}{n} = \frac {b - a}{n} \sum_ {i = 1} ^ {n} f \left(a + \frac {2 i - 1}{2 n} (b - a)\right), \tag {9.6.3}
$$

这样就得到了 $f$ 在 $[a,b]$ 上积分的近似值, 称为 $f$ 在 $[a,b]$ 上的矩形公式. 当 $f$ 可导时, 误差估计为

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x - R _ {n} \right| \leqslant \sum_ {i = 1} ^ {n} \frac {1}{4} M _ {1} \Big (\frac {b - a}{n} \Big) ^ {2} = \frac {M _ {1}}{4 n} (b - a) ^ {2}; \tag {9.6.4}
$$

当 $f$ 二阶可导时, 误差估计为

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x - R _ {n} \right| \leqslant \sum_ {i = 1} ^ {n} \frac {1}{2 4} M _ {2} \Big (\frac {b - a}{n} \Big) ^ {3} = \frac {M _ {2}}{2 4 n ^ {2}} (b - a) ^ {3}. \tag {9.6.5}
$$

## 2. 梯形公式

设 $f\in C[a,b]$ .记

$$
\ell (x) = \frac {x - b}{a - b} f (a) + \frac {x - a}{b - a} f (b), \forall x \in [ a, b ].
$$

我们有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x \approx \int_ {a} ^ {b} \ell (x) \mathrm{d} x = \frac {f (a) + f (b)}{2} (b - a),
$$

这称为梯形公式. 为了估计误差, 我们先证明一个引理.

引理9.6.1 设 $g \in C[a, b]$. 如果 $g$ 在 $(a, b)$ 中二阶可导且 $g(a) = g(b) = 0$, 则任给 $c \in [a, b]$, 存在 $\xi \in (a, b)$, 使得

$$
g (c) = \frac {1}{2} g ^ {\prime \prime} (\xi) (c - a) (c - b). \tag {9.6.6}
$$

---

9.6 积分的近似计算

35

证明 不妨设 $c \in (a, b)$, 令

$$
h (x) = g (x) - \frac {g (c)}{(c - a) (c - b)} (x - a) (x - b), x \in [ a, b ].
$$

此时 $h(a) = h(c) = h(b) = 0$。由Rolle定理可知，存在 $\xi_1 \in (a, c)$，$\xi_2 \in (c, b)$，使得 $h'(\xi_1) = 0$，$h'(\xi_2) = 0$。对 $h'$ 应用Rolle定理可得 $\xi \in (\xi_1, \xi_2)$，使得 $h''(\xi) = 0$。简单的计算表明

$$
h ^ {\prime \prime} (\xi) = g ^ {\prime \prime} (\xi) - \frac {2 g (c)}{(c - a) (c - b)},
$$

整理以后即得欲证结论.

如果 $f$ 二阶可导, 且 $|f''(x)| \leqslant M_2$, $\forall x \in (a, b)$, 则对 $g = f - \ell$ 应用上述引理可知

$$
| f (x) - \ell (x) | \leqslant \frac {1}{2} M _ {2} (x - a) (b - x), \forall x \in [ a, b ].
$$

积分可得如下误差估计:

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x - \frac {f (a) + f (b)}{2} (b - a) \right| \leqslant \frac {1}{2} M _ {2} \int_ {a} ^ {b} (x - a) (b - x) \mathrm{d} x = \frac {M _ {2}}{1 2} (b - a) ^ {3}. \tag {9.6.7}
$$

将区间  $[a, b]$  作 n 等分, 在每一个小区间上均用梯形面积去逼近积分, 则得到 f 的如下梯形公式:

$$
T _ {n} = \sum_ {i = 1} ^ {n} \frac {f (x _ {i - 1}) + f (x _ {i})}{2} \frac {b - a}{n} = \frac {b - a}{n} \left(\sum_ {i = 1} ^ {n - 1} f \left(a + \frac {i}{n} (b - a)\right) + \frac {f (a) + f (b)}{2}\right). \tag {9.6.8}
$$

相应地有误差估计

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x - T _ {n} \right| \leqslant \sum_ {i = 1} ^ {n} \frac {1}{1 2} M _ {2} \Big (\frac {b - a}{n} \Big) ^ {3} = \frac {M _ {2}}{1 2 n ^ {2}} (b - a) ^ {3}. \tag {9.6.9}
$$

## 3. Simpson $^{①}$ 公式

设 $f$ 三阶可导, 且 $|f'''(x)| \leqslant M_3, \forall x \in [a, b]$. 考虑经过平面上三点

$$
(a, f (a)), \quad \Big (\frac {a + b}{2}, f \Big (\frac {a + b}{2} \Big) \Big), \quad (b, f (b))
$$

的抛物线, 即考虑满足条件

$$
p _ {2} (a) = f (a), p _ {2} \Big (\frac {a + b}{2} \Big) = f \Big (\frac {a + b}{2} \Big), p _ {2} (b) = f (b)
$$

的二次插值多项式, 其表达式为

$$
p _ {2} (x) = \frac {\left(x - \frac {a + b}{2}\right) (x - b)}{\left(a - \frac {a + b}{2}\right) (a - b)} f (a) + \frac {(x - a) (x - b)}{\left(\frac {a + b}{2} - a\right) \left(\frac {a + b}{2} - b\right)} f \left(\frac {a + b}{2}\right) +
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Simpson, Thomas, 1710 年 8 月 20 日—1761 年 5 月 14 日, 英国数学家.</span></small>

---

36

第九章 Riemann 积分

$$
\frac {(x - a) \left(x - \frac {a + b}{2}\right)}{(b - a) \left(b - \frac {a + b}{2}\right)} f (b),
$$

直接的计算表明

$$
\int_ {a} ^ {b} p _ {2} (x) \mathrm{d} x = \frac {b - a}{6} \left(f (a) + 4 f \left(\frac {a + b}{2}\right) + f (b)\right),
$$

这是 $f$ 积分的近似值, 称为一次抛物线公式或 Simpson 公式. 为了较好地估计误差, 下面假设 $f$ 四阶可导. 我们选定常数 $\mu$, 使得函数

$$
g (x) = f (x) - p _ {2} (x) - \mu (x - a) \left(x - \frac {a + b}{2}\right) (x - b)
$$

在 $\frac{a + b}{2}$ 处的导数为零. 设 $c \neq a, \frac{a + b}{2}, b$. 考虑辅助函数

$$
F (x) = g (x) - \frac {g (c)}{(c - a) \left(c - \frac {a + b}{2}\right) ^ {2} (c - b)} (x - a) \left(x - \frac {a + b}{2}\right) ^ {2} (x - b),
$$

此时 $F$ 以 $a, \frac{a + b}{2}, b, c$ 为零点, $F^{\prime}\left(\frac{a + b}{2}\right) = 0$. 由 Rolle 定理可知, $F^{\prime}$ 存在三个不同的零点 $\xi_1, \xi_2, \xi_3$, 且这三个点与 $\frac{a + b}{2}$ 也不相同. 因此对 $F^{\prime}$ 继续重复使用 Rolle 定理, 就得到一个 $\xi$, 使得 $F^{(4)}(\xi) = 0$. 即

$$
f ^ {(4)} (\xi) - \frac {g (c)}{(c - a) \left(c - \frac {a + b}{2}\right) ^ {2} (c - b)} 4! = 0,
$$

上式可以改写为 (c 换成 x)

$$
g (x) = \frac {1}{2 4} f ^ {(4)} (\xi) (x - a) \Big (x - \frac {a + b}{2} \Big) ^ {2} (x - b),
$$

积分可得

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) \mathrm{d} x - \frac {b - a}{6} \left(f (a) + 4 f \left(\frac {a + b}{2}\right) + f (b)\right) \\ = \frac {1}{2 4} \int_ {a} ^ {b} f ^ {(4)} (\xi) (x - a) \left(x - \frac {a + b}{2}\right) ^ {2} (x - b) \mathrm{d} x. \\ \end{array}
$$

如果 $|f^{(4)}|\leqslant M_4$ ，则有下面的误差估计:

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x - \frac {b - a}{6} \left(f (a) + 4 f \left(\frac {a + b}{2}\right) + f (b)\right) \right|
$$

---

9.6 积分的近似计算

37

$$
\leqslant \frac {1}{2 4} M _ {4} \int_ {a} ^ {b} (x - a) \left(x - \frac {a + b}{2}\right) ^ {2} (b - x) \mathrm{d} x = \frac {M _ {4}}{1 8 0 \times 2 ^ {4}} (b - a) ^ {5}. \tag {9.6.10}
$$

我们可以将区间 $[a, b]$ 作 $n$ 等分, 在每个小区间上用抛物线做逼近得到一般的 Simpson 公式:

$$
S _ {n} = \sum_ {i = 1} ^ {n} \frac {b - a}{6 n} \left(f (x _ {i - 1}) + 4 f \left(\frac {x _ {i - 1} + x _ {i}}{2}\right) + f (x _ {i})\right). \tag {9.6.11}
$$

误差估计为

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x - S _ {n} \right| \leqslant \frac {M _ {4}}{1 8 0 (2 n) ^ {4}} (b - a) ^ {5}. \tag {9.6.12}
$$

还可以用高阶多项式去逼近被积函数, 从而得到积分的其他近似计算公式, 读者可参考其他专门著作, 我们不再赘述.

例9.6.1 计算积分 $\frac{\pi}{4} = \int_0^1\frac{1}{1 + x^2}\mathrm{d}x$ 的近似值.

解 以 $n = 2$ 为例. 用矩形公式计算积分的近似值为

$$
R _ {2} = \frac {1}{2} \Big (f \Big (\frac {1}{4} \Big) + f \Big (\frac {3}{4} \Big) \Big) = \frac {3 3 6}{4 2 5} \approx 0. 7 9 1;
$$

用梯形公式计算积分的近似值为

$$
T _ {2} = \frac {1}{2} \Big (\frac {1}{2} f (0) + f \Big (\frac {1}{2} \Big) + \frac {1}{2} f (1) \Big) = \frac {3 1}{4 0} = 0. 7 7 5;
$$

用 Simpson 公式计算积分的近似值为

$$
\begin{array}{l} S _ {2} = \frac {1}{1 2} \left(f (0) + 4 f \left(\frac {1}{4}\right) + 2 f \left(\frac {1}{2}\right) + 4 f \left(\frac {3}{4}\right) + f (1)\right) \\ = \frac {8 0 1 1}{1 0 2 0 0} \approx 0. 7 8 5 3 9. \\ \end{array}
$$

利用数学归纳法可以将函数 $f(x) = \frac{1}{1 + x^2}$ 的四阶导数表示为

$$
f ^ {(4)} (x) = (\arctan x) ^ {(5)} = 2 4 \cos^ {5} (\arctan x) \sin 5 \Bigl (\arctan x + \frac {\pi}{2} \Bigr),
$$

这说明 $\left| {f}^{\left( 4\right) }\right|  \leq  {24}$ . 于是 $n = 2$ 时 Simpson 公式的误差要小于

$$
\frac {2 4}{1 8 0 \times 4 ^ {4}} = \frac {1}{1 9 2 0} <   0. 0 0 0 5.
$$

## 习题9.6

1. 分别用矩形公式、梯形公式和 Simpson 公式计算积分 $\ln 2 = \int_{1}^{2} \frac{\mathrm{d}x}{x}$ 的近似值, 要求误差小于 $10^{-2}$.

---

38

第九章 Riemann 积分

2. Simpson 公式计算积分 $\int_{0}^{1} \mathrm{e}^{-x^{2}} \, \mathrm{d}x$ 的近似值, 要求误差小于 $10^{-4}$.

3. 分别用 $n = 10$ 时的梯形公式和 Simpson 公式计算积分 $\int_{0}^{1} \frac{\mathrm{d}x}{\sqrt{1 + x^3}}$ 的近似值, 并估计误差.

4. 证明: 矩形公式和梯形公式之间满足关系式 $R_{n} = 2T_{2n} - T_{n}$.

5. 证明: 矩形公式、梯形公式和 Simpson 公式之间满足关系式

$$
S _ {n} = \frac {2}{3} R _ {n} + \frac {1}{3} T _ {n}.
$$

6. 设 $f \in C^{1}[a, b]$, 且 $|f'| \leqslant M$. 证明:

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x - \frac {f (a) + f (b)}{2} (b - a) \right| \leqslant \frac {1}{4} M (b - a) ^ {2}.
$$

7. 设 $f \in C^{2}[a, b]$, 证明: 存在 $\xi \in (a, b)$, 使得

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = (b - a) f \left(\frac {a + b}{2}\right) + \frac {1}{2 4} (b - a) ^ {3} f ^ {\prime \prime} (\xi).
$$

8. 设 $f \in C^4[a, b]$, 用分部积分证明:

$$
\begin{array}{l} \int_ {a} ^ {b} f (x) \mathrm{d} x - \frac {f (a) + f (b)}{2} (b - a) \\ = \frac {1}{2 4} \int_ {a} ^ {b} f ^ {(4)} (x) (x - a) ^ {2} (x - b) ^ {2} \mathrm{d} x - \frac {1}{1 2} (b - a) ^ {2} (f ^ {\prime} (b) - f ^ {\prime} (a)). \\ \end{array}
$$

9. 是否存在常数 $C$, 使得对于满足条件 $|f^{(3)}| \leqslant M$ 的每一个函数 $f$, 均有如下估计:

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x - \frac {f (a) + f (b)}{2} (b - a) \right| \leqslant C M (b - a) ^ {4}?
$$

请说明理由.

10. 设 $f$ 在 $[a, b]$ 上三阶可导, 请用 $f$ 的三阶导数对 Simpson 公式做误差估计.

## 9.7 积分的应用

许多实际的应用问题都可以转化为积分。我们以几何中求弧长、面积、体积以及物理中求功、力矩、转动惯量等为例说明怎样将问题转化为积分的形式并计算出相应的积分。

---

9.7 积分的应用

39

## 9.7.1 曲线的长度

设 $I = [\alpha, \beta]$, $\sigma$ 是从 $I$ 到平面的映射, 用分量表示为

$$
\sigma (t) = (x (t), y (t)), t \in I.
$$

如果 $x, y \in C(I)$, 则称 $\sigma$ 为 $\mathbb{R}^2$ 上的连续曲线. 如果 $x, y \in C^1(I)$, 则称 $\sigma$ 为 $C^1$ 曲线.

设 $\sigma$ 为 $C^1$ 曲线, 我们想求它的弧长. 为此, 在 $\sigma$ 上取相邻的两点 $\sigma(t), \sigma(t + \delta t)$, 这两点之间的弧长 $\delta s$ 约等于连接这两点的直线段的长度:

$$
\begin{array}{l} \delta s \approx \sqrt {(x (t + \delta t) - x (t)) ^ {2} + (y (t + \delta t) - y (t)) ^ {2}} \\ \approx \left((x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}\right) ^ {\frac {1}{2}} \delta t. \\ \end{array}
$$

将 $\sigma$ 分成若干小段, 将每一段的弧长相加, 得到的总弧长可以转化为如下积分:

$$
L (\sigma) = \int_ {\alpha} ^ {\beta} \left((x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}\right) ^ {\frac {1}{2}} \mathrm{d} t.
$$

这种局部分析方法常称为微元法. 下面我们再补充一些推导细节. 将  $[\alpha, \beta]$  分割为  $\alpha = t_{0} < t_{1} < \cdots < t_{n} = \beta$ , 点  $(x(t_{i}), y(t_{i}))$  把曲线分成若干段, 每一段的长度可以近似地用直线段的长度表示 (图 9.4), 即

$$
L (\sigma) \approx \sum_ {i = 1} ^ {n} \sqrt {(x (t _ {i}) - x (t _ {i - 1})) ^ {2} + (y (t _ {i}) - y (t _ {i - 1})) ^ {2}}.
$$

![](../../raw/pages_0337-0352/images/page_346_chart_12.jpg)

<details>
<summary>line</summary>

| X | Y |
| --- | --- |
| 0 | 0 |
| ~1.5 | ~0.2 |
| ~3.5 | ~0.8 |
| ~6.5 | ~0.95 |
| ~8.5 | ~0.98 |
</details>

图 9.4 曲线的长度

由Lagrange微分中值定理，存在 $\xi_{i},\eta_{i}\in (t_{i - 1},t_{i})$ ，使得

$$
x (t _ {i}) - x (t _ {i - 1}) = x ^ {\prime} (\xi_ {i}) (t _ {i} - t _ {i - 1}), y (t _ {i}) - y (t _ {i - 1}) = y ^ {\prime} (\eta_ {i}) (t _ {i} - t _ {i - 1}),
$$

从而有

$$
\sqrt {(x (t _ {i}) - x (t _ {i - 1})) ^ {2} + (y (t _ {i}) - y (t _ {i - 1})) ^ {2}} = \sqrt {(x ^ {\prime} (\xi_ {i})) ^ {2} + (y ^ {\prime} (\eta_ {i})) ^ {2}} \Delta t _ {i}.
$$

利用不等式 $\left|\sqrt{a^2 + b^2} -\sqrt{a^2 + c^2}\right|\leqslant |b - c|$ 可得

$$
\left| \sqrt {(x ^ {\prime} (\xi_ {i})) ^ {2} + (y ^ {\prime} (\eta_ {i})) ^ {2}} \Delta t _ {i} - \sqrt {(x ^ {\prime} (\xi_ {i})) ^ {2} + (y ^ {\prime} (\xi_ {i})) ^ {2}} \Delta t _ {i} \right| \leqslant | y ^ {\prime} (\eta_ {i}) - y ^ {\prime} (\xi_ {i}) | \Delta t _ {i},
$$

而当 $\| \mathrm{P}\| = \max \{|t_i - t_{i - 1}|\} \to 0$ 时

$$
\sum_ {i = 1} ^ {n} | y ^ {\prime} (\eta_ {i}) - y ^ {\prime} (\xi_ {i}) | \Delta t _ {i} \leqslant \sum_ {i = 1} ^ {n} \omega_ {i} (y ^ {\prime}) \Delta t _ {i} \rightarrow 0,
$$

---

40

第九章 Riemann积分

因此有

$$
\begin{array}{l} L (\sigma) = \lim _ {\| P \| \rightarrow 0} \sum_ {i = 1} ^ {n} \sqrt {(x (t _ {i}) - x (t _ {i - 1})) ^ {2} + (y (t _ {i}) - y (t _ {i - 1})) ^ {2}} \\ = \lim _ {\| P \| \rightarrow 0} \sum_ {i = 1} ^ {n} \sqrt {\left(x ^ {\prime} \left(\xi_ {i}\right)\right) ^ {2} + \left(y ^ {\prime} \left(\xi_ {i}\right)\right) ^ {2}} \Delta t _ {i} \\ = \int_ {\alpha} ^ {\beta} \left((x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}\right) ^ {\frac {1}{2}} \mathrm{d} t. \\ \end{array}
$$

只要 $x^{\prime},y^{\prime}$ 在 $[\alpha ,\beta ]$ 中可积，上述推导就是成立的.记 $\sigma '(t) = (x'(t),y'(t))$ ，称为 $\sigma$ 的切向量. $\sigma$ 的弧长就等于其切向量长度的积分.如果切向量处处非零，令

$$
\varphi (t) = \int_ {\alpha} ^ {t} \| \sigma^ {\prime} (u) \| \mathrm{d} u = \int_ {\alpha} ^ {t} \big ((x ^ {\prime} (u)) ^ {2} + (y ^ {\prime} (u)) ^ {2} \big) ^ {\frac {1}{2}} \mathrm{d} u, t \in [ \alpha , \beta ].
$$

则 $\varphi : [\alpha, \beta] \to [0, L(\sigma)]$ 是严格单调递增函数，从而可逆，其反函数记为 $t = \psi(s)$. 记 $\tilde{\sigma}(s) = \sigma(\psi(s)), s \in [0, L(\sigma)]$. 根据反函数的求导公式可得

$$
\tilde {\sigma} ^ {\prime} (s) = \sigma^ {\prime} (\psi (s)) \psi^ {\prime} (s) = \sigma^ {\prime} (\psi (s)) / \varphi^ {\prime} (t) = \sigma^ {\prime} (t) / \| \sigma^ {\prime} (t) \|,
$$

这说明  $\|\tilde{\sigma}^{\prime}(s)\|=1$ ，此时，s 称为  $\tilde{\sigma}$  的弧长参数.

例 9.7.1 求平面上半径为 r 的圆周的周长.

解 设圆心为 $(a, b)$, 则该圆周可以用参数表示为

$$
x (t) = a + r \cos t, y (t) = b + r \sin t, t \in [ 0, 2 \pi ].
$$

此时 $(x'(t))^2 + (y'(t))^2 \equiv r^2$，这说明圆周的周长为

$$
L = \int_ {0} ^ {2 \pi} r \mathrm{d} t = 2 \pi r.
$$

例 9.7.2 设 a > 0, 求摆线  $(x(t), y(t)) = (a(t - \sin t), a(1 - \cos t))$  一拱的长度 (图 9.5).

解 我们求 $t \in [0, 2\pi]$ 时曲线的长度:

$$
\begin{array}{l} L = \int_ {0} ^ {2 \pi} \left((x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}\right) ^ {\frac {1}{2}} \mathrm{d} t \\ = \int_ {0} ^ {2 \pi} a \big ((1 - \cos t) ^ {2} + \sin^ {2} t \big) ^ {\frac {1}{2}} \mathrm{d} t \\ = 2 a \int_ {0} ^ {2 \pi} \sin \frac {t}{2} \mathrm{d} t = 8 a. \\ \end{array}
$$

![](../../raw/pages_0337-0352/images/page_347_image_17.jpg)

<details>
<summary>text_image</summary>

y
O
x
</details>

图9.5 摆线

---

9.7 积分的应用

41

## 9.7.2 简单图形的面积

(1) 设 $f \in C[a, b]$, 如果 $f > 0$, 则由 $y = f(x)$, $x = a$, $x = b$ ($a < b$) 与 $y = 0$ 围成的曲边梯形的面积为

$$
S = \int_ {a} ^ {b} f (x) \mathrm{d} x.
$$

一般地, 当 $f$ 变号时, 上式仍有意义, 称为代数面积, 而

$$
S = \int_ {a} ^ {b} | f (x) | \mathrm{d} x
$$

才是几何面积 (图 9.6(a)). 更一般地, 由  $y = f_{2}(x)$ ,  $y = f_{1}(x)$  以及 x = a, x = b 围成的图形 (图 9.6(b)) 的面积为

$$
S = \int_ {a} ^ {b} | f _ {2} (x) - f _ {1} (x) | \mathrm{d} x. \tag {9.7.1}
$$

![](../../raw/pages_0337-0352/images/page_348_image_9.jpg)

<details>
<summary>text_image</summary>

y
y = |f(x|)
O a b x
</details>

(a)

![](../../raw/pages_0337-0352/images/page_348_image_11.jpg)

<details>
<summary>text_image</summary>

y
y = f₂(x)
O a b x
y = f₁(x)
</details>

(b)

图 9.6 函数图像围成的图形

例 9.7.3 设 a, b > 0, 求椭圆  $\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1$  所围成的图形面积.

解 由图形的对称性, 有

$$
S = 4 \int_ {0} ^ {a} b \sqrt {1 - \frac {x ^ {2}}{a ^ {2}}} \mathrm{d} x = 4 b \int_ {0} ^ {\frac {\pi}{2}} \sqrt {1 - \sin^ {2} t} a \cos t \mathrm{d} t = 4 a b \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2} t \mathrm{d} t = \pi a b. \quad \square
$$

(2) 设  $\sigma$  为平面曲线, 由极坐标方程

$$
r = r (\theta), \quad \theta \in [ \alpha , \beta ]
$$

给出 (图 9.7), 其中  $r(\theta)$  关于  $\theta$  连续,  $\beta - \alpha \leqslant 2\pi$ . 由  $\sigma$ ,  $\theta = \alpha$ ,  $\theta = \beta$  所围成的图形面积为

$$
S = \lim _ {\| \mathrm{P} \| \to 0} \sum_ {i = 1} ^ {m} \frac {1}{2} r ^ {2} (\xi_ {i}) \Delta \theta_ {i} = \frac {1}{2} \int_ {\alpha} ^ {\beta} r ^ {2} (\theta) \mathrm{d} \theta . \tag {9.7.2}
$$

这个公式是通过使用扇形的面积之和逼近图形面积得到的.

![](../../raw/pages_0337-0352/images/page_348_image_22.jpg)

<details>
<summary>text_image</summary>

y
σ
α
β
O
x
</details>

图9.7 极坐标中的曲线

---

42

第九章 Riemann积分

例 9.7.4 设 a > 0, 求双纽线  $(x^{2} + y^{2})^{2} = a^{2}(x^{2} - y^{2})$  所围成的图形面积.

解 用极坐标  $x = r \cos \theta, y = r \sin \theta$  代入方程, 得

$$
r ^ {2} = a ^ {2} \cos 2 \theta , \quad \theta \in \left[ - \frac {\pi}{4}, \frac {\pi}{4} \right] \cup \left[ \frac {3 \pi}{4}, \frac {5 \pi}{4} \right].
$$

由图形的对称性 (图 9.8) 可得所求面积为

![](../../raw/pages_0337-0352/images/page_349_image_6.jpg)

<details>
<summary>text_image</summary>

r² = a²cos 2θ
O
a
x
y
</details>

图9.8 双纽线

$$
S = 4 \cdot \frac {1}{2} \int_ {0} ^ {\frac {\pi}{4}} r ^ {2} (\theta)   \mathrm{d} \theta = 2 a ^ {2} \int_ {0} ^ {\frac {\pi}{4}} \cos 2 \theta   \mathrm{d} \theta = a ^ {2}. \quad \square
$$

(3) 如果曲线 $\sigma$ 由 $\sigma(t) = (x(t), y(t)), t \in [\alpha, \beta]$ 给出, 其中 $y(t) \geqslant 0$, $x$ 关于 $t$ 单调递增, $x([\alpha, \beta]) = [a, b]$. 则 $\sigma$ 与 $x = a$, $x = b$ 以及 $y = 0$ 围成的曲边梯形 (图9.9(a)) 的面积为

$$
S = \int_ {\alpha} ^ {\beta} y (t) x ^ {\prime} (t)   \mathrm{d} t.
$$

这个公式仍然是通过使用矩形面积之和去逼近曲边梯形得到. 一般地, 如果只设 $x$ 是单调的, 则面积公式为

$$
S = \int_ {\alpha} ^ {\beta} | y (t) x ^ {\prime} (t) |   \mathrm{d} t.
$$

![](../../raw/pages_0337-0352/images/page_349_image_13.jpg)

<details>
<summary>text_image</summary>

y
σ(α)
σ
σ(β)
O
a
b
x
</details>

(a)

![](../../raw/pages_0337-0352/images/page_349_image_15.jpg)

<details>
<summary>text_image</summary>

y
σ
O
x
</details>

(b)

图 9.9 曲线围成的图形

如果 $\sigma$ 在 $t = \alpha, \beta$ 处以外无其他自相交点，则称 $\sigma$ 为简单闭曲线 (图9.9(b))，它所围成的图形的面积为

$$
S = \left| \int_ {\alpha} ^ {\beta} y (t) x ^ {\prime} (t) \mathrm{d} t \right| = \left| \int_ {\alpha} ^ {\beta} x (t) y ^ {\prime} (t) \mathrm{d} t \right|, \tag {9.7.3}
$$

因为

$$
\begin{array}{l} \int_ {\alpha} ^ {\beta} y (t) x ^ {\prime} (t) \mathrm{d} t = y x \Big | _ {\alpha} ^ {\beta} - \int_ {\alpha} ^ {\beta} y ^ {\prime} (t) x (t) \mathrm{d} t \\ = - \int_ {\alpha} ^ {\beta} y ^ {\prime} (t) x (t) \mathrm{d} t, \\ \end{array}
$$

---

9.7 积分的应用

43

所以这个面积公式也可以改写为

$$
S = \frac {1}{2} \left| \int_ {\alpha} ^ {\beta} (y (t) x ^ {\prime} (t) - y ^ {\prime} (t) x (t)) \mathrm{d} t \right|. \tag {9.7.4}
$$

这个公式其实是 Green 公式的推论, 见第十八章.

(4) 旋转曲面的面积

设 $\sigma$ 为平面曲线

$$
\sigma (t) = (x (t), y (t)), t \in [ \alpha , \beta ], y (t) \geqslant 0.
$$

$\sigma$  绕 x 轴旋转所得曲面 (图 9.10) 的面积为

$$
S = \int_ {\alpha} ^ {\beta} 2 \pi y (t) \big ((x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2} \big) ^ {\frac {1}{2}} \mathrm{d} t.
$$

这个公式可推导如下:取 $[\alpha, \beta]$ 的一个分割，在分点 $t_{i-1}, t_i$ 之间的曲线段经过旋转后所形成的曲面的面积约等于圆台的面积，这一部分圆台的面积为

$$
\pi (y (t _ {i - 1}) + y (t _ {i})) \sqrt {(x (t _ {i}) - x (t _ {i - 1})) ^ {2} + (y (t _ {i}) - y (t _ {i - 1})) ^ {2}},
$$

因此

$$
S \approx \sum_ {i = 1} ^ {n} \pi (y (t _ {i - 1}) + y (t _ {i})) \sqrt {(x (t _ {i}) - x (t _ {i - 1})) ^ {2} + (y (t _ {i}) - y (t _ {i - 1})) ^ {2}},
$$

和曲线弧长公式的推导过程类似, 当分割的模趋于零时, 我们近似地有

$$
y (t _ {i - 1}) + y (t _ {i}) \approx 2 y (\xi_ {i}) \quad (\xi_ {i} \in [ t _ {i - 1}, t _ {i} ]),
$$

以及

$$
\sqrt {(x (t _ {i}) - x (t _ {i - 1})) ^ {2} + (y (t _ {i}) - y (t _ {i - 1})) ^ {2}} \approx \sqrt {(x ^ {\prime} (\xi_ {i})) ^ {2} + (y ^ {\prime} (\xi_ {i})) ^ {2}} \Delta t _ {i},
$$

当分割的模趋于零时, 近似逼近所引起的这些误差之和趋于零. 因此有

$$
\begin{array}{l} S = \lim _ {\| \mathrm{P} \| \to 0} \sum_ {i = 1} ^ {n} 2 \pi y (\xi_ {i}) \big ((x ^ {\prime} (\xi_ {i})) ^ {2} + (y ^ {\prime} (\xi_ {i})) ^ {2} \big) ^ {\frac {1}{2}} \Delta t _ {i} \\ = \int_ {\alpha} ^ {\beta} 2 \pi y (t) \big ((x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2} \big) ^ {\frac {1}{2}} \mathrm{d} t. \\ \end{array}
$$

![](../../raw/pages_0337-0352/images/page_350_image_20.jpg)

<details>
<summary>text_image</summary>

y
σ(t)
O
x
</details>

图9.10 旋转曲面

![](../../raw/pages_0337-0352/images/page_350_image_22.jpg)

<details>
<summary>natural_image</summary>

Simple line drawing of a human eye within an oval shape (no text or symbols)
</details>

图 9.11 环面 (轮胎面)

---

44

第九章 Riemann积分

例 9.7.5 设 b > a > 0, 将圆周  $(x - b)^{2} + y^{2} = a^{2}$  绕 y 轴旋转, 求所得旋转曲面 (图 9.11) 的面积.

解 圆周的参数方程为

$$
x (t) = b + a \cos t, y (t) = a \sin t, t \in [ 0, 2 \pi ].
$$

故旋转曲面 (轮胎面) 面积为

$$
\begin{array}{l} S = \int_ {0} ^ {2 \pi} 2 \pi (b + a \cos t) (a ^ {2} \sin^ {2} t + a ^ {2} \cos^ {2} t) ^ {\frac {1}{2}} \mathrm{d} t \\ = 2 \pi a \int_ {0} ^ {2 \pi} (b + a \cos t) \mathrm{d} t = 4 \pi^ {2} a b. \\ \end{array}
$$

![](../../raw/pages_0337-0352/images/page_351_image_7.jpg)

## 9.7.3 简单立体的体积

## (1) 平行截面之间的立体体积

设 $\Omega$ 为 $\mathbb{R}^3$ 中一块物体, 夹在平面 $x = a$ 与 $x = b (a < b)$ 之间 (图9.12(a)). 记 $S(x)$ 为 $x \in [a, b]$ 处垂直于 $x$ 轴的平面截 $\Omega$ 的截面面积函数. 如果 $S(x)$ 关于 $x$ 连续, 则 $\Omega$ 的体积为

$$
V = \int_ {a} ^ {b} S (x) \mathrm{d} x. \tag {9.7.5}
$$

这个公式是重积分化累次积分的特例, 见第十六章. 特别地, 如果两块物体 $\Omega_{A}$ 和 $\Omega_{B}$ 的截面面积函数相等, 则其体积相同 (图 9.12(b)). 这是公元 5 到 6 世纪由祖暅 (祖冲之之子) 在刘徽思想的基础上所发现的事实, 17 世纪时 Cavalieri$^{①}$ 也发现了这样的事实.

![](../../raw/pages_0337-0352/images/page_351_image_13.jpg)

<details>
<summary>text_image</summary>

x
b
Ω
a
O
z
y
</details>

(a)

![](../../raw/pages_0337-0352/images/page_351_image_15.jpg)

<details>
<summary>text_image</summary>

Ω_A
Ω_B
</details>

(b)

图9.12 简单立体图形

例 9.7.6 设 a, b, c > 0, 求椭球体  $\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} + \frac{z^{2}}{c^{2}} \leqslant 1$  (图 9.13) 的体积.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Cavalieri, Bonaventura Francesco, 1598 年—1647 年 11 月 30 日, 意大利数学家.</span></small>

---

9.7 积分的应用

45

解 固定 $x \in (-a, a)$, 它的截面为椭圆面

$$
\frac {y ^ {2}}{b ^ {2}} + \frac {z ^ {2}}{c ^ {2}} \leqslant 1 - \frac {x ^ {2}}{a ^ {2}},
$$

截面面积为

$$
\begin{array}{l} S (x) = \pi b \Big (1 - \frac {x ^ {2}}{a ^ {2}} \Big) ^ {\frac {1}{2}} c \Big (1 - \frac {x ^ {2}}{a ^ {2}} \Big) ^ {\frac {1}{2}} \\ = \pi b c \Big (1 - \frac {x ^ {2}}{a ^ {2}} \Big), \\ \end{array}
$$

故椭球体的体积为

$$
V = \int_ {- a} ^ {a} S (x) \mathrm{d} x = \int_ {- a} ^ {a} \pi b c \Big (1 - \frac {x ^ {2}}{a ^ {2}} \Big) \mathrm{d} x = \frac {4}{3} \pi a b c.
$$

![](../../raw/pages_0353-0368/images/page_352_image_8.jpg)

<details>
<summary>text_image</summary>

y
b
O
a
x
c
z
</details>

图9.13 椭球体

## (2) 旋转体的体积

设 $f \in C[a, b]$, $\Omega$ 是由平面图形 $\{(x, y) | a \leqslant x \leqslant b, 0 \leqslant |y| \leqslant |f(x)|\}$ 绕 $x$ 轴旋转一周所得的旋转体 (图9.14). 该旋转体在 $x \in [a, b]$ 处的截面为圆盘, 其面积为 $S(x) = \pi f^2(x)$. 因此 $\Omega$ 的体积为

$$
V = \int_ {a} ^ {b} S (x)   \mathrm{d} x = \pi \int_ {a} ^ {b} f ^ {2} (x)   \mathrm{d} x.
$$

例 9.7.7 求高为 h, 底半径为 r 的圆锥体 (图 9.15) 的体积.

解 由上面的体积公式可得

$$
V = \pi \int_ {0} ^ {h} \left(\frac {r}{h} x\right) ^ {2} \mathrm{d} x = \frac {1}{3} \pi r ^ {2} h.
$$

![](../../raw/pages_0353-0368/images/page_352_image_16.jpg)

<details>
<summary>text_image</summary>

|y| ≤ |f(x)|
O
a
b
x
y
z
</details>

图9.14 旋转体

![](../../raw/pages_0353-0368/images/page_352_image_18.jpg)

<details>
<summary>text_image</summary>

y
r
O
h
x
z
</details>

图9.15 圆锥体

## 9.7.4 物理应用举例

例 9.7.8 设某线状物质分布在区间  $[a, a + l]$  上, 其中 a, l > 0. 设该物质的线密度为  $\rho(x) = x - a$ , 求位于原点的质量为 m 的质点所受该物质的引力.

---

46

第九章 Riemann积分

解 取位于 $[x, x + \delta x]$ 的一小段物质, 其质量 $\delta M$ 约等于 $\rho(x)\delta x$, 它对质点的引力为

$$
\delta F \approx \frac {G m \delta M}{x ^ {2}} \approx \frac {G m (x - a)}{x ^ {2}} \delta x,
$$

其中 $G$ 为引力常量. 于是质点所受到的总的引力为

$$
\begin{array}{l} F = \int_ {a} ^ {a + l} \frac {G m (x - a)}{x ^ {2}} \mathrm{d} x = G m \int_ {a} ^ {a + l} \left(\frac {1}{x} - \frac {a}{x ^ {2}}\right) \mathrm{d} x \\ = G m \Big (\ln \frac {a + l}{a} - \frac {l}{a + l} \Big). \\ \end{array}
$$

![](../../raw/pages_0353-0368/images/page_353_image_6.jpg)

例 9.7.9 设轻质弹簧一端固定, 将另一端从平衡位置拉伸一小段, 求所需要做的功.

解 设平衡位置为原点, 拉伸长度为 $l$. 当 $x \in [0, l]$ 时, 弹簧的拉力为 $F = \kappa x$, 其中 $\kappa$ 为弹簧的弹性系数. 从 $x$ 拉伸一小段到 $x + \delta x$ 时, 所需要做的功 $\delta W$ 约等于 $F \delta x$. 因此总的功为

$$
W = \int_ {0} ^ {l} F \mathrm{d} x = \int_ {0} ^ {l} \kappa x \mathrm{d} x = \frac {1}{2} \kappa l ^ {2}.
$$

![](../../raw/pages_0353-0368/images/page_353_image_10.jpg)

设质量为 $m$ 的质点绕某定轴 $\ell$ 旋转, 转动的角速度 $\omega$ 为常数, 则质点的动能为

$$
E = \frac {1}{2} m v ^ {2} = \frac {1}{2} m r ^ {2} \omega^ {2} = \frac {1}{2} I _ {\ell} \omega^ {2},
$$

其中 $r$ 是质点到定轴的距离, $I_{\ell} = mr^{2}$, 称为质点对轴 $\ell$ 的转动惯量.

例 9.7.10 设平面上有某线状物质, 其坐标用参数表示为  $x = x(t)$ ,  $y = y(t)$ ,  $t \in [\alpha, \beta]$ . 设该物质的线密度为  $\rho(t)$ , 求该物质关于 x 轴以及 y 轴的转动惯量.

解 取参数位于  $[t, t + \delta t]$  的一小段物质, 其质量  $\delta m$  约等于  $\rho(t)\delta s$ , 其中  $\delta s$  是这一小段物质的长度:

$$
\delta s \approx \sqrt {(x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}} \delta t.
$$

这一小段物质关于 $x$ 轴的转动惯量 ${\delta }{I}_{x}$ 约等于

$$
\delta I _ {x} \approx (\delta m) y ^ {2} (t) \approx \rho (t) y ^ {2} (t) \sqrt {(x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}} \delta t,
$$

这说明该物质关于 $x$ 轴的转动惯量为

$$
I _ {x} = \int_ {\alpha} ^ {\beta} \rho (t) y ^ {2} (t) \sqrt {(x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}}   \mathrm{d} t.
$$

同理, 它关于 $y$ 轴的转动惯量为

$$
I _ {y} = \int_ {\alpha} ^ {\beta} \rho (t) x ^ {2} (t) \sqrt {(x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}}   \mathrm{d} t.
$$

![](../../raw/pages_0353-0368/images/page_353_image_23.jpg)

例 9.7.11 设线状物质如前例所述, 求其质量和质心.

---

9.7 积分的应用

47

解 根据前例中的讨论我们可以知道,该物质的总质量为

$$
M = \int_ {\alpha} ^ {\beta} \rho (t) \sqrt {(x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}}   \mathrm{d} t.
$$

该物质关于 $x, y$ 轴的静力矩分别为

$$
M _ {x} = \int_ {\alpha} ^ {\beta} y (t) \rho (t) \sqrt {(x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}}   \mathrm{d} t, M _ {y} = \int_ {\alpha} ^ {\beta} x (t) \rho (t) \sqrt {(x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}}   \mathrm{d} t.
$$

于是质心坐标 $\bar{x},\bar{y}$ 分别为

$$
\bar {x} = \frac {M _ {y}}{M} = \frac {1}{M} \int_ {\alpha} ^ {\beta} x (t) \rho (t) \sqrt {(x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}}   \mathrm{d} t,
$$

$$
\bar {y} = \frac {M _ {x}}{M} = \frac {1}{M} \int_ {\alpha} ^ {\beta} y (t) \rho (t) \sqrt {(x ^ {\prime} (t)) ^ {2} + (y ^ {\prime} (t)) ^ {2}}   \mathrm{d} t.
$$

□

特别地, 当上述线状物质均匀分布时, 不妨设 $\rho \equiv 1$, 物质的长度为 $l$, 则

$$
\bar {x} = \frac {1}{l} \int_ {0} ^ {l} x \mathrm{d} s, \bar {y} = \frac {1}{l} \int_ {0} ^ {l} y \mathrm{d} s,
$$

其中 $\mathrm{ds} = \sqrt{(x'(t))^2 + (y'(t))^2}\mathrm{dt}$ 上式中的第二个等式可以改写为

$$
2 \pi \bar {y} l = 2 \pi \int_ {0} ^ {l} y \mathrm{d} s,
$$

上式右边表示旋转面的面积, 由此得到

## 定理 9.7.1 (Guldin $^{①}$ 第一定理)

平面曲线绕平面上不与其相交的轴旋转一周，

所得旋转面的面积等于该曲线的质心绕同一轴旋转所产生的圆周长乘该曲线的弧长.

类似于曲线的情形, 我们也可以处理面状物质的静力矩和质心. 为了方便起见, 设物质的面密度恒为 1, 其形状为曲边四边形:

$$
a \leqslant x \leqslant b, 0 \leqslant g (x) \leqslant y \leqslant f (x).
$$

取小区间 $[x, x + \delta x]$, 将相应的曲边梯形底长为 $\delta x$, 高为 $f(x) - g(x)$ 的小矩形, 其质量 $\delta m$ 约等于 $(f(x) - g(x))\delta x$, 因此总质量为

$$
M = \int_ {a} ^ {b} (f (x) - g (x))   \mathrm{d} x.
$$

小矩形关于 $y$ 轴的静力矩为

$$
\delta M _ {y} \approx x \delta m \approx x (f (x) - g (x)) \delta x,
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Guldin, Paul, 1577 年 6 月 12 日—1643 年 12 月 3 日, 瑞士数学家.</span></small>

---

48

第九章 Riemann 积分

关于 $x$ 轴的静力矩为

$$
\delta M _ {x} \approx \frac {1}{2} (f (x) + g (x)) \delta m \approx \frac {1}{2} \big (f ^ {2} (x) - g ^ {2} (x) \big) \delta x.
$$

因此质心坐标为

$$
\begin{array}{l} \bar {x} = \frac {M _ {y}}{M} = \frac {1}{M} \int_ {a} ^ {b} x (f (x) - g (x))   \mathrm{d} x, \\ \bar {y} = \frac {M _ {x}}{M} = \frac {1}{2 M} \int_ {a} ^ {b} \left(f ^ {2} (x) - g ^ {2} (x)\right) \mathrm{d} x. \\ \end{array}
$$

由上式还可得到

$$
2 \pi \bar {y} M = \pi \int_ {a} ^ {b} \left(f ^ {2} (x) - g ^ {2} (x)\right) \mathrm{d} x,
$$

上式左端的 $M$ 为曲边梯形的面积, 右端是旋转体的体积. 由此可得

定理 9.7.2 (Guldin 第二定理) 平面图形绕此平面上不与其内部相交的轴旋转一周, 所得旋转体的体积等于该平面图形的质心绕同一轴旋转所产生的圆周长乘该平面图形的面积.

## 习题 9.7

1. 求下列曲线的弧长:

(1) $y = x^{\frac{3}{2}}, 0 \leqslant x \leqslant 4;$
(2) $x = \mathrm{e}^{t}\cos t, y = \mathrm{e}^{t}\sin t, t \in [0, 2\pi]$;
(3) $r = a(1 + \cos \theta), a > 0, \theta \in [0, 2\pi]$;
(4) $y^{2}=2ax,\quad a>0,\quad0\leqslant x\leqslant a.$

2. 求下列曲线所围成图形的面积:

(1) $y^{2}=ax,\quad y=\frac{1}{a}x^{2},\quad a>0;$
(2) $y^{2}=2x,\quad x=5;$
(3) $x^{2} + 9y^{2} = 1$;
(4) $y = x(x - 1)(x - 2), y = 0;$
(5) $r = a(1 - \cos \theta), a > 0, \theta \in [0, 2\pi]$;
(6) $x = a\cos^3 t, y = a\sin^3 t, a > 0, t \in [0, 2\pi]$;

3. 求下列旋转面的面积:

(1) $y = \tan x$ 绕 $x$ 轴, $x \in \left[0, \frac{\pi}{4}\right]$;
(2) $x = a(t - \sin t), y = a(1 - \cos t)$ 绕直线 $y = a, a > 0, t \in \left[\frac{\pi}{2}, \frac{3\pi}{2}\right]$;
(3) $x = a\cos^3 t, y = a\sin^3 t$ 绕 $x$ 轴, $a > 0$;
(4) $r^{2}=a^{2}\cos2\theta$ 绕射线 $\theta=\frac{\pi}{4}$.

---

9.7 积分的应用

49

4. 求下列曲面所围成的体积:

(1) $x + y + z^2 = 1$, $x = 0$, $y = 0$;
(2) $2z = x^{2} + y^{2}, x^{2} + y^{2} + z^{2} = 3;$
(3) $x^{2} + y^{2} = a^{2}, y^{2} + z^{2} = a^{2}, a > 0;$
(4) $x^{2} + y^{2} + z^{2} + xy + yz + zx = a^{2}, a > 0.$

5. 求下列旋转体的体积:

(1)  $x = a(t - \sin t)$ ,  $y = a(1 - \cos t)$ ,  $t \in [0, 2\pi]$  绕 x 轴旋转所围成的旋转体;
(2) $(x-a)^{2}+y^{2}=b^{2}\quad(a>b>0)$ 的内部绕y轴旋转所围成的旋转体;
(3)  $y^{2}=2ax\ (a>0)$  绕  $x=b\ (b>0)$  旋转所围成的旋转体;
(4)  $y = \sin x, \quad x \in [0, \pi]$  绕 x 轴旋转所围成的旋转体.

6. 将质量为 m 的物体从地球表面提升到高度为 h 的位置, 需要做多少功?

7. 求下列曲线的质量 (设线密度为 1) 与质心坐标:

(1)  $y = 1 - x^{2}, \quad x \in [-1, 1];$
(2) $x = a(t - \sin t)$, $y = a(1 - \cos t)$, $a > 0$, $t \in [0, 2\pi]$.

8. 求下列平面图形的质心:

(1) $0 \leqslant y \leqslant \sqrt{a^2 - x^2}, a > 0$;
(2) $ax = y^2$, $ay = x^2$ 所围图形, $a > 0$.

9. 利用 Guldin 定理求轮胎面的表面积.

10. 设 $a, b, n$ 为正整数, 记 $f(x) = \frac{1}{n!} x^n (a - bx)^n$.

(1) 当  $0 \leqslant k \leqslant 2n$  时, 验证  $f^{(k)}(x)$  在 x = 0 和  $x = \frac{a}{b}$  处取值均为整数;
(2) 若  $\pi$  可以表示为既约分数  $\frac{a}{b}$ ，利用 (1) 和分部积分证明积分  $\int_{0}^{\pi} f(x) \sin x \, dx$  必为整数；
(3) 由此利用反证法证明  $\pi$  不是有理数.
