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

注意到当 $f$ 缺乏光滑性的时候, 很难做到 (21.5.1) 式处处成立, 因此, 要使得问题更有意义, 对于这两个问题, 我们需要在更弱的条件下来讨论. 另一方面, 为了更好地看清楚问题, 我们来引入容易与前两个问题混淆的第三个问题: 若 $f \in \mathcal{R}_{\#}^{1}(\mathbb{R})$ 的 Fourier 级数 (除个别点外) 处处收敛到 $g$, 则 $g$ 是否本质上就是 $f$? 确切地讲, 是否就有 $\int_{0}^{2\pi}|g(x) - f(x)| \mathrm{d}x = 0$?

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

![](images/page_835_image_9.jpg)

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

证明 不妨设 $A = 0$ ，记 $S_{n} = \sum_{k = 1}^{n}c_{k}(n\geqslant 1)$ .则

$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} c _ {n} \left(\frac {\sin n h}{n h}\right) ^ {2} = \sum_ {n = 1} ^ {\infty} S _ {n} \left(\frac {\sin n h}{n h}\right) ^ {2} - \sum_ {n = 2} ^ {\infty} S _ {n - 1} \left(\frac {\sin n h}{n h}\right) ^ {2} \\ = \sum_ {n = 1} ^ {\infty} S _ {n} \left[ \left(\frac {\sin n h}{n h}\right) ^ {2} - \left(\frac {\sin (n + 1) h}{(n + 1) h}\right) ^ {2} \right]. \\ \end{array}
$$

于是对任何  $m \geqslant 1$ ,

$$
\begin{array}{l} \varlimsup_ {h \to 0} \left| \sum_ {n = 1} ^ {\infty} c _ {n} \left(\frac {\sin n h}{n h}\right) ^ {2} \right| \leqslant \varlimsup_ {h \to 0} \sum_ {n = m} ^ {\infty} | S _ {n} | \left| \left(\frac {\sin n h}{n h}\right) ^ {2} - \left(\frac {\sin (n + 1) h}{(n + 1) h}\right) ^ {2} \right| \\ \leqslant \sup _ {n \geqslant m} | S _ {n} | \int_ {0} ^ {+ \infty} \left| \frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {\sin t}{t}\right) ^ {2} \right| \mathrm{d} t. \\ \end{array}
$$

注意到  $\int_{0}^{+\infty}\left|\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\sin t}{t}\right)^{2}\right|$  dt 收敛, 在上式中令  $m\to+\infty$  即得 (21.5.14) 式.

![](images/page_836_image_7.jpg)

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

![](images/page_836_image_19.jpg)

引理21.5.7的证明也可以通过证明 $\frac{Mx^2}{2} -g(x)$ 和 $g(x) - \frac{mx^2}{2}$ 均为凸函数得到.

现在我们来证明定理 21.5.2.

定理 21.5.2 的证明 不妨设  $a_{0}=0$  。对 (21.5.1) 式形式上逐项积分两次，得到由 (21.5.7) 式定义的函数 F。

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

![](images/page_840_image_11.jpg)

## 习题 21.5

1. 试利用闭区间套定理证明引理 21.5.3.
2. 设函数 $f \in C[a, b]$，且在区间 $[a, b]$ 内的二阶广义导数 $f^{[n]}$ 非负。证明:$f$ 是凸函数。
3. 试构造一个可列闭集使得其二阶导集非空.

## 参考文献

