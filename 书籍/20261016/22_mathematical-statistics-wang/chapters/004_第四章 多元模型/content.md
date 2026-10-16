# 第四章 多元模型

原始 PDF 第 176–223 页。

## 第四章

## 多元模型

---

164

第四章 多元模型

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

---

4.1 多元分布

165

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

![](../../raw/pages_0177-0192/images/page_177_chart_6.jpg)

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

---

166

第四章 多元模型

![](../../raw/pages_0177-0192/images/page_178_chart_2.jpg)

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

---

4.1 多元分布

167

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

---

168

第四章 多元模型

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

---

4.1 多元分布

169

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

---

170

第四章 多元模型

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

---

4.1 多元分布

171

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

![](../../raw/pages_0177-0192/images/page_183_chart_10.jpg)

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

---

172

第四章 多元模型

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

---

4.1 多元分布

173

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

---

174

第四章 多元模型

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

---

4.1 多元分布

175

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

---

176

第四章 多元模型

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

---

4.1 多元分布

177

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

---

178

第四章 多元模型

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

---

4.1 多元分布

179

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

---

180

第四章 多元模型

- $Z_{1}, Z_{2}, \cdots, Z_{p}$ 独立同分布于 $N(0,1)$.
- $Z_{i}^{2} \sim \chi^{2}(1)$, $E(Z_{i}^{2}) = 1$ 且 $E(Z_{i}^{4}) = \mathrm{Var}(Z_{i}^{2}) + E^{2}(Z_{i}^{2}) = 3$.

于是, 我们有

$$
\begin{array}{l} E \left[ \left(\boldsymbol {Y} ^ {\mathrm{T}} A \boldsymbol {Y}\right) ^ {2} \right] = E \left[ \left(\boldsymbol {Z} ^ {\mathrm{T}} D \boldsymbol {Z}\right) ^ {2} \right] = 3 \sum_ {i = 1} ^ {p} \lambda_ {i} ^ {2} + \sum_ {i = 1} ^ {p} \sum_ {i \neq j} \lambda_ {i} \lambda_ {j} \\ = 2 \sum_ {i = 1} ^ {p} \lambda_ {i} ^ {2} + \sum_ {i = 1} ^ {p} \sum_ {j = 1} ^ {p} \lambda_ {i} \lambda_ {j} \\ = 2 \mathrm{tr} (A ^ {2}) + \mathrm{tr} ^ {2} (A). \\ \end{array}
$$

进而得到 $\mathrm{Var}(\mathbf{Y}^{\mathrm{T}}\mathbf{A}\mathbf{Y}) = 2\mathrm{tr}(A^{2}).$

同理可证 $\mathrm{Cov}(\mathbf{Y}^{\mathrm{T}}\Sigma^{1 / 2}A\Sigma^{1 / 2}\mathbf{Y},2\pmb{\mu}^{\mathrm{T}}A\Sigma^{1 / 2}\mathbf{Y}) = 0.$

![](../../raw/pages_0193-0208/images/page_192_image_9.jpg)

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

---

4.2 多元模型的统计推断

181

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

---

182

第四章 多元模型

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

---

4.2 多元模型的统计推断

183

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

---

184

第四章 多元模型

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

注 4.2.1 类似一元情形 (见习题一 36), 多元情形的样本相关系数也有相应的分布, 但其精确分布较为复杂 (见 Fisher(1915)), 通常我们使用其渐近分布. 假设  $\rho$  和  $\hat{\rho}$  分别为二元正态向量  $(X,Y)^{\mathrm{T}}$  的总体和样本相关系数, 由附

---

4.2 多元模型的统计推断

185

录 A.4 的内容, 基于多元 Delta 方法可证明,

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

---

186

第四章 多元模型

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

---

4.2 多元模型的统计推断

187

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

---

188

第四章 多元模型

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

---

4.2 多元模型的统计推断

189

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

---

190

第四章 多元模型

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

---

4.2 多元模型的统计推断

191

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

---

192

第四章 多元模型

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

---

4.2 多元模型的统计推断

193

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

---

194

第四章 多元模型

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

---

4.3 多重检验

195

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

---

196

第四章 多元模型

下面以  $m_{0}$  表示 m 个检验中的零假设是正确的检验的个数，并记  $m_{1}=m-m_{0}$  。令  $H_{0}=\{i:$  真实的  $H_{0i}\}$ ， $H_{1}=\{i:$  真实的  $H_{1i}\}$ ，用  $p_{1}, p_{2}, \cdots, p_{m}$  表示这 m 个检验的 p 值。

此时, 控制一个检验的第一类错误概率  $\alpha$ , 比如 0.05, 意义并不大, 必须对全部检验统一来考虑. 我们需要新的准则以及针对新准则开发出确定拒绝域的方法. 这里我们仅用两个最常用的错误率准则, 也就是总体错误率和错误发现率为例进行阐述.

## 4.3.2 总体错误率的控制

第一类方法是考虑 family-wise error rate (FWER), 一般也称为总体错误率, 其定义就是错误拒绝任何一个零假设的概率.

下面我们以例 4.3.2 中的多重比较问题来探讨如何选取临界值控制 FWER. 为方便讨论, 我们假设每个水平下的观测次数相等, 即  $n_{i}=t, i=1,2,\cdots,r, n=rt$ . 此时两样本均值检验统计量为

$$
T _ {i j} = \frac {\sqrt {t} (\bar {Y} _ {i .} - \bar {Y} _ {j .})}{\hat {\sigma} \sqrt {2}}, \tag {4.3.3}
$$

其中  $\bar{Y}_{i.}=\sum_{j=1}^{n_{i}}Y_{ij},\hat{\sigma}^{2}=(n-r)^{-1}\sum_{i=1}^{r}\sum_{j=1}^{n_{i}}(Y_{ij}-\bar{Y}_{i.})^{2},n=\sum_{i=1}^{r}n_{i}.$

为控制该多重检验的FWER，我们需要寻找适当的临界值 $L$ 使得 $P(W) \leqslant \alpha$ 这里

$$
W = \bigcup_ {i <   j} \left\{\frac {\sqrt {t} | \bar {Y} _ {i .} - \bar {Y} _ {j .} |}{\hat {\sigma}} \geqslant L \right\}.
$$

注意到

