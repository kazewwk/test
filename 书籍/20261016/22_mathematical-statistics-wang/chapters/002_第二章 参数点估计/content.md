# 第二章 参数点估计

原始 PDF 第 66–123 页。

## 第二章

## 参数点估计

---

54

第二章 参数点估计

参数估计是数理统计研究的重要内容之一, 且在实际中有广泛的应用. 参数估计包括点估计 (point estimate) 和区间 (interval) 估计, 它们各有各的特点与用途, 互为补充. 本章仅考虑点估计, 而区间估计将在下一章中讲述.

参数点估计的主要研究内容包括三个方面, 一是估计方法, 二是优良性准则, 三是渐近分布. 本章将讲述两个最基本的估计方法: 矩估计 (moment estimate) 和最大似然估计 (maximum likelihood estimate, 简记为 MLE), 简单介绍 Bayes 估计及 minimax(极小化极大) 估计, 以及几个优良性准则, 如无偏性、一致最小方差、相合性、有效性、渐近性等.

在本章, 假设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $X \sim f(x; \theta)$  的样本, 其中  $\theta \in \Theta \subset R^{k}$  为参数, 记  $g(\theta)$  为感兴趣的参数. 另外, 为了书写简单, 记  $T_{n}(X)$  为基于前述 n 个样本的统计量, 在不引起混淆的情况下, 省略下标 n 及把样本简记为 X, 从而简记统计量  $T(X_{1}, X_{2}, \cdots, X_{n})$  为  $T(X)$ . 再者,  $E_{\theta}[T(X)], \operatorname{Var}_{\theta}[T(X)], \operatorname{Cov}_{\theta}[T(X), S(X)]$  分别表示统计量 T 的期望、方差, 以及 T 与估计量 S 间的协方差, 下标  $\theta$  表示上述值与参数  $\theta$  有关, 或表示在上述计算时, 总体分布或抽样分布是参数  $\theta$  的函数.

## 2.1 几个常用的估计准则

统计与数学的一个典型区别就是:数学的评价准则是对与错，而统计的评价准则是好与坏。显然，好与坏的评价就依赖于所选用的评价准则。本节将介绍统计中几个最常用的评价准则:无偏、一致最小方差无偏、相合，及相合渐近正态等。

## 2.1.1 无偏估计

当用统计量  $T(X)$  估计参数  $g(\theta)$  时, 自然要求二者相等或相近为好, 但由于样本具有随机性, 于是有如下的无偏估计 (unbiased estimate, 简记为 UE) 的定义.

定义 2.1.1 (无偏估计) 如果统计量  $T(X)$  满足

$$
E _ {\theta} [ T (X) ] = g (\theta), \forall \theta \in \Theta ,
$$

则称之为  $g(\theta)$  的无偏估计.

从期望的定义, 不难理解无偏估计的含义: 虽然一次抽样得到的  $T(X)$  的值不一定等于待估参数  $g(\theta)$ , 但多次重复抽样后, 此统计量的平均值等于待估参数  $g(\theta)$ .

例 2.1.1 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本, 总体均值与总体方差分别为  $\mu, \sigma^{2}$ , 证明样本均值  $\bar{X}$  与样本方差  $S_{n}^{2}$  分别是  $\mu, \sigma^{2}$  的 UE.

---

2.1 几个常用的估计准则

55

证明 对于样本均值, 由于

$$
E (\bar {X}) = \frac {1}{n} \sum_ {i = 1} ^ {n} E (X _ {i}) = \mu ,
$$

故样本均值是总体均值 $\mu$ 的无偏估计. 对于样本方差, 因为

$$
S _ {n} ^ {2} = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) ^ {2} = \frac {1}{n - 1} \left(\sum_ {i = 1} ^ {n} X _ {i} ^ {2} - n \bar {X} ^ {2}\right),
$$

而

$$
E (X _ {i} ^ {2}) = \mathrm{Var} (X _ {i}) + [ E (X) ] ^ {2} = \sigma^ {2} + \mu^ {2}, E (\bar {X} ^ {2}) = \frac {\sigma^ {2}}{n} + \mu^ {2},
$$

则可验证它是总体方差的无偏估计.

例 2.1.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自 Poisson 总体  $P(\lambda)$  的独立同分布样本，记  $p_{\lambda}(k) = \frac{\lambda^{k} e^{-\lambda}}{k!}$ ，其中 k 为给定的正整数，求  $p_{\lambda}(k)$  的 UE.

解 由 $p_{\lambda}(k)$ 的形式知,

$$
p _ {\lambda} (k) = P (X = k),
$$

于是, 可知 $I(X_{1} = k), \frac{1}{n} \sum_{i=1}^{n} I(X_{i} = k)$ 都是 $p_{\lambda}(k)$ 的 UE.

例 2.1.3 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $X \sim P(\lambda)$  的独立同分布样本, 求  $g(\lambda) = \mathrm{e}^{-2\lambda}$  的 UE.

解 取 $T(X) = (-1)^{X_1}$. 由于

$$
E _ {\lambda} [ T (X) ] = \sum_ {k = 0} ^ {\infty} (- 1) ^ {k} \frac {\lambda^ {k}}{k !} \mathrm{e} ^ {- \lambda} = \mathrm{e} ^ {- 2 \lambda},
$$

故  $T(X)$  是  $g(\lambda)$  的一个 UE.

在上例中, 当  $X_{1}$  为奇数时, 一个正参数的无偏估计为负值, 这说明此无偏估计有不合理的时候.

如果参数 $g(\theta)$ 存在无偏估计, 则称其可估, 否则称之不可估. 如果 $T(X)$ 不是 $g(\theta)$ 的无偏估计, 则称之为有偏估计, 且记其偏差 (bias) 为 $b_{T}(\theta) = E[T(X)] - g(\theta)$.

例 2.1.4 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自 Poisson 总体  $P(\lambda)$  的独立同分布样本, 验证参数  $1/\lambda$  是否可估.

解 此时 $1 / \lambda$ 是不可估的. 事实上, 如果存在一个统计量 $T(X)$ 是它的 UE, 则有

$$
E _ {\lambda} [ T (X) ] = \sum_ {k _ {1}, k _ {2}, \dots , k _ {n} = 0} ^ {\infty} T (k _ {1}, k _ {2}, \dots , k _ {n}) \frac {\sum_ {i = 1} ^ {n} k _ {i}}{k _ {1} ! k _ {2} ! \cdots k _ {n} !} \mathrm{e} ^ {- n \lambda} = \frac {1}{\lambda}, \forall \lambda > 0,
$$

---

56

第二章 参数点估计

即

$$
\sum_ {k _ {1}, k _ {2}, \dots , k _ {n} = 0} ^ {\infty} T (k _ {1}, k _ {2}, \dots , k _ {n}) \frac {\sum_ {i = 1} ^ {n} k _ {i}}{k _ {1} ! k _ {2} ! \cdots k _ {n} !} = \frac {\mathrm{e} ^ {n \lambda}}{\lambda} = \frac {1}{\lambda} \sum_ {k = 0} ^ {\infty} \frac {(n \lambda) ^ {k}}{k !}, \forall \lambda > 0.
$$

但由多项式性质可知: 上述等式永远不成立. 于是, 参数  $1/\lambda$  不可估.

由例2.1.1可知，无论总体分布如何，样本均值与样本方差始终是总体均值与总体方差的无偏估计.由此能说样本标准差 $S_{n}$ 是总体标准差 $\sigma$ 的无偏估计吗？

例 2.1.5 设总体  $X \sim N(\mu, \sigma^{2})$ ，验证样本标准差  $S_{n}$  是否为  $\sigma$  的 UE.

解 由于 $(n - 1)S_n^2 /\sigma^2\sim \chi^2 (n - 1)$ ，故

$$
\begin{array}{l} E \left(\sqrt {n - 1} S _ {n} / \sigma\right) = \int_ {0} ^ {\infty} \frac {\sqrt {x}}{2 ^ {(n - 1) / 2} \Gamma ((n - 1) / 2)} \mathrm{e} ^ {- x / 2} x ^ {\frac {n - 1}{2} - 1} \mathrm{d} x \\ = \frac {\sqrt {2} \Gamma (n / 2)}{\Gamma ((n - 1) / 2)}, \\ \end{array}
$$

故

$$
E (S _ {n}) = \sigma \sqrt {\frac {2}{n - 1}} \frac {\Gamma (n / 2)}{\Gamma ((n - 1) / 2)},
$$

所以, 样本标准差不是  $\sigma$  的 UE.

表 2.1.1 列出了  $c_{n}=\sqrt{\frac{2}{n-1}}\frac{\Gamma(n/2)}{\Gamma((n-1)/2)}$  针对不同 n 的取值. 此表显示, 当 n 越来越大时, 样本标准差  $S_{n}$  越来越接近总体标准差  $\sigma$  的无偏估计. 实际上, 利用前述提到的 Stirling 公式, 可以证明  $\lim_{n\to\infty}c_{n}=1$ .

表 2.1.1 例 2.1.5 中 ${c}_{n}$ 的值

| n | 5 | 10 | 100 | 200 |
| --- | --- | --- | --- | --- |
| $c_n$ | 0.940 0 | 0.972 7 | 0.997 5 | 0.998 7 |

定义 2.1.2 如果统计量  $T_{n}(X)$  是  $g(\theta)$  的有偏估计, 但满足

$$
\lim _ {n \to \infty} E _ {\theta} [ T _ {n} (X) ] = g (\theta), \forall \theta \in \Theta ,
$$

则称之为 $g(\theta)$ 的渐近无偏估计.

由上述定义可知, 当总体为正态时, 样本标准差是总体标准差的渐近无偏估计.

综上可知, 不是所有参数都是可估的; 即使参数可估, 也可能存在不合理的无偏估计; 一个可估参数的无偏估计多数情况下不唯一; 无偏估计不具有变换不变性, 即 $T(X)$ 为 $\theta$ 的无偏估计, 但 $H(T)$ 并不一定是 $H(\theta)$ 的无偏估计, 除非 $H$ 为线性函数.

关于无偏估计与充分统计量的关系, 有如下结论:

---

2.1 几个常用的估计准则

57

定理2.1.1 设 $T(X)$ 为充分统计量, $g(\theta)$ 可估, 且 $S(X)$ 为任一无偏估计, 则 $H(T) = E[S(X)|T(X)]$ 是 $g(\theta)$ 的无偏估计, 且

$$
\mathrm{Var} _ {\theta} [ H (T) ] \leqslant \mathrm{Var} _ {\theta} [ S (X) ], \forall \theta \in \Theta , \tag {2.1.1}
$$

其中等号成立的充要条件是 $P(S(X) = H(T)) = 1$

证明 因为 T 是充分统计量, 所以由充分统计量定义知: 在给定 T 时, 样本  $X_{1}, X_{2}, \cdots, X_{n}$  的条件分布与参数  $\theta$  无关. 因此,  $H(T)$  是一统计量. 另外, 由于

$$
E _ {\theta} [ H (T) ] = E _ {\theta} \left\{E [ S (X) | T (X) ] \right\} = E _ {\theta} [ S (X) ] = g (\theta), \forall \theta \in \Theta ,
$$

故  $H(T)$  也是  $g(\theta)$  的一个 UE.

又因为

$$
\begin{array}{l} \mathrm{Var} _ {\theta} [ S (X) ] = E _ {\theta} [ S (X) - g (\theta) ] ^ {2} \\ = E _ {\theta} [ S (X) - H (T) + H (T) - g (\theta) ] ^ {2} \\ = E _ {\theta} [ S (X) - H (T) ] ^ {2} + \\ \mathrm{Var} _ {\theta} [ H (T) ] + 2 E _ {\theta} \{[ S (X) - H (T) ] [ H (T) - g (\theta) ] \}, \\ \end{array}
$$

且

$$
\begin{array}{l} E _ {\theta} \{[ S (X) - H (T) ] [ H (T) - g (\theta) ] \} \\ = E _ {\theta} \{E _ {\theta} \{[ S (X) - H (T) ] [ H (T) - g (\theta) ] | T \} \} \\ = E _ {\theta} \{[ H (T) - g (\theta) ] \cdot E _ {\theta} [ S (X) - H (T) ] | T \} \\ = E _ {\theta} \{[ H (T) - g (\theta) ] \cdot E _ {\theta} \{[ S (X) - H (T) ] | T \} \} \\ = E _ {\theta} \{[ H (T) - g (\theta) ] \cdot \{[ E _ {\theta} S (X) | T ] - H (T) \} \} = 0, \\ \end{array}
$$

故

$$
\mathrm{Var} _ {\theta} [ S (X) ] = E _ {\theta} [ S (X) - H (T) ] ^ {2} + \mathrm{Var} _ {\theta} [ H (T) ] \geqslant \mathrm{Var} _ {\theta} [ H (T) ], \forall \theta \in \Theta ,
$$

且等号成立当且仅当  $E_{\theta}[S(X)-H(T)]^{2}=0$ ，即  $P(S(X)=H(T))=1$ .

注2.1.1 本定理是由C.R.Rao(拉奥,1920—2023)和D.Blackwell(布莱克维尔,1919—2010)独立给出的，参见Rao(1945)和Blackwell(1947).所以，在统计中也称之为Rao-Blackwell定理.另外,Hodges et al.(1950)证明了如果将作为二次损失的方差换成其他凸损失，上述结论仍成立.

---

58

第二章 参数点估计

此定理表明, 关于可估参数 $g(\theta)$, 如果有充分统计量, 则可由一个无偏估计构造一个依赖于充分统计量的新无偏估计, 且这个新无偏估计的方差不大于原来无偏估计的方差. 那是否可找到一个方差最小的无偏估计呢?

## 2.1.2 一致最小方差无偏估计

为回答上小节最后一个问题, 我们有如下准则:

定义2.1.3 设 $g(\theta)$ 是一可估函数, $T(X)$ 是 $g(\theta)$ 的一个无偏估计, 如对于 $g(\theta)$ 的任一无偏估计 $S(X)$, 均有

$$
\mathrm{Var} _ {\theta} (T) \leqslant \mathrm{Var} _ {\theta} (S), \forall \theta \in \Theta ,
$$

则称 $T(X)$ 是 $g(\theta)$ 的一致最小方差无偏估计 (uniformly minimum variance unbiased estimate, 简记为 UMVUE).

如果UMVUE存在，则如何求取呢？为此，引入两个统计量的集合:

$$
\mathcal {T} = \{T (X): E _ {\theta} [ T (X) ] = g (\theta), E _ {\theta} [ T (X) ] ^ {2} <   \infty , \forall \theta \in \Theta \}, \tag {2.1.2}
$$

$$
\mathcal {T} _ {0} = \{T (X): E _ {\theta} [ T (X) ] = 0, E _ {\theta} [ T (X) ] ^ {2} <   \infty , \forall \theta \in \Theta \}, \tag {2.1.3}
$$

它们分别表示  $g(\theta)$  与 0 的二阶矩有限的无偏估计类.

定理2.1.2 设 $g(\theta)$ 可估，则估计量 $T \in \mathcal{T}$ 是 $g(\theta)$ 的UMVUE，当且仅当

$$
E _ {\theta} [ S (X) T (X) ] = 0, \forall \theta \in \Theta , \forall S (X) \in \mathcal {T} _ {0}. \tag {2.1.4}
$$

证明 先证必要性. 反证:

设 $T \in \mathcal{T}$ 是 $g(\theta)$ 的一个UMVUE, 但条件(2.1.4)不成立, 即存在 $S_0 \in \mathcal{T}_0$ 和 $\theta_0 \in \Theta$, 使得 $E_{\theta_0}(S_0T) \neq 0$.

因为 $S_0 \in \mathcal{T}_0$，所以对于任意常数 $\lambda, T_\lambda = T - \lambda S_0 \in \mathcal{T}$，而

$$
E _ {\theta_ {0}} (T _ {\lambda} ^ {2}) = E _ {\theta_ {0}} (T - \lambda S _ {0}) ^ {2} = E _ {\theta_ {0}} (T ^ {2}) + \lambda^ {2} E _ {\theta_ {0}} (S _ {0} ^ {2}) - 2 \lambda E _ {\theta_ {0}} (T S _ {0}).
$$

由于 $E_{\theta_0}(S_0T) \neq 0$，故取 $\lambda_0 = E_{\theta_0}(S_0T) / E_{\theta_0}(S_0^2) \neq 0$，就有

$$
E _ {\theta_ {0}} (T _ {\lambda_ {0}} ^ {2}) <   E _ {\theta_ {0}} (T ^ {2}),
$$

即 $\mathrm{Var}_{\theta_0}(T_{\lambda_0}) < \mathrm{Var}_{\theta_0}(T)$，与 $T$ 是UMVUE矛盾.

下证充分性.

设 $T$ 满足(2.1.4)式, 则对于任意 $\tilde{T} \in \mathcal{T}$, 由于 $T - \tilde{T} \in \mathcal{T}_0$, 则由(2.1.4)式知

$$
E _ {\theta} [ (T - \tilde {T}) T ] = 0, \forall \theta \in \Theta ,
$$

---

2.1 几个常用的估计准则

59

即

$$
E _ {\theta} (T ^ {2}) = E _ {\theta} (T \tilde {T}), \forall \theta \in \Theta ,
$$

于是由 Cauchy-Schwarz(柯西-施瓦茨) 不等式知,

$$
E _ {\theta} (T ^ {2}) \leqslant [ E _ {\theta} (\tilde {T} ^ {2}) ] ^ {1 / 2} [ E _ {\theta} (T ^ {2}) ] ^ {1 / 2},   \forall   \theta \in \Theta ,
$$

即

$$
E _ {\theta} (T ^ {2}) \leqslant E _ {\theta} (\tilde {T} ^ {2}), \forall \theta \in \Theta .
$$

由于  $T, \tilde{T}$  均是  $g(\theta)$  的 UE, 且  $\tilde{T}$  是任意的, 故由上式可知, T 是  $g(\theta)$  的 UMVUE.

![](../../raw/pages_0065-0080/images/page_71_image_9.jpg)

UMVUE 如存在, 那它唯一吗? 见下面定理:

定理 2.1.3 如果  $g(\theta)$  的无偏估计类 T 非空, 则其 UMVUE 最多有一个.

证明 如果 $T \neq T_0$ 是 $g(\theta)$ 的两个UMVUE, 则必有

$$
E _ {\theta} (T) = E _ {\theta} (T _ {0}) = g (\theta), \operatorname{Var} _ {\theta} (T _ {0}) = \operatorname{Var} _ {\theta} (T), \forall \theta \in \Theta .
$$

于是, $T-T_{0}\in\mathcal{T}_{0}$ . 因为 T 是 UMVUE, 故由定理 2.1.2 知

$$
E _ {\theta} [ (T - T _ {0}) T ] = 0, \forall \theta \in \Theta .
$$

又由于 $T_0$ 也是UMVUE,故由定理2.1.2知

$$
E _ {\theta} [ (T - T _ {0}) T _ {0} ] = 0, \forall \theta \in \Theta .
$$

综合以上两式, 我们有

$$
E _ {\theta} (T - T _ {0}) ^ {2} = E _ {\theta} [ (T - T _ {0}) (T - T _ {0}) ] = 0, \forall \theta \in \Theta ,
$$

故 $P_{\theta}(T = T_0) = 1, \forall \theta \in \Theta.$

![](../../raw/pages_0065-0080/images/page_71_image_21.jpg)

从定理 2.1.3 可知, UMVUE 如存在, 则在概率 1 相等的意义下是唯一的. 如果存在充分统计量, 则结合定理 2.1.1 与定理 2.1.2, 我们有如下的结论.

定理2.1.4 设 $T(X)$ 为充分统计量, $g(\theta)$ 可估. 记

$$
\mathcal {S} (T) = \{S (T): E _ {\theta} [ S (T) ] = g (\theta), E _ {\theta} [ S (T) ] ^ {2} <   \infty , \forall \theta \in \Theta \}, \tag {2.1.5}
$$

$$
\mathcal {S} _ {0} (T) = \{S (T): E _ {\theta} [ S (T) ] = 0, E _ {\theta} [ S (T) ] ^ {2} <   \infty , \forall \theta \in \Theta \}, \tag {2.1.6}
$$

则 $S(T)\in \mathcal{S}(T)$ 为 $g(\theta)$ 的UMVUE的充要条件是

$$
E _ {\theta} [ S (T) S _ {0} (T) ] = 0, \forall S _ {0} (T) \in \mathcal {S} _ {0} (T), \forall \theta \in \Theta . \tag {2.1.7}
$$

---

60

第二章 参数点估计

证明 由于 $\mathcal{S}(T)\subset \mathcal{T},\mathcal{S}_0(T)\subset \mathcal{T}_0$ ，故只要证明:由

$$
E _ {\theta} [ S (T) S _ {0} (T) ] = 0, \forall S _ {0} (T) \in \mathcal {S} _ {0} (T), \forall \theta \in \Theta
$$

可推得

$$
E _ {\theta} [ S (T) S _ {0} ] = 0, \forall S _ {0} \in \mathcal {S} _ {0}, \forall \theta \in \Theta
$$

即可. 实际上, 对于任意的 $S_0 \in \mathcal{S}_0$, 因为 $E[S_0|T] \in \mathcal{S}_0(T)$, 且

$$
E _ {\theta} [ S (T) S _ {0} ] = E _ {\theta} \{E [ S (T) S _ {0} | T ] \} = E _ {\theta} [ S (T) \cdot E (S _ {0} | T) ],
$$

故上述条件可证.

![](../../raw/pages_0065-0080/images/page_72_image_9.jpg)

例 2.1.6 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $U(0, \theta)$  的独立同分布样本, 其中  $\theta > 0$ . 求  $\theta$  的 UMVUE.

解 由例1.4.5知, $T(X) = X_{(n)}$ 是充分统计量, 且其概率密度为

$$
f _ {T} (t; \theta) = \frac {n t ^ {n - 1}}{\theta^ {n}} I _ {(0, \theta)} (t),
$$

故我们可以利用定理 2.1.4 求  $\theta$  的 UMVUE. 下设  $S(T)$  为 0 的一个 UE, 则

$$
E _ {\theta} [ S (T) ] = 0, \forall \theta > 0.
$$

又由例 1.4.10 知, T 是完全统计量, 故由上式知

$$
P (S (T) = 0) = 1.
$$

于是, 只要  $H(T)$  是  $\theta$  的无偏估计, 就有

$$
E _ {\theta} [ H (T) S (T) ] = 0, \forall \theta > 0.
$$

这样, 由定理 2.1.4 可知, 任一个基于充分完全统计量 T 的无偏估计就是  $\theta$  的 UMVUE. 由  $X_{(n)}$  的概率密度, 可以验证  $E_{\theta}[X_{(n)}] = \frac{n}{n+1}\theta$ . 于是可知  $\theta$  的 UMVUE 为  $\frac{n+1}{n}X_{(n)}$ . ☐

上例说明, 我们可以利用充分完全统计量比较容易地求得某参数的 UMVUE, 这即为下面定理.

定理2.1.5 设参数 $g(\theta)$ 可估, $T(X)$ 为充分完全统计量. 如果 $S(X)$ 是 $g(\theta)$ 的 UE, 则 $S_0(T) = E[S(X)|T]$ 是 $g(\theta)$ 的 UMVUE.

证明 设 $S_{1}, S_{2}$ 是 $g(\theta)$ 的任意两个 UE, 则由条件期望的性质可知, $E(S_{1}|T), E(S_{2}|T)$ 均是 $g(\theta)$ 的 UE, 即

$$
E _ {\theta} [ E (S _ {1} | T) ] = E _ {\theta} [ E (S _ {2} | T) ] = g (\theta), \forall \theta \in \Theta , \tag {*}.
$$

---

2.1 几个常用的估计准则

61

且

$$
\mathrm{Var} _ {\theta} [ E (S _ {1} | T) ] \leqslant \mathrm{Var} _ {\theta} (S _ {1}), \forall \theta \in \Theta ,
$$

$$
\mathrm{Var} _ {\theta} [ E (S _ {2} | T) ] \leqslant \mathrm{Var} _ {\theta} (S _ {2}), \forall \theta \in \Theta .
$$

另由 (\*) 式可知,  $E(S_{1}|T)-E(S_{2}|T)$  是 0 的无偏估计, 即

$$
E _ {\theta} [ E (S _ {1} | T) - E (S _ {2} | T) ] = 0, \forall \theta \in \Theta ,
$$

又由于 T 是完全统计量, 故由定义知

$$
P _ {\theta} (E (S _ {1} | T) = E (S _ {2} | T)) = 1, \forall \theta \in \Theta ,
$$

这说明在概率 1 的意义下, $E(S_1|T)$ 与 $E(S_2|T)$ 相等, 又由于 $S_1$ 与 $S_2$ 的任意性, 故 $S_0 = E(S|T)$ 是唯一的 UMVUE. $\square$

![](../../raw/pages_0065-0080/images/page_73_image_10.jpg)

注2.1.2 由定理2.1.5可知, 如果 $T(X)$ 是充分完全统计量, 且 $S(T)$ 是 $g(\theta)$ 的 UE, 则它就是 $g(\theta)$ 的 UMVUE.

例 2.1.7 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自 Poisson 总体  $P(\lambda)$  的独立同分布样本, 对于给定的非负整数 k, 求参数

$$
p _ {\lambda} (k) = \frac {\lambda^ {k}}{k !} \mathrm{e} ^ {- \lambda}
$$

的 UMVUE.

解 由 $p_{\lambda}(k)$ 的定义可以看出, $S_{k}(X) = I_{k}(X_{1})$ 是其一个 UE. 再由例 1.4.11 可知, $T(X) = \sum_{i=1}^{n} X_{i}$ 是完全统计量, 且由因子分解定理可证明, 它也是充分统计量. 于是, 根据定理 2.1.5 可知, $E[S_{k}(X)|T]$ 是 $p_{\lambda}(k)$ 的 UMVUE.

由于

$$
\begin{array}{l} E [ S _ {k} (X) | T = t ] = P (X _ {1} = k | T = t) = \frac {P (X _ {1} = k , T = t)}{P (T = t)} \\ = \frac {P (X _ {1} = k , X _ {2} + X _ {3} + \cdots + X _ {n} = t - k)}{P (T = t)}, \\ \end{array}
$$

且  $X_{1} \sim P(\lambda)$  与  $X_{2} + X_{3} + \cdots + X_{n} \sim P((n-1)\lambda)$  独立, 则代入上式后, 有

$$
E [ S _ {k} (X) | T = t ] = \binom{t}{k} \left(\frac {1}{n}\right) ^ {k} \left(1 - \frac {1}{n}\right) ^ {t - k}.
$$

于是, $p_{\lambda}(k)$ 的 UMVUE 为

$$
\binom{T}{k} \left(\frac {1}{n}\right) ^ {k} \left(1 - \frac {1}{n}\right) ^ {T - k}.
$$

![](../../raw/pages_0065-0080/images/page_73_image_22.jpg)

---

62

第二章 参数点估计

从上述几个例子可以看到, 多数情况下可以求得 UMVUE, 但在某些情况下 UMVUE 不一定存在, 即使存在也有不合理的情况发生.

例 2.1.8 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自 Poisson 总体  $P(\lambda)$  的独立同分布样本, 求参数  $g(\lambda) = \mathrm{e}^{-a\lambda}$  的 UMVUE, 其中 a > 0 为常数.

解 由前述内容可知 $T(X) = \sum_{i=1}^{n} X_i$ 为充分完全统计量, 且如果 $S(T)$ 是 $g(\lambda)$ 的 UE, 则它就是其 UMVUE. 下设 $S(T)$ 为 $g(\lambda)$ 的 UE, 则

$$
\sum_ {t = 0} ^ {\infty} \frac {S (t) (n \lambda) ^ {t}}{t !} = \mathrm{e} ^ {(n - a) \lambda} = \sum_ {t = 0} ^ {\infty} \frac {(n - a) ^ {t} \lambda^ {t}}{t !},
$$

于是，

$$
S (T) = (1 - a / n) ^ {T}
$$

是  $g(\lambda)$  的 UMVUE, 但是当  $a \geqslant n$  时, 这个 UMVUE 并不合理.

既然 UMVUE 的方差在无偏估计类中最小, 那这个最小方差有一个下界吗? Fréchet (1943) 最早注意到了这个问题, 并引入信息不等式. 后来 Rao (1945) 和 Cramér (1946) 分别对此进行了推广, 其结果被称为 Cramér-Rao (克拉默-拉奥) 不等式, 简记为 C-R 不等式. 为了便于书写, 在下一定理中, 记 $\boldsymbol{X} = (X_1, X_2, \cdots, X_n), \boldsymbol{x} = (x_1, x_2, \cdots, x_n)$.

定理 2.1.6 (C-R 不等式) 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $X \sim f(x; \theta)$  的独立同分布样本，其中  $\theta \in \Theta \subset R$ ，且  $\Theta$  为开区间（有限、无限或半无限）。假设支撑集  $S = \{x : f(x; \theta) > 0\}$  与参数  $\theta$  无关， $f(x; \theta)$  关于  $\theta$  可导，且总体概率分布的微分与积分可互换，即

$$
\frac {\mathrm{d}}{\mathrm{d} \theta} \int_ {- \infty} ^ {\infty} f (x; \theta) \mathrm{d} x = \int_ {- \infty} ^ {\infty} \frac {\partial}{\partial \theta} f (x; \theta) \mathrm{d} x. \tag {2.1.8}
$$

再设  $g(\theta)$  可估，

$$
I (\theta) = E _ {\theta} \left[ \frac {\partial}{\partial \theta} \ln f (X; \theta) \right] ^ {2} \text {存在,且} I (\theta) > 0. \tag {2.1.9}
$$

如果  $T(\boldsymbol{X})$  是  $g(\theta)$  的 UE, 且满足积分与微分可互换, 即

$$
\frac {\mathrm{d}}{\mathrm{d} \theta} \int T (\pmb {x}) f (\pmb {x}; \theta) \mathrm{d} \pmb {x} = \int T (\pmb {x}) \frac {\partial}{\partial \theta} f (\pmb {x}; \theta) \mathrm{d} \pmb {x},
$$

则

$$
\mathrm{Var} _ {\theta} [ T (\boldsymbol {X}) ] \geqslant \frac {[ g ^ {\prime} (\theta) ] ^ {2}}{n I (\theta)}, \forall \theta \in \Theta , \tag {2.1.10}
$$

且等号成立当且仅当，存在 $c(\theta)\neq 0$ ，使得

$$
\frac {\partial \ln f (\boldsymbol {X} ; \theta)}{\partial \theta} = c (\theta) [ T (\boldsymbol {X}) - g (\theta) ].
$$

---

2.1 几个常用的估计准则

63

证明 如 $I(\theta) = \infty$ 或 $\operatorname{Var}_{\theta}(T) = \infty$，则 (2.1.10) 式均显然成立。故下面假设 $I(\theta) < \infty, \operatorname{Var}_{\theta}(T) < \infty$。

因为

$$
\int \frac {\partial \ln f (x ; \theta)}{\partial \theta} f (x; \theta) \mathrm{d} x = \int \frac {\partial f (x ; \theta)}{\partial \theta} \mathrm{d} x = \frac {\mathrm{d}}{\mathrm{d} \theta} \int f (x; \theta) \mathrm{d} x = 0, \tag {*1}
$$

又因为样本是 iid 的, 且样本分布 $f(\boldsymbol{x}; \theta) = \prod_{i=1}^{n} f(x_i; \theta)$, 故由 (\*1) 式知

$$
\int \frac {\partial \ln f (\boldsymbol {x} ; \theta)}{\partial \theta} f (\boldsymbol {x}; \theta) \mathrm{d} \boldsymbol {x} = 0, \forall \theta \in \Theta ,
$$

于是, 对于任意的 $g(\theta)$, 我们有

$$
\int g (\theta) \frac {\partial \ln f (\boldsymbol {x} ; \theta)}{\partial \theta} f (\boldsymbol {x}; \theta) \mathrm{d} \boldsymbol {x} = 0, \forall \theta \in \Theta . \tag {*2}
$$

又因为

$$
\begin{array}{l} g ^ {\prime} (\theta) = \frac {\partial}{\partial \theta} g (\theta) = \frac {\partial}{\partial \theta} E _ {\theta} [ T (\boldsymbol {X}) ] \\ = \frac {\partial}{\partial \theta} \int T (\boldsymbol {x}) f (\boldsymbol {x}; \theta) \mathrm{d} \boldsymbol {x} \\ = \int \frac {\partial}{\partial \theta} T (\boldsymbol {x}) f (\boldsymbol {x}; \theta) \mathrm{d} \boldsymbol {x} \\ = \int T (\boldsymbol {x}) \frac {\partial \ln f (\boldsymbol {x} , \theta)}{\partial \theta} f (\boldsymbol {x}; \theta) \mathrm{d} \boldsymbol {x} \\ \stackrel {(* 2)} {=} \int [ T (\boldsymbol {x}) - g (\theta) ] \frac {\partial \ln f (\boldsymbol {x} ; \theta)}{\partial \theta} f (\boldsymbol {x}; \theta) \mathrm{d} \boldsymbol {x}, \forall \theta \in \Theta . \\ \end{array}
$$

于是, 由 Cauchy-Schwarz 不等式知, 对于 $\forall \theta \in \Theta$, 有

$$
\begin{array}{l} [ g ^ {\prime} (\theta) ] ^ {2} = \left\{\int [ T (\boldsymbol {x}) - g (\theta) ] \frac {\partial \ln f (\boldsymbol {x} ; \theta)}{\partial \theta} f (\boldsymbol {x}; \theta) \mathrm{d} \boldsymbol {x} \right\} ^ {2} \\ \leqslant \int [ T (\boldsymbol {x}) - g (\theta) ] ^ {2} f (\boldsymbol {x}; \theta) \mathrm{d} \boldsymbol {x} \cdot \int \left[ \frac {\partial \ln f (\boldsymbol {x} ; \theta)}{\partial \theta} \right] ^ {2} f (\boldsymbol {x}; \theta) \mathrm{d} \boldsymbol {x} \\ = \operatorname{Var} _ {\theta} (T) \cdot n I (\theta), \\ \end{array}
$$

且由 Cauchy-Schwarz 不等式知, 上述等号成立的条件为: 存在 $c(\theta) \neq 0$, 使得

$$
\frac {\partial \ln f (\boldsymbol {X} ; \theta)}{\partial \theta} = c (\theta) [ T (\boldsymbol {X}) - g (\theta) ].
$$

![](../../raw/pages_0065-0080/images/page_75_image_15.jpg)

---

64

第二章 参数点估计

注2.1.3 上一定理中几个条件的解释:

(1) 关于总体概率分布的微分与积分可互换条件 (2.1.8), 相当于要求

$$
E _ {\theta} \left[ \frac {\partial \ln f (X ; \theta)}{\partial \theta} \right] = 0, \forall \theta \in \Theta . \tag {2.1.11}
$$

(2) (2.1.9) 式的  $I(\theta)$  被称为 Fisher 信息量, 它反映着总体分布为参数  $\theta$  所提供的信息量, 且

$$
I (\theta) = \mathrm{Var} _ {\theta} \left[ \frac {\partial \ln f (X ; \theta)}{\partial \theta} \right] = - E _ {\theta} \left[ \frac {\partial^ {2} \ln f (X ; \theta)}{\partial \theta^ {2}} \right].
$$

另外, 如果 n 个样本相互独立, 则

$$
E _ {\theta} \left[ \frac {\partial \ln f (\boldsymbol {X} ; \theta)}{\partial \theta} \right] ^ {2} = n I (\theta). \tag {2.1.12}
$$

上述 Fisher 信息量 $I(\theta)$ 仅反映了总体给参数 $\theta$ 提供的信息量. 在统计中还有度量两个概率密度间差异的信息量: Kullback-Leibler(库尔贝克-莱布勒) 信息, 简记为 K-L 信息, 其定义如下:

定义 2.1.4(K-L 信息) 设  $f(x)$ ,  $g(x)$  为两个概率密度, 则二者间的 K-L 信息定义为

$$
K (f, g) = E _ {X \sim f} \left[ \ln \frac {f (X)}{g (X)} \right]. \tag {2.1.13}
$$

如果  $X \sim f(x; \theta)$ ,  $\theta \in \Theta$ ，则对于任给的  $\theta_{1}, \theta_{2} \in \Theta$ ，总体 X 的 K-L 信息定义为

$$
K _ {X} (\theta_ {1}, \theta_ {2}) = E _ {\theta} \left[ \ln \frac {f (X ; \theta_ {1})}{f (X ; \theta_ {2})} \right]. \tag {2.1.14}
$$

定理 2.1.7 设  $X \sim f(x; \theta)$ ，统计量  $T(X) \sim g(t; \theta)$ ，且两个分布都满足定理 2.1.6 中的条件，则

$$
K _ {X} (\theta_ {1}, \theta_ {2}) \geqslant K _ {T} (\theta_ {1}, \theta_ {2}),
$$

且等式成立当且仅当 $T(X)$ 是充分统计量.

证明请参见韦博成 (2006).

如果一个无偏估计的方差达到了上述下界, 则它是 UMVUE, 但反之不成立.

例 2.1.9 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $X \sim B(1, p)$  的独立同分布样本, 求 p 的 UMVUE.

解 可以验证总体分布满足定理 2.1.7 中的条件, 且其 Fisher 信息量为

