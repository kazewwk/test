$$
\begin{array}{l} = \sum_ {k = 0} ^ {\infty} \mathbf {P} (N _ {s} = k) \mathbf {E} \bigg (\exp \left\{\mathrm{i} \sum_ {j = 1} ^ {n} \theta_ {j} \xi_ {k + j} \right\} \bigg) \\ = \sum_ {k = 0} ^ {\infty} \mathbf {P} (N _ {s} = k) \prod_ {j = 1} ^ {n} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {j} x} \mu (\mathrm{d} x) \\ = \prod_ {j = 1} ^ {n} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {j} x} \mu (\mathrm{d} x), \\ \end{array}
$$

所以 $\{\xi_{N_s + n}:n\geqslant 1\}$ 是独立同分布随机变量序列且有分布 $\mu$ .再由(1.4.6)式有

$$
X _ {s + t} - X _ {s} = \sum_ {n = 1} ^ {N _ {s + t} - N _ {s}} \xi_ {N _ {s} + n}. \tag {1.4.8}
$$

易知 $(N_{s + t} - N_s:t\geqslant 0)$ 是以 $\alpha \geqslant 0$ 为参数的零初值泊松过程, 且与 $\{\xi_{N_s + n}:n\geqslant 1\}$ 独立. 因此, 在 $N_{s + t} - N_s = k$ 条件下, 上式右边为 $k$ 个以 $\mu$ 为分布的独立同分布随机变量之和. 再根据全期望公式有

$$
\begin{array}{l} \mathbf {E} \mathrm{e} ^ {\mathrm{i} \theta (X _ {s + t} - X _ {s})} = \mathbf {E} \exp \left\{\mathrm{i} \theta \sum_ {n = 1} ^ {N _ {s + t} - N _ {s}} \xi_ {N _ {s} + n} \right\} \\ = \mathrm{e} ^ {- \alpha t} \sum_ {k = 0} ^ {\infty} \frac {(\alpha t) ^ {k}}{k !} \left[ \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta x} \mu (\mathrm{d} x) \right] ^ {k} \\ = \exp \left\{t \int_ {\mathbb {R}} (\mathrm{e} ^ {\mathrm{i} \theta x} - 1) \mu (\mathrm{d} x) \right\}. \\ \end{array}
$$

即 (1.4.7) 式成立. 对任何  $0 \leqslant t_{0} < t_{1} < t_{2} < \cdots < t_{n}$  及实数  $\theta_{1}, \theta_{2}, \cdots, \theta_{n}$ ，利用形如 (1.4.8) 式的表达可以得到

$$
\mathbf {E} \exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} (X _ {t _ {k}} - X _ {t _ {k - 1}}) \right\} = \prod_ {k = 1} ^ {n} \mathbf {E} \exp \left\{\mathrm{i} \theta_ {k} (X _ {t _ {k}} - X _ {t _ {k - 1}}) \right\}.
$$

由随机向量的特征函数的性质知  $X_{t_{1}} - X_{t_{0}}, X_{t_{2}} - X_{t_{1}}, \cdots, X_{t_{n}} - X_{t_{n-1}}$  相互独立. 显然这些随机变量与  $X_{t_{0}} = X_{0} = \xi_{0}$  独立. □

例 1.4.2 在某保险公司的理赔业务中, 申请赔偿的顾客按照参数为 $\alpha > 0$ 的零初值泊松过程 $(N_{t}: t \geqslant 0)$ 到达, 而顾客申请赔偿的金额由独立同分布的非负随机变量序列 $\{\xi_{n}: n \geqslant 0\}$ 给出. 这样, 在时间段 $(0, t]$ 到来的顾客申请赔偿金额的总和 $X_{t}$ 就由 (1.4.6) 式给出, 而 $(X_{t}: t \geqslant 0)$ 是一个复合泊松过程. 则对任何 $x \geqslant 0$ 有

$$
\mathbf {P} (X _ {t} \geqslant x) = \mathrm{e} ^ {- \alpha t} \sum_ {k = 0} ^ {\infty} \frac {(\alpha t) ^ {k}}{k !} \mu^ {* k} [ x, \infty),
$$

其中 $\mu^{*k}$ 表示 $\mu$ 的 $k$ 重卷积. 对于足够小的概率值 $p (0 < p < 1)$, 由上式可确定出最小的 $x = x_{t}(p) \geqslant 0$ 使得 $\mathbf{P}(X_{t} \geqslant x) \leqslant p$. 这样只要准备额度为 $x_{t}(p)$ 的预备金, 在时间段 $(0, t]$ 出现赔偿金不足的概率就不会超过 $p$.

例 1.4.3 考虑某个服务站的工作情况. 设其顾客按照参数为  $\alpha > 0$  的零初值泊松过程 ( $N_{t}: t \geqslant 0$ ) 到达, 而顾客所需服务的工作量由独立同分布的非负随机变量序列  $\{\xi_{n}: n \geqslant 0\}$  给出. 令 ( $X_{t}: t \geqslant 0$ ) 是由 (1.4.6) 式定义的复合泊松过程, 则  $X_{t}$  表示在时间段 (0, t] 到来的顾客所需服务工作量的总和. 设服务站的工作效率为  $\beta > 0$ , 则其在时间段 (0, t] 能够提供的最大服务量为  $\beta t$ . 记  $Y_{t} = X_{t} - \beta t$ . 考虑到在等待顾客数量清零时服务器不提供服务, 可以发现 t 时刻等待的顾客所需服务的工作总量应为  $Z_{t} = Y_{t} - \inf_{0 \leqslant s \leqslant t} Y_{s}$ .

## 练习题

1. 设 $(N(t): t \geqslant 0)$ 是参数为 $\lambda > 0$ 的泊松过程。对 $t > s > 0$ 求条件概率 $\mathbf{P}(N(s) = k | N(t) = n)$。
2. 设  $(N_{t}: t \geqslant 0)$  是从零出发参数为  $\alpha > 0$  的泊松过程。对  $n \geqslant 1$  令  $S_{n} = \inf\{t \geqslant 0 : N_{t} \geqslant n\}$  是  $(N_{t}: t \geqslant 0)$  的第 n 次跳跃的等待时间。证明对于 t > 0 在给定  $\{N(t) = n\}$  之下  $(S_{1}, S_{2}, \cdots, S_{n})$  的联合条件概率分布密度为

