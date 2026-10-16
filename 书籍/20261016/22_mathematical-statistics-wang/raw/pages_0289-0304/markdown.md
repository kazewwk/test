证明 对于示性函数 $I(X_{i} \leqslant x)$, 其等于 1 若 $X_{i} \leqslant x$, 否则为 0, 由于 $X_{i}$ 是随机变量, 故 $I(X_{i} \leqslant x)$ 也是随机变量, 而且 $P(I(X_{i} \leqslant x) = 1) = P(X_{i} \leqslant x) = F(x)$, 相应地, $P(I(X_{i} \leqslant x) = 0) = P(X_{i} > x) = 1 - F(x)$. 从而,

$$
E [ I (X _ {i} \leqslant x) ] = 1 \cdot F (x) + 0 \cdot [ 1 - F (x) ] = F (x),
$$

$$
\begin{array}{l} \mathrm{Var} [ I (X _ {i} \leqslant x) ] = E [ I (X _ {i} \leqslant x) ] ^ {2} - \{E [ I (X _ {i} \leqslant x) ] \} ^ {2} \\ = F (x) - [ F (x) ] ^ {2} = F (x) [ 1 - F (x) ]. \\ \end{array}
$$

对于独立同分布的  $X_{1}, X_{2}, \cdots, X_{n}, I(X_{i} \leqslant x)$  为两点分布  $B(1, F(x))$  的独立同分布样本。因此，经验分布函数  $F_{n}(x)$  可视为独立同分布的随机变量  $I(X_{i} \leqslant x)$  的样本均值，即  $F_{n}(x) = \frac{1}{n} \sum_{i=1}^{n} I(X_{i} \leqslant x)$ ，则

$$
\begin{array}{l} E [ F _ {n} (x) ] = \frac {1}{n} \sum_ {i = 1} ^ {n} E [ I (X _ {i} \leqslant x) ] = F (x), \\ \mathrm{Var} [ F _ {n} (x) ] = \frac {1}{n ^ {2}} \sum_ {i = 1} ^ {n} \mathrm{Var} [ I (X _ {i} \leqslant x) ] = \frac {1}{n} F (x) [ 1 - F (x) ]. \\ \end{array}
$$

因此, 由 Bernoulli 大数定律可得 $F_{n}(x)$ 依概率收敛于 $F(x)$, 即得 (1). 由于

$$
E [ F _ {n} (x) - F (x) ] ^ {2} = \mathrm{Var} [ F _ {n} (x) ] = \frac {1}{n} F (x) [ 1 - F (x) ] \leqslant \frac {1}{4 n} \longrightarrow 0 (n \rightarrow \infty),
$$

故得 (2). 根据 Borel (博雷尔) 强大数定律, 可得 (3). 根据 De Moivre-Laplace (棣莫弗-拉普拉斯) 中心极限定理, 可得 (4). □

由定理 6.2.1(1) 可进一步地推出对于任意 x，经验分布函数依分布收敛于分布函数，即  $F_{n}(x) \stackrel{F}{\longrightarrow} F(x)$ ， $\forall x \in R$ 。从定理 6.2.1 可知，对于任意给定的实数 x，经验分布函数  $F_{n}(x)$  依分布、依概率、均方、几乎处处收敛于  $F(x)$ 。因此，当 n 充分大时， $F_{n}(x)$  与  $F(x)$  的值，在概率意义下是非常接近的。同时，根据定理 6.2.1(4) 可以构造大样本性质下的置信区间。对于任意点 x，其分布函数  $F(x)$  的一个可能的近似  $1 - \alpha$  置信区间为  $[L_{n}, U_{n}]$ ，其中

$$
\begin{array}{l} L _ {n} = \max \left\{0, F _ {n} (x) - u _ {\alpha / 2} \sqrt {\frac {F _ {n} (x) [ 1 - F _ {n} (x) ]}{n}} \right\}, \tag {6.2.2} \\ U _ {n} = \min \left\{1, F _ {n} (x) - u _ {\alpha / 2} \sqrt {\frac {F _ {n} (x) [ 1 - F _ {n} (x) ]}{n}} \right\}, \\ \end{array}
$$

且 $u_{\alpha /2}$ 为标准正态分布的上 $\alpha /2$ 分位数.这里，渐近标准差中用 $F_{n}(x)$ 代替未知的$F(x)$ ，置信下界与0取大的原因在于经验分布函数不小于0，置信上界与1取小的原因在于经验分布函数不大于1.图6.2.1展示标准正态分布 $N(0,1)$ 的50个随机样本所对应的经验分布函数及其近似 $95\%$ 置信区间, 其中窄的近似置信区间是用渐近正态性得到的, 宽的是用后面的定理6.2.4得到的. 从中可见, 经验分布函数在已有的数据点上有个跳跃, 其跳跃高度为 $1 / n$. 用渐近正态性得到的近似置信区间在部分 $x$ 处并没有包含真值, 而宽的没有这个问题.

![](images/page_289_chart_3.jpg)

<details>
<summary>line</summary>

| x | 经验分布函数 | 正态分布函数 | 置信下限 | 置信上限 | 置信下限2 | 置信上限2 |
| --- | --- | --- | --- | --- | --- | --- |
| -3 | 0 | 0 | — | — | — | — |
| -2.5 | ~0.01 | ~0.01 | ~0.06 | ~0.21 | ~0.01 | ~0.21 |
| -2 | ~0.04 | ~0.04 | ~0.13 | ~0.25 | ~0.01 | ~0.25 |
| -1.5 | ~0.07 | ~0.07 | ~0.13 | ~0.25 | ~0.01 | ~0.25 |
| -1 | ~0.08 | ~0.13 | ~0.13 | ~0.27 | ~0.01 | ~0.27 |
| -0.5 | ~0.16 | ~0.23 | ~0.16 | ~0.35 | ~0.01 | ~0.35 |
| 0 | ~0.45 | ~0.45 | ~0.45 | ~0.65 | ~0.25 | ~0.65 |
| 0.5 | ~0.72 | ~0.65 | ~0.65 | ~0.92 | ~0.55 | ~0.92 |
| 1 | ~0.82 | ~0.82 | ~0.82 | 1.0 | ~0.65 | 1.0 |
| 1.5 | ~0.91 | ~0.91 | ~0.91 | 1.0 | ~0.72 | 1.0 |
| 2 | ~0.98 | ~0.98 | ~0.98 | 1.0 | ~0.78 | 1.0 |
| 2.5 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| 3 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
</details>

图 6.2.1 标准正态分布的经验分布函数及其置信区间

下一定理进一步给出了经验分布函数和分布函数之间的接近程度的大样本度量.

定理 6.2.2 (Glivenko-Cantelli (格利文科-坎泰利) 定理) 对于任意给定的正整数 n, 设  $X_{1}, X_{2}, \cdots, X_{n}$  为取自总体分布  $F(x)$  的独立同分布样本,  $F_{n}(x)$  为其经验分布函数, 记

$$
D _ {n} = \sup _ {x} | F _ {n} (x) - F (x) |,
$$

则有 $P\left(\lim_{n\to \infty}D_n = 0\right) = 1.$

证明 将 x 取值分段. 对任意正整数 r, 取  $x_{r,k}$  为满足下述不等式的最小 x:

$$
F (x - 0) \leqslant \frac {k}{r} \leqslant F (x) = F (x + 0), k = 1, 2, \dots , r. \tag {6.2.3}
$$

