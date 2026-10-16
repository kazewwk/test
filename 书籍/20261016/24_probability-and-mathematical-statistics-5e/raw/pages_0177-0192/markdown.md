证 因为  $E(\overline{X})=E(X)=\theta$ ，所以  $\overline{X}$  是  $\theta$  的无偏估计量。而  $Z=\min\{X_{1}, X_{2}, \cdots, X_{n}\}$  具有概率密度

$$
f _ {\min} (x; \theta) = \left\{ \begin{array}{l l} { \frac {n}{\theta} \mathrm{e} ^ {- n x / \theta},} & {x > 0,} \\ {0,} & {\text {其他}.} \end{array} \right.
$$

故知 $E(Z) = \frac{\theta}{n},$

$$
E (n Z) = \theta .
$$

即 $nZ$ 也是参数 $\theta$ 的无偏估计量.

由此可见一个未知参数可以有不同的无偏估计量. 事实上, 在本例中 $X_{1}, X_{2}, \cdots, X_{n}$ 中的每一个都可以作为 $\theta$ 的无偏估计量.

## (二) 有效性

现在来比较参数 $\theta$ 的两个无偏估计量 $\hat{\theta}_1$ 和 $\hat{\theta}_2$，如果在样本容量 $n$ 相同的情况下，$\hat{\theta}_1$ 的观察值较 $\hat{\theta}_2$ 在真值 $\theta$ 的附近更密集，我们就认为 $\hat{\theta}_1$ 较 $\hat{\theta}_2$ 更为理想。由于方差是随机变量取值与其数学期望（此时数学期望 $E(\hat{\theta}_1) = E(\hat{\theta}_2) = \theta$）的偏离程度的度量，所以无偏估计以方差小者为好。这就引出了估计量的有效性这一概念。

有效性 设  $\hat{\theta}_{1}=\hat{\theta}_{1}(X_{1},X_{2},\cdots,X_{n})$  与  $\hat{\theta}_{2}=\hat{\theta}_{2}(X_{1},X_{2},\cdots,X_{n})$  都是  $\theta$  的无偏估计量，若对于任意  $\theta\in\Theta$ ，有

$$
D (\hat {\theta} _ {1}) \leqslant D (\hat {\theta} _ {2}),
$$

且至少对于某一个 $\theta \in \Theta$ 上式中的不等号成立，则称 $\hat{\theta}_1$ 较 $\hat{\theta}_2$ 有效.

例3(续例2) 试证当 $n > 1$ 时，$\theta$ 的无偏估计量 $\overline{X}$ 较 $\theta$ 的无偏估计量 $nZ$ 有效.

证 由于 $D(X) = \theta^2$ ，故有 $D(\overline{X}) = \theta^2 / n.$ 再者，由于 $D(Z) = \theta^2 / n^2$ ，故有 $D(nZ) = \theta^2.$ 当 $n > 1$ 时 $D(nZ) > D(\overline{X})$ ，故 $\overline{X}$ 较 $nZ$ 有效. □

## (三) 相合性

前面讲的无偏性与有效性都是在样本容量 $n$ 固定的前提下提出的. 我们自然希望随着样本容量的增大, 一个估计量的值稳定于待估参数的真值. 这样, 对估计量又有下述相合性的要求.

相合性 设  $\hat{\theta}(X_{1}, X_{2}, \cdots, X_{n})$  为参数  $\theta$  的估计量，若对于任意  $\theta \in \Theta$ ，当  $n \to \infty$

时  $\hat{\theta}(X_{1},X_{2},\cdots,X_{n})$  依概率收敛于  $\theta$ ，则称  $\hat{\theta}$  为  $\theta$  的相合估计量.

即,若对于任意  $\theta\in\Theta$  都满足:对于任意  $\varepsilon>0$ ,有

$$
\lim _ {n \to \infty} P \{| \hat {\theta} - \theta | <   \varepsilon \} = 1,
$$

则称 $\hat{\theta}$ 是 $\theta$ 的相合估计量.

例如由第六章§3知,样本 $k(k\geqslant 1)$ 阶矩是总体 $X$ 的 $k$ 阶矩 $\mu_{k} = E(X^{k})$ 的相合估计量,进而若待估参数 $\theta = g(\mu_1,\mu_2,\dots ,\mu_k)$,其中 $g$ 为连续函数,则 $\theta$ 的矩估计量 $\hat{\theta} = g(\hat{\mu}_1,\hat{\mu}_2,\dots ,\hat{\mu}_k) = g(A_1,A_2,\dots ,A_k)$ 是 $\theta$ 的相合估计量.

由最大似然估计法得到的估计量,在一定条件下也具有相合性.其详细讨论已超出本书范围,从略.

相合性是对一个估计量的基本要求,若估计量不具有相合性,那么不论将样本容量 n 取得多么大,都不能将  $\theta$  估计得足够准确,这样的估计量是不可取的.

上述无偏性、有效性、相合性是评价估计量的一些基本标准,其他的标准这里就不讲了.

## § 4 区间估计

对于一个未知量,人们在测量或计算时,常不以得到近似值为满足,还需估计误差,即要求知道近似值的精确程度(亦即所求真值所在的范围).类似地,对于未知参数 $\theta$ ,除了求出它的点估计 $\hat{\theta}$ 外,我们还希望估计出一个范围,并希望知道这个范围包含参数 $\theta$ 真值的可信程度.这样的范围通常以区间的形式给出,同时还给出此区间包含参数 $\theta$ 真值的可信程度.这种形式的估计称为区间估计,这样的区间即所谓置信区间.现在我们引入置信区间的定义.

置信区间 设总体 X 的分布函数  $F(x;\theta)$  含有一个未知参数  $\theta,\theta\in\Theta$  ( $\Theta$  是  $\theta$  可能取值的范围)，对于给定值  $\alpha(0<\alpha<1)$ ，若由来自 X 的样本  $X_{1},X_{2},\cdots,X_{n}$  确定的两个统计量  $\underline{\theta}=\underline{\theta}(X_{1},X_{2},\cdots,X_{n})$  和  $\bar{\theta}=\bar{\theta}(X_{1},X_{2},\cdots,X_{n})(\underline{\theta}<\bar{\theta})$ ，对于任意  $\theta\in\Theta$  满足

$$
P \{\underline {{\theta}} (X _ {1}, X _ {2}, \dots , X _ {n}) <   \theta <   \bar {\theta} (X _ {1}, X _ {2}, \dots , X _ {n}) \} \geqslant 1 - \alpha , \tag {4.1}
$$

则称随机区间 $(\underline{\theta},\bar{\theta})$ 是 $\theta$ 的置信水平为 $1 - \alpha$ 的置信区间，$\underline{\theta}$ 和 $\bar{\theta}$ 分别称为置信水平为 $1 - \alpha$ 的双侧置信区间的置信下限和置信上限，$1 - \alpha$ 称为置信水平.

当 $X$ 是连续型随机变量时，对于给定的 $\alpha$ ，我们总是按要求 $P\{\underline{\theta} < \theta <\overline{\theta}\} = 1 - \alpha$ 求出置信区间.而当 $X$ 是离散型随机变量时，对于给定的 $\alpha$ ，常找不到区间 $(\underline{\theta},\overline{\theta})$

使得 $P\{\underline{\theta} < \theta < \overline{\theta}\}$ 恰为 $1 - \alpha$. 此时我们去找区间 $(\underline{\theta}, \overline{\theta})$ 使得 $P\{\underline{\theta} < \theta < \overline{\theta}\}$ 至少为 $1 - \alpha$, 且尽可能地接近 $1 - \alpha$.

(4.1)式的含义如下:若反复抽样多次(各次得到的样本的容量相等,都是n).每个样本值确定一个区间 $(\underline{\theta},\bar{\theta})$ ,每个这样的区间要么包含 $\theta$ 的真值,要么不包含 $\theta$ 的真值(参见图7-1).按伯努利大数定律,在这么多的区间中,包含 $\theta$ 真值的约占 $100(1-\alpha)\%$ ,不包含 $\theta$ 真值的约仅占 $100\alpha\%$ .例如,若 $\alpha=0.01$ ,反复抽样1000次,则得到的1000个区间中不包含 $\theta$ 真值的约仅为10个.

例 设总体  $X \sim N(\mu, \sigma^{2})$ ,  $\sigma^{2}$  为已知,  $\mu$  为未知, 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自 X 的样本, 求  $\mu$  的置信水平为  $1 - \alpha$  的置信区间.

解 我们知道  $\overline{X}$  是  $\mu$  的无偏估计, 且有

$$
\frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} \sim N (0, 1). \tag {4.2}
$$

