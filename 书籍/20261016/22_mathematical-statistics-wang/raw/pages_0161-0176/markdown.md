证明 令 $z_{1} < z_{2} < \dots < z_{m}$ 为 $\{X_{1}, X_{2}, \dots, X_{n}\}$ 中不相同的 $m$ 个值，而 $n_{j} \geqslant 1$ 是 $X_{i}$ 等于 $z_{j}$ 的个数。令 $p_{j} = F(z_{j}) - F(z_{j-})$ 且设 $\hat{p}_{j} = n_{j}/n$。如果对任意的某个 $j$ 有 $p_{j} = 0$，则 $L(F) = 0 < L(F_{n})$；所以我们假设 $p_{j} > 0$ 且至少有一个 $j$ 使得 $p_{j} \neq \hat{p}_{j}$。注意到对任意的 $x > 0$ 有 $\ln(x) \leqslant x - 1$，且等式仅当 $x = 1$ 时成立。因此，

$$
\ln \left[ \frac {L (F)}{L (F _ {n})} \right] = \sum_ {j = 1} ^ {m} n _ {j} \ln \left(\frac {p _ {j}}{\hat {p} _ {j}}\right) = n \sum_ {j = 1} ^ {m} \hat {p} _ {j} \ln \left(\frac {p _ {j}}{\hat {p} _ {j}}\right) <   n \sum_ {j = 1} ^ {m} \hat {p} _ {j} \left(\frac {p _ {j}}{\hat {p} _ {j}} - 1\right) \leqslant 0,
$$

所以  $L(F) < L(F_{n})$ .

因此, 经验分布函数是 F 的非参数最大似然估计. 类似于参数情形, 我们可使用非参数似然比来构造似然比检验. 对于某个分布 F, 定义非参数似然比为

$$
R (F) = \frac {L (F)}{L (F _ {n})}.
$$

假设我们感兴趣的参数是 $\theta = T(F)$, 其中 $T$ 是关于分布的某一函数. 比如, $\theta = \int x\mathrm{d}F(x)$ 或 $\theta = F^{-1}(\alpha)$. 定义 (剖面) 似然比函数为

$$
R (\theta) = \sup \left\{R (F) \mid T (F) = \theta , F \in \mathcal {F} \right\}.
$$

当 $R(\theta_0) < r_0$ 时, 我们拒绝 $H_0: T(F_0) = \theta_0$, 其中 $r_0$ 是某一临界值. 相应地, 经验似然置信区间构造如下: $\{\theta \mid R(\theta) \geqslant r_0\}$. 在许多问题下, $r_0$ 可由如下的非参数 Wilks 定理得到.

定理 3.4.6（一元经验似然定理）设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自分布函数为  $F_{0}$  的独立同分布样本。令  $\mu_{0} = E(X_{i})$ ，且假设  $0 < \operatorname{Var}(X_{i}) < \infty$ 。则当  $n \to \infty$  时，

$$
- 2 \ln [ R (\mu_ {0}) ] \xrightarrow {\mathrm{d}} \chi_ {1} ^ {2}.
$$

这个定理告诉我们当  $-2\ln[R(\mu_{0})]>\chi_{\alpha}^{2}(1)$  时, 我们以渐近水平为  $\alpha$  拒绝  $\mu=\mu_{0}$ . 下面我们来看如何计算经验似然. 我们可以将剖面经验似然比函数写为

$$
R (\mu) = \max _ {w _ {1}, w _ {2}, \dots , w _ {n}} \left\{\prod_ {i = 1} ^ {n} n w _ {i} \Big | \sum_ {i = 1} ^ {n} w _ {i} X _ {i} = \mu , \sum_ {i = 1} ^ {n} w _ {i} = 1, w _ {i} \geqslant 0 \right\}.
$$

记次序统计量为  $X_{(1)} \leqslant X_{(2)} \leqslant \cdots \leqslant X_{(n)}$ . 首先我们来排除一种情形, 也就是如果  $\mu < X_{(1)}$  或  $\mu > X_{(n)}$ , 则此时不存在权和为 1 的  $w_{i} \geqslant 0$  使得  $\sum_{i=1}^{n} w_{i} X_{i} = \mu$ . 在此情况下, 我们定义  $\ln[R(\mu)] = -\infty$  或者  $R(\mu) = 0$ .

下面我们考虑一般情形, 即  $X_{(1)} < \mu < X_{(n)}$ . 我们需要最大化  $\prod_{i=1}^{n} nw_{i}$ , 或者等价地在约束  $w_{i} \geqslant 0, \sum_{i} w_{i} = 1, \sum_{i} w_{i}(X_{i} - \mu) = 0$  下最大化  $\sum_{i=1}^{n} \ln(nw_{i})$ . 目标函数  $\sum_{i=1}^{n} \ln(nw_{i})$

是一个定义在凸集合上的严格凹函数. 相应地, 唯一的全局最大值是存在的. 我们也知道达到最大值的 $w_{i}$ 不会等于零, 因此是定义域内的一内点. 我们可以使用Lagrange(拉格朗日)乘子法来求解. 记

$$
G = \sum_ {i = 1} ^ {n} \ln (n w _ {i}) - n \lambda \sum_ {i = 1} ^ {n} w _ {i} (X _ {i} - \mu) - \gamma \left(\sum_ {i = 1} ^ {n} w _ {i} - 1\right),
$$

其中 $\lambda$ 和 $\gamma$ 是Lagrange乘子.对 $G$ 关于 $w_{i},\gamma$ 和 $\lambda$ 求偏导得

$$
\frac {\partial G}{\partial w _ {i}} = \frac {1}{w _ {i}} - \gamma - n \lambda (X _ {i} - \mu) = 0, \tag {3.4.9}
$$

$$
\frac {\partial G}{\partial \gamma} = - \sum_ {i = 1} ^ {n} w _ {i} + 1 = 0, \tag {3.4.10}
$$

$$
\frac {\partial G}{\partial \lambda} = n \sum_ {i = 1} ^ {n} w _ {i} (X _ {i} - \mu) = 0. \tag {3.4.11}
$$