由定理 6.2.1(3) 的强大数定律可知

$$
P \left(\lim _ {n \to \infty} F _ {n} \left(x _ {r, k}\right) = F \left(x _ {r, k}\right)\right) = 1.
$$

类似地, 考虑示性函数并结合定理 6.2.1 的证明思路, 可得

$$
P \left(\lim _ {n \to \infty} F _ {n} \left(x _ {r, k} - 0\right) = F \left(x _ {r, k} - 0\right)\right) = 1.
$$

下面构造概率为 1 的事件 A, 使其包含所证的事件. 令

$$
A _ {k} ^ {r} = \left\{\lim _ {n \to \infty} F _ {n} \left(x _ {r, k}\right) = F \left(x _ {r, k}\right) \right\} = \left\{\lim _ {n \to \infty} | F _ {n} \left(x _ {r, k}\right) - F \left(x _ {r, k}\right) | = 0 \right\},
$$

$$
\begin{array}{l} B _ {k} ^ {r} = \left\{\lim _ {n \to \infty} F _ {n} \left(x _ {r, k} - 0\right) = F \left(x _ {r, k} - 0\right) \right\} \\ = \left\{\lim _ {n \to \infty} \left| F _ {n} \left(x _ {r, k} - 0\right) - F \left(x _ {r, k} - 0\right) \right| = 0 \right\}, \\ A ^ {r} = \bigcap_ {k = 1} ^ {r} \left(A _ {k} ^ {r} \bigcap B _ {k} ^ {r}\right) \\ = \Big \{\lim _ {n \to \infty} \max _ {1 \leqslant k \leqslant r} \left\{\max \{| F _ {n} (x _ {r, k}) - F (x _ {r, k}) |, | F _ {n} (x _ {r, k} - 0) - F (x _ {r, k} - 0) | \} \right\} = 0 \Big \}, \\ A = \bigcap_ {r = 1} ^ {\infty} A ^ {r}. \\ \end{array}
$$

由强大数定律, 有 $P(A_k^r) = P(B_k^r) = 1$. 根据和事件概率小于各事件概率之和, 可得

$$
P (\overline {{A ^ {r}}}) = P \left(\bigcup_ {k = 1} ^ {r} (\overline {{A _ {k} ^ {r}}} \cup \overline {{B _ {k} ^ {r}}})\right) \leqslant \sum_ {k = 1} ^ {r} [ P (\overline {{A _ {k} ^ {r}}}) + P (\overline {{B _ {k} ^ {r}}}) ] = 0,
$$

其中 $\overline{A^r}$ 表示事件 $A^r$ 的补事件. 从而

$$
\begin{array}{l} P (\bar {A}) = P \left(\bigcup_ {r = 1} ^ {\infty} \overline {{A ^ {r}}}\right) = P \left(\lim _ {n \to \infty} \bigcup_ {r = 1} ^ {n} \overline {{A ^ {r}}}\right) \\ = \lim _ {n \to \infty} P \left(\bigcup_ {r = 1} ^ {n} \overline {{A ^ {r}}}\right) \leqslant \lim _ {n \to \infty} \sum_ {r = 1} ^ {n} P (\overline {{A ^ {r}}}) = 0, \\ \end{array}
$$

即得事件 A 的概率为 1. 下面说明 A 包含所证的事件. 根据经验分布函数与总体分布函数的非降性质, 对满足  $x_{r,k} \leqslant x < x_{r,k+1}(k = 1, 2, \cdots, r-1)$  的 x 有如下不等式成立:

$$
F _ {n} \left(x _ {r, k}\right) \leqslant F _ {n} (x) \leqslant F _ {n} \left(x _ {r, k + 1} - 0\right),
$$

$$
F \left(x _ {r, k}\right) \leqslant F (x) \leqslant F \left(x _ {r, k + 1} - 0\right).
$$

因此, 由 (6.2.3) 式可知, 当  $k = 1, 2, \cdots, r - 1$  时,

$$
\begin{array}{l} F _ {n} (x) - F (x) \leqslant F _ {n} \left(x _ {r, k + 1} - 0\right) - F \left(x _ {r, k}\right) \\ = F _ {n} \left(x _ {r, k + 1} - 0\right) - F \left(x _ {r, k + 1} - 0\right) + F \left(x _ {r, k + 1} - 0\right) - F \left(x _ {r, k}\right) \\ \leqslant \max _ {k} \left| F _ {n} \left(x _ {r, k} - 0\right) - F \left(x _ {r, k} - 0\right) \right| + \frac {1}{r}. \\ \end{array}
$$

类似地

$$
\begin{array}{l} F (x) - F _ {n} (x) \leqslant F \left(x _ {r, k + 1} - 0\right) - F _ {n} \left(x _ {r, k}\right) \\ = F \left(x _ {r, k + 1} - 0\right) - F \left(x _ {r, k}\right) + F \left(x _ {r, k}\right) - F _ {n} \left(x _ {r, k}\right) \\ \leqslant \frac {1}{r} + \max _ {k} \left| F \left(x _ {r, k}\right) - F _ {n} \left(x _ {r, k}\right) \right|. \\ \end{array}
$$

此外, 当 k=0, r 时也有类似的式子成立, 从而得到

$$
\begin{array}{l} \sup _ {x \in \mathbb {R}} | F _ {n} (x) - F (x) | \\ \leqslant \max _ {1 \leqslant k \leqslant r} \left\{\max \left\{| F _ {n} \left(x _ {r, k} - 0\right) - F \left(x _ {r, k} - 0\right) |, | F _ {n} \left(x _ {r, k}\right) - F \left(x _ {r, k}\right) | \right\} \right\} + \frac {1}{r}. \\ \end{array}
$$

由于当事件 A 发生时, 事件  $A^{T}$  发生, 因此

$$
\begin{array}{l} \lim _ {n \to \infty} \sup _ {x \in \mathbb {R}} | F _ {n} (x) - F (x) | \\ \leqslant \lim _ {n \to \infty} \max _ {1 \leqslant k \leqslant r} \{\max \{| F _ {n} (x _ {r, k} - 0) - F (x _ {r, k} - 0) |, | F _ {n} (x _ {r, k}) - F (x _ {r, k}) | \} \} + \frac {1}{r} \\ = 0 + \frac {1}{r}. \\ \end{array}
$$

令 $r$ 趋于无穷, 则事件 $\lim_{n\to \infty}\sup_{x\in \mathbb{R}}|F_n(x) - F(x)|$ 发生的概率为0, 因此事件 $A$ 包含所证事件, 定理证毕. □

Glivenko-Cantelli 定理由 Glivenko (1933) 证明了 $F$ 为连续的情况, Cantelli (1933) 证明了 $F$ 为一般的情况. $D_{n}$ 实际上是下一节中讨论的 Kolmogorov-Smirnov (科尔莫戈罗夫-斯米尔诺夫) 检验统计量, 其在非参数检验中有重要应用. 特别地, 当总体分布为均匀分布时, $D_{n}$ 变为星偏差这一种特殊的均匀性度量. 星偏差在高维积分的近似计算以及均匀试验设计等方面都有重要应用, 详细讨论参见 Fang et al. (2018).

此外, Kolmogorov (1933) 给出了 $D_{n}$ 在一维且连续时的极限分布; Dvoretzky et al. (1956) 给出 $D_{n}$ 的取值范围, Massart (1990) 进一步地明确了 $D_{n}$ 的取值范围. 下面不加证明地给出他们的结论.

定理 6.2.3 (Kolmogorov) 当 F 为一维且连续时, 有

$$
\lim _ {n \to \infty} P (\sqrt {n} D _ {n} \leqslant d) = 1 - 2 \sum_ {j = 1} ^ {\infty} (- 1) ^ {j + 1} \exp \{- 2 j ^ {2} d ^ {2} \}, \forall d > 0.
$$

定理 6.2.4 (Dvoretzky, Kiefer, Wolfowitz) 对于独立同分布样本  $X_{1}, X_{2}, \cdots, X_{n}$ ，存在一个不依赖于分布函数 F 的正常数 C，使得

$$
P (D _ {n} > d) \leqslant C \mathrm{e} ^ {- 2 n d ^ {2}}, \forall d > 0.
$$

进一步地, Massart 证明了

$$
P (D _ {n} > d) \leqslant 2 \mathrm{e} ^ {- 2 n d ^ {2}}, \forall d > 0.
$$

定理 6.2.4 给出的结论并不是极限性质, 而是直接对  $D_{n}$  的取值进行讨论, 这个不等式形式简单, 并给出经验分布函数关于 x 一致的概率上界, 且其是指数衰减的. 由定理 6.2.4, 可构造  $F(x)$  的另一种置信区间. 只需令  $\alpha = 2e^{-2nd^{2}}$ , 反解出

$$
d = \sqrt {\frac {\ln \left(\frac {2}{\alpha}\right)}{2 n}}.
$$

因此, 对于任意 $x, F(x)$ 的一个近似 $1 - \alpha$ 置信区间为

$$
\left[ \max \left\{0, F _ {n} (x) - \sqrt {\frac {\ln \left(\frac {2}{\alpha}\right)}{2 n}} \right\}, \min \left\{1, F _ {n} (x) + \sqrt {\frac {\ln \left(\frac {2}{\alpha}\right)}{2 n}} \right\} \right]. \tag {6.2.4}
$$

根据 $D_{n}$ 的定义, $F(x)$ 落入上面置信区间的概率不小于 $1 - \alpha$. 而 (6.2.2) 式给出的近似置信区间并不能保证 $F(x)$ 落入的概率不小于 $1 - \alpha$. 因此, (6.2.4) 式给出的置信区间往往比 (6.2.2) 式给出的要宽, 也更合理.

## 6.2.2 替代原理

参数统计中, 常需要估计与总体分布 $F$ 有关的参数, 例如均值、方差、中位数等. 这些参数是从总体分布函数 $F$ 出发而得到的, 也可以看成定义在某分布函数空间取值为实数的泛函 $T(F)$, 称 $F$ 为函数参数 (functional parameter), 其为某个随机变量的分布函数. 所谓的泛函, 简单地说, 就是以函数为自变量的函数.

例 6.2.1 对于分布函数为 F 的随机变量,

均值: $\mu = T(F) = \int_{-\infty}^{\infty} x \mathrm{d}F(x)$,

方差: $\sigma^2 = T(F) = \int_{-\infty}^{\infty} x^2 \mathrm{d}F(x) - \left[\int_{-\infty}^{\infty} x \mathrm{d}F(x)\right]^2$,

中位数:  $\mathrm{med}(F)=T(F)=F^{-1}(0.5)=\inf\{x:F(x)\geqslant1/2\}$ ,

密度: $f(x) = T(F) = F'(x)$,

其中 $\inf \{x:F(x)\geqslant 1 / 2\}$ 表示满足条件 $F(x)\geqslant 1 / 2$ 的最小的 $x$ ，在均值、方差和中位数的定义中， $F(x)$ 可以是任意类型的随机变量的分布函数.当随机变量为连续型时，存在密度函数 $f(x)$ ，则 $\mathrm{d}F(x) = f(x)\mathrm{d}x$ ，相应的均值 $\mu = E(X) = \int_{-\infty}^{\infty}xf(x)\mathrm{d}x$ ，方差 $\sigma^2 = E(X^2) - [E(X)]^2 = \int_{-\infty}^{\infty}x^2 f(x)\mathrm{d}x - \left[\int_{-\infty}^{\infty}xf(x)\mathrm{d}x\right]^2$ 当随机变量为离散型时，其相应的分布函数即退化为(6.2.1）式的经验分布函数，则对于离散总体的样本

$$
x _ {1}, x _ {2}, \dots , x _ {n},
$$

$$
\int_ {- \infty} ^ {\infty} x \mathrm{d} F (x) = \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i}, \quad \int_ {- \infty} ^ {\infty} x ^ {2} \mathrm{d} F (x) = \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} ^ {2},
$$

因为微分 $\mathrm{d}F(x)$ 只有在 $x_{i}$ 处才有取值 $\frac{1}{n}$, 其余的地方都为0.

设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自分布函数为  $F(x)$  的总体的独立同分布样本, F 或者完全未知或者依赖于某些有限参数. 现在考虑参数  $\theta = T(F)$  的估计问题. 由于  $T(F)$  为 F 的泛函, 因此启示  $\theta$  的估计可以分两步: 先找到 F 的一个好的估计  $\hat{F}$ , 然后用  $\hat{\theta} = T(\hat{F})$  来估计  $\theta = T(F)$ . 这种用  $\hat{F}$  代替 F 得到  $\theta$  的估计方法称为替代原理. 替代原理有两个基本问题:

(1) 怎样估计 F?
(2) 替代原理能否得到好的估计  $\hat{\theta}$ ?

根据前一小节的讨论可知, 经验分布函数  $F_{n}(x)$  是总体分布函数 F 一个较好的估计. 由于  $F_{n}(x)$  是一个阶梯函数, 有时  $F_{n}(x)$  并不适合来估计 F, 例如对于密度函数  $f(x)$  的估计, 不能由  $F_{n}(x)$  求导而得到. 对于密度函数, 可用 6.1 节的核密度估计方法来估计. 不过对于很多情形, 用  $F_{n}(x)$  来估计 F 后, 可以得到  $\theta$  较好的估计  $\hat{\theta}$ .

例 6.2.2 设总体 X 的分布为  $F(x)$ ,  $X_{1}, X_{2}, \cdots, X_{n}$  是其独立同分布样本. 待估参数  $\theta = T(F) = E[h(X)] = \int_{-\infty}^{\infty} h(x) \mathrm{d}F(x)$ . 用经验分布函数  $F_{n}(x)$  代替 F 后, 可得

$$
\hat {\theta} = T (F _ {n}) = \int_ {- \infty} ^ {\infty} h (x) \mathrm{d} F _ {n} (x) = \frac {1}{n} \sum_ {i = 1} ^ {n} h (X _ {i}),
$$

即用  $h(X_{1}), h(X_{2}), \cdots, h(X_{n})$  的样本均值来估计  $E[h(X)]$ . 这里  $h(x)$  可取  $x^{k}, k \geqslant 1$ ，或其他函数. 通过替代原理，可得总体 k 阶矩  $E(X^{k})$  的估计为样本 k 阶原点矩  $a_{k} = \frac{1}{n} \sum_{i=1}^{n} X_{i}^{k}, k \geqslant 1$ .

此外, 对于方差  $\sigma^{2}=T(F)$ , 应用替代原理可得其估计为

$$
\hat {\theta} = T (F _ {n}) = \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i}\right) ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) ^ {2},
$$

其中  $\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_{i}$  为样本均值.

例6.2.3 替代原理也可以应用于参数 $\theta = T(F)$ 不是显式形式的情形. 设 $X \sim F$, $\theta$ 满足 $\int_{-\infty}^{\infty} g(x; \theta) \mathrm{d}F(x) = 0$, 即 $E[g(X; \theta)] = 0$. 则由替代原理, 估计 $\hat{\theta} = T(F_n)$ 满足

$$
\int_ {- \infty} ^ {\infty} g \left(x; T \left(F _ {n}\right)\right) \mathrm{d} F _ {n} (x) = \frac {1}{n} \sum_ {i = 1} ^ {n} g (X _ {i}; \hat {\theta}) = 0.
$$

由上式求得  $\hat{\theta}$  即可.

进一步地, 可以利用替代原理去估计参数统计模型中的未知参数. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为总体  $X \sim F_{\theta}(x)$  的独立同分布样本, 其中  $\theta = (\theta_{1}, \theta_{2}, \cdots, \theta_{p})^{\mathrm{T}}$  为 p 个总体参数. 为用替代原理, 找关于 F 且依赖  $\theta$  的 p 个泛函  $\eta_{1}(F), \eta_{2}(F), \cdots, \eta_{p}(F)$ , 即  $\eta_{k}(F) = g_{k}(\theta), k = 1, 2, \cdots, p$ , 其中  $g_{1}, g_{2}, \cdots, g_{p}$  为已知函数. 这样给定  $\eta_{1}(F), \eta_{2}(F), \cdots, \eta_{p}(F)$ , 由 p 个方程可求解出  $\theta$ . 利用替代原理, 先找 F 的估计  $F_{n}$ , 定义  $\theta$  的估计为  $\hat{\theta}$  满足

$$
\eta_ {k} (F _ {n}) = g _ {k} (\hat {\theta}), \quad k = 1, 2, \dots , p.
$$

对于给定的  $\eta_{k}(F)$ ，相应的  $\eta_{k}(F_{n})$  的形式往往已知， $k=1,2,\cdots,p$ 。由此，可根据这 p 个方程解得  $\theta$  的估计  $\hat{\theta}$ 。选取  $\eta_{k}(F)$  的一个通常做法是取

$$
\eta_ {k} (F) = \int_ {- \infty} ^ {\infty} x ^ {k} \mathrm{d} F _ {\theta} (x) = E (X ^ {k}), k = 1, 2, \dots , p.
$$

此时, 根据替代原理可知, $\theta$ 的估计 $\hat{\theta}$ 满足

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {k} = g _ {k} (\hat {\theta}), \quad k = 1, 2, \dots , p.
$$

从而可得估计  $\hat{\theta}$ . 上述估计总体参数  $\theta$  的做法即为矩估计方法. 因此, 矩估计可以认为是替代原理的一种应用.

## 6.3 拟合优度检验

在参数统计中，往往假设样本服从特定的概率分布，如正态分布、对数正态分布、Poisson分布或其他分布，并基于分布假设导出许多统计检验和方法。例如，$t$ 检验和方差分析假设样本来自正态总体。然而，首先需要检验来自某个特定分布的假设是否成立，即检验样本分布是否与假设分布一致。所谓的拟合优度检验(goodness of fit test)是确定样本数据与分布之间的差异是否具有统计学意义。下面分别介绍对于离散数据和连续数据的拟合优度检验方法。

## 6.3.1 分类数据的  $\chi^{2}$  拟合优度检验

对于分类数据或离散总体的情形, K. Pearson 提出了  $\chi^{2}$  拟合优度检验方法, 其为现代统计学的奠基性工作之一. 先看一个在生物中很有名的例子.

例 6.3.1 在 19 世纪, Mendel 按颜色与形状把豌豆分为四类: 黄圆、青圆、黄皱和青皱. 在 Mendel 观测的 556 颗豌豆中, 这四类豌豆的颗数分别为 315, 108, 101, 32. 于是, Mendel 判断这四类的比例为 9:3:3:1. 请问这个比例符合遗传规律吗?

上一例子是关于分类数据的检验问题. 更一般地, 根据某项指标, 总体被分成 r 类:  $A_{1}, A_{2}, \cdots, A_{r}$ . 此时, 考虑下面关于各类所占比例的假设:

$$
H _ {0}: \text {第} i \text {类} A _ {i} \text {所占的比例为} p _ {i}, i = 1, 2, \dots , r, \tag {6.3.1}
$$

其中  $\sum_{i=1}^{r}p_{i}=1$ . 记  $X_{1},X_{2},\cdots,X_{n}$  为从此总体抽出的 n 个独立同分布样本, 且以  $n_{i}$  记这 n 个样本中属于  $A_{i}$  的样本个数. 由于当  $H_{0}$  成立时, 在 n 个样本中属于  $A_{i}$  类的 “理论频次” 或 “期望频次” 为  $np_{i}$ , 而我们实际观测到的值为  $n_{i}$ , 因此当  $H_{0}$  成立时,  $n_{i}$  与  $np_{i}$  应相差不大. 于是, K. Pearson 提出用统计量

$$
\chi^ {2} = \sum_ {i = 1} ^ {r} \frac {(n _ {i} - n p _ {i}) ^ {2}}{n p _ {i}} \tag {6.3.2}
$$

来衡量“理论频次”与实际观测频次之间的差别. 式中除以分母  $np_{i}$  是为了标准化, 因为不同的类别所占比例不同. 可以把  $\chi^{2}$  拟合优度检验统计量概括如下:

$$
\chi^ {2} = \sum_ {i = 1} ^ {r} \frac {(O _ {i} - E _ {i}) ^ {2}}{E _ {i}},
$$

其中  $O_{i}, E_{i}$  分别表示观测值和期望值. 对于  $\chi^{2}$  统计量 (6.3.2), 观测频次和理论频次差异越小, 则统计量值越小, 越应接受假设的分布; 观测频次和理论频次差异越大, 则统计量值越大, 越应拒绝假设的分布. 因此, 该检验统计量的拒绝域为  $\{\chi^{2} \geqslant c\}$ .

对于  $\chi^{2}$  统计量 (6.3.2) 的一种自然推广是采用检验统计量  $\sum_{i=1}^{r} c_{ni}(n_{i}-np_{i})^{2}$ . 但只有取  $c_{ni}=1/np_{i}$  时, 上述检验统计量的极限分布总存在且形式最简单 (陈希孺 (2009)).

为了控制上述检验的第一类错误, 必须知道此检验统计量的零分布, 为此, K. Pearson 证明了如下定理.

定理 6.3.1 当  $H_{0}$  成立且  $p_{i}$  均已知时, 有

$$
\chi^ {2} \xrightarrow {\mathrm{d}} \chi^ {2} (r - 1).
$$

证明 当  $H_{0}$  成立时, 由于  $(n_{1}, n_{2}, \cdots, n_{r})$  服从如下的多项分布:

$$
\frac {n !}{n _ {1} ! n _ {2} ! \cdots n _ {r} !} p _ {1} ^ {n _ {1}} p _ {2} ^ {n _ {2}} \dots p _ {r} ^ {n _ {r}},
$$

于是, 当 r = 2 时,  $n_{1} \sim B(n, p_{1})$ , 且

$$
\chi^ {2} = \frac {(n _ {1} - n p _ {1}) ^ {2}}{n p _ {1}} + \frac {(n _ {2} - n p _ {2}) ^ {2}}{n p _ {2}} = \frac {(n _ {1} - n p _ {1}) ^ {2}}{n p _ {1} p _ {2}}.
$$

而由中心极限定理可知，

$$
\frac {n _ {1} - n p _ {1}}{\sqrt {n p _ {1} p _ {2}}} \xrightarrow {\mathrm{d}} N (0, 1),
$$

故 $\chi^2\stackrel {\mathrm{d}}{\to}\chi^2 (1)$ ，即定理结论成立.下证 $r > 2$ 的情形

当 $r > 2$ 时，令

$$
Y _ {i} = \frac {n _ {i} - n p _ {i}}{\sqrt {n p _ {i}}}, i = 1, 2, \dots , r,
$$

于是 $\chi^2 = \sum_{i=1}^{r} Y_i^2$. 因为 $\sum n_i = n, \sum p_i = 1$, 故 $\sum_{i=1}^{r} \sqrt{p_i} Y_i = 0$, 即不同的 $Y_i$ 之间并不独立.

因为 $(n_{1},n_{2},\cdots,n_{r})$ 的特征函数为

$$
\begin{array}{l} \psi (t _ {1}, t _ {2}, \dots , t _ {r}) = E (\exp \{\mathrm{i} t _ {1} n _ {1} + \mathrm{i} t _ {2} n _ {2} + \dots + \mathrm{i} t _ {r} n _ {r} \}) \\ = \sum_ {n _ {1} + n _ {2} + \dots + n _ {r} = n} \frac {n !}{n _ {1} ! n _ {2} ! \cdots n _ {r} !} \left(p _ {1} \mathrm{e} ^ {\mathrm{i} t _ {1}}\right) ^ {n _ {1}} \left(p _ {2} \mathrm{e} ^ {\mathrm{i} t _ {2}}\right) ^ {n _ {2}} \dots \left(p _ {r} \mathrm{e} ^ {\mathrm{i} t _ {r}}\right) ^ {n _ {r}} \\ = \left(\sum_ {k = 1} ^ {r} p _ {k} \mathrm{e} ^ {\mathrm{i} t _ {k}}\right) ^ {n}, \\ \end{array}
$$

所以, $(Y_{1},Y_{2},\cdots,Y_{r})$ 的特征函数为

$$
\begin{array}{l} \psi_ {y} (t _ {1}, t _ {2}, \dots , t _ {r}) = E (\exp \{\mathrm{i} t _ {1} Y _ {1} + \mathrm{i} t _ {2} Y _ {2} + \dots + \mathrm{i} t _ {r} Y _ {r} \}) \\ = E \left(\exp \left\{\mathrm{i} \sum_ {k = 1} ^ {r} \frac {t _ {k} (n _ {k} - n p _ {k})}{\sqrt {n p _ {k}}} \right\}\right) \\ = \exp \left\{- \mathrm{i} \sum_ {k = 1} ^ {r} t _ {k} \sqrt {n p _ {k}} \right\} \left(\sum_ {k = 1} ^ {r} p _ {k} \exp \left\{\frac {\mathrm{i} t _ {k}}{\sqrt {n p _ {k}}} \right\}\right) ^ {n}, \\ \end{array}
$$

两边取对数后得到

$$
\ln [ \psi_ {y} (t _ {1}, t _ {2}, \dots , t _ {r}) ] = - \mathrm{i} \sum_ {k = 1} ^ {r} t _ {k} \sqrt {n p _ {k}} + n \ln \left(\sum_ {k = 1} ^ {r} p _ {k} \exp \left\{\frac {\mathrm{i} t _ {k}}{\sqrt {n p _ {k}}} \right\}\right).
$$

由 Taylor 展开知, $\mathrm{e}^{x} = 1 + x + \frac{x^{2}}{2} + o(x^{2})$, $\ln(1 + x) = x - \frac{x^{2}}{2} + o(x^{2})$, 故对于充分大的 $n$, 有

$$
\exp \left\{\frac {\mathrm{i} t _ {k}}{\sqrt {n p _ {k}}} \right\} = 1 + \frac {\mathrm{i} t _ {k}}{\sqrt {n p _ {k}}} - \frac {t _ {k} ^ {2}}{2 n p _ {k}} + o (n ^ {- 1}),
$$

$$
\sum_ {k = 1} ^ {r} p _ {k} \exp \left\{\frac {\mathrm{i} t _ {k}}{\sqrt {n p _ {k}}} \right\} = 1 + \mathrm{i} \sum_ {k = 1} ^ {r} \frac {t _ {k} \sqrt {p _ {k}}}{\sqrt {n}} - \frac {1}{2 n} \sum_ {k = 1} ^ {r} t _ {k} ^ {2} + o (n ^ {- 1}),
$$

$$
\ln \left(\sum_ {k = 1} ^ {r} p _ {k} \exp \left\{\frac {\mathrm{i} t _ {k}}{\sqrt {n p _ {k}}} \right\}\right) = \mathrm{i} \sum_ {k = 1} ^ {r} \frac {t _ {k} \sqrt {p _ {k}}}{\sqrt {n}} - \frac {1}{2 n} \sum_ {k = 1} ^ {r} t _ {k} ^ {2} - \frac {1}{2} \left(\mathrm{i} \sum_ {k = 1} ^ {r} \frac {t _ {k} \sqrt {p _ {k}}}{\sqrt {n}}\right) ^ {2} + o (n ^ {- 1}),
$$

于是

$$
\ln [ \psi_ {y} (t _ {1}, t _ {2}, \dots , t _ {r}) ] = - \frac {1}{2} \left[ \sum_ {k = 1} ^ {r} t _ {k} ^ {2} - \left(\sum_ {k = 1} ^ {r} t _ {k} \sqrt {p _ {k}}\right) ^ {2} \right] + o (1).
$$

作如下的正交变换:

$$
\left\{ \begin{array}{l} Z _ {k} = \sum_ {j = 1} ^ {r} a _ {k j} Y _ {j}, k = 1, 2, \dots , r - 1, \\ Z _ {r} = \sum_ {j = 1} ^ {r} \sqrt {p _ {j}} Y _ {j}. \end{array} \right.
$$

若再令

$$
\left\{ \begin{array}{l} u _ {k} = \sum_ {j = 1} ^ {r} a _ {k j} t _ {j}, k = 1, 2, \dots , r - 1, \\ u _ {r} = \sum_ {j = 1} ^ {r} \sqrt {p _ {j}} t _ {j}, \end{array} \right.
$$

则

$$
\sum_ {j = 1} ^ {r} t _ {j} ^ {2} - \left(\sum_ {j = 1} ^ {r} t _ {j} \sqrt {p _ {j}}\right) ^ {2} = \sum_ {k = 1} ^ {r - 1} u _ {k} ^ {2},
$$

于是, 当  $n \to \infty$  时,  $(Z_{1}, Z_{2}, \cdots, Z_{r})$  的特征函数为

$$
\lim _ {n \to \infty} \psi_ {z} (u _ {1}, u _ {2}, \dots , u _ {r}) = \exp \left\{- \frac {1}{2} \sum_ {k = 1} ^ {r - 1} u _ {k} ^ {2} \right\},
$$

这是 r-1 个独立的标准正态随机向量的特征函数. 由此可以看出,  $Z_{1}, Z_{2}, \cdots, Z_{r-1}$  是 r-1 个独立的标准正态随机变量,  $Z_{r}$  依概率收敛于 0. 于是可得

$$
\chi^ {2} = \sum_ {k = 1} ^ {r} Y _ {k} ^ {2} = \sum_ {k = 1} ^ {r} Z _ {k} ^ {2} \xrightarrow {\mathrm{d}} \chi^ {2} (r - 1).
$$

于是, 对于假设 (6.3.1), 可以根据其极限分布采取如下的水平近似为  $\alpha$  的显著性检验, 即其拒绝域为

$$
\mathcal {W} = \{\chi^ {2} \geqslant \chi_ {\alpha} ^ {2} (r - 1) \}.
$$

这就是 K. Pearson 最早提出的一个检验方法, 称之为 Pearson  $\chi^{2}$  拟合优度检验.

例 6.3.2 (例 6.3.1 续) 针对给出的数据, 可以做如下的  $\chi^{2}$  拟合优度检验. 注意到, 此时

$$
n = 5 5 6, \quad n _ {1} = 3 1 5, \quad n _ {2} = 1 0 8, \quad n _ {3} = 1 0 1, \quad n _ {4} = 3 2,
$$

待检验的假设为

$$
H _ {0}: p _ {1} = \frac {9}{1 6}, \quad p _ {2} = \frac {3}{1 6}, \quad p _ {3} = \frac {3}{1 6}, \quad p _ {4} = \frac {1}{1 6}.
$$

由于

$$
\chi^ {2} = 0. 4 7 <   7. 8 1 = \chi_ {0. 0 5} ^ {2} (4 - 1),
$$

故在水平 0.05 下, 没有理由拒绝  $H_{0}$ , 即可以认为 Mendel 的结论是可接受的.

Pearson $\chi^2$ 拟合优度检验提供了一种对于分类总体的概率分布的检验方法. 该方法可以应用于检验下面一般的分布假设:

$$
H _ {0}: F (x) = F _ {0} (x), \quad H _ {1}: F (x) \neq F _ {0} (x), \tag {6.3.3}
$$

其中  $F_{0}(x)$  为一个形式及参数均已知的分布函数.  $F_{0}(x)$  可以是连续型分布或离散型分布. 此时, 可以把  $(-\infty, \infty)$  (或样本空间) 分成 r 个互不相交的区间:

$$
(- \infty , \infty) = \bigcup_ {i = 1} ^ {r} I _ {i} = (- \infty , a _ {1}) \cup [ a _ {1}, a _ {2}) \cup \dots \cup [ a _ {r - 1}, \infty),
$$

且记 $n_i$ 为落在第 $i$ 个区间 $I_{i}$ 内的样本个数，再记

$$
\begin{array}{l} p _ {1} = F (a _ {1}), \quad p _ {1 0} = F _ {0} (a _ {1}), \\ p _ {2} = F (a _ {2}) - F (a _ {1}), \quad p _ {2 0} = F _ {0} (a _ {2}) - F _ {0} (a _ {1}), \\ \cdots , \\ \end{array}
$$

$$
p _ {r} = 1 - F (a _ {r - 1}), \quad p _ {r 0} = 1 - F _ {0} (a _ {r - 1}),
$$

则可以利用统计量

$$
\chi^ {2} = \sum_ {i = 1} ^ {r} \frac {(n _ {i} - n p _ {i 0}) ^ {2}}{n p _ {i 0}}
$$

及定理 6.3.1 的结论来检验假设 (6.3.3).

![](images/page_298_image_15.jpg)

注6.3.1 拟合优度检验的分组不能过多或者过少. 在一般情形下, 分点的选取应保证落在每个区间内的样本点个数不小于5, 且总的样本量不应小于30.

![](images/page_298_image_17.jpg)

注6.3.2 通过上面分析, 可以看到, 当 $F_{0}$ 中含有未知参数时, 上述 $\chi^{2}$ 拟合优度检验无法实施.

虽然上述的  $\chi^{2}$  拟合优度检验可以用来检验一般的分布假设 (6.3.3)，但通过上面的分析不难看出，此时检验的假设仅为

$$
H _ {0}: p _ {i} = p _ {i 0}, i = 1, 2, \dots , r
$$

而不是真正想检验的假设 (6.3.3). 上面的假设问题与假设 (6.3.3) 有着一定的区别. 如果分点选得不是很好, $\chi^2$ 拟合优度检验可能会把两个有一定差别的分布检验为没有区别. 例如, 图 6.3.1 给出了两个累积分布函数, 可选取合适的分点, 使得这两个不同的分布在每个区间的概率值是相同的, 从而 Pearson $\chi^2$ 拟合优度检验统计量无法区分这两个分布.

![](images/page_299_chart_3.jpg)

<details>
<summary>line</summary>

| x | F(x) (Step Function) | F(x) (Dashed Curve) |
| --- | --- | --- |
| -3 | 0.01 | ~0.01 |
| -2 | 0.01 | ~0.05 |
| -1.7 | 0.01 | ~0.08 |
| -1.5 | 0.2 | ~0.12 |
| -0.5 | 0.2 | ~0.35 |
| -0.2 | 0.5 | ~0.45 |
| 0.2 | 0.5 | ~0.6 |
| 0.5 | 0.75 | ~0.75 |
| 1.1 | 0.75 | ~0.9 |
| 1.4 | 1.0 | ~0.95 |
| 3 | 1.0 | 1.0 |
</details>

图 6.3.1 针对连续情形的  $\chi^{2}$  拟合优度检验

例 6.3.3 从标准正态分布  $N(0,1)$  中产生 30 个随机样本如下:

| 0.276, | 0.459, | -0.218, | 0.796, | -1.518, | -1.075, | -3.072, | 0.521, | -0.991, | -0.253 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.009, | 0.051, | -0.440, | -0.849, | -0.241, | 0.603, | -1.516, | -0.068, | 0.782, | -1.421 |
| 0.669, | 0.683, | -0.882, | -1.505, | 0.433, | 0.808, | 0.579, | 0.763, | -1.182, | 0.584 |

若将 $-1, -0.5, 0, 0.5, 1$ 作为分点，把 $(-\infty, \infty)$ 分为6部分，则相应的 $p_i$ 分别为0.159, 0.150, 0.191, 0.191, 0.150, 0.159. 得到 $\chi^2$ 拟合优度检验统计量(6.3.2)的取值为11.8842，其大于检验临界值 $\chi_{0.05}^2 (6 - 1) = 11.07$ ，则要拒绝原假设，即认为这批数据不来自标准正态分布.因此，犯了第一类错误.这批数据落入这6个区间的个数分别为7,3,5,4,10,1，这与注6.3.1的第一个要求不符合.出现错误的主要原因是这批数据的分布不太符合标准正态分布.若产生另外30个标准正态分布的随机样本，则很有可能接受原假设.

## 6.3.2 带有未知参数的  $\chi^{2}$  拟合优度检验

在许多实际问题中, 感兴趣的假设可能为

$$
H _ {0}: F (x) = F _ {0} (x; \theta_ {1}, \theta_ {2}, \dots , \theta_ {k}),
$$

其中  $F_{0}(x;\theta_{1},\theta_{2},\cdots,\theta_{k})$  是依赖于 k 个未知参数的形式已知的分布，如一般的正态分布、二项分布、Poisson 分布等。此时，无法计算 (6.3.2) 式的  $\chi^{2}$  统计量。K. Pearson 在其 1900 年的论文中注意到了这个问题，并建议用样本估计未知参数后，再得到  $\hat{p}_{i0}$  的值，之后可利用下面的统计量:

$$
\chi^ {2} = \sum_ {i = 1} ^ {r} \frac {(n _ {i} - n \hat {p} _ {i 0}) ^ {2}}{n \hat {p} _ {i 0}}
$$

作为检验统计量, 且当 $H_0$ 成立及 $n \to \infty$ 时, 仍然成立 $\chi^2 \xrightarrow{\mathrm{d}} \chi^2 (r - 1)$.

但是, Fisher 在 20 世纪 20 年代发现了上述结论是错误的. Fisher 指出, 当  $H_{0}$  成立时, 估计参数后的  $\chi^{2}$  统计量在一定条件下有如下的极限零分布:

$$
\chi^ {2} = \sum_ {i = 1} ^ {r} \frac {(n _ {i} - n \hat {p} _ {i 0}) ^ {2}}{n \hat {p} _ {i 0}} \xrightarrow {\mathrm{d}} \chi^ {2} (r - 1 - k), \tag {6.3.4}
$$

Fisher 还指出, 并不是所有的参数估计都能满足 (6.3.4) 式的要求, 比如一般情况下的矩估计等, 而 MLE 是近似可行的 (请参见陈希孺 (1997)). 故对于此类问题, 将采用 MLE 先估计未知参数, 之后再利用 (6.3.4) 式的结论进行检验.

例 6.3.4 现在某地区随机地抽取 1 000 人, 检查其性别与色盲的数据如下左表所示. 按照遗传学规律, 这些数据具有右表的规律 (其中  $p + q = 1$ ).

性别与色盲的数据

|  | 男 | 女 |
| --- | --- | --- |
| 正常 | 442 | 514 |
| 色盲 | 38 | 6 |

性别与色盲模型

|  | 男 | 女 |
| --- | --- | --- |
| 正常 | $p/2$ | $p^{2}/2 + pq$ |
| 色盲 | $q/2$ | $q^{2}/2$ |

请问这些数据符合遗传学规律吗？ $(\alpha = 0.05)$

解 对于本问题, 所需检验的假设为

$$
H _ {0}: p _ {1} = \frac {p}{2}, \quad p _ {2} = \frac {p ^ {2}}{2} + p q = \frac {p (2 - p)}{2}, \quad p _ {3} = \frac {1 - p}{2}, \quad p _ {4} = \frac {(1 - p) ^ {2}}{2},
$$

其中参数 $p$ 是未知的, 故需要估计. 由于当 $H_0$ 成立时, 数据 (442,514,38,6) 服从一个多项分布, 故其似然函数为

$$
\begin{array}{l} L (p) \propto \left(\frac {p}{2}\right) ^ {4 4 2} \left[ \frac {p (2 - p)}{2} \right] ^ {5 1 4} \left(\frac {1 - p}{2}\right) ^ {3 8} \left[ \frac {(1 - p) ^ {2}}{2} \right] ^ {6} \\ = p ^ {9 5 6} (2 - p) ^ {5 1 4} (1 - p) ^ {5 0} / 2 ^ {1 0 0 0}. \\ \end{array}
$$

于是, 由 $\partial L(p) / \partial p = 0$ 可求得 $p$ 的MLE为 $\hat{p} = 0.91$. 由此可算得 $\chi^2$ 的值为

$$
\chi^ {2} = \sum_ {i = 1} ^ {4} \frac {(n _ {i} - n \hat {p} _ {i}) ^ {2}}{n \hat {p} _ {i}} = 3. 0 5 6 <   5. 9 9 = \chi_ {0. 0 5} ^ {2} (4 - 1 - 1),
$$

因此, 在水平 0.05 下, 没有理由拒绝  $H_{0}$ , 即认为此地区的数据符合遗传学规律.

例 6.3.5 某工厂生产一种滚珠, 现随机地抽取了 50 件产品, 测得其直径为 (单位: mm)

15.0, 15.8, 15.2, 15.1, 15.9, 14.7, 14.8, 15.5, 15.6, 15.3, 15.1, 15.3, 15.0, 15.6,

15.7, 15.8, 14.5, 14.9, 14.9, 15.2, 15.0, 15.3, 15.6, 15.1, 14.9, 14.2, 14.6, 15.8,

15.2, 15.9, 15.2, 15.0, 14.9, 14.8, 15.1, 15.5, 15.5, 15.1, 15.1, 15.0, 15.3, 14.7,

14.5, 15.5, 15.0, 14.7, 14.6, 14.2, 14.2, 14.5

问:滚珠直径是否服从正态分布？ $(\alpha = 0.05)$

解 设滚珠直径为 X, 其分布函数为  $F(x)$ , 现感兴趣的假设为

$$
H _ {0}: F (x) \in \left\{\varPhi \left(\frac {x - \mu}{\sigma}\right): \mu \in \mathbb {R}, \sigma > 0 \right\}.
$$

对于此问题, 首先由数据求得  $\mu, \sigma^{2}$  的 MLE 为  $\hat{\mu} = 15.1, \hat{\sigma}^{2} = 0.4325^{2}$ . 另外, 由于 50 个数据的最小值为 14.2, 最大值为 15.9, 故取分点为

$$
a _ {0} = 1 4. 0 5, a _ {1} = 1 4. 3 5, a _ {2} = 1 4. 6 5, a _ {3} = 1 4. 9 5,
$$

$$
a _ {4} = 1 5. 2 5, a _ {5} = 1 5. 5 5, a _ {6} = 1 5. 8 5, a _ {7} = 1 6. 1 5.
$$

由此, 可利用公式

$$
\hat {p} _ {i} = \varPhi \left(\frac {a _ {i} - 1 5 . 1}{0 . 4 3 2 5}\right) - \varPhi \left(\frac {a _ {i - 1} - 1 5 . 1}{0 . 4 3 2 5}\right), i = 1, 2, \dots , 7,
$$

求得

$$
\hat {p} _ {1} = 0. 0 4 1 4, \hat {p} _ {2} = 0. 1 0 7 7, \hat {p} _ {3} = 0. 2 1 5 4,
$$

$$
\hat {p} _ {4} = 0. 2 7 1 0, \hat {p} _ {5} = 0. 2 1 5 4, \hat {p} _ {6} = 0. 1 0 7 7, \hat {p} _ {7} = 0. 0 4 1 4.
$$

由于

$$
\chi^ {2} = 1. 7 2 8 4 <   9. 4 9 = \chi_ {0. 0 5} ^ {2} (7 - 1 - 2),
$$

故不能拒绝  $H_{0}$ .

![](images/page_301_image_18.jpg)

## 6.3.3 Kolmogorov-Smirnov 检验

前面两小节的  $\chi^{2}$  拟合优度检验是针对离散型数据, 或把连续型分布离散化之后的数据. 然而,  $\chi^{2}$  拟合优度检验具有如图 6.3.1 所示的不足. 因此需要一个直接针对连续型分布的检验统计量. Kolmogorov-Smirnov 检验即可满足要求, 其可以用来很好地检验形如 (6.3.3) 式的假设.

由于样本经验分布函数 $F_{n}(x)$ 是 $F(x)$ 的一个很好的估计，故当(6.3.3)式的 $H_0$ 成立时，$F_{n}(x)$ 与 $F_{0}(x)$ 应相差不大，于是，可以用统计量

$$
D _ {n} = \sup _ {x} | F _ {n} (x) - F _ {0} (x) |
$$

来衡量经验分布函数 $F_{n}(x)$ 与理论分布 $F_{0}(x)$ 之间的差别，且拒绝域为 $\{D_n\geqslant c\}$ ，其中 $c$ 是临界值.此检验是由Kolmogorov(1933)针对单样本提出的，并给出了 $D_{n}$ 的极限零分布，见定理6.2.3.Smirnov(1939)把单样本推广至两样本的情形.因此，称之为Kolmogorov-Smirnov检验.对于单样本的情形， $D_{n}$ 的精确分布见下面的定理

定理6.3.2 如果 $F_{0}(x)$ 连续, 则当 $H_0$ 成立时, 有

$$
P \left(D _ {n} <   \lambda\right) = \left\{ \begin{array}{l l} 0, & \lambda <   \frac {1}{2 n}, \\ n! \prod_ {i = 1} ^ {n} \int_ {\max \left\{0, \frac {n - i + 1}{n} - t \right\}} ^ {\min \left\{u _ {n - i + 2}, \frac {n - i}{n} + t \right\}} \mathrm{d} u _ {1} \mathrm{d} u _ {2} \dots \mathrm{d} u _ {n}, & \frac {1}{2 n} \leqslant \lambda <   1, \\ 1, & \lambda \geqslant 1. \end{array} \right. \tag {6.3.5}
$$

定理 6.3.2 的详细证明可参见陈希孺 (1997). 从中可见,  $D_{n}$  的分布与真实分布  $F_{0}$  无关. 虽然定理 6.2.3 和定理 6.3.2 的结论较复杂, 但是现在已有现成的分位数表可供大家查找.

从 $D_{n}$ 的定义可知, 对于某些连续型分布检验, Kolmogorov-Smirnov 检验优于 $\chi^2$ 拟合优度检验. 但是, 它的计算看起来比较复杂. 然而, 由于 $F(x)$ 及 $F_{n}(x)$ 均是单增的, 且 $F_{n}(x)$ 是一阶梯函数, 于是其上确界仅可能在 $n$ 个点 $x_{(i)}$ 处达到. 如果 $F_{0}$ 连续,

$$
D _ {n} = \max _ {1 \leqslant i \leqslant n} \left\{F _ {0} (x _ {(i)}) - \frac {i - 1}{n}, \quad \frac {i}{n} - F _ {0} (x _ {(i)}) \right\}.
$$

类似地, 如果  $F_{0}$  是右连续的, 则  $D_{n}$  可以写成如下便于计算的公式:

$$
D _ {n} = \max _ {1 \leqslant i \leqslant n} \left\{F _ {0} (x _ {(i)} - 0) - \frac {i - 1}{n}, \quad \frac {i}{n} - F _ {0} (x _ {(i)}) \right\}.
$$

关于前面讲述的两个分布检验方法: $\chi^2$ 拟合优度检验与 Kolmogorov-Smirnov 检验, 有如下几点注解:

注6.3.3 当 $F_{0}$ 为完全已知的连续型分布时，Kolmogorov-Smirnov检验优于 $\chi^2$ 拟合优度检验.但如果 $F_{0}$ 是离散的或含有未知参数，则Kolmogorov-Smirnov检验无法应用.
注6.3.4 当 $F_{0}$ 为含有未知参数的连续型分布时，如用样本去估计未知参数，则定理6.2.3和定理6.3.2的结论均不成立，故此时无法利用Kolmogorov-Smirnov检验，但 $\chi^2$ 拟合优度检验是可以的.
注6.3.5 Kolmogorov检验很难处理高维数据的分布检验，而 $\chi^2$ 拟合优度检验则与一维的类似.

例 6.3.6 问在水平  $\alpha = 0.1$  下是否可以认为下列 10 个数:

$$
0. 4 3 7, 0. 8 6 3, 0. 0 3 4, 0. 9 6 4, 0. 3 6 6, 0. 4 6 9, 0. 6 3 7, 0. 6 2 3, 0. 8 0 4, 0. 2 6 1
$$

来自均匀分布  $U(0,1)$ ?

解 对于此组数据, 为了便于计算, 表 6.3.1 给出了相应的数据, 其中

$$
\delta_ {i} = \max \left\{F _ {0} (x _ {(i)}) - \frac {i - 1}{n}, \frac {i}{n} - F _ {0} (x _ {(i)}) \right\}.
$$

从表 6.3.1 可以看出，本问题的 Kolmogorov-Smirnov 统计量的值为  $D_{n} = 0.166 < 0.3687 = D_{0.1}(10)$ ，故没有理由拒绝  $H_{0}$ ，即可以认为这组数是来自  $U(0,1)$  的样本。☐

表 6.3.1 例 6.3.6 的计算表

| i | $x_{(i)}$ | $F_0(x_{(i)})$ | $\frac{i-1}{n}$ | $\frac{i}{n}$ | $\delta_i$ | i | $x_{(i)}$ | $F_0(x_{(i)})$ | $\frac{i-1}{n}$ | $\frac{i}{n}$ | $\delta_i$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.034 | 0.034 | 0.0 | 0.1 | 0.066 | 6 | 0.623 | 0.623 | 0.5 | 0.6 | 0.123 |
| 2 | 0.261 | 0.261 | 0.1 | 0.2 | 0.161 | 7 | 0.637 | 0.637 | 0.6 | 0.7 | 0.063 |
| 3 | 0.366 | 0.366 | 0.2 | 0.3 | 0.166 | 8 | 0.804 | 0.804 | 0.7 | 0.8 | 0.104 |
| 4 | 0.437 | 0.437 | 0.3 | 0.4 | 0.137 | 9 | 0.863 | 0.863 | 0.8 | 0.9 | 0.063 |
| 5 | 0.469 | 0.469 | 0.4 | 0.5 | 0.069 | 10 | 0.964 | 0.964 | 0.9 | 1.0 | 0.064 |

前面讨论的是单样本的 Kolmogorov-Smirnov 检验, 该结果可以推广至两样本的分布检验, 即检验相互独立的两个总体分布是否相同. 对于两样本分布假设检验问题, 即设  $X_{1}, X_{2}, \cdots, X_{m}$  和  $Y_{1}, Y_{2}, \cdots, Y_{n}$  为分别来自总体 F 和 G 的独立同分布样本, 且全样本独立, 则可以用统计量

$$
D _ {m, n} = \sup _ {x} | F _ {m} (x) - G _ {n} (x) |
$$

进行分布检验, 且拒绝域为  $\{D_{m,n} \geqslant c\}$ , 其中  $F_{m}, G_{n}$  分别表示总体 X, Y 的经验分布函数. 检验统计量  $D_{m,n}$  的极限分布如下:

$$
\lim _ {m, n \to \infty} P (\sqrt {m n / (m + n)} D _ {m, n} \leqslant t) = \sum_ {j = - \infty} ^ {\infty} (- 1) ^ {j - 1} \exp \{- 2 j ^ {2} t ^ {2} \}, t > 0.
$$

根据该极限分布, 有相应的分布表可供查询.

关于 Kolmogorov-Smirnov 检验还有许多更深入的结论, 有兴趣的读者请参见 Serfling(1980) 等有关大样本的书籍. 关于分布检验, 有许多类似于 Kolmogorov-Smirnov 统计量的检验统计量, 如

\- $\sup_{x}|w(x)[F_n(x) - F_0(x)]|$, 其中 $w(x)$ 为给定的权函数.