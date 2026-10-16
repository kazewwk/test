因此 A 为零测集.

(2) 设 $A = \{x_{i}\}_{i=1}^{\infty}$ 为可数点集, 任给 $\varepsilon > 0$, 记

$$
I _ {i} = \left(x _ {i} - \frac {\varepsilon}{2 ^ {i + 1}}, x _ {i} + \frac {\varepsilon}{2 ^ {i + 1}}\right), i = 1, 2, \dots .
$$

显然， $\{I_{i}\}$  组成了 A 的一个覆盖，且

$$
\sum_ {i = 1} ^ {\infty} | I _ {i} | = \sum_ {i = 1} ^ {\infty} 2 \frac {\varepsilon}{2 ^ {i + 1}} \leqslant \varepsilon ,
$$

因此 A 为零测集.

(3) 按定义, 这是显然的.

(4) 设 $A_{i} (i \geqslant 1)$ 为一列零测集. 于是任给 $\varepsilon > 0$, 对于每一个 $i$, 存在覆盖 $A_{i}$ 的开区间 $\{I_{ij}\}$, 使得 $\{I_{ij}\}$ 中任意有限个区间的长度之和均不超过 $\frac{\varepsilon}{2^{i}}$. 由于可数个可数集的并集仍是可数的, 故所有这些开区间 $\{I_{ij}\}$ 仍组成了 $\{A_{i}\}$ 的并集的覆盖, 且任意有限个开区间的长度和不超过

$$
\frac {\varepsilon}{2} + \frac {\varepsilon}{2 ^ {2}} + \frac {\varepsilon}{2 ^ {3}} + \dots \leqslant \varepsilon .
$$

因此  $\{A_{i}\}$  的并集仍为零测集.

设 $f$ 为 $[a,b]$ 上的有界函数, 它在 $x \in [a,b]$ 处的振幅为

$$
\omega (f, x) = \lim _ {r \to 0 ^ {+}} \sup \{| f (x _ {1}) - f (x _ {2}) | | x _ {1}, x _ {2} \in (x - r, x + r) \cap [ a, b ] \}.
$$

f 的间断点的全体记为  $D_{f}$ ，则

$$
D _ {f} = \{x \in [ a, b ] \mid \omega (f, x) > 0 \}.
$$

当 $\delta > 0$ 时, 记

$$
D _ {f} (\delta) = \{x \in [ a, b ] \mid \omega (f, x) \geqslant \delta \},
$$

则

$$
D _ {f} = \bigcup_ {n = 1} ^ {\infty} D _ {f} (1 / n). \tag {9.2.1}
$$

定理 9.2.2 (Lebesgue) 设 f 为  $[a, b]$  上的有界函数，则  $f \in R[a, b]$  当且仅当其间断点集  $D_{f}$  为零测集.

证明 (必要性) 设 $f \in R[a, b]$. 固定 $\delta > 0$. 根据 Riemann 定理, 任给 $\varepsilon > 0$, 存在 $[a, b]$ 的分割

$$
\mathrm{P}: a = x _ {0} <   x _ {1} <   \dots <   x _ {n} = b,
$$

使得

$$
\sum_ {i = 1} ^ {n} \omega_ {i} \Delta x _ {i} <   \varepsilon \frac {\delta}{2}.
$$

如果 $x \in D_f(\delta) \cap (x_{i-1}, x_i)$, 则显然 $\omega_i \geqslant \omega(f, x) \geqslant \delta$. 因此从上式可得

$$
\sum_ {\{i | D _ {f} (\delta) \cap (x _ {i - 1}, x _ {i}) \neq \varnothing \}} \Delta x _ {i} <   \frac {\varepsilon}{2}.
$$

显然

$$
D _ {f} (\delta) \subseteq \left(\bigcup_ {\{i | D _ {f} (\delta) \cap (x _ {i - 1}, x _ {i}) \neq \varnothing \}} (x _ {i - 1}, x _ {i})\right) \cup \left(\bigcup_ {i = 0} ^ {n} \left(x _ {i} - \frac {\varepsilon}{4 (n + 1)}, x _ {i} + \frac {\varepsilon}{4 (n + 1)}\right)\right),
$$

且

$$
\sum_ {\{i | D _ {f} (\delta) \cap (x _ {i - 1}, x _ {i}) \neq \varnothing \}} \Delta x _ {i} + \frac {2 \varepsilon}{4 (n + 1)} (n + 1) <   \frac {\varepsilon}{2} + \frac {\varepsilon}{2} = \varepsilon ,
$$

由定义即知 $D_{f}(\delta)$ 为零测集. 由(9.2.1)式可知 $D_{f}$ 为零测集

(充分性) 任给 $\varepsilon, \eta > 0$, 由 $D_{f}$ 为零测集可知, 存在开区间 $\{(\alpha_{j}, \beta_{j})\}_{j \geqslant 1}$, 使得

$$
D _ {f} \subseteq \bigcup_ {j \geqslant 1} (\alpha_ {j}, \beta_ {j}), \quad \sum_ {j \geqslant 1} (\beta_ {j} - \alpha_ {j}) <   \varepsilon .
$$

当 $x \in [a, b] \setminus \bigcup_{j \geqslant 1} (\alpha_j, \beta_j)$ 时, $f$ 在 $x$ 处连续, 故存在包含 $x$ 的开区间 $I_x$, 使得 $f$ 在 $I_x$ 上的振幅小于 $\eta$. 根据Lebesgue覆盖引理, 可取 $[a, b]$ 的分割

$$
\mathrm{P}: a = x _ {0} <   x _ {1} <   \dots <   x _ {n} = b,
$$

使得每一个小区间 $[x_{i - 1},x_i]$ 必含于某个 $(\alpha_{j},\beta_{j})$ 或某个 $I_{x}$ 之中.此时

$$
\sum_ {\{i | \omega_ {i} \geqslant \eta \}} \Delta x _ {i} \leqslant \sum_ {j \geqslant 1} (\beta_ {j} - \alpha_ {j}) <   \varepsilon ,
$$

由 Riemann 定理可知 $f \in R[a, b]$.

## 习题9.2

1. 请说明在零测集的定义中可以将“开区间”换成“闭区间”.
2. 利用 Lebesgue 定理重新证明命题 9.1.7 和例 9.2.1.
3. 设 $f$ 为定义在 $[a, b]$ 上的函数, 证明: 若 $f^2 \in R[a, b]$, 则 $|f| \in R[a, b]$.
4. 设 $f \in R[a, b]$, 如果 $f$ 处处大于零, 证明: $f$ 在 $[a, b]$ 上的积分也大于零.

