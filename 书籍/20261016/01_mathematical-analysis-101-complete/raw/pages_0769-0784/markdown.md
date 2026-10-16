![](images/page_768_chart_2.jpg)

<details>
<summary>partition</summary>

| X | Y |
| --- | --- |
| 0 | 1 |
| 1 | 1 |
| 1 | 2 |
| 1 | 3 |
| 2 | 2 |
| 2 | 3 |
| 2 | 4 |
| 3 | 3 |
| 3 | 4 |
| 3 | 5 |
| 4 | 4 |
| 4 | 5 |
| 5 | 5 |
</details>

图20.1

则易见

$$
\int_ {0} ^ {+ \infty} \mathrm{d} y \int_ {0} ^ {+ \infty} f (x, y) \mathrm{d} x = 1, \quad \int_ {0} ^ {+ \infty} \mathrm{d} x \int_ {0} ^ {+ \infty} f (x, y) \mathrm{d} y = 0.
$$

例20.3.2 计算 $\lim_{n\to +\infty}n^2\int_0^{+\infty}\frac{\cos x^2}{(1 + x + 2x^2)^n}\ln (1 + x)\mathrm{d}x.$

解 作变量代换可得

$$
n ^ {2} \int_ {0} ^ {+ \infty} \frac {\cos x ^ {2}}{(1 + x + 2 x ^ {2}) ^ {n}} \ln (1 + x) \mathrm{d} x = \int_ {0} ^ {+ \infty} \frac {n \cos \frac {x ^ {2}}{n ^ {2}}}{\left(1 + \frac {x}{n} + \frac {2 x ^ {2}}{n ^ {2}}\right) ^ {n}} \ln \left(1 + \frac {x}{n}\right) \mathrm{d} x.
$$

当 $n \geqslant 4$ 时, 有

$$
\left| \frac {n \cos \frac {x ^ {2}}{n ^ {2}}}{\left(1 + \frac {x}{n} + \frac {2 x ^ {2}}{n ^ {2}}\right) ^ {n}} \ln \left(1 + \frac {x}{n}\right) \right| \leqslant \frac {x}{1 + \mathrm{C} _ {n} ^ {3} \frac {x ^ {3}}{n ^ {3}}} \leqslant \frac {x}{1 + \frac {x ^ {3}}{2 4}}, \quad \forall x \in [ 0, + \infty).
$$

而

$$
\lim _ {n \to + \infty} \frac {n \cos \frac {x ^ {2}}{n ^ {2}}}{\left(1 + \frac {x}{n} + \frac {2 x ^ {2}}{n ^ {2}}\right) ^ {n}} \ln \left(1 + \frac {x}{n}\right) = \frac {x}{\mathrm{e} ^ {x}}, \qquad \forall   x \in [ 0, + \infty).
$$

于是，由控制收敛定理得到

$$
\lim _ {n \to + \infty} n ^ {2} \int_ {0} ^ {+ \infty} \frac {\cos x ^ {2}}{(1 + x + 2 x ^ {2}) ^ {n}} \ln (1 + x) \mathrm{d} x = \int_ {0} ^ {+ \infty} x \mathrm{e} ^ {- x} \mathrm{d} x = 1.
$$

利用含参变量积分的性质计算积分是一种常用的方法. 计算的常规方法是首先引入恰当的参数. 在此基础上, 通常的方法是以下三类: 利用积分交换次序, 先积分后求导, 或先求导再积分 (包含求导后得到微分方程).

例 20.3.3 设 a, b > 0, 计算  $\int_{0}^{1}\frac{x^{b}-x^{a}}{\ln x}dx$ .

解 事实上, 所求积分为常义积分. 我们用两种方法计算.

解法1 注意到 $x^{y}$ 在 $[0,1] \times [a,b]$ 上连续，从而根据二重积分化为累次积分的定理16.3.1,或根据定理20.1.7,我们有

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {x ^ {b} - x ^ {a}}{\ln x} \mathrm{d} x = \int_ {0} ^ {1} \mathrm{d} x \int_ {a} ^ {b} x ^ {y} \mathrm{d} y = \int_ {a} ^ {b} \mathrm{d} y \int_ {0} ^ {1} x ^ {y} \mathrm{d} x \\ = \int_ {a} ^ {b} \frac {1}{y + 1} \mathrm{d} y = \ln \frac {b + 1}{a + 1}. \\ \end{array}
$$

解法 2 固定 a > 0, 记

$$
F (b) = \int_ {0} ^ {1} \frac {x ^ {b} - x ^ {a}}{\ln x} \mathrm{d} x, \qquad b \geqslant a.
$$

则由定理 20.1.6,

$$
F ^ {\prime} (b) = \int_ {0} ^ {1} x ^ {b} \mathrm{d} x = \frac {1}{b + 1}.
$$

于是

$$
F (b) = \ln (b + 1) + C, \quad \forall b \geqslant a.
$$

注意到 $F(a) = 0$ ，得到

$$
F (b) = \ln \frac {b + 1}{a + 1}.
$$

□

不难看到, 在本例中, 这两种方法并无本质区别.

例 20.3.4 计算 Dirichlet 积分  $\int_{0}^{+\infty}\frac{\sin x}{x}dx$ .

解 考虑含参变量积分

$$
f (\alpha) = \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- \alpha x} \frac {\sin x}{x} \mathrm{d} x, \qquad \forall \alpha \geqslant 0.
$$

由于 $\int_0^{+\infty}\mathrm{e}^{-\alpha x}\frac{\sin x}{x}\mathrm{d}x$ 关于 $\alpha \in [0, + \infty)$ 一致收敛，从而由定理20.3.3可得 $f$ 在$[0, + \infty)$ 上连续.

另一方面, 上述积分形式求导后的积分 $\int_{0}^{+\infty}\mathrm{e}^{-\alpha x}\sin x\mathrm{d}x$ 关于 $\alpha \in (0, + \infty)$ 内闭一致收敛, 从而由定理20.3.4可得

$$
f ^ {\prime} (\alpha) = - \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- \alpha x} \sin x \mathrm{d} x = - \frac {1}{1 + \alpha^ {2}}, \quad \forall \alpha > 0.
$$

两边求积分得到

$$
f (\alpha) = - \arctan \alpha + C, \quad \forall \alpha > 0.
$$

由 $f$ 在 $[0, +\infty)$ 上的连续性, 得到

$$
f (\alpha) = - \arctan \alpha + C, \quad \forall \alpha \geqslant 0.
$$

而由控制收敛定理，

$$
\lim _ {\alpha \to + \infty} f (\alpha) = 0.
$$

从而 $C = \frac{\pi}{2}$ .由此即得

$$
f (\alpha) = \frac {\pi}{2} - \arctan \alpha , \qquad \forall \alpha \geqslant 0.
$$

特别地，

$$
\int_ {0} ^ {+ \infty} \frac {\sin x}{x} \mathrm{d} x = f (0) = \frac {\pi}{2}.
$$

例20.3.5 设 $\alpha \in (-\infty, +\infty)$, 计算 $\int_0^\pi \ln (1 - 2\alpha \cos x + \alpha^2) \, \mathrm{d}x$.

解 在 (13.5.3) 式中, 我们利用幂级数的性质计算过这一积分. 现在我们利用积分的性质来计算. 在例 20.2.4, 我们证明了对任何 $A > 0$, 积分 $\int_{0}^{\pi} \ln(1 - 2\alpha \cos x + \alpha^{2}) \, \mathrm{d}x$ 关于 $\alpha \in [-A, A]$ 一致收敛. 因此,

$$
F (\alpha) := \int_ {0} ^ {\pi} \ln (1 - 2 \alpha \cos x + \alpha^ {2}) \mathrm{d} x
$$

在 R 上连续.

