# 第三章 随机向量和独立性

原始 PDF 第 78–105 页。

## 第三章

## 随机向量和独立性

---

64

第三章 随机向量和独立性

在随机现象的描述中, 我们经常需要同时考虑多个随机变量. 将多个随机变量组合起来, 就得到了随机向量, 也称为多维或高维随机变量. 从抽象的角度看, 随机向量与随机变量都是可测函数, 后者的分布是多维欧氏空间上的概率测度, 有更丰富的结构和性质. 本章介绍随机向量的联合分布、边缘分布、条件分布与独立性、随机向量的函数等基本概念和性质, 并分别讨论离散型和绝对连续型随机向量的典型例子.

## 3.1 随机向量与联合分布

对于随机向量, 经常需要研究它们的联合与边缘分布. 为此我们首先对 $d$ 维欧氏空间上的有限测度及其分布函数做简单的介绍.

## 3.1.1 多维分布函数

称 $\mathbb{R}^2$ 上的函数 $G$ 为分布函数, 是指存在欧氏可测空间 $(\mathbb{R}^2, \mathcal{B}^2)$ 上的局部有限测度 $\mu$ 满足: 任何矩形 $(a, b] \times (c, d] \subseteq \mathbb{R}^2$ 有

$$
G (b, d) - G (a, d) - G (b, c) + G (a, c) = \mu ((a, b ] \times (c, d ]). \tag {3.1.1}
$$

此时也称 $G$ 是 $\mu$ 的分布函数. 不难证明下面的命题:

命题 3.1.1 二维欧氏可测空间  $(\mathbb{R}^{2}, \mathcal{B}^{2})$  上的局部有限测度  $\mu$  的分布函数 G 具有性质:

(1) $G$ 右连续且在任何矩形 $(a,b]\times (c,d]\subseteq \mathbb{R}^2$ 上有非负增量，即

$$
\Delta G ((a, b ] \times (c, d ]) := G (b, d) - G (a, d) - G (b, c) + G (a, c) \geqslant 0; \tag {3.1.2}
$$

(2) $G$ 有界当且仅当 $\mu$ 是有限测度, 且此时有

$$
\mu (\mathbb {R} ^ {2}) = G (\infty , \infty) - G (- \infty , - \infty); \tag {3.1.3}
$$

(3) 若 $G$ 是 $\mu$ 的分布函数, 则 $G + c$ 也是 $\mu$ 的分布函数, 其中 $c$ 为常数.

例3.1.1 对于 $(x,y)\in \mathbb{R}^2$ 令 $F(x,y) = 1$ 若 $x + y\geqslant 1$; $F(x,y) = 0$ 若 $x + y < 1$. 则函数 $F(x,y)$ 关于 $x$ 和 $y$ 都是不降的, 但命题3.1.1的条件(1)不满足. 因此 $F$ 不是 $\mathbb{R}^2$ 上的分布函数.

设 $(\mathbb{R}^2, \mathcal{B}^2)$ 上的局部有限测度 $\mu$ 有分布函数 $G$. 称 $(x, y) \in \mathbb{R}^2$ 为 $\mu$ 或 $G$ 的跳跃点, 是指

$$
\Delta G (x, y) := G (x, y) - G (x -, y) - G (x, y -) + G (x -, y -) > 0.
$$

---

3.1 随机向量与联合分布

65

此时称  $\Delta G(x,y)=\mu(\{(x,y)\})$  为  $\mu$  或 G 在点  $(x,y)$  的跳幅。易知，跳跃点集  $E:=\{(x,y)\in\mathbb{R}^{2}:\Delta G(x,y)>0\}$  至多为可数集。写该集合为  $E=\{(x_{1},y_{1}),(x_{2},y_{2}),\cdots\}$ ，并记  $q(x_{i},y_{i})=\Delta G(x_{i},y_{i})$ 。称  $\mu$  或 G 是离散型的，是指有

$$
\Delta G ((a, b ] \times (c, d ]) = \sum_ {x _ {i} \in (a, b ]} \sum_ {y _ {i} \in (c, d ]} q (x _ {i}, y _ {i}), \quad (a, b ] \times (c, d ] \subseteq \mathbb {R} ^ {2}. \tag {3.1.4}
$$

此时称 $q$ 为 $\mu$ 或 $G$ 的密度函数或密度. 与一维情况不同, 当 $E$ 非空时分布函数 $G$ 并不在整个集合 $E^{c} = \mathbb{R}^{2} \setminus E$ 上连续.

称 $(\mathbb{R}^2, \mathcal{B}^2)$ 上的局部有限测度 $\mu$ 或其分布函数 $G$ 是绝对连续型的, 是指存在 $\mathbb{R}^2$ 上的非负黎曼可积函数 $q$ 使得

$$
\Delta G ((a, b ] \times (c, d ]) = \int_ {a} ^ {b} \int_ {c} ^ {d} q (x, y) \mathrm{d} x \mathrm{d} y, \quad (a, b ] \times (c, d ] \subseteq \mathbb {R} ^ {2}. \tag {3.1.5}
$$

此时称 $q$ 为 $\mu$ 或 $G$ 的密度函数或密度. 显然, 绝对连续型分布函数是 $\mathbb{R}$ 上的连续函数. 另外, 根据数学分析的结果, 若函数 $G$ 二次连续可微, 则 (3.1.5) 式对 $q = G_{xy}^{\prime \prime}$ 成立.

这里的讨论可以平行地推广到多维情况. 多维空间  $(\mathbb{R}^{d}, \mathcal{B}^{d})$  上的局部有限测度也由其分布函数唯一决定. 特别地, 对应于  $(\mathbb{R}^{d}, \mathcal{B}^{d})$  上的有限测度  $\mu$ , 有唯一的分布函数 G 满足  $G(-\infty, -\infty, \cdots, -\infty) = 0$ . 该分布函数由下式给出:

$$
G (x _ {1}, x _ {2}, \dots , x _ {d}) = \mu ((- \infty , x _ {1} ] \times (- \infty , x _ {2} ] \times \dots \times (- \infty , x _ {d} ]), \tag {3.1.6}
$$

其中  $(x_{1}, x_{2}, \cdots, x_{d}) \in \mathbb{R}^{d}$ . 后面当提到  $(\mathbb{R}^{d}, \mathcal{B}^{d})$  上的有限测度  $\mu$  的分布函数时, 总是指由 (3.1.6) 式定义的函数. 此时, 对  $1 \leqslant k \leqslant d$  令

$$
\mu_ {k} (B) = \mu (\mathbb {R} \times \dots \times \mathbb {R} \times B \times \mathbb {R} \times \dots \times \mathbb {R}), \quad B \in \mathcal {B},
$$

其中等号右端乘积集中的第 $k$ 个集合取 $B$ 而其他集合均取 $\mathbb{R}$. 显然 $\mu_k$ 是 $(\mathbb{R}, \mathcal{B})$ 上的有限测度, 称为 $\mu$ 的第 $k$ 个边缘分布. 称 $\mu_k$ 的分布函数 $G_k$ 为 $\mu$ 的第 $k$ 个边缘分布函数. 易见

$$
G _ {k} (x) = G (\infty, \dots , \infty , x, \infty , \dots , \infty), \quad x \in \mathbb {R}, \tag {3.1.7}
$$

其中等号右端第 k 个分量取 x 而其他分量取  $\infty$ .

## 3.1.2 随机向量的分布

定义 3.1.1 设  $(\Omega, \mathcal{F}, \mathbf{P})$  为概率空间，而  $\xi_{1}, \xi_{2}, \cdots, \xi_{d}$  为其上的 d 个随机变量。我们称  $\xi := (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  为 d 维随机向量或 d 维随机变量。

---

66

第三章 随机向量和独立性

定理 3.1.2 设  $\xi=(\xi_{1},\xi_{2},\cdots,\xi_{d})$  为  $(\Omega,\mathcal{F},\mathbf{P})$  上的 d 维随机向量. 则对任何  $B\in B^{d}$  有

$$
\xi^ {- 1} (B) := \{\omega : \xi (\omega) \in B \} \in \mathscr {F}. \tag {3.1.8}
$$

证明 令 $\mathcal{S}^d$ 为 $\mathbb{R}^d$ 中的左开右闭区间构成的集类. 由命题1.2.4知 $\sigma(\mathcal{S}^d) = \mathcal{B}^d$. 对于任何 $(a, b] = (a_1, b_1] \times (a_2, b_2] \times \cdots \times (a_d, b_d] \in \mathcal{S}^d$, 显然有

$$
\xi^ {- 1} (a, b ] = \left\{\omega : \xi_ {i} (\omega) \in (a _ {i}, b _ {i} ], i = 1, 2, \dots , d \right\}
$$

$$
= \bigcap_ {i = 1} ^ {d} \left\{\omega : \xi_ {i} (\omega) \in (a _ {i}, b _ {i} ] \right\} \in \mathscr {F}.
$$

这说明 $\xi^{-1}(\mathcal{S}^d)\subseteq \mathcal{F}$ .再根据命题2.1.2有

$$
\xi^ {- 1} (\mathcal {B} ^ {d}) = \xi^ {- 1} (\sigma (\mathcal {S} ^ {d})) = \sigma (\xi^ {- 1} (\mathcal {S} ^ {d})) \subseteq \mathcal {F}.
$$

即 (3.1.8) 式对任何 $B \in \mathcal{B}^d$ 均成立.

与定理 2.1.8 的证明类似地, 可以得到

定理 3.1.3 设  $\xi=(\xi_{1},\xi_{2},\cdots,\xi_{d})$  为  $\Omega$  上的 d 维向量值函数, 而 f 为  $R^{d}$  上的博雷尔可测函数. 则  $\eta:=f(\xi)$  关于  $\Omega$  上的  $\sigma$  代数  $\sigma(\{\xi_{1},\xi_{2},\cdots,\xi_{d}\})$  可测. 特别地, 若  $\xi$  为  $(\Omega,\mathcal{F},\mathbf{P})$  上的 d 维随机向量, 则  $\eta$  为  $(\Omega,\mathcal{F},\mathbf{P})$  上的随机变量.

设  $\xi=(\xi_{1},\xi_{2},\cdots,\xi_{d})$  为概率空间  $(\Omega,\mathcal{F},\mathbf{P})$  上的 d 维随机向量. 对于  $A\in B^{d}$ ，令

$$
\mu (A) = \mathbf {P} (\xi^ {- 1} (A)) = \mathbf {P} (\xi \in A). \tag {3.1.9}
$$

与定理 2.1.14 类似地, 可以证明  $\mu$  为  $(\mathbb{R}^{d}, \mathcal{B}^{d})$  上的概率测度.

定义 3.1.2 我们称由 (3.1.9) 式定义的概率测度  $\mu$  为随机向量  $\xi = (\xi_{1}, \xi_{2}, \cdots, \xi_{d})$  的联合概率分布，简称联合分布。称  $\mu$  的分布函数

$$
F (x _ {1}, x _ {2}, \dots , x _ {d}) := \mathbf {P} (\xi_ {1} \leqslant x _ {1}, \xi_ {2} \leqslant x _ {2}, \dots , \xi_ {d} \leqslant x _ {d}), \quad (x _ {1}, x _ {2}, \dots , x _ {d}) \in \mathbb {R} ^ {d} \tag {3.1.10}
$$

为  $\xi$  的联合概率分布函数, 简称联合分布函数.

利用联合分布 $\mu$ 可以容易地确定出 $\xi$ 的 $d$ 个分量的分布. 事实上, 对于 $1 \leqslant k \leqslant d$ 和 $B \in \mathcal{B}$ 有

$$
\mu_ {k} (B) := \mathbf {P} (\xi_ {k} \in B) = \mu (\mathbb {R} \times \dots \times \mathbb {R} \times B \times \mathbb {R} \times \dots \times \mathbb {R}), \tag {3.1.11}
$$

其中等式右端乘积集中的第 $k$ 个集合取 $B$ 而其他集合均取 $\mathbb{R}$. 称 $\mu_{k}$ 为 $\xi_{k}$ 的边缘分布, 它也就是 $\mu$ 的第 $k$ 个边缘分布. 类似地, 对于 $1 \leqslant k \leqslant d$ 和 $x \in \mathbb{R}$ 有

$$
F _ {k} (x) := \mathbf {P} \left(\xi_ {k} \leqslant x\right) = F (\infty , \dots , \infty , x, \infty , \dots , \infty), \tag {3.1.12}
$$

---

3.1 随机向量与联合分布

67

其中等式右端第 $k$ 个分量取 $x$ 而其他分量取 $\infty$. 称 $F_{k}$ 为 $\xi_{k}$ 的边缘分布函数, 它也就是 $\mu$ 的第 $k$ 个边缘分布函数.

为简单起见, 下面重点讨论二维随机向量及其联合分布的性质, 所得到的结果容易推广到多维情况. 设  $(\xi,\eta)$  为  $(\Omega,\mathcal{F},\mathbf{P})$  上的随机向量. 其联合分布函数为

$$
F (x, y) := \mathbf {P} (\xi \leqslant x, \eta \leqslant y), \quad x, y \in \mathbb {R}. \tag {3.1.13}
$$

相应的边缘分布函数为

$$
F _ {\xi} (x) := \mathbf {P} (\xi \leqslant x), F _ {\eta} (y) := \mathbf {P} (\eta \leqslant y), x, y \in \mathbb {R}.
$$

由命题3.1.1知函数 $F(x,y)$ 关于 $x$ 和 $y$ 都是不降且右连续的，且它在任一矩形$(a,b]:=(a_{1},b_{1}]\times(a_{2},b_{2}]$ 上有非负增量，即

$$
\Delta F (a, b ] := F (b _ {1}, b _ {2}) - F (b _ {1}, a _ {2}) - F (a _ {1}, b _ {2}) + F (a _ {1}, a _ {2}) \geqslant 0.
$$

不难发现

$$
\mathbf {P} (a _ {1} <   \xi \leqslant b _ {1}, a _ {2} <   \eta \leqslant b _ {2}) = \mathbf {P} ((\xi , \eta) \in (a, b ]) = \Delta F (a, b ].
$$

## 3.1.3 离散型随机向量

设  $\xi$  和  $\eta$  是定义在概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  的离散型随机变量, 分别取值于可数集  $\{x_{i}: i = 1, 2, \cdots\}$  和  $\{y_{j}: j = 1, 2, \cdots\}$ . 此时称随机向量  $(\xi, \eta)$  为离散型的, 它取值于可数集  $E := \{(x_{i}, y_{j}): i, j = 1, 2, \cdots\}$ . 此时  $(\xi, \eta)$  的联合分布函数 F 可表示为

$$
F (x, y) = \mathbf {P} (\xi \leqslant x, \eta \leqslant y) = \sum_ {x _ {i} \leqslant x} \sum_ {y _ {j} \leqslant y} p (x _ {i}, y _ {j}), \quad (x, y) \in \mathbb {R} ^ {2}, \tag {3.1.14}
$$

其中

$$
p (x _ {i}, y _ {j}) = \mathbf {P} (\xi = x _ {i}, \eta = y _ {j}), \quad i, j = 1, 2, \dots .
$$

注意

$$
\sum_ {i, j} p (x _ {i}, y _ {j}) = 1.
$$

我们称 $p$ 为 $(\xi, \eta)$ 的联合分布列或联合分布密度. 定义

$$
p _ {\xi} (x _ {i}) = \sum_ {j = 1} ^ {\infty} p (x _ {i}, y _ {j}) = \mathbf {P} (\xi = x _ {i}), \quad i = 1, 2, \dots ,
$$

---

68

第三章 随机向量和独立性

$$
p _ {\eta} (y _ {j}) = \sum_ {i = 1} ^ {\infty} p (x _ {i}, y _ {j}) = \mathbf {P} (\eta = y _ {j}), \quad j = 1, 2, \dots .
$$

分别称 $p_{\xi}$ 和 $p_{\eta}$ 为 $\xi$ 和 $\eta$ 的边缘分布列或边缘分布密度. 此时 $\xi$ 和 $\eta$ 的边缘分布函数可以表示为

$$
F _ {\xi} (x) = \mathbf {P} (\xi \leqslant x) = \sum_ {x _ {i} \leqslant x} p _ {\xi} (x _ {i}), \quad x \in \mathbb {R},
$$

$$
F _ {\eta} (y) = \mathbf {P} (\eta \leqslant x) = \sum_ {y _ {j} \leqslant y} p _ {\eta} (y _ {j}), \quad y \in \mathbb {R}.
$$

离散型随机向量 $(\xi, \eta)$ 的分布性质由它的联合分布密度确定. 显然

$$
\mathbf {P} \{(\xi , \eta) \in B \} = \sum_ {(x _ {i}, y _ {j}) \in B} p (x _ {i}, y _ {j}), \quad B \in \mathcal {B} ^ {2}. \tag {3.1.15}
$$

例 3.1.2 设袋中有 4 个红球和 2 个黑球. 采用如下两种方式抽球: (1) 从中有放回抽取 2 次; (2) 从中无放回抽取 2 次. 分别用  $\xi$  和  $\eta$  表示第 1 次和第 2 次抽到的黑球数. 分别就两种方式求出  $(\xi, \eta)$  的联合分布列.

解 两种抽取方式所对应的随机试验都可用古典概型描述. 为此我们将 4 个红球用数字 1, 2, 3, 4 编号, 将 2 个黑球用数字 5, 6 编号. 显然 $\xi$ 和 $\eta$ 可能的取值均为 0, 1.

(1) 对于有放回抽取, 可将样本空间取为 $\Omega_1 = \{(i,j): 1 \leqslant i \leqslant 6, 1 \leqslant j \leqslant 6\}$. 令

$$
A = \{(i, j) \in \Omega_ {1}: 5 \leqslant i \leqslant 6 \}, B = \{(i, j) \in \Omega_ {1}: 5 \leqslant j \leqslant 6 \}.
$$

则

$$
A ^ {c} = \{(i, j) \in \Omega_ {1}: 1 \leqslant i \leqslant 4 \}, B ^ {c} = \{(i, j) \in \Omega_ {1}: 1 \leqslant j \leqslant 4 \}.
$$

注意

$$
\xi (\omega) = 1 _ {A} (\omega), \eta (\omega) = 1 _ {B} (\omega), \omega = (i, j) \in \Omega_ {1}.
$$

显然

$$
A ^ {c} B ^ {c} = \{(i, j) \in \Omega_ {1}: 1 \leqslant i \leqslant 4; 1 \leqslant j \leqslant 4 \},
$$

$$
A ^ {c} B = \{(i, j) \in \Omega_ {1}: 1 \leqslant i \leqslant 4; 5 \leqslant j \leqslant 6 \},
$$

故有

$$
\mathbf {P} (\xi = 0, \eta = 0) = \mathbf {P} (A ^ {c} B ^ {c}) = \frac {4 \times 4}{6 \times 6} = \frac {4}{9},
$$

$$
\mathbf {P} (\xi = 0, \eta = 1) = \mathbf {P} (A ^ {c} B) = \frac {4 \times 2}{6 \times 6} = \frac {2}{9}.
$$

---

3.1 随机向量与联合分布

69

类似地可求得

$$
\mathbf {P} (\xi = 1, \eta = 0) = \mathbf {P} (A B ^ {c}) = \frac {2 \times 4}{6 \times 6} = \frac {2}{9},
$$

$$
\mathbf {P} (\xi = 1, \eta = 1) = \mathbf {P} (A B) = \frac {2 \times 2}{6 \times 6} = \frac {1}{9}.
$$

(2) 对于无放回抽取, 样本空间可取为 $\Omega_{2} = \{(i,j):1\leqslant i\leqslant 6,1\leqslant j\leqslant 6$ 且 $i\neq j\}$. 令

$$
A = \{(i, j) \in \Omega_ {2}: 5 \leqslant i \leqslant 6 \}, B = \{(i, j) \in \Omega_ {2}: 5 \leqslant j \leqslant 6 \}.
$$

则有

$$
\xi (\omega) = 1 _ {A} (\omega), \eta (\omega) = 1 _ {B} (\omega), \omega = (i, j) \in \Omega_ {2}.
$$

与有放回情况类似地可以求得

$$
\mathbf {P} (\xi = 0, \eta = 0) = \frac {4 \times 3}{6 \times 5} = \frac {2}{5}, \quad \mathbf {P} (\xi = 0, \eta = 1) = \frac {4 \times 2}{6 \times 5} = \frac {4}{1 5},
$$

$$
\mathbf {P} (\xi = 1, \eta = 0) = \frac {2 \times 4}{6 \times 5} = \frac {4}{1 5}, \quad \mathbf {P} (\xi = 1, \eta = 1) = \frac {2 \times 1}{6 \times 5} = \frac {1}{1 5}. \quad \square
$$

例3.1.3 例3.1.2中的边缘分布为

(1) 对于有放回抽取,

$$
\mathbf {P} (\xi = 0) = \frac {2}{3}, \quad \mathbf {P} (\xi = 1) = \frac {1}{3}, \quad \mathbf {P} (\eta = 0) = \frac {2}{3}, \quad \mathbf {P} (\eta = 1) = \frac {1}{3}.
$$

注意此时 $\mathbf{P}\{\xi = i,\eta = j\} = \mathbf{P}\{\xi = i\} \mathbf{P}\{\eta = j\}$

(2) 对于无放回抽取,

$$
\mathbf {P} (\xi = 0) = \frac {2}{3}, \quad \mathbf {P} (\xi = 1) = \frac {1}{3}, \quad \mathbf {P} (\eta = 0) = \frac {2}{3}, \quad \mathbf {P} (\eta = 1) = \frac {1}{3}.
$$

此时 $\mathbf{P}(\xi = i, \eta = j) \neq \mathbf{P}(\xi = i)\mathbf{P}(\eta = j)$.

在上面的例子中, 两种假设导致不同的联合分布列, 但它们却有相同的边缘分布列. 这说明联合分布列不能由边缘分布列唯一确定.

## 3.1.4 绝对连续型随机向量

称随机向量 $(\xi, \eta)$ 为绝对连续型的, 是指它的联合分布函数 $F$ 是绝对连续型的, 即有表达式

$$
F (x, y) = \int_ {- \infty} ^ {x} \int_ {- \infty} ^ {y} p (u, v) \mathrm{d} u \mathrm{d} v, \quad (x, y) \in \mathbb {R} ^ {2},
$$

---

70

第三章 随机向量和独立性

其中 $p$ 为 $F$ 的密度函数, 它是 $\mathbb{R}^2$ 上的非负可积函数且满足

$$
\int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {\infty} p (x, y) \mathrm{d} x \mathrm{d} y = 1.
$$

我们也称 $p$ 为 $(\xi, \eta)$ 的联合分布密度. 绝对连续型随机向量 $(\xi, \eta)$ 的分布性质完全由它的联合分布密度确定. 显然

$$
\mathbf {P} \{(\xi , \eta) \in B \} = \iint_ {B} p (x, y) \mathrm{d} x \mathrm{d} y, \quad B \in \mathcal {B} ^ {2}. \tag {3.1.16}
$$

特别地, 对 $x, y \in \mathbb{R}$ 有

$$
F _ {\xi} (x) := \mathbf {P} (\xi \leqslant x) = \int_ {- \infty} ^ {x} \int_ {- \infty} ^ {\infty} p (u, v) \mathrm{d} u \mathrm{d} v = \int_ {- \infty} ^ {x} p _ {\xi} (u) \mathrm{d} u,
$$

$$
F _ {\eta} (y) := \mathbf {P} (\eta \leqslant y) = \int_ {- \infty} ^ {\infty} \int_ {- \infty} ^ {y} p (u, v) \mathrm{d} u \mathrm{d} v = \int_ {- \infty} ^ {y} p _ {\eta} (v) \mathrm{d} v,
$$

其中

$$
p _ {\xi} (x) = \int_ {- \infty} ^ {\infty} p (x, v) \mathrm{d} v, \quad p _ {\eta} (y) = \int_ {- \infty} ^ {\infty} p (u, y) \mathrm{d} u. \tag {3.1.17}
$$

可见 $\xi$ 和 $\eta$ 都是绝对连续型随机变量. 此时分别称 $p_{\xi}$ 和 $p_{\eta}$ 为 $\xi$ 和 $\eta$ 的边缘分布密度.

若有区域 $E \subseteq \mathbb{R}^2$ 使得 $p(x, y) = 0, (x, y) \in E^c$, 我们也说 $(\xi, \eta)$ 是 $E$ 上的绝对连续型随机向量. 此时, 对任何 $B \in \mathcal{B}^2$ 有

$$
\mathbf {P} \{(\xi , \eta) \in B \} = \iint_ {E \cap B} p (x, y) \mathrm{d} x \mathrm{d} y. \tag {3.1.18}
$$

例3.1.4 设集合 $E \in \mathcal{B}^2$ 满足 $0 < m(E) < \infty$, 其中 $m$ 表示 $\mathbb{R}^2$ 上的勒贝格测度. 我们称 $E$ 上的绝对连续型随机向量 $(\xi, \eta)$ 服从 $E$ 上的均匀分布, 是指其分布密度满足

$$
p (x, y) = \frac {1}{m (E)}, \quad (x, y) \in E.
$$

此时, 对任何 $B \in E \cap \mathcal{B}^2$ 有

$$
\mathbf {P} \{(\xi , \eta) \in B \} = \frac {m (B)}{m (E)}.
$$

例 3.1.5 设随机向量  $(\xi,\eta)$  服从单位圆盘  $D=\{(x,y):x^{2}+y^{2}<1\}$  上的均匀分布, 即有联合分布密度

$$
p (x, y) = \frac {1}{\pi}, \quad x ^ {2} + y ^ {2} <   1.
$$

则  $\xi,\eta$  均取值于  $(-1,1)$ ，而两个边缘分布密度分别为

$$
p _ {\xi} (x) = \int_ {- \sqrt {1 - x ^ {2}}} ^ {\sqrt {1 - x ^ {2}}} \frac {1}{\pi} \mathrm{d} y = \frac {2}{\pi} \sqrt {1 - x ^ {2}}, \quad - 1 <   x <   1
$$

---

3.1 随机向量与联合分布

71

和

$$
p _ {\eta} (y) = \int_ {- \sqrt {1 - y ^ {2}}} ^ {\sqrt {1 - y ^ {2}}} \frac {1}{\pi} \mathrm{d} x = \frac {2}{\pi} \sqrt {1 - y ^ {2}}, \quad - 1 <   y <   1.
$$

注意, 这两个边缘分布都不是一维均匀分布, 且 $p(x,y) \neq p_{\xi}(x)p_{\eta}(y)$.

令 $p_{\xi}(x)$ 和 $p_{\eta}(y)$ 由(3.1.17)式定义, 再令 $q(x,y) = p_{\xi}(x)p_{\eta}(y)$. 则 $q$ 也是 $\mathbb{R}^2$ 上的某个概率测度的密度函数, 而且它也有边缘分布密度 $p_{\xi}$ 和 $p_{\eta}$. 例3.1.5表明未必有 $p = q$. 所以由边缘分布密度不能唯一确定联合分布密度.

例3.1.6 对 $0 < x, y < 1$，令 $F(x, y) = xy(1 + xy)/2$. 因为 $F_{xy}''(x, y) = (1 + 4xy)/2$，我们有

$$
F (x, y) = \frac {1}{2} \int_ {0} ^ {x} \int_ {0} ^ {y} (1 + 4 u v) \mathrm{d} u \mathrm{d} v, \quad 0 <   x, y <   1.
$$

所以 $F$ 是矩形 $(0,1)^{2}$ 上的以 $p(x,y) = (1 + 4xy) / 2$ 为密度函数的绝对连续型概率分布函数.

例3.1.7 设 $\xi$ 服从均匀分布 $U(0,1)$. 令 $\eta = \sqrt{\xi}$. 易证 $\eta$ 也服从绝对连续型分布且有分布密度 $p_{\eta}(y) = 2y, 0 < y < 1$. 记 $E = \{(x, \sqrt{x}) : 0 < x < 1\}$. 显然有 $\mathbf{P}\{(\xi, \eta) \in E\} = 1$. 由于集合 $E$ 的二维勒贝格测度为零, 随机向量 $(\xi, \eta)$ 不是绝对连续型的. 可见, 随机向量的边缘分布是绝对连续型的并不能保证其联合分布是绝对连续型的.

## 3.1.5 二维正态随机向量

二维正态分布随机向量是绝对连续型二维随机向量的典型例子.对于给定的常数 $a_1, a_2 \in \mathbb{R}, \sigma_1, \sigma_2 > 0, -1 < r < 1$，我们定义 $\mathbb{R}^2$ 上的函数

$$
\begin{array}{l} p (x, y) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2} \sqrt {1 - r ^ {2}}} \exp \left\{- \frac {1}{2 (1 - r ^ {2})} \left[ \left(\frac {x - a _ {1}}{\sigma_ {1}}\right) ^ {2} - \right. \right. \\ \left. \frac {2 r (x - a _ {1}) (y - a _ {2})}{\sigma_ {1} \sigma_ {2}} + \left(\frac {y - a _ {2}}{\sigma_ {2}}\right) ^ {2} \right] \Bigg \}. \tag {3.1.19} \\ \end{array}
$$

