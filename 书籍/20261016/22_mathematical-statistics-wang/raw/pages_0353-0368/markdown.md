注意到  $e^{sX}$  是关于 X 的一个凸函数和条件  $E(X)=0$ ，有

$$
\mathrm{e} ^ {s X} \leqslant \frac {b - X}{b - a} \mathrm{e} ^ {s a} + \frac {X - a}{b - a} \mathrm{e} ^ {s b}.
$$

两边对 X 取期望:

$$
\begin{array}{l} E \left(\mathrm{e} ^ {s X}\right) \leqslant \frac {b - E (X)}{b - a} \mathrm{e} ^ {s a} + \frac {E (X) - a}{b - a} \mathrm{e} ^ {s b} = \frac {b}{b - a} \mathrm{e} ^ {s a} - \frac {a}{b - a} \mathrm{e} ^ {s b} \\ = \left(- \frac {a}{b - a}\right) \mathrm{e} ^ {s a} \left(- \frac {b}{a} + \mathrm{e} ^ {s b - s a}\right). \\ \end{array}
$$

令 $\theta = -\frac{a}{b - a} > 0$ ，上式变成

$$
\theta \mathrm{e} ^ {- s \theta (b - a)} \left[ \frac {1}{\theta} - 1 + \mathrm{e} ^ {s (b - a)} \right] = \left[ 1 - \theta + \theta \mathrm{e} ^ {s (b - a)} \right] \mathrm{e} ^ {- s \theta (b - a)}.
$$

令 $u = s(b - a)$, 定义

$$
\begin{array}{l} \varphi : \mathbb {R} \to \mathbb {R}, \\ \varphi (u) = - \theta u + \ln \left(1 - \theta + \theta \mathrm{e} ^ {u}\right). \\ \end{array}
$$

这个函数是存在的, 因为由  $e^{u} \geqslant 0, a < 0, b > 0$  和  $\theta > 0$  有

$$
1 - \theta + \theta \mathrm{e} ^ {u} = \theta \left(\frac {1}{\theta} - 1 + \mathrm{e} ^ {u}\right) = \theta \left(- \frac {b}{a} + \mathrm{e} ^ {u}\right) > 0.
$$

由定义知

$$
E \left(\mathrm{e} ^ {s X}\right) \leqslant \mathrm{e} ^ {\varphi (u)}.
$$

根据 Taylor 展开, 和 Taylor 中值定理, 存在一个  $v \in [0, u]$  使得

$$
\varphi (u) = \varphi (0) + u \varphi^ {\prime} (0) + \frac {1}{2} u ^ {2} \varphi^ {\prime \prime} (v).
$$

由于

$$
\begin{array}{l} \varphi (0) = 0, \\ \varphi^ {\prime} (0) = - \theta + \left. \frac {\theta \mathrm{e} ^ {u}}{1 - \theta + \theta \mathrm{e} ^ {u}} \right| _ {u = 0} = 0, \\ \varphi^ {\prime \prime} (v) = \frac {\theta \mathrm{e} ^ {v} \left(1 - \theta + \theta \mathrm{e} ^ {v}\right) - \theta^ {2} \mathrm{e} ^ {2 v}}{\left(1 - \theta + \theta \mathrm{e} ^ {v}\right) ^ {2}} \\ = \frac {\theta \mathrm{e} ^ {v}}{1 - \theta + \theta \mathrm{e} ^ {v}} \left(1 - \frac {\theta \mathrm{e} ^ {v}}{1 - \theta + \theta \mathrm{e} ^ {v}}\right) = t (1 - t) \leqslant \frac {1}{4}, \\ \end{array}
$$

$$
\begin{array}{l} \varphi^ {\prime \prime} (v) = \frac {\theta \mathrm{e} ^ {v} \left(1 - \theta + \theta \mathrm{e} ^ {v}\right) - \theta^ {2} \mathrm{e} ^ {2 v}}{\left(1 - \theta + \theta \mathrm{e} ^ {v}\right) ^ {2}} \\ = \frac {\theta \mathrm{e} ^ {v}}{1 - \theta + \theta \mathrm{e} ^ {v}} \left(1 - \frac {\theta \mathrm{e} ^ {v}}{1 - \theta + \theta \mathrm{e} ^ {v}}\right) = t (1 - t) \leqslant \frac {1}{4}, \\ \end{array}
$$

其中 $t = \frac{\theta\mathrm{e}^v}{1 - \theta + \theta\mathrm{e}^v} > 0$。因此 $\varphi(u) \leqslant 0 + 0 + \frac{1}{2} u^2 \cdot \frac{1}{4} = \frac{1}{8} u^2 = \frac{1}{8}s^2 (b - a)^2$。这便证明了引理

$$
E \left(\mathrm{e} ^ {s X}\right) \leqslant \exp \left\{\frac {1}{8} s ^ {2} (b - a) ^ {2} \right\}.
$$

根据 Markov 不等式, 有

$$
\begin{array}{l} P \left(S _ {n} - E \left(S _ {n}\right) \geqslant t\right) = P \left(\mathrm{e} ^ {s \left[ S _ {n} - E (S _ {n}) \right]} \geqslant \mathrm{e} ^ {s t}\right) \\ \leqslant \mathrm{e} ^ {- s t} E \left\{\mathrm{e} ^ {s [ S _ {n} - E (S _ {n}) ]} \right\} \\ = \mathrm{e} ^ {- s t} \prod_ {i = 1} ^ {n} P \left(\mathrm{e} ^ {s [ X _ {i} - E (X _ {i}) ]}\right) \\ \leqslant \mathrm{e} ^ {- s t} \prod_ {i = 1} ^ {n} \mathrm{e} ^ {\frac {s ^ {2} (b _ {i} - a _ {i}) ^ {2}}{8}} \\ = \exp \left\{- s t + \frac {1}{8} s ^ {2} \sum_ {i = 1} ^ {n} \left(b _ {i} - a _ {i}\right) ^ {2} \right\}. \\ \end{array}
$$

