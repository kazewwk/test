$$
\begin{array}{l} \leqslant \left| \sum_ {k = 0} ^ {n} a _ {k} - \sum_ {k = 0} ^ {n} a _ {k} x ^ {k} \right| + \left| \sum_ {k = n + 1} ^ {+ \infty} a _ {k} x ^ {k} \right| + \left| \sum_ {k = 0} ^ {+ \infty} a _ {k} x ^ {k} - S \right| \\ = \left| \sum_ {k = 0} ^ {n} a _ {k} (1 - x ^ {k}) \right| + \left| \sum_ {k = n + 1} ^ {+ \infty} a _ {k} x ^ {k} \right| + \left| \sum_ {k = 0} ^ {+ \infty} a _ {k} x ^ {k} - S \right|. \\ \end{array}
$$

我们分别给出右端三项的估计.

首先, 由 $\lim_{n\to +\infty}na_n = 0$ 知, $\forall \varepsilon > 0, \exists N_1$, 使得 $\forall n > N_1$ 成立 $|na_n| < \frac{\varepsilon}{3}$. 又由于

$$
\lim _ {n \to + \infty} \frac {1}{n} \sum_ {k = 0} ^ {n} k | a _ {k} | = \lim _ {n \to + \infty} n | a _ {n} | = 0,
$$

从而有 $\frac{1}{n}\sum_{k = 0}^{n}k|a_k| <   \frac{\varepsilon}{3}.$

其次, 由于 $\lim_{x\to 1^{-}}f(x) = S$, 故 $\exists N_2$, 使得 $\forall n > N_2$,

$$
\left| f \Big (1 - \frac {1}{n} \Big) - S \right| <   \frac {\varepsilon}{3}.
$$

取 $x = 1 - \frac{1}{n}, N = N_{1} + N_{2}$, 当 $n > N$ 时, 有

$$
\left| \sum_ {k = 0} ^ {n} a _ {k} (1 - x ^ {k}) \right| \leqslant \sum_ {k = 0} ^ {n} k | a _ {k} | (1 - x) = \frac {1}{n} \sum_ {k = 0} ^ {n} k | a _ {k} | <   \frac {\varepsilon}{3}.
$$

$$
\left| \sum_ {k = n + 1} ^ {+ \infty} a _ {k} x ^ {k} \right| \leqslant \frac {1}{n} \sum_ {k = n + 1} ^ {+ \infty} k | a _ {k} | \cdot | x | ^ {k} \leqslant \frac {\varepsilon}{3} \cdot \frac {1}{n} \sum_ {k = n + 1} ^ {+ \infty} | x | ^ {k} \leqslant \frac {\varepsilon}{3 n} \cdot \frac {1}{1 - | x |} = \frac {\varepsilon}{3}.
$$

最后, 注意到  $\left|\sum_{k=0}^{+\infty}a_{k}x^{k}-S\right|=\left|f\left(1-\frac{1}{n}\right)-S\right|<\frac{\varepsilon}{3}$ . 这样我们就得到了

$$
\left| \sum_ {k = 0} ^ {n} a _ {k} - S \right| <   \varepsilon .
$$

因此 $\sum_{n=0}^{+\infty} a_n$ 收敛, 且 $\sum_{n=0}^{+\infty} a_n = S$.

## 13.2.2 和函数的可微性

给定级数 $\sum_{n=0}^{+\infty} a_n x^n$, 我们称 $\sum_{n=1}^{+\infty} n a_n x^{n-1}$ 和 $\sum_{n=0}^{+\infty} \frac{a_n}{n+1} x^{n+1}$ 分别为其逐项求导后的幂级数与逐项积分后的幂级数. 显然, 三个级数 $\sum_{n=0}^{+\infty} a_n x^n, \sum_{n=0}^{+\infty} \frac{a_n}{n+1} x^{n+1}$ 和 $\sum_{n=1}^{+\infty} n a_n x^{n-1}$

具有完全相同的收敛半径. 事实上, 成立

$$
\varlimsup_ {n \to + \infty} \sqrt [ n ]{\left| \frac {a _ {n - 1}}{n} \right|} = \varliminf_ {n \to + \infty} \sqrt [ n ]{| (n + 1) a _ {n + 1} |} = \varliminf_ {n \to + \infty} \sqrt [ n ]{| a _ {n} |}. \tag {13.2.2}
$$

关于幂级数的逐项求导, 下面的定理成立:

定理 13.2.3 设幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  的收敛半径为 R，则  $S(x)=\sum_{n=0}^{+\infty}a_{n}x^{n}$  在  $(-R, R)$  中任意次可导，且

$$
S ^ {(k)} (x) = \sum_ {n = k} ^ {+ \infty} n (n - 1) \dots (n - k + 1) a _ {n} x ^ {n - k}.
$$

证明 考虑 $k = 1$ 的情况:首先，幂级数 $\sum_{n=0}^{+\infty}(a_n x^n)' = \sum_{n=1}^{+\infty} na_n x^{n-1}$ 的收敛半径仍为 $R$, 故对闭区间 $I \subset (-R, R)$, 级数在 $I$ 上一致收敛. 所以, $\sum_{n=0}^{+\infty} a_n x^n$ 在 $I$ 中可导, 且

$$
S ^ {\prime} (x) = \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}\right) ^ {\prime} = \sum_ {n = 0} ^ {+ \infty} (a _ {n} x ^ {n}) ^ {\prime} = \sum_ {n = 1} ^ {+ \infty} n a _ {n} x ^ {n - 1}.
$$

对一般的 $k > 1$ ，可以完全类似证明 $S(x)$ 的 $k$ 阶可导性.由于 $S^{(n)}(0) = n!a_n$ ，这说明函数 $S(x)$ 在 $x = 0$ 处的Taylor展开就是该幂级数本身. □

例13.2.2 幂级数

$$
\sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n - 1}}{(2 n - 1) !} x ^ {2 n - 1}
$$

的收敛半径 $R = +\infty$ ，即幂级数在 $\mathbb{R}$ 上收敛，记其和函数为 $S(x)$ .则该幂级数可以逐项求导，从而得到幂级数

$$
\sum_ {n = 0} ^ {+ \infty} \frac {(- 1) ^ {n}}{(2 n) !} x ^ {2 n}, \quad x \in \mathbb {R},
$$

而且, 如果记其和函数为  $C(x)$  的话, 有