在 (3.4.9) 式两边乘 $w_{i}$ 得 $1 - \gamma w_{i} - n\lambda [w_{i}(X_{i} - \mu)] = 0$. 对 $i$ 求和并利用 (3.4.10) 式和 (3.4.11) 式可得 $n - \gamma - 0 = 0$. 也就是, $\gamma = n$. 将 $\gamma = n$ 代入 (3.4.9) 式得 $w_{i} = \frac{1}{n[1 + \lambda(X_{i} - \mu)]}$.

最后, 我们有 $l(\mu) = 2\sum_{i=1}^{n}\ln [1 + \lambda (\mu)(X_i - \mu)]$, 其中 $\lambda(\mu)$ 是方程

$$
\sum_ {i = 1} ^ {n} \frac {X _ {i} - \mu}{1 + \lambda (X _ {i} - \mu)} = 0 \tag {3.4.12}
$$

的解.  $\lambda(\mu)$  的值可通过数值解法得到.

由上述讨论可以看出, 经验似然比检验与参数似然比检验使用类似的思想, 通过比较零假设和备则假设最大似然函数值 (参数或非参数) 的大小来给出零假设正确与否的证据, 而经验似然比也具有类似的 Wilks 现象, 从另一个角度也说明似然比思想具有独特优势. 关于更加复杂情形下的经验似然比检验可参考 Owen (2001).

## 3.5 置信区间

在第二章中我们介绍了点估计, 点估计仅用一个点的数值来估计参数, 因此估计量恰好等于参数真实值的概率往往不会很高. 我们用一个例子说明, 考虑正态总体  $N(\mu,1)$ , 均值  $\mu$  的最大似然估计  $\bar{X}$  恰好正确的概率  $P(\bar{X} = \mu) = 0$ . 因此这种情况下区间估计是更常用的选择. 而在日常生活中, 我们经常听到这样的说法, “这次大选中, 某位候选人支持率为 $65\%$ 到 $75\%$ ，置信水平为 $95\%$ ”，或者“某人身高是 $180~\mathrm{cm}$ ，以 $90\%$ 可能性上下浮动 $1\mathrm{cm}$ ”，这都是常见的区间估计的例子。区间估计是除点估计外参数估计的另外一种方法，那么为什么使用区间估计？如何理解其含义？怎么构造区间估计？事实上，区间估计与假设检验有自然的联系，我们在这一节中就对区间估计的这些相关问题进行介绍。

区间估计最早由统计学家 Neyman 提出, 顾名思义区间估计给出的是参数的一个区间范围, 并且基于样本统计量的分布能够给出参数落入此范围的概率. 下面我们就将具体介绍区间估计、置信区间的基本概念和一些构造方法, 并用单样本和两样本正态总体作为例子来进行解释说明.

## 3.5.1 基本概念

我们先给出区间估计的定义:

定义 3.5.1 设总体参数为  $\theta, \boldsymbol{X} = (X_{1}, X_{2}, \cdots, X_{n})$  是来自总体的一组样本, 如果  $\hat{\theta}_{L}(\boldsymbol{X})$  和  $\hat{\theta}_{U}(\boldsymbol{X})$  是两个统计量, 且对于样本空间内任意一点 x, 满足  $\hat{\theta}_{L}(\boldsymbol{x}) \leqslant \hat{\theta}_{U}(\boldsymbol{x})$ , 则称随机区间  $[\hat{\theta}_{L}(\boldsymbol{X}), \hat{\theta}_{U}(\boldsymbol{X})]$  是  $\theta$  的一个区间估计.

注意, 这里的定义中我们使用的是闭区间, 但实际应用中取决于我们感兴趣的问题, 有时候开区间、半开半闭区间, 甚至单侧区间 (即 $\hat{\theta}_L(X), \hat{\theta}_U(X)$ 之一为 $\infty$) 是更合适的选择. 我们再考虑上文提到的正态总体 $N(\mu,1)$, 均值 $\mu$ 的一个区间估计是 $[\bar{X} - 1, \bar{X} + 1]$. 假设样本量为 3, 则这个区间能覆盖 $\mu$ 的概率是

$$
\begin{array}{l} P (\bar {X} - 1 \leqslant \mu \leqslant \bar {X} + 1) = P \left(- \sqrt {3} \leqslant \frac {\bar {X} - \mu}{\sqrt {1 / 3}} \leqslant \sqrt {3}\right) \\ \approx 0. 9 1 6 7. \qquad \left(\text {注意到} \frac {\bar {X} - \mu}{\sqrt {1 / 3}} \sim N (0, 1).\right) \\ \end{array}
$$

我们从这个例子中看到, 区间估计放弃了点估计的部分精确性, 却使得我们论断正确的概率明显提高. 上述计算的覆盖概率 (coverage probability) 是对区间估计优劣的一个衡量标准. 在这里我们再次强调, 区间估计量是随机区间, 而参数是确定的值, 对覆盖概率的一个频率解释是: 大量重复抽取样本, 每组样本得到的区间要么覆盖参数真值, 要么不覆盖, 此时谈覆盖概率没有意义, 但平均而言, 覆盖真值的区间所占比例差不多就是覆盖概率. 一种常见的错误说法是 “参数以某一概率落入区间”, 这就混淆了区间估计和参数的随机性与确定性.

通常而言, 覆盖概率与参数特定取值有关, 我们更希望的是对参数空间中的任意一个取值, 都有较高的覆盖概率, 换言之, 最低的覆盖概率仍在较高的水平上, 我们将其严格化为下面的置信系数 (confidence coefficient) 的定义.

定义3.5.2 设总体参数空间为 $\Theta$ ，区间估计量 $[\hat{\theta}_L(X),\hat{\theta}_U(X)]$ 的置信系数为

$$
\inf _ {\theta \in \Theta} P \left(\hat {\theta} _ {L} (\boldsymbol {X}) \leqslant \theta \leqslant \hat {\theta} _ {U} (\boldsymbol {X})\right).
$$

可以看到, 如果覆盖概率不依赖于参数取值, 那么置信系数就是覆盖概率.

对于一个区间估计量, 加上其置信系数, 我们就得到了一个置信区间 (confidence interval).

定义3.5.3 对于区间估计量 $[\hat{\theta}_L(\pmb {X}),\hat{\theta}_U(\pmb {X})]$ 和固定的 $\alpha \in (0,1)$，如果

$$
\inf _ {\theta \in \Theta} P \left(\hat {\theta} _ {L} (\boldsymbol {X}) \leqslant \theta \leqslant \hat {\theta} _ {U} (\boldsymbol {X})\right) \geqslant 1 - \alpha,
$$

则称 $[\hat{\theta}_L(\boldsymbol {X}),\hat{\theta}_U(\boldsymbol {X})]$ 是置信水平为 $1 - \alpha$ 的置信区间， $\hat{\theta}_L(\boldsymbol {X}),\hat{\theta}_U(\boldsymbol {X})$ 称为置信下限和置信上限.如果是单侧置信区间，相应地称为单侧置信限.

实际应用中, 上述定义中的 “ $\geqslant$ ” 一般是直接取 “=”, 得到的区间称为同等置信区间, 简便起见, 我们简称为置信区间. 同时对于区间估计, 我们关注的基本都是置信区间, 因此在不引起歧义的情况下, 我们也将两个术语交替使用. 下面, 我们介绍置信区间的构造方法.

## 3.5.2 构造方法

构造置信区间的方法有很多, 一般来说是先得到参数的一个点估计量, 再通过这个估计量的分布确定置信限, 进而获得相应的置信区间. 我们先来看一个例子:

例 3.5.1 考虑一般的正态总体  $N(\mu,\sigma^{2})$ ，其中方差  $\sigma^{2}$  已知， $X_{1},X_{2},\cdots,X_{n}$  是一组来自该总体的独立同分布样本， $\bar{X}$  是  $\mu$  的一个点估计，且服从分布  $N(\mu,\sigma^{2}/n)$ ，也就是  $\frac{\sqrt{n}(\bar{X}-\mu)}{\sigma}\sim N(0,1)$ ，从而我们有

$$
P \left(- u _ {\alpha / 2} \leqslant \frac {\sqrt {n} (\bar {X} - \mu)}{\sigma} \leqslant u _ {\alpha / 2}\right) = 1 - \alpha ,
$$

其中， $u_{\alpha}$  表示标准正态分布的上  $\alpha$  分位数。进一步，

$$
P \left(\bar {X} - u _ {\alpha / 2} \frac {\sigma}{\sqrt {n}} \leqslant \mu \leqslant \bar {X} + u _ {\alpha / 2} \frac {\sigma}{\sqrt {n}}\right) = 1 - \alpha ,
$$

从而, 均值  $\mu$  的一个置信水平为  $1 - \alpha$  的置信区间为  $\left[\bar{X} - u_{\alpha/2}\frac{\sigma}{\sqrt{n}}, \bar{X} + u_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right]$ .

这个例子中，$\frac{\sqrt{n}(\bar{X} - \mu)}{\sigma}$ 是一个特殊的随机变量，称为枢轴量 (pivotal quantity)，它是样本和参数的函数，但是分布与参数无关，如果枢轴量与参数的关系相对简单，那么基于枢轴量可以相对容易地求得置信区间。枢轴量法是最常见的置信区间的构造方法，我们将枢轴量法构造 $1 - \alpha$ 置信水平的置信区间的步骤简要总结如下:

(1) 构造枢轴量  $G(X_{1}, X_{2}, \cdots, X_{n}; \theta)$ ，使其分布已知且与  $\theta$  无关；
(2) 确定常数 $G_{L}, G_{U}$ 满足 $P(G_{L} \leqslant G \leqslant G_{U}) = 1 - \alpha$;
(3) 将 $G_{L} \leqslant G \leqslant G_{U}$ 变为 $\hat{\theta}_{L} \leqslant \theta \leqslant \hat{\theta}_{U}$, 得到区间 $[\hat{\theta}_{L}, \hat{\theta}_{U}]$ 即可.

我们再用一个例子说明枢轴量法.

例 3.5.2 考虑均匀分布  $U(0,\theta)$ ,  $X_{1}, X_{2}, \cdots, X_{n}$  是一组来自该总体的独立同分布样本, 则  $\frac{X_{(n)}}{\theta}$  具有分布函数

$$
F (x) = x ^ {n}, 0 \leqslant x \leqslant 1,
$$

与 $\theta$ 无关, 所以 $\frac{X_{(n)}}{\theta}$ 是一个枢轴量, 对于给定的置信水平 $1 - \alpha$, 我们选择 $a, b$ 使得下面的式子成立:

$$
P \left(a \leqslant \frac {X _ {(n)}}{\theta} \leqslant b\right) = b ^ {n} - a ^ {n} = 1 - \alpha ,
$$

所得置信区间为 $\left[\frac{X_{(n)}}{b},\frac{X_{(n)}}{a}\right]$

对于一般的总体, 有没有相对比较通用的构造枢轴量的方法呢? 下面我们就介绍一种枢轴量化累积分布函数的方法, 我们以定理的形式给出这一方法.

定理3.5.1 设统计量 $T$ 的累积分布函数为 $F_{T}(t;\theta) = P(T\leqslant t;\theta)$，且对于每个$t,F_T(t;\theta)$ 关于 $\theta$ 单调递减.设 $\alpha = \alpha_{1} + \alpha_{2}\in (0,1)$，假设对于 $\theta_L(t),\theta_U(t)$，可以由如下方程定义:

$$
P (T \geqslant t; \theta_ {L} (t)) = \alpha_ {2}, \quad P (T \leqslant t; \theta_ {U} (t)) = \alpha_ {1},
$$

则随机区间 $[\theta_L(T),\theta_U(T)]$ 是 $\theta$ 的置信水平为 $1 - \alpha$ 的置信区间.若 $F_{T}(t;\theta)$ 递增，只要交换方程中 $\theta_L(T),\theta_U(T)$ 的位置即可.

我们用下面的例子说明这一方法的应用.

例 3.5.3 考虑  $X_{1}, X_{2}, \cdots, X_{n}$  是从两点分布  $B(1, p)$  总体中独立抽取的样本，则统计量  $Y_{n} = \sum_{i=1}^{n} X_{i}$  是 pn 的无偏估计，服从二项分布  $B(n, p)$ 。设  $Y_{n}$  的观测值为 y，则 p 的置信水平为  $1 - \alpha$  的置信区间  $[p_{L}, p_{U}]$  可通过以下方程确定:

$$
\sum_ {k = 0} ^ {y} \binom {n} {k} p _ {U} ^ {k} (1 - p _ {U}) ^ {n - k} = \frac {\alpha}{2}, \qquad \sum_ {k = y} ^ {n} \binom {n} {k} p _ {L} ^ {k} (1 - p _ {L}) ^ {n - k} = \frac {\alpha}{2}.
$$

方程的解可以通过查二项分布表或软件计算得到.

事实上, 除了枢轴量法以外, 由于置信区间和假设检验的密切联系, 另一种构造置信区间的方法是通过反转检验统计量, 给定一个检验, 自然地就有相对应的置信区间, 我们将在下一章中讨论. 接下来, 我们仍继续关注枢轴量法, 将其应用到单样本、两样本正态总体参数的置信区间构造中.

## 3.5.3 正态总体参数的置信区间

正态分布  $N(\mu,\sigma^{2})$  是最常见的分布, 我们在这一小节用几个例子展示如何用枢轴量法构造两个参数的置信区间:

例 3.5.4 考虑正态分布  $N(\mu, \sigma^{2})$ ，假设方差  $\sigma^{2}$  未知， $X_{1}, X_{2}, \cdots, X_{n}$  是一组来自该总体的独立同分布样本。由于方差未知，一个自然的想法是用方差的无偏估计  $S^{2} = \frac{1}{n-1} \sum_{i=1}^{n} (X_{i} - \bar{X})^{2}$  去代替总体方差。同时我们知道  $\frac{\sqrt{n}(\bar{X} - \mu)}{S} \sim t(n-1)$  是一个枢轴量，记  $t_{\alpha}(n-1)$  为  $t(n-1)$  的上  $\alpha$  分位数，类似例 3.5.1，均值  $\mu$  的置信水平为  $1 - \alpha$  的置信区间为

$$
\left[ \bar {X} - t _ {\alpha / 2} (n - 1) \frac {S}{\sqrt {n}}, \bar {X} + t _ {\alpha / 2} (n - 1) \frac {S}{\sqrt {n}} \right].
$$

如果要构造 $\sigma^2$ 的置信区间, 则只需注意到 $\frac{(n - 1)S^2}{\sigma^2} \sim \chi^2 (n - 1)$ 是枢轴量, 篇幅所限, 我们略去细节, 读者可自行推导.

下面我们把讨论拓展到两样本正态总体:

例 3.5.5 考虑正态分布  $N(\mu_{1},\sigma_{1}^{2}), N(\mu_{2},\sigma_{2}^{2}), X_{1}, X_{2}, \cdots, X_{n}$  和  $Y_{1}, Y_{2}, \cdots, Y_{m}$  分别是来自两个总体的独立同分布样本，假设方差  $\sigma_{1}^{2}, \sigma_{2}^{2}$  均已知，则

$$
\frac {(\bar {X} - \bar {Y}) - (\mu_ {1} - \mu_ {2})}{\sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}}} \sim N (0, 1),
$$

所以它是一个枢轴量, $\mu_{1}-\mu_{2}$ 的置信水平为 $1-\alpha$ 的置信区间为

$$
\left[ \bar {X} - \bar {Y} - u _ {\alpha / 2} \sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}}, \bar {X} - \bar {Y} + u _ {\alpha / 2} \sqrt {\frac {\sigma_ {1} ^ {2}}{n} + \frac {\sigma_ {2} ^ {2}}{m}} \right].
$$

例 3.5.6 在例 3.5.5 中, 假设  $\sigma_{1}^{2} = \sigma_{2}^{2} = \sigma^{2}$ , 但  $\sigma^{2}$  未知, 类似地, 可以得到  $\mu_{1} - \mu_{2}$  的置信水平为  $1 - \alpha$  的置信区间为

$$
\left[ \bar {X} - \bar {Y} - t _ {\alpha / 2} (n + m - 2) \sqrt {\frac {1}{n} + \frac {1}{m}} S, \bar {X} - \bar {Y} + t _ {\alpha / 2} (n + m - 2) \sqrt {\frac {1}{n} + \frac {1}{m}} S \right].
$$

例 3.5.7 在例 3.5.5 中, 考虑构造  $\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}$  的置信区间. 我们知道  $\frac{S_{1}^{2}/\sigma_{1}^{2}}{S_{2}^{2}/\sigma_{2}^{2}} \sim F(n-1, m-1)$  是枢轴量, 经过简单代数变换可以得到置信水平为  $1-\alpha$  的置信区间为

$$
\left[ \frac {S _ {1} ^ {2}}{S _ {2} ^ {2} F _ {1 - \alpha / 2} (n - 1 , m - 1)}, \frac {S _ {1} ^ {2}}{S _ {2} ^ {2} F _ {\alpha / 2} (n - 1 , m - 1)} \right].
$$

## 3.5.4 大样本置信区间

前面的例子中, 我们都可以推导出枢轴量的精确分布, 但在有些情况下, 这一点并不容易做到. 比如著名的 Behrens-Fisher 问题, 即例 3.5.5 中假设方差及方差的关系均未知, 我们仍希望构造 $\mu_{1} - \mu_{2}$ 的置信区间, 这时候我们就可以借助统计量的大样本性质, 根据渐近分布构造置信区间. 我们知道, 根据中心极限定理,

$$
\frac {(\bar {X} - \bar {Y}) - (\mu_ {1} - \mu_ {2})}{\sqrt {\frac {S _ {1} ^ {2}}{n} + \frac {S _ {2} ^ {2}}{m}}} \xrightarrow {\mathrm{d}} N (0, 1).
$$

所以 $\mu_1 - \mu_2$ 的近似置信区间就是

$$
\left[ \bar {X} - \bar {Y} - u _ {\alpha / 2} \sqrt {\frac {S _ {1} ^ {2}}{n} + \frac {S _ {2} ^ {2}}{m}}, \bar {X} - \bar {Y} + u _ {\alpha / 2} \sqrt {\frac {S _ {1} ^ {2}}{n} + \frac {S _ {2} ^ {2}}{m}} \right].
$$

我们再举一个例子. 在例 3.5.3 中, 即便我们给出了相应的方程, 获得精确解也很困难, 甚至精确解并不存在. 但我们注意到当 n 足够大时, 仍根据中心极限定理, 有

$$
\frac {Y _ {n} - n p}{\sqrt {n p (1 - p)}} \xrightarrow {\mathrm{d}} N (0, 1).
$$

也就是说，

