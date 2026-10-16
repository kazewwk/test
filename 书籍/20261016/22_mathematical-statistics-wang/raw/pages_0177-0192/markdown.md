实证科学中大部分可观察现象都具有多变量的特性. 例如, 股票市场中的资产同时被观察, 并分析它们的联合走势, 以更好地理解一般趋势和跟踪指数. 在医学中, 记录在不同地点的受试者的观察是可靠诊断和药物治疗的基础. 在定量营销中, 收集消费者偏好以构建消费者行为模型. 这些以及许多其他应用科学的定量研究的基本理论结构是多变量的. 现代数据分析很大程度上是围绕多变量 (或称为多元) 问题展开的, 而变量之间的相关性使得我们在建模分析的理论和方法上都需要新的手段. 因此, 在本章中我们考虑如何将前三章中的基本统计推断方法推广至多元情形下.

多元统计分析是统计学的核心课程之一, 由于篇幅所限, 在本书中我们仅选择最核心的部分内容予以介绍, 力图与前三章内容相呼应, 使读者对多元模型统计推断的基本思想建立较为初步的基础, 并作为第五章中线性回归模型的理论基础. 我们将首先回顾多元随机变量及其分布, 之后以多元正态分布这个最为经典的多元分布为例介绍参数多元模型下的统计推断方法, 最后对多重检验 (比较) 问题给予初步探讨.

## 4.1 多元分布

## 4.1.1 随机向量

首先我们回顾一下二元随机变量 $(X,Y)$ ，其协方差为

$$
\sigma_ {X Y} = \mathrm{Cov} (X, Y) = E [ (X - \mu_ {X}) (Y - \mu_ {Y}) ] = E (X Y) - \mu_ {X} \mu_ {Y},
$$

相应地, 相关系数为

$$
\rho_ {X Y} = \mathrm{Corr} (X, Y) = \frac {\sigma_ {X Y}}{\sigma_ {X} \sigma_ {Y}}.
$$

当  $\sigma_{XY}=0$  时, 我们称 X 和 Y 是线性独立的. 进一步地, 当 X 和 Y 是二元正态分布时, 二者不相关与独立等价.

对于随机成对样本  $\{(x_{1},y_{1}),(x_{2},y_{2}),\cdots,(x_{n},y_{n})\}$ ，相应的样本协方差为

$$
s _ {x y} = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) (y _ {i} - \bar {y}) = \frac {\sum_ {i = 1} ^ {n} x _ {i} y _ {i} - n \bar {x} \bar {y}}{n - 1},
$$

而样本相关系数为  $r_{xy} = \frac{s_{xy}}{s_{x}s_{y}}$ . 由第二章可知  $E(s_{xy}) = \sigma_{XY}$ ，因此样本方差度量了变量 X 和 Y 之间的线性相关程度. 而  $r_{xy}$  可看作是两个 n 维中心化向量  $(x_{1} - \bar{x}, x_{2} - \bar{x}, \cdots, x_{n} - \bar{x})^{\mathrm{T}}$  和  $(y_{1} - \bar{y}, y_{2} - \bar{y}, \cdots, y_{n} - \bar{y})^{\mathrm{T}}$  之间角度的余弦值.

例 4.1.1 表 4.1.1 为收集到的 20 位男性的身高 (cm) 和体重 (kg) 数据.

表 4.1.1 20 位男性的身高 (cm) 和体重 (kg) 数据

| 序号 | 身高(X) | 体重(Y) | 序号 | 身高(X) | 体重(Y) |
| --- | --- | --- | --- | --- | --- |
| 1 | 168 | 64 | 11 | 176 | 59 |
| 2 | 181 | 74 | 12 | 194 | 115 |
| 3 | 166 | 65 | 13 | 181 | 79 |
| 4 | 171 | 56 | 14 | 163 | 46 |
| 5 | 176 | 73 | 15 | 161 | 59 |
| 6 | 163 | 63 | 16 | 173 | 63 |
| 7 | 161 | 47 | 17 | 181 | 70 |
| 8 | 171 | 57 | 18 | 183 | 79 |
| 9 | 186 | 86 | 19 | 183 | 90 |
| 10 | 166 | 54 | 20 | 186 | 95 |

我们将两个变量“身高”(X)和“体重”(Y)各自通过散点图表示在图4.1.1中, 其中,  $\bar{X}=174.5$ ,  $s_{X}=9.633$ ,  $\bar{Y}=69.7$ ,  $s_{Y}=17.196$ , 可以看出两个变量有协同变化的趋势. 进一步地, 我们可以将两个变量通过二元散点图表示, 见图4.1.2, 可以看出其呈现出较强的线性相关性. 通过计算可得  $s_{xy}=147.684$ ,  $r_{xy}=0.892$ .

![](images/page_177_chart_6.jpg)

<details>
<summary>scatter</summary>

| 序号 | 身高(X) | 体重(Y) |
| --- | --- | --- |
| 1 | ~0.85 | ~0.35 |
| 2 | ~1.05 | ~0.45 |
| 3 | ~0.85 | ~0.35 |
| 4 | ~0.95 | ~0.25 |
| 5 | ~1.05 | ~0.45 |
| 6 | ~0.75 | ~0.35 |
| 7 | ~0.75 | ~0.15 |
| 8 | ~0.95 | ~0.25 |
| 9 | ~1.15 | ~0.45 |
| 10 | ~0.85 | ~0.25 |
| 11 | ~1.05 | ~0.35 |
| 12 | ~1.35 | ~0.65 |
| 13 | ~1.15 | ~0.45 |
| 14 | ~0.85 | ~0.15 |
| 15 | ~0.85 | ~0.35 |
| 16 | ~1.05 | ~0.45 |
| 17 | ~1.15 | ~0.45 |
| 18 | ~1.25 | ~0.65 |
| 19 | ~1.25 | ~0.75 |
| 20 | ~1.35 | ~0.85 |
</details>

图4.1.1 身高 $(X)$ 和体重 $(Y)$ 各自的散点图

![](images/page_178_chart_2.jpg)

<details>
<summary>scatter</summary>

| 身高 (X) | 体重 (Y) |
| --- | --- |
| ~161 | ~47 |
| ~162 | ~59 |
| ~163 | ~46 |
| ~164 | ~63 |
| ~166 | ~54 |
| ~167 | ~65 |
| ~168 | ~64 |
| ~171 | ~57 |
| ~171 | ~56 |
| ~173 | ~63 |
| ~176 | ~59 |
| ~176 | ~73 |
| ~180 | ~70 |
| ~180 | ~74 |
| ~180 | ~79 |
| ~183 | ~79 |
| ~183 | ~90 |
| ~186 | ~86 |
| ~186 | ~95 |
| ~194 | ~115 |
</details>

图 4.1.2 身高 (X) 和体重 (Y) 的二元散点图

描述一个 p 维多元数据需要随机向量  $X \in R^{p}$ ，它是一个分量是随机变量的向量，即  $\boldsymbol{X} = (X_{1}, X_{2}, \cdots, X_{p})^{\mathrm{T}}$ . X 的期望定义为

$$
E (\boldsymbol {X}) = \left( \begin{array}{c} E (X _ {1}) \\ E (X _ {2}) \\ \vdots \\ E (X _ {p}) \end{array} \right) = \left( \begin{array}{c} \mu_ {1} \\ \mu_ {2} \\ \vdots \\ \mu_ {p} \end{array} \right) = \boldsymbol {\mu},
$$

而其 $p \times p$ 协方差矩阵 $\Sigma$ 定义为