$\frac{\overline{X} - \mu}{\sigma / \sqrt{n}}$ 所服从的分布 $N(0,1)$ 不依赖于任何未知参数. 按标准正态分布的上 $\alpha$ 分位数的定义, 有 (参见图7-2)

$$
P \left\{\left| \frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} \right| <   z _ {\alpha / 2} \right\} = 1 - \alpha , \tag {4.3}
$$

即 $P\left\{\overline{X} -\frac{\sigma}{\sqrt{n}} z_{\alpha /2} <   \mu <  \overline{X} +\frac{\sigma}{\sqrt{n}} z_{\alpha /2}\right\} = 1 - \alpha .$ (4.4)

这样,我们就得到了  $\mu$  的一个置信水平为  $1-\alpha$  的置信区间

$$
\left(\overline {{X}} - \frac {\sigma}{\sqrt {n}} z _ {\alpha / 2}, \quad \overline {{X}} + \frac {\sigma}{\sqrt {n}} z _ {\alpha / 2}\right). \tag {4.5}
$$

这样的置信区间常写成

$$
\left(\overline {{X}} \pm \frac {\sigma}{\sqrt {n}} z _ {\alpha / 2}\right). \tag {4.6}
$$

![](images/page_178_image_14.jpg)

<details>
<summary>text_image</summary>

θ
</details>

图7-1

![](images/page_178_chart_16.jpg)

<details>
<summary>contour</summary>

| Region | Description |
| --- | --- |
| Left Tail | \(\alpha/2\) |
| Shaded Area 1 | \(-z_\alpha/2\) |
| Center | O |
| Shaded Area 2 | \(\alpha/2\) |
| Shaded Area 3 | \(z_\alpha/2\) |
</details>

图7-2

如果取 $1 - \alpha = 0.95$ ，即 $\alpha = 0.05$ ，又若 $\sigma = 1, n = 16$ ，查表得 $z_{\alpha / 2} = z_{0.025} = 1.96.$ 于是我们得到一个置信水平为0.95的置信区间

$$
\left(\overline {{X}} \pm \frac {1}{\sqrt {1 6}} \times 1. 9 6\right), \quad \text {即} (\overline {{X}} \pm 0. 4 9). \tag {4.7}
$$

再者,若由一个样本值算得样本均值的观察值  $\bar{x}=5.20$ , 则得到一个区间  $(5.20\pm0.49)$ , 即  $(4.71,5.69)$ .

注意,这已经不是随机区间了.但我们仍称它为  $\theta$  的置信水平为 0.95 的置信区间.其含义是:若反复抽样多次,每个样本值(n=16)按(4.7)式确定一个区间,按上面的解释,在这么多的区间中,包含  $\mu$  的约占 95%,不包含  $\mu$  的约仅占 5%.现在抽样得到区间(4.71,5.69),则该区间属于那些包含  $\mu$  的区间的可信程度为 95%,或“该区间包含  $\mu$ ”这一陈述的可信程度为 95%.

置信水平为 $1 - \alpha$ 的置信区间并不是唯一的. 以上例来说, 若给定 $\alpha = 0.05$, 则又有

$$
P \left\{- z _ {0. 0 4} <   \frac {\overline {{X}} - \mu}{\sigma / \sqrt {n}} <   z _ {0. 0 1} \right\} = 0. 9 5,
$$

即 $P\left\{\overline{X} - \frac{\sigma}{\sqrt{n}} z_{0.01} < \mu < \overline{X} + \frac{\sigma}{\sqrt{n}} z_{0.04}\right\} = 0.95.$

故 $\left(\overline{X} -\frac{\sigma}{\sqrt{n}} z_{0.01},\quad \overline{X} +\frac{\sigma}{\sqrt{n}} z_{0.04}\right)$ (4.8)

也是 $\mu$ 的置信水平为0.95的置信区间.我们将它与(4.5)式中令 $\alpha = 0.05$ 所得的置信水平为0.95的置信区间相比较，可知由(4.5)式所确定的区间的长度为$2\times \frac{\sigma}{\sqrt{n}} z_{0.025} = 3.92\times \frac{\sigma}{\sqrt{n}}$ ，这一长度要比区间(4.8)式的长度 $\frac{\sigma}{\sqrt{n}} (z_{0.04} + z_{0.01}) =$ $4.08\times \frac{\sigma}{\sqrt{n}}$ 短.置信区间短表示估计的精度高.故由(4.5)式给出的区间较(4.8)式为优.易知，像 $N(0,1)$ 分布那样其概率密度的图形是单峰且对称的情况，当 $n$ 固定时，以形如(4.5)式那样的区间其长度为最短，我们自然选用它

参考上例可得寻求未知参数 $\theta$ 的置信区间的具体做法如下.

$1^{\circ}$ 寻求一个样本 $X_{1}, X_{2}, \cdots, X_{n}$ 和 $\theta$ 的函数 $W = W(X_{1}, X_{2}, \cdots, X_{n}; \theta)$，使得 $W$ 的分布不依赖于 $\theta$ 以及其他未知参数，称具有这种性质的函数 $W$ 为枢轴量.

$2^{\circ}$ 对于给定的置信水平 $1 - \alpha$ ，定出两个常数 $a, b$ 使得

$$
P \{a <   W (X _ {1}, X _ {2}, \dots , X _ {n}; \theta) <   b \} = 1 - \alpha .
$$

若能从  $a < W(X_{1}, X_{2}, \cdots, X_{n}; \theta) < b$  得到与之等价的  $\theta$  的不等式  $\underline{\theta} < \theta < \overline{\theta}$ ，其中$\underline{\theta}=\underline{\theta}(X_{1},X_{2},\cdots,X_{n}),\bar{\theta}=\bar{\theta}(X_{1},X_{2},\cdots,X_{n})$ 都是统计量，那么 $(\underline{\theta},\bar{\theta})$ 就是 $\theta$ 的一个置信水平为 $1-\alpha$ 的置信区间.

枢轴量  $W(X_{1}, X_{2}, \cdots, X_{n}; \theta)$  的构造，通常可以从  $\theta$  的点估计着手考虑。常用的正态总体的参数的置信区间可以用上述步骤推得。

## § 5 正态总体均值与方差的区间估计

## （一）单个总体  $N(\mu, \sigma^{2})$  的情况

设已给定置信水平为  $1-\alpha$ ，并设  $X_{1}, X_{2}, \cdots, X_{n}$  为总体  $N(\mu, \sigma^{2})$  的样本。 $\overline{X}$ ， $S^{2}$  分别是样本均值和样本方差。

1. 均值 $\mu$ 的置信区间

(1) $\sigma^2$ 为已知, 此时由 §4 例 1 采用 (4.2) 式中的枢轴量 $\frac{\overline{X} - \mu}{\sigma / \sqrt{n}}$, 已得到 $\mu$ 的一个置信水平为 $1 - \alpha$ 的置信区间为

$$
\left(\overline {{X}} \pm \frac {\sigma}{\sqrt {n}} z _ {\alpha / 2}\right). \tag {5.1}
$$

(2) $\sigma^2$ 为未知, 此时不能使用 (5.1) 式给出的区间, 因其中含未知参数 $\sigma$. 考虑到 $S^2$ 是 $\sigma^2$ 的无偏估计, 将 (4.2) 式中的 $\sigma$ 换成 $S = \sqrt{S^2}$, 由第六章 §3 定理 4, 知

$$
\frac {\overline {{X}} - \mu}{S / \sqrt {n}} \sim t (n - 1), \tag {5.2}
$$

并且右边的分布 $t(n - 1)$ 不依赖于任何未知参数. 使用 $\frac{\overline{X} - \mu}{S / \sqrt{n}}$ 作为枢轴量可得（参见图7-3）

![](images/page_180_chart_13.jpg)

<details>
<summary>area</summary>

| Interval | Value |
| --- | --- |
| Left Tail | \(\alpha/2\) |
| Left to center | \(-t_{\alpha/2}(n-1)\) |
| Center | O |
| Right Tail | \(\alpha/2\) |
| Right to center | \(t_{\alpha/2}(n-1)\) |
</details>

图7-3

$$
P \Biggl \{- t _ {\alpha / 2} (n - 1) <   \frac {\overline {{X}} - \mu}{S / \sqrt {n}} <   t _ {\alpha / 2} (n - 1) \Biggr \} = 1 - \alpha , \tag {5.3}
$$

即

$$
P \Bigg \{\overline {{X}} - \frac {S}{\sqrt {n}} t _ {\alpha / 2} (n - 1) <   \mu <   \overline {{X}} + \frac {S}{\sqrt {n}} t _ {\alpha / 2} (n - 1) \Bigg \} = 1 - \alpha .
$$

于是得 $\mu$ 的一个置信水平为 $1 - \alpha$ 的置信区间

$$
\left(\overline {{X}} \pm \frac {S}{\sqrt {n}} t _ {\alpha / 2} (n - 1)\right). \tag {5.4}
$$

例 1 有一大批糖果. 现从中随机地取 16 袋, 称得质量(以 g 计)如下:

| 506 | 508 | 499 | 503 | 504 | 510 | 497 | 512 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 514 | 505 | 493 | 496 | 506 | 502 | 509 | 496 |

设袋装糖果的质量近似地服从正态分布,试求总体均值  $\mu$  的置信水平为 0.95 的置信区间.

解 这里 $1 - \alpha = 0.95, \alpha / 2 = 0.025, n - 1 = 15, t_{0.025}(15) = 2.1315$，由给出的数据算得 $\bar{x} = 503.75, s = 6.2022$。由(5.4)式得均值 $\mu$ 的一个置信水平为0.95的置信区间为

$$
\left(5 0 3. 7 5 \pm \frac {6 . 2 0 2 2}{\sqrt {1 6}} \times 2. 1 3 1 5\right),
$$

即 (500.4, 507.1).

这就是说估计袋装糖果质量的均值在 $500.4\mathrm{g}$ 与 $507.1\mathrm{g}$ 之间，这个估计的可信程度为 $95\%$ .若以此区间内任一值作为 $\mu$ 的近似值，其误差不大于 $\frac{6.2022}{\sqrt{16}}\times$ $2.1315\times 2 = 6.61(\mathrm{g})$ ，这个误差估计的可信程度为 $95\%$ □

在实际问题中,总体方差  $\sigma^{2}$  未知的情况居多,故区间(5.4)式较区间(5.1)式有更大的实用价值.

## 2. 方差 $\sigma^2$ 的置信区间

此处,根据实际问题的需要,只介绍  $\mu$  未知的情况.

$\sigma^{2}$  的无偏估计为  $S^{2}$ ，由第六章 §3

定理3知

$$
\frac {(n - 1) S ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n - 1), \quad (5. 5)
$$

并且上式右端的分布不依赖于任何未知参数, 取  $\frac{(n-1)S^{2}}{\sigma^{2}}$  作为枢轴量, 即得 (参见图7-4)

![](images/page_181_chart_16.jpg)

<details>
<summary>area</summary>

| Interval | Description |
| --- | --- |
| Left | \(\alpha/2\) |
| Right | \(\alpha/2\) |
</details>

图7-4

$$
P \Bigg \{\chi_ {1 - \alpha / 2} ^ {2} (n - 1) <   \frac {(n - 1) S ^ {2}}{\sigma^ {2}} <   \chi_ {\alpha / 2} ^ {2} (n - 1) \Bigg \} = 1 - \alpha , \tag {5.6}
$$

即 $P\left\{\frac{(n - 1)S^2}{\chi_{\alpha /2}^2(n - 1)} < \sigma^2 < \frac{(n - 1)S^2}{\chi_{1 - \alpha /2}^2(n - 1)}\right\} = 1 - \alpha .$ (5.6)'

这就得到方差 $\sigma^2$ 的一个置信水平为 $1 - \alpha$ 的置信区间

$$
\Big (\frac {(n - 1) S ^ {2}}{\chi_ {\alpha / 2} ^ {2} (n - 1)}, \frac {(n - 1) S ^ {2}}{\chi_ {1 - \alpha / 2} ^ {2} (n - 1)} \Big). \tag {5.7}
$$

由 $(5.6)^{\prime}$ 式,还可得到标准差 $\sigma$ 的一个置信水平为 $1-\alpha$ 的置信区间

$$
\left(\frac {\sqrt {n - 1} S}{\sqrt {\chi_ {\alpha / 2} ^ {2} (n - 1)}}, \frac {\sqrt {n - 1} S}{\sqrt {\chi_ {1 - \alpha / 2} ^ {2} (n - 1)}}\right). \tag {5.8}
$$

注意，在概率密度函数不对称时，如 $\chi^2$ 分布和 $F$ 分布，习惯上仍是取对称的分位数（如图7-4中的上分位数 $\chi_{1 - \alpha /2}^2 (n - 1)$ 与 $\chi_{\alpha /2}^2 (n - 1)$ )来确定置信区间的.

例 2 求例 1 中总体标准差  $\sigma$  的置信水平为 0.95 的置信区间.

解 现在 $\alpha / 2 = 0.025, 1 - \alpha / 2 = 0.975, n - 1 = 15$，查表得 $\chi_{0.025}^{2}(15) = 27.488, \chi_{0.975}^{2}(15) = 6.262$，又 $s = 6.2022$，由(5.8)式得所求的标准差 $\sigma$ 的一个置信水平为0.95的置信区间为

