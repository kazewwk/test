# 下册 / 第二十一章 Fourier级数

原始 PDF 第 789–841 页。

## 第二十一章

## Fourier 级数

---

150

第二十一章 Fourier 级数

## 21.1 三角级数与 Fourier 级数

设 $T > 0$ ，形为

$$
\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {n \pi x}{T} + b _ {n} \sin \frac {n \pi x}{T}\right) \tag {21.1.1}
$$

的函数项级数, 称为 (周期为 ${2T}$ 的) 三角级数. 函数列

$$
1, \cos \frac {\pi x}{T}, \sin \frac {\pi x}{T}, \cos \frac {2 \pi x}{T}, \sin \frac {2 \pi x}{T}, \cos \frac {3 \pi x}{T}, \sin \frac {3 \pi x}{T}, \dots \tag {21.1.2}
$$

称为  $[-T,T]$  上的基本三角函数系.

对

$$
f (x) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {n \pi x}{T} + b _ {n} \sin \frac {n \pi x}{T}\right)
$$

形式上作逐项积分, 有

$$
a _ {n} = \frac {1}{T} \int_ {0} ^ {2 T} f (x) \cos \frac {n \pi x}{T} \mathrm{d} x, \quad b _ {n} = \frac {1}{T} \int_ {0} ^ {2 T} f (x) \sin \frac {n \pi x}{T} \mathrm{d} x, \quad n \geqslant 0. \tag {21.1.3}
$$

为保证 (21.1.3) 式有意义, 一般我们假设 $f$ 是 $[0, 2T]$ 上的绝对可积函数. 在本章中, 我们对绝对可积函数的瑕点集作一个界定. 为方便起见, 我们把函数无定义的点也归入瑕点. 在定义广义积分时, 如果在任何有界区间内, 瑕点都只有有限个, 则可以方便地定义广义积分. 进一步, 若任何有界区间内瑕点集只有有限个聚点, 也可以方便地定义广义积分. 鉴于此, 在绝对可积函数的定义中, 我们要求 (允许) 在有界区间内, 瑕点集的导集是有限集, 即瑕点集的导集的导集 (本章中称之为两阶导集) 是空集. 此时, 瑕点集必然是至多可列的.

对于以 $2T$ 为周期且在 $[0,2T]$ 上绝对可积的函数 $f$, 可由 (21.1.3) 式给出一个三角级数 (21.1.1), 我们称之为 $f$ 的 Fourier 级数①, 记作

$$
f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos \frac {n \pi x}{T} + b _ {n} \sin \frac {n \pi x}{T}\right). \tag {21.1.4}
$$

此时， $\{a_{n}\}$  和  $\{b_{n}\}$  称为 f 的 Fourier 系数.

通过伸缩变换, 对周期为 $2T$ 的函数的研究可转化为对周期为 $2\pi$ 的函数的研究. 因此, 以下主要考虑 $T = \pi$ 的情形. 此时, (21.1.3) 式与 (21.1.4) 式化为

$$
a _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} f (x) \cos n x \mathrm{d} x, \quad b _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 T} f (x) \sin n x \mathrm{d} x, \quad n \geqslant 0. \tag {21.1.5}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 引入Lebesgue积分后，可以把基于Riemann积分的绝对可积性减弱为基于Lebesgue积分的绝对可积性（等价于Lebesgue可积).具体地，对于以 $2T$ 为周期且在 $[0,2T]$ 上Lebesgue可积的函数 $f$ ，称由(21.1.3)式给出的三角级数(21.1.1)为 $f$ 的Fourier级数</span></small>

---

21.1 三角级数与 Fourier 级数

151

$$
f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} (a _ {n} \cos n x + b _ {n} \sin n x). \tag {21.1.6}
$$

由于只要给出一个周期上的函数值, 就能够确定周期函数在其他点的函数值, 所以我们经常只给出函数在一个周期的值. 习惯上, 人们在表达函数时, 会给出函数在闭区间 $[0, 2\pi]$ 上 (或 $[- \pi, \pi]$ 上) 的表达式. 若函数在端点的值不相等, 则与周期性矛盾. 我们忽略这一矛盾——因为 (在有界区间内) 改变有限个点上的函数值, 不影响函数的 Fourier 级数.

为方便起见, 对一些函数空间引入如下记号. 若 $f$ 在区间 $I$ 上绝对可积, 记 $f \in \mathcal{R}^1(I)$. 一般地, 对于 $p \in [1, +\infty)$, 若 $(f^+)^p, (f^-)^p \in \mathcal{R}^1(I)$, 则记 $f \in \mathcal{R}^p(I)$, 并称 $f$ 在 $I$ 上 $p$ 次可积, 称 $\| f \|_{\mathcal{R}^p(I)} := \left( \int_I |f(x)|^p \, \mathrm{d}x \right)^{\frac{1}{p}}$ 为 $f$ 在 $I$ 上的 $p$-范数. 对应于 $p = +\infty$, 若 $f$ 在 $I$ 上有界, 且在 $I$ 的有界子区间上 Riemann 可积, 则记 $f \in \mathcal{R}^\infty(I)$, 并定义

$$
\| f \| _ {\infty} \equiv \| f \| _ {\mathcal {R} ^ {\infty} (I)} := \inf \left\{\sup _ {x \in I} | g (x) | \Big | \int_ {I} | f (x) - g (x) | \mathrm{d} x = 0, g \in \mathcal {R} ^ {\infty} (I) \right\}. \tag {21.1.7}
$$

若 I 是有界区间, 则我们有

$$
\| f \| _ {\mathcal {R} ^ {\infty} (I)} = \lim _ {p \to + \infty} \| f \| _ {\mathcal {R} ^ {p} (I)}.
$$

一般地，

$$
\| f \| _ {\mathcal {R} ^ {\infty} (I)} = \lim _ {A \to + \infty} \lim _ {p \to + \infty} \| f \| _ {\mathcal {R} ^ {p} (I \cap [ - A, A ])}
$$

容易证明, 对于 $p \in [1, +\infty]$, 若 $f, g \in \mathcal{R}^p(I)$, $\alpha, \beta \in \mathbb{R}$, 则 $\alpha f + \beta g \in \mathcal{R}^p(I)$. 具体地, 对于 $p \in (1, +\infty)$, 设 $q = \frac{p}{p - 1}$ 为其对偶数, 则利用 Young 不等式, 对于 $f \in \mathcal{R}^p(I), g \in \mathcal{R}^q(I), \|f\|_{\mathcal{R}^p(I)} = \|g\|_{\mathcal{R}^p(I)} = 1$, 可得

$$
\int_ {I} \left| f (x) g (x) \right| \mathrm{d} x \leqslant \int_ {I} \left(\frac {1}{p} \big | f (x) \big | ^ {p} + \frac {1}{q} \big | g (x) \big | ^ {q}\right) \mathrm{d} x = 1.
$$

一般地, 得到积分型的 Hölder 不等式

$$
\left| \int_ {I} f (x) g (x) \mathrm{d} x \right| \leqslant \| f \| _ {\mathcal {R} ^ {p} (I)} \| g \| _ {\mathcal {R} ^ {q} (I)}, \quad \forall f \in \mathcal {R} ^ {p} (I), g \in \mathcal {R} ^ {q} (I). \tag {21.1.8}
$$

基于 Hölder 不等式, 对于  $f_{k} \in \|f\|_{\mathcal{R}^{p}(I)} (k = 1, 2, \cdots, n)$ , 有

$$
\int_ {I} \left(\sum_ {k = 1} ^ {n} \left| f _ {k} (x) \right|\right) ^ {p} \mathrm{d} x = \sum_ {j = 1} ^ {n} \int_ {I} \left(\sum_ {k = 1} ^ {n} \left| f _ {k} (x) \right|\right) ^ {p - 1} \left| f _ {j} (x) \right| \mathrm{d} x
$$

---

152

第二十一章 Fourier级数

$$
\leqslant \sum_ {j = 1} ^ {n} \left(\int_ {I} \left(\sum_ {k = 1} ^ {n} | f _ {k} (x) |\right) ^ {p} \mathrm{d} x\right) ^ {\frac {p - 1}{p}} \left(\int_ {I} | f _ {j} (x) | ^ {p} \mathrm{d} x\right) ^ {\frac {1}{p}}.
$$

由此得到积分型的 Minkowski 不等式

$$
\left\| \sum_ {k = 1} ^ {n} f _ {k} \right\| _ {\mathcal {R} ^ {p} (I)} \leqslant \sum_ {k = 1} ^ {n} \| f _ {k} \| _ {\mathcal {R} ^ {p} (I)}, \quad \forall f _ {k} \in \mathcal {R} ^ {p} (I), 1 \leqslant k \leqslant n. \tag {21.1.9}
$$

易见 Minkowski 不等式中的和式也可以改为无穷级数. 另一方面, 它对于 $p = 1, +\infty$ 也成立. Minkowski 不等式表明 $\| \cdot \|_{\mathcal{R}^p(I)}$ 确实是一个范数①.

进一步, 用 $C_{\#}^{k}(\mathbb{R})$ 表示 $\mathbb{R}$ 中以 $2\pi$ 为周期且 $k$ 阶连续可导的实函数全体, $C_{\#}^{0}(\mathbb{R})$ 简记为 $C_{\#}(\mathbb{R})$. 用 $\mathcal{R}_{\#}^{p}(\mathbb{R})$ 表示 $\mathbb{R}$ 中以 $2\pi$ 为周期且限制在 $[0, 2\pi]$ 上属于 $\mathcal{R}^{p}[0, 2\pi]$ 的实函数全体②.

在不引起混淆的情况下, 我们把 $\mathcal{R}^p[0, 2\pi]$ (或 $\mathcal{R}^p[-\pi, \pi]$) 视为 $\mathcal{R}_{\#}^p(\mathbb{R})$, 也用 $C_{\#}^k[0, 2\pi]$ (或 $C_{\#}^k[-\pi, \pi]$) 表示 $C_{\#}^k(\mathbb{R})$. 例如, $f \in C_{\#}[0, 2\pi]$ 本质上就是 $f \in C[0, 2\pi]$ 且 $f(0) = f(2\pi)$.

类似地, 可引入  $C_{\#}^{k,\alpha}(\mathbb{R})$  等记号.

由 Euler 公式,  $\cos x = \frac{e^{ix} + e^{-ix}}{2}, \sin x = \frac{e^{ix} - e^{-ix}}{2i}$ , 这样, 形式上, 三角级数

$$
\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} (a _ {n} \cos n x + b _ {n} \sin n x) \tag {21.1.10}
$$

可以化为级数

$$
\sum_ {n = - \infty} ^ {+ \infty} c _ {n} \mathrm{e} ^ {\mathrm{i} n x}, \tag {21.1.11}
$$

其中

$$
c _ {0} := \frac {a _ {0}}{2}, \quad c _ {n} := \frac {a _ {n} - b _ {n} \mathrm{i}}{2}, \quad c _ {- n} := \frac {a _ {n} + b _ {n} \mathrm{i}}{2}, \quad n \geqslant 1. \tag {21.1.12}
$$

(21.1.11) 式称为三角级数 (21.1.10) 的复形式. 复形式具有幂级数形式, 因此, 我们有可能通过幂级数来研究三角级数. 但人们所讨论的三角级数的定义域时常对应相应的幂级数的 (复数域内的) 收敛域的边界, 而幂级数在边界的性质比较复杂, 因此, 直接利用幂级数来研究三角级数通常不是很便利.

当 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 是偶函数时, 它的Fourier系数满足

$$
a _ {n} = \frac {2}{\pi} \int_ {0} ^ {\pi} f (x) \cos n x \mathrm{d} x, \quad b _ {n} = 0, \quad \forall n \geqslant 0. \tag {21.1.13}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 对于 $f, g \in \mathcal{R}^p(I)$, 若 $\int_{I} |f(x) - g(x)| \, \mathrm{d}x = 0$, 我们认为 $f$ 与 $g$ 在 $\mathcal{R}^p(I)$ 中是同一个元素.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② 将上述各定义中 (基于 Riemann 积分) 的绝对可积性改为 Lebesgue 可积, 则相应的空间记为 $L^{p}(I)$, $L_{\#}^{p}(\mathbb{R})$ 等.</span></small>

---

21.1 三角级数与Fourier级数

153

当 $f \in L_{\#}^{1}(\mathbb{R})$ 是奇函数时, 它的Fourier系数满足

$$
a _ {n} = 0, \quad b _ {n} = \frac {2}{\pi} \int_ {0} ^ {\pi} f (x) \sin n x \mathrm{d} x, \quad \forall n \geqslant 0. \tag {21.1.14}
$$

对于 $f\in \mathcal{R}^1 [0,\pi ]$ ，我们可以将它延拓成以 $2\pi$ 为周期的偶函数

$$
f _ {e} (x) := f (| x |), \quad \forall x \in [ - \pi , \pi ]. \tag {21.1.15}
$$

函数 $f_{e}$ 称为 $f$ 的偶延拓. 它的Fourier级数就只含有余弦项. 当通过偶延拓将 $[0, \pi]$ 上的函数展开成Fourier级数时, 我们简称其为将函数展开成余弦级数. 我们也可以将 $f$ 延拓成以 $2\pi$ 为周期的奇函数

$$
f _ {o} (x) := \operatorname{sgn} (x) f (| x |), \quad \forall x \in [ - \pi , \pi ]. \tag {21.1.16}
$$

函数 $f_{o}$ 称为 $f$ 的奇延拓. 它的Fourier级数就只含有正弦项. 当通过奇延拓将 $[0, \pi]$ 上的函数展开成Fourier级数时, 我们简称其为将函数展开成正弦级数.

例 21.1.1 将  $f(x) := \frac{\pi - x}{2} (x \in [0, 2\pi])$  展开成 Fourier 级数.

解 我们有

$$
a _ {0} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} \frac {\pi - x}{2} \mathrm{d} x = 0, \quad a _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} \frac {\pi - x}{2} \cos n x \mathrm{d} x = 0, \quad n \geqslant 1,
$$

$$
b _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} x \sin n x \mathrm{d} x = \frac {1}{n}, \quad n \geqslant 1.
$$

因此，

$$
f (x) \sim \sum_ {n = 1} ^ {+ \infty} \frac {1}{n} \sin n x. \tag {21.1.17}
$$

需要注意的是, 在 (21.1.17) 式中, $f$ 默认为以 $2\pi$ 为周期的函数, 其中 “$\sim$” 不能随便换成 “=” . 如果 $f(x)$ 用其在 $[0, 2\pi]$ 上的表达式 $\frac{\pi - x}{2}$ 代替, 则宜写成

$$
\frac {\pi - x}{2} \sim \sum_ {n = 1} ^ {\infty} \frac {1}{n} \sin n x, \quad x \in [ 0, 2 \pi ]. \tag {21.1.18}
$$

□

例 21.1.2 将  $f(x):=-\ln\left(2\sin\frac{x}{2}\right)$  ( $x\in(0,2\pi)$ ) 展开成 Fourier 级数.

解 由例10.3.7可得

$$
a _ {0} = - \frac {1}{\pi} \int_ {0} ^ {2 \pi} \ln \left(2 \sin \frac {x}{2}\right) \mathrm{d} x = - 2 \ln 2 - \frac {2}{\pi} \int_ {0} ^ {\pi} \ln \sin x \mathrm{d} x = 0.
$$

而对于自然数 $n$ 易得

$$
\int_ {0} ^ {\pi} \frac {\sin (n + 2) x - \sin n x}{\sin x} \mathrm{d} x = 2 \int_ {0} ^ {\pi} \cos (n + 1) x \mathrm{d} x = 0.
$$

---

154

第二十一章 Fourier 级数

于是归纳可得

$$
\int_ {0} ^ {\pi} \frac {\sin (2 n + 1) x}{\sin x} \mathrm{d} x = \pi , \quad n \geqslant 0. \tag {21.1.19}
$$

从而

$$
\begin{array}{l} a _ {n} = - \frac {1}{\pi} \int_ {0} ^ {2 \pi} \ln \left(2 \sin \frac {x}{2}\right) \cos n x \mathrm{d} x = - \frac {2}{\pi} \int_ {0} ^ {\pi} \ln (2 \sin x) \cos 2 n x \mathrm{d} x \\ = \frac {2}{\pi} \int_ {0} ^ {\pi} \frac {\sin 2 n x \cos x}{2 n \sin x} \mathrm{d} x = \frac {1}{2 n \pi} \int_ {0} ^ {\pi} \frac {\sin (2 n + 1) x + \sin (2 n - 1) x}{\sin x} \mathrm{d} x \\ = \frac {1}{n}, \quad n \geqslant 1. \\ \end{array}
$$

另一方面, 注意到 $f$ (以 $2\pi$ 为周期作延拓后) 是偶函数, 可得 $b_{n} = 0 (n \geqslant 1)$. 因此,

$$
f (x) \sim \sum_ {n = 1} ^ {\infty} \frac {\cos n x}{n}.
$$

对于以 $2\pi$ 为周期的复值函数, 同样可以用 (21.1.5) 式和 (21.1.6) 式定义其 Fourier 级数. 简单说来, 复值函数 $f$ 的 Fourier 级数的实部和虚部就是 $f$ 的实部与虚部的 Fourier 级数.

例 21.1.3 设  $\lambda \in C, \lambda \neq 0$ ，将  $f(x) := e^{\lambda x} (x \in [0, 2\pi])$  展开成 Fourier 级数.

解 直接计算得到

$$
a _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} \mathrm{e} ^ {\lambda x} \cos n x \mathrm{d} x = \frac {\lambda (\mathrm{e} ^ {2 \pi \lambda} - 1)}{\pi (n ^ {2} + \lambda^ {2})}, \quad n \geqslant 0,
$$

$$
b _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} \mathrm{e} ^ {\lambda x} \sin n x \mathrm{d} x = - \frac {n (\mathrm{e} ^ {2 \pi \lambda} - 1)}{\pi (n ^ {2} + \lambda^ {2})}, \quad n \geqslant 1.
$$

因此，

$$
f (x) \sim \frac {\mathrm{e} ^ {2 \pi \lambda} - 1}{2 \pi \lambda} + \sum_ {n = 1} ^ {\infty} \frac {\mathrm{e} ^ {2 \pi \lambda} - 1}{\pi (n ^ {2} + \lambda^ {2})} (\lambda \cos n x - n \sin n x). \tag {21.1.20}
$$

特别地, 若 $\alpha$ 为非整的实数, $\lambda = \mathrm{i}\alpha$, 则得到

$$
\cos (\alpha x) \sim \frac {\sin (2 \pi \alpha)}{2 \pi \alpha} + \sum_ {n = 1} ^ {\infty} \frac {2 \sin (\pi \alpha)}{\pi (n ^ {2} - \alpha^ {2})} \left[ - \alpha \cos (\pi \alpha) \cos n x + n \sin (\pi \alpha) \sin n x \right],
$$

$$
x \in [ 0, 2 \pi ],
$$

$$
\sin (\alpha x) \sim \frac {\sin^ {2} (\pi \alpha)}{\pi \alpha} + \sum_ {n = 1} ^ {\infty} \frac {2 \sin (\pi \alpha)}{\pi (n ^ {2} - \alpha^ {2})} [ - \alpha \sin (\pi \alpha) \cos n x + n \cos (\pi \alpha) \sin n x ],
$$

$$
x \in [ 0, 2 \pi ].
$$

□

---

21.1 三角级数与 Fourier 级数

155

例 21.1.4 将  $f(x) := \cos x (x \in [0, \pi])$  展开成正弦级数.

解 直接计算得到

$$
b _ {n} = \frac {2}{\pi} \int_ {0} ^ {\pi} \cos x \sin n x \mathrm{d} x = \left\{ \begin{array}{l l} {{\frac {4 n}{(n ^ {2} - 1) \pi}},} & {{n \text {为偶数},}} \\ {{0,}} & {{n \text {为奇数}.}} \end{array} \right.
$$

因此

$$
f (x) \sim \sum_ {n = 1} ^ {\infty} \frac {8 n}{(4 n ^ {2} - 1) \pi} \sin 2 n x.
$$

例 21.1.5 将  $f(x) := \sin x (x \in [0, \pi])$  展开成余弦级数.

解 直接计算得到

$$
a _ {n} = \frac {2}{\pi} \int_ {0} ^ {\pi} \sin x \cos n x \mathrm{d} x = \left\{ \begin{array}{l l} - \frac {4}{(n ^ {2} - 1) \pi}, & n \text {为偶数,} \\ 0, & n \text {为奇数.} \end{array} \right.
$$

因此

$$
f (x) \sim \frac {2}{\pi} - \sum_ {n = 1} ^ {\infty} \frac {4}{(4 n ^ {2} - 1) \pi} \cos 2 n x.
$$

## 习题 21.1

1. 设 $f$ 以 $2\pi$ 为周期, 对于 $x \in [0, 2\pi)$, $f(x) = \chi_{[a,b]}(x)$, 其中 $0 \leqslant a < b < 2\pi$. 试将 $f$ 展开成 Fourier 级数.

2. 试将 $|\cos x|$ 和 $|\sin x|$ 展开成 Fourier 级数.

3. 设 $p, q$ 为对偶数, $f \in \mathcal{R}_{\#}^{p}(\mathbb{R}), g \in \mathcal{R}_{\#}^{q}(\mathbb{R})$. 令

$$
h (x) := \int_ {0} ^ {2 \pi} f (y) g (x - y) \mathrm{d} y, \qquad x \in \mathbb {R}.
$$

证明: $h$ 以 $2\pi$ 为周期. 进一步有, 试用 $f, g$ 的 Fourier 系数表示 $h$ 的 Fourier 系数.

4. 设 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$, $h_1(x) := f(-x)$, $h_2(x) := f(x + x_0)(x \in \mathbb{R})$, 其中 $x_0 \in \mathbb{R}$. 试用 $f$ 的 Fourier 系数表示 $h_1$ 和 $h_2$ 的 Fourier 系数.

5. 设 $f(x) := x^2 - x (x \in [0, \pi])$. 试将 $f$ 分别展开成以 $2\pi$ 为周期的余弦级数和正弦级数.

6. 设 $k \geqslant 1, a_{n}, b_{n}$ 为 $f \in C_{\#}^{k}(\mathbb{R})$ 的 Fourier 系数. 证明: $\lim_{n \to +\infty} n^{k} a_{n} = \lim_{n \to +\infty} n^{k} b_{n} = 0$.

---

156

第二十一章 Fourier 级数

7. 给定 $m \geqslant 1$.

(1) 证明: 当 $n \to +\infty$ 时, $m$ 阶三角多项式列

$$
T _ {n} (x) = a _ {n 0} + \sum_ {k = 1} ^ {m} (a _ {n k} \cos k x + b _ {n k} \sin k x)
$$

关于 $x \in [0, 2\pi]$ 一致收敛当且仅当对每个 $k$ ($0 \leqslant k \leqslant m$), $\{a_{nk}\}$ 和 $\{b_{nk}\}$ 均收敛.

(2) 设 $\mathcal{T}_m$ 表示以 $2\pi$ 为周期的 $m$ 阶三角多项式全体. 证明: $\forall f \in C_{\#}(\mathbb{R})$, 存在 $S \in \mathcal{T}_m$, 使得

$$
\max _ {x \in [ 0, 2 \pi ]} | f (x) - S (x) | = \inf _ {T (x) \in \mathcal {T} _ {m}} \max _ {x \in [ 0, 2 \pi ]} | f (x) - T (x) |.
$$

8. 试寻找比习题 6. 更一般的条件使得 $f$ 的 Fourier 系数 ${a}_{n},{b}_{n}$ 满足

$$
\lim _ {n \to + \infty} n ^ {k} a _ {n} = \lim _ {n \to + \infty} n ^ {k} b _ {n} = 0.
$$

## 21.2 Fourier 级数的收敛性

本节主要介绍 Fourier 级数本身的收敛性以及 Cesáro 求和意义下的收敛性. 在此基础上, 进一步讨论逐项可积性, 逐项可微性以及一致收敛性.

## 21.2.1 Fourier 级数部分和的收敛性, Dirichlet 积分

对于 $f\in \mathcal{R}_\#^1 (\mathbb{R})$ ，设其Fourier级数为

$$
f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} (a _ {n} \cos n x + b _ {n} \sin n x). \tag {21.2.1}
$$

则利用

$$
\frac {1}{2} + \sum_ {k = 1} ^ {n} \cos n x = \frac {\sin \left(n + \frac {1}{2}\right) x}{2 \sin \frac {x}{2}}, \quad x \neq 2 k \pi , \tag {21.2.2}
$$

可得 $f$ 的Fourier级数部分和的表达式. 具体地, 有

$$
S _ {n} (f; x) := a _ {0} + \sum_ {k = 1} ^ {n} (a _ {k} \cos k x + b _ {k} \sin k x)
$$

---

21.2 Fourier 级数的收敛性

157

$$
\begin{array}{l} = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} f (\theta) \mathrm{d} \theta + \frac {1}{\pi} \sum_ {k = 1} ^ {n} \left(\int_ {0} ^ {2 \pi} f (\theta) \cos k \theta \mathrm{d} \theta \cos k x + \int_ {0} ^ {2 \pi} f (\theta) \sin k \theta \mathrm{d} \theta \sin k x\right) \\ = \frac {1}{\pi} \int_ {0} ^ {2 \pi} f (\theta) \left(\frac {1}{2} + \sum_ {k = 1} ^ {n} \cos k (\theta - x)\right) \mathrm{d} \theta = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (\theta + x) \left(\frac {1}{2} + \sum_ {k = 1} ^ {n} \cos k \theta\right) \mathrm{d} \theta \\ = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (\theta + x) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta (21.2.3) \\ = \frac {1}{\pi} \int_ {0} ^ {\pi} (f (x + \theta) + f (x - \theta)) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta , \quad \forall n \geqslant 0, x \in \mathbb {R}. (21.2.4) \\ \end{array}
$$

称 (21.2.3) 式中的积分为 Dirichlet 积分, 函数  $\frac{\sin\left(n+\frac{1}{2}\right)\theta}{2\pi\sin\frac{\theta}{2}}$  称为 Dirichlet 核.

在 (21.2.4) 式中令 $f = 1$ (或对 (21.2.2) 式积分, 或利用 (21.1.19) 式) 可得

$$
\frac {1}{\pi} \int_ {0} ^ {\pi} \frac {\sin \left(n + \frac {1}{2}\right) \theta}{\sin \frac {\theta}{2}} \mathrm{d} \theta = 1, \quad \forall n \geqslant 0. \tag {21.2.5}
$$

于是, 对于 $A \in \mathbb{R}$, 我们有

$$
S _ {n} (f; x) - A = \frac {1}{\pi} \int_ {0} ^ {\pi} (f (x + \theta) + f (x - \theta) - 2 A) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta . \tag {21.2.6}
$$

为处理 Dirichlet 积分, 我们将例 9.5.1 中的 Riemann-Lebesgue 引理推广到 $\mathcal{R}^1(\mathbb{R})$ 中.

引理 21.2.1 设  $f \in R^{1}[a, b]$ ，则

$$
\lim _ {p \to \infty} \int_ {\mathbb {R}} f (x) \cos p x \mathrm{d} x = \lim _ {p \to \infty} \int_ {\mathbb {R}} f (x) \sin p x \mathrm{d} x = 0. \tag {21.2.7}
$$

证明 不失一般性, 设 0 为 f 唯一可能的瑕点, 则由例 9.5.1,

$$
\begin{array}{l} \varlimsup_ {p \to \infty} \left| \int_ {\mathbb {R}} f (x) \cos p x \mathrm{d} x \right| \\ \leqslant \int_ {A} ^ {+ \infty} | f (x) | \mathrm{d} x + \int_ {- \infty} ^ {A} | f (x) | \mathrm{d} x + \int_ {- \varepsilon} ^ {\varepsilon} | f (x) | \mathrm{d} x, \quad \forall A > \varepsilon > 0. \\ \end{array}
$$

令 $A \to +\infty, \varepsilon \to 0^{+}$ 即得 $\lim_{p \to \infty} \int_{\mathbb{R}} f(x) \cos px \, \mathrm{d}x = 0.$ 同理，$\lim_{p \to \infty} \int_{\mathbb{R}} f(x) \sin px \, \mathrm{d}x = 0.$

---

158

第二十一章 Fourier 级数

由 Riemann-Lebesgue 引理和 (21.2.6) 式, 立即可得如下的局部性原理.

定理21.2.2 设 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$，则任取 $\delta \in (0, \pi)$，$f$ 的Fourier级数在点 $x$ 处是否收敛及级数的和均只与 $f$ 在 $(x - \delta, x + \delta)$ 内的值有关。

证明 事实上, 我们要证明的就是对于任何 $A \in \mathbb{R}$, 成立

$$
\lim _ {n \to + \infty} \frac {1}{\pi} \int_ {\delta} ^ {\pi} (f (x + \theta) + f (x - \theta) - 2 A) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta = 0. \tag {21.2.8}
$$

注意到 $\theta \mapsto \frac{f(x + \theta) + f(x - \theta) - 2A}{2\sin\frac{\theta}{2}}$ 在 $[\delta, \pi]$ 上绝对可积, (21.2.8) 式是 Riemann-Lebesgue 引理的直接推论.

以下给出 Fourier 级数在给定点收敛的常用的两个判别法. 首先, 有如下的 Dini-Lipschitz 判别法.

定理 21.2.3 设  $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ ,  $x_{0} \in R$ . 若  $f(x_{0}^{+})$  和  $f(x_{0}^{-})$  均存在, 且存在  $\alpha \in (0,1]$  以及 M > 0,  $\delta \in (0,\pi)$ , 使得 f 在  $x_{0}$  处满足如下的 “Hölder 条件”:

$$
\left\{ \begin{array}{l l} \big | f (x) - f (x _ {0} ^ {+}) \big | \leqslant M \big | x - x _ {0} \big | ^ {\alpha}, & \forall   x \in (x _ {0}, x _ {0} + \delta), \\ \big | f (y) - f (x _ {0} ^ {-}) \big | \leqslant M \big | y - x _ {0} \big | ^ {\alpha}, & \forall   y \in (x _ {0} - \delta , x _ {0}). \end{array} \right. \tag {21.2.9}
$$

则

$$
\lim _ {n \to + \infty} S _ {n} (f; x _ {0}) = \frac {f (x _ {0} ^ {+}) + f (x _ {0} ^ {-})}{2}. \tag {21.2.10}
$$

证明 记

$$
g (\theta) = \left(f (x _ {0} + \theta) + f (x _ {0} - \theta) - f (x _ {0} ^ {+}) - f (x _ {0} ^ {-})\right) \frac {1}{2 \sin \frac {\theta}{2}}, \qquad \theta \in (0, \pi ].
$$

则由定理假设, 可见 $g \in \mathcal{R}^{1}[0, \pi]$. 从而, 由 Riemann-Lebesgue 引理

$$
\lim _ {n \to + \infty} \int_ {0} ^ {\pi} g (\theta) \sin \left(n + \frac {1}{2}\right) \theta \mathrm{d} \theta = 0.
$$

因此，

$$
\begin{array}{l} \lim _ {n \to + \infty} S _ {n} (f; x _ {0}) = \lim _ {n \to + \infty} \frac {1}{\pi} \int_ {0} ^ {\pi} (f (x + \theta) + f (x - \theta)) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta \\ = \lim _ {n \to + \infty} \frac {1}{\pi} \int_ {0} ^ {\pi} \left(f (x _ {0} ^ {+}) + f (x _ {0} ^ {-})\right) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta = \frac {f (x _ {0} ^ {+}) + f (x _ {0} ^ {-})}{2}. \\ \end{array}
$$

□

---

21.2 Fourier级数的收敛性

159

由积分第二中值定理 (参见定理 9.5.5), 我们可以利用单调性来得到 Fourier 级数收敛性的另一个常用判别法. 首先, 我们给出如下的 Dirichlet 引理.

引理 21.2.4 设 a > 0, f 在  $[0, a]$  上单调, 则

$$
\lim _ {p \to \infty} \int_ {0} ^ {a} \frac {f (x) - f (0 ^ {+})}{x} \sin p x \mathrm{d} x = 0. \tag {21.2.11}
$$

证明 由于 $\int_0^{+\infty}\frac{\sin x}{x}\mathrm{d}x$ 收敛.因此，存在常数 $C > 0$ 使得

$$
\left| \int_ {0} ^ {A} \frac {\sin x}{x} \mathrm{d} x \right| \leqslant C, \quad \forall A > 0. \tag {21.2.12}
$$

任取 $\delta \in (0,a)$ ，由积分第二中值定理，存在 $\xi \in [0,\delta ]$ 使得

$$
\begin{array}{l} \left| \int_ {0} ^ {\delta} \frac {f (x) - f (0 ^ {+})}{x} \sin p x \mathrm{d} x \right| = \left| (f (\delta) - f (0 ^ {+})) \int_ {\xi} ^ {\delta} \frac {\sin p x}{x} \mathrm{d} x \right| \\ = \left| (f (\delta) - f (0 ^ {+})) \int_ {| p | \xi} ^ {| p | \delta} \frac {\sin x}{x} \mathrm{d} x \right| \leqslant 2 C | f (\delta) - f (0 ^ {+}) |. \tag {21.2.13} \\ \end{array}
$$

于是, 注意到 $x \mapsto \frac{f(x) - f(0^+)\}{x}$ 在 $[\delta, a]$ 上可积, 由 Riemann-Lebesgue 引理,

$$
\begin{array}{l} \overline {{\lim _ {p \to \infty}}} \left| \int_ {0} ^ {a} \frac {f (x) - f (0 ^ {+})}{x} \sin p x \mathrm{d} x \right| \\ = \varlimsup_ {p \to \infty} \left| \int_ {0} ^ {\delta} \frac {f (x) - f (0 ^ {+})}{x} \sin p x \mathrm{d} x \right| \leqslant 2 C | f (\delta) - f (0 ^ {+}) |. \\ \end{array}
$$

再令  $\delta \rightarrow 0^{+}$  即得 (21.2.11) 式.

基于上述引理, 立即可得如下的 Dirichlet-Jordan 判别法.

定理 21.2.5 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R}), x_{0} \in \mathbb{R}$. 进一步, 存在 $\delta \in (0, \pi)$, 使得 $f$ 在 $[x_{0} - \delta, x_{0} + \delta]$ 上是两个单调函数之和. 则 (21.2.10) 式成立.

证明 注意到 0 是 $\theta \mapsto \frac{1}{2\sin\frac{\theta}{2}} -\frac{1}{\theta}$ 的可去间断点, 由 (局部性原理和) Riemann-Lebesgue 引理以及 Dirichlet 引理, 可得

$$
\begin{array}{l} \lim _ {n \to + \infty} \left(S _ {n} (f; x _ {0}) - \frac {f (x _ {0} ^ {+}) + f (x _ {0} ^ {-})}{2}\right) \\ = \lim _ {n \to + \infty} \frac {1}{\pi} \int_ {0} ^ {\delta} \left(f (x _ {0} + \theta) + f (x _ {0} - \theta) - f (x _ {0} ^ {+}) - f (x _ {0} ^ {-})\right) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta \\ \end{array}
$$

---

160

第二十一章 Fourier级数

$$
= \lim _ {n \to + \infty} \frac {1}{\pi} \int_ {0} ^ {\delta} \left(f (x _ {0} + \theta) + f (x _ {0} - \theta) - f (x _ {0} ^ {+}) - f (x _ {0} ^ {-})\right) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{\theta} \mathrm{d} \theta = 0.
$$

即 (21.2.10) 成立.

我们看到, Fourier 级数在一点收敛的条件比较弱. 自然地, 人们提出这样的问题, 若 $f \in \mathcal{R}_{\#}(\mathbb{R})$ 在 $x_0$ 处连续, 是否有 $\lim_{n \to +\infty} S_n(f; x_0) = f(x_0)$? 这一问题的回答是否定的. du Bois-Reymond①于 1876 年给出了连续周期函数的 Fourier 级数在某些点不收敛的例子 (参见 [23]).

## 21.2.2 Fourier 级数的 Cesáro 和的收敛性, Fejér 积分

由于 Cesáro 求和法可提升级数的收敛性, 我们考虑 Fourier 级数的 Cesáro 和. 对 Fourier 级数的部分和作平均, 可得

$$
\sigma_ {n} (f; x) := \frac {1}{n} \sum_ {k = 0} ^ {n - 1} S _ {k} (f; x) = \frac {1}{2 n \pi} \int_ {- \pi} ^ {\pi} f (x + t) \left(\frac {\sin \frac {n t}{2}}{\sin \frac {t}{2}}\right) ^ {2} \mathrm{d} t, \quad n \geqslant 1. \tag {21.2.14}
$$

上式中的积分称为 Fejér $^{②}$  积分，函数  $\frac{1}{2n\pi}\left(\frac{\sin\frac{nt}{2}}{\sin\frac{t}{2}}\right)^{2}$  称为 Fejér 核。在上式中令  $f \equiv 1$  得到

$$
\frac {1}{n \pi} \int_ {0} ^ {\pi} \left(\frac {\sin \frac {n t}{2}}{\sin \frac {t}{2}}\right) ^ {2} \mathrm{d} t = 1, \quad \forall n \geqslant 1. \tag {21.2.15}
$$

我们有如下结果.

定理21.2.6 设 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R}), x_0 \in \mathbb{R}$. 若 $f(x_0^+)$ 与 $f(x_0^-)$ 存在, 则

$$
\lim _ {n \to + \infty} \sigma_ {n} (f; x _ {0}) = \frac {f (x _ {0} ^ {+}) + f (x _ {0} ^ {-})}{2}. \tag {21.2.16}
$$

证明 对于 $r > 0$ ，记 $\omega (r) := \sup_{0 < t \leqslant r} |g(t)|$ ，其中

$$
g (t) := f (x _ {0} + t) + f (x _ {0} - t) - f (x _ {0} ^ {+}) - f (x _ {0} ^ {-}), \qquad t \in [ 0, \pi ].
$$

则 $\lim_{r\to 0^{+}}\omega (r) = 0$ .任取 $\delta \in (0,\pi)$ ，由(21.2.14)—(21.2.15)式可得

$$
\left| \sigma_ {n} (f; x _ {0}) - \frac {f (x _ {0} ^ {+}) + f (x _ {0} ^ {-})}{2} \right| = \frac {1}{2 n \pi} \left| \int_ {0} ^ {\pi} g (t) \left(\frac {\sin \frac {n t}{2}}{\sin \frac {t}{2}}\right) ^ {2} \mathrm{d} t \right|
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① du Bois-Reymond, Paul David Gustav, 1831 年 12 月 2 日—1889 年 4 月 7 日, 德国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Fejér, Lipót (Leopold), 1880 年 2 月 9 日—1959 年 10 月 15 日, 匈牙利数学家.</span></small>

---

21.2 Fourier 级数的收敛性

161

$$
\begin{array}{l} \leqslant \frac {1}{2 n \pi} \int_ {\delta} ^ {\pi} \frac {| g (t) |}{\sin^ {2} \frac {t}{2}} \mathrm{d} t + \frac {\omega (\delta)}{2 n \pi} \int_ {0} ^ {\delta} \left(\frac {\sin \frac {n t}{2}}{\sin \frac {t}{2}}\right) ^ {2} \mathrm{d} t \\ \leqslant \frac {1}{2 n \pi} \int_ {\delta} ^ {\pi} \frac {| g (t) |}{\sin^ {2} \frac {t}{2}} \mathrm{d} t + \omega (\delta). \\ \end{array}
$$

从而

$$
\varlimsup_ {n \to + \infty} \left| \sigma_ {n} (f; x _ {0}) - \frac {f (x _ {0} ^ {+}) + f (x _ {0} ^ {-})}{2} \right| \leqslant \omega (\delta). \tag {21.2.17}
$$

令 $\delta \to 0^{+}$ 即得定理结论.

Fejér 积分之所以在收敛性方面有良好的表现, 在于其具有局部性以及 Fejér 核绝对值的积分的有界性. 即对任何 $\delta \in (0, \pi)$ 和可积函数 $f$,

$$
\lim _ {n \to + \infty} \frac {1}{2 n \pi} \int_ {\delta} ^ {\pi} f (\theta) \left(\frac {\sin \frac {n \theta}{2}}{\sin \frac {\theta}{2}}\right) ^ {2} \mathrm{d} \theta = 0
$$

以及

$$
\sup _ {n \geqslant 1} \frac {1}{2 n \pi} \int_ {0} ^ {\pi} \left| \frac {\sin \frac {n \theta}{2}}{\sin \frac {\theta}{2}} \right| ^ {2} \mathrm{d} \theta <   + \infty
$$

成立.

而 Dirichlet 积分尽管也具有局部性, 其核的绝对值的积分却是无界的, 即

$$
\sup _ {n \geqslant 1} \frac {1}{2 \pi} \int_ {0} ^ {\pi} \left| \frac {\sin \left(n + \frac {1}{2}\right) \theta}{\sin \frac {\theta}{2}} \right| \mathrm{d} \theta = + \infty .
$$

这导致了 Dirichlet 积分在收敛性方面的表现不够好.

由定理21.2.6立即得到

推论21.2.7 设 $f \in C_{\#}(\mathbb{R})$，则

$$
\lim _ {n \to + \infty} \sigma_ {n} (f; x) = f (x), \quad \forall x \in \mathbb {R}. \tag {21.2.18}
$$

从定理21.2.6可见, 对于 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$, 以及 $f$ 的连续点 $x_0$, 若在 $x_0$ 处, $\{S_n(f; x_0)\}$ 收敛, 则其极限必为 $f(x_0)$.

那么, 当 $f \in C_{\#}(\mathbb{R})$ 时, 是否有可能在任何点 $x$ 处, $\{S_n(f; x)\}$ 均不收敛? 这一问题的回答是否定的. 事实上, 对于任何 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$, 可以证明, 使 $\{S_n(f; \cdot)\}$ 发散的点集是一个零测度集.

---

162

第二十一章 Fourier 级数

Luzin 猜想-Carleson 定理 Luzin $^{①}$ 于 1913 年猜测, 平方可积函数 $^{②}$ 的 Fourier 级数一定几乎处处收敛, 即不收敛点集是一个零测度集.

1922 年 6 月, 尚在上大学的 Kolmogorov $^{③}$ 给出了 Lebesgue 可积函数的 Fourier 级数几乎处处发散的例子, 1926 年他又给出了 Lebesgue 可积函数的 Fourier 级数处处发散的例子 (参见 [34], [35], [81]). 由于这些函数对于任何 p > 1, 都不是 p 次可积的, 因此, Kolmogorov 的反例并没有否定 Luzin 猜想.

直到 1966 年, 才由 Carleson $^{④}$  证明了 Luzin 猜想. 现称这一结果为 Carleson 定理. 其后, Hunt [29] 证明了对于 (Lebesgue 积分意义下的) p 次可积的函数 (p > 1), 其 Fourier 级数几乎处处收敛.

另一方面, 对于 $f \in L_{\#}^{p}(\mathbb{R})$ ($p \in [1, +\infty)$), 易证 $\sigma_n(f; \cdot)$ 在 $f \in L_{\#}^{p}(\mathbb{R})$ 中收敛于 $f(\cdot)$. 由此, 利用泛函分析的知识, 可以证明, 若 $\{S_n(f; \cdot)\}$ 在 $\mathbb{R}$ 上几乎处处收敛, 则一定几乎处处收敛到 $f(\cdot)$.

值得注意的是, Kolmogorov 的反例中的函数不属于 $\mathcal{R}_{\#}^{1}(\mathbb{R})$. 按我们的定义, $\mathcal{R}_{\#}^{1}(\mathbb{R})$ 中的元, 其瑕点集的两阶导集是空集, 由此可得, 对于 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$, 存在可列个两两不交的区间 $\{I_k\}$ 使得 $[0, 2\pi] \setminus \bigcup_{k=1}^{\infty} I_k$ 是至多可列集且对任何 $k \geqslant 1$, $f$ 在 $I_k$ 上是有界的, 从而 $f|_{I_k} \in \mathcal{R}^2(I_k)$. 结合局部性原理以及 Carleson 定理, $\{S_n(f; \cdot)\}$ 在 $I_k$ 上几乎处处收敛. 进而 $\{S_n(f; \cdot)\}$ 在 $\mathbb{R}$ 上几乎处处收敛.

另一方面, 根据 Lebesgue 判据, $f$ 在每个 $I_{k}$ 上几乎处处连续, 从而 $f$ 在 $\mathbb{R}$ 上几乎处处连续. 因此, 此时可进一步由定理 21.2.6 直接得到 $\{S_{n}(f; \cdot)\}$ 在 $\mathbb{R}$ 上几乎处处收敛到 $f(\cdot)$.

## 21.2.3 Fourier 级数的逐项可积性

容易由定理 21.2.5 得到 Fourier 级数的逐项可积性.

定理 21.2.8 设 $f \in  {\mathcal{R}}_{\# }^{1}\left( \mathbb{R}\right)$ ,其Fourier级数为(21.2.1). 则 $\mathop{\sum }\limits_{{n = 1}}^{\infty }\frac{{b}_{n}}{n}$ 收敛,且对任何 $x \in  \mathbb{R}$ ,有

$$
\int_ {0} ^ {x} f (t) \mathrm{d} t = \frac {a _ {0} x}{2} + \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {x} (a _ {n} \cos n t + b _ {n} \sin n t) \mathrm{d} t. \tag {21.2.19}
$$

即

$$
\int_ {0} ^ {x} f (t) \mathrm{d} t = \frac {a _ {0} x}{2} + \sum_ {n = 1} ^ {\infty} \frac {b _ {n}}{n} + \sum_ {n = 1} ^ {\infty} \left(- \frac {b _ {n} \cos n x}{n} + \frac {a _ {n} \sin n x}{n}\right) \mathrm{d} t. \tag {21.2.20}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Лузин, Николай Николаевич, 英文 Lusin (也拼作 Luzin), Nikolai Nikolaevich, 1883 年 12 月 9 日—1950 年 2 月 28 日, 苏联数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② 这里指的是 $L_{\#}^{2}(\mathbb{R})$ 中的函数, $L_{\#}^{2}(\mathbb{R})$ 表示以 $2\pi$ 为周期且在 $[0, 2\pi]$ 上在Lebesgue积分意义下平方可积的函数. $\mathcal{R}_{\#}^{2}(\mathbb{R})$ 是 $L_{\#}^{2}(\mathbb{R})$ 的真子集.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">③ Колмогоров, Андрей Николаевич, 英文 Kolmogorov, Andrey Nikolaevich, 1903 年 4 月 25 日—1987 年 10 月 20 日, 苏联数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">④ Carleson, Lennart, 1928 年 3 月 18 日—，瑞典数学家.</span></small>

---

21.2 Fourier级数的收敛性

163

证明 记 $g = f - \frac{a_0}{2}$

$$
F (x) := \int_ {0} ^ {x} g (t) \mathrm{d} t, \qquad x \in \mathbb {R}.
$$

则 F 为以  $2\pi$  为周期的连续函数. 进一步,

$$
F (x) = \int_ {0} ^ {x} g ^ {+} (t) \mathrm{d} t - \int_ {0} ^ {x} g ^ {-} (t) \mathrm{d} t, \qquad x \in \mathbb {R}.
$$

因此， $F$ 是一个单调递增函数和一个单调递减函数之和.于是，由定理21.2.5， $F$ 的Fourier级数收敛到 $F$ 设 $F$ 的Fourier级数为:

$$
F (x) \sim \frac {A _ {0}}{2} + \sum_ {n = 1} ^ {\infty} (A _ {n} \cos n x + B _ {n} \sin n x).
$$

利用累次积分交换次序或利用分部积分, 直接计算可得当  $n \geqslant 1$  时,

$$
A _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} \mathrm{d} x \int_ {0} ^ {x} f (t) \cos n x \mathrm{d} t = - \frac {b _ {n}}{n},
$$

$$
B _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} \mathrm{d} x \int_ {0} ^ {x} f (t) \sin n x \mathrm{d} t = \frac {a _ {n}}{n}.
$$

于是

$$
\int_ {0} ^ {x} g (t) \mathrm{d} t = \frac {A _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(- \frac {b _ {n}}{n} \cos n x + \frac {a _ {n}}{n} \sin n x\right), \quad \forall x \in \mathbb {R}. \tag {21.2.21}
$$

上式中令 $x = 0$ 可得 $\frac{A_0}{2} = \sum_{n=1}^{\infty} \frac{b_n}{n}$. 结合 (21.2.21) 式即得

$$
\int_ {0} ^ {x} g (t) \mathrm{d} t = \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {x} (a _ {n} \cos n t + b _ {n} \sin n t) \mathrm{d} t.
$$

即 (21.2.19) 式及 (21.2.20) 式成立.

由定理 21.2.8 易得存在处处收敛但不是 Fourier 级数的三角级数. 易见, 三角级数  $\sum_{n=2}^{\infty}\frac{\sin nx}{\ln n}$  在 R 上处处收敛, 但由于  $\sum_{n=2}^{\infty}\frac{1}{n\ln n}$  发散,  $\sum_{n=2}^{\infty}\frac{\sin nx}{\ln n}$  不是 Fourier 级数.

可以直接说明该级数的和函数 $S$ 在 $[0,2\pi]$ 上不属于 $\mathcal{R}_{\#}^{1}(\mathbb{R})$。否则，对于 $x \in [0,\pi)$，记 $F(x) := \int_{x}^{\pi} S(t) \, \mathrm{d}t + \sum_{n=2}^{\infty} \frac{(-1)^n}{n \ln n}$，则由内闭一致收敛性，对任何 $x \in (0,\pi)$，有 $F(x) = \sum_{n=2}^{\infty} \frac{\cos nx}{n \ln n}$。进一步，当 $m > 2$ 时，

$$
\int_ {0} ^ {x} F (t) \mathrm{d} t = \lim _ {\varepsilon \to 0 ^ {+}} \int_ {\varepsilon} ^ {x} F (t) \mathrm{d} t = \lim _ {\varepsilon \to 0 ^ {+}} \sum_ {n = 2} ^ {\infty} \frac {\sin n x - \sin n \varepsilon}{n ^ {2} \ln n} = \sum_ {n = 2} ^ {\infty} \frac {\sin n x}{n ^ {2} \ln n},
$$

---

164

第二十一章 Fourier 级数

$$
\int_ {0} ^ {x} \mathrm{d} t \int_ {0} ^ {t} F (s) \mathrm{d} s = \sum_ {n = 2} ^ {\infty} \frac {1 - \cos n x}{n ^ {3} \ln n} \geqslant \sum_ {n = 2} ^ {m} \frac {1 - \cos n x}{n ^ {3} \ln n}.
$$

由 L'Hôpital 法则可得

$$
F (0) = \lim _ {x \to 0 ^ {+}} \frac {2}{x ^ {2}} \int_ {0} ^ {x} \mathrm{d} t \int_ {0} ^ {t} F (s) \mathrm{d} s \geqslant \sum_ {n = 2} ^ {m} \frac {1}{n \ln n}.
$$

令 $m\to +\infty$ ，便有 $F(0)\geqslant +\infty$ ，得到矛盾.因此， $S\notin \mathcal{R}_\#^1 (\mathbb{R})$

那么, 能不能由 $S \notin \mathcal{R}_{\#}^{1}(\mathbb{R})$ 得出 $\sum_{n=2}^{\infty} \frac{\sin nx}{\ln n}$ 不是 Fourier 级数? 由于给出的是具体的三角级数, 这问题的提法不是很恰当. 如果对于一般的三角级数来提相应的问题, 我们可以这样提: 设三角级数 $\frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)$ 处处 (或除去一个两阶导集为空集的集合外) 收敛于 $S(x)$, 则 $S \notin \mathcal{R}_{\#}^{1}(\mathbb{R})$ 是否蕴涵该级数不是 (某个 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 的) Fourier 级数? 这一问题并不是一个简单的问题.

首先我们给出一个类似问题的相关结果. 若三角级数 $\frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)$ 几乎处处收敛于 $S(x)$ 而 $S \notin L_{\#}^{1}(\mathbb{R})$, 则该级数一定不是某个 $f \in L_{\#}^{1}(\mathbb{R})$ 的 Fourier 级数. 这是因为由 $f \in L_{\#}^{1}(\mathbb{R})$ 可得 $\lim_{n \to +\infty} \int_{0}^{2\pi} |\sigma_n(f; x) - f(x)| \, \mathrm{d}x = 0$. 结合 $S_n(f; \cdot)$ 几乎处处收敛于 $S(\cdot)$ 得到 $S = f$ 几乎处处成立.

回到原问题, 若 $\frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)$ 几乎处处收敛于 $S(x)$, 而对任何 $g \in \mathcal{R}_{\#}^{1}(\mathbb{R})$, $S$ 几乎处处等于 $g$ 都不成立, 则 $\frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)$ 不是某个 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 的 Fourier 级数.

## 21.2.4 Fourier 级数的逐项可微性

首先, 我们想到的问题是如下问题.

问题1 对于 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 以及相应的Fourier级数(21.2.1)，若 $f$ 在 $x_0$ 处可导，则 $f'(x_0)$ 是否可由(21.2.1)在 $x_0$ 处逐项求导得到？

这一问题的回答是否定的. 在完整回答这个问题之前, 我们先讨论下一个问题.

问题2设 $f\in \mathcal{R}_\#^1 (\mathbb{R})$ ，且 $f$ 处处可导，或除去一个二阶导集为空集的集合外可导，则 $f^{\prime}$ 的Fourier级数是否可由 $f$ 的Fourier级数(21.2.1)逐项求导得到？

即使 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 处处可导, 也不一定有 $f' \in \mathcal{R}_{\#}^{1}(\mathbb{R})$, 因此, $f'$ 不一定有 Fourier 级数. 要使得问题有意义, 我们需要进一步假设 $f' \in \mathcal{R}_{\#}^{1}(\mathbb{R})$. 此时, 由定理 21.2.8 即得如下定理.

定理21.2.9 设 $f \in C_{\#}(\mathbb{R})$, $f' \in \mathcal{R}_{\#}^{1}(\mathbb{R})$, 其中 $f'$ 可以在一个两阶导集为空的集合上不存在. 则 $f'$ 的Fourier级数就是 $f$ 的Fourier级数逐项求导得到的级数.

回到问题1, 取 $g \in C_{\#}(\mathbb{R})$ 使得 $g$ 的Fourier级数在点 $x_0$ 处不收敛. 不妨设 $\int_0^{2\pi} g(t) \, \mathrm{d}t = 0$. 令

---

21.2 Fourier级数的收敛性

165

$$
f (x) := \int_ {0} ^ {x} g (t) \mathrm{d} t, \qquad x \in \mathbb {R}.
$$

则 $f \in \mathcal{R}_{\#}(\mathbb{R})$ 处处可导且导函数为 $g$. 此时, $f$ 的 Fourier 级数逐项求导得到 $g$ 的 Fourier 级数. 这表明 $f'(x_0)$ 不可以通过对 $f$ 的 Fourier 级数在 $x_0$ 处逐项求导得到.

我们指出, 可以构造 $g \in C_{\#}(\mathbb{R})$ 使得 $g$ 的 Fourier 级数在事先任意指定的一个可列集上发散.

基于上述讨论, 我们自然地在如下的定理中提出了一个新的问题并给出结论.

定理21.2.10 设 $f \in C_{\#}(\mathbb{R})$ 在一个二阶导集为空集的集合之外可导，且 $f' \in \mathcal{R}_{\#}^{1}(\mathbb{R})$。若 $f$ 在 $x_0$ 处可导且 $\lim_{n \to +\infty} \sigma_n(f'; x_0) = A$，则 $f'(x_0) = A$。

证明 不妨设: $x_0 = 0, f(0) = f'(0) = 0$. 此时有常数 $M > 0$ 使得 $|f(x)| \leqslant M|x| (\forall x \in [-\pi, \pi])$. 而由 Fejér 积分的性质, 有

$$
\lim _ {n \to + \infty} \frac {1}{2 n \pi} \int_ {- \pi} ^ {\pi} \left| \frac {f (t)}{\sin \frac {t}{2}} \right| \frac {\sin^ {2} \frac {n t}{2}}{\sin^ {2} \frac {t}{2}} \mathrm{d} t = \lim _ {t \to 0} \left| \frac {f (t)}{\sin \frac {t}{2}} \right| = 0.
$$

进而由夹逼准则, 有

$$
\lim _ {n \to + \infty} \frac {1}{2 n \pi} \int_ {- \pi} ^ {\pi} f (t) \frac {\sin^ {2} \frac {n t}{2}}{\sin^ {3} \frac {t}{2}} \cos \frac {t}{2} \mathrm{d} t = 0. \tag {21.2.22}
$$

而由 $\lim_{n\to +\infty}\sigma_n(f';0) = A$ 并利用分部积分，可得

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {1}{4 \pi} \int_ {- \pi} ^ {\pi} f (t) \frac {\sin n t}{\sin^ {2} \frac {t}{2}} \mathrm{d} t \\ = \lim _ {n \to + \infty} \frac {1}{2 n \pi} \int_ {- \pi} ^ {\pi} f (t) \left(\frac {n \sin n t}{2 \sin^ {2} \frac {t}{2}} - \frac {\sin^ {2} \frac {n t}{2}}{\sin^ {3} \frac {t}{2}} \cos \frac {t}{2}\right) \mathrm{d} t \\ = \lim _ {n \to + \infty} \frac {1}{2 n \pi} \int_ {- \pi} ^ {\pi} f ^ {\prime} (t) \left(\frac {\sin \frac {n t}{2}}{\sin \frac {t}{2}}\right) ^ {2} \mathrm{d} t \\ = \lim _ {n \to + \infty} \sigma_ {n} (f ^ {\prime}; 0) = A. \tag {21.2.23} \\ \end{array}
$$

从而由Stolz公式得到

$$
\lim _ {n \to + \infty} \frac {1}{4 n \pi} \int_ {- \pi} ^ {\pi} f (t) \sum_ {k = 1} ^ {n} \frac {\sin k t}{\sin^ {2} \frac {t}{2}} \mathrm{d} t = A.
$$

即

$$
\lim _ {n \to + \infty} \frac {1}{4 n \pi} \int_ {- \pi} ^ {\pi} f (t) \frac {\sin \frac {(n + 1) t}{2} \sin \frac {n t}{2}}{\sin^ {3} \frac {t}{2}} \mathrm{d} t = A.
$$

---

166

第二十一章 Fourier级数

这样, 将  $\sin\frac{(n+1)t}{2}$  用和角公式展开, 并注意到 (21.2.23) 式或直接利用

$$
\left| \frac {f (t)}{8 n \pi} \frac {\sin n t}{\sin^ {2} \frac {t}{2}} \right| \leqslant \frac {M | t |}{8 n \pi} \frac {\sqrt {n | t |}}{\frac {4 t ^ {2}}{\pi^ {2}}} = \frac {M \pi}{3 2 \sqrt {n | t |}}, \quad \forall t \in [ - \pi , \pi ],
$$

再结合 (21.2.22) 式可得

$$
A = \lim _ {n \to + \infty} \frac {1}{4 n \pi} \int_ {- \pi} ^ {\pi} f (t) \left(\frac {\sin^ {2} \frac {n t}{2}}{\sin^ {3} \frac {t}{2}} \cos \frac {t}{2} + \frac {\sin n t}{2 \sin^ {2} \frac {t}{2}}\right) \mathrm{d} t = 0.
$$

这就证明了定理.

![](../../raw/pages_0801-0816/images/page_805_image_7.jpg)

有趣的是, 上述定理中关于 $f$ 可微性的条件可以大大减弱. 事实上, Fatou$^{①}$ 给出了如下的结果.

定理21.2.11 设 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$，其Fourier级数为 $\frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)$. 若 $f$ 在 $x_0$ 处可导，则 $\lim_{r \to 1^-} \sum_{n=1}^{\infty} n r^n (-a_n \sin nx + b_n \cos nx) = f'(x_0)$. 即 $f$ 的Fourier级数形式求导后的级数在 $x_0$ 处的Abel和为 $f'(x_0)$.

证明 不失一般性, 设 $x_0 = 0$. 由 Riemann 引理, $\{a_n\}$ 和 $\{b_n\}$ 均收敛于零. 因此, 固定 $r \in (0,1)$, 级数 $\frac{a_0}{2} + \sum_{n=1}^{\infty} r^n (a_n \cos nx + b_n \sin nx)$ 关于 $x \in \mathbb{R}$ 一致收敛. 记

$$
F (r, x) := \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} r ^ {n} (a _ {n} \cos n x + b _ {n} \sin n x), \qquad r \in (0, 1), x \in \mathbb {R}. \tag {21.2.24}
$$

则上式右端可以关于 x 逐项求导, 即

$$
\frac {\partial F}{\partial x} (r, x) := \sum_ {n = 1} ^ {\infty} n r ^ {n} (- a _ {n} \sin n x + b _ {n} \cos n x), \qquad r \in (0, 1), x \in \mathbb {R}. \tag {21.2.25}
$$

我们要证的就是  $\lim_{r\to1^{-}}\frac{\partial F}{\partial x}(r,0)=f'(0)$ .

利用

$$
\begin{array}{l} \frac {1}{2} + \sum_ {n = 1} ^ {\infty} r ^ {n} \cos n t = \frac {1}{2} + \mathrm{Re} \sum_ {n = 1} ^ {\infty} (r \mathrm{e} ^ {\mathrm{i} t}) ^ {n} \\ = \frac {1 - r ^ {2}}{2 (1 - 2 r \cos t + r ^ {2})}, \qquad r \in (- 1, 1), t \in \mathbb {R}, \\ \end{array}
$$

直接计算可得

$$
F (r, x) = \frac {1}{\pi} \int_ {- \pi} ^ {\pi} f (t) \left[ \frac {1}{2} + \sum_ {n = 1} ^ {\infty} r ^ {n} \cos n (t - x) \right] f (t) \mathrm{d} t
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Fatou, Pierre Joseph Louis, 1878 年 2 月 28 日—1929 年 8 月 10 日, 法国数学家.</span></small>

---

21.2 Fourier级数的收敛性

167

$$
= \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} f (t) \frac {1 - r ^ {2}}{1 - 2 r \cos (t - x) + r ^ {2}} \mathrm{d} t, \quad r \in (- 1, 1), x \in \mathbb {R}. \tag {21.2.26}
$$

易见, (21.2.26) 式右端的积分可以对 $x$ 在积分号下求导, 因此, 有

$$
\begin{array}{l} \frac {\partial F}{\partial x} (r, 0) = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} f (t) \frac {2 r (1 - r ^ {2}) \sin (t - x)}{(1 - 2 r \cos (t - x) + r ^ {2}) ^ {2}} \mathrm{d} t \Big | _ {x = 0} \\ = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} f (t) \frac {2 r (1 - r ^ {2}) \sin t}{(1 - 2 r \cos t + r ^ {2}) ^ {2}} \mathrm{d} t \\ = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} (f (t) - f (0)) \frac {2 r (1 - r ^ {2}) \sin t}{(1 - 2 r \cos t + r ^ {2}) ^ {2}} \mathrm{d} t, \quad r \in (- 1, 1). \tag {21.2.27} \\ \end{array}
$$

在 (21.2.27) 式中取 $f(x) = \sin x$，则对应的 $F(r, x) = r \sin x$，可得

$$
r = \frac {1}{2 \pi} \int_ {- \pi} ^ {\pi} \frac {2 r (1 - r ^ {2}) \sin^ {2} t}{(1 - 2 r \cos t + r ^ {2}) ^ {2}} \mathrm{d} t, \quad r \in (- 1, 1).
$$

因此，

$$
\frac {\partial F}{\partial x} (r, 0) - r f ^ {\prime} (0) = \frac {r}{2 \pi} \int_ {- \pi} ^ {\pi} \left(\frac {f (t) - f (0)}{\sin t} - f ^ {\prime} (0)\right) \frac {2 (1 - r ^ {2}) \sin^ {2} t}{(1 - 2 r \cos t + r ^ {2}) ^ {2}} \mathrm{d} t, \qquad r \in (- 1, 1).
$$

于是，任取 $\delta \in (0,\pi)$ ，由控制收敛定理，

$$
\begin{array}{l} \varlimsup_ {r \to 1 ^ {-}} \left| \frac {\partial F}{\partial x} (r, 0) - f ^ {\prime} (0) \right| = \varlimsup_ {r \to 1 ^ {-}} \left| \frac {\partial F}{\partial x} (r, 0) - r f ^ {\prime} (0) \right| \\ = \varlimsup_ {r \to 1 ^ {-}} \frac {r}{2 \pi} \left| \int_ {- \delta} ^ {\delta} \left(\frac {f (t) - f (0)}{\sin t} - f ^ {\prime} (0)\right) \frac {2 (1 - r ^ {2}) \sin^ {2} t}{(1 - 2 r \cos t + r ^ {2}) ^ {2}} \mathrm{d} t \right| \\ \leqslant \sup _ {0 <   | t | <   \delta} \left| \frac {f (t) - f (0)}{\sin t} - f ^ {\prime} (0) \right| \lim _ {r \rightarrow 1 ^ {-}} \frac {1}{2 \pi} \int_ {- \delta} ^ {\delta} \frac {2 \left(1 - r ^ {2}\right) \sin^ {2} t}{\left(1 - 2 r \cos t + r ^ {2}\right) ^ {2}} \mathrm{d} t \\ = \sup _ {0 <   | t | <   \delta} \left| \frac {f (t) - f (0)}{\sin t} - f ^ {\prime} (0) \right|. \\ \end{array}
$$

上式中令  $\delta \rightarrow 0^{+}$  即得结论.

注意到 Cesáro 可和蕴含 Abel 可和, 因此, 定理 21.2.11 蕴含定理 21.2.10.

## 21.2.5 Fourier级数的一致收敛性

若 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 的 Fourier 级数一致收敛, 则其和函数 $g$ 连续. 由一致收敛级数的逐项可积性,

$$
\int_ {0} ^ {x} g (t) \mathrm{d} t = \int_ {0} ^ {x} f (t) \mathrm{d} t, \quad \forall x \in \mathbb {R}. \tag {21.2.28}
$$

由此不难证明

$$
\int_ {0} ^ {2 \pi} | f (x) - g (x) | \mathrm{d} x = 0.
$$

---

168

第二十一章 Fourier 级数

这表明此时 $f$ 本质上等于一个连续函数.

对定理 21.2.6 的证明略加修改, 可得连续周期函数 Fourier 级数的 Fejér 积分一致收敛到该函数.

定理 21.2.12 设 $f \in  {C}_{\# }\left( \mathbb{R}\right)$ ,则 ${\sigma }_{n}\left( {f;\cdot  }\right)$ 一致收敛到 $f\left( \cdot  \right)$ .

证明 记 $\omega$ 为 $f$ 的连续模. 任取 $\delta \in (0, \pi)$, 我们有

$$
\begin{array}{l} \left| \sigma_ {n} (f; x) - f (x) \right| = \frac {1}{2 n \pi} \left| \int_ {- \pi} ^ {\pi} (f (x + t) - f (x)) \left(\frac {\sin \frac {n t}{2}}{\sin \frac {t}{2}}\right) ^ {2} \mathrm{d} t \right| \\ \leqslant \frac {\omega (\pi)}{n \pi} \int_ {\delta} ^ {\pi} \frac {1}{\sin^ {2} \frac {t}{2}} \mathrm{d} t + \frac {\omega (\delta)}{n \pi} \int_ {0} ^ {\delta} \left(\frac {\sin \frac {n t}{2}}{\sin \frac {t}{2}}\right) ^ {2} \mathrm{d} t \\ \leqslant \frac {\omega (\pi)}{n \pi} \int_ {\delta} ^ {\pi} \frac {1}{\sin^ {2} \frac {t}{2}} \mathrm{d} t + \omega (\delta). \\ \end{array}
$$

从而

$$
\varlimsup_ {n \to + \infty} \sup _ {x \in \mathbb {R}} | \sigma_ {n} (f; x) - f (x) | \leqslant \omega (\delta). \tag {21.2.29}
$$

在上式中令  $\delta \rightarrow 0^{+}$  即得定理结论.

定理 21.2.12 蕴涵了如下的 Weierstrass 第二逼近定理.

定理 21.2.13 R 上的连续周期函数可用三角多项式一致逼近.

对定理 21.2.3 和 21.2.5 的证明略加修改, 可以建立 Fourier 级数部分和一致收敛性的结果. 首先, 我们来给出关于参变量具有一致性的 Riemann-Lebesgue 引理.

引理21.2.14 设 $g$ 是 $[a, b] \times [c, d]$ 上的连续函数，则

$$
\lim _ {p \to \infty} \sup _ {x \in [ a, b ]} \left| \int_ {c} ^ {d} g (x, t) \sin p t \mathrm{d} t \right| = 0. \tag {21.2.30}
$$

证明 记 $\omega$ 为 $g$ 的连续模. 任取 $m \geqslant 1$, 我们有

$$
\sup _ {x \in [ a, b ]} \left| \int_ {c} ^ {d} g (x, t) \sin p t \mathrm{d} t \right| \leqslant (d - c) \omega \left(\frac {b - a}{m}\right) + \sum_ {k = 1} ^ {m} \left| \int_ {c} ^ {d} g \left(a + \frac {k (b - a)}{m}, t\right) \sin p t \mathrm{d} t \right|.
$$

这样, 由 Riemann-Lebesgue 引理

$$
\varlimsup_ {p \to \infty} \sup _ {x \in [ a, b ]} \left| \int_ {c} ^ {d} g (x, t) \sin p t \mathrm{d} t \right| \leqslant (d - c) \omega \left(\frac {b - a}{m}\right).
$$

最后, 令 $m \to +\infty$ 即得结论.

□

---

21.2 Fourier级数的收敛性

169

定理 21.2.15 设 f 以  $2\pi$  为周期且 Hölder 连续, 则 f 的 Fourier 级数一致收敛到 f.

证明 设 $\alpha \in (0,1], M > 0$ 使得

$$
| f (x) - f (y) | \leqslant M | x - y | ^ {\alpha}, \quad \forall   x, y \in \mathbb {R}.
$$

则任取  $\delta\in(0,\pi)$ ，由引理 21.2.14，

$$
\begin{array}{l} \varlimsup_ {n \to + \infty} \sup _ {x \in [ - \pi , \pi ]} \left| S _ {n} (f; x) - f (x) \right| \\ = \varlimsup_ {n \to + \infty} \sup _ {x \in [ - \pi , \pi ]} \frac {1}{\pi} \left| \int_ {0} ^ {\pi} (f (x + \theta) + f (x - \theta) - 2 f (x)) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta \right| \\ = \varlimsup_ {n \to + \infty} \sup _ {x \in [ - \pi , \pi ]} \frac {1}{\pi} \left| \int_ {0} ^ {\delta} (f (x + \theta) + f (x - \theta) - 2 f (x)) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta \right| \\ \leqslant \int_ {0} ^ {\delta} \sup _ {x \in [ - \pi , \pi ]} \frac {| f (x + \theta) + f (x - \theta) - 2 f (x) |}{2 \theta} \mathrm{d} \theta \leqslant M \int_ {0} ^ {\delta} \theta^ {\alpha - 1} \mathrm{d} \theta = \frac {M \delta^ {\alpha}}{\alpha}. \\ \end{array}
$$

令  $\delta \rightarrow 0^{+}$  即得结论.

定理 21.2.16 设  $f \in C_{\#}(\mathbb{R})$ ，且 f 为两个单调函数之和。则 f 的 Fourier 级数一致收敛到 f。

证明 此时 $f$ 必可以表示为一个连续单增函数 $f_{1}$ 与一个连续单减函数 $f_{2}$ 之和. 记

$$
\omega (r):= \sup_{\substack{|x - y|\leqslant r\\ x,y\in [-2\pi ,2\pi ]}}\max_{1\leqslant k\leqslant 2}|f_{k}(x) - f_{k}(y)|,\quad M = \sup_{X > 0}\left|\int_{0}^{X}\frac{\sin x}{x}  \mathrm{d}x\right|.
$$

任取 $\delta \in (0,\pi)$ ，由积分第二中值定理，对于 $x\in [-\pi ,\pi ]$

$$
\left| \int_ {0} ^ {\delta} (f _ {k} (x + \varepsilon \theta) - f _ {k} (x)) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{\theta} \mathrm{d} \theta \right| \leqslant 2 M \omega (\delta), \quad k = 1, 2; \varepsilon = \pm 1 \tag {21.2.31}
$$

成立 (参见 (21.2.13) 式).

于是, 由引理 21.2.14 以及 (21.2.31) 式, 有

$$
\varlimsup_ {n \to + \infty} \sup _ {x \in [ - \pi , \pi ]} \left| S _ {n} (f; x) - f (x) \right|
$$

---

170

第二十一章 Fourier 级数

$$
\begin{array}{l} = \varlimsup_ {n \rightarrow + \infty} \sup _ {x \in [ - \pi , \pi ]} \frac {1}{\pi} \left| \int_ {0} ^ {\pi} (f (x + \theta) + f (x - \theta) - 2 f (x)) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta \right| \\ = \varlimsup_ {n \rightarrow + \infty} \sup _ {x \in [ - \pi , \pi ]} \frac {1}{\pi} \left| \int_ {0} ^ {\pi} (f (x + \theta) + f (x - \theta) - 2 f (x)) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{\theta} \mathrm{d} \theta \right| \\ = \varlimsup_ {n \to + \infty} \sup _ {x \in [ - \pi , \pi ]} \frac {1}{\pi} \left| \int_ {0} ^ {\delta} (f (x + \theta) + f (x - \theta) - 2 f (x)) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{\theta} \mathrm{d} \theta \right| \\ \leqslant \varlimsup_ {n \rightarrow + \infty} \sup _ {x \in [ - \pi , \pi ]} \sum_ {k = 1} ^ {2} \sum_ {\varepsilon \in \{- 1, 1 \}} \frac {1}{\pi} \left| \int_ {0} ^ {\delta} \left(f _ {k} (x + \varepsilon \theta) - f _ {k} (x)\right) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{\theta} \mathrm{d} \theta \right| \\ \leqslant 8 M \omega (\delta). \\ \end{array}
$$

令 $\delta \to 0^{+}$ 即得结论.

![](../../raw/pages_0801-0816/images/page_809_image_4.jpg)

不难看到, 利用定理 21.2.15 和定理 21.2.16 都可以得到 Weierstrass 第二逼近定理.

犹如 du Bois Reymond 指出连续函数的 Fourier 级数不见得在每一点都收敛, Lebesgue 于 1906 年给出了一个连续函数的例子, 其 Fourier 级数处处收敛, 但不一致收敛. Fourier 级数的此类性质称为 Fourier 级数的奇异性. 有兴趣的读者可以参看 [41] 及该书所列文献.

## 21.2.6 Gibbs 现象

设 $f\in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 分段连续可微, 在 $x_0$ 处, $a = f(x_0^-)\leqslant f(x_0^+) = b.$ 若 $\lim_{\substack{n\to +\infty \\ x\to x_0^+}}S_n(f;x) = B>$ $b,\quad \varliminf_{\substack{n\to +\infty \\ x\to x_0^-}}S_n(f;x) = A <   a,$ 则称 $f$ 的Fourier级数在 $x_0$ 处存在Gibbs①现象.

Gibbs 现象由 Wilbraham $^{②}$ 发现 $^{③}$. 但当时未引起注意. 其后 Gibbs 重新发现了这一现象 $^{④}$.

在 $f$ 分段连续可微的假设之下, 若 $f(x_0^-) = f(x_0^+)$, 则类似定理21.2.15的证明, 可得存在 $\delta > 0$ 使得 $\{S_n(f; x)\}$ 关于 $x \in [x_0 - \delta, x_0 + \delta]$ 一致收敛. 因此, 此时不会发生 Gibbs现象. 当 $f(x_0^-) \neq f(x_0^+)$ 时, 则会发生 Gibbs现象. 具体地有如下结果.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Gibbs, Josiah Willard, 1839 年 2 月 11 日—1903 年 4 月 28 日, 美国物理学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Wilbraham, Henry, 1825 年 7 月 25 日—1883 年 2 月 13 日, 英国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">③ H. Wilbraham, On a certain periodic function. The Cambridge and Dublin Mathematical Journal, 3(1848), pp.198–201.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">④ J. W. Gibbs, Fourier's Series. Nature 59(1899), pp. 606.</span></small>

---

21.2 Fourier级数的收敛性

171

定理21.2.17 设 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 分段连续可微，在 $x_0$ 处，$a = f(x_0^-) < f(x_0^+) = b$. 记 $B = \varlimsup_{\substack{n \to +\infty \\ x \to x_0^+}} S_n(f; x)$，$A = \varliminf_{\substack{n \to +\infty \\ x \to x_0^-}} S_n(f; x)$. 则 $B > b > a > A$，且 $\frac{B - A}{b - a} = 2\ell$，其中

$$
\ell = \frac {1}{\pi} \int_ {0} ^ {\pi} \frac {\sin x}{x} \mathrm{d} x - \frac {1}{2} \approx 0. 0 8 9 4 8 9 8 7 2 2 3 6 0 8 3 6 \dots . \tag {21.2.32}
$$

证明 不妨设 $x_0 = 0, f(0) = b$. 记 $g := f - (b - a)\chi_{[0,\pi]}$. 则 $g(0^-) = g^+(0) = g(0) = a$. 由定理假设, $g$ 分段连续可微且存在 $\delta \in (0,1)$ 使得 $g$ 在 $[-2\delta, 2\delta]$ 上连续. 从而易得 $\{S_n(g; x)\}$ 关于 $x \in [-\delta, \delta]$ 一致收敛到 $g(x)$. 我们有

$$
\begin{array}{l} \varlimsup_ {\substack {n \to + \infty \\ x \to 0 ^ {+}}} S _ {n} (\chi_ {[ 0, \pi ]}; x) = \varlimsup_ {\substack {n \to + \infty \\ x \to 0 ^ {+}}} \frac {1}{\pi} \int_ {- \pi} ^ {\pi} \chi_ {[ 0, \pi ]} (\theta + x) \frac {\sin \frac {(2 n + 1) \theta}{2}}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta \\ = \varlimsup_ {\substack {n \rightarrow + \infty\\x \rightarrow 0 ^ {+}}} \frac {1}{\pi} \int_ {- x} ^ {\pi - x} \frac {\sin \frac {(2 n + 1) \theta}{2}}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta = \varliminf_ {\substack {n \rightarrow + \infty\\x \rightarrow 0 ^ {+}}} \frac {1}{\pi} \int_ {- x} ^ {\pi - x} \frac {\sin \frac {(2 n + 1) \theta}{2}}{\theta} \mathrm{d} \theta \\ = \varlimsup_ {\substack {n \rightarrow + \infty\\x \rightarrow 0 ^ {+}}} \frac {1}{\pi} \left(\int_ {0} ^ {\frac {(2 n + 1) x}{2}} \frac {\sin \theta}{\theta} \mathrm{d} \theta + \int_ {0} ^ {\frac {(2 n + 1) (\pi - x)}{2}} \frac {\sin \theta}{\theta} \mathrm{d} \theta\right) \\ = \varlimsup_ {\substack {n \rightarrow + \infty\\x \rightarrow 0 ^ {+}}} \frac {1}{\pi} \int_ {0} ^ {\frac {(2 n + 1) x}{2}} \frac {\sin \theta}{\theta} \mathrm{d} \theta + \lim_ {\substack {n \rightarrow + \infty\\x \rightarrow 0 ^ {+}}} \frac {1}{\pi} \int_ {0} ^ {\frac {(2 n + 1) (\pi - x)}{2}} \frac {\sin \theta}{\theta} \mathrm{d} \theta \\ = \frac {1}{\pi} \int_ {0} ^ {\pi} \frac {\sin \theta}{\theta} \mathrm{d} \theta + \frac {1}{\pi} \int_ {0} ^ {+ \infty} \frac {\sin \theta}{\theta} \mathrm{d} \theta = 1 + \ell . \\ \end{array}
$$

进而

$$
B = \varlimsup_ {\substack {n \rightarrow + \infty\\x \rightarrow 0 ^ {+}}} S _ {n} (f; x) = \lim_ {\substack {n \rightarrow + \infty\\x \rightarrow 0 ^ {+}}} S _ {n} (g; x) + (b - a) \varliminf_ {\substack {n \rightarrow + \infty\\x \rightarrow 0 ^ {+}}} S _ {n} (\chi_ {[ 0, \pi ]}; x)
$$

$$
= a + (b - a) (1 + \ell) = b + (b - a) \ell .
$$

同理，

$$
\begin{array}{l} \varliminf_ {\substack {n \to + \infty \\ x \to 0 ^ {-}}} S _ {n} (\chi_ {[ 0, \pi ]}; x) = \varliminf_ {\substack {n \to + \infty \\ x \to 0 ^ {-}}} \frac {1}{\pi} \int_ {- \frac {(2 n + 1) x}{2}} ^ {\frac {(2 n + 1) (\pi - x)}{2}} \frac {\sin \theta}{\theta} \mathrm{d} \theta \\ = \frac {1}{\pi} \int_ {\pi} ^ {+ \infty} \frac {\sin \theta}{\theta} \mathrm{d} \theta = \frac {1}{2} - \frac {1}{\pi} \int_ {0} ^ {\pi} \frac {\sin \theta}{\theta} \mathrm{d} \theta = - \ell , \\ A = \varliminf_ {\substack {n \to + \infty \\ x \to 0 ^ {+}}} S _ {n} (f; x) = a - (b - a) \ell . \\ \end{array}
$$

因此, $B > b > a > A$, 且 $\frac{B - A}{b - a} = 2\ell$.

□

---

172

第二十一章 Fourier 级数

## 21.2.7 例题

例 21.2.1 利用例 21.1.1 及定理 21.2.5 或定理 21.2.3, 我们有

$$
\sum_ {n = 1} ^ {\infty} \frac {\sin n x}{n} = \frac {\pi - x}{2}, \quad x \in (0, 2 \pi). \tag {21.2.33}
$$

例 21.2.2 利用例 21.1.2 及定理 21.2.5 或定理 21.2.3, 我们有

$$
\sum_ {n = 1} ^ {\infty} \frac {\cos n x}{n} = - \ln \left(2 \sin \frac {x}{2}\right), \quad x \in (0, 2 \pi). \tag {21.2.34}
$$

例21.2.3 利用Fourier级数计算 $\sum_{n = 1}^{\infty}\frac{1}{n^2},\sum_{n = 1}^{\infty}\frac{1}{n^4}.$

解 对于 $x \in [0, 2\pi]$, 对 (21.2.33) 式利用逐项可积性在 $[0, x]$ 上积分得到

$$
\frac {2 \pi x - x ^ {2}}{4} = \sum_ {n = 1} ^ {\infty} \frac {1 - \cos n x}{n ^ {2}}, \qquad x \in [ 0, 2 \pi ].
$$

上式在 $[0, 2\pi]$ 上积分得到 $\sum_{n=1}^{\infty} \frac{1}{n^{2}} = \frac{\pi^{2}}{6}$. 于是又有

$$
\sum_ {n = 1} ^ {\infty} \frac {\cos n x}{n ^ {2}} = \frac {\pi^ {2}}{6} - \frac {x (2 \pi - x)}{4}, \quad x \in [ 0, 2 \pi ]. \tag {21.2.35}
$$

上式积分两次得到

$$
\sum_ {n = 1} ^ {\infty} \frac {1 - \cos n x}{n ^ {4}} = \frac {x ^ {2} (2 \pi - x) ^ {2}}{4 8}, \quad x \in [ 0, 2 \pi ]. \tag {21.2.36}
$$

对上式在 $[0,2\pi]$ 上积分得到① $\sum_{n = 1}^{\infty}\frac{1}{n^4} = \frac{\pi^4}{90}$.

例21.2.4 设 $\alpha \neq 0$ ，利用Fourier级数计算 $\sum_{n = 1}^{\infty}\frac{1}{n^2 + \alpha^2}$

解 由例21.1.3以及Fourier级数的收敛性, 我们有

$$
\frac {\mathrm{e} ^ {2 \pi \alpha} - 1}{2 \pi \alpha} + \sum_ {n = 1} ^ {\infty} \frac {\alpha (\mathrm{e} ^ {2 \pi \alpha} - 1)}{\pi (n ^ {2} + \alpha^ {2})} = \frac {1 + \mathrm{e} ^ {2 \alpha \pi}}{2}.
$$

即

$$
\sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2} + \alpha^ {2}} = - \frac {1}{2 \alpha^ {2}} + \frac {\pi}{2 \alpha \tanh (\alpha \pi)}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 自然, 也可以在相应公式中代入具体的 x 得到上述结果. 今后, 也可以分别对 (21.2.33) 式和 (21.2.35) 式运用 Parseval 等式得到结果.</span></small>

---

21.2 Fourier 级数的收敛性

173

例21.2.5 设 $\alpha$ 非整, 利用Fourier级数计算 $\sum_{n=1}^{\infty} \frac{1}{n^2 - \alpha^2}$.

解 由例 21.1.3 以及 Fourier 级数的收敛性, 我们有

$$
\frac {\sin (2 \pi \alpha)}{2 \pi \alpha} + \sum_ {n = 1} ^ {\infty} \frac {- 2 \alpha \cos (\pi \alpha) \sin (\pi \alpha)}{\pi (n ^ {2} - \alpha^ {2})} = \frac {1 + \cos (2 \alpha \pi)}{2} = \cos^ {2} (\alpha \pi).
$$

于是

$$
\sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2} - \alpha^ {2}} = \frac {1}{2 \alpha^ {2}} - \frac {\pi \cot (\alpha \pi)}{2 \alpha}.
$$

在例 20.4.5 中, 我们曾经得到上式对  $\alpha \in (0,1)$  成立.

![](../../raw/pages_0801-0816/images/page_812_image_8.jpg)

例 21.2.6 设  $f \in C(\mathbb{R})$  以 1 为周期, 求解热传导方程

$$
\left\{ \begin{array}{l l} u _ {t} (t, x) = u _ {x x} (t, x), & t \geqslant 0,   x \in \mathbb {R}, \\ u (0, x) = f (x), & x \in \mathbb {R} \end{array} \right. \tag {21.2.37}
$$

关于 x 的周期解 $^{①}$ .

解 我们引入分离变量的思想, 尝试寻找形为 $u(t,x) = \sum_{n=0}^{\infty} \psi_n(t)\varphi_n(x)$ 这样的解, 其中, 对于每一个 $n \geqslant 0$, $\psi_n(t)\varphi_n(x)$ 均满足 (21.2.37) 式中的微分方程, 且 $\varphi_n$ 以 1 为周期. 对于每一个非平凡的 $\psi(t)\varphi(x) = \psi_n(t)\varphi_n(x)$, 我们有

$$
\psi^ {\prime} (t) \varphi (x) = \psi (t) \varphi^ {\prime \prime} (x), \qquad t \geqslant 0,   x \in [ 0, 1 ].
$$

于是有常数 $C$ 使得 $\psi'(t) = C\psi(t)$ 以及 $\varphi''(x) = C\varphi(x)$.

易见 $\varphi''(x) = C\varphi(x)$ 有周期为1的非平凡解的充要条件是 $C = -4n^{2}\pi^{2}$，相应地，有 $\varphi(x) = C_1\cos 2n\pi x + C_2\sin 2n\pi x$ 以及 $\psi(t) = C_3\mathrm{e}^{-4n^2\pi^2 t}$.

因此, 我们有方程 (21.2.37) 的形式解:

$$
u (t, x) = a _ {0} + \sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {- 4 n ^ {2} \pi^ {2} t} (a _ {n} \cos 2 n \pi x + b _ {n} \sin 2 n \pi x), \tag {21.2.38}
$$

其中, 根据初值条件,

$$
f (x) = u (0, x) = a _ {0} + \sum_ {n = 1} ^ {\infty} (a _ {n} \cos 2 n \pi x + b _ {n} \sin 2 n \pi x). \tag {21.2.39}
$$

接下来, 我们需要讨论的是在何种条件下, (21.2.38)—(21.2.39) 式给出了方程 (21.2.37) 的唯一解. 对于这一问题, 我们不在本教材中展开讨论.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Fourier 级数理论正是在研究此类问题时发展起来的.</span></small>

---

174

第二十一章 Fourier 级数

## 习题 21.2

1. 设 $f$ 在 $[0, +\infty)$ 上单调且 $\lim_{x \to +\infty} f(x) = 0$. 证明: $\lim_{n \to +\infty} \int_{0}^{+\infty} f(x) \sin nx \mathrm{d}x = 0$.

2. 设 $n \geqslant 1$, 证明: $\int_{0}^{\frac{\pi}{2}} x \left( \frac{\sin nx}{\sin x} \right)^{4} \mathrm{~d}x < \frac{n^{2}\pi^{2}}{4}$.

3. 设 $f \in C(\mathbb{R})$ 以 1 为周期, $f(x) + f\left(x + \frac{1}{2}\right) = f(2x)$. 若存在 $g \in L^{1}[0,1]$ 使得 $f(x) = f(0) + \int_{0}^{x} g(t) \, \mathrm{d}t$, 证明: $f \equiv 0$.

4. 试推广引理 21.2.14.

5. 推广 Riemann-Lebesgue 引理: 设 $p, q \in [1, +\infty]$ 为对偶数, 即 $\frac{1}{p} + \frac{1}{q} = 1$, $f \in \mathcal{R}^p(\mathbb{R})$. 又设 $T > 0$, $g$ 以 $T$ 为周期, 且 $g \in \mathcal{R}^q[0, T]$. 证明:

$$
\lim _ {p \to \infty} \int_ {\mathbb {R}} f (x) g (p x) \mathrm{d} x = \frac {1}{T} \int_ {0} ^ {T} g (x) \mathrm{d} x \int_ {\mathbb {R}} f (x) \mathrm{d} x.
$$

6. 试考察函数 $f(x) := \sum_{n=2}^{\infty} \frac{\cos nx}{\ln n}$ 在 $[- \pi, \pi]$ 上的可积性.

7. 设 $\alpha \in (0,1)$, 考察函数 $f(x) := \sum_{n=1}^{\infty} \frac{\sin nx}{n^{\alpha}}$ 和 $g(x) := \sum_{n=1}^{\infty} \frac{\cos nx}{n^{\alpha}}$ 在 $x \to 0^{+}$ 时的阶.

8. 设 $f \in C_{\#}[0, 2\pi]$ 的 Fourier 级数为 $\sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)$. 问: $\sum_{n=1}^{\infty} (b_n \cos nx - a_n \sin nx)$ 是不是某个 $g \in C_{\#}[0, 2\pi]$ 的 Fourier 级数?

9. 试讨论如何定义方程 (21.2.37) 的解, 以及在何种条件下, 方程 (21.2.37) 有唯一解, 而 (21.2.38)—(21.2.39) 式给出了方程的解.

10. 设 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 在 $[0, 2\pi]$ 上可以表示为两个单调函数之和, $\{a_{n}\}, \{b_{n}\}$ 为 $f$ 的 Fourier 系数. 证明: $\{na_{n}\}$ 与 $\{nb_{n}\}$ 有界.

11. 设 $f \in C_{\#}(\mathbb{R})$ 在 $[0, 2\pi]$ 上可以表示为两个单调函数之和, $\{a_n\}, \{b_n\}$ 为 $f$ 的 Fourier 系数. 证明:

$$
\lim _ {n \to + \infty} n a _ {n} = \lim _ {n \to + \infty} n b _ {n} = 0.
$$

## 21.3 平方可积周期函数的 Fourier 级数

对于 $f, g \in \mathcal{R}^2[0, 2\pi]$, 定义

$$
\langle f, g \rangle := \int_ {0} ^ {2 \pi} f (x) g (x) \mathrm{d} x, \tag {21.3.1}
$$

---

21.3 平方可积周期函数的 Fourier 级数

175

称为 $f, g$ (在 $\mathcal{R}^2[0, 2\pi]$ 中) 的内积. 此时, $\mathcal{R}^2[0, 2\pi]$ 构成一个内积空间. 我们把 $\| f \|_2 \equiv \| f \|_{\mathcal{R}^2[0, 2\pi]} := \sqrt{\langle f, f \rangle}$ 称为 $f$ (在 $\mathcal{R}^2[0, 2\pi]$ 中) 的范数.

现考虑 $\mathcal{R}^2 [0,2\pi ]$ 中的函数列 $\{\psi_n\}_{n = 0}^{\infty}$ 若

$$
\langle \psi_ {k}, \psi_ {j} \rangle = \delta_ {k j} \equiv \left\{ \begin{array}{l l} 1, & k = j, \\ 0, & k \neq j, \end{array} \quad k, j \geqslant 0, \right. \tag {21.3.2}
$$

则称  $\{\psi_{n}\}_{n=0}^{\infty}$  为  $R^{2}[0,2\pi]$  中的标准正交（函数）系.

对于 $f\in \mathcal{R}^2 [0,2\pi ]$ ，令

$$
c _ {n} = \left\langle f, \psi_ {n} \right\rangle , \quad n = 0, 1, 2, \dots , \tag {21.3.3}
$$

则称  $\sum_{n=0}^{\infty}c_{n}\psi_{n}$  为 f 对应于  $\{\psi_{n}\}_{n=0}^{\infty}$  的 Fourier 级数,  $\{c_{n}\}$  称为 f 的 Fourier 系数. 对于  $n \geqslant 0$ , 记  $T_{n}(f;x)=\sum_{k=0}^{n}c_{k}\psi_{k}(x)$ .

直接计算, 得到

$$
\int_ {0} ^ {2 \pi} | f (x) | ^ {2} \mathrm{d} x = \int_ {0} ^ {2 \pi} | f (x) - \sum_ {k = 0} ^ {n} c _ {k} \psi_ {k} (x) | ^ {2} \mathrm{d} x + \sum_ {k = 0} ^ {n} | c _ {k} | ^ {2}. \tag {21.3.4}
$$

从而

$$
\sum_ {k = 0} ^ {n} | c _ {k} | ^ {2} \leqslant \int_ {0} ^ {2 \pi} | f (x) | ^ {2} \mathrm{d} x. \tag {21.3.5}
$$

即

$$
\int_ {0} ^ {2 \pi} \left| T _ {n} (f; x) \right| ^ {2} \mathrm{d} x \leqslant \int_ {0} ^ {2 \pi} | f (x) | ^ {2} \mathrm{d} x. \tag {21.3.6}
$$

在 (21.3.5) 式中令 $n \to +\infty$ 即得 Bessel$^{①}$ 不等式:

$$
\sum_ {n = 0} ^ {\infty} | c _ {n} | ^ {2} \leqslant \int_ {0} ^ {2 \pi} | f (x) | ^ {2} \mathrm{d} x. \tag {21.3.7}
$$

另一方面，对于任何数列 $\{\beta_n\}_{n=0}^{\infty}$，在 (21.3.4) 式中用 $f - \sum_{k=0}^{n} \beta_k \psi_k(x)$ 代替 $f$，我们有

$$
\int_ {0} ^ {2 \pi} \left| f (x) - \sum_ {k = 0} ^ {n} \beta_ {k} \psi_ {k} (x) \right| ^ {2} \mathrm{d} x
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Bessel, Friedrich Wilhelm, 1784 年 7 月 22 日—1846 年 3 月 17 日, 德国天文学家、数学家、天体测量学家.</span></small>

---

176

第二十一章 Fourier 级数

$$
\begin{array}{l} = \int_ {0} ^ {2 \pi} | f (x) - \sum_ {k = 0} ^ {n} c _ {k} \psi_ {k} (x) | ^ {2} \mathrm{d} x + \sum_ {k = 0} ^ {n} | c _ {k} - \beta_ {k} | ^ {2} \\ \geqslant \int_ {0} ^ {2 \pi} | f (x) - \sum_ {k = 0} ^ {n} c _ {k} \psi_ {k} (x) | ^ {2} \mathrm{d} x. \tag {21.3.8} \\ \end{array}
$$

这就是说, 若固定 f 以及  $\{\psi_{k}\}_{k=0}^{\infty}$ ，则  $\left\|f-\sum_{k=0}^{n}\beta_{k}\psi_{k}\right\|_{2}$  当且仅当  $\beta_{k}=c_{k}(k=0,1,2,\cdots,n)$  时取得最小值. 我们称这一性质为 Fourier 级数具有的最佳均方逼近性质.

现取  $\psi_{0}(x),\psi_{1}(x),\psi_{2}(x),\cdots$  为

$$
\frac {1}{\sqrt {2 \pi}}, \frac {\sin x}{\sqrt {\pi}}, \frac {\cos x}{\sqrt {\pi}}, \frac {\sin 2 x}{\sqrt {\pi}}, \frac {\cos 2 x}{\sqrt {\pi}}, \dots ,
$$

则 (21.3.6) 式和 (21.3.7) 式成为

$$
\int_ {0} ^ {2 \pi} \left| S _ {n} (f; x) \right| ^ {2} \mathrm{d} x \leqslant \int_ {0} ^ {2 \pi} | f (x) | ^ {2} \mathrm{d} x, \tag {21.3.9}
$$

$$
\frac {a _ {0} ^ {2}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) \leqslant \frac {1}{\pi} \int_ {0} ^ {2 \pi} | f (x) | ^ {2} \mathrm{d} x. \tag {21.3.10}
$$

进一步, 可得如下定理.

定理 21.3.1 设  $f, g \in R^{2}[0, 2\pi]$ ，其 Fourier 级数依次为

$$
f (x) \sim \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} \cos n x + b _ {n} \sin n x\right), \tag {21.3.11}
$$

$$
g (x) \sim \frac {\alpha_ {0}}{2} + \sum_ {n = 1} ^ {\infty} (\alpha_ {n} \cos n x + \beta_ {n} \sin n x). \tag {21.3.12}
$$

则

$$
\lim _ {n \to + \infty} \int_ {0} ^ {2 \pi} | S _ {n} (f; x) - f (x) | ^ {2} \mathrm{d} x = 0, \tag {21.3.13}
$$

$$
\frac {1}{\pi} \int_ {0} ^ {2 \pi} f (x) g (x) \mathrm{d} x = \frac {a _ {0} \alpha_ {0}}{2} + \sum_ {n = 1} ^ {\infty} (a _ {n} \alpha_ {n} + b _ {n} \beta_ {n}). \tag {21.3.14}
$$

特别地, 以下的 Parseval $^{①}$ 等式

$$
\frac {a _ {0} ^ {2}}{2} + \sum_ {n = 1} ^ {\infty} \left(a _ {n} ^ {2} + b _ {n} ^ {2}\right) = \frac {1}{\pi} \int_ {0} ^ {2 \pi} | f (x) | ^ {2} \mathrm{d} x \tag {21.3.15}
$$

成立.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Parseval des Chénes, Marc-Antoine, 1755 年 4 月 27 日—1836 年 8 月 16 日, 法国数学家.</span></small>

---

21.3 平方可积周期函数的 Fourier 级数

177

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

---

178

第二十一章 Fourier 级数

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

---

21.3 平方可积周期函数的 Fourier 级数

179

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

---

180

第二十一章 Fourier级数

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

---

21.3 平方可积周期函数的 Fourier 级数

181

完备性与完全性有如下关系.

定理 21.3.5 设 X 是内积空间,  $M \subseteq X$ . 若 M 是完备系, 则 M 是完全系.

证明 设 M 是完备系. 设  $f \in X$  使得对任何  $g \in M$ , 有  $\langle f, g \rangle = 0$ . 任取  $\varepsilon > 0$ , 根据 M 是完备系, 有  $g_{1}, g_{2}, \cdots, g_{n} \in M$  以及  $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n} \in R$  使得  $\left\| f - \sum_{k=1}^{n} \alpha_{k} g_{k} \right\|_{X} < \varepsilon$ . 不妨设  $g_{1}, g_{2}, \cdots, g_{n}$  标准正交. 此时对  $1 \leqslant k \leqslant n, c_{k} = \langle f, g_{k} \rangle = 0$ . 于是由最佳均方逼近性质 (参见 (21.3.8) 式), 有

$$
\| f \| _ {X} ^ {2} = \left\| f - \sum_ {k = 0} ^ {n} c _ {k} g _ {k} \right\| _ {X} ^ {2} \leqslant \left\| f - \sum_ {k = 0} ^ {n} \alpha_ {k} g _ {k} \right\| _ {X} ^ {2} <   \varepsilon^ {2}.
$$

由  $\varepsilon > 0$  的任意性, 得到  $\|f\|_{X} = 0$ . 即 f = 0. 因此, M 是完全系.

![](../../raw/pages_0817-0832/images/page_820_image_7.jpg)

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

---

182

第二十一章 Fourier 级数

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

---

21.3 平方可积周期函数的 Fourier 级数

183

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

---

184

第二十一章 Fourier 级数

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

---

21.4 Fourier变换

185

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

Fourier 变换有着重要的应用, 但完整地介绍 Fourier 变换的性质难以避开 $L^2$ 空间, 这就有待于引入 Lebesgue 积分理论. 本节中, 我们把讨论的范围限制在速降函数空间内, 则可以方便地介绍 Fourier 变换的主要性质. 今后很容易将这些在速降函数空间建

---

186

第二十一章 Fourier 级数

立的结果推广到一般情形. 自然, 某些特定的性质目前也可以在比速降函数类更广的范围内加以建立.

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

---

21.4 Fourier 变换

187

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

---

188

第二十一章 Fourier级数

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

---

21.4 Fourier 变换

189

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

---

190

第二十一章 Fourier级数

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

---

21.4 Fourier变换

191

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

---

192

第二十一章 Fourier级数

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

---

21.5 Fourier级数的唯一性

193

3. 对于

$f \in X_a := \left\{ f \mid f \text{ 为非负偶函数, } \operatorname{supp} f = \left[ -\frac{a}{2}, \frac{a}{2} \right], f \text{ 在 } (-a/2, a/2) \text{ 内 Lipschitz 连续} \right\}$, 证明: $\int_{\mathbb{R}} \widehat{f}(x) \, \mathrm{d}x = f(0)$.

4. 设 $f(x) := \pi \mathrm{e}^{-2\pi |x|} (x \in \mathbb{R})$. 试求 $f$ 的 Fourier 变换.

5. 设 $f \in C^{1}(\mathbb{R})$，且 $\int_{\mathbb{R}} \left( f^{2}(x) + \left( f'(x) \right)^{2} \right) \, \mathrm{d}x = 1$。证明:$\lim_{x \to \infty} f(x) = 0$，且 $\|f\|_{\infty} < \frac{\sqrt{2}}{2}$。

6. 设 $\alpha \in \mathbb{R}$, 计算含参变量积分 $\int_{0}^{+\infty} \frac{\cos(\alpha\pi x)}{1 + x^2} \, \mathrm{d}x, \int_{0}^{+\infty} \frac{x \sin(\alpha\pi x)}{1 + x^2} \, \mathrm{d}x.$

## 21.5 Fourier 级数的唯一性

设  $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ ,

$$
f (x) = \frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} (a _ {n} \cos n x + b _ {n} \sin n x) \tag {21.5.1}
$$

$$
= \frac {\alpha_ {0}}{2} + \sum_ {n = 1} ^ {\infty} (\alpha_ {n} \cos n x + \beta_ {n} \sin n x), \quad x \in \mathbb {R}.
$$

自然地, 产生一个问题, 即是否有

$$
a _ {0} = \alpha_ {0}, \quad a _ {n} = \alpha_ {n}, \quad b _ {n} = \beta_ {n}, \quad \forall n \geqslant 1? \tag {21.5.2}
$$

这一问题体现了周期函数展开成三角级数的唯一性问题. 若上述问题的答案是肯定的, 那就产生第二个问题, 即该三角级数是否就是 f 的 Fourier 级数, 即

$$
a _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} f (x) \cos n x \mathrm{d} x, \quad n = 0, 1, 2, \dots , \tag {21.5.3}
$$

$$
b _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} f (x) \sin n x \mathrm{d} x, \quad n = 1, 2, \dots \tag {21.5.4}
$$

是否成立？我们称之为 Fourier 级数的唯一性问题.

如果 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 的Fourier级数处处收敛到 $f$, 那么第一个问题的回答就包含了第二个问题的回答.

然而, 对于一般的 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$, 其 Fourier 级数并不一定处处收敛, 而且即使收敛, 也不一定收敛到 $f$. 因此, (在得到第一个问题的肯定回答后) 第二个问题远非平凡.

注意到当 $f$ 缺乏光滑性的时候, 很难做到 (21.5.1) 式处处成立, 因此, 要使得问题更有意义, 对于这两个问题, 我们需要在更弱的条件下来讨论. 另一方面, 为了更好地看清楚问题, 我们来引

---

194

第二十一章 Fourier 级数

入容易与前两个问题混淆的第三个问题: 若 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 的 Fourier 级数 (除个别点外) 处处收敛到 $g$, 则 $g$ 是否本质上就是 $f$? 确切地讲, 是否就有 $\int_{0}^{2\pi}|g(x) - f(x)| \mathrm{d}x = 0$?

从上面的讨论可见, Fourier 级数的唯一性问题远比函数展开成幂级数的唯一性来得复杂. 本节我们简要介绍相关结果, 有兴趣的读者可以进一步参看文献 [23] 第二十章第三节以及文献 [36].

对于第一个问题, 可以由如下 Cantor-Lebesgue 定理 $^{①}$ 得到解决.

定理21.5.1 设 $E \subset [0, 2\pi]$ 是一个闭的可列集，

$$
\frac {a _ {0}}{2} + \sum_ {n = 1} ^ {\infty} (a _ {n} \cos n x + b _ {n} \sin n x) = 0, \quad \forall   x \in [ 0, 2 \pi ] \setminus E, \tag {21.5.5}
$$

则

$$
a _ {n} = b _ {n} = 0, \qquad \forall n = 1, 2, \dots . \tag {21.5.6}
$$

易见, 上述定理是以下的 du Bois Reymond-Vallée Poussin $^{②}$  定理的特例.

定理 21.5.2 设  $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ , E 为可列闭集, f 在  $R \setminus E$  中局部有界. 如果等式 (21.5.1) 对任何  $x \notin E$  成立, 则 (21.5.1) 式右端必为 f 的 Fourier 级数.

定理的证明颇为复杂, 我们先介绍大致的证明思路. 证明的关键困难自然在于不能直接对 (21.5.1) 式逐项积分.

顺便指出, 若集合的二阶导集为空, 则其闭包一定是至多可列的闭集. 但可列闭集的二阶导集不一定为空集.

若定理结论成立, 则由 Riemann-Lebesgue 引理, $\{a_{n}\}$ 和 $\{b_{n}\}$ 均趋于零. 因此, 我们首先应该证明这一点.

接下来, 考虑

$$
G (x) \equiv \sum_ {n = 1} ^ {\infty} \left(\frac {a _ {n}}{n} \sin n x - \frac {b _ {n}}{n} \cos n x\right), \qquad x \in \mathbb {R}
$$

和

$$
F (x) \equiv - \sum_ {n = 1} ^ {\infty} \left(\frac {a _ {n}}{n ^ {2}} \cos n x + \frac {b _ {n}}{n ^ {2}} \sin n x\right), \qquad x \in \mathbb {R}. \tag {21.5.7}
$$

若定理结论成立, 则 $G$ 的 Fourier 系数是 $\left\{-\frac{b_n}{n}\right\}$ 和 $\left\{\frac{a_n}{n}\right\}, F$ 的 Fourier 系数是 $\left\{-\frac{a_n}{n^2}\right\}$ 和 $\left\{-\frac{b_n}{n^2}\right\}$. 且有常数 $C_1, C_2$ 使得

$$
G (x) = \int_ {0} ^ {x} f (t) \mathrm{d} t + C _ {1} - \frac {a _ {0}}{2} x, \qquad x \in \mathbb {R} \tag {21.5.8}
$$

和

$$
F (x) = \int_ {0} ^ {x} \mathrm{d} t \int_ {0} ^ {t} f (s) \mathrm{d} s + C _ {2} + C _ {1} x - \frac {a _ {0}}{4} x ^ {2}, \qquad x \in \mathbb {R}. \tag {21.5.9}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 值得注意的是, Cantor 正是在研究上述问题时, 发现处理无穷集的重要性, 进而建立了集合论.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② de la Vallée Poussin, Charles Jean, 1866 年 8 月 14 日—1962 年 3 月 2 日, 比利时数学家.</span></small>

---

21.5 Fourier级数的唯一性

195

另一方面, 若能够证明 (21.5.8) 式成立且 $G$ 的 Fourier 系数是 $\left\{-\frac{b_n}{n}\right\}$ 和 $\left\{\frac{a_n}{n}\right\}$, 则自然可得 $\{a_n\}$ 和 $\{b_n\}$ 是 $f$ 的 Fourier 系数.

或者, 如果能够证明 (21.5.9) 式成立且 $F$ 的 Fourier 系数是 $\left\{-\frac{a_n}{n^2}\right\}$ 和 $\left\{-\frac{b_n}{n^2}\right\}$, 则同样可得 $\{a_n\}$ 和 $\{b_n\}$ 是 $f$ 的 Fourier 系数.

在 $\{a_{n}\}$ 和 $\{b_{n}\}$ 均趋于零的前提下, 由级数 $\sum_{n=1}^{\infty} \left( \frac{a_{n}}{n^{2}} \cos nx + \frac{b_{n}}{n^{2}} \sin nx \right)$ 的一致收敛性, 可得 $F$ 的 Fourier 系数是 $\left\{-\frac{a_{n}}{n^{2}}\right\}$ 和 $\left\{-\frac{b_{n}}{n^{2}}\right\}$. 但要直接证明 $G$ 的 Fourier 系数是 $\left\{-\frac{b_{n}}{n}\right\}$ 和 $\left\{\frac{a_{n}}{n}\right\}$ 要困难许多. 同样, 直接证明 (21.5.8) 式也要比直接证明 (21.5.9) 式更困难. 因此, 我们将选择证明 (21.5.9) 式. 对此, 若能够通过 (21.5.7) 式得到 $F'' = f$, 就可以得到 (21.5.9) 式. 但这在一般情况下是不能指望的. 幸运的是, 可以用二阶的广义导数在代替二阶导数, 然后得到 (21.5.7) 式. 这是证明的关键. 最后, 由于 (21.5.1) 式在 $E$ 上不一定成立, 因此, 一开始不能直接整体地得到 (21.5.7) 式. 我们需要先在 $\mathbb{R} \setminus E$ 中局部地建立相关结果, 然后再拓展到整个 $\mathbb{R}$.

以下的 Cantor 引理表明在定理条件下, 可以得到 $\{a_{n}\}$ 和 $\{b_{n}\}$ 均趋于零.

引理21.5.3 设 $\sum_{n=1}^{\infty}(a_n\cos nx + b_n\sin nx)$ 在区间 $[a, b]$ 上收敛，则 $\lim_{n \to +\infty} a_n = \lim_{n \to +\infty} b_n = 0$.

证明 记 $A_{n}:= \sqrt{a_{n}^{2} + b_{n}^{2}} (n\geqslant 1)$ ，我们有 $\{\theta_n\}$ 使得

$$
a _ {n} \cos n x + b _ {n} \sin n x = A _ {n} \sin (n x + \theta_ {n}), \quad \forall x \in \mathbb {R}. \tag {21.5.10}
$$

由引理假设, 对于任何  $x \in [a, b]$ ,  $\lim_{n \to +\infty} A_n \sin(nx + \theta_n) = 0$ . 我们要证  $\lim_{n \to +\infty} A_n = 0$ .

如若不然, 则有 $n_1 < n_2 < n_3 < \cdots$ 及 $\varepsilon_0$ 使得对任何 $k \geqslant 1$, 有 $A_{n_k} > \varepsilon_0$. 从而对任何 $x \in [a, b]$, 有

$$
\lim _ {k \to + \infty} \sin (n _ {k} x + \theta_ {n _ {k}}) = 0. \tag {21.5.11}
$$

由 Arzelà 有界收敛定理, 得到

$$
\lim _ {k \to + \infty} \int_ {a} ^ {b} \sin^ {2} (n _ {k} x + \theta_ {n _ {k}}) \mathrm{d} x = 0. \tag {21.5.12}
$$

而另一方面，

$$
\begin{array}{l} \lim _ {k \to + \infty} \int_ {a} ^ {b} \sin^ {2} (n _ {k} x + \theta_ {n _ {k}}) \mathrm{d} x \\ = \lim _ {k \to + \infty} \int_ {a} ^ {b} \frac {1 - \cos 2 (n _ {k} x + \theta_ {n _ {k}})}{2} \mathrm{d} x \\ = \frac {1}{2} \lim _ {k \to + \infty} \left(b - a - \frac {\sin 2 (n _ {k} b + \theta_ {n _ {k}}) - \sin 2 (n _ {k} a + \theta_ {n _ {k}})}{2 n _ {k}}\right) \mathrm{d} x = \frac {b - a}{2}. \\ \end{array}
$$

得到矛盾. 因此, 引理成立.

以下两个引理用于将 $\mathbb{R} \setminus E$ 中建立的局部结果, 连接为整个 $\mathbb{R}$ 上的结果.

---

196

第二十一章 Fourier级数

引理 21.5.4 (Riemann 第二定理) 设  $\lim_{n\to+\infty}c_n=0$ ，则

$$
\lim _ {h \to 0} \sum_ {n = 1} ^ {\infty} \frac {c _ {n} \sin^ {2} n h}{n ^ {2} h} = 0. \tag {21.5.13}
$$

证明 设 $M$ 为 $|c_n|$ 的上界. 任取 $\varepsilon > 0$, 对于 $0 < |h| < \varepsilon$, 记 $N \equiv N_{\varepsilon, h}$ 为 $\frac{\varepsilon}{|h|}$ 的整数部分. 则

$$
\begin{array}{l} \left| \sum_ {n = 1} ^ {\infty} \frac {c _ {n} \sin^ {2} n h}{n ^ {2} h} \right| \leqslant \sum_ {n = 1} ^ {N} \left| \frac {c _ {n} \sin^ {2} n h}{n ^ {2} h} \right| + \sum_ {n = N + 1} ^ {\infty} \left| \frac {c _ {n} \sin^ {2} n h}{n ^ {2} h} \right| \\ \leqslant M N | h | + \sup _ {k \geqslant N} \left| c _ {k} \right| \sum_ {n = N + 1} ^ {\infty} \frac {1}{n ^ {2} | h |} \leqslant M \varepsilon + \frac {\sup _ {k \geqslant N} \left| c _ {k} \right|}{N | h |} \leqslant M \varepsilon + \frac {2 \sup _ {k \geqslant N} \left| c _ {k} \right|}{\varepsilon}. \\ \end{array}
$$

于是注意到  $\lim_{h\to0}N_{\varepsilon,h}=+\infty$ ，我们有

$$
\overline {{\lim _ {h \to 0}}} \left| \sum_ {n = 1} ^ {\infty} \frac {c _ {n} \sin^ {2} n h}{n ^ {2} h} \right| \leqslant M \varepsilon .
$$

由  $\varepsilon > 0$  的任意性, 即得 (21.5.13) 式.

![](../../raw/pages_0833-0848/images/page_835_image_9.jpg)

引理 21.5.5 R 中的可列闭集必有孤立点.

证明 设 $E \subset \mathbb{R}$ 为可列闭集, $E = \{x_k | k \geqslant 1\}$. 若 $E$ 没有孤立点, 则 $E$ 中每一点均为其聚点.

于是, 有 $y_{1} \in E$ 使得 $y_{1} \neq x_{1}$. 取 $\delta_{1} = \frac{|y_{1} - x_{1}|}{2}$, 则 $\delta_{1} > 0$, $x_{1} \notin [y_{1} - \delta_{1}, y_{1} + \delta_{1}]$.

进一步，由于 $y_{1}$ 是 $E$ 的聚点，因此，有 $y_{2} \in E \cap (y_{1} - \delta_{1}, y_{1} + \delta_{1})$ 使得 $y_{2} \neq x_{2}$. 取 $\delta_{2} = \frac{1}{2} \min \{|y_{2} - x_{1}|, \delta_{1} - |y_{2} - y_{1}|\}$，则 $0 < \delta_{2} \leqslant \frac{\delta_{1}}{2}, [y_{2} - \delta_{2}, y_{2} + \delta_{2}] \subset [y_{1} - \delta_{1}, y_{1} + \delta_{1}], x_{2} \notin [y_{2} - \delta_{2}, y_{2} + \delta_{2}]$.

一般地, 可取到 $E$ 中点列 $\{y_k\}$ 以及相应的正数列 $\{\delta_k\}$ 使得对任何 $k \geqslant 2$, 有 $0 < \delta_k \leqslant \frac{\delta_{k-1}}{2}, [y_k - \delta_k, y_k + \delta_k] \subset [y_{k-1} - \delta_{k-1}, y_{k-1} + \delta_{k-1}], x_k \notin [y_k - \delta_k, y_k + \delta_k]$.

由闭集套定理, $\{[y_k - \delta_k, y_k + \delta_k]\}$ 有唯一的公共点 $\xi$. 则对任何 $k \geqslant 1$, $\xi \neq x_k$. 从而 $\xi \notin E$. 另一方面, 由于 $E$ 是闭集, 从而 $\xi = \lim_{k \to +\infty} y_k \in E$. 矛盾. 因此, 引理结论成立.

引理 21.5.5 是 Baire $^{①}$ 纲定理的特例. 在引入以下的引理前, 我们考察一种二阶广义导数. 对于函数 g, 如果 $g^{[\prime\prime]}(x):=\lim_{h\to0}\frac{\Delta_{h}^{2}g(x)}{h^{2}}$ 存在, 则称之为 g 在 x 点的二阶广义导数, 其中对于 $h\neq0$,

$$
\Delta_ {h} ^ {2} g (x) := g (x + h) + g (x - h) - 2 g (x).
$$

以下引理用于证明 F 的两阶广义导数为 f.

引理21.5.6 设 $\sum_{n=1}^{\infty} c_n = A$, 则

$$
\lim _ {h \to 0} \sum_ {n = 1} ^ {\infty} c _ {n} \left(\frac {\sin n h}{n h}\right) ^ {2} = A. \tag {21.5.14}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Baire, René-Louis, 1874 年 1 月 21 日—1932 年 7 月 5 日, 法国数学家.</span></small>

---

21.5 Fourier级数的唯一性

197

证明 不妨设 $A = 0$ ，记 $S_{n} = \sum_{k = 1}^{n}c_{k}(n\geqslant 1)$ .则

$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} c _ {n} \left(\frac {\sin n h}{n h}\right) ^ {2} = \sum_ {n = 1} ^ {\infty} S _ {n} \left(\frac {\sin n h}{n h}\right) ^ {2} - \sum_ {n = 2} ^ {\infty} S _ {n - 1} \left(\frac {\sin n h}{n h}\right) ^ {2} \\ = \sum_ {n = 1} ^ {\infty} S _ {n} \left[ \left(\frac {\sin n h}{n h}\right) ^ {2} - \left(\frac {\sin (n + 1) h}{(n + 1) h}\right) ^ {2} \right]. \\ \end{array}
$$

于是对任何  $m \geqslant 1$ ,

$$
\begin{array}{l} \varlimsup_ {h \to 0} \left| \sum_ {n = 1} ^ {\infty} c _ {n} \left(\frac {\sin n h}{n h}\right) ^ {2} \right| \leqslant \varlimsup_ {h \to 0} \sum_ {n = m} ^ {\infty} | S _ {n} | \left| \left(\frac {\sin n h}{n h}\right) ^ {2} - \left(\frac {\sin (n + 1) h}{(n + 1) h}\right) ^ {2} \right| \\ \leqslant \sup _ {n \geqslant m} | S _ {n} | \int_ {0} ^ {+ \infty} \left| \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {\sin t}{t}\right) ^ {2} \right| \mathrm{d} t. \\ \end{array}
$$

注意到  $\int_{0}^{+\infty}\left|\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\sin t}{t}\right)^{2}\right|$  dt 收敛, 在上式中令  $m\to+\infty$  即得 (21.5.14) 式.

![](../../raw/pages_0833-0848/images/page_836_image_7.jpg)

以下引理用于证明 (21.5.7) 式在 $\mathbb{R} \setminus E$ 中局部成立.

引理21.5.7 设函数 $g \in C[a, b]$，且在区间 $[a, b]$ 内的二阶广义导数 $g^{[n]}$ 存在，且 $m \leqslant g^{[n]} \leqslant M$。则对任何 $h \in \left(0, \frac{b - a}{2}\right)$，当 $a + h \leqslant x \leqslant b - h$ 时，

$$
m \leqslant \frac {\Delta_ {h} ^ {2} g (x)}{h ^ {2}} \leqslant M \tag {21.5.15}
$$

成立.

证明 任取 $x_0 \in (a, b)$, $h > 0$ 满足 $a \leqslant x_0 - h \leqslant x_0 + h \leqslant b$. 考察

$$
\varphi (x) := g (x) - g (x _ {0}) - \frac {g (x _ {0} + h) - g (x _ {0} - h)}{2 h} (x - x _ {0}) - \frac {\Delta_ {h} ^ {2} g (x _ {0})}{h ^ {2}} \frac {(x - x _ {0}) ^ {2}}{2},
$$

则 $\varphi (x_0 + h) = \varphi (x_0) = \varphi (x_0 - h) = 0.$ 因此，$\varphi$ 在 $[x_0 - h, x_0 + h]$ 上的最大值和最小值都可以在 $(x_0 - h, x_0 + h)$ 的内部取到. 设 $\xi, \eta$ 分别为最大值点和最小值点，则

$$
\varphi^ {[ \prime \prime ]} (\xi) \leqslant 0, \quad \varphi^ {[ \prime \prime ]} (\eta) \geqslant 0.
$$

即

$$
g ^ {[ \prime \prime ]} (\xi) \leqslant \frac {\Delta_ {h} ^ {2} g (x _ {0})}{h ^ {2}} \leqslant g ^ {[ \prime \prime ]} (\eta).
$$

从而 (21.5.15) 式成立.

![](../../raw/pages_0833-0848/images/page_836_image_19.jpg)

引理21.5.7的证明也可以通过证明 $\frac{Mx^2}{2} -g(x)$ 和 $g(x) - \frac{mx^2}{2}$ 均为凸函数得到.

现在我们来证明定理 21.5.2.

定理 21.5.2 的证明 不妨设  $a_{0}=0$  。对 (21.5.1) 式形式上逐项积分两次，得到由 (21.5.7) 式定义的函数 F。

---

198

第二十一章 Fourier级数

由引理21.5.3, $\{a_{n}\}$ 和 $\{b_n\}$ 均趋于零. 因此, $\sum_{n=1}^{\infty} \left( \frac{a_{n}}{n^{2}} \cos nx + \frac{b_{n}}{n^{2}} \sin nx \right)$ 一致收敛, 从而 $F \in C(\mathbb{R})$. 直接计算得到

$$
\frac {\Delta_ {h} ^ {2} F (x)}{h ^ {2}} = \sum_ {n = 1} ^ {\infty} \frac {a _ {n} \cos n x + b _ {n} \sin n x}{n ^ {2}} \left(\frac {2 \sin \frac {n h}{2}}{h}\right) ^ {2}. \tag {21.5.16}
$$

于是, 由引理 21.5.6, 有 $^{①}$

$$
F ^ {[ \prime \prime ]} (x) = f (x), \qquad \forall   x \in \mathbb {R} \setminus E. \tag {21.5.17}
$$

现考虑区间  $[a, b] \subset R \setminus E$ . 我们要建立以下等式:

$$
\begin{array}{l} F (x) - F (a) - \frac {F (b) - F (a)}{b - a} (x - a) \\ = \int_ {a} ^ {x} (x - s) f (s) \mathrm{d} s - \frac {x - a}{b - a} \int_ {a} ^ {b} (b - s) f (s) \mathrm{d} s, \quad \forall x \in [ a, b ]. \tag {21.5.18} \\ \end{array}
$$

首先, 利用 L'Hôpital 法则易得

$$
\begin{array}{l} \lim _ {h \to 0 ^ {+}} \left(\int_ {a} ^ {x} (x - s) \frac {\Delta_ {h} ^ {2} F (s)}{h ^ {2}} \mathrm{d} s - \frac {x - a}{b - a} \int_ {a} ^ {b} (b - s) \frac {\Delta_ {h} ^ {2} F (s)}{h ^ {2}} \mathrm{d} s\right) \\ = \lim _ {h \to 0 ^ {+}} \frac {1}{h ^ {2}} \left(\int_ {x} ^ {x + h} (x + h - s) F (s) \mathrm{d} s - \int_ {x - h} ^ {x} (x - h - s) F (s) \mathrm{d} s + \right. \\ \int_ {a - h} ^ {a} \frac {(b - x) (a - h - s)}{b - a} F (s) \mathrm{d} s - \int_ {a} ^ {a + h} \frac {(b - x) (a + h - s)}{b - a} F (s) \mathrm{d} s - \\ \frac {x - a}{b - a} \int_ {b} ^ {b + h} (b + h - s) F (s) \mathrm{d} s + \frac {x - a}{b - a} \int_ {b - h} ^ {b} (b - h - s) F (s) \mathrm{d} s\left. \right) \\ = F (x) - F (a) - \frac {F (b) - F (a)}{b - a} (x - a), \quad \forall x \in [ a, b ]. \tag {21.5.19} \\ \end{array}
$$

即 (21.5.19) 式左端的极限等于 (21.5.18) 的左端. 为得到 (21.5.18) 式, 我们要证 (21.5.19) 式左端的极限也等于 (21.5.18) 式的右端. 这只要说明 $\frac{\Delta_h^2 F(x)}{h^2}$ 满足 Arzelà 有界收敛定理的条件. 注意到 $E$ 为闭集, 因此, 存在 $h_0 > 0$ 使得 $[a - h_0, b + h_0]$ 与 $E$ 不交. 又由假设条件, $f$ 在 $[a - h_0, b + h_0]$ 上有界, 设上界为 $M$, 下界为 $m$. 这样, 由引理 21.5.7,

$$
m \leqslant \frac {\Delta_ {h} ^ {2} F (x)}{h ^ {2}} \leqslant M, \quad \forall h \in (0, h _ {0}), x \in [ a, b ]. \tag {21.5.20}
$$

于是, 由 (21.5.17) 式以及 Arzelà 有界收敛定理得到

$$
\begin{array}{l} \lim _ {h \to 0 ^ {+}} \left(\int_ {a} ^ {x} (x - s) \frac {\Delta_ {h} ^ {2} F (s)}{h ^ {2}} \mathrm{d} s - \frac {x - a}{b - a} \int_ {a} ^ {b} (b - s) \frac {\Delta_ {h} ^ {2} F (s)}{h ^ {2}} \mathrm{d} s\right) \\ = \int_ {a} ^ {x} (x - s) f (s) \mathrm{d} s - \frac {x - a}{b - a} \int_ {a} ^ {b} (b - s) f (s) \mathrm{d} s, \quad \forall x \in [ a, b ]. \tag {21.5.21} \\ \end{array}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① (21.5.17) 式称为 Riemann 第一定理.</span></small>

---

21.5 Fourier 级数的唯一性

199

结合 (21.5.19) 式和 (21.5.21) 式, 就得到 (21.5.18) 式. 于是 $F$ 限制在 $[a, b]$ 上连续可导且

$$
F ^ {\prime} (x) - \frac {F (b) - F (a)}{b - a} = \int_ {a} ^ {x} f (s) \mathrm{d} s - \int_ {a} ^ {b} (b - s) f (s) \mathrm{d} s, \quad \forall x \in [ a, b ]. \tag {21.5.22}
$$

进而

$$
F ^ {\prime} (x) - F ^ {\prime} (a) = \int_ {a} ^ {x} f (t) \mathrm{d} t, \quad \forall x \in [ a, b ]. \tag {21.5.23}
$$

由 $f\in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 可见 $F$ 在 $\mathbb{R}\setminus E$ 内连续可导，且对任何 $[\alpha ,\beta ]\subset \mathbb{R}\setminus E,$ 有

$$
F ^ {\prime} (\beta) - F ^ {\prime} (\alpha) = \int_ {\alpha} ^ {\beta} f (t) \mathrm{d} t. \tag {21.5.24}
$$

现设

$$
V := \left\{x \in \mathbb {R}   \big |   \exists   \delta > 0, \text {s.t.} \right. \text {对任意} [ \alpha , \beta ] \subset (x - \delta , x + \delta), (2 1. 5. 2 4) \text {式成立} \left. \right\}.
$$

则 $V$ 为开集, $E^{*} := \mathbb{R} \setminus V \subseteq E$. 我们断言 $V = \mathbb{R}$. 否则 $E^{*}$ 为至多可列的非空闭集. 由引理21.5.5, $E^{*}$ 有孤立点 $\xi$. 进而有 $\alpha, \beta$ 使得 $\alpha < \xi < \beta$, $[\alpha, \xi) \cup (\xi, \beta] \subset V$, 从而由 (21.5.23) 式,

$$
\lim _ {x \to \xi^ {-}} F ^ {\prime} (x) = F ^ {\prime} (\alpha) + \int_ {\alpha} ^ {\xi} f (t) \mathrm{d} t.
$$

结合 F 的连续性以及 L'Hôpital 法则, 可得  $F_{-}^{\prime}(\xi)$  存在, 且

$$
F _ {-} ^ {\prime} (\xi) = F ^ {\prime} (\alpha) + \int_ {\alpha} ^ {\xi} f (t) \mathrm{d} t. \tag {21.5.25}
$$

同理, $F_{+}^{\prime}(\xi)$ 存在,且

$$
F _ {+} ^ {\prime} (\xi) = F ^ {\prime} (\beta) + \int_ {\beta} ^ {\xi} f (t) \mathrm{d} t. \tag {21.5.26}
$$

由 (21.5.16) 式和引理 21.5.4,

$$
\lim _ {h \to 0 ^ {+}} \frac {F (\xi + h) + F (\xi - h) - 2 F (\xi)}{h} = \lim _ {h \to 0} \frac {\Delta_ {h} ^ {2} F (\xi)}{h} = 0.
$$

因此，

$$
F _ {+} ^ {\prime} (\xi) = \lim _ {h \to 0 ^ {+}} \frac {F (\xi + h) - F (\xi)}{h} = \lim _ {h \to 0 ^ {+}} \frac {F (\xi) - \dot {F} (\xi - h)}{h} = F _ {-} ^ {\prime} (\xi).
$$

结合(21.5.25)式—(21.5.26)式可见 $\xi \in V$. 得到矛盾. 因此, $V = \mathbb{R}$. 从而 $F$ 在 $\mathbb{R}$ 上连续可导, 且

$$
F ^ {\prime} (x) - F ^ {\prime} (0) = \int_ {0} ^ {x} f (t) \mathrm{d} t, \quad \forall x \in \mathbb {R}. \tag {21.5.27}
$$

注意到 $F$ 以 $2\pi$ 为周期, 因此 $\int_{0}^{2\pi} f(t) \, \mathrm{d}t = F'(2\pi) - F'(0) = 0$. 于是, 利用分部积分可得

$$
\begin{array}{l} \frac {1}{\pi} \int_ {0} ^ {2 \pi} f (x) \cos n x \mathrm{d} x = \frac {n}{\pi} \int_ {0} ^ {2 \pi} \left(\int_ {0} ^ {x} f (t) \mathrm{d} t\right) \sin n x \mathrm{d} x \\ = \frac {n}{\pi} \int_ {0} ^ {2 \pi} \left(F ^ {\prime} (x) - F ^ {\prime} (0)\right) \sin n x \mathrm{d} x = \frac {n}{\pi} \int_ {0} ^ {2 \pi} F ^ {\prime} (x) \sin n x \mathrm{d} x \\ \end{array}
$$

---

200

第二十一章 Fourier 级数

$$
= - \frac {n ^ {2}}{\pi} \int_ {0} ^ {2 \pi} F (x) \cos n x \mathrm{d} x = a _ {n}, \quad \forall n \geqslant 1.
$$

即 (21.5.3) 式成立. 同理, 可以得到 (21.5.4) 式. 定理得证.

现在我们来回答本节开头提到的第三个问题. 在第二节, 我们谈及了 Luzin 猜想-Calson 定理, 知道 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 中函数的 Fourier 级数是几乎处处收敛到 $f$ 的. 在这个基础上来看第三个问题, 回答是肯定的. 即有 $\int_{0}^{2\pi}|g(x) - f(x)| \mathrm{d}x = 0$. 然而, 这里的积分需要在 Lebesgue 积分的意义下去理解. 换言之, 当 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 时, 其 Fourier 级数的和函数 $g$ (若存在) 是否属于 $\mathcal{R}_{\#}^{1}(\mathbb{R})$ 仍然是一个问题. 值得注意的是, Kolmogorov 给出过 Lebesgue 可积函数的 Fourier 级数处处发散的例子, 因此, 在第三个问题中把 $\mathcal{R}_{\#}^{1}(\mathbb{R})$ 换成 $L_{\#}^{1}(\mathbb{R})$ 是两个相当不同的问题. 而对于 $\mathcal{R}_{\#}^{1}(\mathbb{R})$ 中的函数, 我们可以找出一个函数使得它的 Fourier 级数在任何一个预先给定的可列集上发散. 此时 Fourier 级数的和函数可以在一个稠密集上无定义, 从而也无从谈它属于 $\mathcal{R}_{\#}^{1}(\mathbb{R})$. 从中, 我们也可以看到, 如果降低第三个问题的条件, 则可以产生很多不同的问题. 而这些问题在 $\mathcal{R}_{\#}^{1}(\mathbb{R})$ 中讨论通常要比在 $L_{\#}^{1}(\mathbb{R})$ 中讨论更复杂一些. 另一方面, 对第三个问题的上述回答是基于困难的 Calson 定理. 以下我们对相关结论作一个相对简单的证明.

定理21.5.8 设 $E \subset \mathbb{R}$ 的二阶导集为空集, $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 在 $\mathbb{R} \setminus E$ 上收敛到 $g$, 且对于任何有界闭区间 $[a, b] \subset \mathbb{R} \setminus \overline{E}$, $g$ 在 $[a, b]$ 上 Riemann 可积. 则 $g \in \mathcal{R}_{\#}^{1}(\mathbb{R})$, 且

$$
\int_ {0} ^ {2 \pi} | g (x) - f (x) | \mathrm{d} x = 0. \tag {21.5.28}
$$

证明 不妨设 $E$ 包含 $f$ 的所有瑕点. 任取 $\delta \in (0, \pi)$, 则

$$
\begin{array}{l} \| \sigma_ {n} (f; \cdot) - f (\cdot) \| _ {\mathcal {R} ^ {1} [ 0, 2 \pi ]} \\ = \int_ {- \pi} ^ {\pi} \left| \frac {1}{2 n \pi} \int_ {- \pi} ^ {\pi} (f (x + t) - f (x)) \left(\frac {\sin \frac {n t}{2}}{\sin \frac {t}{2}}\right) ^ {2} \mathrm{d} t \right| \mathrm{d} x \\ \leqslant \frac {1}{2 n \pi} \int_ {- \pi} ^ {\pi} \mathrm{d} t \int_ {- \pi} ^ {\pi} | f (x + t) - f (x) | \left(\frac {\sin \frac {n t}{2}}{\sin \frac {t}{2}}\right) ^ {2} \mathrm{d} x \\ \leqslant \frac {1}{2 n \pi} \int_ {\delta <   | t | \leqslant \pi} \left(\frac {\sin \frac {n t}{2}}{\sin \frac {t}{2}}\right) ^ {2} \mathrm{d} t \cdot 2 \| f \| _ {\mathcal {R} ^ {1} [ 0, 2 \pi ]} + \sup _ {| t | \leqslant \delta} \int_ {- \pi} ^ {\pi} | f (x + t) - f (x) | \mathrm{d} x. \\ \end{array}
$$

因此，

$$
\varlimsup_ {n \to + \infty} \| \sigma_ {n} (f; \cdot) - f (\cdot) \| _ {\mathcal {R} ^ {1} [ 0, 2 \pi ]} \leqslant \sup _ {| t | \leqslant \delta} \int_ {- \pi} ^ {\pi} | f (x + t) - f (x) | \mathrm{d} x.
$$

再令 $\delta \to 0^{+}$ 得到 $\lim_{n\to +\infty}\| \sigma_n(f;\cdot) - f(\cdot)\|_{\mathcal{R}^1 [0,2\pi]} = 0.$ 从而对于 $[a,b]\subset \mathbb{R}\setminus \overline{E},$

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} | \sigma_ {n} (f; x) - f (x) | \mathrm{d} x = 0.
$$

---

21.5 Fourier级数的唯一性

201

这等价于

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} | \arctan \sigma_ {n} (f; x) - \arctan f (x) | \mathrm{d} x = 0. \tag {21.5.29}
$$

另一方面，由定理假设， $S_{n}(f;\cdot)$ 在 $[a,b]$ 上收敛到 $g(\cdot)$. 从而 $\sigma_n(f;\cdot)$ 在 $[a,b]$ 上收敛到 $g(\cdot)$. 由Arzelà有界收敛定理，

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} | \arctan \sigma_ {n} (f; x) - \arctan g (x) | \mathrm{d} x = 0. \tag {21.5.30}
$$

因此, 结合 (21.5.29) 式—(21.5.30) 式得到

$$
\int_ {a} ^ {b} | \arctan f (x) - \arctan g (x) | \mathrm{d} x = 0.
$$

这等价于

$$
\int_ {a} ^ {b} | f (x) - g (x) | \mathrm{d} x = 0.
$$

由此即可得到定理结论.

![](../../raw/pages_0833-0848/images/page_840_image_11.jpg)

## 习题 21.5

1. 试利用闭区间套定理证明引理 21.5.3.
2. 设函数 $f \in C[a, b]$，且在区间 $[a, b]$ 内的二阶广义导数 $f^{[n]}$ 非负。证明:$f$ 是凸函数。
3. 试构造一个可列闭集使得其二阶导集非空.