$$
\begin{array}{l} P (W) = 1 - P \left(\bigcap_ {i <   j} \left\{\frac {\sqrt {t} | \bar {Y} _ {i .} - \bar {Y} _ {j .} |}{\hat {\sigma}} \leqslant L \right\}\right) \\ = 1 - P \left(\max _ {i <   j} \frac {\sqrt {t} | \bar {Y} _ {i .} - \bar {Y} _ {j .} |}{\hat {\sigma}} \leqslant L\right) \\ = P \left(\max _ {i <   j} \frac {\sqrt {t} | \bar {Y} _ {i .} - \bar {Y} _ {j .} |}{\hat {\sigma}} \geqslant L\right) \\ = P \left(\max _ {i <   j} \frac {\sqrt {t} | (\bar {Y} _ {i .} - \mu_ {i}) - (\bar {Y} _ {j .} - \mu_ {j}) |}{\hat {\sigma}} \geqslant L\right) \\ = P \left(\max _ {i} \frac {\sqrt {t} (\bar {Y} _ {i .} - \mu_ {i})}{\hat {\sigma}} - \min _ {i} \frac {\sqrt {t} (\bar {Y} _ {i .} - \mu_ {i})}{\hat {\sigma}} \geqslant L\right). \\ \end{array}
$$

由于在模型 (4.3.1) 下,

$$
\frac {\sqrt {t} (\bar {Y} _ {i .} - \mu_ {i})}{\hat {\sigma}} \sim t (n - r),
$$

---

4.3 多重检验

197

因此, L 可选取为如下随机变量  $SR(r, n - r)$  分布的上  $\alpha$  分位数: 设  $T_{1}, T_{2}, \cdots, T_{r}$  为来自  $t(m)$  的独立同分布样本, 记其次序统计量为  $T_{(1)} \leqslant T_{(2)} \leqslant \cdots \leqslant T_{(r)}$ . 定义

$$
S R (r, m) = T _ {(r)} - T _ {(1)}. \tag {4.3.4}
$$

在文献中, $SR(r,m)$ 被称为Tukey学生化极差, 其分布称为学生化极差分布 (studentized range distribution).

例 4.3.3 为研究四种防锈剂 (记  $A_{1}, A_{2}, A_{3}, A_{4}$ ) 的防锈能力, 现把 40 件同一厂家生产的大小、形状、质地相同的铁件随机分成四组, 每组 10 件, 随机分配防锈剂给每组铁件, 最后把涂好防锈剂的 40 件铁件放置到相同环境中. 一段时间后请 5 位专家对每一铁件的锈迹程度打分: 没有锈迹的 100 分, 全锈的 0 分. 每一铁件的 5 位专家打分的平均值如表 4.3.1 所示.

表 4.3.1 例 4.3.3 中四种防锈剂的防锈能力分数

| 序号 | $A_1$ | $A_2$ | $A_3$ | $A_4$ |
| --- | --- | --- | --- | --- |
| 1 | 43.9 | 89.8 | 68.4 | 36.2 |
| 2 | 39.0 | 87.1 | 69.3 | 45.2 |
| 3 | 46.7 | 92.7 | 68.5 | 40.7 |
| 4 | 43.8 | 90.6 | 66.4 | 40.5 |
| 5 | 44.2 | 87.7 | 70.0 | 39.3 |
| 6 | 47.7 | 92.4 | 68.1 | 40.3 |
| 7 | 43.6 | 86.1 | 70.6 | 43.2 |
| 8 | 38.9 | 88.1 | 65.2 | 38.7 |
| 9 | 43.6 | 90.8 | 63.8 | 40.9 |
| 10 | 40.0 | 89.1 | 69.2 | 39.7 |

请问四种防锈剂的防锈能力是否存在差异？如存在差异，哪种最好？(见茆诗松等(2012).)

解 方差分析显示这四种防锈剂间存在显著差异. 另外, 它们的估计值分别为

$$
\hat {\mu} _ {1} = \bar {y} _ {1.} = 4 3. 1 3, \hat {\mu} _ {2} = \bar {y} _ {2.} = 8 9. 4 4, \hat {\mu} _ {3} = \bar {y} _ {3.} = 6 7. 9 5, \hat {\mu} _ {4} = \bar {y} _ {4.} = 4 0. 4 7,
$$

可见第二种防锈剂的防锈能力最强.

下面应用上述多重比较方法检验两两间的差异如何. 此时, $r = 4$, $s = 10$, $n = 40$, $\hat{\sigma}^2 = 6.148$. 对于 $\alpha = 0.05$, 可知 $L = 3.82$, 故有

$$
\frac {\hat {\sigma}}{\sqrt {s}} L = \frac {\sqrt {6 . 1 4 8}}{\sqrt {1 0}} \times 3. 8 2 = 2. 9 9 5.
$$

而两两水平均值之差为

$$
\left| \bar {y} _ {1.} - \bar {y} _ {2.} \right| = 4 6. 3,
$$

---

198

第四章 多元模型

$$
| \bar {y} _ {1.} - \bar {y} _ {3.} | = 2 4. 8,
$$

$$
\left| \bar {y} _ {1.} - \bar {y} _ {4.} \right| = 2. 6 6 <   2. 9 9 5,
$$

$$
| \bar {y} _ {2.} - \bar {y} _ {3.} | = 2 1. 4 9,
$$

$$
\left| \bar {y} _ {2.} - \bar {y} _ {4.} \right| = 4 8. 9 7,
$$

$$
| \bar {y} _ {3.} - \bar {y} _ {4.} | = 2 7. 4 8,
$$

故由多重比较知, 仅接受  $H_{0}^{14}$ , 即可以把四种防锈剂分为三类: 第一类为  $A_{2}$ ; 第二类为  $A_{3}$ ; 第三类为  $A_{1}, A_{4}$ .

对于本问题来说, 在最理想的假设下, 即 r 个水平所对应的样本相互独立以及正态分布情形下, 我们可以有严格控制 FWER 等于  $\alpha$  的方法. 是否有更加一般化的控制 FWER 的手段呢? 著名的 Bonferroni (邦费罗尼) 方法就是最常用、最简单的用于控制检验 FWER 的工具, 即

$$
\text {如果} p _ {i} <   \alpha / m, \text {则拒绝原假设} H _ {0 i}.
$$

我们有如下的定理.

定理 4.3.1 使用 Bonferroni 方法, 错误地拒绝任何一个零假设的概率小于或等于  $\alpha$ .

证明 令 R 表示至少有一个零假设被错误拒绝的事件, 而  $R_{i}$  表示第 i 个零假设被错误拒绝的事件. 则由经典的 Bonferroni 不等式, 我们有

$$
P (R) = P \left(\bigcup_ {i = 1} ^ {m} R _ {i}\right) \leqslant \sum_ {i = 1} ^ {m} P (R _ {i}) = \sum_ {i = 1} ^ {m} \frac {\alpha}{m} = \alpha .
$$

注意到, Bonferroni 方法不要求各个检验是独立的, 我们仅需要知道每个检验统计量的零分布即可, 这在实际使用上是非常方便的. 控制 FWER 还有一种改进的方法, 其是序贯进行的, 被称为 Holm (霍尔姆) 方法, 其检验过程如下:

(1) 如果  $p_{(1)} \leqslant \alpha / m$ ，则拒绝  $H_{(1)}$ ，转到第二步；否则接受  $H_{(1)}, H_{(2)}, \cdots, H_{(m)}$  并停止.
(2) 如果  $p_{(i)} \leqslant \alpha / (m - i + 1)$ ，则拒绝  $H_{(i)}$ ，转到第  $i + 1$  步；否则接受  $H_{(i)}, \cdots, H_{(m)}$  并停止.

当 $p_{(i)}$ 超过临界值 $\alpha_{i} = \alpha / (m - i + 1)$ 时, Holm 方法就停止了. 可以看出, 该方法比 Bonferroni 方法具有更高的势, 这是因为 Bonferroni 方法中每个 $p$ 值的临界值都是 $\alpha / m$. 下面我们证明该方法的有效性.

记 $i_0$ 是所有零假设中 $p$ 值最小的所对应的秩, 此处的秩指数据从小到大排序后所对应的次序, 也就是在Holm方法中我们会在第 $i_0$ 步第一次遇到真实的零假设. 显然有,

$$
i _ {0} \leqslant m - m _ {0} + 1.
$$

---

4.3 多重检验

199

也就是说, 在 Holm 方法的步骤中第一个真实的零假设会在最多  $m - m_{0}$  个假设前遇到.
注意到, 我们做出一个错误的拒绝当且仅当

$$
p _ {(1)} \leqslant \frac {\alpha}{m}, p _ {(2)} \leqslant \frac {\alpha}{m - 1}, \dots , p _ {(i _ {0})} \leqslant \frac {\alpha}{m - i _ {0} + 1}.
$$

这就意味着

$$
p _ {(i _ {0})} \leqslant \frac {\alpha}{m - i _ {0} + 1} \leqslant \frac {\alpha}{m _ {0}}.
$$

因此, 错误拒绝的概率就被下式所控制:

$$
P \left(\min _ {i \in \mathcal {H} _ {0}} p _ {i} \leqslant \frac {\alpha}{m _ {0}}\right) \leqslant \sum_ {i \in \mathcal {H} _ {0}} P (p _ {i} \leqslant \alpha / m _ {0}) = \alpha .
$$

![](../../raw/pages_0209-0224/images/page_211_image_8.jpg)

## 4.3.3 错误发现率的控制

在例 4.3.1 中, 如果我们使用考虑控制 FWER 低于  $\alpha = 0.05$  并使用 Bonferroni 方法, 则对每一个检验我们等价于需要使用显著性水平  $0.05 / 12256 \approx 4 \times 10^{-6}$ . 因此得到, 对于任何一个基因, 只有其 p 值小于  $4 \times 10^{-6}$ , 我们才能说该基因在两组患者中有不同的表达水平.

显然, 控制 FWER, 或者说 Bonferroni 方法在这样同时做成千上万个检验的时候是非常保守的, 这是因为它试图使你不可能做出一次错误的拒绝. 即便使用 Holm 改进方法, 当 m 非常大时, 改进非常有限. 此时, 我们可能需要换个思路: 保守不是因为检验统计量不好, 而是我们的这个 “至少错误拒绝一个” 的要求在实际中可能太过苛刻了. 由此, 在 Benjamini et al.(1995) 中 Benjamini 和 Hochberg 提出了一个更加合理的策略, 即控制所谓的 false discovery rate (FDR), 一般称之为错误发现率, 其定义是在所有拒绝的检验中错误拒绝比例的期望.

假设给定一个临界值, 我们拒绝掉所有 p 值小于该临界值的零假设. 所有的检验可以被划分在如表 4.3.2 中.

表 4.3.2 判断表

|  | $H_0$没有被拒绝 | $H_0$被拒绝 | 总和 |
| --- | --- | --- | --- |
| $H_0$是正确的 | U | V | $m_0$ |
| $H_0$是错误的 | T | S | $m_1$ |
| 总和 | m-R | R | m |

此时, 我们定义错误拒绝比例 (false discovery proportion, 简记为 FDP) 为

$$
\mathrm{FDP} = \frac {V}{R} I (R > 0).
$$

---

200

第四章 多元模型

注意到这个 FDP 是一个随机变量, 其依赖于  $p_{1}, p_{2}, \cdots, p_{m}$ , 代表了所有拒绝的决策中错误的比例, 而错误发现率就是其期望, 即  $\mathrm{FDR} = E(\mathrm{FDP})$ . 使用这样的准则, 例如, 在一次性检验成千上万的假设时, 是合理的, 因为我们很多时候可以接受一定数量的拒真错误 (也就是假阳性), 而找到更多的真实信号 (备择假设) 从而带来更多的收益. 当然, 这并不意味着 FWER 不再有用, 当检验个数较少, 或者对拒真错误的风险较为敏感时 (比如确定几种不同的治疗方案), 统计工作者需要根据问题来选定相应的准则.

FDR 这一概念在著名论文 Benjamini et al.(1995) 中被提出, 由于其简单直观, 在诸多的大数据推断问题中体现出了强大的功效, 因此很快成了一个标准的多重检验度量, 获得了极高的引用 (该论文是迄今为止统计科学史上引用率最高的论文). 尽管经过了二十多年的发展, 已有大量的 FDR 理论分析和控制方法, 但该领域仍是现代统计的一个非常热门的方向, 新思想、新方法仍然层出不穷.

这里的核心问题有两个, 一是如何选取临界值, 从而控制 FDR; 二是如何利用 m 个检验的 (其他) 信息, 如相关性等, 来提高检验的功效. 在这里我们仅探讨最经典的 Benjamini-Hochberg(简称 BH) 控制方法, 其在今天仍是大家最常用的、最标准的方法. BH 检验过程如下:

(1) 令  $p_{(1)} < p_{(2)} < \cdots < p_{(m)}$  表示 p 值  $p_{1}, p_{2}, \cdots, p_{m}$  的次序统计量.
(2) 定义 $\ell_i = i\alpha / (mC_m)$, $R = \max \{i : p_{(i)} < \ell_i\}$, 其中如果 $m$ 个检验独立则令 $C_m = 1$; 否则取 $C_m = \sum_{i=1}^{m}(1/i)$.
(3) 令  $T = p_{(R)}$ ; 此时 T 就是 BH 方法的临界值.
(4) 拒绝所有满足  $p_{i} \leqslant T$  的  $H_{0i}$ .

我们有如下结论.

定理 4.3.2 假设 p 个检验独立. 使用 BH 方法, 无论  $H_{0}$  正确的个数是多少, 也无论  $H_{0}$  错误的时候 p 值的分布如何, 我们总是有

$$
\mathrm{FDR} = E (\mathrm{FDP}) = \frac {m _ {0}}{m} \alpha \leqslant \alpha .
$$

关于该结论的证明以及其各种推广在最近二十年的文献中有很多讨论, 这里我们采用在 FDR 文献中常用的 “leave-one-out” 方法.

证明 当 $m_0 = 0$ 时结论自然成立, 我们假设 $m_0 \geqslant 1$. 定义

$$
V _ {i} = I (H _ {0 i} \text {被拒绝}), i \in \mathcal {H} _ {0},
$$

因此我们可表示 FDP 为

$$
\mathrm{FDP} = \sum_ {i \in \mathcal {H} _ {0}} \frac {V _ {i}}{R \vee 1}.
$$

---

4.3 多重检验

201

我们将证明 $E[V_i / (R\vee 1)] = \alpha /n.$ 如果该式成立，则立即有

$$
\mathrm{FDR} = \sum_ {i \in \mathcal {H} _ {0}} E \left(\frac {V _ {i}}{R \vee 1}\right) = \sum_ {i \in \mathcal {H} _ {0}} \frac {\alpha}{n} = \frac {n _ {0}}{n} \alpha .
$$

由定义有 $\frac{V_i}{R\vee 1} = \sum_{k = 1}^{m}\frac{V_iI(R = k)}{k}$. 当 $R = 0$ 时, 我们得到 $V_{i} / (R\vee 1) = 0$, 则结论自然成立, 下面考虑 $R \neq 0$.

注意到在 BH 方法中的两个事实:

- 当共有 $k$ 个拒绝时, $H_{0i}$ 被拒绝当且仅当 $p_i \leqslant \alpha k / m$. 因此, $V_i = I(p_i \leqslant \alpha k / m)$.
- 假设 $p_i \leqslant \alpha k / m$, 我们将 $p_i$ 的值置为零. 将此时的拒绝总数记为 $R(p_i \to 0)$. 此时, 这个值精确等于 $R$, 因为, 我们置零这一操作仅影响前 $k$ 个 $p$ 值的顺序, 所有这 $k$ 个值仍然低于临界值 $\alpha k / m$. 另一方面, 如果 $p_i > \alpha k / m$, 则我们不拒绝 $p_i$, 因此 $V_i = 0$. 所以我们总是有 $V_i I(R = k) = V_i I(R(p_i \to 0) = k)$.

基于如上事实, 取关于  $F_{i}=\{p_{1},\cdots,p_{i-1},p_{i+1},\cdots,p_{m}\}$  的条件期望, 我们有

$$
\begin{array}{l} E \left(\frac {V _ {i}}{R \vee 1} \Big | \mathcal {F} _ {i}\right) = \sum_ {k = 1} ^ {m} \frac {E \left[ I (p _ {i} \leqslant \alpha k / m) I (R (p _ {i} \rightarrow 0) = k) \mid \mathcal {F} _ {i} \right]}{k} \\ = \sum_ {k = 1} ^ {m} \frac {I (R (p _ {i} \to 0) = k) \alpha k / m}{k}, \\ \end{array}
$$

其中第二个等式是因为在给定  $F_{i}$  和  $p_{i}=0$  下  $I(R(p_{i}\rightarrow0)=k)$  是确定的. 这里我们也用到了  $p_{i}\sim U(0,1)$  且相互独立.

最后, 我们有结论

$$
E \left(\frac {V _ {i}}{R \vee 1} \Big | \mathcal {F} _ {i}\right) = \frac {\alpha}{m} \sum_ {k = 1} ^ {m} I (R (p _ {i} \to 0) = k) = \frac {\alpha}{m}.
$$

这里利用了事实  $\sum_{k=1}^{m} I(R(p_{i} \to 0) = k) = 1$ . 这是因为当我们置一个真实零假设的  $p_{i}$  为零时，则至少做了一次错误拒绝——我们总是会拒绝  $H_{0i}$ . 因此， $R(p_{i} \to 0) \geqslant 1$ ，并且  $R(p_{i} \to 0)$  取 [1, m] 中的一个值. □

注意到, 上面的标准 BH 方法的有效性是基于所有真实零假设对应的 p 值是独立这一前提的. 事实上, 当这些 p 值的相关性不是很强时, 可以证明相应的 FDR 是能够被渐近地控制在  $\alpha$  水平的  $(m \to \infty)$ , 参见 Storey et al.(2004). 对于有限样本的情形, 就需要更为具体的相关性假设. 这里介绍文献中著名的 PRDS 假设. 下面的叙述中我们用  $x = (x_{1}, x_{2}, \cdots, x_{n}) \geqslant y = (y_{1}, y_{2}, \cdots, y_{n})$  表示  $x_{i} \geqslant y_{i}, \forall i$ .

定义 4.3.1 如果  $x \in D$  且  $y \geqslant x$  意味着  $y \in D$ ，则集合  $D \in R^{m}$  被称作是单增的.

---

202

第四章 多元模型

定义 4.3.2 如果对于任意单增集合和所有的  $i \in G_{0}$ ,  $P((X_{1}, X_{2}, \cdots, X_{m}) \in D \mid X_{i} = x)$  是关于 x 单增的，则我们称随机向量  $\boldsymbol{X} = (X_{1}, X_{2}, \cdots, X_{m})^{\mathrm{T}}$  是在  $G_{0}$  上 PRDS (positive regression dependence on each of a subset) 的.

如果 $X$ 是在 $\mathcal{H}_0$ 上PRDS的, 则基于样本均值构造的 $t$ 统计量所对应的 $p$ 值也是PRDS的.

我们看一个经典的 PRDS 例子.

命题 4.3.1 假设  $X \sim N_{m}(\mu, \Sigma)$ . 如果对  $i \in H_{0}$  和所有的 j 都有  $\sigma_{ij} > 0$ , 则 X 是在  $H_{0}$  上 PRDS 的.

证明 令  $\boldsymbol{X}_{1}=(X_{1},X_{2},\cdots,X_{m-1})$ ，注意到

$$
\boldsymbol {X} = \binom{\boldsymbol {X} _ {1}}{X _ {m}}, \quad \Sigma = \left( \begin{array}{c c} \Sigma_ {1 1} & \Sigma_ {1 2} \\ \Sigma_ {2 1} & \Sigma_ {2 2} \end{array} \right),
$$

$$
(\boldsymbol {X} _ {1} \mid X _ {m} = x) \sim N _ {m - 1} \left(\boldsymbol {\mu} _ {1} + \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} \left(x - \boldsymbol {\mu} _ {2}\right), \Sigma_ {1 1 \cdot 2}\right),
$$

$$
\Sigma_ {1 1 \cdot 2} = \Sigma_ {1 1} - \Sigma_ {1 2} \Sigma_ {2 2} ^ {- 1} \Sigma_ {2 1},
$$

注意到协方差不依赖于 x，因此如果  $\Sigma_{12}$  是正定的，则上面的条件分布是关于 x (随机) 单增的。因此，对于非降函数  $f, x \leqslant x'$  意味着

$$
E \left[ f (X) \mid X _ {m} = x \right] \leqslant E \left[ f (X) \mid X _ {m} = x ^ {\prime} \right].
$$

取 f 为单增集合的示性函数则可得到结论.

我们有如下在 PRDS 假设下的 FDR 控制结论.

定理 4.3.3 如果检验统计量的联合分布 (或者 p 值的联合分布) 是在  $H_{0}$  上 PRDS 的, 则 BH 方法控制 FDR 在  $\alpha \frac{m_{0}}{m}$  水平上.

证明 回顾 $\mathrm{FDR} = E\left(\sum_{i\in \mathcal{H}_0}\frac{V_i}{R\vee 1}\right)$. 下面我们证明 $E[V_i / (R\vee 1)]\leqslant \alpha /m$. 令 $\alpha_{k} = \alpha k / m,$ 我们有

$$
\begin{array}{l} \frac {V _ {i}}{R \vee 1} = \sum_ {k \geqslant 1} \frac {I (p _ {i} \leqslant \alpha_ {k}) I (R = k)}{k} \\ = \sum_ {k \geqslant 1} \frac {I \left(p _ {i} \leqslant \alpha_ {k}\right) \left[ I \left(R \leqslant k\right) - I \left(R \leqslant k - 1\right) \right]}{k} \\ = \sum_ {k = 1} ^ {m - 1} \left[ \frac {I (p _ {i} \leqslant \alpha_ {k})}{k} - \frac {I (p _ {i} \leqslant \alpha_ {k + 1})}{k + 1} \right] I (R \leqslant k) + \frac {I (R \leqslant m) I (p _ {i} \leqslant \alpha)}{m}. \\ \end{array}
$$

注意到 $E\left[\frac{I(R \leqslant m)I(p_i \leqslant \alpha)}{m}\right] = \frac{\alpha}{m}$ 总是成立的. 对于每个 $k$, 我们有

$$
E \left\{\left[ \frac {I (p _ {i} \leqslant \alpha_ {k})}{k} - \frac {I (p _ {i} \leqslant \alpha_ {k + 1})}{k + 1} \right] I (R \leqslant k) \right\}
$$

---

4.3 多重检验

203

$$
\begin{array}{l} = \frac {P (p _ {i} \leqslant \alpha_ {k} , R \leqslant k)}{k} - \frac {P (p _ {i} \leqslant \alpha_ {k + 1} , R \leqslant k)}{k + 1} \\ = \frac {P (R \leqslant k \mid p _ {i} \leqslant \alpha_ {k}) P (p _ {i} \leqslant \alpha_ {k})}{k} - \frac {P (R \leqslant k \mid p _ {i} \leqslant \alpha_ {k + 1}) P (p _ {i} \leqslant \alpha_ {k + 1})}{k + 1} \\ \leqslant \frac {P (R \leqslant k \mid p _ {i} \leqslant \alpha_ {k + 1}) P (p _ {i} \leqslant \alpha_ {k})}{k} - \frac {P (R \leqslant k \mid p _ {i} \leqslant \alpha_ {k + 1}) P (p _ {i} \leqslant \alpha_ {k + 1})}{k + 1} = 0. \\ \end{array}
$$

这里的不等式就利用了 PRDS 性质: 对于 $t \leqslant t'$, 如果 $i$ 属于 $\mathcal{H}_0$ 且 $D$ 是单增的, 则 $P(D \mid p_i \leqslant t) \leqslant P(D \mid p_i \leqslant t')$. 事实上, $\{R \leqslant k\}$ 确实是一个单增集合, 这是因为当 $p_i$ 增大, $R$ 就会降低 (我们将会拒绝更少的假设).

最后, 我们讨论在不对相关性做任何假设下, 如何调整 BH 方法使其仍然能够控制 FDR.

命题 4.3.2 当检验之间存在相关性时, BH 方法的 FDR 水平上界为  $\alpha \cdot a(m) \cdot \frac{m_{0}}{m}$ , 这里  $a(m) = 1 + 1/2 + 1/3 + \cdots + 1/m \approx \ln m + 0.577$ .

证明 回顾 $\mathrm{FDP} = \sum_{i\in \mathcal{H}_0}\frac{V_i}{R\vee 1}$. 如果我们证明对于任意的真实零假设都有

$$
E \left(\frac {V _ {i}}{R \vee 1}\right) \leqslant \frac {\alpha}{m} a (m),
$$

则 $\mathrm{FDR}\leqslant \alpha \cdot a(m)\cdot \frac{m_0}{m}.$

令  $\alpha_{k}=\alpha k/m,$  我们有

$$
\begin{array}{l} \frac {V _ {i}}{1 \vee R} = \sum_ {k = 1} ^ {m} \frac {I (p _ {i} \leqslant \alpha_ {k}) I (R = k)}{k} \\ = \sum_ {k = 1} ^ {m} \sum_ {\ell = 1} ^ {k} \frac {I \left(p _ {i} \in (\alpha_ {\ell - 1} , \alpha_ {\ell})\right) I (R = k)}{k} \\ = \sum_ {\ell = 1} ^ {m} \sum_ {k \geqslant \ell} ^ {m} \frac {I (R = k)}{k} I \left(p _ {i} \in (\alpha_ {\ell - 1}, \alpha_ {\ell})\right) \\ = \sum_ {\ell = 1} ^ {m} \frac {I (R \geqslant \ell)}{R} I \left(p _ {i} \in (\alpha_ {\ell - 1}, \alpha_ {\ell})\right) \\ \leqslant \sum_ {\ell = 1} ^ {m} \frac {1}{\ell} I \left(p _ {i} \in (\alpha_ {\ell - 1}, \alpha_ {\ell})\right). \\ \end{array}
$$

取期望后就可以得到结论.

由该命题可知, 当没有任何相关性信息且对有限样本下的 FDR 控制要求较为严格时, 我们可以在 BH 方法中用  $\alpha/a(m)$  取代  $\alpha$  来进行检验, 此时相应的 FDR 被控制在  $\alpha$  以下. 当然, 这是个保守的策略, 这再次体现了统计学中的 “平衡”——精确性和一般性之间总是要进行一定的 “妥协”.

---

204

第四章 多元模型

## 习题四

1. 如果 $X = (X_{1}, X_{2}, X_{3})^{\mathrm{T}} \sim N_{3}(\pmb{\mu}, \Sigma)$，且

$$
\Sigma = \left( \begin{array}{c c c} 4 & 1 & 0 \\ 1 & 3 & 0 \\ 0 & 0 & 2 \end{array} \right),
$$

则 $X_{1}$ 与 $X_{2}$ 是否相互独立？ $(X_{1},X_{2})$ 与 $X_{3}$ 是否独立？

2. 如果 $A$ 为 $p \times p$ 对称常数矩阵, $\mathbf{X} \sim N_p(\boldsymbol{\mu}, \Sigma)$, 证明:

$$
\mathrm{Cov} (\boldsymbol {X}, \boldsymbol {X} ^ {\mathrm{T}} A \boldsymbol {X}) = 2 \Sigma A \boldsymbol {\mu}. \tag {4.1}
$$