$$
P \left(- u _ {\alpha / 2} \leqslant \frac {Y _ {n} - n p}{\sqrt {n p (1 - p)}} \leqslant u _ {\alpha / 2}\right)\rightarrow P \left(- u _ {\alpha / 2} \leqslant N (0, 1) \leqslant u _ {\alpha / 2}\right) = 1 - \alpha .
$$

括号中不等式等价于 $n(Y_{n} / n - p)^{2}\leqslant p(1 - p)u_{\alpha /2}^{2}$ ，不难证明对应的二次函数有两个不等实根，记为 $\hat{p}_L,\hat{p}_U$ ，则所求置信区间为 $[\hat{p}_L,\hat{p}_U]$ .篇幅所限，我们略去具体表达式.类似地，读者可以考虑Poisson分布总体 $P(\lambda)$ 参数 $\lambda$ 的置信区间的构造.

这一节中我们讨论了置信区间的基本概念、构造方法和大样本置信区间的有关内容，除此之外，关于置信区间的优劣性评判准则以及和假设检验的关系，感兴趣的读者可以参考相关文献，例如 Berger et al.(2001)，王兆军等 (2023).

## 3.5.5 反转检验方法

假设检验与置信区间有着自然的联系, 文献中也称之为二者的对偶性 (duality), 即一个检验的接受域可以被反转给出置信区间或者更一般的置信区域 (多参数情形下).

回顾 3.4 节中的假设检验问题, 若  $\boldsymbol{X} = (X_{1}, X_{2}, \cdots, X_{n})$ , 假设  $A(\boldsymbol{\theta}_{0})$  是  $H_{0}: \boldsymbol{\theta} = \boldsymbol{\theta}_{0}$  的水平为  $\alpha$  的接受域, 定义

$$
C (\boldsymbol {X}) = \{\boldsymbol {\theta}: \boldsymbol {X} \in A (\boldsymbol {\theta}) \}.
$$

注意到 $1 - P_{\theta}(\pmb{\theta}\in C(\pmb {X}))$ 就是当 $\pmb{\theta}$ 为真时我们拒绝它的概率，因此其等于 $\alpha$ ，所以

$$
P _ {\boldsymbol {\theta}} (\boldsymbol {\theta} \in C (\boldsymbol {X})) = 1 - \alpha .
$$

相应地, $C(\boldsymbol{X})$ 就是参数 $\theta$ 的置信水平为 $1 - \alpha$ 的置信区域 (confidence region), 有时也称为置信集合 (confidence set). 当这一区域为一个区间时, 则退化为我们前面所讨论的置信区间问题.

当然, 上述结论反之亦然: 如果 $C(\mathbf{X})$ 是置信水平为 $1 - \alpha$ 的置信区域, 则检验 $I(\boldsymbol{\theta}_0 \notin C(\mathbf{X}))$ 就是水平为 $\alpha$ 的假设检验.

以似然比检验为例, $\Theta_0 = \{\pmb{\theta} : \pmb{\theta} = \pmb{\theta}_0\}$ 对应的似然比检验的接受域为

$$
A \left(\boldsymbol {\theta} _ {0}\right) = \left\{\boldsymbol {X}: f \left(\boldsymbol {X}; \boldsymbol {\theta} _ {0}\right) \geqslant \exp \{- \chi_ {k, \alpha} ^ {2} / 2 \} f (\boldsymbol {X}; \widehat {\boldsymbol {\theta}} _ {n}) \right\},
$$

则

$$
C (\boldsymbol {X}) = \{\boldsymbol {\theta}: f (\boldsymbol {X}; \boldsymbol {\theta}) \geqslant \exp \{- \chi_ {k, \alpha} ^ {2} / 2 \} f (\boldsymbol {X}; \widehat {\boldsymbol {\theta}} _ {n}) \}
$$

就是一个置信水平为 $1 - \alpha$ 的渐近置信区域. 事实上, 在3.4节中介绍的Wald检验和Rao得分检验也都可以被用来类似构造置信区域.

可以看到这种获得置信集合的方法仅需要我们构造适当的假设检验即可, 因此从这一角度来说, 该方法为置信区间或者置信区域的求取提供了系统化的解决方案: 只要能够构造有效的假设检验, 我们就能得到相应的置信集合. 特别地, 这样构造出来的置信集合通常与我们的枢轴量法等其他方法构造出来的置信集合等价或者渐近等价, 因此在现代的复杂问题中, 该方法最为标准常用. 我们会在第四章中进一步看到如何使用这种方法求取多元问题下的置信区域.

## 习题三

1. 假设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自均值为  $\theta$ 、方差为  $\sigma^{2} > 0$  的独立同分布样本。请证明对于假设检验问题  $H_{0}: \theta = 0 \leftrightarrow H_{1}: \theta > 0$ ，基于 t 统计量的假设检验是相合检验。
2. 假设例 3.2.1 中的方差是未知的, 试检验包装机是否工作正常.
3. 假设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自两点分布  $B(1, p)$  的独立同分布样本，则对于假设检验问题  $H_{0}: p = p_{0} \leftrightarrow H_{1}: p \neq p_{0}$ ，考虑似然比检验统计量、Wald 检验统计量、得分检验统计量与其对应的拒绝域，并给出其对应的参数 p 的反转检验方法的置信区间.

4. 在正常情况下, 如乘坐某品牌出租车从南开大学东门到天津火车站需要 23 元左右. 为检验该品牌出租车运营是否规范, 现随机地乘坐其中 15 辆出租车从东门到火车站 (假设路况正常), 其平均花费为 25.4, 标准差为 2.3, 请在水平 0.05 下, 检验该品牌出租车运营是否规范.
5. 为研究硅肺病患者肺功能的变化情况, 某医院对第 I, II 期硅肺病患者各 33 名测定其肺活量, 得到二者的平均值分别为 $2710 \mathrm{ml}$ 和 $2830 \mathrm{ml}$, 其标准差分别为 $147 \mathrm{ml}$ 和 $118 \mathrm{ml}$. 请问: 在水平 0.05 下, 第 I, II 期硅肺病患者的肺活量有无显著差异?
6. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自均匀分布  $U(0, \theta)$  的独立同分布样本, 其中参数  $\theta > 0$ . 如对于假设

$$
H _ {0}: \theta \geqslant 2 \leftrightarrow H _ {1}: \theta <   2,
$$

取检验统计量为最大次序统计量  $X_{(n)}$ ，且拒绝域为  $W = \{\bar{X} : X_{(n)} \leqslant 1.5\}$ ，求此检验犯第一类错误概率的最大值.

7. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自两点分布  $B(1, p)$  的独立同分布样本.

(1) 试求假设 $H_0: p \leqslant 0.01 \leftrightarrow H_1: p > 0.01$ 的水平为 0.05 的显著性检验;
(2) 如要求这个检验在 $p = 0.08$ 时的第二类错误概率不超过 0.1, 样本容量 $n$ 应为多少?

8. 下列哪些假设是简单的, 哪些是复合的?

(1) X 服从正态分布;
(2) X 服从正态分布  $N(4,3^{2})$ ;
(3)  $E(X)=2,\mathrm{Var}(X)=0.5^{2};$
(4) X 不服从正态分布;
(5) X 服从参数为 0.5 的两点分布;
(6) X 服从参数为 0.5 的二项分布;
(7) X 服从指数分布  $Exp(3)$ .

9. 设 $X$ 是来自均匀分布 $U(\theta - 0.5, \theta + 0.5)$ 的一个样本, 对于假设

$$
H _ {0}: \theta \leqslant 3 \leftrightarrow H _ {1}: \theta \geqslant 4,
$$

构造一个检验法, 使其功效函数  $\beta(\theta)$  满足

$$
\beta (\theta) = 0, \text {当} \theta \leqslant 3 \text {时}; \beta (\theta) = 1, \text {当} \theta \geqslant 4 \text {时}.
$$

10. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自指数分布  $Exp(\lambda_{1})$  的独立同分布样本,  $Y_{1}, Y_{2}, \cdots, Y_{m}$  为来自指数分布  $Exp(\lambda_{2})$  的独立同分布样本, 且两组样本独立, 其中  $\lambda_{1}, \lambda_{2}$  是未知的正参数:

(1) 求假设 $H_0: \lambda_1 = \lambda_2 \leftrightarrow H_1: \lambda_1 \neq \lambda_2$ 的似然比检验;

(2) 证明上述检验法的拒绝域仅依赖于比值 $\sum_{i=1}^{n} X_i / \sum_{i=1}^{m} Y_i$;
(3) 求统计量  $\sum_{i=1}^{n} X_{i} / \sum_{i=1}^{m} Y_{i}$  的零分布.

11. 用甲、乙两种材料的灯丝制造灯泡, 现随机地从中抽取若干个进行寿命试验, 得到如下数据 (单位: h):

甲材料:1 610, 1 650, 1 680, 1 710, 1 720, 1 800;

乙材料: 1 580, 1 600, 1 640, 1 630, 1 700.

假设寿命服从指数分布, 在水平 0.05 下检验这两种材料生产的灯泡寿命有无显著性差异.

12. 设  $X_{1}, X_{2}, \cdots, X_{m}$  和  $Y_{1}, Y_{2}, \cdots, Y_{n}$  是分别来自正态总体  $N(\mu_{1}, \sigma^{2})$  和  $N(\mu_{2}, \sigma^{2})$  的独立同分布样本，且全样本独立，其中  $\mu_{1}, \mu_{2}, \sigma^{2}$  均未知。请仿照两样本 t 检验，构造假设  $H_{0}: \mu_{1} = c\mu_{2}$  的水平  $\alpha$  的显著性检验，其中  $c \neq 0$  为常数。
13. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自均匀分布  $U(0, \theta)$  的独立同分布样本, 其中  $\theta > 0$  为参数. 对于给定的  $\theta_{0} > 0$ , 请给出假设  $H_{0}: \theta \leqslant \theta_{0}$  的水平  $\alpha$  的显著性检验.
14. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自正态总体  $N(\mu, \sigma^{2})$  的独立同分布样本, 其中  $\mu, \sigma^{2}$  为未知参数. 试证明关于假设

$$
H _ {0}: \sigma^ {2} = \sigma_ {0} ^ {2} \leftrightarrow H _ {1}: \sigma^ {2} \neq \sigma_ {0} ^ {2}
$$

的似然比检验就是检验统计量为  $\chi^{2}=(n-1)S_{n}^{2}/\sigma_{0}^{2}$  的  $\chi^{2}$  检验, 其中  $S_{n}^{2}$  为样本方差.

15. 在对一种新的流感疫苗进行人体试验时, 为试验组的 900 位志愿者注射了新疫苗, 在 6 个月内他们中有 9 个人得了流感. 为对照组的 900 位志愿者注射了老疫苗, 在 6 个月内他们中有 19 个人得了流感. 请问新疫苗是否更有效?
16. 在 A 村随机调查了 90 位男村民, 其中有 45 人对现任村委会主任表示满意, 又随机调查了 100 位女村民, 有 69 人对现任村委会主任表示满意. 在显著性水平 0.05 下,

(1) 能否认为男、女村民的态度有明显的差异？
(2) 求村中满意村委会主任的男、女村民的比例  $p_{1}$  和  $p_{2}$  的置信水平为 95% 的置信区间.
(3) 由 (2) 的区间估计能否认为 $p_1 > p_2$?

17. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自概率密度函数为

$$
f (x; \theta) = 2 \frac {x}{\theta^ {2}} \exp \left\{- \frac {x ^ {2}}{\theta^ {2}} \right\}, x > 0
$$

的 Rayleigh (瑞利) 分布的独立同分布样本, 其中  $\theta > 0$  为未知参数.

(1) 利用此总体的充分完备统计量, 建立一个关于假设

$$
H _ {0}: \theta = 1 \leftrightarrow H _ {1}: \theta > 1
$$

的水平近似为  $\alpha$  的检验;

(2) 验证此检验统计量在  $H_{1}$  下比在  $H_{0}$  下具有更大的均值.

18. 设 $X_{1}, X_{2}$ 相互独立, 且 $X_{1} \sim N(\mu_{1}, \sigma^{2}), X_{2} \sim N(\mu_{2}, \sigma^{2})$. 当 $\sigma^{2}$ 已知时, 求关于假设

$$
H _ {0}: \mu_ {1} = \mu_ {2} = 0 \leftrightarrow H _ {1}: \mu_ {1} ^ {2} + \mu_ {2} ^ {2} > 0
$$

的水平为  $\alpha$  的检验.

