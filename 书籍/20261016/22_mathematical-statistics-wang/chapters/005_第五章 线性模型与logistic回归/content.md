# 第五章 线性模型与logistic回归

原始 PDF 第 224–277 页。

## 第五章

## 线性模型与

## logistic回归

---

212

第五章 线性模型与logistic回归

第四章介绍的多元分布中并没有区别不同变量的作用。然而，在实际应用中，需研究某些变量取值的改变，怎么影响其他变量的变化。例如，考虑身高对体重影响。在该问题中有很多可以变化的量，如身高、腰围、体重等统称变量。其中身高是探究的因素，称为协变量，而体重会因身高这个协变量而变化，所以称作响应。有时也称协变量为特征 (feature)。又例如医生根据患者的各类检查指标，来判断是否存在某种疾病。此时，各类检查指标为协变量，而疾病是否存在为响应。这两个例子中，响应的类型不一样，前例中体重这一响应可以连续取值，而后例中是否存在某种疾病为一个二元离散取值的响应。为了分析不同类型的响应，可以建立不同的模型。通常地，前例中的协变量和响应之间可建立线性回归模型，后例中的协变量和响应之间可建立 logistic (逻辑斯谛) 回归模型。在本章中，将介绍线性回归模型和 logistic 回归模型，从而进一步分析多元分布中不同变量之间的关系。通常，线性回归模型用于处理连续响应的回归问题，logistic 回归模型用于处理离散响应的分类问题。logistic 回归模型也是一类特殊的广义线性模型。线性模型是一类简单有效的模型，具有广泛用途，也是复杂的深度学习模型的基础。

## 5.1 最小二乘估计

先考虑只有一个协变量和一个响应的情形.

例5.1.1 考察某地区便利店的商品零售额 $(x)$ 与商品流通费率 $(y)$ 之间的关系，抽样得到的数据如下:

| 商品零售额/万元 | 9.5 | 11.5 | 13.5 | 15.5 | 17.5 | 19.5 | 21.5 | 23.5 | 25.5 | 27.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 商品流通费率/% | 6.0 | 4.6 | 4.0 | 3.2 | 2.8 | 2.5 | 2.4 | 2.3 | 2.2 | 2.1 |

该数据的散点图见图 5.1.1. 从中可见, 协变量 x 与响应 y 之间存在某种趋势性的关系. 如何刻画两者之间的关系是值得研究的问题.

给定样本  $\{(x_{i},y_{i}),i=1,2,\cdots,n\}$ ，建立协变量和响应之间关系的最简单方法是考虑如下的简单线性模型:

$$
y = \beta_ {0} + \beta_ {1} x + \varepsilon ,
$$

其中 $\varepsilon \sim (0, \sigma^2)$. 令每个观测点处的拟合误差 $e_i = y_i - \beta_0 - \beta_1 x_i$, 见图5.1.1(a). 记 $\boldsymbol{\beta} = (\beta_0, \beta_1)^{\mathrm{T}}$, 样本数为 $n$. 为了得到参数 $\boldsymbol{\beta}$ 合适的估计, 一种直观的方法是使得拟合误差的绝对值之和最小化, 即

$$
\hat {\beta} = \arg \min _ {\beta} \sum_ {i = 1} ^ {n} | e _ {i} | = \arg \min _ {\beta_ {0}, \beta_ {1}} \sum_ {i = 1} ^ {n} | y _ {i} - \beta_ {0} - \beta_ {1} x _ {i} |. \tag {5.1.1}
$$

---

5.1 最小二乘估计

213

![](../../raw/pages_0225-0240/images/page_225_chart_2.jpg)

<details>
<summary>scatter</summary>

| X | Y |
| --- | --- |
| ~9.5 | 6 |
| ~11.5 | 4.6 |
| ~13.5 | 4 |
| ~15.5 | 3.2 |
| ~17.5 | 2.8 |
| ~19.5 | 2.5 |
| ~21.5 | 2.4 |
| ~23.5 | 2.3 |
| ~25.5 | 2.2 |
| ~27.5 | 2.1 |
</details>

(a) 简单线性回归模型

![](../../raw/pages_0225-0240/images/page_225_chart_4.jpg)

<details>
<summary>line</summary>

| X | Y |
| --- | --- |
| ~9.5 | 6 |
| ~11.5 | ~4.6 |
| ~13.5 | 4 |
| ~15.5 | ~3.2 |
| ~17.5 | ~2.8 |
| ~19.5 | 2.5 |
| ~21.5 | ~2.4 |
| ~23.5 | ~2.3 |
| ~25.5 | ~2.2 |
| ~27.5 | ~2.1 |
</details>

(b) 二次回归模型

图5.1.1 例5.1.1数据的散点图和回归模型

这种估计  $\beta$  的方法为最小一乘法. 然而, 由于 (5.1.1) 式中存在绝对值函数, 并不容易得到估计值  $\hat{\beta}$ . 为此, 考虑最小化拟合误差平方和, 即

$$
\hat {\boldsymbol {\beta}} = \arg \min _ {\boldsymbol {\beta}} \sum_ {i = 1} ^ {n} e _ {i} ^ {2} = \arg \min _ {\beta_ {0}, \beta_ {1}} \sum_ {i = 1} ^ {n} (y _ {i} - \beta_ {0} - \beta_ {1} x _ {i}) ^ {2}. \tag {5.1.2}
$$

称估计 $\beta$ 的这种方法为最小二乘法，相应的 $\hat{\beta}$ 为 $\beta$ 的最小二乘估计 (least squares estimation, LSE).

为了得到 (5.1.2) 式中参数的估计, 一个自然的想法是分别对  $\beta_{0}$  和  $\beta_{1}$  求导并令其为 0, 即

$$
\left\{ \begin{array}{l} - 2 \sum_ {i = 1} ^ {n} (y _ {i} - \beta_ {0} - \beta_ {1} x _ {i}) = 0, \\ - 2 \sum_ {i = 1} ^ {n} (y _ {i} - \beta_ {0} - \beta_ {1} x _ {i}) x _ {i} = 0. \end{array} \right.
$$

从而可得 $\beta_0$ 和 $\beta_{1}$ 的最小二乘估计为

$$
\left\{ \begin{array}{l} \hat {\beta} _ {0} = \bar {y} - \hat {\beta} _ {1} \bar {x}, \\ \hat {\beta} _ {1} = \frac {\sum_ {i = 1} ^ {n} x _ {i} y _ {i} - n \bar {x} \bar {y}}{\sum_ {i = 1} ^ {n} x _ {i} ^ {2} - n \bar {x} ^ {2}}, \end{array} \right. \tag {5.1.3}
$$

其中  $\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_{i},\bar{y}=\frac{1}{n}\sum_{i=1}^{n}y_{i}.$  对于例 5.1.1 的数据, 可得  $\hat{\beta}_{0}=6.747\ 4,\hat{\beta}_{1}=-0.191\ 2,$  从而拟合模型为

$$
\hat {y} = 6. 7 4 7 4 - 0. 1 9 1 2 x, \tag {5.1.4}
$$

---

214

第五章 线性模型与logistic回归

相应的线性回归模型见图 5.1.1(a). 从中可见, 简单线性回归模型 (5.1.4) 从某种程度上刻画了协变量与响应之间的关系.

给定拟合模型后, 对于任意 x 可以得到其预测值. 特别地, 当  $x = x_{i}, i = 1, 2, \cdots, n$  时, 称相应的  $\hat{y}_{i}$  为该点的拟合值,  $e_{i} = y_{i} - \hat{y}_{i}$  为该处的残差 (residual). 表 5.1.1 给出例 5.1.1 中简单线性拟合模型在不同  $x_{i}$  处的残差, 相应的残差点图见图 5.1.2(a). 从残差点图中可以直观地判断拟合模型是否合理. 一个表现良好的拟合模型的残差点图应具有以下特点:

- 各残差点应均匀地分布在横轴上下, 即一半左右的点在横轴上方, 另一半在横轴下方.
- 大部分点靠近横轴.
- 残差点图没有明显的趋势.

表 5.1.1 例 5.1.1 中简单线性拟合模型的残差

| $y_i$ | 6.0 | 4.6 | 4.0 | 3.2 | 2.8 | 2.5 | 2.4 | 2.3 | 2.2 | 2.1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\hat{y}_i$ | 4.930 9 | 4.548 5 | 4.166 1 | 3.783 6 | 3.401 2 | 3.018 8 | 2.636 4 | 2.253 9 | 1.871 5 | 1.489 1 |
| $e_i$ | 1.069 1 | 0.051 5 | -0.166 1 | -0.583 6 | -0.601 2 | -0.518 8 | -0.236 4 | 0.046 1 | 0.328 5 | 0.610 9 |

![](../../raw/pages_0225-0240/images/page_226_chart_10.jpg)

<details>
<summary>scatter</summary>

| x | e_i |
| --- | --- |
| ~9.5 | ~1.08 |
| ~11.5 | ~0.05 |
| ~13.5 | ~-0.18 |
| ~15.5 | ~-0.58 |
| ~17.5 | ~-0.60 |
| ~19.5 | ~-0.52 |
| ~21.5 | ~-0.25 |
| ~23.5 | ~0.05 |
| ~25.5 | ~0.33 |
| ~27.5 | ~0.62 |
</details>

(a) 简单线性回归模型

![](../../raw/pages_0225-0240/images/page_226_chart_12.jpg)

<details>
<summary>scatter</summary>

| x | e_i |
| --- | --- |
| ~9.5 | ~0.25 |
| ~11.5 | ~-0.22 |
| ~13.5 | ~-0.03 |
| ~15.5 | ~-0.17 |
| ~17.5 | ~-0.06 |
| ~19.5 | ~0.03 |
| ~21.5 | ~0.17 |
| ~23.5 | ~0.18 |
| ~25.5 | ~0.06 |
| ~27.5 | ~-0.20 |
</details>

(b) 二次回归模型

图5.1.2 例5.1.1不同拟合模型的残差

根据这些要求, 由图 5.1.2(a) 可知, 简单线性回归模型的拟合效果并不理想, 因为其中存在某种趋势性. 因此需要考虑其他拟合模型. 一般地, 给定样本  $\{(x_{i}, y_{i}), i = 1, 2, \cdots, n\}$ , 可以考虑以下的多项式回归模型:

$$
y = \beta_ {0} + \beta_ {1} x + \beta_ {2} x ^ {2} + \dots + \beta_ {p} x ^ {p} + \varepsilon , \tag {5.1.5}
$$

其中 p 为次数. 则 (5.1.5) 式中参数  $\boldsymbol{\beta} = (\beta_{0}, \beta_{1}, \beta_{2}, \cdots, \beta_{p})^{\mathrm{T}}$  的最小二乘估计为最小

---

5.1 最小二乘估计

215

化下面的目标函数:

$$
\sum_ {i = 1} ^ {n} (y _ {i} - \beta_ {0} - \beta_ {1} x _ {i} - \beta_ {2} x _ {i} ^ {2} - \dots - \beta_ {p} x _ {i} ^ {p}) ^ {2},
$$

上式分别对参数  $\beta_{0}, \beta_{1}, \beta_{2}, \cdots, \beta_{p}$  求导并令其为 0，则得到  $p+1$  个方程，从而得到  $\beta_{0}, \beta_{1}, \beta_{2}, \cdots, \beta_{p}$  这  $p+1$  个参数的估计。例如，取 p=2 时，则可得拟合模型为

$$
\hat {y} = 1 1. 9 8 9 4 - 0. 8 1 8 4 x + 0. 0 1 7 0 x ^ {2},
$$

其拟合效果见图 5.1.1(b)，相应的残差点图见图 5.1.2(b). 从中可见，二次模型的拟合效果比简单线性模型有明显改进，因为残差点更靠近横轴且没有很明显的趋势。然而，进一步观测可见，在样本中随着协变量的增大，响应有变小的趋势，而二次回归模型在右边尾部有翘尾的表现，因此二次回归模型在右边尾部的拟合效果并不理想。从而，需要更合理的拟合模型。提高拟合次数是一种可能的方法，但也可能出现类似的问题。

在例 5.1.1 中, 协变量的个数只有一个, 更一般的情形是存在多个协变量和一个响应. 例如, 在实际经济问题中, 家庭消费支出, 除了受家庭可支配收入的影响外, 还受诸如家庭所有的财富、物价水平、金融机构存款利息等多种因素的影响. 又例如人体的体重, 除了受身高影响外, 还可能受到腰围、臂围、性别、年龄等因素的影响. 对于多变量的情形, 除了研究协变量之间是否存在某些关系, 更关心这些协变量是怎么影响响应的.

考虑多个协变量的情形. 给定样本数据  $\{(x_{i1}, x_{i2}, \cdots, x_{ip}, y_{i}), i = 1, 2, \cdots, n\}$ ，我们希望建立协变量的函数来拟合数据，即

$$
y = f (x _ {1}, x _ {2}, \dots , x _ {p}) + \varepsilon . \tag {5.1.6}
$$

基于样本数据, 由不同方法得到函数  $f(x_{1}, x_{2}, \cdots, x_{p})$  的估计  $\hat{f}(x_{1}, x_{2}, \cdots, x_{p})$  后, 即可预测协变量在其他点处的响应值. 如何得到合适的  $\hat{f}(x_{1}, x_{2}, \cdots, x_{p})$  是统计学的关键问题之一, 其贯穿统计学的诸多分支. 在后续的回归分析、多元统计分析、非参数统计等统计学课程中都有详细的介绍. 一类方法是假设  $f(x_{1}, x_{2}, \cdots, x_{p})$  具有某种参数结构, 即

$$
y = f (x _ {1}, x _ {2}, \dots , x _ {p}; \boldsymbol {\beta}) + \varepsilon , \tag {5.1.7}
$$

其中  $f(x_{1},x_{2},\cdots,x_{p};\beta)$  的形式已知, 而这里参数  $\beta$  未知. 例如,

$$
y = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {p} x _ {p} + \varepsilon , \tag {5.1.8}
$$

其即为多元线性回归模型且  $\boldsymbol{\beta}=(\beta_{0},\beta_{1},\cdots,\beta_{p})^{\mathrm{T}}$ ，或者

$$
y = \beta_ {0} + \sum_ {i = 1} ^ {p} \beta_ {i} x _ {i} + \sum_ {1 \leqslant i \leqslant j \leqslant p} \beta_ {i j} x _ {i} x _ {j} + \varepsilon , \tag {5.1.9}
$$

---

216

第五章 线性模型与logistic回归

其为多元二次回归模型, 这里  $\beta_{i}$  为线性项系数,  $\beta_{ii}$  为二次项系数,  $\beta_{ij}(i \neq j)$  为交互项系数. 基于样本, 可给出参数模型 (5.1.7) 中参数  $\beta$  的估计. 称这类方法为参数估计法. 另一种估计 f 的方法是不限定其具体形式, 也不具有特殊的参数结构, 即  $f(x_{1}, x_{2}, \cdots, x_{p})$  的形式未知, 则称相应的方法为非参数估计法.

基于样本  $\{(x_{i1}, x_{i2}, \cdots, x_{ip}, y_{i}), i = 1, 2, \cdots, n\}$ ，估计参数模型 (5.1.7) 中参数  $\beta$  的常用方法是寻找合适的  $\hat{\beta}$  使得残差平方和达到最小，即

$$
\hat {\boldsymbol {\beta}} = \arg \min _ {\boldsymbol {\beta}} \sum_ {i = 1} ^ {n} [ y _ {i} - f (x _ {i 1}, x _ {i 2}, \dots , x _ {i p}; \boldsymbol {\beta}) ] ^ {2}.
$$

则  $\hat{\beta}$  为参数  $\beta$  的最小二乘估计. 为了得到  $\hat{\beta}$ , 通常的做法是由目标函数分别对各参数  $\beta_{i}$  求导并令其为 0, 建立方程组求解. 下一节将详细给出当  $f(x_{1}, x_{2}, \cdots, x_{p}; \beta)$  为线性模型时的求解过程和性质. 当 f 的形式未知时, 估计 f 的非参数估计法则是非参数统计这一后续课程的重要内容.

## 5.2 线性模型的估计与检验

若协变量和响应之间的拟合模型中不同参数之间满足线性的要求, 则称该拟合模型为线性模型. 记 p 个协变量  $\boldsymbol{x} = (x_{1}, x_{2}, \cdots, x_{p})$ , 则线性模型可写成以下形式:

$$
y = \beta_ {1} f _ {1} (\boldsymbol {x}) + \beta_ {2} f _ {2} (\boldsymbol {x}) + \dots + \beta_ {m} f _ {m} (\boldsymbol {x}) + \varepsilon , \tag {5.2.1}
$$

其中  $f_{i}(\boldsymbol{x})$  为 x 的确定性函数,  $\beta_{i}$  为待估参数,  $i=1,2,\cdots,m$ . 在该定义下, 线性模型不仅包括 (5.1.6) 式, 其中  $f_{i}(\boldsymbol{x})=x^{i-1}, i=1,2,\cdots,p+1$ , 也包括 (5.1.8) 式和 (5.1.9) 式. 若记  $f_{i}(\boldsymbol{x})$  为新的协变量, 则线性模型都可以表示为 (5.1.8) 式的形式. 不失一般性, 下面考虑线性模型 (5.1.8) 的参数估计和检验.

## 5.2.1 模型估计

给定样本  $\{(x_{i1},x_{i2},\cdots,x_{ip},y_{i}),i=1,2,\cdots,n\}$ ，拟合的线性模型为

$$
y _ {i} = \beta_ {0} + \beta_ {1} x _ {i 1} + \dots + \beta_ {p} x _ {i p} + \varepsilon_ {i}, i = 1, \dots , n. \tag {5.2.2}
$$

对于线性模型 (5.2.2) 中的误差项  $\varepsilon_{i}$ ，可以有不同的限制。一种方式是对误差项的分布不做假设而对其相关性和方差齐性做限制，常见的约束是使其满足 Gauss-Markov (高斯-马尔可夫) 条件；另一种方式是对误差项的分布做进一步的假设，例如服从正态分布。

---

5.2 线性模型的估计与检验

217

前者情形下, 可以应用最小二乘估计方法估计模型参数; 而对于后者, 还可以应用最大似然估计方法来估计模型参数, 因为最大似然估计中需要分布的假设. 特别地, 在后续的模型参数的显著性检验中, 可进一步要求误差项服从正态分布. 下面分别针对误差项满足 Gauss-Markov 条件和进一步的正态分布的约束, 给出模型参数  $\{\beta_{0}, \beta_{1}, \cdots, \beta_{p}, \sigma^{2}\}$  的估计方法以及相应性质.

## 1. Gauss-Markov 条件

在线性模型 (5.2.2) 中, 通常假设 $x_{i1}, x_{i2}, \cdots, x_{ip}$ 是事先给定的, 因此是固定值而没有随机性; 误差项 $\varepsilon_i$ 具有随机性, 从而响应 $y_i$ 也是随机的. 对于误差项 $\varepsilon_i$, 首先考虑以下约束:

(1) 误差项的期望值为 0, 即  $E(\varepsilon_{i}) = 0$ .
(2) 误差项的方差相同, 即 $\operatorname{Var}(\varepsilon_i) = \sigma^2$, 其中 $\sigma^2 > 0$.
(3) 不同处的误差项之间不相关, 即  $\mathrm{Corr}(\varepsilon_{i}, \varepsilon_{j}) = 0, i \neq j.$

上面三个条件被称为 Gauss-Markov 条件. 显然, 条件 (1) 容易满足, 若 $E(\varepsilon_i) = a \neq 0$, 则可设 $\varepsilon_i' = \varepsilon_i - a$ 且把 $a$ 并入 $\beta_0$ 即可使 $E(\varepsilon_i') = 0$. 而给定数据后, 条件 (2) 和条件 (3) 是否满足并不容易判断. 通常, 可通过数据的直观分析以及假设检验的方法来判断这两个条件是否满足. 若条件 (2) 或/和条件 (3) 不满足, 则需要做一些处理才能得到参数的良好估计, 相应的估计方法为广义最小二乘估计或加权最小二乘估计, 其在后续的回归分析等课程中将给出详细过程. 这里, 假设误差项满足 Gauss-Markov 条件.

记

$$
Y = \left( \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {n} \end{array} \right), \quad X = \left( \begin{array}{c c c c} 1 & x _ {1 1} & \dots & x _ {1 p} \\ 1 & x _ {2 1} & \dots & x _ {2 p} \\ \vdots & \vdots & & \vdots \\ 1 & x _ {n 1} & \dots & x _ {n p} \end{array} \right), \quad \boldsymbol {\beta} = \left( \begin{array}{c} \beta_ {0} \\ \beta_ {1} \\ \vdots \\ \beta_ {p} \end{array} \right), \quad \boldsymbol {\varepsilon} = \left( \begin{array}{c} \varepsilon_ {1} \\ \varepsilon_ {2} \\ \vdots \\ \varepsilon_ {n} \end{array} \right),
$$

则 $(5.2.2)$ 式可写为如下的矩阵形式:

$$
Y = X \beta + \varepsilon . \tag {5.2.3}
$$

参数  $\beta$  的最小二乘估计  $\hat{\beta}$  即为最小化下面的目标函数:

$$
L (\boldsymbol {\beta}) = \sum_ {i = 1} ^ {n} \left[ y _ {i} - (\beta_ {0} + \beta_ {1} x _ {i 1} + \dots + \beta_ {p} x _ {i p}) \right] ^ {2} = (Y - X \boldsymbol {\beta}) ^ {\mathrm{T}} (Y - X \boldsymbol {\beta}). \tag {5.2.4}
$$

根据对向量求导的性质, 上式对向量  $\beta$  求导并令其为 0 可得

$$
\frac {\partial L (\boldsymbol {\beta})}{\partial \boldsymbol {\beta}} = - 2 X ^ {\mathrm{T}} (Y - X \boldsymbol {\beta}) = \mathbf {0},
$$

---

218

第五章 线性模型与logistic回归

则

$$
(X ^ {\mathrm{T}} X) \boldsymbol {\beta} = X ^ {\mathrm{T}} Y.
$$

若方阵  $X^{T}X$  可逆, 则参数  $\beta$  的最小二乘估计为

$$
\hat {\boldsymbol {\beta}} = (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y. \tag {5.2.5}
$$

通常, 称 $X^{\mathrm{T}}X$ 为信息矩阵. 显然, $X^{\mathrm{T}}X$ 是半正定矩阵, 若使其可逆, 只需 $X$ 为列满秩矩阵, 且 $X^{\mathrm{T}}X$ 为正定矩阵. 列满秩的要求说明 $X$ 中不存在某一列可被其他列线性表出. 若协变量的个数 $p \geqslant n$, 则 $X$ 不可能是列满秩的. 此时, 有两种方法解决: 一是应用伪逆这一工具; 二是做变量选择, 选出部分重要变量. 第一种方法对于后续的性质讨论有较大影响, 因此常用第二种方法来解决这类问题, 并在5.3节中给出详细处理过程. 此外, 由(5.2.5)式可知, $\hat{\beta}$ 是 $Y$ 的线性函数, 该性质在后续的理论证明中将发挥重要作用.

例 5.2.1 当协变量个数 p = 1 时, 模型 (5.2.2) 退化为一元线性回归,

$$
y _ {i} = \beta_ {0} + \beta_ {1} x _ {i} + \varepsilon_ {i}, i = 1, 2, \dots , n.
$$

此时

$$
X = \left( \begin{array}{c c} 1 & x _ {1} \\ 1 & x _ {2} \\ \vdots & \vdots \\ 1 & x _ {n} \end{array} \right), \boldsymbol {\beta} = \binom{\beta_ {0}}{\beta_ {1}}, X ^ {\mathrm{T}} X = \left( \begin{array}{c c} n & \sum x _ {i} \\ \sum x _ {i} & \sum x _ {i} ^ {2} \end{array} \right), X ^ {\mathrm{T}} Y = \binom{\sum y _ {i}}{\sum x _ {i} y _ {i}},
$$

其中求和都是从1到 $n$ 的，则

$$
\begin{array}{l} (X ^ {\mathrm{T}} X) ^ {- 1} = \frac {1}{n \sum x _ {i} ^ {2} - (\sum x _ {i}) ^ {2}} \left( \begin{array}{c c} \sum x _ {i} ^ {2} & - \sum x _ {i} \\ - \sum x _ {i} & n \end{array} \right), \\ \hat {\boldsymbol {\beta}} = \frac {1}{n \sum x _ {i} ^ {2} - (\sum x _ {i}) ^ {2}} \binom{\sum x _ {i} ^ {2} \sum y _ {i} - \sum x _ {i} \sum x _ {i} y _ {i}}{n \sum x _ {i} y _ {i} - \sum x _ {i} y _ {i}}, \tag {5.2.6} \\ \end{array}
$$

易验证 (5.2.6) 式与 (5.1.3) 式是相同的.

例5.2.2 设某试验的三个协变量 $x_{1}, x_{2}, x_{3}$ 和响应 $y$ 的数据如下:

---

5.2 线性模型的估计与检验

219

| $x_1$ | $x_2$ | $x_3$ | y |
| --- | --- | --- | --- |
| -1 | -1 | -1 | -20 |
| -1 | 0 | 0 | -44 |
| -1 | 1 | 1 | 4 |
| 0 | -1 | 0 | 15 |
| 0 | 0 | 1 | -5 |
| 0 | 1 | -1 | 10 |
| 1 | -1 | 1 | 55 |
| 1 | 0 | -1 | 30 |
| 1 | 1 | 0 | 40 |

前三列协变量的数据是列正交的. 对于线性模型

$$
y = \beta_ {0} + \beta_ {1} x _ {1} + \beta_ {2} x _ {2} + \beta_ {3} x _ {3} + \varepsilon , \tag {5.2.7}
$$

我们有

$$
X ^ {\mathrm{T}} X = \left( \begin{array}{c c c c} 9 & & & \\ & 6 & & \\ & & 6 & \\ & & & 6 \end{array} \right), \quad X ^ {\mathrm{T}} Y = \left( \begin{array}{c} 8 5 \\ 1 8 5 \\ 4 \\ 3 4 \end{array} \right),
$$

$$
\hat {\boldsymbol {\beta}} = (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y = \left(\frac {8 5}{9}, \frac {1 8 5}{6}, \frac {2}{3}, \frac {1 7}{3}\right) ^ {\mathrm{T}}. \tag {5.2.8}
$$

在本例中, 信息矩阵 $X^{\mathrm{T}}X$ 很特殊, 是一个对角矩阵. 不过, 在一般情形下, 信息矩阵不是对角的.

在试验设计等统计学课程中, 称例 5.2.2 中三个协变量相应的数据是一个正交表, 其为一个特殊的正交设计. 在试验设计中, 数据量往往不大. 此时, 由于线性回归模型中参数个数不多, 是建立协变量和响应之间关系的合适模型.

现考虑 (5.2.5) 式中最小二乘估计  $\hat{\beta}$  的相关性质.

定理 5.2.1 若线性模型 (5.2.2) 满足 Gauss-Markov 条件, 且 X 为列满秩矩阵, 则关于  $\hat{\beta}$  有以下结果:

(1)  $\hat{\beta}$  是  $\beta$  的无偏估计.
(2) $\mathrm{Var}(\hat{\beta}) = \sigma^2 (X^{\mathrm{T}}X)^{-1}$.
(3) 令 $Q(\hat{\beta}) = (Y - X\hat{\beta})^{\mathrm{T}}(Y - X\hat{\beta})$，则

$$
E [ Q (\hat {\boldsymbol {\beta}}) ] = (n - p - 1) \sigma^ {2}. \tag {5.2.9}
$$

---

220

第五章 线性模型与logistic回归

证明 (1) 由于 $E(Y) = E(X\beta + \varepsilon) = X\beta$，则

$$
E (\hat {\boldsymbol {\beta}}) = E [ (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y ] = (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} E (Y) = (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} X \boldsymbol {\beta} = \boldsymbol {\beta}.
$$

(2) 由于不同的误差项之间互不相关, 故

$$
\operatorname{Var} (\boldsymbol {\varepsilon}) = \operatorname{Cov} (\boldsymbol {\varepsilon}, \boldsymbol {\varepsilon}) = \left( \begin{array}{c c c c} \operatorname{Cov} (\varepsilon_ {1}, \varepsilon_ {1}) & \operatorname{Cov} (\varepsilon_ {1}, \varepsilon_ {2}) & \dots & \operatorname{Cov} (\varepsilon_ {1}, \varepsilon_ {n}) \\ \operatorname{Cov} (\varepsilon_ {2}, \varepsilon_ {1}) & \operatorname{Cov} (\varepsilon_ {2}, \varepsilon_ {2}) & \dots & \operatorname{Cov} (\varepsilon_ {2}, \varepsilon_ {n}) \\ \vdots & \vdots & & \vdots \\ \operatorname{Cov} (\varepsilon_ {n}, \varepsilon_ {1}) & \operatorname{Cov} (\varepsilon_ {n}, \varepsilon_ {2}) & \dots & \operatorname{Cov} (\varepsilon_ {n}, \varepsilon_ {n}) \end{array} \right) = \sigma^ {2} I _ {n},
$$

其中 $I_{n}$ 为 $n$ 阶单位矩阵, 且 $\mathrm{Var}(Y) = \mathrm{Var}(X\beta + \varepsilon) = \mathrm{Var}(\varepsilon) = \sigma^2 I_n$. 则

$$
\begin{array}{l} \mathrm{Var} (\hat {\boldsymbol {\beta}}) = \mathrm{Cov} ((X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y, (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y) \\ = (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} \mathrm{Cov} (Y, Y) [ (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] ^ {\mathrm{T}} \\ = \sigma^ {2} (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} I _ {n} X (X ^ {\mathrm{T}} X) ^ {- 1} \\ = \sigma^ {2} (X ^ {\mathrm{T}} X) ^ {- 1}. \\ \end{array}
$$

(3) 由于

$$
\begin{array}{l} Q (\hat {\boldsymbol {\beta}}) = (Y - X \hat {\boldsymbol {\beta}}) ^ {\mathrm{T}} (Y - X \hat {\boldsymbol {\beta}}) \\ = [ Y - X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y ] ^ {\mathrm{T}} [ Y - X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y ] \\ = Y ^ {\mathrm{T}} [ I _ {n} - X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] [ I _ {n} - X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] Y \\ = Y ^ {\mathrm{T}} [ I _ {n} - X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] Y, \\ \end{array}
$$

故

$$
\begin{array}{l} E [ Q (\hat {\boldsymbol {\beta}}) ] = E \{Y ^ {\mathrm{T}} [ I _ {n} - X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] Y \} \\ = \mathrm{tr} \{\sigma^ {2} [ I _ {n} - X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] I _ {n} \} + \\ (X \boldsymbol {\beta}) ^ {\mathrm{T}} [ I _ {n} - X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] (X \boldsymbol {\beta}) \\ = \sigma^ {2} \mathrm{tr} [ I _ {n} - X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] \\ = \sigma^ {2} \{n - \mathrm{tr} [ X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] \} \\ = \sigma^ {2} \{n - \mathrm{tr} [ (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} X ] \} \\ = \sigma^ {2} (n - p - 1), \\ \end{array}
$$

---

5.2 线性模型的估计与检验

221

其中最后一个等式成立的原因为 $X^{\mathrm{T}}X$ 是一个 $(p + 1)\times (p + 1)$ 正定矩阵，则 $(X^{\mathrm{T}}X)^{-1}X^{\mathrm{T}}X = I_{p + 1}$ □

定理5.2.1说明最小二乘估计 $\hat{\beta}$ 是一个无偏估计，其协方差矩阵只和 $\sigma^2$ 以及 $X^{\mathrm{T}}X$ 的逆矩阵有关.模型给定后， $\sigma^2$ 是固定值，不能优化；不过对 $X$ 是可以事先做出选择的若记矩阵 $(X^{\mathrm{T}}X)^{-1} = (c_{ij})_{(p + 1)\times (p + 1)}$ ，则

$$
\mathrm{Var} (\hat {\beta} _ {i}) = c _ {i i}, \mathrm{Cov} (\hat {\beta} _ {i}, \hat {\beta} _ {j}) = c _ {i j}, i \neq j,
$$

特别地, 若 $X$ 是列正交矩阵, 则 $X^{\mathrm{T}}X$ 为对角矩阵, 即得 $c_{ij} = 0$, $i \neq j$. 在试验设计这一统计学的重要分支中, 将介绍如何选择合适的试验数据 $X$ 使得 $\hat{\beta}$ 尽可能地好, 即使 $(X^{\mathrm{T}}X)^{-1}$ 尽可能地小. 然而, $(X^{\mathrm{T}}X)^{-1}$ 是一个矩阵, 评价一个矩阵的优良性有诸多准则, 例如考虑其行列式等. 试验设计中的最优设计部分将详细讨论这些准则, 以及相应的选择试验点的方法.

记  $\hat{Y}=(\hat{y}_{1},\hat{y}_{2},\cdots,\hat{y}_{n})^{\mathrm{T}}$ ，则由定理 5.2.1(3) 的证明可知，

$$
\hat {Y} = X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y = H Y, \tag {5.2.10}
$$

其中 $H = X(X^{\mathrm{T}}X)^{-1}X^{\mathrm{T}}$ 被称为帽子矩阵 (hat matrix). 由此可见, 拟合值 $\hat{Y}$ 也是 $Y$ 的线性函数. 由于帽子矩阵 $H$ 具有 $H^{2} = H$ 的性质, 因而 $H$ 也是一个投影矩阵. 从某种意义上讲, $\hat{Y}$ 是 $Y$ 的一种投影.

记残差向量  $E = Y - X \hat{\beta}$ ，则

$$
E = Y - X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y = (I _ {n} - H) Y, \tag {5.2.11}
$$

从而说明残差向量 E 也是 Y 的线性函数.

此外, 由 (5.2.9) 式可知, 若记

$$
\hat {\sigma} ^ {2} = \frac {1}{n - p - 1} (Y - X \hat {\boldsymbol {\beta}}) ^ {\mathrm{T}} (Y - X \hat {\boldsymbol {\beta}}), \tag {5.2.12}
$$

则 $E(\hat{\sigma}^2) = \sigma^2$ ，这说明 $\hat{\sigma}^2$ 是 $\sigma^2$ 的无偏估计.因此，对于线性模型(5.2.2)，由(5.2.5)式给出参数 $\beta_{i}$ 的估计，由(5.2.12)式给出误差方差 $\sigma^2$ 的估计.

定理 5.2.1 给出了  $\hat{\beta}$  的部分性质. 进一步地,  $\hat{\beta}$  还有其他优良性质. 为此, 先给出最佳线性无偏估计 (best linear unbiased estimation, BLUE) 这一概念.

定义 5.2.1 设 A, C 是  $p \times n$  矩阵，且线性模型 (5.2.2) 中误差项  $\varepsilon_{i}$  满足 Gauss-Markov 条件，记  $\tilde{\beta} = CY$ 。若  $\tilde{\beta}$  是参数  $\beta$  的无偏估计，且对于  $\beta$  的其他线性无偏估计  $\breve{\beta} = AY$ ，即  $E(\breve{\beta}) = E(AY) = \beta$ ，都有

$$
\mathrm{Var} (\tilde {\boldsymbol {\beta}}) \leqslant \mathrm{Var} (\breve {\boldsymbol {\beta}}),
$$

则称  $\tilde{\beta}$  是  $\beta$  的 BLUE.

---

222

第五章 线性模型与logistic回归

下面的定理说明, 线性模型 (5.2.2) 的最小二乘估计  $\hat{\beta}$  具有 BLUE 的优良统计性质.

定理5.2.2 若线性模型(5.2.2)满足Gauss-Markov条件且 $X$ 是列满秩的，则(5.2.5)式中的最小二乘估计 $\hat{\beta}$ 是 $\beta$ 的BLUE.

证明 定理 5.2.1 已证明了  $\hat{\beta}$  的线性无偏性, 下证其方差在所有线性无偏估计中是最小的. 设  $\check{\beta}=AY$  是  $\beta$  的一个线性无偏估计. 则对于任意  $\beta$ , 根据无偏性, 有

$$
\boldsymbol {\beta} = E (\breve {\boldsymbol {\beta}}) = E (A Y) = E [ A (X \boldsymbol {\beta} + \varepsilon) ] = A X \boldsymbol {\beta} + A E (\varepsilon) = A X \boldsymbol {\beta},
$$

则 $AX = I_{p + 1}$ ，且 $\breve{\beta}$ 的方差为

$$
\begin{array}{l} \mathrm{Var} (\breve {\boldsymbol {\beta}}) = \mathrm{Var} (A Y) = E [ (A Y - \hat {\boldsymbol {\beta}} + \hat {\boldsymbol {\beta}} - \boldsymbol {\beta}) (A Y - \hat {\boldsymbol {\beta}} + \hat {\boldsymbol {\beta}} - \boldsymbol {\beta}) ^ {\mathrm{T}} ] \\ = \mathrm{Var} (A Y - \hat {\boldsymbol {\beta}}) + \mathrm{Var} (\hat {\boldsymbol {\beta}}) - 2 \mathrm{Cov} (A Y - \hat {\boldsymbol {\beta}}, \hat {\boldsymbol {\beta}} - \boldsymbol {\beta}). \\ \end{array}
$$

由于 $E(AY - \hat{\beta}) = 0, \beta$ 是确定值，且 $\operatorname{Var}(Y) = \sigma^2 I_n$ ，故可得

$$
\begin{array}{l} \mathrm{Cov} (A Y - \hat {\boldsymbol {\beta}}, \hat {\boldsymbol {\beta}} - \boldsymbol {\beta}) = \mathrm{Cov} ([ A - (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] Y, (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y) \\ = [ A - (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] \operatorname{Var} (Y) [ (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] ^ {\mathrm{T}} \\ = \sigma^ {2} [ A X - (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} X ] (X ^ {\mathrm{T}} X) ^ {- 1} = 0. \\ \end{array}
$$

因此, $\operatorname{Var}(\breve{\boldsymbol{\beta}}) = \operatorname{Var}(AY - \hat{\boldsymbol{\beta}}) + \operatorname{Var}(\hat{\boldsymbol{\beta}})$, 从而可知 $\operatorname{Var}(\breve{\boldsymbol{\beta}}) \geqslant \operatorname{Var}(\hat{\boldsymbol{\beta}})$, 且等号成立的充要条件是 $\operatorname{Var}(AY - \hat{\boldsymbol{\beta}}) = 0$, 即在几乎处处意义下 $AY = \hat{\boldsymbol{\beta}}$. 因此, 在几乎处处意义下, $\boldsymbol{\beta}$ 的最小二乘估计 $\hat{\boldsymbol{\beta}}$ 是唯一的 BLUE.

进一步地, 可能感兴趣的是  $\beta$  的线性组合  $a^{T}\beta$ , 其中  $a \in R^{p+1}$ , 例如, 只考虑  $\beta$  的第 i 个分量, 则只需取  $\boldsymbol{a} = (0, \cdots, 0, 1, 0, \cdots, 0)^{\mathrm{T}}$ , 其中第 i 个元素为 1, 其他都为 0. 对于线性组合  $a^{T}\beta$ , 有下面的结论.

定理 5.2.3 若线性模型 (5.2.2) 满足 Gauss-Markov 条件且 X 是列满秩的, 则对于任意的  $a \in R^{p+1}$ , 在几乎处处意义下,  $a^{T}\hat{\beta}$  是  $a^{T}\beta$  的唯一的 BLUE.

定理 5.2.3 的证明与定理 5.2.2 的证明类似, 留作习题.

由定理 5.2.3 知,  $\hat{\beta}$  的任一分量均是其对应参数的 BLUE.

## 2. 正态条件

在前面的讨论中, 只要求误差项服从 Gauss-Markov 条件, 而没有假设数据的分布形式. 进一步地, 假设误差项除了服从 Gauss-Markov 条件, 还服从正态分布, 即  $\varepsilon_{i} \sim N(0, \sigma^{2}), i = 1, 2, \cdots, n$ . 可知  $\varepsilon \sim N_{n}(\mathbf{0}, \sigma^{2}I_{n})$ , 其中  $I_{n}$  为 n 阶单位矩阵, 由于  $E(Y) = X\beta, \operatorname{Var}(Y) = \sigma^{2}I_{n}$ , 则

$$
Y \sim N _ {n} (X \beta , \sigma^ {2} I _ {n}), \tag {5.2.13}
$$

---

5.2 线性模型的估计与检验

223

即第 i 个响应  $y_{i} \sim N(X_{i}\beta, \sigma^{2})$ ，其中  $X_{i} = (1, x_{i1}, \cdots, x_{ip})$ ，而且不同的  $y_{i}$  和  $y_{j}$  是相互独立的， $i \neq j$ ，因为在正态情形下，不相关和独立是等价的。确定随机向量 Y 的分布后，可以应用最大似然估计方法来估计参数  $\beta$  和  $\sigma^{2}$ 。

定理 5.2.4 若线性模型 (5.2.2) 满足 Gauss-Markov 条件, X 是列满秩的, 且  $\varepsilon_{i} \sim N(0, \sigma^{2})$ , 则

(1)  $\beta$  的最大似然估计  $\hat{\beta} = (X^{\mathrm{T}} X)^{-1} X^{\mathrm{T}} Y$ .
(2) $\sigma^2$ 的最大似然估计 $\hat{\sigma}_n^2 = \frac{1}{n} Q(\hat{\boldsymbol{\beta}})$, 其中 $Q(\hat{\boldsymbol{\beta}}) = (Y - X\hat{\boldsymbol{\beta}})^{\mathrm{T}}(Y - X\hat{\boldsymbol{\beta}})$.
(3)  $\hat{\beta} \sim N_{p+1}(\boldsymbol{\beta}, \sigma^{2}(X^{\mathrm{T}}X)^{-1}).$
(4)  $\hat{\beta}$  与  $\hat{\sigma}_{n}^{2}$  相互独立.

证明 根据 (5.2.13) 式, $Y$ 的联合密度函数为

$$
f (Y; \boldsymbol {\beta}, \sigma^ {2}) = (2 \pi) ^ {- n / 2} (\sigma^ {2}) ^ {n / 2} \exp \left\{- \frac {1}{2 \sigma^ {2}} (Y - X \boldsymbol {\beta}) ^ {\mathrm{T}} (Y - X \boldsymbol {\beta}) \right\}.
$$

其对数似然函数为

$$
\begin{array}{l} l (\boldsymbol {\beta}, \sigma^ {2}) = \ln f (Y; \boldsymbol {\beta}, \sigma^ {2}) \\ = - \frac {n}{2} \ln (2 \pi) + \frac {n}{2} \ln (\sigma^ {2}) - \frac {1}{2 \sigma^ {2}} (Y - X \beta) ^ {\mathrm{T}} (Y - X \beta). \\ \end{array}
$$

则  $\beta$  和  $\sigma^{2}$  的最大似然估计即使得上式最大化的估计. 上式分别对  $\beta$  和  $\sigma^{2}$  求导, 并令其为 0, 则得

$$
\left\{ \begin{array}{l} \frac {\partial l (\boldsymbol {\beta} , \sigma^ {2})}{\partial \boldsymbol {\beta}} = - \frac {1}{\sigma^ {2}} X ^ {\mathrm{T}} (Y - X \boldsymbol {\beta}) = \mathbf {0}, \\ \frac {\partial l (\boldsymbol {\beta} , \sigma^ {2})}{\partial \sigma^ {2}} = \frac {n}{2 \sigma^ {2}} + \frac {1}{2 \sigma^ {4}} (Y - X \boldsymbol {\beta}) ^ {\mathrm{T}} (Y - X \boldsymbol {\beta}) = \mathbf {0}. \end{array} \right.
$$

因此

$$
\left\{ \begin{array}{l} \hat {\boldsymbol {\beta}} = (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y, \\ \hat {\sigma} ^ {2} = \frac {1}{n} (Y - X \hat {\boldsymbol {\beta}}) ^ {\mathrm{T}} (Y - X \hat {\boldsymbol {\beta}}). \end{array} \right.
$$

从而证明了 (1) 和 (2). 此外, 由于 $Y$ 服从多元正态分布, $\hat{\beta}$ 是 $Y$ 的线性函数, 因此 $\hat{\beta}$ 也服从多元正态分布. 由定理 5.2.1 可知 $E(\hat{\beta}) = \beta$, $\operatorname{Var}(\hat{\beta}) = \sigma^2(X^{\mathrm{T}}X)^{-1}$, 从而证明了 (3).

下证 (4). 对于残差向量 $E = Y - X\hat{\beta}$, 由 (5.2.11) 式可知 $E$ 也是 $Y$ 的线性函数, 从而 $E$ 也服从正态分布. 根据 (5.2.13) 式,

$$
\begin{array}{l} \mathrm{Cov} (\hat {\boldsymbol {\beta}}, E) = \mathrm{Cov} ((X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} Y, \quad [ I _ {n} - X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] Y) \\ = (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} \mathrm{Var} (Y) (I _ {n} - H) ^ {\mathrm{T}} \\ \end{array}
$$

---

224

第五章 线性模型与logistic回归

$$
\begin{array}{l} = \sigma^ {2} (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} (I _ {n} - H) \\ = \sigma^ {2} [ (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} - (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] \\ = 0. \\ \end{array}
$$

这说明  $\hat{\beta}$  和 E 这两个正态分布向量之间是不相关的, 从而也是独立的. 因此,  $\hat{\beta}$  和  $E^{T}E$  也是独立的, 从而  $\hat{\beta}$  和  $\hat{\sigma}_{n}^{2}$  相互独立. □

根据 (5.2.5) 式和定理 5.2.4(1), $\beta$ 的最小二乘估计和最大似然估计是一样的, 而结合 (5.2.12) 式和定理 5.2.4(2) 可知, $\sigma^2$ 的最大似然估计并不是无偏估计. 在实际应用中, 常用 (5.2.12) 式作为参数 $\sigma^2$ 的估计.

## 5.2.2 模型检验

前一小节给出了线性模型 (5.2.2) 中参数  $\beta$  和  $\sigma^{2}$  的最小二乘估计和最大似然估计. 本小节给出参数  $\beta_{1}, \beta_{2}, \cdots, \beta_{p}$  的显著性检验. 考虑以下的检验:

$$
H _ {0}: \beta_ {1} = \beta_ {2} = \dots = \beta_ {p} = 0 \Leftrightarrow H _ {1}: \text {至少存在某个} i, \beta_ {i} \neq 0. \tag {5.2.14}
$$

若假设问题 (5.2.14) 中 $H_0$ 被接受, 则每个 $\beta_{i}$ 都为 0 , 这说明线性模型 (5.2.2) 是不显著的. 下面将构造检验问题 (5.2.14) 的检验统计量, 并确定其在 $H_0$ 成立时的分布, 从而确定其接受域和拒绝域.

为了构造检验统计量, 假设线性模型 (5.2.2) 满足 Gauss-Markov 条件,  $\varepsilon_{i} \sim N(0, \sigma^{2})$ , 且 X 是列满秩的. 这里对误差项做正态性假设的目的是得到检验统计量的分布. 此时,

$$
y _ {i} \sim N \left(\beta_ {0} + \sum_ {j = 1} ^ {p} \beta_ {j} x _ {i j}, \sigma^ {2}\right), i = 1, 2, \dots , n.
$$

记

$$
\bar {y} = \frac {1}{n} \sum_ {i = 1} ^ {n} y _ {i}, \hat {y} _ {i} = \hat {\beta} _ {0} + \sum_ {j = 1} ^ {p} \hat {\beta} _ {j} x _ {i j},
$$

其中  $\hat{\beta}=(\hat{\beta}_{0},\hat{\beta}_{1},\cdots,\hat{\beta}_{p})^{\mathrm{T}}$  是  $\beta$  的最小二乘估计. 令

$$
S S _ {T} = \sum_ {i = 1} ^ {n} (y _ {i} - \bar {y}) ^ {2}, \quad S S _ {R} = \sum_ {i = 1} ^ {n} (\hat {y} _ {i} - \bar {y}) ^ {2}, \quad S S _ {E} = \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) ^ {2}. \tag {5.2.15}
$$

由于 $SS_{T}$ 表示响应每个取值 $y_{i}$ 对于响应的总均值的偏离程度的平方和，故在回归分析中被称为总平方和；$SS_{R}$ 表示回归值对于响应的总均值的偏离程度的平方和，故被称为回归平方和；$SS_{E}$ 表示观测值和回归值的误差的平方之和，故被称为残差平方和或误差平方和.实际上 $SS_{E}$ 即为定理5.2.4中的 $Q(\hat{\beta})$

---

5.2 线性模型的估计与检验

225

定理5.2.5 若线性模型(5.2.2)满足Gauss-Markov条件，且 $X$ 是列满秩的，则

$$
S S _ {T} = S S _ {R} + S S _ {E}.
$$

证明 由于

$$
\begin{array}{l} S S _ {T} = \sum_ {i = 1} ^ {n} (y _ {i} - \bar {y}) ^ {2} = \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i} + \hat {y} _ {i} - \bar {y}) ^ {2} \\ = \sum_ {i = 1} ^ {n} (\hat {y} _ {i} - \bar {y}) ^ {2} + \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) ^ {2} + 2 \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) (\hat {y} _ {i} - \bar {y}) \\ = S S _ {R} + S S _ {E} + 2 \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) (\hat {y} _ {i} - \bar {y}). \\ \end{array}
$$

下面只需证 $\sum_{i=1}^{n}(y_i - \hat{y}_i)(\hat{y}_i - \bar{y}) = 0.$

令  $\hat{Y}=(\hat{y}_{1},\hat{y}_{2},\cdots,\hat{y}_{n})^{\mathrm{T}}$ ，由 (5.2.10) 式以及帽子矩阵的性质可知

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) \hat {y} _ {i} = (Y - \hat {Y}) ^ {\mathrm{T}} \hat {Y} \\ = (Y - H Y) ^ {\mathrm{T}} H Y = Y ^ {\mathrm{T}} [ (I _ {n} - H) H ] Y = 0. \tag {5.2.16} \\ \end{array}
$$

此外, 由误差向量  $E = Y - \hat{Y} = (I_{n} - H)Y$  可知,

$$
X ^ {\mathrm{T}} E = X ^ {\mathrm{T}} (I _ {n} - H) Y = [ X ^ {\mathrm{T}} - X ^ {\mathrm{T}} X (X ^ {\mathrm{T}} X) ^ {- 1} X ^ {\mathrm{T}} ] Y = \mathbf {0}.
$$

由于 X 的第一列是元素都为 1 的列, 可记为  $1_{n}$ , 故  $1_{n}^{T}E=0$ , 即  $1_{n}^{\mathrm{T}}(Y-\hat{Y})=0$ , 从而  $1_{n}^{T}Y=1_{n}^{T}\hat{Y}$ . 因此,

$$
\sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) \bar {y} = \bar {y} \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) = \bar {y} (\mathbf {1} _ {n} ^ {\mathrm{T}} Y - \mathbf {1} _ {n} ^ {\mathrm{T}} \hat {Y}) = 0. \tag {5.2.17}
$$

由 (5.2.16) 和 (5.2.17) 式可知  $\sum_{i=1}^{n}(y_{i}-\hat{y}_{i})(\hat{y}_{i}-\bar{y})=0.$

定理 5.2.5 表明当线性模型 (5.2.2) 满足 Gauss-Markov 条件且 X 是列满秩的时, 总平方和都可以分解为回归平方和与残差平方和. 由回归平方和、残差平方和以及总平方和的定义可知, 若一个模型可以很好地拟合数据, 则回归平方和应该比较接近总平方和. 由此, 定义一个评价模型拟合效果的  $R^{2}$  准则如下:

$$
R ^ {2} = \frac {S S _ {R}}{S S _ {T}} = 1 - \frac {S S _ {E}}{S S _ {T}}. \tag {5.2.18}
$$

显然, $R^2 \in [0,1]$, $R^2$ 越接近 1, 拟合效果越好. $R^2$ 在回归分析中是衡量拟合效果的最重要准则之一, 其不仅可以评价线性回归模型的拟合效果, 还可以评价非线性回归模型.

---

226

第五章 线性模型与logistic回归

在实际应用中, 推荐使用  $R^{2}$  大的拟合模型. 然而,  $R^{2}$  大的模型也可能存在过拟合的现象, 以至于模型的预测能力不佳. 为了避免这类现象, 可以综合评价回归模型的其他准则来选择模型.

进一步地, 若误差还服从正态分布, 则可得到下面的结论.

定理 5.2.6 若线性模型 (5.2.2) 满足 Gauss-Markov 条件, X 是列满秩的, 且  $\varepsilon_{i} \sim N(0, \sigma^{2})$ , 则

(1)  $SS_{R}$  与  $SS_{E}$  独立.
(2) $SS_{E}/\sigma^{2}\sim\chi^{2}(n-p-1).$
(3) 假设 (5.2.14) 中 $H_0$ 为真, 则 $SS_R / \sigma^2 \sim \chi^2(p)$.

定理 5.2.6 的证明留为习题.

根据定理 5.2.6 可知, 当误差项服从正态分布时,  $SS_{R}$  与  $SS_{E}$  独立且根据这两项的分布, 可以构造假设检验问题 (5.2.14) 的检验统计量, 即

$$
F = \frac {S S _ {R} / p}{S S _ {E} / (n - p - 1)} = \frac {\frac {S S _ {R}}{\sigma^ {2}} / p}{\frac {S S _ {E}}{\sigma^ {2}} / (n - p - 1)} \stackrel {H _ {0}} {\sim} F (p, n - p - 1). \tag {5.2.19}
$$

从而当 $H_0$ 为真时, 构造的 $F$ 检验统计量服从自由度为 $p$ 和 $n - p - 1$ 的 $F$ 分布. 通常记 $MS_R = SS_R / p$, $MS_E = SS_E / (n - p - 1)$, 并被称为回归均方和误差均方. 可以证明, $MS_E$ 是误差方差 $\sigma^2$ 的无偏估计. 给定检验水平 $\alpha$ 时, 可确定相应的检验临界值 $F_\alpha(p, n - p - 1)$. 当实际数据代入检验统计量后大于 $F_\alpha(p, n - p - 1)$ 时, 认为线性模型 (5.2.2) 是显著的, 否则模型不显著. 同时也可以计算出相应的 $p$ 值, 当 $p < \alpha$ 时, 认为模型显著, 否则模型不显著. 上述过程通常用表 5.2.1 的方差分析表来表示.

表 5.2.1 检验线性模型 (5.2.2) 是否显著的方差分析表

| 来源 | 平方和 | 自由度 | 均方 | 检验统计量 | p值 |
| --- | --- | --- | --- | --- | --- |
| 回归 | $SS_{R}$ | p | $MS_{R} = \frac{SS_{R}}{p}$ | $F_{0} = \frac{MS_{R}}{MSE}$ | $p(F \geqslant F_{0})$ |
| 误差 | $SS_{E}$ | n-p-1 | $MS_{E} = \frac{SS_{E}}{n-p-1}$ |  |  |
| 总计 | $SS_{T}$ | n-1 |  |  |  |

显然, p 值越小, 模型的显著性越强, 即其更好地拟合数据. 因此, 若有多个线性模型同时拟合同一批数据, 往往选取 p 值最小的模型作为拟合模型.

例 5.2.3(例 5.2.2 续) 由数据可得  $\bar{y}=9.444\ 4$ ，对于多元线性模型 (5.2.7)，根据  $\beta$  的估计 (5.2.8) 式，可得

$$
\hat {Y} = X \hat {\beta} = (- 2 7. 7 2 2, - 2 1. 3 8 9, - 1 5. 0 5 6, 8. 7 7 8, 1 5. 1 1 1, 4. 4 4 4, 4 5. 2 7 8, 3 4. 6 1 1, 4 0. 9 4 4) ^ {\mathrm{T}},
$$

---

5.2 线性模型的估计与检验

227

则根据 (5.2.15) 式可得总平方和 $SS_T$，回归平方和 $SS_R$，残差平方和 $SS_E$，以及相应的均方，从而得到方差分析表如下:

| 来源 | 平方和 | 自由度 | 均方 | 检验统计量 | p值 |
| --- | --- | --- | --- | --- | --- |
| 回归 | 5899.500 | 3 | 1966.500 | 6.449 | 0.036 |
| 误差 | 1524.722 | 5 | 304.944 |  |  |
| 总计 | 7424.222 | 8 |  |  |  |

若取检验水平  $\alpha = 0.05$ ，则 p 值小于  $\alpha$ ，从而说明线性模型 (5.2.7) 是显著的.

即使某回归模型通过方差分析表的检验可得其为显著的, 也不能说明该回归模型中的任一参数都是显著的. 进一步地, 还希望检验线性模型 (5.2.2) 的参数  $\beta_{1}, \beta_{2}, \cdots, \beta_{p}$  是否显著. 显然, 如果某个协变量  $x_{j}$  对 y 的作用不显著, 则在线性模型 (5.2.2) 中相应的系数  $\beta_{j}$  可以取值为零. 因此, 检验  $x_{j}$  是否显著, 等价于检验假设

$$
H _ {0}: \beta_ {j} = 0 \leftrightarrow H _ {1}: \beta_ {j} \neq 0. \tag {5.2.20}
$$

下面考虑相应的检验统计量.

当线性模型 (5.2.2) 满足 Gauss-Markov 条件, $X$ 是列满秩的, 且 $\varepsilon_{i} \sim N(0, \sigma^{2})$ 时, 可知 $\hat{\beta} \sim N(\beta, \sigma^{2}(X^{\mathrm{T}}X)^{-1})$. 记矩阵 $(X^{\mathrm{T}}X)^{-1}$ 的第 $j$ 个对角元素为 $c_{jj}$, 则 $\hat{\beta}_{j} \sim N(\beta_{j}, c_{jj}\sigma^{2})$, 从而

$$
\frac {\hat {\beta} _ {j} - \beta_ {j}}{\sqrt {c _ {j j} \sigma^ {2}}} \sim N (0, 1), \frac {(\hat {\beta} _ {j} - \beta_ {j}) ^ {2}}{c _ {j j} \sigma^ {2}} \sim \chi^ {2} (1).
$$

由定理5.2.6可知， $SS_{E} / \sigma^{2}\sim \chi^{2}(n - p - 1)$ .又由定理5.2.4可知， $\hat{\beta}$ 与 $\hat{\sigma}_n^2 = SS_E / n$ 相互独立，从而 $\hat{\beta}$ 与 $SS_{E}$ 独立.因此，

$$
F = \frac {(\hat {\beta} _ {j} - \beta_ {j}) ^ {2} / c _ {j j}}{S S _ {E} / (n - p - 1)} \sim F (1, n - p - 1),
$$

即 F 服从自由度为 1 和 n-p-1 的 F 分布, 其等价于

$$
t = \frac {(\hat {\beta} _ {j} - \beta_ {j}) / \sqrt {c _ {j j}}}{\sqrt {S S _ {E} / (n - p - 1)}} \sim t (n - p - 1),
$$

其服从自由度为 $n - p - 1$ 的 $t$ 分布. 对于检验问题 (5.2.20), 在 $H_0$ 成立时, 可取检验统计量

$$
F = \frac {\hat {\beta} _ {j} ^ {2} / c _ {j j}}{S S _ {E} / (n - p - 1)}, \tag {5.2.21}
$$

---

228

第五章 线性模型与logistic回归

或

$$
t = \frac {\hat {\beta} _ {j}}{\sqrt {c _ {j j} S S _ {E} / (n - p - 1)}}. \tag {5.2.22}
$$

在 $H_0$ 成立时, 检验统计量 $F \sim F(1, n - p - 1)$, $t \sim t(n - p - 1)$. 给定检验水平 $\alpha$ 后, 可确定检验临界值, 从而判断是否接受检验 (5.2.20).

例 5.2.4 (例 5.2.2 续) 对于线性模型 (5.2.7) 相应的参数估计值 (5.2.8), 根据检验统计量 (5.2.22), 可得以下结果:

| 参数 | 估计值 | 检验统计量 | p值 |
| --- | --- | --- | --- |
| $\beta_1$ | 30.833 | 4.325 | 0.008 |
| $\beta_2$ | 0.667 | 0.094 | 0.929 |
| $\beta_3$ | 5.667 | 0.795 | 0.463 |

由此可见, 若取检验水平 $\alpha = 0.05$, 则只有参数 $\beta_{1}$ 是显著的, 而 $\beta_{2}$ 和 $\beta_{3}$ 都不显著. 这说明, 对于线性模型 (5.2.7) 而言, 协变量 $x_{1}$ 对结果有显著影响, 而 $x_{2}$ 和 $x_{3}$ 对结果没有显著影响. 由上面的检验结果可知, 该线性模型不一定很好地拟合这批数据. 为此, 需要考虑更复杂的模型.

## 5.3 变量选择

例 5.2.4 说明多元线性模型有时并不能很好地拟合数据, 而且其中的部分回归项可能不显著. 因此, 可以考虑下面的二次回归模型:

$$
y = \beta_ {0} + \sum_ {i = 1} ^ {s} \beta_ {i} x _ {i} + \sum_ {i = 1} ^ {s} \beta_ {i i} x _ {i} ^ {2} + \sum_ {1 \leqslant i <   j \leqslant s} \beta_ {i j} x _ {i} x _ {j} + \varepsilon , \tag {5.3.1}
$$

其中  $\varepsilon$  为均值为 0, 方差为  $\sigma^{2}$  的随机误差,  $\beta_{i}$  是线性项的回归参数,  $\beta_{ii}$  是平方项的回归参数,  $\beta_{ij}$  是交互项的回归参数. 二次回归模型 (5.3.1) 中待估参数为  $p=1+s+s+\frac{1}{2}s(s-1)=\frac{1}{2}(s+1)(s+2)$  个. 若令  $x_{s+i}=x_{i}^{2}, i=1,2,\cdots,s,$  且  $x_{2s+i}, i=1,2,\cdots,s(s-1)/2$  表示交互项, 则模型 (5.3.1) 也可以看成多元线性回归模型

$$
y = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {p} x _ {p} + \varepsilon \tag {5.3.2}
$$

的一种特殊情形. 换句话说, 模型 (5.3.1) 也是一类特殊的线性模型.

当试验次数 n 小于 p 时, 不能估计模型 (5.3.1) 中的全部参数. 此时, 可以选取部分回归项来拟合数据, 从而使得模型可估. 当试验次数 n 不小于 p 时, 模型 (5.2.2) 也可能

---

5.3 变量选择

229

不可估, 因为信息矩阵 $X^{\mathrm{T}}X$ 可能不可逆, 其原因在于部分协变量可由其他部分协变量线性表出. 为了避免这种情形, 需要选择合适的回归项使得模型可估. 此外, 协变量的作用大小不一, 也需要剔除那些作用不是很大的协变量. 下面考虑对于模型 (5.2.2), 通过一些方法选择部分协变量. 称相应的方法为变量选择方法. 通过变量选择, 有以下两个好处: 一是提高模型的预测准确性. 过于复杂的模型可能会导致过拟合, 从而其预测能力不好. 通过变量选择方法使变量少一点, 从而简化模型以提升模型的预测能力. 二是提高模型的可解释性. 对于模型 (5.2.2) 中, 当特征个数 $p$ 达到几百、几千甚至几万时, 通常并非每一个特征都是显著的. 若把这些特征全部放到模型中进行回归, 则难以对回归结果进行解释. 此外, 协变量的作用大小不一, 剔除那些作用不是很大的协变量, 并筛选出作用大的协变量, 可以更好地解释哪些协变量起到的影响更大.

常见的变量选择方法有向前法 (forward selection method)、向后法 (backward selection method)、逐步回归法 (stepwise regression method) 以及 Lasso (least absolute shrinkage and selection operator) 回归法等. 这里前三类方法属于子集选择 (subset selection) 法, 即选择 $p$ 个协变量的合适子集, 而 Lasso 回归法是属于正则化 (regularization) 的一类方法. 本节将分别介绍这些方法.

## 5.3.1 子集选择法

一种最简单的变量选择方法是最优子集法. 该方法的思想是遍历所有可能的协变量组合, 用所有可能的子集来进行建模, 然后根据一些方法或者准则选出最优的模型. 对于模型 (5.2.2) 的 $p$ 个协变量, 有 $2^{p}$ 种子集. 因此, 该方法至少要拟合 $2^{p}$ 次, 其计算量很大. 向前法、向后法和逐步回归法等可以减少计算量. 下面分别介绍这三种方法.

## 1. 向前法

考虑模型 (5.2.2) 中 p 个协变量  $x_{1}, x_{2}, \cdots, x_{p}$  与响应 y 之间的线性关系. 一个自然的想法是把所有协变量按相关性或重要性排序, 哪个变量最重要, 则考虑把该变量先选进来. 具体做法如下: 对于变量  $x_{1}, x_{2}, \cdots, x_{p}$ , 逐个检验模型

$$
y = \beta_ {0} + \beta_ {1} x _ {i} + \varepsilon , \tag {5.3.3}
$$

其中  $i = 1, 2, \cdots, p$ . 由 (5.2.19) 式可知, 检验  $\beta_{1}$  是否等于 0 的检验统计量 F 在原假设成立时服从  $F(1, n - 2)$ . 给出这 p 个一元线性模型的显著性检验的 F 值, 记为  $F_{1}, F_{2}, \cdots, F_{p}$ . 若  $F_{1}, F_{2}, \cdots, F_{p}$  中的最大值不大于  $F_{\alpha}(1, n - 2)$ , 则说明没有一个变量是重要的, 整个流程结束; 若  $F_{1}, F_{2}, \cdots, F_{p}$  中的最大值不小于  $F_{\alpha}(1, n - 2)$ , 说明所对应的模型是显著的, 则把相应的变量选进来.

现假设有 t 个变量已被选进来, 不失一般性, 假设这 t 个变量为  $x_{1}, x_{2}, \cdots, x_{t}$ . 可

---

230

第五章 线性模型与logistic回归

以得到相应的回归模型的残差平方和, 记为  $SS_{E}^{(t)}$ . 现考虑下面的  $t+1$  元线性回归模型:

$$
y = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {t} x _ {t} + \beta_ {t + j} x _ {t + j} + \varepsilon , j \in \{1, 2, \dots , p - t \}. \tag {5.3.4}
$$

对于每个  $j \in \{1, 2, \cdots, p - t\}$ ，计算上面的  $t + 1$  元线性回归模型的残差平方和，从而得到 p - t 个残差平方和，以及其中的最小值，记为  $SS_{E}^{(t+1)}$ 。此外，可以检验每个  $t + 1$  元线性回归模型中回归系数  $\beta_{t+j}$  是否显著不等于 0，相应的检验统计量类似于 (5.2.21) 的 F 检验统计量或 (5.2.22) 的 t 检验统计量，只需把其中的 p 改为  $t + 1$ 。若  $SS_{E}^{(t+1)}$  相比  $SS_{E}^{(t)}$  有显著下降，而且经检验模型系数  $\beta_{t+j}$  显著不等于 0，则把这个变量选进来。否则整个流程结束。这里残差平方和显著下降是指  $SS_{E}^{(t)} - SS_{E}^{(t+1)}$  大于给定的临界值  $\varepsilon$ ，而  $\beta_{t+j}$  是否显著可与给定检验水平  $\alpha$  后的临界值相比较。重复上面的过程直到没有新的变量被选出。因此，对于 p 个变量的回归模型 (5.3.2)，向前法的过程总结为下面的算法。

## 算法 5.1 (向前法)

步骤 1 给定残差平方和显著下降的临界值  $\varepsilon$  和检验水平  $\alpha$ .

步骤 2 得到 p 个一元线性回归模型 (5.3.3) 中参数  $\beta_{1}$  显著性检验的 F 值, 并取其最大值, 记为  $F^{(1)}$ . 若  $F^{(1)} \geqslant F_{\alpha}(1, n-2)$ , 则把相应的变量选出, 并得到该模型下的残差平方和  $SS_{E}^{(1)}$ , 令 t = 1, 转步骤 3; 否则算法中止.

步骤 3 设已选出 t 个协变量及相应的  $SS_{E}^{(t)}$ ，不妨记为  $x_{1}, x_{2}, \cdots, x_{t}$ 。分别得到 p-t 个  $t+1$  元线性回归模型 (5.3.3) 的残差平方和，并取其最小值，记为  $SS_{E}^{(t+1)}$ ；若  $SS_{E}^{(t)} - SS_{E}^{(t+1)} \leqslant \varepsilon$ ，则算法中止；否则转步骤 4。

步骤 4 得到使残差平方和最小的模型回归参数  $\beta_{t+j}$  的检验统计量, 记为 F. 若  $F \geqslant F_{\alpha}(1, n - t - 2)$ , 则算法中止; 否则令  $t = t + 1$ , 转步骤 3.

由向前法的步骤可知, 其构建的线性回归模型的协变量是从无到有, 逐个纳入进来的. 从几何直观来看, 向前法先将 $y$ 往与其相关性最大的协变量 $x_{i}$ 上作投影, 假设与 $x_{1}$ 最近, 得到 $\beta_{1}$ 的估计 $\hat{\beta}_{1}$ 和相应的残差; 接着, 把残差向剩余的 $p - 1$ 个变量中最相关的协变量上作投影, 不妨设与 $x_{2}$ 最近, 从而得到 $\beta_{2}$ 的估计 $\hat{\beta}_{2}$, 依次得到相应的参数估计.

例 5.3.1(例 5.2.2 续) 对于该数据, 前面已说明简单的多元线性回归模型 (5.2.7) 并不一定合适, 因为其中仅有  $x_{1}$  这一项是显著的. 下面考虑二次回归模型 (5.3.1), 把线性项、平方项和交互项都看成协变量, 并用向前法选择部分变量. 设定检验水平  $\alpha = 0.05$ , 向前法得到 5 个协变量, 按顺序分别为  $x_{1}, x_{2}^{2}, x_{1}x_{2}, x_{2}x_{3}$  和  $x_{3}^{2}$ , 回归模型如下:

$$
\hat {y} = - 8. 3 5 5 + 3 5. 3 8 7 x _ {1} + 2 3. 6 6 7 x _ {2} ^ {2} - 1 1. 2 6 9 x _ {1} x _ {2} + 9. 1 0 8 x _ {2} x _ {3} + 3. 0 3 2 x _ {3} ^ {2},
$$

---

5.3 变量选择

231

该模型的方差分析表如下所示:

| 来源 | 平方和 | 自由度 | 均方 | 检验统计量 | p值 |
| --- | --- | --- | --- | --- | --- |
| 回归 | 7 421.168 | 5 | 1 484.234 | 1 458.103 | 0.000 |
| 误差 | 3.054 | 3 | 1.018 |  |  |
| 总计 | 7 424.222 | 8 |  |  |  |

上述方差分析表中 p 值 0.000 表示该值很小, 其不等于 0. 从中可见, 该模型可以很好地拟合这批数据. 这 5 个协变量相应的检验结果如下所示:

| 参数 | 对应协变量 | 估计值 | 估计标准差 | 检验统计量 | p值 |
| --- | --- | --- | --- | --- | --- |
| $\beta_1$ | $x_1$ | 35.387 | 0.533 | 66.335 | 0.000 |
| $\beta_{22}$ | $x_2^2$ | 23.667 | 0.713 | 33.174 | 0.000 |
| $\beta_{12}$ | $x_1x_2$ | -11.269 | 0.573 | -19.665 | 0.000 |
| $\beta_{23}$ | $x_2x_3$ | 9.108 | 0.678 | 13.433 | 0.001 |
| $\beta_{33}$ | $x_3^2$ | 3.032 | 0.769 | 3.944 | 0.029 |

从中可见这 5 个协变量都是显著的.

向前法适用于任意变量个数 $p$ ，不过也存在一个缺点，即其没有剔除机制。每加入一个新协变量，可能会使此前已存在于模型中的协变量变得不显著，但在该方法中这样的协变量会被保留下来。

## 2. 向后法

与向前法相反, 向后法是先用全部变量进行建模, 再逐步地删除变量. 向后法的思路如下: 先对响应 $y$ 拟合包括所有 $p$ 个协变量的线性回归模型. 逐个考察去掉一个协变量而保留其他 $p - 1$ 个协变量的回归模型, 分别计算其残差平方和 $SS_{E}$; 使模型的 $SS_{E}$ 值减小最少的协变量被挑选出来并从模型中剔除. 持续这种迭代过程, 一直将协变量从模型中剔除, 直至剔除回归模型中任一协变量都不会使 $SS_{E}$ 显著减小为止. 此时, 模型中所剩协变量的 $t$ 检验都是显著的. 向后法的具体步骤如下所示.

## 算法 5.2 (向后法)

步骤 1 给定残差平方和显著下降的临界值  $\varepsilon$  和检验水平  $\alpha$ .

步骤 2 得到 p 元线性回归模型 (5.3.2) 的残差平方和  $SS_{E}^{(p)}$ ，令 t = p.

步骤3 设当前回归模型有 $t$ 个协变量及相应的 $SS_{E}^{(t)}$ ，对当前模型去掉一个变量，从而得到 $t$ 个 $t - 1$ 元回归模型及其相应的残差平方和，并取其最小值，记为 $SS_{E}^{(t - 1)}$；若 $SS_{E}^{(t)} - SS_{E}^{(t - 1)} \leqslant \varepsilon$，则算法中止；否则令 $t = t - 1$，重复本步骤.

---

232

第五章 线性模型与logistic回归

向后法对试验次数有要求, 即试验次数 $n$ 应大于协变量的个数 $p$, 否则整个过程一开始就无法进行. 例如例 5.2.2 中只有 9 次试验点, 因此向后法不能应用于二次回归模型 (5.3.1), 其有 9 个协变量. 而且, 向后法中从模型中剔除某个变量后, 它就不能在下一步再重新进入模型. 实际中, 有些被踢掉的协变量可能在某个阶段时可以重新加入模型, 而向后法无法做到这点.

## 3. 逐步回归法

为了兼顾向前法和向后法的优点而避免这两个方法的缺点, 逐步回归法是最常用的子集选择法. 逐步回归法的思路是先按照向前法一个接着一个引入新变量; 当引入一个新变量后, 再按照向后法的步骤对回归模型中包括该变量的所有变量进行剔除变量的操作, 直到保留的每个变量都是显著的; 重复这样的过程, 直到既没有显著的协变量选入回归方程, 也没有不显著的协变量从回归方程中剔除为止. 逐步回归法的步骤如下所示.

## 算法 5.3 (逐步回归法)

步骤 1 给定残差平方和显著下降的临界值  $\varepsilon$  和检验水平  $\alpha$ .

步骤 2 应用算法 5.1 的向前法引入一个变量.

步骤 3 对于当前回归模型, 应用算法 5.2 的向后法剔除不显著的变量.

步骤 4 重复步骤 2 和步骤 3, 直到没有新的变量被引入且没有已有的变量被剔除.

在逐步回归的算法中, 步骤 2 引入新变量后, 当前回归模型中的部分变量可能变得不显著, 因为该变量可能与新变量以及其他变量的某种线性组合具有高度线性性, 从而该变量变得不重要. 此外, 在步骤 3 中被剔除的变量, 有可能后面在步骤 2 中重新被引入.

例 5.3.2 已知影响石墨炉原子吸光度的主要因素有灰化温度  $x_{1}$ 、灰化时间  $x_{2}$ 、原子化温度  $x_{3}$  和原子化时间  $x_{4}$ . 做了 12 次试验并得到相应的吸光度 y, 具体数据如表 5.3.1 所示. 表中这 4 个协变量的取值已标准化, 即按照各协变量的取值范围均匀地取 12 个值, 并用  $1, 2, \cdots, 12$  表示.

对于该数据, 首先考虑这 4 个变量的线性回归模型

$$
y = \beta_ {0} + \beta_ {1} x _ {1} + \beta_ {2} x _ {2} + \beta_ {3} x _ {3} + \beta_ {4} x _ {4} + \varepsilon .
$$

则可得拟合模型如下:

$$
\hat {y} = 0. 1 2 5 3 - 0. 0 0 9 8 x _ {1} - 0. 0 0 3 2 x _ {2} + 0. 0 0 9 5 x _ {3} + 0. 0 0 1 3 x _ {4},
$$

相应的方差分析表如表 5.3.2 所示. 由于 p 值等于 0.0006, 若取检验水平  $\alpha = 0.05, 0.01$  甚至 0.001, 该拟合模型都是显著的. 进一步地, 考虑每个协变量的显著性检验, 其结果见表 5.3.3. 从中可知, 若取检验水平  $\alpha = 0.05$  或 0.1, 则协变量  $x_{2}$  和  $x_{4}$  都不显著.

---

5.3 变量选择

233

表 5.3.1 例 5.3.2 的吸光度试验数据

| 试验点 | $x_1$ | $x_2$ | $x_3$ | $x_4$ | y |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 6 | 8 | 10 | 0.151 |
| 2 | 2 | 12 | 3 | 7 | 0.113 |
| 3 | 3 | 5 | 11 | 4 | 0.199 |
| 4 | 4 | 11 | 6 | 1 | 0.116 |
| 5 | 5 | 4 | 1 | 11 | 0.091 |
| 6 | 6 | 10 | 9 | 8 | 0.142 |
| 7 | 7 | 3 | 4 | 5 | 0.099 |
| 8 | 8 | 9 | 12 | 2 | 0.135 |
| 9 | 9 | 2 | 7 | 12 | 0.128 |
| 10 | 10 | 8 | 2 | 9 | 0.029 |
| 11 | 11 | 1 | 10 | 6 | 0.116 |
| 12 | 12 | 7 | 5 | 3 | 0.016 |

表 5.3.2 例 5.3.2 中多元线性回归模型的方差分析表

| 来源 | 平方和 | 自由度 | 均方 | 检验统计量 | p值 |
| --- | --- | --- | --- | --- | --- |
| 回归 | 0.025 3 | 4 | 0.006 3 | 19.644 4 | 0.000 6 |
| 误差 | 0.002 3 | 7 | 0.000 3 |  |  |
| 总计 | 0.027 5 | 11 |  |  |  |

表 5.3.3 例 5.3.2 中多元线性回归模型的协变量显著性检验表

| 参数 | 对应协变量 | 估计值 | 估计标准差 | 检验统计量 | p值 |
| --- | --- | --- | --- | --- | --- |
| $\beta_1$ | $x_1$ | -0.0098 | 0.0017 | -5.7823 | 0.0007 |
| $\beta_2$ | $x_2$ | -0.0032 | 0.0019 | -1.6887 | 0.1351 |
| $\beta_3$ | $x_3$ | 0.0095 | 0.0017 | 5.6235 | 0.0008 |
| $\beta_4$ | $x_4$ | 0.0013 | 0.0019 | 0.6796 | 0.5186 |

为此, 考虑用逐步回归法进行变量选择. 首先进来的是协变量 $x_{3}$, 接着依次进来的协变量是 $x_{1}$ 和 $x_{2}$, 而 $x_{4}$ 没有被选入. 这说明逐步回归法的第一次拟合模型是 $y = \beta_{0} + \beta_{1}x_{3} + \varepsilon$, 第二次的拟合模型是 $y = \beta_{0} + \beta_{1}x_{3} + \beta_{2}x_{1} + \varepsilon$, 第三次的拟合模型是 $y = \beta_{0} + \beta_{1}x_{3} + \beta_{2}x_{1} + \beta_{3}x_{2} + \varepsilon$. 由数据可得拟合模型为

$$
\hat {y} = 0. 1 4 3 3 - 0. 0 1 0 1 x _ {1} - 0. 0 0 3 8 x _ {2} + 0. 0 0 9 0 x _ {3},
$$

其相应的系数显著性检验结果如下所示:

---

234

第五章 线性模型与logistic回归

| 协变量 | 估计值 | 估计标准差 | 检验统计量 | p值 |
| --- | --- | --- | --- | --- |
| x3 | 0.009 0 | 0.001 5 | 6.171 8 | 0.000 3 |
| x1 | -0.010 1 | 0.001 6 | -6.502 6 | 0.000 2 |
| x2 | -0.003 8 | 0.001 6 | -2.425 3 | 0.041 5 |

若取检验水平 $\alpha = 0.05$ ，则这3个变量都是显著的.在该逐步回归的过程中，没有出现在某一步的拟合模型中剔除不显著的变量.这3次回归模型相应的方差分析表见表5.3.4.从中可知，随着选入模型的变量个数的增加，模型的 $F$ 检验统计量的取值越来越大，相应的 $p$ 值越来越小，而且包括 $\{x_3\}$ ， $\{x_3,x_1\}$ 和 $\{x_3,x_1,x_2\}$ 的线性模型对应的$R^2$ 值分别为0.452,0.849和0.913.这说明，逐步得到的模型拟合效果越来越好.

表 5.3.4 例 5.3.2 中多元线性回归模型的逐步回归中的方差分析表

<table><tr><td>模型变量</td><td>来源</td><td>平方和</td><td>自由度</td><td>均方</td><td>检验统计量</td><td>p值</td></tr><tr><td rowspan="3"> $x_3$ </td><td>回归</td><td>0.0124</td><td>1</td><td>0.0124</td><td>8.2455</td><td>0.0166</td></tr><tr><td>误差</td><td>0.0151</td><td>10</td><td>0.0015</td><td></td><td></td></tr><tr><td>总计</td><td>0.0275</td><td>11</td><td></td><td></td><td></td></tr><tr><td rowspan="3"> $x_3, x_1$ </td><td>回归</td><td>0.0234</td><td>2</td><td>0.0117</td><td>25.2416</td><td>0.0002</td></tr><tr><td>误差</td><td>0.0042</td><td>9</td><td>0.0005</td><td></td><td></td></tr><tr><td>总计</td><td>0.0275</td><td>11</td><td></td><td></td><td></td></tr><tr><td rowspan="3"> $x_3, x_1, x_2$ </td><td>回归</td><td>0.0251</td><td>3</td><td>0.0084</td><td>27.9165</td><td>0.0001</td></tr><tr><td>误差</td><td>0.0024</td><td>8</td><td>0.0003</td><td></td><td></td></tr><tr><td>总计</td><td>0.0275</td><td>11</td><td></td><td></td><td></td></tr></table>

实际上, 在本线性模型中用向前法得到的结果和逐步回归法是一样的, 即依次选入  $x_{3}, x_{1}$  和  $x_{2}$ ; 此外, 若用向后法, 则第一步剔除  $x_{4}$  后, 得到的拟合模型也和逐步回归法或向前法得到的结果是一致的.

进一步地, 考虑 (5.3.1) 式的二次回归模型. 在显著性水平 $\alpha = 0.05$ 下, 用向前法和逐步回归法, 依次选入的变量都为 $x_{3}, x_{1}^{2}, x_{2}x_{3}$ 和 $x_{1}x_{4}$, 相应的拟合模型为

$$
\hat {y} = 0. 0 8 4 6 + 0. 0 1 2 6 x _ {3} - 0. 0 0 0 9 x _ {1} ^ {2} - 0. 0 0 0 5 x _ {2} x _ {3} + 0. 0 0 0 3 x _ {1} x _ {4},
$$

相应的方差分析表如下所示:

| 来源 | 平方和 | 自由度 | 均方 | 检验统计量 | p值 |
| --- | --- | --- | --- | --- | --- |
| 回归 | 0.027 1 | 4 | 0.006 8 | 111.522 6 | 0.000 0 |
| 误差 | 0.000 4 | 7 | 0.000 1 |  |  |
| 总计 | 0.027 5 | 11 |  |  |  |

---

5.3 变量选择

235

从中可知, $F$ 统计量值 111.5226 比表 5.3.4 中的 27.9165 更大, $p$ 值更小. 这说明对于二次模型再做逐步回归, 得到的拟合模型效果更好. 若用向后法进行变量选择, 由于二次模型中变量个数为 15, 超过 12 个试验次数. 直接用向后法是无法进行变量选择的. 不过, 若剔除最不显著的一些变量后, 可再应用向后法. 这样做之后最终入选的协变量, 往往和逐步回归法得到的协变量不完全相同.

在回归分析中, 人们也常用 AIC、BIC 等准则, 以及计算每个模型的预测误差的交叉验证法等方法得到最优子集. 这里不再详细展开介绍.

## 5.3.2 正则化法

前一小节介绍的向前法、向后法、逐步回归法、最优子集法等子集选择法，往往是针对数据集较小的情形。然而随着时代的发展，数据集变得越来越大而且协变量的个数也越来越多，例如协变量的个数达到几百、几千甚至几万的量级，此时子集选择法不是最好的选择，而正则化法是更常用的方法。

对于回归模型 (5.3.2), 若对响应变量 y 和 p 个协变量都做中心化处理, 即分别减去其均值, 则可以去掉常数项  $\beta_{0}$ , 而不影响回归参数  $\beta_{1}, \beta_{2}, \cdots, \beta_{p}$ . 不失一般性, 仍记中心化后的协变量和响应变量为  $x_{1}, x_{2}, \cdots, x_{p}$  和 y, 则中心化后的回归模型为

$$
y = \beta_ {1} x _ {1} + \beta_ {2} x _ {2} + \dots + \beta_ {p} x _ {p} + \varepsilon , \tag {5.3.5}
$$

其残差平方和用矩阵的形式表示仍为  $(Y-X\boldsymbol{\beta})^{\mathrm{T}}(Y-X\boldsymbol{\beta})$ ，其中  $\boldsymbol{\beta}=(\beta_{1},\beta_{2},\cdots,\beta_{p})^{\mathrm{T}}$ 。下面仅考虑中心化后的数据.正则化的主要思想是在残差平方和上加一个惩罚项（penalty），其形式如下:

$$
J (\boldsymbol {\beta}) = (Y - X \boldsymbol {\beta}) ^ {\mathrm{T}} (Y - X \boldsymbol {\beta}) + p (\boldsymbol {\beta}), \tag {5.3.6}
$$

其中 $p(\beta)$ 是对参数 $\beta$ 的某种惩罚, 其目的是用于惩罚模型的复杂度. 这个惩罚项也叫正则化项. 常见的惩罚函数有

$$
p (\boldsymbol {\beta}) = \lambda \boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {\beta}, \tag {5.3.7}
$$

其中  $\lambda$  是惩罚系数. 本质上,  $\beta^{T}\beta$  是  $\beta$  的  $L_{2}$  范数的平方, 即  $\beta^{T}\beta=\|\beta\|_{2}^{2}=\beta_{1}^{2}+\beta_{2}^{2}+\cdots+\beta_{p}^{2}$ . 为了简单起见, 把  $\|\beta\|_{2}^{2}$  简记为  $\|\beta\|^{2}$ . 也可以取其他的  $p(\beta)$ , 例如

$$
p (\boldsymbol {\beta}) = \lambda \| \boldsymbol {\beta} \| _ {1}, \tag {5.3.8}
$$

其中  $\|\beta\|_{1}=|\beta_{1}|+|\beta_{2}|+\cdots+|\beta_{p}|$  为  $\beta$  的  $L_{1}$  范数. 在 (5.3.7) 式和 (5.3.8) 式中的惩罚系数  $\lambda$  决定了对参数  $\beta$  的惩罚力度.  $\lambda$  越大, 对于参数的惩罚就越大;  $\lambda$  越小, 惩罚就越小. 例如, 当  $\lambda=0$  时, (5.3.6) 式就退化为最简单的线性回归. 当  $p(\beta)$  取 (5.3.7) 式且

---

236

第五章 线性模型与logistic回归

$\lambda > 0$ 时, 称相应的估计为岭回归 (ridge regression) 估计; 当 $p(\beta)$ 取 (5.3.8) 式且 $\lambda > 0$ 时, 称相应的估计为 Lasso 回归估计. 岭回归估计是 1970 年由 Hoerl 和 Kennard 提出的, 参见 Hoerl et al. (1970), 其主要目的并不是用于解决变量选择的问题, 而是解决信息矩阵 $X^{\mathrm{T}}X$ 接近退化甚至不可逆的情形. Lasso 回归估计由 Robert Tibshirani (蒂施莱尼) 于 1996 年提出, 其为第一个可应用于变量选择的正则化方法, 参见 Tibshirani (1996). 下面分别介绍这两种常用的正则化方法.

## 1. 岭回归

使最小化 (5.2.4) 式的  $\beta$  存在且唯一的条件是  $X^{T}X$  列满秩。然而，当数据特征中存在共线性的情形，即部分特征之间的相关性比较大时，会使得标准最小二乘求解式 (5.2.5) 不稳定，即信息矩阵  $X^{T}X$  的行列式接近零从而其接近退化，计算  $X^{T}X$  的误差会变大。

例5.3.3 设真实模型为 $y = 5 + 2x_{1} + 3x_{2} + \varepsilon$. 在某10次试验中的 $x_{1}, x_{2}, \varepsilon$ 和相应的 $y$ 分别如下所示:

| $x_{1}$ | 1.1 | 1.4 | 1.7 | 1.7 | 1.8 | 1.8 | 1.9 | 2.0 | 2.3 | 2.4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $x_{2}$ | 1.2 | 1.3 | 1.8 | 1.7 | 1.9 | 1.8 | 2.0 | 2.1 | 2.4 | 2.5 |
| $\varepsilon$ | 0.7 | -0.5 | 0.4 | -0.5 | 0.2 | 1.5 | 1.1 | 0.6 | -1.5 | -0.5 |
| y | 11.5 | 11.2 | 14.2 | 13.0 | 14.5 | 15.5 | 15.9 | 15.9 | 15.3 | 16.8 |

由最小二乘估计 (5.2.5) 式, 可得

$$
\hat {y} = 6. 9 2 1 4 - 2. 8 1 9 7 x _ {1} + 6. 7 1 7 8 x _ {2}.
$$

分别对 $x_{1}$ 和 $x_{2}$ 减去其样本均值1.81和1.87，对 $y$ 减去其样本均值14.38后，仍记为$x_{1},x_{2}$ 和 $y,$ 则由最小二乘估计(5.2.5)式，可得

$$
\hat {y} = - 2. 8 1 9 7 x _ {1} + 6. 7 1 7 8 x _ {2}.
$$

因此, $x_{1}$ 和 $x_{2}$ 相应的系数估计很不准确, 其原因在于 $x_{1}$ 和 $x_{2}$ 的相关系数为 0.988, 这说明这两个变量之间相关性很强. 进一步地, $X^{\mathrm{T}}X$ 的特征根分别为 2.8727 和 0.0173, 这说明该矩阵接近退化. 从而导致估计不准确.

从例 5.3.3 可知, 当信息矩阵接近退化时, 直接用最小二乘估计方法并不能得到好的估计. 对于 (5.3.7) 式的惩罚函数, 根据对向量求导的性质, 目标函数

$$
J (\boldsymbol {\beta}) = (Y - X \boldsymbol {\beta}) ^ {\mathrm{T}} (Y - X \boldsymbol {\beta}) + \lambda \boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {\beta}
$$

对向量  $\beta$  求导并令其为 0, 可得

$$
\frac {\partial J (\boldsymbol {\beta})}{\partial \boldsymbol {\beta}} = - 2 X ^ {\mathrm{T}} (Y - X \boldsymbol {\beta}) + 2 \lambda \boldsymbol {\beta} = \mathbf {0},
$$

---

5.3 变量选择

237

则

$$
(X ^ {\mathrm{T}} X + \lambda I _ {p}) \beta = X ^ {\mathrm{T}} Y,
$$

其中  $I_{p}$  为  $p+1$  阶单位矩阵. 由于方阵  $X^{T}X$  是非负定矩阵, 而当  $\lambda>0$  时,  $X^{T}X+\lambda I_{p}$  一定是正定矩阵, 故参数  $\beta$  的岭估计为

$$
\hat {\boldsymbol {\beta}} _ {\lambda} = (X ^ {\mathrm{T}} X + \lambda I _ {p}) ^ {- 1} X ^ {\mathrm{T}} Y. \tag {5.3.9}
$$

也称  $\hat{\beta}_{\lambda}$  为岭迹, 即关于不同的  $\lambda$  对应于不同的  $\hat{\beta}_{\lambda}$ . 因此, 岭估计仍是 Y 的线性函数. 若 Y 服从多元正态分布, 则  $\hat{\beta}_{\lambda}$  也服从多元正态分布.

为了评价多元估计量的好坏, 可以考虑均方误差这一准则. 对于参数  $\beta$  的任一估计 b, 其均方误差定义为  $E[(\boldsymbol{b}-\boldsymbol{\beta})^{\mathrm{T}}(\boldsymbol{b}-\boldsymbol{\beta})]$ , 它是一个数. 设  $\operatorname{tr}(A)$  表示方阵 A 的迹. 由于

$$
\begin{array}{l} E [ (\boldsymbol {b} - \boldsymbol {\beta}) ^ {\mathrm{T}} (\boldsymbol {b} - \boldsymbol {\beta}) ] = \mathrm{tr} (\boldsymbol {b} - \boldsymbol {\beta}) (\boldsymbol {b} - \boldsymbol {\beta}) ^ {\mathrm{T}} \\ = \mathrm{tr} \{[ \boldsymbol {b} - E (\boldsymbol {b}) ] [ \boldsymbol {b} - E (\boldsymbol {b}) ] ^ {\mathrm{T}} + [ E (\boldsymbol {b}) - \beta ] [ E (\boldsymbol {b}) - \beta ] ^ {\mathrm{T}} \} \\ = \mathrm{trVar} (\boldsymbol {b}) + [ E (\boldsymbol {b}) - \boldsymbol {\beta} ] ^ {\mathrm{T}} [ E (\boldsymbol {b}) - \boldsymbol {\beta} ], \tag {5.3.10} \\ \end{array}
$$

故当 b 为  $\beta$  的最小二乘估计  $\hat{\beta}$  时, 均方误差为  $\sigma^{2}\mathrm{tr}(X^{\mathrm{T}}X)^{-1}$ .

定理 5.3.1 当  $\lambda > 0$  时, 岭估计有以下性质:

(1) $\hat{\beta}_{\lambda}$ 是有偏估计.
(2) $\hat{\beta}_{\lambda}$ 将部分参数向0收缩.
(3) 当 $\lambda \leqslant \frac{2\sigma^2}{\beta^{\mathrm{T}}\beta}$ 时, $\hat{\beta}_{\lambda}$ 的均方误差比最小二乘估计 $\hat{\beta}$ 的均方误差更小.

证明 显然, 当  $\lambda > 0$  时, 由  $\hat{\beta}$  的无偏性, 可得

$$
\begin{array}{l} E (\hat {\boldsymbol {\beta}} _ {\lambda}) = E [ (X ^ {\mathrm{T}} X + \lambda I _ {p}) ^ {- 1} X ^ {\mathrm{T}} Y ] \\ = (X ^ {\mathrm{T}} X + \lambda I _ {p}) ^ {- 1} X ^ {\mathrm{T}} E (Y) \\ = (X ^ {\mathrm{T}} X + \lambda I _ {p}) ^ {- 1} X ^ {\mathrm{T}} X \beta \\ = (X ^ {\mathrm{T}} X + \lambda I _ {p}) ^ {- 1} (X ^ {\mathrm{T}} X + \lambda I _ {p} - \lambda I _ {p}) \beta \\ = \boldsymbol {\beta} - \lambda (X ^ {\mathrm{T}} X + \lambda I _ {p}) ^ {- 1} \boldsymbol {\beta}. \\ \end{array}
$$

因此, 岭估计  $\hat{\beta}_{\lambda}$  并不是  $\beta$  的无偏估计, 且偏差为

$$
E (\hat {\boldsymbol {\beta}} _ {\lambda}) - \boldsymbol {\beta} = - \lambda (X ^ {\mathrm{T}} X + \lambda I _ {p}) ^ {- 1} \boldsymbol {\beta}. \tag {5.3.11}
$$

从而证明了性质(1).

---

238

第五章 线性模型与logistic回归

若记信息矩阵 $M = X^{\mathrm{T}}X, Z_{\lambda} = (I_p + \lambda M^{-1})^{-1}$，则

$$
\begin{array}{l} \hat {\boldsymbol {\beta}} _ {\lambda} = (M + \lambda I _ {p}) ^ {- 1} M M ^ {- 1} X ^ {\mathrm{T}} Y \\ = (I _ {p} + \lambda M ^ {- 1}) ^ {- 1} (M ^ {- 1} X ^ {\mathrm{T}} Y) = Z _ {\lambda} \hat {\boldsymbol {\beta}}, \tag {5.3.12} \\ \end{array}
$$

其中  $\hat{\beta}$  为 (5.2.5) 式的最小二乘估计. 由于 M 为非负定对称矩阵, 其特征根不小于 0, 且存在一个正交矩阵 Q, 使得  $M = Q \Delta Q^{T}$ , 其中  $\Delta = \mathrm{diag}(\delta_{1}, \delta_{2}, \cdots, \delta_{p})$  为对角矩阵, 其对角元素是 M 的特征根. 从而,

$$
Z _ {\lambda} = [ I _ {p} + \lambda (Q \varDelta Q ^ {\mathrm{T}}) ^ {- 1} ] ^ {- 1} = Q (I _ {p} + \lambda \varDelta^ {- 1}) ^ {- 1} Q ^ {\mathrm{T}} = Q \varGamma Q ^ {\mathrm{T}},
$$

其中  $\Gamma$  为对角矩阵, 即  $\Gamma = \mathrm{diag}(\gamma_{1}, \gamma_{2}, \cdots, \gamma_{p})$ , 其中

$$
\gamma_ {i} = \frac {\delta_ {i}}{\delta_ {i} + \lambda}, i = 1, 2, \dots , p.
$$

则当 $\lambda > 0$ 时, $Z_{\lambda}$ 的特征根为不大于1的正数. 因此,

$$
\| \hat {\boldsymbol {\beta}} _ {\lambda} \| ^ {2} = \| Z _ {\lambda} \hat {\boldsymbol {\beta}} \| ^ {2} = \| Q \Lambda Q \hat {\boldsymbol {\beta}} \| ^ {2} = \| \Lambda Q \hat {\boldsymbol {\beta}} \| ^ {2}.
$$

则当 $\lambda > 0$ 时，

$$
\| \hat {\boldsymbol {\beta}} _ {\lambda} \| ^ {2} <   \| Q \hat {\boldsymbol {\beta}} \| ^ {2} = \| \hat {\boldsymbol {\beta}} \| ^ {2}.
$$

因此, 参数  $\beta$  的岭估计更趋于将部分参数向 0 收缩. 从而证明了性质 (2).

根据 (5.3.12) 式, 有

$$
E (\hat {\boldsymbol {\beta}} _ {\lambda}) = E (Z _ {\lambda} \hat {\boldsymbol {\beta}}) = Z _ {\lambda} E (\hat {\boldsymbol {\beta}}) = Q \Gamma Q ^ {\mathrm{T}} \boldsymbol {\beta}.
$$

从而  $\hat{\beta}_{\lambda}-E(\hat{\beta}_{\lambda})=Q\Gamma Q^{\mathrm{T}}(\hat{\beta}-\beta)$ ，根据定理 5.2.1(2)，可得

$$
\begin{array}{l} \mathrm{Var} (\hat {\boldsymbol {\beta}} _ {\lambda}) = E \{[ \hat {\boldsymbol {\beta}} _ {\lambda} - E (\hat {\boldsymbol {\beta}} _ {\lambda}) ] [ \hat {\boldsymbol {\beta}} _ {\lambda} - E (\hat {\boldsymbol {\beta}} _ {\lambda}) ] ^ {\mathrm{T}} \} \\ = Q \Gamma Q ^ {\mathrm{T}} E [ (\hat {\boldsymbol {\beta}} - \boldsymbol {\beta}) (\hat {\boldsymbol {\beta}} - \boldsymbol {\beta}) ^ {\mathrm{T}} ] Q \Gamma Q ^ {\mathrm{T}} \\ = \sigma^ {2} Q \Gamma Q ^ {\mathrm{T}} M ^ {- 1} Q \Gamma Q ^ {\mathrm{T}} \\ = \sigma^ {2} Q \Gamma \Delta^ {- 1} \Gamma Q ^ {\mathrm{T}} \\ = \sigma^ {2} Q \Theta Q ^ {\mathrm{T}}, \tag {5.3.13} \\ \end{array}
$$

其中  $\Theta$  为对角矩阵,

$$
\Theta = \left( \begin{array}{c c c c} \frac {\delta_ {1}}{(\delta_ {1} + \lambda) ^ {2}} & & & \\ & \frac {\delta_ {2}}{(\delta_ {2} + \lambda) ^ {2}} & & \\ & & \ddots & \\ & & & \frac {\delta_ {p}}{(\delta_ {p} + \lambda) ^ {2}} \end{array} \right).
$$

---

5.3 变量选择

239

根据 (5.3.11) 式可知, $[E(\hat{\beta}_{\lambda}) - \beta]^{\mathrm{T}}[E(\hat{\beta}_{\lambda}) - \beta] = \lambda^2\beta^{\mathrm{T}}(M + \lambda I_p)^{-2}\beta$. 记 $\hat{\beta}_{\lambda}$ 的均方误差为 $H(\lambda)$, 则由 (5.3.10) 式和 (5.3.13) 式可知,

$$
\begin{array}{l} H (\lambda) = E [ (\hat {\boldsymbol {\beta}} _ {\lambda} - \boldsymbol {\beta}) ^ {\mathrm{T}} (\hat {\boldsymbol {\beta}} _ {\lambda} - \boldsymbol {\beta}) ] \\ = \mathrm{trVar} (\hat {\boldsymbol {\beta}} _ {\lambda}) + [ E (\hat {\boldsymbol {\beta}} _ {\lambda}) - \boldsymbol {\beta} ] ^ {\mathrm{T}} [ E (\hat {\boldsymbol {\beta}} _ {\lambda}) - \boldsymbol {\beta} ] \\ = \mathrm{trVar} (\hat {\boldsymbol {\beta}} _ {\lambda}) + \lambda^ {2} \boldsymbol {\beta} ^ {\mathrm{T}} (M + \lambda I _ {p}) ^ {- 2} \boldsymbol {\beta} \\ = \mathrm{tr} (\sigma^ {2} Q \Theta Q ^ {\mathrm{T}}) + \lambda^ {2} \boldsymbol {\beta} ^ {\mathrm{T}} (M + \lambda I _ {p}) ^ {- 2} \boldsymbol {\beta} \\ = \sigma^ {2} \sum_ {i = 1} ^ {p} \frac {\delta_ {i}}{(\delta_ {i} + \lambda) ^ {2}} + \lambda^ {2} \boldsymbol {\beta} ^ {\mathrm{T}} (M + \lambda I _ {p}) ^ {- 2} \boldsymbol {\beta}. \\ \end{array}
$$

显然, $\lambda = 0$, $\hat{\beta}_{\lambda}$ 退化为最小二乘估计, 相应的均方误差为 $H(0)$. 因此, 通过优化理论可知, 当 $\lambda \leqslant \frac{2\sigma^2}{\beta^{\mathrm{T}}\beta}$ 时, $H(\lambda) < H(0)$. 从而证明了性质 (3).

当 $\lambda = 0$ ，岭回归 $\hat{\beta}_{\lambda}$ 即为最小二乘估计 $\hat{\beta}$ ; 当 $\lambda = \infty$ ，岭回归 $\hat{\beta}_{\lambda} = 0$ ，即所有参数都收缩到0.由定理5.3.1可知，岭回归是对最小二乘估计的参数做某种程度的收缩，可认为是一种改良的最小二乘估计法.岭估计放弃了最小二乘法的无偏性，来获得均方误差更小的收缩估计.从而，岭估计可以缓解多重共线问题，以及过拟合问题.然而，由$\hat{\beta}_{\lambda}$ 的定义可知，其元素并不等于0.因此，岭估计并不能直接做变量选择，而且牺牲一些模型的解释性，也无法从根本上解决多重共线问题

定理 5.3.1(3) 说明在某些情形下, 岭估计的均方误差比最小二乘估计的要小, 但具体求最优的  $\lambda$  依赖于未知参数  $\sigma^{2}$  和  $\beta$ . 而在实际应用中必须通过样本来确定  $\lambda$ . 然而, 由于最优的  $\lambda$  对未知参数  $\sigma^{2}$  和  $\beta$  的依赖关系未知, 理论上并不能给出最优  $\lambda$  的明确回答. 实际应用中, 确定  $\lambda$  的常用方法是岭迹法. 称估计向量  $\hat{\beta}_{\lambda}$  中每个元素随着  $\lambda$  的变化作图而得到的曲线为相应的岭迹. 通过岭迹图可以观察较佳的  $\lambda$  的取值, 即选择使每条岭迹都比较平稳的  $\lambda$  作为其取值. 此外, 还可以观察变量是否有多重共线性; 若不存在多重共线性, 则岭迹图应稳定地逐渐趋于 0.

例如, 对于例 5.3.3 的数据, 参数  $\hat{\beta}_{\lambda} = (\hat{\beta}_{\lambda,1}, \hat{\beta}_{\lambda,2})^{\mathrm{T}}$  的岭迹分别如图 5.3.1 所示. 从中可见, 当  $\lambda$  取 0.3 左右时, 岭迹基本稳定. 此外,  $\hat{\beta}_{\lambda,1}$  的最小二乘估计是负数, 即协变量  $x_{1}$  对 y 的影响是负的; 然而, 随着  $\lambda$  的增大,  $\hat{\beta}_{\lambda,1}$  的取值变为正的, 这更好地反映该协变量和 y 的关系. 由于岭迹并不能稳定地趋于 0, 说明该数据存在多重共线性. 因此, 存在多重共线性时, 从某种意义上来说, 岭估计比最小二乘估计可能更好.

进一步地, 从优化的角度来看, 求解岭回归估计的目标函数 $J(\beta)$ 等价于下面的优化问题:

$$
\min (Y - X \boldsymbol {\beta}) ^ {\mathrm{T}} (Y - X \boldsymbol {\beta}) \tag {5.3.14}
$$

$$
\text {s.t.} \quad \boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {\beta} \leqslant t.
$$

---

240

第五章 线性模型与logistic回归

这里 $t$ 预先给定. 显然, 若 $t$ 取无穷大, 优化问题 (5.3.14) 变为普通的最小二乘估计, 若 $t$ 趋于 0 , 优化问题 (5.3.14) 把所有参数压缩到 0 . 由于 $(Y - X\beta)^{\mathrm{T}}(Y - X\beta)$ 是关于参数 $\beta$ 的二次函数, 其在 $p$ 维空间中为椭球体, 而 $\beta^{\mathrm{T}}\beta \leqslant t$ 的几何含义是在 $p$ 维空间中以原点为球心的超球体内部. 当 $p = 2$ 时, 优化问题 (5.3.14) 的示意图如图 5.3.2(a) 所示. 椭圆等高线和半径为 $\sqrt{t}$ 的圆的交点即为参数的岭回归估计. 此外, 这个交点不同于参数的最小二乘估计 $\hat{\beta}$.

![](../../raw/pages_0241-0256/images/page_252_chart_3.jpg)

<details>
<summary>line</summary>

| \(\lambda\) | \(\beta\)̂\(\lambda\),1 | \(\beta\)̂\(\lambda\),2 |
| --- | --- | --- |
| 0 | -3 | 7 |
| 0.2 | ~1.5 | ~2.5 |
| 0.4 | ~1.6 | ~2.2 |
| 0.6 | ~1.6 | ~2.0 |
| 0.8 | ~1.5 | ~1.9 |
| 1.0 | ~1.4 | ~1.8 |
</details>

图5.3.1 例5.3.3的岭迹图

![](../../raw/pages_0241-0256/images/page_252_image_5.jpg)

<details>
<summary>text_image</summary>

β̂
</details>

(a) 岭回归

![](../../raw/pages_0241-0256/images/page_252_image_7.jpg)

<details>
<summary>text_image</summary>

β̂
</details>

(b) Lasso回归

图5.3.2 岭回归和Lasso回归的几何示意图

## 2. Lasso 回归

前面的岭估计是用 $L_{2}$ 范数对参数 $\beta$ 进行惩罚, 而Lasso回归用 $L_{1}$ 范数对参数 $\beta$ 进行惩罚, 即最小化下面的目标函数:

---

5.3 变量选择

241

$$
\begin{array}{l} J (\boldsymbol {\beta}) = (Y - X \boldsymbol {\beta}) ^ {\mathrm{T}} (Y - X \boldsymbol {\beta}) + \lambda \| \boldsymbol {\beta} \| _ {1} \tag {5.3.15} \\ = \sum_ {i = 1} ^ {n} (y _ {i} - \beta_ {1} x _ {i 1} - \beta_ {2} x _ {i 2} - \dots - \beta_ {p} x _ {i p}) + \lambda \sum_ {j = 1} ^ {p} | \beta_ {j} |. \\ \end{array}
$$

从优化的角度来看, 求解 Lasso 估计的目标函数  $J(\beta)$  等价于下面的优化问题:

$$
\min (Y - X \boldsymbol {\beta}) ^ {\mathrm{T}} (Y - X \boldsymbol {\beta}) \tag {5.3.16}
$$

$$
\text {s.t.} \quad \| \boldsymbol {\beta} \| _ {1} \leqslant t.
$$

这里 $t$ 预先给定. 类似于岭估计, 若 $t$ 取无穷大, 优化问题 (5.3.16) 变为普通的最小二乘估计, 若 $t$ 趋于 0, 优化问题 (5.3.16) 把所有参数压缩到 0. 当 $p = 2$ 时, 优化问题 (5.3.16) 的示意图如图 5.3.2(b) 所示. 椭圆等高线和菱形 $|\beta_1| + |\beta_2| \leqslant t$ 的交点即为参数的 Lasso 回归估计. 对比图 5.3.2(a) 可知, 岭回归不易使参数变为 0, 而 Lasso 回归有较大可能使得部分参数收缩到 0. 不管 Lasso 估计还是岭估计, 加了约束条件后, 它们都是有偏估计, 因此与通过最小二乘法得到的无偏估计有差距.

Lasso 估计可以起到变量选择作用的具体原理涉及一些凸优化理论. 一个函数 $f(\cdot)$ 被称为凸函数, 是指其定义域是凸集, 且对于定义域中任意两点 $x$ 和 $y$, 和任意的 $\alpha \in (0,1)$, $f(\alpha x + (1 - \alpha)y) \leqslant \alpha f(x) + (1 - \alpha)f(y)$. 对于凸优化问题, 最小值总是出现在极值点 (extreme point) 处, 而对于参数空间, 极值点一般是落在坐标轴上的点. 从优化理论的角度来看, 在 (5.3.15) 式中的目标函数 $J(\beta)$ 是一个凸函数. 相应地, 求解该问题也是一个凸优化问题. 这也从某种意义上解释了 Lasso 回归可得到变量选择的效果. 由于 Lasso 估计的目标函数 $J(\beta)$ 中有绝对值函数, 因此不能通过求导的方法得到参数 $\beta$ 的解, 从而优化理论中常规的解法如梯度下降法、Newton (牛顿) 法无法使用. 实际上, 该问题并没有显式解, 且往往需应用迭代算法进行求解. 常用的求解方法有以下两种: 坐标轴下降法与最小角回归法 (least angle regression), 后者是 Bradley Efron 于 2004 年提出的.

坐标轴下降法是一种迭代算法, 其是在当前坐标轴上搜索函数最小值, 而不需求目标函数的导数. 先以 2 维为例介绍坐标轴下降法的主要思路. 对于目标函数 $J(\beta_1, \beta_2)$, 给定初始值 $\boldsymbol{\beta}^{(0)} = (\beta_1^{(0)}, \beta_2^{(0)})$, 固定 $\beta_1^{(0)}$, 找使得 $J(\beta_1^{(0)}, \beta_2)$ 达到最小的 $\beta_2$, 记为 $\beta_2^{(1)}$; 固定 $\beta_2^{(1)}$, 找使得 $J(\beta_1, \beta_2^{(1)})$ 达到最小的 $\beta_1$, 记为 $\beta_1^{(1)}$, 从而得到 $\boldsymbol{\beta}^{(1)} = (\beta_1^{(1)}, \beta_2^{(1)})$; 这样一直迭代下去, 直到收敛. 收敛的判断条件为 $\boldsymbol{\beta}^{(t+1)}$ 和 $\boldsymbol{\beta}^{(t)}$ 的距离小于给定的临界值. 对于 $p$ 维参数 $\boldsymbol{\beta} = (\beta_1, \beta_2, \cdots, \beta_p)$, 类似地, 固定 $p-1$ 个参数, 计算剩下的那个参数使得凸函数 $J(\boldsymbol{\beta})$ 达到最小的点, 依次更新这 $p$ 个参数, 得到该次迭代的最小值点; 迭代直到收敛. 具体步骤如下所示.

## 算法 5.4 (Lasso 回归估计的坐标轴下降法)

步骤 1 给定初始值  $\boldsymbol{\beta}^{(0)}=\left(\beta_{1}^{(0)},\beta_{2}^{(0)},\cdots,\beta_{p}^{(0)}\right)$ .

---

242

第五章 线性模型与logistic回归

步骤 2 固定  $\beta_{2}^{(k-1)}, \beta_{3}^{(k-1)}, \cdots, \beta_{p}^{(k-1)}$ ，计算使得  $J\left(\beta_{1}, \beta_{2}^{(k-1)}, \cdots, \beta_{p}^{(k-1)}\right)$  达到最小的  $\beta_{1}$ ，得到  $\beta_{1}^{(k)}$ ；依次往后计算，得到  $\beta_{p}^{(k)}$  为止，一共执行 p 次运算:

$$
\beta_ {1} ^ {(k)} = \arg \min _ {\beta_ {1}} J \left(\beta_ {1}, \beta_ {2} ^ {(k - 1)}, \beta_ {3} ^ {(k - 1)}, \dots , \beta_ {p} ^ {(k - 1)}\right),
$$

$$
\beta_ {2} ^ {(k)} = \arg \min _ {\beta_ {2}} J \left(\beta_ {1} ^ {(k)}, \beta_ {2}, \beta_ {3} ^ {(k - 1)}, \dots , \beta_ {p} ^ {(k - 1)}\right),
$$

$$
\beta_ {3} ^ {(k)} = \arg \min _ {\beta_ {3}} J \left(\beta_ {1} ^ {(k)}, \beta_ {2} ^ {(k)}, \beta_ {3}, \dots , \beta_ {p} ^ {(k - 1)}\right),
$$

...，

$$
\beta_ {p} ^ {(k)} = \arg \min _ {\beta_ {p}} J \left(\beta_ {1} ^ {(k)}, \beta_ {2} ^ {(k)}, \beta_ {3} ^ {(k)}, \dots , \beta_ {p}\right),
$$

从而得到第 k 次迭代  $\boldsymbol{\beta}^{(k)}=\left(\beta_{1}^{(k)},\beta_{2}^{(k)},\cdots,\beta_{p}^{(k)}\right)$ .

步骤3 若 $p$ 维向量 $\beta^{(k)}$ 和 $\beta^{(k - 1)}$ 的距离 $||\beta^{(k)} - \beta^{(k - 1)}|| \leqslant \varepsilon,$ 其中 $\varepsilon$ 是预先给定的临界值, 迭代结束; 否则继续迭代.

一般地, 坐标轴下降法会收敛到局部最优解. 幸运的是, 对于凸函数, 局部最优解即为全局最优解. 理论上可以证明, Lasso 回归估计的坐标轴下降法可以收敛到全局最优解. 不过坐标轴下降法的收敛速度可以进一步提高. 最小角回归法有更好的效果.

最小角回归法与向前法的思想比较接近. 以2维为例, 其主要思想如图5.3.3所示: 设 $y$ 与 $x_{1}$ 之间的夹角比与 $x_{2}$ 的更小, 即 $y$ 与 $x_{1}$ 的相关性更大, 则沿着 $x_{1}$ 的方向走, 走到 $x_{1}$ 使 $x_{2}$ 和当前残差相关性相等的地方, 开始沿着 $x_{1}, x_{2}$ 的角平分线前进, 即图中 $\mu_{2}$ 的方向, 直到与 $y$ 最靠近之处停止. 这里可选择Pearson相关系数, 其在数值上等于角的余弦值. 由解析几何可知, 两向量同方向, 夹角为0, 余弦值为1, Pearson相关系数为1, 若两向量垂直, 则余弦值与Pearson相关系数为0; 若完全反方向, 则余弦值与Pearson相关系数为-1. 因此, 夹角越小, 说明相关性越大.

![](../../raw/pages_0241-0256/images/page_254_image_12.jpg)

<details>
<summary>text_image</summary>

x₂
x₂
y
μ₂=β₂(x₁+x₂)
O
μ₁=β₁x₁
x₁
</details>

图5.3.3 Lasso回归的最小角回归法的示意图

类似地, 对于 $p$ 维情形, 所有的 $p$ 个参数都从 0 开始, 首先找到与响应变量 $y$ 最相关的预测变量 $x$, 比如 $x_1$; 接着, 朝着这个预测变量的方向尽可能地迈出最大的一步, 直到另一个预测变量, 比如 $x_2$, 它与当前残差有与 $x_1$ 相同的相关性. 此时, 沿着 $x_1$ 和 $x_2$

---

5.3 变量选择

243

这两者的角平分线前进, 直到第三个变量  $x_{3}$  与当前残差有与  $x_{1}, x_{2}$  相同的相关性, 然后沿着  $x_{1}, x_{2}, x_{3}$  的角平分线前进; 直到第四个变量进入, 然后以同样的方式继续下去. 由于每次都沿着角平分线前进, 其为最小角方向, 故称为最小角回归. 给定样本  $\{(x_{i1}, x_{i2}, \cdots, x_{ip}, y_{i}), i = 1, 2, \cdots, n\}$  后, 最小角回归法的详细步骤如下所示.

## 算法 5.5 (Lasso 回归估计的最小角回归法)

步骤 1 标准化协变量, 使每个协变量变化后的均值都为 0, 其平方和为 1. 设初始残差向量  $r = y - \bar{y}$ , 令  $\beta_{1}, \beta_{2}, \cdots, \beta_{p}$  的初始值均为 0.

步骤 2 找出与 r 最相关的协变量  $x_{j}$ .

步骤 3 把  $\beta_{j}$  从 0 沿着最小二乘估计系数  $\langle x_{j}, r \rangle$  的方向移动, 直到当前残差和其他协变量  $x_{k}$  的相关性跟其与  $x_{j}$  的相关性相同.

步骤 4 把  $\beta_{j}$  和  $\beta_{k}$  沿着当前残差与  $(x_{j}, x_{k})$  的最小二乘估计系数的方向移动，直到与另一个协变量  $x_{l}$  有同样的相关性.

步骤 5 若某个估计系数接近 0, 则把该变量剔除, 并重新计算其他已选入的变量的最小二乘估计, 得到新的方向.

步骤 6 持续上述过程, 直到 p 个协变量都被考虑. 经过  $\min\{n-1,p\}$  步后, 得到保留的协变量的估计系数.

在算法 5.5 中, 步骤 3 是和向前法不同的, 向前法是把  $\beta_{j}$  从 0 变为最小二乘估计系数  $\langle x_{j}, r \rangle$ , 而最小角回归法中  $\beta_{j}$  从 0 沿着最小二乘估计系数  $\langle x_{j}, r \rangle$  的方向移动, 可能不到  $\langle x_{j}, r \rangle$  时, 就改变方向了. 步骤 5 中, 当某个变量相应的系数接近 0 时, 即把该变量剔除, 从而起到变量选择的效果. 步骤 6 中, 迭代步数与样本量 n 和维数 p 有关, 可使得每步的最小二乘估计的系数是有意义的.

在 Lasso 回归估计中, 目标函数 (5.3.15) 中的参数 $\lambda$ 严重影响估计结果. 当 $\lambda$ 很大时, 把各参数基本上都压缩到 0; 当 $\lambda$ 很小时, 参数会趋于最小二乘估计. $\lambda$ 的选择是 Lasso 回归估计中重要的问题. 一般地, 按照预测均方误差准则来选择最优的 $\lambda$, 例如可考虑 $k$-折叠交叉验证方法. 该方法的主要思路如下: 把 $n$ 个样本均分为 $k$ 份. 给定某个 $\lambda$ 之后, 每次用 $k-1$ 份样本得到参数 $\beta$ 的估计 $\hat{\beta}_{\lambda}$, 从而用剩下的那一份样本得到预测误差; 这样, 每次选不同的 $k-1$ 份样本估计参数, 再得到剩下那份样本的预测误差; 从而, 可得到每一份样本上的预测误差, 综合而成为该 $\lambda$ 对应的预测误差; 选择不同的 $\lambda$ 得到不同的预测误差, 故往往选择使预测误差最小的 $\lambda$ 为所求的 $\lambda$. 有时, 也取 $\lambda$ 使预测误差稍大些从而可剔除更多的变量. 通常选 $k=5$ 或 10.

例 5.3.4 设  $x_{1}, x_{2}, \cdots, x_{8}$  独立且均服从标准正态分布, 令

$$
y = 2 x _ {2} - 3 x _ {4} + 3 x _ {7} + \varepsilon ,
$$

---

244

第五章 线性模型与logistic回归

其中  $\varepsilon \sim N(0, \sigma^{2})$ ，即协变量  $x_{1}, x_{3}, x_{5}, x_{6}, x_{8}$  是不显著的。分别取  $\sigma = 0.2$  和 2，产生 100 个随机样本。应用 Lasso 回归估计，并用 10-折叠交叉验证方法。图 5.3.4(a) 给出  $\sigma = 0.2$  的情形，其横坐标  $\lambda$  取了  $\ln$  变换，图形上方的数字  $1 \sim 8$  的位置表示随着  $\lambda$  的减少，第几个变量进入模型。当随机误差方差比较小时，随着  $\lambda$  逐渐变小，对参数  $\beta$  的约束越来越小， $\beta_{2}, \beta_{4}$  和  $\beta_{7}$  逐渐往其真值靠拢，而其他不显著的变量的参数也接近 0.10-折叠交叉验证的结果显示，使预测误差最小的  $\lambda = 0.0074$ ，对应于图中 “minMSE” 处，这时选入线性模型的变量个数为 5 个，剔除了 3 个变量。若取  $\lambda$  使预测误差控制在离最小值的 1 倍标准差，即  $\lambda$  为图中 “1SE” 处，此时  $\lambda = 0.0434$ ，且恰好保留了 3 个重要变量。类似地，图 5.3.4(b) 给出  $\sigma = 2$  的情形，使预测误差最小的  $\lambda = 0.0367$ ，使预测均方误差控制在离最小值的 1 倍标准差的  $\lambda = 0.5445$ ；前者保留了全部 8 个变量，而后者保留了 3 个重要变量。此外，图 5.3.5 给出  $\sigma = 2$  时，用 10-折叠交叉验证得到不同  $\lambda$  的预测均方误差。从中可知， $\lambda$  严重影响预测效果。不过  $\lambda$  从取 “1SE” 处后，预测 MSE 变化不大。

![](../../raw/pages_0257-0272/images/page_256_chart_3.jpg)

<details>
<summary>contour</summary>

| \(\lambda\) | Curve 1 (Top) | Curve 2 (Middle) | Curve 3 (Bottom) |
| --- | --- | --- | --- |
| ~0.5 | 0 | 0 | 0 |
| ~0.2 | 3 | 2 | -3 |
| ~0.01 | 3 | 2 | -3 |
| ~0.001 | 3 | 2 | -3 |
</details>

(a) $\sigma = 0.2$

![](../../raw/pages_0257-0272/images/page_256_chart_5.jpg)

<details>
<summary>line</summary>

| \(\lambda\) | Series 1 (Top) | Series 2 | Series 3 | Series 4 | Series 5 (Bottom) |
| --- | --- | --- | --- | --- | --- |
| 10^0 | 0 | 0 | 0 | 0 | 0 |
| ~10^-0.5 | ~2.5 | ~1.1 | ~0.1 | ~-0.1 | ~-0.2 |
| ~10^-1 | ~3.0 | ~1.4 | ~0.3 | ~-0.3 | ~-0.4 |
| ~10^-2 | ~3.0 | ~1.4 | ~0.3 | ~-0.3 | ~-0.4 |
| ~10^-3 | ~3.0 | ~1.4 | ~0.3 | ~-0.3 | ~-0.4 |
</details>

(b) $\sigma = 2$

图5.3.4 例5.3.4的Lasso回归结果

![](../../raw/pages_0257-0272/images/page_256_chart_8.jpg)

<details>
<summary>error_bar</summary>

| \(\lambda\) | MSE |
| --- | --- |
| ~0.2 | ~30 |
| ~0.25 | ~28 |
| ~0.3 | ~26 |
| ~0.4 | ~23 |
| ~0.5 | ~21 |
| ~0.6 | ~19 |
| ~0.7 | ~17 |
| ~0.8 | ~15 |
| ~0.9 | ~14 |
| ~1.0 | ~12 |
| ~1.2 | ~10 |
| ~1.4 | ~9 |
| ~1.6 | ~8 |
| ~1.8 | ~7 |
| ~2.0 | ~6 |
| ~2.5 | ~5 |
| ~3.0 | ~4.5 |
| ~4.0 | ~4.5 |
| ~5.0 | ~4.5 |
| ~6.0 | ~4.5 |
| ~8.0 | ~4.5 |
| ~10.0 | ~4.5 |
| ~20.0 | ~4.5 |
| ~30.0 | ~4.5 |
| ~40.0 | ~4.5 |
| ~50.0 | ~4.5 |
| ~60.0 | ~4.5 |
| ~80.0 | ~4.5 |
| ~100.0 | ~4.5 |
| ~200.0 | ~4.5 |
| ~300.0 | ~4.5 |
| ~400.0 | ~4.5 |
| ~500.0 | ~4.5 |
| ~600.0 | ~4.5 |
| ~800.0 | ~4.5 |
| ~1000.0 | ~4.5 |
| ~2000.0 | ~4.5 |
| ~3000.0 | ~4.5 |
| ~4000.0 | ~4.5 |
| ~5000.0 | ~4.5 |
| ~6000.0 | ~4.5 |
| ~8000.0 | ~4.5 |
| ~10000.0 | ~4.5 |
| ~20000.0 | ~4.5 |
| ~30000.0 | ~4.5 |
| ~40000.0 | ~4.5 |
| ~50000.0 | ~4.5 |
| ~60000.0 | ~4.5 |
| ~80000.0 | ~4.5 |
| ~100000.0 | ~4.5 |
| ~200000.0 | ~4.5 |
| ~300000.0 | ~4.5 |
| ~400000.0 | ~4.5 |
| ~500000.0 | ~4.5 |
| ~600000.0 | ~4.5 |
| ~800000.0 | ~4.5 |
| ~1000000.0 | ~4.5 |
| ~2000000.0 | ~4.5 |
| ~3000000.0 | ~4.5 |
| ~4000000.0 | ~4.5 |
| ~5000000.0 | ~4.5 |
| ~6000000.0 | ~4.5 |
| ~8000000.0 | ~4.5 |
| ~10000000.0 | ~4.5 |
| ~20000000.0 | ~4.5 |
| ~30000000.0 | ~4.5 |
| ~40000000.0 | ~4.5 |
| ~50000000.0 | ~4.5 |
| ~60000000.0 | ~4.5 |
| ~80000000.0 | ~4.5 |
| ~10^3 | 4~35 (minMSE) |
</details>

图5.3.5 例5.3.4中 $\sigma = 2$ 时Lasso回归的预测误差

---

5.3 变量选择

245

由例 5.3.4 可知, Lasso 回归估计可以起到变量选择的效果, 而参数  $\lambda$  严重影响预测效果. 一般地, Lasso 回归估计可把显著的变量选出来, 不过保留的协变量个数往往比真实的参数个数稍多, 即部分不显著的变量也被纳入回归模型. 对于变量个数达到几百、几千甚至几万的情形, 这个缺点尤为突出. 此外, 在 Lasso 回归估计的求解路径中, 对于  $n \times p$  的设计矩阵, 最多只能选出  $\min\{n, p\}$  个变量, 当 p > n 时, 最多只能选出 n 个预测变量, 因此, 对于 p > n 的情况, Lasso 回归估计方法不能很好地选出真实模型.

为此, 不同的研究人员对 (5.3.6) 式中的惩罚项  $p(\beta)$  做了其他定义, 使估计效果更好. 例如, Zou et al. (2005) 提出弹性网 (elastic net) 回归方法, 其惩罚项为岭回归估计和 Lasso 回归估计的惩罚项的加权, 即

$$
p (\boldsymbol {\beta}) = \lambda \left[ \alpha \parallel \boldsymbol {\beta} \parallel_ {1} + (1 - \alpha) \parallel \boldsymbol {\beta} \parallel^ {2} \right],
$$

其中权重 $\alpha \in [0,1]$. 当 $\alpha = 0$ 时, 弹性网回归即为岭回归; 当 $\alpha = 1$ 时, 弹性网回归即为 Lasso 回归. 因此, 弹性网回归兼有 Lasso 回归和岭回归的优点, 既能达到变量选择的目的, 又具有对重要特征选择的作用. 此外, Fan et al. (2001) 提出了 SCAD (smoothly clipped absolute deviation) 这一变量选择的新方法, 其惩罚函数为

$$
p (\boldsymbol {\beta}) = \sum_ {i = 1} ^ {p} p _ {\lambda} (| \beta_ {i} |),
$$

其中函数 $p_{\lambda}(\beta)$ 的导函数为

$$
p _ {\lambda} ^ {\prime} (\beta) = \lambda \left[ I (\beta \leqslant \lambda) + \frac {(a \lambda - \beta) _ {+}}{(a - 1) \lambda} I (\beta > \lambda) \right],
$$

且 $a > 2, \beta > 0$. 这里 $I(\cdot)$ 是示性函数,

$$
b _ {+} = \left\{ \begin{array}{l l} b, & b > 0, \\ 0, & \text {否则}. \end{array} \right.
$$

对于该惩罚函数中的两个参数 $\lambda$ 和 $a$, 可以通过交叉验证来得到. 不过该文中也给出了一个较为通用的值, $\lambda = \sqrt{2\ln(p)}$, 在 $p < 100$ 时, 可取 $a = 3.7$. 他们证明了在该惩罚函数下, 兼具变量选择一致性和与经典最小二乘估计相同的收敛速度. 前者是指不仅可以把显著的变量选出来, 而且尽量避免不显著的变量被纳入模型. 不过由于 SCAD 回归模型的形式过于复杂, 以至于迭代算法运行速度较慢, 因此比较适合于维数在一百以内的情形; 此外, 该方法在低噪声水平的情况下表现较优, 但在高噪声水平的情况下表现一般. 除了前面提到的弹性网回归和 SCAD 回归, 人们还提出自适应 Lasso (adaptive Lasso) 回归、群组 Lasso (group Lasso) 回归等变量选择方法.

---

246

第五章 线性模型与logistic回归

在实际应用时, 没有一种变量选择算法是万能的. 对于不同的数据集, 需寻找合适的变量选择算法. 对于超高维的情形, 也有研究人员推荐把 Lasso 和 SCAD 两种方法结合起来使用, 即先用 Lasso 法在超高维的协变量中筛选出部分变量, 再用 SCAD 法筛选重要变量.

## 5.4 logistic 回归

前面讨论的回归模型中, 响应 $y$ 取值往往是连续的, 然而在实际应用中, 经常遇到 $y$ 是离散的情形, 即 $y$ 是分类数据. 最常见的是二分类问题, 即 $y$ 的取值仅为 0 和 1. 二分类的问题可以推广到多分类问题. 例如, 在疾病研究中, 经常需要分析疾病的发生与各危险因素之间的定量关系. 例如, 研究胃癌的发生与吸烟、饮酒、不良饮食习惯等危险因素的关系. 对于二分类问题, 由于响应 $y$ 为分类变量, 不满足正态分布和方差齐性等条件, 若采用多元线性回归分析, 则其预测值可能会大于 1 或小于 0, 从而无法给出合理的解释. logistic 回归模型较好地解决了上述问题. 由于该方法简单、实用、高效, 因此在医学、大数据分析等诸多领域都有十分广泛的应用. logistic 回归通常用于解决分类问题, 例如客户是否会购买某个商品, 借款人是否会违约等.

## 5.4.1 二分类

首先考虑 $y$ 取值为0和1的二分类问题. 给定数据集

$$
D = \{(\boldsymbol {x} _ {i}, y _ {i}): \boldsymbol {x} _ {i} = (x _ {i 1}, x _ {i 2}, \dots , x _ {i p}), y _ {i} \in \{0, 1 \}, i = 1, 2, \dots , n \},
$$

一个自然的做法是直接对该数据集用多元线性回归模型 (5.1.8) 式来拟合数据. 如图 5.4.1(a) 所示, 一个只有一个协变量的二分类数据, 若直接用线性回归模型来拟合, 得到的拟合模型

$$
\hat {f} (x) = - 0. 2 9 5 0 + 1. 4 3 3 7 x
$$

并不能保证其预测值落在 $[0,1]$，而且线性回归拟合的曲线似乎和数据点没有关系，从而没有意义。一种简单的处理方式是通过下面的阶跃函数:

$$
\hat {y} = \left\{ \begin{array}{l l} 1, & \hat {f} (x) > 0. 5, \\ 0, & \hat {f} (x) \leqslant 0. 5 \end{array} \right.
$$

把数据的预测值强行变为0或1. 对于该拟合数据，当 $x > 0.5545$ 时，令 $\hat{y} = 1$ ，否则 $\hat{y} = 0$ .然而，阶跃函数不是连续函数.为此，希望像线性回归的函数一样，使协变量

---

5.4 logistic 回归

247

和响应 $Y$ 之间的关系用一个单调可导的函数来描述. 常见的拟合函数为 sigmoid 函数:

$$
f (z) = \frac {1}{1 + \mathrm{e} ^ {- z}},
$$

该函数在机器学习中的神经网络中有诸多应用。该函数图形是一条S形曲线，如图5.4.1(b)所示，其有个平滑的过渡且可导。从中可见，sigmoid函数曲线将取值范围 $(-\infty ,\infty)$ 映射到(0,1).从而，sigmoid函数值更适宜表示预测的概率。

![](../../raw/pages_0257-0272/images/page_259_chart_5.jpg)

<details>
<summary>scatter</summary>

| x | y |
| --- | --- |
| ~0.1 | 0 |
| ~0.15 | 0 |
| ~0.18 | 0 |
| ~0.2 | 0 |
| ~0.25 | 0 |
| ~0.28 | 0 |
| ~0.3 | 0 |
| ~0.35 | 0 |
| ~0.45 | 0 |
| ~0.48 | 1.0 |
| ~0.5 | 1.0 |
| ~0.55 | 0 |
| ~0.58 | 0 |
| ~0.6 | 1.0 |
| ~0.7 | 1.0 |
| ~0.78 | 1.0 |
| ~0.8 | 1.0 |
| ~0.85 | 1.0 |
| ~0.9 | 1.0 |
| ~0.95 | 1.0 |
| ~0.98 | 1.0 |
</details>

(a)

![](../../raw/pages_0257-0272/images/page_259_chart_7.jpg)

<details>
<summary>line</summary>

| X | Y |
| --- | --- |
| -6 | 0 |
| -4 | ~0.02 |
| -2 | ~0.15 |
| 0 | 0.5 |
| 2 | ~0.85 |
| 4 | ~0.98 |
| 6 | 1.0 |
</details>

(b)

图 5.4.1 logistic 回归示意图

令 y 取值为 1 的概率为  $P(y=1|x)$ ，则  $P(y=0|x)=1-P(y=1|x)$ 。两者的比值称为几率 (odds)，其指该事件发生与不发生的概率比值。则对数几率为

$$
\ln (\text {odds}) = \ln \frac {P (y = 1 | \boldsymbol {x})}{1 - P (y = 1 | \boldsymbol {x})}.
$$

对于 p 维变量  $x_{1}, x_{2}, \cdots, x_{p}$ ，在不混淆的情形下，令  $\boldsymbol{x} = (x_{0}, x_{1}, \cdots, x_{p})^{\mathrm{T}}$ ，其中  $x_{0} = 1$ ， $\boldsymbol{\beta} = (\beta_{0}, \boldsymbol{\beta}_{1})^{\mathrm{T}}$ ， $\boldsymbol{\beta}_{1} = (\beta_{1}, \beta_{2}, \cdots, \beta_{p})^{\mathrm{T}}$ 。则线性回归项  $\boldsymbol{\beta}^{T}x = \beta_{0} + \beta_{1}x_{1} + \cdots + \beta_{p}x_{p}$ ，对线性回归项  $\beta^{T}x$  经过 sigmoid 函数变换后，令其为 y = 1 的概率，即

$$
P (y = 1 | \boldsymbol {x}) = \frac {1}{1 + \exp \{- \boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} \}} = \frac {\exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} \}}{1 + \exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} \}}.
$$

因此，

$$
P (y = 0 | \boldsymbol {x}) = 1 - P (y = 1 | \boldsymbol {x}) = \frac {1}{1 + \exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} \}},
$$

且

$$
\ln \frac {P (y = 1 | \boldsymbol {x})}{1 - P (y = 1 | \boldsymbol {x})} = \boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {p} x _ {p}, \tag {5.4.1}
$$

---

248

第五章 线性模型与logistic回归

该式即为 logistic 回归模型, 即输出 $y = 1$ 的对数几率由输入 $\pmb{x}$ 的线性函数表示. 当 (5.4.1) 式右边的取值越接近 $+\infty$ 时, $y = 1$ 的概率越接近 1. 因此 logistic 回归的思路是, 先拟合决策边界, 再建立这个边界与分类的概率联系, 从而得到二分类情况下的概率.

给定数据集 $D$ 后, 需要估计 logistic 回归模型 (5.4.1) 的参数 $\beta$. 下面考虑最大似然估计方法. 由于 $P(y = 1|\pmb{x})$ 与 $\beta$ 有关, 为方便记, 可设 $P(y = 1|\pmb{x}) = P(y = 1|\pmb{x}, \beta) = p(\pmb{x}, \beta)$, 则 $P(y = 0|\pmb{x}) = 1 - p(\pmb{x}, \beta)$, 且 $P(y|\pmb{x}, \beta) = [p(\pmb{x}, \beta)]^y [1 - p(\pmb{x}, \beta)]^{1 - y}$. 因此, 似然函数为

$$
L (\boldsymbol {\beta}) = \prod_ {i = 1} ^ {n} [ p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) ] ^ {y _ {i}} [ 1 - p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) ] ^ {1 - y _ {i}}. \tag {5.4.2}
$$