3. 考虑一个多元正态分布 $N_{3}(\pmb{\mu}, \Sigma)$, 请用矩阵语言 $A\pmb{\mu} = \pmb{a}$ 叙述假设 $H_{0}: \mu_{1} = \mu_{2} = \mu_{3}$.

4. 模拟一个具有  $\boldsymbol{\mu}=\begin{pmatrix}1\\2\end{pmatrix}$  和  $\Sigma=\begin{pmatrix}1&0.5\\0.5&2\end{pmatrix}$  的正态样本, 首先在  $\Sigma$  已知的情况下, 然后在  $\Sigma$  未知的情况下, 检验  $H_{0}:2\mu_{1}-\mu_{2}=0.2$ .

5. 假设  $X_{1}, X_{2}, \cdots, X_{n}$  是从  $N_{p}(\boldsymbol{\mu}, \Sigma)$  总体中抽取的独立同分布样本. 在  $\Sigma$  未知且  $\mu = \mu_{0}$  的条件下, 证明对数似然函数的最大值为

$$
\ell_ {0} ^ {*} = \ell \left(\boldsymbol {\mu} _ {0}, \hat {\Sigma} + \boldsymbol {d} \boldsymbol {d} ^ {\mathrm{T}}\right), \quad \boldsymbol {d} = \bar {\boldsymbol {x}} - \boldsymbol {\mu} _ {0}.
$$

6. 假设  $X_{1}, X_{2}, \cdots, X_{n}$  是从  $N_{p}(\boldsymbol{\mu}, \Sigma)$  总体中抽取的独立同分布样本，并考虑在  $\Sigma$  未知的条件下检验  $H_{0}: \mu = \mu_{0} \leftrightarrow H_{1}: \mu \neq \mu_{0}$  。证明似然比检验的统计量等于

$$
- 2 \ln \lambda = n \ln \left(1 + \boldsymbol {d} ^ {\mathrm{T}} \hat {\Sigma} ^ {- 1} \boldsymbol {d}\right), \quad \boldsymbol {d} = \bar {\boldsymbol {X}} - \boldsymbol {\mu} _ {0}.
$$

7. 考虑 $X \sim N_3(\mu, \Sigma)$. 一个大小为 $n = 10$ 的独立同分布样本给出:

$$
\bar {\pmb {X}} = (1, 0, 2) ^ {\mathrm{T}} \quad \text {和} \quad \hat {\Sigma} = \left( \begin{array}{c c c} {{3}} & {{2}} & {{1}} \\ {{2}} & {{3}} & {{1}} \\ {{1}} & {{1}} & {{4}} \end{array} \right).
$$

(1) 计算  $\mu_{1}, \mu_{2}$  和  $\mu_{3}$  的同时置信区间.
(2) 我们可以断言 $\mu_{1}$ 是 $\mu_{2}$ 和 $\mu_{3}$ 的平均值吗?

8. 假设  $\boldsymbol{X} \sim N_{2}(\boldsymbol{\mu}, \Sigma)$ ，其中  $\Sigma = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ ，我们有一个大小为 n = 6 的独立同分布样本，根据其计算得到了  $\bar{\boldsymbol{X}}^{\mathrm{T}} = \left(1, \frac{1}{2}\right)$ 。解决以下检验问题 ( $\alpha = 0.05$ ):

---

习题四

205

(1) $H_0: \boldsymbol{\mu} = \left(2, \frac{2}{3}\right)^{\mathrm{T}} \leftrightarrow H_1: \boldsymbol{\mu} \neq \left(2, \frac{2}{3}\right)^{\mathrm{T}}$.
(2) $H_0: \mu_1 + \mu_2 = \frac{7}{2} \leftrightarrow H_1: \mu_1 + \mu_2 \neq \frac{7}{2}$.
(3) $H_0: \mu_1 - \mu_2 = \frac{1}{2} \leftrightarrow H_1: \mu_1 - \mu_2 \neq \frac{1}{2}$.
(4) $H_0: \mu_1 = 2 \leftrightarrow H_1: \mu_1 \neq 2$.

对于每一种情况, 计算拒绝域.

9. 同习题 8 的设定, 但  $\Sigma$  未知且样本协方差矩阵为  $\hat{\Sigma} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ , 比较结果.

10. 考虑来自两个二元正态总体的两个独立的同分布样本, 每个样本大小为 10, 从样本计算的结果如下:

$$
\bar {\boldsymbol {X}} _ {1} = (3, 1) ^ {\mathrm{T}}; \quad \bar {\boldsymbol {X}} _ {2} = (1, 1) ^ {\mathrm{T}};
$$

$$
\hat {\Sigma} _ {1} = \left( \begin{array}{c c} 4 & - 1 \\ - 1 & 2 \end{array} \right); \quad \hat {\Sigma} _ {2} = \left( \begin{array}{c c} 2 & - 2 \\ - 2 & 4 \end{array} \right).
$$

对以下假设检验提供解决方案:

(1) $H_0: \mu_1 = \mu_2 \leftrightarrow H_1: \mu_1 \neq \mu_2$.
(2) $H_0: \mu_{11} = \mu_{21} \leftrightarrow H_1: \mu_{11} \neq \mu_{21}$.
(3) $H_0: \mu_{12} = \mu_{22} \leftrightarrow H_1: \mu_{12} \neq \mu_{22}$.

比较这些解决方案.

11. 假设  $X \sim N_{p}(\boldsymbol{\mu}, \Sigma)$ ，其中  $\Sigma$  未知.

(1) 导出用于检验 p 个分量是否独立的对数似然比检验, 即  $H_{0}: \Sigma$  是对角矩阵.
(2) 假设 $\Sigma$ 是对角矩阵 (所有变量都是独立的). 能否导出针对 $H_0: \mu = \mu_0$ 的对立假设 $H_1: \mu \neq \mu_0$ 的渐近检验? 这与对每个 $\mu_j$ 进行的 $p$ 个独立的单变量 $t$ 检验相比如何?
(3) 提供一个检验 p 个均值相等的渐近检验的简易导出方法. 将此与简单的方差分析 (ANOVA) 比较.

12. Olkin (奥尔金) 和 Vaeth (维斯) (1981) 观察了在一天中三个不同时间点, 遵循不同饮食的两组患者的血浆柠檬酸浓度的变化. (患者在平衡设计下随机分配到每组, $n_1 = n_2 = 5$). 数据集在表 4.1 中给出, 检验两组的血浆柠檬酸浓度曲线是否平行变化.

13. 在 30 个地块中测量小麦产量, 这些地块随机分配给三个使用三种不同肥料 A, B 和 C 处理的批次. 数据集在表 4.2 中给出, 利用习题 11, 完成以下要求:

(1) 测试三列数据之间的独立性.
(2) 检验  $\boldsymbol{\mu}=(2,6,4)^{\mathrm{T}}$  并将此与三个单变量 t 检验进行比较.

---

206

第四章 多元模型

