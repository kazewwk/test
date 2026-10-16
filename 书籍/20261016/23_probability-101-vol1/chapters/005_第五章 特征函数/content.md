# 第五章 特征函数

原始 PDF 第 148–171 页。

## 第五章

## 特征函数

---

134

第五章 特征函数

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

---

5.1 随机变量的特征函数

135

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

---

136

第五章 特征函数

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

---

5.1 随机变量的特征函数

137

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

---

138

第五章 特征函数

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

---

5.1 随机变量的特征函数

139

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

---

140

第五章 特征函数

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

---

5.2 分布性质和反演公式

141

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

---

142

第五章 特征函数

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

---

5.2 分布性质和反演公式

143

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

---

144

第五章 特征函数

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

---

5.2 分布性质和反演公式

145

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

---

146

第五章 特征函数

这样, 对 (5.2.5) 式应用控制收敛定理得

$$
F ^ {\prime} (x) = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} t x} f (t) \lim _ {\delta \to 0} \frac {1 - \mathrm{e} ^ {- \mathrm{i} t \delta}}{\mathrm{i} t \delta} \mathrm{d} t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {- \mathrm{i} t x} f (t) \mathrm{d} t.
$$

所以 $F$ 是绝对连续型分布函数, 且具有所给的密度函数 $p(x)$. 再次应用控制收敛定理可知 $p(x)$ 为连续函数. $\square$

## 练习题

1. 称随机变量 $\xi$ 是对称的, 是指对于任何 $x \geqslant 0$ 有 $\mathbf{P}(\xi \geqslant x) = \mathbf{P}(\xi \leqslant -x)$. 证明 $\xi$ 为对称随机变量当且仅当其特征函数 $f_{\xi}$ 为实值偶函数.
2. 设非负数列  $\{r_{1}, r_{2}, \cdots\}$  满足  $\sum_{k=1}^{\infty} r_{k} = 1$ . 证明  $f(t) = \sum_{k=1}^{\infty} r_{k} \cos(kt)$  是某个概率分布的特征函数, 并给出此概率分布.
3. 设 $\mathbb{R}$ 上的概率分布函数 $F$ 有特征函数 $f$. 证明对任何 $x \in \mathbb{R}$ 有

$$
\lim _ {T \to \infty} \frac {1}{2 T} \int_ {- T} ^ {T} \mathrm{e} ^ {- \mathrm{i} t x} f (t) \mathrm{d} t = F (x) - F (x -).
$$

提示: 注意

$$
\frac {1}{2 T} \int_ {- T} ^ {T} \mathrm{e} ^ {- \mathrm{i} t x} f (t) \mathrm{d} t = \int_ {- \infty} ^ {\infty} g _ {T} (x, y) \mathrm{d} F (y),
$$

其中

$$
g _ {T} (x, y) = \frac {1}{T} \int_ {0} ^ {T} \cos [ t (y - x) ] \mathrm{d} t \rightarrow 1 _ {\{x = y \}}, \quad T \rightarrow \infty .
$$

4. 设 $X$ 为绝对连续型随机变量。令 $f(t)$ 为其特征函数。证明当 $t \to \infty$ 时有 $f(t) \to 0$.

提示: 称为泊松引理. 利用一致连续性和模可积性.

5. 设 $\mathbb{R}$ 上的概率分布函数 $F$ 有特征函数 $f$. 对于 $n \geqslant 1$ 令

$$
F _ {n} (x) = \frac {n}{2} \int_ {x - 1 / n} ^ {x + 1 / n} F (y) \mathrm{d} y, \quad x \in \mathbb {R}.
$$

(1) 证明每个 $F_{n}$ 都是绝对连续型概率分布函数;
(2) 证明当 $n \to \infty$ 时对 $F$ 的任何连续点 $x \in \mathbb{R}$ 有 $F_{n}(x) \to F(x)$;
(3) 求 $F_{n}$ 的特征函数 $f_{n}$, 并证明当 $n \to \infty$ 时对一切 $t \in \mathbb{R}$ 有 $f_{n}(t) \to f(t)$.

---

5.3 多元特征函数

147

## 5.3 多元特征函数

## 5.3.1 定义和基本性质

定义 5.3.1 设  $\xi=(\xi_{1},\xi_{2},\cdots,\xi_{d})$  是定义在概率空间  $(\Omega,\mathcal{F},\mathbf{P})$  上的 d 维随机向量，且有联合分布函数 F. 我们称

$$
f (t) := \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \langle t, \xi \rangle}) = \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} (t _ {1} \xi_ {1} + t _ {2} \xi_ {2} + \dots + t _ {n} \xi_ {n})} \big ], \quad t = (t _ {1}, t _ {2}, \dots , t _ {d}) \in \mathbb {R} ^ {d}
$$

为  $\xi$  或 F 的特征函数, 这里  $\langle t, \xi \rangle = t_{1}\xi_{1} + t_{2}\xi_{2} + \cdots + t_{n}\xi_{n}$  表示内积. 为了强调, 有时也称 f 为多元特征函数.

利用随机向量的特征函数可以容易地得到其分量的特征函数, 这就是

命题 5.3.1 令 f 为随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  的特征函数. 则对  $1 \leqslant k \leqslant d$  分量  $\xi_{k}$  的特征函数为

$$
f _ {k} (t _ {k}) = f (0, \dots , t _ {k}, \dots , 0), \quad t _ {k} \in \mathbb {R}.
$$

上式右端 $f$ 的第 $k$ 个变量取 $t_k$ 而其余的变量全部取零.

多元特征函数有着与一元特征函数类似的性质. 下面的命题和定理的证明可模仿一元情况给出, 这里省略.

命题 5.3.2 随机向量  $\xi=(\xi_{1},\xi_{2},\cdots,\xi_{d})$  的特征函数 f 具有如下性质:

(1) 有界性:  $|f(t)| = |f(t_{1}, t_{2}, \cdots, t_{d})| \leqslant f(0) = f(0, 0, \cdots, 0) = 1;$
(2) 共轭对称性:  $f(-t_{1}, -t_{2}, \cdots, -t_{d}) = \overline{f(t_{1}, t_{2}, \cdots, t_{d})}$ ;
(3) 线性变换的特征函数: 对于 $a \in \mathbb{R}$ 和 $b \in \mathbb{R}^d$, 随机变量 $\eta := a + \langle b, \xi \rangle$ 的特征函数为

$$
f _ {\eta} (t) = \mathrm{e} ^ {\mathrm{i} a t} f (b t) = \mathrm{e} ^ {\mathrm{i} a t} f (b _ {1} t, b _ {2} t, \dots , b _ {d} t), \quad t \in \mathbb {R}.
$$

(4) 一致连续性: $f$ 在 $\mathbb{R}^d$ 上一致连续;
(5) 与矩的关系: 若随机变量  $\xi_{1}^{k_{1}}\xi_{2}^{k_{2}}\cdots\xi_{d}^{k_{d}}$  可积, 则

$$
\mathbf {E} \big (\xi_ {1} ^ {k _ {1}} \xi_ {2} ^ {k _ {2}} \dots \xi_ {d} ^ {k _ {d}} \big) = \mathrm{i} ^ {- k} \frac {\partial^ {k} f}{\partial t _ {1} ^ {k _ {1}} \partial t _ {2} ^ {k _ {2}} \cdots \partial t _ {d} ^ {k _ {d}}} (0, 0, \dots , 0),
$$

其中  $k = k_{1} + k_{2} + \cdots + k_{d}.$

定理 5.3.3（反演公式）设 d 维随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  有特征函数 f. 对于  $1 \leqslant k \leqslant d$  用  $C_{F_{k}}$  表示分量  $\xi_{k}$  的边缘分布函数  $F_{k}$  的连续点集，并取  $a_{k} \leqslant b_{k} \in C_{F_{k}}$ . 则有

$$
\mathbf {P} \big (a _ {1} <   \xi_ {1} <   b _ {1}, a _ {2} <   \xi_ {2} <   b _ {2}, \dots , a _ {d} <   \xi_ {d} <   b _ {d} \big)
$$

---

148

第五章 特征函数

$$
= \lim _ {c \to \infty} \frac {1}{(2 \pi) ^ {d}} \int_ {[ - c, c ] ^ {d}} \Big (\prod_ {k = 1} ^ {d} \frac {\mathrm{e} ^ {- \mathrm{i} t _ {k} a _ {k}} - \mathrm{e} ^ {- \mathrm{i} t _ {k} b _ {k}}}{\mathrm{i} t _ {k}} \Big) f (t) \mathrm{d} t.
$$

定理 5.3.4（唯一性定理） 随机向量的联合分布函数由其特征函数唯一决定.

## 5.3.2 独立性条件

由独立随机变量构成的随机向量的特征函数具有非常简单的结构. 事实上, 下面的定理给出了有限个随机变量相互独立的充要条件.

定理 5.3.5 设随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  有特征函数 f. 则  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  相互独立当且仅当

$$
f (t) = f _ {1} (t _ {1}) f _ {2} (t _ {2}) \dots f _ {d} (t _ {d}), \quad t = (t _ {1}, t _ {2}, \dots , t _ {d}) \in \mathbb {R} ^ {d}, \tag {5.3.1}
$$

其中  $f_{k}$  表示分量  $\xi_{k}$  的特征函数.

证明 假设  $\xi_{1},\xi_{2},\cdots,\xi_{d}$  相互独立. 则  $e^{it\xi_{1}},e^{it\xi_{2}},\cdots,e^{it\xi_{d}}$  相互独立. 因此

$$
f (t) = \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} (t _ {1} \xi_ {1} + t _ {2} \xi_ {2} + \dots + t _ {d} \xi_ {d})} \big ] = \mathbf {E} (\mathrm{e} ^ {\mathrm{i} t _ {1} \xi_ {1}}) \mathbf {E} (\mathrm{e} ^ {\mathrm{i} t _ {2} \xi_ {2}}) \dots \mathbf {E} (\mathrm{e} ^ {\mathrm{i} t _ {d} \xi_ {d}}) = f _ {1} (t _ {1}) f _ {2} (t _ {2}) \dots f _ {d} (t _ {d}).
$$

反之，假设(5.3.1)式成立.设 $x = (x_{1}, x_{2}, \dots, x_{d}) \in \mathbb{R}^{d}$.对于 $1 \leqslant k \leqslant d$ 可取 $a_{k,n} \leqslant b_{k,n} \in C_{F_k}$ 使当 $n \to \infty$ 时有 $a_{k,n} \downarrow -\infty$ 且 $b_{k,n} \downarrow x_k$.由反演公式和(5.3.1)式易得

$$
\begin{array}{l} \mathrm{P} \left(a _ {1, n} <   \xi_ {1} <   b _ {1, n}, a _ {2, n} <   \xi_ {2} <   b _ {2, n}, \dots , a _ {d, n} <   \xi_ {d} <   b _ {d, n}\right) \\ = \lim _ {c \to \infty} \frac {1}{(2 \pi) ^ {d}} \int_ {[ - c, c ] ^ {d}} \Big (\prod_ {k = 1} ^ {d} \frac {\mathrm{e} ^ {- \mathrm{i} t _ {k} a _ {k , n}} - \mathrm{e} ^ {- \mathrm{i} t _ {k} b _ {k , n}}}{\mathrm{i} t _ {k}} \Big) f (t) \mathrm{d} t \\ = \lim _ {c \to \infty} \frac {1}{(2 \pi) ^ {d}} \int_ {[ - c, c ] ^ {d}} \left[ \prod_ {k = 1} ^ {d} \frac {\mathrm{e} ^ {- \mathrm{i} t _ {k} a _ {k , n}} - \mathrm{e} ^ {- \mathrm{i} t _ {k} b _ {k , n}}}{\mathrm{i} t _ {k}} f _ {k} (t _ {k}) \right] \mathrm{d} t \\ = \lim _ {c \to \infty} \frac {1}{(2 \pi) ^ {d}} \prod_ {k = 1} ^ {d} \int_ {[ - c, c ]} \left[ \frac {\mathrm{e} ^ {- \mathrm{i} t _ {k} a _ {k , n}} - \mathrm{e} ^ {- \mathrm{i} t _ {k} b _ {k , n}}}{\mathrm{i} t _ {k}} f _ {k} (t _ {k}) \right] \mathrm{d} t _ {k} \\ = \mathbf {P} \big (a _ {1, n} <   \xi_ {1} <   b _ {1, n} \big) \mathbf {P} (a _ {2, n} <   \xi_ {2} <   b _ {2, n}) \dots \mathbf {P} \big (a _ {d, n} <   \xi_ {d} <   b _ {d, n} \big). \\ \end{array}
$$

在上式两端令 $n\to \infty$ 得

$$
F (x _ {1}, x _ {2}, \dots , x _ {d}) = F _ {1} (x _ {1}) F _ {2} (x _ {2}) \dots F _ {d} (x _ {d}).
$$

由此知  $\xi_{1},\xi_{2},\cdots,\xi_{d}$  相互独立.

![](../../raw/pages_0161-0176/images/page_162_image_16.jpg)

---

5.3 多元特征函数

149

## 5.3.3 独立和的特征函数

定理 5.3.6 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  相互独立. 对  $1 \leqslant k \leqslant d$  用  $f_{k}$  表示分量  $\xi_{k}$  的特征函数. 令  $\eta = \xi_{1} + \xi_{2} + \cdots + \xi_{d}$ . 则

$$
f _ {\eta} (t) = f _ {1} (t) f _ {2} (t) \dots f _ {d} (t), \quad t \in \mathbb {R}. \tag {5.3.2}
$$

证明 用  $f_{\xi}$  表示随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  的特征函数. 则对任意  $t \in R$  有

$$
f _ {\eta} (t) = \mathbf {E} [ \mathrm{e} ^ {\mathrm{i} t (\xi_ {1} + \xi_ {2} + \dots + \xi_ {d})} ] = \mathbf {E} [ \mathrm{e} ^ {\mathrm{i} (t \xi_ {1} + t \xi_ {2} + \dots + t \xi_ {d})} ] = f _ {\xi} (t, t, \dots , t).
$$

由定理 5.3.5 即得欲证结论.

在定理 5.3.6 的情况下, 令  $\mu_{1}, \mu_{2}, \cdots, \mu_{d}$  分别为随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  的分布, 称  $\eta = \xi_{1} + \xi_{2} + \cdots + \xi_{d}$  的分布  $\mu$  为  $\mu_{1}, \mu_{2}, \cdots, \mu_{d}$  的卷积, 并记作  $\mu = \mu_{1} * \mu_{2} * \cdots * \mu_{d}$ . 类似地, 令  $F_{1}, F_{2}, \cdots, F_{d}$  分别为随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  的分布函数, 称  $\eta = \xi_{1} + \xi_{2} + \cdots + \xi_{d}$  的分布函数 F 为  $F_{1}, F_{2}, \cdots, F_{d}$  的多重卷积, 并记作  $F = F_{1} * F_{2} * \cdots * F_{d}$ . 根据定理 5.2.7 和定理 5.3.6, 卷积  $\mu$  和 F 由其特征函数 (5.3.2) 式唯一决定.

定理5.3.7 给定 $\mathbb{R}$ 上的概率分布函数 $F, G,$ 令 $H = F * G.$ 则

$$
H (x) = \int_ {- \infty} ^ {\infty} G (x - z) \mathrm{d} F (z), \quad x \in \mathbb {R}. \tag {5.3.3}
$$

证明 令 $H$ 由 (5.3.3) 式定义. 则对任意 $t \in \mathbb{R}$ 有

$$
\begin{array}{l} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t x} \mathrm{d} H (x) = \int_ {- \infty} ^ {\infty} \mathrm{d} F (z) \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t x} \mathrm{d} G (x - z) \\ = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t z} \mathrm{d} F (z) \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t x} \mathrm{d} G (x). \\ \end{array}
$$

由定理 5.3.5 即知  $H = F * G$ .

积分表达式 (5.3.3) 称为卷积公式. 该定义也用于 $F, G$ 为 $\mathbb{R}$ 上的任意有界分布函数的情况.

例 5.3.1 假设  $\xi,\eta$  独立且均服从泊松分布  $P(\lambda)$ . 则有  $f_{\xi}(t)=f_{\eta}(t)=\mathrm{e}^{\lambda(\mathrm{e}^{\mathrm{i}t}-1)}$ . 由  $\xi,\eta$  的独立性, 有

$$
f _ {\xi + \eta} (t) = f _ {\xi} (t) f _ {\eta} (t) = \mathrm{e} ^ {2 \lambda (\mathrm{e} ^ {\mathrm{i} t} - 1)}.
$$

再根据唯一性定理知  $\xi + \eta$  服从分布  $P(2\lambda)$ .

例 5.3.2 利用定理 5.3.6 及二项分布与伯努利分布的关系, 可得二项分布  $B(n,p)$  的特征函数为  $f(t)=(1-p+pe^{it})^{n}$ .

定理5.3.8 假设 $g$ 是母函数, 而 $f$ 是特征函数. 则 $g(f(t))$ 也是一个特征函数.

---

150

第五章 特征函数

证明 设  $\eta, \xi_{1}, \xi_{2}, \cdots$  为独立随机变量, 其中  $\eta$  只取非负整数值且有母函数 g, 而  $\xi_{1}, \xi_{2}, \cdots$  同分布且有特征函数 f. 再令  $X = \sum_{k=1}^{\eta} \xi_{k}$ . 利用全期望公式和定理 5.3.6 得

$$
\begin{array}{l} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} t X}) = \mathbf {E} \Big (\exp \left\{\mathrm{i} t \sum_ {k = 1} ^ {\eta} \xi_ {k} \right\} \Big) \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) \mathbf {E} \left(\exp \left\{\mathrm{i} t \sum_ {k = 1} ^ {\eta} \xi_ {k} \right\} \mid \eta = n\right) \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) \mathbf {E} \left(\exp \left\{\mathrm{i} t \sum_ {k = 1} ^ {n} \xi_ {k} \right\} \mid \eta = n\right) \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) \mathbf {E} \left(\exp \left\{\mathrm{i} t \sum_ {k = 1} ^ {n} \xi_ {k} \right\}\right) \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = n) f (t) ^ {n} = g (f (t)). \\ \end{array}
$$

所以  $g(f(t))$  是 X 的特征函数.

![](../../raw/pages_0161-0176/images/page_164_image_5.jpg)

推论 5.3.9 若 f 是特征函数, 则对任意  $\lambda \geqslant 0$  函数  $e^{\lambda[f(t)-1]}$  也是特征函数.

证明 令 $\eta$ 服从泊松分布 $P(\lambda)$. 则它有母函数 $g(z) = \mathrm{e}^{\lambda (z - 1)}$. 再应用命题5.3.8即得欲证结论. □

## \*5.3.4 拉普拉斯变换

特征函数涉及复值函数的积分, 有时会带来一些处理上的不便. 对于非负随机变量, 有一种简便和常用的变换, 即拉普拉斯变换, 它可以作为特征函数的替代工具.

定义 5.3.2 设  $\xi=(\xi_{1},\xi_{2},\cdots,\xi_{d})$  是取值于  $R_{+}^{d}$  的随机向量，且有联合分布函数 F. 我们称

$$
L (t) := \mathbf {E} (\mathrm{e} ^ {- \langle t, \xi \rangle}) = \mathbf {E} \big [ \mathrm{e} ^ {- (t _ {1} \xi_ {1} + t _ {2} \xi_ {2} + \dots + t _ {n} \xi_ {n})} \big ], \quad t = (t _ {1}, t _ {2}, \dots , t _ {d}) \in \mathbb {R} _ {+} ^ {d}
$$

为  $\xi$  或 F 的拉普拉斯变换, 这里  $\langle t, \xi \rangle = t_{1}\xi_{1} + t_{2}\xi_{2} + \cdots + t_{n}\xi_{n}$  表示内积.

拉普拉斯变换本质上是特征函数的特殊情况. 若分别用 $L$ 和 $f$ 表示取值于 $\mathbb{R}_+^d$ 的随机向量 $\xi$ 的拉普拉斯变换和特征函数, 则形式上有

$$
L (t) = f (\mathrm{i} t), \quad t = (t _ {1}, t _ {2}, \dots , t _ {d}) \in \mathbb {R} ^ {d}.
$$

对于拉普拉斯变换, 我们不加证明地给出如下的定理.

定理 5.3.10（唯一性定理） 取值于  $R_{+}^{d}$  的随机向量的联合分布函数由其拉普拉斯变换唯一决定.

---

5.3 多元特征函数

151

定理 5.3.11 设取值于  $R_{+}^{d}$  的随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  有拉普拉斯变换 L. 则  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  相互独立当且仅当

$$
L (t) = L _ {1} (t _ {1}) L _ {2} (t _ {2}) \dots L _ {d} (t _ {d}), \quad t = (t _ {1}, t _ {2}, \dots , t _ {d}) \in \mathbb {R} _ {+} ^ {d},
$$

其中  $L_{k}$  表示分量  $\xi_{k}$  的拉普拉斯变换.

定理 5.3.12 设非负随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  相互独立. 对  $1 \leqslant k \leqslant d$ , 用  $L_{k}$  表示分量  $\xi_{k}$  的特征函数. 则  $\eta := \xi_{1} + \xi_{2} + \cdots + \xi_{d}$  的拉普拉斯变换为

$$
L _ {\eta} (t) = L _ {1} (t) L _ {2} (t) \dots L _ {d} (t), \quad t \in \mathbb {R} _ {+}. \tag {5.3.4}
$$

例5.3.3 伽马分布 $\Gamma (\lambda ,r)$ 的拉普拉斯变换为

$$
L (t) = \frac {\lambda^ {r}}{\Gamma (r)} \int_ {0} ^ {\infty} x ^ {r - 1} \mathrm{e} ^ {- (\lambda + t) x} \mathrm{d} x = \frac {\lambda^ {r}}{(\lambda + t) ^ {r}}.
$$

因此, 若独立随机变量 $\xi_{1}$ 和 $\xi_{2}$ 分别服从分布 $\Gamma(\lambda, r_{1})$ 和 $\Gamma(\lambda, r_{2})$, 则 $\xi_{1} + \xi_{2}$ 服从分布 $\Gamma(\lambda, r_{1} + r_{2})$.

关于拉普拉斯变换的更多的讨论, 可以参阅 [7,8,11].

## 练习题

1. 设随机向量 $(\xi, \eta)$ 服从二维正态分布 $N(a_{1}, a_{2}; \sigma^{2}, \sigma^{2}; r)$. 证明

$$
\mathbf {E} (\xi \vee \eta) = \sqrt {\frac {1 - r}{\pi}}.
$$

2. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且均服从  $N(0,1)$ . 记

$$
X = \sum_ {k = 1} ^ {n} a _ {k} \xi_ {k}, \quad Y = \sum_ {k = 1} ^ {n} b _ {k} \xi_ {k},
$$

证明 $X$ 与 $Y$ 独立的充要条件为 $\sum_{k=1}^{n} a_k b_k = 0$.

3. 设随机向量  $(\xi,\eta)$  服从  $N(a_{1},a_{2};\sigma_{1}^{2},\sigma_{2}^{2};r)$ . 记

$$
U = a \xi + b \eta , \quad V = c \xi + d \eta .
$$

(1) 求 U 与 V 的数学期望, 方差及相关系数;
(2) 写出 $(U, V)$ 的分布;
(3) 在何种情况下  $(U, V)$  的分布退化为一维分布?
(4) 在何种情况下 U 与 V 独立?

---

152

第五章 特征函数

4. 伽马分布 $\Gamma(\lambda, r)$ 的密度函数为

$$
p (x) = \frac {\lambda^ {r}}{\Gamma (r)} x ^ {r - 1} \mathrm{e} ^ {- \lambda x}, \quad x > 0.
$$

对满足 a > 0 的复数  $c = a + ib$ ，承认如下等式成立:

$$
c ^ {r} \int_ {0} ^ {\infty} x ^ {r - 1} \mathrm{e} ^ {- c x} \mathrm{d} x = \Gamma (r).
$$

求  $\Gamma(\lambda,r)$  的特征函数.

5. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且均服从指数分布  $E(\lambda)$ . 证明  $\xi_{1} + \xi_{2} + \cdots + \xi_{n}$  服从伽马分布  $\Gamma(\lambda, n)$ .
6. 设  $\xi_{1}, \xi_{2}, \cdots$  是某个概率空间上的随机变量序列，且对任何  $n \geqslant 1$  随机向量  $(\xi_{1}, \xi_{2}, \cdots, \xi_{n})$  和  $\xi_{n+1}$  独立。证明  $\xi_{1}, \xi_{2}, \cdots$  相互独立。

## \*5.4 正态随机向量

本节讨论多维正态随机向量, 多元特征函数的工具在这里发挥了关键作用. 后面提到的正态分布允许是退化的.

## 5.4.1 多维正态分布

定理5.4.1 设 $a \in \mathbb{R}^d$ 是 $d$ 维行向量, 而 $B$ 是 $d$ 阶正定矩阵. 对于 $x \in \mathbb{R}^d$, 令

$$
p (x) = \frac {1}{(2 \pi) ^ {d / 2} | B | ^ {1 / 2}} \exp \Big \{- \frac {1}{2} \big \langle (x - a) B ^ {- 1}, x - a \big \rangle \Big \}. \tag {5.4.1}
$$

则 $p$ 为 $\mathbb{R}^d$ 上的分布密度函数, 且相应的特征函数为

$$
f (t) = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t B, t \rangle \right\}, \quad x \in \mathbb {R} ^ {d}.
$$

证明 由于 $B$ 正定, 存在可逆矩阵 $A$ 使得 $B = A^{\mathrm{T}}A$. 令 $y = (x - a)A^{-1}$, 则 $x = a + yA$. 容易计算该变换的雅可比行列式为

$$
\left| \frac {\mathrm{d} x}{\mathrm{d} y} \right| = | A | = | B | ^ {1 / 2}.
$$

所以

$$
\int_ {\mathbb {R} ^ {d}} p (x) \mathrm{d} x = \frac {1}{(2 \pi) ^ {d / 2}} \int_ {\mathbb {R} ^ {d}} \exp \Big \{- \frac {1}{2} \langle y, y \rangle \Big \} \mathrm{d} y
$$

---

\*5.4 正态随机向量

153

$$
= \prod_ {k = 1} ^ {d} \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} \exp \left\{- \frac {1}{2} y _ {k} ^ {2} \right\} \mathrm{d} y _ {k} = 1,
$$

故 $p$ 为 $\mathbb{R}^d$ 上的分布密度函数. 对应的特征函数为

$$
\begin{array}{l} f (t) = \int_ {\mathbb {R} ^ {d}} \exp \{\mathrm{i} \langle t, x \rangle \} p (x) \mathrm{d} x \\ = \frac {1}{(2 \pi) ^ {d / 2}} \int_ {\mathbb {R} ^ {d}} \exp \left\{\mathrm{i} \langle t, a + y A \rangle - \frac {1}{2} \langle y, y \rangle \right\} \mathrm{d} y \\ = \exp \{\mathrm{i} \langle t, a \rangle \} \frac {1}{(2 \pi) ^ {d / 2}} \int_ {\mathbb {R} ^ {d}} \exp \left\{\mathrm{i} t (y A) ^ {\mathrm{T}} - \frac {1}{2} \langle y, y \rangle \right\} \mathrm{d} y \\ = \exp \left\{\mathrm{i} \langle t, a \rangle \right\} \frac {1}{(2 \pi) ^ {d / 2}} \int_ {\mathbb {R} ^ {d}} \exp \left\{\mathrm{i} t A ^ {\mathrm{T}} y ^ {\mathrm{T}} - \frac {1}{2} \langle y, y \rangle \right\} \mathrm{d} y \\ = \exp \{\mathrm{i} \langle a, t \rangle \} \frac {1}{(2 \pi) ^ {d / 2}} \int_ {\mathbb {R} ^ {d}} \exp \left\{\mathrm{i} \langle s, y \rangle - \frac {1}{2} \langle y, y \rangle \right\} \mathrm{d} y, \\ \end{array}
$$

其中 $s = tA^{\mathrm{T}}$ 利用一维标准正态分布的特征函数的表达式得

$$
\begin{array}{l} f (t) = \exp \{\mathrm{i} \langle a, t \rangle \} \prod_ {k = 1} ^ {d} \frac {1}{(2 \pi) ^ {1 / 2}} \int_ {- \infty} ^ {\infty} \exp \left\{i s _ {k} y _ {k} - \frac {1}{2} y _ {k} ^ {2} \right\} \mathrm{d} y _ {k} \\ = \exp \{\mathrm{i} \langle a, t \rangle \} \prod_ {k = 1} ^ {d} \exp \left\{- \frac {1}{2} s _ {k} ^ {2} \right\} \\ = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle s, s \rangle \right\} \\ = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t A ^ {\mathrm{T}}, t A ^ {\mathrm{T}} \rangle \right\} \\ = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} t A ^ {\mathrm{T}} A t ^ {\mathrm{T}} \right\} \\ = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t B, t \rangle \right\}. \\ \end{array}
$$

故 p 具有所给的特征函数.

定义 5.4.1 设  $a \in R^{d}$ ，而 B 为 d 阶半正定矩阵。我们称特征函数

$$
f (t) = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t B, t \rangle \right\}, \quad t \in \mathbb {R} ^ {d} \tag {5.4.2}
$$

所对应的 $\mathbb{R}^d$ 上的概率分布为 $d$ 维正态分布, 并记作 $N(a, B)$. 当 $B$ 退化时, 称 $N(a, B)$ 为退化 $d$ 维正态分布.

令 $I$ 为 $d$ 阶单位矩阵. 若 $B$ 为 $d$ 阶半正定矩阵, 则 $B_{n} := B + I / n$ 为 $d$ 阶正定矩阵, 且当 $n \to \infty$ 时有 $\langle tB_{n}, t \rangle \to \langle tB, t \rangle$. 令 $f_{n}$ 是将 (5.4.2) 式中的 $B$ 换为 $B_{n}$ 后所定义的函数. 由定理 5.4.1 知 $f_{n}$ 是 $\mathbb{R}^{d}$ 上的某个绝对连续型概率分布的特征函数. 据此, 利用后面将要学习的莱维连续性定理的多维形式可知, $f$ 的确是 $\mathbb{R}^{d}$ 上的某个概率分布的特征函数. 下面我们给出 $d$ 维正态分布的若干性质.

---

154

第五章 特征函数

## 5.4.2 子向量的分布

定理 5.4.2 设随机向量  $\xi=(\xi_{1},\xi_{2},\cdots,\xi_{d})$  服从 d 维正态分布  $N(a,B)$ ，而  $1\leqslant k_{1}<k_{2}<\cdots<k_{n}\leqslant d$ 。则  $\xi$  的子向量  $\eta=(\xi_{k_{1}},\xi_{k_{2}},\cdots,\xi_{k_{n}})$  服从 n 维正态分布  $N(b,C)$ ，其中 b 是由 a 的第  $k_{1},k_{2},\cdots,k_{n}$  个分量构成的子向量，而 C 是由矩阵 B 的第  $k_{1},k_{2},\cdots,k_{n}$  行和列构成的子矩阵。

证明 令 $s = (s_1, s_2, \cdots, s_n) \in \mathbb{R}^n$, 并令 $t = (t_1, t_2, \cdots, t_d) \in \mathbb{R}^d$ 是第 $k_1, k_2, \cdots, k_n$ 个分量由 $s$ 的分量给出且其他分量为零的 $d$ 维向量. 则

$$
\mathbf {E} \exp \{\mathrm{i} \langle \eta , s \rangle \} = \mathbf {E} \exp \{\mathrm{i} \langle \xi , t \rangle \} = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t B, t \rangle \right\},
$$

其中 $\langle a, t \rangle = \langle b, s \rangle$ 而 $\langle tB, t \rangle = \langle sC, s \rangle$. 因此 $\eta$ 服从分布 $N(b, C)$.