上面的推导都只假定 s > 0, 定义

$$
\begin{array}{l} g: \mathbb {R} _ {+} \to \mathbb {R}, \\ g (s) = - s t + \frac {1}{8} s ^ {2} \sum_ {i = 1} ^ {n} \left(b _ {i} - a _ {i}\right) ^ {2}. \\ \end{array}
$$

求 $g^{\prime}(s) = 0$ 得到 $s = \frac{4t}{\sum_{i=1}^{n}\left(b_i - a_i\right)^2}$, 代入不等式, 即可得到

$$
P \left(S _ {n} - E \left(S _ {n}\right) \geqslant t\right) \leqslant \exp \left\{- \frac {2 t ^ {2}}{\sum_ {i = 1} ^ {n} \left(b _ {i} - a _ {i}\right) ^ {2}} \right\}.
$$

将上式中 $S_{n}$ 取为 $-S_{n}$，即可得到

$$
P \left(E \left(S _ {n}\right) - S _ {n} \geqslant t\right) \leqslant \exp \left\{- \frac {2 t ^ {2}}{\sum_ {i = 1} ^ {n} \left(b _ {i} - a _ {i}\right) ^ {2}} \right\}.
$$

例 A.5.3 Hoeffding 不等式可以用于给出置信区间. 假如一个特制的硬币正面朝上的概率是 p. 投 n 次硬币, 并得到 n 个样本  $X_{1}, X_{2}, \cdots, X_{n}$ . 令  $H_{n} = \sum_{i=1}^{n} X_{i}$  为观察到的正面朝上的次数, 则 Hoeffding 不等式给出

$$
P \left(\left| S _ {n} - n p \right| > n \varepsilon\right) \leqslant 2 \exp \left\{- 2 n \varepsilon^ {2} \right\}.
$$

令 $\bar{X} = \frac{1}{n} H_{n}$ 为观察到的均值, 我们想构造一个长度为 $2\varepsilon$ 且置信水平为 $1 - \alpha$ 的关于 $\bar{X}$ 的置信区间. 由于

$$
\alpha = P (\bar {X} \notin [ p - \varepsilon , p + \varepsilon ]) \leqslant 2 \exp \left\{- 2 n \varepsilon^ {2} \right\} \Leftrightarrow n \geqslant \frac {\ln (2 / \alpha)}{2 \varepsilon^ {2}}.
$$

我们至少需要 $\frac{\ln(2 / \alpha)}{2\varepsilon^2}$ 个样本, 才能构造出置信水平为 $1 - \alpha$ 的置信区间 $[p - \varepsilon, p + \varepsilon]$.

Hoeffding 不等式没有用到关于随机变量的分布的信息, 而 Bernstein (伯恩斯坦) 不等式利用随机变量的方差给出了一个更紧的界.

定理 A.5.7 (Bernstein 不等式) 令 $X_{1}, X_{2}, \cdots, X_{n}$ 为独立随机变量, 使得对于任意 $i \in \{1, 2, \cdots, n\}$, $E(X_{i}) = 0$, 且 $|X_{i}| \leqslant c$. 令 $\sigma^{2} = \frac{1}{n} \sum_{i=1}^{n} \operatorname{Var}(X_{i})$, 则

$$
P \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} \geqslant \varepsilon\right) \leqslant \exp \left\{- \frac {n \varepsilon^ {2}}{2 \sigma^ {2} + 2 c \varepsilon / 3} \right\}.
$$

证明 令 $\sigma_i^2 = E(X_i^2)$. 对于 $t > 0$, 令 $F_i = \sum_{k=2}^{\infty} \frac{t^{k-2} E(X_i^k)}{k! \sigma_i^2}$. 由于 $\mathrm{e}^x = 1 + x + \sum_{k=2}^{\infty} \frac{x^k}{k!}$, 且 $E(X_i) = 0$, 我们有

$$
E \left(\mathrm{e} ^ {t X _ {i}}\right) = 1 + F _ {i} t ^ {2} \sigma_ {i} ^ {2} \leqslant \mathrm{e} ^ {F _ {i} t ^ {2} \sigma_ {i} ^ {2}}.
$$

由于 $E\left(X_{i}^{k}\right) = \int x_{i}x_{i}^{k - 1}\mathrm{d}F(x)$ ，根据Cauchy不等式，有

$$
E \left(X _ {i} ^ {k}\right) \leqslant \left[ \int | x _ {i} | ^ {2} \mathrm{d} F (x) \right] ^ {\frac {1}{2}} \left[ \int \left| x _ {i} ^ {k - 1} \right| ^ {2} \mathrm{d} F (x) \right] ^ {\frac {1}{2}} = \sigma_ {i} \left[ \int \left| x _ {i} ^ {k - 1} \right| ^ {2} \mathrm{d} F (x) \right] ^ {\frac {1}{2}}.
$$

递归地应用 Cauchy 不等式, 我们有

$$
\begin{array}{l} E \left(X _ {i} ^ {k}\right) \leqslant \sigma_ {i} ^ {1 + \frac {1}{2} + \dots + \frac {1}{2 ^ {n - 1}}} \left[ \int \left| x _ {i} ^ {2 ^ {n} k - 2 ^ {n + 1} - 1} \right| \mathrm{d} F (x) \right] ^ {\frac {1}{2 ^ {n}}} \\ = \sigma_ {i} ^ {2 \left(1 - \frac {1}{2 ^ {n}}\right)} \left[ \int \left| x _ {i} ^ {2 ^ {n} k - 2 ^ {n + 1} - 1} \right| \mathrm{d} F (x) \right] ^ {\frac {1}{2 ^ {n}}}. \\ \end{array}
$$