5. 设 $A \subseteq \mathbb{R}$, 考虑 $A$ 的特征函数 $\chi_A: \mathbb{R} \to \mathbb{R}$:

$$
\chi_ {A} (x) = \left\{ \begin{array}{l l} 1, & x \in A, \\ 0, & x \in \mathbb {R} \setminus A. \end{array} \right.
$$

如果 $A$ 为闭的零测集, 证明: $\chi_A$ 在任何闭区间上均可积且积分等于零.

6. 设 $a, b \in \mathbb{R}, a < b$. 证明: 区间 $[a, b]$ 不是零测集.

7. 设 $f, g \in R[a, b]$, 如果 $f$ 与 $g$ 只在一个零测集上不相等, 证明: 它们的积分相等.

8. 设 $f \in R[a, b]$, $g$ 为有界函数且与 $f$ 只在一个闭的零测集上不相等, 证明: $g \in R[a, b]$.

9. 有理数的全体记为 $\{r_n\}_{n=1}^{\infty}$. 令

$$
U = \bigcup_ {n = 1} ^ {\infty} \left(r _ {n} - 2 ^ {- n}, r _ {n} + 2 ^ {- n}\right),
$$

问: $\mathbb{R} \setminus U$ 是否为零测集? 请说明理由.

## 9.3 微积分基本定理

从历史上来看, 积分概念的形成先于微分概念, 但积分的通用计算方法却直到 17 世纪中叶才由 Newton 和 Leibniz 所发现.

定理 9.3.1 (Newton-Leibniz 公式) 设 F 在  $[a, b]$  上可导且  $f = F' \in R[a, b]$ , 则

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = F (b) - F (a). \tag {9.3.1}
$$

证明 设 n 为正整数, 将  $[a, b]$  作 n 等分, 分点记为  $\{x_{i}\}_{i=0}^{n}$ . 当  $i = 1, 2, \cdots, n$  时, 由 Lagrange 微分中值定理可知, 存在  $\xi_{i} \in [x_{i-1}, x_{i}]$ , 使得

$$
F (x _ {i}) - F (x _ {i - 1}) = F ^ {\prime} (\xi_ {i}) (x _ {i} - x _ {i - 1}) = f (\xi_ {i}) \Delta x _ {i}.
$$

此时有

$$
\sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} = \sum_ {i = 1} ^ {n} (F (x _ {i}) - F (x _ {i - 1})) = F (x _ {n}) - F (x _ {0}) = F (b) - F (a).
$$

令 $n\to \infty$ ，由 $f\in R[a,b]$ 即得(9.3.1)式注 9.3.1 只要 F 连续, 至多在有限个点处不可导, 且  $F' \in R[a, b]$ , 则定理结论仍成立. 这只要将  $[a, b]$  分成有限个小区间, 然后在每一个小区间中运用 Newton-Leibniz 公式即可.

推论 9.3.2 设 $F \in  {C}^{1}\left\lbrack  {a,b}\right\rbrack$ ,则

$$
\int_ {a} ^ {b} F ^ {\prime} (x) \mathrm{d} x = F (b) - F (a). \tag {9.3.2}
$$

证明 当 $F \in C^{1}[a, b]$ 时 $F' \in C[a, b]$, 因此 $F' \in R[a, b]$, 由上述定理即得欲证结论. $\square$

注9.3.2 我们经常用记号 $F\big|_{a}^{b}$ 表示 $F(b) - F(a)$.

有了 Newton-Leibniz 公式, 要计算某个函数的积分, 只要能求出该函数的原函数即可. 为了研究原函数的存在性, 我们先来介绍积分的几个基本性质.

为了方便起见, 我们约定

当 $a = b$ 时， $\int_{a}^{b}f(x)\mathrm{d}x = 0;$ 当 $a <   b$ 时， $\int_{b}^{a}f(x)\mathrm{d}x = -\int_{a}^{b}f(x)\mathrm{d}x.$

定理 9.3.3 (1) 设 $f, g \in  R\left\lbrack  {a,b}\right\rbrack  ,\lambda ,\mu  \in  \mathbb{R}$ ,则

$$
\int_ {a} ^ {b} (\lambda f + \mu g) \mathrm{d} x = \lambda \int_ {a} ^ {b} f (x) \mathrm{d} x + \mu \int_ {a} ^ {b} g (x) \mathrm{d} x.
$$

(2) 设 $f \in R[a, b]$, $c \in (a, b)$, 则

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \int_ {a} ^ {c} f (x) \mathrm{d} x + \int_ {c} ^ {b} f (x) \mathrm{d} x.
$$

证明 (1) 任给 $\varepsilon > 0$, 由 $f, g$ 可积知, 存在 $\delta > 0$, 当 $[a, b]$ 的分割 $\mathrm{P}$ 满足 $\| \mathrm{P} \| < \delta$ 时,

$$
\left| \sum_ {i = 1} ^ {n} f (\xi_ {i}) \Delta x _ {i} - \int_ {a} ^ {b} f (x) \mathrm{d} x \right| <   \varepsilon , \quad \left| \sum_ {i = 1} ^ {n} g (\xi_ {i}) \Delta x _ {i} - \int_ {a} ^ {b} g (x) \mathrm{d} x \right| <   \varepsilon .
$$

记

$$
h = \lambda f + \mu g, I = \lambda \int_ {a} ^ {b} f (x) \mathrm{d} x + \mu \int_ {a} ^ {b} g (x) \mathrm{d} x,
$$

由前式可得

$$
\left| \sum_ {i = 1} ^ {n} h (\xi_ {i}) \Delta x _ {i} - I \right| <   (| \lambda | + | \mu |) \varepsilon ,
$$

这说明 h 可积, 且积分等于 I.

(2) 由推论 9.1.6 可知 f 在  $[a, c]$  和  $[c, b]$  上均可积. 设  $P_{1}, P_{2}$  分别是  $[a, c]$  和  $[c, b]$  的分割, 当  $\|P_{1}\| \to 0, \|P_{2}\| \to 0$  时,  $P = P_{1} \cup P_{2}$  也满足条件  $\|P\| \to 0$ . 于是

$$
\begin{array}{l} \int_{a}^{b}f(x)\mathrm{d}x = \lim_{\substack{\| \mathrm{P}_{1}\| \to 0\\ \| \mathrm{P}_{2}\| \to 0}}\sum_{\mathrm{P}_{1}\cup \mathrm{P}_{2}}f(\xi_{i})\Delta x_{i} \\ = \int_ {a} ^ {c} f (x) \mathrm{d} x + \int_ {c} ^ {b} f (x) \mathrm{d} x. \\ \end{array}
$$

