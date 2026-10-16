# 中册 / 第十章 广义积分

原始 PDF 第 358–374 页。

## 第十章

## 广义积分

---

52

第十章 广义积分

在前一章中, 我们用极限定义了 Riemann 积分:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \lim _ {\| \mathrm{P} \| \to 0} \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i},
$$

其中 $[a, b]$ 为有界闭区间, 被积函数 $f$ 必须是有界函数. 在实际应用中, 这样的要求往往太强了. 下面我们在一定的条件下适当降低关于积分区间和被积函数的要求.

## 10.1 积分的推广

考虑平面曲线 $y = \frac{1}{x}, x \in [1, +\infty)$. 将该曲线绕 $x$ 轴旋转一周, 所得旋转体是无界的, 我们来说明它具有有限的体积. 当 $B > 1$ 时, 该旋转体介于 $x = 1$ 和 $x = B$ 的部分的体积为

$$
V _ {B} = \int_ {1} ^ {B} \pi \Big (\frac {1}{x} \Big) ^ {2} \mathrm{d} x = \pi - \frac {\pi}{B},
$$

这说明整个旋转体的体积为

$$
V = \lim _ {B \to + \infty} V _ {B} = \pi .
$$

一般地, 为了考虑无穷区间上的积分, 我们引入如下定义:

定义 10.1.1 (无穷限积分) 设 f 是定义在  $[a, +\infty)$  上的函数. 如果 f 在任何有界区间  $[a, B]$  上都是 Riemann 可积的, 且极限

$$
\lim _ {B \to + \infty} \int_ {a} ^ {B} f (x)   \mathrm{d} x
$$

存在 (且有限), 则称无穷限积分  $\int_{a}^{+\infty} f(x) \, dx$  存在或收敛, 记为

$$
\int_ {a} ^ {+ \infty} f (x)   \mathrm{d} x = \lim _ {B \to + \infty} \int_ {a} ^ {B} f (x)   \mathrm{d} x,
$$

否则就称无穷限积分 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 不存在或发散.

类似地, 我们也可以定义无穷限积分

$$
\int_ {- \infty} ^ {a} f (x)   \mathrm{d} x = \lim _ {A \to - \infty} \int_ {A} ^ {a} f (x)   \mathrm{d} x.
$$

---

10.1 积分的推广

53

设 $f$ 定义在 $\mathbb{R}$ 上, 如果存在 $a \in \mathbb{R}$, 使得 $\int_{-\infty}^{a} f(x) \mathrm{d}x$ 和 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 均收敛, 则称 $\int_{-\infty}^{+\infty} f(x) \mathrm{d}x$ 收敛, 并定义

$$
\int_ {- \infty} ^ {+ \infty} f (x) \mathrm{d} x = \int_ {- \infty} ^ {a} f (x) \mathrm{d} x + \int_ {a} ^ {+ \infty} f (x) \mathrm{d} x.
$$

利用积分关于区间的可加性质容易验证此定义与 $a$ 的选取无关. 需要注意的是, 利用极限

$$
\lim _ {A \to + \infty} \int_ {- A} ^ {A} f (x)   \mathrm{d} x
$$

也可以定义 $f$ 在 $(-\infty, +\infty)$ 上的一种积分, 称为 Cauchy 主值积分, 记为

$$
(V. P.) \int_ {- \infty} ^ {+ \infty} f (x) \mathrm{d} x = \lim _ {A \to + \infty} \int_ {- A} ^ {A} f (x) \mathrm{d} x.
$$

它和前一种定义不是等价的. 例如 $f(x) = x$ 的 Cauchy 主值积分为零, 但它在 $\mathbb{R}$ 上的无穷限积分是发散的.

从无穷限积分的定义立即得到如下的基本判别法:

(无穷限积分的 Cauchy 准则) f 在  $[a, +\infty)$  上的无穷限积分收敛当且仅当任给  $\varepsilon > 0$ ，存在  $M = M(\varepsilon)$ ，使得当 B > A > M 时，

$$
\left| \int_ {A} ^ {B} f (x) \mathrm{d} x \right| <   \varepsilon .
$$

对于 $(-∞,a]$ 和 $(-∞,+∞)$ 上的无穷限积分也有完全类似的基本判别法.

例 10.1.1 讨论无穷限积分  $\int_{1}^{+\infty}\frac{1}{x^{p}}\mathrm{d}x\left(p\in\mathbb{R}\right)$  的敛散性.

解 当 A > 1 时,

$$
\int_ {1} ^ {A} \frac {1}{x ^ {p}}   \mathrm{d} x = \left\{ \begin{array}{l l} \ln A, & p = 1, \\ \frac {1}{1 - p} (A ^ {1 - p} - 1), & p \neq 1. \end{array} \right.
$$

因此只有 $p > 1$ 时无穷限积分才是收敛的, 此时

$$
\int_ {1} ^ {+ \infty} \frac {1}{x ^ {p}} \mathrm{d} x = \lim _ {A \to + \infty} \frac {1}{1 - p} (A ^ {1 - p} - 1) = \frac {1}{p - 1}.
$$

一般地, 如果连续函数 $f$ 在 $[a, +\infty)$ 上存在原函数 $F$, 则由微积分基本定理可知

$$
\lim _ {A \to + \infty} \int_ {a} ^ {A} f (x)   \mathrm{d} x = \lim _ {A \to + \infty} F (A) - F (a),
$$

即此时无穷限积分是否收敛与极限  $\lim_{A\to+\infty}F(A)$  是否存在是一致的.

---

54

第十章 广义积分

例10.1.2 计算无穷限积分 $\int_{-\infty}^{+\infty}\frac{1}{1 + x^2}\mathrm{d}x.$

解 $\frac{1}{1 + x^2}$ 的原函数为 $\arctan x$ ，因此

$$
\begin{array}{l} \int_ {- \infty} ^ {+ \infty} \frac {1}{1 + x ^ {2}} \mathrm{d} x = \int_ {- \infty} ^ {0} \frac {1}{1 + x ^ {2}} \mathrm{d} x + \int_ {0} ^ {+ \infty} \frac {1}{1 + x ^ {2}} \mathrm{d} x \\ = \arctan x \big | _ {- \infty} ^ {0} + \arctan x \big | _ {0} ^ {+ \infty} \\ = \frac {\pi}{2} + \frac {\pi}{2} = \pi . \\ \end{array}
$$

和无穷限积分类似, 我们也可以利用极限来处理无界函数的积分.

定义 10.1.2 (瑕积分) 设函数 f 在  $(a, b]$  上有定义, 且任给  $a' \in (a, b)$ , 均有  $f \in R[a', b]$ . 如果极限

$$
\lim _ {a ^ {\prime} \to a ^ {+}} \int_ {a ^ {\prime}} ^ {b} f (x)   \mathrm{d} x
$$

存在 (且有限), 则称瑕积分 $\int_{a}^{b} f(x) \, \mathrm{d}x$ 存在或收敛, 记为

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \lim _ {a ^ {\prime} \to a ^ {+}} \int_ {a ^ {\prime}} ^ {b} f (x) \mathrm{d} x,
$$

否则就称瑕积分 $\int_{a}^{b}f(x)\mathrm{d}x$ 不存在或发散.

不难看出, 若 $f \in R[a, b]$, 则 $f$ 的瑕积分等于其 Riemann 积分. 如果 $f$ 在某一点附近无界, 则称该点为 $f$ 的瑕点. 当 $b$ 为 $f$ 的瑕点时, 可以在 $[a, b)$ 上定义瑕积分如下:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \lim _ {b ^ {\prime} \to b ^ {-}} \int_ {a} ^ {b ^ {\prime}} f (x) \mathrm{d} x.
$$

设 $c \in (a, b)$ 为 $f$ 在 $[a, b]$ 上的唯一瑕点, 则定义

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {c} f (x) \mathrm{d} x + \int_ {c} ^ {b} f (x) \mathrm{d} x,
$$

前提是上式右边的两个瑕积分均收敛. 当瑕点不止一个时也可类似地定义瑕积分, 瑕积分的收敛性仍有和无穷限积分类似的基本判别法.

如果一个函数既是无界的, 定义域又是无限区间, 则通过适当地分割区间, 可以把上面两种积分, 即无穷限积分和瑕积分结合起来, 得到的积分统称广义积分, 又称反常积分.

例10.1.3 讨论积分 $\int_0^1\frac{1}{x^p}\mathrm{d}x(p\in \mathbb{R})$ 的敛散性.

---

10.1 积分的推广

55

解 当 $0 < a < 1$ 时,