相应的对数似然函数为

$$
l (\boldsymbol {\beta}) = \ln L (\boldsymbol {\beta}) = \sum_ {i = 1} ^ {n} \{y _ {i} \ln p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) + (1 - y _ {i}) \ln [ 1 - p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) ] \}.
$$

把 $p(\pmb{x}_i,\beta)$ 的表达式代入 $l(\beta)$ 可得

$$
l (\boldsymbol {\beta}) = \sum_ {i = 1} ^ {n} \left[ y _ {i} \boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} _ {i} - \ln (1 + \exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}) \right].
$$

为了最大化  $l(\beta)$ ，将上式分别对  $\beta_{0}, \beta_{1}, \cdots, \beta_{p}$  求偏导并令其为 0。由于

$$
\begin{array}{l} \frac {\partial l (\boldsymbol {\beta})}{\partial \beta_ {j}} = \sum_ {i = 1} ^ {n} y _ {i} x _ {i j} - \sum_ {i = 1} ^ {n} \frac {x _ {i j} \exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}}{1 + \exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}} = \sum_ {i = 1} ^ {n} y _ {i} x _ {i j} - \sum_ {i = 1} ^ {n} p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) x _ {i j} \\ = \sum_ {i = 1} ^ {n} x _ {i j} [ y _ {i} - p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) ], \quad j = 0, 1, \dots , p, \\ \end{array}
$$

写成矩阵形式, 可得

$$
\frac {\partial l (\boldsymbol {\beta})}{\partial \boldsymbol {\beta}} = \sum_ {i = 1} ^ {n} \boldsymbol {x} _ {i} [ y _ {i} - p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) ],
$$

因此, 最大似然估计即为求解这  $p + 1$  个非线性方程

$$
\frac {\partial l (\boldsymbol {\beta})}{\partial \beta_ {j}} = 0, \quad j = 0, 1, \dots , p.
$$

该方程组没有显式解, 其可通过 Newton-Raphson (牛顿-拉弗森) 算法求解. 为此, 求出它的二阶导数, 即得

$$
\frac {\partial^ {2} l (\boldsymbol {\beta})}{\partial \beta_ {j} \partial \beta_ {k}} = - \sum_ {i = 1} ^ {n} \frac {(1 + \exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}) \exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \} x _ {i j} x _ {i k} - (\exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}) ^ {2} x _ {i j} x _ {i k}}{(1 + \exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}) ^ {2}}
$$

---

5.4 logistic 回归

249

$$
\begin{array}{l} = - \sum_ {i = 1} ^ {n} \left[ x _ {i j} x _ {i k} p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) - x _ {i j} x _ {i k} p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) ^ {2} \right] \\ = - \sum_ {i = 1} ^ {n} x _ {i j} x _ {i k} p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) [ 1 - p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) ]. \\ \end{array}
$$