(3) 使用简单的方差分析 (ANOVA) 和  $\chi^{2}$  近似测试是否  $\mu_{1} = \mu_{2} = \mu_{3}$ .

表 4.1 血浆柠檬酸浓度

<table><tr><td>组别</td><td>8:00</td><td>11:00</td><td>15:00</td></tr><tr><td rowspan="5">I</td><td>125</td><td>137</td><td>121</td></tr><tr><td>144</td><td>173</td><td>147</td></tr><tr><td>105</td><td>119</td><td>125</td></tr><tr><td>151</td><td>149</td><td>128</td></tr><tr><td>137</td><td>139</td><td>109</td></tr><tr><td rowspan="5">II</td><td>93</td><td>121</td><td>107</td></tr><tr><td>116</td><td>135</td><td>106</td></tr><tr><td>109</td><td>83</td><td>100</td></tr><tr><td>89</td><td>95</td><td>83</td></tr><tr><td>116</td><td>128</td><td>100</td></tr></table>

表 4.2 小麦产量

| 肥料 A | 肥料 B | 肥料 C |
| --- | --- | --- |
| 4 | 6 | 2 |
| 3 | 7 | 1 |
| 2 | 7 | 1 |
| 5 | 5 | 1 |
| 4 | 5 | 3 |
| 4 | 5 | 4 |
| 3 | 8 | 3 |
| 3 | 9 | 3 |
| 3 | 9 | 2 |
| 1 | 6 | 2 |

14. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $N_{p}(\boldsymbol{\mu}, \Sigma)$  的独立同分布样本, 其中

$$
\Sigma = \sigma^ {2} \left( \begin{array}{c c c c} 1 & \rho & \dots & \rho \\ \rho & 1 & \dots & \rho \\ \vdots & \vdots & & \vdots \\ \rho & \rho & \dots & 1 \end{array} \right).
$$

令 $Q_{H} = \sum_{j = 1}^{p}\left(\bar{X}_{.j} - \bar{X}_{..}\right)^{2},Q_{E} = \sum_{i = 1}^{n}\sum_{j = 1}^{p}\left(X_{ij} - \bar{X}_{i.} - \bar{X}_{.j} + \bar{X}_{..}\right)^{2}$ ，其中 $X_{ij}$ 为

---

习题四

207

$X_{i}$  的第 j 个元素.证明:检验  $H_{0}:\mu_{1}=\mu_{2}=\cdots=\mu_{p}$  可用统计量  $F=(n-1)Q_{H}/Q_{E}$ ，当  $H_{0}$  为真时  $F\sim F(p-1,(n-1)(p-1))$ .

15. 表 4.3 的数据为 38 个人的体重和身高, 试检验假设  $H_{0} : \boldsymbol{\mu} = (63.64, 1615.38)^{\mathrm{T}}$ .

表 4.3 体重、身高数据

| 体重/kg | 71.0 | 56.5 | 56.0 | 61.0 | 65.0 | 62.0 | 53.0 | 53.0 | 65.0 | 71.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 身高/mm | 1 629 | 1 569 | 1 561 | 1 619 | 1 566 | 1 639 | 1 494 | 1 568 | 1 610 | 1 572 |
| 体重/kg | 65.0 | 57.0 | 66.5 | 59.1 | 64.0 | 69.5 | 64.0 | 56.5 | 60.2 | 55.0 |
| 身高/mm | 1 540 | 1 530 | 1 622 | 1 486 | 1 578 | 1 645 | 1 648 | 1 521 | 1 534 | 1 536 |
| 体重/kg | 57.0 | 55.0 | 57.0 | 58.0 | 59.5 | 61.0 | 57.0 | 57.5 | 70.0 | 64.0 |
| 身高/mm | 1 547 | 1 505 | 1 473 | 1 538 | 1 513 | 1 653 | 1 566 | 1 580 | 1 630 | 1 640 |
| 体重/kg | 74.0 | 72.0 | 62.5 | 68.0 | 63.4 | 68.0 | 69.0 | 73.0 |  |  |
| 身高/mm | 1 647 | 1 620 | 1 637 | 1 528 | 1 647 | 1 605 | 1 625 | 1 615 |  |  |

16. (1) 测量了 35 只雌性青蛙的头骨长和宽的数据后, 得到下面的统计量:

$$
\bar {\boldsymbol {X}} = \binom{2 2. 8 6 0}{2 4. 3 9 7}, \quad S _ {1} = \left( \begin{array}{c c} 1 7. 1 7 8 & 1 9. 7 1 0 \\ 1 9. 7 1 0 & 2 3. 7 1 0 \end{array} \right),
$$

检验假设  $H_{0}:\mu_{1}=\mu_{2}.$

(2) 对 14 只雄性青蛙进行同样的测量得到统计量

$$
\bar {\boldsymbol {X}} = \binom{2 1. 8 2 1}{2 2. 8 4 3}, \quad S _ {2} = \left( \begin{array}{c c} 1 7. 1 5 9 & 1 7. 7 3 1 \\ 1 7. 7 3 1 & 1 9. 2 7 3 \end{array} \right),
$$

检验假设  $H_{0}:\mu_{1}=\mu_{2}$ .

(3) 求上面数据综合起来后的协方差矩阵，并检验雄性和雌性青蛙是否相同 $(\mu_{1}=\mu_{2})$ .

17. 为了研究某城市男性高中学生吸烟问题, 随机抽取了 300 名高中男生, 调查每天吸烟量, 结果如表 4.4 所示.

表 4.4 吸烟数据

| 吸烟量 | 不吸烟 | 少量 (1~4支) | 中等 (5~10支) | 严重 (10支以上) |
| --- | --- | --- | --- | --- |
| 人数 | 168 | 85 | 30 | 17 |

试对这四种情况的人的比例 $p_i, i = 1,2,3,4, \sum_{i=1}^{4} p_i = 1$, 作出 $95\%$ 的联立置信区间.

---

208

第四章 多元模型

18. 在地质勘探中, 在三个不同的地区 (A, B 和 C) 采集了一些岩石, 测得它们的化学成分如表 4.5 所示.

表 4.5 岩石化学成分数据

<table><tr><td colspan="3">A</td><td colspan="3">B</td><td colspan="3">C</td></tr><tr><td> $SiO_2$ </td><td>FeO</td><td> $K_2O$ </td><td> $SiO_2$ </td><td>FeO</td><td> $K_2O$ </td><td> $SiO_2$ </td><td>FeO</td><td> $K_2O$ </td></tr><tr><td>47.22</td><td>5.06</td><td>0.10</td><td>54.33</td><td>6.22</td><td>0.12</td><td>43.12</td><td>10.33</td><td>0.05</td></tr><tr><td>47.45</td><td>4.35</td><td>0.15</td><td>56.17</td><td>3.31</td><td>0.15</td><td>42.05</td><td>9.67</td><td>0.08</td></tr><tr><td>47.52</td><td>6.85</td><td>0.12</td><td>48.40</td><td>2.43</td><td>0.22</td><td>42.50</td><td>9.62</td><td>0.02</td></tr><tr><td>47.86</td><td>4.19</td><td>0.17</td><td>52.62</td><td>5.92</td><td>0.12</td><td>40.77</td><td>9.68</td><td>0.04</td></tr><tr><td>47.31</td><td>7.57</td><td>0.18</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

假定这三个地区岩石的三个成分服从  $N_{3}\left(\boldsymbol{\mu}_{i},\Sigma_{i}\right), i=1,2,3.$

(1) 检验  $H_{0}:\Sigma_{1}=\Sigma_{2}=\Sigma_{3}\leftrightarrow H_{1}$  : 存在  $i\neq j$  使  $\Sigma_{i}\neq\Sigma_{j}$ .
(2) 检验  $H_{0}:\mu_{1}=\mu_{2}\leftrightarrow H_{1}:\mu_{1}\neq\mu_{2}.$
(3) 检验  $H_{0}:\mu_{1}=\mu_{2}=\mu_{3}\leftrightarrow H_{1}$ : 存在  $i\neq j$  使  $\mu_{i}\neq\mu_{j}$ .
(4) 给出  $\mu_{1}-\mu_{2}$  的置信区间.

19. 设  $\boldsymbol{X} = (\boldsymbol{X}_{1}, \boldsymbol{X}_{2}, \cdots, \boldsymbol{X}_{n})$  为来自总体  $N_{p}(\boldsymbol{\mu}, \Sigma)$  的独立同分布样本， $\Sigma$  正定并未知，p = 2k. 设  $\boldsymbol{\mu} = \left(\boldsymbol{\mu}_{(1)}^{\mathrm{T}}, \boldsymbol{\mu}_{(2)}^{\mathrm{T}}\right)^{\mathrm{T}}$ ,  $\boldsymbol{\mu}_{(i)}^{\mathrm{T}}$  的维数为 k. 试导出检验假设  $H_{0}: \boldsymbol{\mu}_{(1)}^{\mathrm{T}} = \boldsymbol{\mu}_{(2)}^{\mathrm{T}}$  的 LRT 统计量和分布.
20. 设 X 为来自  $N_{p}(\boldsymbol{\mu}, \sigma^{2}I_{p})$  的观测, 其中  $\sigma^{2}$  已知, 试基于这一观测求出检验假设  $H_{0}: \boldsymbol{\mu}^{T}\boldsymbol{\mu}=1$  的 LRT 统计量.
21. 为了判断两个不同产地的鸢尾花是否属于一个种, 各取 50 个样品测量了 $X_{1} =$ 花的萼片长, $X_{2} =$ 花的萼片宽, $X_{3} =$ 花瓣长, $X_{4} =$ 花瓣宽, 希望比较这些形态上的差异是否显著, 作为一个分类的依据, 由测得的数据算得两地的样本均值向量为

$$
\bar {\boldsymbol {X}} ^ {(1)} = (5. 9 3 6, 2. 7 7 0, 4. 2 6 0, 1. 3 2 8) ^ {\mathrm{T}}, \quad \bar {\boldsymbol {X}} ^ {(2)} = (5. 0 0 6, 3. 4 2 8, 1. 4 6 2, 0. 2 4 6) ^ {\mathrm{T}}
$$

及样本协方差矩阵为

$$
\begin{array}{l} \hat {\Sigma} _ {1} = \sum_ {i = 1} ^ {5 0} \left[ \boldsymbol {X} _ {i} ^ {(1)} - \bar {\boldsymbol {X}} ^ {(1)} \right] \left[ \boldsymbol {X} _ {i} ^ {(1)} - \bar {\boldsymbol {X}} ^ {(1)} \right] ^ {\mathrm{T}} \\ = \left( \begin{array}{c c c c} 9. 6 0 1 2 & & & \\ 5. 0 0 6 7 & 5. 8 8 2 3 & & \\ 4. 7 6 5 4 & 2. 8 0 1 1 & 6. 1 9 1 9 & \\ 1. 8 0 1 1 & 1. 3 0 2 5 & 1. 9 0 2 6 & 1. 3 1 1 8 \end{array} \right), \\ \end{array}
$$

---

习题四

209

$$
\begin{array}{l} \hat {\Sigma} _ {2} = \sum_ {i = 1} ^ {5 0} \left[ \boldsymbol {X} _ {i} ^ {(2)} - \bar {\boldsymbol {X}} ^ {(2)} \right] \left[ \boldsymbol {X} _ {i} ^ {(2)} - \bar {\boldsymbol {X}} ^ {(2)} \right] ^ {\mathrm{T}} \\ = \left( \begin{array}{c c c c} 9. 5 4 2 2 & & & \\ 4. 9 2 8 9 & 5. 9 8 3 5 & & \\ 4. 9 9 8 0 & 1. 8 2 3 1 & 6. 1 0 5 9 & \\ 1. 4 3 8 3 & 1. 1 7 2 1 & 1. 9 7 6 8 & 1. 1 4 8 6 \end{array} \right). \\ \end{array}
$$

(1) 设两种鸢尾花形态的协方差矩阵相等, 对于  $\alpha = 0.05$ , 判断两地鸢尾花形态均值向量是否有显著差异.
(2) 检验两地的鸢尾花形态的协方差矩阵是否相等 ( $\alpha = 0.05$ ).

22. 设  $X_{i}, i = 1, 2, \cdots, n (n > p)$  为总体  $N_{p}(\boldsymbol{\mu}, \Sigma)$ , ( $\Sigma$  正定,  $\mu, \Sigma$  都未知) 的独立同分布样本, 试证明检验假设

$$
H _ {0}: \Sigma = \mathrm{diag} \left\{\sigma_ {1 1}, \sigma_ {2 2}, \dots , \sigma_ {p p} \right\} \leftrightarrow H _ {1}: \Sigma \neq \mathrm{diag} \left\{\sigma_ {1 1}, \sigma_ {2 2}, \dots , \sigma_ {p p} \right\}
$$

的似然比统计量为  $\lambda = |R|^{n/2}$ ，其中 R 为样本相关系数.

23. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体  $N_{d}(\boldsymbol{\mu}, \Sigma)$  的独立同分布样本,  $d \leqslant n - 1$ , 设  $H_{0}$  为线性假设  $\mu \in V$ , 其中 V 为 d 维 Euclid 空间的一个 p 维子空间, 证明当  $H_{0}$  成立时有

$$
\min _ {\boldsymbol {\mu} \in V} n (\bar {\boldsymbol {X}} - \boldsymbol {\mu}) ^ {\mathrm{T}} S ^ {- 1} (\bar {\boldsymbol {X}} - \boldsymbol {\mu}) \sim T ^ {2} (d - p, n - 1).
$$

---