$$
S ^ {\prime} (x) = C (x).
$$

不难看出, $C(x)$ 对应的幂级数仍然可以继续求导, 且成立

$$
C ^ {\prime} (x) = - S (x).
$$

## 13.2.3 和函数的可积性

关于幂级数的逐项积分, 下面的定理成立:

定理 13.2.4 设幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  的收敛半径为 R>0，则当  $x\in(-R,R)$  时，有

$$
\int_ {0} ^ {x} \left(\sum_ {n = 0} ^ {+ \infty} a _ {n} t ^ {n}\right) \mathrm{d} t = \sum_ {n = 0} ^ {+ \infty} \int_ {0} ^ {x} a _ {n} t ^ {n} \mathrm{d} t = \sum_ {n = 0} ^ {+ \infty} \frac {a _ {n}}{n + 1} x ^ {n + 1}, \quad \forall x \in (- R, R).
$$

证明 不妨设 $x > 0$, 根据前面的讨论, 级数 $\sum_{n=0}^{+\infty} a_n t^n$ 在 $[0, x]$ 中一致收敛, 因此可以逐项积分. $\square$

![](images/page_482_image_7.jpg)

注13.2.1 如果 $\sum_{n=0}^{+\infty} a_n R^n$ 收敛, 则上面的等式对 $x = R$ 也成立. 对 $-R$ 有类似结果.

例13.2.3 幂级数

$$
\sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} x ^ {2 n} = 1 - x ^ {2} + x ^ {4} - \dots
$$

的收敛半径为 R=1 。在  $(-1,1)$  内幂级数有和函数  $\frac{1}{1+x^{2}}$  。因此，对于任意的  $|x|<1$  ，成立

$$
\arctan x = \int_ {0} ^ {x} \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} t ^ {2 n} \mathrm{d} t = x - \frac {x ^ {3}}{3} + \frac {x ^ {5}}{5} - \dots .
$$

注意到上式左端的函数在 $x = 1$ 处连续, 右端的级数收敛, 因此根据Abel第二定理知上式对 $-1 < x \leqslant 1$ 均成立, 特别地, 有

$$
1 - \frac {1}{3} + \frac {1}{5} - \dots = \arctan 1 = \frac {\pi}{4}.
$$

且上式对  $-1 \leqslant x \leqslant 1$  均成立, 在 x = -1 处也连续, 右端的级数也收敛.

上述讨论表明, 逐项积分和逐项求导后的幂级数, 其收敛半径保持不变, 但对收敛域可能产生细微的影响: 逐项积分后的幂级数收敛域不会减小, 逐项求导后的幂级数收敛域不会增大. 区别只可能表现在收敛区间的端点处.

比如, 考虑级数 $\sum_{n=1}^{+\infty} \frac{x^n}{n}$ 以及 $\sum_{n=1}^{+\infty} \frac{x^{n+1}}{n(n+1)}$ 在 $x = 1$ 处的敛散性, 第一个级数在收敛域的边界点 $x = 1$ 处发散, 但它逐项积分后得到的第二个级数在该点收敛. 等价地, 第二个级数在收敛域的边界点 $x = 1$ 处收敛, 而它逐项求导后得到的第一个级数在该点发散.

关于幂级数的上述性质, 在论证一些等式或讨论幂级数展开时非常有用.

例 13.2.4 对于显然的等式

$$
\frac {1}{1 + x} = \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} x ^ {n}, \quad | x | <   1,
$$

当  $x \in (-1,1)$  时, 逐项积分可得  $\ln(1+x)$  的表达式:

$$
\ln (1 + x) = \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} \frac {x ^ {n + 1}}{n + 1} = \sum_ {n = 1} ^ {+ \infty} (- 1) ^ {n - 1} \frac {x ^ {n}}{n}, \quad | x | <   1. \tag {13.2.3}
$$

注意到等式两端在 x = 1 处可能的延拓:左端函数有意义，右端级数收敛。因此 (13.2.3) 式可以延拓到  $-1 < x \leqslant 1$ 。

类似地可得

$$
\sum_ {n = 0} ^ {+ \infty} (n + 1) x ^ {n} = \frac {1}{(1 - x) ^ {2}}, \quad | x | <   1. \tag {13.2.4}
$$

$$
\sum_ {n = 0} ^ {+ \infty} \frac {(n + 1) (n + 2)}{2} x ^ {n} = \frac {1}{(1 - x) ^ {3}}, \quad | x | <   1. \tag {13.2.5}
$$

$$
\sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} \frac {x ^ {2 n + 1}}{2 n + 1} = \arctan x, \quad | x | \leqslant 1. \tag {13.2.6}
$$

逐项求导或逐项积分在许多相关学科有广泛的应用, 比如读者可以直接验证下面的结论:

例 13.2.5 证明:Bessel 函数

$$
B (x) = \sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n}}{(n !) ^ {2}} \left(\frac {x}{2}\right) ^ {2 n}
$$

满足二阶常微分方程

$$
x B (x) ^ {\prime \prime} + B ^ {\prime} (x) + x B (x) = 0, \quad x \in \mathbb {R}.
$$

## 习题 13.2

1. 证明函数

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \mathrm{e} ^ {- n} \cos^ {2} x
$$

是  $C^{\infty}$  的, 试求其 Maclaurin 级数以及它的收敛半径.

2. 证明:函数

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \mathrm{e} ^ {- n} \cos n ^ {2} x
$$

是无穷次可微的, 其 Maclaurin 级数只有偶数次幂, 并且 $2k$ 次幂项的绝对值为

$$
\sum_ {n = 0} ^ {+ \infty} \frac {x ^ {2 k} \mathrm{e} ^ {- n} n ^ {4 k}}{(2 k) !} > \left(\frac {n ^ {2} x}{2 k}\right) ^ {2 k} \mathrm{e} ^ {- n}.
$$

进一步证明, 此幂级数仅在 $x = 0$ 处收敛.

3. 设 $S(x) = \sum_{n=0}^{+\infty} a_n x^n$ 的收敛半径为 $R > 0$, 证明:

(1) 当  $\sum_{n=0}^{+\infty}\frac{a_{n}}{n+1}R^{n+1}$  收敛时, 有  $\int_{0}^{R}S(x)\mathrm{d}x=\sum_{n=0}^{+\infty}\frac{a_{n}}{n+1}R^{n+1}.$
(2) 当  $\sum_{n=1}^{+\infty} na_{n} R^{n-1}$  收敛时, 有  $S'(R) = \sum_{n=1}^{+\infty} na_{n} R^{n-1}$ .

