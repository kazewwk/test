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

![](images/page_210_image_17.jpg)

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

注意到

$$
1 - \cos x = \int_ {0} ^ {x} \sin y \mathrm{d} y \leqslant \int_ {0} ^ {x} | \sin y | \mathrm{d} y \leqslant \int_ {0} ^ {x} y \mathrm{d} y = \frac {x ^ {2}}{2}.
$$

因此 (7.4.10) 中的随机变量是非负的, 故对任意的 $\varepsilon > 0$ 有

$$
\begin{array}{l} \sum_ {k = 1} ^ {n} \mathbf {E} \left[ \cos (t \xi_ {n k}) - 1 + \frac {t ^ {2} \xi_ {n k} ^ {2}}{2} \right] \\ \geqslant \sum_ {k = 1} ^ {n} \mathbf {E} \left\{\left[ \cos (t \xi_ {n k}) - 1 + \frac {t ^ {2} \xi_ {n k} ^ {2}}{2} \right] 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \right\} \\ \geqslant \sum_ {k = 1} ^ {n} \mathbf {E} \left[ \left(\frac {t ^ {2} \xi_ {n k} ^ {2}}{2} - 2\right) 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \right] \\ \geqslant \sum_ {k = 1} ^ {n} \mathbf {E} \left[ \left(\frac {t ^ {2} \xi_ {n k} ^ {2}}{2} - \frac {2 \xi_ {n k} ^ {2}}{\varepsilon^ {2}}\right) 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \right] \\ = \left(\frac {t ^ {2}}{2} - \frac {2}{\varepsilon^ {2}}\right) \sum_ {k = 1} ^ {n} \mathbf {E} \left[ \xi_ {n k} ^ {2} 1 _ {\{| \xi_ {n k} | \geqslant \varepsilon \}} \right]. \\ \end{array}
$$

取 $t > 0$ 充分大可使 $t^2 / 2 - 2 / \varepsilon^2 > 0$. 由上式及 (7.4.10) 式知林德伯格条件成立.

![](images/page_212_image_7.jpg)

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

在现实中人们经常需要回答一定范围内两种带有随机性的现象之间是否存在关联性或相互影响的问题。例如，就读不同学校是否对学生的成绩有影响，吸烟是否会增加患肺癌的风险，新研制的药物是否有效等。上述问题是随机独立性判断的典型案例。概率统计为这些问题提供了可行的解决方案, 也就是独立性检验. 独立性检验蕴含了深刻的统计学思想, 而由中心极限定理导出的卡方分布定理在这里发挥了关键作用.

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

如上所述, 在假设 $H_0$ 成立的情况下, 当 $\chi^2 \geqslant x_\alpha$ 时拒绝 $H_0$ 的推断是错误的, 即出现拒真错误, 它发生的概率就是显著性水平 $\alpha = \mathbf{P}(\chi^2 \geqslant x_\alpha)$. 也就是说, 在 $H_0$ 成立的情况下, 我们错误地拒绝该假设的概率为 $\alpha$. 类似地, 在 $H_0$ 成立的情况下, 我们正确地接受该假设的概率为 $1 - \alpha$.

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

例 7.5.2 某医院用甲、乙两类药物治疗某种急性疾病, 对随机抽取的 147 名患者的治疗情况进行统计, 得到如下数据: 抽到接受甲类药物的患者 69 名, 其中三天内未治愈 13 名, 治愈 56 名; 抽到接受乙类药物的患者 78 名, 其中三天内未治愈 6 名, 治愈 72 名. 试根据显著性水平  $\alpha = 0.05$  的卡方独立性检验, 分析两类药物的治疗效果.

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

![](images/page_222_chart_0.jpg)

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

## 附录