命题 3.1.4 由 (3.1.19) 式定义的函数  $p(x,y)$  是一个二维密度函数, 且其边缘分布密度分别为一维正态分布密度

$$
p _ {\xi} (x) = \frac {1}{\sqrt {2 \pi} \sigma_ {1}} \exp \Big \{- \frac {(x - a _ {1}) ^ {2}}{2 \sigma_ {1} ^ {2}} \Big \},
$$

$$
p _ {\eta} (y) = \frac {1}{\sqrt {2 \pi} \sigma_ {2}} \exp \Big \{- \frac {(y - a _ {2}) ^ {2}}{2 \sigma_ {2} ^ {2}} \Big \}.
$$

---

72

第三章 随机向量和独立性

证明 显然 $p(x,y)\geqslant 0$ .作积分变量替换 $u = (x - a_1) / \sigma_1$ 和 $v = (y - a_2) / \sigma_2$ 有

$$
\begin{array}{l} p _ {\xi} (x) = \int_ {- \infty} ^ {\infty} p (x, y) \mathrm{d} y \\ = \frac {1}{2 \pi \sigma_ {1} \sqrt {1 - r ^ {2}}} \int_ {- \infty} ^ {\infty} \exp \left\{- \frac {1}{2 (1 - r ^ {2})} [ u ^ {2} - 2 r u v + v ^ {2} ] \right\} \mathrm{d} v \\ = \frac {1}{2 \pi \sigma_ {1} \sqrt {1 - r ^ {2}}} \int_ {- \infty} ^ {\infty} \exp \left\{- \frac {(v - r u) ^ {2} + (1 - r ^ {2}) u ^ {2}}{2 (1 - r ^ {2})} \right\} \mathrm{d} v \\ = \frac {1}{\sqrt {2 \pi} \sigma_ {1}} \mathrm{e} ^ {- \frac {u ^ {2}}{2}} \int_ {- \infty} ^ {\infty} \frac {1}{\sqrt {2 \pi (1 - r ^ {2})}} \exp \left\{- \frac {(v - r u) ^ {2}}{2 (1 - r ^ {2})} \right\} \mathrm{d} v \\ = \frac {1}{\sqrt {2 \pi} \sigma_ {1}} \mathrm{e} ^ {- \frac {u ^ {2}}{2}} = \frac {1}{\sqrt {2 \pi} \sigma_ {1}} \exp \Big \{- \frac {(x - a _ {1}) ^ {2}}{2 \sigma_ {1} ^ {2}} \Big \}. \\ \end{array}
$$

上式为正态分布 $N(a_{1},\sigma_{1}^{2})$ 的密度函数. 再对 $x \in \mathbb{R}$ 积分知 $p(x,y)$ 满足规范性. 因此 $p(x,y)$ 是一个二维密度函数, 且其一边缘分布密度为 $p_{\xi}(x)$. 类似地可以算出另一个边缘分布密度 $p_{\eta}(y)$ 就是正态分布 $N(a_{2},\sigma_{2}^{2})$ 的密度函数. □

定义 3.1.3 我们称以 (3.1.19) 式定义的函数  $p(x,y)$  为密度的二维绝对连续型分布为二维正态分布, 记作  $N(a_{1},a_{2};\sigma_{1}^{2},\sigma_{2}^{2};r)$ .

根据命题3.1.4, 二维正态分布 $N(a_{1}, a_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; r)$ 的两个边缘分布分别是一维正态分布 $N(a_{1}, \sigma_{1}^{2})$ 和 $N(a_{2}, \sigma_{2}^{2})$.

## 练习题

1. 从 $1,2,\cdots,n$ 中随机选取一个数记为 $\eta$, 再从 $1,2,\cdots,\eta$ 中随机选取一数记为 $\xi$. 求 $(\xi,\eta)$ 的联合分布和边缘分布.
2. 设  $(\xi, \eta)$  为绝对连续型随机向量. 证明  $\mathbf{P}(\xi = \eta) = 0$ .
3. 设 $f_{1}, f_{2}$ 是一维概率分布密度函数, 而 $g$ 为 $\mathbb{R}^{2}$ 上的黎曼可积函数. 使得 $h(x, y) := f_{1}(x)f_{2}(y) + g(x, y)$ 为二维概率分布密度函数的充要条件是什么?
4. 随机向量 $(\xi, \eta)$ 的联合分布密度为 $p(x, y) = a\mathrm{e}^{-(2x + y)}1_{\{x > 0\}}1_{\{y > 0\}}$. 求:

(1) 常数 $a$; (2) $\xi$ 的边缘密度; (3) $\mathbf{P}(\xi \leqslant 2, \eta \leqslant 1)$; (4) $\mathbf{P}(\xi + \eta \leqslant 2)$.

5. 设随机向量 $(\xi, \eta)$ 的联合分布密度为 $p(x, y) = 3(1 - x)1_{\{0 < x < y < 1\}}$. 求其边缘分布密度.

6. 函数 $F(x, y) = (1 - \mathrm{e}^{-xy})1_{\{x > 0, y > 0\}}$ 是否为二维概率分布函数？

---

3.2 条件分布与独立性

73

## 3.2 条件分布与独立性

对应于事件的条件概率, 在联合分布的基础上, 我们可以讨论随机变量的条件分布, 它们是研究随机向量的基本而重要的工具. 在此基础上, 我们可以讨论随机变量的独立性. 限于目前的知识储备, 本节主要讨论离散型和绝对连续型两种随机向量.

## 3.2.1 随机变量的条件分布

考虑概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$，设事件 $B \in \mathcal{F}$ 满足 $\mathbf{P}(B) > 0$。我们知道，在事件 $B$ 发生的情况下事件 $A \in \mathcal{F}$ 的条件概率为

$$
\mathbf {P} (A | B) = \frac {\mathbf {P} (A B)}{\mathbf {P} (B)}.
$$

令  $\mathbf{P}_{B}:=\mathbf{P}(\cdot|B)$  为给定事件 B 的条件概率测度.

注意 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的随机变量 $\xi$ 也是概率空间 $(\Omega, \mathcal{F}, \mathbf{P}_B)$ 上的随机变量. 在后一概率空间上, 我们当然也可以讨论 $\xi$ 的概率分布、分布函数等. 这就引出了

定义3.2.1 设 $\xi$ 为概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的随机变量. 若 $B \in \mathcal{F}$ 满足 $\mathbf{P}(B) > 0$, 则称

$$
\mu_ {\xi} (A | B) := \mathbf {P} (\xi \in A | B), \quad A \in \mathscr {B}
$$

为 $B$ 发生时 $\xi$ 的条件分布. 此时在 $B$ 发生时 $\xi$ 的条件分布函数定义为

$$
F _ {\xi} (x | B) = \mathbf {P} (\xi \leqslant x | B), \quad x \in \mathbb {R}.
$$

定义 3.2.2 设离散型随机向量  $(\xi,\eta)$  为取值于  $E:=\{(x_{i},y_{j}):i,j=1,2,\cdots\}$  且有联合分布列

$$
p (x _ {i}, y _ {j}) = \mathbf {P} (\xi = x _ {i}, \eta = y _ {j}), \quad i, j = 1, 2, \dots
$$

及边缘分布列

$$
p _ {\xi} (x _ {i}) = \sum_ {j = 1} ^ {\infty} p (x _ {i}, y _ {j}) = \mathbf {P} (\xi = x _ {i}), \quad i = 1, 2, \dots ,
$$

$$
p _ {\eta} (y _ {j}) = \sum_ {i = 1} ^ {\infty} p (x _ {i}, y _ {j}) = \mathbf {P} (\eta = y _ {j}), \quad j = 1, 2, \dots .
$$

若 $p_{\eta}(y_j) > 0$ ，则称

$$
p _ {\xi} (x _ {i} | \eta = y _ {j}) := \frac {p (x _ {i} , y _ {j})}{p _ {\eta} (y _ {j})} = \mathbf {P} (\xi = x _ {i} | \eta = y _ {j}), \quad i = 1, 2, \dots
$$

---

74

第三章 随机向量和独立性

为当 $\eta = y_{j}$ 时 $\xi$ 的条件分布列或条件分布密度. 类似地, 若 $p_{\xi}(x_i) > 0$, 则称

$$
p _ {\eta} (y _ {j} | \xi = x _ {i}) := \frac {p (x _ {i} , y _ {j})}{p _ {\xi} (x _ {i})} = \mathbf {P} (\eta = y _ {j} | \xi = x _ {i}), \quad j = 1, 2, \dots
$$

为当 $\xi = x_{i}$ 时 $\eta$ 的条件分布列或条件分布密度.

定义 3.2.3 设绝对连续型随机向量  $(\xi,\eta)$  有联合分布密度 p 及边缘分布密度

$$
p _ {\xi} (x) = \int_ {- \infty} ^ {\infty} p (x, v) \mathrm{d} v, \quad p _ {\eta} (y) = \int_ {- \infty} ^ {\infty} p (u, y) \mathrm{d} u, \quad x, y \in \mathbb {R}.
$$

若 $p_{\eta}(y) > 0$ ，则称

$$
p _ {\xi} (x | \eta = y) := \frac {p (x , y)}{p _ {\eta} (y)}, \quad x \in \mathbb {R}
$$

为当 $\eta = y$ 时 $\xi$ 的条件分布密度. 类似地, 若 $p_{\xi}(x) > 0$, 则称

$$
p _ {\eta} (y | \xi = x) := \frac {p (x , y)}{p _ {\xi} (x)}, \quad y \in \mathbb {R}
$$

为当 $\xi = x$ 时 $\eta$ 的条件分布密度.

在适当的连续性条件下, 当 $\delta > 0$ 很小时有

$$
\begin{array}{l} \mathbf {P} (\eta \leqslant y | \xi \in [ x, x + \delta ]) = \frac {\mathbf {P} (\xi \in [ x , x + \delta ] , \eta \leqslant y)}{\mathbf {P} (\xi \in [ x , x + \delta ])} \\ = \frac {\int_ {- \infty} ^ {y} \mathrm{d} v \int_ {x} ^ {x + \delta} p (u , v) \mathrm{d} u}{\int_ {x} ^ {x + \delta} p _ {\xi} (u) \mathrm{d} u} \\ \approx \int_ {- \infty} ^ {y} \frac {p (x , v)}{p _ {\xi} (x)} \mathrm{d} v. \\ \end{array}
$$

这在一定程度上说明了定义 3.2.3 的合理性.

例3.2.1 设随机向量 $(\xi, \eta)$ 服从单位圆盘 $D = \{(x, y): x^2 + y^2 < 1\}$ 上的均匀分布，即其联合分布密度为

$$
p (x, y) = \frac {1}{\pi}, \quad x ^ {2} + y ^ {2} <   1.
$$

则 $\eta$ 的边缘分布密度为

$$
p _ {\eta} (y) = \frac {1}{\pi} \int_ {- \sqrt {1 - y ^ {2}}} ^ {\sqrt {1 - y ^ {2}}} \mathrm{d} x = \frac {2}{\pi} \sqrt {1 - y ^ {2}}, \quad | y | <   1.
$$

所以

$$
p _ {\xi} (x | \eta = y) = \frac {1}{2 \sqrt {1 - y ^ {2}}}, \quad | x | <   \sqrt {1 - y ^ {2}}.
$$

即当 $\eta = y$ 时 $\xi$ 的条件分布是 $\left(-\sqrt{1 - y^2},\sqrt{1 - y^2}\right)$ 上的均匀分布.

---

3.2 条件分布与独立性

75

例3.2.2 设 $(\xi, \eta)$ 服从二维正态分布 $N(a_{1}, a_{2}; \sigma_{1}^{2}, \sigma_{2}^{2}; r)$. 则当 $\eta = y$ 时 $\xi$ 的条件分布密度为

$$
\begin{array}{l} p _ {\xi} (x | \eta = y) = \frac {1}{\sigma_ {1} \sqrt {2 \pi (1 - r ^ {2})}} \exp \left\{- \frac {1}{2 (1 - r ^ {2})} \left[ \left(\frac {x - a _ {1}}{\sigma_ {1}}\right) ^ {2} - \right. \right. \\ \left. \frac {2 r (x - a _ {1}) (y - a _ {2})}{\sigma_ {1} \sigma_ {2}} + r ^ {2} \left(\frac {y - a _ {2}}{\sigma_ {2}}\right) ^ {2} \right] \Bigg \} \\ = \frac {1}{\sigma_ {1} \sqrt {2 \pi (1 - r ^ {2})}} \exp \left\{- \frac {1}{2 (1 - r ^ {2})} \left[ \frac {x - a _ {1}}{\sigma_ {1}} - \frac {r (y - a _ {2})}{\sigma_ {2}} \right] ^ {2} \right\} \\ = \frac {1}{\sigma_ {1} \sqrt {2 \pi (1 - r ^ {2})}} \exp \Big \{- \frac {1}{2 \sigma_ {1} ^ {2} (1 - r ^ {2})} \Big [ x - \Big (a _ {1} + \frac {r \sigma_ {1} (y - a _ {2})}{\sigma_ {2}} \Big) \Big ] ^ {2} \Big \}. \\ \end{array}
$$

此为一维正态分布 $N(a_{1} + r\sigma_{1}(y - a_{2}) / \sigma_{2},\sigma_{1}^{2}(1 - r^{2}))$ 的密度函数.注意当 $r = 0$ 时，这里的 $p_{\xi}(x|\eta = y) = p_{\xi}(x)$ 就是 $N(a_{1},\sigma_{1}^{2})$ 的密度函数.

例3.2.3 设 $\eta$ 服从泊松分布 $P(\lambda)$. 令 $\xi$ 是成功概率为 $p (0 < p < 1)$ 的 $\eta$ 重伯努利试验的成功次数. 于是在给定 $\eta = n$ 时 $\xi$ 的条件分布为二项分布 $B(n, p)$. 因此离散型随机向量 $(\xi, \eta)$ 有联合分布列

$$
\mathbf {P} (\xi = i, \eta = n) = \mathrm{e} ^ {- \lambda} \frac {\lambda^ {n}}{n !} \mathrm{C} _ {n} ^ {i} p ^ {i} (1 - p) ^ {n - i}, \quad n \geqslant i \geqslant 0.
$$

例3.2.4 设 $\eta$ 服从指数分布 $E(\lambda)$, 而在给定 $\eta$ 的条件下 $\xi$ 服从均匀分布 $U(0, \eta)$. 于是在给定 $\eta = y$ 时 $\xi$ 的条件分布密度为 $p_{\xi}(x|\eta = y) = y^{-1}1_{\{0 < x < y\}}$. 因此绝对连续型随机向量 $(\xi, \eta)$ 有联合分布密度

$$
p (x, y) = p _ {\eta} (y) p _ {\xi} (x | \eta = y) = \frac {\lambda}{y} \mathrm{e} ^ {- \lambda y}, \quad y > x > 0.
$$

## 3.2.2 两个随机变量的独立性

定义3.2.4 称概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的随机变量 $\xi$ 和 $\eta$ 独立, 是指它们生成的 $\sigma$ 代数 $\sigma(\xi) = \xi^{-1}(\mathcal{B})$ 和 $\sigma(\eta) = \eta^{-1}(\mathcal{B})$ 独立, 即对任意的 $A, B \in \mathcal{B}$ 都有

$$
\mathbf {P} (\xi \in A, \eta \in B) = \mathbf {P} (\xi \in A) \mathbf {P} (\eta \in B). \tag {3.2.1}
$$

定理3.2.1 设随机变量 $\xi, \eta$ 相互独立. 令 $F_{\xi}$ 和 $F_{\eta}$ 为随机向量 $(\xi, \eta)$ 的两个边缘分布函数. 则对 $B \in \mathcal{B}$, 只要 $\mathbf{P}(\eta \in B) > 0$ 就有

$$
F _ {\xi} (x | \eta \in B) = F _ {\xi} (x), \quad x \in \mathbb {R};
$$

而对 $A \in \mathcal{B}$, 只要 $\mathbf{P}(\xi \in A) > 0$ 就有

$$
F _ {\eta} (y | \xi \in A) = F _ {\eta} (y), \quad y \in \mathbb {R}.
$$

---

76

第三章 随机向量和独立性

证明 在假定条件下, 由 (3.2.1) 式对任何 $x \in \mathbb{R}$ 有

$$
\mathbf {P} (\xi \leqslant x, \eta \in B) = \mathbf {P} (\xi \leqslant x) \mathbf {P} (\eta \in B).
$$

所以

$$
F _ {\xi} (x | \eta \in B) = \mathbf {P} (\xi \leqslant x | \eta \in B) = \mathbf {P} (\xi \leqslant x) = F _ {\xi} (x).
$$

故得第一个结论. 第二个结论的证明类似.

定理3.2.2 设随机向量 $(\xi, \eta)$ 有联合分布函数 $F$ 和边缘分布函数 $F_{\xi}, F_{\eta}$. 则随机变量 $\xi, \eta$ 相互独立当且仅当

$$
F (x, y) = F _ {\xi} (x) F _ {\eta} (y), \quad x, y \in \mathbb {R}. \tag {3.2.2}
$$

证明 假定 $\xi, \eta$ 相互独立. 在 (3.2.1) 式中取 $A = (-\infty, x]$ 和 $B = (-\infty, y]$ 即得 (3.2.2) 式. 反之, 假定 (3.2.2) 式成立, 下证 (3.2.1) 式成立, 从而 $\xi, \eta$ 相互独立. 该证明分为两步:

(1) 取定 $x \in \mathbb{R}$. 对于任意的 $B \in \mathcal{B}$ 定义

$$
\mu_ {x} (B) = \mathbf {P} (\xi \leqslant x, \eta \in B), \quad \nu_ {x} (B) = \mathbf {P} (\xi \leqslant x) \mathbf {P} (\eta \in B).
$$

显然 $\mu_{x}$ 和 $\nu_{x}$ 是 $(\mathbb{R},\mathcal{B})$ 上的两个有限测度. 由(3.2.2)式知对每个 $y\in \mathbb{R}$ 有 $\mu_x(-\infty ,y] =$ $\nu_{x}(-\infty ,y]$. 根据定理2.1.13有 $\mu_{x} = \nu_{x}$, 即对每个 $B\in \mathcal{B}$ 有

$$
\mathbf {P} (\xi \leqslant x, \eta \in B) = \mathbf {P} (\xi \leqslant x) \mathbf {P} (\eta \in B). \tag {3.2.3}
$$

(2) 取定 $B \in \mathcal{B}$. 对于任意的 $A \in \mathcal{B}$ 定义

$$
\mu_ {B} (A) = \mathbf {P} (\xi \in A, \eta \in B), \quad \nu_ {B} (A) = \mathbf {P} (\xi \in A) \mathbf {P} (\eta \in B).
$$

则 $\mu_B$ 和 $\nu_B$ 是 $(\mathbb{R},\mathcal{B})$ 上的两个有限测度. 由 (3.2.3) 式知对每个 $x \in \mathbb{R}$ 有 $\mu_B(-\infty, x] = \nu_B(-\infty, x]$. 再根据定理 2.1.13 有 $\mu_B = \nu_B$, 即对每个 $A \in \mathcal{B}$ 等式 (3.2.1) 式成立. □

定理 3.2.3 设离散型随机向量  $(\xi,\eta)$  取值于  $E:=\{(x_{i},y_{j}):i,j=1,2,\cdots\}$  且有联合分布密度  $p(x_{i},y_{j})=\mathbf{P}(\xi=x_{i},\eta=y_{j})$  及边缘分布密度

$$
p _ {\xi} (x _ {i}) = \mathbf {P} (\xi = x _ {i}), p _ {\eta} (y _ {j}) = \mathbf {P} (\eta = y _ {j}), i, j = 1, 2, \dots .
$$

则 $\xi, \eta$ 独立当且仅当

$$
p (x _ {i}, y _ {j}) = p _ {\xi} (x _ {i}) p _ {\eta} (y _ {j}), \quad i, j = 1, 2, \dots . \tag {3.2.4}
$$

证明 “$\Leftarrow$” 假设 (3.2.4) 式成立. 则 $(\xi, \eta)$ 的联合分布函数满足

$$
F (x, y) = \sum_ {x _ {i} \leqslant x, y _ {j} \leqslant y} p (x _ {i}, y _ {j}) = \sum_ {x _ {i} \leqslant x} \sum_ {y _ {j} \leqslant y} p _ {\xi} (x _ {i}) p _ {\eta} (y _ {j})
$$

---

3.2 条件分布与独立性

77

$$
= \sum_ {x _ {i} \leqslant x} p _ {\xi} (x _ {i}) \sum_ {y _ {j} \leqslant y} p _ {\eta} (y _ {j}) = F _ {\xi} (x) F _ {\eta} (y).
$$

由定理3.2.2知 $\xi, \eta$ 相互独立.

“$\Rightarrow$”若 $\xi, \eta$ 独立，在 (3.2.1) 式中取 $A, B$ 为单点集即得 (3.2.4) 式.

定理3.2.4 设绝对连续型随机向量 $(\xi, \eta)$ 有联合分布密度 $p(x, y)$ 及边缘分布密度 $p_{\xi}(x)$ 和 $p_{\eta}(y)$. 则 $\xi$ 与 $\eta$ 独立当且仅当相对于 $\mathbb{R}^2$ 上的勒贝格测度有

$$
p (x, y) \stackrel {\mathrm{a.e.}} {=} p _ {\xi} (x) p _ {\eta} (y). \tag {3.2.5}
$$

证明 “$\Leftarrow$” 假设 (3.2.5) 式成立. 对于任何 $x, y \in \mathbb{R}$ 有

$$
\begin{array}{l} F (x, y) = \int_ {- \infty} ^ {x} \int_ {- \infty} ^ {y} p (u, v) \mathrm{d} u \mathrm{d} v = \int_ {- \infty} ^ {x} \int_ {- \infty} ^ {y} p _ {\xi} (u) p _ {\eta} (v) \mathrm{d} u \mathrm{d} v \\ = \int_ {- \infty} ^ {x} p _ {\xi} (u) \mathrm{d} u \int_ {- \infty} ^ {y} p _ {\eta} (v) \mathrm{d} v = F _ {\xi} (x) F _ {\eta} (y). \\ \end{array}
$$

由定理3.2.2知 $\xi, \eta$ 相互独立.

“$\Rightarrow$”假设 $\xi, \eta$ 独立. 根据定理 3.2.2, 对于任何 $x, y \in \mathbb{R}$ 有 $F(x, y) = F_{\xi}(x)F_{\eta}(y)$, 即

$$
\int_ {- \infty} ^ {x} \int_ {- \infty} ^ {y} p (u, v) \mathrm{d} u \mathrm{d} v = \int_ {- \infty} ^ {x} p _ {\xi} (u) \mathrm{d} u \int_ {- \infty} ^ {y} p _ {\eta} (v) \mathrm{d} v.
$$

如果联合分布密度 $p$ 和边缘分布密度 $p_{\xi}, p_{\eta}$ 均为有界连续函数, 在上式两端求导数即得 (3.2.5) 式. 对于一般情况的证明需要用到测度论的知识, 这里从略. $\square$

根据定理3.2.3和定理3.2.4, 若 $(\xi, \eta)$ 为离散型或绝对连续型随机向量, 且 $\xi, \eta$ 相互独立, 则当 $p_{\eta}(y) > 0$ 时有 $p_{\xi}(\cdot | \eta = y) = p_{\xi}(\cdot)$; 而当 $p_{\xi}(x) > 0$ 时有 $p_{\eta}(\cdot | \xi = x) = p_{\eta}(\cdot)$.

例3.2.5 设绝对连续型随机向量 $(\xi, \eta)$ 有联合分布密度

$$
p (x, y) = \frac {1 + x y}{4}, \quad | x | <   1, | y | <   1.
$$

证明 $\xi, \eta$ 不相互独立, 但 $\xi^2, \eta^2$ 相互独立.

证明 首先算出边缘分布密度, 对 $|x| < 1, |y| < 1$ 有

$$
p _ {\xi} (x) = \int_ {- 1} ^ {1} \frac {1 + x y}{4} \mathrm{d} y = \frac {1}{2}, \quad p _ {\eta} (y) = \int_ {- 1} ^ {1} \frac {1 + x y}{4} \mathrm{d} x = \frac {1}{2}.
$$

因 (3.2.5) 式不成立, 故知 $\xi, \eta$ 不独立. 当 $x \geqslant 0, y \geqslant 0$ 时有

$$
\mathbf {P} (\xi^ {2} \leqslant x) = \mathbf {P} (| \xi | \leqslant \sqrt {x}) = \sqrt {x}, \quad \mathbf {P} (\eta^ {2} \leqslant y) = \sqrt {y}
$$

和

$$
\mathbf {P} (\xi^ {2} \leqslant x, \eta^ {2} \leqslant y) = \mathbf {P} (| \xi | \leqslant \sqrt {x}, | \eta | \leqslant \sqrt {y})
$$

---

78

第三章 随机向量和独立性

$$
= \int_ {- \sqrt {x}} ^ {\sqrt {x}} \int_ {- \sqrt {y}} ^ {\sqrt {y}} \frac {1 + u v}{4} \mathrm{d} u \mathrm{d} v = \sqrt {x} \sqrt {y},
$$

故 $F_{(\xi^2,\eta^2)}(x,y) = F_{\xi^2}(x)F_{\eta^2}(y)$. 因此 $\xi^2, \eta^2$ 相互独立.

定理3.2.5 设 $\xi_{1}$ 和 $\eta_{2}$ 分别是概率空间 $(\Omega_1, \mathcal{F}_1, \mathbf{P}_1)$ 和 $(\Omega_2, \mathcal{F}_2, \mathbf{P}_2)$ 上的随机变量. 令 $(\Omega, \mathcal{F}, \mathbf{P}) = (\Omega_1 \times \Omega_2, \mathcal{F}_1 \times \mathcal{F}_2, \mathbf{P}_1 \times \mathbf{P}_2)$. 再定义

$$
\xi (\omega) = \xi_ {1} (\omega_ {1}), \eta (\omega) = \eta_ {2} (\omega_ {2}), \quad \omega = (\omega_ {1}, \omega_ {2}) \in \Omega . \tag {3.2.6}
$$

则如下性质成立:

(1)  $\xi,\eta$  是概率空间  $(\Omega,\mathcal{F},\mathbf{P})$  上的随机变量且相互独立;
(2) $\xi$ 与 $\xi_{1}$ 有相同分布, 而 $\eta$ 与 $\eta_{2}$ 有相同分布.

证明 首先, 注意对任何 $A, B \in \mathcal{B}$, 有

$$
\{\xi_ {1} \in A \} = \xi_ {1} ^ {- 1} (A) \in \mathscr {F} _ {1}, \quad \{\eta_ {2} \in B \} = \eta_ {2} ^ {- 1} (B) \in \mathscr {F} _ {2}.
$$

由 (3.2.6) 式及乘积 $\sigma$ 代数 $\mathcal{F} = \mathcal{F}_1 \times \mathcal{F}_2$ 的定义有

$$
\{\xi \in A \} = \{\xi_ {1} \in A \} \times \Omega_ {2} \in \mathscr {F}, \{\eta \in B \} = \Omega_ {1} \times \{\eta_ {2} \in B \} \in \mathscr {F}.
$$

根据乘积概率测度的定义得

$$
\mathbf {P} (\xi \in A) = \mathbf {P} _ {1} (\xi_ {1} \in A) \mathbf {P} _ {2} (\Omega_ {2}) = \mathbf {P} _ {1} (\xi_ {1} \in A)
$$

和

$$
\mathbf {P} (\eta \in B) = \mathbf {P} _ {1} (\Omega_ {1}) \mathbf {P} _ {2} (\eta_ {2} \in B) = \mathbf {P} _ {2} (\eta_ {2} \in B).
$$

所以 $\xi$ 与 $\xi_{1}$ 同分布, 而 $\eta$ 与 $\eta_{2}$ 同分布. 注意

$$
\{\xi \in A, \eta \in B \} = \{\xi_ {1} \in A \} \times \{\eta_ {2} \in B \} \in \mathscr {F}.
$$

再由乘积概率测度的定义有

$$
\mathbf {P} (\xi \in A, \eta \in B) = \mathbf {P} _ {1} (\xi_ {1} \in A) \mathbf {P} _ {2} (\eta_ {2} \in B) = \mathbf {P} (\xi \in A) \mathbf {P} (\eta \in B).
$$

这说明 $\xi$ 和 $\eta$ 相互独立.

定理 3.2.5 与前面的定理 2.4.3 相结合, 给出了构造具有任意边缘分布的独立随机变量的方法.

---

3.2 条件分布与独立性

79

## 3.2.3 多个随机变量的独立性

定义 3.2.5 称概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的 n 个随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  独立，是指它们生成的  $\sigma$  代数  $\sigma(\xi_{1}), \sigma(\xi_{2}), \cdots, \sigma(\xi_{n})$  独立，即对于任意的  $B_{1} \in B, B_{2} \in B, \cdots, B_{n} \in B$  都有

$$
\mathbf {P} (\xi_ {1} \in B _ {1}, \xi_ {2} \in B _ {2}, \dots , \xi_ {n} \in B _ {n}) = \mathbf {P} (\xi_ {1} \in B _ {1}) \mathbf {P} (\xi_ {2} \in B _ {2}) \dots \mathbf {P} (\xi_ {n} \in B _ {n}). \tag {3.2.7}
$$

由定义不难看出, 若  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立, 则从中去掉若干随机变量后得到的随机变量组  $\xi_{n_{1}}, \xi_{n_{2}}, \cdots, \xi_{n_{k}}$  也是相互独立的. 前面证明的关于两个随机变量的独立性的结果可以容易地推广到多个随机变量的情况. 例如, 我们有

定理 3.2.6 随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立当且仅当随机向量  $(\xi_{1}, \xi_{2}, \cdots, \xi_{n})$  的联合分布函数等于其边缘分布函数的乘积，即

$$
F (x _ {1}, x _ {2}, \dots , x _ {n}) = F _ {1} (x _ {1}) F _ {2} (x _ {2}) \dots F _ {n} (x _ {n}), \quad x _ {1}, x _ {2}, \dots , x _ {n} \in \mathbb {R}. \tag {3.2.8}
$$

独立性的概念可以容易地推广到任意多个随机变量或随机向量的情况. 例如, 我们有

定义3.2.6 称概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的一族随机变量 $X_{i}, i \in I$ 独立, 是指它们生成的 $\sigma$ 代数 $\sigma(X_{i}), i \in I$ 独立.

特别地, 一随机变量列 $\xi_1, \xi_2, \cdots$ 独立当且仅当对于任意的 $n \geqslant 2$ 有限随机变量列 $\xi_1, \xi_2, \cdots, \xi_n$ 独立. 与定理3.2.5类似, 利用乘积概率空间, 可构造任意个独立随机变量.

例 3.2.6 令  $\xi_{1}, \xi_{2}, \cdots$  是例 2.2.1 中定义的可数无穷维乘积伯努利空间上的随机变量. 注意

$$
\mathbf {P} (\xi_ {k} = 1) = \mathbf {P} (B _ {k}) = p, \quad \mathbf {P} (\xi_ {k} = 0) = \mathbf {P} (B _ {k} ^ {c}) = 1 - p,
$$

其中 $0 \leqslant p \leqslant 1$. 由于事件 $B_{1}, B_{2}, \cdots$ 相互独立, 易见随机变量 $\xi_{1}, \xi_{2}, \cdots$ 相互独立.

例 3.2.7 设  $\zeta_{1}, \zeta_{2}, \cdots$  是定义在概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的一列独立的随机变量列且有  $\mathbf{P}(\zeta_{k}=1)=p$  和  $\mathbf{P}(\zeta_{k}=-1)=q$ ，其中 q=1-p。取定  $i\in Z$ ，并令  $S_{0}=i$  和

$$
S _ {n} = i + \zeta_ {1} + \zeta_ {2} + \dots + \zeta_ {n}, \quad n \geqslant 1.
$$

由定理3.1.3知 $S_{n}$ 是随机变量. 称 $(S_{n}: n \geqslant 0)$ 为从 $i$ 出发的（一维）简单随机游动. 给定整数 $a$, 称 $\tau_{a} := \inf \{n \geqslant 0 : S_{n} = a\}$ 为 $(S_{n}: n \geqslant 0)$ 对于 $a$ 的首达时. 显然, 对整数 $k \geqslant 0$ 有

$$
\{\tau_ {a} = k \} = \{S _ {0} \neq a \} \cap \{S _ {1} \neq a \} \cap \dots \cap \{S _ {k - 1} \neq a \} \cap \{S _ {k} = a \} \in \mathscr {F}.
$$

所以该首达时是 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的随机变量. 再任取整数 $c$. 若 $c = a$, 则

$$
\{S _ {n \wedge \tau_ {a}} = c \} = \{S _ {n \wedge \tau_ {a}} = a \} = \{\tau_ {a} \leqslant n \} \in \mathscr {F},
$$

---

80

第三章 随机向量和独立性

其中 $n \wedge \tau_{a} = \min(n, \tau_{a})$. 若 $c \neq a$, 则

$$
\{S _ {n \wedge \tau_ {a}} = c \} = \{n <   \tau_ {a} \} \cap \{S _ {n} = c \} \in \mathcal {F}.
$$

所以 $X_{n}:= S_{n\wedge \tau_{a}}$ 是随机变量, 称 $(X_{n}:n\geqslant 0)$ 为具有吸收态 $a$ 的简单随机游动.

## \*3.2.4 伊辛模型

令 $S$ 为 $d$ 维整数格点空间 $\mathbb{Z}^d$ 的有限子集, 再令 $X = \{-1, 1\}^S$ 为乘积空间. 注意 $X$ 为有限集, 令 $\mathcal{F}$ 为 $X$ 的全体子集构成的 $\sigma$ 代数. 给定常数 $\beta > 0$, 可以在 $(X, \mathcal{F})$ 上定义唯一的概率测度 $G_{\beta}$ 使得

$$
G _ {\beta} (\sigma) = Z _ {\beta} ^ {- 1} \exp \left\{\sum_ {| i - j | = 1} \beta \sigma_ {i} \sigma_ {j} \right\}, \quad \sigma = (\sigma_ {i}) \in X, \tag {3.2.9}
$$

其中 $|\cdot|$ 表示欧氏距离，而

$$
Z _ {\beta} = \sum_ {\sigma \in X} \exp \left\{\sum_ {| i - j | = 1} \beta \sigma_ {i} \sigma_ {j} \right\}. \tag {3.2.10}
$$

显然 $(\sigma_{i}:i\in S)$ 是概率空间 $(X,\mathcal{F},G_{\beta})$ 上的随机向量. 物理中称概率测度 $G_{\beta}$ 为吉布斯 (Gibbs) 态, 它描述了 $S$ 代表的铁磁体达到磁平衡时的状态, 而 $(\sigma_{i}:i\in S)$ 给出了 $S$ 中的所有铁原子的磁极的方向. 常数 $\beta >0$ 为绝对温度的倒数, 称为反温度, 它决定了铁原子间的磁力相对于热运动的作用强度. 该模型称为伊辛 (Ising) 模型; 详见 [2,14].

对于伊辛模型, 人们关心的一个基本问题是当 $S$ 扩展为无穷集时, 相应的吉布斯态 $G_{\beta}$ 的合理的扩展是否唯一. 若这样的扩展唯一, 则称铁磁体 $S$ 没有相变, 否则称该铁磁体有相变. 在伊辛模型中, 将 (3.2.9) 式和 (3.2.10) 式中求和的限制条件 $|i - j| = 1$ 去掉, 改为对所有 $i, j \in S$ 求和, 就得到居里-外斯 (Curie-Weiss) 模型.

与伊辛模型类似的磁体相变模型还有自旋玻璃 (Spin Glass) 模型, 包括爱德华兹-安德森 (Edwards-Anderson) 模型和谢灵顿-柯克帕特里克 (Sherrington-Kirkpatrick) 模型, 二者的定义都要用到由独立同分布正态随机变量构成的随机矩阵, 关于这些模型仍有很多困难的理论问题需要解决; 详见 [16, 17].

## 练习题

1. 设矩形 $(0, \pi / 2)^2$ 上的随机向量 $(\xi, \eta)$ 有联合分布密度 $p(x, y) = \frac{1}{2} \sin (x + y)$. 对于 $0 < y < \pi / 2$ 求给定 $\eta = y$ 时 $\xi$ 的条件密度函数.
2. 设 $\eta$ 服从几何分布 $G(\lambda)$. 令 $\xi$ 是成功概率为 $p (0 < p < 1)$ 的 $\eta$ 重伯努利试验的成功次数. 求离散型随机向量 $(\xi, \eta)$ 的联合分布列.

---

3.3 随机向量函数的分布

81

3. 设 $\eta$ 服从指数分布 $E(\lambda)$, 而在给定 $\eta$ 的条件下 $\xi$ 服从正态分布 $N(0, \eta^2)$. 求绝对连续型随机向量 $(\xi, \eta)$ 的联合分布密度.
4. 设随机向量 $(\xi, \eta)$ 的联合分布密度为 $p(x, y) = 4xy1_{\{0 < x, y < 1\}}$. 求 $\xi$ 和 $\eta$ 的边缘分布密度, 并证明 $\xi$ 和 $\eta$ 相互独立.
5. 设随机向量 $(\xi, \eta)$ 的联合分布密度为 $p(x, y) = 8xy1_{\{0 < x < y < 1\}}$. 求 $\xi$ 和 $\eta$ 的边缘分布密度, 并说明 $\xi$ 和 $\eta$ 是否相互独立.
6. 通过独立可数重伯努利试验构造一独立同分布的随机变量列 $Z_{1}, Z_{2}, \cdots$, 使其满足 $\mathbf{P}(Z_{k} = 1) = p$ 和 $\mathbf{P}(Z_{k} = -1) = 1 - p$, 其中 $0 \leqslant p \leqslant 1$.

## 3.3 随机向量函数的分布

前面我们曾经利用均匀分布变量与广义逆的复合构造了任意概率分布函数的随机变量. 事实上, 通过随机变量与一般可测函数的复合, 可以构造出很多有用的随机变量, 从而为随机现象的描述和研究提供便利.

## 3.3.1 一维随机变量的函数

设 $\xi$ 为概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的随机变量, 而 $f$ 为 $\mathbb{R}$ 上的可测函数. 由定理2.1.8知 $\zeta := f(\xi)$ 也是随机变量, 其分布函数可以通过下式确定:

$$
F _ {\zeta} (z) = \mathbf {P} (f (\xi) \leqslant z), \quad z \in \mathbb {R}. \tag {3.3.1}
$$

离散型随机变量的函数的分布可以如下确定: 设  $\xi$  是取值于  $\{x_{i}: i=1,2,\cdots\}$  的离散型随机变量且有分布列

$$
p (x _ {i}) = \mathbf {P} (\xi = x _ {i}), \quad i = 1, 2, \dots .
$$

令  $\{z_{k}:k=1,2,\cdots\}$  是去除数列  $\{f(x_{i}):i=1,2,\cdots\}$  中多余的重复元素所得的集合.
则  $\zeta := f(\xi)$  是取值于  $\{z_{k}: k = 1, 2, \cdots\}$  的离散型随机变量且有分布列

$$
q (z _ {k}) = \mathbf {P} (\zeta = z _ {k}) = \sum_ {f (x _ {i}) = z _ {k}} p (x _ {i}), \quad k = 1, 2, \dots . \tag {3.3.2}
$$

例3.3.1 设随机变量 $\eta$ 服从几何分布 $G(p)$, 其中 $0 < p < 1$. 求 $X = (-1)^{\eta}$ 的分布.

解 显然 $X$ 可能的取值为 $-1$ 和 1. 根据假定对 $k \geqslant 1$ 有 $\mathbf{P}(\eta = k) = (1 - p)^{k - 1}p$.

---

82

第三章 随机向量和独立性

所以

$$
\begin{array}{l} \mathbf {P} (X = - 1) = \sum_ {n = 0} ^ {\infty} \mathbf {P} (\eta = 2 n + 1) = \sum_ {n = 0} ^ {\infty} (1 - p) ^ {2 n} p \\ = \frac {p}{1 - (1 - p) ^ {2}} = \frac {1}{2 - p}, \\ \end{array}
$$

进而

$$
\mathbf {P} (X = 1) = \frac {1 - p}{2 - p}.
$$

例3.3.2 设 $\xi$ 服从均匀分布 $U(-\pi / 2, \pi / 2)$. 求 $\eta = \tan \xi$ 的分布.

解 因为 $\xi$ 有密度函数 $q(x) = 1 / \pi, |x| < \pi / 2$, 对于 $y \in \mathbb{R}$ 有

$$
\begin{array}{l} F _ {\eta} (y) = \mathbf {P} (\tan \xi \leqslant y) \\ = \mathbf {P} (\xi \leqslant \arctan y, | \xi | <   \pi / 2) \\ = \int_ {- \frac {\pi}{2}} ^ {\arctan y} \frac {1}{\pi} \mathrm{d} x = \left. \frac {1}{\pi} x \right| _ {- \frac {\pi}{2}} ^ {\arctan y} \\ = \frac {1}{\pi} \arctan y + \frac {1}{2} \\ \end{array}
$$

求导得 $\eta$ 的密度函数为

$$
p (y) = \frac {1}{\pi (1 + y ^ {2})}, \quad y \in \mathbb {R}.
$$

直线上的绝对连续型概率分布称为具有参数 $a \in \mathbb{R}$ 和 $\lambda > 0$ 的柯西 (Cauchy) 分布, 是指它有密度函数

$$
p (x) = \frac {1}{\pi [ \lambda^ {2} + (x - a) ^ {2} ]}, \quad x \in \mathbb {R}.
$$

所以例 3.3.2 中得到的分布是柯西分布当 a = 0,  $\lambda = 1$  时的特殊形式.

注意, 例 3.3.2 的计算中用到了函数 $y = \tan x$ 在 $(- \pi / 2, \pi / 2)$ 内的严格单增性质. 在这种情况下, 有 $\tan \xi \leqslant y$ 当且仅当 $\xi \leqslant \arctan y$, $|\xi| < \pi / 2$.

定理3.3.1 设区间 $(a, b)$ 上的绝对连续型随机变量 $\xi$ 有密度函数 $p$, 而函数 $f$ 在 $(a, b)$ 上可导且单调. 令 $\alpha = f(a) \wedge f(b)$ 和 $\beta = f(a) \vee f(b)$. 再令 $h: (\alpha, \beta) \to (a, b)$ 为 $f$ 的反函数. 则 $\eta := f(\xi)$ 为区间 $(\alpha, \beta)$ 上的绝对连续型随机变量且有密度函数

$$
p _ {\eta} (y) = p (h (y)) | h ^ {\prime} (y) |, \quad y \in (\alpha , \beta).
$$

证明 不妨设函数 $f$ 在 $(a, b)$ 上不降. 则 $\eta$ 有分布函数

$$
F _ {\eta} (y) = \mathbf {P} (f (\xi) \leqslant y) = \int_ {\{\alpha <   f (x) \leqslant y \}} p (x) \mathrm{d} x, \quad y \in (\alpha , \beta).
$$

---

3.3 随机向量函数的分布

83

注意 $\alpha = f(a)$. 令 $x = h(t)$, 利用换元法计算积分得

$$
F _ {\eta} (y) = \int_ {\alpha} ^ {y} p (h (t)) h ^ {\prime} (t) \mathrm{d} t.
$$

对上式求导即得  $\eta$  的密度函数  $p_{\eta}$  的表达式.

上面定理的证明包含了求解绝对连续型随机变量函数密度方法的基本思想. 在实际问题中, 往往需要根据具体情况灵活运用.

例3.3.3 设 $\xi$ 服从正态分布 $N(0,1)$. 求 $\eta = \xi^2$ 的分布.

解 显然, 可以认为 $\eta = \xi^2$ 以概率 1 取值于开区间 $(0, \infty)$. 对 $y > 0$ 有

$$
F (y) = \mathbf {P} (| \xi | \leqslant \sqrt {y}) = \int_ {- \sqrt {y}} ^ {\sqrt {y}} \frac {1}{\sqrt {2 \pi}} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x = \sqrt {2} \int_ {0} ^ {\sqrt {y}} \frac {1}{\sqrt {\pi}} \mathrm{e} ^ {- \frac {x ^ {2}}{2}} \mathrm{d} x.
$$

求导得 $\eta$ 的密度函数

$$
p (y) = \frac {1}{\sqrt {2 \pi y}} \mathrm{e} ^ {- \frac {y}{2}}, \quad y > 0.
$$

半直线 $(0,\infty)$ 上的绝对连续型分布称为卡方分布, 并记作 $\chi^2 (n)$, 是指它有密度函数

$$
p _ {n} (y) = \frac {1}{2 ^ {\frac {n}{2}} \Gamma \left(\frac {n}{2}\right)} y ^ {\frac {n}{2} - 1} \mathrm{e} ^ {- \frac {y}{2}}, \quad y > 0.
$$

参数 $n$ 称为 $\chi^2 (n)$ 的自由度. 注意 $\chi^2 (n)$ 就是伽马分布 $\Gamma(1 / 2, n / 2)$. 例3.3.3中得到的分布就是自由度为1的卡方分布.

定理3.3.2 设随机变量 $\xi$ 和 $\eta$ 独立. 则对任何博雷尔可测函数 $f$ 和 $g$, 随机变量 $f(\xi)$ 和 $g(\eta)$ 也相互独立.

证明 因为 $f, g$ 是博雷尔可测函数, 由定理2.1.8知 $f(\xi), g(\eta)$ 都是随机变量. 对任意的 $A, B \in \mathcal{B}$ 有 $f^{-1}(A), g^{-1}(B) \in \mathcal{B}$. 故由 $\xi$ 和 $\eta$ 的独立性,

$$
\begin{array}{l} \mathbf {P} \{f (\xi) \in A, g (\eta) \in B \} = \mathbf {P} \{\xi \in f ^ {- 1} (A), \eta \in g ^ {- 1} (B) \} \\ = \mathbf {P} \{\xi \in f ^ {- 1} (A) \} \mathbf {P} (\eta \in g ^ {- 1} (B) \} \\ = \mathbf {P} \{f (\xi) \in A \} \mathbf {P} \{g (\eta) \in B \}. \\ \end{array}
$$

所以 $f(\xi)$ 和 $g(\eta)$ 相互独立.

## 3.3.2 二维随机向量的函数

设 $(\xi, \eta)$ 为概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的二维随机向量, 而 $f$ 为 $\mathbb{R}^2$ 上的可测函数. 由定理3.1.3知 $\zeta := f(\xi, \eta)$ 也是随机变量, 其分布函数可以通过下式确定:

$$
F (z) = \mathbf {P} \{f (\xi , \eta) \leqslant z \}, \quad z \in \mathbb {R}. \tag {3.3.3}
$$

---

84

第三章 随机向量和独立性

下面的定理显然成立.

定理 3.3.3（和的分布列） 若  $(\xi,\eta)$  为取非负整数值的离散型随机向量且有联合分布列

$$
p (i, j) = \mathbf {P} (\xi = i, \eta = j), \quad i, j = 0, 1, 2, \dots .
$$

则 $\zeta := \xi + \eta$ 为离散型随机变量且有分布

$$
\mathbf {P} (\zeta = k) = \sum_ {(i, j): i + j = k} p (i, j) = \sum_ {i = 0} ^ {k} p (i, k - i) = \sum_ {j = 0} ^ {k} p (k - j, j), \tag {3.3.4}
$$

其中  $k=0,1,2,\cdots$

例3.3.4 设 $\xi, \eta$ 分别服从二项分布 $B(n, p)$ 和 $B(m, p)$ 且相互独立. 根据 (3.3.4) 式有

$$
\begin{array}{l} \mathbf {P} (\xi + \eta = k) = \sum_ {i = 0} ^ {k} \mathrm{C} _ {n} ^ {i} p ^ {i} q ^ {n - i} \mathrm{C} _ {m} ^ {k - i} p ^ {k - i} q ^ {m - k + i} \\ = p ^ {k} q ^ {n + m - k} \sum_ {i = 0} ^ {k} \mathrm{C} _ {n} ^ {i} \mathrm{C} _ {m} ^ {k - i} = \mathrm{C} _ {n + m} ^ {k} p ^ {k} q ^ {n + m - k}. \\ \end{array}
$$

因此 $\xi +\eta$ 服从分布 $B(m + n,p)$ .此性质称为二项分布的再生性.

例3.3.5 设 $\xi, \eta$ 分别服从泊松分布 $P(\lambda_1), P(\lambda_2)$ 且相互独立. 利用 (3.3.4) 式有

$$
\begin{array}{l} \mathbf {P} (\xi + \eta = k) = \sum_ {i = 0} ^ {k} \frac {\lambda_ {1} ^ {i}}{i !} \mathrm{e} ^ {- \lambda_ {1}} \frac {\lambda_ {2} ^ {k - i}}{(k - i) !} \mathrm{e} ^ {- \lambda_ {2}} \\ = \mathrm{e} ^ {- \lambda_ {1} - \lambda_ {2}} \frac {1}{k !} \sum_ {i = 0} ^ {k} \frac {k !}{i ! (k - i) !} \lambda_ {1} ^ {i} \lambda_ {2} ^ {k - i} \\ = \frac {1}{k !} (\lambda_ {1} + \lambda_ {2}) ^ {k} \mathrm{e} ^ {- \lambda_ {1} - \lambda_ {2}}, \\ \end{array}
$$

故 $\xi +\eta$ 服从分布 $P(\lambda_1 + \lambda_2)$ .此性质称为泊松分布的再生性.

定理3.3.4（和的密度函数） 若 $(\xi, \eta)$ 为绝对连续型随机向量且有联合分布密度 $p(x, y)$，则 $\zeta := \xi + \eta$ 为绝对连续型随机变量且有密度函数

$$
p _ {\zeta} (z) = \int_ {- \infty} ^ {\infty} p (x, z - x) \mathrm{d} x = \int_ {- \infty} ^ {\infty} p (z - y, y) \mathrm{d} y, \quad z \in \mathbb {R}. \tag {3.3.5}
$$

证明 根据 (3.3.3) 式有

$$
\begin{array}{l} F _ {\xi + \eta} (z) = \iint_ {\{x + y \leqslant z \}} p (x, y) \mathrm{d} x \mathrm{d} y = \int_ {- \infty} ^ {\infty} \mathrm{d} x \int_ {- \infty} ^ {z - x} p (x, y) \mathrm{d} y \\ = \int_ {- \infty} ^ {\infty} \mathrm{d} x \int_ {- \infty} ^ {z} p (x, v - x) \mathrm{d} v = \int_ {- \infty} ^ {z} \mathrm{d} v \int_ {- \infty} ^ {\infty} p (x, v - x) \mathrm{d} x. \\ \end{array}
$$

对上式求导知欲证等式中的第一个等号成立, 同理可知第二个等号成立.

![](../../raw/pages_0097-0112/images/page_98_image_19.jpg)

---

3.3 随机向量函数的分布

85

我们分别称 (3.3.4) 式和 (3.3.5) 式为离散型和绝对连续型随机向量的卷积公式.

例 3.3.6 设  $X_{1}, X_{2}, \cdots, X_{n}$  相互独立且均服从指数分布  $E(\lambda)$ . 证明  $\eta_{n} := X_{1} + X_{2} + \cdots + X_{n}$  服从伽马分布  $\Gamma(\lambda, n)$ .

证明 利用数学归纳法证明. 显然, 当 $n = 1$ 时结论成立, 即 $\eta_1 = X_1$ 有密度函数 $p_1(x) = \lambda \mathrm{e}^{-\lambda x}, x > 0$. 设 $\eta_{n-1}$ 服从伽马分布 $\Gamma(\lambda, n-1)$, 即它有密度函数

$$
p _ {n - 1} (x) = \frac {\lambda^ {n - 1}}{\Gamma (n - 1)} x ^ {n - 2} \mathrm{e} ^ {- \lambda x}, \quad x > 0.
$$

注意 $\eta_{n} = \eta_{n - 1} + X_{n}$ ，其中 $X_{n}$ 有密度函数 $p_1$ .利用卷积公式知 $\eta_{n}$ 有密度函数

$$
\begin{array}{l} p _ {n} (z) = \int_ {- \infty} ^ {\infty} p _ {n - 1} (x) p _ {1} (z - x) \mathrm{d} x \\ = \frac {\lambda^ {n}}{\Gamma (n - 1)} \int_ {0} ^ {z} x ^ {n - 2} \mathrm{e} ^ {- \lambda z} \mathrm{d} x = \frac {\lambda^ {n}}{\Gamma (n)} z ^ {n - 1} \mathrm{e} ^ {- \lambda z}, \quad z > 0 \\ \end{array}
$$

即  $\eta_{n}$  服从伽马分布  $\Gamma(\lambda, n)$ .

定理 3.3.5（积的密度函数） 若绝对连续型随机向量  $(\xi,\eta)$  有联合分布密度  $p(x,y)$ ，则  $\xi\eta$  为绝对连续型随机变量且有密度函数

$$
p _ {\xi \eta} (z) = \int_ {- \infty} ^ {\infty} | y | ^ {- 1} p (y ^ {- 1} z, y) 1 _ {\{y \neq 0 \}} \mathrm{d} y, \quad z \in \mathbb {R}.
$$

证明 在假设条件之下, 我们来计算 $\xi \eta$ 的分布函数 $F_{\xi \eta}$. 注意 $\eta$ 为绝对连续型随机变量. 故对于 $z \in \mathbb{R}$ 有

$$
\begin{array}{l} F _ {\xi \eta} (z) = \mathbf {P} (\xi \eta \leqslant z, \eta \neq 0) = \iint_ {\{x y <   z, y \neq 0 \}} p (x, y) \mathrm{d} x \mathrm{d} y \\ = \iint_ {\{x <   y ^ {- 1} z, y > 0 \}} p (x, y) \mathrm{d} x \mathrm{d} y + \iint_ {\{x > y ^ {- 1} z, y <   0 \}} p (x, y) \mathrm{d} x \mathrm{d} y \\ = \int_ {0} ^ {\infty} \mathrm{d} y \int_ {- \infty} ^ {y ^ {- 1} z} p (x, y) \mathrm{d} x + \int_ {- \infty} ^ {0} \mathrm{d} y \int_ {y ^ {- 1} z} ^ {\infty} p (x, y) \mathrm{d} x \\ = \int_ {0} ^ {\infty} \mathrm{d} y \int_ {- \infty} ^ {z} y ^ {- 1} p (y ^ {- 1} u, y) \mathrm{d} u + \int_ {- \infty} ^ {0} \mathrm{d} y \int_ {z} ^ {- \infty} y ^ {- 1} p (y ^ {- 1} u, y) \mathrm{d} u \\ = \int_ {- \infty} ^ {z} \mathrm{d} u \int_ {- \infty} ^ {\infty} | y | ^ {- 1} p (y ^ {- 1} u, y) 1 _ {\{y \neq 0 \}} \mathrm{d} y. \\ \end{array}
$$

这里应用了积分变量替换 $x = y^{-1}u$。对上式求导即得 $p_{\xi \eta}(z)$ 的表达式。

## 3.3.3 多维随机向量的函数

在应用中, 我们经常需要计算多个独立随机变量的最大或最小值的分布. 这时独立性假定可以大为化简相应的计算. 这里只讨论绝对连续型随机向量的情况. 离散型随机向量的情况可以类似地处理.

---

86

第三章 随机向量和独立性

例 3.3.7 设  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  相互独立且均服从参数为  $\lambda > 0$  的指数分布。证明  $\eta := \xi_{1} \wedge \xi_{2} \wedge \cdots \wedge \xi_{n}$  服从参数为  $n\lambda > 0$  的指数分布。

证明 根据假设, 对任何 x > 0 有  $\mathbf{P}(\xi_{i} > x) = \mathrm{e}^{-\lambda x}$ . 再由  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  的独立性得

$$
\begin{array}{l} \mathbf {P} (\eta > x) = \mathbf {P} (\xi_ {1} > x, \xi_ {2} > x, \dots , \xi_ {n} > x) \\ = \mathbf {P} (\xi_ {1} > x) \mathbf {P} (\xi_ {2} > x) \dots \mathbf {P} (\xi_ {n} > x) = \mathrm{e} ^ {- n \lambda x}, \\ \end{array}
$$

故

$$
F _ {\eta} (x) = \mathbf {P} (\eta \leqslant x) = 1 - \mathrm{e} ^ {- n \lambda x}.
$$

所以  $\eta$  服从参数为  $n\lambda > 0$  的指数分布.

定理 3.3.6（最大最小值的分布）设  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  为独立随机变量，有共同的分布函数  $F(x)$  与密度函数  $p(x)$ . 令  $\eta = \xi_{1} \wedge \xi_{2} \wedge \cdots \wedge \xi_{n}$  和  $\zeta = \xi_{1} \vee \xi_{2} \vee \cdots \vee \xi_{n}$ . 则  $(\eta, \zeta)$  有联合密度

$$
p _ {(\eta , \zeta)} (x, y) = n (n - 1) [ F (y) - F (x) ] ^ {n - 2} p (x) p (y), \quad x <   y.
$$

证明 当 $x \geqslant y$ 时,

$$
F _ {(\eta , \zeta)} (x, y) = \mathbf {P} (\eta \leqslant x, \zeta \leqslant y) = \mathbf {P} (\xi_ {1} \leqslant y, \xi_ {2} \leqslant y, \dots , \xi_ {n} \leqslant y) = F (y) ^ {n}.
$$

当 x < y 时,

$$
\begin{array}{l} F _ {(\eta , \zeta)} (x, y) = \mathbf {P} (\eta \leqslant x, \zeta \leqslant y) = \mathbf {P} (\zeta \leqslant y) - \mathbf {P} (\eta > x, \zeta \leqslant y) \\ = \mathbf {P} (\xi_ {1} \leqslant y, \xi_ {2} \leqslant y, \dots , \xi_ {n} \leqslant y) - \mathbf {P} (x <   \xi_ {1} \leqslant y, x <   \xi_ {2} \leqslant y, \dots , x <   \xi_ {n} \leqslant y) \\ = F (y) ^ {n} - [ F (y) - F (x) ] ^ {n}. \\ \end{array}
$$

对 x, y 求导即得  $p_{(\eta,\zeta)}(x,y)$  的表达式.

例 3.3.8 向区间  $(0,1)$  中独立地随机投掷 n 个点. 求这些个点全分布在长为 1/2 的子区间内的概率.

解 以  $\xi_{i}$  表示第 i 个点的坐标,  $i=1,2,\cdots,n$ . 根据假设, 这些随机变量相互独立, 且每个  $\xi_{i}$  服从分布  $U(0,1)$ . 令  $\eta=\xi_{1}\wedge\xi_{2}\wedge\cdots\wedge\xi_{n}$  和  $\zeta=\xi_{1}\vee\xi_{2}\vee\cdots\vee\xi_{n}$ . 根据定理 3.3.6,

$$
\begin{array}{l} \mathbf {P} (\zeta - \eta <   1 / 2) = \iint_ {\{y - x <   1 / 2, 0 <   x <   y <   1 \}} n (n - 1) (y - x) ^ {n - 2} \mathrm{d} x \mathrm{d} y \\ = \int_ {0} ^ {1 / 2} \mathrm{d} x \int_ {x} ^ {x + 1 / 2} n (n - 1) (y - x) ^ {n - 2} \mathrm{d} y + \\ \end{array}
$$

---

3.3 随机向量函数的分布

87

$$
\begin{array}{l} \int_ {1 / 2} ^ {1} \mathrm{d} x \int_ {x} ^ {1} n (n - 1) (y - x) ^ {n - 2} \mathrm{d} y \\ = \int_ {0} ^ {1 / 2} \left[ n (y - x) ^ {n - 1} \Big | _ {y = x} ^ {y = x + 1 / 2} \right] \mathrm{d} x + \\ \int_ {1 / 2} ^ {1} \left[ n (y - x) ^ {n - 1} \Big | _ {y = x} ^ {y = 1} \right] \mathrm{d} x \\ = \int_ {0} ^ {1 / 2} \frac {n}{2 ^ {n - 1}} \mathrm{d} x + \int_ {1 / 2} ^ {1} n (1 - x) ^ {n - 1} \mathrm{d} x = \frac {n + 1}{2 ^ {n}}. \\ \end{array}
$$

此即为所求概率.

![](../../raw/pages_0097-0112/images/page_101_image_4.jpg)

与定理 3.3.2 类似地可以证明:

定理 3.3.7 设随机向量  $\xi := (\xi_{1}, \xi_{2}, \cdots, \xi_{m})$  和  $\eta := (\eta_{1}, \eta_{2}, \cdots, \eta_{n})$  独立. 再设 f 和 g 分别为  $R^{m}$  和  $R^{n}$  上的博雷尔可测函数. 则随机变量  $f(\xi)$  和  $g(\eta)$  也相互独立.

## \*3.3.4 随机向量的向量值函数

在本小节中, 我们讨论绝对连续型随机向量的向量值函数的分布问题.

定理3.3.8 若 $(\xi, \eta)$ 为绝对连续型随机向量且有联合分布密度 $p(x, y)$，则 $(\xi, -\eta)$ 为绝对连续型随机向量且有联合分布密度 $p(x, -y)$.

证明 根据假设, 对于任何 $x, y \in \mathbb{R}$, 作积分变量替换 $v = -w$, 我们有

$$
\begin{array}{l} \mathrm{P} (\xi \leqslant x, - \eta \leqslant y) = \iint_ {\{u \leqslant x, - v \leqslant y \}} p (u, v) \mathrm{d} u \mathrm{d} v \\ = \iint_ {\{u \leqslant x, w \leqslant y \}} p (u, - w) \mathrm{d} u \mathrm{d} w. \\ \end{array}
$$

所以 $(\xi,-\eta)$ 为绝对连续型随机向量且有联合分布密度 $p(x,-y)$ .

推论 3.3.9 若  $(\xi,\eta)$  为绝对连续型随机向量且有联合分布密度  $p(x,y)$ ，则  $\zeta:=\xi-\eta$  为绝对连续型随机变量且有密度

$$
p _ {\zeta} (z) = \int_ {- \infty} ^ {\infty} p (x, x - z) \mathrm{d} x = \int_ {- \infty} ^ {\infty} p (z - y, - y) \mathrm{d} y, \quad z \in \mathbb {R}.
$$

定理3.3.10 若 $(\xi, \eta)$ 为绝对连续型随机向量且有联合分布密度 $p(x, y)$，则 $(\xi, \eta^{-1})$ 为绝对连续型随机向量且有联合分布密度 $p(x, y^{-1})y^{-2}1_{\{y \neq 0\}}$.

证明 在假设条件之下 $\eta$ 为绝对连续型随机变量, 故 $\mathbf{P}(\eta = 0) = 0$. 因此, 对任何 $x, y \in \mathbb{R}$ 有

$$
\begin{array}{l} \mathrm{P} (\xi \leqslant x, 1 / \eta \leqslant y) = \iint_ {\{u \leqslant x, 1 / v \leqslant y, v \neq 0 \}} p (u, v) \mathrm{d} v \\ = \iint_ {\{u \leqslant x, w \leqslant y, w \neq 0 \}} p (u, w ^ {- 1}) w ^ {- 2} \mathrm{d} u \mathrm{d} w. \\ \end{array}
$$

---

88

第三章 随机向量和独立性

故 $(\xi, \eta^{-1})$ 为绝对连续型随机向量且有联合分布密度 $p(x, y^{-1})y^{-2}1_{\{y \neq 0\}}$.

推论 3.3.11 (商的密度函数) 若绝对连续型随机向量  $(\xi, \eta)$  有联合分布密度  $p(x, y)$ ，则  $\xi/\eta$  为绝对连续型随机变量且有密度

$$
p _ {\xi / \eta} (z) = \int_ {- \infty} ^ {\infty} | v | p (z v, v) \mathrm{d} v, \quad z \in \mathbb {R}.
$$

证明 根据定理3.3.10知 $(\xi, \eta^{-1})$ 为绝对连续型随机向量且有联合分布密度 $q(x, y) = p(x, y^{-1})y^{-2}1_{\{y \neq 0\}}$. 再由定理3.3.5知 $\xi / \eta = \xi \eta^{-1}$ 为绝对连续型随机变量且有密度

$$
\begin{array}{l} p _ {\xi / \eta} (z) = \int_ {- \infty} ^ {\infty} | y | ^ {- 1} q (y ^ {- 1} z, y) 1 _ {\{y \neq 0 \}} \mathrm{d} y \\ = \int_ {- \infty} ^ {\infty} | y | ^ {- 1} p (y ^ {- 1} z, y ^ {- 1}) y ^ {- 2} 1 _ {\{y \neq 0 \}} \mathrm{d} y \\ = \int_ {- \infty} ^ {\infty} | v | p (v z, v) 1 _ {\{v \neq 0 \}} \mathrm{d} v. \\ \end{array}
$$

故得欲证结果.

定理 3.3.12 设  $\xi := (\xi_{1}, \xi_{2}, \cdots, \xi_{n})$  是区域  $E \subseteq R^{n}$  上的绝对连续型随机向量，且有联合密度函数 p. 再设  $f := (f_{1}, f_{2}, \cdots, f_{n})$  是 E 到区域  $F \subseteq R^{n}$  的映射，且对每一点  $y := (y_{1}, y_{2}, \cdots, y_{n}) \in F$ ，方程

$$
\left\{ \begin{array}{l} y _ {1} = f _ {1} (x _ {1}, x _ {2}, \dots , x _ {n}), \\ y _ {2} = f _ {2} (x _ {1}, x _ {2}, \dots , x _ {n}), \\ \dots \dots \\ y _ {n} = f _ {n} (x _ {1}, x _ {2}, \dots , x _ {n}) \end{array} \right. \tag {3.3.6}
$$

有唯一解  $x := (x_{1}, x_{2}, \cdots, x_{n}) \in E$ ，即

$$
\left\{ \begin{array}{l} x _ {1} = h _ {1} (y _ {1}, y _ {2}, \dots , y _ {n}), \\ x _ {2} = h _ {2} (y _ {2}, y _ {2}, \dots , y _ {n}), \\ \dots \dots \\ x _ {n} = h _ {n} (y _ {1}, y _ {2}, \dots , y _ {n}). \end{array} \right.
$$

若  $h := (h_{1}, h_{2}, \cdots, h_{n})$  连续可微，则  $\eta := (f_{1}(\xi), f_{2}(\xi), \cdots, f_{n}(\xi))$  为 F 上的绝对连续型随机向量，且有联合分布密度

$$
q (y) = p (h _ {1} (y), h _ {2} (y), \dots , h _ {n} (y)) | J (y) |, \quad y = (y _ {1}, y _ {2}, \dots , y _ {n}) \in F,
$$

其中 $J(y)$ 为坐标变换的雅可比 (Jacobi) 行列式, 即

---

3.3 随机向量函数的分布

89

$$
J (y) = \frac {\mathrm{d} (x _ {1} , x _ {2} , \cdots , x _ {n})}{\mathrm{d} (y _ {1} , y _ {2} , \cdots , y _ {n})} = \left| \begin{array}{c c c c} \frac {\mathrm{d} x _ {1}}{\mathrm{d} y _ {1}} & \frac {\mathrm{d} x _ {1}}{\mathrm{d} y _ {2}} & \dots & \frac {\mathrm{d} x _ {1}}{\mathrm{d} y _ {n}} \\ \frac {\mathrm{d} x _ {2}}{\mathrm{d} y _ {1}} & \frac {\mathrm{d} x _ {2}}{\mathrm{d} y _ {2}} & \dots & \frac {\mathrm{d} x _ {2}}{\mathrm{d} y _ {n}} \\ \vdots & \vdots & & \vdots \\ \frac {\mathrm{d} x _ {n}}{\mathrm{d} y _ {1}} & \frac {\mathrm{d} x _ {n}}{\mathrm{d} y _ {2}} & \dots & \frac {\mathrm{d} x _ {n}}{\mathrm{d} y _ {n}} \end{array} \right|.
$$

证明 记  $F_{\eta}(z_{1},z_{2},\cdots,z_{n})=\mathbf{P}\{f_{1}(\xi)\leqslant z_{1},f_{2}(\xi)\leqslant z_{2},\cdots,f_{n}(\xi)\leqslant z_{n}\}$ . 则

$$
F _ {\eta} (z _ {1}, z _ {2}, \dots , z _ {n}) = \int_ {\{f _ {1} (x) \leqslant z _ {1} \}} \dots \int_ {\{f _ {n} (x) \leqslant z _ {n} \}} p (x _ {1}, x _ {2}, \dots , x _ {n}) \mathrm{d} x _ {1} \mathrm{d} x _ {2} \dots \mathrm{d} x _ {n}.
$$

由重积分的变量替换公式,

$$
F _ {\eta} (z _ {1}, z _ {2}, \dots , z _ {n}) = \int_ {- \infty} ^ {z _ {1}} \dots \int_ {- \infty} ^ {z _ {n}} p (h _ {1} (y), h _ {2} (y), \dots , h _ {n} (y)) | J (y) | \mathrm{d} y _ {1} \mathrm{d} y _ {2} \dots \mathrm{d} y _ {n}.
$$

求导即得  $q(y_{1},y_{2},\cdots,y_{n})$  的表达式.

例3.3.9 设 $\xi, \eta$ 服从分布 $N(0,1)$ 且相互独立. 求 $(\xi, \eta)$ 的极坐标 $(\rho, \theta)$ 的分布密度.

解 为了使定理3.3.12的条件得到满足, 我们可以认为 $(\xi, \eta)$ 是区域 $E := \mathbb{R}^2 \setminus \{(x, 0) : x \geqslant 0\}$ 上的绝对连续型随机向量. 因为 $\mathbf{P}\{(\xi, \eta) \in E\} = 1$, 这样的做法是合理的. 由题意 $\xi = \rho \cos \theta$ 和 $\eta = \rho \sin \theta$, 其中随机向量 $(\rho, \theta)$ 取值于区域 $F := (0, \infty) \times (0, 2\pi)$. 定义坐标变换 $x = r \cos t$ 和 $y = r \sin t$. 则

$$
J (r, t) = \left| \begin{array}{c c} \cos t & - r \sin t \\ \sin t & r \cos t \end{array} \right| = r.
$$

注意 $(\xi, \eta)$ 的联合分布密度为

$$
p (x, y) = \frac {1}{2 \pi} \mathrm{e} ^ {- (x ^ {2} + y ^ {2}) / 2}, \quad (x, y) \in E.
$$

所以 $(\rho, \theta)$ 有联合分布密度

$$
q (r, t) = p (r \cos t, r \sin t) | J (r, t) | = \frac {r}{2 \pi} \mathrm{e} ^ {- \frac {r ^ {2}}{2}},
$$

其中 $(r,t)\in F$

显然, 上例中得到的随机向量 $(\rho, \theta)$ 相互独立. 注意 $\theta$ 服从分布 $U(0, 2\pi)$, 而 $\rho$ 服从以 $q_{1}(r) = r e^{-r^{2} / 2}, r > 0$ 为密度的绝对连续型分布. 后一分布称为瑞利 (Rayleigh) 分布.

例3.3.10 设 $(\xi, \eta)$ 有联合分布密度 $p(x, y) = 3x, 0 < y < x < 1$. 求 $\xi - \eta$ 的分布.

---

90

第三章 随机向量和独立性

解 解法1（利用公式） 定义随机变量 $\alpha = \xi -\eta ,\beta = \eta .$ 对应的坐标变换为

$$
\left\{ \begin{array}{l} u = x - y, \\ v = y. \end{array} \right. \quad \left\{ \begin{array}{l} x = u + v, \\ y = v. \end{array} \right.
$$

显然, 变换的雅可比行列式为

$$
\left| \frac {\mathrm{d} (x , y)}{\mathrm{d} (u , v)} \right| = \left| \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right| = 1 > 0.
$$

显然 $0 < y < x < 1$ 当且仅当 $u, v > 0$ 且 $u + v < 1$. 由此得到 $(\alpha, \beta)$ 的密度函数为 $q(u, v) = 3(u + v)$, 其中 $u, v > 0$ 且 $u + v < 1$. 故 $\alpha$ 的边缘分布密度为

$$
q _ {\alpha} (u) = \int_ {0} ^ {1 - u} 3 (u + v) \mathrm{d} v = \frac {3}{2} (1 - u ^ {2}), \quad 0 \leqslant u <   1.
$$

解法2（直接计算）令 $\alpha = \xi -\eta$ 对于 $0\leqslant z <   1$ 有

$$
\begin{array}{l} F _ {\alpha} (z) = \iint_ {\{x - y \leqslant z, 0 <   y <   x <   1 \}} 3 x \mathrm{d} x \mathrm{d} y \\ = \int_ {0} ^ {z} \mathrm{d} x \int_ {0} ^ {x} 3 x \mathrm{d} y + \int_ {z} ^ {1} \mathrm{d} x \int_ {x - z} ^ {x} 3 x \mathrm{d} y \\ = z ^ {3} + \int_ {z} ^ {1} 3 x z \mathrm{d} x = z ^ {3} + \frac {3}{2} z (1 - z ^ {2}) \\ = \frac {3}{2} z - \frac {1}{2} z ^ {3}. \\ \end{array}
$$

求导得到分布密度

$$
q _ {\alpha} (z) = \frac {3}{2} (1 - z ^ {2}), \quad 0 \leqslant z <   1.
$$

## 练习题

1. 设随机变量 $\xi$ 和 $\eta$ 独立且都服从均匀分布 $U(0,1)$. 求 $\xi + \eta$ 的分布密度.

2. 设  $\xi$  和  $\eta$  独立且都服从标准正态分布. 求  $\eta + \xi, \eta - \xi, \eta\xi$  和  $\eta/\xi$  的分布密度.

3. 设随机变量  $\xi_{1}$  和  $\xi_{2}$  独立且分别服从泊松分布  $P(\lambda_{1})$  和  $P(\lambda_{2})$ . 求

(1) $\xi_{1} + \xi_{2}$ 的分布列；(2) 在给定 $\xi_{1} + \xi_{2} = n$ 时 $\xi_{1}$ 的条件分布列.

4. 设随机变量  $\xi_{1}$  和  $\xi_{2}$  独立且均服从指数分布  $E(\lambda)$ . 证明  $\xi_{1} + \xi_{2}$  与  $\xi_{1}/\xi_{2}$  独立.

5. 设  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  独立且都服从标准正态分布. 求  $X_{n} = \xi_{1}^{2} + \xi_{2}^{2} + \cdots + \xi_{n}^{2}$  的分布.

6. 设随机变量  $\xi_{1}, \xi_{2}, \cdots, \xi_{n}$  独立且分别服从指数分布  $E(\lambda_{1}), E(\lambda_{2}), \cdots, E(\lambda_{n})$ . 求  $\eta_{n} = \xi_{1} \wedge \xi_{2} \wedge \cdots \wedge \xi_{n}$  的分布.
