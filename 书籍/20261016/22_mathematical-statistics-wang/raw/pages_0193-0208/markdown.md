- $Z_{1}, Z_{2}, \cdots, Z_{p}$ 独立同分布于 $N(0,1)$.
- $Z_{i}^{2} \sim \chi^{2}(1)$, $E(Z_{i}^{2}) = 1$ 且 $E(Z_{i}^{4}) = \mathrm{Var}(Z_{i}^{2}) + E^{2}(Z_{i}^{2}) = 3$.

于是, 我们有

$$
\begin{array}{l} E \left[ \left(\boldsymbol {Y} ^ {\mathrm{T}} A \boldsymbol {Y}\right) ^ {2} \right] = E \left[ \left(\boldsymbol {Z} ^ {\mathrm{T}} D \boldsymbol {Z}\right) ^ {2} \right] = 3 \sum_ {i = 1} ^ {p} \lambda_ {i} ^ {2} + \sum_ {i = 1} ^ {p} \sum_ {i \neq j} \lambda_ {i} \lambda_ {j} \\ = 2 \sum_ {i = 1} ^ {p} \lambda_ {i} ^ {2} + \sum_ {i = 1} ^ {p} \sum_ {j = 1} ^ {p} \lambda_ {i} \lambda_ {j} \\ = 2 \mathrm{tr} (A ^ {2}) + \mathrm{tr} ^ {2} (A). \\ \end{array}
$$

进而得到 $\mathrm{Var}(\mathbf{Y}^{\mathrm{T}}\mathbf{A}\mathbf{Y}) = 2\mathrm{tr}(A^{2}).$

同理可证 $\mathrm{Cov}(\mathbf{Y}^{\mathrm{T}}\Sigma^{1 / 2}A\Sigma^{1 / 2}\mathbf{Y},2\pmb{\mu}^{\mathrm{T}}A\Sigma^{1 / 2}\mathbf{Y}) = 0.$

![](images/page_192_image_9.jpg)

## 4.2 多元模型的统计推断

在本节中, 我们以前述的多元正态分布为例, 介绍多元模型下的统计推断问题和方法, 包括估计、假设检验以及置信区域等.

## 4.2.1 多元正态的最大似然估计

由第二、三章可知, 在分布给定下, 似然方法为我们提供了进行统计推断的系统化工具, 因此这里我们就基于似然方法展开. 当总体为多元正态分布时, 对于参数  $\mu$  和  $\Sigma$  的估计可以基于观测向量  $X_{1}, X_{2}, \cdots, X_{n}$ , 使得最大化似然函数获得:

$$
\begin{array}{l} L (\boldsymbol {\mu}, \Sigma ; \mathbb {X}) = \prod_ {i = 1} ^ {n} f (\boldsymbol {x} _ {i}; \boldsymbol {\mu}, \Sigma) \\ = \prod_ {i = 1} ^ {n} \frac {1}{(2 \pi) ^ {p / 2} | \Sigma | ^ {1 / 2}} \exp \left\{- \frac {\left(\boldsymbol {x} _ {i} - \boldsymbol {\mu}\right) ^ {\mathrm{T}} \Sigma^ {- 1} \left(\boldsymbol {x} _ {i} - \boldsymbol {\mu}\right)}{2} \right\} \\ = \frac {1}{(2 \pi) ^ {n p / 2} | \Sigma | ^ {n / 2}} \exp \left\{- \frac {\sum_ {i = 1} ^ {n} (\boldsymbol {x} _ {i} - \boldsymbol {\mu}) ^ {\mathrm{T}} \Sigma^ {- 1} (\boldsymbol {x} _ {i} - \boldsymbol {\mu})}{2} \right\}. \\ \end{array}
$$

相应的对数似然方程为

$$
\ell (\boldsymbol {\mu}, \Sigma ; \mathbb {X}) = \ln \left[ L \left(\boldsymbol {\mu}, \Sigma ; \mathbb {X}\right) \right]
$$

$$
= - \frac {n p}{2} \ln (2 \pi) - \frac {n}{2} \ln (| \Sigma |) - \frac {1}{2} \sum_ {i = 1} ^ {n} (\boldsymbol {x} _ {i} - \boldsymbol {\mu}) ^ {\mathrm{T}} \Sigma^ {- 1} (\boldsymbol {x} _ {i} - \boldsymbol {\mu}). \tag {4.2.1}
$$

为证明上述结论, 我们引入如下引理.

引理 4.2.1 设 A 为  $p \times p$  对称矩阵, v 为 p 维向量. 则有

(1) $\boldsymbol{v}^{\mathrm{T}}\boldsymbol{A}\boldsymbol{v} = \mathrm{tr}(\boldsymbol{v}^{\mathrm{T}}\boldsymbol{A}\boldsymbol{v}) = \mathrm{tr}(\boldsymbol{v}\boldsymbol{v}^{\mathrm{T}}\boldsymbol{A}) = \mathrm{tr}(A\boldsymbol{v}\boldsymbol{v}^{\mathrm{T}})$.
(2) 如果 A 正定, 则当且仅当  $A = I_{p}$  时,  $\mathrm{tr}(A) - \ln(|A|) \geqslant p$  成立.

证明 利用 $|A| = \prod_{i=1}^{p} \lambda_i$ 及 $\operatorname{tr}(A) = \sum_{i=1}^{p} \lambda_i$. 注意到对于任意 $x > 0, x - \ln(x) \geqslant 1$. □ 我们固定 $\Sigma$, 并考虑 $\max_{\boldsymbol{\mu}} \ell(\boldsymbol{\mu}, \Sigma)$.

$$
\begin{array}{l} \frac {\partial \ell (\boldsymbol {\mu} , \Sigma)}{\partial \boldsymbol {\mu}} = \sum_ {i = 1} ^ {n} \Sigma^ {- 1} (\boldsymbol {x} _ {i} - \boldsymbol {\mu}) = \boldsymbol {0} \\ \Longleftrightarrow \sum_ {i = 1} ^ {n} \boldsymbol {x} _ {i} - n \boldsymbol {\mu} = \boldsymbol {0} \\ \Longleftrightarrow \hat {\mu} = \bar {x}. \\ \end{array}
$$

接下来, 我们考虑最大化  $\ell(\bar{\boldsymbol{x}}, \Sigma)$ ,

$$
\begin{array}{l} \ell (\bar {\boldsymbol {x}}, \Sigma) = - \frac {n p}{2} \ln (2 \pi) - \frac {n}{2} \ln (| \Sigma |) - \frac {1}{2} \sum_ {i = 1} ^ {n} \left(\boldsymbol {x} _ {i} - \bar {\boldsymbol {x}}\right) ^ {\mathrm{T}} \Sigma^ {- 1} \left(\boldsymbol {x} _ {i} - \bar {\boldsymbol {x}}\right) \\ = - \frac {n p}{2} \ln (2 \pi) - \frac {n}{2} \ln (| \Sigma |) - \frac {1}{2} \mathrm{tr} \left[ \Sigma^ {- 1} \sum_ {i = 1} ^ {n} \left(\boldsymbol {x} _ {i} - \bar {\boldsymbol {x}}\right) \left(\boldsymbol {x} _ {i} - \bar {\boldsymbol {x}}\right) ^ {\mathrm{T}} \right] \\ = - \frac {n p}{2} \ln (2 \pi) - \frac {n}{2} \ln (| \Sigma |) - \frac {1}{2} \mathrm{tr} \left[ \Sigma^ {- 1} \cdot (n - 1) S \right] \\ = - \frac {n p}{2} \ln (2 \pi) - \frac {n}{2} \ln (| \Sigma |) - \\ \frac {n}{2} \left[ \mathrm{tr} \left(\Sigma^ {- 1 / 2} A \Sigma^ {- 1 / 2}\right) - \ln \left(| \Sigma^ {- 1 / 2} A \Sigma^ {- 1 / 2} |\right) \right] - \\ \frac {n}{2} \ln \left(| \Sigma^ {- 1 / 2} A \Sigma^ {- 1 / 2} |\right) \\ \Longleftrightarrow \text {最小化} \mathrm{tr} \left(\Sigma^ {- 1 / 2} A \Sigma^ {- 1 / 2}\right) - \ln \left(| \Sigma^ {- 1 / 2} A \Sigma^ {- 1 / 2} |\right) \\ \Longleftrightarrow \Sigma^ {- 1 / 2} A \Sigma^ {- 1 / 2} = I _ {p} \\ \Longleftrightarrow \hat {\Sigma} = A = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(\boldsymbol {x} _ {i} - \bar {\boldsymbol {x}}\right) \left(\boldsymbol {x} _ {i} - \bar {\boldsymbol {x}}\right) ^ {\mathrm{T}}, \\ \end{array}
$$

其中 $A = \frac{n - 1}{n} S.$ 同时注意到

$$
\ln \left(| \Sigma^ {- 1 / 2} A \Sigma^ {- 1 / 2} |\right) = \ln \left(| \Sigma | ^ {- 1 / 2} | A | | \Sigma | ^ {- 1 / 2}\right) = - \ln \left(| \Sigma |\right) + \ln \left(| A |\right).
$$

简单计算可得 (4.2.1) 式.

由 (4.2.1) 式可知, 对于多元正态分布而言,  $\mu$  和  $\Sigma$  的最大似然估计分别为