$$
\int_ {a} ^ {1} \frac {1}{x ^ {p}} \mathrm{d} x = \left\{ \begin{array}{l l} - \ln a, & p = 1, \\ \frac {1}{1 - p} (1 - a ^ {1 - p}), & p \neq 1. \end{array} \right.
$$

因此只有 $p < 1$ 时积分才是收敛的, 此时

$$
\int_ {0} ^ {1} \frac {1}{x ^ {p}} \mathrm{d} x = \lim _ {a \to 0 ^ {+}} \frac {1}{1 - p} (1 - a ^ {1 - p}) = \frac {1}{1 - p}.
$$

例 10.1.4 计算积分  $\int_{-1}^{1}\frac{1}{\sqrt{1-x^{2}}}\mathrm{d}x.$

解 被积函数有两个瑕点 ±1. 我们有

$$
\begin{array}{l} \int_ {- 1} ^ {1} \frac {1}{\sqrt {1 - x ^ {2}}} \mathrm{d} x = \int_ {- 1} ^ {0} \frac {1}{\sqrt {1 - x ^ {2}}} \mathrm{d} x + \int_ {0} ^ {1} \frac {1}{\sqrt {1 - x ^ {2}}} \mathrm{d} x \\ = \arcsin x \big | _ {- 1} ^ {0} + \arcsin x \big | _ {0} ^ {1} \\ = \frac {\pi}{2} + \frac {\pi}{2} = \pi . \\ \end{array}
$$

广义积分具有和 Riemann 积分类似的性质, 一些运算法则, 例如分部积分、换元法等也可以直接推广过来. 例如, 我们有

定理 10.1.1 设 u, v 在  $[a, +\infty)$  上可导且  $u', v'$  在每一个有界的闭子区间  $[a, B]$  上均可积，则

$$
\int_ {a} ^ {+ \infty} u (x) v ^ {\prime} (x) \mathrm{d} x = u v \Big | _ {a} ^ {+ \infty} - \int_ {a} ^ {+ \infty} u ^ {\prime} (x) v (x) \mathrm{d} x,
$$

即上式右端有意义时, 其左端也有意义且等于右端的值.

证明 当 $B > a$ 时,由通常的分部积分公式可得

$$
\int_ {a} ^ {B} u (x) v ^ {\prime} (x) \mathrm{d} x = u v \Big | _ {a} ^ {B} - \int_ {a} ^ {B} u ^ {\prime} (x) v (x) \mathrm{d} x,
$$

令  $B \rightarrow +\infty$  即得欲证结论.

定理 10.1.2 设  $f \in C(a, b)$ ,  $\varphi$  是  $(\alpha, \beta)$  上严格单调的可导函数, 且  $\varphi'$  在  $(\alpha, \beta)$  的任何闭子区间上均可积. 若  $\varphi((\alpha, \beta)) \subseteq (a, b)$ , 且  $\varphi(\alpha^{+}) = a$ ,  $\varphi(\beta^{-}) = b$ , 则

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {\alpha} ^ {\beta} f (\varphi (t)) \varphi^ {\prime} (t) \mathrm{d} t,
$$

即上式右端有意义时, 左端也有意义且等于右端的值.

证明 任取 $[a', b'] \subseteq (a, b)$，利用介值定理，我们可以选取 $\alpha', \beta' \in (\alpha, \beta)$，使得 $\varphi(\alpha') = a', \varphi(\beta') = b'$。由通常的换元法可得

$$
\int_ {\varphi (\alpha^ {\prime})} ^ {\varphi (\beta^ {\prime})} f (x) \mathrm{d} x = \int_ {\alpha^ {\prime}} ^ {\beta^ {\prime}} f (\varphi (t)) \varphi^ {\prime} (t) \mathrm{d} t.
$$

---

56

第十章 广义积分

令 $a^{\prime}\rightarrow a^{+},b^{\prime}\rightarrow b^{-}$ ，由 $\varphi$ 严格单调可知 $\alpha^{\prime}\to \alpha^{+},\beta^{\prime}\to \beta^{-}$ ，由此即得欲证结论. □

例 10.1.5 计算积分  $\int_{0}^{1}\ln x dx$ .

解 利用 $\lim_{x\to 0^{+}}x\ln x = 0$ 得

$$
\int_ {0} ^ {1} \ln x \mathrm{d} x = x \ln x \Big | _ {0} ^ {1} - \int_ {0} ^ {1} x \cdot \frac {1}{x} \mathrm{d} x = - 1.
$$

例 10.1.6 讨论积分  $\int_{0}^{+\infty}\cos x^{2}dx$  的敛散性.

解 只要讨论被积函数在 $[1, +\infty)$ 上的积分就可以了. 作变换 $x = \sqrt{t}$ 可得

$$
\int_ {1} ^ {+ \infty} \cos x ^ {2} \mathrm{d} x = \frac {1}{2} \int_ {1} ^ {+ \infty} \frac {\cos t}{\sqrt {t}} \mathrm{d} t.
$$

我们利用分部积分和 Cauchy 准则来判断积分的收敛性:

$$
\begin{array}{l} \left| \int_ {A} ^ {B} \frac {\cos t}{\sqrt {t}} \mathrm{d} t \right| = \left| \frac {\sin t}{\sqrt {t}} \right| _ {A} ^ {B} + \frac {1}{2} \int_ {A} ^ {B} \frac {\sin t}{t ^ {\frac {3}{2}}} \mathrm{d} t \\ \leqslant \frac {1}{\sqrt {A}} + \frac {1}{\sqrt {B}} + \frac {1}{2} \int_ {A} ^ {B} t ^ {- \frac {3}{2}} \mathrm{d} t = \frac {2}{\sqrt {A}} \rightarrow 0 (B > A \rightarrow + \infty). \\ \end{array}
$$

这说明积分是收敛的.

![](../../raw/pages_0353-0368/images/page_362_image_12.jpg)

注 10.1.1 这个例子也告诉我们，f 在  $[a, +\infty)$  上的积分存在并不意味着  $f(x) \to 0 (x \to +\infty)$ .

## 习题 10.1

1. 设 $f$ 为 $[a, b]$ 上的有界函数. 如果任给 $a' \in (a, b)$, 均有 $f \in R[a', b]$, 证明: $f \in R[a, b]$, 且

$$
\lim _ {a ^ {\prime} \to a ^ {+}} \int_ {a ^ {\prime}} ^ {b} f (x)   \mathrm{d} x = \int_ {a} ^ {b} f (x)   \mathrm{d} x.
$$

2. 证明:

$$
\frac {\pi}{2 \sqrt {2}} <   \int_ {0} ^ {1} \frac {\mathrm{d} x}{\sqrt {1 - x ^ {4}}} <   \frac {\pi}{2}.
$$

3. 计算下列无穷限积分:

(1) $\int_{2}^{+\infty}\frac{\mathrm{d}x}{x(\ln x)^{2}};$

(2) $\int_{1}^{+\infty}\frac{\ln x}{x^2}\mathrm{d}x;$

(3) $\int_{\mathrm{e}^2}^{+\infty}\frac{\mathrm{d}x}{x\ln x\ln^2(\ln x)};$

(4) $\int_{1}^{+\infty}\frac{\mathrm{d}x}{x(1 + x)};$

(5) $\int_0^{+\infty}\frac{\mathrm{d}x}{(x + 2)(x + 3)};$

(6) $\int_{0}^{+\infty}\frac{\mathrm{d}x}{x^2 + 2x + 2}.$

---

10.2 广义积分的收敛判别法

57

4. 计算下列瑕积分:

(1) $\int_0^1\frac{x^3\mathrm{d}x}{\sqrt{1 - x^2}};$

(2) $\int_{-1}^{1}\frac{x\mathrm{d}x}{\sqrt{1 - x^2}};$

(3) $\int_{-1}^{1} \frac{\arcsin x}{\sqrt{1 - x^2}} \, \mathrm{d}x;$

(4) $\int_0^1\frac{\mathrm{d}x}{(2 - x)\sqrt{1 - x}};$

(5) $\int_{\alpha}^{\beta}\frac{x\mathrm{d}x}{\sqrt{(x - \alpha)(\beta - x)}};$

(6) $\int_0^1\frac{\arcsin\sqrt{x}}{\sqrt{x(1 - x)}}\mathrm{d}x.$

5. 讨论下列广义积分的敛散性:

(1) $\int_{0}^{+\infty}|\cos x^2 |\mathrm{d}x;$

(2) $\int_0^{+\infty}\frac{\mathrm{d}x}{\mathrm{e}^x\sqrt{x}}.$

6. 讨论下列瑕积分的敛散性:

(1) $\int_0^1\frac{\mathrm{d}x}{\sqrt{x}};$

(2) $\int_0^1\frac{\ln x}{1 - x}\mathrm{d}x;$

(3) $\int_0^2\frac{\mathrm{d}x}{(x - 1)^2}.$

7. 设 $g \leqslant f \leqslant h$ 且 $g, h$ 在 $[a, +\infty)$ 上的无穷限积分都收敛, 证明: $f$ 在 $[a, +\infty)$ 上的无穷限积分也收敛.

8. 设 $f$ 为单调递减函数且它在 $[a, +\infty)$ 上的无穷限积分收敛, 证明: $\lim_{x \to +\infty} x f(x) = 0$.

9. 设 $f$ 在 $[a, +\infty)$ 上的无穷限积分收敛, 且 $f$ 一致连续, 证明: $\lim_{x \to +\infty} f(x) = 0$.

10. 举例说明, 当 $f$ 为正连续函数且它在 $[a, +\infty)$ 上的无穷限积分收敛时, 未必有 $\lim_{x \to +\infty} f(x) = 0$.

11. 设 f 为  $(0,1]$  上的单调递减函数, 证明:

$$
\int_ {0} ^ {1} f (x) \mathrm{d} x = \lim _ {n \to + \infty} \frac {1}{n} \sum_ {k = 1} ^ {n} f \left(\frac {k}{n}\right).
$$

12. 利用上一题证明: $\lim_{n\to +\infty}\frac{\sqrt[n]{n!}}{n} = \frac{1}{\mathrm{e}}.$

## 10.2 广义积分的收敛判别法

我们知道 Cauchy 准则可以用来判断广义积分的敛散性. 下面我们进一步介绍其他的几个判别法. 首先研究非负函数, 注意到如果 $f$ 非负且在有界区间上均可积, 则积分 $\int_{a}^{B} f(x) \mathrm{d}x$ 关于 $B$ 单调递增, 因此其极限存在当且仅当它有上界, 这就得到了非负函数无穷限积分的如下判别法:

定理 10.2.1 设  $f \geqslant 0$  且在有界区间  $[a, B]$  上均可积，则无穷限积分  $\int_{a}^{+\infty} f(x) \, dx$ 
收敛当且仅当

---

58

第十章 广义积分

$$
F (B) = \int_ {a} ^ {B} f (x)   \mathrm{d} x
$$

关于  $B \in [a, +\infty)$  有界；对瑕积分有完全类似的结果.

由此又得到如下的比较判别法:

定理 10.2.2 设 $0 \leqslant f \leqslant M g$, 其中 $M > 0$ 为常数. 如果 $f, g$ 在有界区间 $[a, B]$ 上均可积, 则当无穷限积分 $\int_{a}^{+\infty} g(x) \mathrm{d}x$ 收敛时, 无穷限积分 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 也收敛; 当无穷限积分 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 发散时, 无穷限积分 $\int_{a}^{+\infty} g(x) \mathrm{d}x$ 也发散; 瑕积分有完全类似的结果.

证明 令

$$
F (B) = \int_ {a} ^ {B} f (x)   \mathrm{d} x, G (B) = \int_ {a} ^ {B} g (x)   \mathrm{d} x,
$$

则 $0 \leqslant F(B) \leqslant M \cdot G(B), \forall B \in [a, +\infty)$. 因此, 当 $G(B)$ 有界时 $F(B)$ 也有界, 当 $F(B)$ 无界时 $G(B)$ 也无界. □

注 10.2.1 (1) 通常利用极限去找 M. 如果极限  $l = \lim_{x \to +\infty} \frac{f(x)}{g(x)}$  存在，则当  $0 < l < +\infty$  时，无穷限积分  $\int_{a}^{+\infty} f(x) \, dx$  和  $\int_{a}^{+\infty} g(x) \, dx$  同时收敛或发散；当 l = 0 时，如果  $\int_{a}^{+\infty} g(x) \, dx$  收敛，则  $\int_{a}^{+\infty} f(x) \, dx$  也收敛；当  $l = +\infty$  时，如果  $\int_{a}^{+\infty} g(x) \, dx$  发散，则  $\int_{a}^{+\infty} f(x) \, dx$  也发散.

(2) 我们可以将函数 f 与  $x^{-p}$  比较, 则得到如下的 Cauchy 判别法:

(i) 如果 p > 1，且存在常数 C > 0，使得

$$
0 \leqslant f (x) \leqslant \frac {C}{x ^ {p}} (\forall x \geqslant x _ {0}),
$$

则 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 收敛；

(ii) 如果 $p \leqslant 1$, 且存在常数 $C > 0$, 使得

$$
f (x) \geqslant \frac {C}{x ^ {p}} (\forall x \geqslant x _ {0}),
$$

则 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 发散；

通常利用极限取寻找 C. 设极限  $\lim_{x\to+\infty}x^{p}f(x)=l$  存在, 则

(iii) 如果 $p > 1, 0 \leqslant l < +\infty$，则 $\int_{a}^{+\infty} f(x) \, \mathrm{d}x$ 收敛；

(iv) 如果 $p \leqslant 1, 0 < l \leqslant +\infty$，则 $\int_{a}^{+\infty} f(x) \, \mathrm{d}x$ 发散.

(3) 类似地, 考虑以 $a$ 为瑕点的瑕积分 $\int_{a}^{b} f(x) \mathrm{d}x$, 有

---

10.2 广义积分的收敛判别法

59

(i) 如果 $p < 1$, 且存在常数 $C > 0$, 使得 $0 \leqslant f(x) \leqslant C(x - a)^{-p}$, 则瑕积分 $\int_{a}^{b} f(x) \, \mathrm{d}x$ 收敛;

(ii) 如果 $p \geqslant 1$, 且存在常数 $C > 0$, 使得 $f(x) \geqslant C(x - a)^{-p}$, 则瑕积分 $\int_{a}^{b} f(x) \, \mathrm{d}x$ 发散;

我们往往通过求极限去寻找 $C$ 设 $\lim_{x\to a^{+}}(x - a)^{p}f(x) = l$ 存在, 则

(iii) 如果 $p < 1, 0 \leqslant l < +\infty$，则瑕积分 $\int_{a}^{b} f(x) \, \mathrm{d}x$ 收敛；

(iv) 如果 $p \geqslant 1, 0 < l \leqslant +\infty$，则瑕积分 $\int_{a}^{b} f(x) \, \mathrm{d}x$ 发散.

例 10.2.1 判别积分  $\int_{1}^{+\infty}\frac{1}{x\sqrt{x^{2}+x+1}}\mathrm{d}x$  的敛散性.

解 因为

$$
0 \leqslant \frac {1}{x \sqrt {x ^ {2} + x + 1}} \leqslant x ^ {- 2}, \forall x \geqslant 1,
$$

所以积分是收敛的.

例 10.2.2 判别积分  $\int_{1}^{+\infty} x^{a} e^{-x} dx (a \in R)$  的敛散性.

解 因为

$$
\lim _ {x \to + \infty} x ^ {2} x ^ {a} \mathrm{e} ^ {- x} = \lim _ {x \to + \infty} \frac {x ^ {2 + a}}{\mathrm{e} ^ {x}} = 0,
$$

所以积分是收敛的.

例 10.2.3 判别积分  $\int_{1}^{+\infty}\frac{1}{x(1+\ln x)}\mathrm{d}x$  的敛散性.

解 被积函数有原函数 $F(x) = \ln (1 + \ln x)$，由 Newton-Leibniz 公式易见积分是发散的.

这里要提醒读者注意, 比较判别法只适用于不变号的函数. 对于变号函数的广义积分, 有时可以化为非负函数的积分来判断它是否收敛.

设 $f$ 为函数, 记

$$
f ^ {+} (x) = \max \{0, f (x) \}, \quad f ^ {-} (x) = \max \{0, - f (x) \},
$$

则 $f^{+}$ 和 $f^{-}$ 均为非负函数, 且 $f = f^{+} - f^{-}$. 因此, 当 $f^{+}$ 和 $f^{-}$ 的广义积分均收敛时, $f$ 的广义积分也收敛, 此时称 $f$ 的广义积分绝对收敛, 采用这个称呼的部分原因是 $|f| = f^{+} + f^{-}$ 的广义积分的确是收敛的. 如果 $f$ 的广义积分收敛, 但 $|f|$ 的广义积分发散, 则称 $f$ 的广义积分条件收敛.

设 f, g 在有界区间  $[a, B]$  上均可积, 且

$$
| f (x) | \leqslant g (x), \forall x \geqslant x _ {0},
$$

---

60

第十章 广义积分

则当积分 $\int_{a}^{+\infty}g(x)\mathrm{d}x$ 收敛时，积分 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 绝对收敛.这只要注意到 $f^{+}\leqslant g,$ $f^{-}\leqslant g$ 并利用比较判别法即可.

例10.2.4 判别积分 $\int_{1}^{+\infty}\frac{\cos x}{x^p}\mathrm{d}x$ $(p > 1)$ 是否绝对收敛.

解 因为

$$
\left| \frac {\cos x}{x ^ {p}} \right| \leqslant x ^ {- p}, \forall x \geqslant 1,
$$

而 $p > 1$ 时 $x^{-p}$ 积分收敛, 所以原积分是绝对收敛的.

例 10.2.5 判别积分  $\int_{1}^{+\infty}\cos(x^{p})\mathrm{d}x\ (p>1)$  的敛散性, 若收敛则判断它是否绝对收敛.

解 利用变量代换 $x = t^{\frac{1}{p}}$ 以及前节最后例子中的办法不难看出积分是收敛的. 另一方面, 注意到

$$
\left| \cos (x ^ {p}) \right| \geqslant \cos^ {2} (x ^ {p}) = \frac {1}{2} \big (1 + \cos (2 x ^ {p}) \big),
$$

函数 $\cos (2x^{p})$ 的无穷限积分是收敛的, 因此 $|\cos (x^p)|$ 在 $[1, +\infty)$ 上的无穷限积分是发散的.

对于两个函数乘积的广义积分, 在某些情形下利用积分第二中值公式可以判断积分是否条件收敛.

定理 10.2.3 (Dirichlet) 设当 B > a 时函数 f, g 在有界区间  $[a, B]$  上均可积，如果积分  $F(B) = \int_{a}^{B} f(x) \, dx$  关于  $B \in [a, +\infty)$  有界，函数 g 在  $[a, +\infty)$  上单调，且  $\lim_{x \to +\infty} g(x) = 0$ ，则无穷限积分  $\int_{a}^{+\infty} f(x) g(x) \, dx$  收敛.

证明 设 $|F(B)| \leqslant C, \forall B \geqslant a$. 则当 $B \geqslant A \geqslant a$ 时, 有

$$
\left| \int_ {A} ^ {B} f (x) \mathrm{d} x \right| = \left| \int_ {a} ^ {B} f (x) \mathrm{d} x - \int_ {a} ^ {A} f (x) \mathrm{d} x \right| \leqslant 2 C,
$$

又因为 $\lim_{x\to +\infty}g(x) = 0$ ，所以任给 $\varepsilon >0$ ，存在 $M > a$ ，使得当 $x > M$ 时

$$
| g (x) | \leqslant \frac {\varepsilon}{4 C}.
$$

由积分第二中值定理, 当 B > A > M 时, 有

$$
\begin{array}{l} \left| \int_ {A} ^ {B} f (x) g (x) \mathrm{d} x \right| = \left| g (A) \int_ {A} ^ {\xi} f (x) \mathrm{d} x + g (B) \int_ {\xi} ^ {B} f (x) \mathrm{d} x \right| \\ \leqslant \frac {\varepsilon}{4 C} \left| \int_ {A} ^ {\xi} f (x) \mathrm{d} x \right| + \frac {\varepsilon}{4 C} \left| \int_ {\xi} ^ {B} f (x) \mathrm{d} x \right| \\ \leqslant \frac {\varepsilon}{4 C} 2 C + \frac {\varepsilon}{4 C} 2 C = \varepsilon . \\ \end{array}
$$

由 Cauchy 准则即得欲证结论.

□

---

10.2 广义积分的收敛判别法

61

例10.2.6 判断积分 $\int_0^{+\infty}\frac{\sin x}{x^p}\mathrm{d}x$ （ $0 <   p <   2$ )的敛散性.

解 因为

$$
\lim _ {x \to 0 ^ {+}} x ^ {p - 1} \frac {\sin x}{x ^ {p}} = 1,
$$

所以在 $(0,1]$ 上 $\frac{\sin x}{x^p}$ 的瑕积分的敛散性和 $x^{1 - p}$ 的瑕积分的敛散性一致，而当 $p < 2$ 时 $x^{1 - p}$ 在 $(0,1]$ 上的瑕积分收敛. 下面只要判断 $\frac{\sin x}{x^p}$ 在 $[1, +\infty)$ 上的无穷限积分的敛散性即可. 由于积分 $\int_{1}^{A}\sin x\mathrm{d}x$ 显然有界，而 $\frac{1}{x^p} (p > 0)$ 在 $[1, +\infty)$ 上单调地趋于零，故由Dirichlet判别法知原积分是收敛的. □

定理 10.2.4 (Abel) 设当 B > a 时函数 f, g 在有界区间  $[a, B]$  上均可积，如果积分  $\int_{a}^{+\infty} f(x) \, dx$  收敛，且 g 在  $[a, +\infty)$  上单调有界，则积分  $\int_{a}^{+\infty} f(x) g(x) \, dx$  也收敛.

证明 由题设可知 $F(B) = \int_{a}^{B} f(x) \, \mathrm{d}x$ 关于 $B \in [a, +\infty)$ 有界. 由 $g$ 单调有界可知极限 $\lim_{x \to +\infty} g(x)$ 存在, 记为 $\alpha$. 此时, $fg$ 可以写成

$$
f g = f \cdot (g - \alpha) + \alpha f (x).
$$

由 Dirichlet 判别法可知  $f \cdot (g - \alpha)$  的积分收敛, 从而 fg 的积分也收敛.

这些判别法对于瑕积分也有完全类似的表达形式, 我们不再赘述.

例 10.2.7 设  $a \geqslant 0$ ，研究积分  $\int_{0}^{+\infty} e^{-ax} \frac{\sin x}{x} dx$  的敛散性.

解 函数 $\mathrm{e}^{-ax}$ 在 $[0, +\infty)$ 上单调递减且有界，函数 $\frac{\sin x}{x}$ 在 $[0, +\infty)$ 上的积分收敛，因此由Abel判别法知原积分收敛. □

例 10.2.8 判断积分  $\int_{1}^{+\infty}\frac{\sin x}{x^{p}}\arctan x\,dx\ (p>0)$  的敛散性.

解 令 $f(x) = \frac{\sin x}{x^p}$, $g(x) = \arctan x$, 则 $f$ 在 $[1, +\infty)$ 上的积分收敛, 而 $g$ 在 $[1, +\infty)$ 上单调有界, 故由 Abel 判别法知原积分收敛. □

## 习题 10.2

1. 研究下列无穷限积分的敛散性:

(1) $\int_{1}^{+\infty}\frac{\mathrm{d}x}{\sqrt[3]{x^4 + 1}};$

(2) $\int_0^{+\infty}\frac{\mathrm{d}x}{1 + \sqrt{x}};$

(3) $\int_0^{+\infty}\frac{x^3\mathrm{d}x}{\sqrt{1 + x^7}};$

(4) $\int_0^{+\infty}\frac{\sin^2x}{\sqrt{x}}\mathrm{d}x;$

(5) $\int_{1}^{+\infty}\frac{x\arctan x}{1 + x^3}\mathrm{d}x;$

(6) $\int_{1}^{+\infty}\frac{x^2\mathrm{d}x}{\sqrt{1 + x^6}};$

---

62

第十章 广义积分

(7) $\int_0^{+\infty}\frac{\cos x}{1 + x^2}\mathrm{d}x;$
(8) $\int_{1}^{+\infty}\frac{\ln(1 + x)}{x^n}\mathrm{d}x;$
(9) $\int_{1}^{+\infty}\frac{\pi / 2 - \arctan x}{x}\mathrm{d}x.$

2. 研究下列瑕积分的敛散性:

(1) $\int_0^1\frac{\mathrm{d}x}{\sqrt[3]{1 - x^3}};$
(2) $\int_0^1\frac{\mathrm{d}x}{\sqrt{x}\ln x};$
(3) $\int_0^1\frac{\mathrm{d}x}{\sqrt{1 - x^4}};$
(4) $\int_0^\pi \frac{\mathrm{d}x}{\sqrt{\sin x}};$
(5) $\int_0^1\frac{1 - \cos x}{x^p}\mathrm{d}x;$
(6) $\int_0^1\frac{1}{\ln x}\mathrm{d}x;$
(7) $\int_0^1\frac{1}{x^p}\sin \frac{1}{x}\mathrm{d}x;$
(8) $\int_0^1\frac{\ln x}{1 - x^2}\mathrm{d}x;$
(9) $\int_0^1\frac{x^{p - 1} - x^{q - 1}}{\ln x}\mathrm{d}x.$

3. 研究下列积分的绝对收敛性和条件收敛性:

(1) $\int_{1}^{+\infty}\frac{\sin\sqrt{x}}{x}\mathrm{d}x;$
(2) $\int_{1}^{+\infty}\frac{\cos x}{x}\mathrm{d}x;$
(3) $\int_{\mathrm{e}}^{+\infty}\frac{\ln(\ln x)}{\ln x}\sin x\mathrm{d}x;$
(4) $\int_{0}^{+\infty}\frac{\sqrt{x}\sin x}{1 + x}\mathrm{d}x;$
(5) $\int_{1}^{+\infty}\frac{\sin\frac{1}{x}}{x}\mathrm{d}x;$
(6) $\int_{1}^{+\infty} (\ln x)^{p} \frac{\sin x}{x} \, \mathrm{d}x.$

4. 判别下列积分的敛散性:

(1) $\int_0^{+\infty}\sin (x^p)\mathrm{d}x;$
(2) $\int_{0}^{+\infty}\frac{\cos x}{x^p}\mathrm{d}x;$
(3) $\int_{0}^{+\infty}\frac{1 - \cos x}{x}\mathrm{e}^{-x}\mathrm{d}x;$
(4) $\int_{1}^{+\infty}\frac{\mathrm{d}x}{x^p\ln^q x};$
(5) $\int_{0}^{+\infty}\frac{\sin x\cos\frac{1}{x}}{x^p}\mathrm{d}x;$
(6) $\int_{0}^{+\infty}\frac{\cos x\sin\frac{1}{x}}{x^p}\mathrm{d}x.$

5. 设 $f \in C[1, +\infty)$, 如果 $\int_{1}^{+\infty} f^{2}(x) \mathrm{d}x$ 收敛, 证明: $\int_{1}^{+\infty} \frac{f(x)}{x} \mathrm{d}x$ 绝对收敛.

6. 设 $b > 0$ 时 $f$ 在有界区间 $(0, b)$ 上的积分均收敛, 且 $\lim_{x \to +\infty} f(x) = 0$. 证明:

$$
\lim _ {b \to + \infty} \frac {1}{b} \int_ {0} ^ {b} f (x)   \mathrm{d} x = 0.
$$

7. 设 $f \in C[0, +\infty)$，如果 $f$ 处处为正且 $\int_{0}^{+\infty} \frac{\mathrm{d}x}{f(x)}$ 收敛，证明:

$$
\lim _ {b \to + \infty} \frac {1}{b ^ {2}} \int_ {0} ^ {b} f (x)   \mathrm{d} x = + \infty .
$$

---

10.3 广义积分的几个例子

63

8. 设 $f$ 在 $[0, +\infty)$ 上单调递减地趋于零, 证明: 积分

$$
\int_ {0} ^ {+ \infty} f (x)   \mathrm{d} x \quad \text {与} \quad \int_ {0} ^ {+ \infty} f (x)   \sin^ {2} x   \mathrm{d} x
$$

同时收敛或发散.

9. 设  $\gamma$  为 Euler 常数, 证明:

$$
\int_ {1} ^ {+ \infty} \left(\frac {1}{[ x ]} - \frac {1}{x}\right) \mathrm{d} x = \gamma .
$$

10. 研究广义积分  $\int_{0}^{+\infty}\frac{dx}{1+x^{4}\sin^{2}x}$  的敛散性.

11. 设 p > 0, 研究广义积分  $\int_{1}^{+\infty}\frac{\sin x}{x^{p} + \sin x}dx$  的敛散性.

12. 设 $p \in \mathbb{R}$, 研究广义积分 $\int_{0}^{+\infty} \frac{\sin\left(x + \frac{1}{x}\right)}{x^p} \, \mathrm{d}x$ 的敛散性.

## 10.3 广义积分的几个例子

我们来计算几个常见的广义积分.

例 10.3.1 计算积分  $I=\int_{0}^{+\infty}\mathrm{e}^{-ax}\sin bx\,\mathrm{d}x$  (a>0).

解 利用分部积分可以计算出被积函数的一个原函数

$$
F (x) = - \frac {a \sin b x + b \cos b x}{a ^ {2} + b ^ {2}} \mathrm{e} ^ {- a x},
$$

因此, 由 Newton-Leibniz 公式, 有

$$
I = F (+ \infty) - F (0) = - F (0) = \frac {b}{a ^ {2} + b ^ {2}}.
$$

例 10.3.2 计算积分  $I=\int_{0}^{+\infty}\frac{1}{1+x^{4}}\mathrm{d}x.$

解 令 $x = \frac{1}{t}$ 可得

$$
I = \int_ {0} ^ {+ \infty} \frac {t ^ {- 2} \mathrm{d} t}{1 + t ^ {- 4}} = \int_ {0} ^ {+ \infty} \frac {t ^ {2} \mathrm{d} t}{1 + t ^ {4}},
$$

这说明

$$
2 I = \int_ {0} ^ {+ \infty} \frac {1 + x ^ {2}}{1 + x ^ {4}} \mathrm{d} x = \int_ {0} ^ {+ \infty} \frac {1 + x ^ {- 2}}{x ^ {2} + x ^ {- 2}} \mathrm{d} x
$$

---

64

第十章 广义积分

$$
\begin{array}{l} = \int_ {0} ^ {+ \infty} \frac {(x - 1 / x) ^ {\prime} \mathrm{d} x}{(x - 1 / x) ^ {2} + 2} = \int_ {- \infty} ^ {+ \infty} \frac {\mathrm{d} u}{u ^ {2} + 2} \\ = \frac {1}{\sqrt {2}} \arctan \left. \frac {u}{\sqrt {2}} \right| _ {- \infty} ^ {+ \infty} = \frac {\pi}{\sqrt {2}}. \\ \end{array}
$$

这说明  $I=\frac{\pi}{2\sqrt{2}}$ .

例 10.3.3 设 n 为非负整数, 计算积分  $I_{n}=\int_{0}^{+\infty}x^{n}e^{-x}dx$ .

解 当 $n = 0$ 时, $I_0 = -\mathrm{e}^{-x}|_0^{+\infty} = 1$. 当 $n \geqslant 1$ 时, 由分部积分可得

$$
\begin{array}{l} I _ {n} = \int_ {0} ^ {+ \infty} x ^ {n} \mathrm{e} ^ {- x} \mathrm{d} x = - \mathrm{e} ^ {- x} x ^ {n} \Big | _ {0} ^ {+ \infty} + n \int_ {0} ^ {+ \infty} x ^ {n - 1} \mathrm{e} ^ {- x} \mathrm{d} x \\ = n \int_ {0} ^ {+ \infty} x ^ {n - 1} \mathrm{e} ^ {- x} \mathrm{d} x = n I _ {n - 1}, \\ \end{array}
$$

这说明  $I_{n}=n!$ .

例 10.3.4 设 n 为正整数, 计算积分  $I_{n}=\int_{0}^{+\infty}\frac{1}{(1+x^{2})^{n}}\mathrm{d}x.$

解 当 $n = 1$ 时, $I_{1} = \arctan x\big|_{0}^{+\infty} = \frac{\pi}{2}$. 当 $n \geqslant 2$ 时,

$$
\begin{array}{l} I _ {n} = \int_ {0} ^ {+ \infty} \frac {1}{(1 + x ^ {2}) ^ {n}} \mathrm{d} x = \int_ {0} ^ {+ \infty} \frac {1 + x ^ {2} - x ^ {2}}{(1 + x ^ {2}) ^ {n}} \mathrm{d} x \\ = I _ {n - 1} - \int_ {0} ^ {+ \infty} \frac {x ^ {2} \mathrm{d} x}{(1 + x ^ {2}) ^ {n}} \\ = I _ {n - 1} + \frac {1}{2 (n - 1)} \frac {x}{(1 + x ^ {2}) ^ {n - 1}} \Big | _ {0} ^ {+ \infty} - \frac {1}{2 (n - 1)} \int_ {0} ^ {+ \infty} \frac {1}{(1 + x ^ {2}) ^ {n - 1}} \mathrm{d} x \\ = \frac {2 n - 3}{2 n - 2} I _ {n - 1}. \\ \end{array}
$$

这说明 $I_{n} = \frac{\pi}{2}\frac{(2n - 3)!!}{(2n - 2)!!}$.

注 10.3.1 也可以利用变换  $x = \tan t$  化为例 9.4.6.

例 10.3.5 计算 Euler-Poisson $^{①}$ 积分  $\int_{0}^{+\infty} e^{-x^{2}} dx$ .

解 从不等式 $\mathrm{e}^t\geqslant 1 + t$ 可得 $1 - x^{2}\leqslant \mathrm{e}^{-x^{2}}\leqslant (1 + x^{2})^{-1}$ 当 $n\geqslant 1$ 时，就有

$$
\int_ {0} ^ {1} (1 - x ^ {2}) ^ {n} \mathrm{d} x \leqslant \int_ {0} ^ {1} \mathrm{e} ^ {- n x ^ {2}} \mathrm{d} x \leqslant \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- n x ^ {2}} \mathrm{d} x \leqslant \int_ {0} ^ {+ \infty} \frac {\mathrm{d} x}{(1 + x ^ {2}) ^ {n}},
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Poisson, Siméon Denis, 1781 年 6 月 21 日—1840 年 4 月 25 日, 法国数学家、物理学家.</span></small>

---

10.3 广义积分的几个例子

65

上式左边利用变量代换 $x = \cos t$ 以及例9.4.6, 中间利用 $x = \frac{t}{\sqrt{n}}$, 右边利用前一例, 最后得到

$$
\frac {(2 n) ! !}{(2 n + 1) ! !} \leqslant \frac {1}{\sqrt {n}} \int_ {0} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t \leqslant \frac {\pi}{2} \frac {(2 n - 3) ! !}{(2 n - 2) ! !},
$$

两边乘 $\sqrt{n}$, 再利用 Wallis 公式不难看出, 当 $n \to \infty$ 时, 左右极限均为 $\frac{\sqrt{\pi}}{2}$, 这说明

$$
\int_ {0} ^ {+ \infty} \mathrm{e} ^ {- t ^ {2}} \mathrm{d} t = \frac {\sqrt {\pi}}{2}. \tag {10.3.1}
$$

例 10.3.6 计算积分  $\int_{0}^{+\infty}\frac{\sin^{2}x}{x^{2}}\mathrm{d}x.$

解 当 $n \geqslant 0$ 时, 利用等式 $\sin (2n + 1)x - \sin (2n - 1)x = 2\sin x\cos 2nx$ 易得

$$
\int_ {0} ^ {\frac {\pi}{2}} \frac {\sin (2 n + 1) x}{\sin x} \mathrm{d} x = \frac {\pi}{2}. \tag {10.3.2}
$$

