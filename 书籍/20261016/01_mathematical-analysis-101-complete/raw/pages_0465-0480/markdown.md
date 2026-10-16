根据假设, 易知函数列 $\{f_n(x)\}$ 在区间 $[a, b]$ 上一致收敛到某函数 $f(x)$. 在 (\*) 式中令 $n \to +\infty$, 利用逐项积分的定理 12.3.12, 我们可得

$$
f (x) = f (a) + \int_ {a} ^ {x} \varphi (t) \mathrm{d} t,
$$

其中 $\varphi (x)$ 是导函数列 $\{f_n'(x)\}$ 一致收敛的极限函数.这表明函数 $f(x)$ 是连续可微的，并且

$$
f ^ {\prime} (x) = \varphi (x), \quad \forall x \in [ a, b ].
$$

得证.

对于函数项级数, 我们复述一下相应的结论.

定理 12.3.19 设  $\{u_{n}(x)\}$  是 [a, b] 上的可微函数列,  $\sum_{k=1}^{+\infty} u_{k}(c) (c \in [a, b])$  收敛,  $\sum_{k=1}^{+\infty} u_{k}'(x)$  在 [a, b] 上一致收敛, 则  $\sum_{k=1}^{+\infty} u_{k}(x)$  在 [a, b] 上一致收敛到一个处处可微的函数  $S(x)$ , 满足

$$
S ^ {\prime} (x) = \left(\sum_ {k = 1} ^ {+ \infty} u _ {k} (x)\right) ^ {\prime} = \sum_ {k = 1} ^ {+ \infty} u _ {k} ^ {\prime} (x), \quad \forall x \in [ a, b ]. \tag {12.3.5}
$$

例 12.3.11 证明: Riemann- $\zeta$ 函数 $\zeta(s)=\sum_{n=1}^{+\infty}\frac{1}{n^{s}}$ 在 $(1,+\infty)$ 上无穷次可微.

证明 任取 $\delta_0 > 0$ ，由于 $\sum_{n=1}^{+\infty} \frac{1}{n^s}$ 在 $[1 + \delta_0, +\infty)$ 一致收敛，并且有

$$
\left(\frac {1}{n ^ {s}}\right) ^ {\prime} = - \frac {\ln n}{n ^ {s}} \in C (1, + \infty),
$$

且  $\forall x\in[1+\delta_{0},+\infty)$ ，有

$$
\left| - \frac {\ln n}{n ^ {s}} \right| <   \frac {\ln n}{n ^ {(1 + \delta_ {0}) / 2}}.
$$

显然级数 $\sum_{n=1}^{+\infty} \frac{\ln n}{n^{(1 + \delta_0)/2}} \in c$, 因此 $\sum_{n=1}^{+\infty} \frac{-\ln n}{n^s}$ 在 $[1 + \delta_0, +\infty)$ 一致收敛. 根据定理 12.3.19 知 $\sum_{n=1}^{+\infty} \frac{1}{n^s}$ 在 $[1 + \delta_0, +\infty)$ 有连续的导数, 且

$$
\left(\sum_ {n = 1} ^ {+ \infty} \frac {1}{n ^ {s}}\right) ^ {\prime} = \sum_ {n = 1} ^ {+ \infty} \frac {- \ln n}{n ^ {s}}.
$$

完全类似, 可以考虑 $\sum_{n=1}^{+\infty} \frac{-\ln n}{n^s}$ 逐项求导后的级数, 它在 $[1 + \delta_0, +\infty)$ 仍然一致收敛. 故原级数在 $[1 + \delta_0, +\infty)$ 上有连续的二阶导数, 以此类推可得 $\zeta(s) \in C^\infty(1, +\infty)$ 且

$$
\zeta^ {(k)} (s) = (- 1) ^ {k} \sum_ {n = 1} ^ {+ \infty} \frac {\ln^ {k} n}{n ^ {s}}.
$$

至此, 我们完成了函数列和函数项级数的连续性、可微性、可积性等基本性质对极限函数的传承性讨论. 可以看出, 可微性的传承要求的条件相对来说较强一些, 对函数列和导函数列都有一定的要求.

下面给出了函数列一致收敛到极限函数  $g(x)$ ，导函数列逐点收敛甚至内闭一致收敛，但  $g(x)$  在某些点不可导的例子.

例 12.3.12 考察函数项级数  $\sum_{n=1}^{+\infty}\frac{\sin nx}{n^{2}}$  的连续性和可微性.

解 由 Weierstrass M-判别法知, 级数 $\sum_{n=1}^{+\infty} \frac{\sin nx}{n^2}$ 在 $\mathbb{R}$ 上一致收敛, 因此其和函数 $S(x)$ 在 $\mathbb{R}$ 上连续. 现在考察 $\sum_{n=1}^{+\infty} \frac{\sin nx}{n^2}$ 逐项形式求导后的级数 $\sum_{n=1}^{+\infty} \frac{\cos nx}{n}$. 对于 $x \in (0, 2\pi)$, 我们有

$$
\sum_ {k = 1} ^ {n} \cos k x = \frac {\sin \frac {(2 n + 1) x}{2} - \sin \frac {x}{2}}{2 \sin \frac {x}{2}}.
$$

由此, 由 Dirichlet 判别法易见 $\sum_{n=1}^{+\infty} \frac{\cos nx}{n}$ 关于 $x \in (0,2\pi)$ 内闭一致收敛, 从而 $\sum_{n=1}^{+\infty} \frac{\sin nx}{n^2}$ 在 $(0,2\pi)$ 内连续可导.

为了考察和函数  $S(x)$  在 0 点的可微性, 我们采用两种方法.

证法 1 对于  $x \in (0, \pi)$ ，以及  $m \geqslant 1$ ，我们有

$$
\begin{array}{l} \left| \sum_ {n = m + 1} ^ {+ \infty} \frac {\sin n x}{n ^ {2}} \right| = \left| \sum_ {n = m + 1} ^ {+ \infty} \frac {\cos \left(n - \frac {1}{2}\right) x - \cos \left(n + \frac {1}{2}\right) x}{2 n ^ {2} \sin \frac {x}{2}} \right| \\ = \left| \sum_ {n = m} ^ {+ \infty} \frac {\cos \left(n + \frac {1}{2}\right) x}{2 (n + 1) ^ {2} \sin \frac {x}{2}} - \sum_ {n = m + 1} ^ {+ \infty} \frac {\cos \left(n + \frac {1}{2}\right) x}{2 n ^ {2} \sin \frac {x}{2}} \right| \\ \leqslant \frac {1}{2 (m + 1) ^ {2} \sin \frac {x}{2}} + \frac {1}{\sin \frac {x}{2}} \sum_ {n = m + 1} ^ {+ \infty} \left(\frac {1}{2 n ^ {2}} - \frac {1}{2 (n + 1) ^ {2}}\right) \\ = \frac {1}{(m + 1) ^ {2} \sin \frac {x}{2}}. \\ \end{array}
$$

因此，

$$
m \left(S \left(\frac {1}{m}\right) - S (0)\right) = m S \left(\frac {1}{m}\right) = m \left(S _ {m} \left(\frac {1}{m}\right) + R _ {m} \left(\frac {1}{m}\right)\right)
$$

$$
\begin{array}{l} \geqslant m \sum_ {n = 1} ^ {m} \frac {\sin \frac {n}{m}}{n ^ {2}} - \frac {m}{(m + 1) ^ {2} \sin \frac {1}{2 m}} \\ \geqslant \frac {2}{\pi} \sum_ {n = 1} ^ {m} \frac {1}{n} - \frac {1}{(m + 1) \sin \frac {1}{2 m}}, \\ \end{array}
$$

其中  $S_{m}$  和  $R_{m}$  分别为级数的第 m 个部分和以及余项. 由此得知,

$$
\lim _ {m \to + \infty} m \Big (S \Big (\frac {1}{m} \Big) - S (0) \Big) = + \infty .
$$

故  $S(x)$  在 x = 0 处不可导.

证法 2 如果  $S(x)$  在 x = 0 处可导, 则

$$
\lim _ {x \to 0 ^ {+}} \frac {1}{x ^ {2}} \int_ {0} ^ {x} S (t)   \mathrm{d} t = \lim _ {x \to 0 ^ {+}} \frac {1}{2 x} S (x) = \frac {1}{2} S ^ {\prime} (0).
$$

另一方面, 对于  $x \in (0, \pi)$  以及  $m \geqslant 1$ ,

$$
\frac {1}{x ^ {2}} \int_ {0} ^ {x} S (t) \mathrm{d} t = \sum_ {n = 1} ^ {+ \infty} \frac {1 - \cos n x}{n ^ {3} x ^ {2}} \geqslant \sum_ {n = 1} ^ {m} \frac {1 - \cos n x}{n ^ {3} x ^ {2}}.
$$

因此， $\lim_{x\to 0^{+}}\frac{1}{x^{2}}\int_{0}^{x}S(t)\mathrm{d}t\geqslant \sum_{n = 1}^{m}\frac{1}{2n}$ .从而 $\lim_{x\to 0^{+}}\frac{1}{x^{2}}\int_{0}^{x}S(t)\mathrm{d}t = +\infty$ 矛盾

总之, $\sum_{n=1}^{+\infty} \frac{\sin nx}{n^2}$ 在 $\mathbb{R}$ 上连续, 在 $x = 2k\pi$ 不可导, 在其他点可导.

例 12.3.13 下面我们来讨论函数项级数的一些应用. 证明:

$$
\begin{array}{l} \frac {\sin x}{x} = \prod_ {n = 1} ^ {+ \infty} \left(1 - \left(\frac {x}{n \pi}\right) ^ {2}\right), \forall x \in [ - \pi , \pi ]. \\ \frac {\sin x}{\cos x} = \sum_ {n = 1} ^ {+ \infty} \left(\frac {1}{(2 n - 1) \pi / 2 - x} - \frac {1}{(2 n - 1) \pi / 2 + x}\right). \tag {12.3.6} \\ \frac {1}{\sin x} = \frac {1}{x} + \sum_ {n = 1} ^ {+ \infty} (- 1) ^ {n} \left(\frac {1}{x + n \pi} + \frac {1}{x - n \pi}\right). \\ \end{array}
$$

证明 注意

$$
\frac {1}{\sin^ {2} x} = \frac {\cos^ {2} \frac {x}{2} + \sin^ {2} \frac {x}{2}}{4 \sin^ {2} \frac {x}{2} \cos^ {2} \frac {x}{2}} = \frac {1}{4} \left(\frac {1}{\sin^ {2} \frac {x}{2}} + \frac {1}{\sin^ {2} \frac {\pi + x}{2}}\right).
$$

反复利用此等式, 可得

$$
\begin{array}{l} \frac {1}{\sin^ {2} x} = \frac {1}{4} \left(\frac {1}{\sin^ {2} \frac {x}{2}} + \frac {1}{\sin^ {2} \frac {\pi + x}{2}}\right) \\ = \frac {1}{4 ^ {2}} \left(\frac {1}{\sin^ {2} \frac {x}{4}} + \frac {1}{\sin^ {2} \frac {2 \pi + x}{4}} + \frac {1}{\sin^ {2} \frac {\pi + x}{4}} + \frac {1}{\sin^ {2} \frac {3 \pi + x}{4}}\right) \\ = \frac {1}{2 ^ {2 n}} \sum_ {k = 0} ^ {2 ^ {n} - 1} \sin^ {- 2} \frac {k \pi + x}{2 ^ {n}}. \\ \end{array}
$$

当 $2^{n - 1}\leqslant k\leqslant 2^n -1$ 时，再利用

$$
\sin^ {2} \frac {k \pi + x}{2 ^ {n}} = \sin^ {2} \left(\frac {k \pi + x - 2 ^ {n} \pi}{2 ^ {n}} + \pi\right) = \sin^ {2} \frac {(k - 2 ^ {n}) \pi + x}{2 ^ {n}},
$$

可以将前式改写为

$$
\begin{array}{l} \frac {1}{\sin^ {2} x} = \frac {1}{2 ^ {2 n}} \sum_ {k = - 2 ^ {n - 1}} ^ {2 ^ {n - 1} - 1} \sin^ {- 2} \frac {x + k \pi}{2 ^ {n}} \\ = E _ {n} + \sum_ {k = - 2 ^ {n - 1}} ^ {2 ^ {n - 1} - 1} \frac {1}{(x + k \pi) ^ {2}}, \\ \end{array}
$$

其中

$$
E _ {n} = \frac {1}{2 ^ {2 n}} \sum_ {k = - 2 ^ {n - 1}} ^ {2 ^ {n - 1} - 1} \left(\sin^ {- 2} \frac {x + k \pi}{2 ^ {n}} - \left(\frac {x + k \pi}{2 ^ {n}}\right) ^ {- 2}\right). \tag {12.3.7}
$$

注意到不等式

$$
0 <   \frac {1}{\sin^ {2} x} - \frac {1}{x ^ {2}} = 1 + \frac {1}{\tan^ {2} x} - \frac {1}{x ^ {2}} <   1,
$$

有

$$
0 <   E _ {n} <   \frac {1}{2 ^ {2 n}} 2 ^ {n} = \frac {1}{2 ^ {n}}, \forall x \in [ 0, \pi / 2 ],
$$

令 $n\to +\infty$ 可得

$$
\frac {1}{\sin^ {2} x} = \sum_ {k \in \mathbb {Z}} \frac {1}{(x + k \pi) ^ {2}}, \forall x \neq k \pi . \tag {12.3.8}
$$

上式在不包含 $\{k\pi \}$ 的任何闭区间中都是一致收敛的，将其改写为

$$
\frac {1}{\sin^ {2} x} = \frac {1}{x ^ {2}} + \sum_ {n = 1} ^ {+ \infty} \left(\frac {1}{(x + n \pi) ^ {2}} + \frac {1}{(x - n \pi) ^ {2}}\right), x \neq k \pi . \tag {12.3.9}
$$

特别地, 有

$$
\frac {1}{3} = \lim _ {x \to 0} \left(\frac {1}{\sin^ {2} x} - \frac {1}{x ^ {2}}\right) = 2 \sum_ {n = 1} ^ {+ \infty} \frac {1}{(n \pi) ^ {2}},
$$

因此有

$$
\zeta (2) = \sum_ {n = 1} ^ {+ \infty} \frac {1}{n ^ {2}} = \frac {\pi^ {2}}{6}. \tag {12.3.10}
$$

当  $x \in (-\pi, \pi)$  时, 对 (12.3.9) 式两边积分, 利用

$$
\int_ {0} ^ {x} \left(\frac {1}{\sin^ {2} t} - \frac {1}{t ^ {2}}\right) \mathrm{d} t = \left(\frac {1}{t} - \frac {\cos t}{\sin t}\right) \Big | _ {0} ^ {x} = \frac {1}{x} - \frac {\cos x}{\sin x},
$$

可得

$$
\frac {\cos x}{\sin x} - \frac {1}{x} = \sum_ {n = 1} ^ {+ \infty} \left(\frac {1}{x + n \pi} + \frac {1}{x - n \pi}\right), \forall x \in (- \pi , \pi). \tag {12.3.11}
$$

如果再对上式两边积分就可以得到

$$
\frac {\sin x}{x} = \prod_ {n = 1} ^ {+ \infty} \left(1 - \left(\frac {x}{n \pi}\right) ^ {2}\right), \forall x \in [ - \pi , \pi ]. \tag {12.3.12}
$$

这就重新得到了正弦函数的无穷乘积表示.

从等式 (12.3.11) 出发, 利用

$$
\tan x = \cot \left(\frac {\pi}{2} - x\right), \frac {1}{\sin x} = \cot \frac {x}{2} - \cot x,
$$

可得到展开式

$$
\frac {\sin x}{\cos x} = \sum_ {n = 1} ^ {+ \infty} \left(\frac {1}{(2 n - 1) \pi / 2 - x} - \frac {1}{(2 n - 1) \pi / 2 + x}\right), \tag {12.3.13}
$$

以及

$$
\frac {1}{\sin x} = \frac {1}{x} + \sum_ {n = 1} ^ {+ \infty} (- 1) ^ {n} \left(\frac {1}{x + n \pi} + \frac {1}{x - n \pi}\right). \tag {12.3.14}
$$

例 12.3.14 设 p > 1, 计算  $I_{p} = \int_{0}^{+\infty} \frac{dx}{1 + x^{p}}$ .

解 令 $x = t^{1 / p}$ 可得

$$
I _ {p} = \frac {1}{p} \int_ {0} ^ {+ \infty} \frac {t ^ {1 / p - 1}}{1 + t} \mathrm{d} t = \frac {1}{p} \int_ {0} ^ {1} \frac {t ^ {1 / p - 1}}{1 + t} \mathrm{d} t + \frac {1}{p} \int_ {1} ^ {+ \infty} \frac {t ^ {1 / p - 1}}{1 + t} \mathrm{d} t,
$$

对于上式右边第二个积分, 将变量 t 换成 1/t, 整理以后可得

$$
I _ {p} = \frac {1}{p} \int_ {0} ^ {1} \frac {t ^ {1 / p - 1}}{1 + t} \mathrm{d} t + \frac {1}{p} \int_ {0} ^ {1} \frac {t ^ {- 1 / p}}{1 + t} \mathrm{d} t.
$$

利用 $(1 + t)^{-1} = \sum_{k=0}^{n}(-t)^{k} + (-t)^{n+1}(1 + t)^{-1}$ 代入上式可得

$$
I _ {p} = \frac {1}{p} \left(\sum_ {k = 0} ^ {n} \frac {(- 1) ^ {k}}{1 / p + k} + \sum_ {k = 0} ^ {n} \frac {(- 1) ^ {k}}{k - 1 / p + 1}\right) + E _ {n},
$$

其中

$$
E _ {n} = \frac {(- 1) ^ {n + 1}}{p} \left(\int_ {0} ^ {1} \frac {t ^ {n + 1 / p}}{1 + t} \mathrm{d} t + \int_ {0} ^ {1} \frac {t ^ {n + 1 - 1 / p}}{1 + t} \mathrm{d} t\right).
$$

注意到当  $\alpha \rightarrow +\infty$  时，

$$
0 <   \int_ {0} ^ {1} \frac {t ^ {\alpha}}{1 + t} \mathrm{d} t <   \int_ {0} ^ {1} t ^ {\alpha} \mathrm{d} t = \frac {1}{\alpha + 1} \rightarrow 0,
$$

于是

$$
\begin{array}{l} I _ {p} = \frac {1}{p} \lim _ {n \to + \infty} \left(\sum_ {k = 0} ^ {n} \frac {(- 1) ^ {k}}{1 / p + k} + \sum_ {k = 0} ^ {n} \frac {(- 1) ^ {k}}{k - 1 / p + 1}\right) \\ = \frac {1}{p} \left(\frac {1}{1 / p} + \sum_ {k = 1} ^ {+ \infty} (- 1) ^ {k} \left(\frac {1}{1 / p + k} + \frac {1}{1 / p - k}\right)\right) \\ = \frac {\pi}{p} \frac {1}{\sin (\pi / p)}. \\ \end{array}
$$

函数项级数的重要应用之一是通过性质较好的函数的无穷次“叠加”构造出许多具有特殊性质的函数.下面我们举个这方面的例子.

例12.3.15 设 $\{x_{n}\}$ 是[0,1]中的所有有理点构成的序列，证明:级数

$$
\sum_ {n = 1} ^ {+ \infty} \frac {1}{2 ^ {n}} \mathrm{sgn} (x - x _ {n})
$$

定义的和函数  $S(x)$  在且仅在 [0,1] 中的有理点不连续.

证明 首先注意到, 对任意的 $n, \forall x \in [0,1]$, 有

$$
\left| \frac {1}{2 ^ {n}} \mathrm{sgn} (x - x _ {n}) \right| \leqslant \frac {1}{2 ^ {n}}.
$$

因为 $\sum_{n=1}^{+\infty} \frac{1}{2^n}$ 收敛, 所以所考虑的级数在 $[0,1]$ 上一致收敛. 任取 $x_k \in \mathbb{Q} \cap [0,1]$, 则该级数中仅有一项 $\frac{1}{2^k} \operatorname{sgn}(x - x_k)$ 在 $x = x_k$ 处不连续, 其余项均在 $x = x_k$ 处连续, 因此原级数在 $x = x_k$ 处不连续.

当 $\xi \notin \{x_{n}\}$ 时, 由于该级数每一项都在 $x = \xi$ 处连续, 从而所考虑的级数在 $x = \xi$ 处连续. □

例12.3.16 令

$$
f (x) = \left\{ \begin{array}{l l} x ^ {2} \sin \frac {1}{x}, & 0 <   x \leqslant 1, \\ 0, & x = 0, \end{array} \right.
$$

以及

$$
g (x) = \sum_ {n = 1} ^ {+ \infty} \frac {f (x - x _ {n})}{2 ^ {n}},
$$

其中 $\{x_{n}\} = \mathbb{Q}\cap [0,1]$ .则 $g(x)$ 是一个在[0,1]上可导，且导函数在[0,1]上所有的无理点处连续、所有的有理点处不连续的函数.

## 习题 12.3

1. 设 $f_{n}(x) = \frac{1}{n\sqrt{\cos(x / n) - \cos(1 / n)}}$. 求 $\lim_{n\to +\infty}\int_0^1 f_n(x)\mathrm{d}x$.

2. 记 $f(x) = \sum_{n=1}^{+\infty} \frac{x^2}{1 + n^2 x^2}, x \in (-\infty, +\infty)$. 求极限 $\lim_{x \to \infty} f(x)$.

3. 证明定理 12.3.10.

4. 设  $\sum_{n=1}^{+\infty} u_{n}(\cdot)$  在  $[a, b]$  上收敛. 若对任何  $\varepsilon > 0$  及  $N \geqslant 1$ , 存在区间  $(a_{1}, b_{1})$ ,  $(a_{2}, b_{2}), \cdots, (a_{k}, b_{k})$  以及  $n_{1}, n_{2}, \cdots, n_{k} \geqslant N$  使得  $\bigcup_{j=1}^{k} (a_{j}, b_{j}) \supset [a, b]$ , 且

$$
\left| \sum_ {l = n _ {j}} ^ {+ \infty} u _ {l} (x) \right| \leqslant \varepsilon , \quad \forall x \in (a _ {j}, b _ {j}) \cap [ a, b ], \quad j = 1, 2, \dots , k.
$$

则称  $\sum_{n=1}^{+\infty}u_{n}(\cdot)$  在  $[a,b]$  上拟一致收敛. 证明: 若  $u_{n}(n\geqslant1)$  都在  $[a,b]$  上连续, 则
 $\sum_{n=1}^{+\infty}u_{n}$  在  $[a,b]$  上连续当且仅当它在  $[a,b]$  上拟一致收敛.

5. 设 $\{a_{n}\}$ 是一个单调趋于零的序列, 证明: $\sum_{n=1}^{+\infty} a_{n} \cos nx$ 和 $\sum_{n=1}^{+\infty} a_{n} \sin nx$ 给出两个在 $(0,2\pi)$ 上连续的函数.

进一步, 如果 $\{a_{n}\}$ 单调趋于零, 那么当 $\sum_{n=1}^{+\infty} a_{n}$ 收敛时, 则两级数在 $\mathbb{R}$ 上一致收敛; 而当 $\sum_{n=1}^{+\infty} a_{n}$ 发散时, 则级数 $\sum_{n=1}^{+\infty} a_{n} \cos nx$ 在 $(0, 2\pi)$ 上必然不一致收敛.

6. 证明 Dirichlet 函数具有下面的表示:

$$
D (x) = \lim _ {m \to + \infty} \left(\lim _ {n \to + \infty} \cos^ {m} (2 \pi n! x)\right), \quad \forall x \in [ 0, 1 ].
$$

7. 证明: Dirichlet 函数 $D(x)$ 不可能是连续函数列的逐点收敛的极限函数.

8. 证明:函数

$$
f (x) = \sum_ {n = 2} ^ {+ \infty} \left(\frac {x \sin x}{\ln n}\right) ^ {n}
$$

是 $(-∞,+∞)$ 上的连续函数.

9. (1) 证明: $I = \int_{0}^{1} \frac{1}{x^x} \, \mathrm{d}x = \sum_{n=1}^{+\infty} \frac{1}{n^n}$.

(2) 模仿上式, 给出积分  $I_{1}=\int_{0}^{1}x^{x}dx$  的一个级数表示.

10. 设  $u_{n}(x)$  ( $n = 1, 2, \cdots$ ) 在 [a, b] 连续，且  $\sum_{n=1}^{+\infty} u_{n}(x)$  在 (a, b) 一致收敛，证明: $\sum_{n=1}^{+\infty} u_{n}(x)$  在 [a, b] 一致收敛.

11. 设 $\sum_{n=1}^{+\infty} u_n(x)$ 在 $[a, b]$ 上收敛, 如果

$$
| S _ {n} (x) | = \left| \sum_ {k = 1} ^ {n} u _ {k} (x) \right| \leqslant M, \quad a \leqslant x \leqslant b, \quad n = 1, 2, \dots ,
$$

则称  $\sum_{n=1}^{+\infty}u_{n}(x)$  在  $[a,b]$  上有界收敛. 现假设  $\sum_{n=1}^{+\infty}u_{n}(x)$  在  $[a,b]$  上有界收敛, 且对任意  $\delta > 0$  及  $c \in (a,b)$ ,  $\sum_{n=1}^{+\infty}u_{n}(x)$  在  $[a,c-\delta]$  和  $[c+\delta,b]$  上一致收敛, 如果  $u_{n}(x)$   $(n=1,2,\cdots)$  在  $[a,b]$  上 Riemann 可积, 证明:  $\sum_{n=1}^{+\infty}u_{n}(x)$  也在  $[a,b]$  上 Riemann 可积, 而且

$$
\int_ {a} ^ {b} \Big (\sum_ {n = 1} ^ {+ \infty} u _ {n} (x) \Big) \mathrm{d} x = \sum_ {n = 1} ^ {+ \infty} \int_ {a} ^ {b} u _ {n} (x) \mathrm{d} x.
$$

12. 计算下列积分:

(1) $\int_{\ln 2}^{\ln 5}\sum_{n = 1}^{+\infty}n\mathrm{e}^{-nx}\mathrm{d}x;$

(2) $\int_{0}^{2\pi}\sum_{n = 1}^{+\infty}\frac{\cos^2nx}{n(n + 1)}\mathrm{d}x.$

13. 研究函数 $f(x) = \sum_{n=1}^{+\infty} \frac{|x|}{n^2 + x^2}$ 的可微性质.

14. 在 (0,1) 中任一数列 $\{a_{n}\}$, 其中两两不同. 证明: 函数

$$
f (x) = \sum_ {n = 1} ^ {+ \infty} \frac {| x - a _ {n} |}{2 ^ {n}}
$$

在 $(0,1)$ 中连续,且除了点 $x=a_{n}(n=1,2,\cdots)$ 处可微.

15. 设 $f(x) = \sum_{n=1}^{+\infty} \frac{1}{x + 2^n}, x \in (0, +\infty)$. 证明:

(1)  $f(x)$  在  $(0, +\infty)$  上连续.
(2) $\forall x > 0$, 有 $0 < f(x) - \frac{\ln(1 + x)}{x \ln 2} < \frac{1}{1 + x}$.

16. 设 $f(x) = \sum_{n=1}^{+\infty} \frac{\cos nx}{\sqrt{n}}$.

(1) 证明: $\int_{0}^{\pi}|f(x)|\mathrm{d}x$ 收敛.

(2) 求极限  $\lim_{x\to0}f(x)$ .

17. 构造一个可导函数, 使它在有理点处取有理数值, 它的导数在有理点处取无理数值.

18. 设 $f(x)$ 在 $\mathbb{R}$ 上有任意阶导数 $f^{(n)}(x)$，且任意区间 $[a, b]$ 上 $f^{(n)}(x) \to \varphi(x) (n \to +\infty)$. 求证:$\varphi(x) = ce^x$ (其中 $c$ 为常数).

19. 设 $f(x) = \sum_{n=0}^{+\infty} 2^{-n} \cos 2^n x$, 求 $\lim_{x \to 0^+} x^{-1}(f(x) - f(0))$.

20. 设 $f(x) = \sum_{n=1}^{+\infty} \frac{1}{10^n} \{10^n x\}$, 其中 $\{t\}$ 表示 $t$ 到它最近的整数的距离. 证明: $f(x)$ 是一个处处连续、处处不可微的函数.

21. 设 $\{f_n(x)\}$ 是定义在区间 $I$ 上的函数列, 收敛于连续函数 $f(x)$. 又设 $\forall n, f_n(x)$ 在 $I$ 上处处可导, 且导函数列 $\{f_n'(x)\}$ 收敛于连续函数 $g(x)$. 问: 在 $I$ 上是否有 $f'(x) = g(x)$?

22. 设 $b_{n} \geqslant 0, \sum_{n=1}^{+\infty} b_{n} \sin nx$ 在 $\mathbb{R}$ 上一致收敛到 $\varphi(x)$. 证明: $\varphi(x) \in C^{1}(\mathbb{R})$ 的充要条件是 $\sum_{n=1}^{+\infty} nb_{n}$ 收敛.

## 第十三章

## 幂级数

本章讨论一类重要的具有特殊形式 $\sum_{n=0}^{+\infty} a_n (x - x_0)^n$ 的函数项级数——幂级数，其中 $x_0 \in \mathbb{R}$, $\{a_n\}$ 是给定的实数列，当 $x = 0$ 时，$x^0$ 规定为 1. 幂级数看起来是一种形式极为简单的函数项级数，然而无论在理论上还是实际应用中，它都具有极其重要的地位，有着丰富的内容、深刻的理论和广泛的应用。在本章中，我们将系统介绍幂级数的理论，包括幂级数的收敛域问题、和函数的性质、函数的幂级数展开问题，以及幂级数的应用问题。

## 13.1 幂级数的收敛半径与收敛域

由于 $x_0 \neq 0$ 的情形可以通过一个简单的平移化为 $x_0 = 0$ 的情形, 因此, 在下面的讨论中, 我们经常默认 $x_0 = 0$.

考虑幂级数

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = a _ {0} + a _ {1} x + a _ {2} x ^ {2} + \dots . \tag {13.1.1}
$$

一个显然的结论是该幂级数在 x = 0 处总是收敛的, 因此幂级数的收敛域总是非空的, 其中幂级数收敛域的定义仍然沿用函数项级数章节中的定义, 即使得幂级数收敛的点的全体.

例 13.1.1 (1) 幂级数  $\sum_{n=0}^{+\infty} n! x^{n}$  的收敛域为  $\{0\}$ . 事实上, 一方面, 当 x=0 时, 幂级数收敛; 另一方面, 当  $x \neq 0$  时,  $\lim_{n \to +\infty} |n! x^{n}| = +\infty$ , 所以该幂级数发散.

(2) 幂级数  $\sum_{n=0}^{+\infty}\frac{x^{n}}{n!}$  的收敛域为 R.

(3) 考虑幂级数 $\sum_{n=1}^{+\infty} \frac{x^n}{n}$ 的收敛域. 容易看出, 当 $|x| < 1$ 时, $\left|\frac{x^n}{n}\right| \leqslant |x^n|$, 故级数收敛; 当 $x = -1$ 时, 级数为一个收敛的交错级数; 而当 $x = 1$ 时, 是发散的调和级数. 当 $|x| > 1$ 时, 级数通项趋于无穷, 故发散. 因此, 级数的收敛域为 $[-1, 1)$.

例13.1.2 试讨论级数 $\sum_{n=0}^{+\infty} a_n x^n$ 的敛散性.

解 记  $L := \varlimsup_{n \to +\infty} \sqrt[n]{|a_n|}$ ,

$$
R := \frac {1}{L} \equiv \left\{ \begin{array}{l l} + \infty , & L = 0, \\ \frac {1}{L}, & L \in (0, + \infty), \\ 0, & L = + \infty . \end{array} \right. \tag {13.1.2}
$$

则由 $\lim_{n\to +\infty}\sqrt[n]{|a_nx^n|} = L|x|$，不难证明下面结论:

(1) 若 R = 0, 级数在 x = 0 处收敛.

(2) 若 R > 0, 则由  $\varlimsup_{n \to +\infty} \sqrt[n]{|a_{n}x^{n}|} = L|x|$  知:

(i) 当 $|x| < R$ 时, 根据 Cauchy 根值判别法知, 级数 $\sum_{n=0}^{+\infty} a_n x^n$ 绝对收敛, 从而收敛.

(ii) 当 $|x| > R$ 时, 数列 $\{a_{n}x^{n}\}$ 不趋于零, 此时级数 $\sum_{n=0}^{+\infty} a_{n}x^{n}$ 发散.

(iii) 当 $|x| = R$ 时, 级数的敛散性要依具体情况讨论. 比如下面三个级数

$$
\sum_ {n = 1} ^ {+ \infty} x ^ {n}, \quad \sum_ {n = 1} ^ {+ \infty} \frac {x ^ {n}}{n}, \quad \sum_ {n = 1} ^ {+ \infty} \frac {x ^ {n}}{n ^ {2}}
$$

对应的 L 均为 1, 所以 R = 1, 但第一个级数当  $|x| = 1$  时发散; 第二个级数当 x = 1 时发散, 当 x = -1 时条件收敛; 第三个级数当  $|x| = 1$  时绝对收敛. □

幂级数的收敛域有以下特点:

定理 13.1.1 (Abel 第一定理) 幂级数 (13.1.1) 的收敛域是一个区间, 即对于 $x_0 \in \mathbb{R}, x_0 \neq 0$,

(1) 若级数在  $x_{0}$  处收敛, 则它一定在  $(-|x_{0}|, |x_{0}|)$  内闭绝对一致收敛.
(2) 若  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  在  $x_{0}\neq0$  发散, 则当  $|x|>|x_{0}|$  时,  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  发散.

证明 (1) 任取闭区间 $[a, b] \in (-|x_0|, |x_0|)$, 则存在 $0 < \delta_0 < 1$, 使得

$$
[ a, b ] \subset [ - \delta_ {0} | x _ {0} |, \delta_ {0} | x _ {0} | ] \subset (- | x _ {0} |, | x _ {0} |).
$$

下面我们证明 $\sum_{n=0}^{+\infty} a_n x^n$ 在 $[- \delta_0 |x_0|$, $\delta_0 |x_0|$ 上绝对一致收敛. 为此, 由 $\sum_{n=0}^{+\infty} a_n x_0^n$ 收敛, 知 $|a_n x_0^n|$ 有界, 即存在 $c > 0$, 使得 $\forall n$, 有 $|a_n x_0^n| \leqslant c$. 从而 $\forall x \in [-\delta_0 |x_0|$, $\delta_0 |x_0|$ 有

$$
| a _ {n} x ^ {n} | = \left| a _ {n} x _ {0} ^ {n} \frac {x ^ {n}}{x _ {0} ^ {n}} \right| \leqslant c \delta_ {0} ^ {n}.
$$

由 $\sum_{n=0}^{+\infty} c\delta_0^n$ 收敛, 可得 $\sum_{n=0}^{+\infty} |a_n x^n|$ 在 $[- \delta_0 |x_0|$, $\delta_0 |x_0|$ 上一致收敛.

结论 (2) 与结论 (1) 本质上是等价的.

注13.1.1 由定理13.1.1知，如果级数 $\sum_{n=0}^{+\infty} a_n x^n$ 在 $x_0 \neq 0$ 处收敛，且在 $x_1$ 处发散，则必有 $x_1 \neq 0$ ，$|x_0| \leqslant |x_1|$，且一定存在一个开区间 $(-R, R)$，$|x_0| \leqslant R \leqslant |x_1|$，使得幂级数在 $(-R, R)$ 内闭绝对一致收敛，而在 $(- \infty, -R) \cup (R, +\infty)$ 发散。

级数在区间端点的敛散性需要另行做进一步的分析.

定理 13.1.2 (Cauchy-Hadamard 定理) 考虑幂级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$ ，记  $\rho = \lim_{n\to+\infty}|a_{n}|^{\frac{1}{n}}$ ,  $R = \frac{1}{\rho}$ ，则

(1) $R = +\infty$ 时, 幂级数在 $(-\infty, +\infty)$ 中绝对收敛.
(2) R = 0 时, 幂级数仅在 x = 0 处收敛.
(3) $0 < R < +\infty$ 时, 幂级数在 $(-R, R)$ 中绝对收敛, 在 $[-R, R]$ 之外发散.

证明 注意到 $\lim_{n\to \infty}|a_nx^n|^{\frac{1}{n}} = \rho |x|$, 由数项级数的根值判别法, 结合定理 13.1.1 的证明过程, 即可得到定理结论的证明. $\square$

定义 13.1.1 定理 13.1.2 中的 R 称为幂级数 (13.1.1) 的收敛半径.

如果幂级数（13.1.1）的收敛半径是 R > 0，则称区间  $(-R, R)$  为幂级数的收敛区间.

需要特别注意的是:幂级数的收敛区间规定为开区间 $(-R, R)$，它并不一定等同于幂级数的收敛域。收敛区间的引入为下面的讨论带来很多表述上的方便。不同的教科书或参考书上可能有不同的称呼。

可以验证, 幂级数的收敛半径 $R$ 的定义等价于下面的定义

$$
R := \sup \left\{| x |   \Bigg |   \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}   \text {收敛} \right\}.
$$

例 13.1.3 容易证明, 级数  $\sum_{n=1}^{+\infty}\frac{x^{n}}{n^{2}},\sum_{n=1}^{+\infty}\frac{x^{n}}{n}$  和  $\sum_{n=1}^{+\infty}nx^{n}$  有相同的收敛半径 R=1, 但在区间端点处有不同的敛散性. 其收敛域分别为  $[-1,1]$ ,  $[-1,1)$  和  $(-1,1)$ .

事实上, 更一般的结论也成立: $\sum_{n=0}^{+\infty} a_n x^n$, $\sum_{n=0}^{+\infty} \frac{a_n}{n+1} x^{n+1}$ 和 $\sum_{n=1}^{+\infty} n a_n x^{n-1}$ 有相同的收敛半径.

可以看出, 幂级数所有可能的收敛域共有如下五种情况 (其中 $R \in (0, +\infty)$):

$$
\{0 \}, \quad (- R, R), \quad [ - R, R), \quad (- R, R ], \quad [ - R, R ], \quad (- \infty , + \infty).
$$

## 习题 13.1

1. 求下列幂级数的收敛半径,并判断它们在收敛区间端点的收敛性:

(1) $\sum_{n=1}^{+\infty} \frac{x^n}{n(n+1)}$;

(2) $\sum_{n=1}^{+\infty}\left(1 + \frac{1}{n}\right)^{2}x^{n}$;

(3) $\sum_{n=1}^{+\infty} \frac{(n!)^2}{(2n)!} x^n$;
(4) $\sum_{n=1}^{+\infty}\left(1+\frac{1}{2}+\cdots+\frac{1}{n}\right)x^{n};$
(5) $\sum_{n=1}^{+\infty} \frac{x^n}{n^\alpha}, \alpha \in \mathbb{R}$;
(6) $\sum_{n=1}^{+\infty} \frac{(\ln n)^{\alpha}}{n^{2}} x^{n}, \alpha \in \mathbb{R}$.

2. 求幂级数  $\sum_{n=1}^{+\infty}\frac{\sin n\alpha}{n}x^{n}$  的收敛半径, 其中  $\alpha$  为常数.

3. 设  $\sum_{n=0}^{+\infty}a_{n}$  是一个发散的正项级数, 如果  $\lim_{n\to+\infty}\frac{a_{n}}{a_{0}+a_{1}+\cdots+a_{n}}=0$  , 那么级数  $\sum_{n=0}^{+\infty}a_{n}x^{n}$  的收敛半径 R=1. 试证之.

4. 设

$$
l = \varliminf_ {n \to + \infty} \left| \frac {a _ {n}}{a _ {n + 1}} \right|, \quad L = \varlimsup_ {n \to + \infty} \left| \frac {a _ {n}}{a _ {n + 1}} \right|.
$$

如果幂级数 $\sum_{n=0}^{+\infty} a_n x^n$ 的收敛半径为 $R$，证明:

$$
\frac {1}{L} \leqslant R \leqslant \frac {1}{l}.
$$

进一步问:有没有可能使得上述两个不等式都成立严格不等号？

5. 设幂级数 $\sum_{n=0}^{+\infty} a_n x^n$ 的收敛半径为 1, 且 $\lim_{x \to 1^-} \sum_{n=0}^{+\infty} a_n x^n = A$. 如果 $a_n \geqslant 0$, 证明:

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} = A.
$$

## 13.2 幂级数在收敛域内的性质

如果幂级数 $\sum_{n=0}^{+\infty} a_n x^n$ 的收敛半径 $R > 0$, 则在收敛区间 $(-R, R)$ 内幂级数可以定义出一个和函数 $S(x)$. 作为一类特殊的函数项级数, 我们自然很感兴趣于 $S(x)$ 的几个基本性质, 比如连续性、可微性和可积性. 由于幂级数的通项 $a_n x^n$ 总是连续、可微和可积的, 根据前面章节关于一般形式的函数项级数理论, 我们工作的重点也就自然转向了收敛域内幂级数一致收敛方面的讨论.

## 13.2.1 和函数的连续性

关于幂级数和函数的连续性, 有下面的结论:

定理 13.2.1 (Abel 第二定理) 设幂级数  $\sum_{n=0}^{+\infty} a_{n} x^{n}$  的收敛半径为 R (0 < R < +∞). 则

(1) 幂级数在收敛区间  $(-R, R)$  内闭绝对一致收敛.
(2) 若  $\sum_{n=0}^{+\infty}a_{n}R^{n}$  收敛, 则级数在  $(-R,R]$  的任何闭子区间一致收敛, 特别地,

$$
\lim _ {x \to R ^ {-}} \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = \sum_ {n = 0} ^ {+ \infty} a _ {n} R ^ {n}.
$$

(3) 若  $\sum_{n=0}^{+\infty}a_{n}(-R)^{n}$  收敛, 则级数在  $[-R,R)$  的任何闭子区间一致收敛, 特别地,

$$
\lim _ {x \to - R ^ {+}} \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n} = \sum_ {n = 0} ^ {+ \infty} a _ {n} (- R) ^ {n}.
$$

证明 根据函数项级数内闭一致收敛的定理, 知结论 (1) 显然成立.

现设 $\sum_{n=0}^{+\infty} a_n R^n$ 收敛, 考虑 $\sum_{n=0}^{+\infty} a_n x^n = \sum_{n=0}^{+\infty} a_n R^n \left( \frac{x}{R} \right)^n$. 在 $[0, R]$ 上, $\left| \left( \frac{x}{R} \right)^n \right| \leqslant 1$, 且 $\left( \frac{x}{R} \right)^n$ 关于 $n$ 单调. 由 Abel 判别法可知 $\sum_{n=0}^{+\infty} a_n x^n$ 在 $[0, R]$ 中一致收敛, 其和函数 $S(x)$ 在 $[0, R]$ 中连续, 因此

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} R ^ {n} = S (R) = \lim _ {x \to R ^ {-}} S (x) = \lim _ {x \to R ^ {-}} \sum_ {n = 0} ^ {+ \infty} a _ {n} x ^ {n}.
$$

完全类似可以证明情况 (3) 在 $x =  - R$ 收敛时的情况.

注意, 一个幂级数的收敛半径为 $R > 0$, 一般来说我们得不出该级数在收敛区间内的一致收敛性, 比如级数 $\sum_{n=1}^{+\infty} x^n$ 在 $(-1,1)$ 中就不一致收敛. 但是我们能保证在收敛区间内的内闭绝对一致收敛性. 事实上, 如果幂级数在它收敛区间的端点 $x = R$ 处是发散的, 那么级数在区间 $[0,R)$ 是不可能一致收敛的. 这是因为, 如果一致收敛性成立的话, 根据上述定理, 可以对级数逐项取极限 $x \to R^{-}$ 得到一个收敛级数 $\sum_{n=0}^{+\infty} a_n R^n$, 矛盾.

Abel 定理有很重要的应用. 比如, 如果在收敛区间  $(-R, R)$  内

$$
f (x) = \sum_ {n = 1} ^ {+ \infty} a _ {n} x ^ {n} \quad (- R <   x <   R), \tag {13.2.1}
$$

若又知 $f(x)$ 在区间的某端点，比如 $x = R$ 处连续，且在 $x = R$ 处右端的幂级数也收敛，则此展开式在这端点上也成立.即关系式(13.2.1)可以延拓到 $(-R,R]$.

例13.2.1 在 $-1 < x < 1$ 时成立展开式

$$
\ln (1 + x) = x - \frac {x ^ {2}}{2} + \frac {x ^ {3}}{3} - \dots .
$$

由于 x = 1 时右端的幂级数收敛, 左端的函数  $\ln(1 + x)$  在 x = 1 处也连续, 则级数的和为  $\ln 2$ . 即

$$
1 - \frac {1}{2} + \frac {1}{3} - \frac {1}{4} + \dots = \ln 2.
$$

值得指出的是, 如果关系式 (13.2.1) 左端的函数在区间端点不连续, 或者右端的幂级数在端点不收敛, 则一般不可在关系式两端取 $x \to R^{-}$ 或 $x \to -R^{+}$ 的极限. 换句话说, Abel 定理的逆定理不加额外条件的话, 一般来说不成立.

考虑如下经典例子:幂级数

$$
\frac {1}{1 + x} = \sum_ {n = 0} ^ {+ \infty} (- 1) ^ {n} x ^ {n}
$$

的收敛半径为 $R = 1$ ，在 $x = 1$ 处，左端函数连续，其值为 $\frac{1}{2}$ ，但右端为发散级数$\sum_{n = 0}^{+\infty}(-1)^n.$

研究级数求和方式的推广以及 Abel 定理的逆定理方面的问题, 是一个系统和专门的课题, 这些推广使得在经典定义下发散的级数有可能在新的定义下收敛并可求和. 几种常见的推广有: Cesàro 求和、Abel 求和、Euler 求和、Borel 求和等. 特别地, 在所谓的 Abel 求和意义下, 就可以对 “等式”

$$
1 - 1 + 1 - 1 + \dots = \frac {1}{2}
$$

给出某种“合理”的解释. 感兴趣的读者可以参阅有关级数求和的 Tauber 理论等方面的资料. 我们下面简单介绍一个相关结论.

定理 13.2.2 (Tauber $^{①}$ 定理) 设 $|x|<1$ 时, $f(x)=\sum_{n=0}^{+\infty}a_{n}x^{n}$, 其中 $\lim_{n\to+\infty}na_{n}=$

0. 如果 $\lim_{x\to1^{-}}f(x)=S$, 则 $\sum_{n=0}^{+\infty}a_{n}$ 收敛, 且其和为 S.

证明 考虑

$$
\left| \sum_ {k = 0} ^ {n} a _ {k} - S \right| = \left| \sum_ {k = 0} ^ {n} a _ {k} - \sum_ {k = 0} ^ {+ \infty} a _ {k} x ^ {k} + \sum_ {k = 0} ^ {+ \infty} a _ {k} x ^ {k} - S \right|
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Tauber, Alfred, 1866 年 11 月 5 日 — 1942 年 7 月 26 日, 奥地利数学家.</span></small>