由于 $|X_{i}| \leqslant c, \left[\int \left|x_{i}^{2^{n}k - 2^{n + 1} - 1}\right|\mathrm{d}F(x)\right]^{\frac{1}{2^n}} \leqslant \left(c^{2^{n}k - 2^{n + 1} - 1}\right)^{\frac{1}{2^n}}$ ，故

$$
E \left(X _ {i} ^ {k}\right) \leqslant \sigma_ {i} ^ {2 \left(1 - \frac {1}{2 ^ {n}}\right)} c ^ {k - 2 - \frac {1}{2 ^ {n}}}.
$$

令 $n\to \infty$ ，我们得到 $E\left(X_i^k\right)\leqslant \sigma_i^2 c^{k - 2}$ ，所以

$$
F _ {i} \leqslant \sum_ {k = 2} ^ {\infty} \frac {t ^ {k - 2} \sigma_ {i} ^ {2} c ^ {k - 2}}{k ! \sigma_ {i} ^ {2}} = \frac {1}{t ^ {2} c ^ {2}} \sum_ {k = 2} ^ {\infty} \frac {t ^ {k} c ^ {k}}{k !} = \frac {1}{t ^ {2} c ^ {2}} \left(\mathrm{e} ^ {t c} - 1 - t c\right).
$$

那么，

$$
E \left(\mathrm{e} ^ {t X _ {i}}\right) \leqslant \exp \left\{\sigma_ {i} ^ {2} \frac {\mathrm{e} ^ {t c} - 1 - t c}{c ^ {2}} \right\}.
$$

令 $S_{n} = \sum_{i=1}^{n} X_{i}$ 且 $a > 0$, 应用 Chernoff (切尔诺夫) 边界技巧, 我们得到

$$
\begin{array}{l} P \left(S _ {n} \geqslant a\right) \leqslant \mathrm{e} ^ {- t a} E \left(\mathrm{e} ^ {t S _ {n}}\right) \leqslant \exp \{- t a \} \exp \left\{\sum_ {i = 1} ^ {n} \sigma_ {i} ^ {2} \frac {\mathrm{e} ^ {t c} - 1 - t c}{c ^ {2}} \right\} \\ \leqslant \exp \left\{\frac {n \sigma^ {2}}{c ^ {2}} \left[ \frac {a c}{n \sigma^ {2}} - \ln \left(1 + \frac {a c}{n \sigma^ {2}}\right) \right] - \frac {a}{c} \ln \left(1 + \frac {a c}{n \sigma^ {2}}\right) \right\} \\ = \exp \left\{\frac {n \sigma^ {2}}{c ^ {2}} \left[ \frac {a c}{n \sigma^ {2}} - \ln \left(1 + \frac {a c}{n \sigma^ {2}}\right) - \frac {a c}{n \sigma^ {2}} \ln \left(1 + \frac {a c}{n \sigma^ {2}}\right) \right] \right\} \\ = \exp \left\{- \frac {n \sigma^ {2}}{c ^ {2}} \theta \left(\frac {a c}{n \sigma^ {2}}\right) \right\}, \\ \end{array}
$$

其中  $\theta(x)=(1+x)\ln(1+x)-x$ . 这里第一个不等式是 Markov 不等式, 第二个不等式是因为  $E\left(\mathrm{e}^{tX_{i}}\right)\leqslant\exp\left\{t^{2}\sigma_{i}^{2}\frac{\mathrm{e}^{tc}-1-tc}{t^{2}c^{2}}\right\}$ , 第三个不等式是因为取  $t=\frac{1}{c}\ln\left(1+\frac{ac}{n\sigma^{2}}\right)$  来对上界进行最小化.

令 $h(x) = \frac{3}{2}\frac{x^2}{x + 3}$ 和 $g(x) = h(x) - \theta (x)$. 由于 $g(0) = 0$, 且 $g(x) \geqslant 0, \forall x \geqslant 0$, 故 $h(x) \geqslant \theta (x), \forall x \geqslant 0$. 令 $a = n\varepsilon$, 我们得到

$$
\begin{array}{l} P \left(\frac {1}{n} \sum_ {i = 1} ^ {n} X _ {i} \geqslant \varepsilon\right) = P \left(\sum_ {i = 1} ^ {n} X _ {i} \geqslant n \varepsilon\right) \\ \leqslant \exp \left\{- \frac {n \sigma^ {2}}{c ^ {2}} h \left(\frac {n \varepsilon c}{n \sigma^ {2}}\right) \right\} = \exp \left\{- \frac {n \varepsilon^ {2}}{2 \sigma^ {2} + 2 c \varepsilon / 3} \right\}. \\ \end{array}
$$

接下来介绍的 Berry-Esseen (贝利埃森) 不等式给出了中心极限定理的收敛速度.

定理 A.5.8 (Berry-Esseen 不等式) 令  $X_{1}, X_{2}, \cdots, X_{n}$  为独立随机变量且  $E(X_{i}) = 0$ ，对某个  $0 < \delta \leqslant 1, E(|X_{i}|^{2+\delta}) < \infty$ 。则存在一个有限的常数 C，使得

$$
\sup _ {x \in \mathbb {R}} | G _ {n} (x) - \varPhi (x) | \leqslant C \frac {\sum_ {i = 1} ^ {n} E (| X _ {i} | ^ {2 + \delta})}{B _ {n} ^ {2 + \delta}},
$$

其中 $G_{n}(x) = P\left(\frac{\sum_{i=1}^{n}X_{i}}{B_{n}} \leqslant x\right), B_{n}^{2} = \sum_{i=1}^{n}\mathrm{Var}(X_{i}).$