再利用等式 $\sin^2 nx - \sin^2 (n - 1)x = \sin (2n - 1)x\sin x$ 可得

$$
\int_ {0} ^ {\frac {\pi}{2}} \frac {\sin^ {2} n x}{\sin^ {2} x} \mathrm{d} x = \sum_ {k = 1} ^ {n} \int_ {0} ^ {\frac {\pi}{2}} \frac {\sin (2 k - 1) x}{\sin x} \mathrm{d} x = \frac {\pi}{2} n. \tag {10.3.3}
$$

当 $x \in \left(0, \frac{\pi}{2}\right)$ 时, 注意到

$$
0 <   \frac {1}{\sin^ {2} x} - \frac {1}{x ^ {2}} = 1 + \frac {1}{\tan^ {2} x} - \frac {1}{x ^ {2}} <   1, \tag {10.3.4}
$$

这说明

$$
\begin{array}{l} \int_ {0} ^ {+ \infty} \frac {\sin^ {2} x}{x ^ {2}} \mathrm{d} x = \lim _ {n \to + \infty} \int_ {0} ^ {\frac {\pi}{2} n} \frac {\sin^ {2} x}{x ^ {2}} \mathrm{d} x = \lim _ {n \to + \infty} \frac {1}{n} \int_ {0} ^ {\frac {\pi}{2}} \frac {\sin^ {2} n x}{x ^ {2}} \mathrm{d} x \\ = \lim _ {n \to + \infty} \frac {1}{n} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} n x \left(\frac {1}{x ^ {2}} - \frac {1}{\sin^ {2} x}\right) \mathrm{d} x + \lim _ {n \to + \infty} \frac {1}{n} \int_ {0} ^ {\frac {\pi}{2}} \frac {\sin^ {2} n x}{\sin^ {2} x} \mathrm{d} x \\ = 0 + \frac {\pi}{2} = \frac {\pi}{2}. \\ \end{array}
$$