$$
\Sigma = \mathrm{Cov} (\boldsymbol {X}) = E \left[ (\boldsymbol {X} - \boldsymbol {\mu}) (\boldsymbol {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} \right] = \left( \begin{array}{c c c c} \sigma_ {1 1} & \sigma_ {1 2} & \dots & \sigma_ {1 p} \\ \sigma_ {2 1} & \sigma_ {2 2} & \dots & \sigma_ {2 p} \\ \vdots & \vdots & & \vdots \\ \sigma_ {p 1} & \sigma_ {p 2} & \dots & \sigma_ {p p} \end{array} \right),
$$

其中  $\sigma_{jk}$  是  $X_{j}$  和  $X_{k}$  的协方差, 而  $\sigma_{jj} = \sigma_{j}^{2}$  是  $X_{j}$  的方差. 由定义可以看出  $\Sigma$  是半正定矩阵, 其另一种计算方式是  $\Sigma = E(\boldsymbol{X}\boldsymbol{X}^{\mathrm{T}}) - \boldsymbol{\mu}\boldsymbol{\mu}^{\mathrm{T}}$ . 进一步地, 我们还可以定义总体相关矩阵

$$
P = (\rho_ {j k}) _ {p \times p} = \left( \begin{array}{c c c c} 1 & \rho_ {1 2} & \dots & \rho_ {1 p} \\ \rho_ {2 1} & 1 & \dots & \rho_ {2 p} \\ \vdots & \vdots & & \vdots \\ \rho_ {p 1} & \rho_ {p 2} & \dots & 1 \end{array} \right),
$$

其中 $\rho_{jk}=\sigma_{jk}/(\sigma_{j}\sigma_{k})$ 就是 $X_{j}$ 和 $X_{k}$ 的相关系数.

此外, 对于两个随机向量  $\boldsymbol{X} = (X_{1}, X_{2}, \cdots, X_{q})^{\mathrm{T}}$  和  $\boldsymbol{Y} = (Y_{1}, Y_{2}, \cdots, Y_{p})^{\mathrm{T}}$ ，它们的  $q \times p$  协方差矩阵为

$$
\mathrm{Cov} (\boldsymbol {X}, \boldsymbol {Y}) = E \left[ (\boldsymbol {X} - \boldsymbol {\mu_ {X}}) (\boldsymbol {Y} - \boldsymbol {\mu_ {Y}}) ^ {\mathrm{T}} \right] = E \left(\boldsymbol {X} \boldsymbol {Y} ^ {\mathrm{T}}\right) - \boldsymbol {\mu_ {X}} \boldsymbol {\mu_ {Y}} ^ {\mathrm{T}}.
$$

当 q = p 时, 我们有  $\mathrm{Cov}(\boldsymbol{X} + \boldsymbol{Y}) = \mathrm{Cov}(\boldsymbol{X}) + \mathrm{Cov}(\boldsymbol{Y}) + \mathrm{Cov}(\boldsymbol{X}, \boldsymbol{Y}) + \mathrm{Cov}(\boldsymbol{Y}, \boldsymbol{X})$ . 简单计算可知  $\mathrm{Cov}(AX, BY) = A\mathrm{Cov}(X, Y)B^{\mathrm{T}}$ .

## 4.1.2 多元数据

假设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自密度函数为  $f(\mathbf{X}) = f(x_{1}, x_{2}, \cdots, x_{p})$  的多元分布的独立同分布样本，则该数据可以表示为一个  $n \times p$  的数据矩阵 X:

$$
\underset {(n \times p)} {\mathbb {X}} = \left( \begin{array}{c c c c c} X _ {1 1} & \dots & X _ {1 j} & \dots & X _ {1 p} \\ \vdots & & \vdots & & \vdots \\ X _ {i 1} & \dots & X _ {i j} & \dots & X _ {i p} \\ \vdots & & \vdots & & \vdots \\ X _ {n 1} & \dots & X _ {n j} & \dots & X _ {n p} \end{array} \right) = \left( \begin{array}{c} \boldsymbol {X} _ {1} ^ {\mathrm{T}} \\ \vdots \\ \boldsymbol {X} _ {i} ^ {\mathrm{T}} \\ \vdots \\ \boldsymbol {X} _ {n} ^ {\mathrm{T}} \end{array} \right) \begin{array}{l} \leftarrow \text {第} 1 \text {个观测} \\ \leftarrow \text {第} i \text {个观测} \\ \leftarrow \text {第} n \text {个观测} \end{array}
$$

其中  $\boldsymbol{X}_{i}=(X_{i1},X_{i2},\cdots,X_{ip})^{\mathrm{T}}$  是 X 的第 i 行.

下面分别计算关于数据 $\mathbb{X}$ 的样本均值向量、样本协方差矩阵和样本相关矩阵. 我们有

$$
\bar {\boldsymbol {X}} = \frac {1}{n} \sum_ {i = 1} ^ {n} \boldsymbol {X} _ {i} = \left(\bar {X} _ {1}, \bar {X} _ {2}, \dots , \bar {X} _ {p}\right) ^ {\mathrm{T}} = \frac {1}{n} \mathbb {X} ^ {\mathrm{T}} \mathbf {1} _ {n},
$$

其中  $\bar{X}_{j}=\frac{1}{n}\sum_{i=1}^{n}X_{ij}$  且  $1_{n}$  为各分量全为 1 的 n 维向量. 不难看出样本均值向量  $\bar{X}$  是总体均值向量  $\mu$  的无偏估计, 而其协方差矩阵  $\mathrm{Cov}(\bar{\mathbf{X}})=\frac{1}{n}\Sigma$ .

进一步地, 数据 X 的样本协方差矩阵 S 定义为

$$
S = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} (\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}) (\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}) ^ {\mathrm{T}} = \left( \begin{array}{c c c c} s _ {1 1} & s _ {1 2} & \dots & s _ {1 p} \\ s _ {2 1} & s _ {2 2} & \dots & s _ {2 p} \\ \vdots & \vdots & & \vdots \\ s _ {p 1} & s _ {p 2} & \dots & s _ {p p} \end{array} \right),
$$

其中 $s_{jk} = \frac{1}{n - 1}\sum_{i = 1}^{n}(X_{ij} - \bar{X}_j)(X_{ik} - \bar{X}_k)$ 是第 $j$ 个和第 $k$ 个的变量的样本协方差.我们有如下计算:

$$
E (S) = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} E \left[ \left(\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}\right) \left(\boldsymbol {X} _ {i} - \bar {\boldsymbol {X}}\right) ^ {\mathrm{T}} \right]
$$

$$
\begin{array}{l} = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} E \left\{\left[ (\boldsymbol {X} _ {i} - \boldsymbol {\mu}) - (\bar {\boldsymbol {X}} - \boldsymbol {\mu}) \right] \left[ (\boldsymbol {X} _ {i} - \boldsymbol {\mu}) - (\bar {\boldsymbol {X}} - \boldsymbol {\mu}) \right] ^ {\mathrm{T}} \right\} \\ = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} E \left[ (\boldsymbol {X} _ {i} - \boldsymbol {\mu}) (\boldsymbol {X} _ {i} - \boldsymbol {\mu}) ^ {\mathrm{T}} \right] + \frac {n}{n - 1} E \left[ (\bar {\boldsymbol {X}} - \boldsymbol {\mu}) (\bar {\boldsymbol {X}} - \boldsymbol {\mu}) ^ {\mathrm{T}} \right] - \\ \frac {2}{n - 1} \sum_ {i = 1} ^ {n} E \left[ (\boldsymbol {X} _ {i} - \boldsymbol {\mu}) \left(\bar {\boldsymbol {X}} - \boldsymbol {\mu}\right) ^ {\mathrm{T}} \right] \\ = \frac {n}{n - 1} \Sigma + \frac {1}{n - 1} \Sigma - \frac {2 n}{n - 1} E \left[ (\bar {\boldsymbol {X}} - \boldsymbol {\mu}) (\bar {\boldsymbol {X}} - \boldsymbol {\mu}) ^ {\mathrm{T}} \right] \\ = \Sigma , \\ \end{array}
$$

即 $S$ 是 $\Sigma$ 的无偏估计. 我们还有如下另一种计算 $S$ 的方式:

$$
\begin{array}{l} S = \frac {1}{n - 1} \left(\sum_ {i = 1} ^ {n} \boldsymbol {X} _ {i} \boldsymbol {X} _ {i} ^ {\mathrm{T}} - n \bar {\boldsymbol {X}} \bar {\boldsymbol {X}} ^ {\mathrm{T}}\right) \\ = \frac {1}{n - 1} \left(\mathbb {X} ^ {\mathrm{T}} \mathbb {X} - n \cdot \frac {1}{n} \mathbb {X} ^ {\mathrm{T}} \mathbf {1} _ {n} \cdot \frac {1}{n} \mathbf {1} _ {n} ^ {\mathrm{T}} \mathbb {X}\right) \\ = \frac {1}{n - 1} \mathbb {X} ^ {\mathrm{T}} \left(I _ {n} - \frac {1}{n} J\right) \mathbb {X}, \\ \end{array}
$$

其中 $I_{n}$ 是 $n\times n$ 单位矩阵，$J$ 是元素均为1的 $n\times n$ 矩阵.

类似地, 数据 X 的样本相关矩阵 R 为

$$
R = (r _ {j k}) _ {p \times p} = \left( \begin{array}{c c c c} 1 & r _ {1 2} & \dots & r _ {1 p} \\ r _ {2 1} & 1 & \dots & r _ {2 p} \\ \vdots & \vdots & & \vdots \\ r _ {p 1} & r _ {p 2} & \dots & 1 \end{array} \right),
$$

其中  $r_{jk}$  是第 j 个和第 k 个变量的样本相关系数. 注意到, 我们可通过如下方式计算 R:

$$
R = D _ {s} ^ {- 1} S D _ {s} ^ {- 1} \text {和} S = D _ {s} R D _ {s},
$$

其中  $D_{s}$  是  $p \times p$  对角矩阵,

$$
D _ {s} = \mathrm{diag} (\sqrt {s _ {1 1}}, \sqrt {s _ {2 2}}, \dots , \sqrt {s _ {p p}}) = \mathrm{diag} (s _ {1}, s _ {2}, \dots , s _ {p}).
$$

注 4.1.1 对于一元数据来说, 我们可以通过样本方差来反映数据分散度. 样本协方差 S 包含了 p 个方差和  $\frac{1}{2}p(p-1)$  对协方差, 因此它从多方面刻画了数据分散程度. 那么如何用一个量来度量 p 维样本  $\{X_{1}, X_{2}, \cdots, X_{n}\}$  的整体分散度呢? 常用的量包括广义样本方差 (generalized sample variance)

$|S|$ ，即 S 的行列式，以及总样本方差 (total sample variance)  $\mathrm{tr}(S)=\sum_{j=1}^{p}s_{jj}$ 。不严格地讲，这两个值如果较大，说明  $\bar{X}$  具有较大的分散度，而特别小的  $|S|$  意味着数据的分散度小或者变量间存在较强的共线性关系 (multilinearity).

在多元数据处理中有时候我们需要将 p 维随机向量  $\boldsymbol{X} = (X_{1}, X_{2}, \cdots, X_{p})^{\mathrm{T}}$  分为两个维数分别是 q 和 p - q 的子向量, 也就是

$$
\boldsymbol {X} = \left( \begin{array}{c} X _ {1} \\ \vdots \\ X _ {q} \\ X _ {q + 1} \\ \vdots \\ X _ {p} \end{array} \right) = \binom{\boldsymbol {X} ^ {(1)}}{\boldsymbol {X} ^ {(2)}},
$$

其中  $\boldsymbol{X}^{(1)}=(X_{1},X_{2},\cdots,X_{q})^{\mathrm{T}},\boldsymbol{X}^{(2)}=(X_{q+1},X_{q+2},\cdots,X_{p})^{\mathrm{T}}.$  相应地，X 的期望可以被分解为  $\boldsymbol{\mu}=\begin{pmatrix}\boldsymbol{\mu}^{(1)}\\ \boldsymbol{\mu}^{(2)}\end{pmatrix}$ ，其中  $\boldsymbol{\mu}^{(1)}=E(\boldsymbol{X}^{(1)})=(\mu_{1},\mu_{2},\cdots,\mu_{q})^{\mathrm{T}},\boldsymbol{\mu}^{(2)}=E(\boldsymbol{X}^{(2)})=(\mu_{q+1},\mu_{q+2},\cdots,\mu_{p})^{\mathrm{T}}$ ，而 X 的协方差矩阵则可以拆分为

$$
\Sigma = \left( \begin{array}{c c} (\Sigma_ {1 1}) _ {q \times q} & (\Sigma_ {1 2}) _ {q \times (p - q)} \\ (\Sigma_ {2 1}) _ {(p - q) \times q} & (\Sigma_ {2 2}) _ {(p - q) \times (p - q)} \end{array} \right) _ {p \times p},
$$

其中  $\Sigma_{11}$  是  $\boldsymbol{X}^{(1)}$  的协方差矩阵,  $\Sigma_{22}$  是  $\boldsymbol{X}^{(2)}$  的协方差矩阵,  $\Sigma_{12} = \Sigma_{21}^{T}$  则包含了  $\boldsymbol{X}^{(1)}$  和  $\boldsymbol{X}^{(2)}$  的所有元变量之间的协方差, 即  $\mathrm{Cov}(\boldsymbol{X}^{(1)}, \boldsymbol{X}^{(2)})$ . 可以看出, 如果  $\boldsymbol{X}^{(1)}$  和  $\boldsymbol{X}^{(2)}$  独立, 则  $\Sigma_{12} = \Sigma_{21}^{T} = \mathbf{0}_{q \times (p-q)}$ . S, P 和 R 都可以按照此方式进行分解.

最后我们对  $X_{1}, X_{2}, \cdots, X_{p}$  的线性组合的基本性质给予讨论.

命题 4.1.1 令  $Z=a^{T}X=\sum_{j=1}^{p}a_{j}X_{j}$  和  $W=b^{T}X=\sum_{j=1}^{p}b_{j}X_{j}$  是  $X_{1}, X_{2}, \cdots, X_{p}$  的两个线性组合，其中  $\boldsymbol{a}=(a_{1}, a_{2}, \cdots, a_{p})^{\mathrm{T}}$  和  $\boldsymbol{b}=(b_{1}, b_{2}, \cdots, b_{p})^{\mathrm{T}}$  是系数向量.则我们有

(1) 随机变量 Z 的期望和方差为

$$
E (Z) = E (\boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {X}) = \boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {\mu}, \quad \operatorname{Var} (Z) = \operatorname{Var} (\boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {X}) = \boldsymbol {a} ^ {\mathrm{T}} \Sigma \boldsymbol {a}.
$$

(2) $Z$ 和 $W$ 的协方差和相关性可表示为

$$
\sigma_ {Z W} = \operatorname{Cov} (Z, W) = \boldsymbol {a} ^ {\mathrm{T}} \Sigma \boldsymbol {b},
$$

$$
\rho_ {Z W} = \mathrm{Corr} (Z, W) = \frac {\boldsymbol {a} ^ {\mathrm{T}} \Sigma \boldsymbol {b}}{\sqrt {(\boldsymbol {a} ^ {\mathrm{T}} \Sigma \boldsymbol {a}) (\boldsymbol {b} ^ {\mathrm{T}} \Sigma \boldsymbol {b})}}.
$$

证明 下面仅就命题的部分结论给出证明.