4. 设幂级数 $\sum_{n=0}^{+\infty} a_n x^n$ 在开区间 $(-R, R)$ 中一致收敛, 证明: 它在闭区间 $[-R, R]$ 中也是一致收敛的.

5. 设 $f(x)$ 是 $[0,1]$ 上的连续函数, 满足

$$
\int_ {0} ^ {1} f (x) x ^ {n} \mathrm{d} x = 0, \quad \forall n = 0, 1, 2, \dots .
$$

证明: 在  $[0,1]$  上  $f(x) \equiv 0$ .

6. 设非常数函数 $f(x)$ 在 $(a, b)$ 内每一点都可以展开成幂级数. 试证明 $f(x)$ 的零点集在 $(a, b)$ 内没有聚点.
7. 设函数 $f(x)$ 在 $x = 0$ 的某个邻域内可以展开成幂级数, 并且序列 $\left\{f^{(n)}(0)\right\}$ 是有界的. 证明: $f(x)$ 必是 $(-\infty, +\infty)$ 内的一个 $C^\infty$ 函数的限制.
8. 设 $f(x)$ 在 $[0,1]$ 连续. 对每个正整数 $n$, 定义

$$
B _ {n} (f, x) = \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} f \left(\frac {k}{n}\right) x ^ {k} (1 - x) ^ {n - k}, \tag {13.2.7}
$$

$B_{n}(f,x)$ 称为函数 $f$ 的 Bernstein 多项式. 证明: $B_{n}(f,x) \Rightarrow f(x), x \in [0,1]$. 进一步对比讨论 $f(x)$ 不连续 (比如取 $f(x)$ 为 Dirichlet 函数) 的情况以及 $f(x)$ 的光滑性更好时的收敛情况.

## 13.3 Taylor 展开式

我们先给出函数的幂级数展开的定义:

定义13.3.1 如果存在 $\delta > 0$，使得在 $(x_0 - \delta, x_0 + \delta)$ 内下式成立:

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} a _ {n} (x - x _ {0}) ^ {n}, \quad \forall x \in (x _ {0} - \delta , x _ {0} + \delta), \tag {13.3.1}
$$

则称函数 $f(x)$ 在 $x_0$ 点附近可以展开成幂级数. 如果函数 $f(x)$ 在区间 $I$ 上每点附近都能展开成幂级数, 则称 $f(x)$ 是 $I$ 上的实解析函数, 集合 $I$ 上实解析函数的全体通常记为 $C^{\omega}(I)$.

![](images/page_485_image_7.jpg)

注13.3.1 显然 $C^\omega (I)\subseteq C^\infty (I)$ ，后面的例13.3.2进一步表明 $C^\omega (I)\subsetneqq$ $C^\infty (I)$

![](images/page_485_image_9.jpg)

注 13.3.2 很容易被忽略的一点是, $f(x)$ 在 $x_0$ 点附近可以展开成幂级数是指等式 (13.3.1) 不但在 $x_0$ 点成立, 而且要存在 $x_0$ 的一个邻域, 使得在整个邻域内等式都成立.

由幂级数在收敛区间 $(x_0 - R, x_0 + R)$ 内的性质立即可得, 若 $f(x)$ 在 $x_0$ 点附近可以展开成幂级数, 则 $f(x)$ 在收敛区间内必须无限次可导, 而且有

$$
f ^ {(n)} (x _ {0}) = n! a _ {n}, \quad n \geqslant 0,
$$

即, $a_{n} = \frac{f^{(n)}(x_0)}{n!}$. 从而 $f(x)$ 又可以表示成

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n}, \quad | x - x _ {0} | <   R. \tag {13.3.2}
$$

上述讨论告诉我们, 如果 $f(x)$ 在 $(x_0 - R, x_0 + R)$ 内满足 (13.3.1) 式, 则必然满足 (13.3.2) 式. 下面我们讨论反过来的问题: 给定一个无穷次可导的光滑函数, 我们来构造它的形式幂级数.

定义 13.3.2 (Taylor 级数) 设  $f(x)$  在  $x_{0}$  处具有任意阶导数, 则称幂级数

$$
\sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n}
$$

为 $f(x)$ 在 $x_0$ 处的Taylor级数，记为

$$
f (x) \sim \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n}. \tag {13.3.3}
$$

特别地，当 $x_0 = 0$ 时，级数

$$
f (x) \sim \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (0)}{n !} x ^ {n}
$$

称为  $f(x)$  的 Maclaurin 级数.

定义 13.3.3 (Taylor 展开式) 设 $f(x)$ 在 $x_0$ 处具有任意阶导数, 如果存在 $x_0$ 的某个邻域 $(x_0 - \delta, x_0 + \delta) (\delta > 0)$, 使得 $f(x)$ 在 $x_0$ 处的 Taylor 级数不但在该邻域内收敛而且收敛于 $f(x)$, 则称 $f(x)$ 在 $x_0$ 附近可 Taylor 展开, 而此时级数 $\sum_{n=0}^{+\infty} \frac{f^{(n)}(x_0)}{n!} (x - x_0)^n$ 称为 $f(x)$ 在该邻域内的 Taylor 展开式, 简称展式.

特别地, 当 $x_0 = 0$ 时, Taylor 展式也称为 Maclaurin 展式.

注13.3.3 值得提醒的是, 任给一个在 $x_0$ 处无穷次可导的函数 $f(x)$, 总可以“诱导”出一个形式幂级数 (13.3.3). 这个“诱导”关系通过 (13.3.3) 式中的 “$\sim$” 而非 “=” 表现得淋漓尽致: 右端的幂级数系数来自 $f(x)$, 但这个幂级数是否仅在一点 $x_0$ 处收敛还是在某个区间内收敛, 收敛时是否收敛于 $f(x)$ 等, 都是两码事. 即, (13.3.3) 式右端的幂级数统称为 $f(x)$ 的 Taylor 级数.

换句话说, 当我们谈论函数  $f(x)$  和它在  $x_{0}$  处的 Taylor 级数 (13.3.3) 时, 我们面对四个不同层次:

(1) $f(x)$ 在 $x_0$ 处的光滑度不够 (不是无穷次可导), 此时谈不上 $f(x)$ 的 Taylor 级数 (对比第一册微分中值定理章节中 $f(x)$ 有限阶光滑时的 Taylor 公式).
(2) 收敛半径为零, 即幂级数除 $x_0$ 外都发散.
(3) 收敛半径大于零但和函数并不等于  $f(x)$ .
(4) 收敛半径大于零且和函数等于  $f(x)$ .

只有情况 (4), 我们才称 $f(x)$ 可Taylor展开. 因此, 函数的Taylor级数与函数的Taylor展式在内涵上有本质的区别.

例 13.3.1 存在无穷光滑函数, 其 Maclaurin 级数的收敛半径为 0. 为此, 考察函数项级数

$$
\sum_ {n = 0} ^ {+ \infty} \frac {\sin (2 ^ {n} x)}{n !}
$$

与幂级数

$$
\sum_ {n = 0} ^ {+ \infty} \left(\frac {1}{n !} \mathrm{e} ^ {2 ^ {n}} \sin \frac {n \pi}{2}\right) x ^ {n}
$$

之间的关系.

解 记 $u_{n}(x) = \frac{\sin(2^{n}x)}{n!}$. 则有 $|u_{n}(x)| \leqslant \frac{1}{n!}$, 因此级数 $\sum_{n=0}^{+\infty} u_{n}(x)$ 在 $\mathbb{R}$ 上一致收敛, 故该函数项级数定义了一个连续函数

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {\sin (2 ^ {n} x)}{n !}.
$$

又因为

$$
| u _ {n} ^ {\prime} (x) | = \left| \frac {2 ^ {n} \cos (2 ^ {n} x)}{n !} \right| \leqslant \frac {2 ^ {n}}{n !},
$$

所以函数项级数 $\sum_{n=0}^{+\infty} u_n'(x)$ 在 $\mathbb{R}$ 上也一致收敛, 从而

$$
f ^ {\prime} (x) = \sum_ {n = 0} ^ {+ \infty} u _ {n} ^ {\prime} (x).
$$

同理对于  $k=1,2,\cdots$ ，可得

$$
f ^ {(k)} (x) = \sum_ {n = 0} ^ {+ \infty} u _ {n} ^ {(k)} (x) = \sum_ {n = 0} ^ {+ \infty} \frac {2 ^ {k n} \sin (2 ^ {n} x + k \pi / 2)}{n !}.
$$

因此, $f(x)$ 是一个无穷光滑的函数. 注意到

$$
f ^ {(k)} (0) = \sum_ {n = 0} ^ {+ \infty} \frac {2 ^ {k n} \sin (k \pi / 2)}{n !} = \mathrm{e} ^ {2 ^ {k}} \sin \frac {k \pi}{2},
$$

故根据前面的讨论, $f(x)$ 可以“诱导”出Maclaurin级数, 即 $f(x)$ 的Taylor级数:

$$
f (x) \sim \sum_ {n = 0} ^ {+ \infty} \left(\frac {1}{n !} \mathrm{e} ^ {2 ^ {n}} \sin \frac {n \pi}{2}\right) x ^ {n}.
$$

但是, 不难算出该幂级数的收敛半径为零. 因此这个幂级数仅在 $x = 0$ 处收敛. 换句话说, 由级数 $\sum_{n=0}^{+\infty} u_n(x)$ 给出的无穷光滑函数 $f(x)$ 并不能展开成 Maclaurin 级数.

例 13.3.2(平坦函数的存在性) 一个函数称为在 $x_0$ 点是平坦的, 是指它在包含 $x_0$ 的某邻域内是无穷光滑的, 且在 $x_0$ 点的各阶导数均为零.

我们在第七章例 7.2.10 曾经讨论过的函数在  $x_{0}=0$  处是平坦的.

$$
f (x) = \left\{ \begin{array}{l l} \mathrm{e} ^ {- \frac {1}{x ^ {2}}}, & x \neq 0, \\ 0, & x = 0. \end{array} \right.
$$

该函数在 x=0 处具有无穷阶导数，且  $f^{(k)}(0)=0\quad(k=0,1,2,\cdots)$ . 因此， $f(x)$  “诱导”出的 Taylor 级数恒为零，其收敛半径为  $+\infty$ ，由于在任何非零点处  $f(x)\neq0$ ，故  $f(x)$  的 Taylor 级数虽然收敛但并不收敛于  $f(x)(x\neq0)$ . 即， $f(x)$  在  $x_{0}=0$  附近不能展开成幂级数.

由于这类平坦函数的存在性, 可以看到, 任何一个无穷光滑函数 $g(x)$ 都和无穷多个函数 $g(x) + f(x)$ 在 $x_0$ 点 “诱导” 出形式上相同的 Taylor 级数, 其中 $f(x)$ 是任意一个在 $x_0$ 处平坦的函数. 因此, 研究一个函数的 Taylor 级数是否收敛到自身是很有必要的.

下面的定理给出了实解析函数在其收敛区间内的每一点都可展开成幂级数的结论.

定理 13.3.1 设 R > 0,

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} c _ {n} x ^ {n}, \quad \forall | x | <   R, \tag {13.3.4}
$$

则 $\forall x_0, |x_0| < R$，当 $|x - x_0| < R - |x_0|$ 时，总成立

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} b _ {n} (x - x _ {0}) ^ {n}, \tag {13.3.5}
$$

其中

$$
b _ {n} = \sum_ {k = n} ^ {+ \infty} \mathrm{C} _ {k} ^ {n} c _ {k} x _ {0} ^ {k - n}, \quad n \geqslant 0. \tag {13.3.6}
$$

证明 当 $|x - x_0| < R - |x_0|$ 时，

$$
\begin{array}{l} \sum_ {k = 0} ^ {+ \infty} \sum_ {n = 0} ^ {k} \left| \mathrm{C} _ {k} ^ {n} c _ {k} x _ {0} ^ {k - n} (x - x _ {0}) ^ {n} \right| \leqslant \sum_ {k = 0} ^ {+ \infty} \sum_ {n = 0} ^ {k} \mathrm{C} _ {k} ^ {n} | c _ {k} | | x _ {0} | ^ {k - n} | x - x _ {0} | ^ {n} \\ = \sum_ {k = 0} ^ {+ \infty} | c _ {k} | \left(| x _ {0} | + | x - x _ {0} |\right) ^ {k} <   + \infty . \\ \end{array}
$$

即级数 $\sum_{k=0}^{+\infty}\sum_{n=0}^{k}\mathrm{C}_{k}^{n}c_{k}x_{0}^{k-n}(x-x_{0})^{n}$ 绝对收敛，从而

$$
\begin{array}{l} \sum_ {n = 0} ^ {+ \infty} b _ {n} (x - x _ {0}) ^ {n} = \sum_ {n = 0} ^ {+ \infty} \sum_ {k = n} ^ {+ \infty} \mathrm{C} _ {k} ^ {n} c _ {k} x _ {0} ^ {k - n} (x - x _ {0}) ^ {n} \\ = \sum_ {k = 0} ^ {+ \infty} \sum_ {n = 0} ^ {k} C _ {k} ^ {n} c _ {k} x _ {0} ^ {k - n} (x - x _ {0}) ^ {n} \\ = \sum_ {k = 0} ^ {+ \infty} c _ {k} x ^ {k} = f (x). \\ \end{array}
$$

定理得证.

□

通过级数的余项来判断一个函数能否展开成 Taylor 级数是一种非常方便和实用的方法. 下面的结论显然:

定理 13.3.2 设区间 I 包含 0 点,  $f(x)$  是定义在 I 上的函数, 在 0 点有任意阶的导数,

$$
r _ {n} (x) := f (x) - \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (0)}{k !} x ^ {k}, \quad \forall x \in I. \tag {13.3.7}
$$

则

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (0)}{n !} x ^ {n}, \quad x \in I \tag {13.3.8}
$$

当且仅当

$$
\lim _ {n \to + \infty} r _ {n} (x) = 0, \quad \forall x \in I. \tag {13.3.9}
$$

我们给出两种特殊情况的幂级数展开. 为此, 我们首先证明一个技术性引理.

引理 13.3.3 设  $a > 0, f \in C^{\infty}[0, a]$ ,  $f^{(n)}(x) \geqslant 0, f^{(n)}(0) = 0 (n \geqslant 0)$ ，则  $f \equiv 0$ .

证明 若结论不真, 不失一般性, 不妨设  $\inf\left\{x>0\mid f(x)>0\right\}=0$ . 任取  $\alpha\in\left(0,\frac{a}{3}\right]$ . 我们有  $\xi_{n}\in(\alpha,a)$  使得

$$
\begin{array}{l} f (a) = \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (\alpha)}{k !} (a - \alpha) ^ {k} + \frac {f ^ {(n + 1)} (\xi_ {n})}{(n + 1) !} (a - \alpha) ^ {n + 1} \\ \geqslant \frac {f ^ {(n + 1)} (\alpha)}{(n + 1) !} (a - \alpha) ^ {n + 1}. \\ \end{array}
$$

即 $f^{(n + 1)}(\alpha)\leqslant \frac{(n + 1)!f(a)}{(a - \alpha)^{n + 1}}.$

另一方面, 有 $\eta_{n} \in (0, \alpha)$ 使得

$$
f (\alpha) = \frac {f ^ {(n + 1)} (\eta_ {n})}{(n + 1) !} \alpha^ {n + 1} \leqslant \frac {f ^ {(n + 1)} (\alpha)}{(n + 1) !} \alpha^ {n + 1} \leqslant f (a) \Big (\frac {\alpha}{a - \alpha} \Big) ^ {n + 1}, \quad \forall n \geqslant 0.
$$

令 $n\to +\infty$ 得到 $f(\alpha) = 0.$ 即 $f|_{[0,\frac{a}{3}]} = 0.$ 矛盾.因此，结论成立

定理 13.3.4 (Bernstein 定理) 设 f 在  $[a, b]$  中无穷次可导，且各阶导数非负， $f^{(n)}(x) \geqslant 0$ . 则对任意的  $x_{0}, x \in [a, b]$ ，只要  $|x - x_{0}| \leqslant b - x_{0}$ ，就有

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n}.
$$

证明 $^{①}$ 显然可以不妨取 $x_{0}=0$ ，此时有 $a\leqslant0<b$ ，而条件 $|x-x_{0}|\leqslant b-x_{0}$ 即为 $|x|\leqslant b$ 。因此，所证结论只需对如下的x成立即可:

(1) 如果  $-a \geqslant b$ ，只需考虑  $x \in [-b, b]$ .
(2) 如果  $-a \leqslant b,$  只需考虑  $x \in [a, b]$ .

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 利用积分余项的证明可参见 R. Redheffer. From center of gravity to Bernstein's theorem. Amer. Math. Monthly, 1983, 90(2): 130-131.</span></small>

记  $\alpha=\min\{-a,b\}\geqslant0,$

$$
P _ {n} (x) = \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (0)}{k !} x ^ {k}, \quad x \in [ - \alpha , b ].
$$

首先我们证明定理对于任意的 $x \in [0, b]$ 成立. 为此, 设 $x \in [0, b], n \geqslant 0$, 有 $\xi_n \in (0, x)$ 使得

$$
f (x) = P _ {n} (x) + \frac {f ^ {(n + 1)} (\xi_ {n})}{(n + 1) !} x ^ {n + 1} \geqslant P _ {n} (x).
$$

因此, 正项级数  $\sum_{k=0}^{+\infty}\frac{f^{(k)}(0)}{k!}x^{k}$  在  $[0,b]$  上收敛. 记其和函数为  $S(x)$ . 则

$$
S (x) \leqslant f (x), \quad \forall x \in [ 0, b ].
$$

注意到 $S^{(n)}$ 即为 $f^{(n)}$ 的Maclaurin级数的和函数，同样有

$$
S ^ {(n)} (x) \leqslant f ^ {(n)} (x), \quad \forall x \in [ 0, b ].
$$

令 $F = f - S$. 则 $F \in C^{\infty}[0, b]$, 且 $F$ 的各阶导数在 $[0, b]$ 上非负, 而 $F^{(n)}(0) = 0 (\forall n \geqslant 0)$. 由引理13.3.3, 可得 $F$ 在 $[0, b]$ 上恒为零. 即, 定理对于 $a = 0$ 时成立.

其次我们证明, 若  $\alpha > 0$ , 定理结论在  $[-\alpha, 0]$  上也成立. 为此考虑

$$
g (x) = f (x) + f (- x), \quad x \in [ 0, \alpha ].
$$

由定理条件 $\forall x\in [-\alpha ,\alpha ],f(x)\geqslant 0,$ 故 $\forall x\in [0,\alpha ],g(x)\geqslant 0.$

