注 1.2.3 关于极小次序统计量的抽样分布, 我们也可以如下求得:

$$
\begin{array}{l} G _ {1} (x) = P (X _ {(1)} \leqslant x) = 1 - P (X _ {(1)} > x) \\ = 1 - P (X _ {1}, X _ {2}, \dots , X _ {n} \text {均大于} x) \\ = 1 - \prod_ {i = 1} ^ {n} P (X _ {i} > x) = 1 - [ 1 - F (x) ] ^ {n}. \\ \end{array}
$$

注1.2.4 利用类似于例1.2.3的方法, 可求得任意两个次序统计量的联合概率密度函数如下: 设 $1 \leqslant r < s \leqslant n$, 则 $X_{(r)}$ 与 $X_{(s)}$ 的联合概率密度函数为 $(x \leqslant y)$

$$
g _ {r, s} (x, y) = \frac {n !}{(r - 1) ! (s - r - 1) ! (n - s) !}.
$$

$$
F ^ {r - 1} (x) [ F (y) - F (x) ] ^ {s - r - 1} [ 1 - F (y) ] ^ {n - s} f (x) f (y),
$$

其中  $f(x)$  为总体 X 的概率密度函数.

注1.2.5 独立同分布样本的 $n$ 个次序统计量的联合概率密度函数为

$$
g (x _ {1}, x _ {2}, \dots , x _ {n}) = n! \prod_ {i = 1} ^ {n} f (x _ {i}), \quad x _ {1} \leqslant x _ {2} \leqslant \dots \leqslant x _ {n}, \tag {1.2.11}
$$

其中  $f(x)$  为总体 X 的概率密度函数.

由 (1.2.11) 式给出的联合概率密度, 可求得任意几个次序统计量的联合概率密度.

## 1.3 一些常用的抽样分布

本节将讲述统计中经常用到的几个抽样分布:$\chi^2$ 分布、$t$ 分布、$F$ 分布，以及指数型分布、$\Gamma$ 分布等。另外，我们也把几个经常遇到的分布，如次 Gauss(高斯) 分布、$\beta$ 分布、Laplace 分布、Cauchy(柯西) 分布、Pareto(帕雷托) 分布、logistic 分布、对数正态分布、Weibull(韦布尔) 分布、双指数分布等的概率密度函数，以及期望、方差列出，供大家参考使用。

## 1.3.1  $\chi^{2}$  分布

定义 1.3.1 ( $\chi^{2}$  分布) 设  $X_{1}, X_{2}, \cdots, X_{n} \stackrel{\mathrm{iid}}{\sim} N(0,1)$ ，则称随机变量

$$
\xi = \sum_ {i = 1} ^ {n} X _ {i} ^ {2}
$$

所服从的分布为自由度 n 的  $\chi^{2}$  分布, 也称  $\xi$  为自由度 n 的  $\chi^{2}$  随机变量, 并记为  $\xi \sim \chi^{2}(n)$ .

定理 1.3.1 设  $X \sim \chi^{2}(n)$ ，则其概率密度为

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{2 ^ {n / 2} \Gamma (n / 2)} \mathrm{e} ^ {- \frac {x}{2}} x ^ {\frac {n}{2} - 1}, & x \geqslant 0, \\ 0, & x <   0. \end{array} \right. \tag {1.3.1}
$$

证明 为求 $X$ 的概率密度, 我们先求其累积分布函数 $F(x) = P(X \leqslant x)$. 显然, 当 $x < 0$ 时, $F(x) = 0$; 当 $x \geqslant 0$ 时,

$$
F (x) = P \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2} \leqslant x\right).
$$

因为  $X_{1}, X_{2}, \cdots, X_{n}$  相互独立且同分布于  $N(0,1)$ ，所以  $(X_{1}, X_{2}, \cdots, X_{n})$  的联合概率密度为

$$
\frac {1}{(2 \pi) ^ {n / 2}} \exp \left\{- \frac {1}{2} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} \right\}.
$$

于是，

$$
F (x) = \frac {1}{(2 \pi) ^ {n / 2}} \int \dots \iint_ {\sum_ {i = 1} ^ {n} x _ {i} ^ {2} \leqslant x} \exp \left\{- \frac {1}{2} \sum_ {i = 1} ^ {n} x _ {i} ^ {2} \right\} \mathrm{d} x _ {1} \mathrm{d} x _ {2} \dots \mathrm{d} x _ {n}.
$$

为求此积分, 做球面坐标变换

$$
\left\{ \begin{array}{l} x _ {1} = \rho \cos \theta_ {1} \cos \theta_ {2} \dots \cos \theta_ {n - 1}, \\ x _ {2} = \rho \cos \theta_ {1} \cos \theta_ {2} \dots \sin \theta_ {n - 1}, \\ \dots \dots \\ x _ {n} = \rho \sin \theta_ {1}, \end{array} \right.
$$

此变换的 Jacobi(雅可比) 行列式的绝对值为

$$
J = \left| \frac {\partial (x _ {1} , x _ {2} , \cdots , x _ {n})}{\partial (\rho , \theta_ {1} , \theta_ {2} , \cdots , \theta_ {n - 1})} \right| = \rho^ {n - 1} D (\theta_ {1}, \theta_ {2}, \dots , \theta_ {n - 1}),
$$

其中  $D(\theta_{1},\theta_{2},\cdots,\theta_{n-1})$  与  $\rho$  无关. 于是,

$$
\begin{array}{l} F (x) = \frac {1}{(2 \pi) ^ {n / 2}} \int_ {0} ^ {\sqrt {x}} \mathrm{d} \rho \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \dots \int_ {- \frac {\pi}{2}} ^ {\frac {\pi}{2}} \int_ {- \pi} ^ {\pi} \mathrm{e} ^ {- \rho^ {2} / 2} \rho^ {n - 1} D (\theta_ {1}, \theta_ {2}, \dots , \theta_ {n - 1}) \mathrm{d} \theta_ {1} \mathrm{d} \theta_ {2} \dots \mathrm{d} \theta_ {n - 1} \\ = C _ {n} \int_ {0} ^ {\sqrt {x}} \mathrm{e} ^ {- \rho^ {2} / 2} \rho^ {n - 1} \mathrm{d} \rho , \\ \end{array}
$$

其中  $C_{n}=\frac{1}{(2\pi)^{n/2}}\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\cdots\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\int_{-\pi}^{\pi}D(\theta_{1},\theta_{2},\cdots,\theta_{n-1})\mathrm{d}\theta_{1}\mathrm{d}\theta_{2}\cdots\mathrm{d}\theta_{n-1}.$

令 $\rho = \sqrt{y}$, 则 $\mathrm{d}\rho = \frac{\mathrm{d}y}{2\sqrt{y}}$, 于是,

$$
\begin{array}{l} F (x) = C _ {n} \int_ {0} ^ {x} \mathrm{e} ^ {- y / 2} y ^ {(n - 1) / 2} \frac {1}{2 y ^ {1 / 2}} \mathrm{d} y \\ = \frac {C _ {n}}{2} \int_ {0} ^ {x} \mathrm{e} ^ {- y / 2} y ^ {n / 2 - 1} \mathrm{d} y. \\ \end{array}
$$

又因为

$$
1 = F (\infty) = \frac {C _ {n}}{2} \int_ {0} ^ {\infty} \mathrm{e} ^ {- y / 2} y ^ {n / 2 - 1} \mathrm{d} y,
$$

而

$$
\int_ {0} ^ {\infty} \mathrm{e} ^ {- y} y ^ {n / 2 - 1} \mathrm{d} y = \Gamma (n / 2),
$$

故

$$
C _ {n} = \frac {1}{2 ^ {\frac {n}{2} - 1} \Gamma \left(\frac {n}{2}\right)}.
$$

这样, $\chi^{2}(n)$ 分布的累积分布函数为

$$
F (x) = \frac {1}{2 ^ {\frac {n}{2}} \Gamma \left(\frac {n}{2}\right)} \int_ {0} ^ {x} \mathrm{e} ^ {- \frac {y}{2}} y ^ {\frac {n}{2} - 1} \mathrm{d} y,
$$

其概率密度为

$$
f (x) = \frac {1}{2 ^ {\frac {n}{2}} \Gamma \left(\frac {n}{2}\right)} \mathrm{e} ^ {- \frac {x}{2}} x ^ {\frac {n}{2} - 1}, \forall x \geqslant 0.
$$

图 1.3.1 给出了自由度分别为 5, 10 和 20 的  $\chi^{2}$  分布的概率密度函数 (记为 pdf). 从中可以看出, 随着自由度增大, 其概率密度函数右移, 对称性越来越好, 且越来越 “像” 正态分布的概率密度函数.

![](images/page_35_chart_2.jpg)

<details>
<summary>line</summary>

| x | pdf (n=5) | pdf (n=10) | pdf (n=20) |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| ~3 | ~0.15 | — | — |
| ~8 | — | ~0.10 | — |
| ~14 | — | — | ~0.05 |
| ~18 | — | — | ~0.07 |
| 40 | 0 | 0 | 0 |
</details>

图1.3.1 $\chi^2$ 分布的概率密度函数

注1.3.1 由于 $\chi^2 (n)$ 分布是 $n$ 个独立的标准正态分布的平方和，故由中心极限定理可知，把其中心标准化后的极限分布就是正态分布。此结论也可由(1.3.2)式给出的其特征函数证明。

利用定理 1.3.1 的结论, 可以求得  $\chi^{2}(n)$  分布的特征函数为

$$
\psi (t) = (1 - 2 \mathrm{i} t) ^ {- n / 2}, \tag {1.3.2}
$$

并由此可求得其期望与方差分别为 n 与 2n. 另外, 利用上述特征函数还可以证明: 如果  $X_{i} \sim \chi^{2}(n_{i}), i = 1, 2, \cdots, k$ , 且  $X_{1}, X_{2}, \cdots, X_{k}$  相互独立, 则  $\sum_{i=1}^{k} X_{i} \sim \chi^{2}\left(\sum_{i=1}^{k} n_{i}\right)$ .

由于抽样分布是某统计量的分布, 自然要问: 哪个统计量的分布是  $\chi^{2}$  分布? 为此, 我们先给一个引理.

引理 1.3.1 设  $X_{1}, X_{2}, \cdots, X_{n}$  相互独立，且  $X_{i} \sim N(\mu_{i}, \sigma^{2})$ ， $A = (a_{ij})$  为 n 阶正交矩阵，记

$$
\left( \begin{array}{c} Y _ {1} \\ Y _ {2} \\ \vdots \\ Y _ {n} \end{array} \right) = A \left( \begin{array}{c} X _ {1} \\ X _ {2} \\ \vdots \\ X _ {n} \end{array} \right).
$$

则  $Y_{1}, Y_{2}, \cdots, Y_{n}$  相互独立，且  $Y_{i} \sim N(\beta_{i}, \sigma^{2})$ ，其中  $\beta_{i} = \sum_{j=1}^{n} a_{ij} \mu_{j}$ .

证明 因为 $A$ 为正交矩阵, 所以由 $X$ 到 $Y$ 的变换的 Jacobi 行列式的绝对值为 1, 且

$$
\sum_ {i = 1} ^ {n} (Y _ {i} - \beta_ {i}) ^ {2} = \sum_ {i = 1} ^ {n} (X _ {i} - \mu_ {i}) ^ {2}.
$$

又因为 $(X_{1},X_{2},\cdots,X_{n})$ 的联合概率密度为

$$
(2 \pi \sigma^ {2}) ^ {- n / 2} \exp \left\{- \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} (x _ {i} - \mu_ {i}) ^ {2} \right\},
$$

则知道 $(Y_{1},Y_{2},\cdots,Y_{n})$ 的联合概率密度为

$$
(2 \pi \sigma^ {2}) ^ {- n / 2} \exp \left\{- \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} (y _ {i} - \beta_ {i}) ^ {2} \right\},
$$

故结论得证.

定理 1.3.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $N(\mu, \sigma^{2})$  的独立同分布样本,  $\bar{X}, S_{n}^{2}$  为样本均值与样本方差, 则

(1)  $\bar{X} \sim N(\mu, \sigma^{2}/n).$
(2) $(n - 1)S_{n}^{2} / \sigma^{2}\sim \chi^{2}(n - 1)$
(3)  $\bar{X}$  与  $S_{n}^{2}$  独立.

证明 设 $A = (a_{ij})$ 为 $n$ 阶正交矩阵, 且其第一行的元素均为 $1 / \sqrt{n}$. 作变换

$$
\left( \begin{array}{c} Y _ {1} \\ Y _ {2} \\ \vdots \\ Y _ {n} \end{array} \right) = A \left( \begin{array}{c} X _ {1} \\ X _ {2} \\ \vdots \\ X _ {n} \end{array} \right).
$$

由引理 1.3.1 知, $Y_{1}, Y_{2}, \cdots, Y_{n}$ 相互独立, 且 $Y_{i} \sim N(\beta_{i}, \sigma^{2})$, 其中 $\beta_{i} = \mu \sum_{j=1}^{n} a_{ij}$. 由于 $A$ 为正交矩阵, 且第一行为 $(1, 1, \cdots, 1)/\sqrt{n}$, 则

