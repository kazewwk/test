## 4.5.2 独立变量和的母函数

定理4.5.3 设 $\xi, \eta$ 为相互独立的非负整数值随机变量，且分别有母函数 $g(s), h(s)$. 则 $\zeta := \xi + \eta$ 的母函数为 $f(s) := g(s)h(s)$.

证明 令 $p(i) = \mathbf{P}(\xi = i)$ 和 $q(j) = \mathbf{P}(\eta = j)$. 由离散卷积公式

$$
\mathbf {P} (\zeta = k) = \sum_ {i = 0} ^ {k} p (i) q (k - i).
$$

因此有

$$
\begin{array}{l} f (s) = \sum_ {k = 0} ^ {\infty} \mathbf {P} (\zeta = k) s ^ {k} = \sum_ {k = 0} ^ {\infty} \sum_ {i = 0} ^ {k} p (i) q (k - i) s ^ {k} \\ = \sum_ {i = 0} ^ {\infty} \sum_ {k = i} ^ {\infty} p (i) s ^ {i} q (k - i) s ^ {k - i} = \sum_ {i = 0} ^ {\infty} \sum_ {j = 0} ^ {\infty} p (i) s ^ {i} q (j) s ^ {j}. \\ \end{array}
$$

故得欲证结果.

例4.5.5 设随机变量 $\xi_{1}$ 和 $\xi_{2}$ 独立且分别服从二项分布 $B(k,p)$ 和 $B(n,p)$. 则 $\xi_{1}$ 和 $\xi_{2}$ 分别有母函数 $(q+ps)^{k}$ 和 $(q+ps)^{n}$. 根据定理4.5.3知 $\xi_{1}+\xi_{2}$ 的母函数为 $(q+ps)^{k+n}$. 再由定理4.5.1知 $\xi_{1}+\xi_{2}$ 服从二项分布 $B(k+n,p)$. 这给出了二项分布的再生性的简单证明. 类似地可以给出泊松分布的再生性的证明.

定理 4.5.4 设  $\{\xi_{i}\}$  为相互独立的非负整数值随机变量列，且有共同的母函数  $g(s)$ . 再设  $\eta$  为非负整数值随机变量，有母函数  $h(s)$  且与  $\{\xi_{i}\}$  独立. 则  $\xi := \xi_{1} + \xi_{2} + \cdots + \xi_{\eta}$  的母函数为  $f(s) = h(g(s))$ .

证明 根据定理 4.5.3, 对于  $n \geqslant 1$  随机变量  $\xi_{1} + \xi_{2} + \cdots + \xi_{n}$  有母函数  $g(s)^{n}$ . 根据全概率公式, 并利用  $\eta$  与  $\{\xi_{i}\}$  的独立性, 有

$$
\begin{array}{l} f (s) = \sum_ {k = 0} ^ {\infty} \mathbf {P} (\xi_ {1} + \xi_ {2} + \dots + \xi_ {\eta} = k) s ^ {k} \\ = \sum_ {k = 0} ^ {\infty} \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) \mathbf {P} (\xi_ {1} + \xi_ {2} + \dots + \xi_ {n} = k | \eta = n) s ^ {k} \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) \sum_ {k = 0} ^ {\infty} \mathbf {P} (\xi_ {1} + \xi_ {2} + \dots + \xi_ {n} = k) s ^ {k} \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) g (s) ^ {n} = h (g (s)). \\ \end{array}
$$

故得欲证结果.

例4.5.6 假设定理4.5.4中的随机变量都可积.则利用母函数与期望的关系易得

$$
\mathbf {E} \xi = f ^ {\prime} (1 -) = h ^ {\prime} (1 -) g ^ {\prime} (1 -) = \mathbf {E} \eta \mathbf {E} \xi_ {1}.
$$

这比例 4.4.3 中相应结果的证明简单了很多.

## 4.5.3 母函数的连续性定理

定理 4.5.5（连续性定理） 设对每个  $n \geqslant 1$  有数列  $\{a_{n}(i): i = 0, 1, 2, \cdots\} \subseteq [0, 1]$ ，并记其母函数为  $g_{n}$ 。则对每个  $i \geqslant 0$  极限  $a(i) := \lim_{n \to \infty} a_{n}(i)$  存在当且仅当对每个 0 < s < 1 极限  $g(s) := \lim_{n \to \infty} g_{n}(s)$  存在。此时 g 与  $\{a(i): i = 0, 1, 2, \cdots\}$  的母函数在区间 (0, 1) 内重合。

证明 设对每个  $i \geqslant 0$  极限  $a(i) := \lim_{n \to \infty} a_n(i)$  存在. 令 f 为  $\{a(i) : i = 0, 1, 2, \cdots\}$  的母函数. 由于  $|a_n(i) - a(i)| \leqslant 1$ , 对于 0 < s < 1 有

$$
\begin{array}{l} | g _ {n} (s) - f (s) | \leqslant \sum_ {i = 0} ^ {k} | a _ {n} (i) - a (i) | s ^ {i} + \sum_ {i = k + 1} ^ {\infty} | a _ {n} (i) - a (i) | s ^ {i} \\ \leqslant \sum_ {i = 0} ^ {k} | a _ {n} (i) - a (i) | + \frac {s ^ {k + 1}}{1 - s}. \\ \end{array}
$$

对任何 $\varepsilon > 0$, 可取充分大的 $N \geqslant 1$ 使当 $k \geqslant N$ 时有 $s^{k+1} / (1 - s) \leqslant \varepsilon$. 这样, 在上式两端取极限有 $\liminf_{n \to \infty} |g_n(s) - f(s)| \leqslant \varepsilon$. 这说明极限 $g(s) := \lim_{n \to \infty} g_n(s)$ 存在, 且 $g$ 与 $f$ 在区间 $(0,1)$ 内重合. 反之, 设对每个 $0 < s < 1$ 极限 $g(s) := \lim_{n \to \infty} g_n(s)$ 存在. 则函数 $g$ 在区间 $(0,1)$ 内单调不降, 故极限 $g(0) := \lim_{s \downarrow 0} g(s)$ 存在. 注意, 对 $0 < s < 1$ 有

$$
a _ {n} (0) \leqslant g _ {n} (s) \leqslant a _ {n} (0) + \sum_ {i = 1} ^ {\infty} s ^ {i} = a _ {n} (0) + \frac {s}{1 - s},
$$

从而

$$
g _ {n} (s) - \frac {s}{1 - s} \leqslant a _ {n} (0) \leqslant g _ {n} (s).
$$

因此有

$$
g (s) - \frac {s}{1 - s} \leqslant \operatorname * {l i m i n f} _ {n \to \infty} a _ {n} (0) \leqslant \operatorname * {l i m s u p} _ {n \to \infty} a _ {n} (0) \leqslant g (s).
$$

令 $s \downarrow 0$ 知 $\lim_{n \to \infty} a_n(0) = g(0) =: a_0$. 再利用假设, 对 $0 < s < 1$ 有