$$
(4. 5 8, 9. 6 0).
$$

## （二）两个总体  $N(\mu_{1},\sigma_{1}^{2})$ ,  $N(\mu_{2},\sigma_{2}^{2})$  的情况

在实际中常遇到下面的问题:已知产品的某一质量指标服从正态分布,但由于原料、设备条件、操作人员不同,或工艺过程的改变等因素,引起总体均值、总体方差有所改变.我们需要知道这些变化有多大,这就需要考虑两个正态总体均值差或方差比的估计问题.

设已给定置信水平为 $1 - \alpha$，并设 $X_{1}, X_{2}, \cdots, X_{n_{1}}$ 是来自第一个总体的样本；$Y_{1}, Y_{2}, \cdots, Y_{n_{2}}$ 是来自第二个总体的样本，这两个样本相互独立。且设 $\overline{X}, \overline{Y}$ 分别为第一、第二个总体的样本均值，$S_{1}^{2}, S_{2}^{2}$ 分别是第一、第二个总体的样本方差。

1. 两个总体均值差 $\mu_{1} - \mu_{2}$ 的置信区间

(1) $\sigma_1^2, \sigma_2^2$ 均为已知. 因 $\overline{X}, \overline{Y}$ 分别为 $\mu_1, \mu_2$ 的无偏估计, 故 $\overline{X} - \overline{Y}$ 是 $\mu_1 - \mu_2$ 的无偏估计. 由 $\overline{X}, \overline{Y}$ 的独立性以及 $\overline{X} \sim N(\mu_1, \sigma_1^2 / n_1), \overline{Y} \sim N(\mu_2, \sigma_2^2 / n_2)$ 得

$$
\overline {{X}} - \overline {{Y}} \sim N \Big (\mu_ {1} - \mu_ {2}, \frac {\sigma_ {1} ^ {2}}{n _ {1}} + \frac {\sigma_ {2} ^ {2}}{n _ {2}} \Big)
$$

或

$$
\frac {(\overline {{X}} - \overline {{Y}}) - (\mu_ {1} - \mu_ {2})}{\sqrt {\frac {\sigma_ {1} ^ {2}}{n _ {1}} + \frac {\sigma_ {2} ^ {2}}{n _ {2}}}} \sim N (0, 1), \tag {5.9}
$$

取(5.9)式左边的函数为枢轴量,即得  $\mu_{1}-\mu_{2}$  的一个置信水平为  $1-\alpha$  的置信区间

$$
\left(\overline {{X}} - \overline {{Y}} \pm z _ {\alpha / 2} \sqrt {\frac {\sigma_ {1} ^ {2}}{n _ {1}} + \frac {\sigma_ {2} ^ {2}}{n _ {2}}}\right). \tag {5.10}
$$

(2) $\sigma_1^2 = \sigma_2^2 = \sigma^2$，但 $\sigma^2$ 为未知。此时，由第六章 §3 定理 5

$$
\frac {(\overline {{X}} - \overline {{Y}}) - (\mu_ {1} - \mu_ {2})}{S _ {\mathrm{w}} \sqrt {\frac {1}{n _ {1}} + \frac {1}{n _ {2}}}} \sim t (n _ {1} + n _ {2} - 2). \tag {5.11}
$$

取(5.11)式左边的函数为枢轴量,可得  $\mu_{1}-\mu_{2}$  的一个置信水平为  $1-\alpha$  的置信区间为

$$
\left(\overline {{X}} - \overline {{Y}} \pm t _ {\alpha / 2} (n _ {1} + n _ {2} - 2) S _ {W} \sqrt {\frac {1}{n _ {1}} + \frac {1}{n _ {2}}}\right). \tag {5.12}
$$

此处 $S_W^2 = \frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2},\quad S_W = \sqrt{S_W^2}.$ (5.13)

例3 为比较I，Ⅱ两种型号步枪子弹的枪口速度，随机地取I型子弹10发，得到枪口速度的平均值为 $\bar{x}_1 = 500\mathrm{m / s}$，标准差 $s_1 = 1.10\mathrm{m / s}$，随机地取Ⅱ型子弹20发，得到枪口速度的平均值为 $\bar{x}_2 = 496\mathrm{m / s}$，标准差 $s_2 = 1.20\mathrm{m / s}$。假设两总体都可认为近似地服从正态分布，且由生产过程可认为方差相等。求两总体均值差 $\mu_{1} - \mu_{2}$ 的一个置信水平为0.95的置信区间。

解 按实际情况, 可认为分别来自两个总体的样本是相互独立的. 又因假设两总体的方差相等, 但数值未知, 故可用(5.12)式求均值差的置信区间. 由于 $1 - \alpha = 0.95, \alpha / 2 = 0.025, n_1 = 10, n_2 = 20, n_1 + n_2 - 2 = 28, t_{0.025}(28) = 2.0484.$ $s_w^2 = (9 \times 1.10^2 + 19 \times 1.20^2) / 28, s_w = \sqrt{s_w^2} = 1.1688$, 故所求的两总体均值差 $\mu_1 - \mu_2$ 的一个置信水平为0.95的置信区间是

$$
\left(\bar {x} _ {1} - \bar {x} _ {2} \pm s _ {w} \times t _ {0. 0 2 5} (2 8) \sqrt {\frac {1}{1 0} + \frac {1}{2 0}}\right) = (4 \pm 0. 9 3),
$$

即
(3.07, 4.93).

本题中得到的置信区间的下限大于零,在实际中我们就认为  $\mu_{1}$  比  $\mu_{2}$  大. □

例 4 为提高某一化学生产过程的得率,试图采用一种新的催化剂.为慎重起见,在实验工厂先进行试验.设采用原来的催化剂进行了 $n_1 = 8$ 次试验,得到得率的平均值 $\bar{x}_1 = 91.73$,样本方差 $s_1^2 = 3.89$;又采用新的催化剂进行了 $n_2 = 8$ 次试验,得到得率的平均值 $\bar{x}_2 = 93.75$,样本方差 $s_2^2 = 4.02$.假设两总体都可认为服从正态分布,且方差相等,两样本独立.试求两总体均值差 $\mu_1 - \mu_2$ 的置信水平为 0.95 的置信区间.

解 现在

$$
s _ {w} ^ {2} = \frac {(n _ {1} - 1) s _ {1} ^ {2} + (n _ {2} - 1) s _ {2} ^ {2}}{n _ {1} + n _ {2} - 2} = 3. 9 6, \quad s _ {w} = \sqrt {3 . 9 6}.
$$

由(5.12)式得所求的置信区间为

$$
\left(\bar {x} _ {1} - \bar {x} _ {2} \pm t _ {0. 0 2 5} (1 4) s _ {w} \sqrt {\frac {1}{8} + \frac {1}{8}}\right) = (- 2. 0 2 \pm 2. 1 3),
$$

即 $(-4.15, 0.11)$.

由于所得置信区间包含零,在实际中我们就认为采用这两种催化剂所得的得率的均值没有显著差别. □

## 2. 两个总体方差比 $\sigma_1^2 / \sigma_2^2$ 的置信区间

我们仅讨论总体均值  $\mu_{1}, \mu_{2}$  均为未知的情况，由第六章 §3 定理 5