[1] SAYEL A A. The mth ratio test: new convergence tests for series. The American Mathematical Monthly, 2008, 115(6): 514–524.
[2] 波利亚, 舍贵. 数学分析中的问题和定理: 第一卷. 张奠宙, 宋国栋, 等, 译. 上海: 上海科学技术出版社, 1981.
[3] 陈传章, 金福临, 朱学炎, 等. 数学分析: 上册. 2 版. 北京: 高等教育出版社, 1983.
[4] 陈传章, 金福临, 朱学炎, 等. 数学分析: 下册. 2 版. 北京: 高等教育出版社, 1983.
[5] 陈纪修, 於崇华, 金路. 数学分析: 上册. 3 版. 北京: 高等教育出版社, 2019.
[6] 陈纪修, 於崇华, 金路. 数学分析: 下册. 3 版. 北京: 高等教育出版社, 2019.
[7] 陈天权. 数学分析讲义: 第一册. 北京: 北京大学出版社, 2009.
[8] 陈天权. 数学分析讲义: 第二册. 北京: 北京大学出版社, 2010.
[9] 陈天权. 数学分析讲义: 第三册. 北京: 北京大学出版社, 2010.
[10] 程艺, 陈卿, 李平. 数学分析讲义: 第一册. 北京: 高等教育出版社, 2019.
[11] 程艺, 陈卿, 李平. 数学分析讲义: 第二册. 北京: 高等教育出版社, 2020.
[12] 程艺, 陈卿, 李平, 等. 数学分析讲义: 第三册. 北京: 高等教育出版社, 2020.
[13] 常庚哲, 史济怀. 数学分析教程: 上册. 3 版. 合肥: 中国科学技术大学出版社, 2012.
[14] 常庚哲, 史济怀. 数学分析教程: 下册. 3 版. 合肥: 中国科学技术大学出版社, 2013.
[15] 崔尚斌. 数学分析教程: 上册. 北京: 科学出版社, 2013.
[16] 崔尚斌. 数学分析教程: 中册. 北京: 科学出版社, 2013.
[17] 崔尚斌. 数学分析教程: 下册. 北京: 科学出版社, 2013.
[18] 布雷苏. 微积分溯源: 伟大思想的历程. 陈见柯, 林开亮, 叶卢庆, 译. 北京: 人民邮电出版社, 2022.
[19] 丁传松, 李秉彝, 布伦. 实分析导论. 北京: 科学出版社, 1998.
[20] DUNHAM W. 微积分的历程: 从牛顿到勒贝格. 李伯民, 汪军, 张怀勇, 译. 北京: 人民邮电出版社, 2010.
[21] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第一卷. 杨弢亮, 叶彦谦, 译. 北京: 高等教育出版社, 2006.
[22] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第二卷. 徐献瑜, 冷生明, 梁文骐, 译. 北京: 高等教育出版社, 2006.
[23] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第三卷. 路见可, 余家荣, 吴亲仁, 译. 北京: 高等教育出版社, 2006.
[24] 郝兆宽, 杨睿之, 杨跃. 数理逻辑证明及其限度. 上海: 复旦大学出版社, 2014.
[25] 华东师范大学数学系. 数学分析: 上册. 5 版. 北京: 高等教育出版社, 2019.
[26] 华东师范大学数学系. 数学分析: 下册. 5 版. 北京: 高等教育出版社, 2019.
[27] 邹中丹, 刘永平, 王昆扬. 简明数学分析. 2 版. 北京: 高等教育出版社, 2009.
[28] 黄玉民, 李成章. 数学分析. 2 版. 北京: 科学出版社, 2004.
[29] HUNT R A. On the convergence of Fourier series//Proceedings of the Conference on Orthogonal Expansions and Their Continuous Analogues. Carbondale: Southern Illinois University Press, 1968: 235–255.
[30] HUYNH E. A second Raabe's test and other series tests. The American Mathematical Monthly, 2022, 129(9): 865–875.
[31] 吉林大学数学系. 数学分析: 上册. 北京: 人民教育出版社, 1978.
[32] 吉林大学数学系. 数学分析: 中册. 北京: 人民教育出版社, 1978.
[33] 吉林大学数学系. 数学分析: 下册. 北京: 人民教育出版社, 1978.
[34] KOLMOGOROFF A N. Une série de Fourier-Lebesgue divergente presque partout. Fundamenta mathematicae, 1923(4): 324–328.
[35] KOLMOGOROFF A N. Une série de Fourier-Lebesgue divergente partout. Comptes Rendus de l'Académie des Sciences Paris, 1926, 183: 1327–1328.
[36] KÖRNER T W. Uniqueness for trigonometric series. Annals of Mathematics, 1987, 126(1): 1–34.
[37] 李逸. 基本分析讲义:第一卷 上册. 北京:高等教育出版社，2025.
[38] 李逸. 基本分析讲义:第一卷 下册. 北京:高等教育出版社，2025.
[39] 刘玉琏, 傅沛仁, 林玎, 等. 数学分析讲义: 上册. 5 版. 北京: 高等教育出版社, 2008.
[40] 刘玉琏, 傅沛仁, 林玎, 等. 数学分析讲义: 下册. 5 版. 北京: 高等教育出版社, 2008.
[41] 楼红卫. 数学分析——要点·难点·拓展. 北京: 高等教育出版社, 2020.
[42] 楼红卫. 微积分进阶. 北京: 科学出版社, 2009.
[43] 楼红卫. 数学分析: 上册. 北京: 高等教育出版社, 2022.
[44] 楼红卫. 数学分析: 下册. 北京: 高等教育出版社, 2023.
[45] 楼红卫. 数学分析技巧选讲. 北京: 高等教育出版社, 2022.
[46] 梅加强. 数学分析. 2 版. 北京: 高等教育出版社, 2020.
[47] 欧阳光中, 朱学炎, 秦曾复. 数学分析: 上册. 上海: 上海科学技术出版社, 1983.
[48] 欧阳光中, 朱学炎, 秦曾复. 数学分析: 下册. 上海: 上海科学技术出版社, 1982.
[49] 裴礼文. 数学分析中的典型问题与方法. 3 版. 北京: 高等教育出版社, 2021.
[50] PRUS-WIŚNIOWSKI F. A refinement of Raabe's test. The American Mathematical Monthly, 2008, 115(3): 249–252.
[51] 齐民友. 重温微积分. 北京: 高等教育出版社, 2004.
[52] RUDIN W. 数学分析原理（原书第3版）. 赵慈庚, 蒋铎, 译. 北京: 机械工业出版社, 2004.
[53] SCHRAMM M, TROUTMAN J, WATERMAN D. Segmentally alternating series. The American Mathematical Monthly, 2014, 121(8): 717–722.
[54] 佘志坤. 全国大学生数学竞赛参赛指南. 北京: 科学出版社, 2022.
[55] 余志坤. 全国大学生数学竞赛解析教程（数学专业类）——数学分析:上册. 北京:科学出版社，2024.
[56] STUART C. An inequality involving  $\sin(n)$ . The American Mathematical Monthly, 2018, 125(2): 173–174.
[57] 陶哲轩. 陶哲轩实分析. 王昆扬, 译. 北京: 人民邮电出版社, 2008.
[58] TRENCH W F. Introduction to Real Analysis. Upper Saddle River: Prentice Hall, 2003.
[59] 王昆扬. 数学分析简明教材. 北京: 高等教育出版社, 2015.
[60] WATSON G N. A Treatise on the Theory of Bessel Functions. 2nd ed. Cambridge: Cambridge University Press, 1944.
[61] 伍胜健. 数学分析: 第一册. 北京: 北京大学出版社, 2009.
[62] 伍胜健. 数学分析: 第二册. 北京: 北京大学出版社, 2010.
[63] 伍胜健. 数学分析: 第三册. 北京: 北京大学出版社, 2010.
[64] 小平邦彦. 微积分入门 I: 一元微积分. 裴东河, 译. 北京: 人民邮电出版社, 2008.
[65] 小平邦彦. 微积分入门 II: 多元微积分. 裴东河, 译. 北京: 人民邮电出版社, 2008.
[66] 肖文灿. 集合论初步. 2 版. 北京: 商务印书馆, 1950.
[67] 谢惠民, 恽自求, 易法槐, 等. 数学分析习题课讲义: 上册. 2 版. 北京: 高等教育出版社, 2018.
[68] 谢惠民, 恽自求, 易法槐, 等. 数学分析习题课讲义: 下册. 2 版. 北京: 高等教育出版社, 2019.
[69] 辛钦. 数学分析八讲. 王会林, 齐民友, 译. 北京: 人民邮电出版社, 2010.
[70] 叶怀安. 连续函数列的极限函数的一个性质及其应用. 湖南数学年刊, 1985, 5(2): 87-88.
[71] 张福保, 薛星美. 数学分析 (全三册). 北京: 科学出版社, 2022.
[72] 张锦文. 公理集合论导引. 北京: 科学出版社, 1991.
[73] 张筑生. 数学分析新讲:第一册. 北京:北京大学出版社，1990.
[74] 张筑生. 数学分析新讲:第二册. 北京:北京大学出版社，1990.
[75] 张筑生. 数学分析新讲:第三册. 北京:北京大学出版社，1991.
[76] 周民强. 实变函数论. 3 版. 北京: 北京大学出版社, 2016.
[77] 周民强. 数学分析习题演练: 第一册. 北京: 科学出版社, 2006.
[78] 周民强. 数学分析习题演练: 第二册. 北京: 科学出版社, 2006.
[79] 卓里奇. 数学分析 (第 4 版): 第一卷. 蒋铎, 王昆扬, 周美珂, 等, 译. 北京: 高等教育出版社, 2006.
[80] 卓里奇. 数学分析 (第 4 版): 第二卷. 蒋铎, 钱佩玲, 周美珂, 等, 译. 北京: 高等教育出版社, 2006.
[81] ZYGMUND A. Trigonometric Series. 3rd. ed. Cambridge: Cambridge University Press, 2002.