注意到 $\forall x\in [-\alpha ,\alpha ],g^{\prime}(x) = f^{\prime}(x) - f^{\prime}(-x)$ 以及 $f^{\prime \prime}(x)\geqslant 0$ ，故 $f^{\prime}(x)$ 单调不减，从而 $\forall x\in [0,\alpha ],f'(x)\geqslant f'(-x)$ ，因此 $g^{\prime}(x)\geqslant 0,\forall x\in [0,\alpha ]$ .同理，对任意自然数 $n$ $\forall x\in [0,\alpha ]$ ，成立 $g^{(n)}(x) = f^{(n)}(x) + (-1)^{n}f^{(n)}(-x)\geqslant 0,x\in [0,\alpha ]$ .由前面的结果，可得

$$
g (x) = \sum_ {k = 0} ^ {+ \infty} \frac {g ^ {(n)} (0)}{k !} x ^ {k}, \quad x \in [ 0, \alpha ].
$$

采取完全类似的论证, 考虑函数

$$
h (x) = f (x) - f (- x), \quad x \in [ 0, \alpha ].
$$

可得

$$
h (x) = \sum_ {k = 0} ^ {+ \infty} \frac {h ^ {(n)} (0)}{k !} x ^ {k}, \quad x \in [ 0, \alpha ].
$$

最后, 由 $f = \frac{1}{2} (g + h)$, 可得

$$
f (x) = \sum_ {k = 0} ^ {+ \infty} \frac {f ^ {(n)} (0)}{k !} x ^ {k}, \quad x \in [ - \alpha , 0 ].
$$

定理得证.

□

例 13.3.3 指数函数  $f(x)=\mathrm{e}^{x}$  在  $(-∞,+∞)$  中的各阶导数均大于零, 根据 Bernstein 定理, 可知其 Taylor 展开式收敛于自身. 即  $\forall x∈R,$  成立

$$
\mathrm{e} ^ {x} = 1 + x + \frac {x ^ {2}}{2} + \dots = \sum_ {n = 0} ^ {+ \infty} \frac {1}{n !} x ^ {n}.
$$

例 13.3.4 考虑前面章节中的关系式 (12.3.9). 当  $x \in [0, \pi)$  时, 根据逐项求导易见, 函数  $\frac{1}{\sin^{2}x} - \frac{1}{x^{2}}$  的各阶导数非负, 因此有 (注意偶函数的展开不含奇次幂项)

$$
\frac {1}{\sin^ {2} x} - \frac {1}{x ^ {2}} = \sum_ {m = 0} ^ {+ \infty} \frac {a _ {2 m}}{(2 m) !} x ^ {2 m}, \forall x \in [ 0, \pi),
$$

其中

$$
a _ {2 m} = \left(\frac {1}{\sin^ {2} x} - \frac {1}{x ^ {2}}\right) ^ {(2 m)} (0) = 2 \sum_ {n = 1} ^ {+ \infty} \frac {(2 m + 1) !}{(n \pi) ^ {2 m + 2}} = 2 (2 m + 1)! \frac {\zeta (2 m + 2)}{\pi^ {2 m + 2}},
$$

因此有

$$
\frac {1}{\sin^ {2} x} - \frac {1}{x ^ {2}} = \sum_ {m = 0} ^ {+ \infty} \frac {\zeta (2 m + 2)}{\pi^ {2 m + 2}} (4 m + 2) x ^ {2 m}, \forall x \in [ 0, \pi). \tag {13.3.10}
$$

定理 13.3.5 设 R > 0, f 在  $(x_{0} - R, x_{0} + R)$  中无穷次可导. 如果存在 M > 0 使得

$$
| f ^ {(n)} (x) | \leqslant M, \forall x \in (x _ {0} - R, x _ {0} + R), \forall n \geqslant 1.
$$

则

$$
f (x) = \sum_ {n = 0} ^ {+ \infty} \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n}, \forall x \in (x _ {0} - R, x _ {0} + R).
$$

证明 当 $x \in (x_0 - R, x_0 + R)$ 时, 由带 Lagrange 余项的 Taylor 公式, 我们有

$$
\begin{array}{l} \left| f (x) - \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (x _ {0})}{k !} (x - x _ {0}) ^ {k} \right| = \left| \frac {f ^ {(n + 1)} (\xi)}{(n + 1) !} (x - x _ {0}) ^ {n + 1} \right| \\ \leqslant \frac {M R ^ {n + 1}}{(n + 1) !} \rightarrow 0 (n \rightarrow + \infty). \\ \end{array}
$$

这说明 f 在  $x_{0}$  处的 Taylor 展开的确收敛到 f 自身.

例 13.3.5 研究幂级数  $\sum_{n=0}^{+\infty} C_{\alpha}^{n} x^{n}$ ，其中  $\alpha \in R \setminus Z$ ,

$$
a _ {n} = \mathrm{C} _ {\alpha} ^ {n} = \frac {1}{n !} \alpha (\alpha - 1) \dots (\alpha - n + 1) \quad (\text {广义组合数}).
$$

解 注意到

$$
\left| \frac {a _ {n + 1}}{a _ {n}} \right| = \left| \frac {\alpha - n}{n + 1} \right|\rightarrow 1 (n \rightarrow + \infty),
$$

由此可知幂级数的收敛半径为 1. 在 $(-1,1)$ 中记和函数为 $f(x)$, 逐项求导可得

$$
\begin{array}{l} (1 + x) f ^ {\prime} (x) = (1 + x) \sum_ {n = 1} ^ {+ \infty} \mathrm{C} _ {\alpha} ^ {n} n x ^ {n - 1} = \sum_ {n = 1} ^ {+ \infty} n \mathrm{C} _ {\alpha} ^ {n} x ^ {n - 1} + \sum_ {n = 1} ^ {+ \infty} n \mathrm{C} _ {\alpha} ^ {n} x ^ {n} \\ = \mathrm{C} _ {\alpha} ^ {1} + \sum_ {n = 1} ^ {+ \infty} \left((n + 1) \mathrm{C} _ {\alpha} ^ {n + 1} + n \mathrm{C} _ {\alpha} ^ {n}\right) x ^ {n} \\ = \alpha + \sum_ {n = 1} ^ {+ \infty} \alpha C _ {\alpha} ^ {n} x ^ {n} = \alpha f (x), \\ \end{array}
$$