- $\beta_{1} = \sqrt{n}\mu, \beta_{i} = 0 (i = 2,3,\dots,n)$.
$\sum_{i=1}^{n}Y_{i}^{2}=\sum_{i=1}^{n}X_{i}^{2}.$
- $Y_{1} = \sqrt{n}\bar{X}$.

而

$$
(n - 1) S _ {n} ^ {2} = \sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) ^ {2} = \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - n \bar {X} ^ {2} = \sum_ {i = 1} ^ {n} Y _ {i} ^ {2} - Y _ {1} ^ {2} = \sum_ {i = 2} ^ {n} Y _ {i} ^ {2}.
$$

综上可知

$$
\bar {X} = Y _ {1} / \sqrt {n} \sim N (\mu , \sigma^ {2} / n), (n - 1) S _ {n} ^ {2} / \sigma^ {2} \sim \chi^ {2} (n - 1).
$$

另外, 由于  $\bar{X}$  仅依赖于  $Y_{1}, S_{n}^{2}$  仅依赖于  $Y_{2}, Y_{3}, \cdots, Y_{n}$ , 而  $Y_{1}, Y_{2}, \cdots, Y_{n}$  相互独立, 则知  $\bar{X}$  与  $S_{n}^{2}$  独立. □注 1.3.2 设 $X_{1}, X_{2}, \cdots, X_{n}$ 为来自总体 $X$ 的独立同分布样本，如果其样本均值 $\bar{X}$ 与样本方差 $S_{n}^{2}$ 独立，则总体 $X$ 必为正态分布（见 Stuart et al.(1987)). 实际上，样本均值与样本方差的协方差为 $\operatorname{Cov}(\bar{X}, S_{n}^{2}) = \frac{\nu_{3}}{n}$，其中 $\nu_{k} = E[X - E(X)]^{k}$ 为总体 $k$ 阶中心矩.

从  $\chi^{2}$  分布的定义不难看出,  $\chi^{2}$  分布是若干个独立的标准正态随机变量的平方和, 而平方和是二次型的一个特殊形式, 那一个正态随机向量的二次型的分布如何呢? 这即是下面的 Cochran(科克伦) 定理.

定理 1.3.3 (Cochran 定理) 设  $X_{1}, X_{2}, \cdots, X_{n}$  相互独立，且  $X_{i} \sim N(\mu_{i}, \sigma^{2})$ ， $i = 1, 2, \cdots, n$ ，令  $\boldsymbol{X} = (X_{1}, X_{2}, \cdots, X_{n})^{\mathrm{T}}$ 。又设  $A_{1}, A_{2}, \cdots, A_{m}$  是 m 个 n 阶非负定矩阵，且  $A_{1} + A_{2} + \cdots + A_{m} = I_{n}$ ， $\sum_{i=1}^{m} \operatorname{rank}(A_{i}) = n$  (rank 表示矩阵的秩)。记  $\xi_{i} = X^{T} A_{i} X$ ， $i = 1, 2, \cdots, m$ ， $\boldsymbol{\mu} = (\mu_{1}, \mu_{2}, \cdots, \mu_{n})^{\mathrm{T}}$ 。则

(1)  $\xi_{1}, \xi_{2}, \cdots, \xi_{m}$  相互独立;
(2) 如果  $\mu^{T}A_{1}\mu=0$ ，则  $\xi_{1}/\sigma^{2}\sim\chi^{2}(\mathrm{rank}(A_{1}))$ .

证明 记  $n_{i}=\mathrm{rank}(A_{i}),\;i=1,2,\cdots,m.$  因为  $A_{i}$  是 n 阶非负定矩阵，则存在一个  $n\times n_{i}$  矩阵  $B_{i}$ ，使得  $A_{i}=B_{i}B_{i}^{T}$ . 记  $B=(B_{1}:B_{2}:\cdots:B_{m})$ ，则由已知条件可知 B 是一个 n 阶正交矩阵.

作如下正交变换:

$$
\boldsymbol {Y} = \left( \begin{array}{c} Y _ {1} \\ Y _ {2} \\ \vdots \\ Y _ {n} \end{array} \right) = B ^ {\mathrm{T}} \boldsymbol {X} = \left( \begin{array}{c} B _ {1} ^ {\mathrm{T}} \boldsymbol {X} \\ B _ {2} ^ {\mathrm{T}} \boldsymbol {X} \\ \vdots \\ B _ {m} ^ {\mathrm{T}} \boldsymbol {X} \end{array} \right),
$$

即

$$
B _ {i} ^ {\mathrm{T}} \boldsymbol {X} = \left( \begin{array}{c} Y _ {n _ {1} + \dots + n _ {i - 1} + 1} \\ Y _ {n _ {1} + \dots + n _ {i - 1} + 2} \\ \vdots \\ Y _ {n _ {1} + \dots + n _ {i - 1} + n _ {i}} \end{array} \right), i = 1, 2, \dots , m,
$$

其中  $n_{0}=0$ .

由于 B 是一正交矩阵, 故由引理 1.3.1 知道:  $Y_{1}, Y_{2}, \cdots, Y_{n}$  独立, 且  $Y_{i} \sim N(\beta_{i}, \sigma^{2})$ ,  $i = 1, 2, \cdots, n$ , 其中  $\boldsymbol{\beta} = (\beta_{1}, \beta_{2}, \cdots, \beta_{n})^{\mathrm{T}} = B^{\mathrm{T}}\boldsymbol{\mu}$ .

又因为

$$
\xi_ {i} = \boldsymbol {X} ^ {\mathrm{T}} A _ {i} \boldsymbol {X} = \boldsymbol {X} ^ {\mathrm{T}} B _ {i} B _ {i} ^ {\mathrm{T}} \boldsymbol {X} = (B _ {i} ^ {\mathrm{T}} \boldsymbol {X}) ^ {\mathrm{T}} B _ {i} ^ {\mathrm{T}} \boldsymbol {X} = \sum_ {j = n _ {1} + \dots + n _ {i - 1} + 1} ^ {n _ {1} + \dots + n _ {i - 1} + n _ {i}} Y _ {j} ^ {2}, i = 1, 2, \dots , m,
$$

所以  $\xi_{1},\xi_{2},\cdots,\xi_{m}$  相互独立, 结论 (1) 得证.

下证结论 (2). 由已知条件知, $\pmb{\mu}^{\mathrm{T}}A_{1}\pmb{\mu}=0$, 即 $\pmb{\mu}^{\mathrm{T}}B_{1}B_{1}^{\mathrm{T}}\pmb{\mu}=0$, 于是, $B_{1}^{\mathrm{T}}\pmb{\mu}=\mathbf{0}$, 即 $\beta_{i}=0, i=1,2,\cdots,n_{1}$. 又由于 $\xi_{1}/\sigma^{2}=\sum_{i=1}^{n_{1}}Y_{i}^{2}/\sigma^{2}$, 而 $Y_{1}, Y_{2}, \cdots, Y_{n_{1}} \stackrel{\mathrm{iid}}{\sim} N(0, \sigma^{2})$, 故 $\xi_{1}/\sigma^{2} \sim \chi^{2}(n_{1})$. □

当在定义 1.3.1 中的正态分布的均值不全为零时, 我们有如下的非中心  $\chi^{2}$  分布的定义.

定义 1.3.2 (非中心  $\chi^{2}$  分布) 设  $X_{1}, X_{2}, \cdots, X_{n}$  相互独立，且  $X_{i} \sim N(\mu_{i}, 1)$ ， $\mu_{i}$  不全为零，则称

$$
\xi = \sum_ {i = 1} ^ {n} X _ {i} ^ {2}
$$

为非中心的  $\chi^{2}$  随机变量，称它的分布为非中心  $\chi^{2}$  分布，自由度为 n，非中心参数为  $\delta = \sum_{i=1}^{n} \mu_{i}^{2}$ ，记为  $\xi \sim \chi^{2}(n, \delta)$ .

相较于上述的非中心  $\chi^{2}$  分布, 定义 1.3.1 中的  $\chi^{2}$  也称为中心  $\chi^{2}$  分布.

用类似于定理 1.3.1 的方法, 经过一些复杂计算可求得非中心  $\chi^{2}$  分布的概率密度为

$$
\mathrm{e} ^ {- \delta^ {2} / 2} \sum_ {m = 0} ^ {\infty} \frac {(\delta^ {2} / 2) ^ {m}}{m !} \chi^ {2} (x; 2 m + n),
$$

其中  $\chi^{2}(x;l)$  为  $\chi^{2}(l)$  分布的概率密度. 另外, 非中心  $\chi^{2}$  分布的特征函数为

$$
\psi (t) = (1 - 2 \mathrm{i} t) ^ {- n / 2} \exp \{\mathrm{i} \delta^ {2} t / (1 - 2 \mathrm{i} t) \},
$$

其期望与方差分别为  $n + \delta$  和  $2n + 4\delta$ .

## 1.3.2 t 分布

在 20 世纪初以前, 或更具体地说, 在 1908 年以前, 统计学的主要用武之地是社会统计, 尤其是人口统计, 后来加入生物统计. 在这些领域中, 数据一般都是大量的、自然采集的, 所用方法多以中心极限定理为依据. 但到了 20 世纪, 由人工试验所得数据的统计分析问题, 日渐引人注意. 这个方向的先驱就是 W. S. Gosset (戈塞特, 1876—1937) 和 R. A. Fisher.

1899 年, Gosset 作为一名酿酒师进入爱尔兰都柏林一家啤酒厂工作, 那里涉及有关酿造过程中的数据处理问题. 1906—1907 年, 他到 K. Pearson 那里学习统计学, 并着重研究少量数据的统计分析问题. 1908 年, 他在 Biometrika 上以笔名 Student 发表了论文《均值的或然误差》(The probable error of a mean). 在这篇文章中, 他提出了如下结果: 设 $X_{1}, X_{2}, \cdots, X_{n}$ 是来自 $N(\mu, \sigma^{2})$ 的独立同分布样本, $\mu, \sigma^{2}$ 均未知, 则当 $n$ 比较小时, $\frac{\sqrt{n}(\bar{X} - \mu)}{S_n}$ 并不服从标准正态分布, 而是一个未知分布, 且给出了这个未知分布的一些概率取值. 最早注意到这个小样本均值分布问题的是 R. A. Fisher, 并于 1922 年给出了此未知分布的严格数学定义, 即本小节的 $t$ 分布. 然而, 直到 Gosset 于 1937 年去世, 尚有许多统计学家并不知道他就是 Student. 有兴趣的读者可参见陈希孺 (2000).

定义 1.3.3 (t 分布) 设  $\xi \sim N(0,1)$ ,  $\eta \sim \chi^{2}(n)$ , 且  $\xi, \eta$  相互独立, 则称随机变量

$$
T = \frac {\xi}{\sqrt {\eta / n}}
$$

服从 t 分布, n 为其自由度, 记  $T \sim t(n)$ .

由于 t 分布是由 Student 提出的, 故有时也称之为 Student t 分布, 或学生 t 分布, 其概率密度由下述定理给出.

定理 1.3.4 设  $T \sim t(n)$ ，其概率密度为

$$
f (x) = \frac {\Gamma ((n + 1) / 2)}{\Gamma (n / 2) \sqrt {n \pi}} \left(1 + \frac {x ^ {2}}{n}\right) ^ {- \frac {n + 1}{2}}.
$$

证明 因为 $\xi, \eta$ 相互独立, 所以可知 $\xi, \eta$ 的联合概率密度为

$$
C \mathrm{e} ^ {- x ^ {2} / 2} \mathrm{e} ^ {- y / 2} y ^ {n / 2 - 1},
$$

其中 C 为不依赖于 x, y 的常数, 但与 n 有关.

为求  $\xi/\sqrt{\eta/n}$  的概率密度, 作如下变换:

$$
\left\{ \begin{array}{l l} \xi = R \sin \Theta , & 0 <   R <   \infty , \\ \eta = R ^ {2} \cos^ {2} \Theta , & - \frac {\pi}{2} <   \Theta <   \frac {\pi}{2}, \end{array} \right.
$$

利用概率密度变换公式, 求得  $R, \Theta$  的联合概率密度为

$$
2 C \mathrm{e} ^ {- r ^ {2} / 2} r ^ {n} (\cos \theta) ^ {n - 1}.
$$

利用概率论知识, 由上式可知, R 与  $\Theta$  是相互独立的, 且  $\Theta$  的概率密度为

$$
C _ {1} (\cos \theta) ^ {n - 1}, \tag {*} \tag {*}
$$

其中 $C_1^{-1} = \int_{-\pi /2}^{\pi /2}(\cos \theta)^{n - 1}\mathrm{d}\theta = \frac{\Gamma(1 / 2)\Gamma(n / 2)}{\Gamma((n + 1) / 2)}.$

又由于 $T = \frac{\sin\Theta}{\cos\Theta}\sqrt{n} = \sqrt{n}\tan \Theta$ ，如令 $t = \sqrt{n}\tan \theta$ ，则 $\cos \theta = (1 + t^2 /n)^{-1 / 2},$ $\mathrm{dt} = \sqrt{n}\sec^2\theta \mathrm{d}\theta = \sqrt{n}(1 + t^2 /n)\mathrm{d}\theta ,$ 于是，由 (\*) 式可得到 $t$ 分布的概率密度为

$$
\begin{array}{l} f (t) = C _ {1} \left[ (1 + t ^ {2} / n) ^ {- 1 / 2} \right] ^ {n - 1} \frac {1}{\sqrt {n} (1 + t ^ {2} / n)} \\ = \frac {\Gamma ((n + 1) / 2)}{\Gamma (n / 2) \sqrt {n \pi}} (1 + t ^ {2} / n) ^ {- \frac {n + 1}{2}}. \\ \end{array}
$$

□

图 1.3.2 给出了 n=2,5,50 时 t 分布的概率密度函数曲线. 此图显示

![](images/page_40_chart_3.jpg)

<details>
<summary>line</summary>

| x | f(x)::n=2 | f(x)::n=5 | f(x)::n=50 |
| --- | --- | --- | --- |
| -8 | ~0.00 | ~0.00 | ~0.00 |
| -6 | ~0.01 | ~0.01 | ~0.01 |
| -4 | ~0.03 | ~0.03 | ~0.03 |
| -2 | ~0.12 | ~0.13 | ~0.14 |
| 0 | ~0.35 | ~0.38 | ~0.40 |
| 2 | ~0.12 | ~0.13 | ~0.14 |
| 4 | ~0.03 | ~0.03 | ~0.03 |
| 6 | ~0.01 | ~0.01 | ~0.01 |
| 8 | ~0.00 | ~0.00 | ~0.00 |
</details>

图 1.3.2 t 分布的概率密度函数

- $t(n)$ 的概率密度关于 $y$ 轴对称, 且 $\lim_{|x|\to \infty}f(x) = 0$.
- 随着 $n$ 的增大, 其峰度越来越高, 尾部越来越薄.
- $t$ 分布的概率密度很像标准正态分布的概率密度.

为了区分它与正态分布的差异, 表 1.3.1 列出了标准正态分布、 $t(4)$ 、 $t(10)$  与  $t(50)$  的尾部概率. 从中可以看出, t 分布的尾部概率大于正态分布的相应概率. 但是, 对于固定的 x, 由于

$$
\lim _ {n \to \infty} \left(1 + \frac {x ^ {2}}{n}\right) ^ {- \frac {n + 1}{2}} = \mathrm{e} ^ {- x ^ {2} / 2},
$$

故当 n 很大时, t 分布的概率密度接近于标准正态分布的概率密度, 其常数可用 Stirling(斯特林) 公式:

$$
\Gamma (x) \approx \sqrt {2 \pi} x ^ {x - 1 / 2} \mathrm{e} ^ {- x}
$$

求得.

表 1.3.1 标准正态分布与 $t$ 分布的尾部概率: ${100} \times  P\left( {T > x}\right)$

| x | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N(0,1) | 30.853 7 | 15.865 5 | 6.680 7 | 2.275 0 | 0.620 9 | 0.135 0 | 0.023 3 | 0.003 2 |
| t(4) | 32.166 5 | 18.695 0 | 10.400 0 | 5.805 8 | 3.338 3 | 1.997 1 | 1.244 8 | 0.806 5 |
| t(10) | 31.394 7 | 17.044 6 | 8.225 3 | 3.669 4 | 1.572 3 | 0.667 2 | 0.286 3 | 0.125 9 |
| t(50) | 30.963 4 | 16.106 2 | 6.995 1 | 2.547 3 | 0.787 2 | 0.210 0 | 0.049 4 | 0.010 4 |

注1.3.3 基于 $t$ 分布与标准正态分布概率密度函数的比较，在统计学中，称尾部概率大于正态分布相应尾部概率的分布为厚尾分布 (heavy-tailed distribution). 经济金融等许多行业中的数据多服从厚尾分布.

由上述概率密度函数, 可求得  $t(n)$  分布的  $r(<n)$  阶中心矩为  $(n>1)$ :

$$
E (T ^ {r}) = \left\{ \begin{array}{l l} {{0,}} & {{r \text {是奇数},}} \\ {{n ^ {r / 2} \frac {\Gamma ((r + 1) / 2) \Gamma ((n - r) / 2)}{\Gamma (1 / 2) \Gamma (n / 2)},}} & {{r \text {是偶数}.}} \end{array} \right.
$$

并由此可知: 当 n > 2 时, 其方差为  $n / (n - 2)$ .

基于定理 1.3.2 与上述 t 分布定义, 可以证明: 对于来自  $N(\mu, \sigma^{2})$  的独立同分布样本  $X_{1}, X_{2}, \cdots, X_{n}$ , 有

$$
\frac {\sqrt {n} (\bar {X} - \mu)}{S _ {n}} \sim t (n - 1). \tag {1.3.3}
$$

这即是 Gosset 于 1908 年论文的结论.

定义 1.3.4 (非中心 t 分布) 设  $\xi \sim N(\mu, \sigma^{2})$ ,  $\eta/\sigma^{2} \sim \chi^{2}(n)$ ，且二者独立， $\mu \neq 0$ ，则称

$$
T = \frac {\xi}{\sqrt {\eta / n}}
$$

服从非中心 t 分布, 其非中心参数为  $\delta = \mu / \sigma$ , 自由度为 n.

经过一些复杂计算可求得非中心  $t(n)$  分布的概率密度为

$$
\frac {n ^ {n / 2} \mathrm{e} ^ {- \delta^ {2} / 2}}{\sqrt {\pi} \Gamma (n / 2) (n + x ^ {2}) ^ {(n + 1) / 2}} \sum_ {m = 0} ^ {\infty} \Gamma \left(\frac {n + m + 1}{2}\right) \left(\frac {\delta^ {m}}{m !}\right) \left(\frac {\sqrt {2} x}{\sqrt {n + x ^ {2}}}\right) ^ {m},
$$

其期望与方差分别为

$$
E (T) = \delta \frac {\Gamma ((n - 1) / 2)}{\Gamma (n / 2)} \sqrt {\frac {n}{2}}, n > 1,
$$

$$
\mathrm{Var} (T) = \frac {n (1 + \delta^ {2})}{n - 2} - \frac {\delta^ {2} n}{2} \left(\frac {\Gamma ((n - 1) / 2)}{\Gamma (n / 2)}\right) ^ {2}, n > 2.
$$

## 1.3.3 $F$ 分布

定义 1.3.5 (F 分布) 设  $\xi, \eta$  相互独立, 且服从自由度分别为 m, n 的  $\chi^{2}$  分布. 称

$$
F = \frac {\xi / m}{\eta / n}
$$

服从的分布为 F 分布, 自由度为  $(m, n)$ , 记为  $F \sim F(m, n)$ .

由上述定义知道，

- 如果 $X \sim F(1, n), Y \sim t(n)$, 则 $X$ 与 $Y^2$ 依分布相等.
- 如果 $X \sim F(m, n)$, 且 $m \neq n$, 则 $X^{-1} \sim F(n, m)$.

定理1.3.5 $F(m,n)$ 分布的概率密度为

$$
f (x; m, n) = \left\{ \begin{array}{l l} 0, & x <   0, \\ \frac {\Gamma ((m + n) / 2)}{\Gamma (m / 2) \Gamma (n / 2)} \left(\frac {m}{n}\right) \left(\frac {m x}{n}\right) ^ {m / 2 - 1} \left(1 + \frac {m x}{n}\right) ^ {- (m + n) / 2}, & x \geqslant 0. \end{array} \right.
$$

证明 由于 $\xi \sim \chi^2 (m),\eta \sim \chi^2 (n)$ ，且二者独立，故它们的联合概率密度为

$$
f (x, y) = \frac {1}{2 ^ {(m + n) / 2} \Gamma (m / 2) \Gamma (n / 2)} \mathrm{e} ^ {- (x + y) / 2} x ^ {m / 2 - 1} y ^ {n / 2 - 1}, x \geqslant 0, y \geqslant 0.
$$

作变换

$$
\left\{ \begin{array}{l} u = x + y, \\ v = \frac {x}{y} \frac {n}{m}, \end{array} \right.
$$

则 $(U,V)$ 的联合概率密度为

$$
\begin{array}{l} g (u, v) = \frac {1}{2 ^ {(m + n) / 2} \Gamma (m / 2) \Gamma (n / 2)} \mathrm{e} ^ {- u / 2} u ^ {\frac {m + n}{2} - 2}. \\ \left(\frac {m}{n}\right) ^ {m / 2 - 1} \frac {v ^ {\frac {m}{2} - 1}}{(1 + m v / n) ^ {\frac {m + n}{2} - 1}} \frac {m}{n} \frac {u}{(1 + m v / n) ^ {2}} \\ = \frac {1}{2 ^ {\frac {m + n}{2}} \Gamma ((m + n) / 2)} \mathrm{e} ^ {- u / 2} u ^ {\frac {m + n}{2} - 1}. \\ \frac {\Gamma ((m + n) / 2) (m / n) ^ {m / 2}}{\Gamma (m / 2) \Gamma (n / 2)} \frac {v ^ {\frac {m}{2} - 1}}{(1 + m v / n) ^ {\frac {m + n}{2}}}, \\ \end{array}
$$

由此可知 $U, V$ 相互独立, 且 $U \sim \chi^2(m + n)$, 而第二部分即为 $V$ 的概率密度, 即为所求.

由上面定理的证明, 知如下结论:

推论 1.3.1 设  $\xi \sim \chi^{2}(m)$ ,  $\eta \sim \chi^{2}(n)$ ，且  $\xi$  与  $\eta$  独立，则  $Y = \xi + \eta$  与  $Z = \xi / \eta$  独立.

图 1.3.3 给出了自由度分别为  $(m, n) = (5, 10)$ ,  $(10, 10)$ ,  $(10, 5)$  的 F 分布的概率密度函数曲线.

![](images/page_43_chart_2.jpg)

<details>
<summary>line</summary>

| x | f(x) (Solid Line) | f(x) (Dashed Line) | f(x) (Dash-Dot Line) |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| ~0.5 | ~0.72 | ~0.68 | ~0.65 |
| 1 | ~0.45 | ~0.42 | ~0.40 |
| 2 | ~0.18 | ~0.17 | ~0.16 |
| 3 | ~0.08 | ~0.07 | ~0.06 |
| 4 | ~0.04 | ~0.03 | ~0.02 |
| 5 | ~0.02 | ~0.01 | ~0.01 |
</details>

图1.3.3 $F$ 分布的概率密度函数

由上述概率密度函数可求得 F 分布的数字特征如下: 设  $F \sim F(m, n)$ ，对 0 < r < n/2，有

$$
E (F ^ {r}) = \left(\frac {n}{m}\right) ^ {r} \frac {\Gamma \left(r + \frac {m}{2}\right) \Gamma \left(\frac {n}{2} - r\right)}{\Gamma (m / 2) \Gamma (n / 2)}.
$$

由此求得其期望与方差分别为

$$
E (F) = \frac {n}{n - 2}, n > 2,
$$

$$
\mathrm{Var} (F) = \frac {n ^ {2} (2 m + 2 n - 4)}{m (n - 2) ^ {2} (n - 4)}, n > 4.
$$

定义 1.3.6 (非中心 F 分布) 设  $\xi \sim \chi^{2}(m, \delta)$ ,  $\eta \sim \chi^{2}(n)$ ,  $\delta \neq 0$ , 且  $\xi, \eta$  独立, 则称  $F = \frac{\xi/m}{\eta/n}$  服从非中心 F 分布, 其自由度为  $(m, n)$ , 非中心参数为  $\delta$ .

由于非中心 $F$ 分布的概率密度非常复杂, 且不常用, 故这里就不再给出. 如有兴趣, 请参见复旦大学编著的《概率论》第二册. 这里仅给出其期望与方差:

$$
E (F) = \frac {n (m + \delta)}{m (n - 2)}, n > 2,
$$

$$
\mathrm{Var} (F) = \frac {2 n ^ {2}}{m ^ {2} (n - 2) ^ {2} (n - 4)} \left[ (m + \delta) ^ {2} + (n - 2) (m + 2 \delta) \right], n > 4.
$$

为考察 F 分布是哪个统计量的抽样分布, 假设有两组独立同分布样本:  $X_{1}, X_{2}, \cdots, X_{m}$  来自正态总体  $N(\mu_{1}, \sigma^{2}), Y_{1}, Y_{2}, \cdots, Y_{n}$  来自正态总体  $N(\mu_{2}, \sigma^{2})$ , 且两组样本独立. 如记

$$
\bar {X} = \frac {1}{m} \sum_ {i = 1} ^ {m} X _ {i}, \quad \bar {Y} = \frac {1}{n} \sum_ {i = 1} ^ {n} Y _ {i},
$$

$$
S _ {x} ^ {2} = \frac {1}{m - 1} \sum_ {i = 1} ^ {m} (X _ {i} - \bar {X}) ^ {2}, \quad S _ {y} ^ {2} = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} (Y _ {i} - \bar {Y}) ^ {2},
$$

则由定理 1.3.2 知道,

$$
(m - 1) S _ {x} ^ {2} / \sigma^ {2} \sim \chi^ {2} (m - 1), \quad (n - 1) S _ {y} ^ {2} / \sigma^ {2} \sim \chi^ {2} (n - 1),
$$

由于两组样本独立, 故两组样本方差独立, 于是, 由 F 分布定义可知

$$
\frac {S _ {x} ^ {2}}{S _ {y} ^ {2}} \sim F (m - 1, n - 1). \tag {1.3.4}
$$

## 1.3.4 一些常用分布

在本小节, 我们介绍几个统计经常用到的分布. 为了简单, 我们仅以总体分布的形式给出. 在有的参考文献中, 考虑到一些分布还包含若干常用分布, 故也称之为分布族.

定义 1.3.7 ( $\Gamma$  分布) 称概率密度为

$$
f (x; \alpha , \lambda) = \frac {\lambda^ {\alpha}}{\Gamma (\alpha)} x ^ {\alpha - 1} \mathrm{e} ^ {- \lambda x}, x \geqslant 0 \tag {1.3.5}
$$

的分布为  $\Gamma$  分布, 记为  $\Gamma(\alpha,\lambda)$ , 其中  $\alpha>0$  为形状参数 (shape parameter),  $\lambda>0$  为尺度参数 (scale parameter).

通过比较式(1.3.1)的 $\chi^2 (n)$ 与上述 $\Gamma (\alpha ,\lambda)$ 分布的概率密度函数，可以发现: $\Gamma (n / 2,$ $1 / 2)$ 分布就是 $\chi^2 (n)$ .另外，通过与指数分布(指数分布的定义见本小节最后内容)的比较，我们发现， $\Gamma (1,\lambda)$ 就是指数分布 $Exp(\lambda)$ .再者，之所以称 $\alpha$ 为形状参数，是由于

- 当 $\alpha \leqslant 1$ 时, 其概率密度严格单调下降;
- 当 $1 < \alpha \leqslant 2$ 时, 其概率密度先上凸后下凸, 且拐点为 $\frac{\alpha - 1}{\lambda}$;
- 当 $\alpha > 2$ 时, 其概率密度先下凸, 再上凸, 最后又下凸, 且峰值在 $\frac{\alpha - 1}{\lambda}$ 处达到. 由 $\Gamma$ 分布的概率密度, 可求得 $\xi \sim \Gamma(\alpha, \lambda)$ 分布的特征函数为

$$
\psi (t) = \left(1 - \frac {\mathrm{i} t}{\lambda}\right) ^ {- \alpha},
$$

并由此可以求得其 k 阶矩为

$$
E (\xi^ {k}) = \frac {\Gamma (\alpha + k)}{\Gamma (\alpha)} \frac {1}{\lambda^ {k}},
$$

特别地, 其期望、方差分别为

$$
E (\xi) = \frac {\alpha}{\lambda}, \mathrm{Var} (\xi) = \frac {\alpha}{\lambda^ {2}}.
$$

利用其特征函数, 可以证明:

定理1.3.6 设 $X_{i}\sim \Gamma (\alpha_{i},\lambda),i = 1,2.$

(1) 如 $X_{1}, X_{2}$ 独立, 则 $X_{1} + X_{2} \sim \Gamma(\alpha_{1} + \alpha_{2}, \lambda)$.
(2) 对于给定的正数 $c, cX_{1} \sim \Gamma(\alpha_{1}, \lambda / c)$.

定义 1.3.8 (指数型分布) 称概率分布为

$$
f (x; \boldsymbol {\theta}) = \exp \left\{a _ {0} (\boldsymbol {\theta}) + b _ {0} (x) + \sum_ {i = 1} ^ {q} c _ {i} (\boldsymbol {\theta}) b _ {i} (x) \right\} \tag {1.3.6}
$$

的分布为指数型分布, 其中  $\theta \in \Theta \subset R^{q}$  为参数, 且要求其支撑集  $S = \{x : f(x; \theta) > 0\}$  与  $\theta$  无关. 如定义  $\eta_{i} = c_{i}(\theta)(i = 1, 2, \cdots, q)$ , 则称  $(\eta_{1}, \eta_{2}, \cdots, \eta_{q})$  为自然参数,  $G = \{(\eta_{1}, \eta_{2}, \cdots, \eta_{q}) : \eta_{i} = c_{i}(\theta), \theta \in \Theta\}$  为自然参数空间.

例 1.3.1 设  $X \sim B(1, p)$ ，其中  $p \in (0, 1)$  为参数，验证它服从指数型分布.

证明 此时 $X$ 的概率分布函数为

$$
f (x; p) = P (X = x) = p ^ {x} (1 - p) ^ {1 - x}, \quad x = 0, 1.
$$

我们可以改写上式为

$$
f (x; p) = \left(\frac {p}{1 - p}\right) ^ {x} (1 - p) = \exp \left\{\ln (1 - p) + x \ln \frac {p}{1 - p} \right\},
$$

故可知, 两点分布是指数型分布. 如取 $\theta = \ln[p / (1 - p)]$, 则上式为

$$
f (x; \theta) = \exp \left\{\ln \frac {1}{1 + \mathrm{e} ^ {\theta}} + \theta x \right\},
$$

其自然参数空间为  $G = R$ .

![](images/page_45_image_17.jpg)

例 1.3.2 设  $X \sim N(\mu, \sigma^{2})$ ，验证其为指数型分布.

证明 此时 X 的概率密度为

$$
\begin{array}{l} f (x; \mu , \sigma^ {2}) = (2 \pi \sigma^ {2}) ^ {- \frac {1}{2}} \exp \left\{- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}} \right\} \\ = (2 \pi \sigma^ {2}) ^ {- \frac {1}{2}} \exp \left\{- \frac {x ^ {2}}{2 \sigma^ {2}} + \frac {x \mu}{\sigma^ {2}} - \frac {\mu^ {2}}{2 \sigma^ {2}} \right\} \\ = \exp \left\{- \frac {1}{2} \ln (2 \pi \sigma^ {2}) - \frac {\mu^ {2}}{2 \sigma^ {2}} - \frac {x ^ {2}}{2 \sigma^ {2}} + \frac {x \mu}{\sigma^ {2}} \right\}, \\ \end{array}
$$

由此可知, 正态分布是指数型分布. 如取 $\eta_1 = -1 / (2\sigma^2), \eta_2 = \mu / \sigma^2$, 则其自然参数空间为 $\mathcal{G} = \{(\eta_1, \eta_2) : \eta_1 < 0, \eta_2 \in \mathbb{R}\}$.

定义 1.3.9(次 Gauss 分布) 称 X 服从参数为  $\sigma > 0$  的次 Gauss 分布 (sub-Gauss), 是指满足

$$
E [ \mathrm{e} ^ {t [ X - E (X) ]} ] \leqslant \mathrm{e} ^ {t ^ {2} \sigma^ {2} / 2}, \forall t \in \mathbb {R}.
$$

如果 $X$ 服从均值为0、参数为 $\sigma$ 的次Gauss分布，则

$$
P (X > t) \leqslant \exp \left\{- \frac {t ^ {2}}{2 \sigma^ {2}} \right\}, \forall t > 0.
$$

实际上，

$$
P (X > t) = P \left(\mathrm{e} ^ {t X / \sigma^ {2}} > \mathrm{e} ^ {t ^ {2} / \sigma^ {2}}\right) \leqslant \frac {E [ \exp \{t X / \sigma^ {2} \} ]}{\exp \{t ^ {2} / \sigma^ {2} \}} \leqslant \exp \left\{- \frac {t ^ {2}}{2 \sigma^ {2}} \right\}.
$$

为什么称上述分布为次 Gauss 分布？原因如下:设 $X \sim N(0, \sigma^2)$，则对于任意的 $t > 0$，有

$$
P (X > t) = \frac {1}{\sqrt {2 \pi \sigma^ {2}}} \int_ {t} ^ {\infty} \mathrm{e} ^ {- \frac {x ^ {2}}{2 \sigma^ {2}}} \mathrm{d} x \leqslant \exp \left\{- \frac {t ^ {2}}{2 \sigma^ {2}} \right\}.
$$

关于次 Gauss 分布, 我们有如下结论:

定理 1.3.7 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自均值为 0、参数为  $\sigma$  的次 Gauss 分布，则

$$
E \left(\max _ {1 \leqslant i \leqslant n} X _ {i}\right) \leqslant \sigma \sqrt {2 \ln n}, P \left(\max _ {1 \leqslant i \leqslant n} X _ {i} > t\right) \leqslant n \exp \left\{- \frac {t ^ {2}}{2 \sigma^ {2}} \right\}.
$$

证明

$$
\begin{array}{l} E \left(\max _ {1 \leqslant i \leqslant n} X _ {i}\right) = \frac {1}{t} E \left(\ln \mathrm{e} ^ {t \max _ {i} X _ {i}}\right) \leqslant \frac {1}{t} \ln E \left(\mathrm{e} ^ {t \max _ {i} X _ {i}}\right) \quad (\text {Jensen(延森) 不等式}) \\ = \frac {1}{t} \ln E \left(\max _ {i} \mathrm{e} ^ {t X _ {i}}\right) \leqslant \frac {1}{t} \ln \sum_ {i = 1} ^ {n} E (\mathrm{e} ^ {t X _ {i}}) \\ \leqslant \frac {1}{t} \ln \sum_ {i = 1} ^ {n} \mathrm{e} ^ {\sigma^ {2} t ^ {2} / 2} = \frac {\ln n}{t} + \frac {\sigma^ {2} t}{2}, \\ \end{array}
$$

取  $t=\sqrt{(2\ln n)/\sigma^{2}}$  即证明了第一个结论.

另外，

$$
P \left(\max _ {i} X _ {i} > t\right) = P \left(\bigcup_ {i = 1} ^ {n} \{X _ {i} > t \}\right) \leqslant \sum_ {i = 1} ^ {n} P (X _ {i} > t) \leqslant n \mathrm{e} ^ {- \frac {t ^ {2}}{2 \sigma^ {2}}}.
$$

第二个结论得证.

在风险预警及管理中，极值统计量应用最广，并由此产生了统计学的一个研究方向——极值统计.极值统计最早是由 L. H. Tippett（蒂珀特，1902—1985）在 Shirley Institute 做统计分析时提出的.当时，他发现一根棉线的强度取决于最弱一根纤维的强度.为解决此强度的建模问题，他于 1924 年到伦敦大学学院的 Galton 生物统计实验室跟随 K. Pearson 学习，之后发现了一个能联系极值分布与数据分布很简单的方程式，但他无法求解，而猜出了一个答案.后来他求助 R. A. Fisher, Fisher 推导出了 Tippett 的解，还给出了另外两个解.这就是下面的三个极值分布.

为了给出极值分布的一般形式, 先给出分布等价的定义: 两个累积分布函数  $F_{1}, F_{2}$ , 如存在常数 a > 0, b, 使

$$
F _ {1} (a x + b) = F _ {2} (x),
$$

则称两者等价. 另外, 对于极大次序统计量  $X_{(n)}$ , 如果存在两个常数  $c_{n} > 0, b_{n}$ , 使得

$$
c _ {n} X _ {(n)} + b _ {n} \xrightarrow {\mathrm{d}} G (x),
$$

则称  $G(X)$  为极值分布.

定义 1.3.10 (极值分布) 如果  $c_{n}X_{(n)} + b_{n}$  有连续的极限分布  $G(X)$ ，则  $G(x)$  必属于以下三种分布所代表的分布类之一:

(1) I 型: $G(x) = \exp \{-\mathrm{e}^{-x}\}, x \in \mathbb{R}$.
(2) II 型: $G(x) = \exp \{-x^{-\alpha}\} I_{(0,\infty)}(x), \alpha > 0.$
(3) III 型:  $G(x)=\left\{\begin{array}{ll}\exp\{-(-x)^{-\alpha}\},&x<0,\\1,&x\geqslant0,\end{array}\right.\quad\alpha>0.$

例 1.3.3 设总体  $X \sim Exp(1)$ ，求  $X_{(n)}$  的极限分布.

解 由前面讲述的极大次序统计量的分布可知, $X_{(n)}$ 的累积分布为

$$
F (x) = (1 - \mathrm{e} ^ {- x}) ^ {n}.
$$

为求其极限分布, 我们先求其期望. 为此, 记  $Y_{i} = X_{(i)} - X_{(i-1)}, i = 1, 2, \cdots, n$ , 其中  $X_{(0)} = 0$ .

由于  $Y_{1}$  的概率密度为  $ne^{-nx}$ ，故可求得  $E(Y_{1}) = 1/n$ .

由例 1.2.3 知,  $X_{(k)}$  的概率密度为

$$
k \binom {n} {k} (1 - \mathrm{e} ^ {- x}) ^ {k - 1} \mathrm{e} ^ {- (n - k + 1) x}.
$$

由此可求得

$$
E (Y _ {k}) = E [ X _ {(k)} ] - E [ X _ {(k - 1)} ] = \frac {1}{n - k + 1}.
$$

于是， $E[X_{(n)}] = \sum_{k = 1}^{n}E(Y_k) = \sum_{k = 1}^{n}\frac{1}{k}$ ，与 $\ln n$ 同阶.

由于 $X_{(n)} - \ln n$ 的累积分布函数满足

$$
P (X _ {(n)} - \ln n \leqslant t) = (1 - \mathrm{e} ^ {- t - \ln n}) ^ {n} = (1 - \mathrm{e} ^ {- t} / n) ^ {n} \rightarrow \exp \{- \mathrm{e} ^ {- t} \},
$$

故知  $X_{(n)}$  是 I 型极值分布.

□

注1.3.4 陈希孺(2009)给出了 $X_{(n)}$ 服从三种极值分布而要求总体分布所满足的充要条件,请有兴趣的读者参阅.