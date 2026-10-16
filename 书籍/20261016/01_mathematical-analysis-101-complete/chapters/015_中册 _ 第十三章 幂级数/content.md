# 中册 / 第十三章 幂级数

原始 PDF 第 474–517 页。

## 第十三章

## 幂级数

---

170

第十三章 幂级数

本章讨论一类重要的具有特殊形式 $\sum_{n=0}^{+\infty} a_n (x - x_0)^n$ 的函数项级数——幂级数，其中 $x_0 \in \mathbb{R}$, $\{a_n\}$ 是给定的实数列，当 $x = 0$ 时，$x^0$ 规定为 1. 幂级数看起来是一种形式极为简单的函数项级数，然而无论在理论上还是实际应用中，它都具有极其重要的地位，有着丰富的内容、深刻的理论和广泛的应用。在本章中，我们将系统介绍幂级数的理论，包括幂级数的收敛域问题、和函数的性质、函数的幂级数展开问题，以及幂级数的应用问题。

## 13.1 幂级数的收敛半径与收敛域

由于 $x_0 \neq 0$ 的情形可以通过一个简单的平移化为 $x_0 = 0$ 的情形, 因此, 在下面的讨论中, 我们经常默认 $x_0 = 0$.

考虑幂级数

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = a _ {0} + a _ {1} x + a _ {2} x ^ {2} + \dots . \tag {13.1.1}
$$

一个显然的结论是该幂级数在 x = 0 处总是收敛的, 因此幂级数的收敛域总是非空的, 其中幂级数收敛域的定义仍然沿用函数项级数章节中的定义, 即使得幂级数收敛的点的全体.

例 13.1.1 (1) 幂级数  $\sum_{n=0}^{+\infty} n! x^{n}$  的收敛域为  $\{0\}$ . 事实上, 一方面, 当 x=0 时, 幂级数收敛; 另一方面, 当  $x \neq 0$  时,  $\lim_{n \to +\infty} |n! x^{n}| = +\infty$ , 所以该幂级数发散.

(2) 幂级数  $\sum_{n=0}^{+\infty}\frac{x^{n}}{n!}$  的收敛域为 R.

(3) 考虑幂级数 $\sum_{n=1}^{+\infty} \frac{x^n}{n}$ 的收敛域. 容易看出, 当 $|x| < 1$ 时, $\left|\frac{x^n}{n}\right| \leqslant |x^n|$, 故级数收敛; 当 $x = -1$ 时, 级数为一个收敛的交错级数; 而当 $x = 1$ 时, 是发散的调和级数. 当 $|x| > 1$ 时, 级数通项趋于无穷, 故发散. 因此, 级数的收敛域为 $[-1, 1)$.

例13.1.2 试讨论级数 $\sum_{n=0}^{+\infty} a_n x^n$ 的敛散性.

解 记  $L := \varlimsup_{n \to +\infty} \sqrt[n]{|a_n|}$ ,

$$
R := \frac {1}{L} \equiv \left\{ \begin{array}{l l} + \infty , & L = 0, \\ \frac {1}{L}, & L \in (0, + \infty), \\ 0, & L = + \infty . \end{array} \right. \tag {13.1.2}
$$

---

13.1 幂级数的收敛半径与收敛域

171

则由 $\lim_{n\to +\infty}\sqrt[n]{|a_nx^n|} = L|x|$，不难证明下面结论:

(1) 若 R = 0, 级数在 x = 0 处收敛.

(2) 若 R > 0, 则由  $\varlimsup_{n \to +\infty} \sqrt[n]{|a_{n}x^{n}|} = L|x|$  知:

(i) 当 $|x| < R$ 时, 根据 Cauchy 根值判别法知, 级数 $\sum_{n=0}^{+\infty} a_n x^n$ 绝对收敛, 从而收敛.

(ii) 当 $|x| > R$ 时, 数列 $\{a_{n}x^{n}\}$ 不趋于零, 此时级数 $\sum_{n=0}^{+\infty} a_{n}x^{n}$ 发散.

(iii) 当 $|x| = R$ 时, 级数的敛散性要依具体情况讨论. 比如下面三个级数

$$
\sum_ {n = 1} ^ {+ \infty} x ^ {n}, \quad \sum_ {n = 1} ^ {+ \infty} \frac {x ^ {n}}{n}, \quad \sum_ {n = 1} ^ {+ \infty} \frac {x ^ {n}}{n ^ {2}}
$$

对应的 L 均为 1, 所以 R = 1, 但第一个级数当  $|x| = 1$  时发散; 第二个级数当 x = 1 时发散, 当 x = -1 时条件收敛; 第三个级数当  $|x| = 1$  时绝对收敛. □

幂级数的收敛域有以下特点:

定理 13.1.1 (Abel 第一定理) 幂级数 (13.1.1) 的收敛域是一个区间, 即对于 $x_0 \in \mathbb{R}, x_0 \neq 0$,

(1) 若级数在  $x_{0}$  处收敛, 则它一定在  $(-|x_{0}|, |x_{0}|)$  内闭绝对一致收敛.
(2) 若  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  在  $x_{0}\neq0$  发散, 则当  $|x|>|x_{0}|$  时,  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  发散.

证明 (1) 任取闭区间 $[a, b] \in (-|x_0|, |x_0|)$, 则存在 $0 < \delta_0 < 1$, 使得

$$
[ a, b ] \subset [ - \delta_ {0} | x _ {0} |, \delta_ {0} | x _ {0} | ] \subset (- | x _ {0} |, | x _ {0} |).
$$

下面我们证明 $\sum_{n=0}^{+\infty} a_n x^n$ 在 $[- \delta_0 |x_0|$, $\delta_0 |x_0|$ 上绝对一致收敛. 为此, 由 $\sum_{n=0}^{+\infty} a_n x_0^n$ 收敛, 知 $|a_n x_0^n|$ 有界, 即存在 $c > 0$, 使得 $\forall n$, 有 $|a_n x_0^n| \leqslant c$. 从而 $\forall x \in [-\delta_0 |x_0|$, $\delta_0 |x_0|$ 有

$$
| a _ {n} x ^ {n} | = \left| a _ {n} x _ {0} ^ {n} \frac {x ^ {n}}{x _ {0} ^ {n}} \right| \leqslant c \delta_ {0} ^ {n}.
$$

由 $\sum_{n=0}^{+\infty} c\delta_0^n$ 收敛, 可得 $\sum_{n=0}^{+\infty} |a_n x^n|$ 在 $[- \delta_0 |x_0|$, $\delta_0 |x_0|$ 上一致收敛.

结论 (2) 与结论 (1) 本质上是等价的.

注13.1.1 由定理13.1.1知，如果级数 $\sum_{n=0}^{+\infty} a_n x^n$ 在 $x_0 \neq 0$ 处收敛，且在 $x_1$ 处发散，则必有 $x_1 \neq 0$ ，$|x_0| \leqslant |x_1|$，且一定存在一个开区间 $(-R, R)$，$|x_0| \leqslant R \leqslant |x_1|$，使得幂级数在 $(-R, R)$ 内闭绝对一致收敛，而在 $(- \infty, -R) \cup (R, +\infty)$ 发散。

---

172

第十三章 幂级数

级数在区间端点的敛散性需要另行做进一步的分析.

定理 13.1.2 (Cauchy-Hadamard 定理) 考虑幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$ ，记  $\rho = \lim_{n\to+\infty}|a_{n}|^{\frac{1}{n}}$ ,  $R = \frac{1}{\rho}$ ，则

(1) $R = +\infty$ 时, 幂级数在 $(-\infty, +\infty)$ 中绝对收敛.
(2) R = 0 时, 幂级数仅在 x = 0 处收敛.
(3) $0 < R < +\infty$ 时, 幂级数在 $(-R, R)$ 中绝对收敛, 在 $[-R, R]$ 之外发散.

证明 注意到 $\lim_{n\to \infty}|a_nx^n|^{\frac{1}{n}} = \rho |x|$, 由数项级数的根值判别法, 结合定理 13.1.1 的证明过程, 即可得到定理结论的证明. $\square$

定义 13.1.1 定理 13.1.2 中的 R 称为幂级数 (13.1.1) 的收敛半径.

如果幂级数（13.1.1）的收敛半径是 R > 0，则称区间  $(-R, R)$  为幂级数的收敛区间.

需要特别注意的是:幂级数的收敛区间规定为开区间 $(-R, R)$，它并不一定等同于幂级数的收敛域。收敛区间的引入为下面的讨论带来很多表述上的方便。不同的教科书或参考书上可能有不同的称呼。

可以验证, 幂级数的收敛半径 $R$ 的定义等价于下面的定义

$$
R := \sup \left\{| x |   \Bigg |   \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}   \text {收敛} \right\}.
$$

例 13.1.3 容易证明, 级数  $\sum_{n=1}^{+\infty}\frac{x^{n}}{n^{2}},\sum_{n=1}^{+\infty}\frac{x^{n}}{n}$  和  $\sum_{n=1}^{+\infty}nx^{n}$  有相同的收敛半径 R=1, 但在区间端点处有不同的敛散性. 其收敛域分别为  $[-1,1]$ ,  $[-1,1)$  和  $(-1,1)$ .

事实上, 更一般的结论也成立: $\sum_{n=0}^{+\infty} a_n x^n$, $\sum_{n=0}^{+\infty} \frac{a_n}{n+1} x^{n+1}$ 和 $\sum_{n=1}^{+\infty} n a_n x^{n-1}$ 有相同的收敛半径.

可以看出, 幂级数所有可能的收敛域共有如下五种情况 (其中 $R \in (0, +\infty)$):

$$
\{0 \}, \quad (- R, R), \quad [ - R, R), \quad (- R, R ], \quad [ - R, R ], \quad (- \infty , + \infty).
$$

## 习题 13.1

1. 求下列幂级数的收敛半径,并判断它们在收敛区间端点的收敛性:

(1) $\sum_{n=1}^{+\infty} \frac{x^n}{n(n+1)}$;

(2) $\sum_{n=1}^{+\infty}\left(1 + \frac{1}{n}\right)^{2}x^{n}$;

---

13.2 幂级数在收敛域内的性质

173

(3) $\sum_{n=1}^{+\infty} \frac{(n!)^2}{(2n)!} x^n$;
(4) $\sum_{n=1}^{+\infty}\left(1+\frac{1}{2}+\cdots+\frac{1}{n}\right)x^{n};$
(5) $\sum_{n=1}^{+\infty} \frac{x^n}{n^\alpha}, \alpha \in \mathbb{R}$;
(6) $\sum_{n=1}^{+\infty} \frac{(\ln n)^{\alpha}}{n^{2}} x^{n}, \alpha \in \mathbb{R}$.

2. 求幂级数  $\sum_{n=1}^{+\infty}\frac{\sin n\alpha}{n}x^{n}$  的收敛半径, 其中  $\alpha$  为常数.

3. 设  $\sum_{n=0}^{+\infty}a_{n}$  是一个发散的正项级数, 如果  $\lim_{n\to+\infty}\frac{a_{n}}{a_{0}+a_{1}+\cdots+a_{n}}=0$  , 那么级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  的收敛半径 R=1. 试证之.

4. 设

$$
l = \varliminf_ {n \to + \infty} \left| \frac {a _ {n}}{a _ {n + 1}} \right|, \quad L = \varlimsup_ {n \to + \infty} \left| \frac {a _ {n}}{a _ {n + 1}} \right|.
$$

如果幂级数 $\sum_{n=0}^{+\infty} a_n x^n$ 的收敛半径为 $R$，证明:

$$
\frac {1}{L} \leqslant R \leqslant \frac {1}{l}.
$$

进一步问:有没有可能使得上述两个不等式都成立严格不等号？

5. 设幂级数 $\sum_{n=0}^{+\infty} a_n x^n$ 的收敛半径为 1, 且 $\lim_{x \to 1^-} \sum_{n=0}^{+\infty} a_n x^n = A$. 如果 $a_n \geqslant 0$, 证明:

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} = A.
$$

## 13.2 幂级数在收敛域内的性质

如果幂级数 $\sum_{n=0}^{+\infty} a_n x^n$ 的收敛半径 $R > 0$, 则在收敛区间 $(-R, R)$ 内幂级数可以定义出一个和函数 $S(x)$. 作为一类特殊的函数项级数, 我们自然很感兴趣于 $S(x)$ 的几个基本性质, 比如连续性、可微性和可积性. 由于幂级数的通项 $a_n x^n$ 总是连续、可微和可积的, 根据前面章节关于一般形式的函数项级数理论, 我们工作的重点也就自然转向了收敛域内幂级数一致收敛方面的讨论.

---

174

第十三章 幂级数

## 13.2.1 和函数的连续性

关于幂级数和函数的连续性, 有下面的结论:

定理 13.2.1 (Abel 第二定理) 设幂级数  $\sum_{n=0}^{+\infty} a_{n} x^{n}$  的收敛半径为 R (0 < R < +∞). 则

(1) 幂级数在收敛区间  $(-R, R)$  内闭绝对一致收敛.
(2) 若  $\sum_{n=0}^{+\infty}a_{n}R^{n}$  收敛, 则级数在  $(-R,R]$  的任何闭子区间一致收敛, 特别地,

$$
\lim _ {x \to R ^ {-}} \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = \sum_ {n = 0} ^ {+ \infty} a _ {n} R ^ {n}.
$$

(3) 若  $\sum_{n=0}^{+\infty}a_{n}(-R)^{n}$  收敛, 则级数在  $[-R,R)$  的任何闭子区间一致收敛, 特别地,

$$
\lim _ {x \to - R ^ {+}} \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = \sum_ {n = 0} ^ {+ \infty} a _ {n} (- R) ^ {n}.
$$

证明 根据函数项级数内闭一致收敛的定理, 知结论 (1) 显然成立.

现设 $\sum_{n=0}^{+\infty} a_n R^n$ 收敛, 考虑 $\sum_{n=0}^{+\infty} a_n x^n = \sum_{n=0}^{+\infty} a_n R^n \left( \frac{x}{R} \right)^n$. 在 $[0, R]$ 上, $\left| \left( \frac{x}{R} \right)^n \right| \leqslant 1$, 且 $\left( \frac{x}{R} \right)^n$ 关于 $n$ 单调. 由 Abel 判别法可知 $\sum_{n=0}^{+\infty} a_n x^n$ 在 $[0, R]$ 中一致收敛, 其和函数 $S(x)$ 在 $[0, R]$ 中连续, 因此

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} R ^ {n} = S (R) = \lim _ {x \to R ^ {-}} S (x) = \lim _ {x \to R ^ {-}} \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}.
$$

完全类似可以证明情况 (3) 在 $x =  - R$ 收敛时的情况.

注意, 一个幂级数的收敛半径为 $R > 0$, 一般来说我们得不出该级数在收敛区间内的一致收敛性, 比如级数 $\sum_{n=1}^{+\infty} x^n$ 在 $(-1,1)$ 中就不一致收敛. 但是我们能保证在收敛区间内的内闭绝对一致收敛性. 事实上, 如果幂级数在它收敛区间的端点 $x = R$ 处是发散的, 那么级数在区间 $[0,R)$ 是不可能一致收敛的. 这是因为, 如果一致收敛性成立的话, 根据上述定理, 可以对级数逐项取极限 $x \to R^{-}$ 得到一个收敛级数 $\sum_{n=0}^{+\infty} a_n R^n$, 矛盾.

Abel 定理有很重要的应用. 比如, 如果在收敛区间  $(-R, R)$  内

$$
f (x) = \sum_ {n = 1} ^ {+ \infty} a _ {n} x ^ {n} \quad (- R <   x <   R), \tag {13.2.1}
$$

---

13.2 幂级数在收敛域内的性质

175

若又知 $f(x)$ 在区间的某端点，比如 $x = R$ 处连续，且在 $x = R$ 处右端的幂级数也收敛，则此展开式在这端点上也成立.即关系式(13.2.1)可以延拓到 $(-R,R]$.

例13.2.1 在 $-1 < x < 1$ 时成立展开式

$$
\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} - \dots .
$$

由于 x = 1 时右端的幂级数收敛, 左端的函数  $\ln(1 + x)$  在 x = 1 处也连续, 则级数的和为  $\ln 2$ . 即

$$
1 - \frac {1}{2} + \frac {1}{3} - \frac {1}{4} + \dots = \ln 2.
$$

值得指出的是, 如果关系式 (13.2.1) 左端的函数在区间端点不连续, 或者右端的幂级数在端点不收敛, 则一般不可在关系式两端取 $x \to R^{-}$ 或 $x \to -R^{+}$ 的极限. 换句话说, Abel 定理的逆定理不加额外条件的话, 一般来说不成立.

考虑如下经典例子:幂级数

$$
\frac {1}{1 + x} = \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} x ^ {n}
$$

的收敛半径为 $R = 1$ ，在 $x = 1$ 处，左端函数连续，其值为 $\frac{1}{2}$ ，但右端为发散级数$\sum_{n = 0}^{+\infty}(-1)^n.$

研究级数求和方式的推广以及 Abel 定理的逆定理方面的问题, 是一个系统和专门的课题, 这些推广使得在经典定义下发散的级数有可能在新的定义下收敛并可求和. 几种常见的推广有: Cesàro 求和、Abel 求和、Euler 求和、Borel 求和等. 特别地, 在所谓的 Abel 求和意义下, 就可以对 “等式”

$$
1 - 1 + 1 - 1 + \dots = \frac {1}{2}
$$

给出某种“合理”的解释. 感兴趣的读者可以参阅有关级数求和的 Tauber 理论等方面的资料. 我们下面简单介绍一个相关结论.

定理 13.2.2 (Tauber $^{①}$ 定理) 设 $|x|<1$ 时, $f(x)=\sum_{n=0}^{+\infty}a_{n}x^{n}$, 其中 $\lim_{n\to+\infty}na_{n}=$

0. 如果 $\lim_{x\to1^{-}}f(x)=S$, 则 $\sum_{n=0}^{+\infty}a_{n}$ 收敛, 且其和为 S.

证明 考虑

$$
\left| \sum_ {k = 0} ^ {n} a _ {k} - S \right| = \left| \sum_ {k = 0} ^ {n} a _ {k} - \sum_ {k = 0} ^ {+ \infty} a _ {k} x ^ {k} + \sum_ {k = 0} ^ {+ \infty} a _ {k} x ^ {k} - S \right|
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Tauber, Alfred, 1866 年 11 月 5 日 — 1942 年 7 月 26 日, 奥地利数学家.</span></small>

---

176

第十三章 幂级数

$$
\begin{array}{l} \leqslant \left| \sum_ {k = 0} ^ {n} a _ {k} - \sum_ {k = 0} ^ {n} a _ {k} x ^ {k} \right| + \left| \sum_ {k = n + 1} ^ {+ \infty} a _ {k} x ^ {k} \right| + \left| \sum_ {k = 0} ^ {+ \infty} a _ {k} x ^ {k} - S \right| \\ = \left| \sum_ {k = 0} ^ {n} a _ {k} (1 - x ^ {k}) \right| + \left| \sum_ {k = n + 1} ^ {+ \infty} a _ {k} x ^ {k} \right| + \left| \sum_ {k = 0} ^ {+ \infty} a _ {k} x ^ {k} - S \right|. \\ \end{array}
$$

我们分别给出右端三项的估计.

首先, 由 $\lim_{n\to +\infty}na_n = 0$ 知, $\forall \varepsilon > 0, \exists N_1$, 使得 $\forall n > N_1$ 成立 $|na_n| < \frac{\varepsilon}{3}$. 又由于

$$
\lim _ {n \to + \infty} \frac {1}{n} \sum_ {k = 0} ^ {n} k | a _ {k} | = \lim _ {n \to + \infty} n | a _ {n} | = 0,
$$

从而有 $\frac{1}{n}\sum_{k = 0}^{n}k|a_k| <   \frac{\varepsilon}{3}.$

其次, 由于 $\lim_{x\to 1^{-}}f(x) = S$, 故 $\exists N_2$, 使得 $\forall n > N_2$,

$$
\left| f \Big (1 - \frac {1}{n} \Big) - S \right| <   \frac {\varepsilon}{3}.
$$

取 $x = 1 - \frac{1}{n}, N = N_{1} + N_{2}$, 当 $n > N$ 时, 有

$$
\left| \sum_ {k = 0} ^ {n} a _ {k} (1 - x ^ {k}) \right| \leqslant \sum_ {k = 0} ^ {n} k | a _ {k} | (1 - x) = \frac {1}{n} \sum_ {k = 0} ^ {n} k | a _ {k} | <   \frac {\varepsilon}{3}.
$$

$$
\left| \sum_ {k = n + 1} ^ {+ \infty} a _ {k} x ^ {k} \right| \leqslant \frac {1}{n} \sum_ {k = n + 1} ^ {+ \infty} k | a _ {k} | \cdot | x | ^ {k} \leqslant \frac {\varepsilon}{3} \cdot \frac {1}{n} \sum_ {k = n + 1} ^ {+ \infty} | x | ^ {k} \leqslant \frac {\varepsilon}{3 n} \cdot \frac {1}{1 - | x |} = \frac {\varepsilon}{3}.
$$

最后, 注意到  $\left|\sum_{k=0}^{+\infty}a_{k}x^{k}-S\right|=\left|f\left(1-\frac{1}{n}\right)-S\right|<\frac{\varepsilon}{3}$ . 这样我们就得到了

$$
\left| \sum_ {k = 0} ^ {n} a _ {k} - S \right| <   \varepsilon .
$$

因此 $\sum_{n=0}^{+\infty} a_n$ 收敛, 且 $\sum_{n=0}^{+\infty} a_n = S$.

## 13.2.2 和函数的可微性

给定级数 $\sum_{n=0}^{+\infty} a_n x^n$, 我们称 $\sum_{n=1}^{+\infty} n a_n x^{n-1}$ 和 $\sum_{n=0}^{+\infty} \frac{a_n}{n+1} x^{n+1}$ 分别为其逐项求导后的幂级数与逐项积分后的幂级数. 显然, 三个级数 $\sum_{n=0}^{+\infty} a_n x^n, \sum_{n=0}^{+\infty} \frac{a_n}{n+1} x^{n+1}$ 和 $\sum_{n=1}^{+\infty} n a_n x^{n-1}$

---

13.2 幂级数在收敛域内的性质

177

具有完全相同的收敛半径. 事实上, 成立

$$
\varlimsup_ {n \to + \infty} \sqrt [ n ]{\left| \frac {a _ {n - 1}}{n} \right|} = \varliminf_ {n \to + \infty} \sqrt [ n ]{| (n + 1) a _ {n + 1} |} = \varliminf_ {n \to + \infty} \sqrt [ n ]{| a _ {n} |}. \tag {13.2.2}
$$

关于幂级数的逐项求导, 下面的定理成立:

定理 13.2.3 设幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  的收敛半径为 R，则  $S(x)=\sum_{n=0}^{+\infty}a_{n}x^{n}$  在  $(-R, R)$  中任意次可导，且

$$
S ^ {(k)} (x) = \sum_ {n = k} ^ {+ \infty} n (n - 1) \dots (n - k + 1) a _ {n} x ^ {n - k}.
$$

证明 考虑 $k = 1$ 的情况:首先，幂级数 $\sum_{n=0}^{+\infty}(a_n x^n)' = \sum_{n=1}^{+\infty} na_n x^{n-1}$ 的收敛半径仍为 $R$, 故对闭区间 $I \subset (-R, R)$, 级数在 $I$ 上一致收敛. 所以, $\sum_{n=0}^{+\infty} a_n x^n$ 在 $I$ 中可导, 且

$$
S ^ {\prime} (x) = \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) ^ {\prime} = \sum_ {n = 0} ^ {+ \infty} (a _ {n} x ^ {n}) ^ {\prime} = \sum_ {n = 1} ^ {+ \infty} n a _ {n} x ^ {n - 1}.
$$

对一般的 $k > 1$ ，可以完全类似证明 $S(x)$ 的 $k$ 阶可导性.由于 $S^{(n)}(0) = n!a_n$ ，这说明函数 $S(x)$ 在 $x = 0$ 处的Taylor展开就是该幂级数本身. □

例13.2.2 幂级数

$$
\sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n - 1}}{(2 n - 1) !} x ^ {2 n - 1}
$$

的收敛半径 $R = +\infty$ ，即幂级数在 $\mathbb{R}$ 上收敛，记其和函数为 $S(x)$ .则该幂级数可以逐项求导，从而得到幂级数

$$
\sum_ {n = 0} ^ {+ \infty} \frac {(- 1) ^ {n}}{(2 n) !} x ^ {2 n}, \quad x \in \mathbb {R},
$$

而且, 如果记其和函数为  $C(x)$  的话, 有

$$
S ^ {\prime} (x) = C (x).
$$

不难看出, $C(x)$ 对应的幂级数仍然可以继续求导, 且成立

$$
C ^ {\prime} (x) = - S (x).
$$

---

178

第十三章 幂级数

## 13.2.3 和函数的可积性

关于幂级数的逐项积分, 下面的定理成立:

定理 13.2.4 设幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  的收敛半径为 R>0，则当  $x\in(-R,R)$  时，有

$$
\int_ {0} ^ {x} \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} t ^ {n}\right) \mathrm{d} t = \sum_ {n = 0} ^ {+ \infty} \int_ {0} ^ {x} a _ {n} t ^ {n} \mathrm{d} t = \sum_ {n = 0} ^ {+ \infty} \frac {a _ {n}}{n + 1} x ^ {n + 1}, \quad \forall x \in (- R, R).
$$

证明 不妨设 $x > 0$, 根据前面的讨论, 级数 $\sum_{n=0}^{+\infty} a_n t^n$ 在 $[0, x]$ 中一致收敛, 因此可以逐项积分. $\square$

![](../../raw/pages_0481-0496/images/page_482_image_7.jpg)

注13.2.1 如果 $\sum_{n=0}^{+\infty} a_n R^n$ 收敛, 则上面的等式对 $x = R$ 也成立. 对 $-R$ 有类似结果.

例13.2.3 幂级数

$$
\sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} x ^ {2 n} = 1 - x ^ {2} + x ^ {4} - \dots
$$

的收敛半径为 R=1 。在  $(-1,1)$  内幂级数有和函数  $\frac{1}{1+x^{2}}$  。因此，对于任意的  $|x|<1$  ，成立

$$
\arctan x = \int_ {0} ^ {x} \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} t ^ {2 n} \mathrm{d} t = x - \frac {x ^ {3}}{3} + \frac {x ^ {5}}{5} - \dots .
$$

注意到上式左端的函数在 $x = 1$ 处连续, 右端的级数收敛, 因此根据Abel第二定理知上式对 $-1 < x \leqslant 1$ 均成立, 特别地, 有

$$
1 - \frac {1}{3} + \frac {1}{5} - \dots = \arctan 1 = \frac {\pi}{4}.
$$

且上式对  $-1 \leqslant x \leqslant 1$  均成立, 在 x = -1 处也连续, 右端的级数也收敛.

上述讨论表明, 逐项积分和逐项求导后的幂级数, 其收敛半径保持不变, 但对收敛域可能产生细微的影响: 逐项积分后的幂级数收敛域不会减小, 逐项求导后的幂级数收敛域不会增大. 区别只可能表现在收敛区间的端点处.

比如, 考虑级数 $\sum_{n=1}^{+\infty} \frac{x^n}{n}$ 以及 $\sum_{n=1}^{+\infty} \frac{x^{n+1}}{n(n+1)}$ 在 $x = 1$ 处的敛散性, 第一个级数在收敛域的边界点 $x = 1$ 处发散, 但它逐项积分后得到的第二个级数在该点收敛. 等价地, 第二个级数在收敛域的边界点 $x = 1$ 处收敛, 而它逐项求导后得到的第一个级数在该点发散.

关于幂级数的上述性质, 在论证一些等式或讨论幂级数展开时非常有用.

---

13.2 幂级数在收敛域内的性质

179

例 13.2.4 对于显然的等式

$$
\frac {1}{1 + x} = \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} x ^ {n}, \quad | x | <   1,
$$

当  $x \in (-1,1)$  时, 逐项积分可得  $\ln(1+x)$  的表达式:

$$
\ln (1 + x) = \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} \frac {x ^ {n + 1}}{n + 1} = \sum_ {n = 1} ^ {+ \infty} (- 1) ^ {n - 1} \frac {x ^ {n}}{n}, \quad | x | <   1. \tag {13.2.3}
$$

注意到等式两端在 x = 1 处可能的延拓:左端函数有意义，右端级数收敛。因此 (13.2.3) 式可以延拓到  $-1 < x \leqslant 1$ 。

类似地可得

$$
\sum_ {n = 0} ^ {+ \infty} (n + 1) x ^ {n} = \frac {1}{(1 - x) ^ {2}}, \quad | x | <   1. \tag {13.2.4}
$$

$$
\sum_ {n = 0} ^ {+ \infty} \frac {(n + 1) (n + 2)}{2} x ^ {n} = \frac {1}{(1 - x) ^ {3}}, \quad | x | <   1. \tag {13.2.5}
$$

$$
\sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} \frac {x ^ {2 n + 1}}{2 n + 1} = \arctan x, \quad | x | \leqslant 1. \tag {13.2.6}
$$

逐项求导或逐项积分在许多相关学科有广泛的应用, 比如读者可以直接验证下面的结论:

例 13.2.5 证明:Bessel 函数

$$
B (x) = \sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n}}{(n !) ^ {2}} \left(\frac {x}{2}\right) ^ {2 n}
$$

满足二阶常微分方程

$$
x B (x) ^ {\prime \prime} + B ^ {\prime} (x) + x B (x) = 0, \quad x \in \mathbb {R}.
$$

## 习题 13.2

1. 证明函数

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \mathrm{e} ^ {- n} \cos^ {2} x
$$

是  $C^{\infty}$  的, 试求其 Maclaurin 级数以及它的收敛半径.

---

180

第十三章 幂级数

2. 证明:函数

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \mathrm{e} ^ {- n} \cos n ^ {2} x
$$

是无穷次可微的, 其 Maclaurin 级数只有偶数次幂, 并且 $2k$ 次幂项的绝对值为

$$
\sum_ {n = 0} ^ {+ \infty} \frac {x ^ {2 k} \mathrm{e} ^ {- n} n ^ {4 k}}{(2 k) !} > \left(\frac {n ^ {2} x}{2 k}\right) ^ {2 k} \mathrm{e} ^ {- n}.
$$

进一步证明, 此幂级数仅在 $x = 0$ 处收敛.

3. 设 $S(x) = \sum_{n=0}^{+\infty} a_n x^n$ 的收敛半径为 $R > 0$, 证明:

(1) 当  $\sum_{n=0}^{+\infty}\frac{a_{n}}{n+1}R^{n+1}$  收敛时, 有  $\int_{0}^{R}S(x)\mathrm{d}x=\sum_{n=0}^{+\infty}\frac{a_{n}}{n+1}R^{n+1}.$
(2) 当  $\sum_{n=1}^{+\infty} na_{n} R^{n-1}$  收敛时, 有  $S'(R) = \sum_{n=1}^{+\infty} na_{n} R^{n-1}$ .

4. 设幂级数 $\sum_{n=0}^{+\infty} a_n x^n$ 在开区间 $(-R, R)$ 中一致收敛, 证明: 它在闭区间 $[-R, R]$ 中也是一致收敛的.

5. 设 $f(x)$ 是 $[0,1]$ 上的连续函数, 满足

$$
\int_ {0} ^ {1} f (x) x ^ {n} \mathrm{d} x = 0, \quad \forall n = 0, 1, 2, \dots .
$$

证明: 在  $[0,1]$  上  $f(x) \equiv 0$ .

6. 设非常数函数 $f(x)$ 在 $(a, b)$ 内每一点都可以展开成幂级数. 试证明 $f(x)$ 的零点集在 $(a, b)$ 内没有聚点.
7. 设函数 $f(x)$ 在 $x = 0$ 的某个邻域内可以展开成幂级数, 并且序列 $\left\{f^{(n)}(0)\right\}$ 是有界的. 证明: $f(x)$ 必是 $(-\infty, +\infty)$ 内的一个 $C^\infty$ 函数的限制.
8. 设 $f(x)$ 在 $[0,1]$ 连续. 对每个正整数 $n$, 定义

$$
B _ {n} (f, x) = \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} f \left(\frac {k}{n}\right) x ^ {k} (1 - x) ^ {n - k}, \tag {13.2.7}
$$

$B_{n}(f,x)$ 称为函数 $f$ 的 Bernstein 多项式. 证明: $B_{n}(f,x) \Rightarrow f(x), x \in [0,1]$. 进一步对比讨论 $f(x)$ 不连续 (比如取 $f(x)$ 为 Dirichlet 函数) 的情况以及 $f(x)$ 的光滑性更好时的收敛情况.

---

13.3 Taylor 展开式

181

## 13.3 Taylor 展开式

我们先给出函数的幂级数展开的定义:

定义13.3.1 如果存在 $\delta > 0$，使得在 $(x_0 - \delta, x_0 + \delta)$ 内下式成立:

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} a _ {n} (x - x _ {0}) ^ {n}, \quad \forall x \in (x _ {0} - \delta , x _ {0} + \delta), \tag {13.3.1}
$$

则称函数 $f(x)$ 在 $x_0$ 点附近可以展开成幂级数. 如果函数 $f(x)$ 在区间 $I$ 上每点附近都能展开成幂级数, 则称 $f(x)$ 是 $I$ 上的实解析函数, 集合 $I$ 上实解析函数的全体通常记为 $C^{\omega}(I)$.

