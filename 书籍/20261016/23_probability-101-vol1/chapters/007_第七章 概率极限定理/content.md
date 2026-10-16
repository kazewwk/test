# 第七章 概率极限定理

原始 PDF 第 190–223 页。

## 第七章

## 概率极限定理

---

176

第七章 概率极限定理

极限定理的研究在概率论中占有重要的地位, 其内容经常是与随机变量列的部分和有关的收敛性质. 本章介绍独立随机变量列的弱大数定律、强大数定律和中心极限定理. 关于中心极限定理, 我们分别给出了基于特征函数和基于斯坦方程的两种方法. 由大数定律可以推出频率的稳定性, 而中心极限定理则说明在很多情况下随机变量的部分和是渐近正态的. 作为中心极限定理的应用, 还讨论了随机事件对的卡方独立性检验.

## 7.1 大数定律

在大量重复的随机试验中, 随机事件出现的频率呈现几乎必然的规律. 更确切地说, 就是在试验条件不变的情况下, 随机事件在多次重复试验中出现的频率近似于它的概率, 偶然中包含着某种必然! 这个规律就是最早的大数定律. 概率论历史上第一个严格描述这个规律的极限定理属于伯努利. 后来的大数定律通常讨论随机变量序列的算术平均值到相应的数学期望的算术平均值的收敛性.

## 7.1.1 大数定律的定义

假设 $\{\xi_n\}$ 为可积的随机变量序列. 为了叙述方便, 我们定义其部分和 $S_{n}$ 与平均部分和 $\bar{S}_{n}$ 如下:

$$
S _ {n} = \sum_ {k = 1} ^ {n} \xi_ {k}, \quad \bar {S} _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} \xi_ {k}. \tag {7.1.1}
$$

定义7.1.1 称序列 $\{\xi_n\}$ 服从（弱）大数定律，是指当 $n\to \infty$ 时有

$$
\bar {S} _ {n} - \mathbf {E} \bar {S} _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} (\xi_ {k} - \mathbf {E} \xi_ {k}) \xrightarrow {\mathrm{P}} 0. \tag {7.1.2}
$$

根据定义, 大数定律是指当 $n \to \infty$ 时平均部分和 $\bar{S}_n$ 与其数学期望有较大偏差的概率会趋近于零. 显然, 序列 $\{\xi_n\}$ 和 $\{\xi_n - \mathbf{E}\xi_n\}$ 同时满足或不满足大数定律.

特别地, 若 $\{\xi_n\}$ 为同分布随机变量序列, 则 (7.1.2) 式等价于

$$
\bar {S} _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} \xi_ {k} \xrightarrow {\mathrm{p}} \mathbf {E} \xi_ {1}. \tag {7.1.3}
$$

## 7.1.2 马尔可夫大数定律

证明 (弱) 大数定律常用的工具是马尔可夫不等式及其如下的特例: 对于任何平方可积随机变量 $\xi$ 及 $\varepsilon > 0$ 有

---

7.1 大数定律

177

$$
\mathbf {P} (| \xi - \mathbf {E} \xi | \geqslant \varepsilon) \leqslant \frac {1}{\varepsilon^ {2}} \mathbf {V a r} \xi . \tag {7.1.4}
$$

上式称为切比雪夫 (Chebyshev) 不等式. 由此易证下面的定理.

定理 7.1.1（马尔可夫大数定律）设  $\{\xi_{n}\}$  为平方可积随机变量序列. 则对于任意的  $\varepsilon > 0$  有

$$
\mathbf {P} \big (| \bar {S} _ {n} - \mathbf {E} \bar {S} _ {n} | \geqslant \varepsilon \big) \leqslant \frac {1}{\varepsilon^ {2}} \mathbf {V a r} (\bar {S} _ {n}) = \frac {1}{n ^ {2} \varepsilon^ {2}} \mathbf {V a r} (S _ {n}).
$$

特别地, 若当 $n \to \infty$ 时有 $\mathbf{Var}(\bar{S}_n) = \mathbf{Var}(S_n)/n^2 \to 0$, 则序列 $\{\xi_n\}$ 满足大数定律 (7.1.2).

推论 7.1.2 (切比雪夫大数定律) 若  $\{\xi_{n}\}$  两两不相关且方差有界, 即有常数  $C \geqslant 0$  使得  $\mathrm{Var}(\xi_{n}) \leqslant C, n = 1, 2, \cdots$ , 则  $\{\xi_{n}\}$  满足大数定律 (7.1.2).

证明 只需注意, 在假设条件下有 $\mathbf{Var}(S_n) = \sum_{k=1}^{n} \mathbf{Var}(\xi_k) \leqslant nC$. 故定理 7.1.1 的条件显然满足. □

推论7.1.3(伯努利大数定律) 假设 $0 < p < 1$. 令 $S_{n}$ 是以 $p$ 为成功概率的伯努利试验前 $n$ 次试验中的成功次数. 则对于任意的 $\varepsilon > 0$ 有

$$
\mathbf {P} \Big (\Big | \frac {S _ {n}}{n} - p \Big | \geqslant \varepsilon \Big) \leqslant \frac {1}{n ^ {2} \varepsilon^ {2}} \mathbf {V a r} (S _ {n}) = \frac {1}{n \varepsilon^ {2}} p (1 - p).
$$

故当  $n \to \infty$  时有  $\bar{S}_{n} := S_{n}/n \xrightarrow{P} p.$

证明 注意 $S_{n} = \sum_{k=1}^{n} \xi_{k}$, 其中 $\xi_{k}$ 表示第 $k$ 次试验中的成功次数. 显然 $\{\xi_{k}\}$ 为独立同分布的随机变量序列且

$$
\mathbf {P} (\xi_ {k} = 1) = p, \quad \mathbf {P} (\xi_ {k} = 0) = 1 - p.
$$

所以

$$
\mathbf {E} (\xi_ {k}) = p, \quad \mathbf {V a r} (\xi_ {k}) = p (1 - p),
$$

进而 $\mathbf{Var}(S_n) = \sum_{k=1}^{n} \mathbf{Var}(\xi_k) = np(1-p)$. 根据推论 7.1.2 即得结论.

例 7.1.1 根据推论 7.1.3, 对于独立重复试验, 当试验次数 n 很大时, 某个随机事件 A 发生的频率与其概率值  $\mathbf{P}(A)$  出现较大偏差的概率很小. 这就基于大数定律给出了频率的稳定性的严格数学解释. 该案例体现了抽象数学理论在认识客观现象和指导实践活动中的作用. 特别地, 在例 1.1.1 的掷硬币试验中, 当投掷次数 n 很大时, 正面出现的频率  $S_{n}/n$  与其概率值 1/2 发生较大偏差的情况很少出现, 与我们的直观经验相吻合.

---

178

第七章 概率极限定理

## 7.1.3 辛钦大数定律

对于独立同分布随机变量序列, 利用特征函数的工具, 只需假定一阶可积性条件, 就可以证明大数定律成立, 也就是辛钦 (Khintchine) 大数定律.

定理 7.1.4（辛钦大数定律） 独立同分布的可积随机变量序列  $\{\xi_{n}\}$  满足大数定律 (7.1.3).

证明 分别用 $f$ 和 $f_{n}$ 表示 $\xi_{1}$ 和 $\bar{S}_n$ 的特征函数. 再记 $a = \mathbf{E}\xi_{1}$. 根据推论5.2.3有 $f'(0) = \mathrm{i}a$. 因为 $\{\xi_n\}$ 是独立同分布的, 我们有

$$
f _ {n} (t) = \mathbf {E} \Big [ \exp \Big \{\sum_ {k = 1} ^ {n} \frac {\mathrm{i} t \xi_ {k}}{n} \Big \} \Big ] = f \Big (\frac {t}{n} \Big) ^ {n}.
$$

所以

$$
\lim _ {n \to \infty} \ln f _ {n} (t) = \lim _ {n \to \infty} n \ln f \Big (\frac {t}{n} \Big) = \lim _ {n \to \infty} n \Big [ f \Big (\frac {t}{n} \Big) - 1 \Big ] = t f ^ {\prime} (0) = \mathrm{i} a t,
$$

故有 $\lim_{n\to \infty}f_n(t) = \mathrm{e}^{\mathrm{i}at}$ 根据连续性定理知 $\bar{S}_n\xrightarrow{\mathrm{w}}a,$ 进而 $\bar{S}_n\xrightarrow{\mathrm{p}}a.$

## 7.1.4 伯恩斯坦多项式

定理7.1.5 设 $f$ 为区间 $[0,1]$ 上的连续函数. 对于整数 $n \geqslant 1$, 记

$$
Q _ {n} (x) = \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} x ^ {k} (1 - x) ^ {n - k} f (k / n), \quad x \in [ 0, 1 ]. \tag {7.1.5}
$$

则当 $n\to \infty$ 时在[0,1]上一致地有 $Q_{n}(x)\rightarrow f(x)$

证明 首先, 注意 $Q_{n}(0) = f(0)$ 和 $Q_{n}(1) = f(1)$. 对于 $0 < x < 1$, 设 $X_{n}$ 是成功概率为 $x$ 的伯努利试验前 $n$ 次试验中的成功的次数, 并记 $\overline{X}_{n} = X_{n} / n$. 由 (7.1.5) 式显然有

$$
Q _ {n} (x) = \mathbf {E} f (X _ {n} / n) = \mathbf {E} f (\overline {{X}} _ {n}).
$$

因为 $f$ 在 $[0,1]$ 上一致连续，对于任意的 $\varepsilon > 0$ ，存在 $\delta > 0$ ，使当 $x, y \in [0,1]$ 满足 $|x - y| < \delta$ 时，有 $|f(x) - f(y)| < \varepsilon$ 。利用全期望公式得

$$
\begin{array}{l} | Q _ {n} (x) - f (x) | \leqslant \mathbf {E} \big [ | f (\overline {{X}} _ {n}) - f (x) | \big ] \\ = \mathbf {P} \big (| \overline {{X}} _ {n} - x | <   \delta \big) \mathbf {E} \big [ | f (\overline {{X}} _ {n}) - f (x) |   | \overline {{X}} _ {n} - x | <   \delta \big ] + \\ \mathbf {P} \big (| \overline {{X}} _ {n} - x | \geqslant \delta \big) \mathbf {E} \big [ | f (\tilde {X} _ {n}) - f (x) |   | \overline {{X}} _ {n} - x | \geqslant \delta \big ] \\ \leqslant \varepsilon \mathbf {P} \big (| \overline {{X}} _ {n} - x | <   \delta \big) + 2 \| f \| \mathbf {P} \big (| \overline {{X}} _ {n} - x | \geqslant \delta \big), \\ \end{array}
$$

---

7.1 大数定律

179

其中 $\| f\| = \sup_{0\leqslant x\leqslant 1}|f(x)|$ .再根据推论7.1.3有

$$
\sup _ {0 \leqslant x \leqslant 1} | Q _ {n} (x) - f (x) | \leqslant \varepsilon + \frac {2 \| f \|}{n \delta^ {2}},
$$

故得欲证结果.

根据著名的魏尔斯特拉斯 (Karl Weierstrass) 逼近定理, 有界闭区间上的连续函数可以用多项式序列一致地逼近. 定理 7.1.5 给出了上述多项式逼近序列的具体构造, 大数定律的方法在证明中起了关键作用. 由 (7.1.5) 式定义的多项式 $Q_{n}, n \geqslant 1$ 称为函数 $f$ 的伯恩斯坦 (Bernstein) 多项式.

## 练习题

1. 设随机变量 $\xi$ 满足 $\mathbf{E}\xi = 0$ 和 $\sigma^2 := \operatorname{Var}\xi < \infty$. 证明对任何 $\lambda > 0$, 有单边切比雪夫不等式

$$
\mathbf {P} (\xi \geqslant \lambda) \leqslant \frac {\sigma^ {2}}{\sigma^ {2} + \lambda^ {2}}
$$

成立.

提示: 对任意的 u > 0 有

$$
\mathbf {P} (\xi \geqslant \lambda) \leqslant \mathbf {P} \{(\xi + u) ^ {2} \geqslant (\lambda + u) ^ {2} \} \leqslant \frac {\mathbf {E} [ (\xi + u) ^ {2} ]}{(\lambda + u) ^ {2}} = \frac {\sigma^ {2} + u ^ {2}}{(\lambda + u) ^ {2}}.
$$

取 $u = \sigma^2 /\lambda$ 最小化右端即得欲证结果.

2. 设 $\{\xi_n\}$ 是独立随机变量序列, 且 $\operatorname{Var}(\xi_n)/n \to 0$. 证明 $\{\xi_n\}$ 服从大数定律. 提示:

$$
\lim _ {n \to \infty} \mathbf {V a r} \Big (\frac {1}{n} \sum_ {k = 1} ^ {n} \xi_ {k} \Big) = \lim _ {n \to \infty} \frac {1}{n ^ {2}} \sum_ {k = 1} ^ {n} \mathbf {V a r} (\xi_ {k}) = 0.
$$

3. 设 $\{\xi_n\}$ 是平方可积的同分布随机变量序列. 证明: 若当 $|n - k| \geqslant 2$ 时 $\xi_n$ 与 $\xi_k$ 独立, 则 $\{\xi_n\}$ 满足大数定律.

4. 设  $\{\xi_{n}\}$  是平方可积的独立同分布随机变量序列. 证明: 当  $n \to \infty$  时有

$$
Z _ {n} := \frac {2}{n (n + 1)} \sum_ {k = 1} ^ {n} k \xi_ {k} \xrightarrow {\mathrm{p}} \mathbf {E} \xi_ {1}.
$$

5. 设  $\{\xi_{n}\}$  是平方可积的独立随机变量序列, 且满足

$$
\sum_ {k = 1} ^ {\infty} \frac {\mathbf {V a r} (\xi_ {k})}{k ^ {2}} <   \infty ,
$$

证明  $\{\xi_{n}\}$  满足大数定律.

---

180

第七章 概率极限定理

## 7.2 强大数定律

考虑可积的随机变量序列  $\{\xi_{n}\}$ ，并用  $S_{n}$  和  $\bar{S}_{n}$  分别表示其部分和与平均部分和，即

$$
S _ {n} = \sum_ {k = 1} ^ {n} \xi_ {k}, \quad \bar {S} _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} \xi_ {k}. \tag {7.2.1}
$$

定义 7.2.1 称序列  $\{\xi_{n}\}$  服从强大数定律, 是指当  $n \to \infty$  时有

$$
\bar {S} _ {n} - \mathbf {E} \bar {S} _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} (\xi_ {k} - \mathbf {E} \xi_ {k}) \stackrel {\mathrm{a.s.}} {\rightarrow} 0. \tag {7.2.2}
$$

根据这个定义, 强大数定律是指当 $n \to \infty$ 时平均部分和 $\bar{S}_n$ 与其数学期望之差几乎必然趋近于零. 因此强大数定律的结论比 (弱) 大数定律的要强. 显然, 序列 $\{\xi_n\}$ 和 $\{\xi_n - \mathbf{E}\xi_n\}$ 同时满足或不满足强大数定律.

特别地, 若 $\{\xi_n\}$ 为同分布随机变量序列, 则 (7.2.2) 式等价于

$$
\bar {S} _ {n} = \frac {1}{n} \sum_ {k = 1} ^ {n} \xi_ {k} \stackrel {\text {a.s.}} {\rightarrow} \mathbf {E} \xi_ {1}. \tag {7.2.3}
$$

## 7.2.1 许-罗宾斯大数定律

定理 7.2.1（许 罗宾斯大数定律） 设  $\{\xi_{n}\}$  为独立同分布平方可积随机变量序列. 则  $\bar{S}_{n} \stackrel{c}{\rightarrow} E\xi_{1}$ ，进而强大数定律 (7.2.3) 成立.

证明 不失一般性, 我们可以假设 $\mathbf{E}\xi_{1}=0$。固定 $n\geqslant 1$。对于 $1\leqslant k\leqslant n$, 记 $\zeta_{n,k}=\xi_{k}1_{\{|\xi_{k}|\leqslant n\}}$。再令 $T_{n}=\sum_{k=1}^{n}\zeta_{n,k}$。则有

$$
\mathbf {P} (| \bar {S} _ {n} | \geqslant \varepsilon) \leqslant \mathbf {P} (| T _ {n} | \geqslant n \varepsilon) + \mathbf {P} \Big (\max _ {1 \leqslant k \leqslant n} | \xi_ {k} | > n \Big).
$$

因 $\{\xi_n\}$ 同分布, 有

$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} \mathbf {P} \Big (\max _ {1 \leqslant k \leqslant n} | \xi_ {k} | > n \Big) \leqslant \sum_ {n = 1} ^ {\infty} \sum_ {k = 1} ^ {n} \mathbf {P} (| \xi_ {k} | > n) = \sum_ {n = 1} ^ {\infty} n \mathbf {P} (| \xi_ {1} | > n) \\ = \sum_ {n = 1} ^ {\infty} \sum_ {k = n} ^ {\infty} n \mathbf {P} (k <   | \xi_ {1} | \leqslant k + 1) \\ \end{array}
$$

---

7.2 强大数定律

181

$$
\begin{array}{l} \leqslant \sum_ {k = 1} ^ {\infty} \sum_ {n = 1} ^ {k} n \mathbf {P} (k <   | \xi_ {1} | \leqslant k + 1) \\ \leqslant \sum_ {k = 1} ^ {\infty} k ^ {2} \mathbf {P} (k <   | \xi_ {1} | \leqslant k + 1) \leqslant \mathbf {E} (\xi_ {1} ^ {2}) <   \infty . \\ \end{array}
$$

由控制收敛定理易知, 当 $n \to \infty$ 时有 $\mathbf{E}(T_n / n) = \mathbf{E}(\xi_1 1_{\{|\xi_1| \leqslant n\}}) \to \mathbf{E}\xi_1 = 0$. 对任意的 $\varepsilon > 0$, 可取 $n_0 \geqslant 1$ 使当 $n \geqslant n_0$ 时有 $|\mathbf{E}T_n| \leqslant n\varepsilon / 2$. 应用马尔可夫不等式, 此时有

$$
\begin{array}{l} \mathbf {P} (| T _ {n} | \geqslant n \varepsilon) \leqslant \mathbf {P} \Big (| T _ {n} - \mathbf {E} T _ {n} | \geqslant \frac {n \varepsilon}{2} \Big) \leqslant \frac {1 6}{(n \varepsilon) ^ {4}} \mathbf {E} \big [ (T _ {n} - \mathbf {E} T _ {n}) ^ {4} \big ] \\ = \frac {1 6}{(n \varepsilon) ^ {4}} \mathbf {E} \left\{\left[ \sum_ {k = 1} ^ {n} (\zeta_ {n, k} - \mathbf {E} \zeta_ {n, k}) \right] ^ {4} \right\} \\ = \frac {1 6}{(n \varepsilon) ^ {4}} \left\{\sum_ {j \neq k} \mathbf {E} \left[ (\zeta_ {n, j} - \mathbf {E} \zeta_ {n, j}) ^ {2} (\zeta_ {n, k} - \mathbf {E} \zeta_ {n, k}) ^ {2} \right] \right] + \\ \sum_ {k = 1} ^ {n} \mathbf {E} \big [ (\zeta_ {n, k} - \mathbf {E} \zeta_ {n, k}) ^ {4} \big ] \Big \} \\ \leqslant \frac {1 6}{(n \varepsilon) ^ {4}} \left\{n ^ {2} (\mathbf {V a r} \zeta_ {n, 1}) ^ {2} + n \mathbf {E} \left[ (\zeta_ {n, 1} - \mathbf {E} \zeta_ {n, 1}) ^ {4} \right] \right\}, \\ \end{array}
$$

其中

$$
\mathbf {V a r} \zeta_ {n, 1} \leqslant \mathbf {E} (\zeta_ {n, 1} ^ {2}) + (\mathbf {E} \zeta_ {n, 1}) ^ {2} \leqslant \mathbf {E} (\xi_ {1} ^ {2}) + (\mathbf {E} | \xi_ {1} |) ^ {2},
$$

而

$$
\mathbf {E} \big [ (\zeta_ {n, 1} - \mathbf {E} \zeta_ {n, 1}) ^ {4} \big ] \leqslant 8 \mathbf {E} \big [ \zeta_ {n, 1} ^ {4} + (\mathbf {E} \zeta_ {n, 1}) ^ {4} \big ] \leqslant 8 \big [ \mathbf {E} (\zeta_ {n, 1} ^ {4}) + (\mathbf {E} | \xi_ {1} |) ^ {4} \big ].
$$

注意

$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} \frac {1}{n ^ {3}} \mathbf {E} (\zeta_ {n, 1} ^ {4}) \leqslant \sum_ {n = 1} ^ {\infty} \sum_ {k = 1} ^ {n} \frac {k ^ {4}}{n ^ {3}} \mathbf {P} (k - 1 <   | \xi_ {1} | \leqslant k) \\ \leqslant \sum_ {k = 1} ^ {\infty} k ^ {4} \mathbf {P} (k - 1 <   | \xi_ {1} | \leqslant k) \sum_ {n = k} ^ {\infty} \frac {1}{n ^ {3}} \\ \leqslant \sum_ {k = 1} ^ {\infty} k ^ {4} \mathbf {P} (k - 1 <   | \xi_ {1} | \leqslant k) \left(\frac {1}{k ^ {3}} + \frac {1}{k ^ {2}}\right) \\ \leqslant 2 \sum_ {k = 1} ^ {\infty} k ^ {2} \mathbf {P} (k - 1 <   | \xi_ {1} | \leqslant k) \\ \leqslant 4 \sum_ {k = 1} ^ {\infty} [ (k - 1) ^ {2} + 1 ] \mathbf {P} (k - 1 <   | \xi_ {1} | \leqslant k) \\ \end{array}
$$

---

182

第七章 概率极限定理

$$
\leqslant 4 \big [ \mathbf {E} (\xi_ {1} ^ {2}) + 1 \big ] <   \infty .
$$

由上面的估计易得

$$
\sum_ {n = 1} ^ {\infty} \mathbf {P} (| \bar {S} _ {n} | \geqslant \varepsilon) <   \infty ,
$$

即有  $\bar{S}_{n} \stackrel{c}{\rightarrow} 0$ . 再根据定理 6.1.2 强大数定律 (7.2.3) 成立.

推论 7.2.2 (博雷尔强大数定律) 若  $\{\xi_{n}\}$  为独立同分布随机变量序列且  $\mathbf{E}(\xi_{1}^{4}) < \infty$ ，则  $\bar{S}_{n} \stackrel{a.s.}{\rightarrow} E\xi_{1}$ .

推论7.2.3 设 $X_{n}$ 为有成功概率 $p(0 < p < 1)$ 的可数重伯努利试验前 $n$ 次试验中的成功次数. 则当 $n \to \infty$ 时有 $X_{n} / n \xrightarrow{\mathrm{a.s.}} p$.

证明 注意 $X_{n} = \sum_{k=1}^{n} \xi_{k}$, 其中 $\xi_{k}$ 表示第 $k$ 次试验中的成功次数. 根据博雷尔强大数定律即得结论. □

例 7.2.1 根据推论 7.2.3, 对于独立重复试验, 当试验次数 n 趋于无穷时, 某个随机事件 A 发生的频率几乎必然收敛到其概率值  $\mathbf{P}(A)$ . 这就从强大数定律的角度解释了频率的稳定性, 深化了我们在例 7.1.1 对于该现象的基于弱大数定律的解释.

## 7.2.2 柯尔莫哥洛夫 0-1 律

给定随机变量序列 $\{\xi_n\}$, 写 $\mathcal{T}_n = \sigma (\xi_{n + k}:k\geqslant 1)$. 我们称 $\mathcal{T}_{\infty}:= \bigcap_{n\geqslant 1}\mathcal{T}_n$ 为 $\{\xi_n\}$ 的尾 $\sigma$ 代数, 而称 $\mathcal{T}_{\infty}$ 中的事件为 $\{\xi_n\}$ 的尾事件.

定理7.2.4（柯尔莫哥洛夫0-1律） 设 $\{\xi_n\}$ 为独立随机变量序列. 则对任何尾事件 $A \in \mathcal{T}_{\infty}$ 有 $\mathbf{P}(A) = 0$ 或1.

证明 对 $n \geqslant 1$ 记 $\mathcal{A}_n = \bigcup_{k=1}^{n} \sigma(\xi_k)$ 和 $\mathcal{C}_n = \bigcup_{k=1}^{\infty} \sigma(\xi_{n+k})$. 易知 $\mathcal{A}_n$ 和 $\mathcal{C}_n$ 均对交运算封闭. 根据假设 $\mathcal{A}_n$ 和 $\mathcal{C}_n$ 独立. 由命题 1.4.2 知 $\mathcal{F}_n = \sigma(\mathcal{A}_n)$ 和 $\mathcal{T}_n = \sigma(\mathcal{C}_n)$ 独立, 故 $\mathcal{F}_n$ 和 $\mathcal{T}_{\infty}$ 独立, 进而 $\bigcup_{n=1}^{\infty} \mathcal{F}_n$ 和 $\mathcal{T}_{\infty}$ 独立. 再次应用由命题 1.4.2 知 $\mathcal{F}_{\infty} := \sigma\left(\bigcup_{n=1}^{\infty} \mathcal{F}_n\right)$ 和 $\mathcal{T}_{\infty}$ 独立, 故 $\mathcal{T}_{\infty} \subseteq \mathcal{F}_{\infty}$ 与自身独立. 因此对 $A \in \mathcal{T}_{\infty}$ 有 $\mathbf{P}(A) = \mathbf{P}(AA) = \mathbf{P}(A)^2$, 故 $\mathbf{P}(A) = 0$ 或 1.

下面定理的结论称为独立同分布随机变量序列的加西亚 (Garsia) 极大不等式.

定理7.2.5 设 $\{\xi_n\}$ 为可积独立同分布随机变量序列. 令 $S_{n} = \sum_{k=1}^{n} \xi_{k}$. 则有

$$
\mathbf {E} \Big (\xi_ {1}; \sup _ {n \geqslant 1} S _ {n} > 0 \Big) \geqslant 0. \tag {7.2.4}
$$

---

7.2 强大数定律

183

证明 首先, 注意对任意的 $x, c \in \mathbb{R}$ 易证下面的不等式:

$$
0 \vee x - 0 \vee (x - c) \leqslant c 1 _ {\{x > 0 \}}. \tag {7.2.5}
$$

写 $M_{n} = S_{1}\vee S_{2}\vee \dots \vee S_{n}$ 和 $N_{n} = (S_{2} - \xi_{1})\vee \dots \vee (S_{n} - \xi_{1})\vee (S_{n + 1} - \xi_{1})$ .则

$$
\begin{array}{l} M _ {n} - \xi_ {1} = 0 \vee (S _ {2} - \xi_ {1}) \vee \dots \vee (S _ {n} - \xi_ {1}) \\ \leqslant 0 \vee \left(S _ {2} - \xi_ {1}\right) \vee \dots \vee \left(S _ {n} - \xi_ {1}\right) \vee \left(S _ {n + 1} - \xi_ {1}\right) \\ = 0 \lor N _ {n}. \\ \end{array}
$$

这样, 对于 $x = M_{n}$ 和 $c = \xi_{1}$ 应用 (7.2.5) 式得

$$
0 \vee M _ {n} - 0 \vee N _ {n} \leqslant 0 \vee M _ {n} - 0 \vee (M _ {n} - \xi_ {1}) \leqslant \xi_ {1} 1 _ {\{M _ {n} > 0 \}}.
$$

因 $N_{n}$ 和 $M_{n}$ 同分布, 在上式两端取期望得 $\mathbf{E}(\xi_1 1_{\{M_n > 0\}}) \geqslant 0$. 再令 $n \to \infty$, 并应用控制收敛定理即得 (7.2.4)式.

## 7.2.3 柯尔莫哥洛夫强大数定律

定理 7.2.6（柯尔莫哥洛夫强大数定律） 可积的独立同分布随机变量序列  $\{\xi_{n}\}$  满足强大数定律 (7.2.3).

证明 不妨假设 $\mathbf{E}\xi_1 = 0$。令 $S_{n} = \sum_{k=1}^{n} \xi_{k}$。任取 $\varepsilon > 0$ 并对序列 $\{\xi_n - \varepsilon\}$ 应用加西亚极大不等式得

$$
\mathbf {E} \Big (\xi_ {1} - \varepsilon ; \sup _ {n \geqslant 1} S _ {n} / n > \varepsilon \Big) \geqslant 0. \tag {7.2.6}
$$

显然 $\{\limsup_{n\to \infty}S_n / n > \varepsilon \}$ 是 $\{\xi_n - \varepsilon \}$ 的尾事件.根据柯尔莫哥洛夫0-1律有

$$
\mathbf {P} \Big (\limsup _ {n \to \infty} S _ {n} / n > \varepsilon \Big) = 0 \text {或} 1.
$$

若上述概率为1, 即 $\mathbf{P}(\sup_{n\geqslant 1}S_n / n > \varepsilon) = 1$, 则由(7.2.6)式推出错误的结论 $\mathbf{E}(\xi_1 - \varepsilon)\geqslant 0$. 所以必有

$$
\mathbf {P} \Big (\limsup _ {n \to \infty} S _ {n} / n > \varepsilon \Big) = 0.
$$

对序列 $\{-\xi_n\}$ 应用上面的推导得

$$
\mathrm{P} \Big (\liminf _ {n \to \infty} S _ {n} / n <   - \varepsilon \Big) = 0.
$$

再由  $\varepsilon > 0$  的任意性, 综合以上二式有  $\mathbf{P}(\lim_{n \to \infty} S_n / n = 0) = 1$ .

---

184

第七章 概率极限定理

## 练习题

1. 利用马尔可夫不等式直接证明博雷尔强大数定律.

2. 设 $\{\xi_n\}$ 为独立同分布随机变量序列, 且均服从均匀分布 $U(0,1)$. 问当 $(0,1)$ 上的博雷尔可测函数 $f$ 满足什么条件时序列 $\{f(\xi_n)\}$ 满足强大数定律?

3. 设随机变量  $\xi_{1}, \xi_{2}, \cdots$  独立且均服从均匀分布  $U(0,1)$ . 证明: 当  $n \to \infty$  时有

$$
X _ {n} := \left(\prod_ {k = 1} ^ {n} \xi_ {k}\right) ^ {1 / n} \xrightarrow {\text {a.s.}} \frac {1}{\mathrm{e}}.
$$

4. 设 $f, g$ 为区间 $[0,1]$ 上的连续函数, 且 $f$ 不恒为零. 再设有常数 $c \geqslant 0$ 使得 $g \leqslant cf$. 证明: 当 $n \to \infty$ 时有

$$
\int_ {0} ^ {1} \mathrm{d} x _ {1} \dots \int_ {0} ^ {1} \frac {g (x _ {1}) + g (x _ {2}) + \cdots + g (x _ {n})}{f (x _ {1}) + f (x _ {2}) + \cdots + f (x _ {n})} \mathrm{d} x _ {n} \rightarrow \int_ {0} ^ {1} g (x) \mathrm{d} x \Big (\int_ {0} ^ {1} f (x) \mathrm{d} x \Big) ^ {- 1}.
$$

## 7.3 中心极限定理

中心极限定理是讨论随机变量序列的标准化部分和的分布渐近于正态分布的定理, 它们以严格的数学形式阐明, 大样本的标准化部分和总是近似地服从正态分布. 历史上最早的中心极限定理是棣莫弗和拉普拉斯针对伯努利试验证明的. 这类定理是数理统计学和误差分析的理论基础.

## 7.3.1 定理的一般形式

定义 7.3.1 考虑平方可积的随机变量序列  $\{\xi_{n}\}$ . 用  $S_{n}$  表示其部分和, 即

$$
S _ {n} = \sum_ {k = 1} ^ {n} \xi_ {k}.
$$

设对每个 $n \geqslant 1$ 有 $\operatorname{Var} S_n > 0$. 定义标准化部分和 $S_n^*$ 如下:

$$
S _ {n} ^ {*} = \frac {S _ {n} - \mathbf {E} S _ {n}}{\sqrt {\mathbf {V a r} S _ {n}}} = \frac {1}{\sqrt {\mathbf {V a r} S _ {n}}} \sum_ {k = 1} ^ {n} (\xi_ {k} - \mathbf {E} \xi_ {k}). \tag {7.3.1}
$$

称序列 $\{\xi_n\}$ 满足中心极限定理, 是指当 $n \to \infty$ 时 $S_n^*$ 的分布函数弱收敛到标准正态分布 $N(0,1)$ 的分布函数, 即有

$$
\mathbf {P} (S _ {n} ^ {*} \leqslant x) \to \varPhi (x) := \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {x} \mathrm{e} ^ {- u ^ {2} / 2} \mathrm{d} u, \quad x \in \mathbb {R}. \tag {7.3.2}
$$

---

7.3 中心极限定理

185

在后面的两个小节, 我们将用两种不同的方法, 针对独立同分布的随机变量序列  $\{\xi_{n}\}$ , 分别建立上述中心极限定理.

例 7.3.1 设  $\xi_{1}$  为平方可积的非退化随机变量, 而对  $n \geqslant 2$  有  $\xi_{n} = 0$ . 则对任何  $n \geqslant 1$  有

$$
S _ {n} ^ {*} = \frac {\xi_ {1} - \mathbf {E} \xi_ {1}}{\sqrt {\mathbf {V a r} \xi_ {1}}} = \xi_ {1} ^ {*}.
$$

显然, 只有当 $\xi_{1}$ 服从正态分布时, 序列 $\{\xi_{n}\}$ 满足中心极限定理. 由此可见, 为保证中心极限定理成立, 我们需要对 $\{\xi_{n}\}$ 的分布作适当的假定.

## 7.3.2 特征函数方法

考虑平方可积的非退化独立同分布随机变量序列 $\{\xi_n\}$, 记 $a = \mathbf{E}\xi_1$ 和 $\sigma^2 = \mathbf{Var}\xi_1 > 0$. 此时有

$$
S _ {n} ^ {*} = \frac {S _ {n} - \mathbf {E} S _ {n}}{\sqrt {\mathbf {V a r} S _ {n}}} = \frac {1}{\sigma \sqrt {n}} \sum_ {k = 1} ^ {n} (\xi_ {k} - a). \tag {7.3.3}
$$

对于这种情况, 林德伯格 (Lindeberg) 在前人工作的基础上建立了下面的林德伯格中心极限定理.

引理 7.3.1 设  $x_{k}$  和  $y_{k}, k=1,2,\cdots,n$  为模不超过 1 的复数. 则有

$$
\Big | \prod_ {k = 1} ^ {n} x _ {k} - \prod_ {k = 1} ^ {n} y _ {k} \Big | \leqslant \sum_ {k = 1} ^ {n} | x _ {k} - y _ {k} |.
$$

证明 当 $n = 1$ 时结果显然. 对于 $n = 2$ 有

$$
\begin{array}{l} \left| x _ {1} x _ {2} - y _ {1} y _ {2} \right| = \left| x _ {1} x _ {2} - y _ {1} x _ {2} + y _ {1} x _ {2} - y _ {1} y _ {2} \right| \\ \leqslant | x _ {1} - y _ {1} | | x _ {2} | + | y _ {1} | | x _ {2} - y _ {2} | \\ \leqslant | x _ {1} - y _ {1} | + | x _ {2} - y _ {2} |. \\ \end{array}
$$

一般情况可由数学归纳法得到.

定理 7.3.2（林德伯格） 平方可积的非退化独立同分布随机变量序列  $\{\xi_{n}\}$  满足中心极限定理 (7.3.2).

证明 用 $f$ 表示标准化随机变量 $\xi_{n}^{*} := (\xi_{n} - a) / \sigma$ 的特征函数, 注意它并不依赖于 $n \geqslant 1$. 另外, 易知 $S_{n}^{*}$ 的特征函数 $f_{n}$ 为

$$
f _ {n} (t) = \mathbf {E} \Big [ \exp \Big \{\sum_ {k = 1} ^ {n} \frac {\mathrm{i} t \xi_ {k} ^ {*}}{\sqrt {n}} \Big \} \Big ]
$$

---

186

第七章 概率极限定理

$$
= \prod_ {k = 1} ^ {n} \mathbf {E} \left[ \exp \left\{\frac {\mathrm{i} t \xi_ {k} ^ {*}}{\sqrt {n}} \right\} \right] = f \left(\frac {t}{\sqrt {n}}\right) ^ {n}.
$$

根据定理5.2.2有

$$
\begin{array}{l} \left| f \left(\frac {t}{\sqrt {n}}\right) - \left(1 - \frac {t ^ {2}}{2 n}\right) \right| \leqslant \mathbf {E} \left[ \left(\frac {\left| t \xi_ {1} ^ {*} \right| ^ {2}}{n}\right) \wedge \left(\frac {\left| t \xi_ {1} ^ {*} \right| ^ {3}}{6 n ^ {3 / 2}}\right) \right] \\ = \frac {1}{n} \mathbf {E} \left[ \left(| t \xi_ {1} ^ {*} | ^ {2}\right) \wedge \left(\frac {| t \xi_ {1} ^ {*} | ^ {3}}{6 \sqrt {n}}\right) \right]. \\ \end{array}
$$

再由引理7.3.1得到

$$
\Big | f \Big (\frac {t}{\sqrt {n}} \Big) ^ {n} - \Big (1 - \frac {t ^ {2}}{2 n} \Big) ^ {n} \Big | \leqslant \mathbf {E} \Big [ \big (| t \xi_ {1} ^ {*} | ^ {2} \big) \wedge \Big (\frac {| t \xi_ {1} ^ {*} | ^ {3}}{6 \sqrt {n}} \Big) \Big ].
$$

应用定理4.2.20可知当 $n\to \infty$ 时上式右端趋于零.所以

$$
\lim _ {n \to \infty} f _ {n} (t) = \lim _ {n \to \infty} f \left(\frac {t}{\sqrt {n}}\right) ^ {n} = \lim _ {n \to \infty} \left(1 - \frac {t ^ {2}}{2 n}\right) ^ {n} = \mathrm{e} ^ {- t ^ {2} / 2}.
$$

再根据连续性定理即得欲证结果.

推论 7.3.3 (棣莫弗-拉普拉斯) 设  $X_{n}$  服从二项分布  $B(n,p)$ ，其中 0 < p < 1.
则

$$
\lim _ {n \to \infty} \mathbf {P} \Big (\frac {X _ {n} - n p}{\sqrt {n p q}} <   x \Big) = \varPhi (x) := \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {x} \mathrm{e} ^ {- u ^ {2} / 2} \mathrm{d} u, \quad x \in \mathbb {R}.
$$

证明 由熟知的结论 $X_{n} \stackrel{\mathrm{d}}{=} \sum_{k=1}^{n} \xi_{k}$, 其中 $\{\xi_{k}\}$ 是独立同分布随机变量序列且服从伯努利分布 $B(1, p)$. 再由定理7.3.2即得推论结果. □

例 7.3.2 利用中心极限定理, 可以给出了频率稳定性的另外一个解释. 注意  $X_{n}$  与伯努利试验前 n 次试验中成功的次数同分布. 根据该定理, 当 n 很大时, 标准化随机变量

$$
X _ {n} ^ {*} = \frac {X _ {n} - n p}{\sqrt {n p q}}
$$

的分布渐近于标准正态分布. 注意

$$
\frac {X _ {n}}{n} - p = \frac {X _ {n} - n p}{n} = \frac {\sqrt {p q} X _ {n} ^ {*}}{\sqrt {n}}.
$$

根据棣莫弗-拉普拉斯中心极限定理, 当 $n$ 很大时 $X_{n}^{*}$ 是近似地服从标准正态分布的随机变量. 因此, 上式说明当 $n \to \infty$ 时, 伯努利试验中前 $n$ 次成功的频率 $X_{n} / n$ 与成功概率 $p$ 之间的误差以 $1 / \sqrt{n}$ 的阶数趋近于零. 这个解释显然比大数定律的解释更为精确!

---

7.3 中心极限定理

187

## 7.3.3 斯坦方法

利用斯坦方法, 可以证明林德伯格中心极限定理的一个加强的版本. 用 $\phi$ 表示标准正态分布 $N(0,1)$ 的密度函数. 设 $Z$ 是以 $N(0,1)$ 为分布的随机变量. 考虑关于有界可测函数 $h$ 的斯坦方程

$$
f ^ {\prime} (x) - x f (x) = h (x) - \mathbf {E} h (Z). \tag {7.3.4}
$$

我们知道, 该方程有特解

$$
f (x) = \frac {1}{\phi (x)} \int_ {- \infty} ^ {x} [ h (y) - \mathbf {E} h (Z) ] \phi (y) \mathrm{d} y. \tag {7.3.5}
$$

命题7.3.4 设函数 $h$ 绝对连续且有有界的密度 $h'$. 则特解(7.3.5)可以表示为

$$
\begin{array}{l} f (x) = - \frac {1}{\phi (x)} \Big [ \mathbf {P} (Z \geqslant x) \int_ {- \infty} ^ {x} h ^ {\prime} (u) \mathbf {P} (Z \leqslant u) \mathrm{d} u + \\ \mathbf {P} (Z \leqslant x) \int_ {x} ^ {\infty} h ^ {\prime} (u) \mathbf {P} (Z \geqslant u) \mathrm{d} u ]. \tag {7.3.6} \\ \end{array}
$$

证明 根据 (7.3.5) 式有

$$
\begin{array}{l} f (x) = \frac {1}{\phi (x)} \Big [ \int_ {- \infty} ^ {x} h (y) \phi (y) \mathrm{d} y - \mathbf {E} h (Z) \Big ] \int_ {- \infty} ^ {x} \phi (y) \mathrm{d} y \\ = \frac {1}{\phi (x)} \Big [ \int_ {- \infty} ^ {x} h (y) \phi (y) \mathrm{d} y - \mathbf {P} (Z \leqslant x) \int_ {- \infty} ^ {\infty} h (y) \phi (y) \mathrm{d} y \Big ] \\ = \frac {1}{\phi (x)} \Big [ \int_ {- \infty} ^ {x} h (y) \phi (y) \mathrm{d} y - \mathbf {P} (Z \leqslant x) \int_ {- \infty} ^ {x} h (y) \phi (y) \mathrm{d} y - \\ \mathbf {P} (Z \leqslant x) \int_ {x} ^ {\infty} h (y) \phi (y) \mathrm{d} y \bigg ] \\ = \frac {1}{\phi (x)} \Big [ \mathbf {P} (Z \geqslant x) \int_ {- \infty} ^ {x} h (y) \phi (y) \mathrm{d} y - \mathbf {P} (Z \leqslant x) \int_ {x} ^ {\infty} h (y) \phi (y) \mathrm{d} y \Big ]. \tag {7.3.7} \\ \end{array}
$$

注意

$$
\begin{array}{l} \int_ {- \infty} ^ {x} h (y) \phi (y) \mathrm{d} y = \int_ {- \infty} ^ {x} h (x) \phi (y) \mathrm{d} y - \int_ {- \infty} ^ {x} [ h (x) - h (y) ] \phi (y) \mathrm{d} y \\ = h (x) \mathbf {P} (Z \leqslant x) - \int_ {- \infty} ^ {x} \phi (y) \mathrm{d} y \int_ {y} ^ {x} h ^ {\prime} (u) \mathrm{d} u \\ = h (x) \mathbf {P} (Z \leqslant x) - \int_ {- \infty} ^ {x} h ^ {\prime} (u) \mathrm{d} u \int_ {- \infty} ^ {u} \phi (y) \mathrm{d} y \\ = h (x) \mathbf {P} (Z \leqslant x) - \int_ {- \infty} ^ {x} h ^ {\prime} (u) \mathbf {P} (Z \leqslant u) \mathrm{d} u. \\ \end{array}
$$

类似地可得

$$
\int_ {x} ^ {\infty} h (y) \phi (y) \mathrm{d} y = h (x) \mathbf {P} (Z \geqslant x) + \int_ {x} ^ {\infty} h ^ {\prime} (u) \mathbf {P} (Z \geqslant u) \mathrm{d} u.
$$

将上面两个表达式代入 (7.3.7) 式并整理即得 (7.3.6) 式.

---

188

第七章 概率极限定理

命题7.3.5 若函数 $h$ 绝对连续且有有界的密度 $h'$，则特解(7.3.5)满足 $\| f''\| \leqslant 2 \| h' \|$.

证明 在假设条件下, 对斯坦方程 (7.3.4) 两端求导数, 并再次应用该方程可得

$$
f ^ {\prime \prime} (x) = h ^ {\prime} (x) + (1 + x ^ {2}) f (x) + x [ h (x) - \mathbf {E} h (Z) ]. \tag {7.3.8}
$$

注意

$$
\begin{array}{l} h (x) - \mathbf {E} h (Z) = \int_ {- \infty} ^ {\infty} [ h (x) - h (y) ] \phi (y) \mathrm{d} y \\ = \int_ {- \infty} ^ {x} \phi (y) \mathrm{d} y \int_ {y} ^ {x} h ^ {\prime} (u) \mathrm{d} u - \int_ {x} ^ {\infty} \phi (y) \mathrm{d} y \int_ {x} ^ {y} h ^ {\prime} (u) \mathrm{d} u \\ = \int_ {- \infty} ^ {x} h ^ {\prime} (u) \mathrm{d} u \int_ {- \infty} ^ {u} \phi (y) \mathrm{d} y - \int_ {x} ^ {\infty} h ^ {\prime} (u) \mathrm{d} u \int_ {u} ^ {\infty} \phi (y) \mathrm{d} y \\ = \int_ {- \infty} ^ {x} h ^ {\prime} (u) \mathbf {P} (Z \leqslant u) \mathrm{d} u - \int_ {x} ^ {\infty} h ^ {\prime} (u) \mathbf {P} (Z \geqslant u) \mathrm{d} u. \\ \end{array}
$$

将上式和 (7.3.6) 式代入 (7.3.8) 式得

$$
f ^ {\prime \prime} (x) = h ^ {\prime} (x) - \left[ (1 + x ^ {2}) \frac {\mathbf {P} (Z \geqslant x)}{\phi (x)} - x \right] \int_ {- \infty} ^ {x} h ^ {\prime} (u) \mathbf {P} (Z \leqslant u) \mathrm{d} u -
$$

$$
\left[ x + (1 + x ^ {2}) \frac {\mathbf {P} (Z \leqslant x)}{\phi (x)} \right] \int_ {x} ^ {\infty} h ^ {\prime} (u) \mathbf {P} (Z \geqslant u) \mathrm{d} u.
$$

根据例2.3.3有

$$
(1 + x ^ {2}) \frac {\mathbf {P} (Z \geqslant x)}{\phi (x)} - x \geqslant 0.
$$

所以

$$
\begin{array}{l} | f ^ {\prime \prime} (x) | \leqslant | h ^ {\prime} (x) | + \left[ (1 + x ^ {2}) \frac {\mathbf {P} (Z \geqslant x)}{\phi (x)} - x \right] \int_ {- \infty} ^ {x} | h ^ {\prime} (u) | \mathbf {P} (Z \leqslant u) \mathrm{d} u + \\ \left[ x + (1 + x ^ {2}) \frac {\mathbf {P} (Z \leqslant x)}{\phi (x)} \right] \int_ {x} ^ {\infty} | h ^ {\prime} (u) | \mathbf {P} (Z \geqslant u) \mathrm{d} u, \tag {7.3.9} \\ \end{array}
$$

其中

$$
\begin{array}{l} \int_ {- \infty} ^ {x} | h ^ {\prime} (u) | \mathbf {P} (Z \leqslant u) \mathrm{d} u = \int_ {- \infty} ^ {x} | h ^ {\prime} (u) | \mathrm{d} u \int_ {- \infty} ^ {u} \phi (y) \mathrm{d} y \\ = \int_ {- \infty} ^ {x} \phi (y) \mathrm{d} y \int_ {y} ^ {x} | h ^ {\prime} (u) | \mathrm{d} u \\ \leqslant \| h ^ {\prime} \| \left[ x \mathbf {P} (Z \leqslant x) - \int_ {- \infty} ^ {x} \phi (y) y \mathrm{d} y \right] \\ = \| h ^ {\prime} \| \left[ x \mathbf {P} (Z \leqslant x) + \int_ {- \infty} ^ {x} \phi^ {\prime} (y) \mathrm{d} y \right] \\ = \| h ^ {\prime} \| \big [ x \mathbf {P} (Z \leqslant x) + \phi (x) \big ]. \\ \end{array}
$$

---

7.3 中心极限定理

189

类似地可得

$$
\int_ {x} ^ {\infty} | h ^ {\prime} (u) | \mathbf {P} (Z \geqslant u) \mathrm{d} u \leqslant \| h ^ {\prime} \| \big [ \phi (x) - x \mathbf {P} (Z \geqslant x) \big ].
$$

这样, 根据 (7.3.9) 式就有

$$
\begin{array}{l} | f ^ {\prime \prime} (x) | \leqslant \| h ^ {\prime} \| + \| h ^ {\prime} \| \left[ (1 + x ^ {2}) \frac {\mathbf {P} (Z \geqslant x)}{\phi (x)} - x \right] \left[ x \mathbf {P} (Z \leqslant x) + \phi (x) \right] + \\ \| h ^ {\prime} \| \Big [ x + (1 + x ^ {2}) \frac {\mathbf {P} (Z \leqslant x)}{\phi (x)} \Big ] \big [ \phi (x) - x \mathbf {P} (Z \geqslant x) \big ]. \\ \end{array}
$$

对上式右端整理即得  $\left|f''(x)\right|\leqslant2\|h'\|$ .

基于命题 7.3.5, 我们可以给出关于正态分布函数逼近的一个非常有用的一致估计. 为此, 对于给定的 a > 0 和  $z \in R$ , 令

$$
h (x) = 1 _ {\{x \leqslant z \}} + \frac {1}{a} (a + z - x) 1 _ {\{z <   x \leqslant z + a \}}, \quad x \in \mathbb {R}. \tag {7.3.10}
$$

定理 7.3.6 设  $W = \sum_{i=1}^{n} X_{i}$ ，其中  $X_{1}, X_{2}, \cdots, X_{n}$  为立方可积的零均值独立随机变量，且有 VarW = 1。则

$$
\sup _ {z \in \mathbb {R}} \left| \mathbf {P} (W \leqslant z) - \varPhi (z) \right| \leqslant 2 \left[ 3 \sum_ {i = 1} ^ {n} \mathbf {E} \big (| X _ {i} | ^ {3} \big) \right] ^ {1 / 2}. \tag {7.3.11}
$$

证明 令 $f$ 和 $h$ 分别由 (7.3.5) 式和 (7.3.10) 式给出. 则它们满足斯坦方程 (7.3.4). 因此有

$$
\begin{array}{l} \mathbf {P} (W \leqslant z) - \Phi (z) \leqslant \left[ \mathbf {E} h (W) - \mathbf {E} h (Z) \right] + \left[ \mathbf {E} h (Z) - \mathbf {P} (Z \leqslant z) \right] \\ \leqslant \left[ \mathbf {E} h (W) - \mathbf {E} h (Z) \right] + \mathbf {P} (z \leqslant Z \leqslant a + z) \\ \leqslant \mathbf {E} [ f ^ {\prime} (W) - W f (W) ] + a. \tag {7.3.12} \\ \end{array}
$$

设 $(Y_{1},Y_{2},\cdots,Y_{n})$ 是与 $(X_{1},X_{2},\cdots,X_{n})$ 独立同分布的随机向量. 再令 $W_{i}=W-X_{i}$ . 根据定理 7.3.5 有 $\|f^{\prime\prime}\|\leqslant2\|h^{\prime}\|=2/a$ . 因此

$$
\begin{array}{l} \left| \mathbf {E} [ f ^ {\prime} (W) - W f (W) ] \right| = \left| \sum_ {i = 1} ^ {n} \mathbf {E} \big [ Y _ {i} ^ {2} f ^ {\prime} (W) - X _ {i} f (W) + X _ {i} f (W _ {i}) \big ] \right| \\ = \Big | \sum_ {i = 1} ^ {n} \mathbf {E} \big [ Y _ {i} ^ {2} f ^ {\prime} (W) - Y _ {i} f (W _ {i} + Y _ {i}) + Y _ {i} f (W _ {i}) \big ] \Big | \\ = \Big | \sum_ {i = 1} ^ {n} \mathbf {E} \Big \{Y _ {i} \int_ {0} ^ {Y _ {i}} \big [ f ^ {\prime} (W) - f ^ {\prime} (W _ {i} + z) \big ] \mathrm{d} z \Big \} \Big | \\ = \left| \sum_ {i = 1} ^ {n} \mathbf {E} \left\{Y _ {i} \int_ {0} ^ {Y _ {i}} \mathrm{d} z \int_ {W _ {i} + z} ^ {W} f ^ {\prime \prime} (y) \mathrm{d} y \right\} \right| \\ \leqslant \frac {2}{a} \Big | \sum_ {i = 1} ^ {n} \mathbf {E} \Big [ Y _ {i} \int_ {0} ^ {Y _ {i}} (| X _ {i} | + | z |) \mathrm{d} z \Big ] \Big | \\ \end{array}
$$

---

190

第七章 概率极限定理

$$
\leqslant \frac {2}{a} \sum_ {i = 1} ^ {n} \Big [ \mathbf {E} (| X _ {i} |) \mathbf {E} (Y _ {i} ^ {2}) + \frac {1}{2} \mathbf {E} (| Y _ {i} | ^ {3}) \Big ].
$$

根据例 4.2.3 的结果,

$$
\mathbf {E} (| X _ {i} |) \mathbf {E} (Y _ {i} ^ {2}) = \mathbf {E} (| X _ {i} |) \mathbf {E} (| X _ {i} | ^ {2}) \leqslant \mathbf {E} (| X _ {i} | ^ {3}).
$$

回到 (7.3.12) 式得

$$
\mathbf {P} (W \leqslant z) - \varPhi (z) \leqslant \frac {3}{a} \sum_ {i = 1} ^ {n} \mathbf {E} \big (| X _ {i} | ^ {3} \big) + a.
$$

另一方面, 注意

$$
\begin{array}{l} \Phi (z) - \mathbf {P} (W \leqslant z) \leqslant \left[ \mathbf {P} (Z \leqslant z) - \mathbf {E} h (a + Z) \right] + \left[ \mathbf {E} h (a + Z) - \mathbf {E} h (a + W) \right] \\ \leqslant \mathbf {P} (z - a \leqslant Z \leqslant z) + [ \mathbf {E} h (a + W) - \mathbf {E} h (a + Z) ] \\ \leqslant \mathbf {E} [ f ^ {\prime} (a + W) - W f (a + W) ] + a. \\ \end{array}
$$

基于此式, 与前面推导类似地可得

$$
\varPhi (z) - \mathbf {P} (W \leqslant z) \leqslant \frac {3}{a} \sum_ {i = 1} ^ {n} \mathbf {E} \big (| X _ {i} | ^ {3} \big) + a.
$$

这样, 只要取

$$
a = \Big [ 3 \sum_ {i = 1} ^ {n} \mathbf {E} \big (| X _ {i} | ^ {3} \big) \Big ] ^ {1 / 2},
$$

便得估计式 (7.3.11).

定理7.3.7 设 $\{\xi_n\}$ 为立方可积的非退化独立同分布随机变量序列. 令 $S_{n}^{*}$ 为(7.3.1)式定义的标准化部分和. 则有

$$
\sup _ {z \in \mathbb {R}} \left| \mathbf {P} (S _ {n} ^ {*} \leqslant z) - \Phi (z) \right| \leqslant \frac {2 \sqrt {3 c}}{n ^ {1 / 4}}, \tag {7.3.13}
$$

其中 $c = \sigma^{-3}\mathbf{E}(|\xi_1 - a|^3)$

证明 记 $a = \mathbf{E}\xi_1$ 和 $\sigma^2 = \mathbf{Var}\xi_1 > 0$. 对于 $i, n \geqslant 1$, 令 $\xi_{ni} = (\xi_i - a) / \sqrt{n}\sigma$. 则有 $S_n^* = \sum_{i=1}^{n} \xi_{ni}$. 根据定理7.3.6有

$$
\sup _ {z \in \mathbb {R}} \big | \mathbf {P} (S _ {n} ^ {*} \leqslant z) - \varPhi (z) \big | \leqslant 2 \Big [ 3 \sum_ {i = 1} ^ {n} \mathbf {E} \big (| \xi_ {n i} | ^ {3} \big) \Big ] ^ {1 / 2},
$$

其中

$$
\mathbf {E} \big (| \xi_ {n i} | ^ {3} \big) = \frac {1}{n ^ {3 / 2} \sigma^ {3}} \mathbf {E} \big (| \xi_ {1} - a | ^ {3} \big) = \frac {c}{n ^ {3 / 2}}.
$$

因此 (7.3.13) 式成立.

---

7.3 中心极限定理

191

为了简化论证, 上面假定序列 $\{\xi_n\}$ 立方可积. 利用截尾方法可以证明, 只假定该序列平方可积, 仍可得到与定理7.3.7类似的结果. 定理中关于标准化部分和的分布函数与 $N(0,1)$ 的分布函数差的上界估计在应用中具有重要的意义. 关于斯坦方法的系统的讨论, 可以参阅[1].

## 7.3.4 应用的例子

例 7.3.3 前面证明的中心极限定理表明, 如果某个随机变量受大量因素的影响, 而每个因素的影响都很微小, 那么该随机变量会服从正态分布. 考虑例 1.1.2 中的高尔顿钉板试验. 假设板上铁钉共有 n 层, 这里 n 是很大的整数. 再设每层相邻铁钉间的距离很小, 不妨设为  $1/\sqrt{n}$ . 为了描述一个小球下落的情况, 考虑独立同分布随机变量序列  $\{\xi_{k}\}$ . 设有

$$
\mathbf {P} (\xi_ {k} = 1) = \mathbf {P} (\xi_ {k} = - 1) = \frac {1}{2}.
$$

直观上, 若第 $k$ 次碰撞使小球向左, 则 $\xi_{k} = -1$; 而若第 $k$ 次碰撞使小球向右, 则 $\xi_{k} = 1$.

以板钉漏斗为中心建立横向坐标轴. 则经过 $n$ 排铁钉落下的小球的位置恰为 $\{\xi_k\}$ 的标准化部分和, 即

$$
S _ {n} ^ {*} := \frac {1}{\sqrt {n}} \sum_ {k = 1} ^ {n} \xi_ {k}.
$$

因为 $n$ 是很大的整数, 由中心极限定理知 $S_{n}^{*}$ 近似地服从标准正态分布 $N(0,1)$, 即对 $x \leqslant y$ 有

$$
\mathbf {P} \big (x <   S _ {n} ^ {*} \leqslant y \big) \approx \frac {1}{\sqrt {2 \pi}} \int_ {x} ^ {y} \mathrm{e} ^ {- u ^ {2} / 2} \mathrm{d} u.
$$

再根据强大数定律, 当小球数量很大时, 最终落入区间 $(x, y)$ 中的小球数占总数的比例接近于上面的概率. 这就使得小球底板堆成的形状近似于 $N(0, 1)$ 的密度函数的图像.

