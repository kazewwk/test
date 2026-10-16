其中  $V(\theta) = \mathrm{Var}[\tilde{S}(\boldsymbol{X};\theta)]$ ,  $\boldsymbol{\Delta} = (g^{1}(\theta), g^{2}(\theta), \cdots, g^{k}(\theta))^{\mathrm{T}}$ , 而  $S^{i}(\boldsymbol{X}, \theta) = \frac{\partial^{i}S(\boldsymbol{X};\theta)}{\partial\theta^{i}}$ ,  $g^{i}(\theta) = \frac{\partial^{i}g(\theta)}{\partial\theta^{i}}$ .

在统计中, (2.1.18) 式右边的值被称为无偏估计 $T(\mathbf{X})$ 的方差的 Bhattacharya 下界. 显然, 当 $k = 1$ 时, 此下界就是 C-R 下界.

## 2.1.4 相合估计

前两小节的准则主要侧重于样本容量给定, 而本节讲述的准则侧重于样本容量趋于无穷: 相合估计 (consistent estimate) 和相合渐近正态估计 (consistent asymptotically normal estimate, 简记为 CAN 估计).

定义 2.1.7 设统计量  $T_{n}(X)$  是参数  $g(\theta)$  的估计量.

(1) 如果当 $n \to \infty$ 时, $T_{n}(X)$ 依概率收敛于 $g(\theta)$, 即 $\forall \theta \in \Theta$ 及 $\varepsilon > 0$, 有

$$
\lim _ {n \to \infty} P (| T _ {n} (X) - g (\theta) | \geqslant \varepsilon) = 0,
$$

则称 $T_{n}(X)$ 是 $g(\theta)$ 的（弱）相合估计.

(2) 如果当 $n \to \infty$ 时, $T_{n}(X)$ 以概率1收敛于 $g(\theta)$, 即 $\forall \theta \in \Theta$, 有

$$
P \left(\lim _ {n \to \infty} T _ {n} (X) = g (\theta)\right) = 1,
$$

则称  $T_{n}(X)$  是  $g(\theta)$  的强相合估计.

(3) 如果当 $n \to \infty$ 时, $T_{n}(X)$ 依 $r$ 阶矩收敛于 $g(\theta)$, 即 $\forall \theta \in \Theta$, 有

$$
\lim _ {n \to \infty} E _ {\theta} | T _ {n} (X) - g (\theta) | ^ {r} = 0,
$$

则称 $T_{n}(X)$ 是 $g(\theta)$ 的 $r$ 阶矩相合估计. 当 $r = 2$ 时, 称为均方相合估计.

由概率论知识知道, 强相合  $\Rightarrow$  弱相合, r 阶矩相合  $\Rightarrow$  弱相合, 反之不成立, 且强相合与 r 阶矩相合之间没有包含关系.

注 2.1.5 关于相合估计,有如下两个有用结论:

- 如果 $T_{n}$ 是 $g(\theta)$ 的相合估计，$\{c_{n}\}, \{d_{n}\}$ 是两个常数列，且 $\lim_{n} c_{n} = 0, \lim_{n} d_{n} = 1$，则 $d_{n} T_{n} + c_{n}$ 也是 $g(\theta)$ 的相合估计.
- 如果 $T_{n}$ 是 $\theta$ 的(强)相合估计, $g(x)$ 连续, 则 $g(T_{n})$ 也是 $g(\theta)$ 的(强)相合估计.

注 2.1.6 关于相合估计的存在性问题, 陈希孺 (2009) 之 4.1.3 小节对此进行了较详细讨论, 由于这是纯理论研究, 而实际应用很少考虑, 故请有兴趣的读者参阅.

定义 2.1.8 设  $T_{n}$  是参数  $g(\theta)$  的相合估计, 如存在与样本容量 n 有关的定义于参数空间  $\Theta$  上的函数  $\mu_{n}(\theta), \sigma_{n}(\theta)$ , 且  $\sigma_{n}(\theta) > 0$ , 使得当  $n \to \infty$  时有

$$
\frac {T _ {n} - \mu_ {n} (\theta)}{\sigma_ {n} (\theta)} \xrightarrow {\mathrm{d}} N (0, 1), \tag {2.1.19}
$$

则称  $T_{n}$  为  $g(\theta)$  的 CAN 估计, 也称  $T_{n}$  渐近正态  $N(\mu_{n}, \sigma_{n}^{2})$ , 记为  $T_{n} \sim AN(\mu_{n}, \sigma_{n}^{2})$ .

从上述定义可以看出, $\sigma_{n}^{2}$  并不唯一,且也不是估计量 $T_{n}$  的方差.这一点可以由下面的结论得到:

\- 如果 $T_{n} \sim AN(\mu_{n}, \sigma_{n}^{2})$，则 $T_{n} \sim AN(\mu_{n}^{\prime}, \sigma_{n}^{\prime 2})$ 的充要条件是

$$
\lim _ {n \to \infty} \frac {\sigma_ {n} ^ {\prime}}{\sigma_ {n}} = 1, \lim _ {n \to \infty} \frac {\mu_ {n} ^ {\prime} - \mu_ {n}}{\sigma_ {n}} = 0.
$$

\- 如果 $T_{n} \sim AN(\mu_{n}, \sigma_{n}^{2})$，则 $a_{n}T_{n} + b_{n} \sim AN(\mu_{n}, \sigma_{n}^{2})$ 的充要条件是

$$
\lim _ {n \to \infty} a _ {n} = 1, \lim _ {n \to \infty} \frac {\mu_ {n} (a _ {n} - 1) + b _ {n}}{\sigma_ {n}} = 0.
$$

对于第一章中定义的经验分布函数, 第六章将证明当样本独立同分布时, 经验分布是总体分布的相合估计, 也是其相合渐近正态估计.

定义 2.1.9 (总体 p 分位数) 设总体 X 的累积分布函数为  $F(x)$ ，对于给定的  $p \in (0,1)$ ，称

$$
\xi_ {p} = \inf \{x: F (x) \geqslant p \} \tag {2.1.20}
$$

为该总体 p 分位数. 特别地,  $\xi_{0.5}$  称为该总体的中位数.

虽然 (1.2.7) 式定义的样本 p 分位数, 和注 1.2.2 中所给出的

$$
\hat {\xi} _ {p} = F _ {n} ^ {- 1} (p) = \inf \{x: F _ {n} (x) \geqslant p \} \tag {2.1.21}
$$

有所不同, 但它们都介于 $X_{([np])}$ 与 $X_{([np]+1)}$ 之间. 从 (2.1.20) 可以看出, $\xi_p$ 是一个左连续函数. 另外, 由 (2.1.21) 式知道, 当 $F$ 连续时, 有

$$
F _ {n} ^ {- 1} (t) = X _ {(i)}, \text {如} (i - 1) / n <   t \leqslant i / n,
$$

即

$$
F _ {n} ^ {- 1} (t) = X _ {(\lceil n t \rceil)}, \quad 0 <   t <   1,
$$

其中 $[x]$ 表示不小于 $x$ 的最小整数. 于是, 我们可以通过研究 $X_{(m)}$ 的相合渐近正态性, 而知道样本分位数的相关性质, 其中 $m / n = p + o_p(n^{-1/2})$. 为此, 需要下面引理.

引理 2.1.1 对于两个随机变量列  $\{T_{n}\},\{V_{n}\}$ ，假设  $T_{n}=O_{p}(1)$ ，且对于任意的  $\varepsilon>0$  及常数 c，有

$$
P (V _ {n} \leqslant c, T _ {n} \geqslant c + \varepsilon) \rightarrow 0, \quad P (V _ {n} \geqslant c + \varepsilon , T _ {n} \leqslant c) \rightarrow 0,
$$

则

$$
V _ {n} - T _ {n} \xrightarrow {\mathrm{p}} 0.
$$

证明 由于 $T_{n} = O_{p}(1)$，故任给 $\varepsilon > 0, \delta > 0$，存在自然数 $m$（与 $\varepsilon, \delta$ 有关），使

$$
P (| T _ {n} | \geqslant m \varepsilon) <   \delta , \forall n.
$$

于是

$$
\begin{array}{l} P (| T _ {n} - V _ {n} | > 2 \varepsilon) \\ <   \delta + P (| T _ {n} | <   m \varepsilon , | T _ {n} - V _ {n} | > 2 \varepsilon) \\ <   \delta + \sum_ {i = - m + 1} ^ {m} P ((i - 1) \varepsilon \leqslant T _ {n} \leqslant i \varepsilon , | T _ {n} - V _ {n} | > 2 \varepsilon) \\ \leqslant \delta + \sum_ {i = - m + 1} ^ {m} P (T _ {n} \leqslant i \varepsilon , V _ {n} \geqslant i \varepsilon + \varepsilon) + \sum_ {i = - m + 1} ^ {m} P (T _ {n} \geqslant (i - 1) \varepsilon , V _ {n} \leqslant (i - 1) \varepsilon - \varepsilon), \\ \end{array}
$$

由条件可知, 结论成立.

定理 2.1.8 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本，以  $X_{n1} \leqslant X_{n2} \leqslant \cdots \leqslant X_{nn}$  表示其次序统计量，以  $f(x)$  记总体概率密度， $\xi_{p}$  记总体 p 分位数。如果  $f(\xi_{p}) > 0$ ,  $f(x)$  在  $\xi_{p}$  点连续，且  $\frac{m}{n} = p + o_{p}(n^{-1/2})$ ，则

$$
X _ {n m} - \xi_ {p} = - \frac {F _ {n} (\xi_ {p}) - p}{f (\xi_ {p})} + R _ {n}, \tag {2.1.22}
$$

其中  $R_{n}=o_{p}(n^{-1/2})$ .

证明 记 $V_{n} = \sqrt{n}(X_{nm} - \xi_{p}), T_{n} = \sqrt{n}[p - F_{n}(\xi_{p})] / f(\xi_{p})$. 则所证结论转化为证明: $V_{n} - T_{n} \xrightarrow{\mathrm{P}} 0$. 由此, 为证明本定理, 仅需验证引理2.1.1中的两个条件即可.

因为

$$
n F _ {n} (\xi_ {p}) \sim B (n, p), \tag {*1}
$$

故 $E(T_{n}^{2}) = \frac{p(1 - p)}{f^{2}(\xi_{p})}$ 与 $n$ 无关. 由 Chebyshev 不等式可得 $T_{n} = O_{p}(1)$.

下证引理的第二个条件. 对于任意的 $\varepsilon > 0$ 及常数 $c$, 令

$$
Z _ {n} = \sqrt {n} [ F (\xi_ {p} + c n ^ {- 1 / 2}) - F _ {n} (\xi_ {p} + c n ^ {- 1 / 2}) ] / f (\xi_ {p}),
$$

$$
U _ {n} = n [ F _ {n} (\xi_ {p} + c n ^ {- 1 / 2}) - F _ {n} (\xi_ {p}) ].
$$

由 $(*)1)$ 式知,

$$
\sqrt {n} (T _ {n} - Z _ {n}) = \frac {U _ {n} - E (U _ {n})}{f (\xi_ {p})},
$$

则

$$
E (T _ {n} - Z _ {n}) ^ {2} = \frac {E [ U _ {n} - E (U _ {n}) ] ^ {2}}{n f ^ {2} (\xi_ {p})}.
$$

如记 $p_n^* = F(\xi_p + cn^{-1/2}) - p,$ 则由 $(\ast 1)$ 式知， $U_{n}\sim B(n,p_{n}^{*})$ 故

$$
E [ U _ {n} - E (U _ {n}) ] ^ {2} = \mathrm{Var} (U _ {n}) = n p _ {n} ^ {*} (1 - p _ {n} ^ {*}).
$$

于是，

$$
E (T _ {n} - Z _ {n}) ^ {2} = \frac {p _ {n} ^ {*} (1 - p _ {n} ^ {*})}{f ^ {2} (\xi_ {p})}.
$$

由于 F 在  $\xi_{p}$  处连续, 故知  $p_{n}^{*} \rightarrow 0$ . 于是, 当  $n \longrightarrow \infty$  时,

$$
T _ {n} - Z _ {n} \xrightarrow {\mathrm{p}} 0. \tag {*2}
$$

我们注意到，

$$
c _ {n} \stackrel {\text {记}} {=} \frac {1}{f \left(\xi_ {p}\right)} \left\{\sqrt {n} \left[ F \left(\xi_ {p} + c n ^ {- 1 / 2}\right) - \frac {m}{n} \right]\right\}\rightarrow c. \tag {*3}
$$

故由 $F_{n}$ 的单调性, 以及 $F_{n}(X_{nm}) \geqslant \frac{m}{n}$, 有

$$
\begin{array}{l} \{V _ {n} \leqslant c \} = \{X _ {n m} \leqslant \xi_ {p} + c n ^ {- 1 / 2} \} \\ \subset \{n F _ {n} (X _ {n m}) \leqslant n F _ {n} (\xi_ {p} + c n ^ {- 1 / 2}) \} \\ \subset \{m \leqslant n F _ {n} (\xi_ {p} + c n ^ {- 1 / 2}) \} \\ = \{Z _ {n} \leqslant c _ {n} \}. \\ \end{array}
$$

因此，

$$
\begin{array}{l} P (V _ {n} \leqslant c, T _ {n} \geqslant c + \varepsilon) \leqslant P (Z _ {n} \leqslant c _ {n}, T _ {n} \geqslant c + \varepsilon) \\ \leqslant P (| T _ {n} - Z _ {n} | \geqslant \varepsilon - | c _ {n} - c |). \\ \end{array}
$$

结合 $(*1), (*2)$ 及 $(*3)$ 式, 则可证

$$
P (V _ {n} \leqslant c, T _ {n} \geqslant c + \varepsilon) \rightarrow 0.
$$

类似证明另一半.

注2.1.7 (2.1.22)式是Bahadur(1960)提出的,故被称为样本分位数的Bahadur表示.实际上,他还证明了,当 $\xi_{p}$ 唯一时,(2.1.22)式中的尾项 $R_{n}$ 满足如下更强的结果:

$$
R _ {n} \stackrel {\text {a.s.}} {=} O (n ^ {- 3 / 4} (\ln \ln n) ^ {1 / 4}).
$$

定理2.1.9 在定理2.1.8的条件下，当 $n\to \infty$ 时，

$$
\sqrt {n} (X _ {n m} - \xi_ {p}) \xrightarrow {\mathrm{d}} N \left(0, \frac {p (1 - p)}{f ^ {2} (\xi_ {p})}\right). \tag {2.1.23}
$$

证明 由 (2.1.22) 式知: $\forall x \in \mathbb{R}$,

$$
\begin{array}{l} P (\sqrt {n} (X _ {n m} - \xi_ {p}) \leqslant x) \\ = P \left(- \frac {\sum_ {i = 1} ^ {n} [ I _ {(- \infty , \xi_ {p} ]} (X _ {i}) - p ]}{\sqrt {n} f (\xi_ {p})} + o _ {p} (1) \leqslant x\right) \\ = P \left(\frac {\sum_ {i = 1} ^ {n} \left[ I _ {(- \infty , \xi_ {p} ]} (X _ {i}) - p \right]}{\sqrt {n p (1 - p)}} \geqslant - \frac {x f (\xi_ {p})}{\sqrt {p (1 - p)}} + o _ {p} (1)\right). \\ \end{array}
$$

又由于样本独立同分布, 故知  $I_{(-\infty,\xi_{p}]}(X_{i})$  独立同分布于  $B(1,p)$ , 于是, 由中心极限定理可知

$$
P (\sqrt {n} (X _ {n m} - \xi_ {p}) \leqslant x) \longrightarrow 1 - \Phi \left(- \frac {x f (\xi_ {p})}{\sqrt {p (1 - p)}}\right) = \Phi \left(\frac {x f (\xi_ {p})}{\sqrt {p (1 - p)}}\right),
$$

结论得证.

由于相合渐近正态估计不唯一, 故一个自然问题就是: 一个参数是否有 “最优” 的相合渐近正态估计? 为此引入下面的准则:

定义 2.1.10 如果参数  $\theta$  的估计量  $T_{n}$  满足

$$
\sqrt {n} (T _ {n} - \theta) \xrightarrow {\mathrm{d}} N (0, I ^ {- 1} (\theta)), \tag {2.1.24}
$$

则称之为最优渐近正态估计 (best asymptotic normal estimate, 简记为 BANE), 其中  $I(\theta)$  为 Fisher 信息量.

我们注意到, 在上述定义中, 暗含  $I^{-1}(\theta)$  为无偏估计的方差下界, 但由于这仅是渐近方差 (定义见下一小节), 故上述定义仅表示渐近最优性.

例 2.1.11 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $N(\theta, 1)$  的独立同分布样本, 考虑  $\theta$  的如下估计:

$$
T _ {n} = \left\{ \begin{array}{c l} \bar {X} _ {n} / 2, & | \bar {X} _ {n} | <   n ^ {- 1 / 2}, \\ \bar {X} _ {n}, & | \bar {X} _ {n} | \geqslant n ^ {- 1 / 2} \end{array} \right.
$$

的相合渐近正态性.

解 可由附录中的 Delta 方法证明:

$$
\sqrt {n} (T _ {n} - \theta) \xrightarrow {\mathrm{d}} \left\{ \begin{array}{l l} N (0, 1), & \theta \neq 0, \\ N (0, 1 / 4), & \theta = 0. \end{array} \right.
$$

而总体 Fisher 信息量  $I(\theta)=1$ .

上例说明, 上例中的估计量  $T_{n}$  在某点突破了  $I^{-1}(\theta)$  这个下界. 统计中称这种情况为 “超有效性”. 但经过研究发现, 这种超有效性仅在很少几个  $\theta$  值上发生. 如果要求 (2.1.24) 式对所有  $\theta \in \Theta$  一致成立, 则这种情况就不会发生, 即要求

$$
\sup _ {\theta \in \Theta} \sup _ {x \in \mathbb {R}} | F _ {T _ {n}} (x; \theta) - \varPhi (x) | \to 0,
$$

其中 $F_{T_n}(x;\theta)$ 为 $\sqrt{n} (T_n - \theta) / \sqrt{I(\theta)}$ 的累积分布函数， $\varPhi (x)$ 为标准正态的累积分布函数.

## 2.1.5 渐近相对效率

上述的评价准则都是由估计自身性质引出的, 由于多数情况下某个参数的估计并不唯一, 那如何比较两个估计间的优劣呢? 为此, 本小节将引进渐近相对效率这一比较准则, 同时简单介绍在统计文献中经常遇到的渐近偏差、渐近方差, 以及渐近均方误差等概念.

定义 2.1.11(渐近偏差、渐近方差、渐近均方误差) 设统计量  $T_{n}(X)$  为基于 n 个样本关于参数  $\theta$  的一个估计。如果存在常数列  $a_{n} \rightarrow a > 0$  (a 可以是  $\infty$ )，以及满足  $E(|Y|) < \infty$  的 Y，使得  $a_{n}[T_{n}(X) - \theta] \xrightarrow{\mathrm{d}} Y$ ，则称  $E(Y)/a_{n}$  为  $T_{n}$  的渐近偏差；如果  $E(Y^{2}) < \infty$ ，则称  $E(Y^{2})/a_{n}^{2}$  为  $T_{n}$  的渐近均方误差， $\operatorname{Var}(Y)/a_{n}^{2}$  为  $T_{n}$  的渐近方差。

有了上述渐近均方误差的定义, 就可以利用渐近均方误差的大小来比较两个估计的好坏, 为此引入渐近相对效率 (asymptotic relative efficiency, 简记为 ARE) 的定义.

定义 2.1.12 (渐近相对效率) 设  $T_{n}, T_{n}^{\prime}$  为参数  $\theta$  的两个估计, 记二者的渐近均方误差为  $AMSE_{T_{n}}, AMSE_{T_{n}^{\prime}}$ , 则称

$$
\mathrm{ARE} (T _ {n} ^ {\prime}, T _ {n}) = \frac {\mathrm{AMSE} _ {T _ {n}}}{\mathrm{AMSE} _ {T _ {n} ^ {\prime}}} \tag {2.1.25}
$$

为 $T_{n}^{\prime}$ 相对于 $T_{n}$ 的渐近相对效率. 如果 $\limsup_{n}\mathrm{ARE}(T_n', T_n) \leqslant 1$, 且对某些参数值不等号成立, 则称 $T_{n}$ 比 $T_{n}^{\prime}$ 渐近有效.

例 2.1.12 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自 Poisson 分布  $P(\theta)$  的独立同分布样本, 参数  $\theta > 0$ . 对于待估参数  $g(\theta) = \mathrm{e}^{-\theta}$ , 求两个估计  $T_{1n} = F_{n}(0), T_{2n} = \mathrm{e}^{-\bar{X}}$  间的渐近相对效率.

解 由于 $g(\theta) = P(X_1 = 0)$, 故知 $T_{1n}$ 是 $g(\theta)$ 的无偏估计, 且由中心极限定理知

$$
\frac {\sqrt {n} [ T _ {1 n} - g (\theta) ]}{\sqrt {g (\theta) [ 1 - g (\theta) ]}} \xrightarrow {\mathrm{d}} N (0, 1),
$$

故知 $T_{1n}$ 的渐近均方误差 $\mathrm{AMSE}_{T_{1n}} = g(\theta)[1 - g(\theta)] / n.$

对于 $T_{2n}$ ，由于 $n\bar{X}\sim P(n\theta)$ ，故由中心极限定理知

$$
\frac {\sqrt {n} (\bar {X} - \theta)}{\sqrt {\theta}} \xrightarrow {\mathrm{d}} N (0, 1).
$$

于是, 由 Delta 方法可知

$$
\sqrt {n} [ T _ {2 n} - g (\theta) ] \stackrel {\mathrm{d}} {\longrightarrow} N (0, \mathrm{e} ^ {- 2 \theta} \theta).
$$

由此知  $T_{2n}$  的渐近均方误差  $AMSE_{T_{2n}} = e^{-2\theta}\theta/n$ .

于是, $T_{1n}$ 相对于 $T_{2n}$ 的渐近相对效率为 $\mathrm{ARE}(T_{1n}, T_{2n}) = \theta / (\mathrm{e}^{\theta} - 1) < 1$, 这说明 $T_{2n}$ 比 $T_{1n}$ 更渐近有效.

## 2.2 矩估计

矩估计是K.Pearson于1894年基于某些生物学方面的数据并非来自正态这一发现而提出的.

设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本, 且总体 k 阶矩存在, 记参数  $\theta \in \Theta \subset R^{k}$ , 总体 X 的 r 阶原点矩与中心矩分别为

$$
\mu_ {r} (\boldsymbol {\theta}) = E (X ^ {r}), \nu_ {r} (\boldsymbol {\theta}) = E [ (X - \mu_ {1}) ^ {r} ], \tag {2.2.1}
$$

其中 r 为正整数.

第一章给出了样本 r 阶原点矩与中心矩如下:

$$
a _ {r} = \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {r}, \quad m _ {r} = \frac {1}{n} \sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) ^ {r}. \tag {2.2.2}
$$

由 Kolmogorov(科尔莫戈罗夫) 强大数定律知, 只要总体矩存在, 样本原点矩  $a_{r}$  就是总体原点矩  $\mu_{r}$  的强相合估计. 注意到中心矩  $\nu_{r}(\boldsymbol{\theta})$  可表示为原点矩  $\mu_{r}(\boldsymbol{\theta})$  的多项式, 故知样本中心矩  $m_{r}$  也是总体中心矩  $\nu_{r}(\boldsymbol{\theta})$  的强相合估计.

由于样本矩已知, 而总体矩包含未知参数, 故由上述强相合性, 当样本量比较大时, 我们可用样本矩 “替代” 总体矩, 即得到如下的方程组:

$$
\mu_ {r} (\boldsymbol {\theta}) = a _ {r}, r = 1, 2, \dots , k. \tag {2.2.3}
$$

记由此方程组得到的解为  $\hat{\theta}$ ，称之为  $\theta$  的矩估计。上述方程被称为矩估计方程。

关于矩估计, 我们注意到:

- 在方程组 (2.2.3) 中也可以通过用样本 $k$ 阶中心矩作为总体 $k$ 阶中心矩的估计而建立相应的估计方程. 这样求得的参数估计也称为矩估计. 当然, 这两种方法得到的矩估计可能不同.
- 方程组 (2.2.3) 的解是否存在且唯一, 取决于具体问题. 如解不存在或不唯一, 则矩估计法不可用.
- 在用矩方法求参数估计时, 尽可能采用低阶矩, 原因之一是避免高阶矩的计算问题, 原因之二是低阶矩提供的信息更重要.

例 2.2.1 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本, 且  $E(X^{2})$  存在有限, 求总体均值与方差的矩估计.

解 记 $\mu = E(X),\sigma^2 = \mathrm{Var}(X)$ ，则由矩估计法知，其估计方程为

$$
\left\{ \begin{array}{l} \hat {\mu} = a _ {1} = \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i}, \\ \hat {\mu} _ {2} = \hat {\mu} ^ {2} + \hat {\sigma} ^ {2} = a _ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2}. \end{array} \right.
$$

由此可求得总体均值与方差的矩估计为

$$
\left\{ \begin{array}{l} \hat {\mu} = \bar {X}, \\ \hat {\sigma} ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) ^ {2} = S _ {n *} ^ {2}. \end{array} \right.
$$

即总体均值的矩估计是样本均值, 总体方差的矩估计是修正的样本方差.

容易验证: 样本均值是总体均值的无偏估计, 但修正的样本方差并不是总体方差的无偏估计. 总之, 虽然样本 r 阶原点矩是总体相应矩的无偏估计, 但是由矩估计方程 (2.2.3) 求得的矩估计并不一定是无偏估计. 另外, 样本 r 阶中心矩也不一定是总体相应矩的无偏估计. 实际上, 有如下结论.

定理 2.2.1 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本, 且 2r 阶矩存在, 则

$$
E (m _ {r}) - \nu_ {r} (\pmb {\theta}) = O (n ^ {- 1}), E [ (\bar {X} _ {n} - \mu_ {1}) ^ {2 r} ] \leqslant c _ {r} \mu_ {2 r} n ^ {- r} = O (n ^ {- r}), \tag {2.2.4}
$$

其中  $c_{r}$  为依赖于 r 的常数.

证明 不妨设 $\mu_{1} = 0$。此时，

$$
E [ (\bar {X} _ {n} - \mu_ {1}) ^ {2 r} ] = E (\bar {X} _ {n} ^ {2 r}) = n ^ {- 2 r} (X _ {1} + X _ {2} + \dots + X _ {n}) ^ {2 r}. \tag {*} \tag *\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\]*\(*\)
$$

在  $(X_{1}+X_{2}+\cdots+X_{n})^{2r}$  的展开式中, 每项均可表示为  $X_{1}^{i_{1}}X_{2}^{i_{2}}\cdots X_{n}^{i_{n}}$ , 其中  $0 \leqslant i_{j} \leqslant 2r, \sum_{j=1}^{n} i_{j} = 2r$ . 如果某项至少有一个  $i_{j} = 1$ , 则该项期望为 0, 于是只需考虑形如

$X_{n_1}^{i_1}X_{n_2}^{i_2}\dots X_{n_t}^{i_t}$ 的项, 其中

$$
1 \leqslant n _ {1} <   n _ {2} <   \dots <   n _ {t} \leqslant n, \quad i _ {j} \geqslant 2, \quad \sum_ {j = 1} ^ {t} i _ {j} = 2 r, \quad t \leqslant r.
$$

由此可知, 在  $(X_{1} + X_{2} + \cdots + X_{n})^{2r}$  的展开式中, 不包括某样本的一次幂的项至多有  $c_{r}n^{r}$  个, 其中  $c_{r}$  为仅依赖于 r 的常数. 由 Hölder(赫尔德) 不等式有

$$
E (| X _ {n _ {1}} ^ {i _ {1}} X _ {n _ {2}} ^ {i _ {2}} \dots X _ {n _ {t}} ^ {i _ {t}} |) \leqslant E (X ^ {2 r}) = \mu_ {2 r}.
$$

结合 (\*) 式, (2.2.4) 式的第二个结论得证.

因为

$$
m _ {r} = a _ {r} - \binom{r}{1} \bar {X} _ {n} a _ {r - 1} + \dots + (- 1) ^ {j} \binom{r}{j} \bar {X} _ {n} ^ {j} a _ {r - j} + \dots + (- 1) ^ {r} \bar {X} _ {n} ^ {r}.
$$

注意到  $\mu_{1}=0,$  则  $E(a_{r})=\mu_{r}=\nu_{r}.$  由上述证明的第二部分, 有

$$
E (| \bar {X} _ {n} ^ {j} a _ {r - j} |) \leqslant \left[ E (\bar {X} _ {n} ^ {2 j}) E (a _ {r - j} ^ {2}) \right] ^ {1 / 2} = O (n ^ {- j / 2}), j = 2, 3, \dots , r.
$$

而

$$
E (\bar {X} a _ {r - 1}) = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} E (X _ {i} ^ {r}) = \frac {1}{n} \mu_ {r} = O (n ^ {- 1}).
$$

由此得证.

定理 2.2.1 说明, 样本 r 阶中心矩是总体中心矩的渐近无偏估计. 陈希孺 (2009) 证明: 当  $n \geqslant r$  时, 存在一个  $\bar{X}, m_{1}, m_{2}, \cdots, m_{n}$  的多项式, 使之为  $\nu_{r}$  的无偏估计. 实际上, 总体方差的无偏估计就是样本方差  $S_{n}^{2} = \frac{n}{n-1} m_{2}$ .

结合注 2.1.5 和强大数定律, 矩估计的强相合性得到了圆满解决, 但矩估计的 r 阶矩相合性则不然. 陈希孺 (2009) 通过样本均值的 r 阶矩相合性证明, 说明了解决问题的烦琐, 且指出: 对于多项式参数  $F(\mu_{1}, \mu_{2}, \cdots, \mu_{m})$ , 如记此多项式每项指数的最大值为 t, 且总体 X 的 rt 阶矩存在, 则此多项式参数的矩估计  $F(a_{1}, a_{2}, \cdots, a_{m})$  是其 r 阶矩相合估计. 如把上述的原点矩换成中心矩, 结论仍成立 (项  $\mu_{1}^{r_{1}} \mu_{2}^{r_{2}} \cdots \mu_{m}^{r_{m}}$  的指数为  $\sum_{i=1}^{m} r_{i}$ ).

下面考虑矩估计的渐近正态性, 为此, 先给出下面引理所述的多元 Delta 定理.

引理 2.2.1 设  $\left\{X_{n}=(X_{n1},X_{n2},\cdots,X_{nk})^{\mathrm{T}}\right\}_{n\geqslant1}$  为一列 k 元随机向量，且满足

$$
\sqrt {n} (\boldsymbol {X} _ {n} - \boldsymbol {\theta}) \xrightarrow {\mathrm{d}} N _ {k} (0, \Sigma),
$$

其中  $\boldsymbol{\theta}=(\theta_{1},\theta_{2},\cdots,\theta_{k})^{\mathrm{T}}$  为参数向量， $\Sigma>0$  为 k 阶对称矩阵。又设  $g_{i}(\boldsymbol{x})$  为 k 元连续可微函数，记  $\boldsymbol{g}=(g_{1},g_{2},\cdots,g_{m})^{\mathrm{T}}$ 。则

$$
\sqrt {n} [ \boldsymbol {g} (\boldsymbol {X} _ {n}) - \boldsymbol {g} (\boldsymbol {\theta}) ] \xrightarrow {\mathrm{d}} N _ {m} (0, \Delta \Sigma \Delta^ {\mathrm{T}}), \tag {2.2.5}
$$

其中  $\Delta=(\partial g_{i}(\boldsymbol{\theta})/\partial\theta_{j})_{m\times k}\neq0.$

证明 由于 $g_{i}$ 连续可微, 故由Taylor(泰勒)展开可知

$$
\sqrt {n} [ \boldsymbol {g} (\boldsymbol {X} _ {n}) - \boldsymbol {g} (\boldsymbol {\theta}) ] = \sqrt {n} \Delta (\boldsymbol {X} _ {n} - \boldsymbol {\theta}) + \sqrt {n} \cdot o (\boldsymbol {X} _ {n} - \boldsymbol {\theta}). \tag {*1}
$$

又由于 $\sqrt{n} (\pmb {X}_n - \pmb {\theta})$ 有极限分布，即弱收敛，故知

$$
\sqrt {n} (\boldsymbol {X} _ {n} - \boldsymbol {\theta}) = O _ {p} (1). \tag {*2}
$$

结合已知条件以及  $(*1)$ ,  $(*2)$  式, 结论得证.

![](images/page_89_image_7.jpg)

结合上述引理及中心极限定理, 有如下结论:

定理 2.2.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本, 假设总体 2m 阶矩存在. 对于给定的整数  $1 \leqslant r_{1} \leqslant r_{2} \leqslant \cdots \leqslant r_{k} \leqslant m$ , 如一个 k 元函数 g 连续可微, 则

$$
\sqrt {n} [ g (a _ {r _ {1}}, a _ {r _ {2}}, \dots , a _ {r _ {k}}) - g (\mu_ {r _ {1}}, \mu_ {r _ {2}}, \dots , \mu_ {r _ {k}}) ] \xrightarrow {\mathrm{d}} N (0, \boldsymbol {\delta} ^ {\mathrm{T}} B \boldsymbol {\delta}),
$$

其中  $\boldsymbol{\delta}=\left(\frac{\partial g(\boldsymbol{x})}{\partial x_{1}},\frac{\partial g(\boldsymbol{x})}{\partial x_{2}},\cdots,\frac{\partial g(\boldsymbol{x})}{\partial x_{k}}\right)^{\mathrm{T}},B=\left(E[(X^{r_{i}}-\mu_{r_{i}})(X^{r_{j}}-\mu_{r_{j}})]\right)_{k\times k}.$