![](../../raw/pages_0481-0496/images/page_485_image_7.jpg)

注13.3.1 显然 $C^\omega (I)\subseteq C^\infty (I)$ ，后面的例13.3.2进一步表明 $C^\omega (I)\subsetneqq$ $C^\infty (I)$

![](../../raw/pages_0481-0496/images/page_485_image_9.jpg)

注 13.3.2 很容易被忽略的一点是, $f(x)$ 在 $x_0$ 点附近可以展开成幂级数是指等式 (13.3.1) 不但在 $x_0$ 点成立, 而且要存在 $x_0$ 的一个邻域, 使得在整个邻域内等式都成立.

由幂级数在收敛区间 $(x_0 - R, x_0 + R)$ 内的性质立即可得, 若 $f(x)$ 在 $x_0$ 点附近可以展开成幂级数, 则 $f(x)$ 在收敛区间内必须无限次可导, 而且有

$$
f ^ {(n)} (x _ {0}) = n! a _ {n}, \quad n \geqslant 0,
$$

即, $a_{n} = \frac{f^{(n)}(x_0)}{n!}$. 从而 $f(x)$ 又可以表示成

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n}, \quad | x - x _ {0} | <   R. \tag {13.3.2}
$$

上述讨论告诉我们, 如果 $f(x)$ 在 $(x_0 - R, x_0 + R)$ 内满足 (13.3.1) 式, 则必然满足 (13.3.2) 式. 下面我们讨论反过来的问题: 给定一个无穷次可导的光滑函数, 我们来构造它的形式幂级数.

定义 13.3.2 (Taylor 级数) 设  $f(x)$  在  $x_{0}$  处具有任意阶导数, 则称幂级数

$$
\sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n}
$$

为 $f(x)$ 在 $x_0$ 处的Taylor级数，记为

$$
f (x) \sim \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n}. \tag {13.3.3}
$$

---

182

第十三章 幂级数

特别地，当 $x_0 = 0$ 时，级数

$$
f (x) \sim \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (0)}{n !} x ^ {n}
$$

称为  $f(x)$  的 Maclaurin 级数.

定义 13.3.3 (Taylor 展开式) 设 $f(x)$ 在 $x_0$ 处具有任意阶导数, 如果存在 $x_0$ 的某个邻域 $(x_0 - \delta, x_0 + \delta) (\delta > 0)$, 使得 $f(x)$ 在 $x_0$ 处的 Taylor 级数不但在该邻域内收敛而且收敛于 $f(x)$, 则称 $f(x)$ 在 $x_0$ 附近可 Taylor 展开, 而此时级数 $\sum_{n=0}^{+\infty} \frac{f^{(n)}(x_0)}{n!} (x - x_0)^n$ 称为 $f(x)$ 在该邻域内的 Taylor 展开式, 简称展式.

特别地, 当 $x_0 = 0$ 时, Taylor 展式也称为 Maclaurin 展式.

注13.3.3 值得提醒的是, 任给一个在 $x_0$ 处无穷次可导的函数 $f(x)$, 总可以“诱导”出一个形式幂级数 (13.3.3). 这个“诱导”关系通过 (13.3.3) 式中的 “$\sim$” 而非 “=” 表现得淋漓尽致: 右端的幂级数系数来自 $f(x)$, 但这个幂级数是否仅在一点 $x_0$ 处收敛还是在某个区间内收敛, 收敛时是否收敛于 $f(x)$ 等, 都是两码事. 即, (13.3.3) 式右端的幂级数统称为 $f(x)$ 的 Taylor 级数.

换句话说, 当我们谈论函数  $f(x)$  和它在  $x_{0}$  处的 Taylor 级数 (13.3.3) 时, 我们面对四个不同层次:

(1) $f(x)$ 在 $x_0$ 处的光滑度不够 (不是无穷次可导), 此时谈不上 $f(x)$ 的 Taylor 级数 (对比第一册微分中值定理章节中 $f(x)$ 有限阶光滑时的 Taylor 公式).
(2) 收敛半径为零, 即幂级数除 $x_0$ 外都发散.
(3) 收敛半径大于零但和函数并不等于  $f(x)$ .
(4) 收敛半径大于零且和函数等于  $f(x)$ .

只有情况 (4), 我们才称 $f(x)$ 可Taylor展开. 因此, 函数的Taylor级数与函数的Taylor展式在内涵上有本质的区别.

例 13.3.1 存在无穷光滑函数, 其 Maclaurin 级数的收敛半径为 0. 为此, 考察函数项级数

$$
\sum_ {n = 0} ^ {+ \infty} \frac {\sin (2 ^ {n} x)}{n !}
$$

与幂级数

$$
\sum_ {n = 0} ^ {+ \infty} \left(\frac {1}{n !} \mathrm{e} ^ {2 ^ {n}} \sin \frac {n \pi}{2}\right) x ^ {n}
$$

---

13.3 Taylor 展开式

183

之间的关系.

解 记 $u_{n}(x) = \frac{\sin(2^{n}x)}{n!}$. 则有 $|u_{n}(x)| \leqslant \frac{1}{n!}$, 因此级数 $\sum_{n=0}^{+\infty} u_{n}(x)$ 在 $\mathbb{R}$ 上一致收敛, 故该函数项级数定义了一个连续函数

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {\sin (2 ^ {n} x)}{n !}.
$$

又因为

$$
| u _ {n} ^ {\prime} (x) | = \left| \frac {2 ^ {n} \cos (2 ^ {n} x)}{n !} \right| \leqslant \frac {2 ^ {n}}{n !},
$$

所以函数项级数 $\sum_{n=0}^{+\infty} u_n'(x)$ 在 $\mathbb{R}$ 上也一致收敛, 从而

$$
f ^ {\prime} (x) = \sum_ {n = 0} ^ {+ \infty} u _ {n} ^ {\prime} (x).
$$

同理对于  $k=1,2,\cdots$ ，可得

$$
f ^ {(k)} (x) = \sum_ {n = 0} ^ {+ \infty} u _ {n} ^ {(k)} (x) = \sum_ {n = 0} ^ {+ \infty} \frac {2 ^ {k n} \sin (2 ^ {n} x + k \pi / 2)}{n !}.
$$

因此, $f(x)$ 是一个无穷光滑的函数. 注意到

$$
f ^ {(k)} (0) = \sum_ {n = 0} ^ {+ \infty} \frac {2 ^ {k n} \sin (k \pi / 2)}{n !} = \mathrm{e} ^ {2 ^ {k}} \sin \frac {k \pi}{2},
$$

故根据前面的讨论, $f(x)$ 可以“诱导”出Maclaurin级数, 即 $f(x)$ 的Taylor级数:

$$
f (x) \sim \sum_ {n = 0} ^ {+ \infty} \left(\frac {1}{n !} \mathrm{e} ^ {2 ^ {n}} \sin \frac {n \pi}{2}\right) x ^ {n}.
$$

但是, 不难算出该幂级数的收敛半径为零. 因此这个幂级数仅在 $x = 0$ 处收敛. 换句话说, 由级数 $\sum_{n=0}^{+\infty} u_n(x)$ 给出的无穷光滑函数 $f(x)$ 并不能展开成 Maclaurin 级数.

例 13.3.2(平坦函数的存在性) 一个函数称为在 $x_0$ 点是平坦的, 是指它在包含 $x_0$ 的某邻域内是无穷光滑的, 且在 $x_0$ 点的各阶导数均为零.

我们在第七章例 7.2.10 曾经讨论过的函数在  $x_{0}=0$  处是平坦的.

$$
f (x) = \left\{ \begin{array}{l l} \mathrm{e} ^ {- \frac {1}{x ^ {2}}}, & x \neq 0, \\ 0, & x = 0. \end{array} \right.
$$

---

184

第十三章 幂级数

该函数在 x=0 处具有无穷阶导数，且  $f^{(k)}(0)=0\quad(k=0,1,2,\cdots)$ . 因此， $f(x)$  “诱导”出的 Taylor 级数恒为零，其收敛半径为  $+\infty$ ，由于在任何非零点处  $f(x)\neq0$ ，故  $f(x)$  的 Taylor 级数虽然收敛但并不收敛于  $f(x)(x\neq0)$ . 即， $f(x)$  在  $x_{0}=0$  附近不能展开成幂级数.

由于这类平坦函数的存在性, 可以看到, 任何一个无穷光滑函数 $g(x)$ 都和无穷多个函数 $g(x) + f(x)$ 在 $x_0$ 点 “诱导” 出形式上相同的 Taylor 级数, 其中 $f(x)$ 是任意一个在 $x_0$ 处平坦的函数. 因此, 研究一个函数的 Taylor 级数是否收敛到自身是很有必要的.

下面的定理给出了实解析函数在其收敛区间内的每一点都可展开成幂级数的结论.

定理 13.3.1 设 R > 0,

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n}, \quad \forall | x | <   R, \tag {13.3.4}
$$

则 $\forall x_0, |x_0| < R$，当 $|x - x_0| < R - |x_0|$ 时，总成立

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} b _ {n} (x - x _ {0}) ^ {n}, \tag {13.3.5}
$$

其中

$$
b _ {n} = \sum_ {k = n} ^ {+ \infty} \mathrm{C} _ {k} ^ {n} c _ {k} x _ {0} ^ {k - n}, \quad n \geqslant 0. \tag {13.3.6}
$$

证明 当 $|x - x_0| < R - |x_0|$ 时，

$$
\begin{array}{l} \sum_ {k = 0} ^ {+ \infty} \sum_ {n = 0} ^ {k} \left| \mathrm{C} _ {k} ^ {n} c _ {k} x _ {0} ^ {k - n} (x - x _ {0}) ^ {n} \right| \leqslant \sum_ {k = 0} ^ {+ \infty} \sum_ {n = 0} ^ {k} \mathrm{C} _ {k} ^ {n} | c _ {k} | | x _ {0} | ^ {k - n} | x - x _ {0} | ^ {n} \\ = \sum_ {k = 0} ^ {+ \infty} | c _ {k} | \left(| x _ {0} | + | x - x _ {0} |\right) ^ {k} <   + \infty . \\ \end{array}
$$

即级数 $\sum_{k=0}^{+\infty}\sum_{n=0}^{k}\mathrm{C}_{k}^{n}c_{k}x_{0}^{k-n}(x-x_{0})^{n}$ 绝对收敛，从而

$$
\begin{array}{l} \sum_ {n = 0} ^ {+ \infty} b _ {n} (x - x _ {0}) ^ {n} = \sum_ {n = 0} ^ {+ \infty} \sum_ {k = n} ^ {+ \infty} \mathrm{C} _ {k} ^ {n} c _ {k} x _ {0} ^ {k - n} (x - x _ {0}) ^ {n} \\ = \sum_ {k = 0} ^ {+ \infty} \sum_ {n = 0} ^ {k} C _ {k} ^ {n} c _ {k} x _ {0} ^ {k - n} (x - x _ {0}) ^ {n} \\ = \sum_ {k = 0} ^ {+ \infty} c _ {k} x ^ {k} = f (x). \\ \end{array}
$$

定理得证.

□

---

13.3 Taylor 展开式

185

通过级数的余项来判断一个函数能否展开成 Taylor 级数是一种非常方便和实用的方法. 下面的结论显然:

定理 13.3.2 设区间 I 包含 0 点,  $f(x)$  是定义在 I 上的函数, 在 0 点有任意阶的导数,

$$
r _ {n} (x) := f (x) - \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (0)}{k !} x ^ {k}, \quad \forall x \in I. \tag {13.3.7}
$$

则

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (0)}{n !} x ^ {n}, \quad x \in I \tag {13.3.8}
$$

当且仅当

$$
\lim _ {n \to + \infty} r _ {n} (x) = 0, \quad \forall x \in I. \tag {13.3.9}
$$

我们给出两种特殊情况的幂级数展开. 为此, 我们首先证明一个技术性引理.

引理 13.3.3 设  $a > 0, f \in C^{\infty}[0, a]$ ,  $f^{(n)}(x) \geqslant 0, f^{(n)}(0) = 0 (n \geqslant 0)$ ，则  $f \equiv 0$ .

证明 若结论不真, 不失一般性, 不妨设  $\inf\left\{x>0\mid f(x)>0\right\}=0$ . 任取  $\alpha\in\left(0,\frac{a}{3}\right]$ . 我们有  $\xi_{n}\in(\alpha,a)$  使得

$$
\begin{array}{l} f (a) = \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (\alpha)}{k !} (a - \alpha) ^ {k} + \frac {f ^ {(n + 1)} (\xi_ {n})}{(n + 1) !} (a - \alpha) ^ {n + 1} \\ \geqslant \frac {f ^ {(n + 1)} (\alpha)}{(n + 1) !} (a - \alpha) ^ {n + 1}. \\ \end{array}
$$

即 $f^{(n + 1)}(\alpha)\leqslant \frac{(n + 1)!f(a)}{(a - \alpha)^{n + 1}}.$

另一方面, 有 $\eta_{n} \in (0, \alpha)$ 使得

$$
f (\alpha) = \frac {f ^ {(n + 1)} (\eta_ {n})}{(n + 1) !} \alpha^ {n + 1} \leqslant \frac {f ^ {(n + 1)} (\alpha)}{(n + 1) !} \alpha^ {n + 1} \leqslant f (a) \Big (\frac {\alpha}{a - \alpha} \Big) ^ {n + 1}, \quad \forall n \geqslant 0.
$$

令 $n\to +\infty$ 得到 $f(\alpha) = 0.$ 即 $f|_{[0,\frac{a}{3}]} = 0.$ 矛盾.因此，结论成立

定理 13.3.4 (Bernstein 定理) 设 f 在  $[a, b]$  中无穷次可导，且各阶导数非负， $f^{(n)}(x) \geqslant 0$ . 则对任意的  $x_{0}, x \in [a, b]$ ，只要  $|x - x_{0}| \leqslant b - x_{0}$ ，就有

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n}.
$$

证明 $^{①}$ 显然可以不妨取 $x_{0}=0$ ，此时有 $a\leqslant0<b$ ，而条件 $|x-x_{0}|\leqslant b-x_{0}$ 即为 $|x|\leqslant b$ 。因此，所证结论只需对如下的x成立即可:

(1) 如果  $-a \geqslant b$ ，只需考虑  $x \in [-b, b]$ .
(2) 如果  $-a \leqslant b,$  只需考虑  $x \in [a, b]$ .

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 利用积分余项的证明可参见 R. Redheffer. From center of gravity to Bernstein's theorem. Amer. Math. Monthly, 1983, 90(2): 130-131.</span></small>

---

186

第十三章 幂级数

记  $\alpha=\min\{-a,b\}\geqslant0,$

$$
P _ {n} (x) = \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (0)}{k !} x ^ {k}, \quad x \in [ - \alpha , b ].
$$

首先我们证明定理对于任意的 $x \in [0, b]$ 成立. 为此, 设 $x \in [0, b], n \geqslant 0$, 有 $\xi_n \in (0, x)$ 使得

$$
f (x) = P _ {n} (x) + \frac {f ^ {(n + 1)} (\xi_ {n})}{(n + 1) !} x ^ {n + 1} \geqslant P _ {n} (x).
$$

因此, 正项级数  $\sum_{k=0}^{+\infty}\frac{f^{(k)}(0)}{k!}x^{k}$  在  $[0,b]$  上收敛. 记其和函数为  $S(x)$ . 则

$$
S (x) \leqslant f (x), \quad \forall x \in [ 0, b ].
$$

注意到 $S^{(n)}$ 即为 $f^{(n)}$ 的Maclaurin级数的和函数，同样有

$$
S ^ {(n)} (x) \leqslant f ^ {(n)} (x), \quad \forall x \in [ 0, b ].
$$

令 $F = f - S$. 则 $F \in C^{\infty}[0, b]$, 且 $F$ 的各阶导数在 $[0, b]$ 上非负, 而 $F^{(n)}(0) = 0 (\forall n \geqslant 0)$. 由引理13.3.3, 可得 $F$ 在 $[0, b]$ 上恒为零. 即, 定理对于 $a = 0$ 时成立.

其次我们证明, 若  $\alpha > 0$ , 定理结论在  $[-\alpha, 0]$  上也成立. 为此考虑

$$
g (x) = f (x) + f (- x), \quad x \in [ 0, \alpha ].
$$

由定理条件 $\forall x\in [-\alpha ,\alpha ],f(x)\geqslant 0,$ 故 $\forall x\in [0,\alpha ],g(x)\geqslant 0.$