$$
= \lim _ {\| \mathrm{P} _ {1} \| \to 0} \sum_ {\mathrm{P} _ {1}} f (\xi_ {i}) \Delta x _ {i} + \lim _ {\| \mathrm{P} _ {2} \| \to 0} \sum_ {\mathrm{P} _ {2}} f (\xi_ {i}) \Delta x _ {i}
$$

![](images/page_324_image_5.jpg)

注9.3.3 根据之前的约定, 如果 $a, b, c$ 属于 $f$ 的某个可积区间, 则不论它们的相对位置如何, (2) 中等式仍成立, 这称为积分关于区间的可加性.

定理 9.3.4 (1) 设 f 为  $[a, b]$  上的非负可积函数，则其积分非负.

(2) 设 $f, g \in R[a, b]$, 且 $f(x) \geqslant g(x)$, 则

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x \geqslant \int_ {a} ^ {b} g (x) \mathrm{d} x.
$$

(3) 设 $f \in R[a, b]$, 则

$$
\left| \int_ {a} ^ {b} f (x) \mathrm{d} x \right| \leqslant \int_ {a} ^ {b} | f (x) | \mathrm{d} x.
$$

证明 (1) 如果 $f$ 非负可积, 则其积分和总是非负的, 从而积分非负.

(2) 由定理 9.3.3 可知 $f - g \in R[a, b]$, 由 (1) 可知

$$
0 \leqslant \int_ {a} ^ {b} (f - g) \mathrm{d} x = \int_ {a} ^ {b} f (x) \mathrm{d} x - \int_ {a} ^ {b} g (x) \mathrm{d} x.
$$

(3) 由命题 9.1.7 可知 $|f| \in R[a, b]$. 任给 $[a, b]$ 的分割 P, 均有

$$
\left| \sum_ {\mathrm{P}} f (\xi_ {i}) \Delta x _ {i} \right| \leqslant \sum_ {\mathrm{P}} | f (\xi_ {i}) | \Delta x _ {i},
$$

令  $\|P\|\rightarrow0$  即得欲证结论.

设 $f \in R[a, b]$, 我们想要寻找 $f$ 的原函数. 受 Newton-Leibniz 公式的启发, 考虑所谓变限积分

$$
F (x) = \int_ {a} ^ {x} f (t) \mathrm{d} t, x \in [ a, b ]. \tag {9.3.3}
$$

设 $|f| \leqslant M$，当 $x, y \in [a, b]$ 时，由积分的上述性质可得

$$
| F (x) - F (y) | = \left| \int_ {y} ^ {x} f (t) \mathrm{d} t \right| \leqslant M | x - y |,
$$

这说明 F 为 Lipschitz 函数. 进一步, 我们有

定理9.3.5 设 $f \in R[a, b]$, $F$ 如 (9.3.3) 式所定义. 如果 $f$ 在 $x_0$ 处连续, 则 $F$ 在 $x_0$ 处可导, 且 $F'(x_0) = f(x_0)$.

证明 由积分的性质可得

$$
F (x) - F (x _ {0}) = \int_ {x _ {0}} ^ {x} f (t) \mathrm{d} t = f (x _ {0}) (x - x _ {0}) + E (x),
$$

其中

$$
E (x) = \int_ {x _ {0}} ^ {x} [ f (t) - f (x _ {0}) ]   \mathrm{d} t.
$$

由 $f$ 在 $x_0$ 处连续可知, 任给 $\varepsilon > 0$, 存在 $\delta > 0$, 当 $|x - x_0| < \delta$ 时 $|f(x) - f(x_0)| < \varepsilon$. 此时, 若 $t$ 介于 $x$ 和 $x_0$ 之间, 则 $|f(t) - f(x_0)| < \varepsilon$. 由积分的绝对值性质可得

$$
| E (x) | \leqslant \varepsilon | x - x _ {0} |.
$$

这说明 $F$ 在 $x_0$ 处可微 (可导), 且 $F'(x_0) = f(x_0)$.

![](images/page_325_image_10.jpg)

下面的重要结果和 Newton-Leibniz 公式一起常称为微积分基本定理:

定理 9.3.6 设  $f \in C[a, b]$ ，F 如 (9.3.3) 式所定义，则 F 为 f 的一个原函数.

证明 这是前一定理的直接推论.

![](images/page_325_image_14.jpg)

注 9.3.4 可积函数未必有原函数. 例如, 考虑如下阶梯函数:

$$
f (x) = - 1, \quad x \in [ 0, 1 ]; \quad f (x) = 1, \quad x \in (1, 2 ].
$$

显然, $f \in R[0,2]$ . 由关于导数的 Darboux 介值定理可知 f 不存在原函数.

推论 9.3.7 设  $f \in C[a, b]$ ,  $u, v : (c, d) \to [a, b]$  均为可导函数, 记

$$
G (x) = \int_ {v (x)} ^ {u (x)} f (t)   \mathrm{d} t, x \in [ c, d ],
$$

则 $G^{\prime}(x) = f(u(x))u^{\prime}(x) - f(v(x))v^{\prime}(x)$.

证明 设 $F$ 如 (9.3.3) 式所定义, 则 $G(x) = F(u(x)) - F(v(x))$. 由复合函数求导的链式法则可得

$$
G ^ {\prime} (x) = F ^ {\prime} (u (x)) u ^ {\prime} (x) - F ^ {\prime} (v (x)) v ^ {\prime} (x) = f (u (x)) u ^ {\prime} (x) - f (v (x)) v ^ {\prime} (x).
$$

![](images/page_325_image_23.jpg)

例 9.3.1 设  $F(x)=\int_{-x}^{2x}\frac{\sin t}{t}\mathrm{d}t,$  求  $F'(x)$  及  $F'(0).$

解 在 $t = 0$ 处规定 $\frac{\sin t}{t}$ 等于1, 此时 $\frac{\sin t}{t}$ 为 $\mathbb{R}$ 上的连续函数. 由上述推论可得

$$
F ^ {\prime} (x) = \frac {\sin (2 x)}{2 x} (2 x) ^ {\prime} - \frac {\sin (- x)}{- x} (- x) ^ {\prime} = \frac {1}{x} (\sin x + \sin 2 x),
$$

特别地, $F'(0)=3$ .

## 习题 9.3

1. 设 $f \in R[a, b]$, $F \in C[a, b]$. 如果 $F$ 在 $(a, b)$ 上可导且 $F' = f$, 证明:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = F (b) - F (a).
$$

2. 举例说明, 当 $F$ 在 $[a, b]$ 上可导时, $F'$ 在 $[a, b]$ 上未必可积.

3. 指出下列计算过程中的错误之处:

