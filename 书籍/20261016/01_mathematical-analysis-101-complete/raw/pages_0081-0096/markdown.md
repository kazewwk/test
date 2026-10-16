根据定义, $\mathbb{R}$ 被分成两两不交的三部分: 内部、外部和边界.

另一方面, 我们定义

定义 3.3.2 设  $E \subseteq R$ .

(1) 若对任何 $\delta > 0$, $(x_0 - \delta, x_0 + \delta) \cap E$ 为无限集, 则称 $x_0$ 为 $E$ 的聚点, 又称为极限点. $E$ 的极限点全体称为 $E$ 的导集, 记作 $E'$.
(2) 若存在 $\delta > 0$ 使得 $(x_0 - \delta, x_0 + \delta) \cap E = \{x_0\}$, 则称 $x_0$ 为 $E$ 的孤立点.

定理 3.3.5 若对任何  $\delta > 0, (x_{0} - \delta, x_{0} + \delta)$  内包含 E 中异于  $x_{0}$  的点，则  $x_{0}$  为 E 的聚点.

证明 任取 $\delta > 0$. 由假设, 存在 $x_{1} \in (x_{0} - \delta, x_{0} + \delta) \cap E$, 且 $x_{1} \neq x_{0}$. 从而 $\delta_{1} := |x_{1} - x_{0}| > 0$.

于是, 又有 $x_{2} \in (x_{0} - \delta_{1}, x_{0} + \delta_{1}) \cap E$, 满足 $x_{2} \neq x_{0}$. 依次可以找到 $E$ 中点列 $\{x_{n}\}$ 满足 $0 < |x_{n+1} - x_{0}| < |x_{n} - x_{0}| < \delta$. 所以 $(x_{0} - \delta, x_{0} + \delta)$ 内包含了 $E$ 中无限多个点. 即 $x_{0}$ 是 $E$ 的聚点. □

在以上定义的基础上, 我们可以给出 $\mathbb{R}$ 的另一种分类: $\mathbb{R}$ 按 $E$ 的导集、孤立点全体以及外部, 分成两两不交的三部分.

接下来我们引入开集和闭集.

定义 3.3.3 若 E 中的点都是其内点, 即  $E = E^{\circ}$ , 则称 E 为开集.

若 E 包含其所有聚点, 即  $E' \subseteq E$ , 则称 E 为闭集.

根据定义, $\varnothing$ 与 $\mathbb{R}$ 既是开集又是闭集. 今后我们将证明这也是 $\mathbb{R}$ 中仅有的两个既是开集又是闭集的集合.

由定义易见集合的内部是开集. 自然, 它的外部也是开集.

以下定理所列条件是集合为闭集的充要条件, 均可作为闭集的等价定义. 也是判断集合是否为闭集的最常用条件.

定理 3.3.6 设  $E \subseteq R$ . 则 E 为闭集当且仅当以下任一条件成立:

(1)  $\partial E \subseteq E;$
(2) CE 为开集;
(3) E 中任何收敛点列的极限均属于 E.

证明 由边界点与聚点的定义易见, 若 $x_0 \notin F$, 则 $x_0$ 是 $F$ 的边界点当且仅当它是 $F$ 的聚点. 即

$$
\mathscr {C} F \cap \partial F = \mathscr {C} F \cap F ^ {\prime}. \tag {3.3.9}
$$

(1) 由 (3.3.9) 式即得 E 为闭集, 即  $E' \subseteq E$  当且仅当  $\partial E \subseteq E$ .
(2) 由于 $\partial E = \partial (\mathscr{C}E)$, 由 (1), $E$ 为闭集当且仅当 $\mathscr{C}E \cap \partial (\mathscr{C}E) = \varnothing$. 注意到总有 $(\mathscr{C}E)^{\circ} \subseteq \mathscr{C}E \subseteq (\mathscr{C}E)^{\circ} \cup \partial (\mathscr{C}E)$, 可见 $E$ 为闭集等价于 $\mathscr{C}E = (\mathscr{C}E)^{\circ}$, 即 $\mathscr{C}E$ 为开集.

(3) 若 $E$ 是闭集, 设 $E$ 中点列 $\{x_k\}$ 收敛到 $x_0$, 则当集合 $F := \{x_k | k \geqslant 1\}$ 为有限集时, 必有 $x_0 \in F$, 从而 $x_0 \in E$; 当 $F$ 为无限集时, 必有 $x_0 \in E'$, 从而也有 $x_0 \in E$.

另一方面, 若 $E$ 中收敛点列 $\{x_k\}$ 的极限总是属于 $E$, 则对任何 $x_0 \in E'$ 以及 $k \geqslant 1$, 存在 $x_k \in \left(x_0 - \frac{1}{k}, x_0 + \frac{1}{k}\right) \cap E$. 由此 $\{x_k\}$ 是 $E$ 中收敛到 $x_0$ 的点列, 所以 $x_0 \in E$, 从而 $E$ 为闭集.

对于开集, 有如下重要性质.

定理 3.3.7 (1) 任意个开集的并是开集;

(2) 任意有限个开集的交是开集.

证明 (1) 设 $\{V_{\alpha} | \alpha \in I\}$ 是开集族①, 我们要证 $V := \bigcup_{\alpha \in I} V_{\alpha}$ 是开集.

任取 $x \in V$, 我们有 $\alpha \in I$ 使得 $x \in V_{\alpha}$. 由于 $V_{\alpha}$ 为开集, 存在 $\delta > 0$ 使得 $(x - \delta, x + \delta) \subset V_{\alpha} \subseteq V$. 因此, $V$ 为开集.

(2) 设  $m \geqslant 1, V_{1}, V_{2}, \cdots, V_{m}$  为开集, 我们要证  $V := \bigcap_{1 \leqslant k \leqslant m} V_{k}$  是开集.

任取 $x \in V$, 则对于 $1 \leqslant k \leqslant m$, 都有 $x \in V_k$. 从而有 $\delta_k > 0$ 使得 $(x - \delta_k, x + \delta_k) \subset V_k$. 取 $\delta = \min_{1 \leqslant k \leqslant m} \delta_k$, 则 $\delta > 0$, 且 $(x - \delta, x + \delta) \subset V$. 因此, $V$ 为开集.

结合定理 3.3.6 (2) 和 De Morgan 定律可得如下定理.

定理 3.3.8 (1) 任意个闭集的交是闭集;

(2) 任意有限个闭集的并是闭集.

由定理3.3.8中的(1)以及 $\mathbb{R}$ 本身为闭集, 可见对于任何 $E \subseteq \mathbb{R}$, 集合 $\cap \{F | E \subseteq F \subseteq \mathbb{R}, F$ 为闭集} 是包含 $E$ 的最小闭集. 我们定义如下.

定义 3.3.4 称包含 E 的最小闭集为 E 的闭包, 记作  $\overline{E}$ .

不难证明

$$
\overline {{E}} = E \cup E ^ {\prime} = E \cup \partial E = \mathscr {C} (\mathscr {C} E) ^ {\circ}. \tag {3.3.10}
$$

我们把证明留给读者.

最后, 我们引入稠密性的概念.

定义3.3.5 (1) 若 $E \subseteq F \subseteq \overline{E}$, 则称 $E$ 在 $F$ 中稠密;

(2) 如果 $E$ 的闭包没有内点, 则称 $E$ 为无处稠密集, 又称疏朗集.

## 3.3.5 致密性定理与聚点原则

致密性定理是一个非常常用的定理, 而聚点原则与它之间的等价性非常直接.

定理 3.3.9 R 中任何有界无限集均有聚点.

证明 设 $E \subseteq \mathbb{R}$ 是有界无限集. 则有有界区间 $[a_1, b_1] \subseteq \mathbb{R}$ 使得 $E \subseteq [a_1, b_1]$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 不能按以下方式设: 设 $\{V_{n} | n \geqslant 1\}$ 为开集族.</span></small>

由于 $E$ 是无限集, 因此 $\left[a_1, \frac{a_1 + b_1}{2}\right] \cap E$ 与 $\left[\frac{a_1 + b_1}{2}, b_1\right] \cap E$ 至少有一个为无限集. 若 $\left[a_1, \frac{a_1 + b_1}{2}\right] \cap E$ 为无限集, 则令 $[a_2, b_2]$ 为 $\left[a_1, \frac{a_1 + b_1}{2}\right]$. 否则令 $[a_2, b_2]$ 为 $\left[\frac{a_1 + b_1}{2}, b_1\right]$. 这样 $[a_2, b_2] \subseteq [a_1, b_1], [a_2, b_2] \cap E$ 为无限集, 且 $b_2 - a_2 = \frac{b_1 - a_1}{2}$.

一般地, 若对于 $n \geqslant 2$, 已经取定 $[a_n, b_n]$ 使得 $[a_n, b_n] \cap E$ 为无限集. 则类似地可以取到 $[a_{n+1}, b_{n+1}] \subseteq [a_n, b_n]$, 使得 $[a_{n+1}, b_{n+1}] \cap E$ 为无限集, $b_{n+1} - a_{n+1} = \frac{b_n - a_n}{2}$.

这样，$\{[a_n, b_n]\}$ 是满足闭区间套定理所列条件的闭区间套，从而有唯一的公共点 $\xi$。

任取 $\delta > 0$, 由 $\lim_{n \to +\infty} a_n = \lim_{n \to +\infty} b_n = \xi$, 存在 $N \geqslant 1$ 使得 $\xi - \delta < a_N < b_N < \xi + \delta$. 从而 $[a_N, b_N] \subset (\xi - \delta, \xi + \delta)$. 由于 $[a_N, b_N] \cap E$ 是无限集, 因此 $(\xi - \delta, \xi + \delta) \cap E$ 是无限集, 即 $\xi$ 是 $E$ 的聚点.

接下来, 我们介绍致密性定理. 首先, 引入子列概念. 对于点列 $\{a_{n}\}_{n=1}^{\infty}$, 任取严格单增的正整数列 $\{n_{k}\}$, 称 $\{a_{n_{k}}\}$ 为 $\{a_{n}\}$ 的子列.

之前我们用到的  $\{a_{2n}\}$  与  $\{a_{2n+1}\}$  都是  $\{a_{n}\}$  的子列.  $\{a_{n}\}$  本身也是它自己的子列.

容易看到, 若 $\{a_{n}\}$ 的极限为 $L$, 则它的任何子列的极限也为 $L$. 这样, 若数列有两个收敛到不同值的子列, 则该数列发散. 例如, 数列 $\{(-1)^{n}\}$ 的子列 $\{(-1)^{2n}\}$ 收敛到 1, 而另一个子列 $\{(-1)^{2n+1}\}$ 收敛到 -1, 因此 $\{(-1)^{n}\}$ 发散.

接下来的 Bolzano $^{①}$ -Weierstrass 定理 3.3.10, 常常被称为致密性定理, 是我们今后最常用到的定理之一. 它与聚点原则非常类似.

定理 3.3.10 R 中任何有界数列都有收敛子列.

证明 设 $\{a_{n}\}$ 是 $\mathbb{R}$ 中有界数列. 考虑集合 $E := \{a_{n} | n \geqslant 1\}$, 则 $E$ 是有界集.

若 E 是有限集, 则必有某个元 a 在  $\{a_{n}\}$  中出现无限多次, 把相应的项取出来就形成  $\{a_{n}\}$  的一个取常值 a 的子列, 自然, 该子列收敛到 a.

若 $E$ 是无限集, 则 $E$ 有聚点, 设为 $\xi$. 由聚点定义, 在 $(\xi - 1, \xi + 1)$ 内有 $E$ 中无限多个点. 因此, 可以取到 $n_1 \geqslant 1$ 使得 $a_{n_1} \in (\xi - 1, \xi + 1)$. 进一步, 可取到 $n_2 > n_1$ 使得 $a_{n_2} \in \left(\xi - \frac{1}{2}, \xi + \frac{1}{2}\right)$. 依次可以取到严格单增的正整数列 $\{n_k\}$ 使得 $a_{n_{k+1}} \in \left(\xi - \frac{1}{k+1}, \xi + \frac{1}{k+1}\right)$. 易见, $\{a_{n_k}\}$ 是 $\{a_n\}$ 的收敛于 $\xi$ 的一个子列.

例3.3.5 设实数列 $\{x_{n}\}$ 满足等式

$$
x _ {n} ^ {5} - 5 x _ {n} ^ {4} + \frac {1 0 n ^ {2} + 1}{n ^ {2}} x _ {n} ^ {3} - (4 + 6 \sqrt [ n ]{n}) x _ {n} ^ {2} + \left(6 - \mathrm{e} ^ {\frac {1}{n}}\right) x _ {n} - 1 = 0, \quad \forall n \geqslant 1. \tag {3.3.11}
$$

证明: $\{x_{n}\}$ 收敛.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Bolzano, Bernhard Placidus Johann Nepomuk, 1781 年 10 月 5 日—1848 年 12 月 18 日, 波希米亚数学家、神学家、哲学家、逻辑学家.</span></small>

证明 我们断言 $\lim_{n\to +\infty}x_n = 1$。否则，由极限定义，存在 $\varepsilon_0 > 0$，使得对任何 $N\geqslant 1$ 都有 $n\geqslant N$ 满足 $|x_{n} - 1|\geqslant \varepsilon_{0}$。特别地，可取到 $\{x_{n}\}$ 的子列 $\{x_{k_n}\}$ 使得

$$
\left| x _ {k _ {n}} - 1 \right| \geqslant \varepsilon_ {0}, \quad \forall n \geqslant 1. \tag {3.3.12}
$$

另一方面，由 $2^{n} = (1 + 1)^{n}\geqslant n$ 可得 $n^{\frac{1}{n}}\leqslant 2(\forall n\geqslant 1)$ .于是当 $|x| > 39$ 时，

$$
\begin{array}{l} \left| x ^ {5} - 5 x ^ {4} + \frac {1 0 n ^ {2} + 1}{n ^ {2}} x ^ {3} - (4 + 6 \sqrt [ n ]{n}) x ^ {2} + (6 - \mathrm{e} ^ {\frac {1}{n}}) x - 1 \right| \\ \geqslant | x | ^ {5} - 5 | x | ^ {4} - 1 1 | x | ^ {3} - 1 6 | x | ^ {2} - 6 | x | - 1 \\ \geqslant | x | ^ {4} (| x | - 5 - 1 1 - 1 6 - 6 - 1) = | x | ^ {4} (| x | - 3 9) > 0, \quad \forall n \geqslant 1. \\ \end{array}
$$

因此， $|x_{n}|\leqslant 39(\forall n\geqslant 1)$ ，即 $\{x_{n}\}$ 是有界数列.进而其子列 $\{x_{k_n}\}$ 也是有界数列

由致密性定理, $\{x_{k_n}\}$ 有子列 $\{x_{m_n}\}$ 收敛, 设极限为 $\xi$. 由 (3.3.11) 式得到

$$
\xi^ {5} - 5 \xi^ {4} + 1 0 \xi^ {3} - 1 0 \xi^ {2} + 5 \xi - 1 = 0.
$$

解得 $\xi = 1$

另一方面, 由 (3.3.12) 式可得 $|\xi - 1| \geqslant \varepsilon_0$. 得到矛盾.

因此, 必有  $\lim_{n\to+\infty}x_{n}=1$ .

利用致密性定理, 容易将闭区间套定理 3.3.4 以及注 3.3.1 中的结论作如下推广. 对于非空集 E, 定义其直径为  $\mathrm{diam}E := \sup_{x, y \in E} |x - y|$ .

定理3.3.11 设 $\{E_n\}$ 为 $\mathbb{R}$ 中的有界非空闭集列，满足 $E_{n + 1}\subseteq E_n(n\geqslant 1)$ .则