$$
\hat {\boldsymbol {\mu}} = \bar {\boldsymbol {X}}, \quad \hat {\Sigma} = \frac {1}{n} \sum_ {i = 1} ^ {n} (\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}) (\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}) ^ {\mathrm{T}} = \frac {n - 1}{n} S.
$$

回顾 $S$ 为 $\Sigma$ 的无偏估计, 现在实际数据分析中 $S$ 和 $\hat{\Sigma}$ 二者效果差异不大, 都很常用.

此外, 我们这里还考虑相关系数的最大似然估计. 我们有如下的简单推论.

推论 4.2.1 如果  $\widehat{\theta_{1}}, \widehat{\theta_{2}}, \cdots, \widehat{\theta_{m}}$  为分布参数  $\theta_{1}, \theta_{2}, \cdots, \theta_{m}$  的最大似然估计，则当  $\theta_{1}, \theta_{2}, \cdots, \theta_{m}$  到  $\psi_{1}, \psi_{2}, \cdots, \psi_{m}$  的变换为一一映射时， $\psi_{1}(\widehat{\theta_{1}}, \widehat{\theta_{2}}, \cdots, \widehat{\theta_{m}}), \psi_{2}(\widehat{\theta_{1}}, \widehat{\theta_{2}}, \cdots, \widehat{\theta_{m}}), \cdots, \psi_{m}(\widehat{\theta_{1}}, \widehat{\theta_{2}}, \cdots, \widehat{\theta_{m}})$  为  $\psi_{1}(\theta_{1}, \theta_{2}, \cdots, \theta_{m}), \psi_{2}(\theta_{1}, \theta_{2}, \cdots, \theta_{m}), \cdots, \psi_{m}(\theta_{1}, \theta_{2}, \cdots, \theta_{m})$  的最大似然估计。如果  $\theta_{1}, \theta_{2}, \cdots, \theta_{m}$  的估计是唯一的，则  $\psi_{1}, \psi_{2}, \cdots, \psi_{m}$  的估计也是唯一的。

由此，“一一映射”使得似然函数由  $\psi_{1},\psi_{2},\cdots,\psi_{m}$  唯一定义，因此相关系数  $\rho_{jk}$  的最大似然估计为

$$
\widehat {\rho} _ {j k} = \frac {\sum_ {i = 1} ^ {n} (X _ {i j} - \bar {X} _ {j}) (X _ {i k} - \bar {X} _ {k})}{\sqrt {\sum_ {i = 1} ^ {n} (X _ {i j} - \bar {X} _ {j}) ^ {2}} \sqrt {\sum_ {i = 1} ^ {n} (X _ {i k} - \bar {X} _ {k}) ^ {2}}}.
$$

下面我们要进一步考虑上述估计的抽样分布, 由此我们需要引入  $\chi^{2}$  分布的多元推广——Wishart(威沙特) 分布.

定义 4.2.1(Wishart 分布) 假设 p 维向量  $Z_{i}, i=1,2,\cdots,q$  独立同分布于  $N_{p}(\mathbf{0}_{p}, \Sigma)$ ，则

$$
\sum_ {i = 1} ^ {q} \mathbf {Z} _ {i} \mathbf {Z} _ {i} ^ {\mathrm{T}} \sim W _ {p} (q, \Sigma),
$$

其中 q 为自由度.

Wishart 分布的性质如下:

(1) 假设有两个独立的  $p \times p$  随机矩阵  $W_{1}$  和  $W_{2}$  分别服从分布  $W_{p}(q_{1}, \Sigma)$  和  $W_{p}(q_{2}, \Sigma)$ ，则  $\boldsymbol{W}_{1} + \boldsymbol{W}_{2} \sim W_{p}(q_{1} + q_{2}, \Sigma)$ .
(2) 如果  $\boldsymbol{W} \sim W_{p}(q, \Sigma)$ ，则  $C\boldsymbol{WC}^{\mathrm{T}} \sim W_{k}(q, C\Sigma C^{\mathrm{T}})$ ，其中 C 为  $k \times p$  常数矩阵.
(3) 如果  $\boldsymbol{W} \sim W_{p}(q, \Sigma)$ ，则当  $a^{T} \Sigma a \neq 0$  时， $\frac{a^{T} W a}{a^{T} \Sigma a} \sim \chi^{2}(q)$ .
(4) 如果  $\boldsymbol{W} \sim W_{p}(q, \Sigma)$ ，则  $E(\boldsymbol{W}) = q\Sigma$ .
(5) 如果 $p = 1, W_{1}(q, \sigma^{2})$ 即为 $\sigma^{2}\chi^{2}(q)$.

证明 (1) 令 $\mathbf{W}_1 = \sum_{i=1}^{q_1} \mathbf{Z}_i \mathbf{Z}_i^{\mathrm{T}}$, $\mathbf{W}_2 = \sum_{i=q_1+1}^{q_1 + q_2} \mathbf{Z}_i \mathbf{Z}_i^{\mathrm{T}}$, 其中 $\mathbf{Z}_1, \cdots, \mathbf{Z}_{q_1}, \mathbf{Z}_{q_1+1}, \cdots, \mathbf{Z}_{q_1 + q_2}$ 独立同分布于 $N_p(\mathbf{0}, \Sigma)$. 因此 $\mathbf{W}_1 + \mathbf{W}_2 = \sum_{i=1}^{q_1 + q_2} \mathbf{Z}_i \mathbf{Z}_i^{\mathrm{T}} \sim W_p(q_1 + q_2, \Sigma)$.

(2) $\mathbf{W} = \sum_{i=1}^{q} \mathbf{Z}_i \mathbf{Z}_i^{\mathrm{T}}$, 且 $C \mathbf{W} C^{\mathrm{T}} = \sum_{i=1}^{q} C \mathbf{Z}_i \mathbf{Z}_i^{\mathrm{T}} C^{\mathrm{T}}$. 同时 $C \mathbf{Z}_i \sim N_k (\mathbf{0}, C \Sigma C^{\mathrm{T}})$. 由定义可得结论.
(3) 由于 $\pmb{a}^{\mathrm{T}}\pmb{W}\pmb{a} = \sum_{i=1}^{q}\pmb{a}^{\mathrm{T}}\pmb{Z}_{i}\pmb{Z}_{i}^{\mathrm{T}}\pmb{a} = \sum_{i=1}^{q}(\pmb{a}^{\mathrm{T}}\pmb{Z}_{i})^{2}$. 注意到 $\pmb{a}^{\mathrm{T}}\pmb{Z}_{i} \sim N(0, \pmb{a}^{\mathrm{T}}\Sigma\pmb{a})$, 因此, $\pmb{a}^{\mathrm{T}}\pmb{Z}_{i}/\sqrt{\pmb{a}^{\mathrm{T}}\Sigma\pmb{a}} \sim N(0,1)$, 进而得到结论.

(4) $E(\boldsymbol{W}) = E\left(\sum_{i=1}^{q}\boldsymbol{Z}_{i}\boldsymbol{Z}_{i}^{\mathrm{T}}\right) = q\Sigma.$

定理 4.2.1 假设  $\{X_{1}, X_{2}, \cdots, X_{n}\}$  是来自  $N_{p}(\boldsymbol{\mu}, \Sigma)$  的独立同分布样本. 则有,

(1) 样本均值  $\bar{X} \sim N_{p}(\boldsymbol{\mu}, \Sigma/n)$ .
(2) 样本协方差 $S$ 满足 $(n - 1)S \sim W_p(n - 1, \Sigma)$.
(3)  $\bar{X}$  与 S 相互独立.

证明 1 (1) 由性质 4.1.6 可得.

(2) (经典方法) 构造正交矩阵 R, 使得  $RR^{T} = R^{T}R = I_{n}$ ,

$$
R _ {n \times n} = \left( \begin{array}{c c c c} r _ {1, 1} & \dots & r _ {1, n - 1} & 1 / \sqrt {n} \\ r _ {2, 1} & \dots & r _ {2, n - 1} & 1 / \sqrt {n} \\ \vdots & & \vdots & \vdots \\ r _ {n, 1} & \dots & r _ {n, n - 1} & 1 / \sqrt {n} \end{array} \right) \stackrel {\text {记为}} {=} \left(\boldsymbol {r} _ {1}, \boldsymbol {r} _ {2}, \dots , \boldsymbol {r} _ {n - 1}, \frac {1}{\sqrt {n}} \mathbf {1} _ {n}\right).
$$

注意到

$$
\mathbb {X} - \underset {(n \times p)} {\mathbf {1} _ {n} \boldsymbol {\mu} ^ {\mathrm{T}}} = \left( \begin{array}{c c c} X _ {1, 1} - \mu_ {1} & \dots & X _ {1, p} - \mu_ {p} \\ X _ {2, 1} - \mu_ {1} & \dots & X _ {2, p} - \mu_ {p} \\ \vdots & & \vdots \\ X _ {n, 1} - \mu_ {1} & \dots & X _ {n, p} - \mu_ {p} \end{array} \right) \stackrel {\text {记为}} {=} \left( \begin{array}{c} \boldsymbol {X} _ {1} ^ {\mathrm{T}} \\ \boldsymbol {X} _ {2} ^ {\mathrm{T}} \\ \vdots \\ \boldsymbol {X} _ {n} ^ {\mathrm{T}} \end{array} \right).
$$

考虑  $\boldsymbol{Z}^{\mathrm{T}} = (\mathbb{X} - \mathbf{1}_{n}\boldsymbol{\mu}^{\mathrm{T}})^{\mathrm{T}} R,$  其中  $\boldsymbol{Z}_{j} = (\mathbb{X} - \mathbf{1}_{n}\boldsymbol{\mu}^{\mathrm{T}})^{\mathrm{T}} \boldsymbol{r}_{j} = \sum_{i=1}^{n} r_{ji} X_{i}, j = 1, 2, \cdots, n.$  我们已知如下事实:

(i)  $Z_{j}$  服从正态分布, 其中  $E(Z_{j}) = 0$ .
(ii) $\mathrm{Cov}(\mathbf{Z}_j, \mathbf{Z}_k) = \sum_{i=1}^{n} r_{ji} r_{ki} \mathrm{Cov}(\mathbf{X}_i) = \left\{ \begin{array}{ll} 0, & j \neq k, \\ \Sigma, & j = k. \end{array} \right.$
(iii) $\sum_{i=1}^{n}\boldsymbol{Z}_i\boldsymbol{Z}_i^{\mathrm{T}} = \boldsymbol{Z}^{\mathrm{T}}\boldsymbol{Z} = (\mathbb{X} - \mathbf{1}_n\boldsymbol{\mu}^{\mathrm{T}})^{\mathrm{T}}(\mathbb{X} - \mathbf{1}_n\boldsymbol{\mu}^{\mathrm{T}}) = \sum_{i=1}^{n}(\boldsymbol{X}_i - \mathbf{1}_n\boldsymbol{\mu}^{\mathrm{T}})(\boldsymbol{X}_i - \mathbf{1}_n\boldsymbol{\mu}^{\mathrm{T}})^{\mathrm{T}}.$
(iv) $Z_{n}Z_{n}^{\mathrm{T}} = n(\bar{X} -\mathbf{1}_{n}\pmb{\mu}^{\mathrm{T}})(\bar{X} -\mathbf{1}_{n}\pmb{\mu}^{\mathrm{T}})^{\mathrm{T}}.$

由事实 (iii) 和 (iv), 我们有 $(n - 1)S = \sum_{i=1}^{n-1} \mathbf{Z}_i \mathbf{Z}_i^{\mathrm{T}} \sim W_p(n - 1, \Sigma)$.

(3) 利用事实 (ii),  $Z_{n}$  与  $Z_{1}, Z_{2}, \cdots, Z_{n-1}$ ，即 S，相互独立.

证明 2 (另一种方法: 首先证明 (3), 然后证明 (2).)

(3) 构造如下随机变量序列,

$$
\begin{array}{l} \mathbf {Z} _ {1} = \bar {\mathbf {X}}, \\ \mathbf {Z} _ {2} = \mathbf {X} _ {2} - \bar {\mathbf {X}}, \\ \dots , \\ \mathbf {Z} _ {n} = \mathbf {X} _ {n} - \bar {\mathbf {X}}. \\ \end{array}
$$

可知  $Z_{i}, i=1,2,\cdots,n$  服从正态分布并且

$$
\mathrm{Cov} (\mathbf {Z} _ {1}, \mathbf {Z} _ {i}) = \mathrm{Cov} (\bar {\mathbf {X}}, \mathbf {X} _ {i} - \bar {\mathbf {X}}) = \frac {1}{n} \Sigma - \frac {1}{n} \Sigma = 0, i = 2, 3, \dots , n.
$$

即说明  $Z_{1}$  与  $\{Z_{2}, Z_{3}, \cdots, Z_{n}\}$  相互独立.

由于 $\sum_{i=1}^{n} (\boldsymbol{X}_i - \bar{\boldsymbol{X}}) = \boldsymbol{0}$, 我们有 $X_1 - \bar{X} = -\sum_{i=2}^{n} (X_i - \bar{X}) = -\sum_{i=2}^{n} Z_i$. 注意到

$$
\begin{array}{l} (n - 1) S = \sum_ {i = 1} ^ {n} (\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}) (\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}) ^ {\mathrm{T}} \\ = \sum_ {i = 2} ^ {n} (\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}) (\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}) ^ {\mathrm{T}} + (\boldsymbol {X} _ {1} - \bar {\boldsymbol {X}}) (\boldsymbol {X} _ {1} - \bar {\boldsymbol {X}}) ^ {\mathrm{T}} \\ = \sum_ {i = 2} ^ {n} \mathbf {Z} _ {i} \mathbf {Z} _ {i} ^ {\mathrm{T}} + \left(\sum_ {i = 2} ^ {n} \mathbf {Z} _ {i}\right) \left(\sum_ {i = 2} ^ {n} \mathbf {Z} _ {i}\right) ^ {\mathrm{T}}, \\ \end{array}
$$

其仅依赖于  $\{Z_{2}, Z_{3}, \cdots, Z_{n}\}$ .

因此,  $\bar{X}$  与 S 相互独立.

(2) 进而, 我们将  $(n-1)S$  如下展开,

$$
\begin{array}{l} (n - 1) S = \sum_ {i = 1} ^ {n} \left(\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}\right) \left(\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}\right) ^ {\mathrm{T}} \\ = \sum_ {i = 1} ^ {n} \left(\boldsymbol {X} _ {i} - \boldsymbol {\mu} + \boldsymbol {\mu} - \bar {\boldsymbol {X}}\right) \left(\boldsymbol {X} _ {i} - \boldsymbol {\mu} + \boldsymbol {\mu} - \bar {\boldsymbol {X}}\right) ^ {\mathrm{T}} \\ = \sum_ {i = 1} ^ {n} \left(\boldsymbol {X} _ {i} - \boldsymbol {\mu}\right) \left(\boldsymbol {X} _ {i} - \boldsymbol {\mu}\right) ^ {\mathrm{T}} - n \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu}\right) \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu}\right) ^ {\mathrm{T}}. \\ \end{array}
$$

由 Wishart 分布的定义，可知展式中的第一项和第二项分别服从分布  $W_{p}(n,\Sigma)$  和  $W_{p}(1,\Sigma)$ . 于是, 由 Wishart 分布的性质, 可得  $(n-1)S \sim W_{p}(n-1,\Sigma)$  成立. □

注 4.2.1 类似一元情形 (见习题一 36), 多元情形的样本相关系数也有相应的分布, 但其精确分布较为复杂 (见 Fisher(1915)), 通常我们使用其渐近分布. 假设  $\rho$  和  $\hat{\rho}$  分别为二元正态向量  $(X,Y)^{\mathrm{T}}$  的总体和样本相关系数, 由附录 A.4 的内容, 基于多元 Delta 方法可证明,

$$
\sqrt {n} (\hat {\rho} - \rho) \xrightarrow {\mathrm{d}} N (0, (1 - \rho^ {2}) ^ {2}).
$$

## 4.2.2 多元正态下的假设检验和置信区域

多元总体参数的检验问题在实际中有很多应用, 其主要包含均值向量的检验问题和协方差矩阵的检验问题. 在本小节中, 我们主要以均值向量为例来进行阐述, 最后对协方差矩阵的检验给予简单探讨.

例如, 在评估治疗后基因表达水平平均值的变化或者比较肿瘤基因表达组与正常基因表达组水平时, 多个基因的表达水平值即是我们考虑的多元向量, 检验问题就是形如  $H_{0}: \mu = 0$  或  $H_{0}: \mu_{1} = \mu_{2}$ . 一个自然的问题是: 我们是否可以通过一元检验过程单独对每一维度变量做一元检验? 即, 对于  $\mu_{1}, \mu_{2}, \cdots, \mu_{p}$  做 p 个假设. 首先, 盲目地使用一元检验会使得第一类错误概率不受控. 例如, 如果我们分别按照 0.05 的显著性水平进行 p = 10 个一元检验, 至少一个错误拒绝的概率将大于 0.05. 如果变量相互独立 (极少情况), 我们有 (在  $H_{0}$  下)

$$
\begin{array}{l} P (\text {至少一个拒绝}) = 1 - P (\text {接受全部} 1 0 \text {个检验} H _ {0}) \\ = 1 - 0. 9 5 ^ {1 0} = 0. 4. \\ \end{array}
$$

此外, 一元检验完全忽略变量间的相关性, 而多元检验可以比分别进行一元检验具有更高的势——较小的个体效应形成显著的联合效应.

## 一、单样本均值向量的多元检验和置信区域

假设  $\{X_{1}, X_{2}, \cdots, X_{n}\}$  为来自  $N_{p}(\boldsymbol{\mu}, \Sigma)$  的 p 维独立同分布样本. 先考虑最简单的情形, 在  $\Sigma$  已知的情况下, 关于  $\mu$  的检验:

$$
H _ {0}: \boldsymbol {\mu} = \boldsymbol {\mu} _ {0} \leftrightarrow H _ {1}: \boldsymbol {\mu} \neq \boldsymbol {\mu} _ {0}.
$$

此时, 我们自然会考虑用  $\bar{X}-\mu_{0}$  的大小作为  $H_{0}$  正确与否的度量, 但是它是一个向量, 我们更希望用一个单值统计量进行检验. 如果直接取这个向量的 Euclid 模, 得到的统计量又不是尺度不变的. 回顾在性质 4.1.8 中介绍的 Mahalanobis 距离可很好地衡量  $\bar{X}-\mu_{0}$  的大小, 而注意到在  $H_{0}$  下,  $Z^{2}=n(\bar{X}-\mu_{0})^{\mathrm{T}}\Sigma^{-1}(\bar{X}-\mu_{0})\sim\chi^{2}(p)$ . 因此, 在显著性水平  $\alpha$  下, 如果  $Z^{2}>\chi_{\alpha}^{2}(p)$ , 则拒绝  $H_{0}$ .