这说明

$$
((1 + x) ^ {- \alpha} f (x)) ^ {\prime} = - \alpha (1 + x) ^ {- \alpha - 1} f (x) + (1 + x) ^ {- \alpha} f ^ {\prime} (x) = 0,
$$

从而 $(1 + x)^{-\alpha}f(x)$ 为常数.由 $f(0) = 1$ 可知 $f(x) = (1 + x)^{\alpha}$ .即

$$
(1 + x) ^ {\alpha} = \sum_ {n = 0} ^ {+ \infty} \mathrm{C} _ {\alpha} ^ {n} x ^ {n}, \forall x \in (- 1, 1). \tag {13.3.11}
$$

特别地, 取 $\alpha = -1 / 2$, 并以 $-x^{2}$ 代替 $x$ 得

$$
\frac {1}{\sqrt {1 - x ^ {2}}} = 1 + \sum_ {n = 1} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} x ^ {2 n}, \forall x \in (- 1, 1). \tag {13.3.12}
$$

对此幂级数逐项积分, 得 (约定  $(-1)!! = 1, 0!! = 1$ )

$$
\arcsin x = \sum_ {n = 0} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {x ^ {2 n + 1}}{2 n + 1}, \forall x \in (- 1, 1). \tag {13.3.13}
$$

在 $x = \pm 1$ 处右式的收敛性可以通过Raabe判别法得到, 故上式在 $[-1,1]$ 中均成立, 并且在 $[-1,1]$ 中一致收敛. 代入 $x = \sin t$, 得

$$
t = \sum_ {n = 0} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {\sin^ {2 n + 1} t}{2 n + 1}, \forall t \in [ - \pi / 2, \pi / 2 ],
$$

并且上式是一致收敛的. 再次逐项积分, 得

$$
\begin{array}{l} \frac {\pi^ {2}}{8} = \sum_ {n = 0} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {1}{2 n + 1} \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2 n + 1} t \mathrm{d} t \\ = \sum_ {n = 0} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {1}{2 n + 1} \frac {(2 n) ! !}{(2 n + 1) ! !} = \sum_ {n = 0} ^ {+ \infty} \frac {1}{(2 n + 1) ^ {2}}. \\ \end{array}
$$

由此容易得到 $\frac{\pi^2}{6} = \sum_{n=1}^{+\infty} \frac{1}{n^2} = \zeta(2)$.

例 13.3.6 计算积分  $I=\int_{0}^{1}\frac{\ln(1+x)}{x}\mathrm{d}x.$

解 根据 $\ln (1 + x)$ 的Taylor展开可得

$$
\frac {\ln (1 + x)}{x} = \sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n - 1} x ^ {n - 1}}{n}, x \in (- 1, 1 ].
$$

上式在  $[0,1]$  中一致收敛, 因此可逐项积分:

$$
I = \sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n - 1}}{n} \int_ {0} ^ {1} x ^ {n - 1}   \mathrm{d} x = \sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n - 1}}{n ^ {2}} = \frac {\pi^ {2}}{1 2}.
$$

我们以总结和对比几个名词结束本节内容.

Taylor 级数: 是指当函数 $f(x)$ 在 $x_0$ 的某邻域内无穷光滑时下面的级数:

$$
f (x) \sim f \left(x _ {0}\right) + f ^ {\prime} \left(x _ {0}\right) \left(x - x _ {0}\right) + \frac {f ^ {\prime \prime} \left(x _ {0}\right)}{2 !} \left(x - x _ {0}\right) ^ {2} + \dots + \frac {f ^ {(n)} \left(x _ {0}\right)}{n !} \left(x - x _ {0}\right) ^ {n} + \dots . \tag {13.3.14}
$$

Taylor 展开式: 当  $f(x)$  在包含  $x_{0}$  的某邻域内无穷光滑时, 其 Taylor 级数 (13.3.14) 中的右端有大于零的收敛半径, 并且在收敛域 I 内 “～” 成立等号 “=”, 即

$$
f (x) = f (x _ {0}) + f ^ {\prime} (x _ {0}) (x - x _ {0}) + \frac {f ^ {\prime \prime} (x _ {0})}{2 !} (x - x _ {0}) ^ {2} + \dots + \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n} + \dots ,
$$

那么我们就称  $f(x)$  可 Taylor 展开或者称  $f(x)$  在区域 I 上可展成 Taylor 级数. 一个函数可展成 Taylor 级数表明不但它的 Taylor 级数收敛, 而且收敛到它自身.

Taylor 公式: Taylor 公式是第一册讨论函数导数应用时出现的内容: 如果函数 $f(x)$ 在包含 $x_0$ 的某个闭区间 $[a, b]$ 上具有 $n$ 阶导数, 且在开区间 $(a, b)$ 上具有 $n + 1$ 阶导数, 则对闭区间 $[a, b]$ 上任意一点 $x$, 成立下式:

$$
f (x) = f (x _ {0}) + \frac {f ^ {\prime} (x _ {0})}{1 !} (x - x _ {0}) + \dots + \frac {f ^ {(n)} (x _ {0})}{n !} (x - x _ {0}) ^ {n} + R _ {n} (x),
$$

其中  $R_{n}(x)$  是 Taylor 公式的余项, 余项具有多种表现形式.

注意, Taylor 公式可以对有限阶光滑函数成立, 而且在其满足定理条件的区域都成立 (对于初等函数, 在其定义域内即可), 而 Taylor 展开则要求函数必须无穷光滑, 而且只能在收敛域内才有意义.

例如, 在  $\ln(1+x)$  的定义域内, 都成立下面的 Taylor 公式:

$$
\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {1}{3} \frac {x ^ {3}}{(1 + \theta x) ^ {3}}, \quad 0 <   \theta <   1,
$$

但  $\ln(1+x)$  的 Taylor 展开式只在  $(-1,1]$  内成立, 即  $\ln(1+x)$  在  $(-1,1]$  内可 Taylor 展开为

$$
\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} + \dots + (- 1) ^ {n - 1} \frac {x ^ {n}}{n} + \dots .
$$

## 习题 13.3

1. 求级数  $\sum_{n=0}^{+\infty}(-1)^{n}\frac{x^{4n+1}}{4n+1}$  的和.

2. 求下列级数之和:

$$
\sum_ {n = 1} ^ {+ \infty} \frac {n ^ {2} + 1}{n} x ^ {n}, \quad \sum_ {n = 1} ^ {+ \infty} n ^ {3} x ^ {n}, \quad \sum_ {n = 0} ^ {+ \infty} \frac {1}{3 !} (n + 1) (n + 2) (n + 3) x ^ {n}.
$$

3. 设

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{x} - \frac {1}{\tan x}, & x \in (0, \pi), \quad x \neq \pi / 2, \\ 2 / \pi , & x = \pi / 2. \end{array} \right.
$$

证明: $f(x)$  的 k 阶导数  $(k=0,1,2,\cdots)$  在  $(0,\pi)$  内均恒正，从而在  $(0,\pi)$  的任何内闭区间上满足 Bernstein 定理 13.3.4 的条件.

4. 设 $x \in \left(-\frac{\pi}{2}, 0\right) \cup \left(0, \frac{\pi}{2}\right)$, 推导下列等式:

$$
\begin{array}{l} \frac {1}{x} - \frac {1}{\tan x} = 2 \sum_ {k = 1} ^ {+ \infty} \frac {\zeta (2 k)}{\pi^ {2 k}} x ^ {2 k - 1}, \\ \frac {1}{\sin x} - \frac {1}{x} = 2 \sum_ {k = 1} ^ {+ \infty} \frac {\zeta (2 k)}{\pi^ {2 k}} \left(1 - 2 ^ {1 - 2 k}\right) x ^ {2 k - 1}. \\ \end{array}
$$

5. 证明等式

$$
\ln (x + \sqrt {1 + x ^ {2}}) = \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {x ^ {2 n + 1}}{2 n + 1}, \quad x \in [ - 1, 1 ].
$$

6. 求级数  $\frac{1}{2}-\frac{1}{5}+\frac{1}{8}-\frac{1}{11}+\cdots$  的和.

7. 证明:

$$
1 - \frac {1}{5} + \frac {1}{9} - \frac {1}{1 3} + \dots = \frac {1}{4 \sqrt {2}} \Big (\pi + 2 \ln (\sqrt {2} + 1) \Big).
$$

8. 证明:

$$
1 + \frac {1}{2} - \frac {1}{3} + \frac {1}{4} - \frac {1}{5} + \frac {1}{6} - \frac {1}{7} + \dots = \frac {\pi}{4} + \frac {1}{2} \ln 2.
$$

9. 证明:

$$
1 + \sum_ {n = 1} ^ {+ \infty} \frac {(2 n + 1) ! !}{(2 n) ! !} \frac {1}{(2 n + 1) ^ {2}} = \frac {\pi}{2} \ln 2.
$$

## 13.4 初等函数的幂级数展开

函数的 Taylor 展开在分析学中有极其重要的意义和应用, 上面我们已经给出了一些初等函数的 Taylor 展开, 本节我们再给出几个常见的初等函数的 Taylor (Maclaurin) 展开. 由前面的定理可知, 一个定义在某区间 $I$ 上的无穷光滑函数 $f(x)$ 能否展开成幂级数, 通常的做法是首先写出它的 Taylor 级数或 Maclaurin 级数 (下面我们主要讨论后者), 然后研究该幂级数的收敛半径 $R$. 如果 $R > 0$, 那么我们再进一步验证该幂级数在收敛区间 $(-R, R)$ 内是否收敛到该函数. 而后者又可依据定理 13.3.2 或 Bernstein 定理 13.3.4 等来判别.

我们先回顾一下曾经得到的几个初等函数的 Taylor 展开.

指数函数的幂级数展开:在(5.2.18)式和例13.3.3中,我们均讨论了 $\mathrm{e}^x$ 的Maclaurin级数展式:

$$
\mathrm{e} ^ {x} = \sum_ {n = 0} ^ {+ \infty} \frac {x ^ {n}}{n !}, \quad x \in \mathbb {R}.
$$

幂函数的幂级数展开:然后我们在例13.3.5中得到了 $(1 + x)^{\alpha},\alpha \in \mathbb{R}\backslash \mathbb{Z}$ 的Maclaurin展式(13.3.11):

$$
(1 + x) ^ {\alpha} = \sum_ {n = 0} ^ {+ \infty} C _ {\alpha} ^ {n} x ^ {n}, \quad \forall x \in (- 1, 1),
$$

其中 $a_{n} = \mathrm{C}_{\alpha}^{n} = \frac{1}{n!}\alpha (\alpha -1)\dots (\alpha -n + 1).$

反三角函数的幂级数展开:我们还得到了 $\arcsin x$ 在 $x \in (-1, 1)$ 上的 Maclaurin 展式 (13.3.13):

$$
\arcsin x = \sum_ {n = 0} ^ {+ \infty} \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {x ^ {2 n + 1}}{2 n + 1}, \quad \forall x \in (- 1, 1).
$$

以及 $\arctan x$ 在 $x\in (-1,1)$ 上的Maclaurin展式(13.2.6):

$$
\arctan x = \sum_ {n = 0} ^ {+ \infty} \frac {(- 1) ^ {n} x ^ {2 n + 1}}{2 n + 1}.
$$

下面我们给出另外几个初等函数的 Maclaurin 展式.

## 三角函数的幂级数展开:

例13.4.1 在第五章讨论三角函数时, 我们通过关系式 (5.5.5) 和 (5.5.6) 引入了正弦函数和余弦函数. 下面我们证明: 对于 $x \in (-\infty, +\infty)$ 成立

$$
\sin x = \sum_ {n = 0} ^ {+ \infty} \frac {(- 1) ^ {n} x ^ {2 n + 1}}{(2 n + 1) !}, \tag {13.4.1}
$$

$$
\cos x = \sum_ {n = 0} ^ {+ \infty} \frac {(- 1) ^ {n} x ^ {2 n}}{(2 n) !}. \tag {13.4.2}
$$

证明 对任意的正整数 $n$, 有 $\sin^{(n)}(0) = \sin \frac{n\pi}{2}$. 对任意的 $x \in \mathbb{R}$, 其 Taylor 公式中的 Lagrange 余项为

$$
\left| \frac {\sin \left(\theta x + (2 n + 1) \frac {\pi}{2}\right)}{(2 n + 1) !} x ^ {2 n + 1} \right| \leqslant \frac {| x | ^ {2 n + 1}}{(2 n + 1) !} \rightarrow 0 \quad (n \rightarrow + \infty),
$$