解法1 对 $\int_0^\pi \ln (1 - 2\alpha \cos x + \alpha^2)\mathrm{d}x$ 形式求导, 得到积分 $\int_0^\pi \frac{2\alpha - 2\cos x}{1 - 2\alpha\cos x + \alpha^2}\mathrm{d}x.$ 该积分对于任何固定的 $\alpha \in \mathbb{R}$, 都是常义积分. 但作为含参变量积分, $\forall \delta \in (0,1)$ 以及 $A > 1$, 我们有

$$
\sup _ {x \in (0, \delta), \frac {1}{A} \leqslant \alpha \leqslant A} \left| \frac {2 \alpha - 2 \cos x}{1 - 2 \alpha \cos x + \alpha^ {2}} \right| \geqslant \sup _ {\frac {1}{A} \leqslant \alpha \leqslant A} \left| \frac {2 \alpha - 2}{1 - 2 \alpha + \alpha^ {2}} \right| = + \infty .
$$

因此, $x = 0$ 是含参变量积分 $\int_0^\pi \frac{2\alpha - 2\cos x}{1 - 2\alpha\cos x + \alpha^2}\mathrm{d}x\left(\frac{1}{A}\leqslant \alpha \leqslant A\right)$ 的一个瑕点.同理, $x = \pi$ 是含参变量积分 $\int_0^\pi \frac{2\alpha - 2\cos x}{1 - 2\alpha\cos x + \alpha^2}\mathrm{d}x\left(-A\leqslant \alpha \leqslant -\frac{1}{A}\right)$ 的一个瑕点.进一步,

$$
\begin{array}{l} \sup _ {\frac {1}{A} \leqslant \alpha \leqslant A} \left| \int_ {0} ^ {\delta} \frac {2 \alpha - 2 \cos x}{1 - 2 \alpha \cos x + \alpha^ {2}} \mathrm{d} x \right| \geqslant \sup _ {1 <   \alpha \leqslant A} \int_ {0} ^ {\delta} \frac {2 \alpha - 2 \cos x}{1 - 2 \alpha \cos x + \alpha^ {2}} \mathrm{d} x \\ = \sup _ {1 <   \alpha \leqslant A} \int_ {0} ^ {\delta} \frac {1}{\alpha} \left(1 + \frac {\alpha^ {2} - 1}{1 - 2 \alpha \cos x + \alpha^ {2}}\right) \mathrm{d} x \\ \end{array}
$$

$$
\begin{array}{l} \geqslant \varlimsup_ {n \rightarrow + \infty} \sup _ {1 <   \alpha \leqslant A} \int_ {0} ^ {\frac {1}{n}} \frac {\alpha - 1}{1 - 2 \alpha \cos x + \alpha^ {2}} \mathrm{d} x \\ \geqslant \lim _ {n \to + \infty} \frac {1}{n ^ {2}} \frac {1}{1 - 2 \left(1 + \frac {1}{n}\right) \cos \frac {1}{n} + \left(1 + \frac {1}{n}\right) ^ {2}} = \frac {1}{2}. \\ \end{array}
$$

因此, $\int_0^\pi \frac{2\alpha - 2\cos x}{1 - 2\alpha\cos x + \alpha^2}\mathrm{d}x$ 关于 $\frac{1}{A}\leqslant \alpha \leqslant A$ 非一致收敛. 这样, 我们不能期望直接通过定理20.3.4得到 $F$ 在1处的可微性. 或即使 $F$ 在1处可微, 也不见得在该处求导和积分可以交换次序①.

另一方面, 任取 $\eta \in (0,1)$, 易见 $\frac{2\alpha - 2\cos x}{1 - 2\alpha\cos x + \alpha^2}$ 在 $(x, \alpha) \in [0, \pi] \times (\mathbb{R} \setminus (1 - \eta, 1 + \eta) \setminus (-1 - \eta, -1 + \eta)$ 上连续. 因此, $F$ 在 $\pm 1$ 之外的点处可微, 且

$$
\begin{array}{l} F ^ {\prime} (\alpha) = \int_ {0} ^ {\pi} \frac {2 \alpha - 2 \cos x}{1 - 2 \alpha \cos x + \alpha^ {2}} \mathrm{d} x = \int_ {0} ^ {+ \infty} \frac {2 \alpha - 2 \frac {1 - t ^ {2}}{1 + t ^ {2}}}{1 - 2 \alpha \frac {1 - t ^ {2}}{1 + t ^ {2}} + \alpha^ {2}} \frac {2}{1 + t ^ {2}} \mathrm{d} t \\ = \int_ {0} ^ {+ \infty} \frac {\alpha - 1 + (\alpha + 1) t ^ {2}}{(\alpha - 1) ^ {2} + (\alpha + 1) ^ {2} t ^ {2}} \frac {4}{1 + t ^ {2}} \mathrm{d} t \\ = \frac {2}{\alpha} \int_ {0} ^ {+ \infty} \left[ \frac {\alpha^ {2} - 1}{(\alpha - 1) ^ {2} + (\alpha + 1) ^ {2} t ^ {2}} + \frac {1}{1 + t ^ {2}} \right] \mathrm{d} t \\ = \frac {2}{\alpha} \left(\arctan \frac {\alpha + 1}{\alpha - 1} t + \arctan t\right) \Big | _ {0} ^ {+ \infty} \\ = \left\{ \begin{array}{l l} \frac {2 \pi}{\alpha}, & \alpha > 1, \\ 0, & \alpha \in (0, 1). \end{array} \right. \\ \end{array}
$$

结合  $F(0)=0$  以及 F 为连续的偶函数, 得到

$$
F (\alpha) = \left\{ \begin{array}{l l} 2 \pi \ln | \alpha |, & | \alpha | > 1, \\ 0, & | \alpha | \leqslant 1. \end{array} \right.
$$

解法 2 接下来, 我们利用对称性来计算这一积分. 我们有

$$
\begin{array}{l} F (\alpha) = F (- \alpha) = \frac {1}{2} (F (\alpha) + F (- \alpha)) \\ = \frac {1}{2} \int_ {0} ^ {\pi} \ln \left((1 + \alpha^ {2}) ^ {2} - 4 \alpha^ {2} \cos^ {2} x\right) \mathrm{d} x \\ = \frac {1}{2} \int_ {0} ^ {\pi} \ln \left((1 + \alpha^ {2}) ^ {2} - 2 \alpha^ {2} \cos 2 x - 2 \alpha^ {2}\right) \mathrm{d} x \\ = \frac {1}{4} \int_ {0} ^ {2 \pi} \ln (1 + \alpha^ {4} - 2 \alpha^ {2} \cos x) \mathrm{d} x \\ \end{array}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 从最后的结果可以看到, F 在 ±1 处均不可微, 但左、右导数均存在.</span></small>

$$
\begin{array}{l} = \frac {1}{2} \int_ {0} ^ {\pi} \ln (1 + \alpha^ {4} - 2 \alpha^ {2} \cos x) \mathrm{d} x \\ = \frac {1}{2} F (\alpha^ {2}). \\ \end{array}
$$

由此立即得到  $F(\pm1)=0$  。而反复运用上式则可得

$$
F (\alpha) = \frac {1}{2 ^ {n}} F (\alpha^ {2 ^ {n}}), \qquad \forall | \alpha | <   1, n \geqslant 1.
$$

于是利用 $F$ 的连续性得到

$$
F (\alpha) = \lim _ {n \to + \infty} \frac {1}{2 ^ {n}} F (\alpha^ {2 ^ {n}}) = 0 \cdot F (0) = 0, \quad \forall | \alpha | <   1.
$$

最后, 结合  $F\left(\frac{1}{\alpha}\right) = -2\pi \ln |\alpha| + F(\alpha)$  可得

$$
F (\alpha) = \left\{ \begin{array}{l l} 2 \pi \ln | \alpha |, & | \alpha | > 1, \\ 0, & | \alpha | \leqslant 1. \end{array} \right.
$$

例 20.3.6 计算 Fresnel $^{①}$ 积分  $\int_{0}^{+\infty}\sin x^{2}dx$ .

解 首先, 我们有

$$
\int_ {0} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2} x} \mathrm{d} t = \frac {1}{\sqrt {x}} \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t = \frac {\sqrt {\pi}}{2 \sqrt {x}}, \quad \forall x > 0.
$$

因此，

$$
\begin{array}{l} \int_ {0} ^ {+ \infty} \sin x ^ {2} \mathrm{d} x = \int_ {0} ^ {+ \infty} \frac {\sin x}{2 \sqrt {x}} \mathrm{d} x \\ = \frac {1}{\sqrt {\pi}} \int_ {0} ^ {+ \infty} \mathrm{d} x \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2} x} \sin x \mathrm{d} t. \\ \end{array}
$$