$$
f (x _ {1}, x _ {2}, \dots , x _ {n}) = \left\{ \begin{array}{l l} n! / t ^ {n}, & 0 <   x _ {1} <   x _ {2} <   \dots <   x _ {n}, \\ 0, & \text {其他.} \end{array} \right.
$$

3. 对 t > 0 令  $(X_{1}, X_{2}, \cdots, X_{n})$  是服从均匀分布  $U(0, t)$  的独立随机变量序列. 再令  $(Z_{1}, Z_{2}, \cdots, Z_{n})$  是  $(X_{1}, X_{2}, \cdots, X_{n})$  的由小到大排列的顺序统计量. 证明  $(Z_{1}, Z_{2}, \cdots, Z_{n})$  具有上题中给出的概率分布密度.
4. 设 $(X_{t}: t \geqslant 0)$ 和 $(Y_{t}: t \geqslant 0)$ 分别是以 $\alpha > 0$ 和 $\beta > 0$ 为参数的泊松过程且二者相互独立. 证明 $(X_{t} + Y_{t}: t \geqslant 0)$ 是以 $\alpha + \beta$ 为参数的泊松过程.
5. 设 $(X_{n}: n \geqslant 0)$ 是离散时间一维随机游动, 而 $(X_{N_{t}}: t \geqslant 0)$ 是例1.4.1中定义的连续时间随机游动. 分别讨论二者的长时间极限行为.

## 1.5 泊松随机测度

## 1.5.1 定义和存在性

考虑可测空间 $(E, \mathcal{E})$。为具体起见，我们假定 $(E, \mathcal{E})$ 是某个有限维欧氏空间的博雷尔可测子空间，即 $E \in \mathcal{B}^d$ ($d \geqslant 1$) 且 $\mathcal{E} = E \cap \mathcal{B}^d$。设 $\mu$ 为 $(E, \mathcal{E})$ 上的 $\sigma$ 有限测度。

定义 1.5.1 称取值于  $\{0,1,2,\cdots,\infty\}$  的随机变量族  $X=\{X(B):B\in\mathcal{E}\}$  是以  $\mu$  为强度的整数值随机测度, 是指它满足下列条件:

(1) 若 $B \in \mathscr{E}$ 满足 $\mu(B) < \infty$, 则 $\mathbf{E}[X(B)] = \mu(B)$;
(2) 若  $B_{1}, B_{2}, \cdots \in E$  两两不相交, 则

$$
X \Big (\bigcup_ {k = 1} ^ {\infty} B _ {k} \Big) = \sum_ {k = 1} ^ {\infty} X (B _ {k}). \tag {1.5.1}
$$

定义 1.5.2 称  $(E, \mathcal{E})$  上的以  $\mu$  为强度的整数值随机测度是泊松随机测度, 是指它满足下列条件:

(1) 若 $B \in \mathscr{E}$ 满足 $\mu(B) < \infty$, 则 $X(B)$ 服从参数为 $\mu(B)$ 的泊松分布, 即

$$
\mathbf {P} (X (B) = k) = \frac {\mu (B) ^ {k}}{k !} \mathrm{e} ^ {- \mu (B)}, \quad k = 0, 1, 2, \dots ;
$$

(2) 若  $B_{1}, B_{2}, \cdots, B_{n} \in E$  两两不相交, 则  $X(B_{1}), X(B_{2}), \cdots, X(B_{n})$  相互独立.

根据泊松分布的性质, 若 $X$ 是以 $\mu$ 为强度的泊松随机测度且 $B \in \mathcal{E}$ 满足 $\mu(B) < \infty$, 则有

$$
\mathbf {E} [ X (B) ] = \mu (B), \quad \mathbf {V a r} [ X (B) ] = \mu (B). \tag {1.5.2}
$$

例 1.5.1 设  $E=\{1,2\}$ ，而  $\mu$  为 E 上的计数测度。再设  $\xi_{1},\xi_{2}$  和  $\xi_{3}$  是独立同分布随机变量，且均服从参数为 1 的泊松分布。令

$$
X (\{1 \}) = \xi_ {1}, X (\{2 \}) = \xi_ {2}, X (\{1, 2 \}) = \xi_ {1} + \xi_ {3},
$$

则 $X$ 满足定义 1.5.2 中的性质 (1) 和 (2). 但 (1.5.1) 式不成立, 故 $X$ 不是整数值随机测度.

定理 1.5.1 设 X 为  $(E, \mathcal{E})$  上的以  $\mu$  为强度的整数值随机测度, 则 X 是泊松随机测度的充要条件是对任意的  $\theta_{1}, \theta_{2}, \cdots, \theta_{n} \in R$  和两两不相交的  $B_{1}, B_{2}, \cdots, B_{n} \in E$  当  $\mu(B_{1}) < \infty, \mu(B_{2}) < \infty, \cdots, \mu(B_{n}) < \infty$  时有

$$
\mathbf {E} \exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} X (B _ {k}) \right\} = \exp \left\{\sum_ {k = 1} ^ {n} (\mathrm{e} ^ {\mathrm{i} \theta_ {k}} - 1) \mu (B _ {k}) \right\}. \tag {1.5.3}
$$

证明 只需注意 (1.5.3) 式成立当且仅当  $X(B_{1}), X(B_{2}), \cdots, X(B_{n})$  独立且分别服从参数为  $\mu(B_{1}), \mu(B_{2}), \cdots, \mu(B_{n})$  的泊松分布. □

定理 1.5.2 设  $\mu$  为非零有限测度. 令  $\eta$  是以  $\mu(E)$  为参数的泊松随机变量, 而  $\xi_{1}, \xi_{2}, \cdots$  是取值于  $(E, \mathcal{E})$  的随机变量且有相同的分布  $\mu(E)^{-1}\mu$ . 再设  $\eta, \xi_{1}, \xi_{2}, \cdots$  相互独立, 则  $X := \sum_{j=1}^{\eta} \delta_{\xi_{j}}$  是以  $\mu$  为强度的泊松随机测度.

证明 显然 X 满足 (1.5.1)式. 根据关于  $\eta, \xi_{1}, \xi_{2}, \cdots$  的分布和独立性的假定, 对于  $\theta_{1}, \theta_{2}, \cdots, \theta_{n} \in R$  和两两不交的  $B_{1}, B_{2}, \cdots, B_{n} \in E$  有

$$
\begin{array}{l} \mathbf {E} \exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} X (B _ {k}) \right\} = \sum_ {m = 0} ^ {\infty} \mathbf {P} (\eta = m) \mathbf {E} \exp \left\{\mathrm{i} \sum_ {j = 1} ^ {m} \sum_ {k = 1} ^ {n} \theta_ {k} \delta_ {\xi_ {j}} (B _ {k}) \right\} \\ = \sum_ {m = 0} ^ {\infty} \mathrm{e} ^ {- \mu (E)} \frac {\mu (E) ^ {m}}{m !} \mathbf {E} \exp \left\{\mathrm{i} \sum_ {j = 1} ^ {m} \sum_ {k = 1} ^ {n} \theta_ {k} 1 _ {B _ {k}} (\xi_ {j}) \right\} \\ = \sum_ {m = 0} ^ {\infty} \mathrm{e} ^ {- \mu (E)} \frac {1}{m !} \left[ \int_ {E} \exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} 1 _ {B _ {k}} (x) \right\} \mu (\mathrm{d} x) \right] ^ {m} \\ = \exp \left\{- \mu (E) + \int_ {E} \exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} 1 _ {B _ {k}} (x) \right\} \mu (\mathrm{d} x) \right\} \\ = \exp \left\{\int_ {E} \left(\exp \left\{\mathrm{i} \sum_ {k = 1} ^ {n} \theta_ {k} 1 _ {B _ {k}} (x) \right\} - 1\right) \mu (\mathrm{d} x) \right\} \\ = \exp \left\{\int_ {E} \sum_ {k = 1} ^ {n} (\mathrm{e} ^ {\mathrm{i} \theta_ {k}} - 1) 1 _ {B _ {k}} (x) \mu (\mathrm{d} x) \right\} \\ = \exp \left\{\sum_ {k = 1} ^ {n} (\mathrm{e} ^ {\mathrm{i} \theta_ {k}} - 1) \mu (B _ {k}) \right\}. \\ \end{array}
$$

由定理 1.5.1 知 X 是以  $\mu$  为强度的泊松随机测度. □

基于定理 1.5.1 和定理 1.5.2, 显然有下面的:

定理 1.5.3 设  $\mu$  是无限的  $\sigma$  有限测度, 而  $\{E_{k}\} \subseteq E$  是两两不相交集合列, 满足  $\bigcup_{k=1}^{\infty} E_{k} = E$  且对每个  $k \geqslant 1$  有  $0 < \mu(E_{k}) < \infty$  且. 令  $\mu_{k}$  为  $\mu$  在  $E_{k}$  上的限制, 即对任何  $B \in E$  有  $\mu_{k}(B) = \mu(B \cap E_{k})$ . 令  $\{X_{k}\}$  为 E 上的独立泊松随机测度列, 其中  $X_{k}$  有强度  $\mu_{k}$ . 对  $B \in E$  令  $X(B) = \sum_{k=1}^{\infty} X_{k}(B)$ . 则  $X = \{X(B) : B \in E\}$  是以  $\mu$  为强度的泊松随机测度.

## 1.5.2 积分和补偿的测度

设 $X$ 为定义在某个概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上以 $(E, \mathcal{E})$ 上的 $\sigma$ 有限测度 $\mu$ 为强度的整数值随机测度. 由 (1.5.1) 式知映射 $B \mapsto X(B)$ 的确是 $(E, \mathcal{E})$ 上的 $\sigma$ 有限测度. 因此可以考虑 $E$ 上的可测函数 $f$ 相对于 $X$ 的积分

$$
\int_ {E} f (x) X (\mathrm{d} x) = \int_ {E} f ^ {+} (x) X (\mathrm{d} x) - \int_ {E} f ^ {-} (x) X (\mathrm{d} x),
$$

其中 $f^{\pm}$ 分别表示 $f$ 的正负部. 这里当然需要假定上式右端的两个积分中至少有一个有限. 为简化记号, 我们将上面的积分记为 $X(f)$. 特别地, 当 $f$ 为 $\mu$ 可积函数时, 通过

简单函数逼近的方法易证

