正如函数时常以函数项级数的形式出现, 函数也时常表示为含参变量积分. 本章主要研究的是含参变量积分的基本性质, 包括含参变量积分的连续性、可微性以及可积性.

## 20.1 含参变量常义积分及其性质

本节介绍含参变量常义积分的连续性、可微性、可积性等. 首先, 我们引入 Arzelà $^{①}$  有界收敛定理. 为此, 先引入如下引理. 我们称函数列  $\{f_{n}\}$  在区间  $[a, b]$  上一致有界, 如果存在常数 M > 0, 使得

$$
| f _ {n} (x) | \leqslant M, \quad \forall x \in [ a, b ], n \geqslant 1. \tag {20.1.1}
$$

引理20.1.1 设 $\{f_n\}$ 为 $[a, b]$ 上一致有界的非负函数列，若

$$
\lim _ {n \to + \infty} f _ {n} (x) = 0, \qquad \forall   x \in [ a, b ], \tag {20.1.2}
$$

则

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} f _ {n} (x) \mathrm{d} x = 0. \tag {20.1.3}
$$

证明 记 $M := \sup_{x \in [a, b], n \geqslant 1} f_n(x)$. 对于 $E \subseteq [a, b]$, 用 $|E|_*$ 表示 $\int_{a}^{b} \chi_E(x) \, \mathrm{d}x$. 当 $\chi_E$ 可积时, 用 $|E|$ 表示 $\int_{a}^{b} \chi_E(x) \, \mathrm{d}x$.

对 $n \geqslant 1$, 定义 $g_{n}(\cdot) := \sup_{k \geqslant n} f_{k}(\cdot)$, 则 $\{g_{n}\}$ 是 $[a, b]$ 上一致有界且单调下降趋于零的函数列. 易见, 要证 (20.1.3) 式, 我们只要证明

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} g _ {n} (x) \mathrm{d} x = 0. \tag {20.1.4}
$$

如果 (20.1.4) 式不成立, 则 $M > 0$, 且有常数 $\delta > 0$ 使得

$$
\int_ {a} ^ {b} g _ {n} (x) \mathrm{d} x \geqslant 2 (b - a) \delta , \quad \forall n \geqslant 1. \tag {20.1.5}
$$

记 $E_{n}:= \{x\in [a,b]|g_{n}(x)\geqslant \delta \}$ ， $\gamma := \frac{(b - a)\delta}{M},\gamma_n\coloneqq |E_n|_*$ .则

$$
\gamma_ {n} \geqslant \frac {1}{M} \int_ {a} ^ {b} \chi_ {E _ {n}} (x) (g _ {n} (x) - \delta) \mathrm{d} x \geqslant \frac {1}{M} \int_ {a} ^ {b} (g _ {n} (x) - \delta) \mathrm{d} x \geqslant \frac {(b - a) \delta}{M} = \gamma , \quad \forall n \geqslant 1.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Arzelà, Cesare, 1847 年 3 月 6 日—1912 年 3 月 15 日, 意大利数学家.</span></small>

另一方面, 由 $\{g_n\}$ 的单调性知 $\{E_n\}$ 是一列单调下降的集合, 进而 $\{\gamma_n\}$ 单调下降. 而由 $\{g_n\}$ 在 $[a, b]$ 上处处趋于零得到

$$
\bigcap_ {n \geqslant 1} E _ {n} = \varnothing . \tag {20.1.6}
$$

对每个 $n \geqslant 1$, 有有限个闭区间的并 $F_{n}$ 使得 $F_{n} \subseteq E_{n}$, 且

$$
\gamma_ {n} \geqslant | F _ {n} | \geqslant \gamma_ {n} - \frac {\gamma}{2 ^ {n + 1}}. \tag {20.1.7}
$$

我们有

$$
\begin{array}{l} \left| \bigcap_ {k = 1} ^ {2} F _ {k} \right| = | F _ {2} | + | F _ {1} | - | F _ {1} \cup F _ {2} | \geqslant | F _ {2} | + | F _ {1} | - | E _ {1} | _ {*} \\ \geqslant \gamma_ {2} - \frac {\gamma}{2 ^ {3}} - \frac {\gamma}{2 ^ {2}}, \\ \left| \bigcap_ {k = 1} ^ {3} F _ {k} \right| = | F _ {3} | + \left| \bigcap_ {k = 1} ^ {2} F _ {k} \right| - \left| \left(\bigcap_ {k = 1} ^ {2} F _ {k}\right) \cup F _ {3} \right| \geqslant | F _ {3} | + \left| \bigcap_ {k = 1} ^ {2} F _ {k} \right| - | E _ {2} | _ {*} \\ \geqslant \gamma_ {3} - \frac {\gamma}{2 ^ {4}} - \frac {\gamma}{2 ^ {3}} - \frac {\gamma}{2 ^ {2}}. \\ \end{array}
$$

类似地, 归纳可证

$$
\big | \bigcap_ {k = 1} ^ {n} F _ {k} \big | \geqslant \gamma_ {n} - \sum_ {k = 1} ^ {n} \frac {\gamma}{2 ^ {k + 1}}, \quad \forall n \geqslant 1.
$$

这表明 $\left\{\bigcap_{k=1}^{n} F_k\right\}$ 是非空紧集构成的闭集套. 因此, $\bigcap_{n=1}^{\infty} F_n$ 非空, 这与 (20.1.6) 式矛盾. 引理得证. □

由以上引理, 立即可得 Arzelà 有界收敛定理.

定理 20.1.2 设  $\{f_{n}\}$  为  $[a, b]$  上一致有界的可积函数列, 若

$$
\lim _ {n \to + \infty} f _ {n} (x) = f (x), \quad \forall x \in [ a, b ], \tag {20.1.8}
$$

且 $f$ 也在 $[a,b]$ 上可积，则

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} f _ {n} (x) \mathrm{d} x = \int_ {a} ^ {b} f (x) \mathrm{d} x. \tag {20.1.9}
$$

证明 由引理 20.1.1,

$$
\varlimsup_ {n \to + \infty} \left| \int_ {a} ^ {b} f _ {n} (x) \mathrm{d} x - \int_ {a} ^ {b} f (x) \mathrm{d} x \right| \leqslant \varliminf_ {n \to + \infty} \int_ {a} ^ {b} \left| f _ {n} (x) - f (x) \right| \mathrm{d} x = 0.
$$

因此, 定理成立.

关于 Arzelà 定理的其他简捷证明, 可以参见梅加强的《数学分析》[46].

基于 Arzelà 定理, 我们可以建立含参变量常义积分的连续性, 可微性以及累次积分的可交换性. 首先, 结合 Heine 定理, 立即可得连续性定理.

定理 20.1.3 设 $f : [a,b] \times [c,d] \rightarrow  \mathbb{R}$ 有界, ${y}_{0} \in  \left\lbrack  {c,d}\right\rbrack$ ,对每个 $x \in  \left\lbrack  {a,b}\right\rbrack  ,f\left( {x,\cdot  }\right)$ 在 ${y}_{0}$ 处连续,对每个 $y \in  \left\lbrack  {c,d}\right\rbrack  ,f\left( {\cdot ,y}\right)$ 在 $\left\lbrack  {a,b}\right\rbrack$ 上可积,则 $F\left( y\right)  :  = \int  _{a}^{b}f\left( {x,y}\right) \mathrm{d}x$ 在 ${y}_{0}$ 处连续.

作为推论, 立即有

定理 20.1.4 设  $f: [a, b] \times [c, d] \rightarrow R$  有界. 对每个  $x \in [a, b]$ ,  $f(x, \cdot)$  在  $[c, d]$  上连续, 对每个  $y \in [c, d]$ ,  $f(\cdot, y)$  在  $[a, b]$  上可积, 则  $F(y) := \int_{a}^{b} f(x, y) \, dx$  在  $[c, d]$  上连续.

进一步, 关于含参变量常义积分的可微性, 我们有

定理20.1.5 设 $f: [a, b] \times (c, d) \to \mathbb{R}, y_0 \in (c, d)$. 若对每个 $y \in (c, d), f(\cdot, y)$ 在 $[a, b]$ 上可积，对每个 $x \in [a, b], f(x, \cdot)$ 在 $y_0$ 处可微，又 $f_y(\cdot, y_0)$ 在 $[a, b]$ 上可积，且存在 $M > 0$ 使得

$$
\(| f (x, y) - f (x, y _ {0}) | \leqslant M | y - y _ {0} |, \quad \forall (x, y) \in [ a, b ] \times (c, d). \tag {20.1.10}
$$

则 $F(y) := \int_{a}^{b} f(x, y) \, \mathrm{d}x$ 在 $y_0$ 处可微，且

$$
F ^ {\prime} (y _ {0}) = \int_ {a} ^ {b} f _ {y} (x, y _ {0}) \mathrm{d} x. \tag {20.1.11}
$$

证明 由(20.1.10)式以及 $f_{y}(\cdot ,y_{0})$ 的有界性得到

$$
\frac {f (x, y) - f (x, y _ {0}) - f _ {y} (x , y _ {0}) (y - y _ {0})}{| y - y _ {0} |} \tag {20.1.12}
$$

关于 $y \in (c, d) \setminus \{y_0\}$ 一致有界. 又由于

$$
\lim _ {y \to y _ {0}} \frac {f (x , y) - f (x , y _ {0}) - f _ {y} (x , y _ {0}) (y - y _ {0})}{| y - y _ {0} |} = 0, \qquad \forall x \in [ a, b ],
$$

从而由 Arzelà 定理和 Heine 定理得到

$$
\begin{array}{l} \lim _ {y \to y _ {0}} \frac {1}{| y - y _ {0} |} \left(F (y) - F (y _ {0}) - \int_ {a} ^ {b} f _ {y} (x, y _ {0}) (y - y _ {0}) \mathrm{d} x\right) \\ = \lim _ {y \to y _ {0}} \int_ {a} ^ {b} \frac {f (x , y) - f (x , y _ {0}) - f _ {y} (x , y _ {0}) (y - y _ {0})}{| y - y _ {0} |} \mathrm{d} x = 0. \\ \end{array}
$$

即 F 在  $y_{0}$  可微且 (20.1.11) 式成立.

□

定理 20.1.5 结合定理 20.1.4 即得如下推论.

定理 20.1.6 设有 $f : [a, b] \times [c, d] \to \mathbb{R}$. 若对每个 $y \in [c, d]$, $f(\cdot, y)$ 在 $[a, b]$ 上可积, 对每个 $x \in [a, b]$, $f(x, \cdot)$ 在 $[c, d]$ 上 (连续) 可微, 且 $f_y$ 在 $[a, b] \times [c, d]$ 上有界, 对每个 $y \in [c, d]$, $f_y(\cdot, y)$ 在 $[a, b]$ 上可积, 则 $F(y) := \int_a^b f(x, y) \, \mathrm{d}x$ 在 $[c, d]$ 上 (连续) 可微, 且

$$
F ^ {\prime} (y) = \int_ {a} ^ {b} f _ {y} (x, y) \mathrm{d} x. \tag {20.1.13}
$$

证明 任取 $y_0 \in [c, d]$. 由中值定理以及 $f_y$ 在 $[a, b] \times [c, d]$ 上的有界性立即可得 (20.1.10) 式, 从而由定理 20.1.5 得到 $F$ 在 $y_0$ 可微, 且 (20.1.13) 式成立.

若对于固定的 $x \in [a, b]$, $f(x, \cdot)$ 连续可微, 则根据 (20.1.13) 式立即得到 $F'$ 连续. 从而 $F$ 连续可微.

略为令人惊奇的是, 关于累次积分, 有如下的结果.

定理 20.1.7 设函数 f 在  $[a,b]\times[c,d]$  上有界，对于任何  $y\in[c,d]$ ， $f(\cdot,y)$  在  $[a,b]$  上可积，而对于任何  $x\in[a,b]$ ， $f(x,\cdot)$  在  $[c,d]$  上可积。则  $\int_{d}^{c}\mathrm{d}y\int_{a}^{b}f(x,y)\mathrm{d}x$  和  $\int_{a}^{b}\mathrm{d}x\int_{c}^{d}f(x,y)\mathrm{d}y$  都存在，且

$$
\int_ {c} ^ {d} \mathrm{d} y \int_ {a} ^ {b} f (x, y) \mathrm{d} x = \int_ {a} ^ {b} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y. \tag {20.1.14}
$$

证明 由假设条件, 我们知 $\int_{c}^{d} f(x, y) \mathrm{~d}y$ 存在且有界. 进一步, 记

$$
I _ {n, k} = \left[ a + \frac {k (b - a)}{n}, a + \frac {(k + 1) (b - a)}{n} \right], \qquad n \geqslant 1; k = 0, 1, \dots , n - 1,
$$

由引理 20.1.1, 我们有

$$
\begin{array}{l} \int_ {a} ^ {\bar {b}} \left(\int_ {c} ^ {d} f (x, y) \mathrm{d} y\right) \mathrm{d} x - \int_ {a} ^ {b} \left(\int_ {c} ^ {d} f (x, y) \mathrm{d} y\right) \mathrm{d} x \\ = \lim _ {n \rightarrow + \infty} \frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} \sup _ {x \in I _ {n, k}} \int_ {c} ^ {d} f (x, y) \mathrm{d} y - \lim _ {n \rightarrow + \infty} \frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} \inf _ {x \in I _ {n, k}} \int_ {c} ^ {d} f (x, y) \mathrm{d} y \\ = \varliminf_ {n \to + \infty} \frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} \sup _ {x \in I _ {n, k}} \int_ {- c} ^ {d} f (x, y) \mathrm{d} y - \varlimsup_ {n \to + \infty} \frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} \inf _ {x \in I _ {n, k}} \int_ {- c} ^ {- d} f (x, y) \mathrm{d} y \\ \leqslant \varliminf_ {n \to + \infty} \int_ {c} ^ {d} \frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} \sup _ {x \in I _ {n, k}} f (x, y) \mathrm{d} y - \varlimsup_ {n \to + \infty} \int_ {c} ^ {\bar {d}} \frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} \inf _ {x \in I _ {n, k}} f (x, y) \mathrm{d} y \\ \leqslant \varliminf_ {n \to + \infty} \left(\int_ {c} ^ {d} \frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} \sup _ {x \in I _ {n, k}} f (x, y) \mathrm{d} y - \int_ {c} ^ {\bar {d}} \frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} \inf _ {x \in I _ {n, k}} f (x, y) \mathrm{d} y\right) \\ \end{array}
$$

$$
\leqslant \varliminf_ {n \to + \infty} \int_ {- c} ^ {d} \left(\frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} \sup _ {x \in I _ {n, k}} f (x, y) - \frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} \inf _ {x \in I _ {n, k}} f (x, y)\right) \mathrm{d} y = 0.
$$

从而  $\int_{a}^{b}\mathrm{d}x\int_{c}^{d}f(x,y)\mathrm{d}y$  存在.类似地， $\int_{c}^{d}\mathrm{d}y\int_{a}^{b}f(x,y)\mathrm{d}x$  存在.于是由 Arzelà 定理得

$$
\begin{array}{l} \int_ {a} ^ {b} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y = \lim _ {n \to + \infty} \frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} \int_ {c} ^ {d} f \left(a + \frac {k (b - a)}{n}, y\right) \mathrm{d} y \\ = \lim _ {n \to + \infty} \int_ {c} ^ {d} \frac {b - a}{n} \sum_ {k = 0} ^ {n - 1} f \left(a + \frac {k (b - a)}{n}, y\right) \mathrm{d} y \\ = \int_ {c} ^ {d} \mathrm{d} y \int_ {a} ^ {b} f (x, y) \mathrm{d} x. \\ \end{array}
$$

即 (20.1.14) 式成立.

总体上, 含参变量常义积分在思想上可以作为含参变量广义积分的特例来讨论. 因此, 在本节中, 我们仅举一个例题. 关于含参变量积分应用进一步的例题可参看本章 20.3 节以及 20.4 节.

例20.1.1 计算 $\lim_{n\to +\infty}n\int_0^\pi \frac{\sin x}{3 + \cos^2x}\sin \frac{x}{n}\mathrm{d}x.$

解 我们有

$$
\begin{array}{l} \left| \frac {n \sin x}{3 + \cos^ {2} x} \sin \frac {x}{n} \right| \leqslant \frac {x \sin x}{3 + \cos^ {2} x} \leqslant \pi , \quad x \in [ 0, \pi ], \\ \lim _ {n \to + \infty} \frac {n \sin x}{3 + \cos^ {2} x} \sin \frac {x}{n} = \frac {x \sin x}{3 + \cos^ {2} x}, \quad x \in [ 0, \pi ]. \\ \end{array}
$$

因此, 由 Arzelà 有界收敛定理得到

$$
\begin{array}{l} \lim _ {n \to + \infty} n \int_ {0} ^ {\pi} \frac {\sin x}{3 + \cos^ {2} x} \sin \frac {x}{n} \mathrm{d} x \\ = \int_ {0} ^ {\pi} \frac {x \sin x}{3 + \cos^ {2} x} \mathrm{d} x = \frac {\pi}{2} \int_ {0} ^ {\pi} \frac {\sin x}{3 + \cos^ {2} x} \mathrm{d} x \\ = \frac {\pi}{2 \sqrt {3}} \arctan \left. \frac {\cos x}{\sqrt {3}} \right| _ {\pi} ^ {0} = \frac {\sqrt {3}}{1 8} \pi^ {2}. \\ \end{array}
$$

## 习题 20.1

1. 求极限: $\lim_{n\to+\infty}\int_{0}^{\frac{\pi}{2}}\frac{\sin^{n}x+\cos^{n}x}{\sin^{n+1}x+\cos^{n+1}x}\mathrm{d}x.$

2. 证明: 若一列一致有界的函数列 $\{f_n\}$ 处处收敛于 $f$, 则

(1) $\lim_{n\to +\infty}\int_{a}^{\bar{b}}f_n(x)\mathrm{d}x\geqslant \int_{a}^{b}f(x)\mathrm{d}x;$ (2) $\varlimsup_{n\to +\infty}\int_{a}^{b}f_{n}(x)\mathrm{d}x\leqslant \int_{a}^{\bar{b}}f(x)\mathrm{d}x.$

特别地, 当 $f$ 可积时, $\lim_{n\to +\infty}\int_{a}^{b}f_n(x)\mathrm{d}x\leqslant \int_{a}^{b}f(x)\mathrm{d}x\leqslant \lim_{n\to +\infty}\int_{a}^{\bar{b}}f_n(x)\mathrm{d}x.$

3. 说明当 $[a, b]$ 上一致有界的函数列 $\{f_n\}$ 处处收敛到 $f$ 时, 下列两种情形都可能发生:

(1) $\lim_{n\to +\infty}\int_{a}^{\overline{b}}f_n(x)\mathrm{d}x > \int_{a}^{\overline{b}}f(x)\mathrm{d}x;$

(2) $\overline{\lim}_{n\to +\infty}\int_{a}^{\overline{b}}f_n(x)\mathrm{d}x <   \int_{a}^{\overline{b}}f(x)\mathrm{d}x.$

4. 设一列在 $[a, b]$ 上一致有界的可积函数列 $\{f_n\}$ 处处收敛于 $f$, 证明 $\int_{a}^{b} f_n(x) \mathrm{d}x$ 收敛.

5. 设

$$
g (x, y) := \left\{ \begin{array}{l l} {0,} & {x, y \text {均为有理数或均为无理数},} \\ {1,} & {x, y \text {中一个为有理数}, \text {另一个为无理数}.} \end{array} \right.
$$

说明 $\int_0^{\overline{1}}\mathrm{d}x\int_0^1 g(x,y)\mathrm{d}y = 0,$ 而 $\int_0^1\mathrm{d}y\int_0^1 g(x,y)\mathrm{d}x = 1.$

6. 令 $\{a_{n}\}$ 为 $[0,1]$ 中所有有理数的一个排列, 定义

$$
h (x, y) := \left\{ \begin{array}{l l} {1,} & {\text {存在} n \text {使得} x = a _ {n}, y - n \pi \text {为有理数},} \\ {0,} & {\text {其他}.} \end{array} \right.
$$

验证 $\int_0^{\overline{1}}\mathrm{d}x\int_0^{\overline{1}}h(x,y)\mathrm{d}y = 1$ ，而 $\int_0^{\overline{1}}\mathrm{d}y\int_0^{\overline{1}}h(x,y)\mathrm{d}x = 0.$

7. 通过引入参数并利用积分号下求导计算 $\int_0^1\frac{\ln(1 + x)}{1 + x^2}\mathrm{d}x.$

8. 构造 $[0,1]$ 上的函数 $f$, 使得 $\overline{\{(x,f(x))|x\in[0,1]\}} = [0,1]\times [0,1]$.

## 20.2 含参变量广义积分及其一致收敛性

我们在20.1节讨论了含参变量常义积分的性质。对于含参变量广义积分，同样需要考察它们的可积性、连续性和可微性。以含参变量无穷积分的连续性为例，我们来考察什么条件可以保证 $F(y) := \int_{a}^{+\infty} f(x, y) \, \mathrm{d}x$ 连续。

为使 $F$ 连续，对于固定的 $x$ ，假设 $f(x,\cdot)$ 在 $[c,d]$ 上连续是合理的，而对于每个$y\in [c,d]$ ，假设 $f(\cdot ,y)$ 在 $[a, + \infty)$ 上的广义积分收敛则是必需的.若对任何 $A > a,f$ 在 $[a,A]\times [c,d]$ 上有界，则根据定理20.1.4， $\int_{a}^{A}f(x,y)\mathrm{d}x$ 在 $[c,d]$ 上连续.这样，对于

$y_{0}\in [c,d],$

$$
\begin{array}{l} \overline {{\lim _ {y \to y _ {0}}}} \left| \int_ {a} ^ {+ \infty} f (x, y) \mathrm{d} x - \int_ {a} ^ {+ \infty} f (x, y _ {0}) \mathrm{d} x \right| \\ = \varlimsup_ {y \to y _ {0}} \left| \int_ {A} ^ {+ \infty} f (x, y) \mathrm{d} x - \int_ {A} ^ {+ \infty} f (x, y _ {0}) \mathrm{d} x \right| \\ \leqslant 2 \sup _ {y \in E} \left| \int_ {A} ^ {+ \infty} f (x, y) \mathrm{d} x \right|, \quad \forall A > a. \\ \end{array}
$$

这样, 若

$$
\lim _ {A \to + \infty} \sup _ {y \in [ c, d ]} \left| \int_ {A} ^ {+ \infty} f (x, y) \mathrm{d} x \right| = 0, \tag {20.2.1}
$$

我们便可得到 F 的连续性.

若 (20.2.1) 式成立, 则我们称无穷积分 $\int_{a}^{+\infty} f(x,y) \mathrm{d}x$ 关于 $y \in [c,d]$ 一致收敛. 这等价于, $\forall \varepsilon > 0$, 存在 $X > a$, 使得当 $A \geqslant X$ 时, 对任何 $y \in [c,d]$, 成立 $\left|\int_{A}^{+\infty} f(x,y) \mathrm{d}x\right| \leqslant \varepsilon$.

类似地, 可以定义含参变量瑕积分的一致收敛性. 需要注意的是, 在考虑含参变量瑕积分时, 我们需要把 $\sup_{y \in E} |f(\cdot, y)|$ 的瑕点看作含参变量积分 $\int_{a}^{b} f(x, y) \mathrm{d}x$ 的瑕点. 例如, 对于每个 $\alpha > 0$, 积分 $\int_{0}^{1} \frac{\alpha}{x^2 + \alpha^2} \mathrm{~d}x$ 均无瑕点. 由于 $\sup_{\alpha > 0} \frac{\alpha}{x^2 + \alpha^2} = \frac{1}{2x}$, 需要将 0 点看作含参变量积分 $\int_{0}^{1} \frac{\alpha}{x^2 + \alpha^2} \mathrm{~d}x$ 的瑕点. 具体地, 我们定义如下.

定义 20.2.1 设 f 在  $(a, b] \times I$  上有定义. 若对任何  $\delta \in (0, b - a)$ ，都有

$$
\sup _ {(x, \alpha) \in (a, a + \delta) \times I} | f (x, \alpha) | = + \infty , \tag {20.2.2}
$$

则称 $a$ 点为含参变量积分 $\int_{a}^{b}f(x,\alpha)\mathrm{d}x$ 的一个瑕点.

同样, 可以给出 b 点为瑕点或  $c \in (a, b)$  为瑕点的定义.

对于单纯的无穷积分, 定义含参变量积分的一致收敛性如下.

定义 20.2.2 设 f 是  $[a, +\infty) \times I$  上的函数, 对任何 A > a, f 在  $[a, A] \times I$  上有界, 且对任何  $\alpha \in I$ ,  $f(\cdot, \alpha)$  在  $[a, A]$  上 Riemann 可积. 另一方面, 对每个  $\alpha \in I$ , 无穷积分  $\int_{a}^{+\infty} f(x, \alpha) \, dx$  收敛. 若

$$
\lim _ {A \to + \infty} \sup _ {\alpha \in I} \left| \int_ {A} ^ {+ \infty} f (x, \alpha) \mathrm{d} x \right| = 0, \tag {20.2.3}
$$

则称含参变量无穷积分 $\int_{a}^{+\infty}f(x,\alpha)\mathrm{d}x$ 关于 $\alpha \in I$ 一致收敛.

对于有单一瑕点的含参变量瑕积分的一致收敛性, 我们作如下定义.

定义 20.2.3 设 f 是  $(a, b] \times I$  上的函数, 对任何  $\delta \in (0, b - a)$ , f 在  $[a + \delta, b] \times I$  上有界, 且对任何  $\alpha \in I$ ,  $f(\cdot, \alpha)$  在  $[a + \delta, b]$  上 Riemann 可积. 另一方面, 对每个  $\alpha \in I$ , 瑕积分  $\int_{a}^{b} f(x, \alpha) \, dx$  收敛. 若

$$
\lim _ {\delta \to 0 ^ {+}} \sup _ {y \in I} \left| \int_ {a} ^ {a + \delta} f (x, y) \mathrm{d} x \right| = 0, \tag {20.2.4}
$$

则称含参变量积分 $\int_{a}^{b}f(x,y)\mathrm{d}x$ 关于 $y\in I$ 一致收敛.

在上面的定义中, 事实上 $a$ 是唯一可能的瑕点, 但不一定就是瑕点. 鉴于某些情形下不容易判断 $a$ 是否是瑕点, 这样定义含参变量积分 $\int_{a}^{b} f(x, y) \mathrm{d}x$ 的一致收敛性对于今后的讨论是有利的.

若含参变量积分在参数集 I 的一个紧子集上一致收敛, 则称该含参变量积分关于  $\alpha \in I$  内闭一致收敛, 也称局部一致收敛.

容易建立含参变量广义积分一致收敛的判别法. 以下以含参变量无穷积分为例叙述相应定理. 为避免重复叙述, 我们引入如下基本条件.

条件 (E) 函数 $f: [a, +\infty) \times I \to \mathbb{R}$ 满足: 对任何 $A > a$, $f$ 在 $[a, A] \times I$ 上有界, 且对每个 $\alpha \in I$, $f(\cdot, \alpha)$ 在 $[a, A]$ 上 Riemann 可积.

含参变量无穷积分一致收敛的 Cauchy 准则可叙述如下:

定理 20.2.1 函数  $f: [a, +\infty) \times I \rightarrow R$  满足条件 (E)，则含参变量无穷积分  $\int_{a}^{+\infty} f(x, \alpha) \, dx$  关于  $\alpha \in I$  一致收敛当且仅当

$$
\lim_ {A \rightarrow + \infty} \sup_ {\substack {A ^ {\prime \prime}, A ^ {\prime} \geqslant A\\\alpha \in I}} \left| \int_ {X ^ {\prime}} ^ {X ^ {\prime \prime}} f (x, \alpha) \mathrm{d} x \right| = 0. \tag{20.2.5}
$$

即:对任何 $\varepsilon > 0$，存在 $A > a$，使得当 $A'' \geqslant A' \geqslant A$ 时，对任何 $\alpha \in I$

$$
\left| \int_ {A ^ {\prime}} ^ {A ^ {\prime \prime}} f (x, \alpha) \mathrm{d} x \right| <   \varepsilon \tag {20.2.6}
$$

成立.

由 Cauchy 准则立即得到如下的 Weierstrass 判别法, 又称大 $M$ 判别法.

定理 20.2.2 函数 $f: [a, +\infty) \times I \to \mathbb{R}$ 满足条件 (E), 若存在绝对可积函数 $M: [a, +\infty) \to \mathbb{R}$ 使得

$$
\(| f (x, \alpha) | \leqslant M (x), \quad \forall (x, \alpha) \in [ a, + \infty) \times I, \tag {20.2.7}
$$

则含参变量无穷积分 $\int_{a}^{+\infty}f(x,\alpha)\mathrm{d}x$ 关于 $\alpha \in I$ 一致收敛.

注 20.2.1 当使用 Weierstrass 判别法处理含参变量瑕积分时, 不必刻意去关注哪些点是瑕点.

同样, 若在定理 20.2.2 中, 用

$$
| f (x, \alpha) | \leqslant M (x, \alpha), \quad \forall (x, \alpha) \in [ a, + \infty) \times I \tag {20.2.8}
$$

代替 (20.2.7) 式, 而含参变量无穷积分 $\int_{a}^{+\infty} M(x, \alpha) \mathrm{d}x$ 关于 $\alpha \in I$ 一致收敛, 则 $\int_{a}^{+\infty} f(x, \alpha) \mathrm{d}x$ 关于 $\alpha \in I$ 一致收敛.

类似于判断广义积分收敛性的 Abel 判别法和 Dirichlet 判别法, 易建立含参变量广义积分一致收敛性的 Abel 判别法和 Dirichlet 判别法.

定理 20.2.3 设函数 $f,g : \left\lbrack  {a, + \infty }\right)  \times  I \rightarrow  \mathbb{R}$ 满足条件 (E).

(1) (Abel 判别法) 设对每个 $\alpha \in E$, $g(\cdot, \alpha)$ 在 $[a, +\infty)$ 上单调, 且关于 $\alpha \in I$ 一致有界, 即 $g$ 在 $[a, +\infty) \times I$ 上有界. 又设 $\int_{a}^{+\infty} f(x, \alpha) \mathrm{d}x$ 关于 $\alpha \in I$ 一致收敛, 则 $\int_{a}^{+\infty} f(x, \alpha) g(x, \alpha) \mathrm{d}x$ 关于 $\alpha \in I$ 一致收敛.

(2) (Dirichlet 判别法) 若对每个 $\alpha \in I, g(\cdot, \alpha)$ 在 $[a, +\infty)$ 上单调, 且当 $x$ 趋于 $+\infty$ 时, $g(x, \alpha)$ 关于 $\alpha \in I$ 一致趋于零, 即 $\lim_{x \to +\infty} \sup_{\alpha \in I} |g(x, \alpha)| = 0$. 又设对于 $A \in [a, +\infty)$, $\int_{a}^{A} f(x, \alpha) \mathrm{d}x$ 关于 $\alpha \in I$ 一致有界, 则 $\int_{a}^{+\infty} f(x, \alpha) g(x, \alpha) \mathrm{d}x$ 关于 $\alpha \in I$ 一致收敛.

例 20.2.1 考察积分  $\int_{0}^{+\infty}\frac{\alpha}{x^{2}+\alpha^{2}}\mathrm{d}x$  关于  $\alpha>0$  的一致收敛性.

解 易见 0 是该积分唯一的瑕点, 且对任何  $\alpha > 0$ , 积分收敛.

对于 A > 1, 我们有

$$
\sup _ {\alpha > 0} \int_ {A} ^ {+ \infty} \frac {\alpha}{x ^ {2} + \alpha^ {2}} \mathrm{d} x = \sup _ {\alpha > 0} \int_ {\frac {A}{\alpha}} ^ {+ \infty} \frac {1}{x ^ {2} + 1} \mathrm{d} x = \int_ {0} ^ {+ \infty} \frac {1}{x ^ {2} + 1} \mathrm{d} x = \frac {\pi}{2}.
$$

因此, 无穷积分 $\int_{1}^{+\infty}\frac{\alpha}{x^2 + \alpha^2}\mathrm{d}x$ 关于 $\alpha >0$ 非一致收敛.

另一方面, 对于任何 X > 0

$$
\lim _ {A \to + \infty} \sup _ {0 <   \alpha \leqslant X} \int_ {A} ^ {+ \infty} \frac {\alpha}{x ^ {2} + \alpha^ {2}} \mathrm{d} x = \lim _ {A \to + \infty} \int_ {\frac {A}{X}} ^ {+ \infty} \frac {1}{x ^ {2} + 1} \mathrm{d} x = 0.
$$

因此, 无穷积分 $\int_{1}^{+\infty}\frac{\alpha}{x^2 + \alpha^2}\mathrm{d}x$ 关于 $\alpha \in (0,X]$ 一致收敛.

类似地, 对任何 $\alpha_0 > 0$, $\int_{0}^{1} \frac{\alpha}{x^2 + \alpha^2} \mathrm{d}x$ 关于 $\alpha \geqslant \alpha_0$ 一致收敛. 而 $\int_{0}^{1} \frac{\alpha}{x^2 + \alpha^2} \mathrm{d}x$

关于  $\alpha > 0$  非一致收敛 $^{①}$ .

总之，$\int_{0}^{+\infty}\frac{\alpha}{x^2 + \alpha^2}\mathrm{d}x$ 关于 $\alpha \in (0, + \infty)$ 内闭一致收敛，但非一致收敛.

![](images/page_761_image_4.jpg)

例20.2.2 考察积分 $\int_0^{+\infty}\frac{\sin x}{x}\mathrm{e}^{-\alpha x}\mathrm{d}x$ 关于 $\alpha \geqslant 0$ 的一致收敛性.

解 由于 $\int_0^{+\infty}\frac{\sin x}{x}\mathrm{d}x$ 收敛且不含 $\alpha$ ，该积分自然关于 $\alpha \geqslant 0$ 一致收敛.

而对于固定的 $\alpha \geqslant 0, \mathrm{e}^{-\alpha x}$ 关于 $x$ 单调. 又 $0 \leqslant \mathrm{e}^{-\alpha x} \leqslant 1$, 因此 $\mathrm{e}^{-\alpha x}$ 在 $[0, +\infty)$ 上关于 $\alpha \geqslant 0$ 一致有界. 于是由Abel判别法, $\int_0^{+\infty} \frac{\sin x}{x} \mathrm{e}^{-\alpha x} \mathrm{d}x$ 关于 $\alpha \geqslant 0$ 一致收敛. □

例 20.2.3 考察积分  $\int_{0}^{+\infty} e^{-\alpha x} \sin x \, dx$  关于  $\alpha > 0$  的一致收敛性.

解 对任何 $A > 0$, $\left|\int_0^A \sin x \, \mathrm{d}x\right| \leqslant 2$. 固定 $\alpha_0 > 0$, 则 $\mathrm{e}^{-\alpha x}$ 是 $(x, \alpha) \in [0, +\infty) \times [\alpha_0, +\infty)$ 的有界函数. 进一步, $\mathrm{e}^{-\alpha x}$ 关于 $x$ 单减, 且当 $x \to +\infty$ 时, 关于 $\alpha \geqslant \alpha_0$ 一致地趋于零. 因此, 由 Dirichlet 判别法, $\int_0^{+\infty} \mathrm{e}^{-\alpha x} \sin x \, \mathrm{d}x$ 关于 $\alpha > \alpha_0$ 一致收敛.

另一方面, 对于任何  $n \geqslant 1$ ,

$$
\sup _ {\alpha > 0} \left| \int_ {n \pi} ^ {(n + 1) \pi} \mathrm{e} ^ {- \alpha x} \sin x \mathrm{d} x \right| = \sup _ {\alpha > 0} \int_ {0} ^ {\pi} \mathrm{e} ^ {- \alpha (x + n \pi)} \sin x \mathrm{d} x \geqslant \sup _ {\alpha > 0} 2 \mathrm{e} ^ {- \alpha (n + 1) \pi} = 2.
$$

因此， $\int_0^{+\infty}\mathrm{e}^{-\alpha x}\sin x\mathrm{d}x$ 关于 $\alpha >0$ 非一致收敛.

![](images/page_761_image_13.jpg)

例 20.2.4 考察积分  $\int_{0}^{\pi}\ln(1-2\alpha\cos x+\alpha^{2})\mathrm{d}x$  关于  $\alpha\in R$  的一致收敛性.

解 按含参变量积分瑕点的定义, $[0, \pi]$ 中的所有点均为该含参变量积分 (参变量 $\alpha \in \mathbb{R}$) 的瑕点. 对于这种瑕点如此多的含参变量瑕积分, 如何定义一致收敛性是一个问题. 因此, 采用定义 20.2.1 给我们带来一些不便. 但那样定义瑕点还是有必要的.

任取 $x_0 \in [0, \pi]$, 均有

$$
\sup _ {\alpha \in \mathbb {R}} \left| \int_ {[ x _ {0} - \delta , x _ {0} + \delta ]} \ln (1 - 2 \alpha \cos x + \alpha^ {2}) \mathrm{d} x \right| = + \infty , \qquad \forall   \delta > 0.
$$

因此, 认为 $\int_0^\pi \ln (1 - 2\alpha \cos x + \alpha^2) \, \mathrm{d}x$ 关于 $\alpha \in \mathbb{R}$ 非一致收敛是自然的.

本例中, 使 $[0, \pi]$ 中的点都成为瑕点的原因在于 $\alpha$ 的取值无界. 在有界范围内, 即对于 $A > 0$, 当只考虑 $\alpha \in [-A, A]$ 时, 含参变量积分 $\int_{0}^{\pi} \ln (1 - 2\alpha \cos x + \alpha^{2}) \mathrm{d}x$ 可能的瑕点只有 $0, \pi$. 此时, 由

$$
\sin^ {2} x \leqslant 1 - 2 \alpha \cos x + \alpha^ {2} \leqslant (1 + A) ^ {2}, \quad \forall x \in [ 0, \pi ], \alpha \in [ - A, A ]
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 值得注意的是, $\int_0^{+\infty}\frac{\alpha}{x^2 + \alpha^2}\mathrm{d}x = \frac{\pi}{2} (\forall \alpha >0)$</span></small>

得到

$$
\left| \ln (1 - 2 \alpha \cos x + \alpha^ {2}) \right| \leqslant 2 \ln (1 + A) + 2 \left| \ln \sin x \right|, \quad \forall x \in (0, \pi), \alpha \in [ - A, A ].
$$

由 $\int_0^\pi (2\ln (1 + A) + 2|\ln \sin x|)\mathrm{d}x$ 收敛以及Weierstrass判别法得到 $\int_0^\pi \ln (1 - 2\alpha \cos x + \alpha^2)\mathrm{d}x$ 关于 $\alpha \in [-A,A]$ 一致收敛.

总之, $\int_0^\pi \ln (1 - 2\alpha \cos x + \alpha^2)\mathrm{d}x$ 关于 $\alpha \in \mathbb{R}$ 内闭一致收敛,但非一致收敛. □

## 习题20.2

1. 证明以下含参变量积分关于所考虑的参数内闭一致收敛,但非一致收敛:

(1) $\int_0^{+\infty} x^{\alpha - 1} \mathrm{e}^{-x} \, \mathrm{d}x, \quad \alpha > 0;$
(2) $\int_{0}^{+\infty} x^{\alpha - 1} \mathrm{e}^{-x} \ln^{3} x \, \mathrm{d}x, \quad \alpha > 0;$
(3) $\int_{0}^{1} x^{p-1}(1 - x)^{q-1} \, \mathrm{d}x, \quad p, q > 0;$
(4) $\int_0^1 x^{p - 1}(1 - x)^{q - 1}(\ln x)\ln^2 (1 - x)\mathrm{d}x,\quad p,q > 0;$
(5) $\int_{0}^{+\infty}\alpha \mathrm{e}^{-\alpha x}\mathrm{d}x,\quad \alpha >0;$
(6) $\int_{0}^{+\infty}\alpha \mathrm{e}^{-\alpha^2 x^2}\mathrm{d}x,\quad \alpha >0.$

2. 考察以下含参变量积分关于所考虑的参数的一致收敛性 $^{①}$ :

(1) $\int_0^1\frac{\ln x}{x}\sin \frac{1}{x^\beta}\mathrm{d}x,\quad \beta >0;$
(2) $\int_{0}^{1} x^{\alpha} \sin \frac{1}{x^{\beta}} \, \mathrm{d}x, \quad \alpha > -2, \beta > 0;$
(3) $\int_{1}^{+\infty}\frac{y^2 - x^2}{(x^2 + y^2)^2}\mathrm{d}x,\quad y\in \mathbb{R};$
(4) $\int_0^1\frac{y^2 - x^2}{(x^2 + y^2)^2}\mathrm{d}x,\quad y > 0.$

3. 设 $f \in C(0, +\infty)$, $\int_{0}^{+\infty} t^{\lambda} f(t) \, \mathrm{d}t$ 当 $\lambda = a, \lambda = b$ 时都收敛. 证明: $\int_{0}^{+\infty} t^{\lambda} f(t) \, \mathrm{d}t$ 关于 $\lambda \in [a, b]$ 一致收敛.

4. 考察使得以下积分收敛的参数  $\alpha, p, q$  以及积分一致收敛的范围:

(1) $\int_{0}^{1} x^{\alpha} \sin \left( x^{p} + \frac{1}{x^{q}} \right) \, \mathrm{d}x;$
(2) $\int_{1}^{+\infty} x^{\alpha} \sin \left( x^{p} + \frac{1}{x^{q}} \right) \, \mathrm{d}x.$

5. 试讨论变量代换对于广义积分收敛性与一致收敛性的影响.

## 20.3 含参变量广义积分的基本性质

本节主要介绍含参变量广义积分的连续性, 可微性以及可积性. 我们将主要以含参变量无穷积分为例叙述相关结果.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 习题中讨论一致收敛性需包括内闭一致收敛性,或者说需要讨论关于一致收敛性能够得到的最好结果.</span></small>

首先我们将 Arzelà 有界收敛定理推广为如下的控制收敛定理.

定理 20.3.1 设 $\{f_n\}$ 为 $[a, +\infty)$ 上的函数列. 满足如下条件:

(1) 存在 $[a, +\infty)$ 上绝对可积的函数 $\varphi$ (允许个别点上取值为 $+\infty$) 使得

$$
\(| f _ {n} (x) | \leqslant \varphi (x), \quad \forall x \in [ a, + \infty), n \geqslant 1; \tag {20.3.1}
$$

(2)

$$
\lim _ {n \to + \infty} f _ {n} (x) = f (x), \quad \forall x \in [ a, + \infty) \tag {20.3.2}
$$

成立, 其中 $f$ 在一些点上可以取值为 $\pm \infty$;

(3) 在不含  $\varphi$  的瑕点的有界闭区间上,  $f_{n}(n \geqslant 1)$  均 Riemann 可积;
(4) 在不含  $\varphi$  的瑕点的有界闭区间上, f Riemann 可积,

则 $\int_{a}^{+\infty}f_n(x)\mathrm{d}x(n\geqslant 1)$ 以及 $\int_{a}^{+\infty}f(x)\mathrm{d}x$ 均收敛，且

$$
\lim _ {n \to + \infty} \int_ {a} ^ {+ \infty} f _ {n} (x) \mathrm{d} x = \int_ {a} ^ {+ \infty} f (x) \mathrm{d} x. \tag {20.3.3}
$$

证明 不失一般性, 设 $a$ 为 $\varphi$ 唯一可能的瑕点. 从而对任何 $A > c > a$, $\varphi$ 在 $[c, A]$ 上有界. 进而 $\{f_n\}$ 在 $[c, A]$ 上一致有界.

结合 (20.3.1) 式和 (20.3.2) 式可得

$$
| f (x) | \leqslant \varphi (x), \quad \forall x \in [ a, + \infty).
$$

因此, 由 Cauchy 准则, $\int_{a}^{+\infty} f_n(x) \mathrm{d}x (n \geqslant 1)$ 与 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 均收敛. 进一步, 对于 $A > c > a$, 我们有

$$
\begin{array}{l} \left| \int_ {a} ^ {+ \infty} f _ {n} (x) \mathrm{d} x - \int_ {a} ^ {+ \infty} f (x) \mathrm{d} x \right| \\ \leqslant \left| \int_ {c} ^ {A} f _ {n} (x) \mathrm{d} x - \int_ {c} ^ {A} f (x) \mathrm{d} x \right| + 2 \int_ {A} ^ {+ \infty} \varphi (x) \mathrm{d} x + 2 \int_ {a} ^ {c} \varphi (x) \mathrm{d} x. \\ \end{array}
$$

由 Arzelà 有界收敛定理,

$$
\varlimsup_ {n \to + \infty} \left| \int_ {a} ^ {+ \infty} f _ {n} (x) \mathrm{d} x - \int_ {a} ^ {+ \infty} f (x) \mathrm{d} x \right| \leqslant 2 \int_ {A} ^ {+ \infty} \varphi (x) \mathrm{d} x + 2 \int_ {a} ^ {c} \varphi (x) \mathrm{d} x.
$$

上式中令  $A \rightarrow +\infty, c \rightarrow a^{+}$  即得 (20.3.3) 式.

定理 20.3.1 可以视为 Lebesgue 控制收敛定理的特例. Riemann 积分的一个缺陷是可积函数列的极限函数, 即使有界也不一定可积. 在定理 20.3.1 的条件中, 条件 (1)—(3) 不足以保证 (4) 成立. 而对于 Lebesgue 积分, f 的 Lebesgue 可积性是自然的.

要保证定理中的 (4) 成立, 一个常用的充分条件是 $\{f_n\}$ 在不包含 $\varphi$ 的瑕点的有界闭集上一致收敛于 $f$. 但时常在应用中, 可以得到 $f$ 的表达式, 从而可以方便地得到它在不含瑕点的有界闭集上的 Riemann 可积性. 此时, 我们就可以方便地运用定理 20.3.1.

定理 20.3.1 中的  $\varphi$  称为控制函数. 控制函数的存在保证了含参变量积分的一致收敛性. 存在控制函数这一条件可以替换为含参变量积分的一致收敛性. 以含参变量无穷积分为例, 我们有如下定理.

定理 20.3.2 设  $\{f_{n}\}$  为  $[a, +\infty)$  上的函数列. 满足如下条件:

(1) 对任何 $A > a, \{f_n\}$ 在 $[a, A]$ 上可积, 且一致有界, $f$ 在 $[a, A]$ 上可积; (2)

$$
\lim _ {n \to + \infty} f _ {n} (x) = f (x), \quad \forall x \in [ a, + \infty) \tag {20.3.4}
$$

成立;

(3) $\int_{a}^{+\infty}f_n(x)\mathrm{d}x$ 关于 $n\geqslant 1$ 一致收敛，

则  $\int_{a}^{+\infty}f(x)\mathrm{d}x$  收敛, 且 (20.3.3) 式成立.

证明 定理的证明与定理20.3.1的证明主要不同在于没有控制函数, $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 的收敛性需要更细致的证明. 对于 $A > a$, 我们有

$$
\begin{array}{l} \int_ {a} ^ {+ \infty} f _ {n} (x) \mathrm{d} x = \int_ {a} ^ {A} f _ {n} (x) \mathrm{d} x + \int_ {A} ^ {+ \infty} f _ {n} (x) \mathrm{d} x \\ \leqslant \int_ {a} ^ {A} f _ {n} (x) \mathrm{d} x + \sup _ {k \geqslant 1} \left| \int_ {A} ^ {+ \infty} f _ {k} (x) \mathrm{d} x \right|, \quad \forall n \geqslant 1. \\ \end{array}
$$

于是, 由 Arzelà 有界收敛定理,

$$
\varlimsup_ {n \to + \infty} \int_ {a} ^ {+ \infty} f _ {n} (x) \mathrm{d} x \leqslant \int_ {a} ^ {A} f (x) \mathrm{d} x + \sup _ {k \geqslant 1} \left| \int_ {A} ^ {+ \infty} f _ {k} (x) \mathrm{d} x \right|.
$$

因此，由一致收敛性， $\lim_{n\to +\infty}\int_{a}^{+\infty}f_n(x)\mathrm{d}x <   + \infty$ ，且

$$
\varlimsup_ {n \to + \infty} \int_ {a} ^ {+ \infty} f _ {n} (x)   \mathrm{d} x \leqslant \varliminf_ {A \to + \infty} \int_ {a} ^ {A} f (x)   \mathrm{d} x.
$$

同理， $\lim_{n\to +\infty}\int_{a}^{+\infty}f_n(x)\mathrm{d}x > - \infty$ ，且

$$
\varliminf_ {n \to + \infty} \int_ {a} ^ {+ \infty} f _ {n} (x)   \mathrm{d} x \geqslant \varlimsup_ {A \to + \infty} \int_ {a} ^ {A} f (x)   \mathrm{d} x.
$$

于是，必有

$$
\begin{array}{l} \varlimsup_ {n \to + \infty} \int_ {a} ^ {+ \infty} f _ {n} (x) \mathrm{d} x = \varliminf_ {A \to + \infty} \int_ {a} ^ {A} f (x) \mathrm{d} x \\ = \varliminf_ {n \to + \infty} \int_ {a} ^ {+ \infty} f _ {n} (x) \mathrm{d} x = \varlimsup_ {A \to + \infty} \int_ {a} ^ {A} f (x) \mathrm{d} x \in \mathbb {R}. \\ \end{array}
$$

即  $\int_{a}^{+\infty}f(x)\mathrm{d}x$  收敛, 且 (20.3.3) 式成立.

结合 Heine 定理, 由定理 20.3.2 立即可得含参变量积分的连续性定理.

定理 20.3.3 设  $y_{0} \in [c, d]$ ,  $f : [a, +\infty) \times [c, d] \rightarrow R$  满足如下条件:

(1) 对任何 $A > a, f$ 在 $[a, A] \times [c, d]$ 上有界. 进一步, 对任何 $y \in [c, d], f(\cdot, y)$ 在 $[a, A]$ 上可积;
(2) 对每个  $x \in [a, +\infty)$ ,  $f(x, \cdot)$  在  $y_{0}$  处连续;
(3) $\int_{a}^{+\infty} f(x, y) \, \mathrm{d}x$ 关于 $y \in [c, d]$ 一致收敛,
则 $F(y) = \int_{a}^{+\infty}f(x,y)\mathrm{d}x$ 在 $y_0$ 处连续.

类似地, 可以得到如下关于含参变量积分的微分性质.

定理 20.3.4 设  $y_{0} \in [c, d]$ ,  $f : [a, +\infty) \times [c, d] \to R$  满足如下条件:

(1) 对每个  $x \in [a, +\infty)$ ,  $f(x, \cdot)$  在  $[c, d]$  上可微;
(2) 对任何 $A > a, f_y$ 在 $[a, A] \times [c, d]$ 上有界. 进一步, 对任何 $y \in [c, d], f(\cdot, y), f_y(\cdot, y)$ 在 $[a, A]$ 上 Riemann 可积;
(3) $\int_{a}^{+\infty} f(x, y_0) \, \mathrm{d}x$ 收敛;
(4) $\int_{a}^{+\infty}f_{y}(x,y)\mathrm{d}x$ 关于 $y\in [c,d]$ 一致收敛，

则  $\int_{a}^{+\infty}f(x,y)\mathrm{d}x$  关于  $y\in[c,d]$  一致收敛，而  $F(y):=\int_{a}^{+\infty}f(x,y)\mathrm{d}x$  在  $[c,d]$  上可微，且

$$
F ^ {\prime} (y) = \int_ {a} ^ {+ \infty} f _ {y} (x, y) \mathrm{d} x, \quad \forall y \in [ a, b ]. \tag {20.3.5}
$$

证明 由定理20.1.6, 对任何 $A > B > a, y \mapsto \int_{B}^{A} f(x, y) \, \mathrm{d}x$ 在 $[c, d]$ 上可微. 从而, 对任何 $y \in [c, d]$, 我们有 $\xi \in (c, d)$ 使得

$$
\begin{array}{l} \left| \int_ {B} ^ {A} \frac {f (x , y) - f (x , y _ {0})}{y - y _ {0}} \mathrm{d} x \right| = \left| \frac {\int_ {B} ^ {A} f (x , y) \mathrm{d} x - \int_ {B} ^ {A} f (x , y _ {0}) \mathrm{d} x}{y - y _ {0}} \right| \\ = \left| \int_ {B} ^ {A} f _ {y} (x, \xi) \mathrm{d} x \right| \leqslant \sup _ {z \in [ c, d ]} \left| \int_ {B} ^ {A} f _ {y} (x, z) \mathrm{d} x \right|. \\ \end{array}
$$

由Cauchy准则和 $\int_{a}^{+\infty}f_{y}(x,y)\mathrm{d}x$ 关于 $y\in [c,d]$ 的一致收敛性得到

$$
\int_ {a} ^ {+ \infty} \frac {f (x , y) - f (x , y _ {0})}{y - y _ {0}} \mathrm{d} x
$$

关于 $y \in [c, d] \setminus \{y_0\}$ 一致收敛. 进而又有 $\int_{a}^{+\infty} f(x, y) \, \mathrm{d}x$ 关于 $y \in [c, d]$ 一致收敛.

于是由定理 20.3.3 即得 F 可微且 (20.3.5) 式成立.

对应于单点可微情形, 我们有

定理 20.3.5 设 $y_0 \in [c, d], f: [a, +\infty) \times [c, d] \to \mathbb{R}$ 满足如下条件:

(1) 对每个  $x \in [a, +\infty)$ ,  $f(x, \cdot)$  在  $y_{0}$  处可微;
(2) 对任何 $A > a$, $\frac{f(x,y) - f(x,y_0)}{y - y_0}$ 在 $[a,A] \times ([c,d] \setminus \{y_0\})$ 上有界. 进一步, 对任何 $y \in [c,d]$, $f(\cdot,y), f_y(\cdot,y_0)$ 在 $[a,A]$ 上可积;
(3) $\int_{a}^{+\infty}f(x,y_0)\mathrm{d}x$ 收敛;
(4) $\int_{a}^{+\infty}\frac{f(x,y) - f(x,y_0)}{y - y_0}\mathrm{d}x$ 关于 $y\in [c,d]\setminus \{y_0\}$ 一致收敛,

则 $F(y) := \int_{a}^{+\infty} f(x, y) \, \mathrm{d}x$ 在 $y_0$ 处可微，且

$$
F ^ {\prime} (y _ {0}) = \int_ {a} ^ {+ \infty} f _ {y} (x, y _ {0}) \mathrm{d} x. \tag {20.3.6}
$$

对于含参变量积分的积分, 容易就含参变量广义积分的常义积分得到积分次序的可交换性.

定理 20.3.6 设  $f: [a, +\infty) \times [c, d] \rightarrow R$  满足如下条件:

(1) 对任何 $A > a, f$ 在 $[a, A] \times [c, d]$ 上有界. 对任何 $y \in [c, d], f(\cdot, y)$ 在 $[a, A]$ 上可积;
(2) 对任何  $x \in [a, +\infty)$ ,  $f(x, \cdot)$  在  $[c, d]$  上可积;
(3) $\int_{a}^{+\infty} f(x, y) \, \mathrm{d}x$ 关于 $y \in [c, d]$ 一致收敛.

令 $\varphi(y) := \int_{a}^{+\infty} f(x, y) \, \mathrm{d}x$, $\psi(x) := \int_{c}^{d} f(x, y) \, \mathrm{d}y$, 则 $\int_{a}^{+\infty} \psi(x) \, \mathrm{d}x$ 收敛, $\int_{c}^{d} \varphi(y) \, \mathrm{d}y$ 存在, 且两者相等, 即

$$
\int_ {a} ^ {+ \infty} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y = \int_ {c} ^ {d} \mathrm{d} y \int_ {a} ^ {+ \infty} f (x, y) \mathrm{d} x. \tag {20.3.7}
$$

证明 由一致收敛性, 存在 $X > a$ 使得

$$
\left| \varphi (y) \right| \leqslant \left| \int_ {a} ^ {X} f (x, y) \mathrm{d} x \right| + 1, \quad \forall y \in [ c, d ].
$$

即 $\varphi$ 在 $[c,d]$ 上有界. 事实上, $\varphi$ 有界的结论也包含在以下的证明之中.

任取 A > a，由定理 20.1.7，我们有

$$
\begin{array}{l} \int_ {c} ^ {\bar {d}} \left(\int_ {a} ^ {+ \infty} f (x, y) \mathrm{d} x\right) \mathrm{d} y \leqslant \int_ {c} ^ {d} \left(\int_ {a} ^ {A} f (x, y) \mathrm{d} x\right) \mathrm{d} y + \int_ {c} ^ {\bar {d}} \left(\int_ {A} ^ {+ \infty} f (x, y) \mathrm{d} x\right) \mathrm{d} y \\ \leqslant \int_ {a} ^ {A} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y + (d - c) \sup _ {y \in [ c, d ]} \left| \int_ {A} ^ {+ \infty} f (x, y) \mathrm{d} x \right|. \\ \end{array}
$$

由一致收敛性得到

$$
\int_ {c} ^ {\bar {d}} \left(\int_ {a} ^ {+ \infty} f (x, y) \mathrm{d} x\right) \mathrm{d} y \leqslant \varliminf_ {A \to + \infty} \int_ {a} ^ {A} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y.
$$

同理，

$$
\int_ {c} ^ {d} \left(\int_ {a} ^ {+ \infty} f (x, y) \mathrm{d} x\right) \mathrm{d} y \geqslant \varlimsup_ {A \to + \infty} \int_ {a} ^ {A} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y.
$$

因此，必有

$$
\begin{array}{l} \int_ {c} ^ {\bar {d}} \left(\int_ {a} ^ {+ \infty} f (x, y) \mathrm{d} x\right) \mathrm{d} y = \varliminf_ {A \to + \infty} \int_ {a} ^ {A} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y \\ = \int_ {c} ^ {d} \left(\int_ {a} ^ {+ \infty} f (x, y) \mathrm{d} x\right) \mathrm{d} y = \varlimsup_ {A \to + \infty} \int_ {a} ^ {A} \mathrm{d} x \int_ {c} ^ {d} f (x, y) \mathrm{d} y. \\ \end{array}
$$

即 $\int_{a}^{+\infty}\psi (x)\mathrm{d}x$ 收敛， $\int_c^d\varphi (y)\mathrm{d}y$ 存在，且两者相等.

以上证明与定理 20.3.2 的证明非常相似. 事实上, 定理 20.3.6 可以视为定理 20.3.2 的推论.

对于含参变量广义积分的无穷积分, 目前要建立相关定理, 条件繁杂且证明不易. 而今后在 Lebesgue 积分意义下, 在 $f$ Lebesgue 可测的前提下, 只要积分 $\int_{c}^{+\infty} \mathrm{d}y \int_{a}^{+\infty} |f(x,y)| \mathrm{~d}x$ 有限, 便可得 $\int_{c}^{+\infty} \mathrm{d}y \int_{a}^{+\infty} f(x,y) \mathrm{~d}x$ 以及 $\int_{a}^{+\infty} \mathrm{d}x \int_{c}^{+\infty} f(x,y) \mathrm{~d}y$ 均收敛且相等.

因此, 对于含参变量广义积分的无穷积分, 我们暂不讨论一般性的结果. 对于特殊的问题, 先采取特殊问题特殊分析.

容易构造二次无穷积分积分次序不可交换的例子.

例 20.3.1 如图 20.1, 考虑

$$
f (x, y) := \left\{ \begin{array}{l l} 1, & (x, y) \in \bigcup_ {n = 0} ^ {\infty} [ n, n + 1) \times [ n, n + 1), \\ - 1, & (x, y) \in \bigcup_ {n = 0} ^ {\infty} [ n, n + 1) \times [ n + 1, n + 2), \\ 0, & \text {其他.} \end{array} \right. \tag {20.3.8}
$$