$$
\int_ {- 1} ^ {1} \frac {\mathrm{d} x}{1 + x ^ {2}} = - \arctan \frac {1}{x} \Big | _ {- 1} ^ {1} = - \frac {\pi}{2}.
$$

4. 利用 Newton-Leibniz 公式计算下列积分:

(1) $\int_0^1 x^2\mathrm{d}x;$

(2) $\int_{a}^{b}\sin x\mathrm{d}x;$

(3) $\int_{0}^{\pi}\cos^{2}x\mathrm{d}x.$

5. 利用积分求下列极限:

(1)  $\lim_{n\to\infty}\left(\frac{1}{n^{2}}+\frac{2}{n^{2}}+\cdots+\frac{n-1}{n^{2}}\right)$ ;
(2) $\lim_{n\to\infty}\frac{1}{n}\left(\sin\frac{\pi}{n}+\sin\frac{2\pi}{n}+\cdots+\sin\frac{n-1}{n}\pi\right);$
(3)  $\lim_{n\to\infty}\frac{1}{n^{4}}\left(1+2^{3}+\cdots+n^{3}\right).$

6. 设 $f \in C[a, b]$ 且 $\int_{a}^{b} f^{2}(x) \, \mathrm{d}x = 0$, 证明: $f \equiv 0$.

7. 设 $f, g \in R[a, b]$, 证明:

$$
\left| \int_ {a} ^ {b} f (x) g (x)   \mathrm{d} x \right| \leqslant \left(\int_ {a} ^ {b} f ^ {2} (x)   \mathrm{d} x\right) ^ {\frac {1}{2}} \left(\int_ {a} ^ {b} g ^ {2} (x)   \mathrm{d} x\right) ^ {\frac {1}{2}}.
$$

8. 设 $f \in C^{1}[a, b]$ 且 $f(a) = 0$, 证明:

$$
\int_ {a} ^ {b} f ^ {2} (x) \mathrm{d} x \leqslant \frac {(b - a) ^ {2}}{2} \int_ {a} ^ {b} [ f ^ {\prime} (x) ] ^ {2} \mathrm{d} x.
$$

9. 设 $f \in C^{1}[a, b]$, 证明:

$$
\max _ {a \leqslant x \leqslant b} | f (x) | \leqslant \frac {1}{b - a} \left| \int_ {a} ^ {b} f (x) \mathrm{d} x \right| + \int_ {a} ^ {b} | f ^ {\prime} (x) | \mathrm{d} x.
$$

10. 求下列函数的导数:

(1) $F(x) = \int_{0}^{\cos^{2}x}\sqrt{1 + t^{2}}\mathrm{d}t;$

(2) $F(x) = \int_{\sin x}^{x}\frac{\mathrm{d}t}{\sqrt{1 + \sin^2t}};$

(3) $F(x) = \int_{a}^{b}\sin (x + t)\mathrm{d}t.$

11. 求下列极限:

(1) $\lim_{x\to 0}\frac{1}{x^4}\int_0^x\sin^3 t\mathrm{d}t;$

(2) $\lim_{x\to 0}\frac{1}{x}\int_0^x\cos t^2\mathrm{d}t;$

(3) $\lim_{x\to +\infty}\frac{\mathrm{e}^{-x^2}}{x}\int_0^x t^2\mathrm{e}^{t^2}\mathrm{d}t.$

12. 设 $f \in C(0, +\infty)$, 如果

$$
\int_ {0} ^ {x} f (t) \mathrm{d} t = \frac {1}{2} x f (x), \forall x > 0,
$$

证明: 存在常数 c, 使得  $f(x) = cx$ .

13. 设 f 为 n 次实系数多项式, 证明:

$$
\int_ {a} ^ {b} | f ^ {\prime} (x) | \mathrm{d} x \leqslant 2 n \max _ {a \leqslant x \leqslant b} | f (x) |.
$$

14. 设 $f$ 是 $[a, b]$ 上的凸函数, 证明: $f \in R[a, b]$ 且

$$
(b - a) f \Big (\frac {a + b}{2} \Big) \leqslant \int_ {a} ^ {b} f (x) \mathrm{d} x \leqslant (b - a) \frac {f (a) + f (b)}{2}.
$$

## 9.4 积分的计算

微积分基本定理将微分和积分统一在一个公式中, 是计算积分的有力工具. 下面我们来讨论微积分基本定理的变化形式, 由此得到计算积分的两个基本方法: 换元法和分部积分法.

定理 9.4.1（换元法） 设 f 在区间 I 上连续,  $\varphi$  在  $[\alpha, \beta]$  上可导且  $\varphi' \in R[\alpha, \beta]$ . 若  $\varphi([\alpha, \beta]) \subseteq I$ , 则

$$
\int_ {\varphi (\alpha)} ^ {\varphi (\beta)} f (x) \mathrm{d} x = \int_ {\alpha} ^ {\beta} f (\varphi (t)) \varphi^ {\prime} (t) \mathrm{d} t.
$$

证明 取 $a \in I$, 设 $F$ 由 (9.3.3) 式所定义. 由定理 9.3.6 可知 $F' = f$, 故

$$
\frac {\mathrm{d}}{\mathrm{d} t} F (\varphi (t)) = F ^ {\prime} (\varphi (t)) \varphi^ {\prime} (t) = f (\varphi (t)) \varphi^ {\prime} (t).
$$

由 Newton-Leibniz 公式可得

$$
\int_ {\alpha} ^ {\beta} f (\varphi (t)) \varphi^ {\prime} (t) \mathrm{d} t = F (\varphi (\beta)) - F (\varphi (\alpha)) = \int_ {\varphi (\alpha)} ^ {\varphi (\beta)} f (x) \mathrm{d} x.
$$

例 9.4.1 设 f 是周期函数, T 为其周期. 如果  $f \in R[0, T]$ , 证明: 任给  $a \in R$ , 均有

$$
\int_ {a} ^ {a + T} f (x) \mathrm{d} x = \int_ {0} ^ {T} f (x) \mathrm{d} x.
$$

证明 由题设可知 $f$ 在每一个闭区间上都是可积的. 由积分关于区间的可加性质可得

$$
\int_ {a} ^ {a + T} f (x) \mathrm{d} x = \int_ {a} ^ {0} f (x) \mathrm{d} x + \int_ {0} ^ {T} f (x) \mathrm{d} x + \int_ {T} ^ {a + T} f (x) \mathrm{d} x.
$$

利用变换 $x = t + T$ ，上式右边第三个积分成为

$$
\int_ {0} ^ {a} f (t + T) \mathrm{d} t = \int_ {0} ^ {a} f (t) \mathrm{d} t,
$$