(1) $\bigcap_{n=1}^{\infty} E_n \neq \varnothing$;
(2) (闭集套定理) 进一步, 若  $\lim_{n\to+\infty}\operatorname{diam}E_n=0$ , 则  $\bigcap_{n=1}^{\infty}E_n$  是单点集.

证明 由定理假设, 对每个 $n \geqslant 1$, 可取到 $x_{n} \in E_{n}$. 进一步, $\{x_{n}\}$ 有界, 从而有收敛子列 $\{x_{k_n}\}$, 设极限为 $\xi$.

对任何 $m \geqslant 1$, 当 $n \geqslant m$ 时有 $k_n \geqslant m$. 从而 $x_{k_n} \in E_{k_n} \subseteq E_m$. 由于 $E_m$ 是闭集, 因此 $\xi \in E_m$. 这就是说 $\xi \in \bigcap_{n=1}^{\infty} E_n$, 即 $\bigcap_{n=1}^{\infty} E_n \neq \varnothing$.

进一步, 对于 $\eta \in \bigcap_{n=1}^{\infty} E_n$, 有 $|\eta - \xi| \leqslant \mathrm{diam} E_n (\forall n \geqslant 1)$. 这样, 如果 $\lim_{n \to +\infty} \mathrm{diam} E_n = 0$, 则可得 $|\eta - \xi| \leqslant 0$, 即 $\eta = \xi$. 这表明此时 $\bigcap_{n=1}^{\infty} E_n$ 是单点集. $\square$

## 3.3.6 Cauchy 收敛准则

数列收敛的 Cauchy 收敛准则时常被看作数列收敛的等价定义, 其优点是不需要事先知道数列的极限. 首先, 定义基本列如下:

定义 3.3.6 称数列  $\{x_{n}\}$  为基本列或 Cauchy 列, 是指  $\forall \varepsilon > 0$ , 存在  $N \geqslant 1$ , 使得当  $m, n \geqslant N$  时, 有

$$
\left| x _ {m} - x _ {n} \right| <   \varepsilon . \tag {3.3.13}
$$

从定义可见 $\{x_{n}\}$ 是Cauchy列当且仅当

$$
\lim _ {N \rightarrow + \infty} \sup _ {m, n \geqslant N} \left| x _ {m} - x _ {n} \right| = 0. \tag {3.3.14}
$$

也等价于

$$
\lim _ {n \rightarrow + \infty} \sup _ {m \geqslant n} \left| x _ {m} - x _ {n} \right| = 0. \tag {3.3.15}
$$

我们有如下的 Cauchy 收敛准则.

定理 3.3.12 数列收敛的充要条件是它是基本列.

证明 (必要性) 若 $\lim_{n\to +\infty}a_n = A,$ 则 $\forall \varepsilon >0,$ 存在 $N\geqslant 1$ ，使得当 $n\geqslant N$ 时，有

$$
| a _ {n} - A | <   \frac {\varepsilon}{2}.
$$

从而当 $n, m \geqslant N$ 时, 有

$$
| a _ {n} - a _ {m} | \leqslant | a _ {n} - A | + | a _ {m} - A | <   \varepsilon ,
$$

即  $\{a_{n}\}$  是 Cauchy 列.

(充分性) 若  $\{a_{n}\}$  是 Cauchy 列, 则有  $N_{1} \geqslant 1$  使得当  $n \geqslant 1$  时, 有

$$
\left| a _ {n} - a _ {N _ {1}} \right| \leqslant 1.
$$

因此, $\{a_{n}\}$ 是有界数列. 于是由致密性定理, $\{a_{n}\}$ 有子列 $\{a_{n_k}\}$ 收敛, 设极限为 $\xi$.

另一方面, $\forall \varepsilon > 0$, 再次利用 $\{a_n\}$ 是 Cauchy 列, 知存在 $N \geqslant 1$, 使得当 $n, m \geqslant N$ 时, 有

$$
\left| a _ {n} - a _ {m} \right| <   \varepsilon .
$$

特别地, 注意到 $n_m \geqslant m \geqslant N$, 可得

$$
\left| a _ {n} - a _ {n _ {m}} \right| <   \varepsilon .
$$

上式中令 $m\to +\infty$ 即得

$$
| a _ {n} - \xi | \leqslant \varepsilon .
$$

于是, 由极限定义得到 $\lim_{n\to +\infty}a_n = \xi$.

□

例 3.3.6 设 p > 1, 证明: (1)  $\sum_{n=1}^{\infty} \frac{1}{n^{p}}$  收敛; (2)  $\sum_{n=1}^{\infty} \frac{\sin n}{n^{p}}$  收敛.

证明 (1) 记 $\alpha = p - 1$. 由定理2.4.4的(2.4.9)式, 对任何 $n \geqslant 2$, 有

$$
\begin{array}{l} \frac {1}{n ^ {\alpha}} - \frac {1}{(n + 1) ^ {\alpha}} = \frac {1}{(n + 1) ^ {\alpha}} \left(\left(1 + \frac {1}{n}\right) ^ {\alpha} - 1\right) \\ > \frac {1}{(n + 1) ^ {\alpha}} \frac {\frac {\alpha}{n}}{1 + \frac {1}{n}} = \frac {\alpha}{(n + 1) ^ {p}}. \tag {3.3.16} \\ \end{array}
$$

于是，

$$
\sum_ {k = 2} ^ {n} \frac {1}{k ^ {p}} \leqslant \frac {1}{\alpha} \sum_ {k = 2} ^ {n} \left(\frac {1}{(k - 1) ^ {\alpha}} - \frac {1}{k ^ {\alpha}}\right) \leqslant \frac {1}{\alpha}.
$$

因此, $\left\{\sum_{k=1}^{n} \frac{1}{k^p}\right\}$ 是单调增加的有界数列. 所以 $\sum_{n=1}^{\infty} \frac{1}{n^p}$ 收敛.

(2) $\forall \varepsilon > 0$, 由 (1) 及 Cauchy 收敛准则, 存在 $N \geqslant 1$ 使得当 $m > n \geqslant N$ 时, 有

$$
\sum_ {k = n + 1} ^ {m} \frac {1}{k ^ {p}} = \left| \sum_ {k = 1} ^ {m} \frac {1}{k ^ {p}} - \sum_ {k = 1} ^ {n} \frac {1}{k ^ {p}} \right| <   \varepsilon .
$$

从而

$$
\left| \sum_ {k = 1} ^ {m} \frac {\sin k}{k ^ {p}} - \sum_ {k = 1} ^ {n} \frac {\sin k}{k ^ {p}} \right| = \left| \sum_ {k = n + 1} ^ {m} \frac {\sin k}{k ^ {p}} \right| \leqslant \sum_ {k = n + 1} ^ {m} \frac {1}{k ^ {p}} <   \varepsilon .
$$

于是, 由 Cauchy 收敛准则得到  $\sum_{n=1}^{\infty}\frac{\sin n}{n^{p}}$  收敛.

例 3.3.7 证明: 调和级数  $\sum_{n=1}^{\infty}\frac{1}{n}$  发散.

证明 证法1 取 $\varepsilon_0 = \frac{1}{2}$, 则对任何 $N \geqslant 1$, 取 $m = 2n = 2N$, 我们有

$$
\Big | \sum_ {k = 1} ^ {m} \frac {1}{k} - \sum_ {k = 1} ^ {n} \frac {1}{k} \Big | = \sum_ {k = n + 1} ^ {m} \frac {1}{k} \geqslant \frac {m - n}{m} = \varepsilon_ {0}.
$$

由 Cauchy 收敛准则,  $\sum_{n=1}^{\infty}\frac{1}{n}$  发散.

证法 2 由 (3.3.6) 式,

$$
\sum_ {k = 1} ^ {n} \frac {1}{k} \geqslant \sum_ {k = 1} ^ {n} \ln \left(1 + \frac {1}{k}\right) = \ln (n + 1).
$$

因此, $\sum_{n=1}^{\infty}\frac{1}{n}=+\infty$ ,从而级数发散.

□

## 3.3.7 有限覆盖定理

最后一个基本定理是 Heine-Borel $^{①}$  有限覆盖定理, 该定理在后继的分析学科中非常重要. 在数学分析课程中, 时常可帮助我们在观察问题时看到问题的本质. 对于  $E \subseteq R$ , 称集族 F 是 E 的一个开覆盖, 是指 F 中的元均为 R 中的开集, 且  $E \subseteq \bigcup_{V \in F} V$ .

定理 3.3.13 R 中有界闭集的任何开覆盖均有有限子覆盖.

证明 证法1 我们用闭集套定理和反证法来证明. 由于 $E$ 有界, 存在有界区间 $[a_1, b_1]$ 使得 $E \subseteq [a_1, b_1]$.

若定理结论不真，则 $E = E \cap [a_1, b_1]$ 不能被 $\mathcal{F}$ 中有限个元素覆盖，简称 $E \cap [a_1, b_1]$ 不能被有限覆盖。将区间 $[a_1, b_1]$ 平分。若 $\left[a_1, \frac{a_1 + b_1}{2}\right] \cap E$ 不能被有限覆盖，令 $[a_2, b_2] = \left[a_1, \frac{a_1 + b_1}{2}\right]$。否则，$\left[\frac{a_1 + b_1}{2}, b_1\right] \cap E$ 必然不能被有限覆盖，此时，令 $[a_2, b_2] = \left[\frac{a_1 + b_1}{2}, b_1\right]$。

以此类推, 可以找到一列闭区间  $\{[a_{n}, b_{n}]\}$  满足如下性质: 对任何  $n \geqslant 1, [a_{n+1}, b_{n+1}] \subseteq [a_{n}, b_{n}], b_{n} - a_{n} = \frac{b_{1} - a_{1}}{2^{n-1}}$ , 且  $[a_{n}, b_{n}] \cap E$  不能被有限覆盖.

由闭集套定理, $\{[a_n, b_n] \cap E\}$ 有唯一的公共点 $\xi$.

由于 $\mathcal{F}$ 覆盖 $E$, 因此, 有 $V \in \mathcal{F}$ 使得 $\xi \in V$. 而由 $V$ 为开集可得存在 $\delta > 0$, 使得 $(\xi - \delta, \xi + \delta) \subseteq V$.

另一方面, 存在 $m \geqslant 1$ 使得 $b_{m} - a_{m} < \delta$. 因此, $\xi - \delta \leqslant b_{m} - \delta < a_{m}$. 同理 $b_{m} < \xi + \delta$. 于是, $[a_{m}, b_{m}] \cap E \subseteq [a_{m}, b_{m}] \subset (\xi - \delta, \xi + \delta) \subseteq V$, 即 $[a_{m}, b_{m}] \cap E$ 可以被 $\mathcal{F}$ 中一个元素 $V$ 覆盖. 得到矛盾.

因此, 一定可以找到 $\mathcal{F}$ 中有限个元覆盖 $E$.

证法2 以下用致密性定理证明. 由定理条件可得, 对于任何 $x \in E$, 令

$$
r (x) := \sup \left\{r \in (0, 1)   \big |   \exists V \in {\mathcal {F}},   \text {使得}   (x - r, x + r) \subseteq V \right\}.
$$

则 $\forall x\in E,$ 有 $r(x) > 0.$ 任取 $x_{1}\in E,$ 有 $V_{1}\in \mathcal{F}$ 使得 $\left(x_1 - \frac{r(x_1)}{2},x_1 + \frac{r(x_1)}{2}\right)\subseteq V_1.$

现设对于某个 $n \geqslant 1$, 已经取到 $x_1, x_2, \dots, x_n \in E$ 以及 $V_1, V_2, \dots, V_n \in \mathcal{F}$. 若 $E \subset \bigcup_{k=1}^{n} V_k$, 则定理得证. 否则, 可取到 $x_{n+1} \in E \setminus \bigcup_{k=1}^{n} V_k$, 以及 $V_{n+1} \in \mathcal{F}$ 使得 $\left(x_{n+1} - \frac{r(x_{n+1})}{2}, x_{n+1} + \frac{r(x_{n+1})}{2}\right) \subset V_{n+1}$.

我们断言以上过程必在有限步内结束. 否则, 因 $E$ 有界, $E$ 中的数列 $\{x_{n}\}$ 有界. 从而它有子列 $\{x_{k_n}\}$ 收敛到某个 $\xi$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Borel, Félix Édouard Justin Émile, 1871 年 1 月 7 日—1956 年 2 月 3 日, 法国数学家、政治家.</span></small>

由 $\{x_{n}\}$ 的构造方法, 对任何 $n \geqslant 1$, 有 $x_{k_{n+1}} \notin V_{k_{n}+1}$. 特别地, $r(x_{k_n}) \leqslant 2|x_{k_{n+1}} - x_{k_n}|$. 因此, $\lim_{n \to +\infty} r(x_{k_n}) = 0$.

另一方面, 由于 $E$ 为闭集, 因此 $\xi \in E$. 从而存在 $U \in \mathcal{F}$ 使得 $\left(\xi - \frac{r(\xi)}{2}, \xi + \frac{r(\xi)}{2}\right) \subset U$. 对于充分大的 $n$, 有 $|x_{k_n} - \xi| < \frac{r(\xi)}{2}$, 进而由

$$
\left(x _ {k _ {n}} - \left(\frac {r (\xi)}{2} - | x _ {k _ {n}} - \xi |\right), x _ {k _ {n}} + \left(\frac {r (\xi)}{2} - | x _ {k _ {n}} - \xi |\right)\right) \subset \left(\xi - \frac {r (\xi)}{2}, \xi + \frac {r (\xi)}{2}\right) \subset U,
$$

可得 $r(x_{k_n}) \geqslant \frac{r(\xi)}{2} - |x_{k_n} - \xi|$. 这样, 又有 $\lim_{n \to +\infty} r(x_{k_n}) \geqslant \frac{r(\xi)}{2} > 0$. 得到矛盾.

总之， $E$ 可以被 $\mathcal{F}$ 的有限子集族覆盖.

由有限覆盖定理易得如下的Lebesgue覆盖引理. 我们称 $\delta > 0$ 为 $E$ 的覆盖 $\mathcal{F}$ 的Lebesgue数, 是指它满足如下条件: 对 $E$ 的任何直径小于 $\delta$ 的子集 $A$, 总有 $\mathcal{F}$ 中的元素 $F$ 使得 $A \subseteq F$.

定理 3.3.14 设 F 是 R 中有界闭集 E 的开覆盖, 则 F 有 Lebesgue 数.

证明 考虑集族

$$
\mathcal {F} _ {0} := \left\{(x - r, x + r)   \big |   \exists V \in \mathcal {F}, \text {使得} (x - 2 r, x + 2 r) \subseteq V \right\},
$$

则 $\mathcal{F}_0$ 是 $E$ 的开覆盖. 从而由有限覆盖定理, 有 $(x_k - r_k, x_k + r_k) \in \mathcal{F}_0 (1 \leqslant k \leqslant n)$, 使得 $E \subset \bigcup_{k=1}^{n} (x_k - r_k, x_k + r_k)$. 令 $\delta = \min_{1 \leqslant k \leqslant n} r_k$. 则对于 $E$ 的直径小于 $\delta$ 的非空子集 $A$, 任取一元素 $x_0 \in A$, 必有某个 $k$ 满足 $1 \leqslant k \leqslant n$, 使得 $x_0 \in (x_k - r_k, x_k + r_k)$. 另一方面, 有 $V_k \in \mathcal{F}$ 使得 $(x_k - 2r_k, x_k + 2r_k) \subseteq V_k$. 从而

$$
A \subseteq [ x _ {0} - \delta , x _ {0} + \delta ] \subseteq (x _ {k} - r _ {k} - \delta , x _ {k} + r _ {k} + \delta) \subseteq (x _ {k} - 2 r _ {k}, x _ {k} + 2 r _ {k}) \subseteq V _ {k}.
$$

即  $\delta$  为 F 的一个 Lebesgue 数.

## 3.3.8 基本定理的新舞台

在 $\mathbb{R}$ 中, 各基本定理是等价的. 承认其中任一个定理, 可推出其他任一个定理. 读者可以尝试证明它们的等价性. 比如可以按下述次序证明这种等价性:

下确界存在定理 $\xleftrightarrow{\text{显然}}$ 上确界存在定理 $\xrightarrow{\text{已证}}$ 单调收敛定理 $\xrightarrow{\text{已证}}$ 闭区间套定理 $\xrightarrow{\text{已证}}$ 有限覆盖定理 $\Rightarrow$ 聚点原则 $\xrightarrow{\text{已证}}$ 致密性定理 $\xrightarrow{\text{已证}}$ Cauchy收敛准则 $\Rightarrow$ 闭区间套定理 $\Rightarrow$ 上确界存在定理.

除了确界存在定理与单调收敛定理, 余下五个基本定理都可以推广到 $\mathbb{R}^n$ 中. 进一步, 它们还可以推广到更一般的空间中去.

通常, 我们把具有一定结构的非空集合 $X$ 称为空间. 各种各样的空间为基本定理提供了广阔的舞台.

## 1. 度量空间与完备性

若  $\rho:X\times X\to[0,+\infty)$  满足如下条件:

(1) 非负性  $\rho(x,y)\geqslant0,$  且等号成立当且仅当 x=y;
(2) 对称性  $\rho(x,y)=\rho(y,x);$
(3) 三角不等式 $\rho(x, z) \leqslant \rho(x, y) + \rho(y, z)$,

则称  $(X,\rho)$  (或 X) 为度量空间或距离空间, 称  $\rho(x,y)$  为 x 与 y 间的距离.

在度量空间中, 可以引入收敛性. 称 $X$ 中的点列 $\{x_{n}\}$ 收敛于 $\xi \in X$, 是指 $\lim_{n\to +\infty} \rho(x_{n}, \xi) = 0$.

类似地, 可以在度量空间中引入 Cauchy 列. 称 X 中的  $\{x_{n}\}$  为 Cauchy 列 (基本列), 是指  $\lim_{N\to+\infty}\sup_{m,n\geqslant N}\rho(x_{m},x_{n})=0$ .

称 $(X, \rho)$ 是完备的度量空间, 是指 $X$ 中的 Cauchy 列都收敛. 即若 $\{x_{n}\}$ 是 Cauchy 列, 则必有 $\xi \in X$ 使得 $\{x_{n}\}$ 收敛到 $\xi$.

易见, $\mathbb{R}$ 及其闭子集 (在通常的度量之下) 是完备度量空间.

## 2. 拓扑空间与紧性

如果  $T \subseteq 2^{X}$  满足如下条件:

(1)  $\varnothing, X \in T;$
(2) $\mathcal{T}$ 的任何子集的并集属于 $\mathcal{T}$, 即若 $\mathcal{F} \subseteq \mathcal{T}$, 则 $\bigcup_{F \in \mathcal{F}} F \in \mathcal{T}$;

(3) T 的任何有限个元素的交集属于 T, 即若  $V_{1}, V_{2}, \cdots, V_{n} \in T$ , 则  $\bigcap_{k=1}^{n} V_{k} \in T$ ,

则称 $(X, \mathcal{T})$ (简记为 $X$) 为一个拓扑空间, $\mathcal{T}$ 中的元素称为 $X$ 的开集. 在拓扑空间中, 如果 $X \setminus F$ 是开集, 则称 $F$ 为闭集. 同样, 对于任何 $E \subseteq X$, 可以定义它的闭包 $\overline{E}$.

若 X 的任何开覆盖都有有限子覆盖, 则称 X 为紧空间. 若  $A \subseteq X$  的任何开覆盖都有有限子覆盖, 则称 A 为紧集, 又称紧致集. 若  $\overline{F} \subseteq E$  且  $\overline{F}$  为紧集, 则称 F 紧包含于 E, 记作  $F \subset \subset E$ .

定理3.3.15 $E$ 是 $\mathbb{R}$ 中的紧集当且仅当 $E$ 是有界闭集.

证明 有限覆盖定理表明, $\mathbb{R}$ 中有界闭集是紧集. 我们只要证明, 若 $E$ 是紧集, 则它一定是有界闭集. 下设 $E$ 为紧集.

为此, 注意到  $\{(-n,n)\}$  是 E 的开覆盖. 因此, 它有有限子覆盖. 即有  $n_{1}, n_{2}, \cdots, n_{m} \in N_{+}$  使得  $E \subseteq \bigcup_{k=1}^{m} (-n_{k}, n_{k}) = (-N, N)$ , 其中  $N = \max_{1 \leqslant k \leqslant m} n_{k}$ . 因此, E 有界.

现设  $\xi\not\in E,$  则  $\left\{\left(-\infty,\xi-\frac{1}{n}\right)\cup\left(\xi+\frac{1}{n},+\infty\right)\right\}$  是 E 的开覆盖. 于是, 它有有限子覆盖, 即有  $n_{1},n_{2},\cdots,n_{m}\in N_{+}$  使得  $E\subseteq\bigcup_{k=1}^{m}\left(\left(-\infty,\xi-\frac{1}{n_{k}}\right)\cup\left(\xi+\frac{1}{n_{k}},+\infty\right)\right)=\mathbb{R}\setminus[\xi-\delta,\xi+\delta]$ , 其中  $\delta=\min_{1\leqslant k\leqslant m}\frac{1}{n_{k}}>0.$  因此,  $\xi\not\in E'$ , 这就是说 E 是闭集. □

## 3. 列紧性

在拓扑空间 $X$ 中可以定义收敛性. 称 $X$ 中的点列 $\{x_{n}\}$ 收敛于 $\xi \in X$, 是指对 $\xi$ 的任何开集 $V$, 有 $N \geqslant 1$ 使得当 $n \geqslant N$ 时, 有 $x_{n} \in V$.

若 $(X,\rho)$ 是度量空间, 定义相应的 $\mathcal{T}$ (称为由度量 $\rho$ 诱导的拓扑) 如下: $V\in \mathcal{T}$ 当且仅当对任何 $x_0\in V$, 存在 $\delta >0$ 使得

$$
\{x \in X | \rho (x, x _ {0}) <   \delta \} \subseteq V.
$$

易见在距离空间中的收敛性与诱导的拓扑空间中的收敛性是一致的. 度量空间中收敛点列的极限是唯一的, 而在一般的拓扑空间中不一定.

若 $X$ 中的点列均有收敛子列, 则称 $X$ 为列紧空间. 若 $X$ 的子集 $A$ 中的点列, 均有收敛于 $A$ 中点的子列, 则称 $A$ 为列紧集.

在 $\mathbb{R}$ 中，一个集合为紧集或列紧集，均当且仅当它为有界闭集.

## 习题3.3

1. 设 $E \subseteq \mathbb{R}$, 称某性质 $P$ 在 $E$ 上局部成立, 是指对任何 $x \in E$, 存在 $x$ 的一个邻域 $V$, 使得 $P$ 在 $E \cap V$ 上成立. 换言之, 对任何 $x \in E$, 存在 $\delta > 0$ 使得 $P$ 在 $(x - \delta, x + \delta) \cap E$ 上成立.

(1) 设 $-\infty \leqslant a < b \leqslant +\infty$. 证明 $f$ 在 $(a, b)$ 内局部有界当且仅当对任何有界闭集 $E \subseteq (a, b)$, $f$ 在 $E$ 上有界.

(2) 设 $-\infty < a < b \leqslant +\infty$. 证明 $f$ 在 $[a, b)$ 上局部有界当且仅当对任何 $c \in (a, b)$, $f$ 在 $[a, c]$ 上有界.

2. 设 $E \subset \mathbb{R}$ 为非空的有界闭集. 证明: $E$ 有最大、最小值, 即 $\sup E \in E$, $\inf E \in E$.