$$
\mathbf {E} [ X (f) ] = \mu (f). \tag {1.5.4}
$$

定理 1.5.2 给出了有限强度泊松随机测度 X 的具体构造或表示. 在这种情况下, 显然有

$$
X (f) = \sum_ {i = 1} ^ {\eta} f (\xi_ {i}).
$$

更一般地, 若 X 由定理 1.5.3 给出, 则 f 相对于 X 的积分可以表示为

$$
X (f) = \sum_ {k = 1} ^ {\infty} X _ {k} (f) = \sum_ {k = 1} ^ {\infty} X _ {k} (f ^ {+}) - \sum_ {k = 1} ^ {\infty} X _ {k} (f ^ {-}).
$$

这里要求上式右端的级数中至少有一个有限.

定理 1.5.4 设 X 为  $(E, \mathcal{E})$  上的以  $\sigma$  有限测度  $\mu$  为强度的整数值随机测度, 则 X 是泊松随机测度当且仅当对  $(E, \mathcal{E})$  上的任何  $\mu$  可积函数 f 有

$$
\mathrm{Ee} ^ {\mathrm{i} X (f)} = \exp \Big \{\int_ {E} (\mathrm{e} ^ {\mathrm{i} f (x)} - 1) \mu (\mathrm{d} x) \Big \}. \tag {1.5.5}
$$

证明 注意 $|\mathrm{e}^{\mathrm{i}f} - 1| \leqslant |f|$. 所以当 $f$ 为 $\mu$ 可积函数时 (1.5.5) 式右边关于 $\mu$ 的积分有限. 设 $X$ 为以 $\mu$ 为强度的泊松随机测度. 若 $B_1, B_2, \dots, B_n \in \mathcal{E}$ 两两不相交且 $\mu(B_1) < \infty$, $\mu(B_2) < \infty, \dots, \mu(B_n) < \infty$, 则 $X(B_1), X(B_2), \dots, X(B_n)$ 相互独立且分别服从参数为 $\mu(B_1), \mu(B_2), \dots, \mu(B_n)$ 的泊松分布. 因此对任何实数 $\theta_1, \theta_2, \dots, \theta_n$ (1.5.3) 式成立. 这说明 (1.5.5) 式对于 $\mu$ 可积的简单函数 $f = \sum_{k=1}^{n} \theta_k 1_{B_k}$ 成立. 利用简单函数列的逼近和控制收敛定理, 易证 (1.5.5) 式对于任何 $\mu$ 可积函数 $f$ 成立. 反之, 假设 (1.5.5) 式对任意的 $\mu$ 可积函数 $f \in \mathcal{E}$ 成立. 取 $B_1, B_2, \dots, B_n \in \mathcal{E}$ 两两不相交且满足 $\mu(B_1) < \infty, \mu(B_2) < \infty, \dots, \mu(B_n) < \infty$. 对于 $\mu$ 可积的简单函数 $f = \sum_{k=1}^{n} \theta_k 1_{B_k}$ 应用 (1.5.5) 式得 (1.5.3)式, 再由定理 1.5.1 即知 $X$ 是以 $\mu$ 为强度的泊松随机测度. □

定理 1.5.5 设  $\mu$  是  $(E, \mathcal{E})$  上的  $\sigma$  有限测度, 而  $\phi$  是由  $(E, \mathcal{E})$  到可测空间  $(F, \mathcal{F})$  的可测映射, 且像测度  $\mu \circ \phi^{-1}$  也是  $\sigma$  有限测度. 若 X 是以  $\mu$  为强度的泊松随机测度, 则像测度  $X \circ \phi^{-1}$  是以  $\mu \circ \phi^{-1}$  为强度的泊松随机测度.

证明 注意对 $(F, \mathcal{F})$ 上的任何 $\mu \circ \phi^{-1}$ 可积函数 $f$ 有 $\mu \circ \phi^{-1}(f) = \mu (\phi \circ f)$ 和 $X \circ \phi^{-1}(f) = X(\phi \circ f)$, 应用定理 1.5.4 即得结论. □

给定以 $\sigma$ 有限测度 $\mu$ 为强度的整数值随机测度 $X$, 其补偿的测度指的是随机的符号测度 $\tilde{X} := X - \mu$, 而 $E$ 上的函数 $f$ 关于该补偿的测度的积分自然定义为 $\tilde{X}(f) = X(f) - \mu(f)$, 该表达式对于任何 $\mu$ 可积函数 $f$ 有意义.

对于泊松随机测度 $X$, 关于其补偿的测度的积分可以做进一步的扩展. 设 $f$ 和 $f^2$ 都关于 $\mu$ 可积. 通过简单函数逼近的方法易证

$$
\mathbf {E} [ X (f) ^ {2} ] = \mu (f ^ {2}) + \mu (f) ^ {2}, \quad \mathbf {E} [ \tilde {X} (f) ^ {2} ] = \mu (f ^ {2}).
$$

对于一般的 $\mu$ 平方可积函数 $f$, 可取函数列 $\{f_n\}$, 其中每个 $f_n$ 关于 $\mu$ 可积且平方可积, 同时当 $n \to \infty$ 时有 $\mu(|f_n - f|^2) \to 0$. 这样 $\{f_n\}$ 就是 $L^2(\mu)$ 中的基本列, 即当 $m, n \to \infty$ 时有 $\mu(|f_m - f_n|^2) \to 0$. 注意

$$
\mathbf {E} [ | \tilde {X} (f _ {m}) - \tilde {X} (f _ {n}) | ^ {2} ] = \mu (| f _ {m} - f _ {n} | ^ {2}).
$$

因此随机变量序列 $\{\tilde{X}(f_n)\}$ 是 $L^2 (\mathbf{P})$ 中的基本列. 于是存在几乎必然意义下唯一的平方可积随机变量 $\tilde{X}(f)$ 使当 $n\to \infty$ 时有 $\mathbf{E}[|\tilde{X} (f_n) - \tilde{X} (f)|^2 ]\to 0.$ 我们称 $\tilde{X}(f)$ 为 $f$ 关于 $\tilde{X}$ 的积分. 由上式易得

$$
\mathbf {E} [ \tilde {X} (f) ^ {2} ] = \mu (f ^ {2}).
$$

## 1.5.3 随机测度的应用

随机测度在随机过程的研究中有很多重要的应用. 作为泊松随机测度的应用, 下面给出复合泊松过程的另外一种构造. 设 $\nu$ 是 $\mathbb{R}$ 上的非零有限测度且有 $\nu(\{0\}) = 0$. 设 $N(\mathrm{ds}, \mathrm{dz})$ 是 $(0, \infty) \times \mathbb{R}$ 上的以 $\mathrm{ds}\nu(\mathrm{dz})$ 为强度的泊松随机测度, 其中 $\mathrm{ds}$ 表示勒贝格测度, 而 $X_0$ 是与之独立的随机变量. 令

$$
X _ {t} = X _ {0} + \int_ {(0, t ]} \int_ {\mathbb {R}} z N (\mathrm{d} s, \mathrm{d} z), \quad t \geqslant 0. \tag {1.5.6}
$$

记 $N_{t} = N((0,t]\times \mathbb{R})$ ，由定义1.5.2中的性质，易知 $(N_{t})$ 是以 $\alpha := \nu (\mathbb{R})$ 为参数的泊松过程.

命题 1.5.6 令  $S = \inf\{t \geqslant 0 : N_{t} > 0\}$  为  $(N_{t})$  首次跳跃的时刻, 则  $(X_{t})$  在此时刻的跳幅  $\Delta X_{S} := X_{S} - X_{S-}$  服从分布  $\mu := \alpha^{-1}\nu$ .

证明 注意 $S$ 也是 $(X_{t})$ 首次跳跃的时刻. 对 $n \geqslant 1$ 令 $\tau_{n} = \inf \{k / 2^{n} > 0 : X_{k / 2^{n}} \neq i\}$. 显然 $\{\tau_{n}\}$ 为递降的停时列, 并且 $\tau_{n} \geqslant S$, 故 $\tau := \lim_{n \to \infty} \tau_{n} \geqslant S$. 显然, 对任何 $k / 2^{n} < \tau$ 有 $X_{k / 2^{n}} = i$. 由轨道右连续性, 对任何 $t \in [0, \tau)$ 有 $X_{t} = i$. 这意味着 $S \geqslant \tau$, 故得 $S = \lim_{n \to \infty} \tau_{n}$. 因为 $\mathbf{P}_{i}(S = t) = 0$, 利用控制收敛定理得