代入前式就得到了等式的证明.

例 9.4.2 计算积分  $\int_{0}^{1}\frac{\sqrt{x}}{1+x}dx.$

解 令 $x = t^2, t \in [0,1]$, 则

$$
\begin{array}{l} \int_ {0} ^ {1} \frac {\sqrt {x}}{1 + x} \mathrm{d} x = 2 \int_ {0} ^ {1} \frac {t ^ {2}}{1 + t ^ {2}} \mathrm{d} t = 2 - 2 \int_ {0} ^ {1} \frac {\mathrm{d} t}{1 + t ^ {2}} \\ = 2 - 2 (\arctan t) \big | _ {0} ^ {1} = 2 - \pi / 2. \\ \end{array}
$$

![](images/page_328_image_10.jpg)

例 9.4.3 计算积分  $\int_{0}^{1}\sqrt{1-x^{2}}\mathrm{d}x$ .

解 令 $x = \cos t, t \in \left[0, \frac{\pi}{2}\right]$, 则

$$
\begin{array}{l} \int_ {0} ^ {1} \sqrt {1 - x ^ {2}} \mathrm{d} x = \int_ {\frac {\pi}{2}} ^ {0} \sqrt {1 - \cos^ {2} t} (\cos t) ^ {\prime} \mathrm{d} t \\ = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {2} t \mathrm{d} t = \int_ {0} ^ {\frac {\pi}{2}} \frac {1}{2} (1 - \cos (2 t)) \mathrm{d} t \\ = \frac {1}{2} \left(x - \frac {1}{2} \sin (2 x)\right) \Big | _ {0} ^ {\frac {\pi}{2}} = \frac {\pi}{4}. \\ \end{array}
$$

![](images/page_328_image_14.jpg)

注 9.4.1 我们计算出来的是单位圆盘在平面第一象限中的面积, 因此整个单位圆盘的面积等于  $\pi$ .

定理 9.4.2（分部积分） 设 u, v 为 [a, b] 上的可导函数且  $u', v' \in R[a, b]$ ，则

$$
\int_ {a} ^ {b} u (x) v ^ {\prime} (x) \mathrm{d} x = u v \big | _ {a} ^ {b} - \int_ {a} ^ {b} u ^ {\prime} (x) v (x) \mathrm{d} x.
$$

证明 由题设可知, $uv'$ 和 $u'v$ 均为可积函数. 由 $(uv)' = u'v + uv'$ 和 Newton-Leibniz 公式可得

$$
u v \big | _ {a} ^ {b} = \int_ {a} ^ {b} (u v) ^ {\prime} (x)   \mathrm{d} x = \int_ {a} ^ {b} u (x) v ^ {\prime} (x)   \mathrm{d} x + \int_ {a} ^ {b} u ^ {\prime} (x) v (x)   \mathrm{d} x,
$$

移项即得欲证等式.

例 9.4.4 计算积分  $\int_{0}^{\pi} x^{2} \cos x \, dx$ .

解 利用分部积分可得

$$
\begin{array}{l} \int_ {0} ^ {\pi} x ^ {2} \cos x \mathrm{d} x = \int_ {0} ^ {\pi} x ^ {2} (\sin x) ^ {\prime} \mathrm{d} x = x ^ {2} \sin x | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} (x ^ {2}) ^ {\prime} \sin x \mathrm{d} x \\ = \int_ {0} ^ {\pi} 2 x (\cos x) ^ {\prime} \mathrm{d} x = 2 x \cos x \big | _ {0} ^ {\pi} - \int_ {0} ^ {\pi} 2 \cos x \mathrm{d} x \\ = - 2 \pi - 2 \sin x \big | _ {0} ^ {\pi} = - 2 \pi. \\ \end{array}
$$

注意这个例子中通过转移导数降低 x 的幂次, 最后消去 x 的幂次. 有时可以暂时升高 x 的幂次再通过分部积分进行化简.

例 9.4.5 计算积分  $\int_{1}^{3} x^{2} \ln x \, dx$ .

解 利用分部积分可得

$$
\begin{array}{l} \int_ {1} ^ {3} x ^ {2} \ln x \mathrm{d} x = \int_ {1} ^ {3} \left(\frac {1}{3} x ^ {3}\right) ^ {\prime} \ln x \mathrm{d} x \\ = \left(\frac {1}{3} x ^ {3}\right) \ln x \Big | _ {1} ^ {3} - \int_ {1} ^ {3} \left(\frac {1}{3} x ^ {3}\right) (\ln x) ^ {\prime} \mathrm{d} x \\ = 9 \ln 3 - \int_ {1} ^ {3} \frac {1}{3} x ^ {2} \mathrm{d} x = 9 \ln 3 - \left. \frac {1}{9} x ^ {3} \right| _ {1} ^ {3} \\ = 9 \ln 3 - \frac {2 6}{9}. \\ \end{array}
$$

例 9.4.6 当 m 为非负整数时, 计算积分

$$
I _ {m} = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {m} x \mathrm{d} x, J _ {m} = \int_ {0} ^ {\frac {\pi}{2}} \cos^ {m} x \mathrm{d} x.
$$

解 利用变换 $x = \frac{\pi}{2} - t$ 易见 $J_{m} = I_{m}$. 我们用递推的方法来计算 $I_{m}$. 显然, $I_{0} = \frac{\pi}{2}, I_{1} = 1$. 当 $m \geqslant 2$ 时, 利用分部积分可得

$$
\begin{array}{l} I _ {m} = \int_ {0} ^ {\frac {\pi}{2}} \sin^ {m} x \mathrm{d} x = \int_ {0} ^ {\frac {\pi}{2}} (\sin^ {m - 1} x) (- \cos x) ^ {\prime} \mathrm{d} x \\ = (\sin^ {m - 1} x) (- \cos x) \big | _ {0} ^ {\frac {\pi}{2}} + \int_ {0} ^ {\frac {\pi}{2}} (m - 1) \sin^ {m - 2} x \cos^ {2} x \mathrm{d} x \\ = (m - 1) \int_ {0} ^ {\frac {\pi}{2}} \sin^ {m - 2} x \left(1 - \sin^ {2} x\right) \mathrm{d} x \\ = (m - 1) I _ {m - 2} - (m - 1) I _ {m}, \\ \end{array}
$$

这就得到了递推公式 $I_{m} = \frac{m - 1}{m} I_{m - 2}$, 从而有

$$
I _ {2 n} = \frac {2 n - 1}{2 n} I _ {2 n - 2} = \frac {2 n - 1}{2 n} \frac {2 n - 3}{2 n - 2} I _ {2 n - 4} = \dots = \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {\pi}{2}. \tag {9.4.1}
$$