例10.3.7 计算Euler积分 $I = \int_0^{\frac{\pi}{2}}\ln \sin x\mathrm{d}x.$

解 令 $x = \frac{\pi}{2} - t$ 可得

$$
I = \int_ {0} ^ {\frac {\pi}{2}} \ln \cos t   \mathrm{d} t,
$$

这说明

$$
\begin{array}{l} 2 I = \int_ {0} ^ {\frac {\pi}{2}} \ln (\sin t \cos t) \mathrm{d} t = \int_ {0} ^ {\frac {\pi}{2}} \ln \sin 2 t \mathrm{d} t - \frac {\pi}{2} \ln 2 \\ = \frac {1}{2} \int_ {0} ^ {\pi} \ln \sin x \mathrm{d} x - \frac {\pi}{2} \ln 2. \\ \end{array}
$$

---

66

第十章 广义积分

在 $\left[\frac{\pi}{2},\pi \right]$ 中令 $x = \pi -t$ 可得

$$
\int_ {\frac {\pi}{2}} ^ {\pi} \ln \sin x   \mathrm{d} x = I,
$$

这说明 $2I = I - \frac{\pi}{2}\ln 2$ ，即 $I = -\frac{\pi}{2}\ln 2.$

例10.3.8 设 $f$ 是定义在 $(0, +\infty)$ 上的函数, 如果任给 $b > a > 0$, 积分 $\int_{a}^{b} \frac{f(x)}{x} \mathrm{d}x$ 均存在, 且

$$
\lim _ {x \to 0 ^ {+}} f (x) = L, \quad \lim _ {x \to + \infty} f (x) = M,
$$

求Frullani积分 $I = \int_0^{+\infty}\frac{f(\alpha x) - f(\beta x)}{x}\mathrm{d}x$ ，其中 $\alpha ,\beta >0$

解 不妨设 $\alpha >\beta$ .任给 $b > a > 0$ ，利用换元法以及积分第一中值定理可得

$$
\begin{array}{l} \int_ {a} ^ {b} \frac {f (\alpha x) - f (\beta x)}{x} \mathrm{d} x = \int_ {a} ^ {b} \frac {f (\alpha x)}{x} \mathrm{d} x - \int_ {a} ^ {b} \frac {f (\beta x)}{x} \mathrm{d} x \\ = \int_ {a \alpha} ^ {b \alpha} \frac {f (y)}{y} \mathrm{d} y - \int_ {a \beta} ^ {b \beta} \frac {f (y)}{y} \mathrm{d} y \\ = \int_ {b \beta} ^ {b \alpha} \frac {f (y)}{y} \mathrm{d} y - \int_ {a \beta} ^ {a \alpha} \frac {f (y)}{y} \mathrm{d} y \\ = \lambda \int_ {b \beta} ^ {b \alpha} \frac {1}{y} \mathrm{d} y - \mu \int_ {a \beta} ^ {a \alpha} \frac {1}{y} \mathrm{d} y \\ = \lambda \ln \frac {\alpha}{\beta} - \mu \ln \frac {\alpha}{\beta}, \\ \end{array}
$$