注意到 $\forall x\in [-\alpha ,\alpha ],g^{\prime}(x) = f^{\prime}(x) - f^{\prime}(-x)$ 以及 $f^{\prime \prime}(x)\geqslant 0$ ，故 $f^{\prime}(x)$ 单调不减，从而 $\forall x\in [0,\alpha ],f'(x)\geqslant f'(-x)$ ，因此 $g^{\prime}(x)\geqslant 0,\forall x\in [0,\alpha ]$ .同理，对任意自然数 $n$ $\forall x\in [0,\alpha ]$ ，成立 $g^{(n)}(x) = f^{(n)}(x) + (-1)^{n}f^{(n)}(-x)\geqslant 0,x\in [0,\alpha ]$ .由前面的结果，可得

$$
g (x) = \sum_ {k = 0} ^ {+ \infty} \frac {g ^ {(n)} (0)}{k !} x ^ {k}, \quad x \in [ 0, \alpha ].
$$

采取完全类似的论证, 考虑函数

$$
h (x) = f (x) - f (- x), \quad x \in [ 0, \alpha ].
$$

可得

$$
h (x) = \sum_ {k = 0} ^ {+ \infty} \frac {h ^ {(n)} (0)}{k !} x ^ {k}, \quad x \in [ 0, \alpha ].
$$

最后, 由 $f = \frac{1}{2} (g + h)$, 可得

$$
f (x) = \sum_ {k = 0} ^ {+ \infty} \frac {f ^ {(n)} (0)}{k !} x ^ {k}, \quad x \in [ - \alpha , 0 ].
$$

定理得证.

□

---

13.3 Taylor 展开式

187

例 13.3.3 指数函数  $f(x)=\mathrm{e}^{x}$  在  $(-∞,+∞)$  中的各阶导数均大于零, 根据 Bernstein 定理, 可知其 Taylor 展开式收敛于自身. 即  $\forall x∈R,$  成立

$$
\mathrm{e} ^ {x} = 1 + x + \frac {x ^ {2}}{2} + \dots = \sum_ {n = 0} ^ {+ \infty} \frac {1}{n !} x ^ {n}.
$$

例 13.3.4 考虑前面章节中的关系式 (12.3.9). 当  $x \in [0, \pi)$  时, 根据逐项求导易见, 函数  $\frac{1}{\sin^{2}x} - \frac{1}{x^{2}}$  的各阶导数非负, 因此有 (注意偶函数的展开不含奇次幂项)

$$
\frac {1}{\sin^ {2} x} - \frac {1}{x ^ {2}} = \sum_ {m = 0} ^ {+ \infty} \frac {a _ {2 m}}{(2 m) !} x ^ {2 m}, \forall x \in [ 0, \pi),
$$

其中

$$
a _ {2 m} = \left(\frac {1}{\sin^ {2} x} - \frac {1}{x ^ {2}}\right) ^ {(2 m)} (0) = 2 \sum_ {n = 1} ^ {+ \infty} \frac {(2 m + 1) !}{(n \pi) ^ {2 m + 2}} = 2 (2 m + 1)! \frac {\zeta (2 m + 2)}{\pi^ {2 m + 2}},
$$

因此有

$$
\frac {1}{\sin^ {2} x} - \frac {1}{x ^ {2}} = \sum_ {m = 0} ^ {+ \infty} \frac {\zeta (2 m + 2)}{\pi^ {2 m + 2}} (4 m + 2) x ^ {2 m}, \forall x \in [ 0, \pi). \tag {13.3.10}
$$

定理 13.3.5 设 R > 0, f 在  $(x_{0} - R, x_{0} + R)$  中无穷次可导. 如果存在 M > 0 使得

$$
| f ^ {(n)} (x) | \leqslant M, \forall x \in (x _ {0} - R, x _ {0} + R), \forall n \geqslant 1.
$$

则

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n}, \forall x \in (x _ {0} - R, x _ {0} + R).
$$

证明 当 $x \in (x_0 - R, x_0 + R)$ 时, 由带 Lagrange 余项的 Taylor 公式, 我们有

$$
\begin{array}{l} \left| f (x) - \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (x _ {0})}{k !} (x - x _ {0}) ^ {k} \right| = \left| \frac {f ^ {(n + 1)} (\xi)}{(n + 1) !} (x - x _ {0}) ^ {n + 1} \right| \\ \leqslant \frac {M R ^ {n + 1}}{(n + 1) !} \rightarrow 0 (n \rightarrow + \infty). \\ \end{array}
$$

这说明 f 在  $x_{0}$  处的 Taylor 展开的确收敛到 f 自身.

例 13.3.5 研究幂级数  $\sum_{n=0}^{+\infty} C_{\alpha}^{n} x^{n}$ ，其中  $\alpha \in R \setminus Z$ ,

$$
a _ {n} = \mathrm{C} _ {\alpha} ^ {n} = \frac {1}{n !} \alpha (\alpha - 1) \dots (\alpha - n + 1) \quad (\text {广义组合数}).
$$

解 注意到

$$
\left| \frac {a _ {n + 1}}{a _ {n}} \right| = \left| \frac {\alpha - n}{n + 1} \right|\rightarrow 1 (n \rightarrow + \infty),
$$

由此可知幂级数的收敛半径为 1. 在 $(-1,1)$ 中记和函数为 $f(x)$, 逐项求导可得

---

188

第十三章 幂级数

$$
\begin{array}{l} (1 + x) f ^ {\prime} (x) = (1 + x) \sum_ {n = 1} ^ {+ \infty} \mathrm{C} _ {\alpha} ^ {n} n x ^ {n - 1} = \sum_ {n = 1} ^ {+ \infty} n \mathrm{C} _ {\alpha} ^ {n} x ^ {n - 1} + \sum_ {n = 1} ^ {+ \infty} n \mathrm{C} _ {\alpha} ^ {n} x ^ {n} \\ = \mathrm{C} _ {\alpha} ^ {1} + \sum_ {n = 1} ^ {+ \infty} \left((n + 1) \mathrm{C} _ {\alpha} ^ {n + 1} + n \mathrm{C} _ {\alpha} ^ {n}\right) x ^ {n} \\ = \alpha + \sum_ {n = 1} ^ {+ \infty} \alpha C _ {\alpha} ^ {n} x ^ {n} = \alpha f (x), \\ \end{array}
$$

这说明

$$
((1 + x) ^ {- \alpha} f (x)) ^ {\prime} = - \alpha (1 + x) ^ {- \alpha - 1} f (x) + (1 + x) ^ {- \alpha} f ^ {\prime} (x) = 0,
$$

从而 $(1 + x)^{-\alpha}f(x)$ 为常数.由 $f(0) = 1$ 可知 $f(x) = (1 + x)^{\alpha}$ .即

$$
(1 + x) ^ {\alpha} = \sum_ {n = 0} ^ {+ \infty} \mathrm{C} _ {\alpha} ^ {n} x ^ {n}, \forall x \in (- 1, 1). \tag {13.3.11}
$$

特别地, 取 $\alpha = -1 / 2$, 并以 $-x^{2}$ 代替 $x$ 得

$$
\frac {1}{\sqrt {1 - x ^ {2}}} = 1 + \sum_ {n = 1} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} x ^ {2 n}, \forall x \in (- 1, 1). \tag {13.3.12}
$$

对此幂级数逐项积分, 得 (约定  $(-1)!! = 1, 0!! = 1$ )

$$
\arcsin x = \sum_ {n = 0} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {x ^ {2 n + 1}}{2 n + 1}, \forall x \in (- 1, 1). \tag {13.3.13}
$$

在 $x = \pm 1$ 处右式的收敛性可以通过Raabe判别法得到, 故上式在 $[-1,1]$ 中均成立, 并且在 $[-1,1]$ 中一致收敛. 代入 $x = \sin t$, 得

$$
t = \sum_ {n = 0} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {\sin^ {2 n + 1} t}{2 n + 1}, \forall t \in [ - \pi / 2, \pi / 2 ],
$$

并且上式是一致收敛的. 再次逐项积分, 得

$$
\begin{array}{l} \frac {\pi^ {2}}{8} = \sum_ {n = 0} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {1}{2 n + 1} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2 n + 1} t \mathrm{d} t \\ = \sum_ {n = 0} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {1}{2 n + 1} \frac {(2 n) ! !}{(2 n + 1) ! !} = \sum_ {n = 0} ^ {+ \infty} \frac {1}{(2 n + 1) ^ {2}}. \\ \end{array}
$$

由此容易得到 $\frac{\pi^2}{6} = \sum_{n=1}^{+\infty} \frac{1}{n^2} = \zeta(2)$.

例 13.3.6 计算积分  $I=\int_{0}^{1}\frac{\ln(1+x)}{x}\mathrm{d}x.$

解 根据 $\ln (1 + x)$ 的Taylor展开可得

$$
\frac {\ln (1 + x)}{x} = \sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n - 1} x ^ {n - 1}}{n}, x \in (- 1, 1 ].
$$

---

13.3 Taylor 展开式

189

上式在  $[0,1]$  中一致收敛, 因此可逐项积分:

$$
I = \sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n - 1}}{n} \int_ {0} ^ {1} x ^ {n - 1}   \mathrm{d} x = \sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n - 1}}{n ^ {2}} = \frac {\pi^ {2}}{1 2}.
$$

我们以总结和对比几个名词结束本节内容.

Taylor 级数: 是指当函数 $f(x)$ 在 $x_0$ 的某邻域内无穷光滑时下面的级数:

$$
f (x) \sim f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(x - x _ {0}\right) + \frac {f ^ {\prime \prime} \left(x _ {0}\right)}{2 !} \left(x - x _ {0}\right) ^ {2} + \dots + \frac {f ^ {(n)} \left(x _ {0}\right)}{n !} \left(x - x _ {0}\right) ^ {n} + \dots . \tag {13.3.14}
$$

Taylor 展开式: 当  $f(x)$  在包含  $x_{0}$  的某邻域内无穷光滑时, 其 Taylor 级数 (13.3.14) 中的右端有大于零的收敛半径, 并且在收敛域 I 内 “～” 成立等号 “=”, 即

$$
f (x) = f (x _ {0}) + f ^ {\prime} (x _ {0}) (x - x _ {0}) + \frac {f ^ {\prime \prime} (x _ {0})}{2 !} (x - x _ {0}) ^ {2} + \dots + \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n} + \dots ,
$$

那么我们就称  $f(x)$  可 Taylor 展开或者称  $f(x)$  在区域 I 上可展成 Taylor 级数. 一个函数可展成 Taylor 级数表明不但它的 Taylor 级数收敛, 而且收敛到它自身.

Taylor 公式: Taylor 公式是第一册讨论函数导数应用时出现的内容: 如果函数 $f(x)$ 在包含 $x_0$ 的某个闭区间 $[a, b]$ 上具有 $n$ 阶导数, 且在开区间 $(a, b)$ 上具有 $n + 1$ 阶导数, 则对闭区间 $[a, b]$ 上任意一点 $x$, 成立下式:

$$
f (x) = f (x _ {0}) + \frac {f ^ {\prime} (x _ {0})}{1 !} (x - x _ {0}) + \dots + \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n} + R _ {n} (x),
$$

其中  $R_{n}(x)$  是 Taylor 公式的余项, 余项具有多种表现形式.

注意, Taylor 公式可以对有限阶光滑函数成立, 而且在其满足定理条件的区域都成立 (对于初等函数, 在其定义域内即可), 而 Taylor 展开则要求函数必须无穷光滑, 而且只能在收敛域内才有意义.

例如, 在  $\ln(1+x)$  的定义域内, 都成立下面的 Taylor 公式:

$$
\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {1}{3} \frac {x ^ {3}}{(1 + \theta x) ^ {3}}, \quad 0 <   \theta <   1,
$$

但  $\ln(1+x)$  的 Taylor 展开式只在  $(-1,1]$  内成立, 即  $\ln(1+x)$  在  $(-1,1]$  内可 Taylor 展开为

$$
\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} + \dots + (- 1) ^ {n - 1} \frac {x ^ {n}}{n} + \dots .
$$

## 习题 13.3

1. 求级数  $\sum_{n=0}^{+\infty}(-1)^{n}\frac{x^{4n+1}}{4n+1}$  的和.

---

190

第十三章 幂级数

2. 求下列级数之和:

$$
\sum_ {n = 1} ^ {+ \infty} \frac {n ^ {2} + 1}{n} x ^ {n}, \quad \sum_ {n = 1} ^ {+ \infty} n ^ {3} x ^ {n}, \quad \sum_ {n = 0} ^ {+ \infty} \frac {1}{3 !} (n + 1) (n + 2) (n + 3) x ^ {n}.
$$

3. 设

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{x} - \frac {1}{\tan x}, & x \in (0, \pi), \quad x \neq \pi / 2, \\ 2 / \pi , & x = \pi / 2. \end{array} \right.
$$

证明: $f(x)$  的 k 阶导数  $(k=0,1,2,\cdots)$  在  $(0,\pi)$  内均恒正，从而在  $(0,\pi)$  的任何内闭区间上满足 Bernstein 定理 13.3.4 的条件.

4. 设 $x \in \left(-\frac{\pi}{2}, 0\right) \cup \left(0, \frac{\pi}{2}\right)$, 推导下列等式:

$$
\begin{array}{l} \frac {1}{x} - \frac {1}{\tan x} = 2 \sum_ {k = 1} ^ {+ \infty} \frac {\zeta (2 k)}{\pi^ {2 k}} x ^ {2 k - 1}, \\ \frac {1}{\sin x} - \frac {1}{x} = 2 \sum_ {k = 1} ^ {+ \infty} \frac {\zeta (2 k)}{\pi^ {2 k}} \left(1 - 2 ^ {1 - 2 k}\right) x ^ {2 k - 1}. \\ \end{array}
$$

5. 证明等式

$$
\ln (x + \sqrt {1 + x ^ {2}}) = \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {x ^ {2 n + 1}}{2 n + 1}, \quad x \in [ - 1, 1 ].
$$

6. 求级数  $\frac{1}{2}-\frac{1}{5}+\frac{1}{8}-\frac{1}{11}+\cdots$  的和.

7. 证明:

$$
1 - \frac {1}{5} + \frac {1}{9} - \frac {1}{1 3} + \dots = \frac {1}{4 \sqrt {2}} \Big (\pi + 2 \ln (\sqrt {2} + 1) \Big).
$$

8. 证明:

$$
1 + \frac {1}{2} - \frac {1}{3} + \frac {1}{4} - \frac {1}{5} + \frac {1}{6} - \frac {1}{7} + \dots = \frac {\pi}{4} + \frac {1}{2} \ln 2.
$$

9. 证明:

$$
1 + \sum_ {n = 1} ^ {+ \infty} \frac {(2 n + 1) ! !}{(2 n) ! !} \frac {1}{(2 n + 1) ^ {2}} = \frac {\pi}{2} \ln 2.
$$

## 13.4 初等函数的幂级数展开

函数的 Taylor 展开在分析学中有极其重要的意义和应用, 上面我们已经给出了一些初等函数的 Taylor 展开, 本节我们再给出几个常见的初等函数的 Taylor (Maclaurin) 展开. 由前面的定理可知, 一个定义在某区间 $I$ 上的无穷光滑函数 $f(x)$ 能否展开成幂

---

13.4 初等函数的幂级数展开

191

级数, 通常的做法是首先写出它的 Taylor 级数或 Maclaurin 级数 (下面我们主要讨论后者), 然后研究该幂级数的收敛半径 $R$. 如果 $R > 0$, 那么我们再进一步验证该幂级数在收敛区间 $(-R, R)$ 内是否收敛到该函数. 而后者又可依据定理 13.3.2 或 Bernstein 定理 13.3.4 等来判别.

我们先回顾一下曾经得到的几个初等函数的 Taylor 展开.

指数函数的幂级数展开:在(5.2.18)式和例13.3.3中,我们均讨论了 $\mathrm{e}^x$ 的Maclaurin级数展式:

$$
\mathrm{e} ^ {x} = \sum_ {n = 0} ^ {+ \infty} \frac {x ^ {n}}{n !}, \quad x \in \mathbb {R}.
$$

幂函数的幂级数展开:然后我们在例13.3.5中得到了 $(1 + x)^{\alpha},\alpha \in \mathbb{R}\backslash \mathbb{Z}$ 的Maclaurin展式(13.3.11):

$$
(1 + x) ^ {\alpha} = \sum_ {n = 0} ^ {+ \infty} C _ {\alpha} ^ {n} x ^ {n}, \quad \forall x \in (- 1, 1),
$$

其中 $a_{n} = \mathrm{C}_{\alpha}^{n} = \frac{1}{n!}\alpha (\alpha -1)\dots (\alpha -n + 1).$

反三角函数的幂级数展开:我们还得到了 $\arcsin x$ 在 $x \in (-1, 1)$ 上的 Maclaurin 展式 (13.3.13):

$$
\arcsin x = \sum_ {n = 0} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {x ^ {2 n + 1}}{2 n + 1}, \quad \forall x \in (- 1, 1).
$$

