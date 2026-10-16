$$
= \frac {1}{n - 1} \left[ \sum_ {i = 1} ^ {n} (\sigma^ {2} + \mu^ {2}) - n (\sigma^ {2} / n + \mu^ {2}) \right] = \sigma^ {2},
$$

即 $E(S^2) = \sigma^2.$ (3.20)

进而，设总体 $X \sim N(\mu, \sigma^2)$，由第四章 §2 的(2.8)式知 $\overline{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$ 也服从正态分布，于是得到以下的定理:

定理 2 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自正态总体  $N(\mu, \sigma^{2})$  的样本， $\overline{X}$  是样本均值，则有

$$
\overline {{X}} \sim N (\mu , \sigma^ {2} / n).
$$

对于正态总体 $N(\mu, \sigma^2)$ 的样本均值 $\overline{X}$ 和样本方差 $S^2$，有以下两个重要定理.

定理 3 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自总体  $N(\mu, \sigma^{2})$  的样本， $\overline{X}, S^{2}$  分别是样本均值和样本方差，则有

$$
1 ^ {\circ} \frac {(n - 1) S ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n - 1). \tag {3.21}
$$

$2^{\circ}$   $\overline{X}$ 与 $S^{2}$ 相互独立.

定理 3 的证明见本章末二维码.

定理 4 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自总体  $N(\mu, \sigma^{2})$  的样本， $\overline{X}, S^{2}$  分别是样本均值和样本方差，则有

$$
\frac {\overline {{X}} - \mu}{S / \sqrt {n}} \sim t (n - 1). \tag {3.22}
$$

证 由定理2、定理3，

$$
\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} \sim N (0, 1), \quad \frac {(n - 1) S ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n - 1),
$$

且两者独立. 由 $t$ 分布的定义知

$$
\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} \Bigg | \sqrt {\frac {(n - 1) S ^ {2}}{\sigma^ {2} (n - 1)}} \sim t (n - 1).
$$

化简上式左边,即得(3.22)式.

对于两个正态总体的样本均值和样本方差有以下的定理.

定理 5 设  $X_{1}, X_{2}, \cdots, X_{n_{1}}$  与  $Y_{1}, Y_{2}, \cdots, Y_{n_{2}}$  分别是来自正态总体  $N(\mu_{1}, \sigma_{1}^{2})$  和  $N(\mu_{2}, \sigma_{2}^{2})$  的样本，且这两个样本相互独立 $^{①}$ . 设  $\overline{X} = \frac{1}{n_{1}} \sum_{i=1}^{n_{1}} X_{i}, \overline{Y} = \frac{1}{n_{2}} \sum_{i=1}^{n_{2}} Y_{i}$  分别是这两个样本的样本均值； $S_{1}^{2} = \frac{1}{n_{1} - 1}\sum_{i = 1}^{n_{1}}(X_{i} - \overline{X})^{2},S_{2}^{2} = \frac{1}{n_{2} - 1}\sum_{i = 1}^{n_{2}}(Y_{i} - \overline{Y})^{2}$ 分别是这两个样本的样本方差，则有

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 这里指随机向量 $(X_{1},X_{2},\cdots,X_{n_{1}})$ 与 $(Y_{1},Y_{2},\cdots,Y_{n_{2}})$ 相互独立.</span></small>

$$
1 ^ {\circ} \frac {S _ {1} ^ {2} / S _ {2} ^ {2}}{\sigma_ {1} ^ {2} / \sigma_ {2} ^ {2}} \sim F (n _ {1} - 1, n _ {2} - 1).
$$

$2^{\circ}$ 当 $\sigma_1^2 = \sigma_2^2 = \sigma^2$ 时，

$$
\frac {(\overline {{X}} - \overline {{Y}}) - (\mu_ {1} - \mu_ {2})}{S _ {\mathrm{w}} \sqrt {\frac {1}{n _ {1}} + \frac {1}{n _ {2}}}} \sim t (n _ {1} + n _ {2} - 2),
$$

其中 $S_{\mathrm{W}}^{2} = \frac{(n_{1} - 1)S_{1}^{2} + (n_{2} - 1)S_{2}^{2}}{n_{1} + n_{2} - 2},\quad S_{\mathrm{W}} = \sqrt{S_{\mathrm{W}}^{2}}.$

证 $1^{\circ}$ 由定理3，

$$
\frac {(n _ {1} - 1) S _ {1} ^ {2}}{\sigma_ {1} ^ {2}} \sim \chi^ {2} (n _ {1} - 1), \quad \frac {(n _ {2} - 1) S _ {2} ^ {2}}{\sigma_ {2} ^ {2}} \sim \chi^ {2} (n _ {2} - 1).
$$

由假设 $S_1^2, S_2^2$ 相互独立，则由 $F$ 分布的定义知

$$
\frac {(n _ {1} - 1) S _ {1} ^ {2}}{(n _ {1} - 1) \sigma_ {1} ^ {2}} \Bigg / \frac {(n _ {2} - 1) S _ {2} ^ {2}}{(n _ {2} - 1) \sigma_ {2} ^ {2}} \sim F (n _ {1} - 1, n _ {2} - 1),
$$

即 $\frac{S_1^2 / S_2^2}{\sigma_1^2 / \sigma_2^2} \sim F(n_1 - 1, n_2 - 1)$.

$2^{\circ}$ 易知 $\overline{X} -\overline{Y}\sim N\left(\mu_{1} - \mu_{2},\frac{\sigma^{2}}{n_{1}} +\frac{\sigma^{2}}{n_{2}}\right)$ ，即有

$$
U = \frac {(\overline {{X}} - \overline {{Y}}) - (\mu_ {1} - \mu_ {2})}{\sigma \sqrt {\frac {1}{n _ {1}} + \frac {1}{n _ {2}}}} \sim N (0, 1).
$$

又由给定条件知

$$
\frac {(n _ {1} - 1) S _ {1} ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n _ {1} - 1), \quad \frac {(n _ {2} - 1) S _ {2} ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n _ {2} - 1),
$$

且它们相互独立,故由  $\chi^{2}$  分布的可加性知

$$
V = \frac {(n _ {1} - 1) S _ {1} ^ {2}}{\sigma^ {2}} + \frac {(n _ {2} - 1) S _ {2} ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n _ {1} + n _ {2} - 2).
$$

由本章末所附“§3定理3的证明及其推广”的 $2^{\circ}$ 知 $U$ 与 $V$ 相互独立.从而按 $t$ 分布的定义知

$$
\frac {U}{\sqrt {V / (n _ {1} + n _ {2} - 2)}} = \frac {(\overline {{X}} - \overline {{Y}}) - (\mu_ {1} - \mu_ {2})}{S _ {\mathrm{w}} \sqrt {\frac {1}{n _ {1}} + \frac {1}{n _ {2}}}} \sim t (n _ {1} + n _ {2} - 2).
$$

本节所介绍的几个分布以及后四个定理,在下面各章中都起着重要的作用.应注意,它们都是在总体为正态总体这一基本假定下得到的.

## 小结

在数理统计中往往研究有关对象的某一项数量指标.对这一数量指标进行试验或观察，将试验的全部可能的观察值称为总体，每个观察值称为个体.总体中的每一个个体是某一随机变量 $X$ 的值，因此一个总体对应一个随机变量 $X$.我们将不区分总体与相应的随机变量 $X$，笼统称为总体 $X$.随机变量 $X$ 服从什么分布，就称总体服从什么分布.在实际中遇到的总体往往是有限总体，它对应一个离散型随机变量.当总体中包含的个体的个数很大时，在理论上可以认为它是一个无限总体.我们说某种型号的灯泡寿命总体服从指数分布，是指无限总体而言的.又如我们说某一年龄段的男性儿童的身高服从正态分布，也是指无限总体而言的.无限总体是人们对具体事物的抽象.无限总体的分布的形式较为简明，便于在数学上进行处理，使用方便.

在相同的条件下,对总体 X 进行 n 次重复的、独立的观察,得到 n 个结果  $X_{1}, X_{2}, \cdots, X_{n}$ , 称随机变量  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体 X 的简单随机样本,它具有两条性质:

$1^{\circ} X_{1}, X_{2}, \cdots, X_{n}$ 都与总体具有相同的分布.

$2^{\circ} X_{1}, X_{2}, \cdots, X_{n}$ 相互独立.

我们就是利用来自样本的信息推断总体,得到有关总体分布的种种结论的.

样本  $X_{1}, X_{2}, \cdots, X_{n}$  的函数  $g(X_{1}, X_{2}, \cdots, X_{n})$ ，若不包含未知参数，则称为统计量.统计量是一个随机变量，它是完全由样本所确定的.统计量是进行统计推断的工具.样本均值

$$
\overline {{X}} = \frac {1}{n} \sum_ {k = 1} ^ {n} X _ {k}
$$

和样本方差

$$
S ^ {2} = \frac {1}{n - 1} \sum_ {k = 1} ^ {n} (X _ {k} - \overline {{X}}) ^ {2}
$$

是两个最重要的统计量.统计量的分布称为抽样分布.下面是三个来自正态分布的抽样分布:

$\chi^{2}$  分布，t 分布，F 分布.

这三个分布称为统计学的三大分布,它们在数理统计中有着广泛的应用.对于这三个分布,要求读者掌握它们的定义和概率密度函数图形的轮廓,还会使用分位数表写出分位数.

关于样本均值  $\overline{X}$ 、样本方差  $S^{2}$ ，有以下的结果。

1. 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自总体 X（不管服从什么分布，只要它的均值和方差存在）的样本，且有  $E(X) = \mu, D(X) = \sigma^{2}$ ，则有

$$
E (\overline {{X}}) = \mu , \quad D (\overline {{X}}) = \sigma^ {2} / n.
$$

2. 设总体  $X \sim N(\mu, \sigma^{2})$ ,  $X_{1}, X_{2}, \cdots, X_{n}$  是来自 X 的样本，则有

$1^{\circ} \overline{X} \sim N(\mu, \sigma^{2}/n)$.
$2^{\circ}\frac{(n - 1)S^{2}}{\sigma^{2}}\sim \chi^{2}(n - 1).$

$3^{\circ} \overline{X}$  与  $S^{2}$  相互独立.

$4^{\circ}\frac{\overline{X} - \mu}{S / \sqrt{n}}\sim t(n - 1).$

3. 对于两个正态总体 $X \sim N(\mu_1, \sigma_1^2), Y \sim N(\mu_2, \sigma_2^2)$，有 §3 定理 5 的重要结果。

## ■ 重要术语及主题

总体 简单随机样本 统计量

$\chi^{2}$  分布、t 分布、F 分布的定义及它们的概率密度函数图形轮廓

上 $\alpha$ 分位数 $F_{1 - \alpha}(n_1,n_2) = \frac{1}{F_\alpha(n_2,n_1)}$

小结中关于样本均值、样本方差的重要结果

## 习题

1. 在总体 $N(52,6.3^2)$ 中随机抽取一容量为36的样本，求样本均值 $\overline{X}$ 落在50.8到53.8之间的概率.

2. 在总体 $N(12,4)$ 中随机抽一容量为5的样本 $X_{1}, X_{2}, X_{3}, X_{4}, X_{5}$.

(1) 求样本均值与总体均值之差的绝对值大于 1 的概率.

(2) 求概率  $P\{\max\{X_{1}, X_{2}, X_{3}, X_{4}, X_{5}\} > 15\}$ ,  $P\{\min\{X_{1}, X_{2}, X_{3}, X_{4}, X_{5}\} < 10\}$ .

3. 求总体 $N(20,3)$ 的容量分别为 10, 15 的两独立样本均值差的绝对值大于 0.3 的概率.

4.（1）设样本  $X_{1}, X_{2}, \cdots, X_{6}$  来自总体  $N(0,1), Y = (X_{1} + X_{2} + X_{3})^{2} + (X_{4} + X_{5} + X_{6})^{2}$ ，试确定常数 C 使 CY 服从  $\chi^{2}$  分布.

(2) 设样本  $X_{1}, X_{2}, \cdots, X_{5}$  来自总体  $N(0,1), Y = \frac{C(X_{1} + X_{2})}{(X_{3}^{2} + X_{4}^{2} + X_{5}^{2})^{1/2}}$ ，试确定常数 C 使 Y 服从 t 分布.

(3) 已知总体  $X \sim t(n)$ ，求证  $X^{2} \sim F(1, n)$ .

5.（1）已知某种能力测试的得分服从正态分布 $N(\mu, \sigma^2)$，随机取10个人参与这一测试。求他们得分的联合概率密度，并求这10个人得分的平均值小于 $\mu$ 的概率。

(2) 在(1)中设  $\mu=62,\sigma^{2}=25$ ，若得分超过70就能得奖，求至少有一人得奖的概率.

6. 设总体  $X \sim b(1, p)$ ,  $X_{1}, X_{2}, \cdots, X_{n}$  是来自 X 的样本.

(1) 求 $(X_{1}, X_{2}, \cdots, X_{n})$ 的分布律.

(2) 求  $\sum_{i=1}^{n} X_{i}$  的分布律.

(3) 求  $E(\overline{X})$ ,  $D(\overline{X})$ ,  $E(S^{2})$ .

7. 设总体  $X \sim \chi^{2}(n)$ ,  $X_{1}, X_{2}, \cdots, X_{10}$  是来自 X 的样本，求  $E(\overline{X}), D(\overline{X}), E(S^{2})$ .

8. 设总体  $X \sim N(\mu, \sigma^{2})$ ,  $X_{1}, X_{2}, \cdots, X_{10}$  是来自 X 的样本.

(1) 写出  $X_{1}, X_{2}, \cdots, X_{10}$  的联合概率密度.

(2) 写出  $\overline{X}$  的概率密度.

9. 设在总体  $N(\mu,\sigma^{2})$  中抽得一容量为 16 的样本, 这里  $\mu,\sigma^{2}$  均未知.

(1) 求  $P\{S^{2}/\sigma^{2}\leqslant2.041\}$ ，其中  $S^{2}$  为样本方差.

(2) 求  $D(S^{2})$ .

10. 下面列出了 30 个美国 NBA 球员的体重(以磅计, 1 磅 = 0.454 kg) 数据. 这些数据是从美国 NBA 球队 1990—1991 年赛季的花名册中抽样得到的.

| 225 | 232 | 232 | 245 | 235 | 245 | 270 | 225 | 240 | 240 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 217 | 195 | 225 | 185 | 200 | 220 | 200 | 210 | 271 | 240 |
| 220 | 230 | 215 | 252 | 225 | 220 | 206 | 185 | 227 | 236 |

(1) 画出这些数据的频率直方图(提示: 最大和最小观察值分别为 271 和 185, 区间 [184.5, 271.5] 包含所有数据, 将整个区间分为 5 等份, 为计算方便, 将区间调整为 (179.5, 279.5).

(2) 作出这些数据的箱线图.

11. 截尾均值 设数据集包含 $n$ 个数据, 将这些数据自小到大排序为

$$
x _ {(1)} \leqslant x _ {(2)} \leqslant \dots \leqslant x _ {(n)},
$$

删去 $100\alpha \%$ 个数值小的数，同时删去 $100\alpha \%$ 个数值大的数，将留下的数据取算术平均，记为 $\bar{x}_{\alpha}$，即

$$
\bar {x} _ {\alpha} = \frac {x _ {([ n \alpha ] + 1)} + \cdots + x _ {(n - [ n \alpha ])}}{n - 2 [ n \alpha ]}
$$

其中 $[n\alpha]$ 是小于或等于 $n\alpha$ 的最大整数（一般取 $\alpha$ 为 $0.1\sim 0.2)$。$x_{\alpha}$ 称为 $100\alpha \%$ 截尾均值。例如对于第10题中的30个数据，取 $\alpha = 0.1$，则有 $[n\alpha] = [30\times 0.1] = 3$，得 $100\times 0.1\%$ 截尾均值为

$$
\bar {x} _ {\alpha} = \frac {2 0 0 + 2 0 0 + \cdots + 2 4 5 + 2 4 5}{3 0 - 6} = 2 2 5. 4 1 6 7.
$$

若数据来自某一总体的样本, 则  $\bar{x}_{\alpha}$  是一个统计量.  $\bar{x}_{\alpha}$  不受样本的极端值的影响. 截尾均值在实际应用问题中是常会用到的.

试求第10题的30个数据的 $\alpha = 0.2$ 的截尾均值.

![](images/page_164_image_14.jpg)

§ 3 定理 3 的

证明及其推广

## 第七章 参数估计

统计推断的基本问题可以分为两大类,一类是估计问题,另一类是假设检验问题.本章讨论总体参数的点估计和区间估计.

## §1 点 估 计

设总体 $X$ 的分布函数的形式已知，但它的一个或多个参数未知，借助于总体 $X$ 的一个样本来估计总体未知参数的值的问题称为参数的点估计问题.

例1 在某炸药制造厂, 一天中发生着火现象的次数 $X$ 是一个随机变量, 假设它服从以 $\lambda > 0$ 为参数的泊松分布, 参数 $\lambda$ 为未知. 现有以下的样本值, 试估计参数 $\lambda$.

| 着火次数k | 0 | 1 | 2 | 3 | 4 | 5 | 6 | ≥7 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 发生k次着火的天数$n_k$ | 75 | 90 | 54 | 22 | 6 | 2 | 1 | 0 | Σ=250 |

解 由于 $X \sim \pi(\lambda)$, 故有 $\lambda = E(X)$. 我们自然想到用样本均值来估计总体的均值 $E(X)$. 现由已知数据计算得到

$$
\bar {x} = \frac {\sum_ {k = 0} ^ {6} k n _ {k}}{\sum_ {k = 0} ^ {6} n _ {k}} = \frac {1}{2 5 0} (0 \times 7 5 + 1 \times 9 0 + 2 \times 5 4 + 3 \times 2 2 + 4 \times 6 + 5 \times 2 + 6 \times 1) = 1. 2 2,
$$

即 $E(X) = \lambda$ 的估计为1.22.

点估计问题的一般提法如下: 设总体 X 的分布函数  $F(x; \theta)^{①}$  的形式为已知,  $\theta$  是待估参数.  $X_{1}, X_{2}, \cdots, X_{n}$  是 X 的一个样本,  $x_{1}, x_{2}, \cdots, x_{n}$  是相应的一个样本值. 点估计问题就是要构造一个适当的统计量  $\hat{\theta}(X_{1}, X_{2}, \cdots, X_{n})$ , 用它的观察值  $\hat{\theta}(x_{1}, x_{2}, \cdots, x_{n})$  作为未知参数  $\theta$  的近似值. 我们称  $\hat{\theta}(X_{1}, X_{2}, \cdots, X_{n})$  为  $\theta$  的估计量,称  $\hat{\theta}(x_{1},x_{2},\cdots,x_{n})$  为  $\theta$  的估计值. 在不致混淆的情况下统称估计量和估计值为估计,并都简记为  $\hat{\theta}$ . 由于估计量是样本的函数. 因此对于不同的样本值,  $\theta$  的估计值一般是不相同的.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 多于一个未知参数时,可同样讨论.</span></small>

例如在例 1 中, 我们用样本均值来估计总体均值. 即有估计量

$$
\hat {\lambda} = \widehat {E (X)} = \frac {1}{n} \sum_ {k = 1} ^ {n} X _ {k}, \quad n = 2 5 0,
$$

估计值 $\hat{\lambda} = E(\widehat{X}) = \frac{1}{n}\sum_{k = 1}^{n}x_{k} = 1.22.$

下面介绍两种常用的构造估计量的方法: 矩估计法和最大似然估计法.

## (一) 矩估计法

