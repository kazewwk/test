证明 任取 $\varepsilon > 0$, 易见有 $F \in C_{\#}[0, 2\pi]$ 使得 $\|f - F\|_2 \leqslant \varepsilon$.

由 Weierstrass 第二逼近定理, 存在以 $2\pi$ 为周期的三角多项式 $P$ 使得 $\max_{x \in [0,2\pi]} |F(x) - P(x)| \leqslant \frac{\varepsilon}{\sqrt{2\pi}}$. 从而 $\|F - P\|_2 \leqslant \varepsilon$. 利用 Minkowski 不等式, 得到 $\|f - P\|_2 \leqslant 2\varepsilon$.

设 P 的次数为 m，则结合最佳均方逼近性质 (参见 (21.3.8))，当  $n \geqslant m$  时，有

$$
\| S _ {n} (f; \cdot) - f (\cdot) \| _ {2} \leqslant \| P - f \| _ {2} \leqslant 2 \varepsilon .
$$

由此可得(21.3.13)式. 不难看到(21.3.15)式与(21.3.13)式等价(参见(21.3.4)式). 最后, 依次用 $f + g$ 和 $f - g$ 代替 $f$ 代入(21.3.15)式, 再将两式相减得到(21.3.14)式. □

## 逐项积分公式的一般化

公式 (21.3.14) 相当于说, 对于 $f, g \in \mathcal{R}^2[0, 2\pi]$, 有

$$
\int_ {0} ^ {2 \pi} f (x) g (x) \mathrm{d} x = \frac {a _ {0}}{2} \int_ {0} ^ {2 \pi} g (t) \mathrm{d} t + \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {2 \pi} (a _ {n} \cos n t + b _ {n} \sin n t) g (t) \mathrm{d} t.
$$

对于 $[a,b]\subseteq [0,2\pi ]$ ，在上式中以 $g\chi_{[a,b]}$ 代替 $g$ 即得

$$
\int_ {a} ^ {b} f (t) g (t) \mathrm{d} t = \frac {a _ {0}}{2} \int_ {a} ^ {b} g (t) \mathrm{d} t + \sum_ {n = 1} ^ {\infty} \int_ {a} ^ {b} (a _ {n} \cos n t + b _ {n} \sin n t) g (t) \mathrm{d} t. \tag {21.3.16}
$$

一般地, 我们希望对于对偶数 $p, q$ 以及 $f \in \mathcal{R}_{\#}^{p}(\mathbb{R})$, $g \in \mathcal{R}_{\log}^{q}(\mathbb{R})$, 同样有逐项积分公式 (21.3.16). 为此, 我们指出, 对于 $1 < p < +\infty$, 有

$$
\lim _ {n \to + \infty} \| S _ {n} (f; \cdot) - f (\cdot) \| _ {p} = 0, \qquad \forall   f \in \mathcal {R} _ {\#} ^ {p} (\mathbb {R}), \tag {21.3.17}
$$

其中

$$
\| f \| _ {p} \equiv \| f \| _ {\mathcal {R} ^ {p} [ 0, 2 \pi ]} = \left(\int_ {0} ^ {2 \pi} | f (x) | ^ {p} \mathrm{d} x\right) ^ {\frac {1}{p}}, \quad \forall f \in \mathcal {R} _ {\#} ^ {p} (\mathbb {R}). \tag {21.3.18}
$$

可以证明 (21.3.17) 式等价于存在常数  $C_{p} > 0$  使得

$$
\| S _ {n} (f; \cdot) \| _ {p} \leqslant C _ {p} \| f \| _ {p}, \quad \forall f \in \mathcal {R} _ {\#} ^ {p} (\mathbb {R}). \tag {21.3.19}
$$

基于上述结果, 可得如下定理.

定理 21.3.2 设 p, q > 1 为对偶数,  $f \in \mathcal{R}_{\#}^{p}(\mathbb{R})$ , 它的 Fourier 级数为 (21.3.11) 式. 又设  $g \in R^{q}[a, b]$ , 则 (21.3.16) 式成立.

证明 不妨设 $[a, b] \subseteq [0, 2\pi]$. 则

$$
\begin{array}{l} \left| \frac {a _ {0}}{2} \int_ {a} ^ {b} g (t) \mathrm{d} t + \sum_ {k = 1} ^ {n} \int_ {a} ^ {b} \left(a _ {k} \cos k t + b _ {k} \sin k t\right) g (t) \mathrm{d} t - \int_ {a} ^ {b} f (t) g (t) \mathrm{d} t \right| \\ = \left| \int_ {a} ^ {b} (f (t) - S _ {n} (f; t)) g (t) \mathrm{d} t \right| \leqslant \| f (\cdot) - S _ {n} (f; \cdot) \| _ {\mathcal {R} ^ {p} [ 0, 2 \pi ]} \| g \| _ {\mathcal {R} ^ {q} [ a, b ]}. \\ \end{array}
$$

令 $n\to +\infty$ 即得(21.3.16)式成立.

□

对于 $p = 1$ (以及 $+\infty$), (21.3.17) 式与 (21.3.19) 式不成立. 但我们可以建立如下结果.

定理 21.3.3 (1) 设 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 的 Fourier 级数为 (21.3.11). 又设 $g$ 在 $[a, b]$ 上单调, 或存在 $\alpha \in (0, 1)$ 使得 $g \in C^{\alpha}[a, b]$, 则 (21.3.16) 式成立.

(2) 设 $f \in C_{\#}^{\alpha}(\mathbb{R})$ 或 $f$ 在 $[0, 2\pi]$ 上可以表示为两个单调函数之和，$f$ 的 Fourier 级数为 (21.3.11) 式. 又设 $g \in \mathcal{R}^{1}[a, b]$，则 (21.3.16) 式成立.

证明 (1) 不妨设 $f$ 非负. 对于 $x > b$; 补充定义 $g(x) = g(b)$, 对于 $x < a$, 补充定义 $g(x) = g(a)$. 我们有

$$
\begin{array}{l} \int_ {a} ^ {b} \left(S _ {n} (f; x) - f (x)\right) g (x) \mathrm{d} x \\ = \frac {1}{\pi} \int_ {a} ^ {b} \mathrm{d} x \int_ {- \pi} ^ {\pi} (f (x + \theta) - f (x)) g (x) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta \\ = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} F (\theta) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta = S _ {n} (F; 0), \\ \end{array}
$$

其中

$$
F (\theta) := \int_ {a} ^ {b} (f (x + \theta) - f (x)) g (x) \mathrm{d} x, \qquad \theta \in \mathbb {R}.
$$

易见 F 是以  $2\pi$  为周期的连续函数. 当  $|\theta| < 1$  时,

$$
\begin{array}{l} F (\theta) = \int_ {a + \theta} ^ {b + \theta} f (x) g (x - \theta) \mathrm{d} x - \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x \\ = \int_ {a - 1} ^ {b + 1} f (x) g (x - \theta) \mathrm{d} x - g (b) \int_ {b + \theta} ^ {b + 1} f (x) \mathrm{d} x - g (a) \int_ {a - 1} ^ {a + \theta} f (x) \mathrm{d} x - \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x, \\ \end{array}
$$

最后一式的第二、第三项关于 $\theta$ 单调, 第四项为常数. 而第一项当 $g$ 单调时单调, 当 $g \in C^{\alpha}[a, b]$ 时, 是 $C^{\alpha}$ 函数. 因此, 由 Dirichlet-Jordan 判别法和 Dini-Lipschitz 判别法, 得到

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} (S _ {n} (f; x) - f (x)) g (x) \mathrm{d} x = \lim _ {n \to + \infty} S _ {n} (F; 0) = F (0) = 0.
$$

即 (21.3.16) 式成立.

(2) 易见, 只需对 $[a, b] = [0, 2\pi]$ 的情形加以证明. 此时, 设 $g$ 的 Fourier 级数为 (21.3.12) 式, 则由 (1) 的结论可得

$$
\begin{array}{l} \int_ {0} ^ {2 \pi} f (x) g (x) \mathrm{d} x = \frac {\alpha_ {0}}{2} \int_ {0} ^ {2 \pi} f (t) \mathrm{d} t + \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {2 \pi} (\alpha_ {n} \cos n t + \beta_ {n} \sin n t) f (t) \mathrm{d} t \\ = \frac {a _ {0} \alpha_ {0} \pi}{2} + \pi \sum_ {n = 1} ^ {\infty} (a _ {n} \alpha_ {n} + b _ {n} \beta_ {n}) \\ = \frac {a _ {0}}{2} \int_ {0} ^ {2 \pi} g (t) \mathrm{d} t + \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {2 \pi} \left(a _ {n} \cos n t + b _ {n} \sin n t\right) g (t) \mathrm{d} t. \\ \end{array}
$$

结论得证.

□

例21.3.1 设 $f \in C_{\#}^{1}[0, 2\pi]$, 证明存在与 $f$ 无关的常数 $C$ 使得

$$
\int_ {0} ^ {2 \pi} \left| f (x) - \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} f (t) \mathrm{d} t \right| ^ {2} \leqslant C \int_ {0} ^ {2 \pi} | f ^ {\prime} (x) | ^ {2} \mathrm{d} x,
$$

其中最佳常数为 C = 1.

证明 设 $f$ 的Fourier级数为

$$
f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} (a _ {n} \cos n x + b _ {n} \sin n x).
$$

则

$$
f ^ {\prime} (x) \sim \sum_ {n = 1} ^ {\infty} (n b _ {n} \cos n x - n a _ {n} \sin n x).
$$

由 Parseval 等式,

$$
\begin{array}{l} \int_ {0} ^ {2 \pi} \left| f (x) - \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} f (t) \mathrm{d} t \right| ^ {2} = \pi \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \\ \leqslant \pi \sum_ {n = 1} ^ {\infty} n ^ {2} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) = \int_ {0} ^ {2 \pi} | f ^ {\prime} (x) | ^ {2} \mathrm{d} x, \\ \end{array}
$$

其中等式成立当且仅当对任何 $n \geqslant 2, a_{n} = b_{n} = 0$. 因此结论成立.

□

例21.3.2 设 $f \in C_{\#}^{1}[0, 2\pi], f(0) = 0$，证明存在与 $f$ 无关的常数 $C$ 使得

$$
\int_ {0} ^ {2 \pi} \left| f (x) \right| ^ {2} \mathrm{d} x \leqslant C \int_ {0} ^ {2 \pi} | f ^ {\prime} (x) | ^ {2} \mathrm{d} x,
$$

其中最佳常数为 C = 4.

证明 令

$$
g (x) = \left\{ \begin{array}{l l} f (2 x), & x \in [ 0, \pi ], \\ - f (- 2 x), & x \in [ - \pi , 0 ]. \end{array} \right.
$$

则 $g\in C_{\#}^{1}[0,2\pi ],\int_{-\pi}^{\pi}g(t)\mathrm{d}t = 0.$ 由上例的结论，

$$
\int_ {0} ^ {2 \pi} \left| f (x) \right| ^ {2} \mathrm{d} x = \int_ {- \pi} ^ {\pi} \left| g (x) \right| ^ {2} \mathrm{d} x \leqslant \int_ {- \pi} ^ {\pi} \left| g ^ {\prime} (x) \right| ^ {2} \mathrm{d} x = 4 \int_ {0} ^ {2 \pi} \left| f ^ {\prime} (x) \right| ^ {2} \mathrm{d} x.
$$

另一方面, 取 $f(x) = \sin \frac{x}{2} (x \in [0, 2\pi])$ 可见 4 是最佳常数.

□

例 21.3.3 计算  $\int_{0}^{\pi}\ln^{2}\sin x\,dx$ .

解 利用例 21.1.2 及 Parseval 等式, 我们有

$$
\int_ {0} ^ {2 \pi} \ln^ {2} \left(2 \sin \frac {x}{2}\right) \mathrm{d} x = \pi \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2}} = \frac {\pi^ {3}}{6}.
$$

即

$$
\int_ {0} ^ {\pi} (\ln 2 + \ln \sin x) ^ {2} \mathrm{d} x = \frac {\pi^ {3}}{1 2}.
$$

结合 $\int_0^\pi \ln \sin x\mathrm{d}x = -\pi \ln 2$ 得到

$$
\int_ {0} ^ {\pi} \ln^ {2} \sin x \mathrm{d} x = \frac {\pi^ {3}}{1 2} + \pi \ln^ {2} 2.
$$

## 完备性与完全性

我们引入如下定义.

定义 21.3.1 设 X 是内积空间,  $M \subseteq X$ . 称 M 是 X 中的完备系, 是指 span M 在 X 中稠密, 即对任何  $x \in X$ , 以及  $\varepsilon > 0$ , 存在 M 中元  $x_{1}, x_{2}, \cdots, x_{n}$  的线性组合  $\sum_{k=1}^{n} \alpha_{k} x_{k}$  使得  $\left\|\sum_{k=1}^{n} \alpha_{k} x_{k} - x\right\|_{X} < \varepsilon$ .

称 $\mathcal{M}$ 是 $X$ 中的完全系, 是指 $\mathcal{M}^{\perp} = \{0\}$, 即若 $x \in X$ 使得 $\langle x, y \rangle = 0$ 对任何 $y \in \mathcal{M}$ 成立, 则必有 $x = 0$.

我们主要关心 $X$ 是无限维空间且 $\mathcal{M}$ 为可列集的情形. 设 $\mathcal{M} = \{\varphi_n | n \geqslant 0\}$. 不失一般性, 可设 $\mathcal{M}$ 中任何有限个元是线性无关的. 利用 Gram$^{①}$-Schmidt$^{②}$ 正交化, 可将 $\{\varphi_n | n \geqslant 0\}$ 标准正交化为 $\{\psi_n | n \geqslant 0\}$.

首先有如下定理.

定理 21.3.4 设 X 是内积空间,  $M \equiv \left\{\psi_{n} \mid n \geqslant 0\right\}$  是 X 中的标准正交系. 则 M 是完备系当且仅当对任何  $f \in X$ , Parseval 等式 (21.3.1) 成立.

证明 必要性的证明同定理 21.3.1 的证明. 细节留给读者.

为证明充分性, 任取 $f \in X$, 设其 Fourier 级数为 $\sum_{n=0}^{\infty} c_n \psi_n$. 则由 Parseval 等式,

$$
\| f \| _ {X} ^ {2} = \sum_ {k = 0} ^ {\infty} | c _ {k} | ^ {2}.
$$

而类似于 (21.3.4) 式, 有

$$
\| f - \sum_ {k = 0} ^ {n} c _ {k} \psi_ {k} \| _ {X} ^ {2} = \| f \| _ {X} ^ {2} - \sum_ {k = 0} ^ {n} | c _ {k} | ^ {2}.
$$

令 $n\to +\infty$ ，即得 $\lim_{n\to +\infty}\| f - \sum_{k = 0}^{n}c_k\psi_k\| _X^2 = 0.$ 这就表明 $\mathcal{M}$ 是完备系.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Gram, Jorgen Pedersen, 1850 年 6 月 27 日—1916 年 4 月 29 日, 丹麦数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Schmidt, Erhard, 1876 年 1 月 13 日—1959 年 12 月 16 日, 德国数学家.</span></small>

完备性与完全性有如下关系.

定理 21.3.5 设 X 是内积空间,  $M \subseteq X$ . 若 M 是完备系, 则 M 是完全系.

证明 设 M 是完备系. 设  $f \in X$  使得对任何  $g \in M$ , 有  $\langle f, g \rangle = 0$ . 任取  $\varepsilon > 0$ , 根据 M 是完备系, 有  $g_{1}, g_{2}, \cdots, g_{n} \in M$  以及  $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n} \in R$  使得  $\left\| f - \sum_{k=1}^{n} \alpha_{k} g_{k} \right\|_{X} < \varepsilon$ . 不妨设  $g_{1}, g_{2}, \cdots, g_{n}$  标准正交. 此时对  $1 \leqslant k \leqslant n, c_{k} = \langle f, g_{k} \rangle = 0$ . 于是由最佳均方逼近性质 (参见 (21.3.8) 式), 有

$$
\| f \| _ {X} ^ {2} = \left\| f - \sum_ {k = 0} ^ {n} c _ {k} g _ {k} \right\| _ {X} ^ {2} \leqslant \left\| f - \sum_ {k = 0} ^ {n} \alpha_ {k} g _ {k} \right\| _ {X} ^ {2} <   \varepsilon^ {2}.
$$

由  $\varepsilon > 0$  的任意性, 得到  $\|f\|_{X} = 0$ . 即 f = 0. 因此, M 是完全系.

![](images/page_820_image_7.jpg)

由上述定理可见, 标准正交系

$$
\frac {1}{\sqrt {2 \pi}}, \frac {\sin x}{\sqrt {\pi}}, \frac {\cos x}{\sqrt {\pi}}, \frac {\sin 2 x}{\sqrt {\pi}}, \frac {\cos 2 x}{\sqrt {\pi}}, \dots
$$

是  $R^{2}[0,2\pi]$  中的完备系，从而也是完全系。等价地，

$$
1, \sin x, \cos x, \sin 2 x, \cos 2 x, \dots
$$

是  $R^{2}[0,2\pi]$  中的完备系, 从而也是完全系.

如果 X 是完备的, 即 X 中的 Cauchy 列都有极限, 则有

定理 21.3.6 设 X 是完备的内积空间,  $M \subseteq X$ . 若 M 是完全系, 则 M 是完备系.

证明 任取 $f \in X$. 令 $\{f_n\}$ 为 $\inf_{g \in \overline{\operatorname{span} \mathcal{M}}} \|f - g\|_X$ 的极小化序列, 即 $f_n \in \overline{\operatorname{span} \mathcal{M}}$, 且

$$
\lim _ {n \to + \infty} \| f - f _ {n} \| _ {X} = d \equiv \inf _ {g \in \overline {{\operatorname{span} \mathcal {M}}}} \| f - g \| _ {X}.
$$

易见在内积空间中有如下的平行四边形公式

$$
\| x - y \| _ {X} ^ {2} + \| x + y \| _ {X} ^ {2} = 2 \| x \| _ {X} ^ {2} + 2 \| y \| _ {X} ^ {2}, \quad \forall x, y \in X.
$$

特别, 注意到  $\frac{f_{n}+f_{k}}{2}\in\overline{\operatorname{span}\mathcal{M}}$ ,

$$
\begin{array}{l} \| f _ {n} - f _ {k} \| _ {X} ^ {2} = 2 \| f _ {n} \| _ {X} ^ {2} + 2 \| f _ {k} \| _ {X} ^ {2} - 4 \left\| \frac {f _ {n} + f _ {k}}{2} \right\| _ {X} ^ {2} \\ \leqslant 2 \| f _ {n} \| _ {X} ^ {2} + 2 \| f _ {k} \| _ {X} ^ {2} - 4 d ^ {2}, \quad \forall n, k \geqslant 1. \\ \end{array}
$$

因此, $\{f_n\}$ 是 $X$ 中的 Cauchy 列, 进而它有极限, 设为 $\bar{f}$. 则 $\bar{f} \in \overline{\operatorname{span} \mathcal{M}}$, 进而

$$
\| f - \bar {f} \| _ {X} = d \leqslant \| f - g \| _ {X}, \quad \forall g \in \operatorname{span} \mathcal {M}.
$$

特别地, 对任何  $\alpha \in R$ ,

$$
\| f - \bar {f} \| _ {X} \leqslant \| f - (\bar {f} + \alpha g) \| _ {X}, \quad \forall g \in \mathcal {M}.
$$

因此，

$$
\langle f - \bar {f}, g \rangle = - \lim _ {\alpha \to 0} \frac {\| f - (\bar {f} + \alpha g) \| _ {X} ^ {2} - \| f - \bar {f} \| _ {X} ^ {2}}{2 \alpha} = 0, \quad \forall g \in \mathcal {M}.
$$

由于 $\mathcal{M}$ 为完全系, 因此 $f - \bar{f} = 0$, 即 $f = \bar{f} \in \overline{\operatorname{span} \mathcal{M}}$.

总之，$\mathcal{M}$ 必为完备系.

另一方面, 我们有以下结果.

例 21.3.4 证明: 在  $R^{2}[0,2\pi]$  中存在不是完备系的完全系.

证明 证明的思想/本质是寻找一个 $f \in L^{2}[0, 2\pi] \setminus \mathcal{R}^{2}[0, 2\pi]$，则

$$
\mathcal {M} := \left\{g \in \mathcal {R} ^ {2} [ 0, 2 \pi ] \Big | \int_ {0} ^ {2 \pi} f (x) g (x) \mathrm{d} x = 0 \right\}
$$

是 $\mathcal{R}^2 [0,2\pi ]$ 中的完全系，但不是完备系.这里 $\mathcal{M}$ 定义中的积分应该理解为Lebesgue积分，而$f\notin \mathcal{R}^2 [0,2\pi ]$ 理解为不存在一个仅在一个零测度集上与 $f$ 不相等的 $g$ ，使得 $g\in \mathcal{R}^2 [0,2\pi ]$ .相关讨论在Lebesgue积分意义下比较容易.但要限制在 $\mathcal{R}^2 [0,2\pi ]$ 中讨论，就显得比较麻烦

可以证明, 存在 $f \in C_{\#}[0, 2\pi]$ 使得 $f$ 处处可导, 导数有界, 但 $f'$ 的间断点全体不是零测度集, 且

$$
\delta \equiv \int_ {0} ^ {2 \pi} \left| f ^ {\prime} (x) \right| ^ {2} \mathrm{d} x > 0.
$$

不妨设 $\int_0^{2\pi}f(x)\mathrm{d}x = 0,\| f\| _2 = 1.$ 考虑

$$
\mathcal {M} := \left\{g \in C _ {\#} ^ {1} [ 0, 2 \pi ] \Bigg | \int_ {0} ^ {2 \pi} g ^ {\prime} (x) f (x) \mathrm{d} x = 0 \right\}.
$$

易见 M 是线性空间.

(i) 我们要证 $\mathcal{M}$ 不是 $\mathcal{R}^2[0, 2\pi]$ 中的完备系.

对于 $n \geqslant 1$ 以及 $h \in \mathcal{R}_{\#}^{1}(\mathbb{R})$, 记

$$
\Delta_ {n} h (x) = n \left(h \left(x + \frac {1}{n}\right) - h (x)\right), \qquad x \in \mathbb {R}.
$$

则函数列 $\{\Delta_n f(x)\}$ 一致有界. 由引理20.1.1及Arzelá有界收敛定理可得

$$
\lim _ {n \to + \infty} \int_ {0} ^ {2 \pi} \left| \left(f ^ {\prime} (x)\right) ^ {2} - (\Delta_ {n} f (x)) ^ {2} \right| \mathrm{d} x = 0, \tag {21.3.20}
$$

$$
\lim_{\substack{m\to +\infty \\ n\to +\infty}}\int_0^{2\pi}\left|\Delta_nf(x) - \Delta_mf(x)\right|^2  \mathrm{d}x = 0 \tag{21.3.21}
$$

由(21.3.20)式得到

$$
\int_ {0} ^ {2 \pi} \left| f ^ {\prime} (x) \right| ^ {2} \mathrm{d} x \leqslant \varliminf_ {n \to + \infty} \int_ {0} ^ {2 \pi} | \Delta_ {n} f (x) | ^ {2} \mathrm{d} x. \tag {21.3.22}
$$

于是有 $N \geqslant 1$ ，使得

$$
\int_ {0} ^ {2 \pi} | \Delta_ {N} f (x) | ^ {2} \mathrm{d} x \geqslant \frac {\delta}{2},
$$

$$
\int_ {0} ^ {2 \pi} \left| \Delta_ {N} f (x) - \Delta_ {m} f (x) \right| ^ {2} \mathrm{d} x \leqslant \frac {\delta}{4}, \quad \forall m \geqslant N.
$$

任取 $\varphi \in \mathcal{M},\| \varphi \|_2 > 0,$ 我们有

$$
\begin{array}{l} \left| \int_ {0} ^ {2 \pi} \varphi (x) \Delta_ {N} f (x) \mathrm{d} x \right| = \left| \int_ {0} ^ {2 \pi} \left(\varphi (x) \Delta_ {N} f (x) + \varphi^ {\prime} (x) f (x)\right) \mathrm{d} x \right| \\ = \lim _ {m \rightarrow + \infty} \left| \int_ {0} ^ {2 \pi} \left(\varphi (x) \Delta_ {N} f (x) + f (x) \Delta_ {m} \varphi \left(x - \frac {1}{m}\right)\right) \mathrm{d} x \right| \\ = \lim _ {m \rightarrow + \infty} \left| \int_ {0} ^ {2 \pi} \varphi (x) \left(\Delta_ {N} f (x) - \Delta_ {m} f (x)\right) \mathrm{d} x \right| \\ \leqslant \varliminf_ {m \to + \infty} \left\| \Delta_ {N} f - \Delta_ {m} f \right\| _ {2} \| \varphi \| _ {2} \\ \leqslant \frac {\sqrt {\delta}}{2} \| \varphi \| _ {2}. \\ \end{array}
$$

于是由 Fourier 级数的最佳均方逼近性质,

$$
\begin{array}{l} \| \Delta_ {N} f - \varphi \| _ {2} ^ {2} \\ \geqslant \left\| \Delta_ {N} f \right\| _ {2} ^ {2} - \frac {1}{\left\| \varphi \right\| _ {2} ^ {2}} \left(\int_ {0} ^ {2 \pi} \varphi (x) \Delta_ {N} f (x) \mathrm{d} x\right) ^ {2} \\ \geqslant \frac {\delta}{2} - \frac {\delta}{4} = \frac {\delta}{4}. \\ \end{array}
$$

这表明 $\Delta_N f$ 不属于 $\overline{\mathcal{M}}$. 即 $\mathcal{M}$ 不是 $\mathcal{R}^2 [0, 2\pi]$ 中的完备系.

(ii) 接下来, 要证明 $\mathcal{M}$ 是完全系. 设 $g \in \mathcal{R}^2[0, 2\pi]$ 满足: 对任何 $\varphi \in \mathcal{M}$, 有

$$
\int_ {0} ^ {2 \pi} g (x) \varphi (x) \mathrm{d} x = 0.
$$

注意到常值函数均属于 $\mathcal{M}$, 可得 $\int_0^{2\pi} g(x) \, \mathrm{d}x = 0$. 记

$$
G (x) := \int_ {0} ^ {x} g (t) \mathrm{d} t, \qquad x \in \mathbb {R},
$$

则 $G\in C_{\#}(\mathbb{R})$ 记 $\alpha = \frac{1}{2\pi}\int_0^{2\pi}G(t)\mathrm{d}t,$

$$
\psi (x) := \int_ {0} ^ {x} \left(G (t) - \alpha - \langle G - \alpha , f \rangle f (t)\right)   \mathrm{d} t, \qquad x \in \mathbb {R},
$$

则 $\psi \in C_{\#}^{1}(\mathbb{R}),\left\langle \psi^{\prime},f\right\rangle = 0.$ 因此， $\psi \in \mathcal{M}$ .从而

$$
\begin{array}{l} 0 = \int_ {0} ^ {2 \pi} g (x) \psi (x) \mathrm{d} x = \int_ {0} ^ {2 \pi} (G (x) - \alpha) \psi^ {\prime} (x) \mathrm{d} x \\ = \int_ {0} ^ {2 \pi} (G (x) - \alpha - \langle G - \alpha , f \rangle f (x)) \psi^ {\prime} (x) \mathrm{d} x \\ = \int_ {0} ^ {2 \pi} (G (x) - \alpha - \langle G - \alpha , f \rangle f (x)) ^ {2} \mathrm{d} x. \\ \end{array}
$$

这意味着

$$
G (x) - \alpha - \langle G - \alpha , f \rangle   f (x) = 0, \quad \forall   x \in \mathbb {R}.
$$

从而

$$
g (x) = \langle G - \alpha , f \rangle   f ^ {\prime} (x), \qquad \forall   x \in \mathbb {R}.
$$

由于 $f' \notin \mathcal{R}^2[0, 2\pi], g \in \mathcal{R}^2[0, 2\pi]$. 因此, 必有 $\langle G - \alpha, f \rangle = 0$. 从而 $g = 0$. 即 $\mathcal{M}$ 是完全系. □ 在例题中, $\mathcal{M}$ 不是可列集, 容易取到 $\mathcal{M}$ 中的点列 $\{\varphi_n | n \geqslant 0\}$ 在 $\mathcal{M}$ 中稠密, 此时, $\{\varphi_n | n \geqslant 0\}$ 仍然是完全系, 但不是完备系.

例 21.3.4 的结论事实上对于一般的不完备内积空间都成立. 即有

定理 21.3.7 设 X 是不完备的内积空间, 则 X 中存在不是完备系的完全系.

## 习题 21.3

1. 按以下步骤对 $C^1$ 平面上的简单闭曲线 $C$, 证明等周不等式 $4\pi S \leqslant L^2$, 其中 $L, S$ 分别为 $C$ 的周长与所围区域的面积. 依次证明:

(1) 设 $s$ 为弧长参数, 令 $t = \frac{2\pi s}{L}$, $C$ 的参数方程为 $x = x(t), y = y(t) (t \in [0, 2\pi])$. 则 $L^2 = 2\pi \int_0^{2\pi} \left(|x'(t)|^2 + |y'(t)|^2\right) \, \mathrm{d}t$.

(2) $S = \frac{1}{2}\int_{0}^{2\pi}(x(t)y'(t) - x'(t)y(t))\mathrm{d}t.$
(3) $4\pi S \leqslant L^2$.

2. 设 $1 \leqslant p < +\infty, f \in \mathcal{R}^p[0, 2\pi]$, 证明: $\lim_{n \to +\infty} \| \sigma_n(f; \cdot) - f(\cdot) \|_{\mathcal{R}^p[0, 2\pi]} = 0$.

3. 对于 $p \in [1, +\infty)$, 证明 (21.3.17) 式与 (21.3.19) 式的等价性.

4. 计算  $\int_{0}^{\frac{\pi}{2}} x \ln(\sin x) \ln(\cos x) \, dx$ .

## 21.4 Fourier 变换

Fourier 级数理论告诉我们可以把一个波 (周期函数) 看成是简谐振动的组合. 通过 Fourier 级数展开, 我们可以把一个波当中某个频率的波给分解出来.

而通过周期延拓, 我们可以把任何有界区间上的函数看作周期函数, 并进行 Fourier 级数展开.

现在, 考虑 $f \in \mathcal{R}^{1}(\mathbb{R})$, 考察当 $T \to +\infty$ 时, $f|_{[-T,T]}$ (视为以 $2T$ 为周期的函数) 的 Fourier 级数与 $f|_{[-T,T]}$ 间的关系. 为简单起见, 以下假设 $f \in C_c^2(\mathbb{R})$.

将 $f|_{[-T,T]}$ 作以 $2T$ 为周期的延拓, 则其Fourier级数的复形式为

$$
\sum_ {n = - \infty} ^ {+ \infty} \left(\frac {1}{2 T} \int_ {- T} ^ {T} f (y) \mathrm{e} ^ {\frac {- \mathrm{i} n \pi y}{T}} \mathrm{d} y\right) \mathrm{e} ^ {\frac {\mathrm{i} n \pi x}{T}}. \tag {21.4.1}
$$

当 $T > 0$ 满足 $\operatorname{supp} f \subset [-T, T]$ 时，以上级数在 $[-T, T]$ 上收敛到 $f|_{[-T, T]}$:

$$
f (x) = \sum_ {n = - \infty} ^ {+ \infty} \frac {1}{2 T} \widehat {f} \left(\frac {n}{2 T}\right) \mathrm{e} ^ {2 \pi \mathrm{i} x \frac {n}{2 T}}, \quad \forall x \in [ - T, T ], \tag {21.4.2}
$$

其中

$$
\widehat {f} (x) \equiv \mathscr {F} (f) (x) := \int_ {\mathbb {R}} f (y) \mathrm{e} ^ {- 2 \pi \mathrm{i} x y} \mathrm{d} y, \quad x \in \mathbb {R}. \tag {21.4.3}
$$

重写 (21.4.2) 式, 有

$$
\begin{array}{l} f (x) = \sum_ {n = - \infty} ^ {+ \infty} \int_ {\frac {n}{2 T}} ^ {\frac {n + 1}{2 T}} \widehat {f} \left(\frac {[ 2 T y ]}{2 T}\right) \mathrm{e} ^ {2 \pi \mathrm{i} x \frac {[ 2 T y ]}{2 T}} \mathrm{d} y \\ = \int_ {\mathbb {R}} \widehat {f} \left(\frac {[ 2 T y ]}{2 T}\right) \mathrm{e} ^ {2 \pi \mathrm{i} x \frac {[ 2 T y ]}{2 T}} \mathrm{d} y, \quad \forall x \in [ - T, T ]. \tag {21.4.4} \\ \end{array}
$$

另一方面, 易见 $\hat{f}$ 连续, 且利用分部积分, 有

$$
\widehat {f} (x) = - \frac {1}{4 \pi^ {2} x ^ {2}} \int_ {\mathbb {R}} f ^ {\prime \prime} (y) \mathrm{e} ^ {- 2 \pi \mathrm{i} x y} \mathrm{d} y, \qquad \forall x \neq 0.
$$

由此, 立即可得存在常数 $C > 0$ 使得

$$
\left| \widehat {f} (x) \right| \leqslant \frac {C}{1 + x ^ {2}}, \quad \forall   x \in \mathbb {R}.
$$

于是在(21.4.4)式中令 $T\to +\infty$ ，由控制收敛定理可得

$$
f (x) = \int_ {\mathbb {R}} \widehat {f} (y) \mathrm{e} ^ {2 \pi \mathrm{i} x y} \mathrm{d} y, \quad \forall x \in \mathbb {R}. \tag {21.4.5}
$$

基于上述讨论, 我们引入如下定义.

定义 21.4.1 设  $f \in \mathcal{R}^{1}(\mathbb{R}; \mathbb{C})$ ，称由 (21.4.3) 式定义的  $\widehat{f} \equiv \mathcal{F}(f)$  为 f 的 Fourier 变换。称下式定义的  $\stackrel{\vee}{f} \equiv \mathcal{F}^{-1}(f)$  为 f 的 Fourier 逆变换:

$$
\stackrel {\vee} {f} (x) = \mathscr {F} ^ {- 1} (f) (x) := \int_ {\mathbb {R}} f (y) \mathrm{e} ^ {2 \pi \mathrm{i} x y} \mathrm{d} y. \tag {21.4.6}
$$

Fourier 变换有着重要的应用, 但完整地介绍 Fourier 变换的性质难以避开 $L^2$ 空间, 这就有待于引入 Lebesgue 积分理论. 本节中, 我们把讨论的范围限制在速降函数空间内, 则可以方便地介绍 Fourier 变换的主要性质. 今后很容易将这些在速降函数空间建立的结果推广到一般情形. 自然, 某些特定的性质目前也可以在比速降函数类更广的范围内加以建立.

我们称 $\mathbb{R}$ 上无穷次可微的（复值）函数 $\varphi$ 为速降函数，又称为 Schwarz 函数，是指

$$
\sup _ {x \in \mathbb {R}} | x ^ {m} \varphi^ {(n)} (x) | <   + \infty, \quad \forall m, n \geqslant 0. \tag {21.4.7}
$$

这等价于

$$
\lim _ {x \to \infty} x ^ {m} \varphi^ {(n)} (x) = 0, \quad \forall m, n \geqslant 0. \tag {21.4.8}
$$

记速降函数的全体为  $\mathcal{S} \equiv \mathcal{S}(\mathbb{R})$ .

速降函数就是其各阶导数乘任何多项式后, 在无穷远处仍然趋于零的光滑函数. 易见 $C_c^\infty (\mathbb{R};\mathbb{C})\subset \mathcal{S}$. 而 $f(x):= \mathrm{e}^{-x^2}$ 所定义的函数 $f$ 是一个没有紧支集的速降函数. 又速降函数的各阶导数是速降函数, 速降函数乘多项式是速降函数.

类似地可以在 $\mathbb{R}^n$ 中定义Fourier变换以及速降函数.为简单起见，本节仅介绍一维情形的结果.读者完全可以把它们推广到高维情形.

以下定理给出了 Fourier 变换的导数以及导数的 Fourier 变换.

定理 21.4.1 设 $f \in  \mathcal{S}$ ,则 $\widehat{f} \in  \mathcal{S}$ ,且对于自然数 $n$ 成立

$$
\frac {\mathrm{d} ^ {n}}{\mathrm{d} x ^ {n}} \widehat {f} (x) = (- 2 \pi \mathrm{i}) ^ {n} \int_ {\mathbb {R}} y ^ {n} f (y) \mathrm{e} ^ {- 2 \pi \mathrm{i} x y} \mathrm{d} y, \quad \forall x \in \mathbb {R}, \tag {21.4.9}
$$

$$
\mathscr {F} (f ^ {(n)}) (x) = (2 \pi \mathrm{i}) ^ {n} x ^ {n} \widehat {f} (x), \quad \forall x \in \mathbb {R}. \tag {21.4.10}
$$

一般地, 对自然数 $m, n$, 有

$$
x ^ {m} \frac {\mathrm{d} ^ {n}}{\mathrm{d} x ^ {n}} \widehat {f} (x) = \frac {(- 2 \pi \mathrm{i}) ^ {n}}{(2 \pi \mathrm{i}) ^ {m}} \int_ {\mathbb {R}} \frac {\mathrm{d} ^ {m}}{\mathrm{d} y ^ {m}} \left(y ^ {n} f (y)\right) \mathrm{e} ^ {- 2 \pi \mathrm{i} x y} \mathrm{d} y, \quad \forall x \in \mathbb {R}. \tag {21.4.11}
$$

证明 由于 $f \in \mathcal{S}$, 易得存在 $M > 0$ 使得

$$
\left| 2 \pi \mathrm{i} x f (x) \right| \leqslant \frac {M}{x ^ {2} + 1}, \quad \forall x \in \mathbb {R}. \tag {21.4.12}
$$

这样, $\int_{\mathbb{R}}(-2\pi \mathrm{i}y)f(y)\mathrm{e}^{-2\pi \mathrm{i}xy}\mathrm{d}y$ 关于 $x\in \mathbb{R}$ 一致收敛，从而可得

$$
\frac {\mathrm{d}}{\mathrm{d} x} \widehat {f} (x) = \int_ {\mathbb {R}} - 2 \pi \mathrm{i} y f (y) \mathrm{e} ^ {- 2 \pi \mathrm{i} x y} \mathrm{d} y. \tag {21.4.13}
$$

归纳可得 (21.4.9) 式. 同样, 利用分部积分, 可得

$$
\mathcal {F} (f ^ {\prime}) (x) = 2 \pi \mathrm{i} x \widehat {f} (x). \tag {21.4.14}
$$

归纳可得 (21.4.10) 式.结合 (21.4.9)—(21.4.10) 式得到 (21.4.11) 式.由  $f \in S$ ，在 (21.4.11) 式右端的被积函数中， $\frac{\mathrm{d}^{m}}{\mathrm{d}y^{m}}(y^{n}f(y))$  也是速降函数，从而绝对可积.因此， $x^{m}\frac{\mathrm{d}^{n}}{\mathrm{d}x^{m}}\widehat{f}(x)$  有界.从而  $\widehat{f} \in S$ .

接下来, 我们来证明 (21.4.6) 式确实定义了 $\mathcal{F}$ 的逆变换, 即 (21.4.5) 式对于 $f \in \mathcal{S}$ 成立.

定理 21.4.2 设  $f \in S$ ，则 (21.4.5) 式成立.

证明 前面在 $f \in C_c^2(\mathbb{R};\mathbb{C})$ 情形下对 (21.4.5) 式的证明过程, 完全可以搬过来用在 $f \in \mathcal{S}$ 的情形. 以下, 给出另一个证明.

任取 A > 0,

$$
\begin{array}{l} \int_ {- A} ^ {A} \widehat {f} (y) \mathrm{e} ^ {2 \pi \mathrm{i} x y} \mathrm{d} y = \int_ {- A} ^ {A} \mathrm{d} y \int_ {\mathbb {R}} f (u) \mathrm{e} ^ {2 \pi \mathrm{i} (x - u) y} \mathrm{d} u \\ = \int_ {- A} ^ {A} \mathrm{d} y \int_ {\mathbb {R}} f (x - u) \mathrm{e} ^ {2 \pi \mathrm{i} u y} \mathrm{d} u = \int_ {\mathbb {R}} \mathrm{d} u \int_ {- A} ^ {A} f (x - u) \mathrm{e} ^ {2 \pi \mathrm{i} u y} \mathrm{d} y \\ = \int_ {\mathbb {R}} f (x - u) \frac {\sin (2 \pi A u)}{\pi u} \mathrm{d} u \\ = \int_ {\mathbb {R}} f ^ {\prime} (x - u) \left(\int_ {0} ^ {2 \pi A u} \frac {\sin t}{\pi t} \mathrm{d} t\right) \mathrm{d} u. \tag {21.4.15} \\ \end{array}
$$

在 (21.4.15) 式两端令 $A \to +\infty$，由控制收敛定理即得

$$
\int_ {\mathbb {R}} \widehat {f} (y) \mathrm{e} ^ {2 \pi \mathrm{i} x y} \mathrm{d} y = \int_ {\mathbb {R}} f ^ {\prime} (x - u) \frac {\operatorname{sgn} (u)}{2} \mathrm{d} u = f (x). \tag {21.4.16}
$$

定理得证.

对于 $f\in \mathcal{R}^p (\mathbb{R};\mathbb{C}),g\in \mathcal{R}^q (\mathbb{R};\mathbb{C})$ ，其中 $p,q$ 为对偶数，可以定义 $f$ 和 $g$ 的卷积为

$$
(f * g) (x) := \int_ {\mathbb {R}} f (x - y) g (y) \mathrm{d} y, \quad \forall x \in \mathbb {R}. \tag {21.4.17}
$$

以下定理给出了卷积与 Fourier 变换间的联系.

定理21.4.3 设 $f, g \in \mathcal{S}$, 则

$$
(f * g) ^ {\wedge} (x) = \widehat {f} (x) \widehat {g} (x), \quad \forall x \in \mathbb {R}, \tag {21.4.18}
$$

$$
(f g) ^ {\wedge} (x) = (\widehat {f} * \widehat {g}) (x), \quad \forall x \in \mathbb {R}. \tag {21.4.19}
$$

证明 证明是简单的. 特别, 容易证明以下过程中的积分交换次序是正确的:

$$
\begin{array}{l} (f * g) ^ {\wedge} (x) = \int_ {\mathbb {R}} (f * g) (y) \mathrm{e} ^ {- 2 \pi \mathrm{i} x \cdot y} \mathrm{d} y = \int_ {\mathbb {R}} \mathrm{d} y \int_ {\mathbb {R}} f (y - u) g (u) \mathrm{e} ^ {- 2 \pi \mathrm{i} x \cdot y} \mathrm{d} u \\ = \int_ {\mathbb {R}} \mathrm{d} u \int_ {\mathbb {R}} f (y - u) g (u) \mathrm{e} ^ {- 2 \pi \mathrm{i} x \cdot y} \mathrm{d} y = \int_ {\mathbb {R}} \mathrm{d} u \int_ {\mathbb {R}} f (y) g (u) \mathrm{e} ^ {- 2 \pi \mathrm{i} x \cdot (y + u)} \mathrm{d} y \\ = \widehat {f} (x) \widehat {g} (x). \\ \end{array}
$$

注意到 $\stackrel{\vee}{f}(x) = \widehat{f} (-x)$, 我们有

$$
(f * g) ^ {\vee} (x) = \stackrel {\vee} {f} (x) \stackrel {\vee} {g} (x), \quad \forall   x \in \mathbb {R}. \tag {21.4.20}
$$

在 (21.4.20) 式中分别用  $\widehat{f}, \widehat{g}$  代替 f, g, 并取 Fourier 变换, 可得 (21.4.19) 式.

利用上述定理, 可得如下定理. 我们用  $\bar{z}$  表示复数 z 的共轭复数.

定理21.4.4 设 $f, g \in \mathcal{S}$, 则

$$
\int_ {\mathbb {R}} f (x) \overline {{g (x)}} \mathrm{d} x = \int_ {\mathbb {R}} \widehat {f} (x) \overline {{\widehat {g} (x)}} \mathrm{d} x. \tag {21.4.21}
$$

证明 令

$$
h (x) := \overline {{g (- x)}}, \quad \forall   x \in \mathbb {R}.
$$

我们有

$$
\begin{array}{l} \int_ {\mathbb {R}} f (x) \overline {{g (x)}} \mathrm{d} x = \int_ {\mathbb {R}} f (x) h (- x) \mathrm{d} x = (f * h) (0) \\ = \left((f * h) ^ {\wedge}\right) ^ {\vee} (0) = \left(\widehat {f} \widehat {h}\right) ^ {\vee} (0) = \int_ {\mathbb {R}} \widehat {f} (x) \widehat {h} (x) \mathrm{d} x \\ = \int_ {\mathbb {R}} \widehat {f} (x) \overline {{\widehat {g} (x)}} \mathrm{d} x. \\ \end{array}
$$

在上述定理中取 g 为 f 即得 Plancherel $^{①}$  定理:

定理 21.4.5 设  $f \in S$ ，则

$$
\int_ {\mathbb {R}} | f (x) | ^ {2} \mathrm{d} x = \int_ {\mathbb {R}} | \widehat {f} (x) | ^ {2} \mathrm{d} x. \tag {21.4.22}
$$

利用卷积的 Young 不等式 (参见定理 21.4.8), 可得

推论 21.4.6 设整数  $n \geqslant 1, f \in S$ ，则

$$
\| \widehat {f} \| _ {2 n} \leqslant \| f \| _ {\frac {2 n}{2 n - 1}}. \tag {21.4.23}
$$

证明 反复利用 (21.4.31) 式, 我们有

$$
\begin{array}{l} \| \widehat {f} \| _ {2 n} = \| \widehat {f} ^ {n} \| _ {2} ^ {\frac {1}{n}} = \| (\overbrace {f * f * \cdots * f} ^ {n \text {个}}) ^ {\wedge} \| _ {2} ^ {\frac {1}{n}} = \| \overbrace {f * f * \cdots * f} ^ {n \text {个}} \| _ {2} ^ {\frac {1}{n}} \\ \leqslant \| f \| _ {\frac {2 n}{n - 1}} ^ {\frac {1}{n}} \| \overbrace {f * f * \cdots * f} ^ {n - 1 \text {个}} \| _ {\frac {2 n}{n + 1}} ^ {\frac {1}{n}} \leqslant \dots \leqslant \| f \| _ {\frac {2 n}{2 n - 1}}. \\ \end{array}
$$

易见，

$$
\| \widehat {f} \| _ {\infty} \leqslant \| f \| _ {1}, \quad \forall f \in \mathcal {R} ^ {1} (\mathbb {R}; \mathbb {C}). \tag {21.4.24}
$$

利用 (21.4.22) 式与 (21.4.24) 式, 以及插值定理可推广推论 21.4.6 的结果, 得到如下的 Hausdorff $^{②}$ -Young 不等式.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Plancherel, Michel, 1885 年 1 月 16 日—1967 年 3 月 4 日, 瑞士数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Hausdorff, Felix, 1868 年 11 月 8 日—1942 年 1 月 26 日, 德国数学家.</span></small>

定理 21.4.7 设 $p \in  \left\lbrack  {1,2}\right\rbrack  ,q$ 为其对偶数,则对于任何 $f \in  S$ ,有

$$
\| \widehat {f} \| _ {q} \leqslant \| f \| _ {p}. \tag {21.4.25}
$$

例21.4.1 计算 $\left(\chi_{[-\frac{1}{2},\frac{1}{2} ]}\right)^{\wedge}$

解

$$
\left(\chi_ {[ - \frac {1}{2}, \frac {1}{2} ]}\right) ^ {\wedge} (x) = \int_ {- \frac {1}{2}} ^ {\frac {1}{2}} \mathrm{e} ^ {- 2 \pi \mathrm{i} x y} \mathrm{d} y = \frac {\sin \pi x}{\pi x}.
$$

例 21.4.2 设  $f(x) := \mathrm{e}^{-\pi x^{2}} (x \in \mathbb{R})$ ，计算  $\widehat{f}$ .

解 解法1

$$
\frac {\mathrm{d}}{\mathrm{d} x} \widehat {f} (x) = - 2 \pi \mathrm{i} \int_ {\mathbb {R}} y \mathrm{e} ^ {- \pi y ^ {2}} \mathrm{e} ^ {- 2 \pi \mathrm{i} x y} \mathrm{d} y = - 2 \pi x \widehat {f} (x), \qquad \forall x \in \mathbb {R}.
$$

因此, 有复常数 C 使得

$$
\widehat {f} (x) = C \mathrm{e} ^ {- \pi x ^ {2}}, \qquad \forall   x \in \mathbb {R}.
$$

结合  $\widehat{f}(0)=1$  得到 C=1. 从而  $\widehat{f}=f$ .

解法2 考虑

$$
g (z) := \int_ {- \infty} ^ {+ \infty} \mathrm{e} ^ {- \pi y ^ {2}} \mathrm{e} ^ {- 2 \pi y z} \mathrm{d} y, \qquad z \in \mathbb {C}.
$$

则 $g$ 是 $\mathbb{C}$ 上的解析函数. 当 $z = x$ 为实数时,

$$
g (x) = \int_ {- \infty} ^ {+ \infty} \mathrm{e} ^ {- \pi (y + x) ^ {2} + \pi x ^ {2}} \mathrm{d} y = \int_ {- \infty} ^ {+ \infty} \mathrm{e} ^ {- \pi y ^ {2} + \pi x ^ {2}} \mathrm{d} y = \mathrm{e} ^ {x ^ {2}}, \quad \forall x \in \mathbb {R}.
$$

于是, 结合 $\mathrm{e}^{z^2}$ 为 $\mathbb{C}$ 上的解析函数以及解析函数的唯一性得到 $g(\mathrm{i}x) = \mathrm{e}^{-\pi x^2} (x \in \mathbb{R})$. 最后, 可得 $\widehat{f}(x) = \mathrm{e}^{-\pi |x|^2}$. 即 $\widehat{f} = f$.

例 21.4.3 (热传导方程的求解) 设  $f \in S$ ，求解热传导方程

$$
\left\{ \begin{array}{l l} u _ {t} (t, x) = u _ {x x} (t, x), & t \geqslant 0,   x \in \mathbb {R}, \\ u (0, x) = f (x), & x \in \mathbb {R}. \end{array} \right. \tag {21.4.26}
$$

解 形式上, 对空间变量作 Fourier 变换, 得到

$$
\left\{ \begin{array}{l l} \widehat {u} _ {t} (t, x) = - 4 \pi^ {2} x ^ {2} \widehat {u} (t, x), & t \geqslant 0,   x \in \mathbb {R}, \\ \widehat {u} (0, x) = \widehat {f} (x), & x \in \mathbb {R}. \end{array} \right.
$$

上式本质上是一个常微分方程, 解得

$$
\widehat {u} (t, x) = \widehat {f} (x) \mathrm{e} ^ {- 4 \pi^ {2} t x ^ {2}}, \qquad t \geqslant 0,   x \in \mathbb {R}.
$$

作 Fourier 逆变换并利用例 21.4.2 的结果得到

$$
u (t, x) \int_ {\mathbb {R}} f (x - 2 \sqrt {\pi t} y) \mathrm{e} ^ {- \pi y ^ {2}} \mathrm{d} y, \quad t \geqslant 0, x \in \mathbb {R}. \tag {21.4.27}
$$

进一步, 可以证明上式确实给出了方程 (21.4.26) 的唯一解. 在此, 我们不展开讨论. $\square$

例 21.4.4 设 0 < a < 1,  $ba \geqslant 1$ ，证明级数  $W(x) := \sum_{n=1}^{\infty} a^{n} \cos b^{n} x$  与  $S(x) := \sum_{n=1}^{\infty} a^{n} \sin b^{n} x$  在 R 上处处连续无处可微。特别地， $\sum_{n=1}^{\infty} \frac{\cos 2^{n} x}{2^{n}}$  与  $\sum_{n=1}^{\infty} \frac{\sin 2^{n} x}{2^{n}}$  在 R 上处处连续无处可微。

证明 由函数项级数的一致收敛性的性质, 易见 W, S 在 R 上处处连续.

任取 $C_c^\infty$ 函数 $\psi$ 使得 $\psi(1) = 1$, $\operatorname{supp} \psi \subseteq \left[\frac{1}{b}, b\right]$. 令 $\varphi = \stackrel{\vee}{\psi}$, 则 $\psi, \varphi$ 都是速降函数. 如果对某个 $x_0 \in \mathbb{R}$, $W$ 在 $x_0$ 可导, 则由控制收敛定理,

$$
\begin{array}{l} \lim _ {\varepsilon \to 0 ^ {+}} \int_ {\mathbb {R}} \frac {W (x _ {0} + 2 \pi \varepsilon x) - W (x _ {0})}{2 \pi \varepsilon x} \cdot x \varphi (x) \mathrm{d} x \\ = W ^ {\prime} (x _ {0}) \int_ {\mathbb {R}} x \varphi (x) \mathrm{d} x = - \frac {1}{2 \pi \mathrm{i}} W ^ {\prime} (x _ {0}) \widehat {\varphi} ^ {\prime} (0) = 0. \tag {21.4.28} \\ \end{array}
$$

另一方面，

$$
\begin{array}{l} \int_ {\mathbb {R}} \frac {W (x _ {0} + 2 \pi \varepsilon x) - W (x _ {0})}{2 \pi \varepsilon x} \cdot x \varphi (x) \mathrm{d} x \\ = \frac {1}{2 \pi \varepsilon} \int_ {\mathbb {R}} W (x _ {0} + 2 \pi \varepsilon x) \varphi (x) \mathrm{d} x - \frac {1}{2 \pi \varepsilon} W (x _ {0}) \widehat {\varphi} (0) \\ = \frac {1}{2 \pi \varepsilon} \sum_ {n = 1} ^ {\infty} \int_ {\mathbb {R}} a ^ {n} \varphi (x) \cos \left(b ^ {n} (x _ {0} + 2 \pi \varepsilon x)\right) \mathrm{d} x \\ = \frac {1}{4 \pi \varepsilon} \sum_ {n = 1} ^ {\infty} \int_ {\mathbb {R}} a ^ {n} \left[ \mathrm{e} ^ {\mathrm{i} b ^ {n} (x _ {0} + 2 \pi \varepsilon x)} + \mathrm{e} ^ {- \mathrm{i} b ^ {n} (x _ {0} + 2 \pi \varepsilon x)} \right] \varphi (x) \mathrm{d} x \\ = \frac {1}{4 \pi \varepsilon} \sum_ {n = 1} ^ {\infty} a ^ {n} \left(\mathrm{e} ^ {\mathrm{i} b ^ {n} x _ {0}} \widehat {\varphi} (- b ^ {n} \varepsilon) + \mathrm{e} ^ {- \mathrm{i} b ^ {n} x _ {0}} \widehat {\varphi} (b ^ {n} \varepsilon)\right). \\ \end{array}
$$

上式中对于 $k \geqslant 1$ ，取 $\varepsilon = b^{-k}$ ，则得到

$$
\int_ {\mathbb {R}} \frac {W (x _ {0} + 2 \pi b ^ {- k} x) - W (x _ {0})}{2 \pi b ^ {- k} x} \cdot x \varphi (x) \mathrm{d} x = \frac {b ^ {k}}{4 \pi} a ^ {k} \mathrm{e} ^ {- \mathrm{i} b ^ {k} x _ {0}}. \tag {21.4.29}
$$

结合 (21.4.28) 式和 (21.4.29) 式得到  $\lim_{k\to+\infty}\frac{b^{k}}{4\pi}a^{k}e^{-ib^{k}x_{0}}=0.$

这与  $ab \geqslant 1$  矛盾. 因此 W 无处可微. 同理可证 S 无处可微.

□

例中的函数 $\varphi \in \mathcal{S}$ 不恒为零, 但满足

$$
\int_ {\mathbb {R}} x ^ {n} \varphi (x) \mathrm{d} x = 0, \quad \forall n \geqslant 0.
$$

这与有界区间上的情形不同.

同样可以构造出处处连续但无处 Hölder 连续的函数.

例 21.4.5 证明  $g(x):=\sum_{n=1}^{\infty}\frac{\cos2^{n}x}{n^{2}}$  处处连续但处处不 Hölder 连续.

证明 易证 $g$ 处处连续. 若对某个 $x_0 \in \mathbb{R}$, 存在 $\alpha \in (0,1)$ 使得函数 $g$ 在 $x_0$ 点满足 $\alpha$ 阶 Hölder 条件, 即存在 $\delta > 0$ 以及常数 $C > 0$ 使得

$$
| g (x) - g (x _ {0}) | \leqslant C | x - x _ {0} | ^ {\alpha}, \quad \forall x \in (x _ {0} - \delta , x _ {0} + \delta).
$$

取 $C_c^\infty$ 函数 $\psi$ 使得 $\psi(1) = 1$, $\operatorname{supp} \psi \subseteq \left[\frac{1}{2}, 2\right]$, $\varphi = \stackrel{\vee}{\psi}$. 则当 $\varepsilon$ 在 $(0,1)$ 中变化时,

$$
\int_ {\mathbb {R}} \frac {g (x _ {0} + 2 \pi \varepsilon x) - g (x _ {0})}{| 2 \pi \varepsilon x | ^ {\alpha}} \cdot | x | ^ {\alpha} \varphi (x) \mathrm{d} x
$$

有界. 而另一方面, 当 $k$ 充分大时,

$$
\begin{array}{l} \int_ {\mathbb {R}} \frac {g (x _ {0} + 2 \pi \cdot 2 ^ {- k} x) - g (x _ {0})}{| 2 \pi \cdot 2 ^ {- k} x | ^ {\alpha}} \cdot | x | ^ {\alpha} \varphi (x) \mathrm{d} x \\ = \frac {2 ^ {(k - 1) \alpha}}{\pi^ {\alpha}} \int_ {\mathbb {R}} g (x _ {0} + 2 \pi \cdot 2 ^ {- k} x) \varphi (x) \mathrm{d} x - \frac {2 ^ {(k - 1) \alpha}}{\pi^ {\alpha}} g (x _ {0}) \widehat {\varphi} (0) \\ = \frac {2 ^ {(k - 1) \alpha}}{\pi^ {\alpha}} \sum_ {n = 1} ^ {\infty} \int_ {\mathbb {R}} \frac {\cos \left(2 ^ {n} (x _ {0} + 2 \pi \cdot 2 ^ {- k} x)\right)}{n ^ {2}} \varphi (x) \mathrm{d} x \\ = \frac {2 ^ {(k - 1) \alpha}}{2 \pi^ {\alpha}} \sum_ {n = 1} ^ {\infty} \int_ {\mathbb {R}} \frac {1}{n ^ {2}} \left[ \mathrm{e} ^ {\mathrm{i} 2 ^ {n} (x _ {0} + 2 \pi \cdot 2 ^ {- k} x)} + \mathrm{e} ^ {- \mathrm{i} 2 ^ {n} (x _ {0} + 2 \pi \cdot 2 ^ {- k} x)} \right] \varphi (x) \mathrm{d} x \\ = \frac {2 ^ {(k - 1) \alpha}}{2 \pi^ {\alpha}} \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2}} \left(\mathrm{e} ^ {\mathrm{i} 2 ^ {n} x _ {0}} \widehat {\varphi} (- 2 ^ {n - k}) + \mathrm{e} ^ {- \mathrm{i} 2 ^ {n} x _ {0}} \widehat {\varphi} (2 ^ {n - k})\right) \\ = \frac {2 ^ {(k - 1) \alpha}}{2 k ^ {2} \pi^ {\alpha}} \mathrm{e} ^ {- \mathrm{i} 2 ^ {k} x _ {0}} \\ \end{array}
$$

无界. 得到矛盾. 因此, $g$ 处处连续无处 Hölder 连续.

在推论 21.4.6 的证明中, 用到了如下关于卷积的 Young 不等式. 为简单起见, 我们仅在速降函数内考虑该不等式.

定理21.4.8 设 $q, p, r \in [1, +\infty]$ 满足

$$
\frac {1}{q} = \frac {1}{p} + \frac {1}{r} - 1, \tag {21.4.30}
$$

$f,g\in \mathcal{S}$ ，则有

$$
\| f * g \| _ {q} \leqslant \| f \| _ {p} \| g \| _ {r}. \tag {21.4.31}
$$

证明 记  $q', p', r'$  为 q, p, r 的对偶数.

由于当 $q, p, r$ 之一为1或 $+\infty$ 时证明是简单的，不妨设 $q, p, r \in (1, +\infty)$. 要证明(21.4.31)式，只要对 $h \in L^{q'}(\mathbb{R}^n)$ 证明

$$
\int_ {\mathbb {R}} (f * g) (x) h (x) \mathrm{d} x \leqslant \| f \| _ {p} \| g \| _ {r} \| h \| _ {q ^ {\prime}}.
$$

即

$$
\int_ {\mathbb {R}} \mathrm{d} x \int_ {\mathbb {R}} f (y - x) g (y) h (x) \mathrm{d} y \leqslant \| f \| _ {p} \| g \| _ {r} \| h \| _ {q ^ {\prime}}. \tag {21.4.32}
$$

不妨设  $\|f\|_{p}=\|g\|_{r}=\|h\|_{q^{\prime}}=1$ . 若

$$
\alpha , \beta , \gamma , u, v, w \in (0, 1), \qquad u + v + w = 1, \tag {21.4.33}
$$

则

$$
\begin{array}{l} f (y - x) g (y) h (x) \\ = f ^ {\alpha} (y - x) g ^ {\beta} (y) f ^ {1 - \alpha} (y - x) h ^ {\gamma} (x) g ^ {1 - \beta} (y) h ^ {1 - \gamma} (x) \\ \leqslant u | f (y - x) | ^ {\frac {\alpha}{u}} | g (y) | ^ {\frac {\beta}{u}} + v | f (y - x) | ^ {\frac {1 - \alpha}{v}} | h (x) | ^ {\frac {\gamma}{v}} + w | g (y) | ^ {\frac {1 - \beta}{w}} | h (x) | ^ {\frac {1 - \gamma}{w}}. \tag {21.4.34} \\ \end{array}
$$

进一步, 若

$$
\frac {\alpha}{u} = \frac {1 - \alpha}{v} = p, \quad \frac {\beta}{u} = \frac {1 - \beta}{w} = r, \quad \frac {\gamma}{v} = \frac {1 - \gamma}{w} = q ^ {\prime}, \tag {21.4.35}
$$

则对 (21.4.34) 式积分即得 (21.4.32) 式. 不难解得 (21.4.33) 式和 (21.4.35) 式的解为

$$
\alpha = \frac {p}{q}, \quad \beta = \frac {r}{q}, \quad \gamma = \frac {q ^ {\prime}}{r ^ {\prime}}, \quad u = \frac {1}{q}, \quad v = \frac {1}{r ^ {\prime}}, \quad w = \frac {1}{p ^ {\prime}}. \tag {21.4.36}
$$

定理由此得证.

## 习题21.4

1. 设 $f \in \mathcal{R}^1(\mathbb{R})$, 试用 $f$ 的 Fourier 变换表示以下函数的 Fourier 变换.

(1)  $g(x) := f(x + x_{0})$ , 其中  $x_{0} \in R$ ;
(2)  $g(x) := f(rx)$ ，其中  $r \neq 0$  为给定实数.

2. 设 $f \in C_c^2(\mathbb{R})$，证明 $\lim_{x \to \infty} |x^2 \widehat{f}(x)| = 0$。进而对于任何 $g \in \mathcal{R}^\infty(\mathbb{R})$，有

$$
\lim _ {T \to + \infty} \sum_ {n = - \infty} ^ {\infty} \frac {1}{T} \widehat {f} \left(\frac {n}{T}\right) g \left(\frac {n}{T}\right) = \int_ {\mathbb {R}} \widehat {f} (x) g (x) \mathrm{d} x.
$$