$$
\frac {S _ {1} ^ {2} / S _ {2} ^ {2}}{\sigma_ {1} ^ {2} / \sigma_ {2} ^ {2}} \sim F (n _ {1} - 1, n _ {2} - 1), \tag {5.14}
$$

并且分布 $F(n_{1} - 1, n_{2} - 1)$ 不依赖任何未知参数. 取 $\frac{S_1^2 / S_2^2}{\sigma_1^2 / \sigma_2^2}$ 为枢轴量得

$$
P \left\{F _ {1 - \alpha / 2} (n _ {1} - 1, n _ {2} - 1) <   \frac {S _ {1} ^ {2} / S _ {2} ^ {2}}{\sigma_ {1} ^ {2} / \sigma_ {2} ^ {2}} <   F _ {\alpha / 2} (n _ {1} - 1, n _ {2} - 1) \right\} = 1 - \alpha , \tag {5.15}
$$

即

$$
P \left\{\frac {S _ {1} ^ {2}}{S _ {2} ^ {2}} \frac {1}{F _ {\alpha / 2} (n _ {1} - 1 , n _ {2} - 1)} <   \frac {\sigma_ {1} ^ {2}}{\sigma_ {2} ^ {2}} <   \frac {S _ {1} ^ {2}}{S _ {2} ^ {2}} \frac {1}{F _ {1 - \alpha / 2} (n _ {1} - 1 , n _ {2} - 1)} \right\} = 1 - \alpha . \tag {5.15}
$$

于是得 $\sigma_1^2 /\sigma_2^2$ 的一个置信水平为 $1 - \alpha$ 的置信区间为

$$
\Big (\frac {S _ {1} ^ {2}}{S _ {2} ^ {2}} \frac {1}{F _ {\alpha / 2} (n _ {1} - 1 , n _ {2} - 1)}, \quad \frac {S _ {1} ^ {2}}{S _ {2} ^ {2}} \frac {1}{F _ {1 - \alpha / 2} (n _ {1} - 1 , n _ {2} - 1)} \Big). \tag {5.16}
$$

例 5 研究由机器 A 和机器 B 生产的钢管的内径(以 mm 计)，随机抽取机器 A 生产的管子 18 只，测得样本方差  $s_{1}^{2}=0.34$ ；抽取机器 B 生产的管子 13 只，测得样本方差  $s_{2}^{2}=0.29$ 。设两样本相互独立，且设由机器 A，机器 B 生产的管子的内径分别服从正态分布  $N(\mu_{1},\sigma_{1}^{2}), N(\mu_{2},\sigma_{2}^{2})$ ，这里  $\mu_{i}, \sigma_{i}^{2} (i=1,2)$  均未知。试求方差比  $\sigma_{1}^{2}/\sigma_{2}^{2}$  的置信水平为 0.90 的置信区间。

解 现在 $n_1 = 18, s_1^2 = 0.34, n_2 = 13, s_2^2 = 0.29, \alpha = 0.10, F_{\alpha/2}(n_1 - 1, n_2 - 1) = F_{0.05}(17, 12) = 2.59, F_{1-\alpha/2}(17, 12) = F_{0.95}(17, 12) = \frac{1}{F_{0.05}(12, 17)} = \frac{1}{2.38}$, 于是由 (5.16) 式得 $\sigma_1^2 / \sigma_2^2$ 的一个置信水平为 0.90 的置信区间为

$$
\left(\frac {0 . 3 4}{0 . 2 9} \times \frac {1}{2 . 5 9}, \quad \frac {0 . 3 4}{0 . 2 9} \times 2. 3 8\right),
$$

即
(0.45, 2.79).

由于 $\sigma_1^2 /\sigma_2^2$ 的置信区间包含1，在实际中我们就认为 $\sigma_1^2,\sigma_2^2$ 两者没有显著差别. □

## § 6 (0-1)分布参数的区间估计

设有一容量 $n > 50$ 的大样本，它来自(0-1)分布的总体 $X, X$ 的分布律为

$$
f (x; p) = p ^ {x} (1 - p) ^ {1 - x}, \quad x = 0, 1, \tag {6.1}
$$

其中 $p$ 为未知参数. 现在来求 $p$ 的置信水平为 $1 - \alpha$ 的置信区间.

已知(0-1)分布的均值和方差分别为

$$
\mu = p, \quad \sigma^ {2} = p (1 - p). \tag {6.2}
$$

设  $X_{1}, X_{2}, \cdots, X_{n}$  是一个样本. 因样本容量 n 较大, 由中心极限定理, 知

$$
\frac {\sum_ {i = 1} ^ {n} X _ {i} - n p}{\sqrt {n p (1 - p)}} = \frac {n \overline {{X}} - n p}{\sqrt {n p (1 - p)}} \tag {6.3}
$$

近似地服从  $N(0,1)$  分布,于是有

$$
P \left\{- z _ {\alpha / 2} <   \frac {n \overline {{X}} - n p}{\sqrt {n p (1 - p)}} <   z _ {\alpha / 2} \right\} \approx 1 - \alpha . \tag {6.4}
$$

而不等式 $-z_{\alpha /2} < \frac{n\overline{X} - np}{\sqrt{np(1 - p)}} < z_{\alpha /2}$ (6.5)

等价于

$$
(n + z _ {\alpha / 2} ^ {2}) p ^ {2} - (2 n \overline {{X}} + z _ {\alpha / 2} ^ {2}) p + n \overline {{X}} ^ {2} <   0. \tag {6.6}
$$

记 $p_1 = \frac{1}{2a} (-b - \sqrt{b^2 - 4ac})$ ， (6.7)

$$
p _ {2} = \frac {1}{2 a} (- b + \sqrt {b ^ {2} - 4 a c}), \tag {6.8}
$$

此处 $a = n + z_{\alpha /2}^2, b = -(2n\overline{X} + z_{\alpha /2}^2), c = n\overline{X}^2$。于是由(6.5)式得 $p$ 的一个近似的置信水平为 $1 - \alpha$ 的置信区间为

$$
(p _ {1}, p _ {2}).
$$

例 设自一大批产品的 100 个样品中, 得一级品 60 个, 求这批产品的一级品率 $p$ 的置信水平为 0.95 的置信区间.

解 一级品率 p 是(0-1)分布的参数, 此处 n=100,  $\bar{x}=60/100=0.6, 1-\alpha=0.95, \alpha/2=0.025, z_{\alpha/2}=1.96$ , 按(6.7), (6.8)式来求 p 的置信区间, 其中

$$
a = n + z _ {\alpha / 2} ^ {2} = 1 0 3. 8 4, \quad b = - (2 n \bar {x} + z _ {\alpha / 2} ^ {2}) = - 1 2 3. 8 4, \quad c = n \bar {x} ^ {2} = 3 6.
$$

于是  $p_{1}=0.50,\quad p_{2}=0.69.$

故得 $p$ 的一个置信水平为0.95的近似置信区间为

$$
(0. 5 0, 0. 6 9).
$$

## § 7 单侧置信区间

在上述讨论中,对于未知参数  $\theta$ , 我们给出两个统计量  $\underline{\theta}, \bar{\theta}$ , 得到  $\theta$  的双侧置信区间  $(\underline{\theta}, \bar{\theta})$ . 但在某些实际问题中, 例如, 对于设备、元件的寿命来说, 平均寿命长是我们所希望的, 我们关心的是平均寿命  $\theta$  的“下限”; 与之相反, 在考虑化学药品中杂质含量的均值 $\mu$ 时，我们常关心参数 $\mu$ 的“上限”.这就引出了单侧置信区间的概念.

对于给定值  $\alpha(0<\alpha<1)$ ，若由样本  $X_{1}, X_{2}, \cdots, X_{n}$  确定的统计量  $\underline{\theta}=\underline{\theta}(X_{1}, X_{2}, \cdots, X_{n})$ ，对于任意  $\theta\in\Theta$  满足

$$
P \{\theta > \underline {{\theta}} \} \geqslant 1 - \alpha , \tag {7.1}
$$

称随机区间 $(\underline{\theta},\infty)$ 是 $\theta$ 的置信水平为 $1 - \alpha$ 的单侧置信区间，$\underline{\theta}$ 称为 $\theta$ 的置信水平为 $1 - \alpha$ 的单侧置信下限.

又若统计量  $\bar{\theta}=\bar{\theta}(X_{1},X_{2},\cdots,X_{n})$ ，对于任意  $\theta\in\Theta$  满足

$$
P \{\theta <   \overline {{\theta}} \} \geqslant 1 - \alpha , \tag {7.2}
$$

称随机区间 $(-∞, \bar{θ})$ 是 $\theta$ 的置信水平为 $1-α$ 的单侧置信区间，$\bar{\theta}$ 称为 $\theta$ 的置信水平为 $1-α$ 的单侧置信上限.

例如对于正态总体 X，若均值  $\mu$ ，方差  $\sigma^{2}$  均为未知，设  $X_{1}, X_{2}, \cdots, X_{n}$  是一个样本，由

$$
\frac {\overline {{X}} - \mu}{S / \sqrt {n}} \sim t (n - 1)
$$

有(见图 7-5)

$$
P \left\{\frac {\overline {{X}} - \mu}{S / \sqrt {n}} <   t _ {\alpha} (n - 1) \right\} = 1 - \alpha ,
$$

即 $P\left\{\mu >\overline{X} -\frac{S}{\sqrt{n}} t_{\alpha}(n - 1)\right\} = 1 - \alpha .$

![](images/page_186_image_14.jpg)

<details>
<summary>text_image</summary>

O
tₐ(n-1)
α
</details>

图7-5

于是得到 $\mu$ 的置信水平为 $1 - \alpha$ 的单侧置信区间

$$
\left(\overline {{X}} - \frac {S}{\sqrt {n}} t _ {\alpha} (n - 1), \quad \infty\right). \tag {7.3}
$$

$\mu$ 的置信水平为 $1 - \alpha$ 的单侧置信下限为

$$
\underline {{\mu}} = \overline {{X}} - \frac {S}{\sqrt {n}} t _ {\alpha} (n - 1). \tag {7.4}
$$

又由

$$
\frac {(n - 1) S ^ {2}}{\sigma^ {2}} \sim \chi^ {2} (n - 1),
$$

有(见图 7-6)

$$
P \Bigg \{\frac {(n - 1) S ^ {2}}{\sigma^ {2}} > \chi_ {1 - \alpha} ^ {2} (n - 1) \Bigg \} = 1 - \alpha ,
$$

即 $P\left\{\sigma^2 < \frac{(n - 1)S^2}{\chi_{1 - \alpha}^2(n - 1)}\right\} = 1 - \alpha .$

![](images/page_187_chart_5.jpg)

<details>
<summary>area</summary>

| X-axis | Y-axis |
| --- | --- |
| O | 0 |
| \(\chi^{2}_{1-\alpha}(n-1)\) | — |
</details>

图7-6

于是得 $\sigma^2$ 的置信水平为 $1 - \alpha$ 的单侧置信区间

$$
\left(0, \frac {(n - 1) S ^ {2}}{\chi_ {1 - \alpha} ^ {2} (n - 1)}\right). \tag {7.5}
$$

$\sigma^2$ 的置信水平为 $1 - \alpha$ 的单侧置信上限为

$$
\overline {{\sigma^ {2}}} = \frac {(n - 1) S ^ {2}}{\chi_ {1 - \alpha} ^ {2} (n - 1)}. \tag {7.6}
$$

例 从一批灯泡中随机地取 5 只作寿命试验, 测得寿命(以 h 计)为

$$
1 0 5 0 \quad 1 1 0 0 \quad 1 1 2 0 \quad 1 2 5 0 \quad 1 2 8 0
$$

设灯泡寿命服从正态分布. 求灯泡寿命均值的置信水平为 0.95 的单侧置信下限.

解 $1 - \alpha = 0.95, n = 5, t_{\alpha}(n - 1) = t_{0.05}(4) = 2.1318, \bar{x} = 1160, s^2 = 9950.$ 由(7.4)式得所求单侧置信下限为

$$
\underline {{\mu}} = \overline {{x}} - \frac {s}{\sqrt {n}} t _ {\alpha} (n - 1) = 1 0 6 5.
$$

小结

参数估计问题分为点估计和区间估计.点估计是适当地选择一个统计量作为未知参数的估计(称为估计量)，若已取得一样本，将样本值代入估计量，得到估计量的值，以估计量的值作为未知参数的近似值(称为估计值).

本章介绍了两种求点估计的方法:矩估计法和最大似然估计法.

矩估计法的做法是,以样本矩作为总体矩的估计量,而以样本矩的连续函数作为相应的总体矩的连续函数的估计量,从而得到总体未知参数的估计.

最大似然估计法的基本想法是，若已观察到样本 $(X_{1},X_{2},\cdots,X_{n})$ 的样本值 $(x_{1},x_{2},\cdots,$ $x_{n}$ ，而取到这一样本值的概率为 p（在离散型的情况），或  $(X_{1}, X_{2}, \cdots, X_{n})$  落在这一样本值  $(x_{1}, x_{2}, \cdots, x_{n})$  的邻域内的概率为 p（在连续型的情况），而 p 与未知参数有关，我们就取  $\theta$  的估计值使概率 p 取到最大.

对于一个未知参数可以提出不同的估计量,因此自然提出比较估计量的好坏的问题,这就需要给出评定估计量好坏的标准.估计量是一个随机变量,对于不同的样本值,一般给出参数的不同估计值.因而在考虑估计量的好坏时,应从某种整体性能去衡量,而不能看它在个别样本之下表现如何.本章介绍了三个标准:无偏性、有效性和相合性.相合性是对估计量的一个基本要求,不具备相合性的估计量,我们一般是不考虑的.

点估计不能反映估计的精度,我们引入了区间估计.置信区间是一个随机区间 $(\underline{\theta},\overline{\theta})$ ,它覆盖未知参数具有预先给定的高概率(置信水平),即对于任意 $\theta\in\Theta$ ,有

$$
P \{\underline {{\theta}} <   \theta <   \overline {{\theta}} \} \geqslant 1 - \alpha .
$$

例如，对于正态分布 $N(\mu, \sigma^2), \sigma^2$ 未知，可得 $\mu$ 的一个置信水平为 $1 - \alpha$ 的置信区间为

$$
\left(\overline {{X}} - t _ {\alpha / 2} (n - 1) \frac {S}{\sqrt {n}}, \quad \overline {{X}} + t _ {\alpha / 2} (n - 1) \frac {S}{\sqrt {n}}\right), \tag {5.4}
$$

就是说这一随机区间覆盖  $\mu$  的概率  $\geqslant 1 - \alpha$ . 一旦有了一个样本值  $x_{1}, x_{2}, \cdots, x_{n}$ ，将它代入 (5.4) 式，得到一个数字区间

$$
\Big (\bar {x} - t _ {\alpha / 2} (n - 1) \frac {s}{\sqrt {n}}, \quad \bar {x} + t _ {\alpha / 2} (n - 1) \frac {s}{\sqrt {n}} \Big) \stackrel {\text {记成}} {=} (- c, c),
$$

$(-c, c)$ 也称为 $\mu$ 的置信水平为 $1 - \alpha$ 的置信区间，意指“$(-c, c)$ 包含 $\mu$”这一陈述的可信程度为 $1 - \alpha$。如果将这事实写成 $P\{-c < \mu < c\} = 1 - \alpha$ 是错误的，因为 $(-c, c)$ 是一个数字区间，要么有 $\mu \in (-c, c)$，此时 $P\{-c < \mu < c\} = 1$；要么有 $\mu \notin (-c, c)$，此时 $P\{-c < \mu < c\} = 0$。

本章还介绍了单侧置信区间，例如，对于正态分布 $N(\mu, \sigma^2), \sigma^2$ 未知，可得 $\mu$ 的置信水平为 $1 - \alpha$ 的单侧置信区间为

(i) $\left(-\infty,\quad\overline{X}+t_{\alpha}(n-1)\frac{S}{\sqrt{n}}\right)$ ，单侧置信上限为 $\overline{\mu}=\overline{X}+t_{\alpha}(n-1)\frac{S}{\sqrt{n}}$ .

(ii) $\left(\overline{X} - t_{\alpha}(n - 1)\frac{S}{\sqrt{n}}, \quad \infty\right)$, 单侧置信下限为 $\underline{\mu} = \overline{X} - t_{\alpha}(n - 1)\frac{S}{\sqrt{n}}$.

在形式上, 只需将置信区间(5.4)式的上下限中的“ $\alpha/2$ ”改成“ $\alpha$ ”, 就得到相应的单侧置信上下限了.

## ■ 重要术语及主题

矩估计量 最大似然估计量

估计量的评选标准:无偏性、有效性、相合性

参数  $\theta$  的置信水平为  $1-\alpha$  的置信区间 枢轴量

参数 $\theta$ 的单侧置信上限和单侧置信下限

单个正态总体均值、方差的置信区间、单侧置信上限与单侧置信下限(见表7-1)

两个正态总体均值差、方差比的置信区间、单侧置信上限与单侧置信下限(见表7-1)

表 7-1 正态总体均值、方差的置信区间与单侧置信限 (置信水平为 $1 - \alpha$ )

<table><tr><td></td><td>待估参数</td><td>其他参数</td><td>枢轴量的分布</td><td>置信区间</td><td>单侧置信限</td></tr><tr><td rowspan="3">单个正态总体</td><td>μ</td><td> $\sigma^2$ 已知</td><td> $Z = \frac{\overline{X} - \mu}{\sigma / \sqrt{n}} \sim N(0,1)$ </td><td> $\left( \overline{X} \pm \frac{\sigma}{\sqrt{n}} z_{\alpha/2} \right)$ </td><td> $\bar{\mu} = \overline{X} + \frac{\sigma}{\sqrt{n}} z_\alpha \quad \underline{\mu} = \overline{X} - \frac{\sigma}{\sqrt{n}} z_\alpha$ </td></tr><tr><td>μ</td><td> $\sigma^2$ 未知</td><td> $t = \frac{\overline{X} - \mu}{S / \sqrt{n}} \sim t(n-1)$ </td><td> $\left( \overline{X} \pm \frac{S}{\sqrt{n}} t_{\alpha/2}(n-1) \right)$ </td><td> $\bar{\mu} = \overline{X} + \frac{S}{\sqrt{n}} t_\alpha(n-1) \quad \underline{\mu} = \overline{X} - \frac{S}{\sqrt{n}} t_\alpha(n-1)$ </td></tr><tr><td> $\sigma^2$ </td><td>μ未知</td><td> $\chi^2 = \frac{(n-1) S^2}{\sigma^2} \sim \chi^2(n-1)$ </td><td> $\left( \frac{(n-1) S^2}{\chi_{\alpha/2}^2(n-1)}, \frac{(n-1) S^2}{\chi_{1-\alpha/2}^2(n-1)} \right)$ </td><td> $\overline{\sigma^2} = \frac{(n-1) S^2}{\chi_{1-\alpha}^2(n-1)} \quad \underline{\sigma^2} = \frac{(n-1) S^2}{\chi_{\alpha}^2(n-1)}$ </td></tr><tr><td rowspan="3">两个正态总体</td><td> $\mu_1 - \mu_2$ </td><td> $\sigma_1^2, \sigma_2^2$ 已知</td><td> $Z = \frac{(\overline{X} - \overline{Y}) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim N(0,1)$ </td><td> $\left( \overline{X} - \overline{Y} \pm z_{\alpha/2} \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}} \right)$ </td><td> $\overline{\mu_1 - \mu_2} = \overline{X} - \overline{Y} + z_\alpha \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$  $\underline{\mu_1 - \mu_2} = \overline{X} - \overline{Y} - z_\alpha \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$ </td></tr><tr><td> $\mu_1 - \mu_2$ </td><td> $\sigma_1^2 = \sigma_2^2 = \sigma^2$ 未知</td><td> $t = \frac{(\overline{X} - \overline{Y}) - (\mu_1 - \mu_2)}{S_W \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t(n_1 + n_2 - 2)$  $S_W^2 = \frac{(n_1 - 1) S_1^2 + (n_2 - 1) S_2^2}{n_1 + n_2 - 2}$ </td><td> $\left( \overline{X} - \overline{Y} \pm t_{\alpha/2}(n_1 + n_2 - 2) \times S_W \sqrt{\frac{1}{n_1} + \frac{1}{n_2}} \right)$ </td><td> $\overline{\mu_1 - \mu_2} = \overline{X} - \overline{Y} + t_\alpha(n_1 + n_2 - 2) S_W \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$  $\underline{\mu_1 - \mu_2} = \overline{X} - \overline{Y} - t_\alpha(n_1 + n_2 - 2) S_W \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$ </td></tr><tr><td> $\frac{\sigma_1^2}{\sigma_2^2}$ </td><td> $\mu_1, \mu_2$ 未知</td><td> $F = \frac{S_1^2 / S_2^2}{\sigma_1^2 / \sigma_2^2} \sim F(n_1 - 1, n_2 - 1)$ </td><td> $\left( \frac{S_1^2}{S_2^2} \frac{1}{F_{\alpha/2}(n_1 - 1, n_2 - 1)}, \frac{S_1^2}{S_2^2} \frac{1}{F_{1-\alpha/2}(n_1 - 1, n_2 - 1)} \right)$ </td><td> $\left( \frac{\overline{\sigma_1^2}}{\sigma_2^2} \right) = \frac{S_1^2}{S_2^2} \frac{1}{F_{1-\alpha}(n_1 - 1, n_2 - 1)}$  $\left( \frac{\sigma_1^2}{\sigma_2^2} \right) = \frac{S_1^2}{S_2^2} \frac{1}{F_\alpha(n_1 - 1, n_2 - 1)}$ </td></tr></table>

## 习题

1. 随机地取 8 只活塞环, 测得它们的直径为 (以 mm 计)

$$
\begin{array}{l} 7 4. 0 0 1 \quad 7 4. 0 0 5 \quad 7 4. 0 0 3 \quad 7 4. 0 0 1 \\ 7 4. 0 0 0 \quad 7 3. 9 9 8 \quad 7 4. 0 0 6 \quad 7 4. 0 0 2 \\ \end{array}
$$

试求总体均值  $\mu$  及方差  $\sigma^{2}$  的矩估计值，并求样本方差  $s^{2}$ .

2. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为总体的一个样本， $x_{1}, x_{2}, \cdots, x_{n}$  为一相应的样本值。求下列各总体的概率密度或分布律中的未知参数的矩估计量和矩估计值。

(1) $f(x)=\left\{\begin{aligned}&\theta c^{\theta}x^{-(\theta+1)},&x>c,\\ &0,&\text{其他},\end{aligned}\right.$ 其中c>0为已知， $\theta>1,\theta$ 为未知参数.
(2) $f(x)=\begin{cases}\sqrt{\theta}x^{\sqrt{\theta}-1},&0\leqslant x\leqslant1,\\0,&\text{其他},\end{cases}$ 其中 $\theta>0,\theta$ 为未知参数.
(3) $P\{X=x\}=\binom{m}{x}p^{x}(1-p)^{m-x}, x=0,1,2,\cdots,m$, 其中 0<p<1, p 为未知参数.

3. 求上题中各未知参数的最大似然估计值和估计量.

4.（1）设总体 X 具有分布律

| X | 1 | 2 | 3 |
| --- | --- | --- | --- |
| $p_k$ | $\theta^2$ | $2\theta(1-\theta)$ | $(1-\theta)^2$ |

其中 $\theta (0 < \theta < 1)$ 为未知参数. 已知取得了样本值 $x_{1} = 1, x_{2} = 2, x_{3} = 1$. 试求 $\theta$ 的矩估计值和最大似然估计值.

(2) 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自参数为  $\lambda$  的泊松分布总体的一个样本，试求  $\lambda$  的最大似然估计量及矩估计量.
(3) 设随机变量 X 服从以 r, p 为参数的负二项分布, 其分布律为

$$
P \{X = x _ {k} \} = \binom {x _ {k} - 1} {r - 1} p ^ {r} (1 - p) ^ {x _ {k} - r}, \quad x _ {k} = r, r + 1, \dots ,
$$

其中 r 已知, p 未知. 设有样本值  $x_{1}, x_{2}, \cdots, x_{n}$ , 试求 p 的最大似然估计值.

5. 设某种电子器件的寿命(以 h 计) T 服从双参数的指数分布, 其概率密度为

$$
f (t) = \left\{ \begin{array}{l l}  \frac {1}{\theta} \mathrm{e} ^ {- (t - c) / \theta}, & t \geqslant c, \\ 0, & \text {其他}, \end{array} \right.
$$

其中  $c, \theta (c, \theta > 0)$  为未知参数. 自一批这种器件中随机地取 n 件进行寿命试验. 设它们的失效时间依次为  $x_{1} \leqslant x_{2} \leqslant \cdots \leqslant x_{n}$ .

(1) 求 c 与  $\theta$  的最大似然估计值.
(2) 求 c 与  $\theta$  的矩估计量.

6. 一地质学家为研究密歇根湖湖滩地区的岩石成分,随机地自该地区取100个样品,每个样品有10块石子,记录了每个样品中属石灰石的石子数.假设这100次观察相互独立,并且由过去经验知, 它们都服从参数为 $m = 10, p$ 的二项分布, $p$ 是这地区一块石子是石灰石的概率. 求 $p$ 的最大似然估计值. 该地质学家所得的数据如下:

| 样品中属石灰石的石子数i | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 观察到i块石灰石的样品个数 | 0 | 1 | 6 | 7 | 23 | 26 | 21 | 12 | 3 | 1 | 0 |

7.（1）设 $X_{1}, X_{2}, \cdots, X_{n}$ 是来自总体 $X$ 的一个样本，且 $X \sim \pi(\lambda)$，求 $P\{X = 0\}$ 的最大似然估计值.

（2）某铁路局证实一个扳道员在五年内所引起的严重事故的次数服从泊松分布. 求一个扳道员在五年内未引起严重事故的概率 $p$ 的最大似然估计值. 使用下面122个观察值. 下表中, $r$ 表示一扳道员五年中引起严重事故的次数, $s$ 表示观察到的扳道员人数.

| r | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| s | 44 | 42 | 21 | 9 | 4 | 2 |

8.（1）设 $X_{1}, X_{2}, \dots, X_{n}$ 是来自概率密度为

$$
f (x; \theta) = \left\{ \begin{array}{l l} \theta x ^ {\theta - 1}, & 0 <   x <   1, \\ 0, & \text {其他} \end{array} \right.
$$

的总体的样本, $\theta$ 未知,求 $U=e^{-1/\theta}$ 的最大似然估计值.

(2) 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自正态总体  $N(\mu, 1)$  的样本,  $\mu$  未知, 求  $\theta = P\{X > 2\}$  的最大似然估计值.

（3）设  $x_{1}, x_{2}, \cdots, x_{n}$  是来自总体  $b(m, \theta)$  的样本值，又  $\theta = \frac{1}{3}(1 + \beta)$ ，求  $\beta$  的最大似然估计值.

9.（1）验证教材第六章§3定理5中的统计量

$$
S _ {W} ^ {2} = \frac {n _ {1} - 1}{n _ {1} + n _ {2} - 2} S _ {1} ^ {2} + \frac {n _ {2} - 1}{n _ {1} + n _ {2} - 2} S _ {2} ^ {2} = \frac {(n _ {1} - 1) S _ {1} ^ {2} + (n _ {2} - 1) S _ {2} ^ {2}}{n _ {1} + n _ {2} - 2}
$$

是两总体公共方差 $\sigma^2$ 的无偏估计量（$S_W^2$ 称为 $\sigma^2$ 的合并估计）.

（2）设总体 X 的数学期望为  $\mu, X_{1}, X_{2}, \cdots, X_{n}$  是来自 X 的样本， $a_{1}, a_{2}, \cdots, a_{n}$  是任意常数，验证  $\left(\sum_{i=1}^{n} a_{i} X_{i}\right) / \sum_{i=1}^{n} a_{i}$  （其中  $\sum_{i=1}^{n} a_{i} \neq 0$ ）是  $\mu$  的无偏估计量.

10. 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自总体 X 的一个样本，设  $E(X) = \mu, D(X) = \sigma^{2}$ .

(1) 确定常数 $c$, 使 $c \sum_{i=1}^{n-1} (X_{i+1} - X_i)^2$ 为 $\sigma^2$ 的无偏估计.

(2) 确定常数 c，使  $\overline{X}^{2}-cS^{2}$  是  $\mu^{2}$  的无偏估计 ( $\overline{X}, S^{2}$  是样本均值和样本方差).

11. 设总体 $X$ 的概率密度为

$$
f (x; \theta) = \left\{ \begin{array}{l l} { \frac {1}{\theta} x ^ {(1 - \theta) / \theta},} & {0 <   x <   1,} \\ {0,} & {\text {其他}.} \end{array} \right. \quad 0 <   \theta <   \infty ,
$$

$X_{1}, X_{2}, \cdots, X_{n}$ 是来自总体 X 的样本.