设 X 为连续型随机变量, 其概率密度为  $f(x; \theta_{1}, \theta_{2}, \cdots, \theta_{k})$ , 或 X 为离散型随机变量, 其分布律为  $P\{X = x\} = p(x; \theta_{1}, \theta_{2}, \cdots, \theta_{k})$ , 其中  $\theta_{1}, \theta_{2}, \cdots, \theta_{k}$  为待估参数,  $X_{1}, X_{2}, \cdots, X_{n}$  是来自 X 的样本. 假设总体 X 的前 k 阶矩

$$
\mu_ {l} = E (X ^ {l}) = \int_ {- \infty} ^ {\infty} x ^ {l} f (x; \theta_ {1}, \theta_ {2}, \dots , \theta_ {k}) \mathrm{d} x \quad (X \text {为连续型})
$$

或 $\mu_{l} = E(X^{l}) = \sum_{x\in R_{X}}x^{l}p(x;\theta_{1},\theta_{2},\dots ,\theta_{k})$ （ $X$ 为离散型）

(其中  $R_{X}$  是 X 可能取值的范围) 存在,  $l=1,2,\cdots,k$ . 一般来说, 它们是  $\theta_{1}, \theta_{2},\cdots,\theta_{k}$  的函数. 基于样本矩

$$
A _ {l} = \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {l}
$$

依概率收敛于相应的总体矩  $\mu_{l}(l=1,2,\cdots,k)$ ，样本矩的连续函数依概率收敛于相应的总体矩的连续函数（见第六章 §3），我们就用样本矩作为相应的总体矩的估计量，而以样本矩的连续函数作为相应的总体矩的连续函数的估计量。这种估计方法称为矩估计法。矩估计法的具体做法如下:设

$$
\left\{ \begin{array}{l} \mu_ {1} = \mu_ {1} (\theta_ {1}, \theta_ {2}, \dots , \theta_ {k}), \\ \mu_ {2} = \mu_ {2} (\theta_ {1}, \theta_ {2}, \dots , \theta_ {k}), \\ \dots \dots \\ \mu_ {k} = \mu_ {k} (\theta_ {1}, \theta_ {2}, \dots , \theta_ {k}). \end{array} \right.
$$

这是一个包含 k 个未知参数  $\theta_{1}, \theta_{2}, \cdots, \theta_{k}$  的联立方程组. 一般来说, 可以从中解出  $\theta_{1}, \theta_{2}, \cdots, \theta_{k}$ , 得到

$$
\left\{ \begin{array}{l} \theta_ {1} = \theta_ {1} (\mu_ {1}, \mu_ {2}, \dots , \mu_ {k}), \\ \theta_ {2} = \theta_ {2} (\mu_ {1}, \mu_ {2}, \dots , \mu_ {k}), \\ \dots \dots \\ \theta_ {k} = \theta_ {k} (\mu_ {1}, \mu_ {2}, \dots , \mu_ {k}). \end{array} \right.
$$

以  $A_{i}$  分别代替上式中的  $\mu_{i}, i=1,2,\cdots,k$ ，就以

$$
\hat {\theta} _ {i} = \theta_ {i} (A _ {1}, A _ {2}, \dots , A _ {k}), \quad i = 1, 2, \dots , k
$$

分别作为  $\theta_{i}, i=1,2,\cdots,k$  的估计量，这种估计量称为矩估计量.矩估计量的观察值称为矩估计值.

例 2 设总体 X 在  $[a, b]$  上服从均匀分布, a, b 未知.  $X_{1}, X_{2}, \cdots, X_{n}$  是来自 X 的样本, 试求 a, b 的矩估计量.

解 $\mu_{1} = E(X) = (a + b) / 2,$

$$
\mu_ {2} = E (X ^ {2}) = D (X) + [ E (X) ] ^ {2} = (b - a) ^ {2} / 1 2 + (a + b) ^ {2} / 4.
$$

即 $\left\{ \begin{array}{l}a + b = 2\mu_1,\\ b - a = \sqrt{12(\mu_2 - \mu_1^2)}. \end{array} \right.$

解这一方程组得

$$
a = \mu_ {1} - \sqrt {3 (\mu_ {2} - \mu_ {1} ^ {2})}, b = \mu_ {1} + \sqrt {3 (\mu_ {2} - \mu_ {1} ^ {2})}.
$$

分别以 $A_{1}, A_{2}$ 代替 $\mu_{1}, \mu_{2}$, 得到 $a, b$ 的矩估计量分别为（注意到 $\frac{1}{n} \sum_{i=1}^{n} X_{i}^{2} - \overline{X}^{2} = \frac{1}{n} \sum_{i=1}^{n} (X_{i} - \overline{X})^{2}$）:

$$
\hat {a} = A _ {1} - \sqrt {3 (A _ {2} - A _ {1} ^ {2})} = \overline {{X}} - \sqrt {\frac {3}{n} \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}},
$$

$$
\hat {b} = A _ {1} + \sqrt {3 (A _ {2} - A _ {1} ^ {2})} = \overline {{X}} + \sqrt {\frac {3}{n} \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}.
$$

例 3 设总体 X 的均值  $\mu$  及方差  $\sigma^{2}$  都存在，且有  $\sigma^{2}>0$ 。但  $\mu,\sigma^{2}$  均为未知。又设  $X_{1},X_{2},\cdots,X_{n}$  是来自 X 的样本。试求  $\mu,\sigma^{2}$  的矩估计量。

解

$$
\left\{ \begin{array}{l} \mu_ {1} = E (X) = \mu , \\ \mu_ {2} = E (X ^ {2}) = D (X) + [ E (X) ] ^ {2} = \sigma^ {2} + \mu^ {2}. \end{array} \right.
$$

解得 $\left\{ \begin{array}{l}\mu = \mu_1,\\ \sigma^2 = \mu_2 - \mu_1^2. \end{array} \right.$

分别以 $A_{1}, A_{2}$ 代替 $\mu_{1}, \mu_{2}$, 得 $\mu$ 和 $\sigma^{2}$ 的矩估计量分别为

$$
\hat {\mu} = A _ {1} = \overline {{X}},
$$

$$
\hat {\sigma} ^ {2} = A _ {2} - \dot {A} _ {1} ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} ^ {2} - \overline {{{{X}}}} ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{{{X}}}}) ^ {2}.
$$

所得结果表明,总体均值与方差的矩估计量的表达式不因不同的总体分布而异.

例如， $X\sim N(\mu ,\sigma^2),\mu ,\sigma^2$ 未知，即得 $\mu ,\sigma^2$ 的矩估计量为

$$
\hat {\mu} = \overline {{X}}, \quad \hat {\sigma} ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}.
$$

## (二) 最大似然估计法

若总体 X 属离散型, 其分布律  $P\{X=x\}=p(x;\theta), \theta\in\Theta$  的形式为已知,  $\theta$  为待估参数,  $\Theta$  是  $\theta$  可能取值的范围. 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自 X 的样本, 则  $X_{1}, X_{2}, \cdots, X_{n}$  的联合分布律为