在实际中, $\Sigma$ 一般是未知的. 当 $\Sigma$ 未知时, 应该如何调整检验统计量? 如同一元 $t$ 统计量, 我们考虑使用 $\Sigma$ 的估计 $S$ 或 $\hat{\Sigma}$ 进行替代, 就得到了著名的 Hotelling(霍特林)

$T^{2}$  检验统计量:

$$
T ^ {2} = n (\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}) ^ {\mathrm{T}} S ^ {- 1} (\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}).
$$

在 $H_0$ 下:$\pmb{\mu} = \pmb{\mu}_0$，$T^2$ 服从参数为 $p$ 和 $n - 1$ 的Hotelling $T^2$ 分布，记为 $T^2 \sim T^2(p, n - 1)$. 事实上，由后面探讨的Hotelling $T^2$ 性质可知，尺度变换后它是一个 $F$ 分布，即 $\frac{(n - 1) - p + 1}{(n - 1)p} T^2 \sim F(p, n - p)$. 因此，此时检验为:如果 $\frac{(n - 1) - p + 1}{(n - 1)p} T^2 > F_\alpha(p, n - p)$，则拒绝 $H_0$.

定义 4.2.2 (Hotelling  $T^{2}$  分布) 假设  $X \sim N_{p}(\mathbf{0}_{p}, \Sigma)$ ,  $W \sim W_{p}(n, \Sigma)$ ，其中  $\Sigma$  正定且  $n \geqslant p$ , X 与 W 相互独立，则  $T^{2} = n X^{T} W^{-1} X$  的分布被称为 Hotelling  $T^{2}$  分布，记作  $T^{2} \sim T^{2}(p, n)$ .

性质 4.2.1 (Hotelling  $T^{2}$  分布)  $T^{2} \sim T^{2}(p, n)$ ，则

$$
\frac {n - p + 1}{n p} T ^ {2} \sim F (p, n - p + 1).
$$

注意到  $T^{2}$  分布仅依赖于 p 和 n, 不依赖于  $\Sigma$ .

证明 回顾自由度为 $d_{1}$ 和 $d_{2}$ 的 $F$ 分布的定义为 $X = \frac{S_1 / d_1}{S_2 / d_2}$ 的分布, 其中 $S_{1} \sim \chi^{2}(d_{1})$ 与 $S_{2} \sim \chi^{2}(d_{2})$ 相互独立. 由定义, $\frac{n - p + 1}{np} T^{2} = \frac{n - p + 1}{p} X^{\mathrm{T}} W^{-1} X$, 其中 $X \sim N_{p}(\mathbf{0}_{p}, \Sigma)$, $W \sim W_{p}(n, \Sigma)$, 且 $X$ 与 $W$ 相互独立. 我们注意到给定 $X = x$, $\frac{x^{\mathrm{T}} \Sigma^{-1} x}{x^{\mathrm{T}} W^{-1} x} \sim \chi^{2}(n - p + 1)$, 不依赖于 $x$. 因此, $X^{\mathrm{T}} \Sigma^{-1} X$ 与 $\frac{X^{\mathrm{T}} \Sigma^{-1} X}{X^{\mathrm{T}} W^{-1} X}$ 相互独立, 且 $X^{\mathrm{T}} \Sigma^{-1} X \sim \chi^{2}(p)$. 进而, 结论成立. □

注 4.2.2  $T^{2}$  具有仿射不变性, 即在  $Y_{i}=AX_{i}+a$  变换下所得到的  $T^{2}$  值相同, 其中 A 为  $p \times p$  非奇异矩阵, a 为 p 维向量. 事实上,

$$
\bar {\boldsymbol {Y}} = A \bar {\boldsymbol {X}} + \boldsymbol {a} \quad \text {且} \quad S _ {\boldsymbol {Y}} = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} \left(\boldsymbol {Y} _ {i} - \bar {\boldsymbol {Y}}\right) \left(\boldsymbol {Y} _ {i} - \bar {\boldsymbol {Y}}\right) ^ {\mathrm{T}} = A S _ {\boldsymbol {X}} A ^ {\mathrm{T}}.
$$

进而, 我们有  $\mu_{Y}=A\mu_{X}+a$ . 因此, 可以计算  $T_{Y}^{2}$ ,

$$
\begin{array}{l} T _ {\boldsymbol {Y}} ^ {2} = n \left(\bar {\boldsymbol {Y}} - \boldsymbol {\mu} _ {\boldsymbol {Y}}\right) ^ {\mathrm{T}} S _ {\boldsymbol {Y}} ^ {- 1} \left(\bar {\boldsymbol {Y}} - \boldsymbol {\mu} _ {\boldsymbol {Y}}\right) \\ = n \left(A \bar {\boldsymbol {X}} - A \boldsymbol {\mu} _ {\boldsymbol {X}}\right) ^ {\mathrm{T}} \left(A S _ {\boldsymbol {X}} A ^ {\mathrm{T}}\right) ^ {- 1} \left(A \bar {\boldsymbol {X}} - A \boldsymbol {\mu} _ {\boldsymbol {X}}\right) \\ = n \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {\boldsymbol {X}}\right) ^ {\mathrm{T}} A ^ {\mathrm{T}} \left(A ^ {\mathrm{T}}\right) ^ {- 1} S _ {\boldsymbol {X}} ^ {- 1} A ^ {- 1} A \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {\boldsymbol {X}}\right) \\ = n \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {\boldsymbol {X}}\right) ^ {\mathrm{T}} S _ {\boldsymbol {X}} ^ {- 1} \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {\boldsymbol {X}}\right) = T _ {\boldsymbol {X}} ^ {2}. \\ \end{array}
$$

此外, 由 F 分布的性质我们知道, 当 n 趋于无穷时,  $T^{2}$  统计量的分布趋于  $\chi^{2}$  分布. 事实上, 由多元中心极限定理和连续映射定理可证明, 当  $X_{1}, X_{2}, \cdots, X_{n} \sim (\mu_{0}, \Sigma)$  时,

$$
T ^ {2} \xrightarrow {\mathrm{d}} \chi_ {p} ^ {2}.
$$

也就是说, 即使样本不是多元正态分布, $T^2$ 仍然是渐近 $\chi^2$ 分布的. 因此, 实际应用中, 当样本量较大时, 我们常使用 $\chi_{\alpha}^{2}(p)$ 作为临界值.

下面, 我们换个思路, 从似然比检验的角度来考察如何构造多元检验. 这里仅考虑 $\Sigma$ 未知的情形.

命题 4.2.1 假设  $X_{1}, X_{2}, \cdots, X_{n}$  独立同分布于  $N_{p}(\boldsymbol{\mu}, \Sigma)$ ，其中  $\mu, \Sigma$  未知。对于  $H_{0}: \mu = \mu_{0} \leftrightarrow H_{1}: \mu \neq \mu_{0}$  的假设检验问题的似然比检验统计量为

$$
\Lambda = \frac {\max _ {\boldsymbol {\mu} = \boldsymbol {\mu} _ {0} , \Sigma} L \left(\boldsymbol {\mu} _ {0} , \Sigma ; \mathbb {X}\right)}{\max _ {\boldsymbol {\mu} , \Sigma} L \left(\boldsymbol {\mu} , \Sigma ; \mathbb {X}\right)} = \left(\frac {| \hat {\Sigma} |}{| \hat {\Sigma} _ {0} |}\right) ^ {n / 2},
$$

其中 $\hat{\Sigma} = \frac{1}{n}\sum_{i = 1}^{n}\left(\boldsymbol {X}_i - \bar{\boldsymbol{X}}\right)\left(\boldsymbol {X}_i - \bar{\boldsymbol{X}}\right)^{\mathrm{T}},\hat{\Sigma}_{0} = \frac{1}{n}\sum_{i = 1}^{n}\left(\boldsymbol {X}_i - \boldsymbol {\mu}_0\right)\left(\boldsymbol {X}_i - \boldsymbol {\mu}_0\right)^{\mathrm{T}}.$

证明 似然函数可写为

$$
\begin{array}{l} L \left(\boldsymbol {\mu}, \Sigma ; \mathbb {X}\right) = \frac {1}{\left(\sqrt {2 \pi}\right) ^ {n p} | \Sigma | ^ {n / 2}} \exp \left\{- \frac {\sum_ {i = 1} ^ {n} \left(\boldsymbol {x} _ {i} - \boldsymbol {\mu}\right) ^ {\mathrm{T}} \Sigma^ {- 1} \left(\boldsymbol {x} _ {i} - \boldsymbol {\mu}\right)}{2} \right\} \\ = \frac {1}{\left(\sqrt {2 \pi}\right) ^ {n p} | \Sigma | ^ {n / 2}} \exp \left\{- \frac {\operatorname{tr} \left[ \sum_ {i = 1} ^ {n} \left(\boldsymbol {x} _ {i} - \boldsymbol {\mu}\right) ^ {\mathrm{T}} \Sigma^ {- 1} \left(\boldsymbol {x} _ {i} - \boldsymbol {\mu}\right) \right]}{2} \right\} \\ = \frac {1}{\left(\sqrt {2 \pi}\right) ^ {n p} | \Sigma | ^ {n / 2}} \exp \left\{- \frac {\operatorname{tr} \left[ \Sigma^ {- 1} \sum_ {i = 1} ^ {n} \left(\boldsymbol {x} _ {i} - \boldsymbol {\mu}\right) \left(\boldsymbol {x} _ {i} - \boldsymbol {\mu}\right) ^ {\mathrm{T}} \right]}{2} \right\}. \\ \end{array}
$$

对于分子:当  $\mu = \mu_{0}$  和  $\hat{\Sigma}_{0} = \frac{1}{n} \sum_{i=1}^{n} (\boldsymbol{x}_{i} - \boldsymbol{\mu}_{0}) (\boldsymbol{x}_{i} - \boldsymbol{\mu}_{0})^{\mathrm{T}}$  时，可以取到最大值，且最大值为

$$
\begin{array}{l} \max _ {\boldsymbol {\mu} = \boldsymbol {\mu} _ {0}, \Sigma} L \left(\boldsymbol {\mu} _ {0}, \Sigma ; \mathbb {X}\right) = \frac {1}{\left(\sqrt {2 \pi}\right) ^ {n p} \left| \hat {\Sigma} _ {0} \right| ^ {n / 2}} \exp \left\{- \frac {\operatorname{tr} \left(n I _ {p}\right)}{2} \right\} \\ = \frac {1}{\left(\sqrt {2 \pi}\right) ^ {n p} | \hat {\Sigma} _ {0} | ^ {n / 2}} \exp \left\{- \frac {n p}{2} \right\}. \\ \end{array}
$$

对于分母: 当  $\mu = \bar{x}$  和  $\hat{\Sigma} = \frac{1}{n} \sum_{i=1}^{n} (\boldsymbol{x}_{i} - \bar{\boldsymbol{x}}) (\boldsymbol{x}_{i} - \bar{\boldsymbol{x}})^{\mathrm{T}}$  时, 可以取到最大值, 且最大值为

$$
\begin{array}{l} \max _ {\boldsymbol {\mu}, \Sigma} L \left(\boldsymbol {\mu}, \Sigma ; \mathbb {X}\right) = \frac {1}{\left(\sqrt {2 \pi}\right) ^ {n p} | \hat {\Sigma} | ^ {n / 2}} \exp \left\{- \frac {\operatorname{tr} \left(n I _ {p}\right)}{2} \right\} \\ = \frac {1}{\left(\sqrt {2 \pi}\right) ^ {n p} | \hat {\Sigma} | ^ {n / 2}} \exp \left\{- \frac {n p}{2} \right\}. \\ \end{array}
$$

计算后可得到结论.

我们有如下结论.

命题4.2.2 $\Lambda^{2 / n} = \left(1 + \frac{T^2}{n - 1}\right)^{-1}.$

证明 注意到

$$
\begin{array}{l} \hat {\Sigma} _ {0} = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(\boldsymbol {X} _ {i} - \boldsymbol {\mu} _ {0}\right) \left(\boldsymbol {X} _ {i} - \boldsymbol {\mu} _ {0}\right) ^ {\mathrm{T}} \\ = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}} + \bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}\right) \left(\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}} + \bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}\right) ^ {\mathrm{T}} \\ = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}\right) \left(\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}\right) ^ {\mathrm{T}} + \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}\right) \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}\right) ^ {\mathrm{T}} \\ = \hat {\Sigma} + \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}\right) \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}\right) ^ {\mathrm{T}}. \\ \end{array}
$$

考虑一个 $(p + 1)\times (p + 1)$ 矩阵，

$$
A = \left( \begin{array}{c c} \hat {\Sigma} & - (\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}) \\ (\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}) ^ {\mathrm{T}} & 1 \end{array} \right) = \left( \begin{array}{c c} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right).
$$

由条件多元正态分布的证明, 我们有  $\left|\hat{\Sigma}_{0}\right|=\left|A\right|=\left|A_{11}\right|\left|A_{22}-A_{21}A_{11}^{-1}A_{12}\right|$ , 因此

$$
\begin{array}{l} \left| \hat {\Sigma} _ {0} \right| = \left| \hat {\Sigma} \right| \left| 1 + \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}\right) ^ {\mathrm{T}} \hat {\Sigma} ^ {- 1} \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}\right) \right| \\ = | \hat {\Sigma} | \left| 1 + \frac {n \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}\right) ^ {\mathrm{T}} S ^ {- 1} \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}\right)}{n - 1} \right|. \\ \end{array}
$$

由此结论成立.

因此， $-2\ln(\Lambda^{2/n})$  与  $T^{2}$  具有一一映射关系，故基于似然比的检验与  $T^{2}$  检验等价。这再次说明，对于参数推断问题，分布已知时，似然方法可以作为我们默认使用的机制。事实上，根据第三章中的 Wilks 定理可知，在  $H_{0}$  下，

$$
- 2 \ln \left(\varLambda^ {2 / n}\right) \xrightarrow {\mathrm{d}} \chi^ {2} (p).
$$

这与前述  $T^{2}$  统计量的零假设渐近分布吻合 (也可通过二者的关系由 Taylor 展开直接得到).

在第三章中我们主要讨论了对于单参数的置信区间的概念, 而对于多元问题来说, 这一概念可相应地拓展为置信区域或更一般地成为置信集. 这里当

$$
P \left(\boldsymbol {\mu} \in R \left(\mathbb {X}\right)\right) \geqslant 1 - \alpha
$$

满足时, 我们称  $R(\mathbb{X})$  为  $\mu$  的  $1 - \alpha$  置信区域.

由 3.5.5 小节中所介绍的通过假设检验求取置信区间的方法我们不难看出, 对于来自  $N_{p}(\boldsymbol{\mu}, \Sigma)$  的独立同分布样本  $X_{1}, X_{2}, \cdots, X_{n}$ ,

$$
\left\{\boldsymbol {\mu}: n \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu}\right) ^ {\mathrm{T}} S ^ {- 1} \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu}\right) \leqslant \frac {(n - 1) p}{n - p} F _ {\alpha} (p, n - p) \right\} \tag {4.2.2}
$$

是关于  $\mu$  的  $1-\alpha$  置信区域.

这个区域依赖于观测值 (即随机区域, 它随样本不同而改变). 对于具体给定的一组样本, 我们有 $1 - \alpha$ 的概率保证所得的 $\mu$ 可以满足 (4.2.2). 注意, 不等式 (4.2.2) 表示的是 $p$ 维空间中关于 $\mu$ 的一个椭圆圆周及其内部, 其中心为 $\bar{X}$, 其大小和形状取决于 $S$ 和 $\alpha$, 而 (4.2.2) 中的 $\mu$ 可以看作是依赖于随机样本的随机椭圆.

由 (4.2.2) 的置信区域出发, 我们还可以给出所有变量的线性组合构成的置信区域, 即  $a^{T}\mu$  的置信区间, 其中  $a \in R^{p}$  是一非零常数向量. 注意到

$$
t _ {\boldsymbol {a}} = \frac {\sqrt {n} (\boldsymbol {a} ^ {\mathrm{T}} \bar {\boldsymbol {X}} - \boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {\mu})}{\sqrt {\boldsymbol {a} ^ {\mathrm{T}} S \boldsymbol {a}}} \sim t (n - 1).
$$

因此，

$$
\left[ \boldsymbol {a} ^ {\mathrm{T}} \bar {\boldsymbol {X}} - t _ {\alpha / 2} (n - 1) \frac {\sqrt {\boldsymbol {a} ^ {\mathrm{T}} S \boldsymbol {a}}}{\sqrt {n}}, \boldsymbol {a} ^ {\mathrm{T}} \bar {\boldsymbol {X}} + t _ {\alpha / 2} (n - 1) \frac {\sqrt {\boldsymbol {a} ^ {\mathrm{T}} S \boldsymbol {a}}}{\sqrt {n}} \right]
$$

就是  $a^{T}\mu$  的  $1-\alpha$  置信区间.

特别地, 如果我们希望得到每个变量的置信区间, 我们可以令  $\boldsymbol{a}^{\mathrm{T}} = (1, 0, \cdots, 0)$ ,  $\boldsymbol{a}^{\mathrm{T}} = (0, 1, \cdots, 0)$  或者  $\boldsymbol{a}^{\mathrm{T}} = (0, \cdots, 0, 1)$ , 但如果我们同时构造了上述 p 个置信区间, 就无法保证它们同时覆盖真实参数值的概率为  $1 - \alpha$ . 我们应该做何种调整呢? 这里我们利用如下引理.

引理 4.2.2 令 A 为一个  $p \times p$  正定矩阵, a 为一个 p 维向量. 则对于任意非零向量 v,

$$
\max _ {\boldsymbol {v} \neq \boldsymbol {0}} \frac {(\boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {a}) ^ {2}}{\boldsymbol {v} ^ {\mathrm{T}} A \boldsymbol {v}} = \boldsymbol {a} ^ {\mathrm{T}} A ^ {- 1} \boldsymbol {a}.
$$

证明 由推广的 Cauchy-Schwarz 不等式,

$$
\begin{array}{l} (\boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {a}) ^ {2} = (\boldsymbol {v} ^ {\mathrm{T}} A ^ {1 / 2} A ^ {- 1 / 2} \boldsymbol {a}) ^ {2} \\ \leqslant (\boldsymbol {v} ^ {\mathrm{T}} A ^ {1 / 2} A ^ {1 / 2} \boldsymbol {v}) (\boldsymbol {a} ^ {\mathrm{T}} A ^ {- 1 / 2} A ^ {- 1 / 2} \boldsymbol {a}) = (\boldsymbol {v} ^ {\mathrm{T}} A \boldsymbol {v}) (\boldsymbol {a} ^ {\mathrm{T}} A ^ {- 1} \boldsymbol {a}). \\ \end{array}
$$

当  $v^{T}A^{1/2}=cA^{-1/2}a$  时, 等式成立, 即  $v=cA^{-1}a$ .

根据该引理, 我们有

$$
\max _ {\boldsymbol {a} \neq \boldsymbol {0}} t _ {\boldsymbol {a}} ^ {2} = \max _ {\boldsymbol {a} \neq \boldsymbol {0}} \frac {n (\boldsymbol {a} ^ {\mathrm{T}} \bar {\boldsymbol {X}} - \boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {\mu}) ^ {2}}{\boldsymbol {a} ^ {\mathrm{T}} S \boldsymbol {a}} = n (\bar {\boldsymbol {X}} - \boldsymbol {\mu}) ^ {\mathrm{T}} S ^ {- 1} (\bar {\boldsymbol {X}} - \boldsymbol {\mu}) = T ^ {2},
$$

而最大值在 $\pmb{a}$ 与 $S^{-1}(\bar{\pmb{X}} -\pmb{\mu})$ 成比例时取得.因此我们可以给出均值向量线性组合的一致置信区间:

$$
\begin{array}{l} \boldsymbol {a} ^ {\mathrm{T}} \bar {\boldsymbol {X}} - \sqrt {\frac {p (n - 1)}{n (n - p)} F _ {\alpha} (p , n - p) \boldsymbol {a} ^ {\mathrm{T}} S \boldsymbol {a}} \leqslant \boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {\mu} \\ \leqslant \boldsymbol {a} ^ {\mathrm{T}} \bar {\boldsymbol {X}} + \sqrt {\frac {p (n - 1)}{n (n - p)} F _ {\alpha} (p , n - p) \boldsymbol {a} ^ {\mathrm{T}} S \boldsymbol {a}}. \\ \end{array}
$$

由此结论, 我们可知对于  $k=1,2,\cdots,p$ , 我们有如下类似一元正态样本时的置信区间,

$$
\left[ \bar {X} _ {k} - \sqrt {\frac {p (n - 1)}{n - p} F _ {\alpha} (p , n - p)} \sqrt {\frac {s _ {k k}}{n}}, \bar {X} _ {k} + \sqrt {\frac {p (n - 1)}{n - p} F _ {\alpha} (p , n - p)} \sqrt {\frac {s _ {k k}}{n}} \right].
$$

这 k 个置信区间以不低于  $1 - \alpha$  的概率同时分别覆盖  $\mu_{k}, k = 1, 2, \cdots, p$ .

此外，我们还可以令  $\boldsymbol{a} = (0, \cdots, 0, a_{i}, 0, \cdots, 0, a_{k}, 0, \cdots, 0)^{\mathrm{T}}$ ，这样可以给出形如  $\mu_{i} - \mu_{k}$  的置信区间，也就是取  $a_{i} = 1$  和  $a_{k} = -1$ 。在此情况下， $a^{T} S a = s_{ii} - 2 s_{ik} + s_{kk}$ ，我们有

$$
\begin{array}{l} P \left((\mu_ {i} - \mu_ {k}) \in \left[ \bar {Y} _ {i} - \bar {Y} _ {k} \pm \sqrt {\frac {p (n - 1)}{n - p} F _ {\alpha} (p , n - p)} \sqrt {\frac {s _ {i i} - 2 s _ {i k} + s _ {k k}}{n}} \right], \forall i, k\right) \\ \geqslant 1 - \alpha . \\ \end{array}
$$

## 二、两样本和多样本均值向量的多元检验

我们先考虑成对样本的检验问题. 假设 $p$ 维样本 $\{\mathbf{X}_i\}_{i=1}^n$ 与 $\{\mathbf{Y}_i\}_{i=1}^n$ 为成对多元正态样本. 目标是考察二者均值向量的差异 $\mu_d = \mu_X - \mu_Y$. 可知 $d_i = X_i - Y_i$ 独立同分布于 $N_p(\mu_d, \Sigma_d)$. 则对于假设检验问题

$$
H _ {0}: \boldsymbol {\mu} _ {d} = \mathbf {0} \leftrightarrow H _ {1}: \boldsymbol {\mu} _ {d} \neq \mathbf {0}.
$$

我们自然地构造检验统计量:

$$
T ^ {2} = n \bar {\boldsymbol {d}} ^ {\mathrm{T}} S _ {\boldsymbol {d}} ^ {- 1} \bar {\boldsymbol {d}} \sim T ^ {2} (p, n - 1), \quad \text {当} H _ {0} \text {成立时},
$$

其中 $\bar{\pmb{d}} = \frac{1}{n}\sum_{i = 1}^{n}\pmb{d}_i$ 为差异样本均值， $S_{\pmb{d}} = \frac{1}{n - 1}\sum_{i = 1}^{n}(\pmb{d}_i - \bar{\pmb{d}})(\pmb{d}_i - \bar{\pmb{d}})^{\mathrm{T}}$ 为差异的样本协方差.如果 $\frac{n - p}{(n - 1)p} T^2 >F_\alpha (p,n - p)$ ，则拒绝 $H_0$ .相应地， $\pmb{\mu}_{\pmb{d}}$ 的置信区域为

$$
\left\{\boldsymbol {\mu} _ {\boldsymbol {d}}: (\bar {\boldsymbol {d}} - \boldsymbol {\mu} _ {\boldsymbol {d}}) ^ {\mathrm{T}} S _ {\boldsymbol {d}} ^ {- 1} (\bar {\boldsymbol {d}} - \boldsymbol {\mu} _ {\boldsymbol {d}}) \leqslant \frac {(n - 1) p}{n (n - p)} F _ {\alpha} (p, n - p) \right\}.
$$

例 4.2.1 为了比较两种类型的涂层的耐腐蚀性, 每种类型对 15 根管道进行了涂层. 两条管道, 每种涂层一根, 埋在一起, 在 15 个不同的位置放置相同的时间. 第一种涂层的腐蚀程度通过如下两个量描述:

$$
y _ {1} = \text {凹坑的最大深度(千分之一英寸} ^ {\text {①}}),
$$

$$
y _ {2} = \text {凹坑的数量},
$$

同时  $x_{1}$  与  $x_{2}$  为第二种涂层中的对应度量定义. 如何比较两种涂层?

解 数据及差值如表 4.2.1 给出.

表 4.2.1 例 4.2.1 中的涂层数据及差值

<table><tr><td rowspan="2">位置</td><td colspan="2">第一种涂层</td><td colspan="2">第二种涂层</td><td colspan="2">差值</td></tr><tr><td>深度 $y_1$ </td><td>数量 $y_2$ </td><td>深度 $x_1$ </td><td>数量 $x_2$ </td><td>深度 $d_1$ </td><td>数量 $d_2$ </td></tr><tr><td>1</td><td>73</td><td>31</td><td>51</td><td>35</td><td>22</td><td>-4</td></tr><tr><td>2</td><td>43</td><td>19</td><td>41</td><td>14</td><td>2</td><td>5</td></tr><tr><td>3</td><td>47</td><td>22</td><td>43</td><td>19</td><td>4</td><td>3</td></tr><tr><td>4</td><td>53</td><td>26</td><td>41</td><td>29</td><td>12</td><td>-3</td></tr><tr><td>5</td><td>58</td><td>36</td><td>47</td><td>34</td><td>11</td><td>2</td></tr><tr><td>6</td><td>47</td><td>30</td><td>32</td><td>26</td><td>15</td><td>4</td></tr><tr><td>7</td><td>52</td><td>29</td><td>24</td><td>19</td><td>28</td><td>10</td></tr><tr><td>8</td><td>38</td><td>36</td><td>43</td><td>37</td><td>-5</td><td>-1</td></tr><tr><td>9</td><td>61</td><td>34</td><td>53</td><td>24</td><td>8</td><td>10</td></tr><tr><td>10</td><td>56</td><td>33</td><td>52</td><td>27</td><td>4</td><td>6</td></tr><tr><td>11</td><td>56</td><td>19</td><td>57</td><td>14</td><td>-1</td><td>5</td></tr><tr><td>12</td><td>34</td><td>19</td><td>44</td><td>19</td><td>-10</td><td>0</td></tr><tr><td>13</td><td>55</td><td>26</td><td>57</td><td>30</td><td>-2</td><td>-4</td></tr><tr><td>14</td><td>65</td><td>15</td><td>40</td><td>7</td><td>25</td><td>8</td></tr><tr><td>15</td><td>75</td><td>18</td><td>68</td><td>13</td><td>7</td><td>5</td></tr></table>

基于 15 个差值向量, 可计算得到