定理5.4.3 设随机向量 $\xi$ 服从 $d$ 维正态分布 $N(a, B)$. 则有 $a = \mathbf{E}\xi$ 和 $B = \operatorname{Var}\xi$.

证明 写  $a=(a_{1},a_{2},\cdots,a_{d})$  和  $B=(b_{kj})_{d\times d}$ . 对子向量  $\xi_{k}$  应用定理 5.4.2 知  $\xi_{k}$  服从正态分布  $N(a_{k},b_{kk})$ ，故有  $a_{k}=\mathbf{E}(\xi_{k})$  和  $b_{kk}=\mathbf{Var}(\xi_{k})$ . 再对子向量  $(\xi_{j},\xi_{k})$  应用定理 5.4.2 得

$$
\mathbf {E} \exp \{\mathrm{i} s _ {1} \xi_ {j} + \mathrm{i} s _ {2} \xi_ {k} \} = \exp \left\{\mathrm{i} a _ {j} s _ {1} + \mathrm{i} a _ {k} s _ {2} - \frac {b _ {j j} s _ {1} ^ {2}}{2} - \frac {b _ {k k} s _ {2} ^ {2}}{2} - b _ {j k} s _ {1} s _ {2} \right\}.
$$

在上式两端求 $s_1 = s_2 = 0$ 处的偏导数得 $\mathbf{E}(\xi_j\xi_k) = a_ja_k + b_{jk}$，故有 $b_{jk} = \mathbf{Cov}(\xi_j,\xi_k)$

定理 5.4.4 设随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  服从 d 维正态分布  $N(a, B)$ . 则  $\xi$  的 d 个分量相互独立当且仅当  $B = Var\xi$  为对角矩阵.

证明 “$\Rightarrow$” 设 $\xi$ 的分量相互独立. 则这些分量两两不相关, 故 $\mathbf{Cov}(\xi_j, \xi_k) = 0$ 对所有 $1 \leqslant j < k \leqslant d$ 成立, 即 $B$ 为对角矩阵.

“$\Leftarrow$”设 $B$ 为对角矩阵. 则 $\xi$ 的特征函数是其 $d$ 个分量的特征函数之积. 由定理5.3.5知这些分量相互独立. □

显然, 在定理 5.4.4 的情况下, $\xi$ 非退化当且仅当 $B = \operatorname{Var} \xi$ 的主对角线元素均严格正.

## 5.4.3 线性变换

定理5.4.5 设 $d$ 维随机向量 $\xi$ 服从分布 $N(a, B)$, 而 $C$ 为 $d \times n$ 矩阵. 则 $n$ 维随机向量 $\eta := \xi C$ 服从分布 $N(aC, C^{\mathrm{T}}BC)$.

证明 对于任意的  $s=(s_{1},s_{2},\cdots,s_{n})\in\mathbb{R}^{n}$ ，我们有

$$
\mathbf {E} \exp \{\mathrm{i} \langle \eta , s \rangle \} = \mathbf {E} \exp \{\mathrm{i} \langle \xi C, s \rangle \} = \exp \left\{\mathrm{i} \langle a C, s \rangle - \frac {1}{2} s C ^ {\mathrm{T}} B C s ^ {\mathrm{T}} \right\}.
$$

---

\*5.4 正态随机向量

155

因此 $\eta$ 服从分布 $N(aC, C^{\mathrm{T}}BC)$.

定理5.4.6 设 $\xi$ 服从分布 $N(a, B)$. 则存在正交矩阵 $C$ 使 $\eta := \xi C$ 的所有分量相互独立.

证明 由矩阵论的结果, 存在正交矩阵 $C$ 使 $C^{\mathrm{T}}BC$ 为对角矩阵. 由定理5.4.4和定理5.4.5知 $\eta$ 的分量相互独立. □

定理5.4.7 随机向量 $\xi$ 服从 $d$ 维正态分布当且仅当对任意的 $s \in \mathbb{R}^d$ 线性组合 $\langle \xi, s \rangle$ 服从一维正态分布.

证明 “$\Rightarrow$” 设 $\xi$ 服从 $d$ 维正态分布 $N(a, B)$. 由定理 5.4.5 知 $\langle \xi, s \rangle$ 服从一维正态分布.

“$\Leftarrow$”设 $\xi = (\xi_1, \xi_2, \cdots, \xi_d)$ 是 $d$ 维随机向量，且对任意的 $s \in \mathbb{R}^d$ 线性组合 $\langle \xi, s \rangle$ 服从一维正态分布。则 $\xi$ 的分量 $\xi_1, \xi_2, \cdots, \xi_d$ 均服从一维正态分布，故它们都是平方可积的。令 $a = (a_1, a_2, \cdots, a_d)$ 和 $B = (b_{jk})_{d \times d}$，其中 $a_j = \mathbf{E}(\xi_j)$ 而 $b_{jk} = \mathbf{Cov}(\xi_j, \xi_k)$。则对 $t \in \mathbb{R}^d$，线性组合 $\eta := \langle \xi, t \rangle$ 有期望 $\langle a, t \rangle$ 和方差 $\langle tB, t \rangle$。再由假定知 $\eta$ 服从一维正态分布 $N(\langle a, t \rangle, \langle tB, t \rangle)$。所以 $\eta$ 有特征函数

$$
f _ {\eta} (s) = \mathbf {E} \exp \{\mathrm{i} s \langle \xi , t \rangle \} = \exp \left\{\mathrm{i} s \langle a, t \rangle - \frac {1}{2} s ^ {2} \langle t B, t \rangle \right\}, \quad s \in \mathbb {R}.
$$

在上式中取 $s = 1$ 知 $\xi$ 有特征函数

$$
f (t) = \mathbf {E} \exp \{\mathrm{i} \langle \xi , t \rangle \} = \exp \left\{\mathrm{i} \langle a, t \rangle - \frac {1}{2} \langle t B, t \rangle \right\}, \quad t \in \mathbb {R} ^ {d}.
$$

这说明  $\xi$  服从 d 维正态分布  $N(a,B)$ .

例5.4.1 设 $\xi, \eta$ 相互独立且均服从正态分布 $N(0,1)$. 令

$$
\zeta = \left\{ \begin{array}{l l} | \eta |, & \xi \geqslant 0, \\ - | \eta |, & \xi <   0. \end{array} \right.
$$

由  $\xi,\eta$  的独立性, 我们有

$$
\begin{array}{l} F _ {\zeta} (x) = \mathbf {P} (\zeta \leqslant x, \xi \geqslant 0) + \mathbf {P} (\zeta \leqslant x, \xi <   0) \\ = \mathbf {P} (| \eta | \leqslant x, \xi \geqslant 0) + \mathbf {P} (- | \eta | \leqslant x, \xi <   0) \\ = \frac {1}{2} \mathbf {P} (| \eta | \leqslant x) + \frac {1}{2} \mathbf {P} (| \eta | \geqslant - x). \\ \end{array}
$$

不论 $x > 0$ 或 $x \leqslant 0$, 均有 $F_{\zeta}(x) = \Phi(x)$, 故 $\zeta$ 服从分布 $N(0,1)$.

例 5.4.2 在上例中, 随机变量  $\xi, \zeta$  均服从正态分布  $N(0,1)$ . 特别地, 有  $\mathbf{P}(\xi \geqslant 0) = \mathbf{P}(\xi < 0) = 1/2$ . 再由  $\xi, \eta$  的独立性,

$$
\mathbf {P} (\eta \geqslant 0 | \xi \geqslant 0) = \mathbf {P} (\eta <   0 | \xi \geqslant 0)
$$

---

156

第五章 特征函数

$$
\begin{array}{l} = \mathbf {P} (\eta \geqslant 0 | \xi <   0) \\ = \mathbf {P} (\eta <   0 | \xi <   0) = 1 / 2. \\ \end{array}
$$

这样, 根据全概率公式,

$$
\begin{array}{l} \mathbf {P} (\zeta + \eta = 0) = \mathbf {P} (\xi \geqslant 0) \mathbf {P} (\zeta + \eta = 0 | \xi \geqslant 0) + \mathbf {P} (\xi <   0) \mathbf {P} (\zeta + \eta = 0 | \xi <   0) \\ = \mathbf {P} (\xi \geqslant 0) \mathbf {P} (\eta <   0 | \xi \geqslant 0) + \mathbf {P} (\xi <   0) \mathbf {P} (\eta \geqslant 0 | \xi <   0) = 1 / 2. \\ \end{array}
$$

所以线性组合 $\zeta +\eta$ 不服从一维正态分布.这说明随机向量 $(\eta ,\zeta)$ 不服从二维正态分布，故两个一维正态分布随机变量并不一定构成一个二维正态分布随机向量.

## 练习题

1. 设随机向量 $\xi = (\xi_1, \xi_2)$ 服从二维正态分布 $N(a, B)$, 其中 $B = \begin{pmatrix} \sigma^2 & r\sigma^2 \\ r\sigma^2 & \sigma^2 \end{pmatrix}$. 证明 $\eta_1 = \xi_1 + \xi_2$ 与 $\eta_2 = \xi_1 - \xi_2$ 独立.
2. 设随机向量 $(\xi_1, \xi_2)$ 服从二维正态分布 $N(a, B)$, 其中 $B = \begin{pmatrix} \sigma_1^2 & r\sigma_1\sigma_2 \\ r\sigma_1\sigma_2 & \sigma_2^2 \end{pmatrix}$. 求 $\xi_1 + \xi_2$ 的密度函数.
3. 设随机向量 $(\xi_1, \xi_2, \xi_3)$ 服从三维正态分布 $N(a, B)$, 其中 $B = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$. 证明 $\xi_1$ 与 $\xi_2$ 不独立, 但 $(\xi_1, \xi_2)$ 与 $\xi_3$ 独立.
4. 设随机向量  $(\xi_{1}, \xi_{2}, \cdots, \xi_{n})$  服从 n 维正态分布. 证明对任何常数  $b_{1}, b_{2}, \cdots, b_{n}, x$  有  $\mathbf{P}(b_{1}\xi_{1} + b_{2}\xi_{2} + \cdots + b_{n}\xi_{n} = x) = 0$  或 1.
5. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  独立且均服从正态分布  $N(a, \sigma^{2})$ . 定义  $\eta_{1} = \sum_{i=1}^{n} \alpha_{i} \xi_{i}$  和  $\eta_{2} = \sum_{i=1}^{n} \beta_{i} \xi_{i}$ , 其中  $\alpha_{i}$  和  $\beta_{i}$  为实常数且满足  $\sum_{i=1}^{n} \alpha_{i} \beta_{i} = 0$ . 证明  $\eta_{1}$  与  $\eta_{2}$  独立且均服从正态分布.