易得

$$
\begin{array}{l} \int_ {0} ^ {+ \infty} \mathrm{d} t \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2} x} \sin x \mathrm{d} x = \int_ {0} ^ {+ \infty} \frac {1}{1 + t ^ {4}} \mathrm{d} t = \int_ {1} ^ {+ \infty} \frac {1 + t ^ {2}}{1 + t ^ {4}} \mathrm{d} t \\ = \frac {1}{\sqrt {2}} \arctan \left. \frac {t - t ^ {- 1}}{\sqrt {2}} \right| _ {1} ^ {+ \infty} = \frac {\pi}{2 \sqrt {2}}. \\ \end{array}
$$

为了说明第一式的累次积分可以交换次序, 我们需要利用本例积分的特殊性. 任取 $A > \varepsilon > 0$, 由 Weierstrass 判别法, 含参变量积分 $\int_{0}^{+\infty} \mathrm{e}^{-t^2 x} \sin x \, \mathrm{d}t$ 关于 $x \in [\varepsilon, A]$ 一致收敛, 因此,

$$
\left| \int_ {\varepsilon} ^ {A} \mathrm{d} x \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2} x} \sin x \mathrm{d} t - \int_ {0} ^ {+ \infty} \mathrm{d} t \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2} x} \sin x \mathrm{d} x \right|
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Fresnel, Augustin-Jean, 1788 年 5 月 10 日—1827 年 7 月 14 日, 法国物理学家和铁路工程师.</span></small>

$$
\begin{array}{l} = \left| \int_ {0} ^ {+ \infty} \mathrm{d} t \int_ {\varepsilon} ^ {A} \mathrm{e} ^ {- t ^ {2} x} \sin x \mathrm{d} x - \int_ {0} ^ {+ \infty} \mathrm{d} t \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2} x} \sin x \mathrm{d} x \right| \\ \leqslant \int_ {0} ^ {+ \infty} \left(\left| \int_ {A} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2} x} \sin x \mathrm{d} x \right| + \left| \int_ {0} ^ {\varepsilon} \mathrm{e} ^ {- t ^ {2} x} \sin x \mathrm{d} x \right|\right) \mathrm{d} t \\ = \int_ {0} ^ {+ \infty} \frac {\left| t ^ {2} \mathrm{e} ^ {- t ^ {2} A} \sin A + \mathrm{e} ^ {- t ^ {2} A} \cos A \right| + \left| - t ^ {2} \mathrm{e} ^ {- t ^ {2} \varepsilon} \sin \varepsilon + 1 - \mathrm{e} ^ {- t ^ {2} \varepsilon} \cos \varepsilon \right|}{t ^ {4} + 1} \mathrm{d} t \\ \leqslant \int_ {0} ^ {+ \infty} \left(\mathrm{e} ^ {- t ^ {2} A} + | \sin \varepsilon | + | 1 - \mathrm{e} ^ {- t ^ {2} \varepsilon} \cos \varepsilon |\right) \frac {t ^ {2} + 1}{t ^ {4} + 1} \mathrm{d} t. \\ \end{array}
$$

上式中令 $A\to +\infty ,\varepsilon \to 0^{+}$ ，由控制收敛定理，即得

$$
\int_ {0} ^ {+ \infty} \mathrm{d} x \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2} x} \sin x \mathrm{d} t = \int_ {0} ^ {+ \infty} \mathrm{d} t \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2} x} \sin x \mathrm{d} x.
$$

最后得到

$$
\int_ {0} ^ {+ \infty} \sin x ^ {2} \mathrm{d} x = \frac {\sqrt {2 \pi}}{4}.
$$

□

## 习题 20.3

1. 对应于定理 20.3.4, 给出并证明含参变量无穷积分被积函数关于参数仅在单点可微时的结果.

2. 对应于定理 20.3.4, 给出可能含有瑕点的含参变量积分可微性的结果并证明.

3. 证明 $\int_{0}^{\pi}\frac{\sin x}{x^{\alpha}(\pi - x)^{2 - \alpha}}\mathrm{d}x$ 是(0,2)区间内关于 $\alpha$ 的无界、连续函数.

4. 计算  $\lim_{n\to+\infty}\int_{0}^{2}\frac{x^{n}\ln x}{1+x^{n}}\mathrm{d}x$ ，并说明计算过程合理.

5. 设 a, b > 0, 利用 Frullani 积分计算  $\int_{0}^{1}\frac{x^{b}-x^{a}}{\ln x}dx$ .

6. 考察以下积分与例 20.3.5 的联系, 并尝试以各种方法计算这些积分:

(1) $\int_{0}^{\frac{\pi}{2}}\ln (a^{2} - \sin^{2}x)\mathrm{d}x,\quad a\geqslant 1;$
(2) $\int_0^\pi \ln (1 + a\cos x)\mathrm{d}x,\quad |a|\leqslant 1;$
(3) $\int_{0}^{\pi}\ln (a^{2}\cos^{2}x + b^{2}\sin^{2}x)\mathrm{d}x,\quad a^{2} + b^{2} > 0.$

7. 证明 $\lim_{\alpha \to +\infty} \int_{0}^{+\infty} \frac{\sin x}{x\sqrt{x}} \mathrm{e}^{-\alpha x} \, \mathrm{d}x = 0.$

8. 计算  $\lim_{n\to+\infty}\int_{0}^{1}\frac{\cos(\pi x)-\mathrm{e}^{-n^{2}x^{2}}}{n\arcsin x}\frac{\mathrm{d}x}{\ln(1+x)}$ ，并说明计算过程成立的理由.

9. 计算  $\lim_{n\to+\infty}\sqrt{n}\int_{0}^{+\infty}\frac{\cos x}{(1+x^{2})^{n}}\mathrm{d}x,$  并说明计算过程的正确性.

10. 证明或否定: $\lim_{n\to +\infty}\int_{0}^{\pi}\mathrm{e}^{xt}\left[\frac{\cos\left(n + \frac{1}{2}\right)t}{\ln(1 + t)} -\frac{\cos nt}{t}\right]\mathrm{d}t$ 关于 $x\in [0,1]$ 一致收敛于零.

11. 设 $f$ 是 $[0,1)$ 上的连续可微函数, $f(0) = 0, f' \in L^2(0,1)$. 证明: $\int_0^1 \frac{|f(x)|^2}{x^2} \mathrm{d}x \leqslant 4\int_0^1 |f'(x)|^2 \mathrm{d}x$.

12. 设 $f$ 为以 $\pi$ 为周期且在 $[0, \pi]$ 上绝对可积的偶函数. 证明:

(1) $\int_{0}^{+\infty} f(x) \frac{\sin x}{x} \, \mathrm{d}x = \int_{0}^{\frac{\pi}{2}} f(x) \, \mathrm{d}x;$
(2) $\int_{0}^{+\infty} f(x) \left( \frac{\sin x}{x} \right)^{2} \, \mathrm{d}x = \int_{0}^{\frac{\pi}{2}} f(x) \, \mathrm{d}x.$