$$
\begin{array}{l} \mathrm{Var} (Z) = E \left[ \left(\boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {X} - \boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {\mu}\right) \left(\boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {X} - \boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {\mu}\right) ^ {\mathrm{T}} \right] \\ = E \left[ \boldsymbol {a} ^ {\mathrm{T}} (\boldsymbol {X} - \boldsymbol {\mu}) (\boldsymbol {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} \boldsymbol {a} \right] \\ = \boldsymbol {a} ^ {\mathrm{T}} E \left[ (\boldsymbol {X} - \boldsymbol {\mu}) (\boldsymbol {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} \right] \boldsymbol {a} \\ = \boldsymbol {a} ^ {\mathrm{T}} \Sigma \boldsymbol {a}, \\ \end{array}
$$

而

$$
\begin{array}{l} \operatorname{Cov} (Z, W) = E \left[ \left(\boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {X} - \boldsymbol {a} ^ {\mathrm{T}} \boldsymbol {\mu}\right) \left(\boldsymbol {b} ^ {\mathrm{T}} \boldsymbol {X} - \boldsymbol {b} ^ {\mathrm{T}} \boldsymbol {\mu}\right) \right] \\ = \boldsymbol {a} ^ {\mathrm{T}} E \left[ (\boldsymbol {X} - \boldsymbol {\mu}) (\boldsymbol {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} \right] \boldsymbol {b} \\ = \boldsymbol {a} ^ {\mathrm{T}} \Sigma \boldsymbol {b}. \\ \end{array}
$$

更一般地, 令 $Y = A X + b$, 其中 $A = (a_{ij})_{q \times p}$, $b$ 是一个 $q$ 维向量. 则类似计算可得

$$
\boldsymbol {\mu} _ {\boldsymbol {Y}} = E (A \boldsymbol {X} + \boldsymbol {b}) = A \boldsymbol {\mu} + \boldsymbol {b}, \Sigma_ {\boldsymbol {Y}} = \mathrm{Cov} (\boldsymbol {Y}) = A \Sigma A ^ {\mathrm{T}}.
$$

## 4.1.3 多元正态分布

回顾第二、三章中所介绍的很多统计推断方法都是基于一元正态分布的, 其主要原因之一是它具有良好的性质. 因此, 对于多元统计推断而言, 多元正态分布同样扮演着重要作用. 多元正态分布具有的优良性质包括:

(1) 分布完全由其期望向量和协方差矩阵所决定;
(2) 变量不相关与独立等价;
(3) 对于服从多元正态分布的随机向量 $X$，其线性组合 $AX + b$ 也服从多元正态分布；
(4) 即便数据不服从多元正态分布, 由多元中心极限定理可知一些常用的统计量仍然服从正态分布.

在本小节中, 我们对多元正态分布的性质给予详细讨论. 假设 p 维随机向量  $\boldsymbol{X} = (X_{1}, X_{2}, \cdots, X_{p})^{\mathrm{T}}$  服从均值为  $\mu$ 、协方差为  $\Sigma$  的多元正态分布 (其中  $\mu$  为 p 维常数向量,  $\Sigma$  为正定矩阵), 记为  $\boldsymbol{X} \sim N_{p}(\boldsymbol{\mu}, \Sigma)$ , 其密度函数为

$$
f (\boldsymbol {X}) = \frac {1}{(2 \pi) ^ {p / 2} | \Sigma | ^ {1 / 2}} \exp \left\{- \frac {(\boldsymbol {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} \Sigma^ {- 1} (\boldsymbol {X} - \boldsymbol {\mu})}{2} \right\}.
$$

$X$ 的特征函数为

$$
\varPhi_ {\boldsymbol {X}} (\boldsymbol {t}) = \exp \left\{\mathrm{i} \boldsymbol {t} ^ {\mathrm{T}} \boldsymbol {\mu} - \frac {1}{2} \boldsymbol {t} ^ {\mathrm{T}} \Sigma \boldsymbol {t} \right\}.
$$

可见, 多元正态分布完全由  $\mu$  和  $\Sigma$  所决定.

例 4.1.2 (二元正态分布) 当 p=2 时,  $\mu$  和  $\Sigma$  表示为

$$
\boldsymbol {\mu} = \binom{\mu_ {1}}{\mu_ {2}}, \Sigma = \left( \begin{array}{c c} \sigma_ {1} ^ {2} & \rho \sigma_ {1} \sigma_ {2} \\ \rho \sigma_ {1} \sigma_ {2} & \sigma_ {2} ^ {2} \end{array} \right).
$$

随机向量  $\boldsymbol{Y} = (Y_{1}, Y_{2})^{\mathrm{T}}$  服从二元正态分布，即  $\boldsymbol{Y} \sim BN(\mu_{1}, \mu_{2}, \sigma_{1}^{2}, \sigma_{2}^{2}, \rho)$ ，其密度函数为

$$
\begin{array}{l} f (y _ {1}, y _ {2}) = \frac {1}{2 \pi \sigma_ {1} \sigma_ {2} \sqrt {1 - \rho^ {2}}}. \\ \exp \left\{- \frac {\left(\frac {y _ {1} - \mu_ {1}}{\sigma_ {1}}\right) ^ {2} + \left(\frac {y _ {2} - \mu_ {2}}{\sigma_ {2}}\right) ^ {2} - 2 \rho \left(\frac {y _ {1} - \mu_ {1}}{\sigma_ {1}}\right) \left(\frac {y _ {2} - \mu_ {2}}{\sigma_ {2}}\right)}{2 (1 - \rho^ {2})} \right\}. \\ \end{array}
$$

如图 4.1.3 所示.

![](images/page_183_chart_10.jpg)

<details>
<summary>surface_3d</summary>

| y1 | y2 | Value |
| --- | --- | --- |
| 0~100 | 0~100 | 0~0.0012 |
</details>

图4.1.3 二元正态分布的密度函数图

下面给出  $\boldsymbol{X} \sim N_{p}(\boldsymbol{\mu}, \Sigma)$  的几个重要性质.

性质 4.1.1 (线性组合) (1) 假设  $\boldsymbol{X} \sim N_{p}(\boldsymbol{\mu}, \Sigma)$  且  $\boldsymbol{a} = (a_{1}, a_{2}, \cdots, a_{p})^{\mathrm{T}}$  是一常数向量，则  $\boldsymbol{a}^{\mathrm{T}}\boldsymbol{X} \sim N(\boldsymbol{a}^{\mathrm{T}}\boldsymbol{\mu}, \boldsymbol{a}^{\mathrm{T}}\Sigma\boldsymbol{a})$ . 反之，如果  $\boldsymbol{a}^{\mathrm{T}}\boldsymbol{X} \sim N(\boldsymbol{a}^{\mathrm{T}}\boldsymbol{\mu}, \boldsymbol{a}^{\mathrm{T}}\Sigma\boldsymbol{a}), \forall\boldsymbol{a}$ ，则  $\boldsymbol{X} \sim N_{p}(\boldsymbol{\mu}, \Sigma)$ .

(2) 假设  $\boldsymbol{X} \sim N_{p}(\boldsymbol{\mu}, \Sigma)$  且  $A \in R^{q \times p}$ ，其秩为  $q (\leqslant p)$ ，则对于  $b \in R^{q}$

$$
A \boldsymbol {X} + \boldsymbol {b} \sim N _ {q} (A \boldsymbol {\mu} + \boldsymbol {b}, A \Sigma A ^ {\mathrm{T}}).
$$

证明 (1) 可由多元正态分布的特征函数性质证明 (留作习题).

(2) 对任意的  $b \in R^{q}$ ，令  $b^{T}AX \stackrel{记为}{=} a^{T}X$ 。根据 (1)， $b^{T}AX$  是正态分布的。由此再根据 (1)，AX 也服从多元正态分布。

例 4.1.3 特别地, 考虑  $\boldsymbol{a}=(1,0,0,\cdots,0)^{\mathrm{T}}$ , 则我们可知  $X_{1}\sim N(\mu_{1},\sigma_{11})$ .

性质 4.1.2 (子向量的正态性) 假设 X,  $\mu$  及  $\Sigma$  从第 r 个分量进行分块:

$$
\boldsymbol {X} = \left( \begin{array}{c} \boldsymbol {X} _ {1} \\ \boldsymbol {X} _ {2} \end{array} \right) \begin{array}{l} \} r \\ \} p - r \end{array} , \boldsymbol {\mu} = \binom{\boldsymbol {\mu} _ {1}}{\boldsymbol {\mu} _ {2}}, \Sigma = \left( \begin{array}{c c} \Sigma_ {1 1} & \Sigma_ {1 2} \\ \Sigma_ {2 1} & \Sigma_ {2 2} \end{array} \right),
$$

其中 $X_{1}$ 和 $\mu_{1}$ 为 $r$ 维向量，$\Sigma_{11}$ 为 $r \times r$ 矩阵. 则有

$$
\boldsymbol {X} _ {1} \sim N _ {r} (\boldsymbol {\mu} _ {1}, \Sigma_ {1 1}), \quad \boldsymbol {X} _ {2} \sim N _ {p - r} (\boldsymbol {\mu} _ {2}, \Sigma_ {2 2}).
$$

证明 由性质4.1.1(2)，令 $A_{(r\times p)} = (I_r\mathbf{0}_{(r\times r)(r\times (p - r))})$ 可得.

特别地, $\boldsymbol{X}=(X_{1},X_{2},\cdots,X_{p})^{\mathrm{T}}$ 的第j个分量服从一元正态分布: $X_{j}\sim N(\mu_{j},\sigma_{jj})$, $j=1,2,\cdots,p$. 一般情况下, $\boldsymbol{X}$ 的任意子向量均服从正态分布.

性质 4.1.3 (子向量的独立性) 同性质 4.1.2, 考虑将 X,  $\mu$  及  $\Sigma$  的分量进行分块.

(1) 当且仅当  $\Sigma_{12}=0$  时,  $X_{1}$  与  $X_{2}$  相互独立.
(2) 当且仅当  $\sigma_{jk}=0$  时,  $X_{j}$  和  $X_{k}$  相互独立.
(3) 如果  $Y \sim N_{q}(\mu_{1}, \Sigma_{11})$ ,  $X \sim N_{p}(\mu_{2}, \Sigma_{22})$ , 并且 Y 与 X 相互独立, 则

$$
\binom{\boldsymbol {Y}}{\boldsymbol {X}} \sim N _ {p + q} \left(\binom{\boldsymbol {\mu} _ {1}}{\boldsymbol {\mu} _ {2}}, \left( \begin{array}{c c} \Sigma_ {1 1} & \boldsymbol {0} \\ \boldsymbol {0} & \Sigma_ {2 2} \end{array} \right)\right).
$$

注:对于非正态变量，(1)，(2) 不成立.

证明 (1) 利用密度函数性质, 即, 当 $X_{1}$ 和 $X_{2}$ 独立时, $f(\boldsymbol{x}) = f(\boldsymbol{x}_{1}, \boldsymbol{x}_{2}) = f(\boldsymbol{x}_{1})f(\boldsymbol{x}_{2})$, 故由

$$
\begin{array}{l} \frac {1}{(2 \pi) ^ {p / 2} | \Sigma | ^ {1 / 2}} \exp \left\{- \frac {(\boldsymbol {x} - \boldsymbol {\mu}) ^ {\mathrm{T}} \Sigma^ {- 1} (\boldsymbol {x} - \boldsymbol {\mu})}{2} \right\} \\ = \frac {1}{(2 \pi) ^ {p / 2} | \Sigma_ {1 1} | ^ {1 / 2} | \Sigma_ {2 2} | ^ {1 / 2}}. \\ \exp \left\{- \frac {(\boldsymbol {x} _ {1} - \boldsymbol {\mu}) ^ {\mathrm{T}} \Sigma_ {1 1} ^ {- 1} (\boldsymbol {x} _ {1} - \boldsymbol {\mu}) + (\boldsymbol {x} _ {2} - \boldsymbol {\mu}) ^ {\mathrm{T}} \Sigma_ {2 2} ^ {- 1} (\boldsymbol {x} _ {2} - \boldsymbol {\mu})}{2} \right\} \\ \end{array}
$$

可知  $\Sigma_{12}=0$ .

(2), (3) 利用以上性质同样得证 (留作习题).

例 4.1.4 将 X,  $\mu$  及  $\Sigma$  同上做分块定义. 令 B 为  $r \times (p - r)$  常数矩阵, 现考虑对于子向量做线性变换,

$$
\boldsymbol {Y} = \binom{\boldsymbol {Y} _ {1}}{\boldsymbol {Y} _ {2}} = \binom{\boldsymbol {X} _ {1} + B \boldsymbol {X} _ {2}}{\boldsymbol {X} _ {2}}.
$$

(1) Y 服从什么分布?
(2) 如果 $|\Sigma_{22}| > 0$, 找到一个矩阵 $B$ 使得 $\operatorname{Cov}(\mathbf{Y}_1, \mathbf{Y}_2) = 0$.

解 (1) 定义一个 $p \times p$ 矩阵 $A = \begin{pmatrix} I_r & B \\ \mathbf{0} & I_{p-r} \end{pmatrix}$, 则有 $\mathbf{Y} = A\mathbf{X} \sim N_p(A\boldsymbol{\mu}, A\Sigma A^{\mathrm{T}})$, 其中

$$
A \boldsymbol {\mu} = \binom{\boldsymbol {\mu} _ {1} + B \boldsymbol {\mu} _ {2}}{\boldsymbol {\mu} _ {2}},
$$

$$
A \Sigma A ^ {\mathrm{T}} = \left( \begin{array}{c c} \Sigma_ {1 1} + B \Sigma_ {1 2} + \Sigma_ {2 1} B ^ {\mathrm{T}} + B \Sigma_ {2 2} B ^ {\mathrm{T}} & \Sigma_ {1 2} + B \Sigma_ {2 2} \\ \Sigma_ {2 1} + \Sigma_ {2 2} B ^ {\mathrm{T}} & \Sigma_ {2 2} \end{array} \right).
$$

(2) 若 $\operatorname{Cov}(\mathbf{Y}_1, \mathbf{Y}_2) = 0$, 则有 $\Sigma_{12} + B\Sigma_{22} = 0$, 即 $B = -\Sigma_{22}^{-1}\Sigma_{12}$.

性质 4.1.4 (子向量的条件正态性) 再次考虑 X,  $\mu$  及  $\Sigma$  的分块情况. 假设  $|\Sigma_{22}| > 0$ . 则在给定  $X_{2}$  的条件下,  $X_{1}$  的条件分布为多元正态分布:

$$
(\boldsymbol {X} _ {1} | \boldsymbol {X} _ {2}) \sim N _ {r} (\boldsymbol {\mu} _ {1} + \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} (\boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2}), \Sigma_ {1 1} - \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} \Sigma_ {2 1}).
$$

证明 1 (直接方法) 已知条件密度函数的定义为

$$
f _ {\boldsymbol {X} _ {1} | \boldsymbol {X} _ {2}} (\boldsymbol {x} _ {1} | \boldsymbol {x} _ {2}) = \frac {f (\boldsymbol {x} _ {1} , \boldsymbol {x} _ {2})}{f _ {\boldsymbol {X} _ {2}} (\boldsymbol {x} _ {2})} = \frac {\frac {1}{(2 \pi) ^ {p / 2} | \Sigma | ^ {1 / 2}} \exp \left\{- \frac {(\boldsymbol {x} - \boldsymbol {\mu}) ^ {\mathrm{T}} \Sigma^ {- 1} (\boldsymbol {x} - \boldsymbol {\mu})}{2} \right\}}{\frac {1}{(2 \pi) ^ {(p - r) / 2} | \Sigma_ {2 2} | ^ {1 / 2}} \exp \left\{- \frac {(\boldsymbol {x} _ {2} - \boldsymbol {\mu} _ {2}) ^ {\mathrm{T}} \Sigma_ {2 2} ^ {- 1} (\boldsymbol {x} _ {2} - \boldsymbol {\mu} _ {2})}{2} \right\}}. \tag {4.1.1}
$$

注意到  $\Sigma^{-1}$  可有如下分块表达. 我们考虑矩阵

$$
A = \left( \begin{array}{c c} I _ {r} & - \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} \\ \mathbf {0} _ {(p - r) \times r} & I _ {p - r} \end{array} \right).
$$

于是, 我们有

$$
\begin{array}{l} A \Sigma A ^ {\mathrm{T}} = \left( \begin{array}{c c} I _ {r} & - \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} \\ \mathbf {0} _ {(p - r) \times r} & I _ {p - r} \end{array} \right) \left( \begin{array}{c c} \Sigma_ {1 1} & \Sigma_ {1 2} \\ \Sigma_ {2 1} & \Sigma_ {2 2} \end{array} \right) \left( \begin{array}{c c} I _ {r} & \mathbf {0} _ {r \times (p - r)} \\ - \Sigma_ {2 2} ^ {- 1} \Sigma_ {2 1} & I _ {p - r} \end{array} \right) \\ = \left( \begin{array}{c c} {\Sigma_ {1 1} - \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} \Sigma_ {2 1}} & {\mathbf {0} _ {r \times (p - r)}} \\ {\mathbf {0} _ {(p - r) \times r}} & {\Sigma_ {2 2}} \end{array} \right) \stackrel {{\text {记为}}} {{=}} D. \\ \end{array}
$$

因此, 得到  $\Sigma^{-1}$  如下:

$$
\Sigma^ {- 1} = [ A ^ {- 1} D (A ^ {\mathrm{T}}) ^ {- 1} ] ^ {- 1} = A ^ {\mathrm{T}} D ^ {- 1} A
$$

$$
= \left( \begin{array}{c c} \Sigma_ {1 1 \cdot 2} ^ {- 1} & - \Sigma_ {1 1 \cdot 2} ^ {- 1} \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} \\ - \Sigma_ {2 2} ^ {- 1} \Sigma_ {2 1} \Sigma_ {1 1 \cdot 2} ^ {- 1} & \Sigma_ {2 2} ^ {- 1} + \Sigma_ {2 2} ^ {- 1} \Sigma_ {2 1} \Sigma_ {1 1 \cdot 2} ^ {- 1} \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} \end{array} \right),
$$

其中 $\Sigma_{11\cdot 2} = \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ .同理可得，

$$
\Sigma^ {- 1} = \left( \begin{array}{c c} \Sigma_ {1 1} ^ {- 1} + \Sigma_ {1 1} ^ {- 1} \Sigma_ {1 2} \Sigma_ {2 2 \cdot 1} ^ {- 1} \Sigma_ {2 1} \Sigma_ {1 1} ^ {- 1} & - \Sigma_ {1 1} ^ {- 1} \Sigma_ {1 2} \Sigma_ {2 2 \cdot 1} ^ {- 1} \\ - \Sigma_ {2 2 \cdot 1} ^ {- 1} \Sigma_ {2 1} \Sigma_ {1 1} ^ {- 1} & \Sigma_ {2 2 \cdot 1} ^ {- 1} \end{array} \right),
$$

其中 $\Sigma_{22\cdot 1} = \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12}$ .由此可得，

$$
\Sigma_ {1 1 \cdot 2} ^ {- 1} = \Sigma_ {1 1} ^ {- 1} + \Sigma_ {1 1} ^ {- 1} \Sigma_ {1 2} \Sigma_ {2 2 \cdot 1} ^ {- 1} \Sigma_ {2 1} \Sigma_ {1 1} ^ {- 1},
$$

$$
\Sigma_ {2 2 \cdot 1} ^ {- 1} = \Sigma_ {2 2} ^ {- 1} + \Sigma_ {2 2} ^ {- 1} \Sigma_ {2 1} \Sigma_ {1 1 \cdot 2} ^ {- 1} \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1},
$$

$$
\Sigma_ {1 1 \cdot 2} ^ {- 1} \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} = \Sigma_ {1 1} ^ {- 1} \Sigma_ {1 2} \Sigma_ {2 2 \cdot 1} ^ {- 1},
$$

$$
| \Sigma | = | \Sigma_ {1 1 \cdot 2} | | \Sigma_ {2 2} | = | \Sigma_ {1 1} | | \Sigma_ {2 2 \cdot 1} |.
$$

将上述所有结果代入 (4.1.1), 可得,

$$
\begin{array}{l} (\boldsymbol {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} \Sigma^ {- 1} (\boldsymbol {X} - \boldsymbol {\mu}) - (\boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2}) ^ {\mathrm{T}} \Sigma_ {2 2} ^ {- 1} (\boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2}), \\ = (\boldsymbol {X} _ {1} - \boldsymbol {\mu} _ {1}) ^ {\mathrm{T}} \Sigma_ {1 1 \cdot 2} ^ {- 1} (\boldsymbol {X} _ {1} - \boldsymbol {\mu} _ {1}) - 2 (\boldsymbol {X} _ {1} - \boldsymbol {\mu} _ {1}) ^ {\mathrm{T}} \Sigma_ {1 1 \cdot 2} ^ {- 1} \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} (\boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2}) + \\ (\boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2}) ^ {\mathrm{T}} \Sigma_ {2 2} ^ {- 1} \Sigma_ {2 1} \Sigma_ {1 1 \cdot 2} ^ {- 1} \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} (\boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2}) \\ = \left[ \boldsymbol {X} _ {1} - \boldsymbol {\mu} _ {1} - \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} \left(\boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2}\right) \right] ^ {\mathrm{T}} \Sigma_ {1 1 \cdot 2} ^ {- 1} \left[ \boldsymbol {X} _ {1} - \boldsymbol {\mu} _ {1} - \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} \left(\boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2}\right) \right] \\ \stackrel {\text {记为}} {=} \left(\boldsymbol {X} _ {1} - \boldsymbol {\mu} _ {1. 2}\right) ^ {\mathrm{T}} \Sigma_ {1 1. 2} ^ {- 1} \left(\boldsymbol {X} _ {1} - \boldsymbol {\mu} _ {1. 2}\right), \\ \end{array}
$$

其中  $\boldsymbol{\mu}_{1,2}=\boldsymbol{\mu}_{1}+\Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol{X}_{2}-\boldsymbol{\mu}_{2})$ . 同时,

$$
f _ {\boldsymbol {X} _ {1} | \boldsymbol {X} _ {2}} (\boldsymbol {x} _ {1} | \boldsymbol {x} _ {2}) = \frac {1}{(2 \pi) ^ {r / 2} | \Sigma_ {1 1 \cdot 2} | ^ {1 / 2}} \exp \left\{- \frac {(\boldsymbol {x} _ {1} - \boldsymbol {\mu} _ {1 \cdot 2}) ^ {\mathrm{T}} \Sigma_ {1 1 \cdot 2} ^ {- 1} (\boldsymbol {x} _ {1} - \boldsymbol {\mu} _ {1 \cdot 2})}{2} \right\},
$$

也就是 $(\pmb{X}_1|\pmb{X}_2) \sim N_r(\pmb{\mu}_{1\cdot 2}, \Sigma_{11\cdot 2})$。同理，我们可得 $(\pmb{X}_2|\pmb{X}_1) \sim N_r(\pmb{\mu}_{2\cdot 1}, \Sigma_{22\cdot 1})$，其中 $\pmb{\mu}_{2\cdot 1} = \pmb{\mu}_2 + \Sigma_{21}\Sigma_{11}^{-1}(\pmb{X}_1 - \pmb{\mu}_1)$。$\square$

证明 2 （间接方法）由例 4.1.4, 考虑 AX,

$$
A (\boldsymbol {X} - \boldsymbol {\mu}) = \binom{\boldsymbol {X} _ {1} - \boldsymbol {\mu} _ {1} - \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} (\boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2})}{\boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2}},
$$

$$
\mathrm{Cov} (\boldsymbol {X} _ {1} - \boldsymbol {\mu} _ {1} - \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} (\boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2}), \boldsymbol {X} _ {2} - \boldsymbol {\mu} _ {2}) = D _ {1 2} = \mathbf {0} _ {(p - r) \times r}.
$$

由于 $\operatorname{Cov}[A(\boldsymbol{X}-\boldsymbol{\mu})] = A\Sigma A^{\mathrm{T}} = D$。因此，$\boldsymbol{X}_1 - \boldsymbol{\mu}_1 - \Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol{X}_2 - \boldsymbol{\mu}_2)$ 和 $\boldsymbol{X}_2 - \boldsymbol{\mu}_2$ 是独立的。并且，$\boldsymbol{X}_1 - \boldsymbol{\mu}_1 - \Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol{X}_2 - \boldsymbol{\mu}_2)$ 服从分布 $N_r(\mathbf{0}, \Sigma_{11.2})$。已知 $\boldsymbol{X}_2 = \boldsymbol{x}_2$，则 $\boldsymbol{\mu}_1 + \Sigma_{12}\Sigma_{22}^{-1}(\boldsymbol{x}_2 - \boldsymbol{\mu}_2)$ 为常数。因此，在 $\boldsymbol{X}_2 = \boldsymbol{x}_2$ 条件下，$\boldsymbol{X}_1$ 服从分布 $N_r(\boldsymbol{\mu}_{1.2}, \Sigma_{11.2})$。

□

由该性质可知, $E(\boldsymbol{X}_1|\boldsymbol{X}_2)$ 为 $\boldsymbol{X}_2$ 的线性函数向量, 而 $\mathrm{Cov}(\boldsymbol{X}_1|\boldsymbol{X}_2)$ 不依赖于 $\boldsymbol{X}_2$. 此外, 当我们由 $\boldsymbol{X}_2$ 对 $\boldsymbol{X}_1$ 做线性回归时 (参见第五章), $\Sigma_{12}\Sigma_{22}^{-1}$ 被称为回归系数矩阵, 即

$$
\mu_ {1} + \beta_ {1, r + 1} (y _ {r + 1} - \mu_ {r + 1}) + \dots + \beta_ {1, p} (y _ {p} - \mu_ {p}),
$$

•
•
•

$$
\mu_ {r} + \beta_ {r, r + 1} (y _ {r + 1} - \mu_ {r + 1}) + \dots + \beta_ {r, p} (y _ {p} - \mu_ {p}),
$$

其中  $\beta$  可以如下给出定义:

$$
\Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} = \left( \begin{array}{c c c c} \beta_ {1, r + 1} & \beta_ {1, r + 2} & \dots & \beta_ {1, p} \\ \beta_ {2, r + 1} & \beta_ {2, r + 2} & \dots & \beta_ {2, p} \\ \vdots & \vdots & & \vdots \\ \beta_ {r, r + 1} & \beta_ {r, r + 2} & \dots & \beta_ {r, p} \end{array} \right).
$$

此外, 该性质还启示我们, 为检查 X 的正态性, 可以利用 X 所有配对的二元散点图探查其中的线性或非线性趋势.

这里的  $\Sigma_{11.2}$  通常被称为  $X_{1}$  的偏协方差矩阵 (partial covariance matrix)，这里所谓“偏”意指在排除了其余部分 (即  $X_{2}$ ) 情形下的净协方差，也就是在  $X_{2}$  取给定值的情形下的条件协方差。我们有如下定义。

定义 4.1.1 令  $\Sigma_{11\cdot2} = \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ ,

(1)  $\sigma_{jk\cdot r+1,\cdots,p}:\Sigma_{11\cdot2}$  的第 j,k 个元素, 称为偏协方差;
(2)  $\sigma_{jj\cdot r+1,\cdots,p}$ :  $\Sigma_{11\cdot2}$  的第 j,j 个元素, 称为偏方差;
(3) 在给定  $\boldsymbol{X}_{2} = (X_{r+1}, X_{r+2}, \cdots, X_{p})^{\mathrm{T}}$  的条件下,  $X_{j}$  与  $X_{k}$  的偏相关系数 (partial correlation coefficient) 为

$$
\rho_ {j k \cdot r + 1, \dots , p} = \frac {\sigma_ {j k \cdot r + 1 , \cdots , p}}{\left(\sigma_ {j j \cdot r + 1 , \cdots , p} \sigma_ {j j \cdot r + 1 , \cdots , p}\right) ^ {1 / 2}}, j, k = 1, 2, \dots , r.
$$

矩阵  $\Sigma^{-1}$ ,  $\Sigma_{11.2}$  在 Gauss 图模型、因果推断等领域都发挥着重要作用, 在这里我们不再展开, 有兴趣的读者可参见 Edwards(2000).

性质 4.1.5 (两个多元正态向量和) 考虑 p 维随机向量  $X \sim N_{p}(\mu_{X}, \Sigma_{X})$  和  $Y \sim N_{p}(\mu_{Y}, \Sigma_{Y})$ ，且二者相互独立，则  $X \pm Y \sim N_{p}(\mu_{X} \pm \mu_{Y}, \Sigma_{X} + \Sigma_{Y})$ .

证明 由性质 4.1.3 (3) 可得, $(\boldsymbol{X}^{\mathrm{T}},\boldsymbol{Y}^{\mathrm{T}})^{\mathrm{T}}$ 的联合分布为

$$
\binom{\boldsymbol {X}}{\boldsymbol {Y}} \sim N _ {2 p} \left(\binom{\boldsymbol {\mu_ {X}}}{\boldsymbol {\mu_ {Y}}}, \left( \begin{array}{c c} \Sigma_ {\boldsymbol {X}} & \boldsymbol {0} _ {p \times p} \\ \boldsymbol {0} _ {p \times p} & \Sigma_ {\boldsymbol {Y}} \end{array} \right)\right).
$$

因此, 结论可由  $\boldsymbol{X} + \boldsymbol{Y} = (I_{p}, I_{p})_{p \times 2p} \begin{pmatrix} \boldsymbol{X} \\ \boldsymbol{Y} \end{pmatrix}$  得到.

该性质也可以容易地推广到 $a\pmb {X}\pm b\pmb{Y}$ 或 $\sum_{j = 1}^{m}a_{j}\pmb{X}_{j}$ 所服从的分布.

性质 4.1.6 随机向量  $X_{1}, X_{2}, \cdots, X_{m}$  来自分布  $N_{p}(\boldsymbol{\mu}_{j}, \Sigma)$  且相互独立， $a_{1}, a_{2}, \cdots, a_{m}$  与  $b_{1}, b_{2}, \cdots, b_{m}$  为两组常数。定义

$$
\boldsymbol {Z} _ {1} = a _ {1} \boldsymbol {X} _ {1} + a _ {2} \boldsymbol {X} _ {2} + \dots + a _ {m} \boldsymbol {X} _ {m},
$$

$$
\boldsymbol {Z} _ {2} = b _ {1} \boldsymbol {X} _ {1} + b _ {2} \boldsymbol {X} _ {2} + \dots + b _ {m} \boldsymbol {X} _ {m},
$$

则有

(1) $Z_{1}\sim N_{p}\left(\sum_{i=1}^{m}a_{i}\mu_{i},\sum_{i=1}^{m}a_{i}^{2}\Sigma\right)$ 并且 $Z_{2}\sim N_{p}\left(\sum_{i=1}^{m}b_{i}\mu_{i},\sum_{i=1}^{m}b_{i}^{2}\Sigma\right)$.
(2) 当且仅当  $a^{T}b=\sum_{i=1}^{m}a_{i}b_{i}=0$  时,  $Z_{1}$  与  $Z_{2}$  相互独立.

证明 再次利用性质 4.1.3 (3),  $(\boldsymbol{X}_{1}^{\mathrm{T}}, \boldsymbol{X}_{2}^{\mathrm{T}}, \cdots, \boldsymbol{X}_{m}^{\mathrm{T}})^{\mathrm{T}}$  的联合分布函数为

$$
\left( \begin{array}{c} \boldsymbol {X} _ {1} \\ \boldsymbol {X} _ {2} \\ \vdots \\ \boldsymbol {X} _ {m} \end{array} \right) _ {m p \times 1} \sim N _ {m p} \left(\left( \begin{array}{c} \boldsymbol {\mu} _ {1} \\ \boldsymbol {\mu} _ {2} \\ \vdots \\ \boldsymbol {\mu} _ {m} \end{array} \right) _ {m p \times 1}, \left( \begin{array}{c c c c} \Sigma & \mathbf {0} & \dots & \mathbf {0} \\ \mathbf {0} & \Sigma & \dots & \mathbf {0} \\ \vdots & \vdots & & \vdots \\ \mathbf {0} & \mathbf {0} & \dots & \Sigma \end{array} \right) _ {m p \times m p}\right),
$$

因此, 我们有

$$
\left( \begin{array}{c} \boldsymbol {Z} _ {1} \\ \boldsymbol {Z} _ {2} \end{array} \right) _ {2 p \times 1} = \left( \begin{array}{c c c c} a _ {1} I _ {p} & a _ {2} I _ {p} & \dots & a _ {m} I _ {p} \\ b _ {1} I _ {p} & b _ {2} I _ {p} & \dots & b _ {m} I _ {p} \end{array} \right) _ {2 p \times m p} \left( \begin{array}{c} \boldsymbol {X} _ {1} \\ \boldsymbol {X} _ {2} \\ \vdots \\ \boldsymbol {X} _ {m} \end{array} \right).
$$

即

- $\boldsymbol{\mu}_{\boldsymbol{Z}_1} = (a_1 I_p, a_2 I_p, \cdots, a_m I_p)\left( \begin{array}{c}\boldsymbol{\mu}_1\\ \boldsymbol{\mu}_2\\ \vdots \\ \boldsymbol{\mu}_m \end{array} \right) = \sum_{i=1}^{m} a_i \boldsymbol{\mu}_i,$
- $\Sigma_{\mathbf{Z}_1} = (a_1I_p, a_2I_p, \cdots, a_mI_p)\left( \begin{array}{cccc}\Sigma & \mathbf{0} & \cdots & \mathbf{0}\\ \mathbf{0} & \Sigma & \cdots & \mathbf{0}\\ \vdots & \vdots & & \vdots \\ \mathbf{0} & \mathbf{0} & \cdots & \Sigma \end{array} \right)\left( \begin{array}{c}a_1I_p\\ a_2I_p\\ \vdots \\ a_mI_p \end{array} \right) = \sum_{i = 1}^m a_i^2\Sigma ,$

$$
\begin{array}{l} \text {Cov} (\mathbf {Z} _ {1}, \mathbf {Z} _ {2}) = (a _ {1} I _ {p}, a _ {2} I _ {p}, \dots , a _ {m} I _ {p}) \left( \begin{array}{c c c c} \Sigma & \mathbf {0} & \dots & \mathbf {0} \\ \mathbf {0} & \Sigma & \dots & \mathbf {0} \\ \vdots & \vdots & & \vdots \\ \mathbf {0} & \mathbf {0} & \dots & \Sigma \end{array} \right) \left( \begin{array}{c} b _ {1} I _ {p} \\ b _ {2} I _ {p} \\ \vdots \\ b _ {m} I _ {p} \end{array} \right) \\ = \sum_ {i = 1} ^ {m} a _ {i} b _ {i} \Sigma . \\ \end{array}
$$

最后我们由 $\sum_{i=1}^{m} a_i b_i = 0$, 可得 $\operatorname{Cov}(\mathbf{Z}_1, \mathbf{Z}_2) = 0$. 由性质 4.1.3 (1) 可知性质的第二部分成立.

性质 4.1.7 (标准化多元正态向量) 对于任意向量 X，均值为  $\mu$ ，协方差矩阵为  $\Sigma$ ，一个标准化向量 Z 可以通过如下两种方式获得:

(1) $Z = (T^{\mathrm{T}})^{-1}(\boldsymbol{X} - \boldsymbol{\mu})$, 其中 $T$ 为来自 $\Sigma$ 的 Cholesky (楚列斯基) 分解的非奇异上三角形矩阵, 即 $\Sigma = T^{\mathrm{T}}T$.
(2) $\boldsymbol{Z}=(\Sigma^{1/2})^{-1}(\boldsymbol{X}-\boldsymbol{\mu})$, 其中 $\Sigma^{1/2}$ 为 $\Sigma$ 的对称方根矩阵, 即 $(\Sigma^{1/2})^{2}=\Sigma$.

经标准化后，Z 的均值为  $0_{p}$ ，协方差矩阵为  $I_{p}$ 。进而，如果  $\boldsymbol{X} \sim N_{p}(\boldsymbol{\mu}, \Sigma)$ ，则  $\boldsymbol{Z} \sim N_{p}(\boldsymbol{0}_{p}, I_{p})$ 。

性质 4.1.8 (多元正态向量的二次型) 如果  $X \sim N_{p}(\boldsymbol{\mu}, \Sigma)$ ，则

