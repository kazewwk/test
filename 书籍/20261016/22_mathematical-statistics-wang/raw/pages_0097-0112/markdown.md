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

其 M 步, 即上式两边关于  $\theta$  求导, 并令其等于 0, 可求得

$$
\theta^ {(i + 1)} = \frac {x _ {1} \theta^ {(i)} + x _ {4} [ \theta^ {(i)} + 2 ]}{x _ {1} \theta^ {(i)} + (x _ {2} + x _ {3} + x _ {4}) [ \theta^ {(i)} + 2 ]} = \frac {1 5 9 \theta^ {(i)} + 6 8}{1 9 7 \theta^ {(i)} + 1 4 4}.
$$

如取  $\theta^{(0)}=0.5$ ，则四步迭代后可求得  $\theta$  的 MLE 为 0.6268.

![](images/page_100_image_5.jpg)

注2.3.5 在 $X_{1} = x_{1}$ 的条件下, $Z \sim B(x_{1}, 2 / (2 + \theta))$ 的原因: 以 $A_{1}$ 表示第一种结果出现的事件, $B_{1}, B_{2}$ 分别表示我们所定义的两个事件, $A_{1} = B_{1} \cup B_{2}$. 由定义知它们是独立的, 且 $P(A_{1}) = \frac{1}{2} + \frac{\theta}{4}, P(B_{1}) = 1 / 2, P(B_{2}) = \theta / 4$, 则可知 $P(B_{1} | A_{1}) = P(B_{1}) / P(A_{1}) = 2 / (2 + \theta)$.

![](images/page_100_image_7.jpg)

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

(2.4.1) 或 (2.4.3) 式显示, 不同先验分布将得到不同的 Bayes 估计. 因此, 如何选取先验分布就是 Bayes 统计的一个重要挑战. 另外, 在求取 Bayes 估计时, 还将面临积分计算问题. 如果参数维数高, 特别是现在流行的大模型中, 参数的维数非常高, 则涉及高维积分的计算问题.

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