3. 设 E 为 R 中的无理点全体. 证明  $\overline{E} = R$ .

4. 设 $x_0 \in (0,2)$, $x_{n+1} = x_n(2 - x_n) (n \geqslant 0)$. 证明: $\lim_{n \to +\infty} x_n = 1$.

由此, 对于 $c > 0$, 任取 $y_0 > 0$ 满足 $cy_0 < 1$. 令 $y_{n+1} = y_n(2 - cy_n) (n \geqslant 0)$, 则 $\lim_{n \to \infty} y_n = \frac{1}{c}$. 这一事实让我们有可能利用乘法来计算倒数的近似值.

5. 设 $a_0, b_0 > 0$, $a_{n+1} = \frac{a_n + b_n}{2}$, $b_{n+1} = \frac{2a_nb_n}{a_nb_n}$. 证明: $\{a_n\}$ 和 $\{b_n\}$ 均收敛且极限相同.

6. 设  $c \geqslant -3$ ,

$$
x _ {1} = \frac {c}{2}, \qquad x _ {n + 1} = \frac {c}{2} + \frac {x _ {n} ^ {2}}{2}, \qquad n = 1, 2, 3, \dots .
$$

问  $\{x_{n}\}$  何时收敛, 并求极限.

7. 梳理或证明以下结果, 并尝试对这些结论有一个直观的理解:

(1) 收敛数列的子列收敛到同一极限;
(2) 如果一个数列有两个子列收敛到不同极限, 则该数列发散;
(3) 如果有界数列的收敛子列均收敛到同一个极限, 则该数列收敛;

(4) 有界数列 $\{a_{n}\}$ 不收敛到 $A$ 当且仅当存在一个收敛到 $B \neq A$ 的子列;
(5)  $\bar{x}$  为 E 的聚点当且仅当存在 E 中两两不同的点列  $\{x_{n}\}$  使得  $x_{n} \rightarrow \bar{x}$ ;
(6)  $\bar{x}$  为 E 的聚点当且仅当存在  $\{x_{n}\} \subseteq E \setminus \{\bar{x}\}$  使得  $x_{n} \to \bar{x}$ .

8. 设 $E \subseteq \mathbb{R}$. 证明存在至多可列集 $F \subseteq E$ 使得 $F$ 在 $E$ 中稠密.

9. 证明: 闭区间 $[a, b]$ 不能表示为两个不相交的非空闭集的并.

10. 证明: $\mathbb{R}$ 中既开又闭的集只有空集和 $\mathbb{R}$.

11. 设 $\{a_{k_n}\}$ 与 $\{a_{m_n}\}$ 是 $\{a_n\}$ 的两个有相同极限的收敛子列, $\{k_n | n \geqslant 1\} \cup \{m_n | n \geqslant 1\} = \mathbb{N}_+$. 证明: $\{a_n\}$ 收敛.

12. 设 E 为 R 中闭集, 证明存在集合 F 使得 F 的导集为 E.

13. 下表穷举了集合的内部、导集、边界和闭包的内部、导集、边界和闭包. 请证明每一格中的结果, 对于非等式的情形, 举出等式成立以及不成立的例子. 进一步, 思考能否得出其他的关系式.

| 集合 | 内部 | 导集 | 边界 | 闭包 |
| --- | --- | --- | --- | --- |
| $E^{\circ}$ | $(E^{\circ})^{\circ}=E^{\circ}$ | $(E^{\circ})'=\overline{E^{\circ}}$ | $\partial(E^{\circ})\subseteq\partial E\cap E'$ | $\overline{E^{\circ}}\subseteq E'$ |
| $E'$ | $(E')^{\circ}=\overline{E}^{\circ}\supseteq E^{\circ}$ | $(E')'\subseteq E'$ | $\partial(E')\subseteq\partial E\cap E'$ | $\overline{E'}=E'$ |
| $\partial E$ | $(\partial E)^{\circ}=\left(\overline{E}\cap\overline{\mathscr{C}E}\right)^{\circ}$ | $(\partial E)'\subseteq\partial E\cap E'$ | $\partial(\partial E)\subseteq\partial E$ | $\overline{\partial E}=\partial E$ |
| $\overline{E}$ | $(\overline{E})^{\circ}\supseteq E^{\circ}$ | $(\overline{E})'=E'$ | $\partial(\overline{E})\subseteq\partial E$ | $(\overline{E})=\overline{E}$ |

14. 试构造 $\mathbb{R}$ 中一列非空集 $\{E_k\}$ 使得 $E_{k + 1} = E_k' \subset E_k (k \geqslant 1)$.

15. 设 $E \subseteq \mathbb{R}$, 用 $S_{E}$ 表示 $E$ 的孤立点全体, $\mathcal{O}_{E}$ 为 $E$ 的外点全体①. 证明:

(1) 内点为不是边界点的聚点, 即  $E^{\circ} = E' \setminus \partial E;$
(2) 外点为既非聚点又非孤立点的点, 即  $\mathcal{O}_{E} = \mathscr{C}(E' \cup \mathcal{S}_{E})$ ;
(3) 边界点为孤立点, 或不是内点的聚点, 即  $\partial E = S_{E} \cup (E' \setminus E^{\circ})$ ;
(4) 聚点为内点, 或不是孤立点的边界点, 即  $E' = E^{\circ} \cup (\partial E \setminus S_{E})$ ;
(5) 孤立点为不是聚点的边界点, 即  $S_{E} = \partial E \setminus E'$ .

16. 设 $x_0 \in (0,1)$, $x_{n+1} = x_n(1 - x_n) (n \geqslant 0)$. 不使用 Stolz 公式, 按以下过程证明:

(1) $\lim_{n\to +\infty}x_n = 0;$
(2) 对任何  $n \geqslant 1$ ，成立  $(n + 1)x_{n} < 1$ ;
(3) 从某一项开始,  $\{nx_{n}\}$  单调有界;
(4) $\lim_{n\to +\infty}nx_n = 1.$

17. 在习题 6 中, 若 c < -3 会如何?

18. 设 $[a, b]$ 上函数列 $\{f_n\}$ 一致有界, 即存在常数 $M > 0$, 使得

$$
| f _ {n} (x) | \leqslant M, \quad \forall n \geqslant 1, x \in [ a, b ].
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 这两个不是通用记号.</span></small>

证明存在子函数列 $\{f_{n_k}\}$ 使得在 $[a,b]$ 的所有有理点收敛.

19. 设整数  $m \geqslant 1$ ，证明: $\lim_{n \to +\infty} \sqrt{m + \sqrt{m + 1 + \sqrt{m + 2 + \cdots + \sqrt{m + n}}}}$  存在，并记该极限为  $a_{m}$ 。进一步，计算  $\lim_{m \to +\infty} (a_{m} - \sqrt{m})$ 。

20. 证明: $\lim_{n\to +\infty}\sqrt{1 + 2\sqrt{1 + 3\sqrt{1 + 4\sqrt{1 + \cdots + n\sqrt{1 + (n + 1)}}}}} = 3.$

21. 推广习题 20.

22. 设 $x_0 \geqslant 0, x_{n+1} = \sqrt{2 + x_n} (n \geqslant 0)$. 问: $\lim_{n \to +\infty} 4^n(2 - x_n)$ 是否存在? 该极限存在时, 能否得到极限的值?

23. 一般地, 对于所求过的极限可考虑进一步的结果, 例如, 若已经得到 $\lim_{n\to +\infty}x_n = A$, 试试能否找到一个与初值 $x_0$ 无关的无穷大量 $\{y_n\}$ 使得 $\lim_{n\to +\infty}y_n(x_n - A)$ 为一个非零实数.

24. 固定 $r \in (0,4)$. 任取 $x_0 \in (0,1)$. 令 $x_{n+1} = rx_n(1 - x_n) (n \geqslant 0)$. 问: 当 $r$ 取什么值时, 你可以证明对于任何 $x_0 \in (0,1)$, 按上述方式定义的数列 $\{x_n\}$ 一定收敛.

试编写一计算机程序, 感受对于不同的 r, 当 n 足够大时  $x_{n}$  的收敛情况.

25. 设 $\{x_{n}\}$ 是在 $[0,1]$ 中稠密的点列, 任取 $\alpha \in \left(0, \frac{1}{2}\right)$, $E := [0,1] \setminus \bigcup_{n=1}^{\infty} \left(x_{n} - \frac{\alpha}{2^{n}}, x_{n} + \frac{\alpha}{2^{n}}\right)$. 证明 $E$ 为非空的疏朗集.

26. 考虑

$$
X := \left\{\{x _ {n} \} _ {n = 1} ^ {\infty} \Big | \sum_ {n = 1} ^ {\infty} | x _ {n} | ^ {2} <   + \infty \right\},
$$

在其上定义

$$
\| \{x _ {n} \} \| := \Big (\sum_ {n = 1} ^ {\infty} | x _ {n} | ^ {2} \Big) ^ {\frac {1}{2}}, \qquad d (\{x _ {n} \}, \{y _ {n} \}) := \| \{x _ {n} - y _ {n} \} \|.
$$

证明 $d$ 是 $X$ 上的距离. 并以此距离定义收敛性、开集、闭集等. 证明:

(1) 在 X 上, Cauchy 收敛准则成立.
(2) 在 X 上, 致密性定理不成立, 即有界点列不一定有收敛子列.
(3) 设 $\{\pmb{x}_k\}$ 是 $X$ 中点列, 它的每一个分量都有界, 即记 $\pmb{x}_k = \{x_{k,n}\}_{n=1}^{\infty}$ 时, 对任何 $n \geqslant 1$, $\{x_{k,n}\}_{k=1}^{\infty}$ 是有界集. 证明: 存在 $\{\pmb{x}_k\}$ 的子列使得其每一个分量都收敛.
(4) 在 X 上, 有限覆盖定理不成立.
(5) 在 $X$ 上, 闭集套定理成立. 即如果 $\{E_n\}$ 是 $X$ 中的一列单调下降且直径趋于零的闭集列, 则 $\bigcap_{n=1}^{\infty} E_n$ 为单点集.

(6) X 中存在一列有界非空闭集  $E_{1} \supseteq E_{2} \supseteq E_{3} \supseteq \cdots$  使得  $\bigcap_{n=1}^{\infty} E_{n}$  为空集.

27. (1) 在 $[- \infty, +\infty]$ 中①, 若 $\lim_{n \to +\infty} a_n = +\infty$ 或 $\lim_{n \to +\infty} a_n = -\infty$, 我们就分别称 $\{a_n\}$ 收敛到 $+\infty$ 或 $-\infty$. 试重新考察习题 7.

(2) 对于 $E \subseteq [-\infty, +\infty]$, 若存在 $a \in \mathbb{R}$ 使得 $(a, +\infty] \subseteq E ([-\infty, a) \subseteq E)$, 则称 $+\infty (-\infty)$ 为 $E$ 的内点. 若 $U \subseteq [-\infty, +\infty]$ 的所有点都是其内点, 则称 $U$ 为 $[- \infty, +\infty]$ 的开集. 考虑在 $[- \infty, +\infty]$ 中, 哪些集合是紧集, 即 $[- \infty, +\infty]$ 中满足任何开覆盖都有有限子覆盖的集合.

28. 设 $E \subseteq \mathbb{R}$. 则 $E$ 满足什么条件时, 成立: 对于 $E$ 的任何闭覆盖, 均有有限子覆盖.

29. 设 $U$ 为 $\mathbb{R}$ 中开集. 证明:

(1) 若  $x_{0} \in U$ ，则存在唯一的开区间  $(\alpha, \beta)$  ——这样的区间称为 U 的构成区间，满足:

(i) $x_0 \in (\alpha, \beta) \subseteq U$; (ii) 若 $x_0 \in (a, b) \subseteq U$, 则 $(a, b) \subseteq (\alpha, \beta)$.

(2) U 可以表示为至多可列个两两不交的构成区间的并.

30. 闭区间 $[a, b]$ 不能表示为至少两个但至多可列个两两不交的非空闭集的并.

31. $\mathbb{R}$ 不能表示成一列无处稠密集的并.

32. 设 $\{V_k\}$ 是一列在 $\mathbb{R}$ 中稠密的开集, 证明: $\bigcap_{k} V_k$ 在 $\mathbb{R}$ 中稠密.

33. 在度量空间的定义中, 由 (2)\~(3) 可以得到

(3') 对任何 $x, y, z \in X$, 成立 $\rho(x, z) \leqslant \rho(y, x) + \rho(y, z)$.

证明: (1)\~(3) 与 (1), (3') 等价.

## 3.4 上、下极限

在讨论问题之初不能确定某些极限是否存在, 时常带来很大的麻烦. 引入上、下极限在技术上可以减少这种麻烦. 而通过研究弱意义下的极限来研究极限, 则提供了一种重要的数学思想.

设  $\{a_{n}\}$  是广义实数系中的点列, 考虑

$$
A _ {n} := \sup _ {k \geqslant n} a _ {k}, \quad B _ {n} := \inf _ {k \geqslant n} a _ {k}.
$$

则 $\{A_{n}\}$ 单调减少, $\{B_n\}$ 单调增加. 因此, 它们在广义实数系中有极限. 我们给出如下

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 以下说法在 R 中不适用.</span></small>

定义.

定义 3.4.1 对于广义实数系中的点列  $\{a_{n}\}$ ，称

$$
\varlimsup_ {n \to + \infty} a _ {n} := \lim _ {n \to + \infty} \sup _ {k \geqslant n} a _ {k} \quad \text {和} \quad \varliminf_ {n \to + \infty} a _ {n} := \lim _ {n \to + \infty} \inf _ {k \geqslant n} a _ {k}
$$

为  $\{a_{n}\}$  的上极限和下极限.

由夹逼准则立即可得如下定理, 它使得通过上、下极限来研究极限成为可能.

定理3.4.1 对于广义实数列 $\{a_{n}\}$ ， $\lim_{n\to +\infty}a_n = \ell$ 当且仅当

$$
\varlimsup_ {n \to + \infty} a _ {n} = \varliminf_ {n \to + \infty} a _ {n} = \ell , \tag {3.4.1}
$$

其中  $\ell\in[-\infty,+\infty]$ .

证明 (充分性) 若 (3.4.1) 式成立, 则由

$$
\inf _ {k \geqslant n} a _ {k} \leqslant a _ {n} \leqslant \sup _ {k \geqslant n} a _ {k}
$$

和夹逼准则即得  $\lim_{n\to+\infty}a_{n}=\ell.$

(必要性) 若 $\lim_{n\to +\infty}a_n = \ell$ ，则当 $\ell \in (-\infty , + \infty)$ 时， $\forall \varepsilon >0,$ 存在 $N > 0$ 使得

$$
\ell - \varepsilon \leqslant a _ {n} \leqslant \ell + \varepsilon , \quad \forall n \geqslant N.
$$

于是

$$
\ell - \varepsilon \leqslant \inf _ {k \geqslant n} a _ {k} \leqslant a _ {n} \leqslant \sup _ {k \geqslant n} a _ {k} \leqslant \ell + \varepsilon , \quad \forall n \geqslant N.
$$

这就表明 $\lim_{n\to +\infty}a_n = \varlimsup_{n\to +\infty}a_n = \ell.$ 即(3.4.1)式成立.

当  $\ell = +\infty$  或  $\ell = -\infty$  时, 类似可证 (3.4.1) 式成立.

除了定理 3.4.1, 上、下极限具有如下自然的性质.

定理 3.4.2 对于广义实数列 $\{a_{n}\}$, 有

(1) $\varlimsup_{n\to +\infty}a_n\geqslant \varliminf_{n\to +\infty}a_n;$
(2) $\lim_{n\to +\infty}a_n = \inf_n\sup_{k\geqslant n}a_k,\quad \varliminf_{n\to +\infty}a_n = \sup_n\inf_{k\geqslant n}a_k;$

(3) 设  $\{a_{n_{k}}\}$  为  $\{a_{n}\}$  的一个子列, 则

$$
\varlimsup_ {k \to + \infty} a _ {n _ {k}} \leqslant \varlimsup_ {n \to + \infty} a _ {n}, \quad \varliminf_ {k \to + \infty} a _ {n _ {k}} \geqslant \varliminf_ {n \to + \infty} a _ {n};
$$

(4) 存在  $\{a_{n}\}$  的子列  $\{a_{n_{k}}\}$  和子列  $\{a_{m_{k}}\}$  使得 $^{①}$

$$
\varlimsup_ {n \to + \infty} a _ {n} = \lim _ {k \to + \infty} a _ {n _ {k}}, \quad \varliminf_ {n \to + \infty} a _ {n} = \lim _ {k \to + \infty} a _ {m _ {k}}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 本结果蕴涵致密性定理.</span></small>

定理 3.4.3 对于广义实数列 $\{a_{n}\}$ 和 $\{b_{n}\}$, 有

(1) 若  $a_{n} \leqslant b_{n}$  ( $n = 1, 2, \cdots$ ), 则

$$
\varliminf_ {n \to + \infty} a _ {n} \leqslant \varliminf_ {n \to + \infty} b _ {n}, \quad \varlimsup_ {n \to + \infty} a _ {n} \leqslant \varlimsup_ {n \to + \infty} b _ {n}.
$$

(2) $\lim_{n\to +\infty}(-a_n) = -\lim_{n\to +\infty}a_n.$

(3) 以下每一个不等式, 只要其两端在广义实数系中都有意义, 就一定成立:

$$
\begin{array}{l} \varliminf_ {n \to + \infty} a _ {n} + \varliminf_ {n \to + \infty} b _ {n} \leqslant \varliminf_ {n \to + \infty} (a _ {n} + b _ {n}) \\ \leqslant \varliminf_ {n \to + \infty} a _ {n} + \varlimsup_ {n \to + \infty} b _ {n} \leqslant \varlimsup_ {n \to + \infty} (a _ {n} + b _ {n}) \\ \leqslant \varlimsup_ {n \to + \infty} a _ {n} + \varlimsup_ {n \to + \infty} b _ {n}. \\ \end{array}
$$

(4) 若 $\lim_{n\to +\infty}a_n$ 存在, 则

$$
\begin{array}{l} \varliminf_ {n \to + \infty} (a _ {n} + b _ {n}) = \lim _ {n \to + \infty} a _ {n} + \varliminf_ {n \to + \infty} b _ {n}, \\ \varlimsup_ {n \to + \infty} (a _ {n} + b _ {n}) = \lim _ {n \to + \infty} a _ {n} + \varlimsup_ {n \to + \infty} b _ {n}. \\ \end{array}
$$

(5) 若  $a_{n} > 0 (n = 1, 2, \cdots)$ ，规定  $\frac{1}{0} = +\infty$ ，则我们有

$$
\varlimsup_ {n \to + \infty} \frac {1}{a _ {n}} = \frac {1}{\varliminf_ {n \to + \infty} a _ {n}}.
$$

(6) 设  $a_{n} > 0, b_{n} > 0 (n = 1, 2, \cdots)$ ，则以下每一个不等式，只要其两端在广义实数系中都有意义，就一定成立:

$$
\begin{array}{l} \varliminf_ {n \to + \infty} a _ {n} \varliminf_ {n \to + \infty} b _ {n} \leqslant \varliminf_ {n \to + \infty} (a _ {n} b _ {n}) \leqslant \varliminf_ {n \to + \infty} a _ {n} \varlimsup_ {n \to + \infty} b _ {n} \\ \leqslant \varlimsup_ {n \to + \infty} (a _ {n} b _ {n}) \leqslant \varlimsup_ {n \to + \infty} a _ {n} \varliminf_ {n \to + \infty} b _ {n}. \\ \end{array}
$$

(7) 设  $a_{n} > 0 (n = 1, 2, \cdots)$ ，且  $\lim_{n \to +\infty} a_{n} = 0$ .

若  $\varliminf_{n\to+\infty}b_{n}$  不为  $\pm\infty$ ，则  $\varliminf_{n\to+\infty}(a_{n}b_{n})=0$ .

若 $\lim_{n\to +\infty}b_n$ 不为 $\pm \infty$ ，则 $\lim_{n\to +\infty}(a_nb_n) = 0.$

(8) 设 $\lim_{n\to +\infty}a_n = A\in (0, + \infty)$, 则

$$
\varliminf_ {n \to + \infty} (a _ {n} b _ {n}) = A \varliminf_ {n \to + \infty} b _ {n}, \quad \varlimsup_ {n \to + \infty} (a _ {n} b _ {n}) = A \varlimsup_ {n \to + \infty} b _ {n}.
$$

利用上、下极限, Stolz 公式可作如下推广.

定理 3.4.4 设  $\{x_{n}\}$  和  $\{y_{n}\}$  是两个实数列,  $\{y_{n}\}$  严格单增, 且  $\lim_{n\to+\infty}y_{n}=+\infty$ . 则

$$
\varliminf_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}} \leqslant \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}}. \tag {3.4.2}
$$

证明 对任何 $n > m \geqslant 1$, 我们有

$$
\inf _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}} \leqslant \frac {\sum_ {j = m} ^ {n - 1} (x _ {j + 1} - x _ {j})}{\sum_ {j = m} ^ {n - 1} (y _ {j + 1} - y _ {j})} \leqslant \sup _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}}.
$$

即

$$
\inf _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}} \leqslant \frac {x _ {n} - x _ {m}}{y _ {n} - y _ {m}} \leqslant \sup _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}}. \tag {3.4.3}
$$

在上式中固定 $m$ ，令 $n\to +\infty$ ，并注意到

$$
\begin{array}{l} \varliminf_ {n \to + \infty} \frac {x _ {n} - x _ {m}}{y _ {n} - y _ {m}} = \varliminf_ {n \to + \infty} \frac {x _ {n} - x _ {m}}{y _ {n}} = \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}}, \\ \varlimsup_ {n \to + \infty} \frac {x _ {n} - x _ {m}}{y _ {n} - y _ {m}} = \varlimsup_ {n \to + \infty} \frac {x _ {n} - x _ {m}}{y _ {n}} = \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}}, \\ \end{array}
$$

得到

$$
\inf _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}} \leqslant \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \sup _ {k \geqslant m} \frac {x _ {k + 1} - x _ {k}}{y _ {k + 1} - y _ {k}}.
$$

再在上式中令 $m\to +\infty$ 得到

$$
\varliminf_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}} \leqslant \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}}.
$$

从而定理成立.

定理 3.4.5 设  $\lim_{n\to+\infty}x_{n}=\lim_{n\to+\infty}y_{n}=0,\{y_{n}\}$  严格单减. 则

$$
\varliminf_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}} \leqslant \varliminf_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n}}{y _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}}. \tag {3.4.4}
$$

证明 对任何 $m > n \geqslant 1$, 同样有

$$
\inf _ {k \geqslant n} \frac {x _ {k} - x _ {k + 1}}{y _ {k} - y _ {k + 1}} \leqslant \frac {x _ {n} - x _ {m}}{y _ {n} - y _ {m}} \leqslant \sup _ {k \geqslant n} \frac {x _ {k} - x _ {k + 1}}{y _ {k} - y _ {k + 1}}.
$$

在上式中固定 $n$, 令 $m \to +\infty$ 得到

$$
\inf _ {k \geqslant n} \frac {x _ {k} - x _ {k + 1}}{y _ {k} - y _ {k + 1}} \leqslant \frac {x _ {n}}{y _ {n}} \leqslant \sup _ {k \geqslant n} \frac {x _ {k} - x _ {k + 1}}{y _ {k} - y _ {k + 1}}.
$$