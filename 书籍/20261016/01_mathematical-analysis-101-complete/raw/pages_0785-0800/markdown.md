$$
= \psi (x + n) - \psi (y + n) - \sum_ {k = 0} ^ {n - 1} \left(\frac {1}{x + k} - \frac {1}{y + k}\right). \tag {20.4.25}
$$

另一方面, 由于 $\Gamma$ 是 log-凸的, 因此 $\psi$ 单调增加, 所以当 $y \leqslant x \leqslant y + 1$ 时,

$$
\begin{array}{l} 0 \leqslant \psi (x + n) - \psi (y + n) \\ = \frac {1}{x + n - 1} + \psi (x + n - 1) - \psi (y + n) \\ \leqslant \frac {1}{x + n - 1}, \quad \forall n \geqslant 1. \\ \end{array}
$$

由此得到

$$
\lim _ {n \to + \infty} (\psi (x + n) - \psi (y + n)) = 0. \tag {20.4.26}
$$

结合 (20.4.24) 式知 (20.4.26) 式对所有 $x, y > 0$ 成立. 于是, 在 (20.4.25) 式中令 $n \to +\infty$ 即得 (20.4.23) 式. □

(3) 对 (20.4.23) 式关于 x 求导即得

$$
\psi^ {\prime} (x) = \sum_ {n = 0} ^ {\infty} \frac {1}{(n + x) ^ {2}}, \quad x > 0. \tag {20.4.27}
$$

(4) 对 (20.4.27) 式求导得

$$
\psi^ {\prime \prime} (x) = - \sum_ {n = 0} ^ {\infty} \frac {2}{(n + x) ^ {3}}, \quad x > 0. \tag {20.4.28}
$$

(5) 对余元公式 (20.4.15) 两边取对数后求导可得 $^{①}$

$$
\psi (x) - \psi (1 - x) = - \pi \cot \pi x, \quad \forall x \in (0, 1). \tag {20.4.29}
$$

(6) 对 (20.4.14) 式两边取对数后求导可得: 对于  $k \geqslant 2$ ,

$$
\sum_ {j = 0} ^ {k - 1} \psi \left(x + \frac {j}{k}\right) = k (\psi (k x) - \ln k), \quad \forall x > 0 \tag {20.4.30}
$$

成立.

(7) $\Gamma'(1) = \psi(1) = -\gamma$, 其中 $\gamma$ 为 Euler 常数 $\gamma := \lim_{n \to +\infty} \left( \sum_{k=1}^{n} \frac{1}{k} - \ln n \right)$.

证明 我们有

$$
\Gamma^ {\prime} (1) = \psi (1) = \psi (n + 1) - \sum_ {k = 1} ^ {n} \frac {1}{k}, \qquad \forall n \geqslant 1.
$$

另一方面, 因为  $\ln \Gamma(x)$  是凸函数, 可得

$$
\ln \Gamma (x + 1) - \ln \Gamma (x) \leqslant \psi (x + 1) \leqslant \ln \Gamma (x + 2) - \ln \Gamma (x + 1), \quad \forall x > 0.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 通过其他方式, 比如利用 Fourier 级数得到 (20.4.29) 式, 即可得到余元公式的另一种证明.</span></small>

由此可得

$$
\ln n \leqslant \psi (n + 1) \leqslant \ln (n + 1).
$$

因此，

$$
\ln n - \sum_ {k = 1} ^ {n} \frac {1}{k} \leqslant \Gamma^ {\prime} (1) \leqslant \ln (n + 1) - \sum_ {k = 1} ^ {n} \frac {1}{k}, \quad \forall n \geqslant 1.
$$

在上式中令  $n \rightarrow +\infty$  即得  $\Gamma'(1) = -\gamma$ .

(8) 在 (20.4.30) 式取 $k = 2, x = \frac{1}{2}$, 得到

$$
\psi \left(\frac {1}{2}\right) = \psi (1) - 2 \ln 2 = - 2 \ln 2 - \gamma .
$$

在 (20.4.30) 式取 $k = 3$, $x = \frac{1}{3}$, 得到 $\psi \left(\frac{1}{3}\right) + \psi \left(\frac{2}{3}\right) = -2\gamma - 3\ln 3$. 再在 (20.4.29) 式中取 $x = \frac{1}{3}$ 得到 $\psi \left(\frac{1}{3}\right) - \psi \left(\frac{2}{3}\right) = -\frac{\sqrt{3}\pi}{3}$. 解得

$$
\psi \left(\frac {1}{3}\right) = - \gamma - \frac {3 \ln 3}{2} - \frac {\sqrt {3} \pi}{6},
$$

$$
\psi \left(\frac {2}{3}\right) = - \gamma - \frac {3 \ln 3}{2} + \frac {\sqrt {3} \pi}{6}.
$$

在 (20.4.30) 式取 $k = 4$, $x = \frac{1}{4}$, 得到 $\psi \left(\frac{1}{4}\right) + \psi \left(\frac{3}{4}\right) = -3\gamma - 4\ln 4 - \psi \left(\frac{1}{2}\right)$. 再在 (20.4.29) 式中取 $x = \frac{1}{4}$ 得到 $\psi \left(\frac{1}{4}\right) - \psi \left(\frac{3}{4}\right) = -\pi$. 解得

$$
\psi \left(\frac {1}{4}\right) = - \gamma - 3 \ln 2 - \frac {\pi}{2},
$$

$$
\psi \left(\frac {3}{4}\right) = - \gamma - 3 \ln 2 + \frac {\pi}{2}.
$$

在 (20.4.30) 式取 $k = 6, x = \frac{1}{6}$, 得到 $\psi \left(\frac{1}{6}\right) + \psi \left(\frac{5}{6}\right) = -5\gamma - 6\ln 6 - \psi \left(\frac{1}{3}\right) - \psi \left(\frac{1}{2}\right) - \psi \left(\frac{2}{3}\right)$. 再在 (20.4.29) 式中取 $x = \frac{1}{6}$ 得到 $\psi \left(\frac{1}{6}\right) - \psi \left(\frac{5}{6}\right) = -\sqrt{3}\pi$. 解得

$$
\psi \left(\frac {1}{6}\right) = - \gamma - 2 \ln 2 - \frac {3 \ln 3}{2} - \frac {\sqrt {3} \pi}{2},
$$

$$
\psi \left(\frac {5}{6}\right) = - \gamma - 2 \ln 2 - \frac {3 \ln 3}{2} + \frac {\sqrt {3} \pi}{2}.
$$

利用  $\psi$  函数的性质 (20.4.23)，例 20.4.5 中的级数也可以计算如下:

$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2} - \alpha^ {2}} = \frac {1}{2 \alpha} \sum_ {n = 1} ^ {\infty} \left(\frac {1}{n - \alpha} - \frac {1}{n + \alpha}\right) = \frac {1}{2 \alpha} (\psi (1 + \alpha) - \psi (1 - \alpha)) \\ = \frac {1}{2 \alpha} \left(\frac {1}{\alpha} + \psi (\alpha) - \psi (1 - \alpha)\right) = \frac {1}{2 \alpha^ {2}} + \frac {1}{2 \alpha} \frac {\mathrm{d}}{\mathrm{d} \alpha} \ln (\Gamma (\alpha) \Gamma (1 - \alpha)) \\ \end{array}
$$

$$
= \frac {1}{2 \alpha^ {2}} - \frac {\pi \cot (\alpha \pi)}{2 \alpha}.
$$

复数域内的 $\Gamma$ 函数 容易对实部为正的复数 $z$ 定义 $\Gamma(z)$ 如下:

$$
\Gamma (z) := \int_ {0} ^ {+ \infty} x ^ {z - 1} \mathrm{e} ^ {- x} \mathrm{d} x, \quad \forall z \in \mathbb {C}, \operatorname{Re} z > 0. \tag {20.4.31}
$$

易见  $\Gamma$  函数是  $\{z \in C | Re z > 0\}$  内的解析函数 $^{①}$ . 进一步, 递推公式  $\Gamma(z + 1) = z \Gamma(z)$  对任何满足 Re z > 0 的 z 成立. 由此可以把  $\Gamma$  函数的定义域拓展到区域  $D_{\Gamma} := \{z \in C | z \neq 0, -1, -2, \cdots\}$ . 进而  $\Gamma$  函数是  $D_{\Gamma}$  内的解析函数. 另一方面,  $z \mapsto \frac{\pi}{\sin(z \pi)}$  也是  $D_{\Gamma}$  内的解析函数, 由解析函数的唯一性 $^{②}$ , 即得

$$
\Gamma (z) \Gamma (1 - z) = \frac {\pi}{\sin (z \pi)} \equiv \frac {2 \mathrm{i} \pi}{\mathrm{e} ^ {\mathrm{i} z \pi} - \mathrm{e} ^ {- \mathrm{i} z \pi}}, \quad \forall z \in D _ {\Gamma}. \tag {20.4.32}
$$

利用 (20.4.9) 式的证明方法, 同样可以得到

$$
\lim _ {s \to + \infty} \frac {\Gamma (s + z)}{\Gamma (s) s ^ {z}} = 1, \quad \forall z \in \mathbb {C}. \tag {20.4.33}
$$

例20.4.6 试计算无穷乘积 $\prod_{n=1}^{\infty}\left(1 + \frac{1}{n^4}\right)$.

解 记 $\omega = \mathrm{e}^{\frac{\pi\mathrm{i}}{4}}$ ，由(20.4.33)式，我们有

$$
\begin{array}{l} \prod_ {n = 1} ^ {\infty} \left(1 + \frac {1}{n ^ {4}}\right) = \lim _ {n \to + \infty} \prod_ {k = 1} ^ {n} \frac {(k - \omega) (k + \omega) (k - \mathrm{i} \omega) (k + \mathrm{i} \omega)}{k ^ {4}} \\ = \lim _ {n \to + \infty} \frac {\Gamma (n + 1 - \omega) \Gamma (n + 1 + \omega) \Gamma (n + 1 - \mathrm{i} \omega) \Gamma (n + 1 + \mathrm{i} \omega)}{(n !) ^ {4} \Gamma (1 - \omega) \Gamma (1 + \omega) \Gamma (1 - \mathrm{i} \omega) \Gamma (1 + \mathrm{i} \omega)} \\ = \frac {1}{\Gamma (1 - \omega) \Gamma (1 + \omega) \Gamma (1 - \mathrm{i} \omega) \Gamma (1 + \mathrm{i} \omega)} \\ = \frac {1}{\mathrm{i} \omega^ {2} \Gamma (1 - \omega) \Gamma (\omega) \Gamma (1 - \mathrm{i} \omega) \Gamma (\mathrm{i} \omega)} = \frac {\sin (\omega \pi) \sin (\mathrm{i} \omega \pi)}{\mathrm{i} \omega^ {2} \pi^ {2}} \\ = \frac {\cos ((1 - \mathrm{i}) \omega \pi) - \cos ((1 + \mathrm{i}) \omega \pi)}{- 2 \pi^ {2}} = \frac {\cosh (\sqrt {2} \pi) - \cos (\sqrt {2} \pi)}{2 \pi^ {2}}. \\ \end{array}
$$

## 习题 20.4

1. 求实数 $a$ 的取值范围, 使得积分 $\int_0^{+\infty} \frac{1}{x^a(x+1)(x+2)(x+3)} \, \mathrm{d}x$ 收敛, 并计算该积分.

2. 试计算如下积分:

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 复区域 $D$ 内的复值函数 $g$ 为解析函数, 是指在每一点 $z_0 \in D$, $g$ 在 $z_0$ 的一个小邻域内等于一个幂级数 $\sum_{n=0}^{\infty} c_n (z - z_0)^n$.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② 若 $g, h$ 都是复区域 $D$ 内的解析函数，且 $\{z \in D | g(z) = h(z)\}$ 有聚点属于 $D$ ，则易证 $g \equiv h$.</span></small>

(1) $\int_0^1\frac{\ln(1 + x)}{x}\mathrm{d}x;$
(2) $\int_0^1\frac{\ln(1 + x^2)}{x}\mathrm{d}x,\quad p,q > 0;$
(3) $\int_{0}^{1}\frac{\ln(1 + x + x^2)}{x}\mathrm{d}x;$
(4) $\int_0^1\frac{\ln(1 - x + x^2)}{x}\mathrm{d}x.$
3. 设 $n \geqslant 2$, 试用多种方法证明 $\prod_{k=0}^{n-1} \sin \left(x + \frac{k\pi}{n}\right) = \frac{\sin nx}{2^{n-1}}$.
4. 设  $n \geqslant 2$ , 证明:  $\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}=\frac{n}{2^{n-1}}$ .
5. 设  $n \geqslant 2$ , 证明:  $\prod_{k=1}^{n-1}\Gamma\left(\frac{k}{n}\right)=\frac{1}{\sqrt{n}}(2\pi)^{\frac{n-1}{2}}$ .
6. 计算  $\int_{0}^{1}\ln\Gamma(x)\mathrm{d}x$ .
7. 设 $f \in C^{1}(\mathbb{R})$ 以 1 为周期, $f(x) + f\left(x + \frac{1}{2}\right) = f(2x)$. 证明: $f \equiv 0$.
8. 给出 (20.4.9) 式、(20.4.33) 式的详细证明过程.
9. 证明: $\int_{0}^{+\infty} \frac{\mathrm{e}^{-x} - \cos x}{x} \, \mathrm{d}x = 0.$
10. 计算  $\int_{0}^{+\infty}\frac{\cos x-\cos x^{2}}{x}dx.$
11. 计算  $\int_{-\infty}^{+\infty}\sin t^{2}\,dt.$
12. 计算 $\lim_{x\to 0^{+}}\sum_{n = 1}^{\infty}\frac{nx^{2}}{1 + n^{3}x^{3}}.$
13. 计算  $\psi'\left(\frac{1}{2}\right)$ .
14. 计算  $\int_{0}^{+\infty}\frac{\ln x\ln(1+x^{2})}{1+x^{2}}\mathrm{d}x.$
15. 计算  $\int_{0}^{+\infty}\frac{\ln x}{x^{2}-1}dx.$

## 第二十一章

## Fourier 级数

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