## 常用符号

| N | 自然数集 |
| --- | --- |
| $\mathbb{Z},\mathbb{Z}_{+}$ | 整数集,正整数集 |
| $\mathbb{Q},\mathbb{Q}_{+}$ | 有理数域,正有理数集 |
| $\mathbb{R},\mathbb{R}_{+}$ | 实数域,正实数集 |
| $\mathbb{R}^{n}$ | n维欧氏空间 |
| C | 复数域 |
| $\mathbb{C}^{n}$ | n维复空间 |
| $S^{n-1}$ | $\mathbb{R}^{n}$中单位球面,即$\{x\in\mathbb{R}^{n}\mid\\\|x\\\|=1\}$ |
| $\mathbb{S}^{n}$ | n阶实对称矩阵全体 |
| $B_{r}(x)$ | 半径为r,中心在$x\in\mathbb{R}^{n}$的开球 |
| $\overset{\circ}{B}_{r}(x)$ | 半径为r,中心在$x\in\mathbb{R}^{n}$的去心开球 |
| $I_{r}(x)$ | 边长为2r,中心在$x\in\mathbb{R}^{n}$且各边平行于坐标轴的闭方体 |
| $A^{\mathrm{T}},x^{\mathrm{T}}$ | 矩阵A,向量x的转置 |
| $x\cdot y$ | $\mathbb{R}^{n}$中向量x与y的内积,也常用$\langle x,y\rangle,x^{\mathrm{T}}y$表示 |
| $\langle x,y\rangle$ | 内积空间中两个元素x,y的内积 |
| $\\\|x\\\|_{p}$ | $\mathbb{R}^{n}$中向量$x=(x_{1},x_{2},\cdots,x_{n})^{\mathrm{T}}$的p-范数$\left(\sum_{k=1}^{n}\|x_{k}\|^{p}\right)^{\frac{1}{p}}$ |
| $\\\|A\\\|_{p}$ | 方阵$A\in\mathbb{R}^{n\times n}$的诱导范数$\\\|A\\\|_{p}:=\max_{\\\|x\\\|_{p}=1}\\\|Ax\\\|_{p}$ |
| $\\\|x\\\|$ | $\mathbb{R}^{n}$中向量x通常的范数,即$\\\|x\\\|_{2}$ |
| $\\\|A\\\|$ | 方阵$A\in\mathbb{R}^{n\times n}$通常的诱导范数$\\\|A\\\|_{2}$ |
| $\nu(E)$ | $\mathbb{R}^{n}$中Jordan可测集E的Jordan测度(容积)——长度、面积、体积 |
| $a^{+},a^{-}$ | 实数a的正部$(\|a\|+a)/2$与负部$(\|a\|-a)/2$ |
| $a\lor b,a\land b$ | 实数a,b的最大值和最小值 |
| Re z,Im z | 复数z=a+bi的实部a和虚部b,其中a,b为实数 |
| $\chi_{E}$ | 集合E的特征函数,即在E上取值为1,在其余点上取值为0的函数 |

| ∃ | 存在 |
| --- | --- |
| ∀ | 对于所有 |
| ≫,≪ | 大大大于, 大大小于 |
| a.e. | 几乎处处 |
| s.t. | 使得 |
| ∅ | 空集 |
| ∈,∃ | a∈E和E⇒a均表示a是E的元素 |
| ⊆,⊃ | E⊆F和F⊇E均表示集合E包含于集合F,即F包含E |
| ⊂,⊃ | E⊂F和F⊃E均表示集合E真包含于集合F,即F真包含E |
| ⊂⊂ | 集合的紧包含关系,E⊂⊂F当且仅当$\overline{E}$是F的紧子集 |
| E{φ∈F} | 表示集合{x∈E\|φ(x)∈F}.在E明确的情况下,简记为{φ∈F} |
| f(D) | 当f是映射,D是集合时,表示D的像集{f(x)\|x∈D} |
| ∩ | 集合的交,A∩B表示同时属于A和B的所有元素组成的集合 |
| ∪ | 集合的并,A∪B表示属于A或属于B的所有元素组成的集合 |
| \\ | 集合的差,A\\B表示属于A而不属于B的所有元素组成的集合 |
| C | 集合的补,C E表示在全集X明确的情况下,E的补集X\\E |
| E° | 集合E的内部,即E的内点的全体 |
| E' | 集合E的导集,即E的极限点(聚点)的全体 |
| $\overline{E}$ | 集合E的闭包 |
| ∂E | 集合E的边界 |
| αE+βF | 线性空间中集合的伸缩、代数和与代数差等,表示集合{αx+βy\|x∈E,y∈F} |
| ∑,Π[x],{x} | 连加号,连乘号 |
| $\overline{\lim},\underline{\lim}$ | 实数x的整数部分(即不大于x的最大整数)与小数部分(即x-[x]) |
| ∫,∫ | 上极限,下极限 |
| R(I) | 上积分符号,下积分符号 |
| $\mathcal{R}^{p}(I)$ | 区间I上的Riemann可积函数全体 |
| $C_{n}^{k}$ | 区间I上正部与负部均p次(广义)可积的函数全体 |
| $C^{\omega}(I)$ | 在n个不同的元素中选取k个的组合数 |
| $C^{k}(\Omega)$ | 在Ω上有k阶连续(偏)导数的函数全体 |
| $C_{c}^{k}(\Omega)$ | 在Ω上有紧支集且有k阶连续(偏)导数的函数全体 |
| $C^{k,\alpha}(\Omega)$ | 在Ω上k阶(偏)导数满足α次Hölder条件的函数全体 |
| S | 速降函数全体 |
| $\widehat{f},\widehat{f}$ | 函数f的Fourier变换,Fourier逆变换 |
| f*g | 函数f和g的卷积 |
| $\ell_{\infty}$ | 有界实数数列的全体 |
| $\ell_{p}$ | 1≤p&lt;+∞,p次可求和序列的全体 |

## 索引

| Abel 判别法 | 120 | Fourier 级数 | 150 |
| --- | --- | --- | --- |
| Arzelà 有界收敛定理 | 113 | Fourier 系数 | 150 |
|  |  | Fresnel 积分 | 132 |
| Bessel 不等式 | 175 |  |  |
| Beta 函数 | 135 | Gamma 函数 | 135 |
| Bohr-Mollerup 定理 | 138 | Gauss 叠乘定理 | 138 |
|  |  | Gauss 公式 | 74 |
| $C^k$ 边界 | 68 | Gibbs 现象 | 170 |
| Carleson 定理 | 162 | Green 公式 | 72 |
| Cauchy 准则 | 119 |  |  |
|  |  | Hölder 不等式 | 151 |
| Darboux 上和 | 3 | Hardy 不等式 | 135 |
| Darboux 下和 | 3 | Hausdorff-Young 不等式 | 188 |
| de Rham 上同调群 | 89 |  |  |
| Dini-Lipschitz 判别法 | 158 | Jordan 测度 | 8 |
| Dirichlet 核 | 157 | Jordan 可测集 | 8 |
| Dirichlet 积分 | 156 | Legendre 公式 | 138 |
| Dirichlet 判别法 | 120 | log-凸 | 136 |
| Dirichlet 引理 | 159 | Luzin 猜想 | 162 |
| Dirichlet-Jordan 判别法 | 159 |  |  |
|  |  | Minkowski 不等式 | 152 |
| Euler 公式 | 138 |  |  |
| Euler 积分 | 135 | Parseval 等式 | 176 |
|  |  | Plancherel 定理 | 188 |
| Fejér 核 | 160 | q-形式 | 82 |
| Fejér 积分 | 160 |  |  |
| Fourier 变换 | 184 | Riemann 和 | 3 |