例 7.3.4 现有 n = 200 台机床, 每台开动时需用电 1 kW. 如果每台机床的开动率均为 p = 0.6. 问至少需供电多少千瓦, 可将电力不足的概率保持在千分之一以下.

证明 设 $X_{n}$ 为开动的机床的数量. 则 $X_{n}$ 服从二项分布 $B(200, 0.6)$. 由题意需求最小的非负整数 $r$ 使得 $\mathbf{P}(X_{n} \leqslant r) \geqslant 0.999$. 直接利用二项分布求 $\mathbf{P}(X_{n} \leqslant r) \geqslant 0.999$ 需要的计算量较大. 由中心极限定理知随机变量

$$
\frac {X _ {n} - n p}{\sqrt {n p q}} = \frac {X _ {n} - 1 2 0}{\sqrt {4 8}}
$$

近似服从标准正态分布 $N(0,1)$ .因此有

---

192

第七章 概率极限定理

$$
\mathbf {P} (X _ {n} \leqslant r) = \mathbf {P} \Big (\frac {X _ {n} - 1 2 0}{\sqrt {4 8}} <   \frac {r - 1 2 0}{\sqrt {4 8}} \Big) \approx \varPhi \Big (\frac {r - 1 2 0}{\sqrt {4 8}} \Big).
$$

查正态分布表知可以取 $(r - 120) / \sqrt{48} = 3.1$ ，故得 $r = 141$

例7.3.5 设独立同分布随机变量序列 $\{\xi_n\}$ 服从均匀分布 $U(0,1)$. 则有 $\mathbf{E}\xi_1 = 1/2$ 和 $\mathrm{Var}\xi_1 = 1/12$. 当 $n$ 充分大时, 标准化部分和

$$
S _ {n} ^ {*} := \frac {1}{\sqrt {n} \mathbf {V a r} \xi_ {1}} \sum_ {k = 1} ^ {n} (\xi_ {k} - \mathbf {E} \xi_ {k}) = \frac {2 \sqrt {3}}{\sqrt {n}} \sum_ {k = 1} ^ {n} \left(\xi_ {k} - \frac {1}{2}\right)
$$

近似服从正态分布 $N(0,1)$。利用计算机可产生服从均匀分布 $U(0,1)$ 的独立伪随机数列 $\{\hat{\xi}_n\}$。取 $n = 12$，可视

$$
\hat {S} _ {1 2} ^ {*} := \sum_ {k = 1} ^ {1 2} \left(\hat {\xi} _ {k} - \frac {1}{2}\right)
$$

为服从正态分布的伪随机数.

例 7.3.6 重复进行某种测量, 用  $\xi_{n}$  表示第 n 测量的误差. 设  $\{\xi_{n}\}$  为独立同分布随机变量序列, 且服从均匀分布  $U(-a, a) (a > 0)$ . 则有  $E\xi_{1} = 0$  和  $Var\xi_{1} = a^{2}/3$ . 当 n 充分大时, 标准化和

$$
S _ {n} ^ {*} := \frac {1}{\sqrt {n \mathbf {V a r} \xi_ {1}}} \sum_ {k = 1} ^ {n} \xi_ {k} = \frac {1}{a \sqrt {n / 3}} \sum_ {k = 1} ^ {n} \xi_ {k}
$$

近似服从正态分布 $N(0,1)$，故平均值

$$
\frac {1}{n} \sum_ {k = 1} ^ {n} \xi_ {k} = \frac {a}{\sqrt {3 n}} S _ {n} ^ {*}
$$

近似服从正态分布 $N(0, a^2 / 3n)$. 可见平均误差随着 $n$ 的增大会更接近于零.

## 练习题

1. 设 $\xi$ 是非负整数值随机变量. 证明 $\xi$ 服从参数为 $\lambda > 0$ 的泊松分布当且仅当对任何满足 $f(0) = 0$ 的有界函数 $f$ 有 $\mathbf{E}[\xi f(\xi)] = \lambda \mathbf{E}f(\xi + 1)$.

2. 设随机变量 $S_{n}$ 服从泊松分布 $P(n)$. 证明当 $n \to \infty$ 时 $(S_{n} - n)/\sqrt{n}$ 依分布收敛, 并求其极限分布.

3. 证明当 $n \to \infty$ 时有

$$
\mathrm{e} ^ {- n} \sum_ {k = 0} ^ {n} \frac {n ^ {k}}{k !} \rightarrow \frac {1}{2}.
$$

---

\*7.4 独立非同分布序列

193

4. 设随机变量 $X_{n}$ 服从伽马分布 $\Gamma(\lambda, n)$. 证明当 $n \to \infty$ 时 $(X_{n} - n / \lambda) / \sqrt{n}$ 依分布收敛, 并求其极限分布.
5. 设 $\{\xi_n\}$ 是独立同分布的平方可积随机变量序列. 记 $X_{n} = n^{-1/2} \sum_{k=1}^{n} \xi_{k}$. 证明: 若 $\{X_{n}\}$ 是同分布随机变量序列, 则 $\{\xi_{k}\}$ 必然服从正态分布 $N(0,1)$.

## \*7.4 独立非同分布序列

本节讨论独立但未必同分布的随机变量序列的中心极限定理. 我们将给出这样的序列满足中心极限定理的充要条件.

## 7.4.1 费勒条件

设 $\{\xi_n\}$ 是平方可积的独立随机变量序列, 未必有相同的分布, 其中 $\xi_n$ 有数学期望 $a_{n} = \mathbf{E}\xi_{n}$ 和方差 $\sigma_{n}^{2} = \mathbf{Var}\xi_{n} > 0$. 分别用 $S_{n}$ 与 $S_{n}^{*}$ 表示其部分和与标准化部分和, 即

$$
S _ {n} = \sum_ {k = 1} ^ {n} \xi_ {k}, \quad S _ {n} ^ {*} = \frac {S _ {n} - \mathbf {E} S _ {n}}{B _ {n}}, \tag {7.4.1}
$$

其中

$$
B _ {n} = \sqrt {\mathbf {V a r} S _ {n}} = \left(\sum_ {k = 1} ^ {n} \sigma_ {k} ^ {2}\right) ^ {1 / 2}.
$$

为了后面的叙述方便, 我们写

$$
S _ {n} ^ {*} = \sum_ {k = 1} ^ {n} \xi_ {n k} \tag {7.4.2}
$$

其中

$$
\xi_ {n k} = \frac {\xi_ {k} - a _ {k}}{B _ {n}}.
$$

于是不难发现

$$
\mathbf {E} (\xi_ {n k}) = 0, \quad \mathbf {V a r} (\xi_ {n k}) = \mathbf {E} (\xi_ {n k} ^ {2}) = \frac {\sigma_ {k} ^ {2}}{B _ {n} ^ {2}}. \tag {7.4.3}
$$

我们称序列 $\{\xi_n\}$ 满足费勒 (Feller) 条件, 是指当 $n \to \infty$ 时有

---

194

第七章 概率极限定理

$$
\max _ {1 \leqslant k \leqslant n} \frac {\sigma_ {k} ^ {2}}{B _ {n} ^ {2}} = \max _ {1 \leqslant k \leqslant n} \mathbf {V a r} (\xi_ {n k}) \rightarrow 0. \tag {7.4.4}
$$

该条件表示, 当 $n \to \infty$ 时用方差衡量标准化部分和 $S_{n}^{*}$ 的表达式 (7.4.2) 中的各项一致地趋向于零.

命题 7.4.1 费勒条件 (7.4.4) 等价于

$$
\lim _ {n \to \infty} B _ {n} ^ {2} = \infty , \quad \lim _ {n \to \infty} \frac {\sigma_ {n} ^ {2}}{B _ {n} ^ {2}} = 0. \tag {7.4.5}
$$

证明 “$\Rightarrow$” 假设费勒条件 (7.4.4) 成立. 则显然

$$
\operatorname * {l i m s u p} _ {n \to \infty} \frac {\sigma_ {1} ^ {2}}{B _ {n} ^ {2}} = 0, \quad \operatorname * {l i m s u p} _ {n \to \infty} \frac {\sigma_ {n} ^ {2}}{B _ {n} ^ {2}} = 0.
$$

因 $\sigma_1^2 > 0$ ，有 $\lim_{n\to \infty}B_n^2 = \infty$ ，故(7.4.5)式成立.

“$\Leftarrow$”假设条件（7.4.5）成立.对于任何 $\varepsilon > 0$，由（7.4.5）式中第二个性质，可取 $N_0 \geqslant 1$ 使当 $n \geqslant N_0$ 时有 $\sigma_n^2 / B_n^2 < \varepsilon$，从而

$$
\max _ {N _ {0} \leqslant k \leqslant n} \frac {\sigma_ {k} ^ {2}}{B _ {n} ^ {2}} \leqslant \max _ {N _ {0} \leqslant k \leqslant n} \frac {\sigma_ {k} ^ {2}}{B _ {k} ^ {2}} <   \varepsilon .
$$

再由 (7.4.5) 式中第一个性质, 可取 $N \geqslant N_0$ 使当 $n \geqslant N$ 时有

$$
\max _ {1 \leqslant k \leqslant N _ {0}} \frac {\sigma_ {k} ^ {2}}{B _ {n} ^ {2}} = \frac {\max _ {1 \leqslant k \leqslant N _ {0}} \sigma_ {k} ^ {2}}{B _ {n} ^ {2}} <   \varepsilon .
$$

所以费勒条件 (7.4.4) 成立.

下面我们分别用 $f_{n}$ 和 $f_{nk}$ 表示 $S_{n}^{*}$ 和 $\xi_{nk}$ 的特征函数. 不难发现

$$
f _ {n} (t) = \prod_ {k = 1} ^ {n} f _ {n k} (t).
$$

定理 7.4.2 在费勒条件 (7.4.4) 下, 独立随机变量序列  $\{\xi_{n}\}$  满足中心极限定理当且仅当

$$
\lim _ {n \to \infty} \sum_ {k = 1} ^ {n} \left[ 1 - f _ {n k} (t) \right] = \frac {t ^ {2}}{2}. \tag {7.4.6}
$$

证明 根据连续性定理, 随机变量序列  $\{\xi_{n}\}$  满足中心极限定理的充要条件为

$$
\lim _ {n \to \infty} f _ {n} (t) = \lim _ {n \to \infty} \prod_ {k = 1} ^ {n} f _ {n k} (t) = \mathrm{e} ^ {- t ^ {2} / 2}. \tag {7.4.7}
$$

---

\*7.4 独立非同分布序列

195

根据定理5.2.2有

$$
\begin{array}{l} \left| f _ {n k} (t) - 1 \right| = \left| f _ {n k} (t) - 1 - \mathrm{i} t \mathbf {E} (\xi_ {n k}) \right| \\ \leqslant \mathbf {E} \left[ \left(| t \xi_ {n k} |\right) \wedge \left(\frac {| t \xi_ {n k} | ^ {2}}{2}\right) \right] \\ \leqslant \frac {t ^ {2}}{2} \mathbf {E} \left(\xi_ {n k} ^ {2}\right) = \frac {t ^ {2} \sigma_ {k} ^ {2}}{2 B _ {n} ^ {2}}. \tag {7.4.8} \\ \end{array}
$$

再由费勒条件, 当 $n \to \infty$ 时有

$$
\max _ {1 \leqslant k \leqslant n} \left| f _ {n k} (t) - 1 \right| \leqslant \max _ {1 \leqslant k \leqslant n} \frac {t ^ {2} \sigma_ {k} ^ {2}}{2 B _ {n} ^ {2}} \to 0.
$$

由推论5.3.9知 $\mathrm{e}^{f_{nk}(t) - 1}$ 是概率分布的特征函数，故有 $|\mathrm{e}^{f_{nk}(t) - 1}| \leqslant 1$。再由引理7.3.1知

$$
\begin{array}{l} \left| \prod_ {k = 1} ^ {n} \mathrm{e} ^ {f _ {n k} (t) - 1} - f _ {n} (t) \right| = \left| \prod_ {k = 1} ^ {n} \mathrm{e} ^ {f _ {n k} (t) - 1} - \prod_ {k = 1} ^ {n} f _ {n k} (t) \right| \\ \leqslant \sum_ {k = 1} ^ {n} \left| \mathrm{e} ^ {f _ {n k} (t) - 1} - f _ {n k} (t) \right| \\ = \sum_ {k = 1} ^ {n} \left| \mathrm{e} ^ {f _ {n k} (t) - 1} - 1 - \left(f _ {n k} (t) - 1\right) \right|. \\ \end{array}
$$

注意对任意 $\delta > 0$，当 $|z|$ 充分小时有 $|\mathrm{e}^z - 1 - z| \leqslant \delta |z|$. 所以，在费勒条件 (7.4.4) 下，由 (7.4.8) 式知当 $n \geqslant 1$ 充分大时有

$$
\begin{array}{l} \left| \prod_ {k = 1} ^ {n} \mathrm{e} ^ {f _ {n k} (t) - 1} - f _ {n} (t) \right| \leqslant \delta \sum_ {k = 1} ^ {n} \left| f _ {n k} (t) - 1 \right| \\ \leqslant \frac {\delta t ^ {2}}{2} \sum_ {k = 1} ^ {n} \frac {\sigma_ {k} ^ {2}}{B _ {n} ^ {2}} = \frac {\delta t ^ {2}}{2}. \\ \end{array}
$$

这里 $\delta > 0$ 可以任意小, 故上式说明

$$
\lim _ {n \to \infty} \Big | \prod_ {k = 1} ^ {n} \mathrm{e} ^ {f _ {n k} (t) - 1} - f _ {n} (t) \Big | = 0.
$$

再由充要条件 (7.4.7) 知 $\{\xi_n\}$ 满足中心极限定理当且仅当

$$
\lim _ {n \to \infty} \exp \left\{\sum_ {k = 1} ^ {n} [ f _ {n k} (t) - 1 ] \right\} = \lim _ {n \to \infty} \prod_ {k = 1} ^ {n} \mathrm{e} ^ {f _ {n k} (t) - 1} = \mathrm{e} ^ {- t ^ {2} / 2}.
$$

因而定理结论成立.

---

196

第七章 概率极限定理

## 7.4.2 林德伯格条件

我们称平方可积的独立随机变量列  $\{\xi_{n}\}$  满足林德伯格条件, 是指对于任意的  $\varepsilon > 0$ , 当  $n \to \infty$  时都有

$$
\frac {1}{B _ {n} ^ {2}} \sum_ {k = 1} ^ {n} \mathbf {E} \big [ (\xi_ {k} - a _ {k}) ^ {2} 1 _ {\{| \xi_ {k} - a _ {k} | \geqslant \varepsilon B _ {n} \}} \big ] = \sum_ {k = 1} ^ {n} \mathbf {E} \big (\xi_ {n k} ^ {2} 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \big) \rightarrow 0. \tag {7.4.9}
$$

显然, 该条件等价于

$$
\lim _ {n \to \infty} \sum_ {k = 1} ^ {n} \mathbf {E} \big (\xi_ {n k} ^ {2} 1 _ {\{| \xi_ {n k} | \leqslant \varepsilon \}} \big) = \lim _ {n \to \infty} \sum_ {k = 1} ^ {n} \mathbf {E} \big (\xi_ {n k} ^ {2} \big) = 1.
$$

上式直观上意味着, 以二阶矩的标准来看, 当 $n \to \infty$ 时 $S_{n}^{*}$ 的表达式 (7.4.2) 中取值较大的项可以忽略不计.

命题 7.4.3 若林德伯格条件 (7.4.9) 成立, 则费勒条件 (7.4.4) 成立.

证明 由 (7.4.3) 式知 $\sigma_k^2 / B_n^2 = \mathbf{E}(\xi_{nk}^2)$. 故对于任意的 $\varepsilon > 0$ 有

$$
\begin{array}{l} \max _ {1 \leqslant k \leqslant n} \frac {\sigma_ {k} ^ {2}}{B _ {n} ^ {2}} = \max _ {1 \leqslant k \leqslant n} \mathbf {E} \big [ \xi_ {n k} ^ {2} (1 _ {\{| \xi_ {n k} | <   \varepsilon \}} + 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}}) \big ] \\ \leqslant \varepsilon^ {2} + \max _ {1 \leqslant k \leqslant n} \mathbf {E} \big (\xi_ {n k} ^ {2} 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \big) \\ \leqslant \varepsilon^ {2} + \sum_ {k = 1} ^ {n} \mathbf {E} \big (\xi_ {n k} ^ {2} 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \big). \\ \end{array}
$$

令 $n\to \infty$ 和 $\varepsilon \rightarrow 0$ ，由林德伯格条件(7.4.9)知费勒条件(7.4.4)成立.

命题 7.4.4 若林德伯格条件 (7.4.9) 成立, 则对于任意的  $\varepsilon > 0$  有

$$
\lim _ {n \to \infty} \mathbf {P} \Big (\max _ {1 \leqslant k \leqslant n} | \xi_ {n k} | \geqslant \varepsilon \Big) = 0.
$$

证明 利用概率测度的次可加性, 有

$$
\begin{array}{l} \mathbf {P} \Big (\max _ {1 \leqslant k \leqslant n} | \xi_ {n k} | \geqslant \varepsilon \Big) = \mathbf {P} \Big (\bigcup_ {k = 1} ^ {n} \{| \xi_ {n k} | \geqslant \varepsilon \} \Big) \\ \leqslant \sum_ {k = 1} ^ {n} \mathbf {P} \left(| \xi_ {n k} | \geqslant \varepsilon\right) \\ \leqslant \frac {1}{\varepsilon^ {2}} \sum_ {k = 1} ^ {n} \mathbf {E} \left[ \xi_ {n k} ^ {2} 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \right]. \\ \end{array}
$$

再由林德伯格条件 (7.4.9) 知欲证结果成立.

![](../../raw/pages_0209-0224/images/page_210_image_17.jpg)

---

\*7.4 独立非同分布序列

197

## 7.4.3 林德伯格-费勒定理

引理7.4.5 设 $\xi$ 是零均值平方可积随机变量, 且有方差 $\sigma^2 = \mathrm{Var}\xi$. 记其特征函数为 $f$. 则对任意的 $\varepsilon > 0$ 有

$$
\left| f (t) - 1 + \frac {1}{2} \sigma^ {2} t ^ {2} \right| \leqslant \sigma^ {2} \varepsilon | t | ^ {3} + t ^ {2} \mathbf {E} \big (\xi^ {2} 1 _ {\{| \xi | \geqslant \varepsilon \}} \big), \quad t \in \mathbb {R}.
$$

证明 根据定理5.2.2有

$$
\begin{array}{l} \left| f (t) - 1 + \frac {1}{2} \sigma^ {2} t ^ {2} \right| = \left| f (t) - \left[ 1 + \mathrm{i} t \mathbf {E} \xi - \frac {t ^ {2}}{2} \mathbf {E} (\xi^ {2}) \right] \right| \\ \leqslant \mathbf {E} \left[ \left(| t \xi | ^ {2}\right) \wedge \left(\frac {| t \xi | ^ {3}}{6}\right) \right] \\ \leqslant \mathbf {E} \left[ | t \xi | ^ {2} 1 _ {\{| \xi | \geqslant \varepsilon \}} \right] + \mathbf {E} \left[ (| t \xi | ^ {3}) 1 _ {\{| \xi | <   \varepsilon \}} \right] \\ \leqslant t ^ {2} \mathbf {E} \left[ \xi^ {2} 1 _ {\{| \xi | \geqslant \varepsilon \}} \right] + \varepsilon | t | ^ {3} \mathbf {E} \left[ \xi^ {2} 1 _ {\{| \xi | <   \varepsilon \}} \right] \\ \leqslant t ^ {2} \mathbf {E} \left[ \xi^ {2} 1 _ {\{| \xi | \geqslant \varepsilon \}} \right] + \sigma^ {2} \varepsilon | t | ^ {3}. \\ \end{array}
$$

故得欲证估计.

定理 7.4.6 独立随机变量序列  $\{\xi_{n}\}$  满足费勒条件 (7.4.4) 和中心极限定理当且仅当林德伯格条件 (7.4.9) 成立.

证明 首先, 假设 $\{\xi_n\}$ 满足林德伯格条件 (7.4.9). 根据命题 7.4.3 知其满足费勒条件 (7.4.4). 注意 $\mathbf{Var}(\xi_{nk}) = \sigma_k^2 / B_n^2$ 和 $B_n^2 = \sum_{k=1}^{n} \sigma_k^2$. 由引理 7.4.5 有

$$
\begin{array}{l} \left| \sum_ {k = 1} ^ {n} \left[ f _ {n k} (t) - 1 \right] + \frac {t ^ {2}}{2} \right| = \left| \sum_ {k = 1} ^ {n} \left[ f _ {n k} (t) - 1 + \frac {1}{2} \frac {\sigma_ {k} ^ {2}}{B _ {n} ^ {2}} t ^ {2} \right] \right| \\ \leqslant \sum_ {k = 1} ^ {n} \left| f _ {n k} (t) - 1 + \frac {1}{2} \frac {\sigma_ {k} ^ {2}}{B _ {n} ^ {2}} t ^ {2} \right| \\ = \varepsilon | t | ^ {3} + t ^ {2} \sum_ {k = 1} ^ {n} \mathbf {E} \left[ \xi_ {n k} ^ {2} 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \right]. \\ \end{array}
$$

$$
\leqslant \sum_ {k = 1} ^ {n} \left[ \frac {\sigma_ {k} ^ {2}}{B _ {n} ^ {2}} \varepsilon | t | ^ {3} + t ^ {2} \mathbf {E} \big (\xi_ {n k} ^ {2} 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \big) \right]
$$

令 $n \to \infty$ 和 $\varepsilon \to 0$ 即知 (7.4.6) 式成立. 由定理 7.4.2 知 $\{\xi_n\}$ 满足中心极限定理.

反之, 假设随机变量序列  $\{\xi_{n}\}$  满足费勒条件 (7.4.4) 和中心极限定理. 注意

$$
\sum_ {k = 1} ^ {n} \mathbf {E} \Big (\mathrm{e} ^ {\mathrm{i} t \xi_ {n k}} - 1 + \frac {t ^ {2} \xi_ {n k} ^ {2}}{2} \Big) = \sum_ {k = 1} ^ {n} \big [ f _ {n k} (t) - 1 \big ] + \frac {t ^ {2}}{2}.
$$

由定理 7.4.2, 当  $n \rightarrow \infty$  时上式趋于零. 特别地, 其左边的实部趋于零, 即有

$$
\sum_ {k = 1} ^ {n} \mathbf {E} \left[ \cos (t \xi_ {n k}) - 1 + \frac {t ^ {2} \xi_ {n k} ^ {2}}{2} \right]\rightarrow 0. \tag {7.4.10}
$$

---

198

第七章 概率极限定理

注意到

$$
1 - \cos x = \int_ {0} ^ {x} \sin y \mathrm{d} y \leqslant \int_ {0} ^ {x} | \sin y | \mathrm{d} y \leqslant \int_ {0} ^ {x} y \mathrm{d} y = \frac {x ^ {2}}{2}.
$$

因此 (7.4.10) 中的随机变量是非负的, 故对任意的 $\varepsilon > 0$ 有

$$
\begin{array}{l} \sum_ {k = 1} ^ {n} \mathbf {E} \left[ \cos (t \xi_ {n k}) - 1 + \frac {t ^ {2} \xi_ {n k} ^ {2}}{2} \right] \\ \geqslant \sum_ {k = 1} ^ {n} \mathbf {E} \left\{\left[ \cos (t \xi_ {n k}) - 1 + \frac {t ^ {2} \xi_ {n k} ^ {2}}{2} \right] 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \right\} \\ \geqslant \sum_ {k = 1} ^ {n} \mathbf {E} \left[ \left(\frac {t ^ {2} \xi_ {n k} ^ {2}}{2} - 2\right) 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \right] \\ \geqslant \sum_ {k = 1} ^ {n} \mathbf {E} \left[ \left(\frac {t ^ {2} \xi_ {n k} ^ {2}}{2} - \frac {2 \xi_ {n k} ^ {2}}{\varepsilon^ {2}}\right) 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \right] \\ = \left(\frac {t ^ {2}}{2} - \frac {2}{\varepsilon^ {2}}\right) \sum_ {k = 1} ^ {n} \mathbf {E} \left[ \xi_ {n k} ^ {2} 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \right]. \\ \end{array}
$$

取 $t > 0$ 充分大可使 $t^2 / 2 - 2 / \varepsilon^2 > 0$. 由上式及 (7.4.10) 式知林德伯格条件成立.

![](../../raw/pages_0209-0224/images/page_212_image_7.jpg)

定理 7.4.6 在文献中被称为林德伯格-费勒或林德伯格-费勒-莱维中心极限定理. 这是一个相当普遍的结果, 由此可以容易地导出一些常见的特殊情况. 下面的李亚普诺夫 (Lyapunov) 中心极限定理是它的一个典型的特例.

定理7.4.7（李亚普诺夫） 设对于独立随机变量序列 $\{\xi_n\}$，存在常数 $\delta > 0$ 使当 $n \to \infty$ 时有

$$
\frac {1}{B _ {n} ^ {2 + \delta}} \sum_ {k = 1} ^ {n} \mathbf {E} \big [ | \xi_ {k} - a _ {k} | ^ {2 + \delta} \big ] = \sum_ {k = 1} ^ {n} \mathbf {E} [ | \xi_ {n k} | ^ {2 + \delta} ] \rightarrow 0, \tag {7.4.11}
$$

则  $\{\xi_{n}\}$  满足中心极限定理.

证明 注意, 对任意的 $\varepsilon > 0$ 有

$$
\sum_ {k = 1} ^ {n} \mathbf {E} \big [ | \xi_ {n k} | ^ {2} 1 _ {\{| \xi_ {n k} | > \varepsilon \}} \big ] \leqslant \frac {1}{\varepsilon^ {\delta}} \sum_ {k = 1} ^ {n} \mathbf {E} \big [ | \xi_ {n k} | ^ {2 + \delta} \big ].
$$

所以在假设条件 (7.4.11) 之下林德伯格条件成立. 再由定理 7.4.6 知 $\{\xi_n\}$ 满足中心极限定理. □

例 7.4.1 设  $\{\xi_{n}\}$  为独立随机变量序列, 且  $\xi_{n}$  服从均匀分布  $U(-\sqrt{n}, \sqrt{n})$ . 证明  $\{\xi_{n}\}$  满足中心极限定理.

证明 首先 $\mathbf{E}(\xi_k) = 0$ 所以

$$
B _ {n} ^ {2} = \sum_ {k = 1} ^ {n} \mathbf {E} (\xi_ {k} ^ {2}) = \sum_ {k = 1} ^ {n} \frac {1}{2 \sqrt {k}} \int_ {- \sqrt {k}} ^ {\sqrt {k}} x ^ {2} \mathrm{d} x = \sum_ {k = 1} ^ {n} \frac {k}{3} = \frac {n (n + 1)}{6},
$$

---

\*7.5 卡方独立性检验

199

则有

$$
\sum_ {k = 1} ^ {n} \mathbf {E} (\xi_ {k} ^ {4}) = \sum_ {k = 1} ^ {n} \frac {1}{2 \sqrt {k}} \int_ {- \sqrt {k}} ^ {\sqrt {k}} x ^ {4} \mathrm{d} x = \sum_ {k = 1} ^ {n} \frac {1}{5} k ^ {2} = \frac {1}{3 0} n (n + 1) (2 n + 1).
$$

因此

$$
\lim _ {n \to \infty} \frac {1}{B _ {n} ^ {4}} \sum_ {k = 1} ^ {n} \mathbf {E} (\xi_ {k} ^ {4}) = \lim _ {n \to \infty} \frac {6 (2 n + 1)}{5 n (n + 1)} = 0.
$$

由定理7.4.7知 $\{\xi_n\}$ 满足中心极限定理.

## 练习题

1. 设平方可积独立随机变量序列  $\{\xi_{n}\}$  满足中心极限定理. 证明  $\{\xi_{n}\}$  满足大数定律的充要条件是  $\mathrm{Var}(\xi_{1}+\xi_{2}+\cdots+\xi_{n})=o(n^{2})$ .
2. 设 $\{\xi_n\}$ 和 $\{\eta_n\}$ 均为非退化平方可积独立同分布随机变量序列, 其中 $\mathbf{P}(\eta_n = \pm 1) = 1/2$, 且两个序列也相互独立. 问序列 $\{\xi_n \eta_n\}$ 是否满足中心极限定理? 为什么?
3. 设  $\{\xi_{n}\}$  为独立随机变量序列, 且  $\xi_{n}$  服从正态分布  $N(0,1/2^{n})$ . 证明  $\{\xi_{n}\}$  满足中心极限定理, 但不满足费勒条件. 该随机变量序列是否满足林德伯格条件?
4. 设 $\{\xi_n\}$ 为独立随机变量序列, 其中 $\xi_1$ 服从均匀分布 $U(-1,1)$, 而当 $n \geqslant 2$ 时 $\xi_n$ 服从正态分布 $N(0,2^{n-1})$. 证明 $\{\xi_n\}$ 满足中心极限定理, 但不满足费勒条件.
5. 设 $\{\xi_n\}$ 为独立随机变量序列, 且 $\xi_n$ 服从均匀分布 $U(-n, n)$. 证明 $\{\xi_n\}$ 满足中心极限定理.
6. 设  $\{\xi_{k}\}$  为独立随机变量序列, 且有

$$
\begin{array}{l} \mathbf {P} (\xi_ {k} = 1) = \mathbf {P} (\xi_ {k} = - 1) = \frac {1}{2} \Big (1 - \frac {1}{k ^ {2}} \Big), \\ \mathbf {P} (\xi_ {k} = k + 1) = \mathbf {P} (\xi_ {k} = - k - 1) = \frac {1}{2 k ^ {2}}. \\ \end{array}
$$

问  $\{\xi_{k}\}$  是否满足中心极限定理？

## \*7.5 卡方独立性检验

在现实中人们经常需要回答一定范围内两种带有随机性的现象之间是否存在关联性或相互影响的问题。例如，就读不同学校是否对学生的成绩有影响，吸烟是否会增加患肺癌的风险，新研制的药物是否有效等。上述问题是随机独立性判断的典型案例。概

---

200

第七章 概率极限定理

率统计为这些问题提供了可行的解决方案, 也就是独立性检验. 独立性检验蕴含了深刻的统计学思想, 而由中心极限定理导出的卡方分布定理在这里发挥了关键作用.

## 7.5.1 卡方分布定理

基于林德伯格中心极限定理, 可以容易地导出在统计学中非常重要的皮尔逊 (Pearson) 卡方分布极限定理的一个特殊形式, 它是卡方独立性检验方法的理论基础. 令 $0 < p, q < 1$. 考虑某个概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的随机事件 $A_1, B_1, A_2, B_2, \dots$. 本节假定下面两个条件成立:

条件 1  $A_{1}, B_{1}, A_{2}, B_{2}, \cdots$  相互独立;

条件 2 对一切  $i \geqslant 1$  有  $\mathbf{P}(A_{i}) = p$  和  $\mathbf{P}(B_{i}) = q$ .

直观上, 这里事件 $A_{i}, B_{i}$ 表示第 $i$ 次随机试验中可能出现的结果. 回忆事件 $A \in \mathcal{F}$ 的示性函数定义为

$$
1 _ {A} (\omega) = \left\{ \begin{array}{l l} 1, & \omega \in A, \\ 0, & \omega \in A ^ {c}. \end{array} \right.
$$

特别地, 记 $\xi_{i} = 1_{A_{i}}$ 和 $\eta_{i} = 1_{B_{i}}$. 则 $\{\xi_{i}\}$ 和 $\{\eta_{i}\}$ 为两个相互独立的独立同分布随机变量序列, 且

$$
\mathbf {P} (\xi_ {i} = 1) = p, \mathbf {P} (\xi_ {i} = 0) = 1 - p, \mathbf {P} (\eta_ {i} = 1) = q, \mathbf {P} (\eta_ {i} = 0) = 1 - q.
$$

对 $n \geqslant 1$ 令

$$
S _ {n} = \sum_ {i = 1} ^ {n} \xi_ {i}, \quad T _ {n} = \sum_ {i = 1} ^ {n} \eta_ {i}. \tag {7.5.1}
$$

它们分别表示在前 n 次试验中事件  $A_{i}, B_{i}$  发生的次数. 再令

$$
a _ {n} = \sum_ {i = 1} ^ {n} (1 - \xi_ {i}) (1 - \eta_ {i}), \quad b _ {n} = \sum_ {i = 1} ^ {n} (1 - \xi_ {i}) \eta_ {i} \tag {7.5.2}
$$

$$
c _ {n} = \sum_ {i = 1} ^ {n} \xi_ {i} (1 - \eta_ {i}), \quad d _ {n} = \sum_ {i = 1} ^ {n} \xi_ {i} \eta_ {i}.
$$

它们分别表示在前 $n$ 次试验中 $A_{i}^{c}B_{i}^{c}, A_{i}^{c}B_{i}, A_{i}B_{i}^{c}$ 和 $A_{i}B_{i}$ 发生的次数. 记

$$
\chi_ {n} = \frac {\sqrt {n} (a _ {n} d _ {n} - b _ {n} c _ {n})}{\sqrt {(a _ {n} + b _ {n}) (c _ {n} + d _ {n}) (a _ {n} + c _ {n}) (b _ {n} + d _ {n})}}. \tag {7.5.3}
$$

引理 7.5.1 由 (7.5.3) 式定义的随机变量  $\chi_{n}$  可以表示为

$$
\chi_ {n} = \frac {\sum_ {i = 1} ^ {n} \xi_ {i} \eta_ {i} - S _ {n} T _ {n} / n}{\sqrt {S _ {n} T _ {n} (1 - S _ {n} / n) (1 - T _ {n} / n) / n}}. \tag {7.5.4}
$$

---

\*7.5 卡方独立性检验

201

证明 根据 (7.5.1) 式和 (7.5.2) 式有

$$
a _ {n} + b _ {n} = n - S _ {n}, c _ {n} + d _ {n} = S _ {n}, a _ {n} + c _ {n} = n - T _ {n}, b _ {n} + d _ {n} = T _ {n}.
$$

再由 (7.5.3) 式得

$$
\begin{array}{l} \chi_ {n} = \frac {\sqrt {n} \left[ (a _ {n} + b _ {n} + c _ {n} + d _ {n}) d _ {n} - (c _ {n} + d _ {n}) (b _ {n} + d _ {n}) \right]}{\sqrt {(a _ {n} + b _ {n}) (c _ {n} + d _ {n}) (a _ {n} + c _ {n}) (b _ {n} + d _ {n})}} \\ = \frac {\sqrt {n} \left[ n d _ {n} - (c _ {n} + d _ {n}) (b _ {n} + d _ {n}) \right]}{\sqrt {(a _ {n} + b _ {n}) (c _ {n} + d _ {n}) (a _ {n} + c _ {n}) (b _ {n} + d _ {n})}}. \\ \end{array}
$$

整理上式即得 (7.5.4) 式.

定理 7.5.2（卡方分布定理） 当  $n \to \infty$  时随机变量  $\chi_{n}^{2}$  的分布函数弱收敛到自由度为 1 的卡方分布函数.

证明 此证明的基本想法是将定理中所述收敛转化为林德伯格中心极限定理的结论. 记

$$
X _ {i} = \frac {(\xi_ {i} - p) (\eta_ {i} - q)}{\sqrt {p q (1 - p) (1 - q)}}.
$$

在前面的假定条件下, 显然  $X_{1}, X_{2}, \cdots$  是独立同分布随机变量. 另外, 易知

$$
\mathbf {E} \xi_ {i} = p, \mathbf {E} \eta_ {i} = q, \mathbf {V a r} \xi_ {i} = p (1 - p), \mathbf {V a r} \eta_ {i} = q (1 - q).
$$

据此并利用 $\xi_{i}$ 和 $\eta_{i}$ 的独立性可求得 $\mathbf{E}X_{i} = 0$ 和 $\operatorname{Var}X_{i} = 1$. 根据林德伯格中心极限定理, 当 $n \to \infty$ 时随机变量

$$
\zeta_ {n} := \frac {1}{\sqrt {n}} \sum_ {i = 1} ^ {n} X _ {i}
$$

弱收敛到标准正态随机变量. 注意

$$
\begin{array}{l} \zeta_ {n} = \frac {1}{\sqrt {n}} \sum_ {i = 1} ^ {n} \frac {(\xi_ {i} - p) (\eta_ {i} - q)}{\sqrt {p q (1 - p) (1 - q)}} \\ = \frac {\sum_ {i = 1} ^ {n} \xi_ {i} \eta_ {i} - q S _ {n} - p T _ {n} + n p q}{\sqrt {n p q (1 - p) (1 - q)}}. \\ \end{array}
$$

现令

$$
Z _ {n} = \frac {\sum_ {i = 1} ^ {n} \xi_ {i} \eta_ {i} - S _ {n} T _ {n} / n}{\sqrt {n p q (1 - p) (1 - q)}}. \tag {7.5.5}
$$

则有

---

202

第七章 概率极限定理

$$
\begin{array}{l} \zeta_ {n} - Z _ {n} = \frac {S _ {n} T _ {n} / n - q S _ {n} - p T _ {n} + n p q}{\sqrt {n p q (1 - p) (1 - q)}} \\ = \frac {S _ {n} / n - p}{\sqrt {p (1 - p)}} \cdot \frac {T _ {n} - n q}{\sqrt {n q (1 - q)}}. \\ \end{array}
$$

由林德伯格中心极限定理知 $(T_{n} - nq) / \sqrt{nq(1 - q)}$ 弱收敛到标准正态随机变量, 而由伯努利大数定律有 $S_{n} / n \stackrel{\mathrm{P}}{\rightarrow} p$. 根据定理 6.2.5 有 $\zeta_{n} - Z_{n} \stackrel{\mathrm{P}}{\rightarrow} 0$, 进而 $Z_{n}$ 弱收敛到标准正态随机变量. 根据伯努利大数定律还有 $T_{n} / n \stackrel{\mathrm{P}}{\rightarrow} q$, 进而不难发现

$$
S _ {n} T _ {n} (1 - S _ {n} / n) (1 - T _ {n} / n) / n ^ {2} \xrightarrow {\mathrm{P}} p q (1 - p) (1 - q).
$$

比较 (7.5.4) 式和 (7.5.5) 式, 根据定理 6.2.5 可知 $\chi_{n}$ 弱收敛到标准正态随机变量. 所以 $\chi_{n}^{2}$ 弱收敛到自由度为 1 的卡方随机变量. □

定理 7.5.2 是皮尔逊卡方分布极限定理的一个特殊形式. 注意, 前面我们假定了事件  $A_{1}, B_{1}, A_{2}, B_{2}, \cdots$  的独立性. 在定理的证明中, 确实用到了该假定, 特别是用到了  $\xi_{i}$  和  $\eta_{i}$  的独立性, 以保证  $EX_{i}=0$  和  $VarX_{i}=1$ . 没有这种独立性假定, 定理 7.5.2 所述的依分布收敛未必成立.

## 7.5.2 独立性问题

用事件 $A$ 和 $B$ 表示某类事物的两种现象或属性, 我们经常需要判断 $A$ 和 $B$ 是相互独立, 还是有关联或影响. 通常人们不会轻易断言这些现象之间存在关联性. 例如, 监管部门一般不会轻易认定新研制的药物对于某种疾病有疗效. 现代药物有效性检验中通行“随机、双盲、大样本”的基本原则, 这也体现了人们对于有效性认定时的谨慎态度.

假如概率值 $\mathbf{P}(A),\mathbf{P}(B)$ 和 $\mathbf{P}(AB)$ 是已知的, 可以直接对比 $\mathbf{P}(A)\mathbf{P}(B)$ 和 $\mathbf{P}(AB)$, 若它们的值相等, 则 $A$ 和 $B$ 独立; 否则 $A$ 和 $B$ 不独立. 但在现实中, 往往并不知道这些概率值. 在这种情况下, 根据频率稳定于概率的原理, 可以在同样条件下多次重复有关的随机试验, 用相应的频率替代上述概率进行计算和对比, 以判断 $A$ 与 $B$ 的独立性. 这里的多重随机试验在概率论中可用多维乘积概率空间描述, 在统计学中对应于有放回简单随机抽样.

典型案例 为比较甲、乙两所学校的教学情况, 在两校中随机抽取 85 名学生. 通过测验得到了如下数据: 甲校 42 名学生中有 9 名成绩优秀; 乙校 43 名学生中有 8 名成绩优秀. 将所给数据进行整理, 可以得到如下表格:

| 学生人数 | 成绩一般 | 成绩优秀 | 合计 |
| --- | --- | --- | --- |
| 甲校 | 33 | 9 | 42 |
| 乙校 | 35 | 8 | 43 |
| 合计 | 68 | 17 | 85 |

---

\*7.5 卡方独立性检验

203

我们希望知道两校学生的学习成绩是否存在明显差异. 用概率论的语言陈述, 该问题就是要判断学生就读于甲校 (事件 A) 或乙校 (事件 $A^c$) 和学生的成绩优秀 (事件 B) 与否 (事件 $B^c$) 是不是独立.

作为上述一般问题的严格化, 考虑概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 和事件 $A, B \in \mathcal{F}$. 用 $H_0$ 表示假设“$A$ 和 $B$ 独立”, 并称之为零假设. 该假设可等价地表示为

$$
H _ {0}: \left\{ \begin{array}{c c} \mathbf {P} (A ^ {c} B ^ {c}) = \mathbf {P} (A ^ {c}) \mathbf {P} (B ^ {c}), & \mathbf {P} (A ^ {c} B) = \mathbf {P} (A ^ {c}) \mathbf {P} (B), \\ \mathbf {P} (A B ^ {c}) = \mathbf {P} (A) \mathbf {P} (B ^ {c}), & \mathbf {P} (A B) = \mathbf {P} (A) \mathbf {P} (B). \end{array} \right. \tag {7.5.6}
$$

在现实中, 零假设 $H_0$ 往往是不应轻易否定的假设.

假定通过在关于零假设 $H_0$ 的样本总体中进行 $n$ 次有放回简单随机抽样, 得到如下数据统计表:

| 事件 | $B^{c}$ | B | 合计 |
| --- | --- | --- | --- |
| $A^{c}$ | a | b | $a+b$ |
| A | c | d | $c+d$ |
| 合计 | $a+c$ | $b+d$ | $n=a+b+c+d$ |

表格第4列的前两个数分别是对立事件 $A^c$ 和 $A$ 发生的频数；第4行的前两个数分别是对立事件 $B^{c}$ 和 $B$ 发生的频数；中间的四个数 $a, b, c, d$ 分别是事件 $A^{c}B^{c}, A^{c}B, AB^{c}, AB$ 发生的频数；最右下角格中的数 $n$ 是样本容量。这种形式的数据统计表称为 $2 \times 2$ 列联表。这里采用有放回简单随机抽样是为保证 $n$ 次抽样的结果是独立同分布的。

在零假设 $H_0$ 成立的情况下, 根据频率稳定于概率的原理, 由 (7.5.6) 式中第一个等式, 可以用概率 $\mathbf{P}(A^c)$ 和 $\mathbf{P}(B^c)$ 对应的频率的乘积 $(a + b)(a + c) / n^2$ 估计概率 $\mathbf{P}(A^c B^c)$, 而把 $(a + b)(a + c) / n$ 视为事件 $A^c B^c$ 发生的频数的期望值. 那么, 该频数的观测值 $a$ 和期望值 $(a + b)(a + c) / n$ 应该比较接近. 类似地, 综合 (7.5.6) 式中的 4 个式子, 下面量的取值都不应该太大:

$$
\left| a - \frac {(a + b) (a + c)}{n} \right|, \left| b - \frac {(a + b) (b + d)}{n} \right|,
$$

$$
\left| c - \frac {(c + d) (a + c)}{n} \right|, \left| d - \frac {(c + d) (b + d)}{n} \right|. \tag {7.5.7}
$$

注意 $a + b + c + d = n$. 据此不难发现, 这 4 个量实际上都等于 $|ad - bc| / n$. 但是, 我们并不能直接用这个的值的大小来推断 $H_0$ 是否成立. 原因是当样本容量很大时, 会导致 4 个频数、对应的期望值以及它们的差都很大. 一般来说, 若某个频数的期望值较大, 则对应的偏差也会较大. 为了合理地平衡这种影响, 我们将 (7.5.7) 式中的值取平方后分别除以相应的期望值再求和, 就得到如下的统计量:

$$
\chi^ {2} = \frac {(a d - b c) ^ {2}}{n (a + b) (a + c)} + \frac {(a d - b c) ^ {2}}{n (a + b) (b + d)} + \frac {(a d - b c) ^ {2}}{n (c + d) (a + c)} + \frac {(a d - b c) ^ {2}}{n (c + d) (b + d)}.
$$

---

204

第七章 概率极限定理

将上式通分并化简后得到

$$
\chi^ {2} = \frac {n (a d - b c) ^ {2}}{(a + b) (c + d) (a + c) (b + d)}. \tag {7.5.8}
$$

根据前面的分析, 在假设 $H_0$ 成立的情况下, 由 (7.5.8) 式定义的随机变量 $\chi^2$ 的取值不应该太大. 因此可将 $\chi^2$ 取值的大小作为推断 $H_0$ 是否成立的依据, 当它比较大时拒绝假设 $H_0$, 认为事件 $A$ 和 $B$ 不独立; 否则就接受 $H_0$ 这个假设, 认为事件 $A$ 和 $B$ 独立. 为确定 $\chi^2$ 的取值的大小的标准, 我们需要用到 $\chi^2$ 的分布.

根据定理7.5.2, 假设 $H_0$ 成立, 对于有放回简单随机抽样, 当样本容量 $n$ 充分大时 $\chi^2$ 的分布近似于自由度为1的卡方分布. 这为后面提出的检验规则提供了理论依据.

## 7.5.3 检验规则

根据前面的讨论, 在假设 $H_0$ 成立的情况下, 当样本容量 $n$ 充分大 (通常指 $n \geqslant 50$) 时由 (7.5.8) 式定义的统计量 $\chi^2$ 近似服从自由度为 1 的卡方分布. 于是, 对于充分小的概率值 $\alpha > 0$, 可以根据卡方分布求得相应的正实数 $x_\alpha$, 使得

$$
\alpha = \mathbf {P} (\chi^ {2} \geqslant x _ {\alpha}).
$$

我们称 $\alpha$ 为显著性水平, 而称 $x_{\alpha}$ 为它对应的临界值. 易见, 显著性水平 $\alpha$ 越小, 其临界值 $x_{\alpha}$ 越大. 下面给出了几个常用的显著性水平和它们对应的临界值的对应关系:

| $\alpha$ | 0.1 | 0.05 | 0.01 | 0.005 | 0.001 |
| --- | --- | --- | --- | --- | --- |
| $x_{\alpha}$ | 2.706 | 3.841 | 6.635 | 7.879 | 10.828 |

在假设 $H_0$ 成立的情况下, 根据小概率随机事件在一次试验中一般不会发生的规律, 只要显著性水平 $\alpha$ 取得充分小, 事件 $\{\chi^2 \geqslant x_\alpha\}$ 在一次试验中一般不会发生. 而如果它发生了, 我们就有理由拒绝假设 $H_0$. 该推断有可能是错误的, 但这种错误发生的概率仅为 $\mathbf{P}(\chi^2 \geqslant x_\alpha) = \alpha$.

根据上面的分析, 临界值 $x_{\alpha}$ 就可作为判断 $\chi^2$ 的大小的标准. 这样, 我们可以具体概括出独立性检验的如下规则:

- 当 $\chi^2 \geqslant x_\alpha$ 时, 我们拒绝零假设 $H_0$, 即认为事件 $A$ 和 $B$ 不独立;
- 当 $\chi^2 < x_\alpha$ 时, 没充分证据拒绝 $H_0$, 于是接受该假设, 即认为 $A$ 和 $B$ 独立.

这种利用 $\chi^2$ 的取值推断事件是否独立的方法称为卡方独立性检验, 也简称为卡方检验或独立性检验.

如上所述, 在假设 $H_0$ 成立的情况下, 当 $\chi^2 \geqslant x_\alpha$ 时拒绝 $H_0$ 的推断是错误的, 即出现拒真错误, 它发生的概率就是显著性水平 $\alpha = \mathbf{P}(\chi^2 \geqslant x_\alpha)$. 也就是说, 在 $H_0$ 成立

---

\*7.5 卡方独立性检验

205

的情况下, 我们错误地拒绝该假设的概率为 $\alpha$. 类似地, 在 $H_0$ 成立的情况下, 我们正确地接受该假设的概率为 $1 - \alpha$.

需要指出的是, 由显著性水平 $\alpha$ 通过等式 $\mathbf{P}(\chi^2 \geqslant x_\alpha) = \alpha$ 确定临界值 $x_\alpha$ 的过程基于 $\chi^2$ 的分布近似于自由度为1的卡方分布这个事实, 后者的理论依据是定理7.5.2.为了保证该定理在此适用, 需要假定 $H_0$ 成立.

当 $\chi^2 < x_\alpha$ 时接受 $H_0$ 的推断也可能是错误的, 即出现受伪错误, 其概率在理论上是未知的. 没有理由认为“当 $\chi^2 < x_\alpha$ 时接受 $H_0$ 的推断错误的概率为 $\alpha$”; 或者“当 $\chi^2 \geqslant x_\alpha$ 时拒绝 $H_0$ 的推断正确的概率为 $1 - \alpha$”. 事实上, 这两个说法都暗含了 $H_0$ 不成立的假定, 此时卡方分布定理不适用. 注意, 没有 $H_0$ 成立的前提条件, 在当前的理论框架下“推断正确”和“推断错误”并不构成对立随机事件!

在应用中, 样本来源总体通常都远大于我们抽取的样本的容量 $n$. 此时抽样是否放回对 $\chi^2$ 的影响很小, 故对无放回抽样等式 $\mathbf{P}(\chi^2 \geqslant x_\alpha) = \alpha$ 仍然近似地成立. 根据这种情况, 应用中往往并不严格要求抽样必须是有放回的.

例 7.5.1(典型案例) 为比较甲、乙两所学校的教学情况, 在两校中随机抽取 85 名学生. 通过测验得到了如下数据: 甲校 42 名学生中有 9 名成绩优秀; 乙校 43 名学生中有 8 名成绩优秀. 试利用显著性水平为  $\alpha = 0.1$  的卡方独立性检验, 分析两校学生的学习成绩是否存在差异.

解 根据题意提出零假设 $H_0$:学生所属校别与其学习成绩独立，即两校学生的成绩没有差异。再将所给数据进行整理，得到两校学生的学习成绩列联表:

| 学生人数 | 成绩一般 | 成绩优秀 | 合计 |
| --- | --- | --- | --- |
| 甲校 | 33 | 9 | 42 |
| 乙校 | 35 | 8 | 43 |
| 合计 | 68 | 17 | 85 |

基于列联表中的数据, 计算卡方统计量的值为

$$
\chi^ {2} = \frac {8 5 \times (3 3 \times 8 - 9 \times 3 5) ^ {2}}{4 2 \times 4 3 \times 6 8 \times 1 7} = \frac {8 5 \times (2 6 4 - 3 1 5) ^ {2}}{2 0 8 7 7 3 6} \approx 0. 1 0 6.
$$

与显著性水平 $\alpha = 0.1$ 对应的临界值比较发现 $\chi^2 \approx 0.106 < x_{0.1} = 2.706$. 根据检验规则, 无充分证据推断出假设 $H_0$ 不成立. 因此不拒绝该假设, 即认为两校学生的学习成绩没有显著差异. □

对于例 7.5.1, 我们知道在假设  $H_{0}$  确实为真的情况下, 我们作出上述正确判断的概率不低于 0.9.

例 7.5.2 某医院用甲、乙两类药物治疗某种急性疾病, 对随机抽取的 147 名患者的治疗情况进行统计, 得到如下数据: 抽到接受甲类药物的患者 69 名, 其中三天内未治

---

206

第七章 概率极限定理

愈 13 名, 治愈 56 名; 抽到接受乙类药物的患者 78 名, 其中三天内未治愈 6 名, 治愈 72 名. 试根据显著性水平  $\alpha = 0.05$  的卡方独立性检验, 分析两类药物的治疗效果.

解 根据题意提出零假设 $H_0$:药物种类与疗效独立，即两类药物的效果没有差异。将所给数据进行整理，得到两类药物的疗效数据列联表:

| 患者人数 | 未治愈 | 治愈 | 合计 |
| --- | --- | --- | --- |
| 甲类药物 | 13 | 56 | 69 |
| 乙类药物 | 6 | 72 | 78 |
| 合计 | 19 | 128 | 147 |

基于列联表中的数据, 计算卡方统计量的值为

$$
\chi^ {2} = \frac {1 4 7 \times (1 3 \times 7 2 - 5 6 \times 6) ^ {2}}{6 9 \times 7 8 \times 1 9 \times 1 2 8} = \frac {1 4 7 \times (9 3 6 - 3 3 6) ^ {2}}{1 3 0 8 9 0 2 4} \approx 4. 0 4 3.
$$

与显著性水平 $\alpha = 0.05$ 对应的临界值比较发现 $\chi^2 \approx 4.043 > x_{0.05} = 3.841$. 根据检验规则, 我们推断假设 $H_0$ 不成立, 即认为两类药物的效果存在差异. 由于乙类药物的治愈率 $72/78 \approx 0.923$ 高于甲类药物的 $56/69 \approx 0.812$, 可以认为乙类药物的治疗效果更好.

对于例 7.5.2, 我们知道在假设  $H_{0}$  事实上为真的情况下, 作出上述错误判断的概率不大于 0.05. 注意, 这并不意味着上面的判断正确的概率不小于 0.95; 也不是说我们有 95% 的 “把握” 认为乙类药物的治疗效果更好.

## 练习题

1. 某商场为提高服务质量, 随机调查了 80 位顾客对该商场服务情况的评价, 得到了如下数据: 在 41 位男顾客中有 16 位对服务不满意, 有 25 位对服务满意; 在 39 位女顾客中有 26 位对服务不满意, 有 13 位对服务满意. 根据显著性水平为 $5\%$ 的卡方独立性检验推断, 男、女顾客对该商场服务评价是否有差异?

答案: 根据检验规则, 推断零假设不成立, 即认为男、女顾客对该商场服务的评价有差异.

2. 某旅游景区为提高服务质量, 随机调查了 800 名男、女游客对该景区服务情况的评价, 得到了如下数据: 在 401 位男游客中有 195 位对服务不满意, 有 206 位对服务满意; 在 399 位女游客中有 207 位对服务不满意, 有 192 位对服务满意. 根据显著性水平为 $5\%$ 的卡方独立性检验推断, 男、女游客对该景区服务评价是否有差异?

答案: 根据检验规则, 不拒绝零假设, 即认为男、女游客对该景区服务的评价无差异.

3. 根据第 1 题和第 2 题的数据分别计算 (7.5.7) 式中的绝对值 $\varepsilon_{1}$ 和 $\varepsilon_{2}$, 比较哪组数据的频率与期望值之差的绝对值更大. 所得比较结果是否说明两题的推断结论不合理? 在统计量 $\chi^{2}$ 的定义中, 为什么要对 (7.5.7) 式中的绝对值进行适当的平衡处理?

---

\*7.5 卡方独立性检验

207

简答: 根据第 1 题的数据推断, 男、女顾客对商场服务的评价有差异; 而根据第 2 题的数据推断, 男、女游客对景区服务的评价无差异. 基于两题的数据分别计算出 (7.5.7) 式中的绝对值为

$$
\varepsilon_ {1} = \frac {\left| 1 6 \times 1 3 - 2 5 \times 2 6 \right|}{8 0} = \frac {\left| 2 0 8 - 6 5 0 \right|}{8 0} \approx 5. 5 2 5
$$

和

$$
\varepsilon_ {2} = \frac {\left| 1 9 5 \times 1 9 2 - 2 0 6 \times 2 0 7 \right|}{8 0 0} = \frac {\left| 3 7 4 4 0 - 4 2 6 4 2 \right|}{8 0 0} \approx 6. 5 0 3.
$$

比较发现 $\varepsilon_1 < \varepsilon_2$，即第2题的数据的频率与期望值之差的绝对值更大。该比较结果并不能说明两题的推断结论不合理。出现 $\varepsilon_1 < \varepsilon_2$ 的情况的原因是第2题的数据的容量比第1题的大很多，这导致其频率、期望值以及它们的差的绝对值也都比较大。所以，在统计量 $\chi^2$ 的定义中，要对(7.5.7)式中的绝对值进行适当的平衡处理。

4. 说明在本节给出的独立性检验的理论框架下, 下面的四个条件概率没有意义:

$$
\mathbf {P} (\chi^ {2} <   x _ {\alpha} | H _ {0}), \mathbf {P} (H _ {0} | \chi^ {2} <   x _ {\alpha}), \mathbf {P} (\chi^ {2} \geqslant x _ {\alpha} | H _ {0} ^ {c}), \mathbf {P} (H _ {0} ^ {c} | \chi^ {2} \geqslant x _ {\alpha}).
$$

提示: 在目前的框架下  $H_{0}$  不是随机事件.

5. 在本节讨论的基础之上, 给出一个扩展的独立性检验的理论框架, 使第4题中的条件概率有意义, 并且对于显著性水平为 $\alpha$ 的检验有 $\mathbf{P}(\chi^2 < x_\alpha | H_0) = 1 - \alpha$. 在该扩展的理论框架之下, 能否确定其他三个条件概率的具体值?

参考范例: 假设在可测空间 $(\Omega, \mathcal{F})$ 上有两个概率测度 $\mathbf{Q}_0$ 和 $\mathbf{Q}_1$, 且事件 $A, B \in \mathcal{F}$ 相对于 $\mathbf{Q}_0$ 独立, 而相对于 $\mathbf{Q}_1$ 不独立. 再设 $(\Omega, \mathcal{F})$ 上的概率测度 $\mathbf{Q}$ 随机地处于状态 $\mathbf{Q}_0$ 或 $\mathbf{Q}_1$. 为了实现对概率测度 $\mathbf{Q}$ 的这种随机化, 需要构造适当的概率空间 $(W, \mathcal{G}, \mathbf{P})$ 使 $H_0 := \{\mathbf{Q} = \mathbf{Q}_0\} \in \mathcal{G}$, 但概率 $\mathbf{P}(H_0)$ 在理论上是未知的. 在这样的框架之下, 显著性水平或拒真概率可表示为条件概率 $\mathbf{P}(\chi^2 \geqslant x_\alpha | H_0) = \alpha$, 故 $\mathbf{P}(\chi^2 < x_\alpha | H_0) = 1 - \alpha$. 受伪概率可表示为条件概率 $\mathbf{P}(\chi^2 < x_\alpha | H_0^c)$, 其中 $H_0^c = W \setminus H_0$, 但它在理论上是未知的.

---

![](../../raw/pages_0209-0224/images/page_222_chart_0.jpg)

<details>
<summary>line</summary>

| Year | Value |
| --- | --- |
| 2018 | ~45 |
| 2019 | ~60 |
| 2020 | ~75 |
| 2021 | ~85 |
| 2022 | ~95 |
| 2023 | ~80 |
</details>
