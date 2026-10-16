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