$$
I (p) = E _ {p} \left[ \frac {\partial \ln f (X ; p)}{\partial p} \right] ^ {2} = \sum_ {k = 0} ^ {1} \left[ \frac {\partial \ln f (k ; p)}{\partial p} \right] ^ {2} f (k; p),
$$

---

2.1 几个常用的估计准则

65

其中 $f(k;p) = P(X = k) = p^k (1 - p)^{1 - k}$. 于是

$$
I (p) = \left[ \frac {\partial \ln (1 - p)}{\partial p} \right] ^ {2} (1 - p) + \left(\frac {\partial \ln p}{\partial p}\right) ^ {2} p = \frac {1}{p (1 - p)},
$$

这样由信息不等式知, p 的 UE 的方差的 C-R 下界为  $\frac{1}{nI(p)} = \frac{p(1 - p)}{n}$ .

另外, 由于 $\sum_{i=1}^{n} X_i \sim B(n, p)$, 故 $\operatorname{Var}(\bar{X}) = \frac{p(1-p)}{n}$ 达到了 C-R 下界, 且是 $p$ 的无偏估计, 故可知 $\bar{X}$ 是 $p$ 的 UMVUE. $\square$

例 2.1.10 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $X \sim N(\mu, \sigma^{2})$  的独立同分布样本, 求  $\mu$  和  $\sigma^{2}$  的 UE 的方差下界.

解 容易验证正态分布满足定理中的要求, 且因为

$$
f (x; \mu , \sigma^ {2}) = \frac {1}{\sqrt {2 \pi} \sigma} \exp \left\{- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}} \right\},
$$

$$
\ln f (x; \mu , \sigma^ {2}) = - \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}} - \frac {1}{2} \ln \sigma^ {2} - \frac {1}{2} \ln 2 \pi ,
$$

所以

$$
\frac {\partial \ln f (x ; \mu , \sigma^ {2})}{\partial \mu} = \frac {x - \mu}{\sigma^ {2}}, \quad \frac {\partial^ {2} \ln f (x ; \mu , \sigma^ {2})}{\partial \mu^ {2}} = - \frac {1}{\sigma^ {2}},
$$

$$
\frac {\partial \ln f (x ; \mu , \sigma^ {2})}{\partial \sigma^ {2}} = \frac {(x - \mu) ^ {2}}{2 \sigma^ {4}} - \frac {1}{2 \sigma^ {2}}, \frac {\partial^ {2} \ln f (x ; \mu , \sigma^ {2})}{\partial (\sigma^ {2}) ^ {2}} = - \frac {(x - \mu) ^ {2}}{\sigma^ {6}} + \frac {1}{2 \sigma^ {4}}.
$$

于是，可知

$$
I (\mu) = 1 / \sigma^ {2}, \quad I (\sigma^ {2}) = 1 / 2 \sigma^ {4},
$$

则  $\mu$  和  $\sigma^{2}$  的 UE 的方差的 C-R 下界分别为  $\sigma^{2}/n, 2\sigma^{4}/n$ .

因为  $\mathrm{Var}(\bar{X}) = \sigma^{2}/n$  达到了 C-R 下界且无偏，故  $\bar{X}$  是  $\mu$  的 UMVUE. 然而，对于  $\sigma^{2}$  的 UMVUE——样本方差  $S_{n}^{2}$ ，由于  $(n-1)S_{n}^{2}/\sigma^{2} \sim \chi^{2}(n-1)$ ，故由此可知， $\mathrm{Var}(S_{n}^{2}) = \frac{2\sigma^{4}}{n-1}$ ，它并没有达到 C-R 下界.

上面仅考虑了单参数的情况, 对于多参数, 设  $\boldsymbol{\theta} = (\theta_{1}, \theta_{2}, \cdots, \theta_{r})^{\mathrm{T}} \in \Theta$ , 则此时的 Fisher 信息矩阵定义为

$$
\boldsymbol {I} (\boldsymbol {\theta}) = - E \left[ \left(\frac {\partial f (X ; \boldsymbol {\theta})}{\partial \boldsymbol {\theta}}\right) \left(\frac {\partial f (X ; \boldsymbol {\theta})}{\partial \boldsymbol {\theta}}\right) ^ {\mathrm{T}} \right].
$$

如记  $\boldsymbol{g}(\boldsymbol{\theta})$  为 s 维参数向量,  $\Delta=\left(\frac{\partial g_{i}(\boldsymbol{\theta})}{\partial\theta_{j}}\right)_{s\times r}$ , s 维统计量  $\boldsymbol{T}(X)$  是 g 的无偏估计, 则在一定正则条件下, C-R 不等式为

$$
\operatorname{Var} _ {\boldsymbol {\theta}} [ \boldsymbol {T} (X) ] \geqslant \Delta I ^ {- 1} (\boldsymbol {\theta}) \Delta^ {\mathrm{T}}, \forall \boldsymbol {\theta} \in \Theta ,
$$

---

66

第二章 参数点估计

其中  $\mathrm{Var}_{\boldsymbol{\theta}}[\boldsymbol{T}(x)]=E_{\boldsymbol{\theta}}[(\boldsymbol{T}(x)-\boldsymbol{g}(\boldsymbol{\theta}))(T(x)-\boldsymbol{g}(\boldsymbol{\theta}))^{\mathrm{T}}]$ ，矩阵  $A\geqslant B$  意味着 A-B 半正定.

在结束本小节前, 我们注意到在不同准则下, 估计量的优良性质是不同的. 如前面讲述的 UMVUE, 它在参数的无偏估计类中方差最小, 但在其他准则下, 就不一定是最优的, 比如在均方误差最小的准则下. 对于参数 $g(\theta)$ 的估计量 $T(X)$, 由于

$$
\mathrm{MSE} _ {\theta} [ T (X) ] = E _ {\theta} [ T (X) - g (\theta) ] ^ {2} = \mathrm{Var} _ {\theta} [ T (X) ] + b _ {T} ^ {2} (\theta),
$$

故可知估计量 $T(X)$ 的均方误差综合了其方差与偏差, 因此, 有些情况下, 也多采用均方误差的大小来衡量估计量的好坏. 比如在例2.1.6中, 记 $T_{n} = X_{(n)}$, $T^{*} = \frac{n + 1}{n} T_{n}$ 是 $\theta$ 的UMVUE, 但如果在形如 $cT_{n}$ 的估计类中, 由于

$$
\mathrm{MSE} _ {\theta} (c T _ {n}) = E _ {\theta} (c T _ {n} - \theta) ^ {2} = \theta^ {2} \left(\frac {n}{n + 2} c ^ {2} - \frac {2 n}{n + 1} c + 1\right),
$$

则当取 $c_{0} = \frac{n + 2}{n + 1}$ 时, $c_{0}T_{n}$ 的MSE达到最小, 即估计量 $\frac{n + 2}{n + 1} X_{(n)}$ 是在形如 $cX_{(n)}$ 的估计类中, 均方误差最小者. 但是

$$
\mathrm{MSE} _ {\theta} [ c _ {0} X _ {(n)} ] = \frac {\theta^ {2}}{(n + 1) ^ {2}} <   \frac {\theta^ {2}}{n (n + 2)} = \mathrm{MSE} _ {\theta} (T ^ {*}),
$$

这就说明, 此时参数  $\theta$  的 UMVUE, 在均方误差最小的准则下, 不是最优的. 另外, 由于均方误差平衡了方差与偏差的大小, 故在许多情况下都有很好的应用, 但其困难点在于估计类的确定.

## 2.1.3 有效估计

从上小节内容可知, 有的 UMVUE 达到了 C-R 下界, 而有的则没有, 于是就有了有效估计的定义.

定义 2.1.5 (有效估计及效率) 设  $T(X)$  是  $g(\theta)$  的一个 UE, 则称比值

$$
e _ {n} = \frac {[ g ^ {\prime} (\theta) ] ^ {2} / n I (\theta)}{\mathrm{Var} _ {\theta} [ T (X) ]}
$$

为 $T(X)$ 的效率. 如果 $e_n = 1$, 则称 $T(X)$ 为 $g(\theta)$ 的有效估计. 如 $\lim_{n \to \infty} e_n = 1$, 则称 $T(X)$ 为 $g(\theta)$ 的渐近有效估计.

由此定义可知, 有效估计一定是 UMVUE, 但 UMVUE 不一定是有效估计. 另外, 有效估计一定要求总体分布及其自身都要满足 C-R 不等式定理中的条件.

注 2.1.4 在文献中, 关于效率, 还有其他定义, 如 Pitman(皮特曼) 渐近相对效率; 关于有效估计, 还有 Bahadur(巴哈杜尔) 渐近有效估计等.

---

2.1 几个常用的估计准则

67

虽然下面讲述的得分函数与估计准则无关,但由于它在统计推断中发挥着非常重要的作用,且与 Fisher 信息量有关,故在这里加以叙述.

定义 2.1.6 (得分函数) 称

$$
S (\boldsymbol {X}; \theta) = \frac {\partial \ln f (\boldsymbol {X} ; \theta)}{\partial \theta}
$$

为得分函数 (score function). 当  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本时,

$$
S (\boldsymbol {X}; \theta) = \sum_ {i = 1} ^ {n} \frac {\partial \ln f (X _ {i} ; \theta)}{\partial \theta}. \tag {2.1.15}
$$

如果样本独立同分布, 则可以证明

$$
E _ {\theta} [ S (\boldsymbol {X}; \theta) ] = 0, \operatorname{Var} _ {\theta} [ S (\boldsymbol {X}; \theta) ] = n I (\theta),
$$

且

$$
\frac {1}{\sqrt {n}} S (\boldsymbol {X}; \theta) \xrightarrow {\mathrm{d}} N (0, I (\theta)). \tag {2.1.16}
$$

另外, 对于任一关于样本 X 和  $\theta$  的函数  $T(X,\theta)$ , 如满足定理 2.1.6 中的条件, 则有如下结论:

$$
E _ {\theta} [ S (\boldsymbol {X}) T (\boldsymbol {X}; \theta) ] = \frac {\partial}{\partial \theta} E _ {\theta} [ T (\boldsymbol {X}; \theta) ] - E _ {\theta} \left[ \frac {\partial T (\boldsymbol {X} ; \theta)}{\partial \theta} \right]. \tag {2.1.17}
$$

由此等式可知:

\- 对 $g(\theta)$ 的任一无偏估计 $T(\pmb {X})$ ，都有

$$
E _ {\theta} [ S (\boldsymbol {X}) T (\boldsymbol {X}) ] = g ^ {\prime} (\theta).
$$

\- 对 $g(\theta)$ 的任一有偏估计 $T(\boldsymbol{X})$, 记 $E_{\theta}(T) = g(\theta) + b_{T}(\theta)$, 则

$$
E _ {\theta} [ S (\boldsymbol {X}) T (\boldsymbol {X}) ] = g ^ {\prime} (\theta) + \frac {\partial b _ {T} (\theta)}{\partial \theta}.
$$

在 C-R 不等式证明中, 我们主要用到了如下的 Cauchy-Schwarz 不等式: 如果  $T(\boldsymbol{X})$  为  $g(\theta)$  的一个无偏估计, 则

$$
\mathrm{Cov} _ {\theta} [ T (\boldsymbol {X}), S (\boldsymbol {X}) ] \leqslant \sqrt {\mathrm{Var} _ {\theta} [ T (\boldsymbol {X}) ] \mathrm{Var} _ {\theta} [ S (\boldsymbol {X}) ]}, \forall \theta \in \Theta .
$$

如果 $g(\theta)$ 以及得分函数 $S(\mathbf{X};\theta)$ 关于 $\theta$ 的 $k$ 阶导数存在, 则在某些条件下 (类似于定理2.1.6中的条件), 取

$$
\tilde {S} (\boldsymbol {X}, \theta) = (S ^ {1} (\boldsymbol {X}, \theta), S ^ {2} (\boldsymbol {X}, \theta), \dots , S ^ {k} (\boldsymbol {X}, \theta)) ^ {\mathrm{T}},
$$

则可以用上述结论证明

$$
\mathrm{Var} _ {\theta} [ T (\boldsymbol {X}) ] \geqslant \boldsymbol {\Delta} ^ {\mathrm{T}} V ^ {- 1} (\theta) \boldsymbol {\Delta}, \tag {2.1.18}
$$

---

68

第二章 参数点估计

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

---

2.1 几个常用的估计准则

69

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

---

70

第二章 参数点估计

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

---

2.1 几个常用的估计准则

71

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

---

72

第二章 参数点估计

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

---

2.1 几个常用的估计准则

73

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

---

74

第二章 参数点估计

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

---

2.2 矩估计

75

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

---

76

第二章 参数点估计

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

---

2.3 最大似然估计

77

证明 由于 $g_{i}$ 连续可微, 故由Taylor(泰勒)展开可知

$$
\sqrt {n} [ \boldsymbol {g} (\boldsymbol {X} _ {n}) - \boldsymbol {g} (\boldsymbol {\theta}) ] = \sqrt {n} \Delta (\boldsymbol {X} _ {n} - \boldsymbol {\theta}) + \sqrt {n} \cdot o (\boldsymbol {X} _ {n} - \boldsymbol {\theta}). \tag {*1}
$$

又由于 $\sqrt{n} (\pmb {X}_n - \pmb {\theta})$ 有极限分布，即弱收敛，故知

$$
\sqrt {n} (\boldsymbol {X} _ {n} - \boldsymbol {\theta}) = O _ {p} (1). \tag {*2}
$$

结合已知条件以及  $(*1)$ ,  $(*2)$  式, 结论得证.

![](../../raw/pages_0081-0096/images/page_89_image_7.jpg)

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

![](../../raw/pages_0081-0096/images/page_89_image_21.jpg)

## 2.3 最大似然估计

最大似然估计 (MLE) 最早由德国数学家 Gauss 在 1821 年针对正态分布提出, 之后 Fisher 于 1922 年提出了一般分布下的最大似然估计. 本节将给出最大似然估计的定义和某些性质, 以及求取某些复杂情况下最大似然估计的一种有效算法——EM 算法.

---

78

第二章 参数点估计

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

---

2.3 最大似然估计

79

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

![](../../raw/pages_0081-0096/images/page_91_image_20.jpg)

注2.3.1 在上述定义中，极值在参数空间闭包上求取的原因在于，如果参数空间 $\Theta$ 为开集，则似然函数的最大值有可能在边界上达到，从而导致在参数空间 $\Theta$ 中无最大值解.

例 2.3.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自正态总体  $N(\mu, \sigma^{2})$  的独立同分布样本, 求  $\mu$  和  $\sigma^{2}$  的 MLE.

---

80

第二章 参数点估计

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

---

2.3 最大似然估计

81

![](../../raw/pages_0081-0096/images/page_93_chart_2.jpg)

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

---

82

第二章 参数点估计

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

---

2.3 最大似然估计

83

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

---

84

第二章 参数点估计

注2.3.3 “以概率1当 $n$ 充分大时(2.3.8)式成立”的含义如下:存在 $\mathcal{X}^{\infty}$ 中的一个可测集 $A, P_{\theta_0}^{\infty}(A) = 1$ ，且当样本点 $(X_1, X_2, \dots) \in A$ 时，存在自然数 $N$ ，使得当 $n > N$ 时，对数似然方程(2.3.7)有一根 $\hat{\theta}_n(X_1, X_2, \dots, X_n)$ 满足 $\lim_{n \to \infty} \hat{\theta}_n(X_1, X_2, \dots, X_n) = \theta_0.$

我们注意到, 由似然方程的根求得的 MLE 也可能是局部极大值, 也存在不相合的情况. 见下面的例子.

例 2.3.6 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自两点分布

$$
P (X = 1) = 1 - P (X = 0) = \left\{ \begin{array}{l l} {\theta ,} & {\theta \text {为有理数},} \\ {1 - \theta ,} & {\theta \text {为无理数}} \end{array} \right.
$$

的独立同分布样本, 其中  $0 < \theta < 1$  为参数. 讨论  $\theta$  的 MLE 的相合性.

解 此时似然函数为

$$
L (\theta ; \pmb {x}) = \left\{ \begin{array}{l l} {{\theta^ {\sum_ {i = 1} ^ {n} x _ {i}} (1 - \theta) ^ {n - \sum_ {i = 1} ^ {n} x _ {i}},}} & {{\theta \text {为有理数},}} \\ {{\theta^ {n - \sum_ {i = 1} ^ {n} x _ {i}} (1 - \theta) ^ {\sum_ {i = 1} ^ {n} x _ {i}},}} & {{\theta \text {为无理数}.}} \end{array} \right.
$$

由此可以求出  $\theta$  的 MLE 为  $\hat{\theta} = \sum_{i=1}^{n} X_{i}/n$ . 但由大数定律知,

$$
\frac {\sum_ {i = 1} ^ {n} X _ {i}}{n} \xrightarrow {\mathrm{P}} \left\{ \begin{array}{l l} \theta , & \theta \text {为有理数,} \\ 1 - \theta , & \theta \text {为无理数,} \end{array} \right.
$$

由此可知此时的MLE并不是 $\theta$ 的相合估计.

虽然最大似估计的相合性需要一些条件才能成立, 但多数情况下, 存在着强相合的最大似然估计, 关于这方面的结果, 请参见陈希孺 (2009) 之 4.3.3 小节给出的较详细的讨论. 下面给出最大似然估计相合渐近正态性的简洁证明, 严格的论述也请参见陈希孺 (2009).

定理 2.3.3 (最大似然的 CAN) 设总体 X 的概率分布  $f(x; \theta)$  满足:

(1) 在参数真值  $\theta_{0}$  的邻域内,  $\partial^{i}\ln f(x;\theta)/\partial\theta^{i}, i=1,2,3$  存在;
(2) 在参数真值  $\theta_{0}$  的邻域内,  $\left|\partial^{3}\ln f(x;\theta)/\partial\theta^{3}\right|\leqslant H(x)$ , 且  $E[H(X)]<\infty;$
(3) 在参数真值  $\theta_{0}$  处,

$$
E _ {\theta_ {0}} \left[ \frac {f ^ {\prime} (X ; \theta_ {0})}{f (X ; \theta_ {0})} \right] = 0, E _ {\theta_ {0}} \left[ \frac {f ^ {\prime \prime} (X ; \theta_ {0})}{f (X ; \theta_ {0})} \right] = 0, I (\theta_ {0}) = E _ {\theta_ {0}} \left[ \frac {f ^ {\prime} (X ; \theta_ {0})}{f (X ; \theta_ {0})} \right] ^ {2} > 0.
$$

则存在 $\theta$ 的BAN估计 $\hat{\theta}_n$ ，它以概率1当 $n$ 充分大时为似然方程的解，即

$$
\sqrt {n} (\hat {\theta} _ {n} - \theta_ {0}) \stackrel {\mathrm{d}} {\longrightarrow} N (0, I ^ {- 1} (\theta_ {0})). \tag {2.3.9}
$$

---

2.3 最大似然估计

85

证明 由已知条件, $\hat{\theta}_n$ 为似然方程的相合解. 将 $\partial l(\theta; \boldsymbol{x}) / \partial \theta$ 在 $\theta_0$ 处 Taylor 展开, 有

$$
\frac {\partial l}{\partial \theta} = \frac {\partial l}{\partial \theta} \Big | _ {\theta_ {0}} + \frac {\partial^ {2} l}{\partial \theta^ {2}} \Big | _ {\theta_ {0}} (\theta - \theta_ {0}) + \frac {\partial^ {3} l}{\partial \theta^ {3}} \Big | _ {\theta_ {1}} \frac {(\theta - \theta_ {0}) ^ {2}}{2},
$$

其中  $\theta_{1}$  介于  $\theta$  与  $\theta_{0}$  之间. 在上式中取  $\theta$  的值为  $\hat{\theta}_{n}$ , 由于  $\hat{\theta}_{n}$  是  $\theta_{0}$  的相合估计, 故可知  $\theta_{1}\stackrel{P}{\longrightarrow}\theta_{0}$ , 于是

$$
0 = \left. \frac {\partial l}{\partial \theta} \right| _ {\hat {\theta} _ {n}} = \left. \frac {\partial l}{\partial \theta} \right| _ {\theta_ {0}} + (\hat {\theta} _ {n} - \theta_ {0}) \left[ \left. \frac {\partial^ {2} l}{\partial \theta^ {2}} \right| _ {\theta_ {0}} + O _ {p} (\hat {\theta} _ {n} - \theta_ {0}) \right],
$$

上式中的 $O_{p}$ 是由条件(2)及上述的相合性得到的. 由此式可以得到

$$
\sqrt {n} (\hat {\theta} _ {n} - \theta_ {0}) = \frac {- \sqrt {n} \frac {1}{n} \frac {\partial l}{\partial \theta} | _ {\theta_ {0}}}{\frac {1}{n} \left[ \frac {\partial^ {2} l}{\partial \theta^ {2}} | _ {\theta_ {0}} + O _ {p} (\hat {\theta} _ {n} - \theta_ {0}) \right]}.\tag {*1}
$$

注意到

$$
\left. \frac {\partial l}{\partial \theta} \right| _ {\theta_ {0}} = \sum_ {i = 1} ^ {n} \frac {f ^ {\prime} (x _ {i} ; \theta_ {0})}{f (x _ {i} ; \theta_ {0})}, \quad \left. \frac {\partial^ {2} l}{\partial \theta^ {2}} \right| _ {\theta_ {0}} = \sum_ {i = 1} ^ {n} \left\{\frac {f ^ {\prime \prime} (x _ {i} ; \theta_ {0})}{f (x _ {i} ; \theta_ {0})} - \left[ \frac {f ^ {\prime} (x _ {i} ; \theta_ {0})}{f (x _ {i} ; \theta_ {0})} \right] ^ {2} \right\}.
$$

因为 $E_{\theta_0}\left[\frac{f'(X;\theta_0)}{f(X;\theta_0)}\right] = 0,\mathrm{Var}_{\theta_0}\left[\frac{f'(X;\theta_0)}{f(X;\theta_0)}\right] = I(\theta_0)$ ，所以，由中心极限定理有

$$
\left. \frac {1}{\sqrt {n}} \frac {\partial l}{\partial \theta} \right| _ {\theta_ {0}} \xrightarrow {\mathrm{d}} N (0, I (\theta_ {0})). \tag {*2}
$$

由条件 (3) 及大数定律知

$$
\frac {1}{n} \frac {\partial^ {2} l}{\partial \theta^ {2}} \Big | _ {\theta_ {0}} \xrightarrow {\mathrm{P}} - I (\theta_ {0}). \tag {*3}
$$

结合 $(*1),(*2),(*3)$ 和 Slutsky(斯卢茨基) 定理, 有 (2.3.9) 式.

注 2.3.4 当总体分布为 (1.3.6) 式给出的指数型分布, 且自然参数空间有内点时, 陈希孺 (2009) 证明: 在一定条件下, 以概率 1 当 n 充分大时, 对数似然方程有唯一解  $\hat{\theta}_{n}$ , 它是  $\theta$  的强相合估计, 也是 BAN 估计.

例 2.3.7 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自正态总体  $N(\mu, \sigma^{2})$  的独立同分布样本, 证明  $\sigma^{2}$  的最大似然估计  $S_{n*}^{2}$  是总体方差的 BAN 估计.

证明 由前述内容可知, $nS_{n*}^{2}/\sigma^{2}\sim\chi^{2}(n-1)$ ,故

$$
E (S _ {n *} ^ {2}) = \frac {n - 1}{n} \sigma^ {2}, \mathrm{Var} (S _ {n *} ^ {2}) = \frac {2 (n - 1) \sigma^ {4}}{n ^ {2}}.
$$

由此可知, $S_{n*}^{2}$ 是 $\sigma^{2}$ 的相合估计.下证是BAN估计.

---

86

第二章 参数点估计

在定理 1.3.2 中, 通过正交变换后, 修正的样本方差可写成如下形式:

$$
n S _ {n *} ^ {2} = \sum_ {i = 2} ^ {n} Y _ {i} ^ {2},
$$

其中  $Y_{2}, Y_{3}, \cdots, Y_{n} \sim N(0, \sigma^{2})$ ，相互独立。由中心极限定理可知

$$
\frac {\sum_ {i = 2} ^ {n} Y _ {i} ^ {2}}{\sqrt {2 (n - 1) \sigma^ {4}}} \xrightarrow {\mathrm{d}} N (0, 1).
$$

因此，

$$
\sqrt {n} S _ {n *} ^ {2} \xrightarrow {\mathrm{d}} N (0, 2 \sigma^ {4}),
$$

即 $S_{n*}^{2} \sim AN(0, 2\sigma^{4}/n)$. 而由例 2.1.10 知, 此时关于 $\sigma^{2}$ 的 Fisher 信息量为 $1/(2\sigma^{4})$, 由此可知, $S_{n*}^{2}$ 是 $\sigma^{2}$ 的 BAN 估计. □

对于不满足定理 2.3.3 条件的总体分布, 如截断型分布, 其 MLE 的极限分布也不是正态, 比如对于均匀分布  $U(0,\theta)$  总体,  $\theta$  的 MLE 是极大次序统计量  $X_{(n)}$ , 可以证明, 它的极限分布不是正态, 而是一种极值分布.

另外, 虽然在多数情况下, MLE 是 BAN 估计, 但它不一定是无偏估计, 而是渐近无偏估计, 故也不一定是 UMVUE. 如对于均匀分布总体 $U(0, \theta), \hat{\theta} = X_{(n)}$ 是 $\theta$ 唯一的 MLE, 但由于 $P(X_{(n)} < \theta) = 1$, 故它总是低估 $\theta$.

再者, 最大似然估计强烈依赖总体分布已知, 如在某些问题中, 总体分布未知, 则无法求得参数的最大似然估计. 基于此, A. B. Owen (欧文) 于 1988 年提出了经验似然 (empirical likelihood) 方法, 从某些角度看, 它是似然思想在非参数中的拓展. 有兴趣的读者可参见 Owen (2001).

## 2.3.3 EM 算法

如例 2.3.5 所示, 在求 MLE 时, 有可能需要迭代方法. 然而在某些情况下, 如分布中有讨厌参数或数据有缺失或截尾, MLE 的求取就比较困难. 于是 Dempster et al. (1977) 提出了 EM 算法, 它把求 MLE 的过程分两步: 第一步求期望, 以便把讨厌的部分去掉; 第二步求极大值. 在某些参考文献中也称之为最大期望算法. 下面以一个例子说明 EM 算法是如何进行的.

例2.3.8 设总体服从多项分布

$$
\left( \begin{array}{c c c c} 1 & 2 & 3 & 4 \\ \frac {1}{2} + \frac {\theta}{4} & \frac {1 - \theta}{4} & \frac {1 - \theta}{4} & \frac {\theta}{4} \end{array} \right),
$$

---

2.3 最大似然估计

87

其中  $\theta\in(0,1)$ ，现进行 197 次独立观测，四种结果出现的次数分别为 125, 18, 20, 34. 求  $\theta$  的 MLE.

解 以 $X_{1}, X_{2}, X_{3}, X_{4}$ 分别记四种结果在 $n$ 次独立抽样后出现的次数, 则此时似然函数

$$
L (\theta ; \boldsymbol {x}) \propto \left(\frac {1}{2} + \frac {\theta}{4}\right) ^ {x _ {1}} \left(\frac {1 - \theta}{4}\right) ^ {x _ {2}} \left(\frac {1 - \theta}{4}\right) ^ {x _ {3}} \left(\frac {\theta}{4}\right) ^ {x _ {4}} \propto (2 + \theta) ^ {x _ {1}} (1 - \theta) ^ {x _ {2} + x _ {3}} \theta^ {x _ {4}},
$$

由此可知, 其对数似然方程是关于 $\theta$ 的二次三项式. 但可以通过引入一个变量 $Z$, 使求解变得比较容易.

假设第一种观测结果可以分成两部分, 其发生概率分别为 1/2 和  $\theta/4$ , 令 Z 和  $X_{1}-Z$  分别表示这两部分出现的次数. 显然, Z 是人为引入的, 它是不可观测的 (在文献中称之为潜在变量 (latent variable)). 数据  $(X, Z)$  被称为完全数据 (complete data), 观测到的数据 X 称为不完全数据. 此时, 完全数据的似然函数为

$$
\begin{array}{l} L (\theta | \boldsymbol {x}, z) \propto \left(\frac {1}{2}\right) ^ {z} \left(\frac {\theta}{4}\right) ^ {x _ {1} - z} \left(\frac {1 - \theta}{4}\right) ^ {x _ {2}} \left(\frac {1 - \theta}{4}\right) ^ {x _ {3}} \left(\frac {\theta}{4}\right) ^ {x _ {4}} \\ \propto \theta^ {x _ {1} - z + x _ {4}} (1 - \theta) ^ {x _ {2} + x _ {3}}, \\ \end{array}
$$

其对数似然函数为

$$
l (\theta | \boldsymbol {x}, z) \propto (x _ {1} - z + x _ {4}) \ln \theta + (x _ {2} + x _ {3}) \ln (1 - \theta).
$$

如果 $X, Z$ 均能观测到, 则由上式很容易求得 $\theta$ 的 MLE, 但遗憾的是, 我们仅观测到了 $X$, 而无法观测到 $Z$ 的值. 然而, 当 $X_1 = x_1$ 及 $\theta$ 已知时, $Z \sim B(x_1, 2/(2 + \theta))$ (其原因见后面的注 2.3.5). 于是, Dempster 等人建议分如下两步求 $\theta$ 的最大似然估计:

E 步: 在给定 X = x 及  $\theta = \theta^{(i)}$  的条件下, 求完全数据对数似然关于潜在变量 Z 的期望:

$$
Q (\theta | \boldsymbol {x}, \theta^ {(i)}) = E _ {Z} [ l (\theta | \boldsymbol {x}, Z) ]; \tag {2.3.10}
$$

M 步: 求  $Q(\theta|\boldsymbol{x},\theta^{(i)})$  关于  $\theta$  的最大值  $\theta^{(i+1)}$ ，即

$$
\theta^ {(i + 1)} = \arg \max _ {\theta} Q (\theta | \boldsymbol {x}, \theta^ {(i)}). \tag {2.3.11}
$$

重复 (2.3.10) 和 (2.3.11) 式给出的 E 步与 M 步, 直至收敛即可得到  $\theta$  的 MLE.

对于本问题, 其 E 步为

$$
\begin{array}{l} Q (\theta | \boldsymbol {x}, \theta^ {(i)}) \propto [ x _ {1} - E _ {Z} (Z | \boldsymbol {x}, \theta = \theta^ {(i)}) + x _ {4} ] \ln \theta + (x _ {2} + x _ {3}) \ln (1 - \theta) \\ = \{x _ {1} - 2 x _ {1} / [ 2 + \theta^ {(i)} ] + x _ {4} \} \ln \theta + (x _ {2} + x _ {3}) \ln (1 - \theta), \\ \end{array}
$$

---

88

第二章 参数点估计

其 M 步, 即上式两边关于  $\theta$  求导, 并令其等于 0, 可求得

$$
\theta^ {(i + 1)} = \frac {x _ {1} \theta^ {(i)} + x _ {4} [ \theta^ {(i)} + 2 ]}{x _ {1} \theta^ {(i)} + (x _ {2} + x _ {3} + x _ {4}) [ \theta^ {(i)} + 2 ]} = \frac {1 5 9 \theta^ {(i)} + 6 8}{1 9 7 \theta^ {(i)} + 1 4 4}.
$$

如取  $\theta^{(0)}=0.5$ ，则四步迭代后可求得  $\theta$  的 MLE 为 0.6268.

![](../../raw/pages_0097-0112/images/page_100_image_5.jpg)

注2.3.5 在 $X_{1} = x_{1}$ 的条件下, $Z \sim B(x_{1}, 2 / (2 + \theta))$ 的原因: 以 $A_{1}$ 表示第一种结果出现的事件, $B_{1}, B_{2}$ 分别表示我们所定义的两个事件, $A_{1} = B_{1} \cup B_{2}$. 由定义知它们是独立的, 且 $P(A_{1}) = \frac{1}{2} + \frac{\theta}{4}, P(B_{1}) = 1 / 2, P(B_{2}) = \theta / 4$, 则可知 $P(B_{1} | A_{1}) = P(B_{1}) / P(A_{1}) = 2 / (2 + \theta)$.

![](../../raw/pages_0097-0112/images/page_100_image_7.jpg)

注2.3.6 在(2.3.10)式右边的期望是关于 $Z$ 在 $\theta = \theta^{(i)}$ 的条件下求取的，而其余的参数不变，故左边与 $\theta^{(i)}$ 有关.

关于上述算法的收敛性, 有如下的结论:

定理 2.3.4 对于上述的 EM 算法, 有

$$
l (\theta^ {(i + 1)}; \boldsymbol {x}) \geqslant l (\theta^ {(i)}; \boldsymbol {x}) \geqslant 0, \tag {2.3.12}
$$

其中  $l(\theta; \boldsymbol{x})$  为不完全数据, 即样本 X 的对数似然函数, 即  $l(\theta; \boldsymbol{x}) = \ln f(\boldsymbol{x}; \theta)$ .

证明 为了方便, 改写前面的记号如下:

不完全数据, 即观测数据 X 的概率分布和对数似然函数分别为  $f(\boldsymbol{x}|\theta)$  和  $l(\theta|\boldsymbol{x})$ ; 完全数据  $(\boldsymbol{X}, Z)$  的概率分布和对数似然函数分别为  $f(\boldsymbol{x}, z|\theta)$  和  $l(\theta|\boldsymbol{x}, z)$ .

由条件分布公式知, 在  $(\boldsymbol{X}, \theta)$  已知时, Z 的条件概率分布为  $f(z|\boldsymbol{x}, \theta) = \frac{f(\boldsymbol{x}, z|\theta)}{f(\boldsymbol{x}|\theta)}$ , 于是,  $f(\boldsymbol{x}|\theta) = \frac{f(\boldsymbol{x}, z|\theta)}{f(z|\boldsymbol{x}, \theta)}$ , 两边取对数后有

$$
l (\theta | \boldsymbol {x}) = l (\theta | \boldsymbol {x}, z) - \ln f (z | \boldsymbol {x}, \theta),
$$

上式两边求 Z 在  $(\boldsymbol{X}, \theta = \theta^{(i)})$  给定下的条件期望:

$$
l (\theta | \boldsymbol {x}) = Q (\theta | \boldsymbol {x}, \theta^ {(i)}) - \int f (z | \boldsymbol {x}, \theta^ {(i)}) \ln f (z | \boldsymbol {x}, \theta) \mathrm{d} z, \tag {*1}
$$

在 $(\ast 1)$ 式中，取 $\theta = \theta^{(i)}$ 和 $\theta^{(i + 1)}$ ，得到

$$
l (\theta^ {(i)} | \boldsymbol {x}) = Q (\theta^ {(i)} | \boldsymbol {x}, \theta^ {(i)}) - \int f (z | \boldsymbol {x}, \theta^ {(i)}) \ln f (z | \boldsymbol {x}, \theta^ {(i)}) \mathrm{d} z, \tag {*2}
$$

$$
l (\theta^ {(i + 1)} | \boldsymbol {x}) = Q (\theta^ {(i + 1)} | \boldsymbol {x}, \theta^ {(i)}) - \int f (z | \boldsymbol {x}, \theta^ {(i)}) \ln f (z | \boldsymbol {x}, \theta^ {(i + 1)}) \mathrm{d} z, \tag {*3}
$$

$(*3) - (*2)$ 式得到

$$
l (\theta^ {(i + 1)} | \boldsymbol {x}) - l (\theta^ {(i)} | \boldsymbol {x})
$$

---

2.3 最大似然估计

89

$$
= Q (\theta^ {(i + 1)} | \boldsymbol {x}, \theta^ {(i)}) - Q (\theta^ {(i)} | \boldsymbol {x}, \theta^ {(i)}) - \int \ln \frac {f (z | \boldsymbol {x} , \theta^ {(i + 1)})}{f (z | \boldsymbol {x} , \theta^ {(i)})} f (z | \boldsymbol {x}, \theta^ {(i)}) \mathrm{d} z,
$$

由 EM 算法的 M 步知道, $Q(\theta^{(i+1)}|\boldsymbol{x},\theta^{(i)})-Q(\theta^{(i)}|\boldsymbol{x},\theta^{(i)})\geqslant0$ . 对于第二部分, 由 Jensen 不等式 ( $E(\ln X)\leqslant\ln E(X)$ ),

$$
\int \ln \frac {f (z | \boldsymbol {x} , \theta^ {(i + 1)})}{f (z | \boldsymbol {x} , \theta^ {(i)})} f (z | \boldsymbol {x}, \theta^ {(i)}) \mathrm{d} z \leqslant \ln \int \frac {f (z | \boldsymbol {x} , \theta^ {(i + 1)})}{f (z | \boldsymbol {x} , \theta^ {(i)})} f (z | \boldsymbol {x}, \theta^ {(i)}) \mathrm{d} z = 0,
$$

于是, 知道 $l(\theta^{(i + 1)}|\pmb{x}) - l(\theta^{(i)}|\pmb{x}) \geqslant 0$, 即得证.

此定理告诉我们，通过EM算法得到的序列 $\theta^{(i)}$ ，保证观测样本的对数似然函数$l(\theta^{(i)}|\pmb {x})$ 单增.详细的严格证明请参见Wu(1983).

如以  $\hat{\theta}$  表示 EM 算法所得到的估计, 则在某些条件下, 其渐近方差近似等于观测数据的 Fisher 信息的倒数, 即

$$
I _ {0} ^ {- 1} = \left[ - E \left(\frac {\partial^ {2} \ln f (\boldsymbol {X} | \theta)}{\partial \theta^ {2}} \Big | _ {\hat {\theta}}\right) \right] ^ {- 1}.
$$

下面考虑数据有缺失, 数据有截尾, 以及混合分布时的简单例子.

例 2.3.9 (数据缺失) 设  $X_{1}, X_{2}$  独立且服从  $Exp(\theta)$ ，且观测到  $x_{1}=5$ ，但  $x_{2}$  的值缺失。用 EM 算法求  $\theta$  的最大似然估计。

解 完全数据 $(X_{1},X_{2})$ 的对数似然函数为

$$
l (\theta | \boldsymbol {x}) = \ln f _ {X} (\boldsymbol {x} | \theta) = 2 \ln \theta - \theta x _ {1} - \theta x _ {2}.
$$

因为 $X_{1}, X_{2}$ 独立, 所以 $E[X_{2}|X_{1}, \theta^{(k)}] = E[X_{2}|\theta^{(k)}] = 1 / \theta^{(k)}$. 于是,

$$
Q (\theta | \theta^ {(k)}) = E _ {X _ {2}} [ l (\theta | X _ {1} = x _ {1}, \theta^ {(k)}) ] = 2 \ln \theta - 5 \theta - \theta / \theta^ {(k)}.
$$

M 步即求上式关于 $\theta$ 的最大值. 对上式求导, 知 $Q(\theta|\theta^{(k)})$ 关于 $\theta$ 的最大值点是 $2 / \theta - 5 - 1 / \theta^{(k)} = 0$ 的根. 于是, 得到 $\theta$ 求解的迭代方程

$$
\theta^ {(k + 1)} = \frac {2 \theta^ {(k)}}{5 \theta^ {(k)} + 1}.
$$

给定初始值后, 反复应用上述迭代公式直至收敛, 就得到了  $\hat{\theta}=0.2$  的估计.

例 2.3.10(截尾数据) 假设一种灯泡的寿命服从指数分布  $Exp(\theta)$ . 现测试了 n 个灯泡直至它们失效, 记失效的时间为  $x_{1}, x_{2}, \cdots, x_{n}$ ; 另外, 还独立进行了另一组实验, 测试了 m 个灯泡, 但是单个灯泡的失效时间没有被记录, 只记录在时刻 t 时共有 r 个灯泡失效. 试使用 EM 算法求  $\theta$  的最大似然估计.

解 不妨记这些缺失的失效时间数据为  $z_{1}, z_{2}, \cdots, z_{m}$ . 则有如下的联合对数似然函数:

$$
l (\theta | \boldsymbol {x}, \boldsymbol {z}) = n (\ln \theta - \theta \bar {x}) + \sum_ {i = 1} ^ {m} (\ln \theta - \theta z _ {i}).
$$

---

90

第二章 参数点估计

关于 Z 取条件期望, 得到

$$
\begin{array}{l} Q (\theta | \theta^ {(k)}) = E [ l (\theta | \boldsymbol {x}, \boldsymbol {z}) \mid \boldsymbol {x}, \theta^ {(k)} ] \\ = (n + m) \ln \theta - \theta \left\{n \bar {x} + (m - r) \left[ t + \frac {1}{\theta^ {(k)}} \right] + r \left[ \frac {1}{\theta^ {(k)}} - \theta^ {(k)} \right] \right\}, \\ \end{array}
$$

其中

$$
r = \frac {\exp \{- t \theta^ {(k)} \}}{1 - \exp \{- t \theta^ {(k)} \}}.
$$

由 M 步得到最大值点  $\theta^{(k+1)}$ :

$$
\theta^ {(k + 1)} = (n + m) \left\{n \bar {x} + (m - r) \left[ t + \frac {1}{\theta^ {(k)}} \right] + r \left[ \frac {1}{\theta^ {(k)}} - \theta^ {(k)} \right] \right\} ^ {- 1}. \tag * {\square}
$$

例 2.3.11 (混合模型) 设 X 服从有 g 个成分的混合分布, 其概率分布为

$$
f (x | \psi) = \sum_ {i = 1} ^ {g} \pi_ {i} f _ {i} (x | \theta_ {i}),
$$

其中  $\pi_{i}>0,\sum_{i=1}^{g}\pi_{i}=1,f_{i}(\cdot|\cdot)$  是已知的概率分布. 记  $\boldsymbol{\psi}=(\pi_{1},\pi_{2},\cdots,\pi_{g-1},\boldsymbol{\theta}^{\mathrm{T}})^{\mathrm{T}}$  和  $\boldsymbol{\theta}=(\theta_{1},\theta_{2},\cdots,\theta_{g})^{\mathrm{T}}$ . 求  $\psi$  的最大似然估计.

解 此时对数似然函数为

$$
l (\boldsymbol {\psi} | \boldsymbol {x}) = \sum_ {j = 1} ^ {n} \ln f (x _ {j} | \boldsymbol {\psi}) = \sum_ {j = 1} ^ {n} \ln \left[ \sum_ {i = 1} ^ {g} \pi_ {i} f _ {i} (x _ {j} | \theta_ {i}) \right].
$$

虽然可用常规方法求  $\psi$  的 MLE, 但由于概率分布可能比较复杂, 故下面利用 EM 算法求解. 为此, 引入潜在变量  $\mathbf{Z} = (\mathbf{Z}_{1}, \mathbf{Z}_{2}, \cdots, \mathbf{Z}_{n})^{\mathrm{T}}$ , 其中  $\mathbf{Z}_{j} = (Z_{1j}, Z_{2j}, \cdots, Z_{gj})$ , 且

$$
Z _ {i j} = \left\{ \begin{array}{l l} 1, & \text {如样本} X _ {j} \text {来自第} i \text {个成分}, \\ 0, & \text {否则}. \end{array} \right.
$$

由此可知  $Z_{1}, Z_{2}, \cdots, Z_{n}$  是来自多点分布  $\mathrm{Mult}_{g}(1, \pi)$  的独立同分布样本. 此时, 完全数据  $(X, Z)$  的对数似然函数为

$$
l (\boldsymbol {\psi} | \boldsymbol {x}, \boldsymbol {z}) = \sum_ {i = 1} ^ {g} \sum_ {j = 1} ^ {n} z _ {i j} \left[ \ln \pi_ {i} + \ln f _ {i} (x _ {j} | \theta_ {i}) \right].
$$

E 步, 即在给定 X 及  $\psi$  下, 求  $l(\psi|x,z)$  关于 Z 的条件期望:

$$
Q (\boldsymbol {\psi} | \boldsymbol {x}, \boldsymbol {\psi} ^ {(k)}) = E _ {\boldsymbol {Z}} [ l (\boldsymbol {\psi} | \boldsymbol {x}, \boldsymbol {z}) | \boldsymbol {x}, \boldsymbol {\psi} ^ {(k)} ].
$$

---

2.4 Bayes 估计

91

由Bayes公式可得到

$$
E \left[ Z _ {i j} | \boldsymbol {x}, \boldsymbol {\psi} ^ {(k)} \right] = P (Z _ {i j} = 1 | \boldsymbol {x}, \boldsymbol {\psi} ^ {(k)}) = \tau_ {i} (x _ {j} | \boldsymbol {\psi} ^ {(k)}),
$$

其中

$$
\begin{array}{l} \tau_ {i} (x _ {j} | \boldsymbol {\psi} ^ {(k)}) = \pi_ {i} ^ {(k)} f _ {i} (x _ {j} | \theta_ {i} ^ {(k)}) / f (x _ {j} | \boldsymbol {\psi} ^ {(k)}) \\ = \pi_ {i} ^ {(k)} f _ {i} (x _ {j} | \theta_ {i} ^ {(k)}) / \sum_ {h = 1} ^ {g} \pi_ {h} ^ {(k)} f _ {h} (x _ {j} | \theta_ {h} ^ {(k)}). \\ \end{array}
$$

则条件期望可写为

$$
Q (\boldsymbol {\psi} | \boldsymbol {x}, \boldsymbol {\psi} ^ {(k)}) = \sum_ {i = 1} ^ {g} \sum_ {j = 1} ^ {n} \tau_ {i} (x _ {j} | \boldsymbol {\psi} ^ {(k)}) \left[ \ln \pi_ {i} + \ln f _ {i} (x _ {j} | \theta_ {i}) \right].
$$

M 步, 可求得

$$
\pi_ {i} ^ {(k + 1)} = \sum_ {j = 1} ^ {n} \tau_ {i} (x _ {j} | \boldsymbol {\psi} ^ {(k)}) / n,
$$

而  $\psi$  中的剩余部分  $\theta$  的第  $(k+1)$  个估计, 可通过极大化下式求得:

$$
\boldsymbol {\theta} ^ {(k + 1)} = \arg \max _ {\boldsymbol {\theta}} \sum_ {i = 1} ^ {g} \sum_ {j = 1} ^ {n} \tau_ {i} (x _ {j} | \boldsymbol {\psi} ^ {(k)}) \ln f _ {i} (x _ {j} | \theta_ {i}).
$$

关于 EM 算法的更多介绍可参见王兆军等 (2023). 实际应用 EM 算法时, 如果其 E 步计算比较困难, 则可采用下面的 Monte Carlo(蒙特卡罗) EM 算法: 由于此时知道潜在变量 Z 在给定 X 及  $\theta = \theta^{(i)}$  时的分布, 故可用随机模拟近似其期望, 即 E 步由下面两步组成, 其 M 步仍然如 (2.3.11) 式:

E1 步: 由 Z 的条件分布  $f(z|x,\theta^{(i)})$  抽取 m 个随机数  $z_{1}, z_{2}, \cdots, z_{m}$ ;

E2 步: $Q(\theta | \boldsymbol{x}, \theta^{(i)}) = \frac{1}{m} \sum_{k=1}^{m} l(\theta | \boldsymbol{x}, z_k)$.

## 2.4 Bayes 估计

在前述所有内容中, 我们均假设参数  $\theta$  是给定的一个未知常数, 但知道它在某个区域, 即参数空间中取值. 然而, 在某些实际问题中, 我们对参数  $\theta$  可能会有一定了解, 比如某产品的次品率 p, 虽说它的参数空间为  $(0,1)$ , 但基于对这种产品已有的认知, p 可能在 0.05 左右. 然而, 我们在前面讲述的所有方法中, 均无法利用这一信息. 本节讲述的 Bayes 方法则将充分考虑这一点.

---

92

第二章 参数点估计

## 2.4.1 Bayes 公式

Bayes 方法来自概率论中学过的 Bayes 公式: 对于  $k+1$  随机事件  $A, H_{1}, H_{2}, \cdots, H_{k}$ ，设  $H_{1}, H_{2}, \cdots, H_{k}$  互斥，且  $\bigcup_{i=1}^{k} H_{i}$  为必然事件，则

$$
P (H _ {i} | A) = \frac {P (H _ {i} \cap A)}{P (A)} = \frac {P (H _ {i}) P (A | H _ {i})}{\sum_ {j = 1} ^ {k} P (H _ {j}) P (A | H _ {j})}, i = 1, 2, \dots , k.
$$

在概率论中, $P(H_{i})$ 称为随机事件 $H_{i}$ 的先验 (prior) 概率, $P(H_{i}|A)$ 称为事件 $A$ 发生下的后验 (posterior) 概率. 上述 Bayes 公式来自 Richard Price (普赖斯, 1723—1791) 于 1763 年在英国皇家学会上宣读的 Thomas Bayes 之文章《机遇理论中一个问题的解》, 后来该文在著名期刊 Biometrika 上重新刊登, 参见 Bayes (1958).

下面通过一个例子看 Bayes 公式的应用.

例2.4.1 假设一道选择题有四个选项, 全班只有 $5\%$ 的学生会做, 且给出正确答案的概率为0.99. 假设如果学生不会做, 就随机猜答案. 计算一个学生答案正确而是猜对的概率.

解 以 A 表示此学生随机猜答案, 以 B 表示答案正确. 则由题意知

$$
P (B | A) = 0. 2 5, \quad P (B | \bar {A}) = 0. 9 9.
$$

由 Bayes 公式, 此学生答案正确而是猜对的概率为

$$
\begin{array}{l} P (A | B) = \frac {P (A) P (B | A)}{P (A) P (B | A) + P (\bar {A}) P (B | \bar {A})} \\ = \frac {0 . 9 5 \times 0 . 2 5}{0 . 9 5 \times 0 . 2 5 + 0 . 0 5 \times 0 . 9 9} = 0. 8 2 7 5. \\ \end{array}
$$

对于上例, 由 Bayes 公式算得学生答案正确而是猜对的概率为 $82.75\%$, 显然高了些, 这也说明此题有点难. 如果把难度降低到: 全班有 $90\%$ 的学生会做, 则答案正确而是猜对的概率降为 0.0273.

## 2.4.2 Bayes 估计

从形式上看, Bayes 公式只是条件概率的简单应用, 但它却包含了归纳推理的思想. 基于此思想, 后来学者发展形成了一套统计推断的系统理论与方法, 统称为 Bayes 统计.

Bayes 统计与前述统计方法的基本假设有如下两个关键不同:

(1) 假设参数 $\theta$ 是随机变量, 且称它所服从的分布为先验分布. 其原因是对参数 $\theta$ 已经积累了一些有用信息, 即关于 $\theta$ 的先验信息, 且随着对信息积累的不同, 其取值也理应发生变化, 故可用随机变量来衡量此信息.

---

2.4 Bayes 估计

93

(2) 把总体 X 的概率分布  $f(x; \theta)$  理解为给定  $\theta$  下的条件概率分布, 并改记为  $f(x|\theta)$ . 这是由于对不同的  $\theta$  值,  $f(x; \theta)$  对应着不同的概率分布; 另外, 总体分布的概率意义为: 对于给定的参数值, 它反映着抽取样本值 x 的概率.

于是, 当有 n 个来自总体  $X \sim f(x|\theta)$  的样本时, 关于参数  $\theta$  的信息来自三个方面: (1) 先验分布  $\pi(\theta)$ ; (2) 总体分布  $f(x|\theta)$ ; (3) 样本  $X_{1}, X_{2}, \cdots, X_{n}$ . Bayes 统计的目的就在于如何利用上述三类信息, 对  $\theta$  进行统计推断. 本节仅讲述关于参数  $\theta$  的 Bayes 估计初步. 有关 Bayes 统计的详细内容, 请有兴趣的读者参见 Berger (1985).

设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $X \sim f(x|\theta)$  的样本,  $\pi(\theta)$  为  $\theta$  的先验分布, 样本分布为  $f(\boldsymbol{x}|\theta)$ , 则样本  $X_{1}, X_{2}, \cdots, X_{n}$  与  $\theta$  的联合分布为

$$
f (\boldsymbol {x}, \theta) = f (\boldsymbol {x} | \theta) \pi (\theta).
$$

由于此时关注的问题在于, 有了样本后如何估计  $\theta$ , 故基于上面的联合分布, 可得到给定样本  $X_{1}, X_{2}, \cdots, X_{n}$  后,  $\theta$  的条件分布:

$$
\pi (\theta | \boldsymbol {x}) = \frac {f (\boldsymbol {x} , \theta)}{f (\boldsymbol {x})} = \frac {f (\boldsymbol {x} | \theta) \pi (\theta)}{\int_ {\Theta} f (\boldsymbol {x} | \theta) \pi (\theta) \mathrm{d} \theta}, \tag {2.4.1}
$$

称之为  $\theta$  的后验分布, 其中  $f(x)$  称为样本的边际分布.

我们可以根据  $\theta$  的后验分布 (2.4.1), 对  $\theta$  进行统计推断. 此时, 参数  $\theta$  的 Bayes 估计包括如下几种:

(1) 取后验分布  $\pi(\theta|x)$  的最大值, 即众数作为  $\theta$  的估计, 称之为众数型的 Bayes 估计.
(2) 取后验分布  $\pi(\theta|x)$  的中位数作为  $\theta$  的估计, 称之为中位数型的 Bayes 估计.
(3) 取后验分布  $\pi(\theta|x)$  的期望作为  $\theta$  的估计, 称之为期望型的 Bayes 估计.

在上述三种类型的 Bayes 估计中, 期望型的 Bayes 估计最为常用, 故后面将采用后验期望作为  $\theta$  的 Bayes 估计, 即

$$
\hat {\theta} _ {B} (\boldsymbol {X}) = E (\theta | \boldsymbol {X}) = \int_ {\Theta} \theta \pi (\theta | \boldsymbol {X}) \mathrm{d} \theta . \tag {2.4.2}
$$

把后验分布代入上式即得到  $\theta$  的 Bayes 估计:

$$
\hat {\theta} _ {B} (\boldsymbol {X}) = \frac { \int_ {\Theta} \theta f (\boldsymbol {X} | \theta) \pi (\theta) \mathrm{d} \theta}{ \int_ {\Theta} f (\boldsymbol {X} | \theta) \pi (\theta) \mathrm{d} \theta}. \tag {2.4.3}
$$

(2.4.1) 或 (2.4.3) 式显示, 不同先验分布将得到不同的 Bayes 估计. 因此, 如何选取先验分布就是 Bayes 统计的一个重要挑战. 另外, 在求取 Bayes 估计时, 还将面临积分

---

94

第二章 参数点估计

计算问题. 如果参数维数高, 特别是现在流行的大模型中, 参数的维数非常高, 则涉及高维积分的计算问题.

从 (2.4.3) 式可以看出, 在求 Bayes 估计时, 不必要求 $\int \pi(\theta) \mathrm{d}\theta = 1$, 即 $\pi(\theta)$ 为标准的概率分布. 实际上, 在许多实际问题中, 应用者可能并不能确定先验分布如何选取, 或没有先验信息, 此时, 一个广泛采用的先验就是 “同等无知” 或 “无信息” 先验, 即均匀分布, 或在无穷区间上取定值 1.

例2.4.2 对于例1.2.1的次品率估计问题, 即设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $B(1, p)$  的独立同分布样本, 求次品率 p 的 Bayes 估计.

解 如果事先对次品率没有任何有用信息, 则可采用 “无信息” 先验: 考虑到  $p \in (0,1)$ , 故可取  $U(0,1)$  上的均匀分布作为先验, 即  $\pi(p) = I_{(0,1)}(p)$ . 由题意知

$$
f (\boldsymbol {x} | p) = p ^ {\sum_ {i = 1} ^ {n} x _ {i}} (1 - p) ^ {n - \sum_ {i = 1} ^ {n} x _ {i}},
$$

故

$$
f (\boldsymbol {x}, p) = p ^ {\sum_ {i = 1} ^ {n} x _ {i}} (1 - p) ^ {n - \sum_ {i = 1} ^ {n} x _ {i}} I _ {(0, 1)} (p),
$$

由此可求得

$$
f (\boldsymbol {x}) = \int_ {0} ^ {1} p ^ {\sum_ {i = 1} ^ {n} x _ {i}} (1 - p) ^ {n - \sum_ {i = 1} ^ {n} x _ {i}} \mathrm{d} p = \beta (n \bar {x} + 1, n - n \bar {x} + 1),
$$

其中  $\beta(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$  为  $\beta$  函数.

于是, p 的后验分布为

$$
\pi (p | \boldsymbol {x}) = \frac {\Gamma (n + 2)}{\Gamma (n \bar {x} + 1) \Gamma (n - n \bar {x} + 1)} p ^ {n \bar {x}} (1 - p) ^ {n - n \bar {x}}, \tag {2.4.4}
$$

由此求得 $p$ 的Bayes估计为

$$
\hat {p} _ {B} = \int_ {0} ^ {1} p \pi (p | \boldsymbol {x}) \mathrm{d} p = \frac {n \bar {x} + 1}{n + 2}. \tag {2.4.5}
$$

□

关于 $p$ 的估计, 前面给出的无偏估计、UMVUE、MLE 均为 $\hat{p}_{ML} = \bar{X}$, 且它也是 BAN 估计. Bayes 估计与频率估计虽然都是样本均值的函数, 但形式略有不同, 表 2.4.1 列出了几种情况下的数值比较.

---

2.4 Bayes 估计

95

表 2.4.1 次品率的两个估计比较

| 情况 | n | $\sum_{i=1}^{n}x_i$ | $\hat{p}_{ML}$ | $\hat{p}_B$ |
| --- | --- | --- | --- | --- |
| 1 | 5 | 5 | 1 | 0.857 |
| 2 | 20 | 20 | 1 | 0.955 |
| 3 | 5 | 0 | 0 | 0.143 |
| 4 | 20 | 0 | 0 | 0.045 |

从表 2.4.1 可以看出:当抽取 5 个产品都为次品时，次品率 p 的最大似然估计与 Bayes 估计分别为 1 和 0.857，而当抽取 20 个也都为次品时，p 的最大似然估计与 Bayes 估计分别为 1 和 0.955。直观来看，抽 20 个产品比抽 5 个产品的检测结果的可信度应有所不同。由此可见，此时的 Bayes 估计更符合我们的心理预期。

## 2.4.3 共轭先验

关于先验分布的选取, 常用方法包括:

(1) 客观法: 利用历史资料提供的关于  $\theta$  的信息确定先验分布.
(2) 主观法: 依研究者或应用者主观选择一个先验分布.
(3) 无信息先验 (noninformative prior): 不包含参数 $\theta$ 的任何信息的先验. 当 $\theta$ 离散且取两个值时, 赋予这两个值各 $1/2$ 概率的先验就是一个无信息先验. 这里经常遵循的一个常用原则就是“同等无知”: 以同等概率赋予参数空间 $\Theta$ 内每一个值.
(4) 共轭先验 (conjugate prior): 设 $\mathcal{F}$ 为 $\theta$ 的一个分布族, 如对任一样本 $X$, 只要先验分布 $\pi \in \mathcal{F}$, 后验分布就属于 $\mathcal{F}$, 则称 $\mathcal{F}$ 为共轭先验分布族.

客观法的好处在于有频率解释, 实际工作者乐于接受; 主观法的好处在于用到了先验, 但又没有特殊对待; 共轭先验的好处是便于计算, 由于从后验分布的定义可能看出, 后验分布的形式依赖于先验与总体分布. 常用的共轭先验分布有:

(1) 当总体分布为两点分布  $B(1,\theta)$  时, 共轭先验分布为如下的  $\beta$  分布  $Beta(a,b)$ :

$$
\pi (\theta) = \frac {\Gamma (a + b)}{\Gamma (a) \Gamma (b)} \theta^ {a - 1} (1 - \theta) ^ {b - 1}, \theta \in [ 0, 1 ], a > 0, b > 0.
$$

此时的后验分布为  $Beta(n\bar{x}+a,n-n\bar{x}+b)$ .

(2) 当总体分布为 Poisson 分布  $P(\theta)$  时, 共轭先验分布为  $\Gamma(a,b)$ . 此时后验分布为  $\Gamma(n\bar{x}+a,n+b)$ .
(3) 当总体分布为 $N(\mu, \sigma^2)$ 时 ($\sigma$ 已知), 共轭先验分布为 $N(\mu_0, \tau^2)$. 此时后验分布为 $N\left(\frac{\tau^2 \bar{x} + \mu_0 \sigma^2 / n}{\tau^2 + \sigma^2 / n}, \frac{\sigma^2 \tau^2}{n \tau^2 + \sigma^2}\right)$.

---

96

第二章 参数点估计

(4) 当总体分布为  $N(\mu, \sigma^{2})$  时 ( $\mu$  已知), 共轭先验分布为如下的逆  $\Gamma$  分布  $IG(\alpha, \lambda)$ :

$$
\pi (\sigma^ {2}) = \frac {\lambda^ {\alpha}}{\Gamma (\alpha)} \frac {1}{\sigma^ {2 (\alpha + 1)}} \exp \{- \lambda / \sigma^ {2} \}.
$$

此时, 后验分布为  $IG(\alpha + n/2, \lambda + \sum_{i=1}^{n}(x_i - \mu)^2/2)$ .

(5) 当总体分布为正态分布  $N(\mu, \sigma^{2})$  时，参数  $(\mu, \sigma^{2})$  的共轭先验分布的概率密度为

$$
\pi (\mu , \sigma) = \sigma^ {a - 1} \exp \{- b / (2 \sigma^ {2}) \} \exp \{- \tau (\mu - \nu) ^ {2} / (2 \sigma^ {2}) \},
$$

记之为 $D(a,b,\nu ,\tau)$ .当 $a <   - 1$ 时，它是标准的，否则就是广义分布.此时， $\mu ,\sigma$ 的后验分布为 $D(a - n,b + s^2,(n\bar{x} +\nu \tau) / (n + \tau),n + \tau)$

(6) 当总体为均匀分布  $U(0,\theta)$  时, 共轭先验分布为 Pareto 分布  $Pa(\beta,\alpha)$ :

$$
\pi (\theta) = \frac {\alpha \beta^ {\alpha}}{\theta^ {\alpha + 1}} I _ {[ \beta , \infty)} (\theta).
$$

此时, 后验分布为  $Pa(\alpha + n, \max\{x_{1}, x_{2}, \cdots, x_{n}, \beta\})$ .

在例 2.4.2 中, 如果取共轭先验为  $\beta$  分布  $\mathrm{Beta}(\alpha,\beta)$ , 即

$$
\pi (p) = \frac {\Gamma (\alpha + \beta)}{\Gamma (\alpha) \Gamma (\beta)} p ^ {\alpha - 1} (1 - p) ^ {\beta - 1}, 0 \leqslant p \leqslant 1, \alpha > 0, \beta > 0,
$$

即例 2.4.2 中的无信息先验为上述共轭先验的特例, 则此时的后验分布为

$$
\pi (p | \boldsymbol {x}) = \frac {\Gamma (\alpha + \beta + n)}{\Gamma (\alpha + n \bar {x}) \Gamma (\beta + n - n \bar {x})} p ^ {\alpha + n \bar {x} - 1} (1 - p) ^ {\beta + n - n \bar {x} - 1},
$$

它仍然是 $\beta$ 分布 $Beta(\alpha + n\bar{x}, \beta + n - n\bar{x})$. 此时的Bayes估计为

$$
\hat {p} _ {B} = \frac {\alpha + n \bar {x}}{\alpha + \beta + n}. \tag {2.4.6}
$$

如取  $\alpha = \beta = 1$ ，则得到了形如 (2.4.4) 式的后验分布和形如 (2.4.5) 式的 Bayes 估计.

例 2.4.3 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自正态总体  $N(\mu, \sigma_{0}^{2})$  的独立同分布样本, 其中  $\sigma_{0}^{2}$  已知. 如取共轭先验分布为  $N(\mu_{0}, \tau^{2})$ , 其中  $\mu_{0}, \tau$  已知, 求  $\mu$  的 Bayes 估计.

解 由前面给出的共轭先验可知, 此时  $\mu$  的 Bayes 估计为

$$
\hat {\mu} _ {B} = \frac {\tau^ {2}}{\tau^ {2} + \sigma_ {0} ^ {2} / n} \bar {X} + \frac {\sigma_ {0} ^ {2} / n}{\tau^ {2} + \sigma_ {0} ^ {2} / n} \mu_ {0}. \tag {2.4.7}
$$

从上式可以看出, 此时的 Bayes 估计是样本均值和先验均值的加权平均, 而权重是样本均值的方差及先验方差之和. □

---

2.5 minimax 估计

97

## 2.4.4 经验Bayes

从前面内容可以看出, Bayes 估计强烈依赖先验分布或先验分布中的参数. 在文献中, 先验分布中的参数被称为超参数 (hyperparameter). 如果这些超参数已知, 则利用前述方法可以得到参数的 Bayes 估计. 但多数情况下, 这些超参数并不已知, 此时如何估计先验分布中的这些未知参数呢? 一般情况下, 有如下几种处理方法.

## 1. 经验 Bayes

经验 Bayes(empirical Bayes, 简记为 EB) 方法首先由 H. Robbins (罗宾斯, 1915—2001) 提出的, 参见 Robbins (1956). 为了较清楚地表达, 我们记参数 $\theta$ 的先验分布为 $\pi(\theta|\eta)$, 其中 $\eta$ 为超参数, 此时参数 $\theta$ 的后验分布为

$$
\pi (\theta | \boldsymbol {x}, \eta) = \frac {f (\boldsymbol {x} | \theta) \pi (\theta | \eta)}{\int f (\boldsymbol {x} | \theta) \pi (\theta | \eta) \mathrm{d} \theta} = \frac {f (\boldsymbol {x} | \theta) \pi (\theta | \eta)}{m (\boldsymbol {x} | \eta)}. \tag {2.4.8}
$$

如果采用共轭先验, 则  $m(\boldsymbol{x}|\eta)$  有解析表达式, 它表示给定超参数  $\eta$  下样本的边际分布. 于是, 基于此边际分布, 记超参数  $\eta$  的最大似然估计为  $\hat{\eta}$ . 由此就得到超参数的估计, 也就可以利用  $\pi(\theta|\boldsymbol{x},\hat{\eta})$  作为后验分布求取 Bayes 估计了.

## 2. BEB(Bayes 经验 Bayes)

假设先验分布中的超参数  $\eta \sim h(\eta|\lambda)$ ，其中  $\lambda$  为超参数分布中的参数。此时，后验分布为

$$
\begin{array}{l} \pi (\theta | \boldsymbol {x}, \lambda) = \frac { \int f (\boldsymbol {x} | \theta) \pi (\theta | \eta) h (\eta | \lambda) \mathrm{d} \eta}{  \iint f (\boldsymbol {x} | \theta) \pi (\theta | \eta) h (\eta | \lambda) \mathrm{d} \theta \mathrm{d} \eta} \\ = \int \pi (\theta | \boldsymbol {x}, \eta) h (\eta | \boldsymbol {x}, \lambda) \mathrm{d} \eta . \tag {2.4.9} \\ \end{array}
$$

上一后验分布是给定  $\eta$  下 (2.4.8) 式的后验分布与给定数据 x 后更新的超参数先验的混合. 一般情况下, 多假设超参数的分布已知, 而不包含参数.

## 2.5 minimax 估计

前述的估计准则与方法, 均是利用样本推断总体中的未知参数, 而不是从统计决策角度讲述的. 统计决策理论是由 A. Wald (沃尔德, 1902—1950) 提出的, 参见 Wald (1950). 这套理论的基本观点与方法已渗入统计的多个分支, 以及机器学习中.

---

98

第二章 参数点估计

统计决策有三个要素: 样本空间 X 及定义在样本空间上的分布族  $\{P_{\theta}: \theta \in \Theta\}$ ，行动空间或决策空间 A，和定义在  $\Theta \times A$  上的非负损失函数  $L(\theta, a)$ .

对于前述的点估计, 假设  $g(\theta)$  是待估参数, 如其决策空间为 R, 则一个常用的损失函数为如下的二次损失:

$$
L (\theta , a) = [ g (\theta) - a ] ^ {2}, \quad \theta \in \Theta , a \in \mathcal {A} = \mathbb {R}. \tag {2.5.1}
$$

一个有用的决策理应是 n 个样本  $X_{1}, X_{2}, \cdots, X_{n}$  的函数, 记之为  $\delta(X_{1}, X_{2}, \cdots, X_{n})$ , 此时其损失函数也是样本  $X_{1}, X_{2}, \cdots, X_{n}$  的函数, 由于样本是随机的, 故定义如下的平均损失, 即风险函数.

定义 2.5.1 (风险函数) 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $X \sim f(x; \theta)$  的样本, 则称

$$
R (\theta , \delta) = E _ {\theta} [ L (\theta , \delta (X _ {1}, X _ {2}, \dots , X _ {n})) ] = \int L (\theta , \delta (\boldsymbol {x})) f (\boldsymbol {x}; \theta) \mathrm{d} \boldsymbol {x}, \theta \in \Theta \tag {2.5.2}
$$

为决策  $\delta$  的风险函数.

如取 (2.5.1) 式的平方损失, 则决策 $\delta(X)$ 的风险就是其均方误差. 如果 $\delta(X)$ 是 $g(\theta)$ 的无偏估计, 则其风险就是方差. 由此可见, 风险是度量用决策 $\delta(X)$ 估计 $g(\theta)$ 好坏的一个标准. 从风险大小准则来看, 一个最好的估计, 应该具有最小的风险, 这即下面的容许性定义.

定义 2.5.2 (容许性) 对于决策  $\delta$ ，如果存在一个决策  $\delta^{*}$ ，严格一致地优于  $\delta$ ，即

$$
R (\theta , \delta) \geqslant R (\theta , \delta^ {*}), \forall \theta \in \Theta ,
$$

且对某些参数值不等号严格成立，则称决策 $\delta$ 是不容许的，否则就称为容许的.

容许性研究是统计学理论中最困难的课题之一, 也产生了许多有趣的现象, 如高维时的 Stein 现象等. 这里仅在后面简单给出其与 minimax 估计间的关系.

定义 2.5.3 (Bayes 风险、Bayes 估计) 设  $\theta$  有先验分布  $\pi(\theta)$ ，称

$$
R _ {\pi} (\delta) = \int R (\theta , \delta) \pi (\theta) \mathrm{d} \theta \tag {2.5.3}
$$

为决策 $\delta$ 的Bayes风险.如果决策 $\delta_{\pi}$ 满足

$$
R _ {\pi} (\delta_ {\pi}) \leqslant R _ {\pi} (\delta), \quad \forall \delta ,
$$

则称  $\delta_{\pi}$  为  $g(\theta)$  的 Bayes 估计.

关于上节的 Bayes 估计, 我们可以从统计决策角度如下叙述: 期望型的 Bayes 估计, 实际上是二次损失时的 Bayes 估计. 如取损失为如下的绝对值:

$$
L (\theta , \delta) = E _ {\theta} [ | g (\theta) - \delta (\boldsymbol {X}) | ],
$$

---

2.5 minimax 估计

99

则中位数型的 Bayes 估计就是此时的 Bayes 估计. 在不引起混淆的情况下, 本节后面所讲的 Bayes 估计均指平方损失下 Bayes 风险最小的决策.

如果没有先验, 为了避免最坏情况的发生, 我们给出如下的 minimax 估计的定义.

定义2.5.4(minimax估计) 记 $M(\delta) = \sup_{\theta} R(\theta, \delta)$. 如果决策 $\delta_0$ 满足

$$
M (\delta_ {0}) \leqslant M (\delta), \forall \delta \in \mathcal {A},
$$

则称  $\delta_{0}$  为  $g(\theta)$  的 minimax 估计.

从 minimax 估计的定义可以看出, minimax 估计就是最大风险最小化的估计. 求解参数 $g(\theta)$ 的 minimax 估计, 相当于在决策空间 $\mathcal{A}$ 中求 $M(\delta)$ 的最小值点. 而由于 $M(\delta)$ 是一元函数, 故一般来说, minimax 估计存在, 但具体求解并不容易. 目前讨论比较多的求解方法一般有两种: 一种是基于 Bayes 方法, 另一种是基于同变估计而展开的. 由于我们并没有涉及同变估计, 故下面仅简单介绍第一种方法.

由于 minimax 估计依赖于损失函数的选取, 故为了易于求取其最大值, 多假设损失函数为凸函数. 对于任意给定的 $\theta \in \Theta$, 称 $L(\theta, \cdot)$ 为凸函数, 是指 $L(\theta, A)$ 是 $\mathcal{A}$ 上的凸函数. 平方损失 $L(\theta, a) = [g(\theta) - a]^2$ 就是凸损失中的重要例子.

Bayes 估计与 minimax 估计间的关系有如下结论:

定理2.5.1 设 $\pi$ 为标准的先验分布, $\delta_{\pi}$ 为 $g(\theta)$ 的Bayes估计, 且其风险函数$R(\theta ,\delta_{\pi})$ 在参数空间 $\Theta$ 上恒等于常数, 则 $\delta_{\pi}$ 为 $g(\theta)$ 的minimax估计. 如果 $\delta_{\pi}$ 是先验分布 $\pi$ 下唯一的Bayes估计, 则它也是唯一的minimax估计.

证明 设  $\delta$  为任一估计, 则

$$
M (\delta) \geqslant \int_ {\Theta} R (\theta , \delta) \pi (\theta) \mathrm{d} \theta \geqslant \int_ {\Theta} R (\theta , \delta_ {\pi}) \pi (\theta) \mathrm{d} \theta = M (\delta_ {\pi}),
$$

第一个结论得证. 又如果 $\delta_{\pi}$ 是唯一的Bayes估计, 则上面的第二个 $\geqslant$ 由 $>$ 代替, 因而 $\delta_{\pi}$ 也是唯一的 minimax 估计. □

关于容许性与 minimax 估计之间, 有如下的结论:

定理2.5.2 设 $\delta$ 是 $g(\theta)$ 的容许估计, 且风险函数为常数 $c$, 则 $\delta$ 是 $g(\theta)$ 的 minimax 估计. 如果损失函数是严格凸的, 则 $\delta$ 是唯一的 minimax 估计.

证明 设 $\delta$ 是容许估计, 但不是其 minimax 估计, 则存在另一估计 $\delta_0$, 使得

$$
M (\delta_ {0}) <   M (\delta).
$$

由于  $\delta$  的风险函数为常数, 则有

$$
R (\theta , \delta_ {0}) \leqslant M (\delta_ {0}) <   M (\delta) = R (\theta , \delta), \forall \theta \in \Theta ,
$$

与  $\delta$  是容许估计矛盾.

---

100

第二章 参数点估计

设损失函数严格凸, 且 $\delta_0$ 是另一 minimax 估计, 则

$$
R (\theta , (\delta + \delta_ {0}) / 2) <   \frac {1}{2} [ R (\theta , \delta) + R (\theta , \delta_ {0}) ] = c = R (\theta , \delta), \forall \theta \in \Theta ,
$$

与  $\delta$  为容许估计矛盾. 故  $\delta$  唯一.

![](../../raw/pages_0113-0128/images/page_112_image_5.jpg)

由此定理, 我们有如下推论.

推论 2.5.1 如果在某标准先验下的 Bayes 估计是唯一的, 且有常数风险, 则必为容许的 minimax 估计.

例 2.5.1 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $X \sim B(1, \theta)$  的独立同分布样本，取二次损失函数  $L(\theta, a) = (\theta - a)^{2}$ ，先验分布为 Beta(a, b) 时，求其 Bayes 估计的风险。当  $a = \sqrt{n}/2, b = \sqrt{n}/2$  时，求  $\theta$  的 minimax 估计。

解 由上节的 (2.4.6) 式知, 此时  $\theta$  的 Bayes 估计为

$$
\hat {\theta} _ {B} = \frac {n \bar {X} + a}{n + a + b},
$$

其风险为

$$
R (\theta , \hat {\theta} _ {B}) = E _ {\theta} \left[ \left(\theta - \frac {n \bar {X} + a}{n + a + b}\right) ^ {2} \right] = \frac {n \theta (1 - \theta) + [ (a + b) \theta - a ] ^ {2}}{(n + a + b) ^ {2}}.
$$

当 $a = \sqrt{n} / 2, b = \sqrt{n} / 2$ 时，代入上面两式得到，Bayes估计为

$$
\hat {\theta} _ {B} = \frac {n \bar {X} + \sqrt {n} / 2}{n + \sqrt {n}},
$$

其风险

$$
R (\theta , \hat {\theta} _ {B}) = E _ {\theta} \left[ \left(\theta - \frac {n \bar {X} + \sqrt {n} / 2}{n + \sqrt {n}}\right) ^ {2} \right] = \frac {1}{4 (1 + \sqrt {n}) ^ {2}}, \tag {2.5.4}
$$

由于其风险为常数, 故知  $\hat{\theta}_{B}$  是  $\theta$  的 minimax 估计. 且由定理 2.5.2 和推论 2.5.1 知, 此 minimax 估计是容许估计, 也是唯一的. □

对于上例, $\theta$ 的 UMVUE 为 $\hat{\theta} = \bar{X}$, 其此时的风险为 $R(\theta, \hat{\theta}) = \theta(1 - \theta)/n$. 与 (2.5.4) 式比较可以看到, 当

$$
\left| \theta - \frac {1}{2} \right| <   \frac {1}{2} \sqrt {1 - \frac {n}{(1 + \sqrt {n}) ^ {2}}}
$$

时, minimax 估计比样本均值有较小的风险, 但二者风险最大差也只是 $\frac{2\sqrt{n} + 1}{4(n + \sqrt{n})^2}$. 由此可见, 随着 $n$ 的增大, minimax 估计比频率估计好的参数区间长度越来越短, 且二者风险之差也越来越小. 这也表明 minimax 估计是保守的, 它旨在降低最坏情况出现时可能遇到的风险, 但其代价就是通常情况下表现并不理想.

---

2.5 minimax 估计

101

当 n = 100 时, 二者的风险函数如图 2.5.1 所示, 其中风险值扩大了 484 倍, 虚线为 minimax 估计的风险函数, 实线为 UMVUE 的风险函数. 此时, minimax 估计优于样本均值的参数区间为  $(0.5 \pm 0.2083)$ , 且二者最大差距为  $4.34 \times 10^{-4}$ ; 当 n = 1000 时, minimax 估计优于样本均值的参数区间为  $(0.5 \pm 0.1228)$ , 二者最大差距为  $1.51 \times 10^{-5}$ . 可见, 当 n 较大时, minimax 相较于样本均值的风险优势并不明显.

![](../../raw/pages_0113-0128/images/page_113_chart_3.jpg)

<details>
<summary>line</summary>

| \(\theta\) | 风险函数 \(R \times 484\) |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | ~0.75 |
| 0.3 | 1.0 |
| 0.5 | 1.2 |
| 0.7 | 1.0 |
| 1.0 | 0.0 |
</details>

图2.5.1 minimax估计与UMVUE的风险函数

定理 2.5.2 要求 Bayes 估计的风险为常数, 但这一点并不满足时, 我们无法利用此结论来求取 minimax 估计. 此时, 我们可以利用如下定理.

定理 2.5.3 设  $\{\pi_{k}\}$  是标准的先验分布列,  $\delta_{k}$  为先验  $\pi_{k}$  时的 Bayes 估计, 如果估计  $\delta$  满足

$$
\infty > M (\delta) \leqslant \operatorname * {l i m s u p} _ {k \to \infty} R _ {\pi_ {k}} (\delta_ {k}) = c <   \infty , \tag {2.5.5}
$$

则  $\delta$  为 minimax 估计, 其中  $R_{\pi_{k}}(\delta_{k})$  为决策  $\delta_{k}$  的 Bayes 风险, c 为常数.

证明 如果 $\delta$ 不是 minimax 估计, 则存在 $\delta^{*}$, 使得 $M(\delta^{*}) < M(\delta)$. 于是, 由条件 (2.5.5) 知, 存在正整数 $K$, 使

$$
M (\delta^ {*}) <   R _ {\pi_ {K}} (\delta_ {K}).
$$

又由  $M(\delta^{*})$  的定义知,  $R_{\pi_{K}}(\delta^{*}) \leqslant M(\delta^{*})$ , 故综合上述有

$$
R _ {\pi_ {K}} (\delta^ {*}) \leqslant M (\delta^ {*}) <   R _ {\pi_ {K}} (\delta_ {K}),
$$

与  $\delta_{K}$  为 Bayes 估计矛盾.

例 2.5.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $N(\mu, \sigma^{2})$  的独立同分布样本, 其中  $\sigma^{2} > 0$  已知, 取平方损失  $L(\mu, a) = (\mu - a)^{2}$ , 证明样本均值  $\bar{X}$  是  $\mu$  的 minimax 估计.

证明 取先验分布列 $\{\pi_k: \mu \sim N(0, k^2)\}$. 由 (2.4.7) 式可知, 此时的 Bayes 估计为

$$
\delta_ {k} = \frac {k ^ {2}}{k ^ {2} + \sigma^ {2} / n} \bar {X},
$$

---

102

第二章 参数点估计

其风险函数

$$
R (\mu , \delta_ {k}) = E [ (\delta_ {k} - \mu) ^ {2} ] = \frac {n k ^ {4} \sigma^ {2} + \sigma^ {4} \mu^ {2}}{(n k ^ {2} + \sigma^ {2}) ^ {2}},
$$

由此求得其 Bayes 风险为

$$
R _ {k} (\delta_ {k}) = E _ {\mu} [ R (\mu , \delta_ {k}) ] = \frac {\sigma^ {2} k ^ {2}}{n k ^ {2} + \sigma^ {2}} \longrightarrow \frac {\sigma^ {2}}{n}, k \to \infty .
$$

由于  $\bar{X}$  的风险函数, 即方差为  $\frac{\sigma^{2}}{n}$ , 满足条件 (2.5.5), 故由定理 2.5.3 知, 样本均值  $\bar{X}$  是  $\mu$  的 minimax 估计. □

## 习题二

1. 对于 n 个常数  $a_{1}, a_{2}, \cdots, a_{n}$ ，取  $l(x) = \sum_{i=1}^{n} |x - a_{i}|$ ，证明: $l(x)$  的最小值点为  $a_{1}, a_{2}, \cdots, a_{n}$  的中位数。如取  $l(x) = \sum_{i=1}^{n} (x - a_{i})^{2}$ ，则  $l(x)$  的最小值点为  $\sum_{i=1}^{n} a_{i}/n$ 。
2. 设 $X_{1} \sim N(\mu_{1}, 1)$, $X_{2} \sim N(\mu_{2}, 1)$ 且相互独立, 其中 $\mu_{1}, \mu_{2} \in \mathbb{R}$. 记 $\theta = \max\{\mu_{1}, \mu_{2}\}$. 证明 $\theta$ 的无偏估计不存在.
3. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $X \sim F(x - \theta)$  的独立同分布样本, 其中  $F(x)$  为总体累积分布, 且关于原点对称, 其中  $\theta \in R$  为参数.

(1) 证明 $\sum_{i=1}^{n} w_i X_{(i)} - \theta$ 关于原点对称, 其中 $w_i$ 为常数且满足 $w_i = w_{n-i+1}$,

$$
\sum_ {i = 1} ^ {n} w _ {i} = 1;
$$

(2) 如总体期望存在, 证明上述估计 $\sum_{i=1}^{n} w_i X_{(i)}$ 是 $\theta$ 的无偏估计.

4. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本, 记  $X_{-i} = (X_{1}, \cdots, X_{i-1}, X_{i+1}, \cdots, X_{n})$ , 即不包括  $X_{i}$  的样本. 设  $T_{n}(X)$  为基于 n 个样本  $X_{1}, X_{2}, \cdots, X_{n}$  的关于总体参数  $\theta$  的一个估计, 且其偏差  $b_{T_{n}}(\theta) = O(n^{-1})$ . 称

$$
T _ {J} (X) = n T _ {n} (X) - \frac {n - 1}{n} \sum_ {i = 1} ^ {n} T _ {n - 1} (X _ {- i})
$$

为  $\theta$  的 jackknife(刀切法) 估计. 证明:  $b_{T_{J}}(\theta)=O(n^{-2})$ .

5. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自正态总体  $N(\mu, \sigma^{2})$  的独立同分布样本, 求常数  $d_{n}$ , 使得  $d_{n}R_{n}$  为  $\sigma$  的无偏估计, 其中  $R_{n} = X_{(n)} - X_{(1)}$  为极差.
6. 设 X 服从 Poisson 分布  $P(\lambda)$ ，求 (1) 关于参数  $\lambda^{-1}$  的 Fisher 信息量；(2)  $\eta = g(\lambda)$ ，使关于  $\eta$  的 Fisher 信息量与  $\lambda$  无关.

---

习题二

103

7. 考虑如下的自回归模型: $X_{1} \sim N(\theta, \sigma^{2}/(1 - \rho^{2}))$, 且在给定 $X_{1} = x_{1}, X_{2} = x_{2}, \cdots, X_{j} = x_{j}$ 的条件下, $X_{j+1} \sim N(\theta + \rho(x_{j} - \theta), \sigma^{2}), j = 1, 2, \cdots, n-1$, 其中 $|\rho| < 1$ 为给定常数, $\theta, \sigma^{2} > 0$ 为参数. (1) 基于样本联合分布, 求 $(\theta, \sigma^{2})$ 的 Fisher 信息矩阵; (2) 证明样本均值 $\bar{X}$ 是 $\theta$ 的无偏估计, 并求其方差; (3) 当 $\sigma$ 已知, 取 $\theta$ 的先验分布为 $N(0, \tau^{2})$, 损失为平方损失时, 求 $\theta$ 的 Bayes 估计.

8. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自均匀分布  $U(0, \theta)$  的独立同分布样本. 证明 (1)  $\hat{\theta}_{1} = X_{(n)} + X_{(1)}$  是  $\theta$  的一个 UE; (2) 对适当选择的常数  $c_{n}, \hat{\theta}_{2} = c_{n}X_{(1)}$  是  $\theta$  的 UE, 但这个估计的方差比另外两个 UE  $\hat{\theta}_{3} = 2\bar{X}$  和  $\hat{\theta}_{4} = \frac{n+1}{n}X_{(n)}$  都大 (除非 n = 1).

9. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自均匀分布  $U(0, \theta)$  的独立同分布样本, 其中  $\theta > 0$  为未知参数. (1) 证明  $\hat{\theta}_{1} = \frac{n+1}{n} X_{(n)}, \hat{\theta}_{2} = (n+1) X_{(1)}, \hat{\theta}_{3} = 2 \bar{X}$  均是  $\theta$  的 UE.
(2) 上述三个估计中哪个方差最小？(3) 试证明  $\hat{\theta}_{1}$  是  $\theta$  的 UMVUE.

10. 设 $X \sim f(x; \theta)$. 记 $Y = g(X) \sim g(y; \theta), Z = h(X) \sim h(z; \theta)$, 设 $Y, Z$ 均满足正则条件 (定理 2.1.6 的条件), 且二者相互独立, 证明: $I_{Y,Z}(\theta) = I_Y(\theta) + I_Z(\theta)$, 其中 $I_{Y,Z}(\theta)$ 表示由 $(Y, Z)$ 联合分布计算得到的 $\theta$ 的 Fisher 信息量.

11. 设 $T_{i}(X)$ 是参数 $g_{i}(\theta)$ 的 UMVUE $(i = 1,2)$. 证明: 对于任意给定的常数 $c_{i}$, $c_{1}T_{1}(X) + c_{2}T_{2}(X)$ 是 $c_{1}g_{1}(\theta) + c_{2}g_{2}(\theta)$ 的 UMVUE.

12. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为总体 X 的独立同分布样本, 记  $E(X) = \mu, \mathcal{T} = \left\{\sum_{i=1}^{n} c_{i} X_{i}: c_{i} \in \mathbb{R}, i = 1, 2, \cdots, n.\right\}$ . (1) 证明  $T(X_{1}, X_{2}, \cdots, X_{n}) \in \mathcal{T}$  为  $\mu$  的无偏估计的充要条件是  $\sum_{i=1}^{n} c_{i} = 1$ ; (2) 在线性无偏估计类  $\mathcal{T}_{1} = \left\{T(x) \in \mathcal{T}, \sum_{i=1}^{n} c_{i} = 1\right\}$  中, 求  $\mu$  的 UMVUE.

13. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本, 且 X 为  $\{1, 2, \cdots, N\}$  上的均匀分布, 即

$$
P _ {N} (X = k) = \frac {1}{N}, k = 1, 2, \dots , N.
$$

其中 N 未知. (1) 证明  $X_{(n)}$  是充分完全统计量; (2) 求 N 的 UMVUE.

14. 设  $X_{1}, X_{2}, \cdots, X_{n}$  相互独立且方差均为  $\sigma^{2}$ ,  $E(X_{i}) = i\theta$ , 其中  $\theta, \sigma$  均为参数.
(1) 在  $\theta$  的所有线性无偏估计中找一个方差最小的无偏估计  $\hat{\theta}$ ; (2) 如果样本服从正态分布, 则  $\hat{\theta}$  是  $\theta$  的 UMVUE 吗?

15. 设  $X_{1}, X_{2}, \cdots, X_{m}$  为来自正态总体  $N(\mu_{1}, \sigma^{2})$  的独立同分布样本,  $Y_{1}, Y_{2}, \cdots, Y_{n}$  为来自正态总体  $N(\mu_{2}, \sigma^{2})$  的独立同分布样本, 且 X 样本与 Y 样本独立,  $\mu_{1}, \mu_{2}, \sigma^{2}$  为参数. 求  $\sigma^{2}$  及  $(\mu_{1} - \mu_{2}) / \sigma$  的 UMVUE.

16. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自 Pareto 分布  $Pa(\alpha, \beta)$  的独立同分布样本, 其中  $\alpha > 0, \beta > 0$  为参数. (1) 当  $\beta$  已知时, 求  $\alpha$  的 UMVUE; (2) 当  $\alpha$  已知时, 求  $\beta$  的

---

104

第二章 参数点估计

UMVUE; (3) 求  $\alpha, \beta$  的 UMVUE.

17. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自 Laplace 总体的独立同分布样本，此时总体分布为  $f(\theta) = -\frac{1}{2\theta} \exp\{-|x|/\theta\}$ ，其中  $\theta > 0$ 。求  $\theta, \theta^{-1}, \theta^{r}$  的 UMVUE，其中 r 为正整数。
18. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自两点分布  $B(1, \theta)$  的独立同分布样本, 其中  $\theta \in (0, 1)$ . 设  $m \leqslant n$  为已知正整数, 求 (1)  $\theta^{m}$  的 UMVUE; (2)  $P\left(\sum_{i=1}^{m} X_{i} = k\right)$  的 UMVUE, 其中  $k \leqslant m$  已知.
19. 设  $X_{1}, X_{2}, \cdots, X_{n}$  相互独立，且  $X_{1} \sim N(\mu, \sigma^{2}), X_{j} \sim N(0, \sigma^{2}) (j = 2, 3, \cdots, n - 1), X_{n} \sim N(0, \beta \sigma^{2})$ . 求  $\mu, \beta, \sigma^{2}$  的 UMVUE.
20. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自均匀分布  $U(0, \theta)$  的独立同分布样本，其中  $\theta > 0$ . 记  $\theta$  的 MLE 和 UMVUE 分别为  $\hat{\theta}_{m} = X_{(n)}$  和  $\hat{\theta}_{u} = (n + 1)\hat{\theta}_{m}/n$ . 如记  $T = (n + 2)\hat{\theta}_{m}/(n + 1)$ ，请证  $\mathrm{MSE}(T) < \min\{\mathrm{MSE}(\hat{\theta}_{m}), \mathrm{MSE}(\hat{\theta}_{u})\}$ .
21. 设某种产品的寿命 X 服从指数分布  $Exp(\lambda)$ ， $t_{0}$  为给定常数， $X_{1}, X_{2}, \cdots, X_{n}$  是独立观测到的 n 件产品的寿命。求产品在  $t_{0}$  前失效的概率  $P(X \leqslant t_{0}) = 1 - \exp\{-\lambda t_{0}\} = g(\lambda)$  的 UMVUE.
22. 设  $X_{1}, X_{2}, \cdots, X_{m}$  和  $Y_{1}, Y_{2}, \cdots, Y_{n}$  为分别来自 Poisson 分布  $P(\lambda_{x})$  和  $P(\lambda_{y})$  的独立同分布样本, 且全样本独立. 求  $(\lambda_{x} - \lambda_{y})^{2}$  的 UMVUE.
23. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $N(\mu, 1)$  的独立同分布样本, 记标准正态的累积分布为  $\Phi(x)$ , 求  $a_{n}$ , 使得  $\Phi(a_{n}\bar{X})$  为  $\Phi(\mu)$  的 UMVUE, 并由此求  $P(X_{1} < c)$  的 UMVUE, 其中 c 为常数.
24. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $N(0, \sigma^{2})$  的独立同分布样本, 求  $\sigma^{2}$  的充分完全统计量,  $\sigma$  和  $3\sigma^{4}$  的 UMVUE, 并证明  $\frac{1}{n} \sum_{i=1}^{n} X_{i}^{2}$  是  $\sigma^{2}$  的有效估计和相合估计.
25. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为某总体的独立同分布样本, 统计量  $T_{n}$  是参数  $\theta$  的无偏估计, 且  $\mathrm{Var}(T_{n}) < \infty$ . 如果对于任何  $\theta$  的无偏估计  $U_{n}$  都有  $\mathrm{Var}(T_{n}) \leqslant \mathrm{Var}(U_{n})$ , 证明  $T_{n}$  是  $\theta$  的均方相合估计.
26. 设  $X \sim \chi^{2}(n)$ ，证明:

$$
\sqrt {X} - \sqrt {n} \xrightarrow {\mathrm{d}} N (0, 1 / 2).
$$

并由此得: $P(X \leqslant x)$ 的值可由 $\Phi(\sqrt{2x} - \sqrt{2n})$ 来近似 (称之为 Fisher 近似).

27. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $B(1, \theta)$  的独立同分布样本, 其中  $0 < \theta < 1$ . 记  $T_{n} = \sum_{i=1}^{n} X_{i}, Y_{n} = \ln(T_{n}) I_{[1,\infty)}(T_{n})$ . 证明:  $Y_{n}$  是  $\ln\theta$  的强相合估计, 也是 CAN 估计.
28. 设  $X_{1}, X_{2}, \cdots, X_{n}$  和  $Y_{1}, Y_{2}, \cdots, Y_{n}$  为分别来自总体 X, Y 的独立同分布样本,

---

习题二

105

且 $P(X > 0) = 1, E(X^2) < \infty, E(Y^2) < \infty$，记 $\theta = E(Y) / E(X)$，证明

$$
\sqrt {n} (\bar {Y} / \bar {X} - \theta) \stackrel {\mathrm{d}} {\longrightarrow} N (0, \sigma^ {2}),
$$

并求  $\sigma^{2}$ .

29. 设 $(X_{i}, Y_{i})$ 为来自某二维总体的独立同分布样本, $r(X, Y)$ 为 (1.2.8) 式定义的样本相关系数, 即

$$
r (X, Y) = \frac {\sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) (Y _ {i} - \bar {Y})}{\sqrt {\sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) ^ {2} \sum_ {i = 1} ^ {n} (Y _ {i} - \bar {Y}) ^ {2}}}.
$$

(1) 如 $E(X_1^4) < \infty, E(Y_1^4) < \infty$, 证明:

$$
\sqrt {n} [ r (X, Y) - \rho ] \stackrel {\mathrm{d}} {\longrightarrow} N (0, c ^ {2}),
$$

其中  $\rho=\mathrm{Cov}(X_{1},Y_{1})/\sqrt{\mathrm{Var}(X_{1})\mathrm{Var}(Y_{1})}$ ，c 为不依赖于样本但依赖某些未知参数的常数.

(2) 如 $X_{1} \sim N(\mu_{1}, \sigma_{1}^{2}), Y_{1} \sim N(\mu_{2}, \sigma_{2}^{2})$, 证明: $r(X, Y)$ 的概率密度为

$$
f (r) = \frac {\Gamma ((n - 1) / 2)}{\sqrt {\pi} \Gamma (n / 2 - 1)} (1 - r ^ {2}) ^ {(n - 4) / 2} I _ {[ - 1, 1 ]} (r).
$$

30. 设  $X_{1}, X_{2}, \cdots, X_{n}$  相互独立，且  $E(X_{i}) = \mu$ ，记  $\sigma_{n}^{2} = \operatorname{Var}\left(\sum_{i=1}^{n} X_{i}\right)$ 。如果  $\sum_{i=1}^{n}(X_{i} - \mu)/\sigma_{n} \xrightarrow{\mathrm{d}} N(0,1)$ ，证明: $\bar{X}$  是  $\mu$  的相合估计当且仅当  $\sigma_{n} = o(n)$ .
31. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $N(\mu, \sigma^{2})$  的独立同分布样本, 证明: 样本方差  $S_{n}^{2}$  是  $\sigma^{2}$  的均方相合估计.
32. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自均匀分布  $U(\theta - 0.5, \theta + 0.5)$  的独立同分布样本, 其中  $\theta \in R$  为参数. 证明:  $[X_{(1)} + X_{(n)}] / 2$  是  $\theta$  的强相合估计, 也是均方相合估计.
33. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本,  $E(X^{4}) < \infty$ , 记

$$
T _ {n} (X) = \frac {\sum_ {i = 1} ^ {n} | X _ {i} | / n}{\sum_ {i = 1} ^ {n} X _ {i} ^ {2} / n}.
$$

(1) 证明: $\sqrt{n}(T_n - \nu) \xrightarrow{\mathrm{d}} N(0, c^2)$, 并用 $X$ 的矩给出 $\nu, c^2$ 的表达式; (2) 当 $X \sim N(0, \sigma^2)$ 时, 验证 (1) 中的结论.

---

106

第二章 参数点估计

34. 证明 $T_{n}(X)$ 是参数 $\theta$ 的均方相合估计的充要条件为: $T_{n}(X)$ 渐近无偏, 且 $\lim_{n\to \infty}\mathrm{Var}_{\theta}[T_n(X)] = 0, \forall \theta \in \Theta$.
35. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本，且  $E(X) = \theta, \operatorname{Var}(X) = \theta$ ，其中  $\theta > 0$ 。对于参数  $g(\theta) = \sqrt{\theta}$ ，设  $T_{1n} = \sqrt{\bar{X}}, T_{2n} = \bar{X}/S_{n}$ 。求  $T_{1n}$  相对于  $T_{2n}$  的渐近相对效率。
36. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本,  $E(X) = \mu, \operatorname{Var}(X) < \infty$ . 记  $T_{1n} = \bar{X}, T_{2n} = \frac{2}{n(n+1)} \sum_{i=1}^{n} iX_{i}$ . (1) 证明  $T_{2n}$  是  $\mu$  的相合估计; (2) 求  $T_{1n}$  相对于  $T_{2n}$  的渐近相对效率.
37. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $N(0, \sigma^{2})$  的独立同分布样本, 其中  $\sigma > 0$ . 对于参数  $g(\sigma^{2}) = \sigma$ , 求两个估计  $\sqrt{\pi/2} \sum_{i=1}^{n} |X_{i}| / n, \sqrt{\sum_{i=1}^{n} X_{i}^{2} / n}$  的渐近相对效率.
38. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $B(1, p)$  的独立同分布样本, 其中  $p \in (0, 1)$ . 考虑估计参数 p, 记 a, b 为两个正常数, 求  $(a + n\bar{X}) / (n + a + b)$  关于  $\bar{X}$  的渐近相对效率.
39. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自均匀分布  $U(\theta - 0.5, \theta + 0.5)$  的独立同分布样本 ( $n \geqslant 2$ ),  $\theta \in R$  为未知参数. (1) 求  $\theta$  的矩估计  $\hat{\theta}_{M}$ . (2)  $\hat{\theta}_{M}$  和  $\hat{\theta}_{1} = [X_{(1)} + X_{(n)}] / 2$  是  $\theta$  的 UE 吗？为什么？(3)  $\hat{\theta}_{M}$  和  $\hat{\theta}_{1}$  哪个方差较小？为什么？
40. 设  $Y \sim N(\mu, \sigma^{2})$ ，称  $X = e^{Y}$  的分布为对数正态分布。（1）求 X 的概率密度；
(2) 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本，求  $\mu, \sigma^{2}$  的矩估计与 MLE.
41. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本, 概率密度为

$$
\frac {1}{2 \sigma} \exp \{- | x - \mu | / \sigma \}.
$$

(1) 求  $\mu, \sigma$  的矩估计与 MLE; (2)  $\mu$  的矩估计是相合估计吗?

42. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本, 记  $\mu, \sigma^{2}$  分别为总体均值与方差. 证明: 对于任意三阶导数存在且有界的函数 h, 都有

$$
E [ h (\bar {X}) ] = h (\mu) + \frac {1}{2 n} h ^ {\prime \prime} (\mu) \sigma^ {2} + O _ {p} (n ^ {- 2}).
$$

43. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本，记  $\mu, \sigma^{2}$  分别为总体均值与方差，且总体三阶中心矩  $\nu_{3}$  存在且有界.证明:(1)  $E(\bar{X} - \mu)^{3} = \nu_{3}/n^{2}$ ; (2) 对于任意三阶导数存在且有界的函数 h，都有

$$
E \left\{\left\{h (\bar {X}) - E [ h (\bar {X}) ] \right\} ^ {3} \right\} = \frac {1}{n ^ {2}} [ h ^ {\prime} (\mu) ] ^ {3} \nu_ {3} + \frac {3}{n ^ {2}} h ^ {\prime \prime} (\mu) [ h ^ {\prime} (\mu) ] ^ {2} \sigma^ {2} + O _ {p} (n ^ {- 3}).
$$

44. 设总体 X 的概率分布为

$$
P (X = x) = p (1 - p) ^ {x - 1}, x = 1, 2, \dots ,
$$

---

习题二

107

$X_{1}, X_{2}, \cdots, X_{n}$  为来自此总体的独立同分布样本, 求 p 的矩估计和 MLE.

45. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自均匀分布  $U(a, b)$  的独立同分布样本, 求  $a^{2}$  的 MLE.
46. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自二项总体  $B(1, p)$  的独立同分布样本, 求 p 的 MLE. 假设  $p \in [1/3, 1/2]$ , 求其 MLE.
47. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自 logistic 分布  $LG(\mu, \sigma)$  的独立同分布样本, (1) 当  $\sigma$  已知,  $\mu \in R$  时, 试求  $\mu$  的 MLE; (2) 当  $\mu$  已知,  $\sigma > 0$  时, 试求  $\sigma$  的 MLE.
48. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $N(\mu, \sigma^{2})$  的独立同分布样本. (1) 当  $\mu \in [a, b]$ , a, b 已知时, 求  $\mu, \sigma^{2}$  的 MLE; (2) 当  $\sigma^{2}$  已知, 且  $\mu \in (0, \infty)$  时, 求  $\mu$  的 MLE.
49. 设  $X_{i1}, X_{i2}, \cdots, X_{in_{i}}$  为来自  $N(\mu_{i}, \sigma_{i}^{2})$  的独立同分布样本  $(i = 1, 2)$ ，且全样本独立。(1) 求  $\mu_{1} - \mu_{2}$  的 MLE。(2) 如  $n_{1} + n_{2} = n$  已知，且  $\sigma_{1}, \sigma_{2}$  已知，求使上述 MLE 的均方误差达到最小的  $n_{1}, n_{2}$  的比例。
50. 设  $X_{1}, \cdots, X_{m}, X_{m+1}, \cdots, X_{m+n}$  为来自 Poisson 分布  $P(\lambda)$  的独立同分布样本, 但由于某种原因, 假设仅观测到前 m 个样本, 以及  $\sum_{i=m+1}^{m+n} X_{i}$ , 求  $\lambda$  的 MLE.
51. 设  $X_{1}, \cdots, X_{m}, X_{m+1}, \cdots, X_{m+n}$  为来自指数分布  $Exp(\lambda)$  的独立同分布样本，但由于采用定时截尾实验，即实验进行到  $\tau$  时刻 ( $\tau$  为已知正数)，停止实验，故只观测到前 m 个样本，以及  $X_{i} > \tau (i = m + 1, m + 2, \cdots, m + n)$ . 求  $\lambda$  的 MLE.
52. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自 Cauchy 分布  $C(\theta, 1)$  的独立同分布样本. (1) 当 n = 1 时, 证明  $\theta$  的 MLE 为  $X_{1}$ ; (2) 当 n = 2 时, 证明  $\theta$  的 MLE 存在且唯一, 但似然方程有多个根.
53. 设总体 $X$ 服从混合正态分布, 即以均等概率按 $N(0,1)$ 分布和按 $N(\mu, \sigma^2)$ 分布取值, 其中 $\mu \in \mathbb{R}, \sigma^2 > 0$ 均未知. 此时 $X$ 的概率密度为

$$
f (x; \mu , \sigma^ {2}) = \frac {1}{2} \frac {1}{\sqrt {2 \pi}} \exp \{- x ^ {2} / 2 \} + \frac {1}{2} \frac {1}{\sqrt {2 \pi} \sigma} \exp \{- (x - \mu) ^ {2} / 2 \sigma^ {2} \}.
$$

设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自此混合分布总体的独立同分布样本, 证明  $\mu, \sigma^{2}$  不存在 MLE. (提示: 当  $\mu = x_{i}$ , 且  $\sigma^{2} \rightarrow 0$  时, 似然函数趋于无穷.)

54. 设样本  $Y_{1}, Y_{2}, \cdots, Y_{n}$  相互独立，且  $Y_{i} \sim B(1, p_{i})$ ，而  $p_{i}$  满足线性方程

$$
\ln \frac {p _ {i}}{1 - p _ {i}} = \alpha + \beta x _ {i}, i = 1, 2, \dots , n,
$$

其中  $x_{i}$  为已知常数,  $\alpha, \beta$  为未知参数. 求  $\alpha, \beta$  的 MLE.

55. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自两点分布  $B(1, \theta)$  的独立同分布样本, 其中  $\theta \in (0, 1)$ . 求在平方损失时下面估计的风险:

$$
T _ {1} (X) = \left\{ \begin{array}{c l} 0, & \text {样本中等于0的个数多于一半}, \\ 1, & \text {样本中等于1的个数多于一半}, \\ 1 / 2, & \text {样本中等于0的个数等于一半}. \end{array} \right.
$$

---

108

第二章 参数点估计

$$
T _ {2} (X) = \left\{ \begin{array}{l l} {{\bar {X},}} & {{\text {概率} 1 / 2,}} \\ {{T _ {1},}} & {{\text {概率} 1 / 2.}} \end{array} \right.
$$

56. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自指数分布总体  $Exp(\theta)$  的独立同分布样本，在平方损失下，求  $\bar{X}, cX_{(1)}$  的风险，其中 c 为正常数.
57. 设  $X_{ij} = \mu + a_i + \varepsilon_{ij}, i = 1, 2, \cdots, m, j = 1, 2, \cdots, n,$  其中  $a_i, \varepsilon_{ij}$  独立，且  $a_i \sim N(0, \sigma_a^2), \varepsilon_{ij} \sim N(0, \sigma_e^2), \mu, \sigma_a, \sigma_e$  未知.记  $\bar{X}_i = \sum_{j=1}^{n} X_{ij} / n, \bar{X} = \sum_{i=1}^{m} \bar{X}_i / m, MSA = \sum_{i=1}^{m} (\bar{X}_i - \bar{X})^2 / [n(m-1)], MSE = \sum_{i=1}^{m} \sum_{j=1}^{n} (X_{ij} - \bar{X}_i)^2 / [m(n-1)].$

设  $m(n-1)>4$ ，且记  $\theta=\sigma_{a}^{2}/\sigma_{e}^{2}$ ，及  $\theta$  的估计类:

$$
\left\{\hat {\theta} (\delta) = \frac {1}{n} \left[ (1 - \delta) \frac {\mathrm{MSA}}{\mathrm{MSE}} - 1 \right]: \delta \in \mathbb {R} \right\}.
$$

(1) 证明 MSA 和 MSE 独立; (2) 求 $\delta$, 使 $\hat{\theta}(\delta)$ 是 $\theta$ 的无偏估计; (3) 求平方损失下 $\hat{\theta}(\delta)$ 的风险; (4) 证明存在一个常数 $\delta^{*} \in \mathbb{R}$, 使得对于任何固定的 $\theta, \hat{\theta}(\delta)$ 的风险当 $\delta < \delta^{*}$ 时关于 $\delta$ 递减, 当 $\delta > \delta^{*}$ 时, 关于 $\delta$ 递增.

58. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自两点分布  $B(1, p)$  的独立同分布样本, 其中  $p \in (0, 1)$ . 取 p 的先验分布为  $U(0, 1)$ , 且损失  $L(p, a) = (p - 1)^{2} / [p(1 - p)]$ , 求此时关于 p 的 Bayes 估计.
59. 设 $X$ 为来自 Poisson 分布 $P(\lambda)$ 的一个样本, 参数 $\lambda$ 的先验密度为 $\pi(\lambda) = \mathrm{e}^{-\lambda} I_{(0,\infty)}(\lambda)$. 求 $\lambda$ 的 Bayes 估计.
60. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自均匀分布  $U(0, \theta)$  的独立同分布样本，其中  $\theta > 0$ . 取先验  $\pi(\theta)$  为 Pareto 分布  $Pa(\beta, \alpha)$ ，即  $\pi(\theta) = \alpha \beta^{\alpha} \theta^{-(\alpha+1)} I_{(\beta, \infty)}(\theta)$ ，其中  $\alpha > 0, \beta > 0$  已知. 求: (1)  $\theta$  的后验分布; (2) 在绝对损失  $L(\theta, a) = |\theta - a|$  下,  $\theta$  的 Bayes 估计.
61. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本, 且总体 X 的概率密度为

$$
f (x; \theta) = \theta \mathrm{e} ^ {- \theta x} I _ {[ 0, \infty)} (x), \quad \theta > c,
$$

其中 $c$ 为已知的正常数. 如取先验 $\pi (\theta) = \mathrm{e}^{-(\theta -c)}I_{[c,\infty)}(\theta)$, 求: (1) $\theta$ 的后验分布; (2) 在绝对损失 $L(\theta ,a) = |\theta -a|$ 下, $\theta$ 的Bayes估计.

62. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的独立同分布样本,  $E(X^{2}) < \infty$ . 记  $\mu = E(X)$ , 取平方损失. 证明: (1) 对于任意两个常数 a > 1, b, 关于  $\mu$  的形如  $a\bar{X} + b$  的估计是不容许的; (2) 如  $b \neq 0$ , 则形如  $\bar{X} + b$  的估计是不容许的.
63. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自两点分布  $B(1, \theta)$  的独立同分布样本, 其中  $\theta \in (0, 1)$ . 取损失为二次损失函数  $(\theta - a)^{2}$ , 先验分布为  $P(\theta = \theta_{0}) = 1 - P(\theta = 1 - \theta_{0}) = 1/2$ . 试决定  $\theta_{0}$ , 使在此先验下  $\theta$  的 Bayes 估计为 minimax 估计.

---

习题二

109

64. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自指数分布  $Exp(\theta)$  的独立同分布样本，其中  $\theta > 0$ . 证明:(1) 任给一  $b \geqslant 0$ ,  $(n\bar{X} + b)/(n + 1)$  是平方损失下  $\theta^{-1}$  的容许估计；(2)  $(n\bar{X} + b)/(n + 1)$  是损失函数  $L(\theta, a) = \theta^{2}(1 - a/\theta)^{2}$  下  $\theta^{-1}$  的 minimax 估计；(3)  $\bar{X}$  不是  $\theta^{-1}$  的容许估计.
65. 设样本 $X$ 来自 Poisson 分布 $P(\theta)$. 证明: 在损失函数为 $L(\theta, a) = (a - \theta)^2 / \theta$ 下, $X$ 为 $\theta$ 的容许的 minimax 估计.

---