以及 $\arctan x$ 在 $x\in (-1,1)$ 上的Maclaurin展式(13.2.6):

$$
\arctan x = \sum_ {n = 0} ^ {+ \infty} \frac {(- 1) ^ {n} x ^ {2 n + 1}}{2 n + 1}.
$$

下面我们给出另外几个初等函数的 Maclaurin 展式.

## 三角函数的幂级数展开:

例13.4.1 在第五章讨论三角函数时, 我们通过关系式 (5.5.5) 和 (5.5.6) 引入了正弦函数和余弦函数. 下面我们证明: 对于 $x \in (-\infty, +\infty)$ 成立

$$
\sin x = \sum_ {n = 0} ^ {+ \infty} \frac {(- 1) ^ {n} x ^ {2 n + 1}}{(2 n + 1) !}, \tag {13.4.1}
$$

$$
\cos x = \sum_ {n = 0} ^ {+ \infty} \frac {(- 1) ^ {n} x ^ {2 n}}{(2 n) !}. \tag {13.4.2}
$$

证明 对任意的正整数 $n$, 有 $\sin^{(n)}(0) = \sin \frac{n\pi}{2}$. 对任意的 $x \in \mathbb{R}$, 其 Taylor 公式中的 Lagrange 余项为

$$
\left| \frac {\sin \left(\theta x + (2 n + 1) \frac {\pi}{2}\right)}{(2 n + 1) !} x ^ {2 n + 1} \right| \leqslant \frac {| x | ^ {2 n + 1}}{(2 n + 1) !} \rightarrow 0 \quad (n \rightarrow + \infty),
$$

---

192

第十三章 幂级数

其中 $\theta \in (0,1)$ 因此有(13.4.1)式成立

同理, 由 $\cos^{(n)}(0) = \cos \frac{n\pi}{2}$, 对任意的 $x \in \mathbb{R}$, 其 Taylor 公式中的 Lagrange 余项为

$$
\left| \frac {\cos (\theta x + n \pi)}{(2 n) !} x ^ {2 n} \right| \leqslant \frac {| x | ^ {2 n}}{(2 n) !} \rightarrow 0 \quad (n \rightarrow + \infty),
$$

其中 $\theta \in (0,1)$ 因此有(13.4.2)式成立

对数函数的幂级数展开:用同样的方法，也可以得到前面已经给出的对数函数的Maclaurin展式:

$$
\ln (1 + x) = \sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n + 1}}{n} x ^ {n}, \quad x \in (- 1, 1).
$$

上述函数的 Taylor 展式的收敛域可以通过单独考虑幂级数在收敛区间端点的敛散性得到, 在此不再赘述. 比如可以证明 $\ln (1 + x)$ 的收敛域为 $(-1,1]$, $\arctan x$ 的收敛域为 $[-1,1]$, $\arcsin x$ 的收敛域为 $[-1,1]$.

更一般函数的 Taylor 展式, 可以通过下一节幂级数之间的代数运算、已知幂级数展开的逐项求导或逐项积分, 再结合幂级数的唯一性的灵活运用得到. 前面提到的等式 (13.2.4), (13.2.5), (13.3.10) 和 (13.3.12) 等, 都是这些方法的灵活应用.

## 13.5 幂级数的代数运算

我们简要讨论一下幂级数间的代数运算. 首先, 关于幂级数的加减, 有下面的结论:

定理 13.5.1 如果幂级数  $\sum_{n=1}^{+\infty}a_{n}x^{n}$  和  $\sum_{n=1}^{+\infty}b_{n}x^{n}$  的收敛半径分别为  $R_{1}$  和  $R_{2}$ ，则幂级数  $\sum_{n=1}^{+\infty}(a_{n}\pm b_{n})x^{n}$  的收敛半径 R 为

(1) 若  $R_{1} \neq R_{2}$ ，则  $R = \min\{R_{1}, R_{2}\}$ .
(2) 若  $R_{1}=R_{2}=R_{0}$ ，则  $R\geqslant R_{0}$ .

不难看出, 在情形 (2), 对于任意的 $\lambda > R_0$, 都可以找到这样的幂级数, 使得两幂级数和形成的幂级数收敛半径为 $\lambda$. 事实上, 只要取 $a_n = -b_n + \frac{1}{\lambda^n}$ 即可.

关于两个幂级数的乘积, 首先, 我们知道, 对于两个给定的幂级数 $\sum_{n=0}^{+\infty} a_n x^n$ 和 $\sum_{n=0}^{+\infty} b_n x^n$, 如果它们的收敛半径均为 $R > 0$, 则当 $|x| < R$ 时, 这两个幂级数都绝对收敛, 因此它们

---

13.5 幂级数的代数运算

193

的乘积都等于它们的 Cauchy 乘积, 即

$$
\left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n},
$$

其中  $c_{n}=\sum_{i=0}^{n}a_{i}b_{n-i}\ (n=0,1,2,\cdots)$ . 即有下面的结论:

定理 13.5.2 设幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  和  $\sum_{n=0}^{+\infty}b_{n}x^{n}$  的收敛半径都是 R, 那么当  $x \in (-R, R)$  时, 有

$$
\left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n},
$$

其中  $c_{n}=\sum_{i=0}^{n}a_{i}b_{n-i}\ (n=0,1,2,\cdots)$ .

我们再从幂级数的角度重新考虑一下 Abel 定理 11.4.11.

定理 13.5.3 (Abel 定理) 设  $\sum_{n=0}^{+\infty}a_{n}=A$  和  $\sum_{n=0}^{+\infty}b_{n}=B$  均为收敛级数, 如果它们的 Cauchy 乘积级数  $\sum_{n=0}^{+\infty}c_{n}=C$  也收敛, 其中  $c_{n}=a_{0}b_{n}+a_{1}b_{n-1}+\cdots+a_{n}b_{0}$ , 则成立

$$
C = A B.
$$

证明 根据假设, 级数

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}, \quad \sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}, \quad \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n}
$$

的收敛半径都不小于1, 因此当  $|x| < 1$  时, 成立

$$
\left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n}.
$$

在上式两端取 $x \to 1^{-}$ 的极限, 根据Abel第二定理知定理成立.

例 13.5.1 假设幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  的收敛半径为 1, 考虑它与幂级数  $\sum_{n=0}^{+\infty}x^{n}$  的乘积. 因为两者有相同的收敛半径, 根据上述定理, 有

$$
\left(\sum_ {n = 0} ^ {+ \infty} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} S _ {n} x ^ {n},
$$

---

194

第十三章 幂级数

其中  $S_{n}=a_{0}+a_{1}+\cdots+a_{n}(n=0,1,2,\cdots)$ . 即

$$
\frac {1}{1 - x} \cdot \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} S _ {n} x ^ {n}.
$$

如果再进行一次上式操作过程, 可得

$$
\frac {1}{(1 - x) ^ {2}} \cdot \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} T _ {n} x ^ {n},
$$

其中  $T_{n}=S_{0}+S_{1}+\cdots+S_{n}(n=0,1,2,\cdots)$ .

例 13.5.2 设  $r \in (-1,1)$ ,  $x \in R$ , 求下面级数的和:

$$
1 + \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos n x.
$$

解 我们计算级数的乘积:

$$
\begin{array}{l} \left(1 - 2 r \cos x + r ^ {2}\right) \left(1 + \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos n x\right) \\ = 1 - 2 r \cos x + r ^ {2} + \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos n x - 2 r \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos x \cos n x + \sum_ {n = 1} ^ {+ \infty} r ^ {n + 2} \cos n x \\ = 1 - 2 r \cos x + r ^ {2} + \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos n x - r \sum_ {n = 1} ^ {+ \infty} r ^ {n} (\cos (n - 1) x + \cos (n + 1) x) + \\ \sum_ {n = 1} ^ {+ \infty} r ^ {n + 2} \cos n x \\ = 1 - r \cos x. \\ \end{array}
$$

由此可得等式

$$
\frac {1 - r \cos x}{1 - 2 r \cos x + r ^ {2}} = 1 + \sum_ {n = 1} ^ {+ \infty} r ^ {n} \cos n x, \quad r \in (- 1, 1). \tag {13.5.1}
$$

将上式中右端的 1 移到左端, 两边除以 $r$, 再关于 $r$ 逐项积分, 得

$$
\ln (1 - 2 r \cos x + r ^ {2}) = - 2 \sum_ {n = 1} ^ {+ \infty} \frac {r ^ {n}}{n} \cos n x, r \in (- 1, 1). \tag {13.5.2}
$$

上式两端关于 x 积分, 则得如下 Dini 积分:

$$
\int_ {0} ^ {\pi} \ln (1 - 2 r \cos x + r ^ {2}) \mathrm{d} x = 0, | r | <   1. \tag {13.5.3}
$$

□

下面我们考虑幂级数的除法运算, 它可以看成是乘法运算的逆运算.

---

13.5 幂级数的代数运算

195

定理 13.5.4 设幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  在区间  $(-R,R)$  中收敛,  $a_{0}\neq0$ . 则存在 r>0,
使得幂级数  $\sum_{n=0}^{+\infty}b_{n}x^{n}$  在  $(-r,r)$  中收敛, 且

$$
\left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) \equiv 1, \forall x \in (- r, r).
$$

证明 不妨设  $a_{0}=1$ . 递归定义  $b_{n}$  如下: 令  $b_{0}=1$ ,

$$
b _ {n} = - \sum_ {i = 0} ^ {n - 1} a _ {n - i} b _ {i}, n \geqslant 1.
$$

我们先证明幂级数 $\sum_{n=0}^{+\infty} b_n x^n$ 具有正的收敛半径. 事实上, 因为 $\sum_{n=0}^{+\infty} a_n x^n$ 在 $(-R, R)$ 中收敛, 故存在 $M > 0$, 使得 $\left|a_n \left(\frac{R}{2}\right)^n \right| \leqslant M$. 因此有

$$
\left| b _ {n} \left(\frac {R}{2}\right) ^ {n} \right| \leqslant \sum_ {i = 0} ^ {n - 1} \left| a _ {n - i} \left(\frac {R}{2}\right) ^ {n - i} \right| \left| b _ {i} \left(\frac {R}{2}\right) ^ {i} \right| \leqslant M \sum_ {i = 0} ^ {n - 1} \left| b _ {i} \left(\frac {R}{2}\right) ^ {i} \right|.
$$

由数学归纳法不难得到

$$
\left| b _ {n} \left(\frac {R}{2}\right) ^ {n} \right| \leqslant (1 + M) ^ {n}, \forall n \geqslant 0.
$$

故幂级数 $\sum_{n=0}^{+\infty} b_n x^n$ 的收敛半径至少为 $r = \frac{R}{2(1 + M)}$. 根据 $\{b_n\}$ 的构造, 显然有

$$
\left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) = \sum_ {n = 0} ^ {+ \infty} \left(\sum_ {i + j = n} a _ {i} b _ {j}\right) x ^ {n} = 1.
$$

例 13.5.3 试研究函数  $\frac{1}{1+x+x^{2}+\cdots+x^{m-1}}\quad(m>1)$  的 Maclaurin 级数展开.
解 直接计算可得

$$
\frac {1}{1 + x + x ^ {2} + \cdots + x ^ {m - 1}} = (1 - x) \sum_ {n = 0} ^ {+ \infty} x ^ {m n} = \sum_ {n = 0} ^ {+ \infty} x ^ {m n} - \sum_ {n = 0} ^ {+ \infty} x ^ {m n + 1}, \quad x \in (- 1, 1).
$$

例 13.5.4 试研究函数  $\frac{x}{e^{x}-1}$  在 x=0 处的幂级数展开.

解记

$$
\frac {x}{\mathrm{e} ^ {x} - 1} = \sum_ {n = 0} ^ {+ \infty} \frac {B _ {n}}{n !} x ^ {n}, \tag {13.5.4}
$$

---

196

第十三章 幂级数

其系数 $B_{n}$ 称为第 $n$ 个Bernoulli数. 我们有

$$
\begin{array}{l} \frac {x}{\mathrm{e} ^ {x} - 1} = \left(\frac {\mathrm{e} ^ {x} - 1}{x}\right) ^ {- 1} = \left(\sum_ {n = 0} ^ {+ \infty} \frac {x ^ {n}}{(n + 1) !}\right) ^ {- 1} \\ = 1 - \frac {x}{2} + \frac {x ^ {2}}{1 2} - \frac {x ^ {4}}{7 2 0} + \frac {x ^ {6}}{3 0 2 4 0} - \frac {x ^ {8}}{1 2 0 9 6 0 0} + \dots . \\ \end{array}
$$

注意到上式中 $B_{1} = -\frac{1}{2}$, 当 $n \geqslant 1$ 时 $B_{2n+1} = 0$, 这是因为

$$
\frac {x}{\mathrm{e} ^ {x} - 1} + \frac {x}{2} = \frac {x}{2} \frac {\mathrm{e} ^ {x} + 1}{\mathrm{e} ^ {x} - 1} = \frac {x}{2} \coth \frac {x}{2}, \tag {13.5.5}
$$

即  $\frac{x}{\mathrm{e}^{x}-1}+\frac{x}{2}$  为偶函数的缘故.

根据幂级数的除法公式, 我们容易得到  $B_{n}$  的如下递推公式:

$$
B _ {0} = 1, B _ {n} = - \frac {1}{n + 1} \sum_ {k = 0} ^ {n - 1} \mathrm{C} _ {n + 1} ^ {k} B _ {k}.
$$

例如, 开头的几个 Bernoulli 数 $^{①}$ 为

$$
B _ {0} = 1, \quad B _ {1} = - \frac {1}{2}, \quad B _ {2} = \frac {1}{6}, \quad B _ {3, 5, 7} = 0, \quad B _ {4} = - \frac {1}{3 0}, \quad B _ {6} = \frac {1}{4 2}, \quad B _ {8} = - \frac {1}{3 0}. \quad \square
$$

例13.5.5 设

$$
f (x) = \frac {x}{1} + \frac {x ^ {3}}{1 \times 3} + \frac {x ^ {5}}{1 \times 3 \times 5} + \dots + \frac {x ^ {2 n + 1}}{(2 n + 1) ! !} + \dots , \tag {13.5.6}
$$

以及

$$
g (x) = 1 + \frac {x ^ {2}}{2} + \frac {x ^ {4}}{2 \times 4} + \dots + \frac {x ^ {2 n}}{(2 n) ! !} + \dots . \tag {13.5.7}
$$

证明: 上述两个幂级数的比值满足

$$
\frac {f (x)}{g (x)} = \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} \frac {x ^ {2 n + 1}}{(2 n) ! ! (2 n + 1)}. \tag {13.5.8}
$$

证明 容易看出, $g(x) = \mathrm{e}^{x^2 / 2}$, 同时还有 (13.5.8) 式右边的级数

$$
\sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} \frac {x ^ {2 n + 1}}{(2 n) ! ! (2 n + 1)} = \sum_ {n = 0} ^ {+ \infty} \int_ {0} ^ {x} \frac {1}{n !} \left(\frac {- t ^ {2}}{2}\right) ^ {n} \mathrm{d} t = \int_ {0} ^ {x} \mathrm{e} ^ {- t ^ {2} / 2} \mathrm{d} t.
$$

因此，只需证明

$$
f (x) = g (x) \int_ {0} ^ {x} \mathrm{e} ^ {- t ^ {2} / 2} \mathrm{d} t = \mathrm{e} ^ {x ^ {2} / 2} \int_ {0} ^ {x} \mathrm{e} ^ {- t ^ {2} / 2} \mathrm{d} t
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 这样定义的 Bernoulli 数称为第一 Bernoulli 数, 此时  $B_{1} = -\frac{1}{2}$ . 当定义  $B_{1} = \frac{1}{2}$ , 其他  $B_{k}$  不变时, 称为第二 Bernoulli 数, 第二 Bernoulli 数可通过考虑函数  $\frac{x e^{x}}{e^{x} - 1}$  的幂级数展开得到.</span></small>

---

13.5 幂级数的代数运算

197

即可. 记 $h(x) = \mathrm{e}^{x^2 / 2}\int_0^x\mathrm{e}^{-t^2 / 2}\mathrm{d}t.$ 事实上，一方面由(13.5.6)式逐项求导，容易看出

$$
f ^ {\prime} (x) = 1 + x f (x).
$$

另一方面，

$$
h ^ {\prime} (x) = \frac {\mathrm{d}}{\mathrm{d} x} \Big (\mathrm{e} ^ {x ^ {2} / 2} \int_ {0} ^ {x} \mathrm{e} ^ {- t ^ {2} / 2} \mathrm{d} t \Big) = 1 + x \mathrm{e} ^ {x ^ {2} / 2} \int_ {0} ^ {x} \mathrm{e} ^ {- t ^ {2} / 2} \mathrm{d} t = 1 + x h (x).
$$

所以，我们看到 $f(x)$ 和 $h(x)$ 满足相同的微分方程关系式 $y' = 1 + xy$ ，并且两者还都满足 $f(0) = 0$ 和 $h(0) = 0$ 因此 $f(x) \equiv h(x)^{\text{①}}$ □

幂级数之间还可以做代入运算, 或者称之为幂级数的复合运算, 即把一个幂级数代入到另一个幂级数. 限于篇幅, 我们在此不再铺开讨论.

下面的例子说明: 光滑函数的 Taylor 展开的系数可以为任意实数列.

例 13.5.6 对于任意给定的数列  $\{a_{n}\}$ ，都可以构造一个光滑函数  $f(x)$ ，使得该函数在 x=0 处的 Maclaurin 级数的系数恰好满足  $f^{(n)}(0)=a_{n}, n=0,1,2,\cdots$ .

解 设 $\varphi \in C^{\infty}(\mathbb{R})$ 满足

$$
\varphi (x) = \left\{ \begin{array}{l l} 1, & | x | \leqslant \frac {1}{4}, \\ 0, & | x | \geqslant \frac {1}{2}. \end{array} \right.
$$

对于实数列  $a_{0}, a_{1}, a_{2}, \cdots$ ，定义

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {a _ {n}}{n !} \varphi (a _ {n} x) x ^ {n}, \quad \forall   x \in \mathbb {R}.
$$

可以证明 $f \in C^{\infty}(\mathbb{R})$，且 $f^{(n)}(0) = a_n, \forall n \geqslant 0$.

事实上, 因为 $x^{k+1}\varphi^{(k)}(x) \in C^{\infty}(\mathbb{R})$ 且仅在有界集上非零. 因此, 它们在 $\mathbb{R}$ 上都是有界的. 设

$$
\sup _ {x \in \mathbb {R}} | x ^ {k + 1} \varphi^ {(k)} (x) | \leqslant M _ {k}, \quad k = 0, 1, 2, \dots .
$$

则

$$
\left| \frac {a _ {n}}{n !} \varphi (a _ {n} x) x ^ {n} \right| \leqslant \frac {M _ {0} | x | ^ {n - 1}}{n !}, \quad \forall n \geqslant 1, x \in \mathbb {R}.
$$

因此, 级数 $\sum_{n=0}^{+\infty} \frac{a_n}{n!} \varphi(a_n x) x^n$ 在 $\mathbb{R}$ 上内闭一致收敛. 进而可得 $f(x)$ 连续. 从而

$$
f (0) = \sum_ {n = 0} ^ {+ \infty} \frac {a _ {n}}{n !} \varphi (a _ {n} x) x ^ {n} \Big | _ {x = 0} = a _ {0}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 这里我们利用了常微分方程的一个基本结论:一阶线性微分方程初值问题的解是存在唯一的。读者也可以直接证明两者相等。</span></small>

---

198

第十三章 幂级数

现考虑级数 $\sum_{n=0}^{+\infty} \frac{a_n}{n!} \varphi(a_n x) x^n$ 形式求导后的级数

$$
a _ {0} ^ {2} \varphi^ {\prime} (a _ {0} x) + \sum_ {n = 1} ^ {+ \infty} \frac {1}{n !} \Big (a _ {n} ^ {2} \varphi^ {\prime} (a _ {n} x) x ^ {n} + n a _ {n} \varphi (a _ {n} x) x ^ {n - 1} \Big).
$$

由于

$$
\left| \frac {1}{n !} \Big (a _ {n} ^ {2} \varphi^ {\prime} (a _ {n} x) x ^ {n} + n a _ {n} \varphi (a _ {n} x) x ^ {n - 1} \Big) \right| \leqslant \frac {1}{n !} \big (M _ {1} + n M _ {0} \big) | x | ^ {n - 2}, \quad \forall   n \geqslant 2,
$$

可知

$$
a _ {0} ^ {2} \varphi^ {\prime} (a _ {0} x) + \sum_ {n = 1} ^ {+ \infty} \frac {1}{n !} \Big (a _ {n} ^ {2} \varphi^ {\prime} (a _ {n} x) x ^ {n} + n a _ {n} \varphi (a _ {n} x) x ^ {n - 1} \Big)
$$

在 $\mathbb{R}$ 上内闭一致收敛. 从而 $f(x)$ 连续可导且导数可以通过对 $\sum_{n=0}^{+\infty} \frac{a_n}{n!} \varphi(a_n x) x^n$ 逐项求导得到. 一般地, 可以证明 $f(x)$ 任意次可导, 且各阶导数可以通过对 $\sum_{n=0}^{+\infty} \frac{a_n}{n!} \varphi(a_n x) x^n$ 逐项求导得到. 因此,

$$
\begin{array}{l} f ^ {(n)} (0) = \sum_ {k = 0} ^ {+ \infty} \left(\frac {a _ {k}}{k !} \varphi (a _ {k} x) x ^ {k}\right) ^ {(n)} \bigg | _ {x = 0} = \sum_ {k = 0} ^ {n} \left(\frac {a _ {k}}{k !} \varphi (a _ {k} x) x ^ {k}\right) ^ {(n)} \bigg | _ {x = 0} \\ = \sum_ {k = 0} ^ {n} \frac {a _ {k}}{k !} \sum_ {i = 1} ^ {n} \mathrm{C} _ {n} ^ {i} (\varphi (a _ {k} x)) ^ {(i)} (x ^ {k}) ^ {(n - i)} \Bigg | _ {x = 0} \\ = \sum_ {k = 0} ^ {n} \frac {a _ {k}}{k !} \mathrm{C} _ {n} ^ {n - k} k! a _ {k} ^ {n - k} \varphi^ {(n - k)} (0) \\ = \sum_ {k = 0} ^ {n} C _ {n} ^ {n - k} a _ {k} ^ {n + 1 - k} \varphi^ {(n - k)} (0) \\ = \mathrm{C} _ {n} ^ {0} a _ {n} \varphi^ {(0)} (0) = a _ {n}, \quad \forall n \in \mathbb {N}. \\ \end{array}
$$

我们上面看到, 的确存在无穷光滑的函数, 其 Taylor 级数的收敛半径为零, 但可以证明, 这些函数不应该是初等函数.

## Tauber 型求和: Cesàro 求和, Abel 求和.

下面我们简要介绍一下另外两种模式下的级数求和: Cesàro 求和与 Abel 求和. 我们知道, 对于给定的数列  $\{a_{n}\}$ , 可以通过引入部分和数列  $\{S_{n}\}$ ,  $S_{n}=a_{1}+a_{2}+\cdots+a_{n}$  ( $n=1,2,\cdots$ ), 以及  $\{S_{n}\}$  的极限存在与否来定义级数的收敛与发散. 因此, 可以看到, 这仅仅是对给定数列  $\{a_{n}\}$  的一种人为的 (经典) 求和模式而已. 既然如此, 我们也可以用其他的方式来定义级数的求和. Cesàro 求和以及 Abel 求和即为另外两种常见求和方式.

Cesàro 求和: 这是由意大利数学家 E. Cesàro 引入的一种计算级数和的方法, 此定义推广了经典的级数求和, 使得不仅适用于收敛的级数, 也适用于某些通常意义下发

---

13.5 幂级数的代数运算

199

散的级数. 如果级数在经典意义下收敛到 $S$, 则其 Cesàro 求和也收敛且其值也为 $S$. 对于某些经典模式下发散的级数, 通过 Cesàro 求和方式, 也有可能给出一个和.

定义 13.5.1 级数  $\sum_{n=1}^{+\infty} c_{n}$  称为可 Cesàro 求和 (或 Cesàro 可知), 是指当  $n \to +\infty$  时数列  $\{\sigma_{n}\}$  极限  $\lim_{n \to +\infty} \sigma_{n}$  存在且为有限, 其中

$$
\sigma_ {n} = \frac {S _ {1} + S _ {2} + \cdots + S _ {n}}{n}, \qquad S _ {k} = \sum_ {n = 1} ^ {k} c _ {n},
$$

并且把极限值定义为级数的 Cesàro 意义下的和, 简称 Cesàro 和.

下面的结论可以由 Stolz 公式 (Stolz-Cesàro 定理) 得到.

定理 13.5.5 如果级数  $\sum_{n=1}^{+\infty} c_{n}$  收敛, 则该级数一定可 Cesàro 求和, 且级数和与 Cesàro 和相等.

注意, 定理的逆命题不成立.

例 13.5.7 发散级数  $\sum_{n=1}^{+\infty}(-1)^{n+1}$  是可 Cesàro 求和的, 且 Cesàro 和为  $\frac{1}{2}$ .

如果我们把上述 Cesàro 求和称为一阶 Cesàro 求和, 并称为 Cesàro  $(C,1)$  求和的话, 那么进一步, 我们还可以定义二阶甚至 p 阶的 Cesàro 求和  $(C,p)$  如下:

首先, 考虑通项为  $b_{n} \equiv 1$  的特殊级数

$$
\sum_ {n = 1} ^ {+ \infty} b _ {n} = 1 + 1 + 1 + \dots .
$$

定义

$$
B _ {n} ^ {(- 1)} = b _ {n} = 1 = \mathrm{C} _ {n} ^ {0}, \qquad B _ {n} ^ {(0)} = \sum_ {k = 1} ^ {n} b _ {k} = n = \mathrm{C} _ {n} ^ {1},
$$

$$
B _ {n} ^ {(1)} = \sum_ {k = 1} ^ {n} B _ {k} ^ {(0)} = \frac {n (n + 1)}{2} = \mathrm{C} _ {n + 1} ^ {2}, \quad \dots , \quad B _ {n} ^ {(p)} = \sum_ {k = 1} ^ {n} B _ {k} ^ {(p - 1)} = \mathrm{C} _ {n + p} ^ {p + 1}, \dots .
$$

其次, 对任一给定级数 $\sum_{n=1}^{+\infty} a_n$, 记 $A_n^{(0)} = \sum_{k=1}^{n} a_k$. 把前面定义中的级数 $\sum_{n=1}^{+\infty} a_n$ 的一阶 Cesàro (C, 1) 求和改记为

$$
A _ {n} ^ {(1)} = \lim _ {n \to + \infty} \frac {\sum_ {k = 1} ^ {n} B _ {k} ^ {(- 1)} A _ {k} ^ {(0)}}{B _ {n} ^ {(0)}} = \frac {A _ {1} ^ {(0)} + A _ {2} ^ {(0)} + \cdots + A _ {n} ^ {(0)}}{\mathrm{C} _ {n} ^ {1}}.
$$

定义级数 $\sum_{n=1}^{+\infty} a_n$ 的二阶 Cesàro $(C,2)$ 求和为

$$
A _ {n} ^ {(2)} = \lim _ {n \to + \infty} \frac {\sum_ {k = 1} ^ {n} B _ {k} ^ {(0)} A _ {k} ^ {(1)}}{\sum_ {k = 1} ^ {n} B _ {k} ^ {(0)}} = \frac {n A _ {1} ^ {(0)} + (n - 1) A _ {2} ^ {(0)} + \cdots + A _ {n} ^ {(0)}}{\mathrm{C} _ {n + 1} ^ {2}}.
$$

---

200

第十三章 幂级数

更一般地, 定义级数  $\sum_{n=1}^{+\infty}a_{n}$  的 p 阶  $(p \geqslant 2)$  Cesàro  $(C, p)$  求和为

$$
A _ {n} ^ {(p)} = \lim _ {n \to + \infty} \frac {\sum_ {k = 1} ^ {n} B _ {k} ^ {(p - 2)} A _ {k} ^ {(p - 1)}}{\sum_ {k = 1} ^ {n} B _ {k} ^ {(p - 2)}} = \frac {\mathrm{C} _ {n + p - 2} ^ {p - 1} A _ {1} ^ {(0)} + \mathrm{C} _ {n + p - 3} ^ {p - 1} A _ {2} ^ {(0)} + \cdots + \mathrm{C} _ {p - 1} ^ {p - 1} A _ {n} ^ {(0)}}{\mathrm{C} _ {n + p - 1} ^ {p}}.
$$

以上求和方法统称为 Cesàro 求和法.

Abel 求和: 我们再来看另一种常见的级数求和——Abel 求和.

定义 13.5.2 级数  $\sum_{n=1}^{+\infty}a_{n}$  称为可 Abel 求和 (或 Abel 可知), 是指极限

$$
\lim _ {x \to 1 ^ {-}} \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = S \tag {13.5.9}
$$

存在且为有限. 极限值 S 定义为级数在 Abel 意义下的和, 简称 Abel 和.

容易看出, 若 $\sum_{n=0}^{+\infty} a_n$ 收敛到 $S$, 则根据 Abel 定理, 关系式 (13.5.9) 必然成立. 另一方面, 易见级数 $\sum_{n=0}^{+\infty} (-1)^n$ 是 Abel 可和的, 但非经典可和. 因此, Abel 可和的确是经典级数可和的推广.

如果我们对级数通项加适当条件, 可以得到 Abel 可和与经典可和的关系:

定理 13.5.6 (小 o Tauber 定理) 设  $\lim_{x\to1^{-}}\sum_{n=1}^{+\infty}a_{n}x^{n}=A$  且  $a_{n}=o\left(\frac{1}{n}\right)$ ，则
 $\sum_{n=1}^{+\infty}a_{n}=A.$

证明 $\forall \varepsilon > 0$, 考虑 $\forall N > 0$, 令 $x = 1 - \frac{1}{N}$. 有

$$
\left| \sum_ {n = 1} ^ {N} a _ {n} - \sum_ {n = 1} ^ {N} a _ {n} x ^ {n} \right| \leqslant \sum_ {n = 1} ^ {N} | a _ {n} | \left(1 - \left(1 - \frac {1}{N}\right) ^ {n}\right) \leqslant \sum_ {n = 1} ^ {N} | a _ {n} | \frac {n}{N} \rightarrow 0 \quad (N \rightarrow + \infty).
$$

又

$$
\begin{array}{l} \left| \sum_ {n = 1} ^ {+ \infty} a _ {n} x ^ {n} - \sum_ {n = 1} ^ {N} a _ {n} x ^ {n} \right| \leqslant \sum_ {n > N} | a _ {n} | \left(1 - \frac {1}{N}\right) ^ {n} \leqslant \sum_ {n > N} \frac {n a _ {n}}{N} \left(1 - \frac {1}{N}\right) ^ {n} \leqslant \sum_ {n > N} \frac {\varepsilon}{N} \left(1 - \frac {1}{N}\right) ^ {n} \\ = \varepsilon \left(1 - \frac {1}{N}\right) ^ {N + 1} \rightarrow \frac {\varepsilon}{\mathrm{e}} \quad (N \rightarrow + \infty). \\ \end{array}
$$

综合二者结论得证.

Cesàro 可和与 Abel 可和的关系: 我们有

---

13.5 幂级数的代数运算

201

定理 13.5.7 若级数  $\sum_{n=0}^{+\infty} a_{n}$  Cesàro 可和, 则  $\sum_{n=0}^{+\infty} a_{n}$  也 Abel 可和, 且 Abel 和等于 Cesàro 和.

证明 不妨设 $\sum_{n=0}^{+\infty} a_n$ 的 Cesàro 和为零. 任取 $m \geqslant 1$, 对于 $x \in (0,1)$, 我们有

$$
\begin{array}{l} \left| \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} \right| = \left| (1 - x) \sum_ {n = 0} ^ {+ \infty} S _ {n} x ^ {n} \right| = \left| (1 - x) ^ {2} \sum_ {n = 0} ^ {+ \infty} (n + 1) \sigma_ {n} x ^ {n} \right| \\ \leqslant (1 - x) ^ {2} \sum_ {n = 0} ^ {m} (n + 1) \left| \sigma_ {n} \right| x ^ {n} + (1 - x) ^ {2} \sup _ {k \geqslant m} \left| \sigma_ {k} \right| \sum_ {n = m + 1} ^ {+ \infty} (n + 1) x ^ {n} \\ \leqslant (1 - x) ^ {2} \sum_ {n = 0} ^ {m} (n + 1) | \sigma_ {n} | x ^ {n} + \sup _ {k \geqslant m} | \sigma_ {k} |. \\ \end{array}
$$

因此 $\lim_{x\to 1^{-}}\left|\sum_{n = 0}^{+\infty}a_nx^n\right|\leqslant \sup_{k\geqslant m}|\sigma_k|$. 再令 $m\to +\infty$ 即得 $\lim_{x\to 1^{-}}\sum_{n = 0}^{+\infty}a_nx^n = 0.$

注意, 上面推导过程中用到关系式

$$
1 = (1 - x) ^ {2} \sum_ {n = 0} ^ {+ \infty} (n + 1) x ^ {n},
$$