同理可得

$$
I _ {2 n + 1} = \frac {(2 n) ! !}{(2 n + 1) ! !}.
$$

注意到当 $0 < x < \frac{\pi}{2}$ 时, $\sin^{2n + 1}x < \sin^{2n}x < \sin^{2n - 1}x$, 由积分的性质可得

$$
I _ {2 n + 1} <   I _ {2 n} <   I _ {2 n - 1},
$$

即

$$
\frac {(2 n) ! !}{(2 n + 1) ! !} <   \frac {(2 n - 1) ! !}{(2 n) ! !} \frac {\pi}{2} <   \frac {(2 n - 2) ! !}{(2 n - 1) ! !}.
$$

整理以后可得

$$
\frac {n \pi}{2 n + 1} <   \frac {1}{2 n + 1} \left(\frac {(2 n) ! !}{(2 n - 1) ! !}\right) ^ {2} <   \frac {\pi}{2}, \tag {9.4.2}
$$

由数列极限的夹逼准则可得

$$
\lim _ {n \to \infty} \frac {1}{2 n + 1} \left(\frac {(2 n) ! !}{(2 n - 1) ! !}\right) ^ {2} = \frac {\pi}{2}. \tag {9.4.3}
$$

上式称为 Wallis 公式.

分部积分还可以用来研究Taylor公式的余项.设 $f$ 为区间 $I$ 上的 $C^2$ 函数，当$x,x_0\in I$ 时，由分部积分可得

$$
\begin{array}{l} f (x) - f (x _ {0}) = \int_ {x _ {0}} ^ {x} f ^ {\prime} (t) \mathrm{d} t = \int_ {x _ {0}} ^ {x} f ^ {\prime} (t) (t - x) ^ {\prime} \mathrm{d} t \\ = f ^ {\prime} (t) (t - x) \big | _ {x _ {0}} ^ {x} - \int_ {x _ {0}} ^ {x} f ^ {\prime \prime} (t) (t - x) \mathrm{d} t \\ = f ^ {\prime} (x _ {0}) (x - x _ {0}) + \int_ {x _ {0}} ^ {x} f ^ {\prime \prime} (t) (x - t) \mathrm{d} t. \\ \end{array}
$$

若 $f$ 为 $C^3$ 函数, 则还可以继续做分部积分. 一般地, 我们有

定理 9.4.3 设 f 为区间 I 上的  $C^{n+1}$  函数,  $x, x_{0} \in I$ , 则

$$
f (x) = \sum_ {k = 0} ^ {n} \frac {f ^ {(k)} (x _ {0})}{k !} (x - x _ {0}) ^ {k} + R _ {n} (x),
$$

其中

$$
R _ {n} (x) = \frac {1}{n !} \int_ {x _ {0}} ^ {x} (x - t) ^ {n} f ^ {(n + 1)} (t) \mathrm{d} t. \tag {9.4.4}
$$

证明 我们对 $n$ 使用数学归纳法. $n = 0$ 的情形就是微积分基本定理. $n = 1$ 的情

形上面已经讨论过. 设 $n = m - 1$ 时结论成立, 则 $n = m$ 时, 利用分部积分可得

$$
\begin{array}{l} R _ {m - 1} (x) = \int_ {x _ {0}} ^ {x} \left(\frac {- 1}{m !} (x - t) ^ {m}\right) ^ {\prime} f ^ {(m)} (t) \mathrm{d} t \\ = \left(\frac {- 1}{m !} (x - t) ^ {m}\right) ^ {\prime} f ^ {(m)} (t) \Big | _ {x _ {0}} ^ {x} + \int_ {x _ {0}} ^ {x} \frac {1}{m !} (x - t) ^ {m} f ^ {(m + 1)} (t) \mathrm{d} t \\ = \frac {f ^ {(m)} (x _ {0})}{m !} (x - x _ {0}) ^ {m} + R _ {m} (x), \\ \end{array}
$$

这说明 n = m 时结论也成立.

![](images/page_331_image_5.jpg)

## 习题 9.4

1. 计算下列积分:

(1) $\int_0^1\frac{x}{(1 + x)^3}\mathrm{d}x;$

(2) $\int_0^1\ln (1 + \sqrt{x})\mathrm{d}x;$

(3) $\int_0^1\sqrt{\frac{1 - x}{1 + x}}\mathrm{d}x;$

(4) $\int_{0}^{1}\arctan\sqrt{\frac{1-x}{1+x}}\mathrm{d}x;$

(5) $\int_0^1 x\sqrt{1 - x}\mathrm{d}x;$

(6) $\int_{1}x^{2}\sqrt{1 - x^{2}}\mathrm{d}x.$

2. 计算下列积分:

(1) $\int_0^1\ln (x + \sqrt{1 + x^2})\mathrm{d}x;$

(2) $\int_0^1 x (\arctan x)^2 \, \mathrm{d}x$;

(3) $\int_0^\pi x^2\sin (3x)\mathrm{d}x;$

(4) $\int_0^\pi \mathrm{e}^x\cos (2x)\mathrm{d}x;$

(5) $\int_{0}^{\pi}\sin^{3}x\mathrm{d}x;$

(6) $\int_{-\pi}^{\pi} x^{2} \cos x \, \mathrm{d}x$;

(7) $\int_0^1 x^2 (1 - x^3)^5\mathrm{d}x;$

(8) $\int_0^1 (1 - x)^2 x^3\mathrm{d}x;$

(9) $\int_0^1\frac{\mathrm{d}x}{(2 - x^2)^2};$

(10) $\int_{0}^{1}\frac{\sqrt{1 + x^2}}{x^2}\mathrm{d}x.$

3. 设 0 < r < 1, 证明:

$$
\int_ {0} ^ {2 \pi} \frac {1 - r ^ {2}}{1 - 2 r \cos x + r ^ {2}} \mathrm{d} x = 2 \pi .
$$

4. 设 n 为正整数, 证明:

$$
\int_ {0} ^ {1} \frac {\mathrm{d} x}{(1 + x ^ {n}) \sqrt [ n ]{1 + x ^ {n}}} = \frac {1}{\sqrt [ n ]{2}}.
$$

5. 设 m, n 为非零整数, 证明:

(1) $\int_{-\pi}^{\pi}\sin^{2}mx\mathrm{d}x = \int_{-\pi}^{\pi}\cos^{2}mx\mathrm{d}x = \pi;$

(2) $\int_{-\pi}^{\pi}\sin mx\sin nx\mathrm{d}x = \int_{-\pi}^{\pi}\cos mx\cos nx\mathrm{d}x = 0 (m\neq \pm n);$
(3) $\int_{-\pi}^{\pi}\sin mx\cos nx\mathrm{d}x = 0.$

6. 求下列积分的递推公式 (m, n 为非负整数):

(1) $\int_{0}^{1}\frac{x^n}{1 + x}\mathrm{d}x;$
(2) $\int_0^1\frac{x^n}{1 + x^2}\mathrm{d}x;$
(3) $\int_{0}^{1}(1 - x^2)^n\mathrm{d}x;$
(4) $\int_{0}^{\frac{\pi}{2}}\cos^{n}x\sin nx\mathrm{d}x;$
(5) $\int_{0}^{\frac{\pi}{2}}\cos^{n}x\cos nx\mathrm{d}x;$
(6) $\int_{0}^{\frac{\pi}{2}}\cos^{m}x\sin^{n}x\mathrm{d}x;$
(7) $\int_{0}^{\frac{\pi}{4}}\tan^{n}x\mathrm{d}x;$
(8) $\int_{0}^{\frac{\pi}{2}}\frac{\sin nx}{\sin x}\mathrm{d}x;$
(9) $\int_{0}^{\frac{\pi}{2}}\frac{\sin^{2}nx}{\sin^{2}x}\mathrm{d}x.$

7. 设  $f \in C[0,1]$ ，证明:

$$
\int_ {0} ^ {\pi} x f (\sin x) \mathrm{d} x = \frac {\pi}{2} \int_ {0} ^ {\pi} f (\sin x) \mathrm{d} x,
$$

并利用上式计算积分  $\int_{0}^{\pi}\frac{x\sin x}{1+\cos^{2}x}\mathrm{d}x.$

8. 设 $f$ 在 $(0, +\infty)$ 上单调递增, 记

$$
F (x) = \frac {1}{x} \int_ {0} ^ {x} f (t)   \mathrm{d} t, \forall x > 0,
$$

证明: $F$ 在 $(0, +\infty)$ 上单调递增.

9. 设 f 是周期为 T 且在  $[0, T]$  上可积的函数, 证明:

$$
\lim _ {\lambda \to + \infty} \frac {1}{\lambda} \int_ {0} ^ {\lambda} f (x)   \mathrm{d} x = \frac {1}{T} \int_ {0} ^ {T} f (x)   \mathrm{d} x.
$$

10. 设 $f \in C^{2}[a, b]$, 证明:

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \frac {1}{2} \left(f (a) + f (b)\right) (b - a) + \frac {1}{2} \int_ {a} ^ {b} (x - a) (x - b) f ^ {\prime \prime} (x) \mathrm{d} x.
$$

11. 设 $f \in C[0,1]$, 证明:

$$
\lim _ {n \to + \infty} n \int_ {0} ^ {1} x ^ {n} f (x)   \mathrm{d} x = f (1).
$$

12. 设 $f \in R[0,1]$, 证明:

$$
\lim _ {n \to + \infty} \int_ {0} ^ {1} \sqrt [ n ]{x} f (x)   \mathrm{d} x = \int_ {0} ^ {1} f (x)   \mathrm{d} x.
$$

13. 证明:

$$
\int_ {0} ^ {1} \frac {\mathrm{d} x}{1 + x ^ {n}} = 1 - \frac {\ln 2}{n} + o \Big (\frac {1}{n} \Big) \quad (n \to + \infty).
$$

14. 设 $f \in C[-1, 1]$, 证明:

$$
\lim _ {h \to 0 ^ {+}} \int_ {- 1} ^ {1} \frac {h f (x)}{h ^ {2} + x ^ {2}}   \mathrm{d} x = \pi f (0).
$$

## 9.5 积分的进一步性质

Newton-Leibniz 公式虽然给出了计算积分的通用方法, 但由于不易获得原函数的解析表达式, 多数情况下只能对积分进行近似计算, 或利用积分中值定理对积分做粗略估计.

定理 9.5.1 (积分第一中值定理) 设 $f, g \in  R\left\lbrack  {a,b}\right\rbrack$ ,且 $g$ 不变号,则

$$
\int_ {a} ^ {b} f (x) g (x) \mathrm{d} x = \mu \int_ {a} ^ {b} g (x) \mathrm{d} x,
$$

其中 $\mu$ 介于 $f$ 的上下确界之间. 特别地, 当 $f$ 连续时, 存在 $\xi \in [a, b]$, 使得 $\mu = f(\xi)$.

证明 不失一般性, 可设 $g \geqslant 0$, 此时 $g$ 在 $[a, b]$ 上的积分大于或等于零. 分别记 $f$ 的上下确界为 $M, m$, 则 $mg \leqslant fg \leqslant Mg$. 由定理9.3.4可知

$$
m \int_ {a} ^ {b} g (x) \mathrm{d} x \leqslant \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x \leqslant M \int_ {a} ^ {b} g (x) \mathrm{d} x.
$$

上式说明, 若 $g$ 在 $[a, b]$ 上的积分为零, 则 $fg$ 在 $[a, b]$ 上的积分也为零, 此时欲证结论当然成立. 下设 $g$ 在 $[a, b]$ 上的积分大于零, 令

$$
\mu = \left(\int_ {a} ^ {b} g (x) \mathrm{d} x\right) ^ {- 1} \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x,
$$

则 $m \leqslant \mu \leqslant M$.

![](images/page_333_image_16.jpg)

注9.5.1 中值定理又称中值公式或平均值公式. 当 $g \equiv 1$ 时, 有

$$
\int_ {a} ^ {b} f (x) \mathrm{d} x = \mu (b - a),
$$

其中 $m \leqslant \mu \leqslant M$.

为了估计积分, 我们往往先用一些较为简单的函数去逼近被积函数.

命题 9.5.2 (阶梯逼近) 设 $f \in  R\left\lbrack  {a,b}\right\rbrack$ ,则存在两列阶梯函数 $\left\{  {\varphi }_{n}\right\}$ , $\left\{  {\psi }_{n}\right\}$ ,使得

$$
\varphi_ {n} \leqslant f \leqslant \psi_ {n}, \quad \int_ {a} ^ {b} \left(\psi_ {n} (x) - \varphi_ {n} (x)\right) \mathrm{d} x <   \frac {1}{n}, \tag {9.5.1}
$$

且每一个 $\varphi_{n},\psi_{n}$ 均介于 $f$ 的上下确界之间.此外，任给 $g\in R[a,b]$ ，均有

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} \varphi_ {n} (x) g (x) \mathrm{d} x = \lim _ {n \to + \infty} \int_ {a} ^ {b} \psi_ {n} (x) g (x) \mathrm{d} x = \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x. \tag {9.5.2}
$$