$$
\mathbf {P} (S \leqslant t) = \mathbf {P} (S <   t) = \lim _ {n \to \infty} \mathbf {P} (\tau_ {n} <   t) \leqslant \lim _ {n \to \infty} \mathbf {P} (\tau_ {n} \leqslant t) \leqslant \mathbf {P} (S \leqslant t).
$$

再由过程轨道的右连续性得

$$
\mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta \varDelta X _ {S}}; S \leqslant t) = \lim _ {n \to \infty} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta \varDelta X _ {S}}; \tau_ {n} \leqslant t) = \lim _ {n \to \infty} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta Z _ {k}}; \tau_ {n} = k / 2 ^ {n}),
$$

其中  $Z_{k}=X_{k/2^{n}}-X_{(k-1)/2^{n}}$ . 根据泊松随机测度的独立增量性,

$$
\begin{array}{l} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta Z _ {k}}; \tau_ {n} = k / 2 ^ {n}) \\ = \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta (X _ {k / 2 ^ {n}} - X _ {(k - 1) / 2 ^ {n}})}; N _ {(k - 1) / 2 ^ {n}} = 0, N _ {k / 2 ^ {n}} - N _ {(k - 1) / 2 ^ {n}} \geqslant 1) \\ = \mathbf {P} (N _ {(k - 1) / 2 ^ {n}} = 0) \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta (X _ {k / 2 ^ {n}} - X _ {(k - 1) / 2 ^ {n}})}; N _ {k / 2 ^ {n}} - N _ {(k - 1) / 2 ^ {n}} \geqslant 1) \\ = \mathrm{e} ^ {- \alpha (k - 1) / 2 ^ {n}} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta (X _ {1 / 2 ^ {n}} - X _ {0})}; N _ {1 / 2 ^ {n}} \geqslant 1) \\ = \mathrm{e} ^ {- \alpha (k - 1) / 2 ^ {n}} \mathbf {E} [ \mathrm{e} ^ {\mathrm{i} \theta (X _ {1 / 2 ^ {n}} - X _ {0})} (1 - 1 _ {\{N _ {1 / 2 ^ {n}} = 0 \}}) ] \\ = \mathrm{e} ^ {- \alpha (k - 1) / 2 ^ {n}} \left[ \exp \left\{\frac {1}{2 ^ {n}} \int_ {\mathbb {R}} (\mathrm{e} ^ {\mathrm{i} \theta z} - 1) \nu (\mathrm{d} z) \right\} - \mathrm{e} ^ {- \alpha / 2 ^ {n}} \right] \\ = \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \left[ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta z} \mu (\mathrm{d} z) \right\} - 1 \right]. \\ \end{array}
$$

回到上面的等式得

$$
\begin{array}{l} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} \theta \Delta X _ {S}}; S \leqslant t) = \lim _ {n \to \infty} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \Big [ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta z} \mu (\mathrm{d} z) \right\} - 1 \Big ] \\ = \lim _ {n \to \infty} \frac {\mathrm{e} ^ {- \alpha / 2 ^ {n}} [ 1 - \mathrm{e} ^ {- \alpha \lfloor 2 ^ {n} t \rfloor / 2 ^ {n}} ]}{1 - \mathrm{e} ^ {- \alpha / 2 ^ {n}}} \Big [ \exp \Big \{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta z} \mu (\mathrm{d} z) \Big \} - 1 \Big ] \\ = (1 - \mathrm{e} ^ {- \alpha t}) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta z} \mu (\mathrm{d} z). \\ \end{array}
$$

在上式中令  $t \rightarrow \infty$  即知  $\Delta X_{S}$  服从分布  $\mu$ . □

定理 1.5.7 由 (1.5.6) 式定义的  $(X_{t}: t \geqslant 0)$  是有跳跃速率  $\alpha$  和跳跃分布  $\mu := \alpha^{-1}\nu$  的复合泊松过程.

证明 令 $S_{k}$ 为 $(N_{t})$ 的第 $k$ 次跳跃发生的时刻。我们需要证明跳幅 $\Delta X_{S_k} = X_{S_k} - X_{S_{k-}}$, $k = 1,2,\cdots$ 独立且服从相同的分布 $\mu$。为简单起见，下面只证明关于前两个跳幅的结论。有兴趣的读者可以参考下面的论证方法自行完成一般情况的证明。对 $n \geqslant 0$ 令 $D_n = \{i/2^n : i = 0,1,2,\cdots\}$。再令 $\tau_{k,n} = \inf \{t \in D_n : t > S_k\}$ 为 $S_k$ 的二分点离散化。显然序列 $\{S_k\}$ 是严格增的。对 $t \geqslant 0$ 和 $\theta_1, \theta_2 \in \mathbb{R}$，与命题1.5.6的证明中类似地有

$$
\begin{array}{l} \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} \Delta X _ {S _ {1}} + \theta_ {2} \Delta X _ {S _ {2}})}; S _ {2} \leqslant t \big) \\ = \lim _ {n \to \infty} \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} \varDelta X _ {S _ {1}} + \theta_ {2} \varDelta X _ {S _ {2}})}; \tau_ {2, n} \leqslant t \big) \\ = \lim _ {n \to \infty} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \sum_ {j = 1} ^ {k} \mathbf {E} (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} Z _ {j} + \theta_ {2} Z _ {k})}; \tau_ {1, n} = j / 2 ^ {n}, \tau_ {2, n} = k / 2 ^ {n}), \tag {1.5.7} \\ \end{array}
$$

其中 $Z_{k} = X_{k / 2^{n}} - X_{(k - 1) / 2^{n}}$ .注意

$$
\sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathbf {P} \big (\tau_ {1, n} = \tau_ {2, n} = k / 2 ^ {n} \big)
$$

$$
\begin{array}{l} = \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathbf {P} \big (N _ {(k - 1) / 2 ^ {n}} = 0, N _ {k / 2 ^ {n}} - N _ {(k - 1) / 2 ^ {n}} \geqslant 2 \big) \\ = \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathrm{e} ^ {- \alpha (k - 1) / 2 ^ {n}} \left(1 - \mathrm{e} ^ {- \alpha / 2 ^ {n}} - \frac {\alpha}{2 ^ {n}} \mathrm{e} ^ {- \alpha / 2 ^ {n}}\right) \\ \leqslant 2 ^ {n} t \Big (1 - \mathrm{e} ^ {- \alpha / 2 ^ {n}} - \frac {\alpha}{2 ^ {n}} \mathrm{e} ^ {- \alpha / 2 ^ {n}} \Big). \\ \end{array}
$$

所以有

$$
\lim _ {n \to \infty} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \mathbf {P} \big (\tau_ {1, n} = \tau_ {2, n} = k / 2 ^ {n} \big) = 0.
$$

另一方面, 当 $1 \leqslant j \leqslant k - 1$ 时有

$$
\begin{array}{l} \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} Z _ {j} + \theta_ {2} Z _ {k})}; \tau_ {1, n} = j / 2 ^ {n}, \tau_ {2, n} = k / 2 ^ {n} \big) \\ = \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} \left(\theta_ {1} Z _ {j} + \theta_ {2} Z _ {k}\right)} 1 _ {\left\{N _ {(j - 1) / 2 ^ {n}} = 0 \right\}} 1 _ {\left\{N _ {j / 2 ^ {n}} - N _ {(j - 1) / 2 ^ {n}} \geqslant 1 \right\}}. \\ \left. 1 _ {\{N _ {(k - 1) / 2 ^ {n}} - N _ {j / 2 ^ {n}} = 0 \}} 1 _ {\{N _ {k / 2 ^ {n}} - N _ {(k - 1) / 2 ^ {n}} \geqslant 1 \}}\right) \\ = \mathbf {E} \big (N _ {(j - 1) / 2 ^ {n}} = 0 \big) \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} \theta_ {1} Z _ {j}} 1 _ {\{N _ {j / 2 ^ {n}} - N _ {(j - 1) / 2 ^ {n}} \geqslant 1 \}} \big)  . \\ \mathbf {E} \big (N _ {(k - 1) / 2 ^ {n}} - N _ {j / 2 ^ {n}} = 0 \big) \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} \theta_ {2} Z _ {k}}) 1 _ {\{N _ {k / 2 ^ {n}} - N _ {(k - 1) / 2 ^ {n}} \geqslant 1 \}}\left. \right) \\ = \mathrm{e} ^ {- \alpha (k - 2) / 2 ^ {n}} \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} \theta_ {1} Z _ {1}}; N _ {1 / 2 ^ {n}} \geqslant 1 \big) \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} \theta_ {2} Z _ {1}}; N _ {1 / 2 ^ {n}} \geqslant 1 \big) \\ = \mathrm{e} ^ {- \alpha (k - 2) / 2 ^ {n}} \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} \theta_ {1} Z _ {1}} (1 - 1 _ {\{N _ {1 / 2 ^ {n}} = 0 \}}) \big ] \mathbf {E} \big [ \mathrm{e} ^ {\mathrm{i} \theta_ {2} Z _ {1}} (1 - 1 _ {\{N _ {1 / 2 ^ {n}} = 0 \}}) \big ] \\ = \mathrm{e} ^ {- \alpha (k - 2) / 2 ^ {n}} \left[ \exp \left\{\frac {1}{2 ^ {n}} \int_ {\mathbb {R}} (\mathrm{e} ^ {\mathrm{i} \theta_ {1} z} - 1) \nu (\mathrm{d} z) \right\} - \mathrm{e} ^ {- \alpha / 2 ^ {n}} \right]. \\ \left[ \exp \left\{\frac {1}{2 ^ {n}} \int_ {\mathbb {R}} (\mathrm{e} ^ {\mathrm{i} \theta_ {2} z} - 1) \nu (\mathrm{d} z) \right\} - \mathrm{e} ^ {- \alpha / 2 ^ {n}} \right] \\ = \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \Big [ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \right\} - 1 \Big ]. \\ \left[ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z) \right\} - 1 \right]. \\ \end{array}
$$

根据上面的计算, 回到 (1.5.7) 式有

$$
\begin{array}{l} \mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} \varDelta X _ {S _ {1}} + \theta_ {2} \varDelta X _ {S _ {2}})}; S _ {2} \leqslant t \big) \\ = \lim _ {n \to \infty} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \sum_ {j = 1} ^ {k - 1} \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \Big [ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \right\} - 1 \Big ]. \\ \left[ \exp \left\{\frac {\alpha}{2 ^ {n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z) \right\} - 1 \right] \\ = \lim _ {n \to \infty} \alpha^ {2} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} \sum_ {j = 1} ^ {k - 1} \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \frac {1}{2 ^ {2 n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z) \\ \end{array}
$$

$$
\begin{array}{l} = \lim _ {n \to \infty} \alpha^ {2} \sum_ {k = 1} ^ {\lfloor 2 ^ {n} t \rfloor} (k - 1) \mathrm{e} ^ {- \alpha k / 2 ^ {n}} \frac {1}{2 ^ {2 n}} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z) \\ = \alpha^ {2} \int_ {0} ^ {t} s \mathrm{e} ^ {- \alpha s} \mathrm{d} s \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z) \\ = \left(1 - \mathrm{e} ^ {- \alpha t} - \alpha t \mathrm{e} ^ {- \alpha t}\right) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z). \\ \end{array}
$$

在上式中令 $t\to \infty$ 时得

$$
\mathbf {E} \big (\mathrm{e} ^ {\mathrm{i} (\theta_ {1} \varDelta X _ {S _ {1}} + \theta_ {2} \varDelta X _ {S _ {2}})} \big) = \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {1} z} \mu (\mathrm{d} z) \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \theta_ {2} z} \mu (\mathrm{d} z).
$$

所以跳幅  $\Delta X_{S_{1}}$  和  $\Delta X_{S_{2}}$  独立且服从相同的分布  $\mu$ . ☐

设 $q$ 为 $\mathbb{R}$ 上的非负博雷尔可测函数, 而 $\mu$ 是 $\mathbb{R}$ 上的 $\sigma$ 有限测度. 再设 $\mu(\{0\}) = 0$ 且 $0 < \beta := \mu(q) < \infty$. 令 $N(\mathrm{d}s, \mathrm{d}z, \mathrm{d}u)$ 是 $(0, \infty) \times \mathbb{R} \times (0, \infty)$ 上的以 $\mathrm{d}s\mu(\mathrm{d}z)\mathrm{d}u$ 为强度的泊松随机测度, 而 $Z_0$ 是与之独立的随机变量. 再令

$$
Z _ {t} = Z _ {0} + \int_ {0} ^ {t} \int_ {\mathbb {R}} \int_ {0} ^ {q (z)} z N (\mathrm{d} s, \mathrm{d} z, \mathrm{d} u), \quad t \geqslant 0. \tag {1.5.8}
$$

定理 1.5.8 由 (1.5.8) 式定义的  $(Z_{t}: t \geqslant 0)$  是有跳跃速率  $\beta$  和跳跃分布  $\beta^{-1} q(z)$   $\mu(\mathrm{d}z)$  的复合泊松过程.

证明 令 $N_{q}(\mathrm{d}s,\mathrm{d}z)$ 为 $1_{\{u\leqslant q(z)\}}N(\mathrm{d}s,\mathrm{d}z,\mathrm{d}u)$ 在映射 $(s,z,u)\mapsto (s,z)$ 之下的像测度.应用定理1.5.5不难证明 $N_{q}(\mathrm{d}s,\mathrm{d}z)$ 是 $(0,\infty)\times \mathbb{R}$ 上的以 $q(z)\mathrm{d}s\mu (\mathrm{d}z)$ 为强度的泊松随机测度,而且与 $Z_0$ 独立.由(1.5.8)式有

$$
Z _ {t} = Z _ {0} + \int_ {0} ^ {t} \int_ {\mathbb {R}} z N _ {q} (\mathrm{d} s, \mathrm{d} z), \quad t \geqslant 0.
$$

再根据定理 1.5.7 即得欲证结论. □

## 练习题

1. 在定理 1.4.8 的条件下, 证明:

(1) $(N_{s+t}-N_{s}:t\geqslant0)$ 是以 $\alpha\geqslant0$ 为参数的零初值泊松过程,而 $\{\xi_{N_{s}+n}:n\geqslant1\}$ 是与之独立的独立同分布随机变量序列且有分布 $\mu;$
(2) 定理 1.4.8 中定义的过程  $(X_{t}: t \geqslant 0)$  满足定理 1.4.8 中的性质 (2).

2. 设 $\mu$ 是可测空间 $(E, \mathcal{E})$ 上的 $\sigma$ 有限测度. 证明 $(E, \mathcal{E})$ 上的以 $\mu$ 为强度的整数值随机测度 $X$ 是泊松随机测度当且仅当对 $(E, \mathcal{E})$ 上的任何非负可测函数 $f$ 有

$$
\mathrm{Ee} ^ {- X (f)} = \exp \bigg \{- \int_ {E} (1 - \mathrm{e} ^ {- f (x)}) \mu (\mathrm{d} x) \bigg \}.
$$

3. 令 $X$ 是 $(E, \mathcal{E})$ 上的以有限测度 $\mu$ 为强度的泊松随机测度. 证明对任意的 $f, g \in \mathrm{p}\mathcal{E}$, 有

(1) $\mathbf{E}[X(f)\mathrm{e}^{-X(g)}] = \mu (f\mathrm{e}^{-g})\mathbf{E}[\mathrm{e}^{-X(g)}]$;
(2) $\mathbf{E}[X(f)^2\mathrm{e}^{-X(g)}] = [\mu (f^2\mathrm{e}^{-g}) + \mu (f\mathrm{e}^{-g})^2 ]\mathbf{E}[\mathrm{e}^{-X(g)}];$
(3) $\mathbf{E}[\tilde{X}(f)^4] = \mu(f^4) + 3\mu(f^2)^2.$

鞅是一类非常重要的随机过程. 从条件期望的观点看, 鞅具有相对平稳性. 鞅方法是现代随机过程理论中最重要的工具之一. 本章介绍鞅论的基本结果, 包括鞅 (上、下鞅) 的概念、离散时间下鞅的不等式、有界停止定理、收敛定理、连续时间鞅论等. 作为预备知识, 回顾了期望和条件期望的基本性质, 并对流和停时进行了简单的讨论.

## 2.1 预备知识

## 2.1.1 数学期望

考虑概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$. 设 $\xi$ 为此概率空间上的随机变量. 令 $\mu_{\xi}$ 和 $F_{\xi}$ 分别为 $\xi$ 在 $\mathbb{R}^d$ 上的概率分布和分布函数. 若 $f$ 为 $\mathbb{R}^d$ 上的博雷尔可测函数, 则随机变量 $f(\xi)$ 的数学期望可表示为斯蒂尔切斯积分

$$
\mathbf {E} f (\xi) = \int_ {\mathbb {R} ^ {d}} f (x) \mathrm{d} F _ {\xi} (x), \tag {2.1.1}
$$

或者用测度积分表示为

$$
\mathbf {E} f (\xi) = \int_ {\Omega} f (\xi (\omega)) \mathbf {P} (\mathrm{d} \omega) = \int_ {\mathbb {R} ^ {d}} f (x) \mu_ {\xi} (\mathrm{d} x). \tag {2.1.2}
$$

若  $\mathbf{E}|f(\xi)|<\infty,$  则称随机变量  $f(\xi)$  是可积的.

值得指出的是, 上面借助斯蒂尔切斯积分定义数学期望的方法有一定的局限性. 例如, 即使 $f$ 为 $\mathbb{R}^d$ 上的有界博雷尔可测函数, (2.1.1) 式右边的积分也可能没有意义. 利用测度积分的表示 (2.1.2) 式则没有这样的问题. 不过对于本书中所遇到的函数, 上面两种积分都是有意义的. 想了解关于测度的严格积分理论的读者, 可以参考高等概率论的著作. 根据本书上册中的讨论, 关于数学期望有如下的定理:

定理 2.1.1 设可积随机变量  $\xi$  和  $\eta$  关于子  $\sigma$  代数  $G \subseteq F$  可测, 则  $\mathbf{P}(\xi \leqslant \eta) = 1$  当且仅当对任何  $A \in G$  都有  $\mathbf{E}(\xi 1_{A}) \leqslant \mathbf{E}(\eta 1_{A})$ .

推论 2.1.2 设可积随机变量  $\xi$  和  $\eta$  关于子  $\sigma$  代数  $G \subseteq F$  可测, 则  $\mathbf{P}(\xi = \eta) = 1$  当且仅当对任何  $A \in G$  都有  $\mathbf{E}(\xi 1_{A}) = \mathbf{E}(\eta 1_{A})$ .

定理 2.1.3 (单调收敛定理) 设  $\xi, \xi_{n}, n = 1, 2, \cdots$  为非负随机变量且单调不降地有  $\lim_{n \to \infty} \xi_{n} \stackrel{a.s.}{=} \xi$ ，则有  $\lim_{n \to \infty} E\xi_{n} = E\xi$ .

定理 2.1.4 (法图 (Fatou) 定理) 对于任何非负随机变量  $\xi_{n}, n = 1, 2, \cdots$ ，有

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \xi_ {n} \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} \big). \tag {2.1.3}
$$

定理 2.1.5（控制收敛定理） 设随机变量  $\xi, \xi_{n}, n = 1, 2, \cdots$  满足  $\lim_{n \to \infty} \xi_{n} \stackrel{a.s.}{=} \xi$ .
若有非负可积随机变量  $\eta$  使得  $|\xi_{n}| \leqslant \eta$  (a.s.),  $n = 1, 2, \cdots$ ，则有  $\lim_{n \to \infty} E\xi_{n} = E\xi$ .

上面的控制收敛定理的条件可以弱化. 称 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的一列随机变量 $\{\xi_n\}$ 是一致可积的, 是指当 $c \to \infty$ 时有

$$
\sup _ {n \geqslant 1} \mathbf {E} \big (| \xi_ {n} | 1 _ {\{| \xi_ {n} | \geqslant c \}} \big) \to 0.
$$

特别地, 不难看出对任何  $\alpha > 1$  有

$$
\mathbf {E} (| \xi_ {n} | 1 _ {\{| \xi_ {n} | \geqslant c \}}) \leqslant c ^ {1 - \alpha} \mathbf {E} (| \xi_ {n} | ^ {\alpha} 1 _ {\{| \xi_ {n} | \geqslant c \}}) \leqslant c ^ {1 - \alpha} \mathbf {E} (| \xi_ {n} | ^ {\alpha}).
$$

因此, 若 $\sup_{n\geqslant 1}\mathbf{E}(|\xi_n|^{\alpha}) < \infty$ ，则 $\{\xi_n\}$ 是一致可积的.

定理 2.1.6 设随机变量  $\xi, \xi_{1}, \xi_{2}, \cdots$  满足  $\lim_{n\to\infty}\xi_{n}\stackrel{a.s.}{=} \xi$ . 若序列  $\{\xi_{n}\}$  一致可积,
则有  $\lim_{n\to\infty}\mathbf{E}\xi_{n}=\mathbf{E}\xi.$

证明 由一致可积性, 对任何 $\varepsilon > 0$, 当 $c(c > 0)$ 充分大时有

$$
\sup _ {n \geqslant 1} \mathbf {E} \big (\xi_ {n} 1 _ {\{\xi_ {n} <   - c \}} \big) \geqslant - \sup _ {n \geqslant 1} \mathbf {E} \big (| \xi_ {n} | 1 _ {\{| \xi_ {n} | > c \}} \big) \geqslant - \varepsilon .
$$

因此有

$$
\mathbf {E} \xi_ {n} = \mathbf {E} \big (\xi_ {n} 1 _ {\{\xi_ {n} \geqslant - c \}} \big) + \mathbf {E} \big (\xi_ {n} 1 _ {\{\xi_ {n} <   - c \}} \big) \geqslant \mathbf {E} \big (\xi_ {n} 1 _ {\{\xi_ {n} \geqslant - c \}} \big) - \varepsilon .
$$

对 $(\xi_{n} - c)1_{\{\xi_{n}\geqslant -c\}}$ 应用法图定理可得

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \big (\xi_ {n} 1 _ {\{\xi_ {n} \geqslant - c \}} \big) \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} 1 _ {\{\xi_ {n} \geqslant - c \}} \big) \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} \big).
$$

因此有

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \xi_ {n} \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} \big) - \varepsilon .
$$

再由 $\varepsilon > 0$ 的任意性得

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} \xi_ {n} \geqslant \mathbf {E} \big (\operatorname * {l i m i n f} _ {n \to \infty} \xi_ {n} \big).
$$

类似地, 可得

$$
\operatorname * {l i m s u p} _ {n \to \infty} \mathbf {E} \xi_ {n} \leqslant \mathbf {E} \big (\operatorname * {l i m s u p} _ {n \to \infty} \xi_ {n} \big).
$$

因为  $\lim_{n\to\infty}\xi_{n}\stackrel{a.s.}{=} \xi,$  以上二式右边的积分都等于  $E\xi,$  故欲证结果成立. □

值域为有限集合的可测函数称为简单函数. 根据上面的关于数学期望的收敛定理, 经常可以利用结构较为简单的随机变量的期望逼近一般随机变量的期望. 典型的做法如下: 对于整数 $n \geqslant 1$ 令

$$
\phi_ {n} (x) = n 1 _ {\{x \geqslant n \}} + \sum_ {k = 1} ^ {n 2 ^ {n}} 2 ^ {- n} (k - 1) 1 _ {[ (k - 1) / 2 ^ {n}, k / 2 ^ {n})} (x), \quad x \geqslant 0. \tag {2.1.4}
$$

显然, 对任意的 $x \geqslant 0$ 有 $\phi_n(x) \uparrow x$. 对于非负随机变量 $\xi$, 当 $n \to \infty$ 时有 $\phi_n(\xi) \uparrow \xi$. 再由积分单调收敛定理有 $\mathbf{E}[\phi_n(\xi)] \uparrow \mathbf{E}\xi$.

## 2.1.2 条件数学期望

定义 2.1.1 设 X 为概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的可积随机变量. 考虑子  $\sigma$  代数  $G \subseteq F$ . 如果对于一切事件  $A \in G$  有

$$
\mathbf {E} (1 _ {A} \xi) = \mathbf {E} (1 _ {A} X), \tag {2.1.5}
$$

则称关于 $\mathcal{G}$ 可测的随机变量 $\xi$ 为 $X$ 的给定 $\mathcal{G}$ 的条件数学期望或条件期望, 并记之为 $\mathbf{E}(X|\mathcal{G})$. 对于 $B \in \mathcal{F}$, 称条件期望 $\mathbf{E}(1_B|\mathcal{G})$ 为 $B$ 的给定 $\mathcal{G}$ 的条件概率, 并记之为 $\mathbf{P}(B|\mathcal{G})$.

根据高等概率论中的结果, 满足定义 2.1.1 中要求的随机变量 $\xi$ 存在; 如可参见 [37]. 由推论 2.1.2 知, 该随机变量在几乎必然相等的意义下唯一. 若 $Z$ 是另一随机变量, 我们写 $\mathbf{E}(X|Z) = \mathbf{E}[X|\sigma(Z)]$. 注意, 这个记号与上册中定义的条件期望相吻合.

定理 2.1.7 设 X 和 Y 是概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的可积随机变量, 则有如下性质:

(1)  $\mathbf{E}[\mathbf{E}(X|\mathcal{G})]=\mathbf{E}(X);$
(2) 若 X 与 G 独立, 则  $\mathbf{E}(X|\mathcal{G}) = \mathbf{E}(X)$ ;
(3) 对任何 $a \in \mathbb{R}$ 有 $\mathbf{E}(aX|\mathcal{G}) = a\mathbf{E}(X|\mathcal{G})$;
(4) $\mathbf{E}(X + Y|\mathcal{G}) = \mathbf{E}(X|\mathcal{G}) + \mathbf{E}(Y|\mathcal{G})$;
(5) 若 $X \leqslant Y$, 则有 $\mathbf{E}(X|\mathcal{G}) \leqslant \mathbf{E}(Y|\mathcal{G})$.

证明 在 (2.1.5) 式中取 $A = \Omega$ 即可得性质 (1). 若 $X$ 与 $\mathcal{G}$ 独立, 则对任何 $A \in \mathcal{G}$ 随机变量 $1_A$ 与 $X$ 独立, 故有

$$
\mathbf {E} (1 _ {A} X) = \mathbf {E} (1 _ {A}) \mathbf {E} X = \mathbf {E} (1 _ {A} \mathbf {E} X),
$$

再由推论 2.1.2 知性质 (2) 成立. 对任何 $A \in \mathcal{G}$ 有

$$
\mathbf {E} (1 _ {A} a X) = a \mathbf {E} (1 _ {A} X) = a \mathbf {E} [ 1 _ {A} \mathbf {E} (X | \mathscr {G}) ] = \mathbf {E} [ 1 _ {A} a \mathbf {E} (X | \mathscr {G}) ],
$$

因而性质 (3) 成立. 类似地可以证明性质 (4) 和 (5) 成立. $\square$

定理 2.1.8 设 X 为概率空间  $(\Omega, \mathcal{F}, \mathbf{P})$  上的随机变量且数学期望 EX 存在, 再设  $\xi$  为关于子  $\sigma$  代数  $G \subseteq F$  可测的随机变量, 则  $\xi = \mathbf{E}(X|\mathcal{G})$  当且仅当对任何 G 可测随机变量 Y, 只要  $Y\xi$  或 YX 可积, 就有

$$
\mathbf {E} (Y \xi) = \mathbf {E} (Y X). \tag {2.1.6}
$$

证明 若 (2.1.6) 式成立, 则对 $A \in \mathcal{G}$ 取 $Y = 1_A$ 即知 $\xi = \mathbf{E}(X|\mathcal{G})$. 反之, 假设 $\xi = \mathbf{E}(X|\mathcal{G})$, 下证 (2.1.6) 式成立. 根据数学期望的线性性, 只需考虑 $X, \xi$ 和 $Y$ 都是非负随机变量的情况. 此时, 显然 (2.1.5) 式对于任意的 $A \in \mathcal{G}$ 成立. 因此, 当 $Y$ 是 $\mathcal{G}$ 中有限个集合的示性函数的线性组合时 (2.1.6) 式成立. 特别地, 若 $\phi_n$ 由 (2.1.4) 式给出, 则有 $\mathbf{E}[\phi_n(Y)X] = \mathbf{E}[\phi_n(Y)\xi]$. 令 $n \to \infty$ 并应用单调收敛定理即得 (2.1.6) 式. □

推论 2.1.9 设 X, Y 是  $(\Omega, \mathcal{F}, \mathbf{P})$  上的随机变量且 Y 关于 G 可测. 若 X 和 YX 都可积, 则

$$
\mathbf {E} (Y X | \mathcal {G}) = Y \mathbf {E} (X | \mathcal {G}). \tag {2.1.7}
$$

证明 对任何 $A \in \mathcal{G}$, 因 $1_A Y$ 和 $1_A$ 都关于 $\mathcal{G}$ 可测, 应用 (2.1.6) 式得

$$
\mathbf {E} \big [ 1 _ {A} Y \mathbf {E} (X | \mathcal {G}) \big ] = \mathbf {E} (1 _ {A} Y X) = \mathbf {E} \big [ 1 _ {A} \mathbf {E} (Y X | \mathcal {G}) \big ].
$$

又因  $Y\mathbf{E}(X|\mathcal{G})$  关于 G 可测, 故 (2.1.7) 式成立. □

推论 2.1.10 设 X 为可积随机变量, 而  $G_{1} \subseteq G_{2}$  都是 F 的子  $\sigma$  代数, 则

$$
\mathbf {E} \big [ \mathbf {E} (X | \mathcal {G} _ {2}) | \mathcal {G} _ {1} \big ] = \mathbf {E} (X | \mathcal {G} _ {1}).
$$

证明 对任何 $A \in \mathcal{G}_1 \subseteq \mathcal{G}_2$, 应用 (2.1.7) 式得

$$
\mathbf {E} \big \{1 _ {A} \mathbf {E} \big [ \mathbf {E} (X | \mathcal {G} _ {2}) | \mathcal {G} _ {1} \big ] \big \} = \mathbf {E} \big \{\mathbf {E} \big [ \mathbf {E} (1 _ {A} X | \mathcal {G} _ {2}) | \mathcal {G} _ {1} \big ] \big \} = \mathbf {E} (1 _ {A} X).
$$

因  $\mathbf{E}[\mathbf{E}(1_{A}X|\mathcal{G}_{2})|\mathcal{G}_{1}]$  关于  $G_{1}$  可测, 故知欲证结论成立. □

## 2.1.3 流和停时

考虑概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$. 令 $I = \mathbb{Z}_{+}$ 或 $\mathbb{R}_{+}$. 如果 $\mathcal{F}$ 的子 $\sigma$ 代数族 $(\mathcal{F}_t : t \in I)$ 满足对任何 $s < t \in I$ 都有 $\mathcal{F}_s \subseteq \mathcal{F}_t$, 就称它是 $\sigma$ 代数流或简称流. 对应于 $I = \mathbb{Z}_{+}$ 或 $\mathbb{R}_{+}$, 我们也经常将 $(\mathcal{F}_t : t \in I)$ 写为 $(\mathcal{F}_t : t \geqslant 0)$ 或 $(\mathcal{F}_n : n \geqslant 0)$. 直观上, 可以将 $\sigma$ 代数 $\mathcal{F}_t$ 解释为观测某些随机现象到 $t \in I$ 时刻所积累的知识或信息.

称状态空间 $(E, \mathcal{E})$ 上的随机过程 $X = (X_{t}: t \in I)$ 关于某个流 $(\mathcal{F}_{t}: t \in I)$ 是适应的, 是指对任何 $t \in I$, 随机变量 $X_{t}$ 都是 $\mathcal{F}_{t}$ 可测的. 直观上, 过程 $X$ 关于流 $(\mathcal{F}_{t})$ 适应可以解释为 X 的运动情况在我们的观测范围内, 或者说我们到任何时刻 t 积累的知识都包含了 X 在此时刻前的运动情况的所有信息. 给定过程 X, 定义

$$
\mathscr {F} ^ {X} = \sigma (\{X _ {s}: s \in I \}), \mathscr {F} _ {t} ^ {X} = \sigma (\{X _ {s}: s \in I, s \leqslant t \}), \tag {2.1.8}
$$

则 $(\mathcal{F}_t^X: t \in I)$ 构成一个流, 称为 $X$ 的自然流, 称 $(\mathcal{F}^X, \mathcal{F}_t^X: t \in I)$ 为 $X$ 的自然 $\sigma$ 代数. 显然 $X$ 关于其自然流 $(\mathcal{F}_t^X: t \in I)$ 适应, 且它在 $X$ 所适应的流中是最小的.

定义 2.1.2 称映射 $T: \Omega \to I \cup \{\infty\}$ 为关于流 $(\mathcal{F}_t : t \in I)$ 的停时或可选时, 是指对任何 $t \in I$ 都有

$$
\{T \leqslant t \} = \{\omega \in \Omega : T (\omega) \leqslant t \} \in \mathscr {F} _ {t}. \tag {2.1.9}
$$

对于给定的 $(\mathcal{F}_{t})$ 停时T, 定义

$$
\mathcal {F} _ {T} = \{A \in \mathcal {F} _ {\infty}: \text {对任意} t \in I \text {有} A \cap \{T \leqslant t \} \in \mathcal {F} _ {t} \},
$$

其中 $\mathcal{F}_{\infty} = \sigma \left( \bigcup_{t \in I} \mathcal{F}_t \right)$. 易证 $\mathcal{F}_T$ 是一个 $\sigma$ 代数, 称为 $T$ 前 $\sigma$ 代数.

停时 $T$ 是相对于某个流而言的. 当流 $(\mathcal{F}_t)$ 明确时, 我们简单地称 $T$ 为停时. 直观上, 性质 $\{T \leqslant t\} \in \mathcal{F}_t$ 表示根据时刻 $t$ 我们掌握的信息 $\mathcal{F}_t$ 可以判断 $T$ 是否已经在 $t$ 时刻或更早地到来. 停时 $\sigma$ 代数 $\mathcal{F}_T$ 可以解释为到随机时刻 $T$ 我们掌握的所有知识或信息的总和. 不难证明, 停时 $T$ 关于 $\sigma$ 代数 $\mathcal{F}_T$ 可测. 另外, 若 $S$ 和 $T$ 都是停时且 $S \leqslant T$, 则 $\mathcal{G}_S \subseteq \mathcal{G}_T$.

命题 2.1.11 若 S 和 T 是  $(\mathcal{F}_{t})$  的停时, 则  $S \vee T, S \wedge T$  和  $S + T$  也是  $(\mathcal{F}_{t})$  的停时.

证明 由 $\{S \vee T \leqslant t\} = \{S \leqslant t\} \cap \{T \leqslant t\}$ 和 $\{S \wedge T \leqslant t\} = \{S \leqslant t\} \cup \{T \leqslant t\}$ 知 $S \vee T$ 和 $S \wedge T$ 是 $(\mathcal{F}_t)$ 的停时. 若 $I = \mathbb{Z}_+$, 则对 $t \in I$ 有

$$
\{S + T = t \} = \bigcup_ {k = 0} ^ {t} \{S = k, T = t - k \} \in \mathscr {F} _ {t},
$$

因而 $S + T$ 是 $(\mathcal{F}_t)$ 的停时.下面考虑 $I = \mathbb{R}_{+}$ 的情况.此时，对任何 $t\geqslant 0$ 有 $\{S>$ $t\} \cup \{T > t\} \in \mathcal{F}_t.$ 而且

$$
\begin{array}{l} \{S + T > t \} = \{S > t \} \cup \{S + T > t, S \leqslant t \} \\ = \{S > t \} \cup \{t - T <   S \leqslant t \}, \tag {2.1.10} \\ \end{array}
$$

其中  $\{S > t\} \in F_{t}$ . 令 Q 表示有理数集, 则有

$$
\{t - T <   S \leqslant t \} = \bigcup_ {r \in [ 0, t) \cap \mathbb {Q}} \{t - T <   r \leqslant S \leqslant t \}
$$

$$
= \bigcup_ {r \in [ 0, t) \cap \mathbb {Q}} \{T > t - r \} \cap \{S \geqslant r \} \cap \{S \leqslant t \},
$$

其中 $\{T > t - r\} \in \mathcal{F}_{t-r} \subseteq \mathcal{F}_t, \{S \geqslant r\} \in \mathcal{F}_r \subseteq \mathcal{F}_t$ 而 $\{S \leqslant t\} \in \mathcal{F}_t$. 所以 $\{t - T < S \leqslant t\} \in \mathcal{F}_t$. 由 (2.1.10) 式知 $\{S + T > t\} \in \mathcal{F}_t$, 故 $T + S$ 是 $(\mathcal{F}_t)$ 的停时. □

例 2.1.1 映射 $T: \Omega \to \{0, 1, \cdots\} \cup \{\infty\}$ 是关于离散时间流 $(\mathcal{F}_n)$ 的停时当且仅当对任何 $n \geqslant 0$ 都有 $\{T = n\} \in \mathcal{F}_n$. 此时 $A \in \mathcal{F}_T$ 当且仅当对任何 $n \geqslant 0$ 都有 $A \cap \{T = n\} \in \mathcal{F}_n$.

例 2.1.2 设离散时间随机过程  $(X_{n})$  关于流  $(\mathcal{F}_{n})$  适应. 再设 T 为  $(\mathcal{F}_{n})$  的停时, 则对任意的  $n \geqslant 0$  和  $i \in E$  有

$$
\{T <   \infty \} \cap \{X _ {T} = i \} \cap \{T = n \} = \{X _ {n} = i \} \cap \{T = n \} \in \mathcal {G} _ {n},
$$

故有 $\{T < \infty\} \cap \{X_T = i\} \in \mathcal{G}_T$. 这说明映射 $\omega \mapsto X_{T(\omega)}(\omega)$ 限制在 $\{T < \infty\}$ 上关于 $\{T < \infty\} \cap \mathcal{G}_T$ 可测.

设 $X = (X_{t}:t\in I)$ 是以 $E$ 为状态空间的随机过程. 分别称 $\tau_A\coloneqq \inf \{t\in I:X_t\in A\}$ 和 $T_{A}:= \inf \{t\in I:t > 0,X_{t}\in A\}$ 为 $X$ 对于集合 $A\subseteq E$ 的首达时与击中时. 直观上 $\tau_{A}$ 和 $T_{A}$ 分别是在考虑和不考虑初始位置的情况下, 随机过程 $X$ 首次进入集合 $A$ 的时刻.

例 2.1.3 设状态空间  $(E, \mathcal{E})$  上的离散时间随机过程  $(X_{n})$  关于流  $(\mathcal{F}_{n})$  适应, 则 X 对于集合  $A \in E$  的首达时  $\tau_{A}$  和击中时  $T_{A}$  都是停时. 例如, 我们有  $\{\tau_{A} \leqslant n\} = \bigcup_{k=0}^{n} \{X_{k} \in A\} \in \mathscr{F}_{n}$ .

设 $\{\xi_n : n \geqslant 1\}$ 是独立同分布随机变量序列. 令 $(\mathcal{F}_n)$ 是 $(\xi_n)$ 的自然 $\sigma$ 代数流. 再定义从原点出发的随机游动

$$
X _ {n} = \sum_ {i = 1} ^ {n} \xi_ {i}, \quad n \geqslant 0. \tag {2.1.11}
$$

注意 $(\mathcal{F}_n)$ 也是 $(X_{n})$ 的自然流. 下面命题的结论称为沃尔德 (Wald) 恒等式.

命题 2.1.12 (沃尔德恒等式) 设  $\mathbf{E}(\xi_{1})$  存在而 T 是关于  $(\mathcal{F}_{n})$  的停时, 则

$$
\mathbf {E} (X _ {T}) = \mathbf {E} (T) \mathbf {E} (\xi_ {1}).
$$

证明 因 $T$ 是 $(\mathcal{F}_n)$ 的停时, 事件 $\{T \geqslant n\} = \{T \leqslant n - 1\}^c \in \mathcal{F}_{n-1}$ 独立于 $\xi_n$. 从而

$$
\begin{array}{l} \mathbf {E} (X _ {T}) = \mathbf {E} \Big (\sum_ {n = 1} ^ {\infty} \xi_ {n} 1 _ {\{n \leqslant T \}} \Big) = \sum_ {n = 1} ^ {\infty} \mathbf {E} \big (\xi_ {n} 1 _ {\{n \leqslant T \}} \big) \\ = \sum_ {n = 1} ^ {\infty} \mathbf {E} (\xi_ {n}) \mathbf {E} (1 _ {\{n \leqslant T \}}) = \mathbf {E} (\xi_ {1}) \sum_ {n = 1} ^ {\infty} \mathbf {P} (n \leqslant T). \\ \end{array}
$$