以及两次用到 Abel 变换:

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = (1 - x) \sum_ {n = 0} ^ {+ \infty} S _ {n} x ^ {n} = (1 - x) ^ {2} \sum_ {n = 0} ^ {+ \infty} (n + 1) \sigma_ {n} x ^ {n}.
$$

这是因为

$$
\begin{array}{l} \left(1 - 2 x + x ^ {2}\right) \sum_ {n = 0} ^ {+ \infty} (n + 1) \sigma_ {n} x ^ {n} = \sum_ {n = 0} ^ {+ \infty} \left((n + 1) \sigma_ {n} - 2 n \sigma_ {n - 1} + (n - 1) \sigma_ {n - 2}\right) x ^ {n} \\ = \sum_ {n = 0} ^ {+ \infty} (((n + 1) \sigma_ {n} - n \sigma_ {n - 1}) - (n \sigma_ {n - 1} - (n - 1) \sigma_ {n - 2})) x ^ {n} \\ = \sum_ {n = 0} ^ {+ \infty} \left(S _ {n} - S _ {n - 1}\right) x ^ {n} = \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}. \\ \end{array}
$$

下面的例子告诉我们, Abel 可和不一定蕴涵着 Cesàro 可和. 因此 Abel 可和是一种比 Cesàro 可和更广的求和方式.

例 13.5.8 考虑通项为  $a_{n}=(-1)^{n+1}n$  的级数

$$
1 - 2 + 3 - 4 + 5 - 6 + \dots .
$$

---

202

第十三章 幂级数

显然, 此级数发散. 进一步, 直接计算可以看出该级数的 Cesàro $(C,1)$ 求和也发散. 事实上, 这是因为

$$
S _ {1} = 1, \quad S _ {2} = - 1, \quad S _ {3} = 2, \quad S _ {4} = - 2, \quad \dots , S _ {2 n - 1} = n, \quad S _ {2 n} = - n, \quad \dots ,
$$

所以

$$
\sigma_ {1} = 1, \quad \sigma_ {2} = 0, \quad \sigma_ {3} = \frac {2}{3}, \quad \sigma_ {4} = 0, \quad \dots , \quad \sigma_ {2 n - 1} = \frac {n}{2 n - 1}, \quad \sigma_ {2 n} = 0, \quad \dots ,
$$

故  $\{\sigma_{n}\}$  的极限不存在.

但可以证明, 此级数是 Abel 可和的. 为此, 考虑幂级数

$$
x - 2 x ^ {2} + 3 x ^ {3} - 4 x ^ {4} + 5 x ^ {5} - 6 x ^ {6} + \dots ,
$$

该幂级数在区间 $(0,1)$ 上有和函数 $f(x) = \frac{x}{(1 + x)^2}$，当 $x\to 1^{-}$ 时趋近于极限 $\frac{1}{4}$，因此该级数在Abel意义下是可和的.

在讨论常数项级数乘积时, 我们在例 11.4.3 中断言, 存在两个条件收敛的级数, 它们的 Cauchy 乘积级数绝对收敛. 下面我们首先证明这个结论.

例 13.5.9 证明: 存在两个条件收敛的级数, 它们的 Cauchy 乘积级数绝对收敛.

证明 注意到当 $|x| < 1$ 时, 对任意实数 $m$, 函数 $(1 + x)^{m}$ 的 Taylor 级数总是绝对收敛的. 若 $-1 < m < 0$, 则当 $x = 1$ 时, 相应的级数是条件收敛的, 当 $x = -1$ 时, 级数发散. 所以, 级数

$$
f (x) = \frac {1 + x}{\sqrt {1 + x ^ {3}}} = \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}
$$

与级数

$$
g (x) = \frac {1 - x + x ^ {2}}{\sqrt {1 + x ^ {3}}} = \sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}
$$

当 $|x| < 1$ 时绝对收敛, $x = 1$ 时条件收敛. 因此, 级数 $\sum_{n=0}^{+\infty} a_n$, $\sum_{n=0}^{+\infty} b_n$ 都是条件收敛的.

由于对任意的 x，都有  $f(x) \cdot g(x) \equiv 1$ ，故  $c_{0} = 1, c_{n} = 0 (n = 1, 2, \cdots)$ ，其中  $c_{n} = a_{0} b_{n} + a_{1} b_{n-1} + \cdots + a_{n} b_{0}$ 。因此，级数  $\sum_{n=0}^{+\infty} c_{n}$  绝对收敛。

另一方面, 在讨论常数项级数乘积时, 定理 11.4.11 告诉我们, 如果两个收敛级数的 Cauchy 乘积级数收敛, 那么 Cauchy 乘积级数的和等于两个收敛级数和的乘积. 但是, 例 11.4.4 告诉我们, 两个条件收敛级数其 Cauchy 乘积级数有可能不收敛. 下面的定理告诉我们, 两个收敛级数的 Cauchy 乘积级数, 在 Cesàro 意义下总是可求和的. 即, 下面的 Cesàro 定理成立.

---

13.5 幂级数的代数运算

203

定理 13.5.8 (Cesàro 定理) 设级数  $\sum_{n=0}^{+\infty}a_{n}$  和  $\sum_{n=0}^{+\infty}b_{n}$  分别收敛到 A 和 B, 则它

们的 Cauchy 乘积  $\sum_{n=0}^{+\infty}c_{n}$  Cesàro 可和, 且和为 AB.

证明 记

$$
A _ {n} = \sum_ {k = 0} ^ {n} a _ {k}, \quad B _ {n} = \sum_ {k = 0} ^ {n} b _ {k}, \quad C _ {n} = \sum_ {k = 0} ^ {n} c _ {k}, \quad H _ {n} = \sum_ {k = 0} ^ {n} C _ {k}, \quad n \geqslant 0.
$$

由定理假设， $\lim_{n\to+\infty}A_{n}=A,\quad\lim_{n\to+\infty}B_{n}=B.$  而  $\forall x\in(-1,1)$ ,

$$
\begin{array}{l} (1 - x) ^ {2} \sum_ {n = 0} ^ {+ \infty} H _ {n} x ^ {n} = \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n} = \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) \left(\sum_ {n = 0} ^ {+ \infty} b _ {n} x ^ {n}\right) \\ = \left((1 - x) \sum_ {n = 0} ^ {+ \infty} A _ {n} x ^ {n}\right) \left((1 - x) \sum_ {n = 0} ^ {+ \infty} B _ {n} x ^ {n}\right) \\ = (1 - x) ^ {2} \sum_ {n = 0} ^ {+ \infty} \sum_ {k = 0} ^ {n} A _ {k} B _ {n - k} x ^ {n}. \\ \end{array}
$$

所以

$$
\lim _ {n \to + \infty} \frac {H _ {n}}{n + 1} = \lim _ {n \to + \infty} \frac {1}{n + 1} \sum_ {k = 0} ^ {n} A _ {k} B _ {n - k} = A B.
$$

定理得证.

关于 Abel 求和, 下面的定理成立:

定理 13.5.9 设  $\sum_{n=0}^{+\infty}a_{n}$  和  $\sum_{n=0}^{+\infty}b_{n}$  均 Abel 可和, 且它们的 Abel 和为 A 和 B, 则
 $\sum_{n=0}^{+\infty}a_{n}$  和  $\sum_{n=0}^{+\infty}b_{n}$  的 Cauchy 乘积也 Abel 可和, 且 Abel 和为 AB.

## 习题 13.5

1. 考虑函数 $f(x) = \ln (1 + x + x^2 + x^3 + x^4)$.

(1) 求 $f(x)$ 在 $x_0 = 0$ 处的幂级数展开 $\sum_{n=1}^{+\infty} a_n x^n$.
(2) 确定幂级数的收敛域.
(3) 计算  $\sum_{n=1}^{+\infty}a_{n}$ .

---

204

第十三章 幂级数

2. 如果在定理 13.5.2 中, 两个幂级数的收敛半径分别为  $R_{1}, R_{2}$ , 问它们乘积级数的收敛半径是多少?

3. 试用形式幂级数的思路, 用待定系数的方法, 即 $y = \sum_{n=0}^{+\infty} a_n x^n$ 以及形式求导和形式二阶导, 验证微分方程 $x^2 y' = (1 - x)y - 1$, $y(0) = 1$ 具有形式幂级数解 $y = \sum_{n=0}^{+\infty} n! x^n$.

4. 试问初等函数的 Taylor 级数有没有可能收敛半径为 0?

5. 设 $P_{m}(x)$ 是给定的 $m$ 次多项式. 考虑由下面级数定义的函数 $f(x)$:

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {P _ {m} ^ {n} (x)}{n !}.
$$

证明: $f(x)$ 的幂级数展开式中，不可能连着出现 $m$ 个零系数.

6. 证明: 当 $\sum_{n=0}^{+\infty} a_n$ Cesàro 可和时, $\left\{\frac{a_n}{n+1}\right\}$ 有界.

7. 求幂级数  $\sum_{n=1}^{+\infty}\frac{2}{4n-1}x^{2n}$  的和函数.

8. 设级数 $\sum_{n=0}^{+\infty} a_n$ 和 $\sum_{n=0}^{+\infty} b_n$ 均 Cesàro 可和, 试讨论它们的 Cauchy 乘积 $\sum_{n=0}^{+\infty} c_n$ 是否 Cesàro 可和?

9. 证明定理 13.5.9.

10. 设 $\sum_{n=0}^{+\infty} a_n$ 的 Abel 和为 $A$. 证明: $\sum_{n=0}^{+\infty} a_n$ 收敛当且仅当

$$
\lim _ {n \to + \infty} \frac {a _ {1} + 2 a _ {2} + \cdots + n a _ {n}}{n} = 0.
$$

11. 试讨论例 13.5.8 中级数是否可二阶 Cesàro 求和？是否可三阶 Cesàro 求和？进一步思考，是否一个发散的但 Abel 可和的级数，一定存在自然数 k，使得该级数是 k 阶 Cesàro 可和的.

12. 设幂级数

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = f (x)
$$

中的所有系数 $a_{n} \in \{0,1,\dots ,9\}$. 试证明:如果 $f\left(\frac{1}{10}\right) \in \mathbb{Q}$, 那么 $f(x)$ 是一个有理函数, 即 $f(x) = \frac{P(x)}{Q(x)}$, 其中 $P(x), Q(x)$ 是多项式.

---

13.6 连续函数的多项式逼近

205

## 13.6 连续函数的多项式逼近

函数的逼近是分析学和有关应用学科中极其重要的一部分内容. 它的基本出发点是由简单的、熟悉的、光滑性好的函数, 按照某种度量标准, 逼近一个给定的通常是相对复杂的、陌生的、性质一般的函数. 比如前面章节中看到的用逐段常值函数、折线函数、连续函数来逼近可积函数, 用 Taylor 多项式来逼近一个光滑的函数, 等等.

我们知道, 如果函数  $f(x)$  在  $(-R, R)$  中能展开成幂级数, 那么对任意  $[a, b] \subset (-R, R)$ ,  $f(x)$  在  $[a, b]$  上能用多项式一致逼近, 即  $\forall \varepsilon > 0, \exists N > 0$ , 只要 n > N, 取 n 阶 Taylor 多项式  $T_{n}(x)$  即可做到  $|f(x) - T_{n}(x)| < \varepsilon$ .

但是能展开成幂级数的函数少之又少, 因为它对函数的要求太高了: 要有足够高阶的导数. 所以, 用幂级数来逼近一个函数具有太大的局限性. 另一方面, 一个非常自然的问题是: 对一些光滑性并不那么好的函数是否存在多项式逼近? 特别地, 比如连续函数可否由多项式逼近? 这是因为从函数的复杂性来看, 多项式是一类光滑性好、形式简单、便于分析的函数.

本节重点讨论连续函数的多项式逼近问题. 当然, 我们也有足够的理由用其他类型的“简单的、基本的、熟悉的”函数去逼近, 比如正弦函数、余弦函数等三角函数也具有上述好的特点, 因为毕竟“简单的、基本的”等字眼是主观的标准. 的确, 比如如何用三角函数逼近一般的函数同样是个重要的话题. 与此相关的内容, 我们将放到 Fourier 级数去讨论.

为了陈述方便, 我们先给出以下定义:

定义 13.6.1 设  $f(x)$  是定义在区间  $I \subseteq R$  上的函数, 如果对任意  $\varepsilon > 0$ , 总能找到多项式  $P(x)$ , 使得对 I 中所有的 x 均有

$$
| f (x) - P (x) | <   \varepsilon , \quad x \in I
$$

成立, 则称  $f(x)$  在 I 上能被多项式一致逼近.

显然, $f(x)$ 在 $I$ 上可被多项式一致逼近的充要条件是存在多项式序列 $\{P_n(x)\}$, 使得 $P_n(x) \Rightarrow f(x) (x \in I)$. 另一方面, 我们知道, 如果 $f(x)$ 在 $I$ 上可被多项式一致逼近, 则显然 $f(x)$ 在 $I$ 上连续.

如果 $f(x)$ 在有限开区间 $(a, b)$ 上可被多项式一致逼近, 则由一致性, 可以证明 $f(x)$ 必可以连续延拓到闭区间 $[a, b]$ 上. 若 $I$ 是无穷区间, 当 $f(x)$ 不是多项式时, 则 $f(x)$ 在 $I$ 上一定不能被多项式逼近. 所以, 很自然提出下面的问题: 对于有限闭区间上的连续函数 $f(x)$, 是否一定可被多项式逼近? 下面著名的 Weierstrass 定理对此问题给出了一个充分性的答案:

如下定理称为 Weierstrass 第一逼近定理.

---

206

第十三章 幂级数

定理 13.6.1. 有界闭区间上的连续函数可用多项式一致逼近. 即对闭区间 $[a, b]$ 上的任意连续函数 $f(x)$, 存在多项式序列 $\{P_n(x)\}$, 使得在 $[a, b]$ 上 $P_n(x) \Rightarrow f(x)$.

Weierstrass 逼近定理有许多经典的证明方法, 这些方法各有鲜明的特点, 其背后通常还蕴含着不同的逼近思想和相关的学科背景. 下面我们给出的证明是基于 Bernstein 多项式的方法.

证法 1 不妨假设  $[a, b] = [0, 1]$ ，因为必要的话，作一个线性变换  $x = a + (b - a)t$ ，即可把问题转化为关于变量  $t \in [0, 1]$  上的连续函数的逼近.

记

$$
p _ {n, k} (x) = \mathrm{C} _ {n} ^ {k} x ^ {k} (1 - x) ^ {n - k},
$$

则有

$$
\sum_ {k = 0} ^ {n} p _ {n, k} (x) = 1. \tag {13.6.1}
$$

设 $f(x)$ 是 $[0,1]$ 上的连续函数, $n \geqslant 0$, 定义 $f$ 的 $n$ 阶 Bernstein 多项式为

$$
B _ {n} (f, x) = \sum_ {k = 0} ^ {n} f \left(\frac {k}{n}\right) p _ {n, k} (x) = \sum_ {k = 0} ^ {n} f \left(\frac {k}{n}\right) \mathrm{C} _ {n} ^ {k} x ^ {k} (1 - x) ^ {n - k}. \tag {13.6.2}
$$

我们将证明: $\{B_{n}(f,x)\}$ 是[0,1]上的一致收敛到 $f(x)$ 的多项式序列.

首先, 对方程 (13.6.1) 两端求导再乘 $x(1 - x)$, 可得

$$
\sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} (k - n x) x ^ {k} (1 - x) ^ {n - k} = 0, \quad \forall   x \in [ 0, 1 ]. \tag {13.6.3}
$$

对上式继续求导后再乘 $x(1 - x)$ 可得

$$
\sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} (k - n x) ^ {2} x ^ {k} (1 - x) ^ {n - k} = n x (1 - x), \quad \forall   x \in [ 0, 1 ]. \tag {13.6.4}
$$

整理上面的计算, 可得

$$
\begin{array}{l} \sum_ {k = 0} ^ {n} k p _ {n, k} (x) = n x, \\ \sum_ {k = 0} ^ {n} k ^ {2} p _ {n, k} (x) = n (n - 1) x ^ {2} + n x \\ \end{array}
$$

$$
\sum_ {k = 0} ^ {n} \left(x - \frac {k}{n}\right) ^ {2} p _ {n, k} (x) = \frac {x (1 - x)}{n}.
$$

由于 $f(x)$ 在 $[0,1]$ 上一致连续，故对任意 $\varepsilon > 0$ ，存在 $\delta > 0$ ，当 $|x - y| < \delta$ 时，有

$$
| f (x) - f (y) | <   \frac {\varepsilon}{2}.
$$

---

13.6 连续函数的多项式逼近

207

再由 $f(x)$ 的有界性, 知 $\exists M > 0$, 使得 $|f(x)| \leqslant M$, 当 $|x - y| \geqslant \delta$ 时,

$$
| f (x) | \leqslant M \leqslant \frac {M (x - y) ^ {2}}{\delta^ {2}}.
$$