19. 设 X, Y 相互独立, 且  $X \sim N(\mu_{1}, 1)$ ,  $Y \sim N(\mu_{2}, 1)$ . 设  $\rho = \mu_{1} / \mu_{2}$ ,  $\theta = (\rho, \mu_{2})$ . 证明

$$
T (X, Y; \rho_ {0}) = {\left\{ \begin{array}{l l} {1,} & {| X - \rho_ {0} Y | > \sqrt {1 + \rho_ {0} ^ {2}} u _ {\alpha / 2},} \\ {0,} & {{\text {否则}}} \end{array} \right.}
$$

是假设  $H_{0}:\rho=\rho_{0}$  的水平为  $\alpha$  的检验, 其中  $u_{\alpha/2}$  为标准正态分布的上  $\alpha/2$  分位数.

20. 设 X 服从二项分布  $B(n,p)$ ，证明关于假设  $H_{0}: p = 1/2 \leftrightarrow H_{1}: p \neq 1/2$  的似然比检验统计量等价于  $|2X - n|$ .
21. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自正态总体  $N(\mu, \sigma^{2})$  的独立同分布样本, 其中  $\mu, \sigma^{2}$  未知. 证明关于假设  $H_{0}: \mu \leqslant \mu_{0} \leftrightarrow H_{1}: \mu > \mu_{0}$  的单边 t 检验是似然比检验 (显著性水平  $\alpha < 1/2$ ).
22. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自正态总体  $N(\mu, \sigma^{2})$  的独立同分布样本, 其中  $\mu, \sigma^{2}$  未知. 证明关于假设  $H_{0}: \sigma^{2} = \sigma_{0}^{2} \leftrightarrow H_{1}: \sigma^{2} \neq \sigma_{0}^{2}$  的水平为  $\alpha$  的似然比检验的拒绝域的补集为

$$
\mathcal {W} ^ {c} = \left\{c _ {1} \leqslant \frac {1}{\sigma_ {0} ^ {2}} \sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) ^ {2} \leqslant c _ {2} \right\},
$$

其中  $c_{1}, c_{2}$  满足

$$
\int_ {c _ {1}} ^ {c _ {2}} \chi^ {2} (x; n - 1) \mathrm{d} x = 1 - \alpha , c _ {1} - c _ {2} = n \ln (c _ {1} / c _ {2}).
$$

23. 设  $X_{1}, X_{2}, \cdots, X_{m}$  和  $Y_{1}, Y_{2}, \cdots, Y_{n}$  为分别来自正态总体  $N(\mu_{1}, \sigma^{2})$  和  $N(\mu_{2}, \sigma^{2})$  的独立同分布样本，其中  $\mu_{1}, \mu_{2}, \sigma^{2}$  未知。证明关于假设  $H_{0}: \mu_{1} \leqslant \mu_{2} \leftrightarrow H_{1}: \mu_{1} > \mu_{2}$  的似然比检验统计量等价于两样本 t 检验量  $|T|$  (统计量 T 的定义见 (3.2.13) 式).
24. 称正态分布随机变量序列  $X_{1}, X_{2}, \cdots, X_{n}$  为一个自回归 (autoregressive) 序列，是指  $X_{i} = \theta X_{i-1} + \varepsilon_{i}, i = 1, 2, \cdots, n,$  其中  $X_{0} = 0, \varepsilon_{1}, \varepsilon_{2}, \cdots, \varepsilon_{n}$  是来自

$N(0,\sigma^{2})$  的独立同分布序列. 证明关于假设  $H_{0}:\theta=0\leftrightarrow H_{1}:\theta\neq0$  的似然比检验统计量等价于  $-\left(\sum_{i=2}^{n}X_{i}X_{i-1}\right)^{2}\bigg/\sum_{i=1}^{n-1}X_{i}^{2}$ .

25. 投 1 000 次硬币, 560 次正面向上, 440 次反面向上, 假设硬币质地均匀是否合理? 证明你的结果.
26. 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $\{1, 2, \cdots, \theta\}$  上的离散均匀分布的独立同分布样本，这里  $\theta$  为整数且  $\theta \geqslant 2$ ，求水平为  $\alpha$  的以下假设的似然比检验:

(1) $H_0: \theta \leqslant \theta_0 \leftrightarrow H_1: \theta > \theta_0$, 其中 $\theta_0$ 为不小于 2 的已知整数;
(2) $H_0: \theta = \theta_0 \leftrightarrow H_1: \theta \neq \theta_0$.

27. 假设  $X_{i1}, X_{i2}, \cdots, X_{in_{i}}, i = 1, 2$  为两个独立的独立同分布样本，分布服从均匀分布  $U(0, \theta_{i}), i = 1, 2$ ，这里  $\theta_{1} > 0, \theta_{2} > 0$  均未知.

(1) 求水平为  $\alpha$  的假设  $H_{0}:\theta_{1}=\theta_{2}\leftrightarrow H_{1}:\theta_{1}\neq\theta_{2}$  的似然比检验;
(2) 求  $-2\ln(\lambda)$  的极限分布, 这里  $\lambda$  为 (1) 中的似然比.

28. 假设  $(X_{11}, X_{12}), (X_{21}, X_{22}), \cdots, (X_{n1}, X_{n2})$  为来自二元正态分布的独立同分布样本, 均值和方差矩阵均未知. 假设  $H_{0}: \rho = 0 \leftrightarrow H_{1}: \rho \neq 0$ , 这里  $\rho$  为相关系数. 证明:  $|W| > c$  为一个似然比检验, 其中

$$
W = \sum_ {i = 1} ^ {n} (X _ {i 1} - \bar {X} _ {1}) (X _ {i 2} - \bar {X} _ {2}) / \left[ \sum_ {i = 1} ^ {n} (X _ {i 1} - \bar {X} _ {1}) ^ {2} + \sum_ {i = 1} ^ {n} (X _ {i 2} - \bar {X} _ {2}) ^ {2} \right],
$$

并求 W 的分布.

29. (p 值) 假设 X 的分布为  $P_{\theta}$ ，其中  $\theta \in R$  为未知参数，对于拒绝域为  $W_{\alpha}$  的原假设  $H_{0}: \theta = \theta_{0}$  （或  $\theta < \theta_{0}$ ）满足  $P_{\theta_{0}}(X \in \mathcal{W}_{\alpha}) = \alpha, 0 < \alpha < 1$  和  $W_{\alpha_{1}} = \bigcap_{\alpha > \alpha_{1}} W_{\alpha}, 0 < \alpha_{1} < 1$ ，考虑  $H_{0}$  的一族非随机化水平检验:

(1) 证明 p 值为  $\hat{\alpha}(x)=\inf\{\alpha:x\in\mathcal{W}_{\alpha}\}$ ;
(2) 证明当  $\theta = \theta_{0}$  时,  $\hat{\alpha}(x)$  服从均匀分布  $U(0,1)$ ;
(3) 如果拒绝域为  $W_{\alpha}$  的检验是无偏的, 证明在  $H_{1}$  下,  $P_{\theta}(\hat{\alpha}(x) \leqslant \alpha) \geqslant \alpha$ .

30. 假设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自正态总体  $N(\theta, \sigma^{2})$  的一组随机样本,  $\sigma^{2}$  已知. 假设  $H_{0}: \theta = \theta_{0} \leftrightarrow H_{1}: \theta \neq \theta_{0}$  的一个似然比检验满足: 若  $|\bar{X} - \theta_{0}| / (\sigma / \sqrt{n}) > w$ , 则拒绝  $H_{0}$ .

(1) 求这个检验的功效函数, 用标准正态的概率写出这个表达式;
(2) 试验者希望在 $\theta = \theta_0 + \sigma$ 点犯第一类错误的概率是 0.05, 犯第二类错误的最大概率是 0.25. 求为达到这些要求的 $n$ 和 $w$ 的值.

31. 设 $f(x \mid \theta)$ 为具有如下形式的参数分布族:

$$
f (x \mid \theta) = \frac {\exp \{x - \theta \}}{\left(1 + \exp \{x - \theta \}\right) ^ {2}}, \quad - \infty <   x <   \infty , \quad - \infty <   \theta <   \infty .
$$

(1) 证明这个族是单调似然比分布族.

(2) 假设 X 是一个观测值, 找出  $H_{0}: \theta = 0 \leftrightarrow H_{1}: \theta = 1$  的水平为  $\alpha$  的 UMP. 对于  $\alpha = 0.2$ , 计算第二类错误的大小.
(3) 证明 (2) 中的检验是对于检验 $H_0: \theta \leqslant 0 \leftrightarrow H_1: \theta > 0$ 的水平为 $\alpha$ 的 UMP 检验.

32. 设 X 为来自 Cauchy 分布  $C(\theta)$  的一个观测值.

(1) 证明这个族不是单调似然比分布族;

(2) 证明检验

$$
\psi (x) = \left\{ \begin{array}{l l} 1, & 1 <   x <   3, \\ 0, & \text {其他} \end{array} \right.
$$

对于检验  $H_{0}:\theta=0\leftrightarrow H_{1}:\theta=1$  是 UMP 的, 并计算第一类和第二类错误的概率;

(3) (2) 中的检验对于检验 $H_0: \theta \leqslant 0 \leftrightarrow H_1: \theta > 0$ 是 UMP 的吗？

33. 设  $X_{1}, X_{2}$  独立同分布于均匀分布  $U(\theta, \theta+1)$ . 对于检验  $H_{0}: \theta = 0 \leftrightarrow H_{1}: \theta > 0$ , 我们有两个需要比较的检验:

$\psi_{1}(X_{1})$ :如果 $X_{1}>0.95$ ，则拒绝 $H_{0}$ ;

$\psi_{2}(X_{1},X_{2})$ :如果 $X_{1}+X_{2}>C$ ，则拒绝 $H_{0}$ .

(1) 找出 C 的值, 使得  $\psi_{2}$  与  $\psi_{1}$  具有相同的显著性水平;
(2) 计算每个检验的功效函数;
(3)  $\psi_{2}$  是一个比  $\psi_{1}$  更有力的检验吗?
(4) 举出一个与  $\psi_{2}$  具有相同水平但功效更高的检验.

34. 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自  $N(\theta, \sigma^{2})$  总体的独立同分布样本, 考虑检验

$$
H _ {0}: \theta_ {1} \leqslant \theta \leqslant \theta_ {2} \leftrightarrow H _ {1}: \theta <   \theta_ {1} \text {或} \theta > \theta_ {2}.
$$

(1) 如果某检验的拒绝域为

$$
C (\bar {X}) = \{\bar {X}: \bar {X} > \theta_ {2} + t _ {\alpha / 2} (n - 1) \sqrt {S ^ {2} / n} \text {或} \bar {X} <   \theta_ {1} - t _ {\alpha / 2} (n - 1) \sqrt {S ^ {2} / n} \},
$$

证明该检验不是一个水平为  $\alpha$  的检验;

(2) 证明: 存在一个适当选择的常数 $k$, 使得一个水平为 $\alpha$ 的拒绝域为

$$
C (\bar {X}) = \{\bar {X}: | \bar {X} - \tilde {\theta} | > k \sqrt {S ^ {2} / n} \},
$$

其中  $\bar{\theta}=(\theta_{1}+\theta_{2})/2.$

35. 设  $(X_{1}, Y_{1}), (X_{2}, Y_{2}), \cdots, (X_{n}, Y_{n})$  是来自具有参数  $(\mu_{X}, \mu_{Y}, \sigma_{X}^{2}, \sigma_{Y}^{2}, \rho)$  的二元正态分布的独立同分布样本. 我们感兴趣的检验是

$$
H _ {0}: \mu_ {X} = \mu_ {Y} \leftrightarrow H _ {1}: \mu_ {X} \neq \mu_ {Y}.
$$

(1) 证明随机变量  $W_{i}=X_{i}-Y_{i}$  服从正态分布并计算其均值和方差;
(2) 证明上述假设可以用统计量

$$
T _ {W} = \frac {\bar {W}}{\sqrt {\frac {1}{n} S _ {W} ^ {2}}}
$$

进行检验, 其中  $\bar{W} = \frac{1}{n} \sum_{i=1}^{n} W_{i}$  和  $S_{W}^{2} = \frac{1}{n-1} \sum_{i=1}^{n} (W_{i} - \bar{W})^{2}$ . 进一步证明, 在  $H_{0}$  下,  $T_{W}$  服从 t 分布, 具有 n-1 的自由度 (这个检验被称为配对样本 t 检验).

## 第四章

## 多元模型