$$
\prod_ {i = 1} ^ {n} p (x _ {i}; \theta).
$$

又设  $x_{1}, x_{2}, \cdots, x_{n}$  是相应于样本  $X_{1}, X_{2}, \cdots, X_{n}$  的一个样本值. 易知样本  $X_{1}, X_{2}, \cdots, X_{n}$  取到观察值  $x_{1}, x_{2}, \cdots, x_{n}$  的概率, 亦即事件  $\{X_{1} = x_{1}, X_{2} = x_{2}, \cdots, X_{n} = x_{n}\}$  发生的概率为

$$
L (\theta) = L (x _ {1}, x _ {2}, \dots , x _ {n}; \theta) = \prod_ {i = 1} ^ {n} p (x _ {i}; \theta), \quad \theta \in \Theta . \tag {1.1}
$$

这一概率随  $\theta$  的取值而变化, 它是  $\theta$  的函数,  $L(\theta)$  称为样本的似然函数(注意, 这里  $x_{1}, x_{2}, \cdots, x_{n}$  是已知的样本值, 它们都是常数).

关于最大似然估计法,我们有以下的直观想法:现在已经取到样本值  $x_{1}, x_{2}, \cdots, x_{n}$  了,这表明取到这一样本值的概率  $L(\theta)$  比较大. 我们当然不会考虑那些不能使样本  $x_{1}, x_{2}, \cdots, x_{n}$  出现的  $\theta \in \Theta$  作为  $\theta$  的估计,再者,如果已知当  $\theta = \theta_{0} \in \Theta$  时使  $L(\theta)$  取很大的值,而  $\Theta$  中其他  $\theta$  的值使  $L(\theta)$  取很小的值,我们自然认为取  $\theta_{0}$  作为未知参数  $\theta$  的估计值,较为合理. 由费希尔引进的最大似然估计法,就是固定样本观察值  $x_{1}, x_{2}, \cdots, x_{n}$ ,在  $\theta$  取值的可能范围  $\Theta$  内挑选使似然函数  $L(x_{1}, x_{2}, \cdots, x_{n}; \theta)$  达到最大的参数值  $\hat{\theta}$ ,作为参数  $\theta$  的估计值. 即取  $\hat{\theta}$  使

$$
L (x _ {1}, x _ {2}, \dots , x _ {n}; \hat {\theta}) = \max _ {\theta \in \Theta} L (x _ {1}, x _ {2}, \dots , x _ {n}; \theta). \tag {1.2}
$$

这样得到的 $\hat{\theta}$ 与样本值 $x_{1},x_{2},\cdots,x_{n}$ 有关，常记为 $\hat{\theta}(x_{1},x_{2},\cdots,x_{n})$ ，称为参数 $\theta$ 的最大似然估计值，而相应的统计量 $\hat{\theta}(X_{1},X_{2},\cdots,X_{n})$ 称为参数 $\theta$ 的最大似然估计量.

若总体 X 属连续型, 其概率密度  $f(x; \theta)$ ,  $\theta \in \Theta$  的形式已知,  $\theta$  为待估参数,  $\Theta$  是  $\theta$  可能取值的范围. 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自 X 的样本, 则  $X_{1}, X_{2}, \cdots, X_{n}$  的联合

概率密度为

$$
\prod_ {i = 1} ^ {n} f (x _ {i}; \theta).
$$

设 $x_{1}, x_{2}, \cdots, x_{n}$ 是相应于样本 $X_{1}, X_{2}, \cdots, X_{n}$ 的一个样本值，则随机点 $(X_{1}, X_{2}, \cdots, X_{n})$ 落在点 $(x_{1}, x_{2}, \cdots, x_{n})$ 的邻域（边长分别为 $\mathrm{dx}_1, \mathrm{dx}_2, \cdots, \mathrm{dx}_n$ 的 $n$ 维立方体）内的概率近似地为

$$
\prod_ {i = 1} ^ {n} f (x _ {i}; \theta) \mathrm{d} x _ {i}, \tag {1.3}
$$

其值随 $\theta$ 的取值而变化.与离散型的情况一样，我们取 $\theta$ 的估计值 $\hat{\theta}$ 使概率(1.3)式取到最大值，但因子 $\prod_{i=1}^{n} \mathrm{d}x_i$ 不随 $\theta$ 而变，故只需考虑函数

$$
L (\theta) = L (x _ {1}, x _ {2}, \dots , x _ {n}; \theta) = \prod_ {i = 1} ^ {n} f (x _ {i}; \theta) \tag {1.4}
$$

的最大值. 这里 $L(\theta)$ 称为样本的似然函数. 若

$$
L (x _ {1}, x _ {2}, \dots , x _ {n}; \hat {\theta}) = \max _ {\theta \in \Theta} L (x _ {1}, x _ {2}, \dots , x _ {n}; \theta),
$$

则称 $\hat{\theta}(x_{1},x_{2},\cdots,x_{n})$ 为 $\theta$ 的最大似然估计值，称 $\hat{\theta}(X_{1},X_{2},\cdots,X_{n})$ 为 $\theta$ 的最大似然估计量.

这样,确定最大似然估计量的问题就归结为微分学中的求最大值的问题了.

在很多情形下， $p(x;\theta)$ 和 $f(x;\theta)$ 关于 $\theta$ 可微，这时 $\hat{\theta}$ 常可从方程

$$
\frac {\mathrm{d}}{\mathrm{d} \theta} L (\theta) = 0 \tag {1.5}
$$

解得①. 又因 $L(\theta)$ 与 $\ln L(\theta)$ 在同一 $\theta$ 处取到极值, 因此, $\theta$ 的最大似然估计 $\hat{\theta}$ 也可以从方程

$$
\frac {\mathrm{d}}{\mathrm{d} \theta} \ln L (\theta) = 0 \tag {1.6}
$$

求得,而从后一方程求解往往比较方便.(1.6)式称为对数似然方程.

例 4 设  $X \sim b(1, p)$ .  $X_{1}, X_{2}, \cdots, X_{n}$  是来自 X 的一个样本, 试求参数 p 的最大似然估计量.

解 设  $x_{1}, x_{2}, \cdots, x_{n}$  是相应于样本  $X_{1}, X_{2}, \cdots, X_{n}$  的一个样本值. X 的分布律为

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 这里没有提到 $L(\theta)$ 取最大值的充分条件，但对于具体的函数是容易讨论的.</span></small>

$$
P \{X = x \} = p ^ {x} (1 - p) ^ {1 - x}, \quad x = 0, 1.
$$

故似然函数为