由于样本中心矩是样本原点矩的多项式, 总体中心矩是总体原点矩的多项式, 故定理 2.2.2 的结论仍适用.

例 2.2.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本, 求样本变异系数  $S_{n}/\bar{X}_{n}$  的极限分布.

解 记  $\sigma^{2}=\mathrm{Var}(X)$ . 由于总体变异系数为

$$
\sigma / \mu_ {1} = \sqrt {\mu_ {2} - \mu_ {1} ^ {2}} / \mu_ {1},
$$

则取 $g(x_{1},x_{2}) = \sqrt{x_{2} - x_{1}^{2}} /x_{1}$ .由于它连续可微,则由定理2.2.2可得

$$
\sqrt {n} \left(\frac {S _ {n}}{\bar {X} _ {n}} - \frac {\sigma}{\mu_ {1}}\right) \xrightarrow {\mathrm{d}} N (0, \lambda^ {2}),
$$

其中

$$
\lambda^ {2} = \frac {\mu_ {1} ^ {2} (\nu_ {4} - \nu_ {2} ^ {2}) - 4 \mu_ {1} \nu_ {2} \nu_ {3} + 4 \nu_ {2} ^ {3}}{4 \mu_ {1} ^ {4} \nu_ {2}}.
$$

当总体分布为 $N(\mu, \sigma^2)$ 时，上述极限分布的方差 $\lambda^2 = (\mu^2 + 2\sigma^2)\sigma^2 / (2\mu^4)$.

![](images/page_89_image_21.jpg)

## 2.3 最大似然估计

最大似然估计 (MLE) 最早由德国数学家 Gauss 在 1821 年针对正态分布提出, 之后 Fisher 于 1922 年提出了一般分布下的最大似然估计. 本节将给出最大似然估计的定义和某些性质, 以及求取某些复杂情况下最大似然估计的一种有效算法——EM 算法.

## 2.3.1 MLE 的定义

在给出最大似然估计定义之前, 先通过下面例子解释最大似然的基本思想.

例 2.3.1 假设一个罐中有白球和黑球, 且二者数目之比为 1:3, 但不知哪种颜色的球多. 现通过返回抽样方法估计罐中黑球数目的比例 p.

解 记从罐中返回抽取 $n$ 次时, 抽到的黑球个数为 $X$. 则由概率论知识有, $X \sim B(n, p)$, 即

$$
P (x; p) \stackrel {\mathrm{def}} {=} P (X = x | p) = \binom {n} {x} p ^ {x} (1 - p) ^ {n - x}. \tag {*}.
$$

由于 $p$ 等于 $1/4$ 或 $3/4$, 故抽样的目的在于通过样本值 $X$ 的大小来估计 $p$, 记 $p$ 的估计为 $\hat{p}(X)$. 为此, 我们先看一个 $n = 3$ 的简单情况. 此时, 对于不同的样本值 $x$, (\*)式的概率见表2.3.1.

表 2.3.1 最大似然原理

| x | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| $P\left(x;\frac{3}{4}\right)$ | $\frac{1}{64}$ | $\frac{9}{64}$ | $\frac{27}{64}$ | $\frac{27}{64}$ |
| $P\left(x;\frac{1}{4}\right)$ | $\frac{27}{64}$ | $\frac{27}{64}$ | $\frac{9}{64}$ | $\frac{1}{64}$ |

由表 2.3.1 可以看出, 当 x = 0 时, 因为  $\frac{27}{64} \gg \frac{1}{64}$ , 所以认为 p 取  $\frac{1}{4}$  更有可能, 或看起来更像. 于是, 取  $\hat{p}(0) = \frac{1}{4}$  比  $\hat{p}(0) = \frac{3}{4}$  更合理. 基于这样的思想, 得到 p 的一个合理估计:

$$
\hat {p} (x) = \left\{ \begin{array}{l l} \frac {1}{4}, & x = 0, 1, \\ \frac {3}{4}, & x = 2, 3. \end{array} \right.
$$

实际上, 上述估计的合理性可如下解释: 概率最大的事件最有可能发生, 即估计值  $\hat{p}(x)$  满足不等式:

$$
P (X = x | \hat {p} (x)) \geqslant P (X = x | p ^ {\prime}), \forall p ^ {\prime}, \forall x.
$$

这就是我们要讲的最大似然的基本思想.

定义 2.3.1 (似然函数 (likelihood function)) 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体分布  $f(x; \theta)$  的样本，其中参数  $\theta \in \Theta \subset R^{k}$ ，记样本分布为  $f(\boldsymbol{x}; \theta)$ 。则对于给定的样本观测值  $\boldsymbol{x} = (x_{1}, x_{2}, \cdots, x_{n})$ ，称  $f(\boldsymbol{x}; \theta)$  为参数  $\theta$  的似然函数，并记之为

$$
L (\boldsymbol {\theta}; \boldsymbol {x}) = f (\boldsymbol {x}; \boldsymbol {\theta}), \forall \boldsymbol {\theta} \in \Theta .
$$

称  $\ln L(\boldsymbol{\theta};\boldsymbol{x})$  为对数似然函数, 记为  $l(\boldsymbol{\theta};\boldsymbol{x})$  或  $l(\boldsymbol{\theta})$ .

从定义可以看出, 似然函数就是样本分布, 但二者的含义却不同:

- 样本分布表示给定参数 $\theta$ 下, 样本取值的概率, 它是样本的函数, 定义域为样本空间 $\mathcal{X}$.
- 似然函数表示给定样本值 $x$ 后, 参数 $\theta$ 的取值可能, 其定义域为参数空间 $\Theta$.

如果把参数  $\theta$  和样本分别看作 “原因” 和 “结果”，则可以理解为:当给定参数后，样本分布告诉我们哪个样本将以多大的概率被观测到；反过来，当有了样本后，似然函数将告诉我们如何最有可能地估计参数  $\theta$ .

“似然”的英文含义是“看起来像”，之所以称为似然函数，就是要利用这个函数得到参数看起来更合理的估计，即下面的最大似然估计.

为书写简单, 在不引起混淆的情况下, 我们以 X 表示样本  $X_{1}, X_{2}, \cdots, X_{n}$ , 而 x 表示样本 X 的取值.

定义 2.3.2 (MLE) 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的样本, 且总体概率分布为  $f(x; \theta)$ , 其中  $\theta \in \Theta \subset R^{k}$  是参数, 且记  $\bar{\Theta}$  为  $\Theta$  的闭包. 如  $\hat{\theta}(x)$  满足

$$
L (\hat {\boldsymbol {\theta}} (\boldsymbol {x}); \boldsymbol {x}) = \sup _ {\boldsymbol {\theta} \in \bar {\Theta}} L (\boldsymbol {\theta}; \boldsymbol {x}), \tag {2.3.1}
$$

或等价地满足

$$
l (\hat {\boldsymbol {\theta}} (\boldsymbol {x}); \boldsymbol {x}) = \sup _ {\boldsymbol {\theta} \in \bar {\Theta}} l (\boldsymbol {\theta}; \boldsymbol {x}), \tag {2.3.2}
$$

则称  $\hat{\theta}(X)$  为  $\theta$  的 MLE.

从上一定义可以看出, 求某参数的 MLE, 就是求 (2.3.1) 或 (2.3.2) 式的极值问题. 如果似然函数  $L(\boldsymbol{\theta}; \boldsymbol{x})$  关于  $\theta$  可微, 则  $\theta$  的 MLE 可以通过解方程

$$
\frac {\partial L (\boldsymbol {\theta} ; \boldsymbol {x})}{\partial \boldsymbol {\theta} _ {j}} = 0, j = 1, 2, \dots , k, \tag {2.3.3}
$$

或解方程

$$
\frac {\partial l (\boldsymbol {\theta} ; \boldsymbol {x})}{\partial \boldsymbol {\theta} _ {j}} = 0, j = 1, 2, \dots , k \tag {2.3.4}
$$

求得. 在统计上, 称方程 (2.3.3) 或 (2.3.4) 为似然方程或对数似然方程.

![](images/page_91_image_20.jpg)

注2.3.1 在上述定义中，极值在参数空间闭包上求取的原因在于，如果参数空间 $\Theta$ 为开集，则似然函数的最大值有可能在边界上达到，从而导致在参数空间 $\Theta$ 中无最大值解.

例 2.3.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自正态总体  $N(\mu, \sigma^{2})$  的独立同分布样本, 求  $\mu$  和  $\sigma^{2}$  的 MLE.

解 此时的似然函数为

$$
L (\mu , \sigma^ {2}; \pmb {x}) = \frac {1}{(\sqrt {2 \pi} \sigma) ^ {n}} \exp \left\{- \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} (x _ {i} - \mu) ^ {2} \right\},
$$

其对数似然函数为

$$
l (\mu , \sigma^ {2}; \pmb {x}) = - \frac {n}{2} \ln (2 \pi) - \frac {n}{2} \ln \sigma^ {2} - \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} (x _ {i} - \mu) ^ {2},
$$

两边分别对  $\mu$  和  $\sigma^{2}$  求导, 再令其为零, 则得到如下的似然方程:

$$
\left\{ \begin{array}{l} \frac {\partial l}{\partial \mu} = \frac {1}{\sigma^ {2}} \sum_ {i = 1} ^ {n} (x _ {i} - \mu) = 0, \\ \frac {\partial l}{\partial \sigma^ {2}} = - \frac {n}{2 \sigma^ {2}} + \frac {1}{2 \sigma^ {4}} \sum_ {i = 1} ^ {n} (x _ {i} - \mu) ^ {2} = 0, \end{array} \right.
$$

由此求得其根为

$$
\left\{ \begin{array}{l} \mu = \bar {x}, \\ \sigma^ {2} = s _ {n *} ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) ^ {2}, \end{array} \right.
$$

容易验证上述两根的确使其似然达到最大, 于是, 所求的 MLE 为

$$
\hat {\mu} = \bar {X}, \hat {\sigma} ^ {2} = S _ {n *} ^ {2}.
$$

比较例 2.2.1 与例 2.3.2 知道, 对于正态总体, 总体均值与方差的矩估计和 MLE 是一样的.

例 2.3.3 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自均匀分布  $U(0, \theta)$  的独立同分布样本, 求参数  $\theta$  的 MLE.

解 此时的似然函数为

$$
L (\theta ; \pmb {x}) = \prod_ {i = 1} ^ {n} f (x _ {i}; \theta) = \left\{ \begin{array}{l l} {{ \frac {1}{\theta^ {n}},}} & {{0 <   \max _ {1 \leqslant i \leqslant n} x _ {i} <   \theta ,}} \\ {{0,}} & {{\text {其他}.}} \end{array} \right.
$$

从图 2.3.1 可以看出, 此似然函数是截断型的, 故不连续, 不能用求导法. 但从其形式上看,  $L(\theta; \boldsymbol{x})$  是  $\theta$  的单调下降函数, 而当  $\theta = \max_{1 \leqslant i \leqslant n} x_i$  时,  $L(\theta; \boldsymbol{x})$  取得最大值, 于是  $\hat{\theta} = X_{(n)}$  是  $\theta$  的 MLE. □

![](images/page_93_chart_2.jpg)

<details>
<summary>line</summary>

| \(\theta\) | \(L(\theta; x)\) |
| --- | --- |
| 0 | 0 |
| X_(n) | ~High Value |
</details>

图2.3.1 例2.3.3的似然函数

由例 2.1.6 知道,  $\frac{n+1}{n}X_{(n)}$  是  $\theta$  的 UMVUE, 这就说明, 此时  $\theta$  的 MLE 并不是 UMVUE.

注2.3.2 从前面的例子可以看出, MLE 是充分统计量的函数. 实际上, 如果 $T$ 是充分统计量, 则由因子分解定理可知, $f(\boldsymbol{x}; \theta) = g_{\theta}(T(\boldsymbol{x}))h(\boldsymbol{x})$, 于是, $l(\theta; \boldsymbol{x}) = \ln g_{\theta}(T(\boldsymbol{x})) + \ln h(\boldsymbol{x})$, 由此可见, 为使对数似然达到最大, 只需使 $g_{\theta}(T(\boldsymbol{x}))$ 达到最大, 所以, MLE 肯定是充分统计量 $T(\boldsymbol{X})$ 的函数.

最大似然估计即使存在, 也可能不唯一, 见下例.

例 2.3.4 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $U(\theta, \theta + 1)$  的独立同分布样本,  $\theta \in R$ , 求  $\theta$  的 MLE.

解 此时其似然函数为

$$
L (\theta ; \pmb {x}) = \left\{ \begin{array}{l l} 1, & \theta \leqslant x _ {(1)} \leqslant x _ {(n)} \leqslant \theta + 1, \\ 0, & \text {其他.} \end{array} \right.
$$

由于此时的似然函数在不为零的区域上是常数, 故只要  $\theta$  不超过  $x_{(1)}$ , 且  $\theta + 1$  不小于  $x_{(n)}$ , 其似然函数均达到最大值 1, 故  $\theta$  的 MLE 不止一个, 在区间  $[X_{(n)} - 1, X_{(1)}]$  中的任何一个均是  $\theta$  的 MLE. □

例 2.3.5 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自 Cauchy 分布  $C(\theta, 1)$  的独立同分布样本, 其总体概率密度为

$$
f (x; \theta) = \frac {1}{\pi [ 1 + (x - \theta) ^ {2} ]}, x \in \mathbb {R}, \theta \in \mathbb {R}.
$$

求  $\theta$  的 MLE.

解 由于似然函数

$$
L (\theta ; \boldsymbol {x}) = \frac {1}{\pi^ {n}} \frac {1}{\prod_ {i = 1} ^ {n} [ 1 + (x _ {i} - \theta) ^ {2} ]}
$$

非负, 且随着 $\theta \to \infty$, 而趋于 0, 故肯定有最大值.

其对数似然函数为

$$
l (\theta ; \boldsymbol {x}) = - n \ln \pi - \sum_ {i = 1} ^ {n} \ln [ 1 + (x _ {i} - \theta) ^ {2} ],
$$

由于它可导, 故其最大值为下面的对数似然方程的解:

$$
g (\theta) \stackrel {\text {def}} {=} \sum_ {i = 1} ^ {n} \frac {x _ {i} - \theta}{1 + (x _ {i} - \theta) ^ {2}} = 0. \tag {*}
$$

由于此对数似然方程没有显式解, 故只能利用迭代法求解. 为求 (\*) 式的对数似然方程的解, 我们采用 Newton-Raphon 迭代算法. 由于其导数为

$$
g ^ {\prime} (\theta) = \frac {\partial g (\theta)}{\partial \theta} = \sum_ {i = 1} ^ {n} \frac {(x _ {i} - \theta) ^ {2} - 1}{[ 1 + (x _ {i} - \theta) ^ {2} ] ^ {2}},
$$

故第 $k + 1$ 步迭代解为

$$
\theta_ {k + 1} = \theta_ {k} - \frac {g (\theta_ {k})}{g ^ {\prime} (\theta_ {k})}.
$$

重复以上迭代, 直到绝对误差  $\left|\theta_{k+1}-\theta_{k}\right|$  或相对误差  $\frac{\left|\theta_{k+1}-\theta_{k}\right|}{\left|\theta_{k}\right|}$  满足事先给定的误差. □

但利用迭代法求取MLE时必须注意到，迭代算法的结果依赖于初值的选取，故无法保证所求得之值确为最大值点，而可能是局部极大值.此时，一个最简单的方法就是尝试多个不同初值，之后再比较哪个似然函数最大.

由例 2.3.2 知道, 修正的样本方差  $S_{n*}^{2}$  是总体方差的 MLE, 一个自然问题是: 修正的样本标准差  $S_{n*}$  是总体标准差的 MLE 吗? 此时, 一个一般问题是: 如参数  $\theta$  的 MLE 为  $\hat{\theta}$ , 则对于给定的函数  $g(\cdot)$ , 参数  $g(\boldsymbol{\theta})$  的 MLE 是  $g(\hat{\boldsymbol{\theta}})$  吗?

答案是肯定的.但如果函数 g 不是一一对应，需要对似然函数做一简单修正.设  $\theta \in \Theta \subset R^{k}$ ，似然函数为  $L(\theta)$ ，对于函数  $g(\cdot)$ ，定义

$$
\boldsymbol {\psi} = g (\boldsymbol {\theta}) \in \varPsi \subset \mathbb {R} ^ {r},
$$

其中 $r \leqslant k$. 注意到 $\psi$ 的取值空间可能比 $\theta$ 的取值空间小, 即在空间 $\Psi$ 上的一个点 $\psi$, 可能对应着 $\Theta$ 上的许多点. 为了求 $\psi$ 的 MLE, 先定义关于它的似然函数如下:

定义 2.3.3 (导出似然) 对于  $\psi \in \Psi$ ，如记  $g^{-1}(\psi) = \{\theta : g(\theta) = \psi\}$ ，则参数  $\psi$  的导出似然定义为

$$
L ^ {*} (\psi) = \max _ {\{\theta : g (\theta) = \psi \}} L (\theta) = \max _ {\theta \in g ^ {- 1} (\psi)} L (\theta). \tag {2.3.5}
$$

则我们称

$$
\hat {\psi} = \arg \max _ {\psi \in \varPsi} L ^ {*} (\psi)
$$

为  $\psi$  的 MLE.

有了上述定义, 则有

$$
L ^ {*} (\hat {\psi}) = \max _ {\boldsymbol {\theta} \in g ^ {- 1} (\hat {\psi})} L (\boldsymbol {\theta}) = \max _ {\boldsymbol {\psi} \in \Psi} L ^ {*} (\boldsymbol {\psi}) \geqslant \max _ {\boldsymbol {\theta} \in g ^ {- 1} (\boldsymbol {\psi})} L (\boldsymbol {\theta}) = L ^ {*} (\boldsymbol {\psi}).
$$

从而有如下被称为最大似然估计变换不变的定理:

定理 2.3.1 设样本来自参数分布族  $f(x;\boldsymbol{\theta})$ ,  $\boldsymbol{\theta} \in \Theta \subset R^{k}$ . 如果参数  $\theta$  的最大似然估计为  $\hat{\theta}$ , 则参数  $\psi = g(\boldsymbol{\theta}) \in \Psi \subset \mathbb{R}^{r}$  的 MLE 为  $\hat{\psi} = g(\hat{\boldsymbol{\theta}})$ , 其中  $r \leqslant k$ .

## 2.3.2 MLE的相合性

为简单, 本小节只考虑单参数情况, 且设参数空间 $\Theta$ 是一个开区间. 另外, 假设 $n$ 个样本独立同分布, 总体概率分布为 $f(x; \theta)$, 且在参数空间 $\Theta$ 上关于 $\theta$ 可导. 记对数似然函数为 $l(\theta; \boldsymbol{x}) = \sum_{i=1}^{n} \ln f(x_i; \theta)$.

定理 2.3.2 记  $\theta_{0}$  为参数真值, 且设

$$
E _ {\theta_ {0}} (| \ln f (X; \theta_ {0}) |) <   \infty . \tag {2.3.6}
$$

则以概率 1 当 n 充分大时, 可找到对数似然方程

$$
\frac {\partial l (\theta ; \boldsymbol {x})}{\partial \theta} = 0 \tag {2.3.7}
$$

之一根 $\hat{\theta}_n(\pmb {x})$ ，满足

$$
\hat {\theta} _ {n} (\boldsymbol {X}) \longrightarrow \theta_ {0}, \text {a.s.} P _ {\theta_ {0}}, \tag {2.3.8}
$$

其中 $P_{\theta_0}$ 表示样本 $\pmb{X}$ 在参数真值 $\theta_0$ 处的概率分布.又若(2.3.6）式对一切 $\theta_0\in \Theta$ 均成立，且存在 $\theta$ 的一个强（弱）相合估计 $\tilde{\theta}_n$ ，则存在 $\theta$ 的一个强（弱）相合估计，是对数似然方程(2.3.7）的一个根.

证明请参见陈希孺 (2009) 第 150—152 页. 另外, 陈希孺 (2009) 也研究了某些情况下, 对数似然方程的解与强相合估计间的关系.