$$
(\boldsymbol {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} \Sigma^ {- 1} (\boldsymbol {X} - \boldsymbol {\mu}) \sim \chi^ {2} (p).
$$

证明 根据 $\chi^2$ 分布的定义和标准化多元正态向量可直接得证 (留作习题). □

此二次型可以看作是 X 到  $\mu$  的 Mahalanobis 距离, 相比于标准的 Euclid(欧几里得) 距离, 它考虑了 X 的协方差带来的影响: 其具有刻度不变性, 也就是说不同方差大小的变量被以 “公平” 的方式在该距离中进行了整合, 而两个高度相关的变量贡献少于两个几乎不相关的变量.

## 性质 4.1.9 (二次型的相关结论)

(1) 令 $X \sim N_p(\mathbf{0}_p, \sigma^2 I_p)$, $A$ 为 $p \times p$ 对称、正半定矩阵, 且 $\operatorname{rank}(A) = r$, 则当且仅当 $A^2 = A$ 有 $\frac{\boldsymbol{X}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{X}}{\sigma^2} \sim \chi^2(r)$.
(2) 令  $\boldsymbol{X} \sim N_{p}(\boldsymbol{0}_{p}, \sigma^{2}I_{p})$ , A, B 为两个  $p \times p$  对称、正半定矩阵, 则当且仅当 AB = 0 时  $X^{T}AX$  与  $X^{T}BX$  相互独立.
(3) 令  $\boldsymbol{X} \sim N_{p}(\boldsymbol{0}_{p}, \sigma^{2}I_{p})$ , A 为  $p \times p$  对称、正半定矩阵, B 为  $q \times p$  矩阵 ( $q \leqslant p$ ), 则当且仅当 BA = 0 时,  $X^{T}AX$  与 BX 相互独立.
(4) 令 $X \sim N_p(\pmb{\mu}, \Sigma)$, $A$ 为 $p \times p$ 对称矩阵, 则有

$$
\begin{array}{l} E (\boldsymbol {X} ^ {\mathrm{T}} A \boldsymbol {X}) = \mathrm{tr} (A \Sigma) + \boldsymbol {\mu} ^ {\mathrm{T}} A \boldsymbol {\mu}, \\ \mathrm{Var} (\boldsymbol {X} ^ {\mathrm{T}} A \boldsymbol {X}) = 2 \mathrm{tr} (A \Sigma A \Sigma) + 4 \boldsymbol {\mu} ^ {\mathrm{T}} A \Sigma A \boldsymbol {\mu}. \\ \end{array}
$$

证明 利用对于 A 或 B 的谱分解.

(1) 由谱分解, 我们有 $A = CDC^{\mathrm{T}}$, 其中 $C$ 为正交矩阵, 由于 $\operatorname{rank}(A) = r$, $D = \operatorname{diag}(\lambda_1, \cdots, \lambda_r, 0, \cdots, 0)$. 令 $\mathbf{Y} = C^{\mathrm{T}}\mathbf{X}$, 则有 $\mathbf{Y} \sim N_p(\mathbf{0}_p, \sigma^2 I_p)$ 且

$$
\xi = \frac {\boldsymbol {X} ^ {\mathrm{T}} A \boldsymbol {X}}{\sigma^ {2}} = \frac {\boldsymbol {Y} ^ {\mathrm{T}} D \boldsymbol {Y}}{\sigma^ {2}} = \frac {\sum_ {i = 1} ^ {r} \lambda_ {i} Y _ {i} ^ {2}}{\sigma^ {2}}.
$$

- “充分性”:由于 $A^2 = A, \lambda_1 = \lambda_2 = \dots = \lambda_r = 1$. 因此 $\xi \sim \chi^2(r)$.
- “必要性”:$\chi^2 (k)$ 的特征函数为 $\varPhi(t) = (1 - 2\mathrm{i}t)^{-k / 2}$。注意到 $Y_{i}^{2} / \sigma^{2}\sim \chi^{2}(1)$，因此 $\xi$ 的特征函数为

$$
\begin{array}{l} \varPhi_ {\xi} (t) = E \left(\exp \left\{\mathrm{i} t \xi \right\}\right) = \prod_ {i = 1} ^ {r} E \left(\exp \left\{\mathrm{i} t \lambda_ {i} Y _ {i} ^ {2} / \sigma^ {2} \right\}\right) \\ = \prod_ {i = 1} ^ {r} (1 - 2 \mathrm{i} t \lambda_ {i}) ^ {- 1 / 2} = (1 - 2 \mathrm{i} t) ^ {- r / 2}. \\ \end{array}
$$

因此, $\lambda_{i}=1,i=1,2,\cdots,r$ ,并且 $A^{2}=A$ .

(2) 利用谱分解, 我们有 $A = C_1D_1C_1^{\mathrm{T}}$, $B = C_2D_2C_2^{\mathrm{T}}$. 令 $\widetilde{\mathbf{Y}}_1 = D_1^{1/2}C_1^{\mathrm{T}}\mathbf{X} \sim N_p(\mathbf{0}_p, \sigma^2 D_1)$, $\widetilde{\mathbf{Y}}_2 = D_2^{1/2}C_2^{\mathrm{T}}\mathbf{X} \sim N_p(\mathbf{0}_p, \sigma^2 D_2)$. 即 $\widetilde{\mathbf{Y}}_1^{\mathrm{T}}\widetilde{\mathbf{Y}}_1 = \mathbf{X}^{\mathrm{T}}\mathbf{A}\mathbf{X}$, 且 $\widetilde{\mathbf{Y}}_2^{\mathrm{T}}\widetilde{\mathbf{Y}}_2 = \mathbf{X}^{\mathrm{T}}\mathbf{B}\mathbf{X}$. 我们仅需证明当且仅当 $AB = 0$ 时, $\widetilde{\mathbf{Y}}_1$ 与 $\widetilde{\mathbf{Y}}_2$ 相互独立.

\- “充分性”:由 $0 = AB = C_1D_1C_1^{\mathrm{T}}C_2D_2C_2^{\mathrm{T}}$ 可知 $D_{1}C_{1}^{\mathrm{T}}C_{2}D_{2} = 0.$ 可得

$$
\mathrm{Cov} (\widetilde {\mathbf {Y}} _ {1}, \widetilde {\mathbf {Y}} _ {2}) = \sigma^ {2} D _ {1} ^ {1 / 2} C _ {1} ^ {\mathrm{T}} C _ {2} ^ {\mathrm{T}} D _ {2} ^ {1 / 2} = 0.
$$

因此, $\tilde{Y}_{1}$ 与 $\tilde{Y}_{2}$ 独立, $\tilde{Y}_{1}^{T}\tilde{Y}_{1}$ 和 $\tilde{Y}_{2}^{T}\tilde{Y}_{2}$ 亦独立.

\- “必要性”:由于 $\widetilde{\mathbf{Y}}_1$ 与 $\widetilde{\mathbf{Y}}_2$ 相互独立，因此 $\mathrm{Cov}(\widetilde{\mathbf{Y}}_1, \widetilde{\mathbf{Y}}_2) = 0$.

(3) 与 (2) 证明类似.
(4) 首先,

$$
\begin{array}{l} E \left(\boldsymbol {X} ^ {\mathrm{T}} A \boldsymbol {X}\right) = E \left[ \left(\boldsymbol {X} - \boldsymbol {\mu} + \boldsymbol {\mu}\right) ^ {\mathrm{T}} A \left(\boldsymbol {X} - \boldsymbol {\mu} + \boldsymbol {\mu}\right) \right] \\ = E \left\{\mathrm{tr} \left[ (\boldsymbol {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} A (\boldsymbol {X} - \boldsymbol {\mu}) \right] \right\} + \boldsymbol {\mu} ^ {\mathrm{T}} A \boldsymbol {\mu} \\ = E \left\{\mathrm{tr} \left[ A (\boldsymbol {X} - \boldsymbol {\mu}) (\boldsymbol {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} \right] \right\} + \boldsymbol {\mu} ^ {\mathrm{T}} A \boldsymbol {\mu} \\ = \operatorname{tr} \left\{A E \left[ (\boldsymbol {X} - \boldsymbol {\mu}) (\boldsymbol {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} \right] \right\} + \boldsymbol {\mu} ^ {\mathrm{T}} A \boldsymbol {\mu} \\ = \mathrm{tr} (A \Sigma) + \boldsymbol {\mu} ^ {\mathrm{T}} A \boldsymbol {\mu}. \\ \end{array}
$$

对于  $X^{T}AX$  的方差, 我们首先考虑  $Y^{T}AY$  的方差, 其中  $\boldsymbol{Y} \sim N_{p}(\boldsymbol{0}_{p}, I_{p})$ , 利用  $X = \Sigma^{1/2}Y + \mu$  来寻找  $\mathrm{Var}(X^{\mathrm{T}}AX)$ .

注意到 $E(\mathbf{Y}^{\mathrm{T}}\mathbf{A}\mathbf{Y}) = \mathrm{tr}(A)$，且 $\mathrm{Var}(\mathbf{Y}^{\mathrm{T}}\mathbf{A}\mathbf{Y}) = E\left[(\mathbf{Y}^{\mathrm{T}}\mathbf{A}\mathbf{Y})^{2}\right] - E^{2}(\mathbf{Y}^{\mathrm{T}}\mathbf{A}\mathbf{Y})$。为计算第一个期望，我们将二次型重写为 $\mathbf{Y}^{\mathrm{T}}\mathbf{A}\mathbf{Y} = \sum_{i,j}a_{ij}Y_iY_j$，得到

$$
(\boldsymbol {Y} ^ {\mathrm{T}} \boldsymbol {A} \boldsymbol {Y}) ^ {2} = \sum_ {i, j, k, l} a _ {i j} a _ {k l} Y _ {i} Y _ {j} Y _ {l} Y _ {k}.
$$

可见

$E(Y_{i}Y_{j}Y_{l}Y_{k})=\left\{\begin{aligned}&3,&\text{如果 }i=j=k=l;\\&1,&\text{如果 }i=j,k=l;\text{ 或者 }i=k,j=l;\text{ 或者 }i=l,j=k;\\&0,&\text{否则.}\end{aligned}\right.$  (4.1.2)

进而, 我们有

$$
\begin{array}{l} E \left[ \left(\boldsymbol {Y} ^ {\mathrm{T}} A \boldsymbol {Y}\right) ^ {2} \right] = 3 \sum_ {i} a _ {i i} ^ {2} + \sum_ {i} \left(\sum_ {k \neq i} a _ {i i} a _ {k k} + \sum_ {j \neq i} a _ {i j} ^ {2} + \sum_ {j \neq i} a _ {i j} a _ {j i}\right) \\ = \sum_ {i} a _ {i i} ^ {2} + \sum_ {i} \sum_ {k \neq i} a _ {i i} a _ {k k} + 2 \left(\sum_ {i} a _ {i i} ^ {2} + \sum_ {j \neq i} a _ {i j} ^ {2}\right) \\ = \mathrm{tr} ^ {2} (A) + 2 \mathrm{tr} (A ^ {2}). \\ \end{array}
$$

因此, 可得  $\mathrm{Var}(\mathbf{Y}^{\mathrm{T}}\mathbf{A}\mathbf{Y})=2\mathrm{tr}(A^{2})$ . 注意到

$$
\begin{array}{l} \boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {A} \boldsymbol {X} = (\Sigma^ {1 / 2} \boldsymbol {Y} + \boldsymbol {\mu}) ^ {\mathrm{T}} \boldsymbol {A} (\Sigma^ {1 / 2} \boldsymbol {Y} + \boldsymbol {\mu}) \\ = \boldsymbol {Y} ^ {\mathrm{T}} \Sigma^ {1 / 2} A \Sigma^ {1 / 2} \boldsymbol {Y} + 2 \boldsymbol {\mu} ^ {\mathrm{T}} A \Sigma^ {1 / 2} \boldsymbol {Y} + \boldsymbol {\mu} ^ {\mathrm{T}} A \boldsymbol {\mu}. \\ \end{array}
$$

因此, 我们有

$$
\begin{array}{l} \mathrm{Var} (\boldsymbol {X} ^ {\mathrm{T}} A \boldsymbol {X}) = 2 \mathrm{tr} (\Sigma^ {1 / 2} A \Sigma^ {1 / 2} \Sigma^ {1 / 2} A \Sigma^ {1 / 2}) + 4 \boldsymbol {\mu} ^ {\mathrm{T}} A \Sigma^ {1 / 2} \Sigma^ {1 / 2} A \boldsymbol {\mu} + \\ \mathrm{Cov} (\boldsymbol {Y} ^ {\mathrm{T}} \Sigma^ {1 / 2} A \Sigma^ {1 / 2} \boldsymbol {Y}, 2 \boldsymbol {\mu} ^ {\mathrm{T}} A \Sigma^ {1 / 2} \boldsymbol {Y}) \\ = 2 \mathrm{tr} (A \Sigma A \Sigma) + 4 \boldsymbol {\mu} ^ {\mathrm{T}} A \Sigma A \boldsymbol {\mu}. \\ \end{array}
$$

(需要检查  $\mathrm{Cov}(\boldsymbol{Y}^{\mathrm{T}}\Sigma^{1/2}A\Sigma^{1/2}\boldsymbol{Y},2\boldsymbol{\mu}^{\mathrm{T}}A\Sigma^{1/2}\boldsymbol{Y})=0.$  同 (4.1.2) 方法类似).

(另一种寻找  $\mathrm{Var}(\mathbf{Y}^{\mathrm{T}}\mathbf{A}\mathbf{Y})$  的方法) 由谱分解, 我们有  $A = CDC^{T}$ , 其中  $D = \mathrm{diag}(\lambda_{1}, \lambda_{2}, \cdots, \lambda_{p}), \lambda_{1} \geqslant \lambda_{2} \geqslant \cdots \geqslant \lambda_{p} \geqslant 0.$  令  $Z = C^{T}Y$ , 则  $Z \sim N_{p}(\mathbf{0}_{p}, I_{p})$ , 且

$$
\mathbf {Y} ^ {\mathrm{T}} A \mathbf {Y} = \mathbf {Z} ^ {\mathrm{T}} D \mathbf {Z} = \sum_ {i = 1} ^ {p} \lambda_ {i} Z _ {i} ^ {2},
$$

$$
(\mathbf {Y} ^ {\mathrm{T}} A \mathbf {Y}) ^ {2} = (\mathbf {Z} ^ {\mathrm{T}} D \mathbf {Z}) ^ {2} = \sum_ {i = 1} ^ {p} \lambda_ {i} ^ {2} Z _ {i} ^ {4} + \sum_ {i = 1} ^ {p} \sum_ {j \neq i} \lambda_ {i} \lambda_ {j} Z _ {i} ^ {2} Z _ {j} ^ {2}.
$$

注意到如下事实: