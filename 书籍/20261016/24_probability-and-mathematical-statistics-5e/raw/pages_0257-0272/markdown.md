## (一) 一元线性回归

设随机变量 Y 与 x 之间存在着某种相关关系. 这里, x 是可以控制或可以精确观察的变量, 如年龄、试验时的温度、施加的压力、电压与时间等. 换句话说我们可以随意指定 n 个值  $x_{1}, x_{2}, \cdots, x_{n}$ . 因此我们干脆不把 x 看成是随机变量, 而将它当作普通的变量. 本章中我们只讨论这种情况.

设随机变量 $Y$ （因变量）与普通变量$x$ （自变量）之间存在着相关关系，由于 $Y$ 是随机变量，对于 $x$ 的各个确定值， $Y$ 有它的分布（如图9-1，图中 $C_1,C_2$ 分别是$x_{1},x_{2}$ 处 $Y$ 的概率密度曲线).用 $F(y|x)$ 表示当 $x$ 取确定的 $x$ 值时，所对应的 $Y$ 的分布函数，如果我们掌握了 $F(y|x)$ 随着

![](images/page_256_image_5.jpg)

<details>
<summary>text_image</summary>

O
x₁
x₂
x
Y
C₁
μ(x₂)
C₂
</details>

图9-1

$x$ 的取值而变化的规律, 那么就能完全掌握 $Y$ 与 $x$ 之间的关系了. 然而这样做往往比较复杂. 作为一种近似, 我们转而去考察 $Y$ 的数学期望, 若 $Y$ 的数学期望 $E(Y)$ 存在, 则其值随 $x$ 的取值而定, 它是 $x$ 的函数. 将这一函数记为 $\mu_{Y|x}$ 或 $\mu(x)$, 称为 $Y$ 关于 $x$ 的回归函数 (如图9-1). 这样, 我们就将讨论 $Y$ 与 $x$ 的相关关系的问题转换为讨论 $E(Y) = \mu(x)$ 与 $x$ 的函数关系了.

我们知道, 若  $\eta$  是一个随机变量, 则  $E[(\eta-c)^{2}]$  作为 c 的函数, 在  $c=E(\eta)$  时  $E[(\eta-c)^{2}]$  达到最小(参见第四章习题第17题). 这表明在一切 x 的函数中以回归函数  $\mu(x)$  作为 Y 的近似, 其均方误差  $E[(Y-\mu(x))^{2}]$  为最小. 因此, 作为一种近似, 为了研究 Y 与 x 的关系转而去研究  $\mu(x)$  与 x 的关系是合适的.

在实际问题中, 回归函数  $\mu(x)$  一般是未知的, 回归分析的任务在于根据试验数据去估计回归函数, 讨论有关的点估计、区间估计、假设检验等问题. 特别重要的是对随机变量 Y 的观察值作出点预测和区间预测.

我们对于 x 取定一组不完全相同的值  $x_{1}, x_{2}, \cdots, x_{n}$ ，设  $Y_{1}, Y_{2}, \cdots, Y_{n}$  分别是在  $x_{1}, x_{2}, \cdots, x_{n}$  处对 Y 的独立观察结果，称

$$
(x _ {1}, Y _ {1}), (x _ {2}, Y _ {2}), \dots , (x _ {n}, Y _ {n}) \tag {3.1}
$$

是一个样本①,对应的样本值记为

$$
(x _ {1}, y _ {1}), (x _ {2}, y _ {2}), \dots , (x _ {n}, y _ {n}).
$$

我们首先要解决的问题是如何利用样本来估计 $Y$ 关于 $x$ 的回归函数 $\mu(x)$. 为此，首先需要推测 $\mu (x)$ 的形式.在一些问题中，我们可以由专业知识知道 $\mu (x)$ 的形式.否则，可将每对观察值 $(x_{i},y_{i})$ 在直角坐标系中描出它的相应的点（如下例中的图9-2），这种图称为散点图.散点图可以帮助我们粗略地看出 $\mu (x)$ 的形式.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 这里  $Y_{1}, Y_{2}, \cdots, Y_{n}$  是相互独立的随机变量，但一般未必同分布，为方便计，也称  $(x_{1}, Y_{1}), (x_{2}, Y_{2}), \cdots, (x_{n}, Y_{n})$  是一个样本.</span></small>

例1 为研究某一化学反应过程中, 温度 $x$ (以 $\mathrm{^\circ C}$ 计) 对产品得率 $Y$ (以 $\%$ 计) 的影响, 测得数据如下:

| 温度x(°C) | 100 | 110 | 120 | 130 | 140 | 150 | 160 | 170 | 180 | 190 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 得率Y(%) | 45 | 51 | 54 | 61 | 66 | 70 | 74 | 78 | 85 | 89 |

这里自变量 $x$ 是普通变量，$Y$ 是随机变量. 画出散点图如图9-2所示. 由图大致看出 $\mu(x)$ 具有线性函数 $a + bx$ 的形式. □

设 $Y$ 关于 $x$ 的回归函数为 $\mu(x)$. 利用样本来估计 $\mu(x)$ 的问题称为求 $Y$ 关于 $x$ 的回归问题. 特别, 若 $\mu(x)$ 为线性函数: $\mu(x) = a + bx$, 此时估计 $\mu(x)$ 的问题称为求一元线性回归问题. 本节只讨论这个问题.

![](images/page_257_chart_7.jpg)

<details>
<summary>scatter</summary>

| x | y |
| --- | --- |
| 100 | ~46 |
| 110 | ~52 |
| 120 | ~55 |
| 130 | ~62 |
| 140 | ~68 |
| 150 | ~71 |
| 160 | ~76 |
| 170 | ~79 |
| 180 | ~86 |
| 190 | ~91 |
</details>

图9-2

我们假设对于 $x$ （在某个区间内）的每一个值有

$$
Y \sim N (a + b x, \sigma^ {2}),
$$

其中 $a, b$ 及 $\sigma^2$ 都是不依赖于 $x$ 的未知参数. 记 $\varepsilon = Y - (a + bx)$, 对 $Y$ 作这样的正态假设, 相当于假设

$$
Y = a + b x + \varepsilon , \quad \varepsilon \sim N (0, \sigma^ {2}), \tag {3.2}
$$

其中未知参数 $a, b$ 及 $\sigma^2$ 都不依赖于 $x$. (3.2) 称为一元线性回归模型, 其中 $b$ 称为回归系数.

(3.2) 式表明, 因变量 Y 由两部分组成, 一部分是 x 的线性函数  $a + bx$ , 另一部分  $\varepsilon \sim N(0, \sigma^{2})$  是随机误差, 是人们不可控制的.

## (二) $a, b$ 的估计

取 x 的 n 个不全相同的值  $x_{1}, x_{2}, \cdots, x_{n}$  作独立试验，得到样本  $(x_{1}, Y_{1}), (x_{2}, Y_{2}), \cdots, (x_{n}, Y_{n})$ . 由 (3.2) 式

$$
Y _ {i} = a + b x _ {i} + \varepsilon_ {i}, \varepsilon_ {i} \sim N (0, \sigma^ {2}), \text {各} \varepsilon_ {i} \text {相互独立}. \tag {3.3}
$$