13. 设 $f$ 为以 $2\pi$ 为周期在 $[0, 2\pi]$ 上绝对可积的偶函数. 证明:

$$
\int_ {0} ^ {+ \infty} f (x) \frac {\sin x}{x} \mathrm{d} x = \frac {1}{2} \int_ {0} ^ {\pi} f (x) (1 + \cos x) \mathrm{d} x.
$$

14. 证明公式 $\int_0^1\frac{1}{x^x}\mathrm{d}x = \sum_{n = 1}^{\infty}\frac{1}{n^n}.$

15. 试利用 $\frac{1}{2} + \sum_{k=1}^{n} \cos kx = \frac{\sin\left(n + \frac{1}{2}\right)x}{2\sin\frac{x}{2}}$ 证明:

$$
\frac {\pi}{2} = \lim _ {n \to + \infty} \int_ {0} ^ {\pi} \frac {\sin \left(n + \frac {1}{2}\right) x}{2 \sin \frac {x}{2}} \mathrm{d} x = \lim _ {n \to + \infty} \int_ {0} ^ {\pi} \frac {\sin \left(n + \frac {1}{2}\right) x}{x} \mathrm{d} x = \int_ {0} ^ {+ \infty} \frac {\sin x}{x} \mathrm{d} x.
$$

16. 设 $a > 0$, 求 $n \to +\infty$ 时 $\int_{n\pi}^{(n+1)\pi} \frac{x}{1 + x^a \sin^2 x} \, \mathrm{d}x$ 的阶.

17. 计算  $\int_{0}^{+\infty}\frac{(1-x^{2})\arctan x^{2}}{x^{4}+4x^{2}+1}\mathrm{d}x.$

18. 设 $a \in [0,1]$, 计算 $\int_{0}^{\frac{\pi}{2}} \ln |a^{2} - \sin^{2} x| \, \mathrm{d}x$.

19. 在例 20.3.1 中, 当  $(x,y)\rightarrow\infty$  时,  $f(x,y)\nrightarrow0$ . 试考虑如下问题:

(1) 设 $\{a_{n}\}, \{b_{n}\}$ 是两个收敛于零的数列,