其中

$$
\inf _ {[ b \beta , b \alpha ]} f \leqslant \lambda \leqslant \sup _ {[ b \beta , b \alpha ]} f, \quad \inf _ {[ a \beta , a \alpha ]} f \leqslant \mu \leqslant \sup _ {[ a \beta , a \alpha ]} f.
$$

令 $a \to 0^{+}, b \to +\infty$ 即得 $I = (M - L) \ln \frac{\alpha}{\beta}$.

## 习题 10.3

1. 设 a > 0, 计算积分  $\int_{0}^{+\infty} e^{-ax} \cos bx \, dx$ .

2. 设 n 为正整数, a > 0, 计算下列积分:

(1) $\int_0^{+\infty}x^{2n - 1}\mathrm{e}^{-x^2}\mathrm{d}x;$

(2) $\int_0^{+\infty}\frac{\mathrm{d}x}{(x^2 + a^2)^n};$

(3) $\int_{0}^{+\infty}\mathrm{e}^{-ax}\sin^{n}x\mathrm{d}x.$

3. 计算积分 $I = \int_{0}^{+\infty} \frac{1}{1 + x^6} \, \mathrm{d}x$.

---

10.3 广义积分的几个例子

67

4. 利用例 10.3.6 证明:  $\int_{0}^{+\infty}\frac{\sin x}{x}dx=\frac{\pi}{2}.$

5. 计算下列积分:

(1) $\int_0^\pi x\ln \sin x\mathrm{d}x;$

(2) $\int_{0}^{\frac{\pi}{2}} x \cot x \, \mathrm{d}x$;

(3) $\int_0^1\frac{\arcsin x}{x}\mathrm{d}x;$

(4) $\int_{0}^{\pi}\frac{x\sin x}{1 - \cos x}\mathrm{d}x;$

(5) $\int_{0}^{\frac{\pi}{2}}\frac{x^2}{\sin^2x}\mathrm{d}x;$

(6) $\int_0^\pi \frac{x^2}{1 - \cos x} \, \mathrm{d}x.$

6. 设 $\alpha \in \mathbb{R}$, 计算下列积分:

(1) $\int_0^{+\infty}\frac{\mathrm{d}x}{(1 + x^2)(1 + x^\alpha)};$

(2) $\int_0^{+\infty}\frac{\ln x}{1 + x^2}\mathrm{d}x.$

7. 计算积分  $\int_{0}^{\frac{\pi}{2}}\left(\sqrt{\tan x}+\sqrt{\cot x}\right)\mathrm{d}x.$

8. 设广义积分  $\int_{0}^{+\infty} f(x^{2}) \, dx$  收敛, a, b > 0, 证明:

$$
\int_ {0} ^ {+ \infty} f \left((a x - b / x) ^ {2}\right) \mathrm{d} x = \frac {1}{a} \int_ {0} ^ {+ \infty} f (y ^ {2}) \mathrm{d} y.
$$

9. 设 $f \in C(-\infty, +\infty)$, 且

$$
\lim _ {x \to - \infty} f (x) = L, \quad \lim _ {x \to + \infty} f (x) = M.
$$

当  $\alpha > 0$  时, 证明: 积分

$$
\int_ {- \infty} ^ {+ \infty} (f (x + \alpha) - f (x)) \mathrm{d} x
$$

收敛, 并计算它的值.

10. 设 $f \in C[0, +\infty)$, 且积分 $\int_{1}^{+\infty} \frac{f(x)}{x} \mathrm{~d} x$ 收敛. 当 $\alpha, \beta > 0$ 时, 证明:

$$
\int_ {0} ^ {+ \infty} \frac {f (\alpha x) - f (\beta x)}{x} \mathrm{d} x = f (0) \ln \frac {\beta}{\alpha}.
$$

11. 设 $f \in C(0, +\infty)$, $\lim_{x \to +\infty} f(x) = M$ 存在, 且积分 $\int_{0}^{1} \frac{f(x)}{x} \, \mathrm{d}x$ 收敛. 当 $\alpha, \beta > 0$ 时, 证明:

$$
\int_ {0} ^ {+ \infty} \frac {f (\alpha x) - f (\beta x)}{x} \mathrm{d} x = M \ln \frac {\beta}{\alpha}.
$$

12. 设  $\alpha, \beta > 0$ , 计算下列积分:

(1) $\int_0^{+\infty}\frac{\mathrm{e}^{-\alpha x} - \mathrm{e}^{-\beta x}}{x}\mathrm{d}x;$

(2) $\int_0^{+\infty}\frac{\cos(\alpha x) - \cos(\beta x)}{x}\mathrm{d}x.$