$$
L (p) = \prod_ {i = 1} ^ {n} p ^ {x _ {i}} (1 - p) ^ {1 - x _ {i}} = p \sum_ {i = 1} ^ {n} x _ {i} (1 - p) ^ {n - \sum_ {i = 1} ^ {n} x _ {i}},
$$

而 $\ln L(p) = \left(\sum_{i=1}^{n} x_i\right) \ln p + \left(n - \sum_{i=1}^{n} x_i\right) \ln (1 - p)$,

令 $\frac{\mathrm{d}}{\mathrm{d}p}\ln L(p) = \frac{\sum_{i=1}^{n}x_i}{p} -\frac{n - \sum_{i=1}^{n}x_i}{1 - p} = 0,$

解得 $p$ 的最大似然估计值

$$
\hat {p} = \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} = \bar {x}.
$$

$p$ 的最大似然估计量为

$$
\hat {p} = \frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} = \overline {{X}}.
$$

我们看到这一估计量与相应的矩估计量是相同的.

最大似然估计法也适用于分布中含多个未知参数  $\theta_{1}, \theta_{2}, \cdots, \theta_{k}$  的情况. 这时, 似然函数 L 是这些未知参数的函数. 分别令

$$
\frac {\partial}{\partial \theta_ {i}} L = 0, i = 1, 2, \dots , k
$$

或令  $\frac{\partial}{\partial\theta_{i}}\ln L=0, i=1,2,\cdots,k.$  (1.7)

解上述由 k 个方程组成的方程组, 即可得到各未知参数  $\theta_{i}(i=1,2,\cdots,k)$  的最大似然估计值  $\hat{\theta}_{i}$ . (1.7) 式称为对数似然方程组.

例 5 设总体  $X \sim N(\mu, \sigma^{2})$ ,  $\mu, \sigma^{2}$  为未知参数,  $x_{1}, x_{2}, \cdots, x_{n}$  是来自 X 的一个样本值. 求  $\mu, \sigma^{2}$  的最大似然估计量.

解 $X$ 的概率密度为

$$
f (x; \mu , \sigma^ {2}) = \frac {1}{\sqrt {2 \pi} \sigma} \exp \left\{- \frac {1}{2 \sigma^ {2}} (x - \mu) ^ {2} \right\},
$$

似然函数为

$$
\begin{array}{l} L (\mu , \sigma^ {2}) = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi} \sigma} \exp \left\{- \frac {1}{2 \sigma^ {2}} (x _ {i} - \mu) ^ {2} \right\} \\ = (2 \pi) ^ {- n / 2} (\sigma^ {2}) ^ {- n / 2} \exp \left\{- \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} (x _ {i} - \mu) ^ {2} \right\}. \\ \end{array}
$$

而 $\ln L = -\frac{n}{2}\ln (2\pi) - \frac{n}{2}\ln \sigma^2 -\frac{1}{2\sigma^2}\sum_{i = 1}^{n}(x_i - \mu)^2.$

令 $\left\{ \begin{array}{l} \frac{\partial}{\partial \mu} \ln L = \frac{1}{\sigma^2} \left( \sum_{i=1}^{n} x_i - n\mu \right) = 0, \\ \frac{\partial}{\partial \sigma^2} \ln L = -\frac{n}{2\sigma^2} + \frac{1}{2(\sigma^2)^2} \sum_{i=1}^{n} (x_i - \mu)^2 = 0. \end{array} \right.$

由前一式解得 $\hat{\mu} = \frac{1}{n}\sum_{i = 1}^{n}x_{i} = \bar{x}$ ，代入后一式得 $\hat{\sigma}^2 = \frac{1}{n}\sum_{i = 1}^{n}(x_i - \bar{x})^2$ 因此得 $\mu$ 和 $\sigma^2$ 的最大似然估计量分别为

$$
\hat {\mu} = \overline {{X}}, \quad \hat {\sigma} ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}.
$$

它们与相应的矩估计量相同.

例 6 设总体 X 在  $[a, b]$  上服从均匀分布，a, b 未知， $x_{1}, x_{2}, \cdots, x_{n}$  是一个样本值。试求 a, b 的最大似然估计量。

解 记  $x_{(1)}=\min\{x_{1},x_{2},\cdots,x_{n}\},x_{(n)}=\max\{x_{1},x_{2},\cdots,x_{n}\}.X$  的概率密度是