$$
\frac {1}{s} [ g _ {n} (s) - a _ {n} (0) ] = \sum_ {i = 0} ^ {\infty} a _ {n} (i + 1) s ^ {i} \rightarrow \frac {1}{s} [ g (s) - a _ {0} ] = \frac {1}{s} [ g (s) - g (0) ].
$$

与前面的推导类似, 可知导数 $g'(0)$ 存在且 $\lim_{n\to \infty}a_n(1) = g'(0) =: a(1)$. 利用数学归纳法可以证明每个 $i \geqslant 0$ 极限 $a(i) := \lim_{n\to \infty}a_n(i)$ 存在. 因此定理结论成立. □

作为定理 4.5.5 的特殊情况, 我们有

定理 4.5.6（连续性定理） 设对每个 $n \geqslant 1$ 有分布列 $\{p_n(i): i = 0,1,2,\cdots\}$，并记其母函数为 $g_n$。则存在分布列 $\{p(i): i = 0,1,2,\cdots\}$ 使对每个 $i \geqslant 0$ 有 $p(i) = \lim_{n \to \infty} p_n(i)$ 当且仅当对每个 $0 < s < 1$ 极限 $g(s) := \lim_{n \to \infty} g_n(s)$ 存在且 $\lim_{s \uparrow 1} g(s) = 1$。此时 $g$ 与 $\{p(i): i = 0,1,2,\cdots\}$ 的母函数在区间 $(0,1)$ 内重合。

例4.5.7 设数列 $\{p_n\} \subseteq [0,1]$ 满足 $\lim_{n\to \infty}np_n = \lambda >0$。则二项分布 $B(n,p_n)$ 的母函数为 $g_{n}(s) = [1 - p_{n}(1 - s)]^{n}$。对 $0 < s < 1$ 有

$$
\lim _ {n \to \infty} g _ {n} (s) = \lim _ {n \to \infty} \left\{\left[ 1 - p _ {n} (1 - s) \right] ^ {- 1 / p _ {n} (1 - s)} \right\} ^ {- n p _ {n} (1 - s)} = \mathrm{e} ^ {- \lambda (1 - s)}.
$$

上式右端是泊松分布 $P(\lambda)$ 的母函数. 根据定理4.5.5有

$$
\lim _ {n \to \infty} \mathrm{C} _ {n} ^ {i} (1 - p _ {n}) ^ {n - i} p _ {n} ^ {i} = \mathrm{e} ^ {- \lambda} \frac {\lambda^ {i}}{i !}.
$$

这就给出了定理 2.2.3 的一个简单证明.

## 练习题

1. 设某公共汽车站在时间区间  $[0, t]$  到来的乘客批数  $\eta(t)$  服从参数为  $\lambda t (\lambda > 0)$  的泊松分布，且第 k 批乘客的人数  $\xi_{k}$  服从分布  $\{p(i): i = 0, 1, \cdots\}$ . 再设随机变量  $\eta(t), \xi_{1}, \xi_{2}, \cdots$  相互独立. 求在时间区间  $[0, t]$  到来的乘客总数  $N(t)$  的母函数和数学期望.

2. 利用母函数方法求帕斯卡分布的期望和方差.

3. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且均服从几何分布  $G(p)$ . 用母函数方法证明  $\xi_{1} + \xi_{2} + \cdots + \xi_{n}$  服从帕斯卡分布  $Pa(n, p)$ .

4. 利用母函数方法给出泊松分布的再生性的证明.

5. 设 $g$ 为离散型概率分布 $\{p(i): i = 0,1,\dots\}$ 的母函数, 其中 $p(1) \neq 1$. 令 $g_1(z) = g(z)$ 并对 $n \geqslant 2$ 递推地定义 $g_n(z) = g_{n-1}(g(z))$. 证明: 对于任何 $0 \leqslant z < 1$ 极限 $q := \lim_{n \to \infty} g_n(z)$ 存在, 且该极限为方程 $z = g(z)$ 在区间 $[0,1]$ 的最小解.

## 第五章

## 特征函数

概率论中所说的随机变量或概率分布的特征函数就是分析学中的傅里叶 (Fourier) 变换, 它是研究随机变量的重要工具. 虽然特征函数不像随机变量的矩那样直观, 但它具有非常好的分析性质. 特征函数与其对应的分布函数相互唯一决定. 由于特征函数适用于任何概率分布, 它比母函数有更好的适用性. 特别是在各类概率极限定理的研究中, 特征函数扮演了不可或缺的角色. 本章分别介绍随机变量和随机向量的特征函数的概念、基本性质、反演公式, 以及非负随机变量的拉普拉斯 (Laplace) 变换, 并利用多元特征函数讨论了正态随机向量.

## 5.1 随机变量的特征函数

## 5.1.1 预备知识

我们知道, 每个复数都具有形式 $z = x + \mathrm{i}y$, 其中 $x, y \in \mathbb{R}$ 分别称为 $z$ 的实部和虚部, 而 $\mathrm{i} = \sqrt{-1}$ 是虚数单位, 满足 $\mathrm{i}^2 = -1$. 在此约定之下, 复数的运算规则与实数完全相同. 称 $\bar{z} := x - \mathrm{i}y$ 为 $z = x + \mathrm{i}y$ 的共轭数.

通常用 $\mathbb{C}$ 表示全体复数构成的集合, 称之为复平面. 直观上, 可以将 $z = x + iy \in \mathbb{C}$ 理解为复平面上的向量. 我们称

$$
| z | := \sqrt {z \bar {z}} = \sqrt {x ^ {2} + y ^ {2}}
$$

为 $z$ 的模或绝对值. 显然, 对任何 $z = x + \mathrm{i}y \in \mathbb{C}$ 有

$$
\left| x \right| \vee \left| y \right| \leqslant \left| z \right|. \tag {5.1.1}
$$

复变量函数的连续性和可微性可以与实变量函数类似地定义. 特别地, 复变量函数 $z \mapsto f(z)$ 在点 $\zeta \in \mathbb{C}$ 的导数定义为 (当右端极限存在时)

$$
f ^ {\prime} (\zeta) = \lim _ {z \to \zeta} \frac {f (z) - f (\zeta)}{z - \zeta}, \tag {5.1.2}
$$

其中 $z \to \zeta$ 意为 $|z - \zeta| \to 0$. 若分别用 $u$ 和 $v$ 表示 $f$ 的实部和虚部, 即 $f = u + \mathrm{i}v$, 则由 (5.1.2) 式可得

$$
f ^ {\prime} (\zeta) = u ^ {\prime} (\zeta) + \mathrm{i} v ^ {\prime} (\zeta).
$$

称 $\mathbb{C}$ 上的函数 $f$ 是解析的或全纯的, 是指它在每一点 $\zeta \in \mathbb{C}$ 的导数存在.