证明 由题设可知, 任给 $n \geqslant 1$, 存在 $[a, b]$ 的分割

$$
\mathrm{P}: a = x _ {0} <   x _ {1} <   x _ {2} <   \dots <   x _ {m} = b,
$$

使得 $\sum_{i=1}^{m}(M_i - m_i)\Delta x_i < \frac{1}{n}$, 其中 $M_i, m_i$ 分别是 $f$ 在 $[x_{i-1}, x_i]$ 上的上确界和下确界.

在 $[a, b]$ 中定义阶梯函数 $\varphi_n, \psi_n$ 如下: 当 $x \in [x_{i-1}, x_i)$ 时 $\varphi_n(x) = m_i, \psi_n(x) = M_i$; 规定 $\varphi_n(b) = m_m, \psi_n(b) = M_m$. 显然, $\varphi_n, \psi_n$ 均介于 $f$ 的上下确界之间, 且满足 (9.5.1) 式.

当  $g \in R[a, b]$  时, 可设  $|g| \leqslant M$ . 此时

$$
| \varphi_ {n} g - f g | \leqslant M (\psi_ {n} - \varphi_ {n}), \quad | \psi_ {n} g - f g | \leqslant M (\psi_ {n} - \varphi_ {n}),
$$

这说明 (9.5.2) 式成立.

我们也可以用连续函数去逼近可积函数. 定义在 $[a, b]$ 中的函数称为是分段线性的, 是指存在 $[a, b]$ 的一个分割, 使得该函数在每一个小区间中都是一次函数.

命题 9.5.3 (分段线性逼近) 设  $f \in R[a, b]$ ，则存在一列连续的分段线性函数  $\{f_{n}\}$ ，使得  $f_{n}(a) = f(a)$ ， $f_{n}(b) = f(b)$ ，每一个  $f_{n}$  均介于 f 的上下确界之间，且

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} | f _ {n} (x) - f (x) | \mathrm{d} x = 0, \tag {9.5.3}
$$

此外, 任给 $g \in R[a, b]$, 均有

$$
\lim _ {n \to + \infty} \int_ {a} ^ {b} f _ {n} (x) g (x) \mathrm{d} x = \int_ {a} ^ {b} f (x) g (x) \mathrm{d} x. \tag {9.5.4}
$$

证明 由题设, 任给 $n \geqslant 1$, 存在 $[a, b]$ 的分割 $\mathrm{P}: a = x_0 < x_1 < x_2 < \dots < x_m = b$, 使得

$$
\sum_ {i = 1} ^ {m} \omega_ {i} (f) \Delta x _ {i} <   \frac {1}{n}.
$$

在 $[a, b]$ 中定义分段线性函数 $f_n$, 使得

$$
f _ {n} (x) = \frac {x _ {i} - x}{\Delta x _ {i}} f (x _ {i - 1}) + \frac {x - x _ {i - 1}}{\Delta x _ {i}} f (x _ {i}), \forall x \in [ x _ {i - 1}, x _ {i} ], i = 1, 2, \dots , m.
$$

显然, $f_{n}$ 连续, 且 $f_{n}$ 在 $a, b$ 处的值与 $f$ 相同, 在其余地方的值介于 $f$ 的上下确界之间. 当 $x \in [x_{i-1}, x_{i}]$ 时, 还有

$$
\begin{array}{l} | f _ {n} (x) - f (x) | = | (x _ {i} - x) (f (x _ {i - 1}) - f (x)) + (x - x _ {i - 1}) (f (x _ {i}) - f (x)) | / \Delta x _ {i} \\ \leqslant ((x _ {i} - x) \omega_ {i} (f) + (x - x _ {i - 1}) \omega_ {i} (f)) / \Delta x _ {i} = \omega_ {i} (f). \\ \end{array}
$$

剩下的证明与上一命题类似, 略.

![](images/page_335_image_5.jpg)

下面我们来考虑几个应用.

例 9.5.1 设  $f \in R[a, b]$ ，证明:

$$
\int_ {a} ^ {b} | f (x) | \mathrm{d} x = \sup \biggl \{\int_ {a} ^ {b} f (x) \varphi (x) \mathrm{d} x \Big | \varphi \in R [ a, b ], | \varphi | \leqslant 1 \biggr \}. \tag {9.5.5}
$$

证明 (9.5.5) 式右端记为 $\alpha$, 由

$$
\int_ {a} ^ {b} f (x) \varphi (x) \mathrm{d} x \leqslant \int_ {a} ^ {b} | f (x) | \mathrm{d} x
$$

可知 $\alpha \leqslant \int_{a}^{b}|f(x)|\mathrm{d}x.$ 反之，任给 $\varepsilon >0$ ，存在阶梯函数 $g$ ，使得

$$
\int_ {a} ^ {b} | f (x) | \mathrm{d} x \leqslant \int_ {a} ^ {b} | g (x) | \mathrm{d} x + \int_ {a} ^ {b} | f (x) - g (x) | \mathrm{d} x <   \int_ {a} ^ {b} | g (x) | \mathrm{d} x + \varepsilon .
$$

由 g 为阶梯函数可知, 存在取值为  $\pm1$  的阶梯函数  $\varphi$ , 使得

$$
\int_ {a} ^ {b} g (x) \varphi (x) \mathrm{d} x = \int_ {a} ^ {b} | g (x) | \mathrm{d} x > \int_ {a} ^ {b} | f (x) | \mathrm{d} x - \varepsilon .
$$

此时有

$$
\begin{array}{l} \alpha \geqslant \int_ {a} ^ {b} f (x) \varphi (x)   \mathrm{d} x = \int_ {a} ^ {b} \left(f (x) - g (x)\right) \varphi (x)   \mathrm{d} x + \int_ {a} ^ {b} g (x) \varphi (x)   \mathrm{d} x \\ \geqslant - \int_ {a} ^ {b} | f (x) - g (x) | \mathrm{d} x + \int_ {a} ^ {b} | f (x) | \mathrm{d} x - \varepsilon \\ > \int_ {a} ^ {b} | f (x) | \mathrm{d} x - 2 \varepsilon , \\ \end{array}
$$

由  $\varepsilon$  的任意性即得欲证结论.

![](images/page_335_image_18.jpg)

例 9.5.2 (Riemann-Lebesgue 引理) 设  $f \in R[a, b]$ ，则

$$
\lim _ {\lambda \to + \infty} \int_ {a} ^ {b} f (x) \sin \lambda x   \mathrm{d} x = 0, \quad \lim _ {\lambda \to + \infty} \int_ {a} ^ {b} f (x) \cos \lambda x   \mathrm{d} x = 0. \tag {9.5.6}
$$