$$
f (x; a, b) = \left\{ \begin{array}{l l} { \frac {1}{b - a},} & {a \leqslant x \leqslant b,} \\ {0,} & {\text {其他}.} \end{array} \right.
$$

似然函数为

$$
L (a, b) = \left\{ \begin{array}{l l} { \frac {1}{(b - a) ^ {n}},} & {a \leqslant x _ {1}, x _ {2}, \dots , x _ {n} \leqslant b,} \\ {0,} & {\text {其他}.} \end{array} \right.
$$

由于  $a \leqslant x_{1}, x_{2}, \cdots, x_{n} \leqslant b$ ，等价于  $a \leqslant x_{(1)}, x_{(n)} \leqslant b$ 。似然函数可写成

$$
L (a, b) = \left\{ \begin{array}{l l} \frac {1}{(b - a) ^ {n}}, & a \leqslant x _ {(1)}, b \geqslant x _ {(n)}, \\ 0, & \text {其他.} \end{array} \right.
$$

于是对于满足条件 $a \leqslant x_{(1)}, b \geqslant x_{(n)}$ 的任意 $a, b$ 有

$$
L (a, b) = \frac {1}{(b - a) ^ {n}} \leqslant \frac {1}{[ x _ {(n)} - x _ {(1)} ] ^ {n}}.
$$

即 $L(a, b)$ 在 $a = x_{(1)}$, $b = x_{(n)}$ 时取到最大值 $\left[x_{(n)} - x_{(1)}\right]^{-n}$. 故 $a, b$ 的最大似然估计值为

$$
\hat {a} = x _ {(1)} = \min _ {1 \leqslant i \leqslant n} x _ {i}, \quad \hat {b} = x _ {(n)} = \max _ {1 \leqslant i \leqslant n} x _ {i}.
$$

$a, b$ 的最大似然估计量为

$$
\hat {a} = \min _ {1 \leqslant i \leqslant n} X _ {i}, \quad \hat {b} = \max _ {1 \leqslant i \leqslant n} X _ {i}.
$$

此外,最大似然估计具有下述性质:设  $\theta$  的函数  $u=u(\theta),\theta\in\Theta$  具有单值反函数  $\theta=\theta(u),u\in\mathcal{U}$ . 又假设  $\hat{\theta}$  是 X 的概率分布中参数  $\theta$  的最大似然估计,则  $\hat{u}=u(\hat{\theta})$  是  $u(\theta)$  的最大似然估计. 这一性质称为最大似然估计的不变性.

事实上，因为 $\hat{\theta}$ 是 $\theta$ 的最大似然估计，于是有

$$
L (x _ {1}, x _ {2}, \dots , x _ {n}; \hat {\theta}) = \max _ {\theta \in \Theta} L (x _ {1}, x _ {2}, \dots , x _ {n}; \theta),
$$

其中  $x_{1}, x_{2}, \cdots, x_{n}$  是 X 的一个样本值，考虑到  $\hat{u} = u(\hat{\theta})$ ，且有  $\hat{\theta} = \theta(\hat{u})$ ，上式可写成

$$
L (x _ {1}, x _ {2}, \dots , x _ {n}; \theta (\hat {u})) = \max _ {u \in \mathcal {U}} L (x _ {1}, x _ {2}, \dots , x _ {n}; \theta (u)).
$$

这就证明了 $\hat{u} = u(\hat{\theta})$ 是 $u(\theta)$ 的最大似然估计.

当总体分布中含有多个未知参数时,也具有上述性质.例如,在例5中已得到 $\sigma^{2}$ 的最大似然估计为

$$
\hat {\sigma} ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}.
$$

函数 $u = u(\sigma^2) = \sqrt{\sigma^2}$ 有单值反函数 $\sigma^2 = u^2 (u\geqslant 0)$ ，根据上述性质，得到标准差 $\sigma$ 的最大似然估计为

$$
\hat {\sigma} = \sqrt {\hat {\sigma} ^ {2}} = \sqrt {\frac {1}{n} \sum_ {i = 1} ^ {n} (X _ {i} - \overline {{X}}) ^ {2}}.
$$

我们还要提到的是,对数似然方程(1.6)或对数似然方程组(1.7)除了一些简单的情况外,往往没有有限函数形式的解,这就需要用数值方法求近似解.常用的算法是牛顿-拉弗森(Newton-Raphson)算法,对于(1.7)式有时也用拟牛顿算法,它们都是迭代算法,读者可参考有关的书籍.

## \* § 2 基于截尾样本的最大似然估计

在研究产品的可靠性时,需要研究产品寿命 T 的各种特征. 产品寿命 T 是一个随机变量,它的分布称为寿命分布. 为了对寿命分布进行统计推断,就需要通过产品的寿命试验,以取得寿命数据.

一种典型的寿命试验是，将随机抽取的 $n$ 个产品在时间 $t = 0$ 时，同时投入试验，直到每个产品都失效。记录每一个产品的失效时间，这样得到的样本（即由所有产品的失效时间 $0 \leqslant t_1 \leqslant t_2 \leqslant \dots \leqslant t_n$ 所组成的样本）称为完全样本。然而产品的寿命往往较长，由于时间和财力的限制，我们不可能得到完全样本，于是就考虑截尾寿命试验。截尾寿命试验常用的有两种:一种是定时截尾寿命试验。假设将随机抽取的 $n$ 个产品在时间 $t = 0$ 时同时投入试验，试验进行到事先规定的截尾时间 $t_0$ 停止。如试验截止时共有 $m$ 个产品失效，它们的失效时间分别为

$$
0 \leqslant t _ {1} \leqslant t _ {2} \leqslant \dots \leqslant t _ {m} \leqslant t _ {0},
$$

此时 m 是一个随机变量, 所得的样本  $t_{1}, t_{2}, \cdots, t_{m}$  称为定时截尾样本. 另一种是定数截尾寿命试验. 假设将随机抽取的 n 个产品在时间 t = 0 时同时投入试验, 试验进行到有 m 个 (m 是事先规定的, m < n) 产品失效时停止. m 个失效产品的失效时间分别为

$$
0 \leqslant t _ {1} \leqslant t _ {2} \leqslant \dots \leqslant t _ {m},
$$

这里  $t_{m}$  是第 m 个产品的失效时间， $t_{m}$  是随机变量.所得的样本  $t_{1}, t_{2}, \cdots, t_{m}$  称为定数截尾样本.用截尾样本来进行统计推断是可靠性研究中常见的问题.

设产品的寿命分布是指数分布,其概率密度为

$$
f (t) = \left\{ \begin{array}{l l} \frac {1}{\theta} \mathrm{e} ^ {- t / \theta}, & t > 0, \\ 0, & t \leqslant 0, \end{array} \right.
$$

$\theta > 0$ 未知.假设有 $n$ 个产品投入定数截尾试验，截尾数为 $m$ ，得到定数截尾样本 $0 \leqslant t_1 \leqslant t_2 \leqslant \dots \leqslant t_m$ ，现在要利用这一样本来估计未知参数 $\theta$ （即产品的平均寿命）. 在时间区间 $[0, t_m]$ 有 $m$ 个产品失效，而有 $n - m$ 个产品在 $t_m$ 时尚未失效，即有 $n - m$ 个产品的寿命超过 $t_m$ . 我们用最大似然估计法来估计 $\theta$ ，为了确定似然函数，需要知道上述观察结果出现的概率.我们知道一个产品在 $(t_i, t_i + \mathrm{d}t_i]$ 失效的概率近似地为 $f(t_i) \mathrm{d}t_i = \frac{1}{\theta} \mathrm{e}^{-t_i / \theta} \mathrm{d}t_i, i = 1,2,\dots,m$ ，其余 $n - m$ 个产品寿命超过 $t_m$ 的概率为 $\left(\int_{t_m}^{\infty} \frac{1}{\theta} \mathrm{e}^{-t / \theta} \mathrm{d}t\right)^{n - m} = (\mathrm{e}^{-t_m / \theta})^{n - m}$，故上述观察结果出现的概率近似地为

$$
\begin{array}{l} \binom {n} {m} \left(\frac {1}{\theta} \mathrm{e} ^ {- t _ {1} / \theta} \mathrm{d} t _ {1}\right) \left(\frac {1}{\theta} \mathrm{e} ^ {- t _ {2} / \theta} \mathrm{d} t _ {2}\right) \dots \left(\frac {1}{\theta} \mathrm{e} ^ {- t _ {m} / \theta} \mathrm{d} t _ {m}\right) \left(\mathrm{e} ^ {- t _ {m} / \theta}\right) ^ {n - m} \\ = \binom {n} {m} \frac {1}{\theta^ {m}} \mathrm{e} ^ {- \frac {1}{\theta} \left[ t _ {1} + t _ {2} + \dots + t _ {m} + (n - m) t _ {m} \right]} \mathrm{d} t _ {1} \mathrm{d} t _ {2} \dots \mathrm{d} t _ {m}, \\ \end{array}
$$

其中  $dt_{1}, dt_{2}, \cdots, dt_{m}$  为常数.因忽略一个常数因子不影响  $\theta$  的最大似然估计，故可取似然函数为

$$
L (\theta) = \frac {1}{\theta^ {m}} \mathrm{e} ^ {- \frac {1}{\theta} [ t _ {1} + t _ {2} + \dots + t _ {m} + (n - m) t _ {m} ]}.
$$

对数似然函数为

$$
\ln L (\theta) = - m \ln \theta - \frac {1}{\theta} [ t _ {1} + t _ {2} + \dots + t _ {m} + (n - m) t _ {m} ].
$$

令 $\frac{\mathrm{d}}{\mathrm{d}\theta}\ln L(\theta) = -\frac{m}{\theta} +\frac{1}{\theta^2}\big[t_1 + t_2 + \dots +t_m + (n - m)t_m\big] = 0.$

于是得到 $\theta$ 的最大似然估计为

$$
\hat {\theta} = \frac {s (t _ {m})}{m}.
$$

其中  $s(t_{m})=t_{1}+t_{2}+\cdots+t_{m}+(n-m)t_{m}$  称为总试验时间，它表示直至时刻  $t_{m}$  为止 n 个产品的试验时间的总和。

对于定时截尾样本

$$
0 \leqslant t _ {1} \leqslant t _ {2} \leqslant \dots \leqslant t _ {m} \leqslant t _ {0}
$$

(其中  $t_{0}$  是截尾时间)，与上面的讨论类似，可得似然函数为

$$
L (\theta) = \frac {1}{\theta^ {m}} \mathrm{e} ^ {- \frac {1}{\theta} [ t _ {1} + t _ {2} + \dots + t _ {m} + (n - m) t _ {0} ]},
$$

$\theta$ 的最大似然估计为

$$
\hat {\theta} = \frac {s (t _ {0})}{m},
$$

其中  $s(t_{0})=t_{1}+t_{2}+\cdots+t_{m}+(n-m)t_{0}$  称为总试验时间，它表示直至时刻  $t_{0}$  为止 n 个产品的试验时间的总和。

例 设电池的寿命服从指数分布,其概率密度为

$$
f (t) = \left\{ \begin{array}{l l} \frac {1}{\theta} \mathrm{e} ^ {- t / \theta}, & t > 0, \\ 0, & t \leqslant 0, \end{array} \right.
$$

$\theta > 0$ 未知.随机地取50只电池投入寿命试验，规定试验进行到其中有15只失效时结束试验，测得失效时间（以h计）为

$$
\begin{array}{l l l l l l l l} 1 1 5 & 1 1 9 & 1 3 1 & 1 3 8 & 1 4 2 & 1 4 7 & 1 4 8 & 1 5 5 \\ 1 5 8 & 1 5 9 & 1 6 3 & 1 6 6 & 1 6 7 & 1 7 0 & 1 7 2 \end{array}
$$

试求电池的平均寿命 $\theta$ 的最大似然估计.

解 $n = 50, m = 15, s(t_{15}) = 115 + 119 + \cdots + 170 + 172 + (50 - 15) \times 172 = 8270$，得 $\theta$ 的最大似然估计为

$$
\hat {\theta} = \frac {8 2 7 0}{1 5} = 5 5 1. 3 3 (\mathrm{h}).
$$

## § 3 估计量的评选标准

自前一节可以看到,对于同一参数,用不同的估计方法求出的估计量可能不相同,如§1的例2和例6.而且,很明显,原则上任何统计量都可以作为未知参数的估计量.我们自然会问,采用哪一个估计量为好呢?这就涉及用什么样的标准来评价估计量的问题. 下面介绍几个常用的标准.

## (一) 无偏性

设  $X_{1}, X_{2}, \cdots, X_{n}$  是总体 X 的一个样本， $\theta \in \Theta$  是包含在总体 X 的分布中的待估参数，这里  $\Theta$  是  $\theta$  的取值范围.

无偏性 若估计量 $\hat{\theta}=\hat{\theta}(X_{1},X_{2},\cdots,X_{n})$ 的数学期望 $E(\hat{\theta})$ 存在，且对于任意 $\theta\in\Theta$ 有

$$
E (\hat {\theta}) = \theta , \tag {3.1}
$$

则称 $\hat{\theta}$ 是 $\theta$ 的无偏估计量.

估计量的无偏性是说对于某些样本值,由这一估计量得到的估计值相对于真值来说偏大,有些则偏小.反复将这一估计量使用多次,就“平均”来说其偏差为零.在科学技术中  $E(\hat{\theta})-\theta$  称为以  $\hat{\theta}$  作为  $\theta$  的估计的系统误差.无偏估计的实际意义就是无系统误差.

例如，设总体 $X$ 的均值 $\mu$ ，方差 $\sigma^2 > 0$ 均未知，由第六章(3.19)，(3.20)式知

$$
E (\overline {{X}}) = \mu , E (S ^ {2}) = \sigma^ {2}.
$$

即不论总体服从什么分布,样本均值  $\overline{X}$  是总体均值  $\mu$  的无偏估计;样本方差  $S^{2}=\frac{1}{n-1}\sum_{i=1}^{n}(X_{i}-\overline{X})^{2}$  是总体方差的无偏估计.而估计量  $\frac{1}{n}\sum_{i=1}^{n}(X_{i}-\overline{X})^{2}$  却不是  $\sigma^{2}$  的无偏估计,因此我们一般取  $S^{2}$  作为  $\sigma^{2}$  的估计量.

例 1 设总体 X 的 k 阶矩  $\mu_{k}=E(X^{k})\quad(k\geqslant1)$  存在，又设  $X_{1},X_{2},\cdots,X_{n}$  是 X 的一个样本。试证明不论总体服从什么分布，样本 k 阶矩  $A_{k}=\frac{1}{n}\sum_{i=1}^{n}X_{i}^{k}$  是总体 k 阶矩  $\mu_{k}$  的无偏估计量。

证  $X_{1}, X_{2}, \cdots, X_{n}$  与 X 同分布，故有

$$
E (X _ {i} ^ {k}) = E (X ^ {k}) = \mu_ {k}, \quad i = 1, 2, \dots , n.
$$

即有 $E(A_{k}) = \frac{1}{n}\sum_{i = 1}^{n}E(X_{i}^{k}) = \mu_{k}. \tag{3.2}$ □

例 2 设总体 X 服从指数分布, 其概率密度为

$$
f (x; \theta) = \left\{ \begin{array}{l l} \frac {1}{\theta} \mathrm{e} ^ {- x / \theta}, & x > 0, \\ 0, & \text {其他}, \end{array} \right.
$$

其中参数  $\theta>0$  为未知，又设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自 X 的样本，试证  $\overline{X}$  和  $nZ=n(\min\{X_{1}, X_{2}, \cdots, X_{n}\})$  都是  $\theta$  的无偏估计量.