$$
\bar {\boldsymbol {d}} = \binom{8. 0 0 0}{3. 0 6 7}, \quad S _ {\boldsymbol {d}} = \left( \begin{array}{c c} 1 2 1. 5 7 1 & 1 7. 0 7 1 \\ 1 7. 0 7 1 & 2 1. 7 8 1 \end{array} \right).
$$

于是

$$
T ^ {2} = 1 5 (8. 0 0 0, 3. 0 6 7) \left( \begin{array}{c c} 1 2 1. 5 7 1 & 1 7. 0 7 1 \\ 1 7. 0 7 1 & 2 1. 7 8 1 \end{array} \right) ^ {- 1} \binom{8. 0 0 0}{3. 0 6 7} = 1 0. 8 1 9.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 1 英寸 =2.54 cm.</span></small>

下面考虑两样本均值比较问题. 假设我们有两个独立的样本  $\{X_{i}\}_{i=1}^{n_{1}}$  和  $\{Y_{i}\}_{i=1}^{n_{2}}$ ，两者分别为来自  $N_{p}(\boldsymbol{\mu}_{1},\Sigma)$  和  $N_{p}(\boldsymbol{\mu}_{2},\Sigma)$  的独立同分布样本，其中  $\Sigma$  为共同但未知的协方差矩阵. 检验问题为

$$
H _ {0}: \boldsymbol {\mu} _ {1} = \boldsymbol {\mu} _ {2} \leftrightarrow H _ {1}: \boldsymbol {\mu} _ {1} \neq \boldsymbol {\mu} _ {2}.
$$

显然, 我们可以用  $\bar{X}-\bar{Y}$  估计  $\mu_{1}-\mu_{2}$ . 则  $E(\bar{X}-\bar{Y})=\mu_{1}-\mu_{2}, \operatorname{Cov}(\bar{X}-\bar{Y})=\left(\frac{1}{n_{1}}+\frac{1}{n_{2}}\right)\Sigma.$  由于已知两个样本具有相同的协方差, 因此合并两样本信息来估计  $\Sigma:$

$$
\begin{array}{l} S _ {p l} = \frac {\sum_ {i = 1} ^ {n _ {1}} (\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}) (\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}) ^ {\mathrm{T}} + \sum_ {i = 1} ^ {n _ {2}} (\boldsymbol {Y} _ {i} - \bar {\boldsymbol {Y}}) (\boldsymbol {Y} _ {i} - \bar {\boldsymbol {Y}}) ^ {\mathrm{T}}}{n _ {1} + n _ {2} - 2} \\ = \frac {(n _ {1} - 1) S _ {1} + (n _ {2} - 1) S _ {2}}{n _ {1} + n _ {2} - 2}, \\ \end{array}
$$

它是  $\Sigma$  的无偏估计. 由此, 可构造检验统计量:

$$
\begin{array}{l} T ^ {2} = (\bar {\boldsymbol {X}} - \bar {\boldsymbol {Y}}) ^ {\mathrm{T}} \left[ \left(\frac {1}{n _ {1}} + \frac {1}{n _ {2}}\right) S _ {p l} \right] ^ {- 1} (\bar {\boldsymbol {X}} - \bar {\boldsymbol {Y}}) \tag {4.2.3} \\ = \frac {n _ {1} n _ {2}}{n _ {1} + n _ {2}} (\bar {\boldsymbol {X}} - \bar {\boldsymbol {Y}}) ^ {\mathrm{T}} S _ {p l} ^ {- 1} (\bar {\boldsymbol {X}} - \bar {\boldsymbol {Y}}) \sim T ^ {2} (p, n _ {1} + n _ {2} - 2). \\ \end{array}
$$

可见, 相应的拒绝域为  $\frac{n_{1}+n_{2}-p-1}{(n_{1}+n_{2}-2)p}T^{2}>F_{\alpha}(p,n_{1}+n_{2}-p-1)$ .

记 $c^2 = \frac{(n_1 + n_2 - 2)p}{n_1 + n_2 - p - 1} F_\alpha (p,n_1 + n_2 - p - 1).\mu_1 - \mu_2$ 的置信区域为

$$
\left\{\boldsymbol {\mu} _ {1} - \boldsymbol {\mu} _ {2}: \left[ (\bar {\boldsymbol {X}} - \bar {\boldsymbol {Y}}) - (\boldsymbol {\mu} _ {1} - \boldsymbol {\mu} _ {2}) \right] ^ {\mathrm{T}} \left[ \left(\frac {1}{n _ {1}} + \frac {1}{n _ {2}}\right) S _ {p l} \right] ^ {- 1} \left[ (\bar {\boldsymbol {X}} - \bar {\boldsymbol {Y}}) - (\boldsymbol {\mu} _ {1} - \boldsymbol {\mu} _ {2}) \right] \leqslant c ^ {2} \right\}.
$$

下面考虑两个样本的协方差不相同时如何处理. 我们有如下关于 (4.2.3) 式所定义的两样本  $T^{2}$  的渐近零分布性质.

定理 4.2.2 在  $H_{0}$  下, 当  $n_{1}, n_{2} \rightarrow \infty$  时,

$$
T ^ {2} = (\bar {\boldsymbol {X}} - \bar {\boldsymbol {Y}}) ^ {\mathrm{T}} \left(\frac {1}{n _ {1}} S _ {1} + \frac {1}{n _ {2}} S _ {2}\right) ^ {- 1} (\bar {\boldsymbol {X}} - \bar {\boldsymbol {Y}}) \stackrel {{\mathrm{d}}} {{\longrightarrow}} \chi^ {2} (p).
$$

因此我们有大样本检验: 当  $T^{2} > \chi_{\alpha}^{2}(p)$  时, 拒绝  $H_{0}$ .

最后, 我们再来考察一下多样本情形下的多元检验问题, 也就是单因素多元方差分析 (MANOVA). 这里我们假设  $X_{\ell1}, X_{\ell2}, \cdots, X_{\ell n_{\ell}}$  分别为来自  $N_{p}(\boldsymbol{\mu}_{\ell}, \Sigma)$  的独立同分布样本,  $\ell = 1, 2, \cdots, k$ , 且所有样本相互独立. 单因素方差分析问题就是

$$
H _ {0}:   \pmb {\mu} _ {1} = \pmb {\mu} _ {2} = \dots = \pmb {\mu} _ {k} \leftrightarrow H _ {1}:   \pmb {\mu} _ {i} \text {不全相等}.
$$

等价地, 令 $\pmb{\mu}_{\ell} = \pmb{\mu} + \pmb{\tau}_{\ell}$, 其中 $\pmb{\mu} = \frac{1}{n} \sum_{\ell=1}^{k} n_{\ell} \pmb{\mu}_{\ell}$, 记 $n = \sum_{\ell=1}^{k} n_{\ell}$, 其约束为 $\sum_{\ell=1}^{k} n_{\ell} \pmb{\tau}_{\ell} = 0$,

$$
H _ {0}: \text {对所有} \ell , \tau_ {\ell} = 0 \leftrightarrow H _ {1}: \tau_ {\ell} \neq 0.
$$

由此我们可以记 $X_{\ell i} = \pmb{\mu} + (\pmb{\mu}_{\ell} - \pmb{\mu}) + \varepsilon_{\ell i} = \pmb{\mu} + \pmb{\tau}_{\ell} + \varepsilon_{\ell i}$. 类似于3.2.3小节中的一元单因素方差分析表, 我们有如下的单因素多元方差分析表 (表4.2.2).

表 4.2.2 单因素多元方差分析表

| 变差源 | 平方和矩阵(SS) | 自由度(df) |
| --- | --- | --- |
| 处理 | $\boldsymbol{B} = \sum_{\ell=1}^{k} n_{\ell} (\bar{\boldsymbol{X}}_{\ell} - \bar{\boldsymbol{X}})(\bar{\boldsymbol{X}}_{\ell} - \bar{\boldsymbol{X}})^{\mathrm{T}}$ | $k-1$ |
| 残差(误差) | $\boldsymbol{W} = \sum_{\ell=1}^{k} \sum_{i=1}^{n_{\ell}} (\boldsymbol{X}_{\ell i} - \bar{\boldsymbol{X}}_{\ell})(\boldsymbol{X}_{\ell i} - \bar{\boldsymbol{X}}_{\ell})^{\mathrm{T}}$ | $\sum_{\ell=1}^{k} (n_{\ell}-1)$ |
| 总和(均值校正) | $\boldsymbol{B} + \boldsymbol{W} = \sum_{\ell=1}^{k} \sum_{i=1}^{n_{\ell}} (\boldsymbol{X}_{\ell i} - \bar{\boldsymbol{X}})(\boldsymbol{X}_{\ell i} - \bar{\boldsymbol{X}})^{\mathrm{T}}$ | $\sum_{\ell=1}^{k} n_{\ell}-1$ |

其中

- $\bar{X} = \frac{1}{\sum_{\ell=1}^{k} n_{\ell}} \sum_{\ell=1}^{k} \sum_{i=1}^{n_{\ell}} X_{\ell i}, \bar{X}_{\ell} = \frac{1}{n_{\ell}} \sum_{i=1}^{n_{\ell}} X_{\ell i}.$
- $\operatorname{Cov}(\boldsymbol{X}_{\ell i}-\bar{\boldsymbol{X}}_{\ell},\bar{\boldsymbol{X}}_{\ell}-\bar{\boldsymbol{X}})=\frac{1}{n_{\ell}}\Sigma-\frac{1}{\sum_{\ell=1}^{k}n_{\ell}}\Sigma-\frac{1}{n_{\ell}}\Sigma+\frac{n_{\ell}}{n_{\ell}\sum_{\ell=1}^{k}n_{\ell}}\Sigma=0.$
- $B \sim W_p(k - 1, \Sigma)$ 与 $B + W \sim W_p\left(\sum_{\ell=1}^{k} n_\ell - 1, \Sigma\right)$ 相互独立.

考虑使用似然比检验. 类似单样本均值的似然比检验, 计算可得似然比统计量  $\Lambda$  可表示为  $\Lambda^{\frac{2}{n}} = \frac{|W|}{|B + W|}$ . 再次使用 Wilks 定理, 可知在  $H_{0}$  下,

$$
- 2 \ln (\varLambda) \to \chi^ {2} (p (k - 1)).
$$

因此, 如果  $-2\ln(\Lambda) > \chi_{\alpha}^{2}(p(k-1))$ , 则拒绝  $H_{0}$ . 这是一个显著性水平为  $\alpha$  的大样本检验.

## 三、协方差矩阵检验

考虑单样本协方差矩阵检验问题. 假设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $N_{p}(\boldsymbol{\mu}, \Sigma)$  的 p 维独立同分布样本. 欲检验  $\Sigma$  是否等于某一给定的矩阵, 如单位矩阵, 即

$$
H _ {0}: \Sigma = \Sigma_ {0} (\Sigma_ {0} \text {正定且已知}) \leftrightarrow H _ {1}: \Sigma \neq \Sigma_ {0}.
$$

此时的似然比检验统计量为

$$
\varLambda = \frac {\max _ {\boldsymbol {\mu}} L (\boldsymbol {\mu} , \Sigma_ {0})}{\max _ {\boldsymbol {\mu} , \Sigma} L (\boldsymbol {\mu} , \Sigma)} = \exp \left\{- \frac {1}{2} \mathrm{tr} \left(A \Sigma_ {0} ^ {- 1}\right) \right\} | A \Sigma_ {0} ^ {- 1} | ^ {n / 2} (\mathrm{e} / n) ^ {n p / 2}.
$$

其中 $A = (n - 1)S = \sum_{i=1}^{n} (\boldsymbol{X}_i - \bar{\boldsymbol{X}})(\boldsymbol{X}_i - \bar{\boldsymbol{X}})^{\mathrm{T}}$。可知，当 $n \to \infty$ 时，$-2\ln(\Lambda) \to \chi^2(p(p + 1)/2)$。则当 $-2\ln(\Lambda) > \chi_\alpha^2(p(p + 1)/2)$ 时拒绝 $H_0$。

最后再考虑多样本情形下的推广. 假设有 $k$ 组独立同分布样本

$$
\boldsymbol {X} _ {\ell 1}, \boldsymbol {X} _ {\ell 2}, \dots , \boldsymbol {X} _ {\ell n _ {\ell}} \sim N _ {p} (\boldsymbol {\mu} _ {\ell}, \Sigma_ {\ell}), \ell = 1, 2, \dots , k,
$$

且所有样本相互独立. 假设检验问题为

$$
H _ {0}: \Sigma_ {1} = \Sigma_ {2} = \dots = \Sigma_ {k} \leftrightarrow H _ {1}: \Sigma_ {i} \neq \Sigma_ {j}, \text {对于某些} i \neq j.
$$

此时的似然比检验统计量为

$$
\begin{array}{l} \Lambda = \frac {\max _ {\boldsymbol {\mu} _ {\ell} , \Sigma} \prod_ {\ell = 1} ^ {k} L (\boldsymbol {\mu} _ {\ell} , \Sigma)}{\max _ {\boldsymbol {\mu} _ {\ell} , \Sigma_ {\ell}} \prod_ {\ell = 1} ^ {k} L (\boldsymbol {\mu} _ {\ell} , \Sigma_ {\ell})} = \frac {\prod_ {\ell = 1} ^ {k} L (\bar {\boldsymbol {X}} _ {\ell} , \widehat {\Sigma})}{\prod_ {\ell = 1} ^ {k} L (\bar {\boldsymbol {X}} _ {\ell} , \widehat {\Sigma} _ {\ell})} \\ = \frac {| \widehat {\Sigma} | ^ {- n / 2}}{\prod_ {\ell = 1} ^ {k} | \widehat {\Sigma} _ {\ell} | ^ {- n _ {\ell} / 2}} = \prod_ {\ell = 1} ^ {k} \left(\frac {| \widehat {\Sigma} _ {\ell} |}{| \widehat {\Sigma} |}\right) ^ {n _ {\ell} / 2}, \\ \end{array}
$$

其中 $n_{\ell}\widehat{\Sigma}_{\ell} = \sum_{i=1}^{n_{\ell}}(\boldsymbol{X}_{\ell i} - \bar{\boldsymbol{X}}_{\ell})(\boldsymbol{X}_{\ell i} - \bar{\boldsymbol{X}}_{\ell})^{\mathrm{T}} = (n_{\ell} - 1)S_{\ell}, \widehat{\Sigma} = \frac{1}{n}\sum_{\ell=1}^{k}n_{\ell}\widehat{\Sigma}_{\ell}$. 由 Wilks 定理可知, $-2\ln(\Lambda)\xrightarrow{\mathrm{d}}\chi^{2}\left(\frac{1}{2}p(p+1)(k-1)\right)$, 这里的自由度仍为备择假设下和原假设下自由参数个数的差异.

## 4.3 多重检验

在 4.2.2 小节中, 我们考虑的多元检验问题通常是单一检验问题, 如多元均值检验问题  $H_{0} : \mu = \mu_{0}$ , 但在很多时候, 我们可能 (或者说在  $H_{0}$  被拒绝后) 需要同时考察每个变量 (分量) 的检验问题, 也就是  $H_{0k} : \mu_{k} = \mu_{0k}$ , 此时我们将同时做多个假设检验. 我们可以容易地构造检验来控制每个检验的第一类错误概率为  $\alpha$ , 但是不难看出同时做多个检验时, 至少有一个检验犯拒真错误的概率就不再是  $\alpha$  了. 因此, 我们需要对检验方法 (包括错误准则和临界值选取) 进行修正, 这就是所谓的多重检验 (multiple testing) 问题. 在文献中, 很多时候又把前面的多元情形下单一检验问题称作全局检验 (global testing) 以示区别.

## 4.3.1 基本概念

我们先来看一个例子.

例 4.3.1 (DNA 微阵列数据的检验问题) DNA 微阵列允许研究人员测量表达成千上万的基因水平. 数据是每一个基因的 mRNA(信使 RNA) 的表达水平, 其被认为是基因产生的蛋白质的一个度量. 大致上, 这个数字越大, 基因就越活跃. 这里我们考虑急性心肌梗死患者的实证分析问题 (Bourgon (布尔贡) 等, 2010). 该问题中我们有一组淋巴母细胞白血病数据, 包括 79 名参加意大利 GIMEMA 中心临床试验的成人患者的 12 256 个基因的表达水平, 该数据可在网上下载得到. 这 79 名患者根据其临床表现被分为两组, 分别有 37 和 42 名患者. 我们的目标就是探究两组患者在每个基因上的差异, 此时我们将同时进行 12 256 个假设检验. 假设每一个检验的水平为 $\alpha$. 则对任何一个检验来说, 被错误拒绝原假设 (即两组患者在这一基因上的表达水平没有差别) 的可能性就是 $\alpha$. 但是, 在这一万多次检验中, 至少有一次错误拒绝的概率要高得多.

例 4.3.2 (多重比较 (multiple comparison)) 事实上, 多重检验问题的历史可追溯到 20 世纪 50 年代由 Tukey (图基) 提出的多重比较问题, 后者就是前者的一个特例. 多重比较来自我们在 3.2.3 小节中考虑的方差分析问题. 假设因素 A 有 r 个水平, 在第 i 个水平下独立做了  $n_{i}$  次试验, 收集到的数据为

$$
\{y _ {i j}, j = 1, 2, \dots , n _ {i}; i = 1, 2, \dots , r \},
$$

假设数据来自单因素方差分析模型:

$$
\left\{ \begin{array}{l} {Y _ {i j} = \mu_ {i} + \varepsilon_ {i j}, j = 1, 2, \dots , n _ {i}, i = 1, 2, \dots , r,} \\ {\varepsilon_ {i j} \text {相互独立且来自} N (0, \sigma^ {2}).} \end{array} \right. \tag {4.3.1}
$$

单因素方差检验的假设问题为

$$
H _ {0}: \mu_ {1} = \mu_ {2} = \dots = \mu_ {r}.
$$

这是一个单一检验问题, 也可以被看作是我们前述的全局检验问题. 那么, 如果我们需要检验上述任两个水平间是否有显著差异, 也就是进行两两比较, 即需要检验如下  $\binom{r}{2}$  (多重) 个假设问题 (比较):

$$
H _ {0} ^ {i j}: \mu_ {i} = \mu_ {j}, i <   j, \tag {4.3.2}
$$

所以这就是一个多重检验问题.

这类问题在现代许多大数据问题中都会遇到, 我们可能经常同时做数百甚至数百万个检验. 我们记 m 个假设检验为

$$
H _ {0 i} \leftrightarrow H _ {1 i}, i = 1, 2, \dots , m.
$$