从而其Hesse(黑塞)矩阵为

$$
\frac {\partial^ {2} l (\boldsymbol {\beta})}{\partial \boldsymbol {\beta} \partial \boldsymbol {\beta} ^ {\mathrm{T}}} = - \sum_ {i = 1} ^ {n} \boldsymbol {x} _ {i} \boldsymbol {x} _ {i} ^ {\mathrm{T}} p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) [ 1 - p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) ].
$$

从某个  $\beta^{old}$  开始, 一个 Newton-Raphson 更新如下:

$$
\boldsymbol {\beta} ^ {\mathrm{new}} = \boldsymbol {\beta} ^ {\mathrm{old}} - \left[ \frac {\partial^ {2} l (\boldsymbol {\beta})}{\partial \boldsymbol {\beta} \partial \boldsymbol {\beta} ^ {\mathrm{T}}} \right] ^ {- 1} \frac {\partial l (\boldsymbol {\beta})}{\partial \boldsymbol {\beta}},
$$

其中的导数是在 $\beta^{\mathrm{old}}$ 处计算的. 这个迭代过程可用矩阵来表示. 令 $\pmb{y}$ 为响应 $y_{i}$ 组成的列向量, $X$ 为 $n \times (p + 1)$ 系数矩阵, $\pmb{p}$ 为 $n$ 维向量且其第 $i$ 个元素为 $p(\pmb{x}_i, \beta^{\mathrm{old}})$, $W$ 为 $n \times n$ 对角矩阵且其第 $i$ 个对角元素为 $p(\pmb{x}_i, \beta^{\mathrm{old}})[1 - p(\pmb{x}_i, \beta^{\mathrm{old}})]$. 则可得

$$
\frac {\partial l (\boldsymbol {\beta})}{\partial \boldsymbol {\beta}} = X ^ {\mathrm{T}} (\boldsymbol {y} - \boldsymbol {p}),
$$

$$
\frac {\partial^ {2} l (\boldsymbol {\beta})}{\partial \boldsymbol {\beta} \partial \boldsymbol {\beta} ^ {\mathrm{T}}} = - X ^ {\mathrm{T}} W X.
$$

因此, Newton-Raphson 迭代式为

$$
\begin{array}{l} \boldsymbol {\beta} ^ {\mathrm{new}} = \boldsymbol {\beta} ^ {\mathrm{old}} + (X ^ {\mathrm{T}} W X) ^ {- 1} X ^ {\mathrm{T}} (\boldsymbol {y} - \boldsymbol {p}) \\ = (X ^ {\mathrm{T}} W X) ^ {- 1} X ^ {\mathrm{T}} W [ X \boldsymbol {\beta} ^ {\text {old}} + W ^ {- 1} (\boldsymbol {y} - \boldsymbol {p}) ] \\ = (X ^ {\mathrm{T}} W X) ^ {- 1} X ^ {\mathrm{T}} W \boldsymbol {z}, \\ \end{array}
$$

其中 $z \stackrel{\mathrm{def}}{=} X\beta^{\mathrm{old}} + W^{-1}(\pmb{y} - \pmb{p})$。因此，求解logistic回归模型参数的迭代过程如算法5.6所示。

## 算法 5.6 (logistic 回归模型参数的最大似然估计迭代算法)

步骤 1 令初始值  $\beta = 0$ .

步骤 2 计算 p, 其元素为

$$
p (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) = \frac {\exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}}{1 + \exp \{\boldsymbol {\beta} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}}, \quad i = 1, 2, \dots , n.
$$

步骤 3 计算对角矩阵 W, 其第 i 个对角元素为  $p(\boldsymbol{x}_{i}, \boldsymbol{\beta})[1 - p(\boldsymbol{x}_{i}, \boldsymbol{\beta})], i = 1, 2, \cdots, n.$

---

250

第五章 线性模型与logistic回归

步骤 4 令  $z = X\beta + W^{-1}(y - p)$ .

步骤 5 更新  $\boldsymbol{\beta}=(X^{\mathrm{T}}WX)^{-1}X^{\mathrm{T}}W\boldsymbol{z}$ .

步骤 6 若满足停止准则, 则中止算法; 否则回到步骤 2.

在算法 5.6 的步骤 6 中, 停止准则可定义为更新后的  $\beta$  与更新前的没有太多变化, 即  $\left|\left|\boldsymbol{\beta}^{\mathrm{new}}-\boldsymbol{\beta}^{\mathrm{old}}\right|\right|<\varepsilon$ , 其中  $\varepsilon$  为给定的小常数. 由算法 5.6 可知, logistic 回归模型参数的最大似然估计通过 Newton-Raphson 迭代算法容易求出. 得到模型参数的估计  $\hat{\beta}$  之后, 则概率  $P(y=1|x)$  和  $P(y=0|x)$  的估计分别为

$$
p (\boldsymbol {x}, \hat {\boldsymbol {\beta}}) = \frac {\exp \{\hat {\boldsymbol {\beta}} ^ {\mathrm{T}} \boldsymbol {x} \}}{1 + \exp \{\hat {\boldsymbol {\beta}} ^ {\mathrm{T}} \boldsymbol {x} \}}, 1 - p (\boldsymbol {x}, \hat {\boldsymbol {\beta}}) = \frac {1}{1 + \exp \{\hat {\boldsymbol {\beta}} ^ {\mathrm{T}} \boldsymbol {x} \}}.
$$

显然, 给定样本 x, 当  $\beta^{T}x > 0$  时, 相应的  $\hat{y} = 1$ ; 否则  $\hat{y} = 0$ . 因此, 确定响应变量 y 属于哪一类的判别边界仍是一个线性函数.

例 5.4.1 对于某个具有两个协变量的二分类数据, 根据算法 5.6 得到  $\beta$  的估计  $\hat{\boldsymbol{\beta}} = (0.7679, -0.6816, -0.3664)^{\mathrm{T}}$ , 从而

$$
P (y = 1 | \boldsymbol {x}) = \frac {\exp \{0 . 7 6 7 9 - 0 . 6 8 1 6 x _ {1} - 0 . 3 6 6 4 x _ {2} \}}{1 + \exp \{0 . 7 6 7 9 - 0 . 6 8 1 6 x _ {1} - 0 . 3 6 6 4 x _ {2} \}},
$$

$$
P (y = 0 | \boldsymbol {x}) = \frac {1}{1 + \exp \{0 . 7 6 7 9 - 0 . 6 8 1 6 x _ {1} - 0 . 3 6 6 4 x _ {2} \}},
$$

且对数几率

$$
\ln (\text {odds}) = 0. 7 6 7 9 - 0. 6 8 1 6 x _ {1} - 0. 3 6 6 4 x _ {2}.
$$

因此, 对于给定样本 x, 其判别函数为

$$
\hat {y} = \left\{ \begin{array}{l l} 1, & 0. 7 6 7 9 - 0. 6 8 1 6 x _ {1} - 0. 3 6 6 4 x _ {2} > 0, \\ 0, & \text {否则}. \end{array} \right.
$$

由该式可知, 判别边界是一个线性函数.

由例 5.4.1 可知, logistic 回归模型可用于解决二分类的问题. 此外, 若某个协变量  $x_{i}$  是定类数据, 则可对其进行伪变量处理. logistic 回归模型中估计的参数有直观解释. 例如, 在研究肺癌与吸烟、饮酒的关系时, 设响应 y 表示是否患肺癌, 吸烟  $x_{1}$  和饮酒  $x_{2}$  为协变量. 令 y=1 表示患肺癌, y=0 表示未患肺癌;  $x_{1}=1$  表示吸烟,  $x_{1}=0$  表示不吸烟;  $x_{2}=1$  表示饮酒,  $x_{2}=0$  表示不饮酒. 实际上, 吸烟和饮酒这两个变量都是定性变量, 经  $x_{1}$  和  $x_{2}$  这样设定后变为伪变量, 可代入 logistic 回归模型中进行回归. 根据数据, 假设得到如下的 logistic 回归模型:

$$
\ln (\text {odds}) = \hat {\beta} _ {0} + \hat {\beta} _ {1} x _ {1} + \hat {\beta} _ {2} x _ {2},
$$

---

5.4 logistic 回归

251

此时, 模型中各参数的解释如下: $\hat{\beta}_0$ 表示不吸烟且不饮酒的人患肺癌与不患肺癌概率之比的对数值; 控制饮酒因素后, 吸烟者患肺癌的概率是不吸烟者的 $\exp \{\hat{\beta}_1\}$ 倍; 控制吸烟因素后, 饮酒者患肺癌的概率是不饮酒者的 $\exp \{\hat{\beta}_2\}$ 倍. 由此可见, logistic 回归模型在医学中可以很好地解释二分类的问题, 因此得以大量应用.

进一步地, 需要检验 logistic 回归模型 (5.4.1) 是否显著. 此时, 原假设和备择假设分别如下:

$$
H _ {0}: \beta_ {1} = \beta_ {2} = \dots = \beta_ {p} = 0 \leftrightarrow H _ {1}: \text {至少存在某个} i, \beta_ {i} \neq 0.
$$

似然比检验法是检验上述问题的常用方法. 似然比检验统计量 $G$ 为

$$
G = - 2 (\ln L _ {1} - \ln L _ {0}).
$$

其中  $L_{1}$  为 (5.4.2) 式包含所有协变量  $\beta_{0}, \beta_{1}, \cdots, \beta_{p}$  的回归模型的似然函数， $L_{0}$  为仅包含常数项  $\beta_{0}$  的回归模型的似然函数。根据似然比检验理论，可知在原假设  $H_{0}$  成立时，G 统计量的极限分布服从自由度为 p 的  $\chi^{2}$  分布。从而，给定样本后，可得相应的 p 值。若 p 值小于给定的显著性水平  $\alpha$ ，则该 logistic 回归模型是显著的。当模型显著时，还需对模型中的每一个协变量的回归系数进行假设检验，以检验每个协变量是否显著，其原假设和备择假设分别如下所示:

$$
H _ {0}: \beta_ {j} = 0 \leftrightarrow H _ {1}: \beta_ {j} \neq 0.
$$

常用的假设检验方法为 Wald  $\chi^{2}$  检验, 相应的检验统计量为

$$
\chi^ {2} = (\hat {\beta} _ {j} / S _ {\hat {\beta} _ {j}}) ^ {2},
$$

其中 $S_{\hat{\beta}_j}$ 为 $\hat{\beta}_j$ 的估计标准差. 在原假设 $H_0$ 成立时, Wald $\chi^2$ 检验统计量服从自由度为1的 $\chi^2$ 分布.

## 5.4.2 多分类

在实际应用中, 经常遇到多分类的情形, 即最终的分类结果中类别数会大于 2. 例如, 新闻可以分为体育、财经、其他等三个类别, 目标是根据某一个用户的各种特征, 判断其更喜欢哪一类新闻. 这是一个典型的多分类任务.

一般地, 对于多分类问题, 设类别为  $\{1,2,\cdots,K\}$ . 对于任一点 x, 可以估计其落入每个类的概率, 从而可以定义一个判别函数 G 如下:

$$
\hat {G} (\boldsymbol {x}) = \arg \max _ {k} P (G = k | \boldsymbol {x}),
$$

---

252

第五章 线性模型与logistic回归

即判别函数 $G$ 是依据最大概率原则来确定其分类. 由于响应 $y$ 为多类别数据, 研究协变量 $\pmb{x}$ 对 $y$ 的影响时, 通常做两两比较来得到相对信息. 对于第 $k$ 和第 $l$ 类, 其判别边界为

$$
P (G = k | \boldsymbol {x}) = P (G = l | \boldsymbol {x}).
$$

对上式两边都除以 $P(G = l|\pmb{x})$ 并取对数，可得

$$
\ln {\frac {P (G = k | \boldsymbol {x})}{P (G = l | \boldsymbol {x})}} = 0.
$$

若希望判别边界是线性的, 则类似于 (5.4.1) 式的二分类 logistic 模型, 可设

$$
\ln \frac {P (G = k | \boldsymbol {x})}{P (G = l | \boldsymbol {x})} = a _ {0} ^ {(k, l)} + \sum_ {j = 1} ^ {p} a _ {j} ^ {(k, l)} x _ {j}.
$$

显然, 给定某个样本 x, 其一定属于某个类, 因此对于不同的  $(k, l)$ ,  $a^{(k, l)}$  之间存在某些约束, 故可设

$$
\ln \frac {P (G = j | \boldsymbol {x})}{P (G = K | \boldsymbol {x})} = \boldsymbol {\beta} _ {j} ^ {\mathrm{T}} \boldsymbol {x}, \quad j = 1, 2, \dots , K - 1, \tag {5.4.3}
$$

其中  $\beta_{j}^{T}x=\beta_{j0}+\beta_{j1}x_{1}+\cdots+\beta_{jp}x_{p}$ . 称 (5.4.3) 式为多分类 logistic 模型. 从而, 对于任一对  $(k,l)$ , 有

$$
\ln \frac {P (G = k | \boldsymbol {x})}{P (G = l | \boldsymbol {x})} = (\boldsymbol {\beta} _ {k} - \boldsymbol {\beta} _ {l}) ^ {\mathrm{T}} \boldsymbol {x}.
$$

因此, 只需以第 K 类作为基准, 考虑其他 K-1 类与第 K 类的比较, 就可以得到任意对  $(k,l)$  之间的关系. 从而, 在整个模型中需要估计的参数个数为  $(K-1)(p+1)$ , 记为  $\boldsymbol{\beta}=\{\beta_{10},\beta_{11},\cdots,\beta_{1p},\beta_{20},\beta_{21},\cdots,\beta_{2p},\cdots,\beta_{(K-1)0},\beta_{(K-1)1},\cdots,\beta_{(K-1)p}\}$ . 易得

$$
P (G = k | \boldsymbol {x}) = \frac {\exp \{\boldsymbol {\beta} _ {k} ^ {\mathrm{T}} \boldsymbol {x} \}}{1 + \sum_ {l = 1} ^ {K - 1} \exp \{\boldsymbol {\beta} _ {l} ^ {\mathrm{T}} \boldsymbol {x} \}}, \quad k = 1, 2, \dots , K - 1,
$$

$$
P (G = K | \boldsymbol {x}) = \frac {1}{1 + \sum_ {l = 1} ^ {K - 1} \exp \{\boldsymbol {\beta} _ {l} ^ {\mathrm{T}} \boldsymbol {x} \}}.
$$

显然, $\sum_{k=1}^{K}P(G=k|\boldsymbol{x})=1.$

给定样本  $\{(\boldsymbol{x}_{i}, g_{i}), i = 1, 2, \cdots, N\}$ ，其中类别  $g_{i} \in \{1, 2, \cdots, K\}$ ，令  $P(G = g_{i} | \boldsymbol{x}_{i}) = P(G = g_{i} | \boldsymbol{x}_{i}, \boldsymbol{\beta}) = p_{g_{i}} (\boldsymbol{x}_{i}, \boldsymbol{\beta})$ 。则对数最大似然估计为

$$
l (\boldsymbol {\beta}) = \sum_ {i = 1} ^ {N} \ln p _ {g _ {i}} (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) = \sum_ {i = 1} ^ {N} \ln \frac {\exp \{\boldsymbol {\beta} _ {g _ {i}} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}}{1 + \sum_ {l = 1} ^ {K - 1} \exp \{\boldsymbol {\beta} _ {l} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}}
$$

---

5.4 logistic 回归

253

$$
= \sum_ {i = 1} ^ {N} \left[ \boldsymbol {\beta} _ {g _ {i}} ^ {\mathrm{T}} \boldsymbol {x} _ {i} - \ln \left(1 + \sum_ {l = 1} ^ {K - 1} \exp \{\boldsymbol {\beta} _ {l} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}\right) \right].
$$

类似于二分类的情形, 用 Newton-Raphson 算法求解. 令 $I(\cdot)$ 为示性函数, 即条件满足时取值为 1, 否则为 0. 则 $l(\beta)$ 的一阶偏导数为

$$
\begin{array}{l} \frac {\partial l (\boldsymbol {\beta})}{\partial \beta_ {k j}} = \sum_ {i = 1} ^ {N} \left[ I (g _ {i} = k) x _ {i j} - \frac {\exp \{\boldsymbol {\beta} _ {k} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \} x _ {i j}}{1 + \sum_ {l = 1} ^ {K - 1} \exp \{\boldsymbol {\beta} _ {l} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}} \right] \\ = \sum_ {i = 1} ^ {N} x _ {i j} \left[ I (g _ {i} = k) - p _ {k} (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) \right], \\ \end{array}
$$

而二阶偏导数为

$$
\begin{array}{l} \frac {\partial^ {2} l (\boldsymbol {\beta})}{\partial \beta_ {k j} \partial \beta_ {m n}} \\ = - \sum_ {i = 1} ^ {N} x _ {i j} \frac {1}{\left(1 + \sum_ {l = 1} ^ {K - 1} \exp \{\boldsymbol {\beta} _ {l} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \}\right) ^ {2}}. \\ \left[ - \exp \{\boldsymbol {\beta} _ {k} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \} I (k = m) x _ {i n} \bigg (1 + \sum_ {l = 1} ^ {K - 1} \exp \{\boldsymbol {\beta} _ {l} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \} \bigg) + \exp \{\boldsymbol {\beta} _ {k} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \} \exp \{\boldsymbol {\beta} _ {m} ^ {\mathrm{T}} \boldsymbol {x} _ {i} \} x _ {i n} \right] \\ = \sum_ {i = 1} ^ {N} x _ {i j} x _ {i n} \left[ - p _ {k} (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) I (k = m) + p _ {k} (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) p _ {m} (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) \right] \\ = - \sum_ {i = 1} ^ {N} x _ {i j} x _ {i n} p _ {k} (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) \left[ I (k = m) - p _ {m} (\boldsymbol {x} _ {i}, \boldsymbol {\beta}) \right]. \\ \end{array}
$$

上述式子也可以用矩阵形式表示. 令 y 是下面由示性函数构成的  $N(K-1)$  维列向量,

$$
\boldsymbol {y} = \left( \begin{array}{c} \boldsymbol {y} _ {1} \\ \boldsymbol {y} _ {2} \\ \vdots \\ \boldsymbol {y} _ {K - 1} \end{array} \right), \quad \boldsymbol {y} _ {k} = \left( \begin{array}{c} I (g _ {1} = k) \\ I (g _ {2} = k) \\ \vdots \\ I (g _ {N} = k) \end{array} \right), 1 \leqslant k \leqslant K - 1.
$$

令 p 为  $N(K-1)$  维的拟合概率

$$
\boldsymbol {p} = \left( \begin{array}{c} \boldsymbol {p} _ {1} \\ \boldsymbol {p} _ {2} \\ \vdots \\ \boldsymbol {p} _ {K - 1} \end{array} \right), \boldsymbol {p} _ {k} = \left( \begin{array}{c} p _ {k} (\boldsymbol {x} _ {1}, \boldsymbol {\beta}) \\ p _ {k} (\boldsymbol {x} _ {2}, \boldsymbol {\beta}) \\ \vdots \\ p _ {k} (\boldsymbol {x} _ {N}, \boldsymbol {\beta}) \end{array} \right), 1 \leqslant k \leqslant K - 1.
$$

---

254

第五章 线性模型与logistic回归

记 $X$ 为 $N \times (p + 1)$ 的系数矩阵, $\tilde{\mathbf{X}}$ 为 $N(K - 1) \times (p + 1)(K - 1)$ 的块对角矩阵:

$$
\tilde {\boldsymbol {X}} = \left( \begin{array}{c c c c} X & 0 & \dots & 0 \\ 0 & X & \dots & 0 \\ \vdots & \vdots & & \vdots \\ 0 & 0 & \dots & X \end{array} \right).
$$

令 W 为  $N(K-1) \times N(K-1)$  的方阵:

$$
W = \left( \begin{array}{c c c c} W _ {1 1} & W _ {1 2} & \dots & W _ {1 (K - 1)} \\ W _ {2 1} & W _ {2 2} & \dots & W _ {2 (K - 1)} \\ \vdots & \vdots & & \vdots \\ W _ {(K - 1) 1} & W _ {(K - 1) 2} & \dots & W _ {(K - 1) (K - 1)} \end{array} \right),
$$

其中 $W_{km}, 1 \leqslant k, m \leqslant K - 1$ 为 $N \times N$ 的对角矩阵，且当 $k = m$ 时，$W_{kk}$ 的第 $i$ 个对角元素为 $p_k(\boldsymbol{x}_i, \boldsymbol{\beta}^{\mathrm{old}})[1 - p_k(\boldsymbol{x}_i, \boldsymbol{\beta}^{\mathrm{old}})]$，当 $k \neq m$ 时，$W_{km}$ 的第 $i$ 个对角元素为 $-p_k(\boldsymbol{x}_i, \boldsymbol{\beta}^{\mathrm{old}}) p_m(\boldsymbol{x}_i, \boldsymbol{\beta}^{\mathrm{old}})$. 从而，类似于二分类问题，可得

$$
\frac {\partial l (\boldsymbol {\beta})}{\partial \boldsymbol {\beta}} = \tilde {\boldsymbol {X}} ^ {\mathrm{T}} (\boldsymbol {y} - \boldsymbol {p}),
$$

$$
\frac {\partial^ {2} l (\boldsymbol {\beta})}{\partial \boldsymbol {\beta} \partial \boldsymbol {\beta} ^ {\mathrm{T}}} = - \tilde {\boldsymbol {X}} ^ {\mathrm{T}} \boldsymbol {W} \tilde {\boldsymbol {X}},
$$

则  $\beta^{new}$  的更新式子和二分类的一样, 即

$$
\boldsymbol {\beta} ^ {\mathrm{new}} = (\tilde {\boldsymbol {X}} ^ {\mathrm{T}} \boldsymbol {W} \tilde {\boldsymbol {X}}) ^ {- 1} \tilde {\boldsymbol {X}} ^ {\mathrm{T}} \boldsymbol {W} \boldsymbol {z},
$$

其中 $z \stackrel{\mathrm{def}}{=} \tilde{X} \beta^{\mathrm{old}} + W^{-1}(y - p)$, 或等价地,

$$
\boldsymbol {\beta} ^ {\mathrm{new}} = \boldsymbol {\beta} ^ {\mathrm{old}} + (\tilde {\boldsymbol {X}} ^ {\mathrm{T}} \boldsymbol {W} \tilde {\boldsymbol {X}}) ^ {- 1} \tilde {\boldsymbol {X}} ^ {\mathrm{T}} (\boldsymbol {y} - \boldsymbol {p}).
$$

由此, 可类似于算法 5.6, 得到多分类的迭代算法. 此外, 多分类 logistic 回归模型的显著性检验类似于二分类的情形.

对于多分类 logistic 回归模型 (5.4.3) 中回归参数进行物理解释时, 需要做两两比较, 即可以把第 $K$ 类作为基准, 再用类似于二分类模型的解释方法. 此外, 在实际应用中, 若响应 $y$ 的类别个数较多, 例如为 10 个, 则可对类别进行某种组合, 以减少类别数量, 从而便于后续进行分析.

---

习题五

255

## 习题五

1. 下面是 7 个地区 2000 年的人均国内生产总值 (GDP) 和人均消费水平的统计数据:

| 地区 | 北京 | 辽宁 | 上海 | 江西 | 河南 | 贵州 | 陕西 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 人均GDP/元 | 22 460 | 11 226 | 34 547 | 4 851 | 5 444 | 2 662 | 4 549 |
| 人均消费水平/元 | 7 326 | 4 490 | 11 546 | 2 396 | 2 208 | 1 608 | 2 035 |

(1) 人均 GDP 作协变量, 人均消费水平作响应, 绘制散点图, 并说明二者之间的关系形态;
(2) 计算两个变量之间的线性相关系数, 说明两个变量之间的关系强度;
(3) 求出估计的回归方程, 并解释回归系数的实际意义;
(4) 计算  $R^{2}$ ，并解释其意义；
(5) 检验回归方程线性关系的显著性 ( $\alpha = 0.05$ );
(6) 如果某地区的人均 GDP 为 5 000 元, 预测其人均消费水平;
(7) 求人均 GDP 为 5 000 元时, 人均消费水平 95% 的置信区间和预测区间.

2. 设 $H = X(X^{\mathrm{T}}X)^{-1}X^{\mathrm{T}}$ 是秩为 $k$ 的 $n \times n$ 矩阵 ($n \geqslant k$), 试证明

(1) H 是秩为 k 的投影矩阵;
(2)  $I_{n}-H$  是秩为 n-k 的投影矩阵, 其中  $I_{n}$  为 n 阶单位矩阵;
(3) $H(I_{n}-H)=0.$

3. 对于拟合模型

$$
y = \beta x ^ {2} + \varepsilon ,
$$

试根据数据  $(x_{i}, y_{i}), i = 1, 2, \cdots, n,$  估计参数  $\beta,$  并证明给出的估计为最小二乘估计.

4. 对于随机样本  $\{(x_{i}, y_{i}), i = 1, 2, \cdots, n\}$ ，对协变量进行中心化，得到一元线性回归模型

$$
y _ {i} = \alpha + (x _ {i} - \bar {x}) \beta + \varepsilon_ {i}, i = 1, 2, \dots , n.
$$

其中  $\bar{x}$  为协变量的样本均值. 求  $\alpha$  和  $\beta$  的最小二乘估计.

5. 一个试验容器靠蒸汽供应热量, 使其保持恒温, 协变量 X 表示容器周围空气单位时间的平均温度 (单位: ℃), Y 表示单位时间内消耗的蒸汽量 (单位: L). 观测了 25 个单位时间的数据如表 5.1 所示.

---

256

第五章 线性模型与logistic回归

表 5.1 容器蒸汽量数据

| 序号 | Y | X | 序号 | Y | X | 序号 | Y | X |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 10.98 | 35.3 | 10 | 9.14 | 57.5 | 19 | 6.83 | 70.0 |
| 2 | 11.13 | 29.7 | 11 | 8.24 | 46.4 | 20 | 8.88 | 74.5 |
| 3 | 12.51 | 30.8 | 12 | 12.19 | 28.9 | 21 | 7.68 | 72.1 |
| 4 | 8.40 | 58.8 | 13 | 11.88 | 28.1 | 22 | 8.47 | 58.1 |
| 5 | 9.27 | 61.4 | 14 | 9.57 | 39.1 | 23 | 8.86 | 44.6 |
| 6 | 8.73 | 71.3 | 15 | 10.94 | 46.8 | 24 | 10.36 | 33.4 |
| 7 | 6.36 | 74.4 | 16 | 9.58 | 48.5 | 25 | 11.08 | 28.6 |
| 8 | 8.50 | 76.7 | 17 | 10.09 | 59.3 |  |  |  |
| 9 | 7.82 | 70.7 | 18 | 8.11 | 70.0 |  |  |  |

画出散点图, 并估计相应的一元线性回归模型.

6. 表 5.2 是教育学家测试的 21 个儿童的记录, 其中 x 是儿童的年龄 (以月为单位), y 表示某种智力指标. 通过这些数据, 建立智力随年龄变化的关系.

表 5.2 智力指标数据

| 序号 | x | y | 序号 | x | y | 序号 | x | y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 15 | 95 | 8 | 11 | 100 | 15 | 11 | 102 |
| 2 | 26 | 71 | 9 | 8 | 104 | 16 | 10 | 100 |
| 3 | 10 | 83 | 10 | 10 | 94 | 17 | 12 | 105 |
| 4 | 9 | 91 | 11 | 7 | 113 | 18 | 42 | 57 |
| 5 | 15 | 102 | 12 | 9 | 96 | 19 | 17 | 121 |
| 6 | 20 | 87 | 13 | 10 | 83 | 20 | 11 | 86 |
| 7 | 18 | 93 | 14 | 11 | 84 | 21 | 10 | 100 |

7. 证明定理 5.2.6.
8. 证明残差平方和 $SS_{E} = Y^{\mathrm{T}}\left[\mathbf{1}_{n} - X(X^{\mathrm{T}}X)^{-1}X^{\mathrm{T}}\right]Y$，且 $\hat{\sigma}^2 = SS_E / (n - p - 1)$ 是 $\sigma^2$ 的无偏估计.
9. 考虑求出 k 个物体的质量  $\mu_{1}, \mu_{2}, \cdots, \mu_{k}$ . 一种方法是将每个物体称 m 次再求平均. 假定称量的误差方差都为  $\sigma^{2}$ . 用  $y_{ij}$  表示第 i 个物体第 j 次称量时得到的质量,  $i = 1, 2, \cdots, k; j = 1, 2, \cdots, m$ .

(1) 试写出相应的线性模型;
(2) 求出  $\mu_{i}$  的最小二乘估计  $\hat{\mu}_{i}$ ;
(3) 计算  $\mathrm{Var}(\hat{\mu}_{i})$ .

10. 设 $y_{1} = 2a + b + e_{1}$, $y_{2} = 2a - b + e_{2}$, $y_{3} = a + b + e_{3}$, 其中 $a, b$ 为未知参数, $e_{1}, e_{2}, e_{3}$ 相互独立, $E(e_{i}) = 0, \mathrm{Var}(e_{i}) = \sigma^{2}, i = 1, 2, 3$. 试求出 $a, b$ 的最小二乘

---

习题五

257

估计.

11. 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自  $N(\theta, \sigma^{2})$  的独立同分布样本, 求  $\theta$  的最小方差线性无偏估计  $\hat{\theta}$ , 并求  $\mathrm{Var}(\hat{\theta})$ .
12. 研究用电高峰时居民家庭每时的用电量 $y$ 与每月总用电量 $x$ 之间的关系, 收集的 53 户居民某月用电记录如表 5.3 所示.

表 5.3 用电高峰时居民家庭数据

| 序号 | x | y | 序号 | x | y | 序号 | x | y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 679 | 0.79 | 19 | 1 748 | 4.88 | 37 | 745 | 0.77 |
| 2 | 292 | 0.44 | 20 | 1 381 | 3.48 | 38 | 435 | 1.39 |
| 3 | 1 012 | 0.56 | 21 | 1 428 | 7.58 | 39 | 540 | 0.56 |
| 4 | 493 | 0.79 | 22 | 1 255 | 2.63 | 40 | 874 | 1.56 |
| 5 | 582 | 2.70 | 23 | 1 777 | 4.99 | 41 | 1 543 | 5.28 |
| 6 | 1 156 | 3.64 | 24 | 370 | 0.59 | 42 | 1 029 | 0.64 |
| 7 | 997 | 4.73 | 25 | 2 316 | 8.19 | 43 | 710 | 4.00 |
| 8 | 2 189 | 9.50 | 26 | 1 130 | 4.79 | 44 | 1 434 | 0.31 |
| 9 | 1 097 | 5.34 | 27 | 463 | 4.51 | 45 | 837 | 4.20 |
| 10 | 2 078 | 6.85 | 28 | 770 | 1.74 | 46 | 468 | 0.64 |
| 11 | 1 818 | 5.84 | 29 | 724 | 4.10 | 47 | 1 114 | 1.90 |
| 12 | 1 700 | 5.21 | 30 | 808 | 3.94 | 48 | 413 | 0.51 |
| 13 | 747 | 3.25 | 31 | 790 | 0.96 | 49 | 1 787 | 8.33 |
| 14 | 2 030 | 4.43 | 32 | 783 | 3.24 | 50 | 3 560 | 14.94 |
| 15 | 1 643 | 3.16 | 33 | 406 | 0.44 | 51 | 1 495 | 5.11 |
| 16 | 414 | 0.50 | 34 | 1 242 | 3.24 | 52 | 2 221 | 3.85 |
| 17 | 354 | 0.17 | 35 | 658 | 2.14 | 53 | 1 526 | 3.93 |
| 18 | 127 4 | 1.88 | 36 | 1 746 | 5.71 |  |  |  |

试编程完成下面的统计分析:

(1) 应用最小二乘法估计回归模型;
(2) 以拟合值 $\hat{y}_i$ 为横坐标, 残差 $\hat{\varepsilon}_i$ 为纵坐标, 作残差图, 分析 Gauss-Markov 条件对本例的适用性;
(3) 考虑响应的变换 $U = y^{1/2}$，再对新变量 $U$ 和 $x$ 重复 (1) 和 (2) 的统计分析；
(4) 考虑响应 y 的 Box-Cox 变换如下:

$$
y (\lambda) = \left\{ \begin{array}{l l} \frac {y ^ {\lambda} - 1}{\lambda}, & y \neq 0, \\ \ln y, & y = 0, \end{array} \right.
$$

---

258

第五章 线性模型与logistic回归

其中  $\lambda$  为待估参数. Box-Cox 变换引入参数  $\lambda$ , 可以一定程度上减小不可观测的误差和预测变量的相关性, 可以明显地改善数据的正态性、对称性和方差相等性. 估计参数  $\lambda$  的通常方法是假设经过转换后的响应服从正态分布, 再画出关于  $\lambda$  的似然函数, 使其最大的  $\lambda$  即为估计值. 查询 Box-Cox 变换的相关理论后编程实现, 并做讨论.

13. 对于随机样本  $\{(x_{i1}, x_{i2}, \cdots, x_{ip}, y_i), i = 1, 2, \cdots, n\}$ ，若对协变量中心化，即设  $X_j = (x_{1j}, x_{2j}, \cdots, x_{nj})^{\mathrm{T}}, \bar{x}_j = \frac{1}{n} \sum_{i=1}^{n} x_{ij}, X_c = (X_1 - \bar{x}_1 \mathbf{1}_n, X_2 - \bar{x}_2 \mathbf{1}_n, \cdots, X_p - \bar{x}_p \mathbf{1}_n)$ ，则对于中心化的线性模型

$$
Y = \alpha \mathbf {1} _ {n} + X _ {c} \boldsymbol {\beta} + \varepsilon , \tag {5.1}
$$

其中  $Y = (y_{1}, y_{2}, \cdots, y_{n})^{\mathrm{T}}, \boldsymbol{\beta} = (\beta_{1}, \beta_{2}, \cdots, \beta_{p})^{\mathrm{T}}$ ，令  $\hat{\alpha} = \bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_{i}, \hat{\beta} = (X_{c}^{\mathrm{T}} X_{c})^{-1} X_{c}^{\mathrm{T}} Y$ ，证明

(1) $E(\hat{\alpha}) = \alpha, E(\hat{\beta}) = \beta;$
(2) $\mathrm{Cov}\left( \begin{array}{c}\hat{\alpha}\\ \hat{\beta} \end{array} \right) = \sigma^{2}\left( \begin{array}{cc}\frac{1}{n} & 0\\ 0 & (X_{c}^{\mathrm{T}}X_{c})^{-1} \end{array} \right);$
(3) 若进一步假设 $\varepsilon \sim N(0, \sigma^2 I_n)$, 则

$$
\hat {\alpha} \sim N \left(\alpha , \frac {\sigma^ {2}}{n}\right), \hat {\beta} \sim N (\boldsymbol {\beta}, \sigma^ {2} (X _ {c} ^ {\mathrm{T}} X _ {c}) ^ {- 1}).
$$

14. 根据经验知, 在人的身高相等的条件下, 其血压的收缩压 y 与体重  $x_{1}$ 、年龄  $x_{2}$  有关. 现收集了 13 名男子的测量数据如表 5.4 所示.

表 5.4 男子测量数据

| 序号 | $x_1$ | $x_2$ | y | 序号 | $x_1$ | $x_2$ | y |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 152 | 50 | 120 | 8 | 158 | 50 | 125 |
| 2 | 183 | 20 | 141 | 9 | 170 | 40 | 132 |
| 3 | 171 | 20 | 124 | 10 | 153 | 55 | 123 |
| 4 | 165 | 30 | 126 | 11 | 164 | 40 | 132 |
| 5 | 158 | 30 | 117 | 12 | 190 | 40 | 155 |
| 6 | 161 | 50 | 125 | 13 | 185 | 20 | 147 |
| 7 | 149 | 60 | 123 |  |  |  |  |

(1) 根据线性回归模型 (5.2.2), 建立 $y$ 关于 $x_{1}, x_{2}$ 的线性回归方程. 给出相应的方差分析表, 并计算 $R^{2}$.

---

习题五

259

(2) 根据中心化线性回归模型 (5.1), 建立 y 关于  $x_{1}, x_{2}$  的线性回归方程. 给出相应的方差分析表, 计算  $R^{2}$ , 并与未中心化的线性模型做比较.

15. 对于线性回归模型 (5.2.3)，设参数  $\beta$  的最小二乘估计为  $\hat{\beta}$ ，令残差向量  $\hat{\varepsilon} = Y - \hat{Y}$ ，其中  $\hat{Y} = (X^{\mathrm{T}} X)^{-1} X^{\mathrm{T}} Y$ ，证明

(1)  $E(\hat{\varepsilon}) = \varepsilon, \operatorname{Var}(\hat{\varepsilon}) = \sigma^{2}(I_{n} - H)$ , 其中 H 为帽子矩阵;
(2) 若进一步假设 $\varepsilon \sim N(\mathbf{0}, \sigma^2 I_n)$, 则

$$
\hat {\varepsilon} \sim N (\varepsilon , \sigma^ {2} (I _ {n} - H)).
$$

16. 对于正态线性模型

$$
y = X \boldsymbol {\beta} + \varepsilon , \quad \varepsilon \sim N (\mathbf {0}, \sigma^ {2} I _ {n}),
$$

证明  $\beta$  的最小二乘估计与最大似然估计是一致的.

17. 对于回归模型 (5.2.3), 若增加约束条件

$$
H \beta = c,
$$

其中 $H$ 为 $q \times (p + 1)$ 矩阵, $\pmb{c}$ 为 $q$ 维向量, 证明

(1) $\beta$ 的最小二乘估计为

$$
\hat {\boldsymbol {\beta}} _ {H} = \hat {\boldsymbol {\beta}} + (X ^ {\mathrm{T}} X) ^ {- 1} H ^ {\mathrm{T}} [ H (X ^ {\mathrm{T}} X) ^ {- 1} H ^ {\mathrm{T}} ] ^ {- 1} (\boldsymbol {c} - H \hat {\boldsymbol {\beta}}),
$$

其中  $\hat{\beta}$  为无约束时  $\beta$  的最小二乘估计;

(2) 有约束时的残差平方和不小于无约束时的残差平方和;
(3) $\mathrm{Var}(\hat{\beta}_H) = \sigma^2 (X^{\mathrm{T}}X)^{-1}\left\{I_n - H^{\mathrm{T}}[H(X^{\mathrm{T}}X)^{-1}H^{\mathrm{T}}]^{-1}H(X^{\mathrm{T}}X)^{-1}\right\}.$

18. 研究一地区土壤内所含植物可给态磷 $y$ 的情况, 观测数据如表 5.5 所示, 其中 $x_{1}$ 是土壤内所含无机磷浓度; $x_{2}$ 是土壤内溶于 $\mathrm{K}_{2} \mathrm{CO}_{3}$ 溶液并受溴化物水解的有机磷; $x_{3}$ 是土壤内溶于 $\mathrm{K}_{2} \mathrm{CO}_{3}$ 溶液, 但不溶于溴化物的有机磷. $y$ 是在 $35^{\circ} \mathrm{C}$ 土壤内的植物可给态磷.

(1) 求 y 对  $x_{1}, x_{2}, x_{3}$  的线性回归模型, 并估计误差方差  $\sigma^{2}$ ;
(2) 给出相应的方差分析表;
(3) 检验每个协变量是否显著.

19. 对于表 5.5 的土壤数据, 考虑二次回归模型 (5.3.1),

(1) 分别应用向前法、向后法和逐步回归法得到相应的回归方程, 并通过  $R^{2}$  等准则做比较;
(2) 应用 Lasso 方法做变量选择, 得到相应的回归方程.

---

260

第五章 线性模型与logistic回归

表 5.5 土壤数据

| 序号 | x1 | x2 | x3 | y | 序号 | x1 | x2 | x3 | y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.4 | 52 | 158 | 64 | 10 | 12.6 | 58 | 112 | 51 |
| 2 | 0.4 | 23 | 163 | 60 | 11 | 10.9 | 37 | 111 | 76 |
| 3 | 3.1 | 19 | 37 | 71 | 12 | 23.1 | 46 | 114 | 96 |
| 4 | 0.6 | 34 | 157 | 61 | 13 | 23.1 | 50 | 134 | 77 |
| 5 | 4.7 | 24 | 59 | 54 | 14 | 21.6 | 44 | 73 | 93 |
| 6 | 1.7 | 65 | 123 | 77 | 15 | 23.1 | 56 | 168 | 95 |
| 7 | 9.4 | 44 | 46 | 81 | 16 | 1.9 | 36 | 143 | 54 |
| 8 | 10.1 | 31 | 117 | 93 | 17 | 26.8 | 58 | 202 | 168 |
| 9 | 11.6 | 29 | 173 | 93 | 18 | 29.9 | 51 | 124 | 99 |

20. 在网络上查找一个样本数不少于 1 000, 变量个数不少于 10 的数据集, 建立多元线性回归模型, 分别应用向前法、向后法、逐步回归法、Lasso 方法得到相应的估计模型, 并做比较.
21. 假设已知 $x_{1}, x_{2}$ 与 $y$ 的关系服从线性回归模型

$$
y = 1 0 + 2 x _ {1} + 3 x _ {2} + \varepsilon .
$$

给定  $x_{1}, x_{2}$  的 10 个值, 如下所示:

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $x_1$ | 1.1 | 1.4 | 1.7 | 1.7 | 1.8 | 1.8 | 1.9 | 2.0 | 2.3 | 2.4 |
| $x_2$ | 1.1 | 1.5 | 1.8 | 1.7 | 1.9 | 1.8 | 1.8 | 2.1 | 2.4 | 2.5 |
| $\varepsilon$ | 0.8 | -0.5 | 0.4 | -0.5 | 0.2 | 1.9 | 1.9 | 0.6 | -1.5 | -1.5 |
| y | 16.3 | 16.8 | 19.2 | 18.0 | 19.5 | 20.9 | 21.1 | 20.9 | 20.3 | 22.0 |

(1) 假设回归系数与误差项未知, 用普通最小二乘法求回归系数的估计值;
(2) 判断协变量之间是否存在多重共线性;
(3) 画出这两个协变量的岭迹图;
(4) 确定合适的参数  $\lambda$ ，并得到相应岭估计回归模型.

22. 表 5.6 是研究法国经济问题时收集的 1949 年至 1959 年共 11 年的数据, 其中响应为进口总额 y, 三个协变量分别为国内生产总值  $x_{1}$ 、储蓄量  $x_{2}$ 、总消费量  $x_{3}$  (单位均为 10 亿法郎).

(1) 直接估计线性回归模型, 给出方差分析表, 并判断该模型是否合适;
(2) 判断协变量之间是否存在多重共线性;

---

习题五

261

(3) 画出这三个协变量的岭迹图;
(4) 确定合适的参数  $\lambda$ ，并得到相应岭估计回归模型.

表 5.6 法国经济数据

| 年份 | x1 | x2 | x3 | y | 年份 | x1 | x2 | x3 | y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1949 | 149.3 | 4.2 | 108.1 | 15.9 | 1955 | 202.1 | 2.1 | 146.0 | 22.7 |
| 1950 | 171.5 | 4.1 | 114.8 | 16.4 | 1956 | 212.4 | 5.6 | 154.1 | 26.5 |
| 1951 | 175.5 | 3.1 | 123.2 | 19.0 | 1957 | 226.1 | 5.0 | 162.3 | 28.1 |
| 1952 | 180.8 | 3.1 | 126.9 | 19.1 | 1958 | 231.9 | 5.1 | 164.3 | 27.6 |
| 1953 | 190.7 | 1.1 | 132.1 | 18.8 | 1959 | 239.0 | 0.7 | 167.6 | 26.3 |
| 1954 | 202.1 | 2.2 | 137.7 | 20.4 |  |  |  |  |  |

23. 在一次住房展销会上, 与房地产商签订初步购房意向书的共有 313 名顾客, 在随后的 3 个月的时间内, 只有一部分顾客确实购买了房屋. 购买了房屋的顾客记为 1, 没有购买房屋的顾客记为 0. 以顾客的家庭年收入为协变量 $x$, 家庭年收入按照高低不同分成了 9 组, 具体数据如表 5.7 所示.

表 5.7 顾客数据

| 序号 | 家庭年收入x/万元 | 签订意向书人数$n_i$ | 实际购房人数$m_i$ |
| --- | --- | --- | --- |
| 1 | 3.5 | 25 | 8 |
| 2 | 5.5 | 32 | 13 |
| 3 | 7.5 | 58 | 26 |
| 4 | 9.5 | 52 | 22 |
| 5 | 11.5 | 43 | 20 |
| 6 | 13.5 | 39 | 22 |
| 7 | 15.5 | 28 | 16 |
| 8 | 17.5 | 21 | 12 |
| 9 | 19.5 | 15 | 15 |

(1) 试通过 logistic 模型建立签订意向的顾客最终买房的概率与家庭年收入之间的关系, 以分析家庭年收入对最终购买住房的影响;
(2) 估计一个家庭年收入为 15 万元的顾客签订意向书后最终买房与不买房的可能性大小之比值;
(3) 估计一个家庭年收入为 15 万元的顾客签订意向书后最终买房的赔率是年收入为 10 万元的顾客的多少倍.

24. 探讨肾细胞癌转移有关的因素研究中, 收集了 26 例进行根治性肾切除术患者的

---

262

第五章 线性模型与logistic回归

肾细胞癌标本资料 (表 5.8), 有关变量说明如下, 试进行 logistic 回归分析, 并得到相应结论:

$X_{1}$ : 确诊时患者的年龄 (岁);

$X_{2}$ :肾细胞癌血管内皮生长因子，其阳性表达由低到高共3个等级，分别赋值1、2、3；

$X_{3}$ : 肾细胞癌组织内微血管数;

$X_{4}$ : 肾细胞癌细胞核组织学分级, 由低到高共 4 级, 分别赋值 1、2、3、4;

$X_{5}$ : 肾细胞癌分期, 由低到高共 4 期, 分别赋值 1、2、3、4;

Y: 肾细胞癌转移情况, 有转移记为 1, 无转移记为 0.

表 5.8 患者标本资料

| 序号 | $X_1$ | $X_2$ | $X_3$ | $X_4$ | $X_5$ | Y | 序号 | $X_1$ | $X_2$ | $X_3$ | $X_4$ | $X_5$ | Y |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 59 | 2 | 43.4 | 2 | 1 | 0 | 14 | 31 | 1 | 47.8 | 2 | 1 | 0 |
| 2 | 36 | 1 | 57.2 | 1 | 1 | 0 | 15 | 36 | 3 | 31.6 | 3 | 1 | 1 |
| 3 | 61 | 2 | 190.0 | 2 | 1 | 0 | 16 | 42 | 1 | 66.2 | 2 | 1 | 0 |
| 4 | 58 | 3 | 128.0 | 4 | 3 | 1 | 17 | 14 | 3 | 138.6 | 3 | 3 | 1 |
| 5 | 55 | 3 | 80.0 | 3 | 4 | 1 | 18 | 32 | 1 | 114.0 | 2 | 3 | 0 |
| 6 | 61 | 1 | 94.4 | 2 | 1 | 0 | 19 | 35 | 1 | 40.2 | 2 | 1 | 0 |
| 7 | 38 | 1 | 76.0 | 1 | 1 | 0 | 20 | 70 | 3 | 177.2 | 4 | 3 | 1 |
| 8 | 42 | 1 | 240.0 | 3 | 2 | 0 | 21 | 65 | 2 | 51.6 | 4 | 4 | 1 |
| 9 | 50 | 1 | 74.0 | 1 | 1 | 0 | 22 | 45 | 2 | 124.0 | 2 | 4 | 0 |
| 10 | 58 | 3 | 68.6 | 2 | 2 | 0 | 23 | 68 | 3 | 127.2 | 3 | 3 | 1 |
| 11 | 68 | 3 | 132.8 | 4 | 2 | 0 | 24 | 31 | 2 | 124.8 | 2 | 3 | 0 |
| 12 | 25 | 2 | 94.6 | 4 | 3 | 1 | 25 | 58 | 1 | 128.0 | 4 | 3 | 0 |
| 13 | 52 | 1 | 56.0 | 1 | 1 | 0 | 26 | 60 | 3 | 149.8 | 4 | 3 | 1 |

25. 生物学家希望了解种子的发芽数 $y$ 是否受水分值 $x_{1}$ 及是否加盖 $x_{2}$ 的影响, 为此, 在加盖 $x_{2} = 1$ 与不加盖 $x_{2} = 0$ 两种情况下对不同水分值情况分别观察 100 粒种子是否发芽, 记录发芽数. 令 $y = 1$ 表示发芽, $y = 0$ 表示不发芽. 相应数据如表 5.9 所示.

(1) 建立关于  $x_{1}, x_{2}$  和  $x_{1}x_{2}$  的 logistic 回归方程;
(2) 分别求加盖与不加盖的情况下发芽率为 50% 的水分值;
(3) 在水分值为 4 的条件下, 分别估计加盖与不加盖的情况下发芽与不发芽的概率之比值, 并估计加盖对不加盖发芽的概率之比值.

---

习题五

263

表 5.9 种子数据

| 序号 | $x_1$ | $x_2$ | y | 频数 | 序号 | $x_1$ | $x_2$ | y | 频数 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0 | 1 | 24 | 11 | 1 | 1 | 1 | 43 |
| 2 | 1 | 0 | 0 | 76 | 12 | 1 | 1 | 0 | 57 |
| 3 | 3 | 0 | 1 | 46 | 13 | 3 | 1 | 1 | 75 |
| 4 | 3 | 0 | 0 | 54 | 14 | 3 | 1 | 0 | 25 |
| 5 | 5 | 0 | 1 | 67 | 15 | 5 | 1 | 1 | 76 |
| 6 | 5 | 0 | 0 | 33 | 16 | 5 | 1 | 0 | 24 |
| 7 | 7 | 0 | 1 | 78 | 17 | 7 | 1 | 1 | 52 |
| 8 | 7 | 0 | 0 | 22 | 18 | 7 | 1 | 0 | 48 |
| 9 | 9 | 0 | 1 | 73 | 19 | 9 | 1 | 1 | 37 |
| 10 | 9 | 0 | 0 | 27 | 20 | 9 | 1 | 0 | 63 |

---