$$
f (x, y) := \left\{ \begin{array}{l l} a _ {n}, & (x, y) \in [ n, n + 1) \times [ n, n + 1), n \geqslant 0, \\ b _ {n}, & (x, y) \in [ n, n + 1) \times [ n + 1, n + 2), n \geqslant 0, \\ 0, & \text {其他} \end{array} \right.
$$

使得 $\int_0^{+\infty}\mathrm{d}y\int_0^{+\infty}f(x,y)\mathrm{d}x$ 与 $\int_0^{+\infty}\mathrm{d}x\int_0^{+\infty}f(x,y)\mathrm{d}y$ 均收敛.证明:

$$
\int_ {0} ^ {+ \infty} \mathrm{d} y \int_ {0} ^ {+ \infty} f (x, y) \mathrm{d} x = \int_ {0} ^ {+ \infty} \mathrm{d} x \int_ {0} ^ {+ \infty} f (x, y) \mathrm{d} y.
$$

(2) 构造 $f: [0, +\infty) \times [0, +\infty) \to \mathbb{R}$ 使得 $\lim_{(x,y) \to \infty} f(x,y) = 0$，且 $\int_0^{+\infty} \mathrm{d}y \int_0^{+\infty} f(x,y) \, \mathrm{d}x$ 与 $\int_0^{+\infty} \mathrm{d}x \int_0^{+\infty} f(x,y) \, \mathrm{d}y$ 均收敛但不相等.

20. 设 $p > 1, f \in \mathcal{R}^p(0, +\infty)$ 且 $f$ 非负①. 证明 Hardy② 不等式:

$$
\int_ {0} ^ {+ \infty} \left(\frac {1}{x} \int_ {0} ^ {x} f (t) \mathrm{d} t\right) ^ {p} \mathrm{d} x \leqslant \left(\frac {p}{p - 1}\right) ^ {p} \int_ {0} ^ {+ \infty} f ^ {p} (x) \mathrm{d} x,
$$

其中 $\left(\frac{p}{p - 1}\right)^{p}$ 为最佳常数, 且等号成立当且仅当 $\int_0^{+\infty}f(x)\mathrm{d}x = 0.$

21. 设 $p > 1, f \in \mathcal{R}^p(0, +\infty)$ 且 $f$ 非负. 又设 $r > 0, r \neq 1$. 证明 Hardy 不等式的推广:

若 $r > 1$ ，则

$$
\int_ {0} ^ {+ \infty} x ^ {- r} \left(\int_ {0} ^ {x} f (t) \mathrm{d} t\right) ^ {p} \mathrm{d} x \leqslant \left(\frac {p}{r - 1}\right) ^ {p} \int_ {0} ^ {+ \infty} x ^ {p - r} f ^ {p} (x) \mathrm{d} x;
$$

若 $0 < r < 1$ ，则

$$
\int_ {0} ^ {+ \infty} x ^ {- r} \left(\int_ {x} ^ {+ \infty} f (t) \mathrm{d} t\right) ^ {p} \mathrm{d} x \leqslant \left(\frac {p}{1 - r}\right) ^ {p} \int_ {0} ^ {+ \infty} x ^ {p - r} f ^ {p} (x) \mathrm{d} x.
$$

22. 设 $p, q > 1$ 为对偶数, $f \in \mathcal{R}^q(0, +\infty)$ 且 $f$ 非负. 令 $F(f)(x) := \int_{x}^{+\infty} \frac{f(t)}{t} \, \mathrm{d}t$. 利用 Hardy 不等式以及对偶关系证明: $\|F(f)\|_{\mathcal{R}^q(0, +\infty)} \leqslant \frac{p}{p-1} \|f\|_{\mathcal{R}^q(0, +\infty)}$.

## 20.4 Euler 积分

在一些具体积分的计算中, 时常会涉及两类重要的 Euler 积分——Γ (Gamma) 函数与 B (Beta) 函数.

Γ 函数的定义 首先, 引入 Γ 函数. 称函数

$$
\Gamma (s) := \int_ {0} ^ {+ \infty} x ^ {s - 1} \mathrm{e} ^ {- x} \mathrm{d} x, \quad s > 0 \tag {20.4.1}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">①  $R^{p}$  与  $\|\cdot\|_{R^{p}}$  等记号的含义, 请参看第二十一章 21.1 节.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Hardy, Godfrey Harold, 1877 年 2 月 7 日 — 1947 年 12 月 1 日, 英国数学家.</span></small>

为  $\Gamma$  函数, 又称为第二类 Euler 积分.

易见对于任何整数 $k \geqslant 0$, 积分 $\int_{0}^{+\infty} x^{s-1} \mathrm{e}^{-x} \ln^{k} x \, \mathrm{d}x$ 关于 $s \in (0, +\infty)$ 内闭一致收敛, 因此, $\Gamma$ 在 $(0, +\infty)$ 中有任意阶的导数, 且可以积分号下求导.

$\Gamma$ 函数的递推公式 利用分部积分立即得到

$$
\Gamma (s + 1) = s \Gamma (s), \qquad \forall s > 0. \tag {20.4.2}
$$

特别地, 结合  $\Gamma(1)=1$  可得

$$
\Gamma (n + 1) = n!, \qquad \forall   n = 0, 1, \dots . \tag {20.4.3}
$$

利用 (20.4.2) 式, 还可以把 $\Gamma$ 函数的定义域扩大到除了 0 和负整数以外的所有实数.

log-凸性 由 Hölder 不等式, 立即可得 $\Gamma$ 是严格 log-凸的, 即 $\ln \Gamma$ 是严格凸函数:

$$
\begin{array}{l} \Gamma (\alpha x + (1 - \alpha) y) = \int_ {0} ^ {+ \infty} t ^ {\alpha x + (1 - \alpha) y - 1} \mathrm{e} ^ {- t} \mathrm{d} t \\ <   \left(\int_ {0} ^ {+ \infty} t ^ {x - 1} \mathrm{e} ^ {- t} \mathrm{d} t\right) ^ {\alpha} \left(\int_ {0} ^ {+ \infty} t ^ {y - 1} \mathrm{e} ^ {- t} \mathrm{d} t\right) ^ {1 - \alpha} \\ = \Gamma (x) ^ {\alpha} \Gamma (y) ^ {1 - \alpha}, \quad \forall \alpha \in (0, 1), x > y > 0. \tag {20.4.4} \\ \end{array}
$$

自然, 也可以利用

$$
(\ln \Gamma (x)) ^ {\prime \prime} > 0, \quad \forall x > 0. \tag {20.4.5}
$$

利用 log-凸性, 我们有

$$
\left\{ \begin{array}{l l} \Gamma (x + s) \leqslant \Gamma (x) ^ {1 - s} \Gamma (x + 1) ^ {s}, \\ \Gamma (x + 1) \leqslant \Gamma (x + s) ^ {s} \Gamma (x + s + 1) ^ {1 - s}, \end{array} \right. \quad \forall x > 0, s \in [ 0, 1 ]. \tag {20.4.6}
$$

结合递推公式得到

$$
\left(\frac {x}{x + s}\right) ^ {1 - s} \leqslant \frac {\Gamma (x + s)}{\Gamma (x) x ^ {s}} \leqslant 1, \quad \forall x > 0, s \in [ 0, 1 ]. \tag {20.4.7}
$$

因此

$$
\lim _ {x \to + \infty} \frac {\Gamma (x + s)}{\Gamma (x) x ^ {s}} = 1 \tag {20.4.8}
$$

对 $s \in [0,1]$ 成立, 进一步, 利用递推公式 (20.4.2) 可得对任何 $s \in \mathbb{R}$, (20.4.8) 式均成立. 注意到

$$
\Gamma (x + s) = \int_ {0} ^ {+ \infty} t ^ {x + s - 1} \mathrm{e} ^ {- t} \mathrm{d} t = x ^ {x + s} \int_ {0} ^ {+ \infty} t ^ {s - 1} \left(t \mathrm{e} ^ {- t}\right) ^ {x} \mathrm{d} t, \qquad x > 0,   x + s > 0,
$$

我们也可以利用 $te^{-t}$ 在 $(0, +\infty)$ 上恒正且最大值仅在 $t = 1$ 处取得，得到(20.4.8)式:

$$
\lim _ {x \to + \infty} \frac {\Gamma (x + s)}{\Gamma (x) x ^ {s}} = \lim _ {x \to + \infty} \frac {\int_ {0} ^ {+ \infty} t ^ {s - 1} \left(t \mathrm{e} ^ {- t}\right) ^ {x} \mathrm{d} t}{\int_ {0} ^ {+ \infty} t ^ {- 1} \left(t \mathrm{e} ^ {- t}\right) ^ {x} \mathrm{d} t} = 1. \tag {20.4.9}
$$

$\Gamma$ 函数在0点附近的阶利用 $\Gamma$ 函数的递推公式以及在1处的连续性可得

$$
\lim _ {s \to 0 ^ {+}} s \Gamma (s) = \lim _ {s \to 0 ^ {+}} \Gamma (s + 1) = \Gamma (1) = 1,
$$

从而得到  $\Gamma$  函数在 0 点附近的阶:

$$
\Gamma (s) \sim \frac {1}{s}, \qquad s \to 0 ^ {+}. \tag {20.4.10}
$$

Stirling 公式, $\Gamma$ 函数在无穷远处的阶 $\Gamma$ 函数在正无穷远处, 有如下的 Stirling$^{①}$公式:

$$
\Gamma (s + 1) \sim \left(\frac {s}{\mathrm{e}}\right) ^ {s} \sqrt {2 \pi s}, \quad s \rightarrow + \infty . \tag {20.4.11}
$$

证明 对于 $s > 0$ ，依次作变量代换 $t = s(x + 1), x = \frac{y}{\sqrt{s}}$ ，可得

$$
\begin{array}{l} \Gamma (s + 1) = \int_ {0} ^ {+ \infty} t ^ {s} \mathrm{e} ^ {- t} \mathrm{d} t = \frac {s ^ {s + 1}}{\mathrm{e} ^ {s}} \int_ {- 1} ^ {+ \infty} \mathrm{e} ^ {- s (x - \ln (1 + x))} \mathrm{d} x \\ = \frac {s ^ {s} \sqrt {s}}{\mathrm{e} ^ {s}} \int_ {- \sqrt {s}} ^ {+ \infty} \mathrm{e} ^ {- s g (\frac {y}{\sqrt {s}})} \mathrm{d} y, \\ \end{array}
$$

其中

$$
g (x) := x - \ln (1 + x), \quad \forall x \in (- 1, + \infty).
$$

易见 g 在  $(-1, +\infty)$  上非负，且  $g(x) = 0$  当且仅当 x = 0.

另一方面， $\lim_{x\to -1^{+}}\frac{g(x)(|x| + 1)}{x^{2}} = +\infty ,\lim_{x\to 0}\frac{g(x)(|x| + 1)}{x^{2}} = \frac{1}{2},$ 而 $\lim_{x\to +\infty}\frac{g(x)(|x| + 1)}{x^2} =$ 1.由此可得存在常数 $c > 0$ 使得

$$
g (x) \geqslant \frac {c x ^ {2}}{| x | + 1}, \quad \forall   x \in (- 1, + \infty).
$$

特别地, 对于 $s > 1$, 有

$$
s g \left(\frac {y}{\sqrt {s}}\right) \geqslant \frac {c y ^ {2}}{\frac {| y |}{\sqrt {s}} + 1} \geqslant \frac {c y ^ {2}}{| y | + 1}, \quad \forall y \in (- \sqrt {s}, + \infty).
$$

这样，由控制收敛定理得到

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Stirling, James, 1692 年 5 月—1770 年 12 月 5 日, 苏格兰数学家.</span></small>

$$
\begin{array}{l} \lim _ {s \to + \infty} \frac {e ^ {s}}{s ^ {s} \sqrt {s}} \Gamma (s + 1) = \lim _ {s \to + \infty} \int_ {- \infty} ^ {+ \infty} \mathrm{e} ^ {- s g (\frac {y}{\sqrt {s}})} \chi_ {(- \sqrt {s}, + \infty)} (y) \mathrm{d} y \\ = \int_ {- \infty} ^ {+ \infty} \mathrm{e} ^ {- \frac {y ^ {2}}{2}} \mathrm{d} y = \sqrt {2 \pi}. \\ \end{array}
$$

这就得到了Stirling公式(20.4.11).

作为特例, 我们有离散型的 Stirling 公式

$$
n! \sim \left(\frac {n}{\mathrm{e}}\right) ^ {n} \sqrt {2 \pi n}, \quad n \to + \infty . \tag {20.4.12}
$$

Euler 公式 由递推公式得到

$$
\Gamma (s) = \frac {(n - 1) !}{s (s + 1) \cdots (s + n - 1)} \frac {\Gamma (s + n)}{\Gamma (n)}, \qquad s > 0.
$$

结合 (20.4.8) 式, 我们有如下的 Euler 公式:

$$
\Gamma (s) = \lim _ {n \to + \infty} n ^ {s} \cdot \frac {(n - 1) !}{s (s + 1) \cdots (s + n - 1)}. \tag {20.4.13}
$$

时常, 也用 (20.4.13) 式来定义 $\Gamma(s)$. 相比于 (20.4.1) 式, (20.4.13) 式的适用范围更广, 它对任何不是 0 或负整数的 $s$ 都成立. 这里的 $s$ 还可以是虚数.

Gauss 叠乘定理, 倍元公式 设 $k \geqslant 2$, 则 $\forall s > 0$, 有如下的 Gauss 叠乘定理:

$$
\Gamma (s) \Gamma \left(s + \frac {1}{k}\right) \dots \Gamma \left(s + \frac {k - 1}{k}\right) = (2 \pi) ^ {\frac {k - 1}{2}} k ^ {\frac {1}{2} - k s} \Gamma (k s). \tag {20.4.14}
$$

当 k=2 时, 又称 (20.4.14) 式为 Legendre $^{①}$ 公式、倍元公式.

证明 考虑

$$
\varphi (s) := \frac {\Gamma (s) \Gamma \left(s + \frac {1}{k}\right) \cdots \Gamma \left(s + \frac {k - 1}{k}\right)}{(2 \pi) ^ {\frac {k - 1}{2}} k ^ {\frac {1}{2} - k s} \Gamma (k s)}, \quad \forall s > 0,
$$

则利用递推公式立即可得 $\varphi$ 以 $\frac{1}{k}$ 为周期. 而利用Stirling公式, 可得 $\lim_{s\to +\infty}\varphi (s) = 1.$ 从而 $\varphi \equiv 1.$ 即(20.4.14)式成立. □

Bohr-Mollerup 定理 以下的 Bohr $^{②}$ -Mollerup $^{③}$  定理表明,  $\Gamma$  函数是满足定理中三个条件的唯一解.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Legendre, Adrien-Marie, 1752 年 9 月 18 日—1833 年 1 月 10 日, 法国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Bohr, Harald August, 1887 年 4 月 22 日—1951 年 1 月 22 日, 丹麦数学家、足球运动员, 曾于 1908 年代表丹麦国家队参加夏季奥运会并获银牌.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">③ Mollerup, Johannes, 1872 年 12 月 3 日—1937 年 6 月 27 日, 丹麦数学家.</span></small>

定理 20.4.1 满足下述三个条件的函数唯一:

(1)  $\psi(x+1)=x\psi(x);$
(2)  $\ln \psi$  在  $(0, +\infty)$  上为凸函数;
(3)  $\psi(1)=1.$

证明 首先, $\Gamma$ 函数满足定理中的条件. 而把推导 (20.4.6)—(20.4.8) 式和 (20.4.13) 式时的 $\Gamma$ 函数换成 $\psi$, 即得满足定理中条件的 $\psi$ 等于 $\Gamma$ 函数. □

Euler 余元公式 我们有如下重要的余元公式:

$$
\Gamma (s) \Gamma (1 - s) = \frac {\pi}{\sin s \pi}, \quad \forall s \in (0, 1). \tag {20.4.15}
$$

证明 余元公式有很多证明, 其简捷与否同 $\Gamma$ 函数采用何种方式定义有关.

对于  $s \in (0,1)$ ，由 (20.4.13) 式以及如下的 Euler 公式 (参见例 12.3.13):

$$
\sin \pi x = \pi x \prod_ {n = 1} ^ {\infty} \left(1 - \frac {x ^ {2}}{n ^ {2}}\right), \qquad \forall   x \in \mathbb {R}, \tag {20.4.16}
$$

即得余元公式.

$$
\begin{array}{l} \Gamma (s) \Gamma (1 - s) = \lim _ {n \to + \infty} \left[ n \cdot \frac {(n - 1) !}{s (s + 1) \cdots (s + n - 1)} \frac {(n - 1) !}{(1 - s) (2 - s) \cdots (n - s)} \right] \\ = \lim _ {n \to + \infty} \frac {(n !) ^ {2}}{s (1 - s ^ {2}) (2 ^ {2} - s ^ {2}) \cdots (n ^ {2} - s ^ {2})} \\ = \frac {1}{s \prod_ {n = 1} ^ {\infty} \left(1 - \frac {s ^ {2}}{n ^ {2}}\right)} = \frac {\pi}{\sin s \pi}. \\ \end{array}
$$

余元公式的其他证明可以参看 [41].

B 函数的定义 函数

$$
\mathrm{B} (p, q) := \int_ {0} ^ {1} x ^ {p - 1} (1 - x) ^ {q - 1} \mathrm{d} x, \quad \forall p, q > 0 \tag {20.4.17}
$$

称为 B 函数, 又称为第一类 Euler 积分.

易见对任何整数 $k, j \geqslant 0$, 积分 $\int_{0}^{1} x^{p-1}(1-x)^{q-1} \ln^{k} x \ln^{j}(1-x) \mathrm{~d}x$ 关于 $(p,q) \in (0,+\infty) \times (0,+\infty)$ 内闭一致收敛, 因此, $\mathrm{B}(p,q)$ 对任何 $p,q > 0$ 均有定义, 且在定义域内的各阶偏导数均连续.

B 函数和  $\Gamma$  函数的关系 B 函数与  $\Gamma$  函数有如下的关系:

$$
\mathrm{B} (p, q) = \frac {\Gamma (p) \Gamma (q)}{\Gamma (p + q)}, \quad \forall p, q > 0. \tag {20.4.18}
$$

利用这一关系式可以方便地研究 B 函数的其他性质.

为证明 (20.4.18) 式, 对  $\Gamma(p)=\int_{0}^{+\infty}t^{p-1}\mathrm{e}^{-t}\mathrm{d}t$  作变量代换  $t=x^{2}$  可得

$$
\Gamma (p) = 2 \int_ {0} ^ {+ \infty} x ^ {2 p - 1} \mathrm{e} ^ {- x ^ {2}} \mathrm{d} x.
$$

于是可得

$$
\begin{array}{l} \Gamma (p) \Gamma (q) = 4 \int_ {0} ^ {+ \infty} \mathrm{d} x \int_ {0} ^ {+ \infty} x ^ {2 p - 1} y ^ {2 q - 1} \mathrm{e} ^ {- x ^ {2} - y ^ {2}} \mathrm{d} y \\ = 4 \iint_ {\mathbb {R} _ {+} ^ {2}} x ^ {2 p - 1} y ^ {2 q - 1} \mathrm{e} ^ {- x ^ {2} - y ^ {2}} \mathrm{d} x \mathrm{d} y \\ = 4 \int_ {0} ^ {\frac {\pi}{2}} \mathrm{d} \theta \int_ {0} ^ {+ \infty} r ^ {2 p + 2 q - 1} \mathrm{e} ^ {- r ^ {2}} \cos^ {2 p - 1} \theta \sin^ {2 q - 1} \theta \mathrm{d} r \\ = 2 \Gamma (p + q) \int_ {0} ^ {\frac {\pi}{2}} \cos^ {2 p - 1} \theta \sin^ {2 q - 1} \theta \mathrm{d} \theta \\ = \mathrm{B} (p, q) \Gamma (p + q), \\ \end{array}
$$

其中最后一个等式通过变量代换  $\sin\theta=\sqrt{s}$  得到 (参见例 20.4.1).

## 利用 Euler 积分计算

例20.4.1 设 $p > -1, q > -1$，则

$$
\begin{array}{l} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {p} x \cos^ {q} x \mathrm{d} x = \int_ {0} ^ {1} t ^ {p} (1 - t ^ {2}) ^ {\frac {q - 1}{2}} \mathrm{d} t = \frac {1}{2} \int_ {0} ^ {1} s ^ {\frac {p - 1}{2}} (1 - s) ^ {\frac {q - 1}{2}} \mathrm{d} s \\ = \frac {1}{2} \mathrm{B} \left(\frac {p + 1}{2}, \frac {q + 1}{2}\right) = \frac {1}{2} \frac {\Gamma \left(\frac {p + 1}{2}\right) \Gamma \left(\frac {q + 1}{2}\right)}{\Gamma \left(\frac {p + q}{2} + 1\right)}. \\ \end{array}
$$

结合余元公式可见, 在题设条件下, 若 $p + q$ 为偶数, 则积分可以用初等函数表示出来. 作为特例, 对于 $\alpha \in (0,1)$, 我们有 $\int_{0}^{\frac{\pi}{2}}\tan^{\alpha}x\mathrm{d}x = \frac{1}{2}\Gamma \left(\frac{1 + \alpha}{2}\right)\Gamma \left(\frac{1 - \alpha}{2}\right) = \frac{\pi}{2\cos\frac{\alpha\pi}{2}}.$

例20.4.2 设 $p > -1; q, r > 0; qr > p + 1$，则作变量代换 $t = \frac{1}{1 + x^q}$ 得

$$
\begin{array}{l} \int_ {0} ^ {+ \infty} \frac {x ^ {p}}{(1 + x ^ {q}) ^ {r}} \mathrm{d} x = \int_ {0} ^ {1} \left(\frac {1}{t} - 1\right) ^ {\frac {p}{q}} t ^ {r} \left[ \frac {1}{q} \left(\frac {1}{t} - 1\right) ^ {\frac {1}{q} - 1} \frac {1}{t ^ {2}} \right] \mathrm{d} t \\ = \frac {1}{q} \int_ {0} ^ {1} \left(\frac {1}{t} - 1\right) ^ {\frac {p + 1}{q} - 1} t ^ {r - 2} \mathrm{d} t = \frac {1}{q} \int_ {0} ^ {1} (1 - t) ^ {\frac {p + 1}{q} - 1} t ^ {r - 1 - \frac {p + 1}{q}} \mathrm{d} t \\ \end{array}
$$

$$
= \frac {1}{q} \mathrm{B} \left(\frac {p + 1}{q}, r - \frac {p + 1}{q}\right) = \frac {1}{q} \frac {\Gamma \left(\frac {p + 1}{q}\right) \Gamma \left(r - \frac {p + 1}{q}\right)}{\Gamma (r)}.
$$

结合余元公式可见, 在题设条件下, 若 r 为正整数, 则积分可以用初等函数表示出来. 作为特例, 对于  $a \in (0,1)$ , 有

$$
\int_ {0} ^ {+ \infty} \frac {1}{(1 + x) x ^ {a}} \mathrm{d} x = \Gamma (a) \Gamma (1 - a) = \frac {\pi}{\sin a \pi}. \tag {20.4.19}
$$

□

例20.4.3 对于 $\alpha > 0$, 用 Euler 积分表示 $\int_{0}^{1} \frac{x^{\alpha - 1} \ln x}{1 - x} \, \mathrm{d}x$.

解 利用含参变量积分一致收敛性的性质, 以下计算过程是正确的:

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {x ^ {\alpha - 1} \ln x}{1 - x} \mathrm{d} x = \lim _ {\beta \rightarrow 1 ^ {-}} \int_ {0} ^ {1} \frac {x ^ {\alpha - 1} \ln x}{(1 - x) ^ {\beta}} \mathrm{d} x = \lim _ {\beta \rightarrow 1 ^ {-}} \frac {\partial}{\partial \alpha} \int_ {0} ^ {1} \frac {x ^ {\alpha - 1}}{(1 - x) ^ {\beta}} \mathrm{d} x \\ = \lim _ {\beta \rightarrow 1 ^ {-}} \frac {\partial}{\partial \alpha} \mathrm{B} (\alpha , 1 - \beta) = \lim _ {\beta \rightarrow 1 ^ {-}} \frac {\partial}{\partial \alpha} \frac {\Gamma (\alpha) \Gamma (1 - \beta)}{\Gamma (1 + \alpha - \beta)} \\ = \lim _ {\beta \to 1 ^ {-}} \left(\frac {\Gamma^ {\prime} (\alpha) \Gamma (1 - \beta)}{\Gamma (1 + \alpha - \beta)} - \frac {\Gamma (\alpha) \Gamma (1 - \beta) \Gamma^ {\prime} (1 + \alpha - \beta)}{\Gamma^ {2} (1 + \alpha - \beta)}\right) \\ = \lim _ {\beta \to 1 ^ {-}} \frac {\Gamma^ {\prime} (\alpha) \Gamma (1 + \alpha - \beta) - \Gamma (\alpha) \Gamma^ {\prime} (1 + \alpha - \beta)}{1 - \beta} \frac {\Gamma (2 - \beta)}{\Gamma^ {2} (1 + \alpha - \beta)} \\ = \lim _ {\beta \rightarrow 1 ^ {-}} \left(\Gamma^ {\prime} (\alpha) \Gamma^ {\prime} (1 + \alpha - \beta) - \Gamma (\alpha) \Gamma^ {\prime \prime} (1 + \alpha - \beta)\right) \frac {\Gamma (1)}{\Gamma^ {2} (\alpha)} \\ = \frac {(\Gamma^ {\prime} (\alpha)) ^ {2} - \Gamma (\alpha) \Gamma^ {\prime \prime} (\alpha)}{\Gamma^ {2} (\alpha)}. \\ \end{array}
$$

也可以这样计算:

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {x ^ {\alpha - 1} \ln x}{1 - x} \mathrm{d} x = \frac {\mathrm{d}}{\mathrm{d} \alpha} \int_ {0} ^ {1} \frac {x ^ {\alpha - 1} - 1}{1 - x} \mathrm{d} x = \frac {\mathrm{d}}{\mathrm{d} \alpha} \lim _ {\beta \rightarrow 1 ^ {-}} \int_ {0} ^ {1} \frac {x ^ {\alpha - 1} - 1}{(1 - x) ^ {\beta}} \mathrm{d} x \\ = \frac {\mathrm{d}}{\mathrm{d} \alpha} \lim _ {\beta \to 1 ^ {-}} (\mathrm{B} (\alpha , 1 - \beta) - \mathrm{B} (1, 1 - \beta)) \\ = \frac {\mathrm{d}}{\mathrm{d} \alpha} \lim _ {\beta \rightarrow 1 ^ {-}} \left(\frac {\Gamma (\alpha) \Gamma (1 - \beta)}{\Gamma (\alpha + 1 - \beta)} - \frac {\Gamma (1) \Gamma (1 - \beta)}{\Gamma (2 - \beta)}\right) \\ = \frac {\mathrm{d}}{\mathrm{d} \alpha} \lim _ {\beta \rightarrow 1 ^ {-}} \frac {\Gamma (\alpha) \Gamma (2 - \beta) - \Gamma (\alpha + 1 - \beta)}{1 - \beta} \frac {\Gamma (2 - \beta)}{\Gamma (\alpha + 1 - \beta)} \\ = \frac {\mathrm{d}}{\mathrm{d} \alpha} \lim _ {\beta \rightarrow 1 ^ {-}} \left(\Gamma (\alpha) \Gamma^ {\prime} (2 - \beta) - \Gamma^ {\prime} (\alpha + 1 - \beta)\right) \frac {1}{\Gamma (\alpha)} \\ = \frac {\mathrm{d}}{\mathrm{d} \alpha} \left(\Gamma^ {\prime} (1) - \frac {\Gamma^ {\prime} (\alpha)}{\Gamma (\alpha)}\right) \\ = - (\ln \Gamma (\alpha)) ^ {\prime \prime}. \\ \end{array}
$$

例20.4.4 计算 $\int_0^1\frac{\ln x}{1 - x}\mathrm{d}x.$

解 解法1 利用 $\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi}{6}$ 可得

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {\ln x}{1 - x} \mathrm{d} x = \int_ {0} ^ {1} \frac {\ln (1 - x)}{x} \mathrm{d} x = - \int_ {0} ^ {1} \sum_ {n = 1} ^ {\infty} \frac {x ^ {n - 1}}{n} \mathrm{d} x \\ = - \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {1} \frac {x ^ {n - 1}}{n} \mathrm{d} x = - \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2}} = - \frac {\pi^ {2}}{6}. \\ \end{array}
$$

解法 2 利用例 20.4.3 的结果, 我们有

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {\ln x}{1 - x} \mathrm{d} x = - (\ln \Gamma (\alpha)) ^ {\prime \prime} \bigg | _ {\alpha = 1} = - \frac {1}{2} (\ln \Gamma (1 + \alpha) + \ln \Gamma (1 - \alpha)) ^ {\prime \prime} \bigg | _ {\alpha = 0} \\ = - \frac {1}{2} \lim _ {\alpha \to 0} \left(\ln \frac {\alpha \pi}{\sin \alpha \pi}\right) ^ {\prime \prime} = - \frac {\pi^ {2}}{6}. \\ \end{array}
$$

例 20.4.5 设  $0 < \alpha < 1$ , 计算  $\sum_{n=1}^{\infty} \frac{1}{n^{2} - \alpha^{2}}$ .

解 解法 1 对于固定的  $\alpha \in (0,1)$ ,  $\sum_{n=1}^{\infty}\left(x^{n-\alpha-1}-x^{n+\alpha-1}\right)$  关于  $x \in [0,1]$  一致收敛, 由此可得

$$
\sum_ {n = 1} ^ {\infty} \int_ {0} ^ {1} \left(x ^ {n - \alpha - 1} - x ^ {n + \alpha - 1}\right) \mathrm{d} x = \int_ {0} ^ {1} \frac {x ^ {- \alpha} - x ^ {\alpha}}{1 - x} \mathrm{d} x.
$$

也可以利用控制收敛定理得到上式:

$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {1} \left(x ^ {n - \alpha - 1} - x ^ {n + \alpha - 1}\right) \mathrm{d} x = \lim _ {n \to + \infty} \int_ {0} ^ {1} \sum_ {k = 1} ^ {n} \left(x ^ {k - \alpha - 1} - x ^ {k + \alpha - 1}\right) \mathrm{d} x \\ = \lim _ {n \to + \infty} \int_ {0} ^ {1} \frac {(x ^ {- \alpha} - x ^ {\alpha}) (1 - x ^ {n + 1})}{1 - x} \mathrm{d} x \\ = \int_ {0} ^ {1} \frac {x ^ {- \alpha} - x ^ {\alpha}}{1 - x} \mathrm{d} x. \\ \end{array}
$$

由此利用例20.4.3的结论可得

$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2} - \alpha^ {2}} = \frac {1}{2 \alpha} \sum_ {n = 1} ^ {\infty} \left(\frac {1}{n - \alpha} - \frac {1}{n + \alpha}\right) = \frac {1}{2 \alpha} \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {1} \left(x ^ {n - \alpha - 1} - x ^ {n + \alpha - 1}\right) \mathrm{d} x \\ = \frac {1}{2 \alpha} \int_ {0} ^ {1} \frac {x ^ {- \alpha} - x ^ {\alpha}}{1 - x} \mathrm{d} x = \frac {1}{2 \alpha} \int_ {0} ^ {1} \mathrm{d} x \int_ {\alpha} ^ {- \alpha} \frac {x ^ {y} \ln x}{1 - x} \mathrm{d} y \\ = \frac {1}{2 \alpha} \int_ {\alpha} ^ {- \alpha} \mathrm{d} y \int_ {0} ^ {1} \frac {x ^ {y} \ln x}{1 - x} \mathrm{d} x \\ \end{array}
$$

$$
\begin{array}{l} = \frac {1}{2 \alpha} \int_ {- \alpha} ^ {\alpha} \frac {\mathrm{d} ^ {2}}{\mathrm{d} y ^ {2}} \ln \Gamma (1 + y) \mathrm{d} y = \frac {1}{2 \alpha} \frac {\mathrm{d}}{\mathrm{d} \alpha} (\ln \Gamma (1 + \alpha) + \ln \Gamma (1 - \alpha)) \\ = \frac {1}{2 \alpha} \frac {\mathrm{d}}{\mathrm{d} \alpha} \ln \frac {\alpha \pi}{\sin \alpha \pi} = \frac {1}{2 \alpha^ {2}} - \frac {\pi \cot (\alpha \pi)}{2 \alpha}. \tag {20.4.20} \\ \end{array}
$$

解法 2 利用 Euler 公式 (20.4.16), 我们有

$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {2} - \alpha^ {2}} = - \frac {1}{2 \alpha} \sum_ {n = 1} ^ {\infty} \left(\ln \left(1 - \frac {\alpha^ {2}}{n ^ {2}}\right)\right) ^ {\prime} = - \frac {1}{2 \alpha} \left(\sum_ {n = 1} ^ {\infty} \ln \left(1 - \frac {\alpha^ {2}}{n ^ {2}}\right)\right) ^ {\prime} \\ = - \frac {1}{2 \alpha} \left(\ln \prod_ {n = 1} ^ {\infty} \left(1 - \frac {\alpha^ {2}}{n ^ {2}}\right)\right) ^ {\prime} = - \frac {1}{2 \alpha} \left(\ln \frac {\sin \alpha \pi}{\alpha \pi}\right) ^ {\prime} = \frac {1}{2 \alpha^ {2}} - \frac {\pi \cot (\alpha \pi)}{2 \alpha}. \\ \end{array}
$$

□

通过计算  $\int_{0}^{+\infty}\frac{1}{(1+x)x^{a}}\mathrm{d}x$  得到余元公式 由例20.4.2,

$$
\int_ {0} ^ {+ \infty} \frac {1}{(1 + x) x ^ {a}} \mathrm{d} x = \Gamma (a) \Gamma (1 - a).
$$

若能够直接计算得到 $\int_0^{+\infty}\frac{1}{(1 + x)x^a}\mathrm{d}x$ 的值, 就可以给出余元公式的另一种证明. 事实上, 在例12.3.14中我们已经计算了这个积分. 我们也可以通过计算有理函数的不定积分 $\frac{x^{2m - 1 - n}}{1 + x^{2m}}$ 来计算 $\int_0^{+\infty}\frac{1}{(1 + x)x^{\frac{n}{2m}}}\mathrm{d}x$, 然后利用含参变量积分的连续性得到结果. 今后, 也可以用留数来计算它.

双  $\Gamma$  函数 定义双  $\Gamma$  函数  $\psi$  如下:

$$
\psi (x) := (\ln \Gamma (x)) ^ {\prime}, \quad \forall x > 0. \tag {20.4.21}
$$

该函数也称为  $\psi$  函数 $^{①}$ ，它具有如下性质:

(1) 利用  $\Gamma(x+1)=x\Gamma(x)$  立即得到

$$
\psi (x + 1) = \psi (x) + \frac {1}{x}, \quad x > 0. \tag {20.4.22}
$$

(2) 设 x, y > 0, 则

$$
\psi (x) - \psi (y) = \sum_ {k = 0} ^ {\infty} \left(\frac {1}{y + k} - \frac {1}{x + k}\right). \tag {20.4.23}
$$

证明 利用 (1) 可得

$$
\psi (x + 1) = \frac {1}{x} + \psi (x), \quad \forall x > 0. \tag {20.4.24}
$$

从而  $\forall n \geqslant 1,$

$$
\psi (x) - \psi (y) = \psi (x + 1) - \psi (y + 1) - \left(\frac {1}{x} - \frac {1}{y}\right) = \dots
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 另有多个函数也被称为  $\psi$  函数.</span></small>