例1 某厂生产的某种型号的电池，其寿命（以h计）长期以来服从方差$\sigma^2 = 5000$ 的正态分布，现有一批这种电池，从它的生产情况来看，寿命的波动性有所改变.现随机取26只电池，测出其寿命的样本方差 $s^2 = 9200$ .问根据这一数据能否推断这批电池的寿命的波动性较以往的有显著的变化(取 $\alpha = 0.02$ )？

解 本题要求在显著性水平 $\alpha = 0.02$ 下检验假设

$$
H _ {0}: \sigma^ {2} = 5 0 0 0, \quad H _ {1}: \sigma^ {2} \neq 5 0 0 0.
$$

现在 $n = 26, \chi_{\alpha /2}^2 (n - 1) = \chi_{0.01}^2 (25) = 44.314, \chi_{1 - \alpha /2}^2 (25) = \chi_{0.99}^2 (25) = 11.524.\sigma_0^2 = 5000$ ，由(3.1)式拒绝域为

$$
\frac {(n - 1) s ^ {2}}{\sigma_ {0} ^ {2}} \geqslant 4 4. 3 1 4 \quad \text {或} \quad \frac {(n - 1) s ^ {2}}{\sigma_ {0} ^ {2}} \leqslant 1 1. 5 2 4.
$$

由观察值 $s^2 = 9200$ 得 $\frac{(n - 1)s^2}{\sigma_0^2} = 46 > 44.314$ ，所以拒绝 $H_0$ ，认为这批电池寿命的波动性较以往的有显著的变化. □

## (二) 两个总体的情况

设 $X_{1}, X_{2}, \cdots, X_{n_{1}}$ 是来自总体 $N(\mu_{1}, \sigma_{1}^{2})$ 的样本，$Y_{1}, Y_{2}, \cdots, Y_{n_{2}}$ 是来自总体 $N(\mu_{2}, \sigma_{2}^{2})$ 的样本，且两样本独立。其样本方差分别为 $S_{1}^{2}, S_{2}^{2}$。且设 $\mu_{1}, \mu_{2}, \sigma_{1}^{2}, \sigma_{2}^{2}$ 均为未知。现在需要检验假设（显著性水平为 $\alpha$）

$$
H _ {0}: \sigma_ {1} ^ {2} \leqslant \sigma_ {2} ^ {2}, \quad H _ {1}: \sigma_ {1} ^ {2} > \sigma_ {2} ^ {2}. \tag {3.6}
$$

当 $H_0$ 为真时，$E(S_1^2) = \sigma_1^2 \leqslant \sigma_2^2 = E(S_2^2)$，当 $H_1$ 为真时，$E(S_1^2) = \sigma_1^2 > \sigma_2^2 = E(S_2^2)$. 当 $H_1$ 为真时，观察值 $\frac{S_1^2}{S_2^2}$ 有偏大的趋势，故拒绝域具有形式

$$
\frac {s _ {1} ^ {2}}{s _ {2} ^ {2}} \geqslant k,
$$

常数 $k$ 确定如下:

$P\{\text{当} H_{0}\text{为真时拒绝} H_{0}\}=P_{\sigma_{1}^{2}\leqslant\sigma_{2}^{2}}\left\{\frac{S_{1}^{2}}{S_{2}^{2}}\geqslant k\right\}$

$\leqslant P_{\sigma_1^2 \leqslant \sigma_2^2} \left\{\frac{S_1^2 / S_2^2}{\sigma_1^2 / \sigma_2^2} \geqslant k \right\}$ （因为 $\sigma_1^2 / \sigma_2^2 \leqslant 1$）.

要控制 $P\{\text{当} H_0$ 为真时拒绝 $H_0\} \leqslant \alpha$ ，只需令

$$
P _ {\sigma_ {1} ^ {2} \leqslant \sigma_ {2} ^ {2}} \left\{\frac {S _ {1} ^ {2} / S _ {2} ^ {2}}{\sigma_ {1} ^ {2} / \sigma_ {2} ^ {2}} \geqslant k \right\} = \alpha . \tag {3.7}
$$

由第六章 §3 定理 5 知 $\frac{S_1^2 / S_2^2}{\sigma_1^2 / \sigma_2^2} \sim F(n_1 - 1, n_2 - 1)$, 由 (3.7) 式得 $k = F_{\alpha}(n_1 - 1,$

$n_2 - 1)$. 即得检验问题(3.6)的拒绝域为

$$
F = \frac {s _ {1} ^ {2}}{s _ {2} ^ {2}} \geqslant F _ {\alpha} (n _ {1} - 1, n _ {2} - 1). \tag {3.8}
$$

上述检验法称为 $F$ 检验法. 关于 $\sigma_1^2, \sigma_2^2$ 的另外两个检验问题的拒绝域在表8-1中给出.

例2设§2例2中的两个样本分别来自总体 $N(\mu_A,\sigma_A^2),N(\mu_B,\sigma_B^2)$ ，且两样本独立.试检验 $H_0:\sigma_A^2 = \sigma_B^2,H_1:\sigma_A^2\neq \sigma_B^2$ ，以说明我们假设 $\sigma_A^2 = \sigma_B^2$ 是合理的（取显著性水平 $\alpha = 0.01$ ).

解此处 $n_1 = 13, n_2 = 8, \alpha = 0.01$ ，拒绝域为

$$
\frac {s _ {A} ^ {2}}{s _ {B} ^ {2}} \geqslant F _ {0. 0 0 5} (1 2, 7) = 8. 1 8,
$$

或 $\frac{s_A^2}{s_B^2} \leqslant F_{0.995}(12,7) = \frac{1}{F_{0.005}(7,12)} = \frac{1}{5.52} = 0.18.$

现在 $s_A^2 = 0.024^2, s_B^2 = 0.031^2, s_A^2 / s_B^2 = 0.60,$

$$
0. 1 8 <   0. 6 0 <   8. 1 8,
$$

故接受 $H_0$ ，认为两总体方差相等.两总体方差相等也称两总体具有方差齐性，这也表明 §2 例2中假设两总体方差相等是合理的. □

## \* § 4 置信区间与假设检验之间的关系

置信区间与假设检验之间有明显的联系,先考察置信区间与双边检验之间的对应关系.设 $X_{1},X_{2},\cdots,X_{n}$ 是一个来自总体的样本, $x_{1},x_{2},\cdots,x_{n}$ 是相应的样本值, $\Theta$ 是参数 $\theta$ 的可能取值范围.

设 $(\underline{\theta}(X_{1},X_{2},\cdots,X_{n}),\overline{\theta}(X_{1},X_{2},\cdots,X_{n}))$ 是参数 $\theta$ 的一个置信水平为 $1-\alpha$ 的置信区间，则对于任意 $\theta\in\Theta$ ，有

$$
P _ {\theta} \{\underline {{\theta}} (X _ {1}, X _ {2}, \dots , X _ {n}) <   \theta <   \overline {{\theta}} (X _ {1}, X _ {2}, \dots , X _ {n}) \} \geqslant 1 - \alpha , \tag {4.1}
$$

考虑显著性水平为 $\alpha$ 的双边检验

$$
H _ {0}: \theta = \theta_ {0}, H _ {1}: \theta \neq \theta_ {0}. \tag {4.2}
$$

由(4.1)式

$$
P _ {\theta_ {0}} \{\underline {{\theta}} (X _ {1}, X _ {2}, \dots , X _ {n}) <   \theta_ {0} <   \overline {{\theta}} (X _ {1}, X _ {2}, \dots , X _ {n}) \} \geqslant 1 - \alpha ,
$$

即有

$$
P _ {\theta_ {0}} \{(\theta_ {0} \leqslant \underline {{\theta}} (X _ {1}, X _ {2}, \dots , X _ {n})) \cup (\theta_ {0} \geqslant \overline {{\theta}} (X _ {1}, X _ {2}, \dots , X _ {n})) \} \leqslant \alpha .
$$