定理的证明参见 Petrov (1975). 特别地, 当  $X_{1}, X_{2}, \cdots, X_{n}$  独立同分布且  $E(X) = 0$ ,  $\text{Var}(X) = \sigma^{2}$ ,  $E(|X|^{3}) = \rho < \infty$  时,

$$
\sup _ {x \in \mathbb {R}} | G _ {n} (x) - \varPhi (x) | \leqslant \frac {C \rho}{\sigma^ {3} \sqrt {n}}.
$$

这表示定理A.3.3中标准化的独立和收敛到正态分布的速度是 $O(n^{-1 / 2})$

Kolmogorov 不等式为随机变量部分和的绝对值的最大值的尾部概率给出了上界.

定理 A.5.9 (Kolmogorov 不等式) 令 $X_{1}, X_{2}, \cdots, X_{n}$ 为实值独立随机变量, 使得对于任意 $k \in \{1, 2, \cdots, n\}$ 和 $t > 0$, $E(\mathrm{e}^{tX_k}) \leqslant \mathrm{e}^{\frac{t^2r^2}{2}}$, 其中 $r > 0$. 那么,

$$
E \left(\max _ {1 \leqslant k \leqslant n} X _ {k}\right) \leqslant r \sqrt {2 \ln n}.
$$

证明 任选 $t > 0$. 由于指数函数是凸函数, 根据 Jensen 不等式, 我们有

$$
\begin{array}{l} \mathrm{e} ^ {t E \left(\max _ {1 \leqslant k \leqslant n} X _ {k}\right)} \leqslant E \left(\mathrm{e} ^ {t \max _ {1 \leqslant k \leqslant n} X _ {k}}\right) = E \left(\max _ {1 \leqslant k \leqslant n} \mathrm{e} ^ {t X _ {k}}\right) \\ \leqslant E \left(\sum_ {k = 1} ^ {n} \mathrm{e} ^ {t X _ {k}}\right) \leqslant n \mathrm{e} ^ {\frac {t ^ {2} r ^ {2}}{2}}. \\ \end{array}
$$

不等式两边同时取对数, 再选取  $t = \frac{\sqrt{2 \ln n}}{r}$  使得右边的表达式最小化, 我们得到

$$
E \left(\max _ {1 \leqslant k \leqslant n} X _ {k}\right) \leqslant \frac {\ln n}{t} + \frac {t r ^ {2}}{2} \Rightarrow E \left(\max _ {1 \leqslant k \leqslant n} X _ {k}\right) \leqslant r \sqrt {2 \ln n}.
$$

特别地，如果  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $N(0,1)$  的独立同分布样本，则 r = 1，从而  $E\left(\max_{1 \leqslant k \leqslant n} X_{k}\right) \leqslant \sqrt{2 \ln n}$ .

## A.6 两种常见轻尾分布

定义A.6.1 如果对随机变量 $X$ 和任意 $\lambda \in \mathbb{R}$，存在一个正数 $\sigma$ 使得

$$
E \left\{\mathrm{e} ^ {\lambda [ X - E (X) ]} \right\} \leqslant \mathrm{e} ^ {\frac {\sigma^ {2} \lambda^ {2}}{2}},
$$

则称 X 服从次 Gauss 分布, $\sigma$ 是 X 的次 Gauss 参数.

如果 $X \sim N(\mu, \sigma^2)$, 则 $E(\mathrm{e}^{\lambda X}) = \mathrm{e}^{\mu \lambda + \frac{\sigma^2\lambda^2}{2}}$. 因此 Gauss 分布是次 Gauss 分布. 由 Hoeffding 引理知, 任意有界的随机变量也服从次 Gauss 分布. 次 Gauss 分布具有可加性, 即任意两个次 Gauss 分布的和仍然是次 Gauss 分布.

次 Gauss 分布还有其他等价定义方式.

定理 A.6.1 对于均值为 0 的随机变量 X, 如下四种性质是等价的:

(1) 存在一个常数 $\sigma > 0$ 使得 $E\left(\mathrm{e}^{\lambda X}\right) \leqslant \mathrm{e}^{\frac{\lambda^2\sigma^2}{2}}, \forall \lambda \in \mathbb{R}$;
(2) 存在一个常数 $c > 0$ 和正态随机变量 $Z \sim N(0, \tau^2)$ 使得

$$
P (| X | \geqslant s) \leqslant c P (| Z | \geqslant s), \quad \forall s \geqslant 0;
$$

(3) 存在一个常数 $\theta > 0$ 使得 $E(X^{2k}) \leqslant \frac{(2k)!}{2^k k!} \theta^{2k}, \forall k \in \mathbb{N}$;
(4) 存在一个常数 $\sigma > 0$ 使得

$$
E \left(\mathrm{e} ^ {\frac {\lambda x ^ {2}}{2 \sigma^ {2}}}\right) \leqslant \frac {1}{\sqrt {1 - \lambda}}, \quad \forall \lambda \in [ 0, 1).
$$

证明参见 Wainwright (2019) 的 2.4 节.

对于次 Gauss 分布, 我们同样有 Hoeffding 不等式.

定理 A.6.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  是一列独立的随机变量且  $X_{i}$  服从参数为  $\sigma_{i}$  的次 Gauss 分布. 则对所有的  $t \geqslant 0$ ,

$$
P \left(\sum_ {i = 1} ^ {n} \left[ X _ {i} - E (X _ {i}) \right] \geqslant t\right) \leqslant \exp \left\{- \frac {t ^ {2}}{2 \sum_ {i = 1} ^ {n} \sigma_ {i} ^ {2}} \right\}.
$$

证明 根据 Markov 不等式, 有

$$
\begin{array}{l} P \left(\sum_ {i = 1} ^ {n} \left[ X _ {i} - E (X _ {i}) \right] \geqslant t\right) = P \left(\mathrm{e} ^ {s \left\{\sum_ {i = 1} ^ {n} \left[ X _ {i} - E (X _ {i}) \right] \right\}} \geqslant \mathrm{e} ^ {s t}\right) \\ \leqslant \mathrm{e} ^ {- s t} E \left\{\mathrm{e} ^ {s \left\{\sum_ {i = 1} ^ {n} \left[ X _ {i} - E (X _ {i}) \right] \right\}} \right\} \\ = \mathrm{e} ^ {- s t} \prod_ {i = 1} ^ {n} P \left(\mathrm{e} ^ {s [ X _ {i} - E (X _ {i}) ]}\right) \\ \leqslant \mathrm{e} ^ {- s t} \prod_ {i = 1} ^ {n} \mathrm{e} ^ {\frac {s ^ {2} \sigma_ {i} ^ {2}}{2}} \\ = \exp \left\{- s t + \frac {1}{2} s ^ {2} \sum_ {i = 1} ^ {n} \sigma_ {i} ^ {2} \right\}. \\ \end{array}
$$

上面的推导都只假定 s > 0, 定义

$$
g: \mathbb {R} _ {+} \to \mathbb {R},
$$

$$
g (s) = - s t + \frac {1}{2} s ^ {2} \sum_ {i = 1} ^ {n} \sigma_ {i} ^ {2}.
$$

求  $g'(s)=0$  得到  $s=\frac{t}{\sum_{i=1}^{n}\sigma_{i}^{2}}$ ，代入不等式，即可得到

$$
P \left(\sum_ {i = 1} ^ {n} \left[ X _ {i} - E (X _ {i}) \right] \geqslant t\right) \leqslant \exp \left\{- \frac {t ^ {2}}{2 \sum_ {i = 1} ^ {n} \sigma_ {i} ^ {2}} \right\}.
$$

由Hoeffding引理知,有界随机变量 $X\in [a,b]$ 的次Gauss参数是 $\frac{b - a}{2}$.因此定理A.5.6是定理A.6.2的特例.

定义A.6.2 若对随机变量 $X$ ，存在非负实数 $(v,\alpha)$ 使得

$$
E \left\{\mathrm{e} ^ {\lambda [ X - E (X) ]} \right\} \leqslant \mathrm{e} ^ {\frac {v ^ {2} \lambda^ {2}}{2}}, \quad \forall | \lambda | <   \frac {1}{\alpha},
$$

则称 X 服从参数为  $(v, \alpha)$  的次指数分布.

次指数分布仍然具有可加性, 即两个次指数分布的和仍然是次指数分布. 次 Gauss 分布是次指数分布, 但是反之不成立.

例A.6.1 设 $X \sim \chi_1^2$，则

$$
E \left[ \mathrm{e} ^ {\lambda (X - 1)} \right] = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\lambda \left(z ^ {2} - 1\right)} \mathrm{e} ^ {- z ^ {2} / 2} \mathrm{d} z = \frac {\mathrm{e} ^ {- \lambda}}{\sqrt {1 - 2 \lambda}}.
$$

当 $\lambda > 1/2$ 时, $E\left[\mathrm{e}^{\lambda(X - 1)}\right]$ 没有定义, 故 $X$ 不服从次 Gauss 分布. 但是

$$
\frac {\mathrm{e} ^ {- \lambda}}{\sqrt {1 - 2 \lambda}} \leqslant \mathrm{e} ^ {2 \lambda^ {2}} = \mathrm{e} ^ {4 \lambda^ {2} / 2}, \quad \forall | \lambda | <   \frac {1}{4}.
$$

因此 X 服从次指数分布.

同样地, 次指数分布也有多种等价定义方式.

定理 A.6.3 对于均值为 0 的随机变量 X, 下列性质等价:

(1) 存在非负实数  $(v, \alpha)$  使得

$$
E \left\{\mathrm{e} ^ {\lambda [ X - E (X) ]} \right\} \leqslant \mathrm{e} ^ {\frac {v ^ {2} \lambda^ {2}}{2}}, \quad \forall | \lambda | <   \frac {1}{\alpha};
$$

(2) 存在正数 $c$ 使得

$$
E \left(\mathrm{e} ^ {\lambda X}\right) <   \infty , \quad \forall | \lambda | \leqslant c;
$$

(3) 存在常数 $c_{1}, c_{2} > 0$ 使得

$$
P (| X | \geqslant t) \leqslant c _ {1} \mathrm{e} ^ {- c _ {2} t}, \quad \forall t > 0;
$$

(4) $\gamma \stackrel{\mathrm{def}}{=} \sup_{k \geqslant 2} \left[ \frac{E(X^k)}{k!} \right]^{1/k}$ 有界.

证明参见 Wainwright (2019) 的 2.5 节.

定理 A.6.4 (Bernstein 不等式) 设  $X_{1}, X_{2}, \cdots, X_{n}$  是一列独立的随机变量,  $X_{i}$  服从参数为  $(v_{i}, \alpha_{i})$  的次指数分布. 则

$$
P \left(\frac {1}{n} \sum_ {i = 1} ^ {n} \left[ X _ {i} - E (X _ {i}) \right] \geqslant t\right) \leqslant \left\{ \begin{array}{l l} \mathrm{e} ^ {- \frac {n t ^ {2}}{2 \left(v _ {*} ^ {2} / n\right)}}, & 0 \leqslant t \leqslant \frac {v _ {*} ^ {2}}{n \alpha_ {*}}, \\ \mathrm{e} ^ {- \frac {n t}{2 \alpha_ {*}}}, & t > \frac {v _ {*} ^ {2}}{n \alpha_ {*}}, \end{array} \right.
$$

其中  $\alpha_{*}\stackrel{def}{=} \max_{k=1,2,\cdots,n} \alpha_{k}, v_{*}\stackrel{def}{=} \sqrt{\sum_{k=1}^{n} v_{k}^{2}}.$

证明参见 Wainwright (2019) 的 2.1.3 节. 有界随机变量服从次指数分布, 因此定理 A.5.7 是定理 A.6.4 的特例.

## 参考文献

- 陈希孺, 1997. 数理统计引论 [M]. 北京: 科学出版社.
- 陈希孺, 2000. 数理统计发展简史 [M]. 长沙: 湖南教育出版社.
- 韦博成, 2006. 参数统计教程 [M]. 北京: 高等教育出版社.
- 陈希孺, 2009. 高等数理统计学 [M]. 合肥: 中国科学技术大学出版社.
- 陈希孺, 倪国策, 2009. 数理统计学教程 [M]. 合肥: 中国科学技术大学出版社.
- 陈希孺, 2012. 非参数统计 [M]. 合肥: 中国科学技术大学出版社.
- 薛留根, 2015. 现代非参数统计 [M]. 北京: 科学出版社.
- 王兆军, 邹长亮, 周永道, 2023. 数理统计教程 [M]. 2 版. 北京: 高等教育出版社.
- 茆诗松, 周纪芗, 陈颖, 2012. 试验设计 [M]. 2 版. 北京: 中国统计出版社.
- BAHADUR R R, 1960. Stochastic comparison of tests[J]. The Annals of Mathematical Statistics, 31: 276–295.
- BASU D, 1955. On statistics independent of a complete sufficient statistic[J]. Sankhya, 15:377–380.
- BAYES F R S, 1958. An essay toward solving a problem in the doctrine of chances[J]. Biometrika, 45(3–4): 296–315.
- BENJAMINI Y, HOCHBERG Y, 1995. Controlling the false discovery rate: a practical and powerful approach to multiple testing[J]. Journal of the Royal Statistical Society: Series B (Methodological), 57(1): 289–300.
- BERGER J O, 1985. Statistical Decision Theory and Bayesian Analysis, 2nd Edition[M]. New York: Springer-Verlag.
- BERGER R L, CASELLA G, 2001. Statistical Inference[M]. New York: Duxbury.
- BICKEL P J, FREEDMAN D A, 1981. Some Asymptotic Theory for the Bootstrap[J]. The annals of statistics, 9(6): 1196–1217.
- BILLINGSLEY P, 1995. Probability and Measure[M]. New York: John Wiley.
- BLACKWELL D, 1947. Conditional expectation and unbiased sequential estimation[J]. The
- Annals of Mathematical Statistics, 18(1): 105–110.
- BOURGON R, GENTLEMAN R, HUBER W, 2010. Independent filtering increases detection power for high-throughput experiments[J]. Proceedings of the National Academy of Sciences, 107(21): 9546–9551.
- CANTELLI F, 1933. Sulla determinazione empirica della leggi di probabilita[J]. Giorn Ist Ital Attuari, 4: 421–424.
- CRAMÉR H, 1946. Mathematical Methods of Statistics[M]. Princeton, NJ: Princeton University Press.
- D'AGOSTINO R B, 1971. An omnibus test of normality for moderate and large size samples[J]. Biometrika, 58: 341–348.
- DEMPSTER A P, LAIRD N M, RUBIN D B, 1977. Maximum likelihood from incomplete data via the EM algorithm[J]. Journal of the Royal Statistical Society: Series B (Methodological), 39(1): 1–22.
- DVORETZKY A, KIEFER J C, WOLFOWITZ J, 1956. Asymptotic minimax character of the sample distribution function and of the classical multinomial estimator[J]. The Annals of Mathematical Statistics, 33: 642–669.
- EDWARDS D, 2000. Introduction to Graphical Modelling[M]. New York: Springer Science & Business Media.
- FAN J, LI R, 2001. Variable selection via nonconcave penalized likelihood and its oracle properties[J]. Journal of the American statistical Association, 96: 1348–1360.
- FANG K T, LIU M Q, QIN H, et al, 2018. Theory and Application of Uniform Experimental Designs[M]. New York: Springer.
- FISHER R A, 1915. Frequency distribution of the values of the correlation coefficient in samples from an indefinitely large population[J]. Biometrika, 10(4): 507–521.
- FISHER R A, 1922. On the mathematical foundations of theoretical statistics[J]. Philosophical Transactions of the Royal Society of London, Ser. A., 222: 309–368.
- FRÉCHET M, 1943. Sur l'existence de certaines évaluations statistiques au cas de petits échantillons[J]. Review of the International Statistical Institute, 11: 182–205.
- GLIVENKO V I, 1933. Sulla determinazione empirica della leggi di probabilita[J]. Giorn Ist Ital Attuari, 4: 92–99.
- HALMOS P R, SAVAGE L J, 1949. Application of the Radon-Nikodym theorem to the theory of sufficient statistics[J]. The Annals of Mathematical Statistics, 20: 225–241.
- HODGES J L, LEHMANN E L, 1950. Some problems in minimax point estimation[J]. The Annals of Mathematical Statistics, 21(2): 182–197.
- HOEFFDING W, 1948. A nonparametric test for independence[J]. The Annals of Mathematical Statistics, 19: 546–557.
- HOERL A E, KENNARD R W, 1970. Ridge regression: biased estimation for nonorthogonal problems[J]. Technometrics, 12: 55–67.
- KOLMOGOROV A, 1933. Sulla determinazione empirica di una legge di distribuzione[J]. 1st. Ital. Attuari. G., 4: 1–11.
- LEHMANN E L, SCHEFFÉ H, 1950. Completeness, similar regions and unbiased estimation: Part I[J]. Sankhyā, 10: 305–340.
- LEHMANN E L, SCHEFFÉ H, 1955. Completeness, similar regions and unbiased estimation: Part II[J]. Sankhyā, 15: 219–236.
- MASSART P, 1990. The tight constant in the Dvoretzky-Kiefer-Wolfowitz inequality[J]. The Annals of Probability, 18(3): 1269–1283.
- OWEN A B, 2001. Empirical Likelihood[M]. New York: Chapman & Hall.
- PETROV V, 1975. Limit Theorems for Sums of Independent Random Variables[M]. New York: Springer-Verlag.
- RAO C R, 1945. Information and the accuracy attainable in the estimation of statistical parameters[J]. Bulletin of the Calcutta Mathematical Society, 27: 81–91.
- RAO C R, 1948. Large sample tests of statistical hypotheses concerning several parameters with applications to problems of estimation[J]. Mathematical Proceedings of the Cambridge Philosophical Society, 44(1): 50–57.
- ROBBINS H, 1956. An empirical Bayes approach to statistics[C]//Proceedings of the Third Berkeley Symposium on Mathematical Statistics and Probability, 1954–1955. Berkeley and Los Angeles: University of California Press: 157–163.
- SERFLING R, 1980. Approximation Theorems of Mathematical Statistics[M]. New York: John Wiley.
- SERFLING R J, 2009. Approximation Theorems of Mathematical Statistics[M]. New York: John Wiley & Sons.
- SHAO J, 2003. Mathematical Statistics[M]. New York: Springer Science & Business Media.
- SHAO J, TU D, 1995. The Jackknife and Bootstrap[M]. New York: Springer-Verlag.
- SHAPIRO S S, WILK M B, 1965. An analysis of variance test for normality (Complete Samples)[J]. Biometrika, 52: 591–611.
- SILVERMAN B W, 1986. Density Estimation for Statistics and Data Analysis[M]. New York: Chapman and Hall.
- SINGH K, 1981. On the asymptotic accuracy of Efron's bootstrap[J]. The Annals of Statistics: 1187–1195.
- SMIRNOV N V, 1939. Estimate of deviation between empirical distribution functions in two independent samples. (Russian)[J]. Bull. Moscow Univ., 2(2): 3–16.
- STONE C J, 1984. An asymptotically optimal window selection rule for kernel density estimates[J]. The Annals of Statistics, 12(4): 1285–1297.
- STOREY J D, TAYLOR J E, SIEGMUND D, 2004. Strong control, conservative point estimation and simultaneous conservative consistency of false discovery rates: a unified approach[J]. Journal of the Royal Statistical Society Series B: Statistical Methodology, 66(1): 187–205.
- STUART A, ORD J K, 1987. Kendall's Advanced Theory of Statistics[M]. London: Charles Griflin & Company Limited.
- TIBSHIRANI R, 1996. Regression shrinkage and selection via the Lasso[J]. Journal of the Royal Statistical Society, Series B, 58: 267–288.
- WAINWRIGHT M J, 2019. High-dimensional Statistics: A Non-asymptotic Viewpoint[M]. Cambridge: Cambridge University Press.
- WALD A, 1950. Statistical Decision Functions[M]. New York: Wiley.
- WARNER S L, 1965. Randomized response: A survey technique for eliminating evasive answer bias[J]. Journal of the American Statistical Association, 60: 63–69.
- WILCOXON F, 1945. Individual comparisons by ranking methods[J]. Biometrics Bulletin, 1(6):80–83.
- WILKS S S, 1938. The large-sample distribution of the likelihood ratio for testing composite hypotheses. Ann. Math. Stat., 9: 60–62.
- WU C F J, 1983. On the convergence properties of the EM algorithm[J]. The Annals of Statistics, 11(1): 95–103.
- ZOU H, HASTIE T, 2005. Regularization and variable selection via the elastic net[J]. Journal of the Royal Statistical Society, Series B, 67: 301–320.

## 索引

$(n,c)$ 方案 137

$\Gamma$ 分布 32

$\beta$ 分布 36

$\chi^{2}$  分布 21-26

非中心 $\chi^2$ 分布 26

$\chi^2$ 拟合优度检验

分类数据 282-285

列联表独立性检验 295

带有未知参数 287

Basu定理 45

Bayes 12, 91–97

Bayes 估计 91, 92, 98

Bayes 风险 98

先验分布 95

共轭先验 95

后验分布 93

经验 Bayes 97

Behrens-Fisher 问题 124, 154

Benjamini 199

Bhattacharya 下界 68

Box-Cox变换 258

Cauchy分布 36

Cochran定理 25

Cornish-Fisher展开 48

Dempster, A. P. 86

D 检验 294

E.Pearson 112, 129, 138

Edgeworth 展开 48

EM算法 91

Euler, L. 6

Fisher, R. A. 5, 8, 18, 26, 34, 37, 41, 77

F 分布 29-32

非中心 $F$ 分布 31

Galton, F. 9

Gauss-Markov 条件 217

Gosset, W. S. 26

Hochberg 199

Hotelling $T^2$ 分布 185

K. Pearson 112, 282, 285

Kolmogorov-Smirnov 检验 289

Kullback-Leibler 信息 64

k-折叠交叉验证 243

Laplace, P.-S. 3

Laplace分布 36

Lasso 回归 240

最小角回归法 243

| 群组 Lasso 回归 | 246 |
| --- | --- |
| 自适应 Lasso 回归 | 246 |
| latent 变量 | 87 |
| Lehmann | 43 |
| logistic 分布 | 37 |
| Mendel | 282 |
| Mendel, G. J. | 8 |
| minimax 估计 | 97-102 |
| 容许性 | 98 |
| 损失函数 | 98 |
| 风险函数 | 98 |
| N-P 引理 | 134 |
| Neyman | 112, 129, 131, 138, 150 |
| Pareto 分布 | 36 |
| Pearson, K. | 6, 8, 26, 34, 74 |
| R. A. Fisher | 112, 288 |
| Rao-Blackwell 定理 | 57 |
| Rayleigh 分布 | 157 |
| SCAD 回归 | 246 |
| Stirling 公式 | 28, 56 |
| Tukey | 195 |
| Tukey 学生化极差 | 196 |
| t 分布 | 26-29 |
| Student t 分布 | 27 |
| 非中心 t 分布 | 29 |
| t 检验 |  |
| 双边 | 121 |
| U 统计量 | 299 |
| 两样本 U 统计量 | 303 |
| Wald, A. | 97, 146 |
| Warner, S. L. | 3 |

| Weibull 分布 | 36 |
| --- | --- |
| Wilks 定理 | 140 |
| Wishart 分布 | 182 |
| W 检验 | 292 |

## B

| 备择假设 | 114 |
| --- | --- |
| 不完全数据 | 87 |

## C

| 参数 | 13 |
| --- | --- |
| 参数空间 | 13 |
| 尺度参数 | 32 |
| 形状参数 | 32 |
| 讨厌参数 | 15 |
| 参数估计法 | 216 |
| 残差 | 214 |
| 超有效性 | 73 |
| 陈希孺 | 11 |
| 抽样调查 | 2-4 |
| 随机应答 | 3 |
| 窗宽 | 269 |
| 次 Gauss 分布 | 33 |

## D

<table><tr><td>单边假设</td><td>114</td></tr><tr><td colspan="2">单样本正态总体参数的显著性检验</td></tr><tr><td>均值</td><td>118-121</td></tr><tr><td>方差</td><td>121</td></tr><tr><td>单因素多元方差分析</td><td>192</td></tr><tr><td>得分函数</td><td>67</td></tr><tr><td>第二类错误</td><td>114</td></tr><tr><td>第一类错误</td><td>114</td></tr><tr><td>对数似然函数</td><td>79</td></tr><tr><td>对数正态分布</td><td>36</td></tr></table>

多样本正态总体参数的显著性检验

| 方差分析 | 126 |
| --- | --- |
| 多元数据 | 166-170 |
| 样本相关矩阵 | 168 |
| 样本协方差矩阵 | 167 |
| 总体相关矩阵 | 166 |
| 总体协方差矩阵 | 166 |
| 多元正态分布 | 170-194 |
| 标准化多元正态向量 | 177 |
| 单样本均值检验 | 185 |
| 多样本均值检验 | 190 |
| 多元正态向量的二次型 | 177 |
| 两个多元正态向量和 | 175 |
| 密度函数 | 170 |
| 偏相关系数 | 175 |
| 线性组合 | 171 |
| 协方差矩阵检验 | 193 |
| 置信区域 | 188 |
| 子向量的独立性 | 172 |
| 子向量的条件正态性 | 173 |
| 子向量的正态性 | 172 |
| 最大似然估计 | 180 |
| 多重检验 | 194-203 |
| BH方法 | 200 |
| Bonferroni方法 | 198 |
| Holm方法 | 198 |
| PRDS | 201 |
| 错误发现率 | 199 |
| 错误发现率的控制 | 199 |
| 多重比较 | 195 |
| 总体错误率(FWER) | 196 |
| 总体错误率的控制 | 195 |

## E

二元正态分布 171

## F

| 非参数方法 | 266 |
| --- | --- |
| 非参数估计法 | 216 |
| 符号检验 | 304 |
| 复合假设 | 114 |

## G

功效函数或势函数 115, 130

## H

| 核函数 | 269 |
| --- | --- |
| 核密度估计 | 268 |
| 厚尾分布 | 29 |
| 后验 | 92 |
| 回归 | 9 |
| 回归系数矩阵 | 175 |
| 混合模型 | 90 |

## J

| 积分均方误差 | 270 |
| --- | --- |
| 假设检验 | 8-9 |
| 女士品茶 | 8 |
| 豌豆杂交 | 8 |
| 检验 | 113, 130 |
| MP或最大功效 | 131 |
| UMP | 136 |
| 等价 | 130 |
| 非随机化检验 | 130 |
| 随机化检验 | 130 |
| 简单假设 | 114 |
| 渐近方差 | 73 |
| 渐近均方误差 | 73 |
| 渐近偏差 | 73 |
| 渐近相对效率 | 73 |

渐近有效估计 66

截尾数据 89

经验分布函数 18,275,289

矩估计 8,74-75,77

强相合估计 76

渐近无偏估计 75

渐近正态性 76

拒绝域 114

均方误差 66

## L

两样本正态总体参数的显著性检验

均值 123

列联表 295

临界值 119

零假设 114

岭回归 236

岭迹 237

岭迹法 239

## M

茆诗松 11

帽子矩阵 221

## N

拟合优度检验 282

女士品茶试验 112

## P

偏协方差矩阵 175

平均绝对偏差 37

## S

似然比检验 137-138

似然函数 78

试验设计 5-6

36名军官排队问题 6

八卦 6

正交拉丁方 6

正交表 6

数据缺失 89

双边假设 114

双指数分布 36

随机对照双盲试验 4-5

脊髓灰质炎 4

临床试验 4

## T

弹性网 246

停时 146

统计决策 97

统计量 16

充分与完全统计量 37-46,60

充分统计量 38,56,64

因子分解定理 40

完全统计量 43

最小充分统计量 42

抽样分布 18

次序统计量 17

抽样分布 19

极差 17

极值分布 34

极值统计量 17

辅助统计量 45

修正的样本方差 16

样本 $p$ 分位数 17

样本均值 16

样本方差 16

自由度 16