因此, $\forall x\in [0,1]$ ，都有

$$
\left| f (x) - f \left(\frac {k}{n}\right) \right| <   \frac {\varepsilon}{2} + \frac {2 M}{\delta^ {2}} \left(x - \frac {k}{n}\right) ^ {2}.
$$

从而

$$
\begin{array}{l} \left| f (x) - B _ {n} (x) \right| = \left| \sum_ {k = 0} ^ {n} \left(f (x) - f \left(\frac {k}{n}\right)\right) p _ {n, k} (x) \right| \\ \leqslant \sum_ {k = 0} ^ {n} \left| f (x) - f \left(\frac {k}{n}\right) \right| p _ {n, k} (x) \\ \leqslant \frac {\varepsilon}{2} + \frac {2 M}{\delta^ {2}} \frac {x (1 - x)}{n} \leqslant \frac {\varepsilon}{2} + \frac {M}{2 \delta^ {2}} \frac {1}{n}. \\ \end{array}
$$

即  $B_{n}(f,x)\Rightarrow f(x)$ .

![](../../raw/pages_0497-0512/images/page_511_image_9.jpg)

下面给出基于 Lebesgue 做法的另一种直观性很强的证明. 我们仅给出基本步骤和思路, 读者可以补充细节.

证法 2  $\forall x \in [-1,1]$ ，令

$$
u _ {0} (x) = 0, \quad u _ {n + 1} (x) = u _ {n} (x) + \frac {1}{2} (x ^ {2} - u _ {n} ^ {2} (x)), \quad n = 0, 1, 2, \dots . \tag {13.6.5}
$$

不难证明以下结论:

(1) 对每个  $n \in N$ ,  $u_{n}(x)$  是一个多项式.
(2) 可以归纳证明, 对每个  $x \in [-1,1]$ ,  $0 \leqslant u_{n}(x) \leqslant u_{n+1}(x) \leqslant |x|$ .
(3) $\{u_{n}(x)\}$ 关于 $n$ 单调, 逐点收敛到极限函数 $|x|$, 由于 $|x|$ 在 $[-1,1]$ 上连续, 根据 Dini 定理, 知上述逐点收敛实则为一致收敛 (注: 也可通过估计

$$
\left| | x | - u _ {n} (x) \right| \leqslant | x | \left(1 - \frac {| x |}{2}\right) ^ {n} <   \frac {2}{n + 1}
$$

直接证明一致收敛性).

(4) 将 (13.6.5) 式中的迭代列换成

$$
u _ {0} (x) = 0, \quad u _ {n + 1} (x) = u _ {n} (x) + \frac {1}{2} \Big ((x - c) ^ {2} - u _ {n} ^ {2} (x) \Big), \quad n = 0, 1, 2, \dots ,
$$

重复上述过程, 可得  $\{u_{n}(x)\}$  一致收敛到  $|x-c|$ .

(5) $\forall \lambda \in \mathbb{R}$, 多项式序列 $\{\lambda u_n(x)\}$ 一致收敛到 $\lambda |x - c|$.
(6) 闭区间 $[a, b]$ 上的连续函数能被逐段折线 (即分段线性函数) 一致逼近.

---

208

第十三章 幂级数

(7) 闭区间 $[a, b]$ 上的逐段线性函数 $g(x)$ 一定可以写成

$$
g (x) = g (a) + \sum_ {i = 1} ^ {n} \lambda_ {i} L (x - c _ {i})
$$

形式, 其中  $L(x)=\frac{1}{2}(|x|+x)=\max\{x,0\}, c_{i}$  为折线的转折点.

(8) 若函数  $\xi_{k}(x)$  ( $k=1,2,\cdots,K$ ) 在  $[a,b]$  上能被多项式一致逼近，则  $\sum_{k=1}^{K}\lambda_{k}\xi_{k}(x)$  在  $[a,b]$  上也能被多项式一致逼近. □

## 习题 13.6

1. 按照下列步骤给出 Weierstrass 逼近定理的另一个证明:

(1) 设 $c_{n} = \int_{-1}^{1}(1 - x^{2})^{n}\mathrm{d}x$, 证明: $c_{n} < \sqrt{\pi n}$.

(2) 设 $f$ 是 $[0,1]$ 上的连续函数, 并且 $f(0) = f(1) = 0$. 当 $x \in [0,1]$ 时, 定义 $f(x) = 0$. 记 $Q_{n}(t) = c_{n}(1 - t^{2})^{n}$. 证明:

$$
P _ {n} (x) = \int_ {0} ^ {1} f (x + t) Q _ {n} (t) \mathrm{d} t, \quad 0 \leqslant x \leqslant 1
$$

是一个多项式, 而且

$$
\lim _ {n \to + \infty} P _ {n} (x) = f (x)
$$

在 $[0,1]$ 上一致收敛成立.

(3) 当 $f(0) \neq 0$ 或 $f(1) \neq 0$ 的条件不成立时, 证明 Weierstrass 逼近定理.

2. 设 $f$ 在 $[0,1]$ 上连续, 证明:

$$
\lim _ {n \to + \infty} \frac {1}{2 ^ {n}} \sum_ {k = 0} ^ {n} (- 1) ^ {k} C _ {n} ^ {k} f \left(\frac {k}{n}\right) = 0.
$$

3. 设 $f$ 是 $[a, b]$ 上的连续函数, 如果

$$
\int_ {a} ^ {b} f (x) x ^ {n} \mathrm{d} x = 0, \quad n = 0, 1, 2, \dots ,
$$

证明: $f$ 在 $[a, b]$ 上恒等于 0.

4. 若 $f$ 在 $(-\infty, +\infty)$ 中能用多项式一致逼近, 证明: $f$ 必为一多项式.

5. 设 $f$ 在 $[0,1]$ 上有定义, $B_{n}(f,x)$ 是函数 $f$ 的 $n$ 阶 Bernstein 多项式 (见习题 13.2 中 8 的表达式 (13.2.7)). 证明:

(1) (端点插值性) $B_{n}(f,0) = f(0), B_{n}(f,1) = f(1)$.

---

13.6 连续函数的多项式逼近

209

(2) (保序性) 如果 $f(t) \geqslant 0 (t \in [0,1])$, 则 $B_{n}(f,x) \geqslant 0$; 如果 $f(t) > 0 (t \in [0,1])$, 则 $B_{n}(f,x) > 0$.

(3) (保有界性) 如果 $m \leqslant f(t) \leqslant M (t \in [0,1])$, 则 $m \leqslant B_n(f,x) \leqslant M$.
(4) (保凸性) 如果 f 是  $[0,1]$  上的凸函数, 那么  $B_{n}(f,x)$  也是凸函数.

6. 设 $f$ 在 $[0,1]$ 上可导, 证明:

$$
B _ {n} ^ {\prime} (f, x) = n \sum_ {k = 0} ^ {n - 1} \left(f \left(\frac {k + 1}{n}\right) - f \left(\frac {k}{n}\right)\right) \mathrm{C} _ {n - 1} ^ {k} x ^ {k} (1 - x) ^ {n - k - 1}.
$$

进一步, $B_{n}(f,x)$ 具有 $C^1$ 收敛性, 即, 如果 $f \in C^{1}[0,1]$, 则 $B_{n}^{\prime}(f,x)$ 一致收敛于 $f'(x)$.

更一般地， $B_{n}(f,x)$ 具有 $C^m$ 收敛性，即，对于 $m\geqslant 1$ ，如果 $f\in C^{m}[0,1]$ ，则$B_{n}^{(m)}(f,x)$ 一致收敛于 $f^{(m)}(x)$

7. 设 $\alpha \in (0,1], L > 0, f$ 在 $[0,1]$ 上有定义, 满足 $\alpha$ 阶 Hölder 连续

$$
| f (x) - f (y) | \leqslant L | x - y | ^ {\alpha}, \quad \forall x, y \in [ 0, 1 ].
$$

设 $B_{n}(f,x)$ 是函数 $f$ 的 $n$ 阶 Bernstein 多项式. 证明:

(1) $\forall x\in [0,1]$ ，成立

$$
| f (x) - B _ {n} (f, x) | \leqslant L \Big (\frac {1}{n} x (1 - x) \Big) ^ {\alpha / 2} \leqslant L n ^ {- \alpha / 2}.
$$

(2) $B_{n}(f,x)$ 在[0,1]上也满足 $\alpha$ 阶 Hölder 连续,且具有相同的系数L:

$$
| B _ {n} (f, x) - B _ {n} (f, y) | \leqslant L | x - y | ^ {\alpha}, \quad \forall x, y \in [ 0, 1 ].
$$

8. 设 $f(x)$ 在一个无穷区间可被多项式逼近, 证明: $f(x)$ 必是一个多项式.

9. 设  $f(x)$  在  $(a, b)$  可被多项式逼近, 证明:  $f(x)$  在  $(a, b)$  一致连续.

10. 设 $f \in C[1, +\infty)$，且存在 $\lim_{x \to +\infty} f(x) = c$，证明:对任给 $\varepsilon > 0$，存在多项式 $P(x)$，使得 $|f(x) - P(1/x)| < \varepsilon, x \geqslant 1$.

11. 设 $f \in C[0, +\infty)$，且存在 $\lim_{x \to +\infty} f(x) = c$，证明:对任给 $\varepsilon > 0$，存在多项式 $P(x)$，使得 $|f(x) - P(\mathrm{e}^{-x})| < \varepsilon, x \geqslant 0$.

12. 设 $f \in  C\left\lbrack  {a,b}\right\rbrack$ ,试证明: 存在多项式

$$
P _ {1} (x) \leqslant P _ {2} (x) \leqslant \dots \leqslant P _ {n} (x) \leqslant \dots
$$

使得  $\{P_{n}(x)\}$  在  $[a,b]$  上一致收敛到  $f(x)$ .

---

210

第十三章 幂级数

## 13.7 Peano 曲线

Peano 曲线又称 Hilbert 曲线, 是 Peano 于 1890 年首次发现的一件令人惊异的事实: 存在一条能够填满整个正方形的连续曲线. Peano 曲线的发现, 是数学史上的一件影响深远的事件, 它表明从低维到高维的连续映射的像集未必是零测集, 甚至一度引起对空间维数定义的基本思考. 后来, 人们就把能填满整个平面区域的连续曲线统称为 Peano 曲线. 下面我们简要介绍的一种构造 Peano 曲线的方法, 这是由 I. J. Schoenberg 在 1938 年给出的. 在 Schoenberg 的构造中, 他利用了实数的 $p$ 进制小数展开 $(p = 2,3)$.

考虑连续函数

$$
f (t) = \left\{ \begin{array}{l l} 0, & t \in [ 0, 1 / 3 ], \\ 3 t - 1, & t \in (1 / 3, 2 / 3 ], \\ 1, & t \in (2 / 3, 1 ]. \end{array} \right.
$$

将 f 延拓为 R 中周期为 2 的偶函数 (图 13.1).

$$
f (t) = f (t + 2), \quad f (t) = f (- t), \quad t \in \mathbb {R}.
$$

![](../../raw/pages_0513-0528/images/page_514_chart_8.jpg)

<details>
<summary>line</summary>

| t | f(t) |
| --- | --- |
| -3 | 1 |
| -2.5 | 0 |
| -2 | 0 |
| -1.5 | 1 |
| -1 | 1 |
| -0.5 | 0 |
| 0 | 0 |
| 0.5 | 1 |
| 1 | 1 |
| 1.5 | 0 |
| 2 | 0 |
| 2.5 | 1 |
</details>

图13.1 锯齿函数

令

$$
x (t) = \sum_ {n = 0} ^ {+ \infty} \frac {f (3 ^ {2 n} t)}{2 ^ {n + 1}}, \quad y (t) = \sum_ {n = 0} ^ {+ \infty} \frac {f (3 ^ {2 n + 1} t)}{2 ^ {n + 1}}, \quad t \in [ 0, 1 ].
$$

由于 $0 \leqslant f(x) \leqslant 1$，故这两个级数均一致收敛，从而 $x(t), y(t)$ 连续，

$$
\sigma (t) = (x (t), y (t)): I \to I \times I \quad (I = [ 0, 1 ])
$$

为连续曲线.

对任意点 $(a,b)\in I^2$ ，设 $a$ 与 $b$ 的二进制表示分别为

$$
a = \sum_ {n = 1} ^ {+ \infty} \frac {a _ {n}}{2 ^ {n}}, \quad b = \sum_ {n = 1} ^ {+ \infty} \frac {b _ {n}}{2 ^ {n}}, \tag {13.7.1}
$$

---

13.7 Peano 曲线

211

其中  $a_{n}, b_{n} \in \{0,1\} (\forall n \geqslant 1)$ ，定义实数  $\tilde{t}$  如下:

$$
0 \leqslant \tilde {t} := \frac {2 a _ {1}}{3} + \frac {2 b _ {1}}{3 ^ {2}} + \frac {2 a _ {2}}{3 ^ {3}} + \frac {2 b _ {2}}{3 ^ {4}} + \dots + \frac {2 a _ {n}}{3 ^ {2 n - 1}} + \frac {2 b _ {n}}{3 ^ {2 n}} + \dots \leqslant 2 \sum_ {n = 1} ^ {+ \infty} \frac {1}{3 ^ {n}} = 1. \tag {13.7.2}
$$

我们断言, 曲线 $\sigma$ 可以覆盖正方形 $I^{2}$, 即可以证明, $\forall (a, b) \in I^{2}$, 具有表示式 (13.7.1), 则由 (13.7.2) 给出的 $\tilde{t}$ 便满足 $a = x(\tilde{t}), b = y(\tilde{t})$. 事实上,

$$
\begin{array}{l} 3 ^ {2 n - 2} \tilde {t} = 3 ^ {2 n - 3} \cdot 2 a _ {1} + 3 ^ {2 n - 4} \cdot 2 b _ {1} + 3 ^ {2 n - 5} \cdot 2 a _ {2} + \dots + \frac {2 a _ {n}}{3} + \frac {2 b _ {n}}{3 ^ {2}} + \dots \\ = 2 \times N + \frac {2 a _ {n}}{3} + \tilde {a}, \\ \end{array}
$$

其中 $N \in \mathbb{N}$, $\tilde{a}$ 为 $\frac{2a_n}{3}$ 之后级数的余项之和. 满足 $0 \leqslant \tilde{a} \leqslant \sum_{n=2}^{+\infty} \frac{2}{3^n} = \frac{1}{3}$, 故有

$$
f (3 ^ {2 n - 2} \tilde {t}) = f \left(2 N + \frac {2 a _ {n}}{3} + \tilde {a}\right) = f \left(\frac {2 a _ {n}}{3} + \tilde {a}\right).
$$

若 $a_{n} = 0$ ，则 $0\leqslant \frac{2a_n}{3} +\tilde{a}\leqslant \frac{1}{3}$ 故 $f(3^{2n - 2}\tilde{t}) = f\left(\frac{2a_n}{3} +\tilde{a}\right) = 0 = a_n.$

若 $a_{n} = 1$ ，则 $\frac{2}{3}\leqslant \frac{2a_n}{3} +\tilde{a}\leqslant 1,$ 故 $f(3^{2n - 2}\tilde{t}) = f\left(\frac{2a_n}{3} +\tilde{a}\right) = 1 = a_n.$

同理有 $f(3^{2n - 1}\tilde{t}) = b_n$ ，从而有

$$
x (\tilde {t}) = a, \quad y (\tilde {t}) = b.
$$

证毕.

从证明中可以看出, 对于一个三进制表示的实数  $\tilde{t}$ , 连续函数  $x(t), y(t)$  事实上起到了把数对  $(a, b)$  分别从  $\tilde{t}$  中过滤出来的作用.

## 习题 13.7

1. 证明: 空间连续曲线

$$
\left\{ \begin{array}{l} x (t) = \sum_ {n = 1} ^ {+ \infty} \varphi (3 ^ {n} t - 3 ^ {n - 1}) \frac {1}{2 ^ {n}}, \\ y (t) = \sum_ {n = 1} ^ {+ \infty} \varphi (3 ^ {n} t - 2 \cdot 3 ^ {n - 1}) \frac {1}{2 ^ {n}}, \quad t \in [ 0, 1 ], \\ z (t) = \sum_ {n = 1} ^ {+ \infty} \varphi (3 ^ {n} t) \frac {1}{2 ^ {n}} \end{array} \right.
$$

---

212

第十三章 幂级数

能填满整个立方体 $[0,1]^3$ ，其中 $\varphi$ 在 $I = [0,1]$ 上定义如下:

$$
\varphi (t) = \left\{ \begin{array}{l l} 0, & t \in \left[ 0, \frac {1}{3} \right], \\ 3 t - 1, & t \in \left(\frac {1}{3}, \frac {2}{3} \right], \\ 1, & t \in \left(\frac {2}{3}, 1 \right]. \end{array} \right.
$$
