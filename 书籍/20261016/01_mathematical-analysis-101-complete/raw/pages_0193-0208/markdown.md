## 第七章

## 微分中值定理

在建立了实数理论、引入了极限工具后, 我们开始着手研究函数, 这是因为数学分析的主要目的之一就是研究函数各种性质的. 这些性质有的是预设的, 比如是否有界、是否连续、是否单调、是否凹凸、发展趋势如何、光滑性如何、振荡性如何等. 这些性质或者具有明确的几何直观, 或者具有重要的分析属性, 抑或是实际问题的需求. 也有不少重要的性质并不是预设的, 而是随着探讨的深入, 无意中发现的奇异现象、偶得的神奇结论、意想不到的应用, 比如充满平面区域的连续曲线, 处处连续、处处不可微的函数, 周期三蕴涵着混沌等.

本章我们将重点讨论微分中值定理及其应用, 这是分析学中很深刻的一部分内容, 有人甚至将其比喻为微积分的巅峰之作. 我们暂不论此说法的夸张程度, 但多少能反映出微分这个基本概念对研究函数的重要性. 我们先简要梳理一下这部分内容发展的脉络.

首先极限是研究函数局部性质的一个基本工具, 一个函数在一点有极限我们就能得到在该点附近的局部有界性. 因此一个函数在一个区间上处处有极限, 就可以得到在此区间内每点附近都局部有界. 至于是否整体有界, 则需要把 (通常是无穷多) 这些点粘合起来统一考虑, 而前面的有限覆盖好像是为此而生的 $^{①}$ . 这样, 函数是否整体有界就与其极限存在的底层集合是否满足有限覆盖对接上了, 这使得我们再度认识到紧致集这个基本概念的重要性. 连续函数作为不仅极限存在而且极限值等于该点函数值的特殊情况, 自然就有了闭区间上的连续函数必定有界这一重要结论. 进而利用有界必有确界我们又得到了闭区间上的连续函数必能取到最大、最小值. 这里就体现出了局部与整体的联系.

如果我们考虑函数在一点附近函数值的大小, 很自然可以引入极值的概念. 这是一个局部概念. 从技术细节上来说, 如果一个函数在一点可微, 同时又是极值点, 那么无论是从几何直观还是从逻辑推导, 都不难证明该点的导数就应该为零. 这就是著名的 Fermat 引理, 这一结论是后续讨论的技术关键.

基于这个技术核心, 我们将其应用到闭区间上的可微函数, 只要加一点点技术限制, 使得最值点在区间内部达到, 那么最值点就是极值点, 从而这一点处的导数便为零. 这就是 Rolle $^{②}$ 中值定理. 由于 Rolle 中值定理有明确的几何意义, 所以无论从几何上还是分析甚至代数上, 都很自然地推广到著名的 Lagrange 中值定理. 两者本质上是等同的, 但是在应用的灵活性和广泛性上, Lagrange 中值定理都要更方便些. 如果把自变量和因变量都参数化, 我们就可以进一步把 Lagrange 中值定理推广到 Cauchy 中值定理. 这又是一个极其重要的结论, 具有深刻的影响和广泛的应用.

微分中值定理作为研究函数的基本工具, 有着多角度的推广. 一种常见的推广是将经典导数框架下的微分中值定理推广到各种广义的导数, 比如单侧导数、Dini 导数、对称导数等, 得到了更宽泛条件下中值定理的多种版本; 另一种推广是把它们作得更精细,表现为把涉及的一阶导数推广到高阶导数, 在表现形式上有 Taylor $^{①}$  展开式之结构; 还有一种推广表现为函数所在的定义域舞台的更一般化, 比如复数域中的微分中值定理、多元函数的微分中值定理、无穷维空间中的微分中值定理、映射的微分中值定理等 $^{②}$ .

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 有限覆盖定理远远晚于有界性这个概念, 前者是 19 世纪后半叶由 Heine 提出, 19 世纪 90 年代由 Borel 完善证明的.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Rolle, Michel, 1652 年 4 月 21 日—1719 年 11 月 8 日, 法国数学家.</span></small>

微分中值定理的深刻之处在于它建立了函数和导函数之间的某些联系, 是利用导数研究函数的强有力的工具. L'Hôpital 法则当属微分中值定理的直接应用之一, 它为计算不定式极限提供了一种简便的操作方法. Taylor 展开式是微分中值定理的一种推广和细化, 利用 Taylor 展开式, 可以考虑用函数的多项式逼近问题. 另外, 它的不同形式的余项表示给我们估计局部误差和整体误差提供了可能.

## 7.1 微分中值定理

## 7.1.1 Fermat 引理

微分中值定理的建立和证明, 需要用到下面的 Fermat 引理, 因此我们先来介绍这一基本结论. 为此, 我们先给出极值的定义.

定义 7.1.1(极值点、极值) 设 f 是定义在区间 I 上的函数,  $x_{0} \in I$ . 如果存在  $\delta > 0$ , 使得

$$
f (x) \geqslant f (x _ {0}) (f (x) \leqslant f (x _ {0})), \forall x \in (x _ {0} - \delta , x _ {0} + \delta) \cap I,
$$

则称 $x_0$ 为 $f$ 在 $I$ 上的一个极小 (大) 值点, $f(x_0)$ 称为极小 (大) 值.

若在上述定义中，在 $x \neq x_0$ 处不等号严格成立，则称 $f(x_0)$ 为严格极小（大）值。极大值点和极小值点统称为极值点，极大值和极小值统称为极值。

直观上看, 如果函数 $y = f(x)$ 在点 $x_0$ 处取极值, 并且该函数在点 $(x_0, f(x_0))$ 处存在切线, 则该切线应该是水平的. 事实上, 对于函数极值点处的导数, 我们有下面的Fermat引理.

引理 7.1.1 (Fermat 引理) 设函数 f 在点  $x_{0}$  处可导且  $x_{0}$  为极值点, 则  $f'(x_{0}) = 0$ .

证明 不妨设 $f$ 在点 $x_0$ 取得极大值, 则

$$
f ^ {\prime} (x _ {0}) = f _ {+} ^ {\prime} (x _ {0}) = \lim _ {x \to x _ {0} ^ {+}} \frac {f (x) - f (x _ {0})}{x - x _ {0}} \leqslant 0.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Taylor, Brook, 1685 年 8 月 18 日—1731 年 12 月 29 日, 英国数学家.<br>② 注意, 不同基空间中的微分中值定理完全对应的表现形式有可能 “不成立”, 比如在复变函数中. 此时, 相应的表现形式可能有些改变, 甚至以不等式的方式出现.</span></small>

同样有

$$
f ^ {\prime} (x _ {0}) = f _ {-} ^ {\prime} (x _ {0}) = \lim _ {x \to x _ {0} ^ {-}} \frac {f (x) - f (x _ {0})}{x - x _ {0}} \geqslant 0.
$$

因此, $f'(x_0) = 0$.

注7.1.1 使得 $f'(x) = 0$ 的点 $x_0$ 也称为 $f(x)$ 的驻点或可疑点. Fermat 引理告诉我们, 若函数在极值点处可导, 则极值点必为驻点. 反之不一定成立, 比如, $x_0 = 0$ 是函数 $y = x^3$ 的驻点, 因为在该点处导数为零, 但该函数的性质告诉我们, 此驻点并不是极值点. 尽管如此, 在寻找函数的极值点时, 我们仍然可以先把范围缩小到仅考虑驻点和那些导数不存在的点, 因此称驻点为极值的可疑点是很形象的.

灵活运用注解中的逻辑推理, 可以得到一些有趣的结论: 比如函数  $y = R^{3}(x)$ , 其中  $R(x)$  是 Riemann 函数, 如果我们能用其他方法证明该函数在某些无理点处可导, 那么这些点处的导数一定为零, 这是因为它们都是极值点.

## 7.1.2 Rolle 中值定理

由 Fermat 引理, 可以立即得到下面的 Rolle 中值定理.

定理 7.1.2 (Rolle 中值定理) 设函数  $f(x)$  在闭区间  $[a, b]$  上连续，在开区间  $(a, b)$  内可微，且  $f(a) = f(b)$ ，则存在  $\xi \in (a, b)$  使  $f'(\xi) = 0$ .

证明 若 $f$ 为常数, 则结论显然成立. 否则, 存在 $x_0 \in (a, b)$ 使得 $f(x_0) \neq f(a) = f(b)$. 不妨设 $f(x_0) > f(a)$.

由于 $f$ 在 $[a, b]$ 上连续, 因而它在 $[a, b]$ 上有最大值. 设 $\xi \in [a, b]$ 是 $f$ 在 $[a, b]$ 上的最大值点. 则 $f(\xi) \geqslant f(x_0) > f(a) = f(b)$. 从而 $\xi \in (a, b)$. 所以 $\xi$ 是极大值点. 于是由 Fermat 引理得 $f'(\xi) = 0$.

例 7.1.1 考虑 2n 次多项式  $P(x)=x^{n}(1-x)^{n}\ (n\in\mathbb{N})$ . 证明 n 次多项式  $P^{(n)}(x)$  在区间  $(0,1)$  内有 n 个互异的实零点.

证明 首先, 利用 Leibniz 求导法则, 可知 $P^{(n)}(x)$ 是一个 $n$ 次多项式, 且

$$
P ^ {(m)} (x) = (x ^ {n} (1 - x) ^ {n}) ^ {(m)} = \sum_ {i + j = m} \frac {m !}{i ! j !} \frac {n !}{(n - i) !} \frac {n !}{(n - j) !} (- 1) ^ {j} x ^ {n - i} (1 - x) ^ {n - j}.
$$

故当  $m=0,1,2,\cdots,n-1$  时，上式右端的各项中均含有因式  $x(1-x)$ . 因此

$$
P ^ {(m)} (0) = P ^ {(m)} (1) = 0, \quad m = 0, 1, 2, \dots , n - 1.
$$

由 $P(0) = P(1) = 0$ 根据Rolle中值定理知，存在 $\xi \in (0,1)$ 使 $P^{\prime}(\xi) = 0$。注意到 $P^{\prime}(x)$ 在区间 $[0,\xi]$ 与 $[\xi ,1]$ 上也适合Rolle中值定理的条件，因此存在 $\eta_1\in (0,\xi)$ 及$\eta_{2}\in (\xi ,1)$ 使得 $P^{\prime \prime}(\eta_i) = 0,i = 1,2,$ 其中 $0 <   \eta_{1} <   \eta_{2} <   1$

注意导函数 $P''(x)$ 在三个区间 $[0, \eta_1], [\eta_1, \eta_2], [\eta_2, 1]$ 上都满足 Rolle 中值定理的条件, 因此存在三个点 $\zeta_i, 0 < \zeta_1 < \zeta_2 < \zeta_3 < 1$, 使得

$$
P ^ {\prime \prime \prime} (\zeta_ {i}) = 0, \qquad i = 1, 2, 3.
$$

将此过程进行下去, 可得题目的结论.

Rolle 中值定理的几何意义是当可微函数 (允许函数在端点只是连续) 在端点的值相等的时候, 则该函数的曲线一定有一条斜率为零的切线, 即该切线平行于曲线端点的连线. 根据这一几何解释, 旋转坐标就可以得到更一般的结论: 一个可微函数, 其函数图像必定有一条切线平行于曲线端点的连线 (图 7.1). 这就是如下极为重要的 Lagrange 中值定理:

![](images/page_196_image_6.jpg)

图 7.1 Rolle 中值定理与 Lagrange 中值定理

## 7.1.3 Lagrange 中值定理

定理 7.1.3 设函数 f 在有界闭区间  $[a, b]$  上连续，在开区间  $(a, b)$  内可微。则存在  $\xi \in (a, b)$  使得

$$
f (b) - f (a) = f ^ {\prime} (\xi) (b - a). \tag {7.1.1}
$$

证明 前面的几何直观解释提示我们，可以试图通过构造辅助函数把问题转化为Rolle中值定理的情形.为此,我们设

$$
F (x) = f (x) - k x, \tag {7.1.2}
$$

其中 $k$ 待定使得 $F(x)$ 满足Rolle中值定理的条件: $F(a) = F(b)$ ，即

$$
f (a) - k a = f (b) - k b.
$$

所以, 只要取 $k = \frac{f(b) - f(a)}{b - a}$ 即可. 易见 $F(x)$ 在 $[a, b]$ 上连续, 在 $(a, b)$ 内可微, 于是由 Rolle 中值定理, 存在 $\xi \in (a, b)$ 使得 $F'(\xi) = 0$. 即

$$
f (b) - f (a) = f ^ {\prime} (\xi) (b - a).
$$

□

注7.1.2 显然,证明过程中的 $F\left( x\right)$ 的选取不是唯一的,因为任何一个形如

$$
F (x) := (f (b) - f (a)) x - f (x) (b - a) + c
$$

的函数都满足 Rolle 中值定理的条件, 因此我们可以通过选取适当的 c, 使得  $F(x)$  的表示更 “简捷”:  $F(a) = F(b) = 0$ . 这只要取  $c = -af(b) + bf(a)$  即可, 即

$$
F (x) := (f (b) - f (a)) (x - a) - (f (x) - f (a)) (b - a). \tag {7.1.3}
$$

另外，函数

$$
F (x) := f (x) - \frac {x - a}{b - a} f (b) - \frac {x - b}{a - b} f (a) \tag {7.1.4}
$$

也满足 $F(a) = F(b) = 0$。在后面章节可以看出，函数 $F$ 的这些表达式都有各自的特点。

Lagrange 中值定理的应用非常灵活和广泛, 比如, 利用此定理我们立即可得下面的几个重要结论.

推论7.1.4 设函数 $f(x) \in C[a, b]$, 且在 $(a, b)$ 内可导. 若 $f'(x) = 0$, 则 $f(x) \equiv c$, 其中 $c$ 是一常数.

证明 $\forall x\in [a,b]$ ，在 $[a,x]$ 上应用Lagrange中值定理知，存在 $\xi \in (a,x)$ ，使得

$$
0 = f ^ {\prime} (\xi) = \frac {f (\xi) - f (a)}{x - a}.
$$

由此可得  $f(x) \equiv f(a) = c.$

该推论的结论似乎显然, 但如果不利用 Lagrange 中值定理, 证明似乎并不平凡.

推论7.1.5 设函数 $f(x), g(x) \in C[a, b]$，且在 $(a, b)$ 内均可导。若 $f'(x) = g'(x)$，则 $f(x) = g(x) + c$，其中 $c$ 为常数。

证明 对函数  $f(x)-g(x)$  应用推论 7.1.4 即得.

例7.1.2 设 $y'(x) = \frac{1}{1 + x^2}$, $y(1) = 0$, 证明 $y(x) = \arctan x - \frac{\pi}{4}$.

证明 考虑函数 $f(x) = y(x) - \arctan x$，则有

$$
f ^ {\prime} (x) = y ^ {\prime} (x) - \frac {1}{1 + x ^ {2}} \equiv 0.
$$

故 $f(x) = y(x) - \arctan x \equiv c$. 注意到 $f(1) = -\frac{\pi}{4}$, 所以 $y(x) = \arctan x - \frac{\pi}{4}$.

推论 7.1.6 设函数  $f(x)$  在  $[a, b]$  上连续，在  $(a, b)$  内可导.

(1) 若 $\forall x \in (a, b), f'(x) > 0$, 则 $f$ 在 $[a, b]$ 上严格单增;
(2) 若 $\forall x \in (a, b)$, $f'(x) \geqslant 0$, 则 $f$ 在 $[a, b]$ 上单增.

证明 (1) 如果 $f'(x) > 0$，则对任意 $a \leqslant x_1 < x_2 \leqslant b$，由 Lagrange 中值定理得

$$
f (x _ {2}) - f (x _ {1}) = f ^ {\prime} (\xi) (x _ {2} - x _ {1}) > 0,
$$

可得  $f(x_{2}) > f(x_{1})$ .

(2) 的证明可类似给出.

注 7.1.3 Lagrange 中值定理的另一种常见的表述形式如下.由于等式(7.1.1)等价于形式

$$
f (b) = f (a) + f ^ {\prime} (\xi) (b - a), \tag {7.1.5}
$$

所以, Lagrange 中值定理又称为有限增量定理.

对于等式 (7.1.1) 中的 $\xi \in (a, b)$, 我们更常用 $\xi = a + \theta(b - a)$ 表示, 其中 $\theta \in (0, 1)$. 这一表述方式在 $a, b$ 的大小关系不清楚时更为便利. 这样, 我们又把有限增量公式写成

$$
f (b) = f (a) + f ^ {\prime} (a + \theta (b - a)) (b - a). \tag {7.1.6}
$$

需要强调的是  $\theta$  一般来说是依赖于端点 a, b 的.

例 7.1.3 证明:  $y = \arctan x$  在  $(-\infty, +\infty)$  上一致连续.

证明 任取 $x_{1}, x_{2} \in \mathbb{R} (x_{1} < x_{2})$，在区间 $[x_{1}, x_{2}]$ 上，函数 $\arctan x$ 满足 Lagrange 中值定理的所有条件，因此存在 $\xi \in (x_{1}, x_{2})$，使得

$$
\arctan x _ {1} - \arctan x _ {2} = \frac {1}{1 + \xi^ {2}} (x _ {1} - x _ {2}).
$$

故

$$
\left| \arctan x _ {1} - \arctan x _ {2} \right| \leqslant \left| x _ {1} - x _ {2} \right|.
$$

因此, 立得函数在整个 $\mathbb{R}$ 上的一致连续性.

注7.1.4 由此例还可以看出, 如果 $(a, b)$ 内的一个连续函数有有界的导数, 则该函数在 $(a, b)$ 内一致连续. 对比注7.1.6.

## 7.1.4 Cauchy 中值定理

如果将 Lagrange 中值定理运用到用参数表示的函数, 则可以得到以下的 Cauchy 中值定理.

定理 7.1.7 (Cauchy 中值定理) 设函数  $f(x)$ ,  $g(x)$  在有界闭区间  $[a, b]$  上连续，在开区间  $(a, b)$  内可微. 则存在  $\xi \in (a, b)$  使得

$$
(f (b) - f (a)) g ^ {\prime} (\xi) = (g (b) - g (a)) f ^ {\prime} (\xi). \tag {7.1.7}
$$

特别地, 若 $g'(x) \neq 0$, 则

$$
\frac {f (b) - f (a)}{g (b) - g (a)} = \frac {f ^ {\prime} (\xi)}{g ^ {\prime} (\xi)}. \tag {7.1.8}
$$

证明 类似于定理 7.1.3 的证明, 我们希望构造出一个辅助函数把定理转化为 Rolle 中值定理的情形. 为此, 我们先形式上设

$$
F (x) := f (x) - k g (x), \tag {7.1.9}
$$

其中 k 待定, 使得  $F(a) = F(b)$ , 即

$$
f (a) - k g (a) = f (b) - k g (b).
$$

因此, 取

$$
k = \frac {f (b) - f (a)}{g (b) - g (a)}.
$$

考虑到分母可能为零的情况, 因此, 我们可以取

$$
F (x) := (f (b) - f (a)) (g (x) - g (a)) - (g (b) - g (a)) (f (x) - f (a)), \quad \forall x \in [ a, b ]. \tag {7.1.10}
$$

则 $F(x)$ 在 $[a,b]$ 上连续, 在 $(a,b)$ 内可微, 且 $F(a) = F(b) = 0$. 由 Rolle 中值定理, 存在 $\xi \in (a,b)$ 使得 $F'(\xi) = 0$. 此即 (7.1.7) 式成立.

当  $g'(x) \neq 0$  时, 即 (7.1.8) 式成立.

## 7.1.5 Darboux 介值定理

上面我们介绍了三个经典的微分中值定理. 事实上, 函数的导函数还具有一个重要的性质: 导数的介值性. 我们给出下面的 Darboux 介值定理.

定理 7.1.8 (Darboux 介值定理) 设 f 在  $[a, b]$  上可微，且  $f'(a) < f'(b)$ . 则对任何  $\lambda \in (f'(a), f'(b))$ ，存在  $\xi \in (a, b)$  使得  $f'(\xi) = \lambda$ .

证明 考虑

$$
F (x) := f (x) - \lambda x, \qquad x \in [ a, b ].
$$

则 $F'(a) < 0, F'(b) > 0$. 于是存在 $\delta > 0$ 使得当 $x \in (a, a + \delta)$ 时, $F(x) < F(a)$. 所以 $a$ 不是 $F$ 在 $[a, b]$ 上的最小值点. 同理, $b$ 不是 $F$ 在 $[a, b]$ 上的最小值点.

另一方面, 由于 $F$ 连续, 它在 $[a, b]$ 上有最小值点 $\xi \in [a, b]$, 则 $\xi \in (a, b)$, 从而它是极小值点. 于是由 Fermat 引理, $F'(\xi) = 0$. 即 $f'(\xi) = \lambda$.

注 7.1.5 定理中的假设条件  $f'(a) < f'(b)$  显然是非实质性的，即如果  $f'(a) > f'(b)$ ，则类似可证:对任何介于  $f'(b)$  和  $f'(a)$  之间的实数  $\lambda$ ，都存在  $\xi \in (a, b)$  使得  $f'(\xi) = \lambda$ .

需要强调的是, 虽然 Darboux 介值定理告诉我们一个函数的导函数总是具有介值性, 这是导函数的一个显著特点, 具有极其重要的应用, 但是这并不是说导函数一定连续. 下面的例子将告诉我们这点. 然而, 由介值性我们可以断定, 导函数如果不连续的话, 那么也一定不会是跳跃间断点或者可去间断点.

另外, 我们看到, 如果一个函数的导函数在某个区间上非零, 那么它要么是恒为正, 要么恒为负; 与之对应的则是原来的函数要么严格单调上升, 要么严格单调下降. 因此, 如果一个函数的导函数非零, 则它一定具有反函数.

关于 Darboux 介值定理更多的性质和应用, 我们在后面还会作进一步的探讨.

例7.1.4 考虑函数

$$
f (x) = \left\{ \begin{array}{l l} x ^ {2} \sin \frac {1}{x}, & x \neq 0, \\ 0, & x = 0. \end{array} \right.
$$

容易得到

$$
f ^ {\prime} (x) = \left\{ \begin{array}{l l} 2 x \sin \frac {1}{x} - \cos \frac {1}{x}, & x \neq 0, \\ 0, & x = 0. \end{array} \right.
$$

由于

$$
\lim _ {n \to + \infty} f ^ {\prime} \left(\frac {1}{2 n \pi}\right) = - 1, \quad \lim _ {n \to + \infty} f ^ {\prime} \left(\frac {1}{(2 n + 1) \pi}\right) = 1,
$$

可知导函数 $f^{\prime}(x)$ 在 $x = 0$ 点不连续.

有了 Darboux 介值定理, 我们回头再看一下 Cauchy 中值定理. 根据注 7.1.5 知, 当 $g'(x) \neq 0$ 时, 根据 Darboux 介值定理, $g'(x)$ 必恒正或恒负, 不妨假设 $g'(x) > 0$. 从而 $g$ 在 $[a, b]$ 上严格单增. 我们可以把 Cauchy 中值定理视为参数方程确定的函数所对应的 Lagrange 中值定理. 具体地, 令 $X = g(x), Y = f(x)$. 则有 $Y = f(g^{-1}(X))$, 即 $Y$ 作为 $X$ 的函数在 $[g(a), g(b)]$ 上连续, 在 $(g(a), g(b))$ 内可微. 因此由 Lagrange 中值定理知存在 $\eta \in (g(a), g(b))$ 使得

$$
Y (g (b)) - Y (g (a)) = \frac {\mathrm{d} Y}{\mathrm{d} X} (\eta) (g (b) - g (a)).
$$

由 $g(x)$ 的连续性和单调性, 存在唯一的 $\xi \in (a, b)$ 使得 $g(\xi) = \eta$. 从而

$$
\begin{array}{l} f (b) - f (a) = Y (g (a)) - Y (g (b)) \\ = \frac {\mathrm{d} Y}{\mathrm{d} X} (g (\xi)) (g (b) - g (a)) = \frac {f ^ {\prime} (\xi)}{g ^ {\prime} (\xi)} (g (b) - g (a)). \\ \end{array}
$$

这就证明了结论.

Cauchy 中值定理有明确的几何意义:设在 XOY 坐标平面上的曲线由参数方程  $X = g(x)$ ,  $Y = f(x)$  给出，其中 f, g 满足定理条件，则存在一点  $\xi \in (a, b)$ ，使得过点  $(g(\xi), f(\xi))$  的切线平行于两端点的连线.

类似于 Lagrange 中值定理, Cauchy 中值定理也常写成如下形式:

$$
\frac {f (b) - f (a)}{g (b) - g (a)} = \frac {f ^ {\prime} (a + \theta (b - a))}{g ^ {\prime} (a + \theta (b - a))}, \quad 0 <   \theta <   1.
$$

上述所有的微分中值定理, 当条件满足 (比如函数足够光滑性) 时, 可以多次应用.

例 7.1.5 设  $f(x)$  在  $(0,1]$  上连续, 在  $(0,1)$  内可导, 且  $\lim_{x\to0^{+}}\sqrt{xf'(x)}=c$ . 证明  $f(x)$  在区间  $(0,1]$  上一致连续.

证明 由假设可知, 存在 $M > 0$ 和 $0 < \delta_0 < 1$, 使得

$$
| \sqrt {x} f ^ {\prime} (x) | \leqslant M, \quad x \in (0, \delta_ {0} ].
$$

任取 $x_{1}, x_{2} \in (0, \delta_{0}], x_{1} < x_{2}$, 根据 Cauchy 中值定理, 知存在一点 $\xi \in (x_{1}, x_{2})$,

$$
\frac {f (x _ {1}) - f (x _ {2})}{\sqrt {x _ {1}} - \sqrt {x _ {2}}} = 2 \sqrt {\xi} f ^ {\prime} (\xi).
$$

于是, 有

$$
| f (x _ {1}) - f (x _ {2}) | <   2 M | \sqrt {x _ {1}} - \sqrt {x _ {2}} |
$$

上式对 $x_{1} = x_{2}$ 时也成立. 注意到

$$
\left| \sqrt {x _ {1}} - \sqrt {x _ {2}} \right| ^ {2} \leqslant \left| x _ {1} - x _ {2} \right|,
$$

故有

$$
| f (x _ {1}) - f (x _ {2}) | <   2 M \sqrt {| x _ {1} - x _ {2} |}.
$$

此关系式蕴涵着函数的一致连续性.

![](images/page_201_image_18.jpg)

注7.1.6 在本例中, 特别取 $f(x) = \sqrt{x}, x \in (0,1]$, 可以得到下面的结论: 存在导函数无界、非 Lipschitz 连续, 但仍然一致连续的函数. 对比注7.1.4.

## 习题 7.1

1. 试构造一个在 $[0,1]$ 上处处可导但其导数在 $[0,1]$ 上无界的函数.
2. 设 $f(x)$ 在 $[a, b]$ 上连续，在 $(a, b)$ 内可微，且 $f(a) = f(b) = 0$. 证明:存在 $\xi \in (a, b)$，使得 $f'(\xi) = 2f(\xi)$.
3. 设 $f(x)$ 在 $[a, b]$ 上二阶可微, 且 $f(a) = f(b) = 0$, $f_{+}^{\prime}(a)f_{-}^{\prime}(b) > 0$. 证明: 存在 $\xi \in (a, b)$, 使得 $f''(\xi) = 0$.

4. 设一元实函数 $f$ 在 $[a, b]$ 上连续, 在 $(a, b)$ 内可导, $ab > 0$. 证明: 存在 $\xi \in (a, b)$ 使得

$$
\frac {1}{a - b} \left| \begin{array}{c c} a & b \\ f (a) & f (b) \end{array} \right| = f (\xi) - \xi f ^ {\prime} (\xi).
$$

5. 设 $f(x)$ 为 $[a, b]$ 上的三阶可导函数，且 $f(a) = f'(a) = f(b) = 0$. 证明:任给 $c \in [a, b]$，存在 $\xi \in (a, b)$，使得

$$
f (c) = \frac {1}{6} f ^ {(3)} (\xi) (c - a) ^ {2} (c - b).
$$

6. 设函数 $f$ 在区间 $[a, b]$ 上可导, 且存在 $M > 0$, 使得

$$
| f ^ {\prime} (x) | \leqslant M, \quad \forall x \in [ a, b ].
$$

证明:

$$
\left| f (x) - \frac {f (a) + f (b)}{2} \right| \leqslant \frac {1}{2} M (b - a), \quad \forall x \in [ a, b ].
$$

7. 证明: 多项式 $x^{3} - 3x + c$ 在 $[0,1]$ 上不存在两个不同的实根.

8. 证明: Chebyshev $^{①}$ 多项式 $e^{x}\frac{d^{n}}{dx^{n}}(x^{n}e^{-x})$ 有 n 个正的实根.

9. 证明: Legendre $^{②}$ 多项式 $\frac{\mathrm{d}^{n}}{\mathrm{d}x^{n}}(x^{2}-1)^{n}$ 在 $(-1,1)$ 内有 n 个两两互异的实根.

10. 设函数 $f(x)$ 在区间 $[a, b]$ 上连续, 在区间 $(a, b)$ 内可导, $\xi$ 是 $(a, b)$ 内一点. 问是否一定存在 $a_1, b_1 \in (a, b), a_1 < \xi < b_1$, 使得 $f'(\xi) = \frac{f(b_1) - f(a_1)}{b_1 - a_1}$?

进一步, 试着给出一定存在  $a_{1}, b_{1}$  使得上式成立的某些函数类.

11. 设 $f$ 在 $[a, +\infty)$ 上可微, 且

$$
0 \leqslant f ^ {\prime} (x) \leqslant f (x), \quad f (a) = 0, \quad \forall x \in [ a, + \infty).
$$

证明: 在  $[a, +\infty)$  上  $f \equiv 0$ .

12. 设 $f$ 在 $[a, +\infty)$ 上可微, 且

$$
| f ^ {\prime} (x) | \leqslant M | f (x) |, \quad f (a) = 0, M > 0, \forall x \in [ a, + \infty).
$$

证明: 在  $[a, +\infty)$  上  $f(x) \equiv 0$ .

13. 设  $f(x)=a_{1}\sin x+a_{2}\sin 2x+\cdots+a_{n}\sin nx$ ，且  $|f(x)|\leqslant|\sin x|$ ，其中  $a_{1}, a_{2}, \cdots, a_{n}$  为常数。求证: $|a_{1}+2a_{2}+\cdots+na_{n}|\leqslant1$ 。

14. 设 $f(x)$ 在 $[0,1]$ 上连续, 在 $(0,1)$ 内可导. 若 $f(0) = 0$, $f(1) = 1$, 证明: 存在 $\xi_1, \xi_2 \in (0,1)$, $\xi_1 \neq \xi_2$, 使得 $f'(\xi_1)f'(\xi_2) = 1$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Чебышёв, Пафнутий Львович, 英文 Chebyshev, Pafnuty Lvovich, 1821 年 5 月 16 日—1894 年 12 月 8 日, 俄国数学家、力学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Legendre, Adrien-Marie, 1752 年 9 月 18 日—1833 年 1 月 10 日, 法国数学家.</span></small>

15. 设  $f(x)$  在  $[a, b]$  上连续, 在  $(a, b)$  内可导. 记  $S(x)$  为由  $(a, f(a)), (b, f(b)), (x, f(x))$  三点组成的三角形面积, 试对  $S(x)$  应用 Rolle 中值定理证明 Lagrange 中值定理.

16. 设 $f(x), g(x)$ 在 $[a, b]$ 上连续, 在 $(a, b)$ 内可导. 记 $T(x)$ 为由 $(f(a), g(a)), (f(b), g(b)), (f(x), g(x))$ 三点组成的三角形面积, 试对 $T(x)$ 应用 Rolle 中值定理证明 Cauchy 中值定理.

17. 设 $f(x), g(x), h(x)$ 在 $[a, b]$ 上连续, 在 $(a, b)$ 内可导. 证明: 存在 $\xi \in (a, b)$ 使得

$$
\left| \begin{array}{c c c} f ^ {\prime} (\xi) & g ^ {\prime} (\xi) & h ^ {\prime} (\xi) \\ f (a) & g (a) & h (a) \\ f (b) & g (b) & h (b) \end{array} \right| = 0.
$$

18. 设函数 $f$ 在 $[a, b]$ 上连续, 在 $(a, b)$ 内 Schwarz 对称可导, 且 $f(a) = f(b) = 0$, 证明: 存在 $x_1, x_2 \in (a, b)$, 使得

$$
f ^ {[ 1 ]} (x _ {1}) \geqslant 0, f ^ {[ 1 ]} (x _ {2}) \leqslant 0.
$$

19. 设函数 $f$ 在 $[a, b]$ 上连续, 在 $(a, b)$ 内 Schwarz 对称可导, 证明: 存在 $x_1, x_2 \in (a, b)$, 使得

$$
f ^ {[ 1 ]} (x _ {1}) \leqslant \frac {f (b) - f (a)}{b - a} \leqslant f ^ {[ 1 ]} (x _ {2}).
$$

20. 设函数 $f$ 在 $[a, b]$ 上连续, 在 $(a, b)$ 内 Schwarz 对称可导, 且对任意的 $x \in (a, b)$, 有 $g^{[1]}(x) \neq 0$, 证明: 存在 $x_1, x_2 \in (a, b)$, 使得 $g(x)$ 为凸函数,

$$
\frac {f ^ {[ 1 ]} (x _ {1})}{g ^ {[ 1 ]} (x _ {1})} \leqslant \frac {f (b) - f (a)}{g (b) - g (a)} \leqslant \frac {f ^ {[ 1 ]} (x _ {2})}{g ^ {[ 1 ]} (x _ {2})}.
$$

21. (类 Rolle 中值定理) 设 $f$ 在区间 $(a, b)$ ((a, b) 可为无界区间) 内可导. 如果存在 $a_{n}, b_{n} \in (a, b)$ 使得当 $n \to +\infty$ 时 $a_{n} \to a, b_{n} \to b$, 且 $\lim_{n \to +\infty} f(a_{n}) = \lim_{n \to +\infty} f(b_{n}) = \alpha \in \mathbb{R}$, 则存在 $\xi \in (a, b)$, 使得 $f'(\xi) = 0$.

22. (类 Lagrange 中值定理) 设 $f$ 在区间 $(a, b)$ 内可导. 如果存在 $a_{n}, b_{n} \in (a, b)$ 使得当 $n \to +\infty$ 时 $a_{n} \to a, b_{n} \to b$, 且 $\lim_{n \to +\infty} f(a_{n}) = \alpha \in \mathbb{R}, \quad \lim_{n \to +\infty} f(b_{n}) = \beta \in \mathbb{R}$, 则存在 $\xi \in (a, b)$, 使得 $f'(\xi) = \frac{\beta - \alpha}{b - a}$.

23. (Lagrange 二阶微分中值定理) 设 $f$ 在 $[a, b]$ 上可导, 在 $(a, b)$ 内二阶可导. 证明: 存在 $\xi \in (a, b)$, 使得

$$
f ^ {\prime} (b) - f ^ {\prime} (a) = f ^ {\prime \prime} (\xi) (b - a).
$$

24. (Cauchy 二阶微分中值定理) 设 $f, g$ 在 $[a, b]$ 上可导, 在 $(a, b)$ 内均二阶可导, 若 $g''$ 在 $(a, b)$ 内处处非零. 证明: 存在 $\xi \in (a, b)$, 使得

$$
\frac {f ^ {\prime} (b) - f ^ {\prime} (a)}{g ^ {\prime} (b) - g ^ {\prime} (a)} = \frac {f ^ {\prime \prime} (\xi)}{g ^ {\prime \prime} (\xi)}.
$$

25. 考虑 Darboux 介值定理退化的情形: 设 $f$ 在 $[a, b]$ 上可微, 且 $f'(a) = A = f'(b)$. 试问在 $(a, b)$ 内是否一定存在 $\xi \in (a, b)$ 使得 $f'(\xi) = A$?

26. (Flett 中值定理 $^{①}$ ) 如果  $f(x)$  在  $[a, b]$  上可导，且  $f'(a) = f'(b)$ . 试证明存在  $\xi \in (a, b)$  满足

$$
\frac {f (\xi) - f (a)}{\xi - a} = f ^ {\prime} (\xi),
$$

并给出此关系式的几何解释. 进一步考虑去掉条件  $f'(a) = f'(b)$  时的推广.

27. 试考虑能否将上题推广到类似 Cauchy 中值定理的框架中去, 即考虑两个函数 $f(x)$ 和 $g(x)$ 的情形.

## 7.2 L'Hôpital 法则

L'Hôpital $^{②}$ 法则是计算函数不定式极限的重要工具之一. 粗略说来, L'Hôpital 法则就是把两个函数商的极限转化为求它们的导函数商的极限. 大致说来, 与之对应的 Stolz 公式讨论的是离散型的场景.

我们先界定一下什么样的极限称为不定式的极限. 在计算函数极限时, 我们经常遇到下列两种情形:

(1) 当  $x \rightarrow x_{0}$  时,  $f(x) \rightarrow 0$ ,  $g(x) \rightarrow 0$ ;
(2) 当  $x \rightarrow x_{0}$  时,  $f(x) \rightarrow \infty$ ,  $g(x) \rightarrow \infty$

(其中  $x_{0}$  可以取  $\pm\infty$ ). 然后我们待求的极限可能是下面的组合 (纯粹是形式记号):

$$
\infty - \infty , \quad 0 \cdot \infty , \quad \frac {0}{0}, \quad \frac {\infty}{\infty}, \quad 1 ^ {\infty}, \quad 0 ^ {0}, \quad \infty^ {0}, \dots .
$$

这些形式我们统称为不定式极限.

所有这些不定式极限, 经过简单的变换都可以转化为  $\frac{0}{0}$  型不定式. 比如,

$$
\infty - \infty = \infty \cdot (1 - 1) = \frac {0}{1 / \infty} = \frac {0}{0}, \quad 0 ^ {0} = \mathrm{e} ^ {0 \cdot \ln 0} = \mathrm{e} ^ {\frac {0}{0}}
$$

等.

考虑到在具体应用中, 虽然 $\frac{\infty}{\infty}$ 型也可以转化为 $\frac{0}{0}$ 型, 但在很多场景下, 能直接给出前者相应的 L'Hôpital 法则, 会带来很多方便. 因此, 下面我们仅详细讨论两种不定式极限: $\frac{0}{0}$ 型和 $\frac{\infty}{\infty}$ 型.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① FLETT T M. A mean value theorem. Math. Gazette, 1958, 42: 38-39.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Marquis de L'Hôpital, Guillaume François Antoine, 1661 年—1704 年 2 月 2 日, 法国数学家.</span></small>

## 7.2.1 $\frac{0}{0}$ 型极限

定理 7.2.1 (L'Hôpital 法则之一) 设 $f(x), g(x)$ 在 $(a, b)$ 内可导, 且 $g'(x)$ 处处非零. 如果

(1) $\lim_{x\to a^{+}}f(x) = \lim_{x\to a^{+}}g(x) = 0;$
(2) $\lim_{x\to a^{+}}\frac{f'(x)}{g'(x)} = \alpha$ ，其中 $\alpha$ 为实数或 $\pm \infty$

则

$$
\lim _ {x \to a ^ {+}} \frac {f (x)}{g (x)} = \lim _ {x \to a ^ {+}} \frac {f ^ {\prime} (x)}{g ^ {\prime} (x)} = \alpha .
$$

证明 补充定义 $f(a) = g(a) = 0$，则 $f, g$ 在 $[a, b)$ 上连续。由 Cauchy 中值定理，任给 $x \in (a, b)$，存在 $\xi \in (a, x)$，使得

$$
\frac {f (x)}{g (x)} = \frac {f (x) - f (a)}{g (x) - g (a)} = \frac {f ^ {\prime} (\xi)}{g ^ {\prime} (\xi)}.
$$

当 $x \to a^{+}$ 时, 有 $\xi \to a^{+}$, 从而

$$
\lim _ {x \to a ^ {+}} \frac {f (x)}{g (x)} = \lim _ {x \to a ^ {+}} \frac {f ^ {\prime} (\xi)}{g ^ {\prime} (\xi)} = \alpha . \tag {7.2.1}
$$

![](images/page_205_image_13.jpg)

<details>
<summary>natural_image</summary>

Vertical gradient bar with light blue to white transition, no text or symbols present
</details>

注 7.2.1 只要定理条件满足, 则可以多次应用 L'Hôpital 法则. 即如果仍有  $f_{+}^{\prime}(a)=g_{+}^{\prime}(a)=0$ , 则可以利用二次导数继续求极限:

$$
\lim _ {x \to a ^ {+}} \frac {f (x)}{g (x)} = \lim _ {x \to a ^ {+}} \frac {f ^ {\prime} (x)}{g ^ {\prime} (x)} = \lim _ {x \to a ^ {+}} \frac {f ^ {\prime \prime} (x)}{g ^ {\prime \prime} (x)},
$$

高阶导数以此类推. 但是必须注意, 在应用 L'Hôpital 法则时, 必须每一步都要先验证极限 $\lim_{x\to a^{+}}\frac{f'(x)}{g'(x)}$ 是否存在: 如果极限存在, 则可以进行下去; 如果极限不存在, 并不能说明原极限不存在, 只是需要另寻他法.

例7.2.1 考虑极限

$$
\lim _ {x \to \infty} \frac {x - \sin x}{x + \sin x}.
$$

一方面显然该极限为 1, 但是如果盲目使用 L'Hôpital 法则, 就会得到

$$
\lim _ {x \to \infty} \frac {x - \sin x}{x + \sin x} = \lim _ {x \to \infty} \frac {1 - \cos x}{1 + \cos x} = \lim _ {x \to \infty} \frac {\sin x}{- \sin x} = - 1.
$$

![](images/page_205_image_21.jpg)

注7.2.2 L'Hôpital法则对于区间 $(a,b)$ 为 $(- \infty, b)$ 或 $(a, +\infty)$, 结论仍然成立, 只需考虑变量替换 $x = \frac{1}{t}$ 即可.

例7.2.2 求极限 $\lim_{x\to 0}\frac{\ln(1 + x) - x}{x^2}.$

解 由 L'Hôpital 法则可得

$$
\lim _ {x \to 0} \frac {\ln (1 + x) - x}{x ^ {2}} = \lim _ {x \to 0} \frac {(1 + x) ^ {- 1} - 1}{2 x} = - \frac {1}{2}.
$$

例 7.2.3 求极限  $\lim_{x\to0}\frac{x-\sin x}{x^{3}}$ .

解 由 L'Hôpital 法则可得

$$
\lim _ {x \to 0} \frac {x - \sin x}{x ^ {3}} = \lim _ {x \to 0} \frac {1 - \cos x}{3 x ^ {2}} = \lim _ {x \to 0} \frac {\sin x}{6 x} = \frac {1}{6}.
$$

在求比较复杂的极限时, 人们常常将适当的等价替换和 L'Hôpital 法则相结合来简化计算. 为了说明问题, 我们略带夸张地考虑下面几个例子, 例 7.2.4 用来说明不作等价替换的话计算可能难以实现; 例 7.2.5 用来说明在适当时候作适当的等价替换能极大简化计算; 而例 7.2.6 则用来说明等价替换必须 “适当”.

例7.2.4 求极限 $\lim_{x\to +\infty}\frac{x}{\sqrt{x^2 + 1}}.$

解 显然等价替换 $\sqrt{x^2 + 1} \sim x$ 可以直接给出题目的答案, 极限为 1. 但如果机械地套用 L'Hôpital 法则, 可得

$$
\lim _ {x \to + \infty} \frac {x}{\sqrt {x ^ {2} + 1}} \stackrel {\mathrm{L'Hôpital}} {\underset {\text {法则}} {=}} \lim _ {x \to + \infty} \frac {\sqrt {x ^ {2} + 1}}{x} \stackrel {\mathrm{L'Hôpital}} {\underset {\text {法则}} {=}} \lim _ {x \to + \infty} \frac {x}{\sqrt {x ^ {2} + 1}} = \dots .
$$

例7.2.5 求极限 $\lim_{x\to 0}\left(\frac{1}{\sin^2x} -\frac{1}{x^2}\right)$

解 注意到

$$
\frac {1}{\sin^ {2} x} - \frac {1}{x ^ {2}} = \frac {(x - \sin x) (x + \sin x)}{(\sin x) ^ {2} x ^ {2}},
$$

利用 $\sin x\sim x(x\to 0)$ 以及例7.2.3的结论 $x - \sin x\sim \frac{x^3}{6} (x\to 0)$ ，可得

$$
\lim _ {x \to 0} \left(\frac {1}{\sin^ {2} x} - \frac {1}{x ^ {2}}\right) = \lim _ {x \to 0} \frac {(x ^ {3} / 6) (x + \sin x)}{x ^ {4}} = \frac {1}{3}. \tag {7.2.2}
$$

例 7.2.6 求极限

$$
\lim _ {x \to 0} \frac {1}{x} \Big ((1 + x) ^ {\frac {1}{x}} - \mathrm{e} \Big).
$$

解 根据 L'Hôpital 法则, 可得

$$
\lim _ {x \to 0} \frac {1}{x} ((1 + x) ^ {\frac {1}{x}} - \mathrm{e}) = \lim _ {x \to 0} (1 + x) ^ {\frac {1}{x}} \Big (\frac {- 1}{x ^ {2}} \ln (1 + x) + \frac {1}{x (1 + x)} \Big). \tag {7.2.3}
$$

由于 $(1 + x)^{\frac{1}{x}}\to \mathrm{e}(x\to 0)$ ，从而只需考虑极限

$$
\lim _ {x \to 0} \frac {x - (1 + x) \ln (1 + x)}{x ^ {2} (1 + x)}.
$$

考虑分母上的等价替换 $1 + x \sim 1 (x \to 0)$, 可以计算极限

$$
\lim _ {x \to 0} \frac {x - (1 + x) \ln (1 + x)}{x ^ {2}}.
$$

对此应用 L'Hôpital 法则, 可得

$$
\lim _ {x \to 0} \frac {x - (1 + x) \ln (1 + x)}{x ^ {2}} = \lim _ {x \to 0} \frac {- \ln (1 + x)}{2 x} = - \frac {1}{2}.
$$

这样一来, 原来的极限为  $-\frac{e}{2}$ .

但是, 如果在 (7.2.3)式中对分母上的  $1 + x$  作等价替换  $1 + x \sim 1 (x \rightarrow 0)$ , 即考虑极限

$$
\lim _ {x \to 0} \left(\frac {- \ln (1 + x)}{x ^ {2}} + \frac {1}{x}\right) = \lim _ {x \to 0} \frac {x - \ln (1 + x)}{x ^ {2}}.
$$

再应用 L'Hôpital 法则, 可得原极限为  $\frac{e}{2}$ . 因此, 上述等价替换至少有一种情况的应用是错误的. 请读者思考一下问题所在. □

L'Hôpital 法则的一个直接应用是可以用来证明下面的导数极限定理, 事实上, 只要注意到定理的条件保证了 L'Hôpital 法则可以实施的充分性, 则立得.

定理 7.2.2（导数极限定理）设 $f(x)$ 在点 $x_0$ 的邻域内连续, 在点 $x_0$ 的去心邻域内可导, 且导函数在点 $x_0$ 处的极限存在, 则 $f(x)$ 在点 $x_0$ 处的导数也存在, 并且等于导函数的极限, 即

$$
\lim _ {x \to x _ {0}} \frac {f (x) - f (x _ {0})}{x - x _ {0}} = \lim _ {x \to x _ {0}} f ^ {\prime} (x)
$$

我们也可以从 Lagrange 中值定理出发, 根据极限定义和最基本的性质, 给出下面这个稍显啰唆的证明.

证明 考虑 $x_0$ 的左半邻域 $x < x_0$, 在 $(x, x_0)$ 内应用Lagrange中值定理, 可得

$$
\lim _ {x \to x _ {0} ^ {-}} \frac {f (x) - f (x _ {0})}{x - x _ {0}} = \lim _ {x \to x _ {0} ^ {-}} f ^ {\prime} (\xi) \qquad (x <   \xi <   x _ {0}).
$$

由假设, 极限 $\lim_{x\to x_0^-}f'(x)$ 存在, 设其极限为 $A$, 即 $\forall \varepsilon > 0, \exists \delta > 0$, 当 $0 < x_0 - x < \delta$ 时, 有 $|f'(x) - A| < \varepsilon$. 所以对满足 $0 < x_0 - x < \delta$ 的 $x$, 都有 $0 < x_0 - \xi < \delta$, 从而 $|f'(\xi) - A| < \varepsilon$, 即 $\lim_{x\to x_0^-}f'(\xi) = A$. 即

$$
\lim _ {x \to x _ {0} ^ {-}} \frac {f (x) - f (x _ {0})}{x - x _ {0}} = A
$$

极限存在, 且

$$
\lim _ {x \to x _ {0} ^ {-}} \frac {f (x) - f (x _ {0})}{x - x _ {0}} = \lim _ {x \to x _ {0} ^ {-}} f ^ {\prime} (\xi) = \lim _ {x \to x _ {0} ^ {-}} f ^ {\prime} (x).
$$

同理, 对右导数有类似的讨论. 再由于  $\lim_{x\to x_{0}^{-}}f'(x)=\lim_{x\to x_{0}^{+}}f'(x)$ , 所以

$$
\lim _ {x \to x _ {0} ^ {-}} \frac {f (x) - f (x _ {0})}{x - x _ {0}} = \lim _ {x \to x _ {0} ^ {+}} \frac {f (x) - f (x _ {0})}{x - x _ {0}}.
$$