按显著性水平为 $\alpha$ 的假设检验的拒绝域的定义，检验(4.2)的拒绝域为

$$
\theta_ {0} \leqslant \underline {{\theta}} (x _ {1}, x _ {2}, \dots , x _ {n}) \quad \text {或} \quad \theta_ {0} \geqslant \overline {{{{\theta}}}} (x _ {1}, x _ {2}, \dots , x _ {n});
$$

接受域为

$$
\underline {{\theta}} (x _ {1}, x _ {2}, \dots , x _ {n}) <   \theta_ {0} <   \overline {{\theta}} (x _ {1}, x _ {2}, \dots , x _ {n}).
$$

这就是说, 当我们要检验假设(4.2)时, 先求出  $\theta$  的置信水平为  $1-\alpha$  的置信区间  $(\underline{\theta},\bar{\theta})$ , 然后考察区间  $(\underline{\theta},\bar{\theta})$  是否包含  $\theta_{0}$ , 若  $\theta_{0}\in(\underline{\theta},\bar{\theta})$ , 则接受  $H_{0}$ , 若  $\theta_{0}\notin(\underline{\theta},\bar{\theta})$ , 则拒绝  $H_{0}$ .

反之，对于任意 $\theta_0\in \Theta$ ，考虑显著性水平为 $\alpha$ 的假设检验问题

$$
H _ {0}: \theta = \theta_ {0}, H _ {1}: \theta \neq \theta_ {0},
$$

假设它的接受域为

$$
\underline {{\theta}} (x _ {1}, x _ {2}, \dots , x _ {n}) <   \theta_ {0} <   \overline {{\theta}} (x _ {1}, x _ {2}, \dots , x _ {n}),
$$

即有

$$
P _ {\theta_ {0}} \{\underline {{\theta}} (X _ {1}, X _ {2}, \dots , X _ {n}) <   \theta_ {0} <   \overline {{\theta}} (X _ {1}, X _ {2}, \dots , X _ {n}) \} \geqslant 1 - \alpha .
$$

由 $\theta_0$ 的任意性，由上式知对于任意 $\theta \in \Theta$ ，有

$$
P _ {\theta} \{\underline {{\theta}} (X _ {1}, X _ {2}, \dots , X _ {n}) <   \theta <   \overline {{\theta}} (X _ {1}, X _ {2}, \dots , X _ {n}) \} \geqslant 1 - \alpha .
$$

因此 $(\underline{\theta}(X_{1},X_{2},\cdots,X_{n}),\bar{\theta}(X_{1},X_{2},\cdots,X_{n}))$ 是参数 $\theta$ 的一个置信水平为 $1-\alpha$ 的置信区间.

这就是说，为求出参数  $\theta$  的置信水平为  $1-\alpha$  的置信区间，我们先求出显著性水平为  $\alpha$  的假设检验问题: $H_{0}:\theta=\theta_{0},H_{1}:\theta\neq\theta_{0}$  的接受域  $\underline{\theta}(x_{1},x_{2},\cdots,x_{n})<\theta_{0}<\bar{\theta}(x_{1},x_{2},\cdots,x_{n})$ ，那么， $(\underline{\theta}(X_{1},X_{2},\cdots,X_{n}),\bar{\theta}(X_{1},X_{2},\cdots,X_{n}))$  就是  $\theta$  的置信水平为  $1-\alpha$  的置信区间。

还可验证，置信水平为 $1 - \alpha$ 的单侧置信区间 $(-\infty, \bar{\theta}(X_1, X_2, \cdots, X_n))$ 与显著性水平为 $\alpha$ 的左边检验问题 $H_0: \theta \geqslant \theta_0, H_1: \theta < \theta_0$ 有类似的对应关系。即若已求得单侧置信区间 $(-\infty, \bar{\theta}(X_1, X_2, \cdots, X_n))$，则当 $\theta_0 \in (-\infty, \bar{\theta}(x_1, x_2, \cdots, x_n))$ 时接受 $H_0$，当 $\theta_0 \notin (-\infty, \bar{\theta}(x_1, x_2, \cdots, x_n))$ 时拒绝 $H_0$。反之，若已求得检验问题 $H_0: \theta \geqslant \theta_0, H_1: \theta < \theta_0$ 的接受域为 $-\infty < \theta_0 \leqslant \bar{\theta}(x_1, x_2, \cdots, x_n)$，则可得 $\theta$ 的一个单侧置信区间 $(- \infty, \bar{\theta}(X_1, X_2, \cdots, X_n))$。

置信水平为 $1 - \alpha$ 的单侧置信区间 $(\underline{\theta}(X_1, X_2, \dots, X_n), \infty)$ 与显著性水平为 $\alpha$ 的右边检验问题 $H_0: \theta \leqslant \theta_0, H_1: \theta > \theta_0$ 也有类似的对应关系。即若已求得单侧置信区间 $(\underline{\theta}(X_1, X_2, \dots, X_n), \infty)$，则当 $\theta_0 \in (\underline{\theta}(x_1, x_2, \dots, x_n), \infty)$ 时接受 $H_0$，当 $\theta_0 \notin (\underline{\theta}(x_1, x_2, \dots, x_n), \infty)$ 时拒绝 $H_0$。反之，若已求得检验问题 $H_0: \theta \leqslant \theta_0, H_1: \theta > \theta_0$ 的接受域为 $\underline{\theta}(x_1, x_2, \dots, x_n) \leqslant \theta_0 < \infty$，则可得 $\theta$ 的一个单侧置信区间 $(\underline{\theta}(X_1, X_2, \dots, X_n), \infty)$。

例1设 $X\sim N(\mu ,1),\mu$ 未知， $\alpha = 0.05,n = 16$ ，且由一样本算得 $\overline{x} = 5.20$ ，于是得到参数 $\mu$ 的一个置信水平为0.95的置信区间

$$
\left(\overline {{x}} - \frac {1}{\sqrt {1 6}} z _ {0. 0 2 5}, \overline {{x}} + \frac {1}{\sqrt {1 6}} z _ {0. 0 2 5}\right) = (5. 2 0 - 0. 4 9, 5. 2 0 + 0. 4 9) = (4. 7 1, 5. 6 9).
$$

现在考虑检验问题 $H_0: \mu = 5.5, H_1: \mu \neq 5.5$. 由于 $5.5 \in (4.71, 5.69)$, 故接受 $H_0$.

例2 数据如上例.试求右边检验问题 $H_0: \mu \leqslant \mu_0, H_1: \mu > \mu_0$ 的接受域，并求 $\mu$ 的单侧置信下限 ($\alpha = 0.05$).

解 检验问题的拒绝域为 $z = \frac{\overline{x} - \mu_0}{1 / \sqrt{16}} \geqslant z_{0.05}$, 或即 $\mu_0 \leqslant 4.79$. 于是检验问题的接受域为 $\mu_0 > 4.79$. 这样就得到 $\mu$ 的单侧置信区间 $(4.79, \infty)$, 单侧置信下限 $\underline{\mu} = 4.79$.

## \* § 5 样本容量的选取

以上我们在进行假设检验时,总是根据问题的要求,预先给出显著性水平以控制犯第Ⅰ类错误的概率,而犯第Ⅱ类错误的概率则依赖于样本容量的选择.在一些实际问题中,我们除了希望控制犯第Ⅰ类错误的概率外,往往还希望控制犯第Ⅱ类错误的概率.在这一节,我们将阐明如何选取样本的容量使得犯第Ⅱ类错误的概率控制在预先给定的限度之内.为此,我们引入施行特征函数.

定义 若 $C$ 是参数 $\theta$ 的某检验问题的一个检验法，

$$
\beta (\theta) = P _ {\theta} (\text {接受} H _ {0}) \tag {5.1}
$$

称为检验法 C 的施行特征函数或 OC 函数, 其图形称为 OC 曲线.

由定义知，若此检验法的显著性水平为 $\alpha$ ，那么当真值 $\theta \in H_0$ 时，$\beta (\theta)$ 就是作出正确判断（即 $H_{0}$ 为真时接受 $H_0$ )的概率，故此时 $\beta (\theta)\geqslant 1 - \alpha$；而当 $\theta \in H_1$ 时，则 $\beta (\theta)$ 就是犯第Ⅱ类错误的概率，而 $1 - \beta (\theta)$ 是作出正确判断（即 $H_0$ 为不真时拒绝 $H_0$ )的概率.函数 $1 - \beta (\theta)$ 称为检验法 $C$ 的功效函数.当 $\theta^{*}\in H_{1}$ 时，值$1 - \beta (\theta^{*})$ 称为检验法 $C$ 在点 $\theta^{*}$ 的功效.它表示当参数 $\theta$ 的真值为 $\theta^{*}$ 时，检验法$C$ 作出正确判断的概率.

本书只介绍正态总体均值的检验法的 OC 函数及其图形.

## 1. $Z$ 检验法的 $OC$ 函数

右边检验问题 $H_0: \mu \leqslant \mu_0, H_1: \mu > \mu_0$ 的 $OC$ 函数是

$$
\begin{array}{l} \beta (\mu) = P _ {\mu} (\text {接受} H _ {0}) = P _ {\mu} \Biggl \{\frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}} <   z _ {\alpha} \Biggr \} \\ = P _ {\mu} \left\{\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} <   z _ {\alpha} - \frac {\mu - \mu_ {0}}{\sigma / \sqrt {n}} \right\} = \Phi (z _ {\alpha} - \lambda), \tag {5.2} \\ \end{array}
$$

其中 $\lambda = \frac{\mu - \mu_0}{\sigma / \sqrt{n}}$。其图形如图8-5所示。此 $OC$ 函数 $\beta(\mu)$ 有如下性质:

（1）它是 $\lambda = \frac{\mu - \mu_0}{\sigma / \sqrt{n}}$ 的单调递减连续函数.

(2) $\lim_{\mu \to \mu_1^+} \beta(\mu) = 1 - \alpha, \quad \lim_{\mu \to \infty} \beta(\mu) = 0.$

由  $\beta(\mu)$  的连续性可知, 当参数的真

![](images/page_212_chart_6.jpg)

<details>
<summary>line</summary>

| \(\mu\) | \(\beta(\mu)\) |
| --- | --- |
| 0 | \(\alpha\) |
| \(\mu_{0}\) | \(\alpha\) |
</details>

图8-5

值 $\mu (\mu >\mu_0)$ 在 $\mu_0$ 附近时，检验法的功效很低，即 $\beta (\mu)$ 的值很大，亦即犯第Ⅱ类错误的概率很大.因为 $\alpha$ 通常取得比较小，而不管 $\sigma$ 多么小， $n$ 多么大，只要 $n$ 给定，总存在 $\mu_0$ 附近的点 $\mu (\mu >\mu_0)$ 使 $\beta (\mu)$ 几乎等于 $1 - \alpha$

这表明,无论样本容量 n 多么大,要想对所有  $\mu\in H_{1}$ , 即真值为  $H_{1}$  所规定的任一点时, 控制犯第Ⅱ类错误的概率都很小是不可能的. 但是我们可以使用 OC 函数  $\beta(\mu)$  以确定样本容量 n, 使当真值  $\mu\geqslant\mu_{0}+\delta(\delta>0$  为取定的值)时, 犯第Ⅱ类错误的概率不超过给定的  $\beta$ . 这是由于  $\beta(\mu)$  是  $\mu$  的递减函数, 故当  $\mu\geqslant\mu_{0}+\delta$  时有

$$
\beta (\mu_ {0} + \delta) \geqslant \beta (\mu).
$$

于是只要 $\beta (\mu_0 + \delta) = \Phi (z_{\alpha} - \sqrt{n}\delta /\sigma)\leqslant \beta$ ，亦即只要 $n$ 满足

$$
z _ {\alpha} - \sqrt {n} \delta / \sigma \leqslant - z _ {\beta}
$$

即可. 这就是说, 只要

$$
\sqrt {n} \geqslant \frac {(z _ {\alpha} + z _ {\beta}) \sigma}{\delta}, \tag {5.3}
$$

就能使当 $\mu \in H_1$ 且 $\mu \geqslant \mu_0 + \delta$ 时（即真值 $\mu \geqslant \mu_0 + \delta$ 时）犯第Ⅱ类错误的概率不超过 $\beta$.

类似地，可得左边检验问题 $H_0:\mu \geqslant \mu_0,H_1:\mu <  \mu_0$ 的 $OC$ 函数为

$$
\beta (\mu) = \Phi (z _ {\alpha} + \lambda), \quad \lambda = \frac {\mu - \mu_ {0}}{\sigma / \sqrt {n}}. \tag {5.4}
$$

当真值 $\mu \geqslant \mu_0$ 时 $\beta (\mu)$ 为作出正确判断的概率；当真值 $\mu < \mu_0$ 时，$\beta (\mu)$ 给出犯第Ⅱ类错误的概率.只要样本容量 $n$ 满足

$$
\sqrt {n} \geqslant \frac {(z _ {\alpha} + z _ {\beta}) \sigma}{\delta}, \tag {5.5}
$$

就能使当 $\mu \in H_1$ 且 $\mu \leqslant \mu_0 - \delta (\delta > 0$，为取定的值)时，犯第Ⅱ类错误的概率不超过给定的值 $\beta$.

双边检验问题 $H_0: \mu = \mu_0$，$H_1: \mu \neq \mu_0$ 的 $OC$ 函数是

$$
\begin{array}{l} \beta (\mu) = P _ {\mu} (\text {接受} H _ {0}) = P _ {\mu} \left\{- z _ {a / 2} <   \frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}} <   z _ {a / 2} \right\} \\ = P _ {\mu} \left\{- \lambda - z _ {\alpha / 2} <   \frac {\bar {X} - \mu}{\sigma / \sqrt {n}} <   - \lambda + z _ {\alpha / 2} \right\} = \Phi \left(z _ {\alpha / 2} - \lambda\right) - \Phi \left(- z _ {\alpha / 2} - \lambda\right) \\ = \Phi (z _ {\alpha / 2} - \lambda) + \Phi (z _ {\alpha / 2} + \lambda) - 1, \quad \lambda = \frac {\mu - \mu_ {0}}{\sigma / \sqrt {n}}. \tag {5.6} \\ \end{array}
$$

OC 曲线如图 8-6 所示. 注意 $\beta(\mu)$ 是 $|\lambda|$ 的严格单调下降函数.

在双边检验问题中,若要求对  $H_{1}$  中满足  $\left|\mu-\mu_{0}\right|\geqslant\delta>0$  的  $\mu$  处的函数值  $\beta(\mu)\leqslant\beta$ , 则需解超越方程

$$
\begin{array}{l} \beta = \Phi (z _ {\alpha / 2} - \sqrt {n} \delta / \sigma) \\ + \Phi (z _ {\alpha / 2} + \sqrt {n} \delta / \sigma) - 1 \\ \end{array}
$$

才能确定 n. 通常因 n 较大, 故总可以

![](images/page_213_chart_7.jpg)

<details>
<summary>line</summary>

| \(\mu\) | \(\beta(\mu)\) |
| --- | --- |
| 0 | ~0.05 |
| \(\mu_{0}\) | \(\alpha{1}\) |
</details>

图8-6

认为 $z_{\alpha /2} + \sqrt{n}\delta /\sigma \geqslant 4$ ，于是 $\Phi (z_{\alpha /2} + \sqrt{n}\delta /\sigma)\approx 1$ ，故近似地有

$$
\beta \approx \Phi (z _ {\alpha / 2} - \sqrt {n} \delta / \sigma).
$$

由此知只要样本容量 $n$ 满足

$$
z _ {\alpha / 2} - \sqrt {n} \delta / \sigma \leqslant - z _ {\beta},
$$

即只要 $n$ 满足

$$
\sqrt {n} \geqslant (z _ {\alpha / 2} + z _ {\beta}) \frac {\sigma}{\delta}, \tag {5.7}
$$

就能使当 $\mu \in H_1$ 且 $|\mu -\mu_0|\geqslant \delta (\delta >0$ ，为取定的值)时，犯第Ⅱ类错误的概率不超过给定的值 $\beta$

例1（工业产品质量抽验方案）设有一大批产品，产品质量指标 $X \sim N(\mu, \sigma^2)$. 以 $\mu$ 小者为佳，厂方要求所确定的验收方案对高质量的产品 $(\mu \leqslant \mu_0)$ 能以高概率 $1 - \alpha$ 为买方所接受. 买方则要求低质产品 $(\mu \geqslant \mu_0 + \delta, \delta > 0)$ 能以高概率 $1 - \beta$ 被拒绝. $\alpha, \beta$ 由厂方与买方协商给出. 并采取一次抽样以确定该批产品是否为买方所接受. 问应怎样安排抽样方案？已知 $\mu_0 = 120, \delta = 20$ ，且由工厂长期经验知 $\sigma^2 = 900$. 又经商定 $\alpha, \beta$ 均取为0.05.

解 检验问题可表达为

$$
H _ {0}: \mu \leqslant \mu_ {0}, \quad H _ {1}: \mu > \mu_ {0}, \tag {5.8}
$$

且要求当 $\mu \geqslant \mu_0 + \delta$ 时能以 $1 - \beta = 0.95$ 的概率拒绝 $H_0$. 由 $Z$ 检验，拒绝域为

$$
\frac {\overline {{x}} - \mu_ {0}}{\sigma / \sqrt {n}} \geqslant z _ {\alpha},
$$

故 $OC$ 函数为

$$
\begin{array}{l} \beta (\mu) = P _ {\mu} \left\{\frac {\overline {{X}} - \mu_ {0}}{\sigma / \sqrt {n}} <   z _ {\alpha} \right\} = P _ {\mu} \left\{\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} <   z _ {\alpha} - \frac {\mu - \mu_ {0}}{\sigma / \sqrt {n}} \right\} \\ = \Phi \bigg (z _ {\alpha} - \frac {\mu - \mu_ {0}}{\sigma / \sqrt {n}} \bigg). \tag {5.9} \\ \end{array}
$$

现要求当 $\mu \geqslant \mu_0 + \delta$ 时 $\beta (\mu)\leqslant \beta .$ 因 $\beta (\mu)$ 是 $\mu$ 的递减函数，故只需 $\beta (\mu_0 + \delta) = \beta$ 即可.此时，由(5.9)式可得

$$
\sqrt {n} \geqslant \frac {(z _ {\alpha} + z _ {\beta}) \sigma}{\delta}.
$$

按给定的数据算得 $n \geqslant 24.35$，故取 $n = 25$。且当 $\bar{x}$ 满足 $\frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}} \geqslant z_\alpha = z_{0.05} = 1.645$ 时，即当 $\bar{x} \geqslant 129.87$ 时，买方就拒绝这批产品，而当 $\bar{x} < 129.87$ 时，买方接受这批产品。$\square$

## 2. $t$ 检验法的 $OC$ 函数

右边检验问题 $H_0: \mu \leqslant \mu_0, H_1: \mu > \mu_0$ 的 $t$ 检验法的 $OC$ 函数是

$$
\beta (\mu) = P _ {\mu} (\text {接受} H _ {0}) = P _ {\mu} \biggl \{\frac {\overline {{X}} - \mu_ {0}}{S / \sqrt {n}} <   t _ {\alpha} (n - 1) \biggr \}, \tag {5.10}
$$

其中变量

$$
\frac {\overline {{X}} - \mu_ {0}}{S / \sqrt {n}} = \left(\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} + \lambda\right) / \left(\frac {S}{\sigma}\right), \lambda = \frac {\mu - \mu_ {0}}{\sigma / \sqrt {n}}. \tag {5.11}
$$

我们称变量 $\frac{\overline{X} - \mu_0}{S / \sqrt{n}}$ 服从非中心参数为 $\lambda$ 、自由度为 $n - 1$ 的非中心 $t$ 分布. 在 $\lambda = 0$ 时, 它是通常的 $t(n - 1)$ 变量.

若给定 $\alpha, \beta$ 以及 $\delta > 0$，则可从书末附表7查得所需容量 $n$，使得当 $\mu \in H_1$ 且 $\frac{\mu - \mu_0}{\sigma} \geqslant \delta$ 时犯第Ⅱ类错误的概率不超过 $\beta$.

若给定 $\alpha, \beta$ 以及 $\delta > 0$，对于左边检验问题 $H_0: \mu \geqslant \mu_0, H_1: \mu < \mu_0$ 的 $t$ 检验法，也可从附表7查得所需容量 $n$，使得当 $\mu \in H_1$ 且 $\frac{\mu - \mu_0}{\sigma} \leqslant -\delta$ 时犯第Ⅱ类错误的概率不超过 $\beta$. 对于双边检验问题 $H_0: \mu = \mu_0, H_1: \mu \neq \mu_0$ 的 $t$ 检验法也可从附表7查得所需容量 $n$，使得当 $\mu \in H_1$，且 $\frac{|\mu - \mu_0|}{\sigma} \geqslant \delta$ 时犯第Ⅱ类错误的概率不超过 $\beta$.

例2 考虑在显著性水平 $\alpha = 0.05$ 下进行 $t$ 检验

$$
H _ {0}: \mu \leqslant 6 8, \quad H _ {1}: \mu > 6 8.
$$

（1）要求在 $H_{1}$ 中 $\mu \geqslant \mu_{1} = 68 + \sigma$ 时犯第Ⅱ类错误的概率不超过 $\beta = 0.05$. 求所需的样本容量.
（2）若样本容量为 $n = 30$ ，问在 $H_{1}$ 中 $\mu = \mu_{1} = 68 + 0.75\sigma$ 时犯第Ⅱ类错误的概率是多少？

解（1）此处 $\alpha = \beta = 0.05, \mu_0 = 68, \delta = \frac{\mu_1 - \mu_0}{\sigma} = \frac{(68 + \sigma) - 68}{\sigma} = 1$，查附表7得 $n = 13$.

（2）现在 $\alpha = 0.05, n = 30, \delta = \frac{\mu_1 - \mu_0}{\sigma} = \frac{(68 + 0.75\sigma) - 68}{\sigma} = 0.75$ ，查附表7，得 $\beta = 0.01.$

例 3 考虑在显著性水平  $\alpha=0.05$  下进行 t 检验

$$
H _ {0}: \mu = 1 4, \quad H _ {1}: \mu \neq 1 4.
$$

要求在 $H_{1}$ 中 $\frac{|\mu - 14|}{\sigma} \geqslant 0.4$ 时犯第Ⅱ类错误的概率不超过 $\beta = 0.1$ ，求所需样本容量.

解 此处  $\alpha=0.05,\beta=0.1,\delta=0.4$  , 查附表 7 得 n=68.

在实际问题中,有时只给出  $\alpha,\beta$  及  $\left|\mu_{1}-\mu_{0}\right|$  的值,而需要确定所需的样本容量 n. 这时由于  $\sigma$  未知,不能确定  $\delta=\left|\mu_{1}-\mu_{0}\right|/\sigma$  的值,因而不能直接查表以确定样本容量. 此时可采用下述近似方法. 先适当取一值  $n_{1}$ , 抽取容量为  $n_{1}$  的样本,根据这一样本计算  $s^{2}$  的值,以  $s^{2}$  作为  $\sigma^{2}$  的估计,算出  $\delta$  的近似值. 由  $\alpha,\beta,\delta$  的值查附表 7 定出样本的容量,记为  $n_{2}$ . 若  $n_{1}\geqslant n_{2}$ , 则取  $n_{1}$  作为所求的容量,即取  $n=n_{1}$ . 否则,再抽  $n_{2}-n_{1}$  个独立观察值与原来抽得的观察值合并,重新计算  $\delta$  的近似值. 然后用  $\delta$  的新近似值和  $\alpha,\beta$  查附表 7,再次定出样本容量. 记为  $n_{3}$ . 若  $n_{2}\geqslant n_{3}$ , 则取  $n=n_{2}$ , 否则再按上法重复进行. 一般,只需试少数几次就可得到所求的样本容量 n.

下面考虑两个正态总体均值差的 t 检验.

若两个正态总体 $N(\mu_1, \sigma_1^2), N(\mu_2, \sigma_2^2)$ 中 $\sigma_1^2 = \sigma_2^2 = \sigma^2$ 而 $\sigma^2$ 未知. 在均值差 $\mu_1 - \mu_2$ 的检验问题 $H_0: \mu_1 - \mu_2 = 0, H_1: \mu_1 - \mu_2 \neq 0$ （或 $H_0: \mu_1 - \mu_2 \leqslant 0, H_1: \mu_1 - \mu_2 > 0$ 或 $H_0: \mu_1 - \mu_2 \geqslant 0, H_1: \mu_1 - \mu_2 < 0$）的 $t$ 检验法中，当分别自两个总体取得的相互独立的样本其容量 $n_1 = n_2 = n$ 时，给定 $\alpha, \beta$ 以及 $\delta = |\mu_1 - \mu_2| / \sigma$ 的值后可以查附表8得到所需样本容量，使当 $|\mu_1 - \mu_2| / \sigma \geqslant \delta$ 时犯第Ⅱ类错误的概率小于或等于 $\beta$. 当仅给出 $\alpha, \beta$ 以及 $|\mu_1 - \mu_2|$ 的值时，可按类似于上面所说的方法处理.

例 4 需要比较两种汽车用的燃料的辛烷值, 得数据:

| 燃料A | 81 | 84 | 79 | 76 | 82 | 83 | 84 | 80 | 79 | 82 | 81 | 79 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 燃料B | 76 | 74 | 78 | 79 | 80 | 79 | 82 | 76 | 81 | 79 | 82 | 78 |

燃料的辛烷值越高，燃料质量越好.因燃料 $B$ 较燃料 $A$ 价格便宜，因此，若两者辛烷值相同，则使用燃料 $B$；但若含量的均值差 $\mu_{A} - \mu_{B} \geqslant 5$，则使用燃料 $A$.设两总体的分布均可认为是正态的，而两个样本相互独立.问应采用哪种燃料（取 $\alpha = 0.01, \beta = 0.01$）？

解 按题意需要在显著性水平 $\alpha = 0.01$ 下检验假设

$$
H _ {0}: \mu_ {A} - \mu_ {B} \leqslant 0, \quad H _ {1}: \mu_ {A} - \mu_ {B} > 0,
$$

并要求在 $\mu_A - \mu_B \geqslant 5$ 时，犯第Ⅱ类错误的概率不超过 $\beta = 0.01$.

所取的样本容量为 $n_A = n_B = 12$ ，且有 $\overline{x}_A = 80.83, \overline{x}_B = 78.67, s_A^2 = 5.61, s_B^2 = 6.06.$ 经显著性水平为0.1的 $F$ 检验知，可认为两总体的方差相等，即有 $\sigma_A^2 = \sigma_B^2$ ，记为 $\sigma^2$ .因 $n_A = n_B$ ，取 $\hat{\sigma}^2 = (s_A^2 + s_B^2) / 2 = 5.835$ 作为 $\sigma^2$ 的点估计，取$\hat{\sigma} = \sqrt{\hat{\sigma}^2}$ ，于是 $\delta = 5 / \hat{\sigma} = 2.07$ ，查附表8，当 $\alpha = 0.01,\beta = 0.01,\delta = 2.07$ 时 $n\geqslant 12.$ 现 $n = 12$ ，故已近似地满足要求.而右边检验的拒绝域为

$$
t = \frac {\overline {{x}} _ {A} - \overline {{x}} _ {B}}{s _ {w} \sqrt {1 / n _ {A} + 1 / n _ {B}}} \geqslant t _ {0. 0 1} (n _ {A} + n _ {B} - 2) = 2. 5 0 8 3.
$$

由样本观察值算得  $t=2.19<2.5083$ ，故接受  $H_{0}$ ，即采用燃料 B.

## § 6 分布拟合检验

上面介绍的各种检验法都是在总体分布形式为已知的前提下进行讨论的。但在实际问题中，有时不能知道总体服从什么类型的分布，这时就需要根据样本来检验关于分布的假设。本节介绍 $\chi^2$ 拟合检验法。它可以用来检验总体是否具有某一个指定的分布或属于某一个分布族。

## (一) 单个分布的 ${\chi }^{2}$ 拟合检验法

设总体 X 的分布未知, $x_{1},x_{2},\cdots,x_{n}$ 是来自 X 的样本值.我们来检验假设

$$
H _ {0}: \text {总体} X \text {的分布函数为} F (x), \tag {6.1}
$$

$$
H _ {1}: \text {总体} X \text {的分布函数不是} F (x), ①
$$

其中设 $F(x)$ 不含未知参数.（也常以分布律或概率密度代替 $F(x)$.）

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 在这里备择假设 $H_{1}$ 可以不必写出.</span></small>

下面来定义检验统计量. 将在  $H_{0}$  下 X 可能取值的全体  $\Omega$  分成互不相交的子集  $A_{1}, A_{2}, \cdots, A_{k}$ ，以  $f_{i} (i=1,2,\cdots,k)$  记样本观察值  $x_{1}, x_{2}, \cdots, x_{n}$  中落在  $A_{i}$  的个数，这表示事件  $A_{i}=\{X$  的值落在子集  $A_{i}$  内\} 在 n 次独立试验中发生  $f_{i}$  次，于是在这 n 次试验中事件  $A_{i}$  发生的频率为  $f_{i}/n$ . 另一方面，当  $H_{0}$  为真时，我们可以根据  $H_{0}$  中所假设的 X 的分布函数来计算事件  $A_{i}$  的概率，得到  $p_{i}=P(A_{i}), i=1,2,\cdots,k$ . 频率  $f_{i}/n$  与概率  $p_{i}$  会有差异，但一般来说，当  $H_{0}$  为真，且试验的次数又甚多时，这种差异不应太大，因此  $\left(\frac{f_{i}}{n}-p_{i}\right)^{2}$  不应太大. 我们采用形如

$$
\sum_ {i = 1} ^ {k} C _ {i} \left(\frac {f _ {i}}{n} - p _ {i}\right) ^ {2} \tag {6.2}
$$

的统计量来度量样本与  $H_{0}$  中所假设的分布的吻合程度, 其中  $C_{i}(i=1,2,\cdots,k)$  ①为给定的常数. 皮尔逊证明, 如果选取

$$
C _ {i} = n / p _ {i} (i = 1, 2, \dots , k),
$$

则由(6.2)定义的统计量具有下述定理中所述的简单性质.于是我们就采用

$$
\chi^ {2} = \sum_ {i = 1} ^ {k} \frac {n}{p _ {i}} \left(\frac {f _ {i}}{n} - p _ {i}\right) ^ {2} = \sum_ {i = 1} ^ {k} \frac {f _ {i} ^ {2}}{n p _ {i}} - n \tag {6.3}
$$

作为检验统计量.

定理 若 $n$ 充分大 $(n\geqslant 50)$ ，则当 $H_0$ 为真时统计量(6.3)近似服从 $\chi^2 (k - 1)$ 分布.(证略.)

据以上的讨论, 当  $H_{0}$  为真时, (6.3) 式中的  $\chi^{2}$  不应太大, 如  $\chi^{2}$  过分大就拒绝  $H_{0}$ , 拒绝域的形式为

$$
\chi^ {2} \geqslant G \quad (G \text {为正常数}).
$$

对于给定的显著性水平 $\alpha$ ，确定 $G$ 使

$$
P \{\text {当} H _ {0} \text {为真时拒绝} H _ {0} \} = P _ {H _ {0}} \{\chi^ {2} \geqslant G \} = \alpha .
$$

由上述定理得 $G = \chi_{\alpha}^{2}(k - 1)$ .即当样本观察值使(6.3)式中的 $\chi^2$ 的值有

$$
\chi^ {2} \geqslant \chi_ {\alpha} ^ {2} (k - 1),
$$

则在显著性水平 $\alpha$ 下拒绝 $H_0$; 否则就接受 $H_0$. 这就是单个分布的 $\chi^2$ 拟合检验法.

$\chi^{2}$  拟合检验法是基于上述定理得到的, 所以使用时必须注意 n 不能小于 50. 另外  $np_{i}$  不能太小, 应有  $np_{i} \geqslant 5$ , 否则应适当合并  $A_{i}$ , 以满足这个要求(见下例).

例1 下表列出了某一地区在夏季的一个月中由100个气象站报告的雷暴雨的次数.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 在每一项前乘 $C_i$ ，是为了能够适当选择 $C_i$ ，使得统计量(6.2)有一个理想的极限分布.</span></small>

| i | 0 | 1 | 2 | 3 | 4 | 5 | $\geqslant 6$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $f_{i}$ | 22 | 37 | 20 | 13 | 6 | 2 | 0 |
| $A_{i}$ | $A_{0}$ | $A_{1}$ | $A_{2}$ | $A_{3}$ | $A_{4}$ | $A_{5}$ | $A_{6}$ |

其中 $f_{i}$ 是报告雷暴雨次数为 $i$ 的气象站数. 试用 $\chi^2$ 拟合检验法检验雷暴雨的次数 $X$ 是否服从均值 $\lambda = 1$ 的泊松分布（取显著性水平 $\alpha = 0.05$）.

解 按题意需检验假设

$$
H _ {0}: \quad P \{X = i \} = \frac {\lambda^ {i} \mathrm{e} ^ {- \lambda}}{i !} = \frac {\mathrm{e} ^ {- 1}}{i !}, \quad i = 0, 1, \dots .
$$

在  $H_{0}$  下 X 所有可能取的值为  $\Omega=\{0,1,2,\cdots\}$ ，将  $\Omega$  分成如表 8-2 所示的两两不相交的子集  $A_{0}, A_{1}, \cdots, A_{6}$ ，则有  $P\{X=i\}$  为

$$
p _ {i} = P \{X = i \} = \frac {\mathrm{e} ^ {- 1}}{i !}, \quad i = 0, 1, \dots , 5.
$$

例如 $p_0 = P\{X = 0\} = \mathrm{e}^{-1} = 0.36788,$

$$
\begin{array}{l} p _ {3} = P \{X = 3 \} = \frac {\mathrm{e} ^ {- 1}}{3 !} = 0. 0 6 1 3 1, \\ p _ {6} = P \{X \geqslant 6 \} = 1 - \sum_ {i = 0} ^ {5} p _ {i} = 0. 0 0 0 5 9. \\ n = 1 0 0. \\ \end{array}
$$

表 8-2 例 1 的 ${\chi }^{2}$ 拟合检验计算表

<table><tr><td> $A_i$ </td><td> $f_i$ </td><td> $p_i$ </td><td> $np_i$ </td><td> $f_i^2 / (np_i)$ </td></tr><tr><td> $A_0 : \{X=0\}$ </td><td>22</td><td> $e^{-1}$ </td><td>36.788</td><td>13.16</td></tr><tr><td> $A_1 : \{X=1\}$ </td><td>37</td><td> $e^{-1}$ </td><td>36.788</td><td>37.21</td></tr><tr><td> $A_2 : \{X=2\}$ </td><td>20</td><td> $e^{-1}/2$ </td><td>18.394</td><td>21.75</td></tr><tr><td> $A_3 : \{X=3\}$ </td><td>13</td><td> $e^{-1}/6$ </td><td>6.131</td><td rowspan="4">8.03</td></tr><tr><td> $A_4 : \{X=4\}$ </td><td>6</td><td> $e^{-1}/24$ </td><td>1.533</td></tr><tr><td> $A_5 : \{X=5\}$ </td><td>2</td><td> $e^{-1}/120$ </td><td>0.307</td></tr><tr><td> $A_6 : \{X\geqslant 6\}$ </td><td>0</td><td> $1-\sum_{i=0}^{5}p_i$ </td><td>0.059</td></tr></table>

$$
\Sigma = 1 2 7. 0 4
$$

计算结果如表8-2所示，其中有些 $np_{i}<5$ 的组予以适当合并，使得每组均有 $np_{i}\geqslant5$，如表中第4列花括号所示。并组后k=4， $\chi^{2}$ 的自由度为k-1=4-1=3。 $\chi^{2}_{0.05}(k-1)=\chi^{2}_{0.05}(3)=7.815$ 。现在 $\chi^{2}=127.04-100=27.04>7.815$，故在显著性水平0.05下拒绝 $H_{0}$，认为样本不是来自均值 $\lambda=1$ 的泊松分布。

例2 在研究牛的毛色与牛角的有无，这样两对性状分离现象时，用黑色无角牛与红色有角牛杂交，子二代出现黑色无角牛192头，黑色有角牛78头，红色无角牛 72 头, 红色有角牛 18 头, 共 360 头, 问这两对性状是否符合孟德尔遗传规律中 9:3:3:1 的遗传比例?

解 现将题中的数据列表如下:

| 序号 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 种类 | 黑色无角 | 黑色有角 | 红色无角 | 红色有角 |
| 数量 | 192 | 78 | 72 | 18 |
| $A_i$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ |

以 $X$ 记各种牛的序号，按题意需检验各类牛的头数符合比例 $9:3:3:1$ ，即$(9 / 16):(3 / 16):(3 / 16):(1 / 16)$ .需检验假设: $H_0:X$ 的分布律为

| X | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| $p_k$ | 9/16 | 3/16 | 3/16 | 1/16 |

取显著性水平为 0.1. 所需计算列在表 8-3 中 (n=360).

表 8-3 例 2 的 ${\chi }^{2}$ 拟合检验计算表

| $A_i$ | $f_i$ | $p_i$ | $np_i$ | $f_i^2/(np_i)$ |
| --- | --- | --- | --- | --- |
| $A_1$ | 192 | 9/16 | 360×9/16=202.5 | 1922/202.5=182.04 |
| $A_2$ | 78 | 3/16 | 360×3/16=67.5 | 782/67.5=90.13 |
| $A_3$ | 72 | 3/16 | 360×3/16=67.5 | 722/67.5=76.8 |
| $A_4$ | 18 | 1/16 | 360×1/16=22.5 | 182/22.5=14.4 |

$$
\Sigma = 3 6 3. 3 7
$$

现在 $\chi^{2}=363.37-360=3.37,k=4,\chi_{0.1}^{2}(4-1)=6.251>3.37$ ，故接受 $H_{0}$ ，认为两对性状符合孟德尔遗传规律中9:3:3:1的遗传比例。

## (二) 分布族的 $\chi^{2}$ 拟合检验

在(一)中要检验的原假设是 $H_0$ :总体 $X$ 的分布函数是 $F(x)$ ，其中 $F(x)$ 是已知的，这种情况是不多的.我们经常遇到的所需检验的原假设是

$$
H _ {0}: \text {总体} X \text {的分布函数是} F (x; \theta_ {1}, \theta_ {2}, \dots , \theta_ {r}), \tag {6.4}
$$

其中 F 的形式已知，而  $\boldsymbol{\theta}=(\theta_{1},\theta_{2},\cdots,\theta_{r})$  是未知参数，它们在某一个范围取值。在  $F(x;\theta_{1},\theta_{2},\cdots,\theta_{r})$  中当参数  $\theta_{1},\theta_{2},\cdots,\theta_{r}$  取不同的值时，就得到不同的分布，因而  $F(x;\theta_{1},\theta_{2},\cdots,\theta_{r})$  代表一族分布。(6.4) 中的  $H_{0}$  表示总体 X 的分布属于分布族  $F(x;\theta_{1},\theta_{2},\cdots,\theta_{r})$ . 采用类似(一)中的方法来定义检验统计量，将在  $H_{0}$  下 X 可能取值的全体  $\Omega$  分成  $k(k>r+1)$  个互不相交的子集  $A_{1}, A_{2}, \cdots, A_{k}$ ，以  $f_{i}(i=1,2,\cdots,k)$  记样本观察值  $x_{1}, x_{2}, \cdots, x_{n}$  落在  $A_{i}$  的个数，则事件  $A_{i}=\{X$  的值落在  $A_{i}$  内  $\}$  的频率为  $f_{i}/n$ . 另一方面，当  $H_{0}$  为真时，由  $H_{0}$  所假设的分布函数来计算  $P(A_{i})$ ，得到  $P(A_{i})=p_{i}(\theta_{1},\theta_{2},\cdots,\theta_{r})=p_{i}(\boldsymbol{\theta})=p_{i}$ . 此时，需先利用样本求出未知参数的最大似然估计（在  $H_{0}$  下），以估计值作为参数值，求出  $p_{i}$  的估计值  $\hat{p}_{i}=\hat{p}(A_{i})$ ，在 (6.3) 式中以  $\hat{p}_{i}$  代替  $p_{i}$ ，取

$$
\chi^ {2} = \sum_ {i = 1} ^ {k} \frac {f _ {i} ^ {2}}{n \hat {p} _ {i}} - n \tag {6.5}
$$

作为检验假设 $H_0$ 的统计量. 可以证明, 在某些条件下, 在 $H_0$ 为真时近似地有

$$
\chi^ {2} = \sum_ {i = 1} ^ {k} \frac {f _ {i} ^ {2}}{n \hat {p} _ {i}} - n \sim \chi^ {2} (k - r - 1)
$$

与在(一)中一样可得假设检验问题(6.4)的拒绝域为

$$
\chi^ {2} \geqslant \chi_ {\alpha} ^ {2} (k - r - 1), \tag {6.6}
$$

$\alpha$ 为显著性水平.以上就是用来检验分布族的 $\chi^2$ 拟合检验法

例3 在一实验中,每隔一定时间观察一次由某种铀所放射的到达计数器上的 $\alpha$ 粒子数 $X$, 共观察了 100 次, 得结果如表 8-4 所示:

表 8-4 铀放射的到达计数器上的 $\alpha$ 粒子数的实验记录

| i | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | $\geqslant 12$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $f_i$ | 1 | 5 | 16 | 17 | 26 | 11 | 9 | 9 | 2 | 1 | 2 | 1 | 0 |
| $A_i$ | $A_0$ | $A_1$ | $A_2$ | $A_3$ | $A_4$ | $A_5$ | $A_6$ | $A_7$ | $A_8$ | $A_9$ | $A_{10}$ | $A_{11}$ | $A_{12}$ |

其中 $f_{i}$ 是观察到有 $i$ 个 $\alpha$ 粒子的次数.从理论上考虑知 $X$ 应服从泊松分布

$$
P \{X = i \} = \frac {\lambda^ {i} \mathrm{e} ^ {- \lambda}}{i !}, \quad i = 0, 1, 2, \dots . \tag {6.7}
$$

问(6.7)式是否符合实际(取 $\alpha = 0.05$ )？即在显著性水平0.05下检验假设

$H_{0}$: 总体 $X$ 服从泊松分布 $P\{X = i\} = \frac{\lambda^{i} \mathrm{e}^{-\lambda}}{i!}, \quad i = 0,1,2,\dots$.

解 因在 $H_0$ 中参数 $\lambda$ 未具体给出，所以先估计 $\lambda$. 由最大似然估计法得 $\hat{\lambda} = \overline{x} = 4.2$. 在 $H_0$ 假设下，即在 $X$ 服从泊松分布的假设下，$X$ 所有可能取的值为 $\Omega = \{0,1,2,\dots\}$，将 $\Omega$ 分成如表8-4所示的两两不相交的子集 $A_0, A_1, \dots, A_{12}$. 则 $P\{X = i\}$ 有估计

$$
\hat {p} _ {i} = \hat {P} \{X = i \} = \frac {4 . 2 ^ {i} \mathrm{e} ^ {- 4 . 2}}{i !}, \quad i = 0, 1, \dots .
$$

例如 $\hat{p}_0 = \hat{P}\{X = 0\} = \mathrm{e}^{-4.2} = 0.015,$

$$
\begin{array}{l} \hat {p} _ {3} = \hat {P} \{X = 3 \} = \frac {4 . 2 ^ {3} \mathrm{e} ^ {- 4 . 2}}{3 !} = 0. 1 8 5, \\ \hat {p} _ {1 2} = \hat {P} \{X \geqslant 1 2 \} = 1 - \sum_ {i = 0} ^ {1 1} \hat {p} _ {i} = 0. 0 0 2. \\ \end{array}
$$

表 8-5 例 3 的 ${\chi }^{2}$ 拟合检验计算表

<table><tr><td> $A_i$ </td><td> $f_i$ </td><td> $\hat{p}_i$ </td><td> $n\hat{p}_i$ </td><td> $f_i^2/n\hat{p}_i$ </td></tr><tr><td> $A_0$ </td><td rowspan="2"> $\begin{array}{c}1 \\5\end{array}\ }6$ </td><td rowspan="2"> $\begin{array}{c}0.015 \\0.063\end{array}\ }0.078$ </td><td rowspan="2"> $\begin{array}{c}1.5 \\6.3\end{array}\ }7.8$ </td><td rowspan="2">4.615</td></tr><tr><td> $A_1$ </td></tr><tr><td> $A_2$ </td><td>16</td><td>0.132</td><td>13.2</td><td>19.394</td></tr><tr><td> $A_3$ </td><td>17</td><td>0.185</td><td>18.5</td><td>15.622</td></tr><tr><td> $A_4$ </td><td>26</td><td>0.194</td><td>19.4</td><td>34.845</td></tr><tr><td> $A_5$ </td><td>11</td><td>0.163</td><td>16.3</td><td>7.423</td></tr><tr><td> $A_6$ </td><td>9</td><td>0.114</td><td>11.4</td><td>7.105</td></tr><tr><td> $A_7$ </td><td>9</td><td>0.069</td><td>6.9</td><td>11.739</td></tr><tr><td> $A_8$ </td><td rowspan="3"> $\begin{array}{c}2 \\1\end{array}\ }6$ </td><td rowspan="3"> $\begin{array}{c}0.036 \\0.017\end{array}\ }0.065$ </td><td rowspan="3"> $\begin{array}{c}3.6 \\1.7\end{array}\ }6.5$ </td><td rowspan="5">5.538</td></tr><tr><td> $A_9$ </td></tr><tr><td> $A_{10}$ </td></tr><tr><td> $A_{11}$ </td><td rowspan="2"> $\begin{array}{c}1 \\0\end{array}$ </td><td rowspan="2"> $\begin{array}{c}0.003 \\0.002\end{array}$ </td><td rowspan="2"> $\begin{array}{c}0.3 \\0.2\end{array}$ </td></tr><tr><td> $A_{12}$ </td></tr></table>

$$
\Sigma = 1 0 6. 2 8 1
$$

计算结果如表8-5所示，其中有些 $n\hat{p}_i < 5$ 的组予以适当合并，使得每组均有$n\hat{p}_i\geqslant 5$ ，如表中第四列花括号所示.此处，并组后 $k = 8$ ，但因在计算概率时，估计了一个参数 $\lambda$ ，故 $r = 1,\chi^2$ 的自由度为 $8 - 1 - 1 = 6.\chi_{0.05}^{2}(k - r - 1) = \chi_{0.05}^{2}(6) = 12.592$ 现在 $\chi^2 = 106.281 - 100 = 6.281 <   12.592$ ，故在显著性水平0.05下接受 $H_0$ .即认为样本来自泊松分布总体.也就是说认为理论上的结论是符合实际的. □

注意,本题答案是“接受  $H_{0}$ , 认为总体 X 的分布属于泊松分布族, 即认为  $X \sim \pi(\lambda)$ ”, 亦即“认为必有某一个参数  $\lambda_{0}, X \sim \pi(\lambda_{0})$ ”, 而不能将答案误写成“X 服从以  $\lambda = 4.2$  为参数的泊松分布”.

例4自1965年1月1日至1971年2月9日共2231天中，全世界记录到里氏震级4级和4级以上地震计162次，统计如下:

| 相继两次地震间隔天数x | 0~4 | 5~9 | 10~14 | 15~19 | 20~24 | 25~29 | 30~34 | 35~39 | ≥40 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 出现的频数 | 50 | 31 | 26 | 17 | 10 | 8 | 6 | 6 | 81 |

试检验相继两次地震间隔的天数 X 服从指数分布( $\alpha=0.05$ ).

解 按题意需检验假设

$H_{0}:X$  的概率密度为

$$
f (x) = \left\{ \begin{array}{l l} \frac {1}{\theta} \mathrm{e} ^ {- x / \theta}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right. \tag {6.8}
$$

在这里， $H_{0}$ 中的参数 $\theta$ 未给出，先由最大似然估计法求得 $\theta$ 的估计为

$$
\hat {\theta} = \overline {{x}} = \frac {2 2 3 1}{1 6 2} = 1 3. 7 7.
$$

在 $H_0$ 下，$X$ 可能取值的全体 $\Omega$ 为区间 $[0, \infty)$. 将区间 $[0, \infty)$ 分为 $k = 9$ 个互不重叠的小区间:

$$
A _ {1} = [ 0, 4. 5 ], \quad A _ {2} = (4. 5, 9. 5 ], \quad \dots , \quad A _ {9} = (3 9. 5, \infty),
$$

如表 8-6 第一列所示. 若 $H_{0}$ 为真, $X$ 的分布函数的估计为

$$
\hat {F} (x) = \left\{ \begin{array}{l l} 1 - \mathrm{e} ^ {- x / 1 3. 7 7}, & x > 0, \\ 0, & x \leqslant 0. \end{array} \right.
$$

由上式可得概率  $p_{i}=P(A_{i})$  的估计:

$$
\hat {p} _ {i} = \hat {P} (A _ {i}) = \hat {P} \{a _ {i} <   X \leqslant a _ {i + 1} \} = \hat {F} (a _ {i + 1}) - \hat {F} (a _ {i}).
$$

例如

$$
\hat {p} _ {2} = \hat {P} (A _ {2}) = \hat {P} \{4. 5 <   X \leqslant 9. 5 \} = \hat {F} (9. 5) - \hat {F} (4. 5) = 0. 2 1 9 6,
$$

而

$$
\hat {p} _ {9} = \hat {P} (A _ {9}) = 1 - \sum_ {i = 1} ^ {8} \hat {P} (A _ {i}) = 0. 0 5 6 8.
$$

将计算结果列表如下:

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 这里 8 个数值是 40,43,44,49,58,60,81,109.</span></small>

表 8-6 例 4 的 ${\chi }^{2}$ 拟合检验计算表

| $A_i$ | $f_i$ | $\hat{p}_i$ | $n\hat{p}_i$ | $f_i^2/(n\hat{p}_i)$ |  |
| --- | --- | --- | --- | --- | --- |
| $A_1:0≤x≤4.5$ | 50 | 0.278 8 | 45.165 6 | 55.351 9 |  |
| $A_2:4.5310.219 635.575 227.013 2$ | 31 | 0.219 6 | 35.575 2 | 27.013 2 |  |
| \\( A_3:9.5260.152 724.737 427.327 0 | 26 | 0.152 7 | 24.737 4 | 27.327 0 |  |
| \\( A_4:14.5170.106 217.204 416.798 0 | 17 | 0.106 2 | 17.204 4 | 16.798 0 |  |
| \\( A_5:19.5100.073 911.971 88.353 0 | 10 | 0.073 9 | 11.971 8 | 8.353 0 |  |
| \\( A_6:24.580.051 48.326 87.686 0 | 8 | 0.051 4 | 8.326 8 | 7.686 0 |  |
| \\( A_7:29.560.035 85.799 66.207 3 | 6 | 0.035 8 | 5.799 6 | 6.207 3 |  |
| \\( A_8:34.5\\left.\\begin{array}{l}6\\\\8\\end{array}\\right\\} \\left.\\begin{array}{l}0.024 8\\\\0.056 8\\end{array}\\right\\} \\left.\\begin{array}{l}4.017 6\\\\9.201 6\\end{array}\\right\\} 13.219 214.826 9 | $\left.\begin{array}{l}6\\8\end{array}\right\}$ | $\left.\begin{array}{l}0.024 8\\0.056 8\end{array}\right\}$ | $\left.\begin{array}{l}4.017 6\\9.201 6\end{array}\right\}$ | 13.219 2 | 14.826 9 |

$$
\Sigma = 1 6 3. 5 6 3 3
$$

现在 $\chi^2 = 163.5633 - 162 = 1.5633, \chi_{0.05}^2 (k - r - 1) = \chi_{0.05}^2 (8 - 1 - 1) = \chi_{0.05}^2 (6) = 12.592 > 1.5633$，故在显著性水平0.05下接受 $H_0$，认为 $X$ 服从指数分布。

例5 对于第六章 §2 例1中的数据,试检验它们是否来自正态总体 $X$ (取显著性水平 $\alpha = 0.1$).

解 需检验假设: $H_{0}:X$ 的概率密度为

$$
f (x) = \frac {1}{\sqrt {2 \pi} \sigma} \mathrm{e} ^ {- \frac {(x - \mu) ^ {2}}{2 \sigma^ {2}}}, - \infty <   x <   \infty .
$$

因在 $H_0$ 中未给出 $\mu, \sigma^2$ 的数值. 需先估计 $\mu, \sigma^2$. 由最大似然估计法得 $\mu, \sigma^2$ 的估计值为 $\hat{\mu} = 143.8, \hat{\sigma^2} = 6.0^2$. 我们将在 $H_0$ 下 $X$ 可能取值的区间 $(-\infty, \infty)$ 分为7个小区间，并取事件 $A_i$ 如表8-7中第一列所示. 若 $H_0$ 为真，$X$ 的概率密度的估计为

$$
\hat {f} (x) = \frac {1}{\sqrt {2 \pi} \times 6 . 0} \mathrm{e} ^ {- \frac {(x - 1 4 3 . 8) ^ {2}}{2 \times 6 . 0 ^ {2}}}, \quad - \infty <   x <   \infty .
$$

按上式并查标准正态分布的分布函数表即可得概率 $P(A_{i})$ 的估计.例如

$$
\hat {p} _ {2} = \hat {P} (A _ {2}) = \hat {P} \{1 2 9. 5 <   X \leqslant 1 3 4. 5 \} = \Phi \Big (\frac {1 3 4 . 5 - 1 4 3 . 8}{6 . 0} \Big) - \Phi \Big (\frac {1 2 9 . 5 - 1 4 3 . 8}{6 . 0} \Big)
$$

$$
= \Phi (- 1. 5 5) - \Phi (- 2. 3 8) = 0. 0 5 1 9.
$$

将计算结果列表如下: