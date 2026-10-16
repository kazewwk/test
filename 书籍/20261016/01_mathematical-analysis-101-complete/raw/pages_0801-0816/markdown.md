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

这样, 将  $\sin\frac{(n+1)t}{2}$  用和角公式展开, 并注意到 (21.2.23) 式或直接利用

$$
\left| \frac {f (t)}{8 n \pi} \frac {\sin n t}{\sin^ {2} \frac {t}{2}} \right| \leqslant \frac {M | t |}{8 n \pi} \frac {\sqrt {n | t |}}{\frac {4 t ^ {2}}{\pi^ {2}}} = \frac {M \pi}{3 2 \sqrt {n | t |}}, \quad \forall t \in [ - \pi , \pi ],
$$

再结合 (21.2.22) 式可得

$$
A = \lim _ {n \to + \infty} \frac {1}{4 n \pi} \int_ {- \pi} ^ {\pi} f (t) \left(\frac {\sin^ {2} \frac {n t}{2}}{\sin^ {3} \frac {t}{2}} \cos \frac {t}{2} + \frac {\sin n t}{2 \sin^ {2} \frac {t}{2}}\right) \mathrm{d} t = 0.
$$

这就证明了定理.

![](images/page_805_image_7.jpg)

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

$$
\begin{array}{l} = \varlimsup_ {n \rightarrow + \infty} \sup _ {x \in [ - \pi , \pi ]} \frac {1}{\pi} \left| \int_ {0} ^ {\pi} (f (x + \theta) + f (x - \theta) - 2 f (x)) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{2 \sin \frac {\theta}{2}} \mathrm{d} \theta \right| \\ = \varlimsup_ {n \rightarrow + \infty} \sup _ {x \in [ - \pi , \pi ]} \frac {1}{\pi} \left| \int_ {0} ^ {\pi} (f (x + \theta) + f (x - \theta) - 2 f (x)) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{\theta} \mathrm{d} \theta \right| \\ = \varlimsup_ {n \to + \infty} \sup _ {x \in [ - \pi , \pi ]} \frac {1}{\pi} \left| \int_ {0} ^ {\delta} (f (x + \theta) + f (x - \theta) - 2 f (x)) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{\theta} \mathrm{d} \theta \right| \\ \leqslant \varlimsup_ {n \rightarrow + \infty} \sup _ {x \in [ - \pi , \pi ]} \sum_ {k = 1} ^ {2} \sum_ {\varepsilon \in \{- 1, 1 \}} \frac {1}{\pi} \left| \int_ {0} ^ {\delta} \left(f _ {k} (x + \varepsilon \theta) - f _ {k} (x)\right) \frac {\sin \left(n + \frac {1}{2}\right) \theta}{\theta} \mathrm{d} \theta \right| \\ \leqslant 8 M \omega (\delta). \\ \end{array}
$$

令 $\delta \to 0^{+}$ 即得结论.

![](images/page_809_image_4.jpg)

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

![](images/page_812_image_8.jpg)

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