我们可以将熟悉的指数函数 $x \mapsto \mathrm{e}^x$ 的定义延拓到复平面, 得到一个复变函数, 该延拓由

$$
\mathrm{e} ^ {z} = \mathrm{e} ^ {x} (\cos y + \mathrm{i} \sin y), \quad z = x + \mathrm{i} y \in \mathbb {C} \tag {5.1.3}
$$

给出. 在 (5.1.3) 式中令 $x = 0$ 就得到欧拉公式

$$
\mathrm{e} ^ {\mathrm{i} y} = \cos y + \mathrm{i} \sin y, \quad y \in \mathbb {R}.
$$

命题 5.1.1 (泰勒展开式) 由 (5.1.3) 式定义的复变量指数函数可写为级数

$$
\mathrm{e} ^ {z} = \sum_ {n = 0} ^ {\infty} \frac {z ^ {n}}{n !}, \quad z \in \mathbb {C}.
$$

证明 写 $z = x + \mathrm{i}y$ 根据实变量三角函数的泰勒展开式, 有

$$
\sin y = \sum_ {k = 1} ^ {\infty} \frac {(- 1) ^ {k - 1} y ^ {2 k - 1}}{(2 k - 1) !}, \quad \cos y = \sum_ {k = 0} ^ {\infty} \frac {(- 1) ^ {k} y ^ {2 k}}{(2 k) !}.
$$

再由欧拉公式得

$$
\begin{array}{l} \mathrm{e} ^ {\mathrm{i} y} = \sum_ {k = 0} ^ {\infty} \frac {(- 1) ^ {k} y ^ {2 k}}{(2 k) !} + \mathrm{i} \sum_ {k = 1} ^ {\infty} \frac {(- 1) ^ {k - 1} y ^ {2 k - 1}}{(2 k - 1) !} \\ = \sum_ {k = 0} ^ {\infty} \frac {\mathrm{i} ^ {2 k} y ^ {2 k}}{(2 k) !} + \sum_ {k = 1} ^ {\infty} \frac {\mathrm{i} ^ {2 k - 1} y ^ {2 k - 1}}{(2 k - 1) !} = \sum_ {k = 0} ^ {\infty} \frac {(\mathrm{i} y) ^ {k}}{k !}. \\ \end{array}
$$

再利用实变量指数函数的泰勒展开式有

$$
\begin{array}{l} \mathrm{e} ^ {x + \mathrm{i} y} = \sum_ {j = 0} ^ {\infty} \frac {x ^ {j}}{j !} \sum_ {k = 0} ^ {\infty} \frac {(\mathrm{i} y) ^ {k}}{k !} = \sum_ {n = 0} ^ {\infty} \sum_ {j + k = n} \frac {x ^ {j} (\mathrm{i} y) ^ {k}}{j ! k !} \\ = \sum_ {n = 0} ^ {\infty} \frac {1}{n !} \sum_ {j + k = n} \frac {n !}{j ! k !} x ^ {j} (\mathrm{i} y) ^ {k} = \sum_ {n = 0} ^ {\infty} \frac {(x + \mathrm{i} y) ^ {n}}{n !}. \\ \end{array}
$$

故得欲证结果.

利用指数函数的定义式 (5.1.3) 或泰勒展开式, 不难证明下面的性质:

$$
\mathrm{e} ^ {z _ {1}} \mathrm{e} ^ {z _ {2}} = \mathrm{e} ^ {z _ {1} + z _ {2}}, \quad z _ {1}, z _ {2} \in \mathbb {C}.
$$

## 5.1.2 复随机变量的数学期望

基于实函数积分和实随机变量数学期望, 可以定义复随机变量的数学期望. 特别地, 给定概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的实随机变量 $\xi$ 和 $\eta$, 可以定义一个复随机变量 $\zeta = \xi + i\eta$. 若 $\xi$ 和 $\eta$ 均可积, 则称 $\zeta$ 可积并定义其数学期望为

$$
\mathbf {E} \zeta = \mathbf {E} \xi + \mathrm{i} \mathbf {E} \eta .
$$

很多关于复随机变量 $\zeta$ 的研究可以转化为讨论实随机向量 $(\xi, \eta)$. 例如, 复随机变量 $\zeta_1 = \xi_1 + \mathrm{i}\eta_1$ 与 $\zeta_2 = \xi_2 + \mathrm{i}\eta_2$ 独立当且仅当随机向量 $(\xi_1, \eta_1)$ 与 $(\xi_2, \eta_2)$ 独立. 此时对复平面上的任意有界博雷尔可测函数 $f$ 和 $g$ 有

$$
\mathbf {E} [ f (\zeta_ {1}) g (\zeta_ {2}) ] = \mathbf {E} [ f (\zeta_ {1}) ] \mathbf {E} [ g (\zeta_ {2}) ].
$$

命题5.1.2 若 $\xi, \eta \in L^2$，则 $|\mathbf{E}(\xi + \mathrm{i}\eta)| \leqslant \mathbf{E}(|\xi + \mathrm{i}\eta|)$.

证明 利用柯西-施瓦茨不等式得

$$
\begin{array}{l} (\mathbf {E} | \eta |) ^ {2} = \left\{\mathbf {E} \left[ \left(\sqrt {\xi^ {2} + \eta^ {2}}\right) ^ {2} - \xi^ {2} \right] ^ {1 / 2} \right\} ^ {2} \\ = \left\{\mathbf {E} \left[ \left(\sqrt {\xi^ {2} + \eta^ {2}} - \xi\right) ^ {1 / 2} \left(\sqrt {\xi^ {2} + \eta^ {2}} + \xi\right) ^ {1 / 2} \right] \right\} ^ {2} \\ \leqslant \mathbf {E} \left(\sqrt {\xi^ {2} + \eta^ {2}} - \xi\right) \mathbf {E} \left(\sqrt {\xi^ {2} + \eta^ {2}} + \xi\right) \\ = \left(\mathbf {E} \sqrt {\xi^ {2} + \eta^ {2}} - \mathbf {E} \xi\right) \left(\mathbf {E} \sqrt {\xi^ {2} + \eta^ {2}} + \mathbf {E} \xi\right) \\ = \left(\mathbf {E} \sqrt {\xi^ {2} + \eta^ {2}}\right) ^ {2} - (\mathbf {E} \xi) ^ {2}. \\ \end{array}
$$

由于 $(\mathbf{E}\eta)^2 = |\mathbf{E}\eta|^2 \leqslant (\mathbf{E}|\eta|)^2$ ，上式蕴涵

$$
(\mathbf {E} \xi) ^ {2} + (\mathbf {E} \eta) ^ {2} \leqslant \left(\mathbf {E} \sqrt {\xi^ {2} + \eta^ {2}}\right) ^ {2}.
$$

此即为欲证不等式.

□

## 5.1.3 特征函数的定义

定义 5.1.1 设欧氏空间  $(\mathbb{F}, \mathcal{B})$  上的有限测度  $\mu$  有分布函数 G. 则  $\mu$  和 G 的特征函数定义为

$$
f (t) = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t x} \mathrm{d} G (x) = \int_ {- \infty} ^ {\infty} \cos (t x) \mathrm{d} G (x) + \mathrm{i} \int_ {- \infty} ^ {\infty} \sin (t x) \mathrm{d} G (x), \tag {5.1.4}
$$

其中 $t \in \mathbb{R}$.

定义 5.1.2 设随机变量  $\xi$  有分布函数 F. 我们也称 F 的特征函数 f 为  $\xi$  的特征函数. 根据 (5.1.4) 式, 此时有

$$
f (t) := \mathbf {E} (\mathrm{e} ^ {\mathrm{i} t \xi}) = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t x} \mathrm{d} F (x), \quad t \in \mathbb {R}. \tag {5.1.5}
$$

例 5.1.1 若  $\xi$  是取值于  $\{x_{k}: k=1,2,\cdots\}$  离散型随机变量, 且有分布列  $p(x_{k})=\mathbf{P}(\xi=x_{k}), k=1,2,\cdots$ , 则其特征函数为

$$
f (t) = \sum_ {k = 1} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t x _ {k}} p (x _ {k}) = \sum_ {k = 1} ^ {\infty} \cos (t x _ {k}) p (x _ {k}) + \mathrm{i} \sum_ {k = 1} ^ {\infty} \sin (t x _ {k}) p (x _ {k}).
$$

例 5.1.2 若  $\xi$  是绝对连续型随机变量, 且有分布密度函数 p, 则其特征函数为

$$
f (t) = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t x} p (x) \mathrm{d} x = \int_ {- \infty} ^ {\infty} \cos (t x) p (x) \mathrm{d} x + \mathrm{i} \int_ {- \infty} ^ {\infty} \sin (t x) p (x) \mathrm{d} x.
$$

例5.1.3 若 $\xi$ 是非负整数值随机变量且有母函数 $g$. 若将 $g$ 理解为复变量函数, 则 $\xi$ 的特征函数可以表示为 $f(t) = g(\mathrm{e}^{\mathrm{i}t}), t \in \mathbb{R}$.

例5.1.4 对于 $0 \leqslant p \leqslant 1$, 伯努利分布 $B(1, p)$ 的特征函数为 $f(t) = 1 - p + p\mathrm{e}^{\mathrm{i}t}, t \in \mathbb{R}$.

例 5.1.5 对于  $\lambda \geqslant 0$ ，泊松分布  $\mathbf{P}(\lambda)$  的特征函数为

$$
f (t) = \mathrm{e} ^ {- \lambda} \sum_ {k = 0} ^ {\infty} \frac {\lambda^ {k}}{k !} \mathrm{e} ^ {\mathrm{i} t k} = \mathrm{e} ^ {- \lambda} \mathrm{e} ^ {\lambda \mathrm{e} ^ {\mathrm{i} t}} = \mathrm{e} ^ {\lambda (\mathrm{e} ^ {\mathrm{i} t} - 1)}, \quad t \in \mathbb {R}.
$$

例5.1.6 对于 $0 < p < 1$ ，几何分布 $G(p)$ 的特征函数为

$$
f (t) = \sum_ {k = 1} ^ {\infty} p (1 - p) ^ {k - 1} \mathrm{e} ^ {\mathrm{i} t k} = p \mathrm{e} ^ {\mathrm{i} t} \lim _ {n \to \infty} \sum_ {k = 1} ^ {n} (1 - p) ^ {k - 1} \mathrm{e} ^ {\mathrm{i} (k - 1) t}.
$$

易证

$$
\left[ 1 - (1 - p) \mathrm{e} ^ {\mathrm{i} t} \right] \sum_ {k = 1} ^ {n} (1 - p) ^ {k - 1} \mathrm{e} ^ {\mathrm{i} (k - 1) t} = 1 - (1 - p) ^ {n} \mathrm{e} ^ {\mathrm{i} n t}.
$$

注意

$$
\lim _ {n \to \infty} \left| (1 - p) ^ {n} \mathrm{e} ^ {\mathrm{i} n t} \right| = \lim _ {n \to \infty} (1 - p) ^ {n} = 0.
$$

所以

$$
f (t) = \lim _ {n \to \infty} \frac {p \mathrm{e} ^ {\mathrm{i} t} \left[ 1 - (1 - p) ^ {n} \mathrm{e} ^ {\mathrm{i} n t} \right]}{1 - (1 - p) \mathrm{e} ^ {\mathrm{i} t}} = \frac {p \mathrm{e} ^ {\mathrm{i} t}}{1 - (1 - p) \mathrm{e} ^ {\mathrm{i} t}}, \quad t \in \mathbb {R}.
$$

例5.1.7 对于 $a < b \in \mathbb{R}$, 均匀分布 $U(a, b)$ 的特征函数为

$$
\begin{array}{l} f (t) = \frac {1}{b - a} \left[ \int_ {a} ^ {b} \cos (t x) \mathrm{d} x + \mathrm{i} \int_ {a} ^ {b} \sin (t x) \mathrm{d} x \right] \\ = \frac {1}{b - a} \left[ \frac {1}{t} \sin (t x) \Big | _ {a} ^ {b} - \frac {\mathrm{i}}{t} \cos (t x) \Big | _ {a} ^ {b} \right] \\ = \frac {1}{(b - a) \mathrm{i} t} \left[ \mathrm{i} \sin (t x) \Big | _ {a} ^ {b} + \cos (t x) \Big | _ {a} ^ {b} \right] \\ = \frac {1}{(b - a) \mathrm{i} t} \mathrm{e} ^ {\mathrm{i} t x} \Big | _ {a} ^ {b} = \frac {1}{(b - a) \mathrm{i} t} (\mathrm{e} ^ {\mathrm{i} t b} - \mathrm{e} ^ {\mathrm{i} t a}). \\ \end{array}
$$

例5.1.8 设 $\xi$ 服从参数为 $\lambda > 0$ 的指数分布. 则其特征函数为

$$
f (t) = \lambda \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda x} \cos (t x) \mathrm{d} x + \mathrm{i} \lambda \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda x} \sin (t x) \mathrm{d} x =: \lambda (J _ {1} + \mathrm{i} J _ {2}),
$$

其中

$$
J _ {1} = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda x} \cos (t x) \mathrm{d} x, J _ {2} = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda x} \sin (t x) \mathrm{d} x.
$$

利用分部积分有

$$
J _ {1} = \frac {1}{t} \mathrm{e} ^ {- \lambda x} \sin (t x) \big | _ {0} ^ {\infty} + \frac {\lambda}{t} \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda x} \sin (t x) \mathrm{d} x
$$

和

$$
J _ {2} = - \frac {1}{t} \mathrm{e} ^ {- \lambda x} \cos (t x) \big | _ {0} ^ {\infty} - \frac {\lambda}{t} \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda x} \cos (t x) \mathrm{d} x.
$$

故有方程组

$$
J _ {1} = \frac {\lambda}{t} J _ {2}, \quad J _ {2} = \frac {1}{t} - \frac {\lambda}{t} J _ {1}.
$$

由此解得

$$
J _ {1} = \frac {\lambda}{\lambda^ {2} + t ^ {2}}, \quad J _ {2} = \frac {t}{\lambda^ {2} + t ^ {2}}.
$$

从而

$$
f (t) = \frac {\lambda (\lambda + \mathrm{i} t)}{\lambda^ {2} + t ^ {2}} = \frac {\lambda}{\lambda - \mathrm{i} t}.
$$

例5.1.9 若对满足 $a > 0$ 的复数 $c = a + \mathrm{i}b,$ 承认等式

$$
c \int_ {0} ^ {\infty} \mathrm{e} ^ {- c x} \mathrm{d} x = 1,
$$

则指数分布  $E(\lambda)$  的特征函数可通过下面的简单计算得到:

$$
f (t) = \lambda \int_ {0} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t x} \mathrm{e} ^ {- \lambda x} \mathrm{d} x = \lambda \int_ {0} ^ {\infty} \mathrm{e} ^ {- (\lambda - \mathrm{i} t) x} \mathrm{d} x = \frac {\lambda}{\lambda - \mathrm{i} t}.
$$

## 5.1.4 基本性质

命题 5.1.3 随机变量  $\xi$  的特征函数  $f(t)=f_{\xi}(t)=\mathbf{E}(\mathrm{e}^{\mathrm{i}t\xi})$  具有如下性质:

(1) 有界性: $|f(t)| \leqslant f(0) = 1$;
(2) 共轭对称性:  $f(-t)=\overline{f(t)}$ ;
(3) 线性变换的特征函数: 对任意的 $a, b \in \mathbb{R}$, 随机变量 $\eta := a + b\xi$ 的特征函数为 $f_{\eta}(t) = \mathrm{e}^{\mathrm{i}at} f_{\xi}(bt)$;
(4) 一致连续性: $f$ 在 $\mathbb{R}$ 上一致连续;
(5) 半正定: 对任意实数  $t_{1}, t_{2}, \cdots, t_{n}$  及复数  $a_{1}, a_{2}, \cdots, a_{n}$ ，有

$$
\sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {n} a _ {j} \bar {a} _ {k} f (t _ {j} - t _ {k}) \geqslant 0.
$$

证明 性质 (1), (2), (3) 显然成立. 下面证明 (4), (5).

(4) 对于 $\delta > 0$, 由 (5.1.5) 式和命题 5.1.2 有

$$
\begin{array}{l} | f (t + \delta) - f (t) | = \Big | \int_ {\mathbb {R}} [ \mathrm{e} ^ {\mathrm{i} (t + \delta) x} - \mathrm{e} ^ {\mathrm{i} t x} ] \mathrm{d} F (x) \Big | \\ \leqslant \int_ {- \infty} ^ {\infty} | \mathrm{e} ^ {\mathrm{i} (t + \delta) x} - \mathrm{e} ^ {\mathrm{i} t x} | \mathrm{d} F (x) \\ = \int_ {- \infty} ^ {\infty} | \mathrm{e} ^ {\mathrm{i} (t + \delta / 2) x} | | \mathrm{e} ^ {\mathrm{i} \delta x / 2} - \mathrm{e} ^ {- \mathrm{i} \delta x / 2} | \mathrm{d} F (x) \\ = \int_ {- \infty} ^ {\infty} 2 | \sin (\delta x / 2) | \mathrm{d} F (x). \\ \end{array}
$$

根据控制收敛定理, 当  $\delta \rightarrow 0$  时有

$$
\sup _ {t \in \mathbb {R}} | f (t + \delta) - f (t) | \leqslant \int_ {\mathbb {R}} 2 | \sin (\delta x / 2) | \mathrm{d} F (x) \to 0.
$$

(5) 由 (5.1.5) 式和命题 5.1.2 有

$$
\begin{array}{l} \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {n} a _ {j} \bar {a} _ {k} f (t _ {j} - t _ {k}) = \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {n} a _ {j} \bar {a} _ {k} \mathbf {E} \mathrm{e} ^ {\mathrm{i} (t _ {j} - t _ {k}) \xi} \\ = \mathbf {E} \Big (\sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {n} a _ {j} \bar {a} _ {k} \mathrm{e} ^ {\mathrm{i} t _ {j} \xi} \overline {{\mathrm{e} ^ {\mathrm{i} t _ {k} \xi}}} \Big) \\ = \mathbf {E} \left(\sum_ {j = 1} ^ {n} a _ {j} \mathrm{e} ^ {\mathrm{i} t _ {j} \xi} \cdot \overline {{\sum_ {k = 1} ^ {n} a _ {k} \mathrm{e} ^ {\mathrm{i} t _ {k} \xi}}}\right) \\ = \mathbf {E} \left(\left| \sum_ {j = 1} ^ {n} a _ {j} \mathrm{e} ^ {\mathrm{i} t _ {j} \xi} \right| ^ {2}\right) \geqslant 0. \\ \end{array}
$$

故得欲证结果.

## 练习题

1. 设  $\xi_{1}, \xi_{2}, \cdots$  为独立同分布随机变量且特征函数为  $f_{1}(t)$ ，而  $\eta$  是非负整数值随机变量，有母函数  $h(s)$  且与  $(\xi_{k})$  独立。求随机变量  $X := \xi_{1} + \xi_{2} + \cdots + \xi_{\eta}$  的特征函数  $f_{X}(t)$ 。

2. 参数为 $a \in \mathbb{R}$ 和 $\lambda > 0$ 的拉普拉斯分布的密度函数由

$$
p (x) = \frac {1}{2 \lambda} \mathrm{e} ^ {- | x - a | / \lambda}, \quad x \in \mathbb {R}
$$

给出. 求其特征函数, 并利用特征函数求其数学期望和方差.

3. 设随机变量 X 服从正态分布  $N(a, \sigma^{2})$ . 求  $X^{2}$  的特征函数.

4. 设随机变量 X 服从正态分布  $N(a, \sigma^{2})$ . 试用特征函数的方法求 X 的 3 阶及 4 阶中心矩.

5. 证明: 对于任何实值特征函数 $f(t)$, 以下两个不等式成立:

$$
1 - f (2 t) \leqslant 4 [ 1 - f (t) ]; \quad (2) 1 + f (2 t) \geqslant 2 f (t) ^ {2}. \tag {1}
$$

## 5.2 分布性质和反演公式

本节中我们应用特征函数研究随机变量的分布性质, 包括特征函数与矩的关系、特征函数的唯一性、分布的绝对连续性等. 唯一性的基本的想法是利用特征函数给出分布函数的表示, 也就是通常所说的反演公式.

## 5.2.1 特征函数与原点矩

随机变量的特征函数与其原点矩之间有密切的联系. 为讨论这种联系, 我们首先给出纯虚数变量指数函数的泰勒展开式余项的一个上界估计.

命题5.2.1 对任意 $x \in \mathbb{R}$ 及整数 $n \geqslant 1$ 有

$$
\left| \mathrm{e} ^ {\mathrm{i} x} - \sum_ {k = 0} ^ {n} \frac {(\mathrm{i} x) ^ {k}}{k !} \right| \leqslant \left(\frac {2 | x | ^ {n}}{n !}\right) \wedge \left(\frac {| x | ^ {n + 1}}{(n + 1) !}\right).
$$

证明 对 $x \in \mathbb{R}$ 令

$$
g _ {n} (x) = \mathrm{e} ^ {\mathrm{i} x} - \sum_ {k = 0} ^ {n} \frac {(\mathrm{i} x) ^ {k}}{k !} = \sum_ {k = n + 1} ^ {\infty} \frac {(\mathrm{i} x) ^ {k}}{k !}.
$$

求 $n + 1$ 次导数得

$$
\frac {\mathrm{d} ^ {n + 1}}{\mathrm{d} x ^ {n + 1}} g _ {n} (x) = \sum_ {k = n + 1} ^ {\infty} \frac {\mathrm{i} ^ {k} x ^ {k - n - 1}}{(k - n - 1) !} = \mathrm{i} ^ {n + 1} \mathrm{e} ^ {\mathrm{i} x}.
$$

所以有

$$
g _ {n} (x) = \int_ {0} ^ {x} \mathrm{d} t _ {1} \int_ {0} ^ {t _ {1}} \mathrm{d} t _ {2} \dots \int_ {0} ^ {t _ {n}} \mathrm{e} ^ {\mathrm{i} t _ {n + 1}} \mathrm{d} t _ {n + 1}
$$

和

$$
g _ {n} (x) = \int_ {0} ^ {x} \mathrm{d} t _ {1} \int_ {0} ^ {t _ {1}} \mathrm{d} t _ {2} \dots \int_ {0} ^ {t _ {n - 1}} \mathrm{i} ^ {- 1} (\mathrm{e} ^ {\mathrm{i} t _ {n}} - 1) \mathrm{d} t _ {n}.
$$

由此分别得

$$
\left| g _ {n} (x) \right| \leqslant \left| \int_ {0} ^ {x} \mathrm{d} t _ {1} \int_ {0} ^ {t _ {1}} \mathrm{d} t _ {2} \dots \int_ {0} ^ {t _ {n}} \mathrm{d} t _ {n + 1} \right| = \frac {| x | ^ {n + 1}}{(n + 1) !}
$$

和

$$
\left| g _ {n} (x) \right| \leqslant 2 \Big | \int_ {0} ^ {x} \mathrm{d} t _ {1} \int_ {0} ^ {t _ {1}} \mathrm{d} t _ {2} \dots \int_ {0} ^ {t _ {n - 1}} \mathrm{d} t _ {n} \Big | = \frac {2 | x | ^ {n}}{n !}.
$$

故得欲证估计.

定理5.2.2 令 $f(t) = \mathbf{E}(\mathrm{e}^{\mathrm{i}t\xi})$ 为随机变量 $\xi$ 的特征函数. 若 $\xi$ 有有限的 $n$ 阶矩, 则

$$
\left| \mathbf {E} (\mathrm{e} ^ {\mathrm{i} t \xi}) - \sum_ {k = 0} ^ {n} \frac {(\mathrm{i} t) ^ {k}}{k !} \mathbf {E} (\xi^ {k}) \right| \leqslant \mathbf {E} \Big [ \Big (\frac {2 | t \xi | ^ {n}}{n !} \Big) \wedge \Big (\frac {| t \xi | ^ {n + 1}}{(n + 1) !} \Big) \Big ].
$$

证明 首先注意

$$
\left| \mathbf {E} (\mathrm{e} ^ {\mathrm{i} t \xi}) - \sum_ {k = 0} ^ {n} \frac {(\mathrm{i} t) ^ {k}}{k !} \mathbf {E} (\xi^ {k}) \right| \leqslant \mathbf {E} \Big | \mathrm{e} ^ {\mathrm{i} t \xi} - \sum_ {k = 0} ^ {n} \frac {(\mathrm{i} t \xi) ^ {k}}{k !} \Big |.
$$

再应用命题 5.2.1 即得欲证的估计.

推论5.2.3 设随机变量 $\xi$ 的 $k$ 阶原点矩 $m_{k}$ 有限. 则其特征函数 $f$ 为 $k$ 阶可微且

$$
\frac {\mathrm{d} ^ {k} f}{\mathrm{d} t ^ {k}} (t) = \mathbf {E} \big [ (\mathrm{i} \xi) ^ {k} \mathrm{e} ^ {\mathrm{i} t \xi} \big ], \quad m _ {k} = \mathrm{i} ^ {- k} \frac {\mathrm{d} ^ {k} f}{\mathrm{d} t ^ {k}} (0).
$$

证明 取 $\delta \neq 0$ .注意

$$
\delta^ {- 1} [ f (t + \delta) - f (t) ] - \mathbf {E} \big (\mathrm{i} \xi \mathrm{e} ^ {\mathrm{i} t \xi} \big) = \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} t \xi} \delta^ {- 1} (\mathrm{e} ^ {\mathrm{i} \delta \xi} - 1 - \mathrm{i} \delta \xi) \big ]. \tag {5.2.1}
$$

由命题5.2.1知

$$
\left| \mathrm{e} ^ {\mathrm{i} t \xi} \delta^ {- 1} (\mathrm{e} ^ {\mathrm{i} \delta \xi} - 1 - \mathrm{i} \delta \xi) \right| \leqslant (2 | \xi |) \land (2 ^ {- 1} | \xi | ^ {2} | \delta |) \leqslant 2 | \xi |.
$$

根据定理 4.2.20, 有

$$
\lim _ {\delta \to 0} \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} t \xi} \delta^ {- 1} (\mathrm{e} ^ {\mathrm{i} \delta \xi} - 1 - \mathrm{i} \delta \xi) \big ] = 0.
$$

再由 (5.2.1) 式得 $f'(t) = \mathbf{E}(\mathrm{i}\xi \mathrm{e}^{\mathrm{i}t\xi})$. 这就证明了 $k = 1$ 的情况. 应用数学归纳法, 通过类似的计算可得一般情况.

推论 5.2.4 令  $f(t)=\mathbf{E}(\mathrm{e}^{\mathrm{i}t\xi})$  为随机变量  $\xi$  的特征函数. 则下面两个性质等价:

(1) $f(t)$ 有展开式

$$
f (t) = \sum_ {k = 0} ^ {\infty} \frac {(\mathrm{i} t) ^ {k}}{k !} \mathbf {E} (\xi^ {k})
$$

且等号右端的级数绝对收敛;

(2) $\xi$ 的各阶矩有限且

$$
\lim _ {k \to \infty} \frac {| t | ^ {k}}{k !} \mathbf {E} (| \xi | ^ {k}) = 0.
$$

例 5.2.1 设  $\xi$  服从正态分布  $N(0,1)$ . 求其特征函数 f.

解 由例4.3.9, 对任意整数 $r \geqslant 1$, 有

$$
\mathbf {E} (\xi^ {2 r - 1}) = 0, \quad \mathbf {E} (\xi^ {2 r}) = (2 r - 1)!!,
$$

则

$$
\lim _ {r \to \infty} \frac {| t | ^ {2 r} \mathbf {E} | \xi | ^ {2 r}}{(2 r) !} = \lim _ {r \to \infty} \frac {| t | ^ {2 r}}{(2 r) ! !} = \lim _ {r \to \infty} \frac {| t | ^ {2 r}}{2 ^ {r} r !} = 0.
$$

作积分变量替换 $x = \sqrt{2t}$ 可得

$$
\begin{array}{l} \mathbf {E} | \xi | ^ {2 r + 1} = \sqrt {\frac {2}{\pi}} \int_ {0} ^ {\infty} x ^ {2 r + 1} \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{d} x = \sqrt {\frac {2}{\pi}} \int_ {0} ^ {\infty} 2 ^ {r} t ^ {r} \mathrm{e} ^ {- t} \mathrm{d} t \\ = \sqrt {\frac {2}{\pi}} 2 ^ {r} \Gamma (r + 1) = \sqrt {\frac {2}{\pi}} (2 r)!!, \\ \end{array}
$$

于是有

$$
\lim _ {r \to \infty} \frac {| t | ^ {2 r + 1} \mathbf {E} | \xi | ^ {2 r + 1}}{(2 r + 1) !} = \lim _ {r \to \infty} \sqrt {\frac {2}{\pi}} \frac {| t | ^ {2 r + 1}}{(2 r + 1) ! !} = 0.
$$

从而推论 5.2.4 的条件满足, 故

$$
f (t) = \sum_ {r = 0} ^ {\infty} \frac {(\mathrm{i} t) ^ {2 r}}{(2 r) !} (2 r - 1)!! = \sum_ {r = 0} ^ {\infty} \frac {(- t ^ {2}) ^ {r}}{2 ^ {r} r !} = \mathrm{e} ^ {- t ^ {2} / 2}.
$$

## 5.2.2 反演公式与唯一性

引理5.2.5 对任意的 $\alpha \in \mathbb{R}$ 有

$$
\big | \int_ {0} ^ {T} \frac {\sin (\alpha t)}{t} \mathrm{d} t \big | \leqslant 4, \quad T \geqslant 0,
$$

并且

$$
\lim _ {T \to \infty} \int_ {0} ^ {T} \frac {\sin (\alpha t)}{t} \mathrm{d} t = \frac {\pi}{2} \mathrm{sgn} (\alpha), \tag {5.2.2}
$$

其中

$$
\operatorname{sgn} (\alpha) = \left\{ \begin{array}{l l} 1, & \alpha > 0, \\ 0, & \alpha = 0, \\ - 1, & \alpha <   0. \end{array} \right.
$$

证明 作积分变量替换可得

$$
\int_ {0} ^ {T} \frac {\sin (\alpha t)}{t} \mathrm{d} t = \operatorname{sgn} (\alpha) \int_ {0} ^ {T} \frac {\sin | \alpha | t}{t} \mathrm{d} t = \operatorname{sgn} (\alpha) \int_ {0} ^ {| \alpha | T} \frac {\sin u}{u} \mathrm{d} u.
$$

注意 $|\sin u| \leqslant |u|$，再利用分部积分公式可得

$$
\begin{array}{l} \left| \int_ {0} ^ {T} \frac {\sin (\alpha t)}{t} \mathrm{d} t \right| \leqslant \left| \int_ {0} ^ {1} \frac {\sin u}{u} \mathrm{d} u \right| + \left| \int_ {1} ^ {| \alpha | T} \frac {\sin u}{u} \mathrm{d} u \right| \\ \leqslant 1 + \left| \frac {\cos u}{u} \right| _ {1} ^ {| \alpha | T} + \left| \int_ {1} ^ {| \alpha | T} \frac {\cos u}{u ^ {2}} \mathrm{d} u \right| \\ \leqslant 3 + \int_ {1} ^ {| \alpha | T} \frac {1}{u ^ {2}} \mathrm{d} u \leqslant 4. \\ \end{array}
$$

由数学分析中的狄利克雷积分知

$$
\int_ {0} ^ {\infty} \frac {\sin t}{t} \mathrm{d} t = \frac {\pi}{2};
$$

参见 [5, p.514]. 所以 (5.2.2) 式成立.

定理5.2.6 设随机变量 $\xi$ 有特征函数 $f$. 则对任何 $a < b \in \mathbb{R}$ 有

$$
\begin{array}{l} \lim _ {c \to \infty} \frac {1}{2 \pi} \int_ {- c} ^ {c} \frac {\mathrm{e} ^ {- \mathrm{i} t a} - \mathrm{e} ^ {- \mathrm{i} t b}}{\mathrm{i} t} f (t) \mathrm{d} t \\ = \mathbf {P} (a <   \xi <   b) + \frac {1}{2} \big [ \mathbf {P} (\xi = a) + \mathbf {P} (\xi = b) \big ]. \tag {5.2.3} \\ \end{array}
$$

特别地, 若 a, b 均为  $\xi$  的分布函数的连续点, 则有

$$
\mathbf {P} (a <   \xi <   b) = \lim _ {c \to \infty} \frac {1}{2 \pi} \int_ {- c} ^ {c} \frac {\mathrm{e} ^ {- \mathrm{i} t a} - \mathrm{e} ^ {- \mathrm{i} t b}}{\mathrm{i} t} f (t) \mathrm{d} t.
$$

证明 根据命题 5.1.3, 特征函数 f 在全实轴上一致连续. 另外, 显然我们可将

$$
h (t) := \frac {\mathrm{e} ^ {- \mathrm{i} t a} - \mathrm{e} ^ {- \mathrm{i} t b}}{\mathrm{i} t}
$$

延拓为全实轴上的有界连续函数. 故对 $c > 0$ 可定义

$$
J (c) = \frac {1}{2 \pi} \int_ {- c} ^ {c} \frac {\mathrm{e} ^ {- \mathrm{i} t a} - \mathrm{e} ^ {- \mathrm{i} t b}}{\mathrm{i} t} f (t) \mathrm{d} t.
$$

交换积分和期望的次序 (承认这是允许的) 得

$$
\begin{array}{l} J (c) = \frac {1}{2 \pi} \int_ {- c} ^ {c} \mathbf {E} \left(\frac {\mathrm{e} ^ {- \mathrm{i} t a} - \mathrm{e} ^ {- \mathrm{i} t b}}{\mathrm{i} t} \mathrm{e} ^ {\mathrm{i} t \xi}\right) \mathrm{d} t \\ = \frac {1}{2 \pi} \mathbf {E} \left(\int_ {- c} ^ {c} \frac {\mathrm{e} ^ {\mathrm{i} t (\xi - a)} - \mathrm{e} ^ {\mathrm{i} t (\xi - b)}}{\mathrm{i} t} \mathrm{d} t\right) \\ = \frac {1}{\pi} \mathbf {E} \left(\int_ {0} ^ {c} \frac {\sin [ t (\xi - a) ] - \sin [ t (\xi - b) ]}{t} \mathrm{d} t\right). \\ \end{array}
$$

根据引理5.2.5有

$$
\left| \int_ {0} ^ {c} \frac {\sin [ t (\xi - a) ] - \sin [ t (\xi - b) ]}{t} \mathrm{d} t \right| \leqslant 8
$$

并且

$$
\begin{array}{l} \lim _ {c \to \infty} \int_ {0} ^ {c} \frac {\sin [ t (\xi - a) ] - \sin [ t (\xi - b) ]}{t} \mathrm{d} t \\ = \frac {\pi}{2} [ \operatorname{sgn} (\xi - a) - \operatorname{sgn} (\xi - b) ] \\ = \pi 1 _ {(a, b)} (\xi) + \frac {\pi}{2} \left[ 1 _ {\{a \}} (\xi) + 1 _ {\{b \}} (\xi) \right]. \\ \end{array}
$$

应用有界收敛定理得

$$
\begin{array}{l} \lim _ {c \to \infty} J (c) = \frac {1}{\pi} \mathbf {E} \left\{\pi 1 _ {(a, b)} (\xi) + \frac {\pi}{2} \left[ 1 _ {\{a \}} (\xi) + 1 _ {\{b \}} (\xi) \right] \right\} \\ = \mathbf {P} (a <   \xi <   b) + \frac {1}{2} \big [ \mathbf {P} (\xi = a) + \mathbf {P} (\xi = b) \big ]. \\ \end{array}
$$

此即欲证结论.

定理 5.2.7（唯一性） 随机变量的分布函数与其特征函数相互唯一决定.

证明 显然特征函数由其分布函数唯一决定. 反之, 设 $F$ 为随机变量 $\xi$ 的分布函数. 令 $C_F$ 和 $D_F$ 分别表示 $F$ 的连续点集和跳跃点集. 则 $D_F$ 至多可数, 故 $C_F$ 在 $\mathbb{R}$ 上稠密. 由定理5.2.6知, 对任意的 $a \leqslant b \in C_F$, 增量 $F(b) - F(a)$ 由特征函数 $f$ 唯一决定. 取数列 $\{a_n\} \subseteq C_F$ 满足 $a_n \to -\infty$. 对于 $x \in \mathbb{R}$ 可取数列 $\{b_n\} \subseteq C_F$ 满足 $b_n \downarrow x$. 由 $F$ 的右连续性, 有

$$
F (x) = \lim _ {n \to \infty} F (b _ {n}) = \lim _ {n \to \infty} \big [ F (b _ {n}) - F (a _ {n}) \big ].
$$

这说明分布函数 F 由特征函数 f 唯一决定.

我们称 (5.2.3) 式为特征函数的反演公式. 从定理 5.2.7 的证明不难看出, 此公式给出了一种由随机变量的特征函数确定其分布函数的方式.

## 5.2.3 绝对连续性条件

利用特征函数可以给出概率分布函数绝对连续性的一个简单的判据, 同时给出其密度函数的表示.

定理 5.2.8 若特征函数 f 模可积, 则对应的分布函数 F 是绝对连续型的且有连续的密度函数

$$
p (x) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} t x} f (t) \mathrm{d} t, \quad x \in \mathbb {R}.
$$

证明 对任意 $a, b \in \mathbb{R}$ 有

$$
\begin{array}{l} \mathrm{e} ^ {\mathrm{i} a} - \mathrm{e} ^ {\mathrm{i} b} = \mathrm{e} ^ {\mathrm{i} (a + b) / 2} [ \mathrm{e} ^ {\mathrm{i} (a - b) / 2} - \mathrm{e} ^ {\mathrm{i} (b - a) / 2} ] \\ = 2 \mathrm{ie} ^ {\mathrm{i} (a + b) / 2} \sin [ (a - b) / 2 ], \\ \end{array}
$$

故得

$$
| \mathrm{e} ^ {\mathrm{i} a} - \mathrm{e} ^ {\mathrm{i} b} | = 2 | \sin [ (a - b) / 2 ] | \leqslant | b - a |. \tag {5.2.4}
$$

若 $a, b$ 均为 $F$ 的连续点, 则由反演公式有

$$
\begin{array}{l} | F (b) - F (a) | = \lim _ {c \to \infty} \frac {1}{2 \pi} \bigg | \int_ {- c} ^ {c} \frac {\mathrm{e} ^ {- \mathrm{i} t a} - \mathrm{e} ^ {- \mathrm{i} t b}}{\mathrm{i} t} f (t) \mathrm{d} t \bigg | \\ \leqslant \lim _ {c \to \infty} \frac {1}{2 \pi} \int_ {- c} ^ {c} \left| \frac {\mathrm{e} ^ {- \mathrm{i} t a} - \mathrm{e} ^ {- \mathrm{i} t b}}{\mathrm{i} t} f (t) \right| \mathrm{d} t \\ \leqslant \frac {| b - a |}{2 \pi} \int_ {- \infty} ^ {\infty} | f (t) | \mathrm{d} t. \\ \end{array}
$$

由此可知 $F$ 在 $\mathbb{R}$ 上连续. 设 $x, \delta \in \mathbb{R}$ 且 $\delta \neq 0$. 再次利用反演公式得

$$
\begin{array}{l} \frac {F (x + \delta) - F (x)}{\delta} = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \frac {\mathrm{e} ^ {- \mathrm{i} t x} - \mathrm{e} ^ {- \mathrm{i} t (x + \delta)}}{\mathrm{i} t \delta} f (t) \mathrm{d} t \\ = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} t x} \frac {1 - \mathrm{e} ^ {- \mathrm{i} t \delta}}{\mathrm{i} t \delta} f (t) \mathrm{d} t. \tag {5.2.5} \\ \end{array}
$$

应用欧拉公式和三角公式得

$$
1 - \mathrm{e} ^ {- \mathrm{i} t \delta} = 1 - \cos (t \delta) + \mathrm{i} \sin (t \delta) = 2 \sin^ {2} (t \delta / 2) + \mathrm{i} \sin (t \delta),
$$

故有

$$
\lim _ {\delta \to 0} (1 - \mathrm{e} ^ {- \mathrm{i} t \delta}) (\mathrm{i} t \delta) ^ {- 1} = 1.
$$