于是  $Y_{i} \sim N(a + bx_{i}, \sigma^{2}), i = 1, 2, \cdots, n.$  由  $Y_{1}, Y_{2}, \cdots, Y_{n}$  的独立性，知  $Y_{1}, Y_{2}, \cdots, Y_{n}$  的联合概率密度为

$$
\begin{array}{l} L = \prod_ {i = 1} ^ {n} \frac {1}{\sigma \sqrt {2 \pi}} \exp \left\{- \frac {1}{2 \sigma^ {2}} (y _ {i} - a - b x _ {i}) ^ {2} \right\} \\ = \left(\frac {1}{\sigma \sqrt {2 \pi}}\right) ^ {n} \exp \left\{- \frac {1}{2 \sigma^ {2}} \sum_ {i = 1} ^ {n} (y _ {i} - a - b x _ {i}) ^ {2} \right\}. \tag {3.4} \\ \end{array}
$$

现用最大似然估计法来估计未知参数 a, b. 对于任意一组观察值  $y_{1}, y_{2}, \cdots, y_{n}$ ，(3.4) 式就是样本的似然函数. 显然，要 L 取最大值，只要 (3.4) 式右端花括弧中的平方和部分为最小，即只需函数

$$
Q (a, b) = \sum_ {i = 1} ^ {n} (y _ {i} - a - b x _ {i}) ^ {2} \tag {3.5}
$$

取最小值①.

取 $Q$ 分别关于 $a, b$ 的偏导数，并令它们等于零:

$$
\left. \begin{array}{l} \frac {\partial Q}{\partial a} = - 2 \sum_ {i = 1} ^ {n} (y _ {i} - a - b x _ {i}) = 0, \\ \frac {\partial Q}{\partial b} = - 2 \sum_ {i = 1} ^ {n} (y _ {i} - a - b x _ {i}) x _ {i} = 0. \end{array} \right\} \tag {3.6}
$$

得方程组

$$
\left\{ \begin{array}{l} n a + \left(\sum_ {i = 1} ^ {n} x _ {i}\right) b = \sum_ {i = 1} ^ {n} y _ {i}, \\ \left(\sum_ {i = 1} ^ {n} x _ {i}\right) a + \left(\sum_ {i = 1} ^ {n} x _ {i} ^ {2}\right) b = \sum_ {i = 1} ^ {n} x _ {i} y _ {i}. \end{array} \right. \tag {3.7}
$$

## (3.7) 式称为正规方程组.

由于 $x_{i}$ 不全相同，正规方程组的系数行列式

$$
\left| \begin{array}{c c} n & \sum_ {i = 1} ^ {n} x _ {i} \\ \sum_ {i = 1} ^ {n} x _ {i} & \sum_ {i = 1} ^ {n} x _ {i} ^ {2} \end{array} \right| = n \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - \left(\sum_ {i = 1} ^ {n} x _ {i}\right) ^ {2} = n \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} \neq 0.
$$

故(3.7)有唯一的一组解. 解得 $b, a$ 的最大似然估计值为

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 如果 $Y$ 不是正态变量，则直接用(3.5)式估计 $a, b$，使 $Y$ 的观察值 $y_{i}$ 与 $a + bx_{i}$ 偏差的平方和 $Q(a, b)$ 为最小。这种方法叫最小二乘法，它是求经验公式的一种常用方法。若 $Y$ 是正态变量，则最小二乘法与最大似然估计法给出相同的结果。</span></small>

$$
\left. \begin{array}{l} \hat {b} = \frac {n \sum_ {i = 1} ^ {n} x _ {i} y _ {i} - \left(\sum_ {i = 1} ^ {n} x _ {i}\right) \left(\sum_ {i = 1} ^ {n} y _ {i}\right)}{n \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - \left(\sum_ {i = 1} ^ {n} x _ {i}\right) ^ {2}} = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) (y _ {i} - \bar {y})}{\sum_ {i = 1} ^ {n} (x _ {i} - \bar {x}) ^ {2}}, \\ \hat {a} = \frac {1}{n} \sum_ {i = 1} ^ {n} y _ {i} - \frac {\hat {b}}{n} \sum_ {i = 1} ^ {n} x _ {i} = \bar {y} - \hat {b} \bar {x}, \end{array} \right\} \tag {3.8}
$$

其中 $\overline{x} = \frac{1}{n}\sum_{i = 1}^{n}x_{i},\quad \overline{y} = \frac{1}{n}\sum_{i = 1}^{n}y_{i}.$

在得到 $a, b$ 的估计 $\hat{a}, \hat{b}$ 后，对于给定的 $x$，我们就取 $\hat{a} + \hat{b}x$ 作为回归函数 $\mu(x) = a + bx$ 的估计，即 $\widehat{\mu(x)} = \hat{a} + \hat{b}x$，称为 $Y$ 关于 $x$ 的经验回归函数。记 $\hat{a} + \hat{b}x = \hat{y}$，方程

$$
\hat {y} = \hat {a} + \hat {b} x \tag {3.9}
$$

称为 $Y$ 关于 $x$ 的经验回归方程, 简称回归方程, 其图形称为回归直线.

将(3.8)中 $\hat{a}$ 的表达式代入(3.9)式,则回归方程可写成

$$
\hat {y} = \overline {{y}} + \hat {b} (x - \overline {{x}}). \tag {3.10}
$$

(3.10) 表明, 对于样本值  $(x_{1}, y_{1}), (x_{2}, y_{2}), \cdots, (x_{n}, y_{n})$ , 回归直线通过散点图的几何中心  $(\overline{x}, \overline{y})$ .

今后我们将视方便而使用(3.9)或(3.10).

为了计算上的方便,我们引入下述记号:

$$
\left. \begin{array}{l} S _ {x x} = \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} = \sum_ {i = 1} ^ {n} x _ {i} ^ {2} - \frac {1}{n} \Big (\sum_ {i = 1} ^ {n} x _ {i} \Big) ^ {2}, \\ S _ {y y} = \sum_ {i = 1} ^ {n} (y _ {i} - \overline {{y}}) ^ {2} = \sum_ {i = 1} ^ {n} y _ {i} ^ {2} - \frac {1}{n} \Big (\sum_ {i = 1} ^ {n} y _ {i} \Big) ^ {2}, \\ S _ {x y} = \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) (y _ {i} - \overline {{y}}) = \sum_ {i = 1} ^ {n} x _ {i} y _ {i} - \frac {1}{n} \Big (\sum_ {i = 1} ^ {n} x _ {i} \Big) \Big (\sum_ {i = 1} ^ {n} y _ {i} \Big). \end{array} \right\} \tag {3.11}
$$

这样， $a,b$ 的估计值可写成

$$
\left. \begin{array}{l} \hat {b} = \frac {S _ {x y}}{S _ {x x}}, \\ \hat {a} = \frac {1}{n} \sum_ {i = 1} ^ {n} y _ {i} - \left(\frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i}\right) \hat {b}. \end{array} \right\} \tag {3.12}
$$

例 2(续例 1) 设在例 1 中的随机变量 Y 符合 (3.2) 式所述的条件, 求 Y 关于 x 的线性回归方程.

解 现在 $n = 10$ ，为求线性回归方程，所需计算列表如下:

表9-17

| x | y | $x^{2}$ | $y^{2}$ | xy |
| --- | --- | --- | --- | --- |
| 100 | 45 | 10 000 | 2 025 | 4 500 |
| 110 | 51 | 12 100 | 2 601 | 5 610 |
| 120 | 54 | 14 400 | 2 916 | 6 480 |
| 130 | 61 | 16 900 | 3 721 | 7 930 |
| 140 | 66 | 19 600 | 4 356 | 9 240 |
| 150 | 70 | 22 500 | 4 900 | 10 500 |
| 160 | 74 | 25 600 | 5 476 | 11 840 |
| 170 | 78 | 28 900 | 6 084 | 13 260 |
| 180 | 85 | 32 400 | 7 225 | 15 300 |
| 190 | 89 | 36 100 | 7 921 | 16 910 |
| Σ 1 450 | 673 | 218 500 | 47 225$^{1}$ | 101 570 |

由表9-17得

$$
S _ {x x} = 2 1 8 5 0 0 - \frac {1}{1 0} \times 1 4 5 0 ^ {2} = 8 2 5 0,
$$

$$
S _ {x y} = 1 0 1 5 7 0 - \frac {1}{1 0} \times 1 4 5 0 \times 6 7 3 = 3 9 8 5,
$$

故得 $\hat{b} = \frac{S_{xy}}{S_{xx}} = 0.48303,$

$$
\hat {a} = \frac {1}{1 0} \times 6 7 3 - \frac {1}{1 0} \times 1 4 5 0 \times 0. 4 8 3 0 3 = - 2. 7 3 9 3 5,
$$

于是得到回归直线方程

$$
\hat {y} = - 2. 7 3 9 3 5 + 0. 4 8 3 0 3 x,
$$

或写成

$$
\hat {y} = 6 7. 3 + 0. 4 8 3 0 3 (x - 1 4 5).
$$

## (三) $\sigma^2$ 的估计

由(3.2)式，

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① $\sum_{i=1}^{n} y_i^2$ 的值下面要用到.</span></small>

$$
E \{[ Y - (a + b x) ] ^ {2} \} = E (\varepsilon^ {2}) = D (\varepsilon) + [ E (\varepsilon) ] ^ {2} = \sigma^ {2},
$$

这表示 $\sigma^2$ 愈小，以回归函数 $\mu(x) = a + bx$ 作为 $Y$ 的近似导致的均方误差就愈小。这样，利用回归函数 $\mu(x) = a + bx$ 去研究随机变量 $Y$ 与 $x$ 的关系就愈有效。然而 $\sigma^2$ 是未知的，因而我们需要利用样本去估计 $\sigma^2$。为了估计 $\sigma^2$，先引入下述残差平方和。

记 $\hat{y}_i = \hat{y}|_{x = x_i} = \hat{a} +\hat{b} x_i$ ，称 $y_{i} - \hat{y}_{i}$ 为 $x_{i}$ 处的残差.平方和

$$
Q _ {e} = \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) ^ {2} = \sum_ {i = 1} ^ {n} (y _ {i} - \hat {a} - \hat {b} x _ {i}) ^ {2} \tag {3.13}
$$

称为残差平方和(图9-3). 它是经验回归函数在 $x_{i}$ 处的函数值 $\mu (\widehat{x_i}) = \hat{a} +\hat{b} x_i$ 与 $x_{i}$ 处的观察值 $y_{i}$ 的偏差的平方和. 为了计算 $Q_{e}$, 我们将$Q_{e}$ 作如下的分解:

$$
\begin{array}{l} Q _ {e} = \sum_ {i = 1} ^ {n} (y _ {i} - \hat {y} _ {i}) ^ {2} = \sum_ {i = 1} ^ {n} [ y _ {i} - \overline {{y}} - \hat {b} (x _ {i} - \overline {{x}}) ] ^ {2} \\ = \sum_ {i = 1} ^ {n} (y _ {i} - \overline {{y}}) ^ {2} - 2 \hat {b} \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) (y _ {i} - \overline {{y}}) \\ + \hat {b} ^ {2} \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2} = S _ {y y} - 2 \hat {b} S _ {x y} + \hat {b} ^ {2} S _ {x x}. \\ \end{array}
$$

![](images/page_261_chart_8.jpg)

<details>
<summary>scatter</summary>

| X | Y |
| --- | --- |
| ~1.5 | ~2.5 |
| ~2.5 | ~3.8 |
| ~3.5 | ~4.0 |
| ~4.5 | ~5.2 |
| ~5.5 | ~4.2 |
| ~6.5 | ~5.5 |
| ~7.5 | ~6.8 |
| ~8.5 | ~6.2 |
</details>

图9-3

由(3.12)式 $\hat{b} = S_{xy} / S_{xx}$ 得 $Q_{e}$ 的一个分解式

$$
Q _ {e} = S _ {y y} - \hat {b} S _ {x y}. \tag {3.14}
$$

由(3.8)式知,b,a的估计量分别为①

$$
\left. \begin{array}{l} \hat {b} = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) (Y _ {i} - \overline {{Y}})}{\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2}} = \frac {\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) Y _ {i}}{\sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) ^ {2}}, \\ \hat {a} = \frac {1}{n} \sum_ {i = 1} ^ {n} Y _ {i} - \frac {\hat {b}}{n} \sum_ {i = 1} ^ {n} x _ {i} = \overline {{Y}} - \hat {b}   \overline {{x}}, \end{array} \right\} \tag {3.15}
$$

其中  $\overline{Y}=\frac{1}{n}\sum_{i=1}^{n}Y_{i},\overline{x}=\frac{1}{n}\sum_{i=1}^{n}x_{i}.$  在  $S_{yy},S_{xy}$  的表达式(3.11)中，将  $y_{i}$  改为  $Y_{i}$   $(i=1,2,\cdots,n)$ ，并把它们分别记为  $S_{YY},S_{xY}$ ，即

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 为方便计，在这里，将 $a, b$ 的估计值和估计量都写成 $\hat{a}, \hat{b}$，在用到它们时，视上下文，是能区分 $\hat{a}, \hat{b}$ 是估计值还是估计量的.</span></small>

$$
S _ {Y Y} = \sum_ {i = 1} ^ {n} (Y _ {i} - \overline {{Y}}) ^ {2}, S _ {x Y} = \sum_ {i = 1} ^ {n} (x _ {i} - \overline {{x}}) (Y _ {i} - \overline {{Y}}).
$$

则(3.14)式中的残差平方和 $Q_{e}$ 的相应的统计量（仍记为 $Q_{e}$ ）为

$$
Q _ {e} = S _ {Y Y} - \hat {b} S _ {x Y}. \tag {3.16}
$$

残差平方和 $Q_{e}$ 服从分布(见本章附录 $4^{\circ}$):

$$
\frac {Q _ {e}}{\sigma^ {2}} \sim \chi^ {2} (n - 2), \tag {3.17}
$$

于是 $E\left(\frac{Q_e}{\sigma^2}\right) = n - 2,$

即知 $E(Q_{e} / (n - 2)) = \sigma^{2}$. 这样就得到了 $\sigma^{2}$ 的无偏估计量:

$$
\hat {\sigma} ^ {2} = \frac {Q _ {e}}{n - 2} = \frac {1}{n - 2} (S _ {Y Y} - \hat {b} S _ {x Y}). \tag {3.18}
$$

在这里，还看到，只要算出表9-17中各栏的和，不但能算出 $\hat{a},\hat{b}$ ，且能算出 $\sigma^2$ 的估计值 $\hat{\sigma}^2$

例 3(续例 2) 求例 2 中  $\sigma^{2}$  的无偏估计.

解 由表9-17, 得

$$
S _ {y y} = \sum_ {i = 1} ^ {n} y _ {i} ^ {2} - \frac {1}{n} \Big (\sum_ {i = 1} ^ {n} y _ {i} \Big) ^ {2} = 4 7 2 2 5 - \frac {1}{1 0} \times 6 7 3 ^ {2} = 1 9 3 2. 1.
$$

又已知 $S_{xy} = 3985, \hat{b} = 0.48303$，即得

$$
Q _ {e} = S _ {y y} - \hat {b} S _ {x y} = 7. 2 3,
$$

$$
\hat {\sigma} ^ {2} = Q _ {e} / (n - 2) = 7. 2 3 / 8 = 0. 9 0.
$$

## (四) 线性假设的显著性检验

在以上的讨论中,我们假定Y关于x的回归函数 $\mu(x)$ 具有形式 $a+bx$ ,在处理实际问题时, $\mu(x)$ 是否为x的线性函数,首先要根据有关专业知识和实践来判断,其次就要根据实际观察得到的数据运用假设检验的方法来判断.这就是说,求得的线性回归方程是否具有实用价值,一般来说,需要经过假设检验才能确定.若线性假设(3.2)符合实际,则b不应为零,因为若b=0,则 $E(Y)=\mu(x)$ 就不依赖于x了.因此我们需要检验假设

$$
H _ {0}: \quad b = 0,
$$

$$
H _ {1}: \quad b \neq 0. \tag {3.19}
$$

我们使用 $t$ 检验法来进行检验. 我们有(见本章附录 $2^{\circ}$):

$$
\hat {b} \sim N (b, \sigma^ {2} / S _ {x x}). \tag {3.20}
$$

又由(3.17)式，(3.18)式知

$$
\frac {(n - 2) \hat {\sigma} ^ {2}}{\sigma^ {2}} = \frac {Q _ {e}}{\sigma^ {2}} \sim \chi^ {2} (n - 2), \tag {3.21}
$$

且 $\hat{b}$ 与 $Q_{e}$ 独立（见本章附录 $5^{\circ}$ ).故有

$$
\frac {\hat {b} - b}{\sqrt {\sigma^ {2} / S _ {x x}}} \Bigg | \sqrt {\frac {(n - 2) \hat {\sigma} ^ {2}}{\sigma^ {2}}} \Bigg | (n - 2) \sim t (n - 2),
$$

即 $\frac{\hat{b} - b}{\hat{\sigma}}\sqrt{\mathrm{S}_{xx}}\sim t(n - 2).$ (3.22)

这里 $\hat{\sigma} = \sqrt{\hat{\sigma}^2}$

当  $H_{0}$  为真时 b = 0, 此时

$$
t = \frac {\hat {b}}{\hat {\sigma}} \sqrt {S _ {x x}} \sim t (n - 2), \tag {3.23}
$$

且 $E(\hat{b}) = b = 0$ ，即得 $H_0$ 的拒绝域为

$$
| t | = \frac {| \hat {b} |}{\hat {\sigma}} \sqrt {S _ {x x}} \geqslant t _ {a / 2} (n - 2), \tag {3.24}
$$

此处  $\alpha$  为显著性水平.

当假设  $H_{0}: b = 0$  被拒绝时，认为回归效果是显著的，反之，就认为回归效果不显著。回归效果不显著的原因可能有如下几种:

$1^{\circ}$ 影响 $Y$ 取值的，除 $x$ 及随机误差外还有其他不可忽略的因素.
$2^{\circ}$   $E(Y)$  与 x 的关系不是线性的, 而存在着其他的关系.
$3^{\circ}Y$ 与 $x$ 不存在关系.

因此需要进一步的分析原因,分别处理.

例 4(续例 2) 检验例 2 中的回归效果是否显著, 取  $\alpha = 0.05$ .

解 由例2、例3已知 $\hat{b} = 0.48303, S_{xx} = 8250, \hat{\sigma}^2 = 0.90$. 查表得 $t_{0.05/2}(n - 2) = t_{0.025}(8) = 2.3060$. 由(3.24)式，假设 $H_0: b = 0$ 的拒绝域为

$$
| t | = \frac {| \hat {b} |}{\hat {\sigma}} \sqrt {S _ {x x}} \geqslant 2. 3 0 6 0.
$$

现在

$$
| t | = \frac {0 . 4 8 3 0 3}{\sqrt {0 . 9 0}} \sqrt {8 2 5 0} = 4 6. 2 5 > 2. 3 0 6 0,
$$

故拒绝  $H_{0}:b=0$  ，认为回归效果是显著的.

## (五)系数 b 的置信区间

当回归效果显著时,我们常需要对系数 b 作区间估计.事实上,可由(3.22)式得到 b 的置信水平为  $1-\alpha$  的置信区间为

$$
\left(\hat {b} \pm t _ {\alpha / 2} (n - 2) \frac {\hat {\sigma}}{\sqrt {S _ {x x}}}\right). \tag {3.25}
$$

例如,例 1 中 b 的置信水平为 0.95 的置信区间为

$$
\left(0. 4 8 3 0 3 \pm 2. 3 0 6 0 \times \sqrt {\frac {0 . 9 0}{8 2 5 0}}\right) = (0. 4 5 8 9 4, 0. 5 0 7 1 2).
$$

## (六) 回归函数 $\mu(x) = a + bx$ 函数值的点估计和置信区间

设 $x_0$ 是自变量 $x$ 的某一指定值. 由(3.9)式可以用经验回归函数 $\hat{y} = \widehat{\mu(x)} = \hat{a} + \hat{b}x$ 在 $x_0$ 的函数值 $\hat{y}_0 = \mu(\hat{x}_0) = \hat{a} + \hat{b}x_0$ 作为 $\mu(x_0) = a + bx_0$ 的点估计, 即

$$
\hat {y} _ {0} = \widehat {\mu (x _ {0})} = \hat {a} + \hat {b} x _ {0}. \tag {3.26}
$$

考虑相应的估计量

$$
\hat {Y} _ {0} = \hat {a} + \hat {b} x _ {0}, \tag {3.27}
$$

由本章附录 $3^{\circ}$ 知，$E(\hat{Y}_0) = a + bx_0$，因此这一估计量是无偏的。下面来求 $\mu(x_0) = a + bx_0$ 的置信区间。由本章附录 $3^{\circ}$ 知

$$
\frac {\hat {Y} _ {0} - (a + b x _ {0})}{\sigma \sqrt {\frac {1}{n} + \frac {(x _ {0} - \overline {{x}}) ^ {2}}{S _ {x x}}}} \sim N (0, 1).
$$

又由(3.17)式，(3.18)式知

$$
\frac {(n - 2) \hat {\sigma} ^ {2}}{\sigma^ {2}} = \frac {Q _ {e}}{\sigma^ {2}} \sim \chi^ {2} (n - 2), \tag {3.28}
$$

且由本章附录 $6^{\circ}$ 知 $Q_{e},\hat{Y}_{0}$ 相互独立.于是

$$
\frac {\hat {Y} _ {0} - (a + b x _ {0})}{\sigma \sqrt {\frac {1}{n} + \frac {(x _ {0} - \overline {{x}}) ^ {2}}{S _ {x x}}}} \left| \sqrt {\frac {(n - 2) \hat {\sigma} ^ {2}}{\sigma^ {2}}} \right| (n - 2) \sim t (n - 2),
$$

即 $\frac{\hat{Y}_0 - (a + bx_0)}{\hat{\sigma}\sqrt{\frac{1}{n} + \frac{(x_0 - \overline{x})^2}{S_{xx}}}}\sim t(n - 2).$

于是得到 $\mu (x_0) = a + bx_0$ 的置信水平为 $1 - \alpha$ 的置信区间为

$$
\left(\hat {Y} _ {0} \pm t _ {\alpha / 2} (n - 2) \hat {\sigma} \sqrt {\frac {1}{n} + \frac {(x _ {0} - \bar {x}) ^ {2}}{S _ {x x}}}\right), \tag {3.29}
$$

或即 $\left(\hat{a} +\hat{b} x_0\pm t_{a / 2}(n - 2)\hat{\sigma}\sqrt{\frac{1}{n} + \frac{(x_0 - \overline{x})^2}{S_{xx}}}\right).$ (3.29)'

这一置信区间的长度是 $x_0$ 的函数，它随 $|x_0 - \overline{x}|$ 的增加而增加，当 $x_0 = \overline{x}$ 时为最短.

## (七) $Y$ 的观察值的点预测和预测区间

若我们对指定点 $x = x_0$ 处因变量 $Y$ 的观察值 $Y_0$ 感兴趣，然而我们在 $x = x_0$ 处并未进行观察或者暂时无法观察，经验回归函数的一个重要应用是，可利用它对因变量 $Y$ 的新观察值 $Y_0$ 进行点预测或区间预测.

若 $Y_{0}$ 是在 $x = x_0$ 处对 $Y$ 的观察结果，由(3.2)式知它满足:

$$
Y _ {0} = a + b x _ {0} + \varepsilon_ {0}, \quad \varepsilon_ {0} \sim N (0, \sigma^ {2}). \tag {3.30}
$$

随机误差 $\varepsilon_0$ 可正也可负，其值无法预料，我们就用 $x_0$ 处的经验回归函数值

$$
\hat {Y} _ {0} = \widehat {\mu (x _ {0})} = \hat {a} + \hat {b} x _ {0}
$$

作为 $Y_{0} = a + bx_{0} + \varepsilon_{0}$ 的点预测. 下面来求 $Y_{0}$ 的预测区间.

因 $Y_{0}$ 是将要做的一次独立试验的结果，因此它与已经得到的试验的结果$Y_{1}, Y_{2}, \cdots, Y_{n}$ 相互独立.由(3.15)式知 $\hat{b}$ 是 $Y_{1}, Y_{2}, \cdots, Y_{n}$ 的线性组合，故 $\hat{Y}_{0} = \overline{Y} + \hat{b}(x_{0} - \overline{x})$ 是 $Y_{1}, Y_{2}, \cdots, Y_{n}$ 的线性组合，故 $Y_{0}$ 与 $\hat{Y}_{0}$ 相互独立.由(3.30)式和本章附录 $3^{\circ}$ 得

$$
\hat {Y} _ {0} - Y _ {0} \sim N \left(0, \left[ 1 + \frac {1}{n} + \frac {(x _ {0} - \overline {{x}}) ^ {2}}{S _ {x x}} \right] \sigma^ {2}\right),
$$

即 $\frac{\hat{Y}_0 - Y_0}{\sigma\sqrt{1 + \frac{1}{n} + \frac{(x_0 - \overline{x})^2}{S_{xx}}}}\sim N(0,1).$ (3.31)

再由(3.28)式、(3.31)式及 $Y_0, \hat{Y}_0, Q_e$ 的相互独立性（本章附录 $6^\circ$）知

$$
\frac {\hat {Y} _ {0} - Y _ {0}}{\sigma \sqrt {1 + \frac {1}{n} + \frac {(x _ {0} - \overline {{x}}) ^ {2}}{S _ {x x}}}} \left| \sqrt {\frac {(n - 2) \hat {\sigma} ^ {2}}{\sigma^ {2}}} \right| (n - 2) \sim t (n - 2),
$$

即 $\frac{\hat{Y}_0 - Y_0}{\hat{\sigma}\sqrt{1 + \frac{1}{n} + \frac{(x_0 - \overline{x})^2}{S_{xx}}}}\sim t(n - 2).$

于是对于给定的置信水平 $1 - \alpha$ 有

$$
P \left\{\frac {| \hat {Y} _ {0} - Y _ {0} |}{\hat {\sigma} \sqrt {1 + \frac {1}{n} + \frac {(x _ {0} - \bar {x}) ^ {2}}{S _ {x x}}}} \leqslant t _ {\alpha / 2} (n - 2) \right\} = 1 - \alpha ,
$$

或 $P\left\{\hat{Y}_0 - t_{\alpha /2}(n - 2)\hat{\sigma}\sqrt{1 + \frac{1}{n} + \frac{(x_0 - \overline{x})^2}{S_{xx}}} < Y_0\right.$

$$
<   \hat {Y} _ {0} + t _ {\alpha / 2} (n - 2) \hat {\sigma} \sqrt {1 + \frac {1}{n} + \frac {(x _ {0} - \bar {x}) ^ {2}}{S _ {x x}}} \Bigg \} = 1 - \alpha .
$$

区间  $\left(\hat{Y}_{0}\pm t_{\alpha/2}(n-2)\hat{\sigma}\sqrt{1+\frac{1}{n}+\frac{(x_{0}-\overline{x})^{2}}{S_{xx}}}\right)$ ，(3.32)

即 $\left(\hat{a} +\hat{b} x_0\pm t_{a / 2}(n - 2)\hat{\sigma}\sqrt{1 + \frac{1}{n} + \frac{(x_0 - \overline{x})^2}{S_{xx}}}\right)$ (3.32)'

称为 $Y_{0}$ 的置信水平为 $1 - \alpha$ 的预测区间①.这一预测区间的长度是 $x_0$ 的函数，它随 $|x_0 - \overline{x}|$ 的增加而增加.当 $x_0 = \overline{x}$ 时为最短.将(3.32)式与(3.29)式比较，知道在相同的置信水平下，回归函数值 $\mu (x_0)$ 的置信区间要比 $Y_{0}$ 的预测区间短.这是因为 $Y_{0} = a + bx_{0} + \varepsilon_{0}$ 比 $\mu (x_0) = a + bx_0$ 多了一项 $\varepsilon_0$

例 5(续例 2) (1) 求回归函数  $\mu(x)$  在 x = 125 处的值  $\mu(125)$  的置信水平为 0.95 的置信区间, 求在 x = 125 处 Y 的新观察值  $Y_{0}$  的置信水平为 0.95 的预测区间. (2) 求在  $x = x_{0}$  处 Y 的新观察值  $Y_{0}$  的置信水平为 0.95 预测区间.

解 （1）由例2，例3已知 $\hat{b}=0.483\ 03,\hat{a}=-2.739\ 35,S_{xx}=8\ 250,\hat{\sigma}^{2}=0.90,\bar{x}=145$ ，查表得 $t_{0.05/2}(8)=2.306\ 0$ ，即得

$$
\begin{array}{l} \hat {Y} _ {0} = \hat {Y} \mid_ {x = 1 2 5} = [ - 2. 7 3 9 3 5 + 0. 4 8 3 0 3 x ] _ {x = 1 2 5} = 5 7. 6 4, \\ t _ {\alpha / 2} (n - 2) \hat {\sigma} \sqrt {\frac {1}{n} + \frac {(x _ {0} - \bar {x}) ^ {2}}{S _ {x x}}} \\ = 2. 3 0 6 0 \times \sqrt {0 . 9 0} \times \sqrt {\frac {1}{1 0} + \frac {(1 2 5 - 1 4 5) ^ {2}}{8 2 5 0}} = 0. 8 4, \\ t _ {\alpha / 2} (n - 2) \hat {\sigma} \sqrt {1 + \frac {1}{n} + \frac {(x _ {0} - \bar {x}) ^ {2}}{S _ {x x}}} = 2. 3 4, \\ \end{array}
$$

得回归函数 $\mu (x)$ 在 $x = 125$ 处的值 $\mu (125)$ 的一个置信水平为0.95的置信区间为

$$
(5 7. 6 4 \pm 0. 8 4).
$$

又得 $x_0 = 125$ 处得率 $Y_{0}$ 的置信水平为0.95的预测区间为

$$
(5 7. 6 4 \pm 2. 3 4).
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 预测区间的含义与置信区间的含义相似，只是后者是对未知参数而言，前者是对随机变量而言.</span></small>

(2) 在  $x = x_{0}$  处 Y 的新观察值  $Y_{0}$  的一个置信水平为 0.95 的预测区间为

$$
\left(\hat {Y} \mid_ {x = x _ {0}} \pm t _ {0. 0 2 5} (8) \hat {\sigma} \sqrt {1 + \frac {1}{1 0} + \frac {(x _ {0} - 1 4 5) ^ {2}}{8 2 5 0}}\right).
$$

取 $x_0$ 为不同的值，得到各点处对应的 $Y$ 的新观察值 $Y_0$ 的预测区间（置信水平为0.95）如下:

| $x_0$ | $Y_0$的预测区间 | $x_0$ | $Y_0$的预测区间 |
| --- | --- | --- | --- |
| 125 | (57.64±2.34) | 150 | (69.72±2.30) |
| 130 | (60.05±2.32) | 155 | (72.13±2.31) |
| 135 | (62.47±2.31) | 160 | (74.55±2.32) |
| 140 | (64.88±2.30) | 165 | (76.96±2.34) |
| 145 | (67.30±2.29) |  |  |

将这些区间的下端点联结起来,又将这些区间的上端点联结起来,得到两条曲线 $L_{1}$ 和 $L_{2}$ ,回归直线位于由 $L_{1},L_{2}$ 所围成的带域的中心线上.

## (八) 可化为一元线性回归的例子

以上讨论了一元线性回归问题,在实际中常会遇到更为复杂的回归问题,但在某些情况下,可以通过适当的变量变换,将它化成一元线性回归来处理.下面介绍几种常见的可转化为一元线性回归的模型.

$$
1 ^ {\circ} \quad Y = \alpha \mathrm{e} ^ {\beta x} \cdot \varepsilon , \quad \ln \varepsilon \sim N (0, \sigma^ {2}), \tag {3.33}
$$

其中 $\alpha, \beta, \sigma^2$ 是与 $x$ 无关的未知参数. 将 $Y = \alpha \mathrm{e}^{\beta x} \cdot \varepsilon$ 两边取对数，得

$$
\ln Y = \ln \alpha + \beta x + \ln \varepsilon .
$$

令 $\ln Y = Y', \ln \alpha = a, \beta = b, x = x', \ln \varepsilon = \varepsilon'$, (3.33) 式可转化为一元线性回归模型

$$
Y ^ {\prime} = a + b x ^ {\prime} + \varepsilon^ {\prime}, \quad \varepsilon^ {\prime} \sim N (0, \sigma^ {2}). \tag {3.34}
$$

$$
2 ^ {\circ} \quad Y = \alpha x ^ {\beta} \cdot \varepsilon , \quad \ln \varepsilon \sim N (0, \sigma^ {2}), \tag {3.35}
$$

其中 $\alpha, \beta, \sigma^2$ 是与 $x$ 无关的未知参数. 将 $Y = \alpha x^\beta \cdot \varepsilon$ 两边取对数，得

$$
\ln Y = \ln \alpha + \beta \ln x + \ln \varepsilon .
$$

令 $\ln Y = Y', \ln \alpha = a, \beta = b, \ln x = x', \ln \varepsilon = \varepsilon'$, (3.35) 式可转化为一元线性回归模型

$$
Y ^ {\prime} = a + b x ^ {\prime} + \varepsilon^ {\prime}, \quad \varepsilon^ {\prime} \sim N (0, \sigma^ {2}). \tag {3.36}
$$

$$
3 ^ {\circ} \quad Y = \alpha + \beta h (x) + \varepsilon , \quad \varepsilon \sim N (0, \sigma^ {2}), \tag {3.37}
$$

其中 $\alpha, \beta, \sigma^2$ 是与 $x$ 无关的未知参数. $h(x)$ 是 $x$ 的已知函数，令 $\alpha = a, \beta = b,$

$h(x) = x^{\prime}$ ，(3.37)式可转化为一元线性回归模型

$$
Y = a + b x ^ {\prime} + \varepsilon , \quad \varepsilon \sim N (0, \sigma^ {2}). \tag {3.38}
$$

若在原模型下，例如在原模型(3.37)下，对于 $(x,Y)$ 有样本 $(x_{1},y_{1}),(x_{2},y_{2}),\dots ,(x_{n},y_{n})$ 就相当于在新模型(3.38)下有样本 $(x_1',y_1),(x_2',y_2),\dots ,(x_n',y_n)$，其中 $x_{i}^{\prime} = h(x_{i})$。于是就能利用上节的方法来估计 $a,b$ 或对 $b$ 作假设检验，或对 $Y$ 进行预测。在得到 $Y$ 关于 $x^{\prime}$ 的回归方程后，再将原自变量 $x$ 代回，就得到 $Y$ 关于 $x$ 的回归方程，它的图形是一条曲线，也称为曲线回归方程。

例6 下表是1957年美国旧轿车价格的调查资料, 今以 $x$ 表示轿车的使用年数, $Y$ 表示相应的平均价格, 求 $Y$ 关于 $x$ 的回归方程.

| 使用年数x | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 平均价格Y(美元) | 2 651 | 1 943 | 1 494 | 1 087 | 765 | 538 | 484 | 290 | 226 | 204 |

解 作散点图如图9-4,看起来Y与x呈指数关系,于是采用模型(3.33),即

$Y = \alpha e^{\beta x} \cdot \varepsilon, \quad \ln \varepsilon \sim N(0, \sigma^{2})$ .

经变量变换后就转化为(3.34)式:

 $Y' = a + bx' + \varepsilon', \varepsilon' \sim N(0, \sigma^{2})$ ,

其中  $Y' = \ln Y, a = \ln \alpha, b = \beta, x' = x, \varepsilon' = \ln \varepsilon$ . 数据经变换后得到

![](images/page_268_chart_9.jpg)

<details>
<summary>scatter</summary>

| x | Y |
| --- | --- |
| 1 | ~2650 |
| 2 | ~1950 |
| 3 | ~1500 |
| 4 | ~1150 |
| 5 | ~900 |
| 6 | ~550 |
| 7 | ~480 |
| 8 | ~300 |
| 9 | ~250 |
| 10 | ~250 |
</details>

图9-4

| $x' = x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $y' = \ln y$ | 7.8827 | 7.5720 | 7.3092 | 6.9912 | 6.6399 | 6.2879 | 6.1821 | 5.6699 | 5.4205 | 5.3181 |

经计算得

$$
\hat {b} = - 0. 2 9 7 6 8, \quad \hat {a} = 8. 1 6 4 5 8 5,
$$

从而有

$$
\hat {y} ^ {\prime} = 8. 1 6 4 5 8 5 - 0. 2 9 7 6 8 x.
$$

又可求得

$$
| t | = \frac {| \hat {b} |}{\hat {\sigma}} \sqrt {S _ {x x}} = 3 2. 3 6 9 3 > t _ {0. 0 5 / 2} (8) = 2. 3 0 6 0,
$$

即知线性回归效果是高度显著的.代回原变量,得曲线回归方程

$$
\hat {y} = \exp \{\hat {y} ^ {\prime} \} = 3 5 1 4. 2 6 \mathrm{e} ^ {- 0. 2 9 7 6 8 x}.
$$

上面所讨论的一元线性回归模型是

$$
Y = a + b x + \varepsilon , \quad \varepsilon \sim N (0, \sigma^ {2}). \tag {3.2}
$$

一般情况,一元回归模型为

$$
Y = \mu (x; \theta_ {1}, \theta_ {2}, \dots , \theta_ {p}) + \varepsilon , \quad \varepsilon \sim N (0, \sigma^ {2}), \tag {3.39}
$$

其中  $\theta_{1},\theta_{2},\cdots,\theta_{p},\sigma^{2}$  是与 x 无关的未知参数.

如果回归函数  $\mu(x;\theta_{1},\theta_{2},\cdots,\theta_{p})$  是参数  $\theta_{1},\theta_{2},\cdots,\theta_{p}$  的线性函数（不必是 x 的线性函数），则称（3.39）为线性回归模型；若  $\mu(x;\theta_{1},\theta_{2},\cdots,\theta_{p})$  是  $\theta_{1},\theta_{2},\cdots,\theta_{p}$  的非线性函数，则称为非线性回归模型。上述模型（3.37）是线性回归模型，而模型（3.33），（3.35）都不是线性回归模型，但是它们都能经过变量变换转化为线性回归模型。又如

$$
Y = \theta_ {1} \mathrm{e} ^ {\theta_ {2} x} + \varepsilon , \quad \varepsilon \sim N (0, \sigma^ {2}). \tag {3.40}
$$

它是非线性回归模型. 它不能经过变量变换转化为线性回归模型①, 称为本质的非线性回归模型. 对于这种模型, 我们就不讨论了.

## § 4 多元线性回归

在实际问题中, 随机变量 Y 往往与多个普通变量  $x_{1}, x_{2}, \cdots, x_{p} (p > 1)$  有关. 对于自变量  $x_{1}, x_{2}, \cdots, x_{p}$  的一组确定的值, Y 有它的分布. 若 Y 的数学期望存在, 则它是  $x_{1}, x_{2}, \cdots, x_{p}$  的函数, 记为

$$
\mu_ {Y \mid x _ {1}, x _ {2}, \dots , x _ {p}} \text {或} \mu (x _ {1}, x _ {2}, \dots , x _ {p}),
$$

它就是 Y 关于 x 的回归函数. 我们感兴趣的是  $\mu(x_{1}, x_{2}, \cdots, x_{p})$  是  $x_{1}, x_{2}, \cdots, x_{p}$  的线性函数的情况. 在这里, 仅讨论下述多元线性回归模型:

$$
Y = b _ {0} + b _ {1} x _ {1} + \dots + b _ {p} x _ {p} + \varepsilon , \quad \varepsilon \sim N (0, \sigma^ {2}), \tag {4.1}
$$

其中 $b_{0}, b_{1}, \cdots, b_{p}, \sigma^{2}$ 都是与 $x_{1}, x_{2}, \cdots, x_{p}$ 无关的未知参数.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 将(3.40)式两边取对数, 得</span></small>

$$
\begin{array}{l} \ln Y = \ln \left(\theta_ {1} \mathrm{e} ^ {\theta_ {2} x} + \varepsilon\right) = \ln \left[ \theta_ {1} \mathrm{e} ^ {\theta_ {2} x} \left(1 + \frac {\varepsilon}{\theta_ {1}} \mathrm{e} ^ {- \theta_ {2} x}\right) \right] \\ = \ln \theta_ {1} + \theta_ {2} x + \ln \left(1 + \frac {\varepsilon}{\theta_ {1}} \mathrm{e} ^ {- \theta_ {2} x}\right). \\ \end{array}
$$

令 $\ln Y = Y'$, $\ln \theta_1 = a, \theta_2 = b$, $\ln \left(1 + \frac{\varepsilon}{\theta_1} \mathrm{e}^{-\theta_2 x}\right) = \varepsilon'$, 则有

$$
Y ^ {\prime} = a + b x + \varepsilon^ {\prime}.
$$

从形式上看，上式好像是线性回归模型。但因误差项 $\varepsilon'$ 中包含未知参数 $\theta_1, \theta_2$，甚至包含自变量 $x$。这在线性回归模型中是不允许的。

设

$$
(x _ {1 1}, x _ {1 2}, \dots , x _ {1 p}, y _ {1}), \dots , (x _ {n 1}, x _ {n 2}, \dots , x _ {n p}, y _ {n}) \tag {4.2}
$$

是一个样本. 和一元线性回归的情况一样, 我们用最大似然估计法来估计参数.
即取  $\hat{b}_{0}, \hat{b}_{1}, \cdots, \hat{b}_{p}$  使当  $b_{0} = \hat{b}_{0}, b_{1} = \hat{b}_{1}, \cdots, b_{p} = \hat{b}_{p}$  时

$$
Q = \sum_ {i = 1} ^ {n} (y _ {i} - b _ {0} - b _ {1} x _ {i 1} - \dots - b _ {p} x _ {i p}) ^ {2} \tag {4.3}
$$

达到最小.

求 Q 分别关于  $b_{0}, b_{1}, \cdots, b_{p}$  的偏导数，并令它们等于零，得

$$
\left. \begin{array}{c} \frac {\partial Q}{\partial b _ {0}} = - 2 \sum_ {i = 1} ^ {n} (y _ {i} - b _ {0} - b _ {1} x _ {i 1} - \dots - b _ {p} x _ {i p}) = 0, \\ \frac {\partial Q}{\partial b _ {j}} = - 2 \sum_ {i = 1} ^ {n} (y _ {i} - b _ {0} - b _ {1} x _ {i 1} - \dots - b _ {p} x _ {i p}) x _ {i j} = 0, \\ j = 1, 2, \dots , p. \end{array} \right\} \tag {4.4}
$$

化简(4.4)式得

$$
\left. \begin{array}{c} b _ {0} n + b _ {1} \sum_ {i = 1} ^ {n} x _ {i 1} + b _ {2} \sum_ {i = 1} ^ {n} x _ {i 2} + \dots + b _ {p} \sum_ {i = 1} ^ {n} x _ {i p} = \sum_ {i = 1} ^ {n} y _ {i}, \\ b _ {0} \sum_ {i = 1} ^ {n} x _ {i 1} + b _ {1} \sum_ {i = 1} ^ {n} x _ {i 1} ^ {2} + b _ {2} \sum_ {i = 1} ^ {n} x _ {i 1} x _ {i 2} + \dots + b _ {p} \sum_ {i = 1} ^ {n} x _ {i 1} x _ {i p} = \sum_ {i = 1} ^ {n} x _ {i 1} y _ {i}, \\ \dots \dots \\ b _ {0} \sum_ {i = 1} ^ {n} x _ {i p} + b _ {1} \sum_ {i = 1} ^ {n} x _ {i p} x _ {i 1} + b _ {2} \sum_ {i = 1} ^ {n} x _ {i p} x _ {i 2} + \dots + b _ {p} \sum_ {i = 1} ^ {n} x _ {i p} ^ {2} = \sum_ {i = 1} ^ {n} x _ {i p} y _ {i}. \end{array} \right\} \tag {4.5}
$$

(4.5) 式称为正规方程组. 为了求解的方便, 将 (4.5) 式写成矩阵的形式. 为此, 引入矩阵

$$
\boldsymbol {X} = \left( \begin{array}{c c c c c} 1 & x _ {1 1} & x _ {1 2} & \dots & x _ {1 p} \\ 1 & x _ {2 1} & x _ {2 2} & \dots & x _ {2 p} \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & x _ {n 1} & x _ {n 2} & \dots & x _ {n p} \end{array} \right), \quad \boldsymbol {Y} = \left( \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {n} \end{array} \right), \quad \boldsymbol {B} = \left( \begin{array}{c} b _ {0} \\ b _ {1} \\ \vdots \\ b _ {p} \end{array} \right).
$$

因 $\mathbf{X}^{\mathrm{T}}\mathbf{X} = \begin{bmatrix} 1 & 1 & \cdots & 1 \\ x_{11} & x_{21} & \cdots & x_{n1} \\ \vdots & \vdots & & \vdots \\ x_{1p} & x_{2p} & \cdots & x_{np} \end{bmatrix}\begin{bmatrix} 1 & x_{11} & x_{12} & \cdots & x_{1p} \\ 1 & x_{21} & x_{22} & \cdots & x_{2p} \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & x_{n1} & x_{n2} & \cdots & x_{np} \end{bmatrix}$

$$
= \left( \begin{array}{c c c c} n & \sum_ {i = 1} ^ {n} x _ {i 1} & \dots & \sum_ {i = 1} ^ {n} x _ {i p} \\ \sum_ {i = 1} ^ {n} x _ {i 1} & \sum_ {i = 1} ^ {n} x _ {i 1} ^ {2} & \dots & \sum_ {i = 1} ^ {n} x _ {i 1} x _ {i p} \\ \vdots & \vdots & & \vdots \\ \sum_ {i = 1} ^ {n} x _ {i p} & \sum_ {i = 1} ^ {n} x _ {i p} x _ {i 1} & \dots & \sum_ {i = 1} ^ {n} x _ {i p} ^ {2} \end{array} \right),
$$

$$
\boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {Y} = \left( \begin{array}{c c c c} 1 & 1 & \dots & 1 \\ x _ {1 1} & x _ {2 1} & \dots & x _ {n 1} \\ \vdots & \vdots & & \vdots \\ x _ {1 p} & x _ {2 p} & \dots & x _ {n p} \end{array} \right) \left( \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {n} \end{array} \right) = \left( \begin{array}{c} \sum_ {i = 1} ^ {n} y _ {i} \\ \sum_ {i = 1} ^ {n} x _ {i 1} y _ {i} \\ \vdots \\ \sum_ {i = 1} ^ {n} x _ {i p} y _ {i} \end{array} \right).
$$

于是(4.5)式即可写成

$$
\boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {X} \boldsymbol {B} = \boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {Y}, \tag {4.5} ^ {\prime}
$$

这就是正规方程组的矩阵形式. 在(4.5)′式两边左乘 $X^{T}X$ 的逆矩阵 $(X^{\mathrm{T}}X)^{-1}$ （设 $(X^{\mathrm{T}}X)^{-1}$ 存在）得到(4.5)′的解

$$
\hat {\boldsymbol {B}} = \left( \begin{array}{c} \hat {b} _ {0} \\ \hat {b} _ {1} \\ \vdots \\ \hat {b} _ {p} \end{array} \right) = (\boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {X}) ^ {- 1} \boldsymbol {X} ^ {\mathrm{T}} \boldsymbol {Y}, \tag {4.6}
$$

这就是我们需要求的 $(b_{0},b_{1},\cdots,b_{p})^{\mathrm{T}}$ 的最大似然估计.我们取

$$
\hat {b} _ {0} + \hat {b} _ {1} x _ {1} + \dots + \hat {b} _ {p} x _ {p} \stackrel {\mathrm{记成}} {=} \hat {y}
$$

作为  $\mu(x_{1},x_{2},\cdots,x_{p})=b_{0}+b_{1}x_{1}+\cdots+b_{p}x_{p}$  的估计. 方程

$$
\hat {y} = \hat {b} _ {0} + \hat {b} _ {1} x _ {1} + \dots + \hat {b} _ {p} x _ {p} \tag {4.7}
$$

称为 Y 关于 x 的 p 元经验线性回归方程, 简称回归方程.

例 下面给出了某种产品每件平均单价 $Y$ (元)与批量 $x$ (件)之间的关系的一组数据: