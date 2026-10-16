再由非负整数值随机变量 T 的期望的计算公式即得欲证等式. □

## 2.1.4 完备化和加强化

给定概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$, 我们称 $N \subseteq \Omega$ 为 $\mathbf{P}$ 零集, 如果存在 $A \in \mathcal{F}$ 满足 $N \subseteq A$ 且 $\mathbf{P}(A) = 0$. 用 $\mathcal{N}$ 表示所有 $\mathbf{P}$ 零集构成的集类. 记 $\mathcal{F}^* = \sigma(\mathcal{F} \cup \mathcal{N})$.

命题 2.1.13 我们有  $\mathscr{F}^{*}=\{F\cup N:F\in\mathscr{F},N\in\mathscr{N}\}$ .

证明 记 $\bar{\mathcal{F}} = \{F \cup N : F \in \mathcal{F}, N \in \mathcal{N}\}$. 显然 $\bar{\mathcal{F}} \subseteq \sigma(\mathcal{F} \cup \mathcal{N}) = \mathcal{F}^*$. 另一方面, 易见 $\Omega \in \bar{\mathcal{F}}$ 且 $\bar{\mathcal{F}}$ 对可数并运算封闭. 现设 $B = F \cup N \in \bar{\mathcal{F}}$, 其中 $F \in \mathcal{F}$ 且 $N \in \mathcal{N}$, 则存在 $A \in \mathcal{F}$ 满足 $N \subseteq A$ 且 $\mathbf{P}(A) = 0$. 注意

$$
B ^ {c} = F ^ {c} \cap N ^ {c} = (F ^ {c} \cap A ^ {c}) \cup (F ^ {c} \cap N ^ {c} \cap A),
$$

其中 $(F^{c} \cap A^{c}) \in \mathcal{F}$ 且 $(F^{c} \cap N^{c} \cap A) \in \mathcal{N}$, 故 $B^{c} \in \bar{\mathcal{F}}$. 所以 $\bar{\mathcal{F}}$ 是 $\sigma$ 代数. 又因为 $\bar{\mathcal{F}} \supseteq \mathcal{F} \cup \mathcal{N}$, 故有 $\bar{\mathcal{F}} \supseteq \sigma(\mathcal{F} \cup \mathcal{N}) = \mathcal{F}^{*}$. □

若 $A \in \mathcal{F}^*$ 可表示为 $A = F \cup N$, 其中 $F \in \mathcal{F}$ 而 $N \in \mathcal{N}$, 我们记 $\mathbf{P}^*(A) = \mathbf{P}(F)$. 易证该记号无歧义, 且 $\mathbf{P}^*$ 为 $\mathcal{F}^*$ 上的概率测度. 分别称 $\mathcal{F}^*$ 和 $\mathbf{P}^*$ 为 $\mathcal{F}$ 和 $\mathbf{P}$ 的完备化. 当 $\mathcal{F} = \mathcal{F}^*$ 时, 称 $\mathcal{F}$ 或 $\mathbf{P}$ 是完备的, 此时也称 $(\Omega, \mathcal{F}, \mathbf{P})$ 是完备概率空间.

对于 $\mathcal{F}$ 的子 $\sigma$ 代数 $\mathcal{G}$, 称 $\mathcal{G}^* := \sigma(\mathcal{G} \cup \mathcal{N})$ 为 $\mathcal{G}$ 的加强化. 若 $\mathcal{G} = \mathcal{G}^*$, 则称 $\mathcal{G}$ 是加强的. 如果一个流 $(\mathcal{G}_t : t \in I)$ 中的每个 $\mathcal{G}_t$ 都是加强的 $\sigma$ 代数, 就称该流是加强的.

我们称 $A \triangle B := (A \setminus B) \cup (B \setminus A)$ 为集合 $A, B \subseteq \Omega$ 的对称差. 易知, 对于 $A, B, C \subseteq \Omega$ 有

$$
A = B \triangle C \Leftrightarrow B = C \triangle A \Leftrightarrow C = A \triangle B.
$$

若有 $A \triangle B \in \mathcal{N}$, 则写成 $A \sim B$. 不难看出“$\sim$”是 $\Omega$ 的子集间的等价关系.

命题 2.1.14 令  $G^{*}$  为 F 的子  $\sigma$  代数 G 的完备化, 则有

$\mathcal{G}^{*} = \{B\triangle C:B\in \mathcal{G},C\in \mathcal{N}\} = \{A\subseteq \Omega :$ 有 $B\in \mathcal{G}$ 使 $A\triangle B\in \mathcal{N}\}$

证明 记 $\bar{\mathcal{G}} = \{A := B \triangle C : B \in \mathcal{G}, C \in \mathcal{N}\}$. 易知欲证等式中的第二个等号成立, 只需证明 $\mathcal{G}^* = \bar{\mathcal{G}}$. 显然 $\bar{\mathcal{G}} \subseteq \sigma(\mathcal{G} \cup \mathcal{N}) = \mathcal{G}^*$. 下面证明 $\bar{\mathcal{G}} \supseteq \mathcal{G}^*$, 而因 $\bar{\mathcal{G}} \supseteq \mathcal{G} \cup \mathcal{N}$, 只需证 $\bar{\mathcal{G}}$ 是 $\sigma$ 代数. 显然 $\Omega \in \bar{\mathcal{G}}$. 设 $A \in \bar{\mathcal{G}}$. 则存在 $B \in \mathcal{G}$ 使 $A \triangle B \in \mathcal{N}$. 易见 $A^c \triangle B^c = A \triangle B \in \mathcal{N}$. 再因 $B^c \in \mathcal{G}$, 有 $A^c \in \bar{\mathcal{G}}$. 所以 $\bar{\mathcal{G}}$ 对取余运算封闭. 对于集合列 $\{A_n\} \subseteq \bar{\mathcal{G}}$, 存在 $\{B_n\} \subseteq \mathcal{G}$ 使对每个 $n \geqslant 0$ 有 $A_n \triangle B_n \in \mathcal{N}$. 注意 $\bigcup_{n} B_n \in \mathcal{G}$ 且

$$
\bigg (\bigcup_ {n} A _ {n} \bigg) \triangle \bigg (\bigcup_ {n} B _ {n} \bigg) \subseteq \bigcup_ {n} (A _ {n} \triangle B _ {n}) \in \mathcal {N},
$$

故 $\bigcup_{n}A_{n}\in \bar{\mathcal{G}}$ 因此 $\bar{\mathcal{G}}$ 是一个 $\sigma$ 代数. □

例2.1.4 设 $\Omega = \Omega_0 \cup \Omega_1$, 其中 $\Omega_0, \Omega_1$ 为不交的非空集合. 令 $\mathcal{F} = \{\varnothing, \Omega_0, \Omega_1, \Omega\}$. 再设 $\mathbf{P}$ 为 $(\Omega, \mathcal{F})$ 上的概率测度, 且满足 $\mathbf{P}(\Omega_0) = 0$ 和 $\mathbf{P}(\Omega_1) > 0$, 则每个 $A \in \mathcal{F}^*$ 都可表示为 $A = A_0 \cup B$ 的形式, 其中 $A_0 \subseteq \Omega_0$ 而 $B \in \mathcal{F}$. 此时有 $\mathbf{P}^*(A) = \mathbf{P}(B)$.

## 2.1.5 连续时间流

考虑概率空间 $(\Omega, \mathcal{G}, \mathbf{P})$ 上的连续时间 $\sigma$ 代数流 $(\mathcal{G}_t : t \geqslant 0)$. 对 $t \geqslant 0$ 令 $\mathcal{G}_{t+} = \bigcap_{s > t} \mathcal{G}_s$, 则 $\mathcal{G}_{t+} \supseteq \mathcal{G}_t$ 且 $(\mathcal{G}_{t+})$ 也是 $\sigma$ 代数流. 如果对一切 $t \geqslant 0$ 有 $\mathcal{G}_{t+} = \mathcal{G}_t$, 就称流 $(\mathcal{G}_t)$ 右连续. 对于 $(\mathcal{G}_{t+})$ 的停时 $T$, 将相应的 $T$ 前 $\sigma$ 代数记为 $\mathcal{G}_{T+}$.

命题 2.1.15 非负随机变量 T 是  $(\mathcal{G}_{t+})$  的停时当且仅当对任何  $t \geqslant 0$  都有  $\{T < t\} \in G_t$ .

证明 若 $T$ 是 $(\mathcal{G}_{t+})$ 的停时, 则对任何 $t \geqslant 0$ 有 $\{T < t\} = \bigcup_{n} \{T \leqslant t - 1/n\} \in \mathcal{G}_t$. 反之, 假设对任何 $t \geqslant 0$ 都有 $\{T < t\} \in \mathcal{G}_t$. 对于 $k \geqslant 1$, 有

$$
\{T \leqslant t \} = \bigcap_ {n = k} ^ {\infty} \{T <   t + 1 / n \} \in \mathscr {G} _ {t + 1 / k},
$$

故 $\{T\leqslant t\} \in \bigcap_{k\geqslant 1}\mathcal{G}_{t + 1 / k} = \mathcal{G}_{t + }$ 故 $T$ 是 $(\mathcal{G}_{t + })$ 的停时. □

命题 2.1.16 令 T 是  $(\mathcal{G}_{t+})$  的停时. 再设  $A \in G_{\infty}$ ，则  $A \in G_{T+}$  当且仅当对任何  $t \geqslant 0$  都有  $A \cap \{T < t\} \in \mathcal{G}_{t}$ .

证明 若 $A \in \mathcal{F}_{T+}$, 则对任何 $n \geqslant 1$ 有 $A \cap \{T \leqslant t - 1/n\} \in \mathcal{F}_{(T \leqslant t - 1/n)+} \subseteq \mathcal{F}_t$, 进而

$$
A \cap \{T <   t \} = \bigcup_ {n = 1} ^ {\infty} (A \cap \{T \leqslant t - 1 / n \}) \in \mathscr {F} _ {t}.
$$

反之, 若对任何 $t \in I$ 都有 $A \cap \{T < t\} \in \mathscr{F}_t$, 则对任何 $k \geqslant 1$ 有

$$
A \cap \{T \leqslant t \} = \bigcap_ {n = k} ^ {\infty} \left(A \cap \{T <   t + 1 / n \}\right) \in \mathscr {F} _ {t + 1 / k}.
$$

故知 $A \cap \{T \leqslant t\} \in \bigcap_{k=1}^{\infty} \mathscr{F}_{t+1/k} = \mathscr{F}_{t+}$, 因而 $A \in \mathscr{F}_{T+}$. $\square$

命题 2.1.17 设每个  $T_{n}$  是  $(\mathcal{G}_{t}: t \geqslant 0)$  的停时且序列  $\{T_{n}\}$  单调不增，则  $T := \lim_{n} T_{n}$  是  $(\mathcal{G}_{t+})$  的停时.

证明 因 $\{T_n\}$ 单调不增, 有 $\{T < t\} = \bigcup_{n} \{T_n < t\} \in \mathcal{G}_t$. 由命题2.1.15知 $T$ 是 $(\mathcal{G}_{t+})$ 的停时. □

对于  $n \geqslant 0$  记  $D_{n} = \{i/2^{n} : i = 0, 1, 2, \cdots\}$ . 给定  $(\mathcal{G}_{t+})$  的停时 T, 令  $T_{n} = \inf\{t \in D_{n} : t > T\}$ . 注意

$$
T _ {n} = \frac {1}{2 ^ {n}} (\lfloor 2 ^ {n} T \rfloor + 1) = \sum_ {k = 1} ^ {\infty} \frac {k}{2 ^ {n}} 1 _ {\{(k - 1) / 2 ^ {n} \leqslant T <   k / 2 ^ {n} \}} + \infty 1 _ {\{T = \infty \}}. \tag {2.1.12}
$$

显然当 $n \to \infty$ 时, 递降地 $T_{n} \to T$. 称 $T_{n}$ 为 $T$ 的二分点离散化.

命题 2.1.18 由 (2.1.12) 式定义的  $T_{n}$  是关于离散时间流  $(\mathcal{G}_{k/2^{n}}:k\geqslant0)$  的停时且有  $G_{T+}\subseteq G_{T_{n}}$ .

证明 对于 $k \geqslant 0$, 根据命题2.1.15有

$$
\{T _ {n} = k / 2 ^ {n} \} = \{T <   k / 2 ^ {n} \} \cap \{T <   (k - 1) / 2 ^ {n} \} ^ {c} \in \mathscr {G} _ {k / 2 ^ {n}}.
$$

所以 $T_{n}$ 是关于流 $(\mathcal{G}_{k / 2^n}:k\geqslant 0)$ 的停时.对于 $G\in \mathcal{G}_{T + }$ ，由命题2.1.15和命题2.1.16有

$$
G \cap \{T _ {n} = k / 2 ^ {n} \} = G \cap \{T <   k / 2 ^ {n} \} \cap \{T <   (k - 1) / 2 ^ {n} \} ^ {c} \in \mathcal {G} _ {k / 2 ^ {n}},
$$

故 $G \in \mathcal{G}_{T_n}$. 因此 $\mathcal{G}_{T+} \subseteq \mathcal{G}_{T_n}$. $\square$

定义 2.1.3 称完备概率空间  $(\Omega, \mathcal{G}, \mathbf{P})$  上的连续时间流  $(\mathcal{G}_{t}: t \geqslant 0)$  满足通常条件, 是指它是右连续的且每个  $G_{t}$  都是加强的.

## 2.1.6 循序可测过程

设 $(\mathcal{G}_t:t\geqslant 0)$ 为概率空间 $(\Omega ,\mathcal{G},\mathbf{P})$ 上的连续时间 $\sigma$ 代数流.称空间 $\mathbb{R}^d$ 上的连续时间过程 $(X_{t}:t\geqslant 0)$ 关于该流循序可测，是指对任意的 $t\geqslant 0$ 映射 $(s,\omega)\mapsto X_s(\omega)$ 限定在 $[0,t]\times \Omega$ 上关于 $\sigma$ 代数 $\mathcal{B}[0,t]\times \mathcal{G}_t$ 可测,其中 $\mathcal{B}[0,t]$ 表示 $[0,t]$ 上的 $\sigma$ 代数.显然,若 $(X_{t})$ 关于 $(\mathcal{G}_t)$ 循序可测，则它关于该流是适应的.

命题 2.1.19 若连续时间随机过程  $(X_{t})$  关于流  $(\mathcal{G}_{t})$  适应且右连续或左连续, 则  $(X_{t})$  关于  $(\mathcal{G}_{t})$  循序可测.

证明 我们只考虑 $(X_{t})$ 为右连续适应过程的情况, 左连续的情况类似. 对于 $n \geqslant 1$, 定义 $X_{n}(0) = X_{0}$ 和

$$
X _ {n} (s) = X _ {k t / 2 ^ {n}}, \quad (k - 1) t / 2 ^ {n} <   s \leqslant k t / 2 ^ {n}, k = 1, 2, 3, \dots , 2 ^ {n},
$$

则对任何 $B \in \mathcal{B}^d$ 有

$$
\{(s, \omega) \in [ 0, t ] \times \Omega : X _ {n} (s, \omega) \in B \}
$$

$$
= \{0 \} \times X _ {0} ^ {- 1} (B) \cup \bigcup_ {k = 1} ^ {2 ^ {n}} ((k - 1) t / 2 ^ {n}, k t / 2 ^ {n}) \times X _ {k t / 2 ^ {n}} ^ {- 1} (B),
$$

其中 $X_{kt / 2^n}^{-1}(B)\in \mathcal{G}_{kt / 2^n}\subseteq \mathcal{G}_t$ .显然，上面的集合属于 $\mathcal{B}[0,t]\times \mathcal{G}_t$ .所以映射 $(s,\omega)\mapsto$ $X_{n}(s,\omega)$ 关于 $\mathcal{B}[0,t]\times \mathcal{G}_t$ 可测.因 $X$ 是右连续的，故 $X_{s}(\omega) = \lim_{n}X_{n}(s,\omega)$ 因此$(s,\omega)\mapsto X_s(\omega)$ 关于 $\mathcal{B}[0,t]\times \mathcal{G}_t$ 可测. □

命题 2.1.20 设连续时间随机过程  $(X_{t})$  关于流  $(\mathcal{G}_{t})$  循序可测, 则对任何  $(\mathcal{G}_{t})$  停时的 T, 映射  $\omega \mapsto X_{T(\omega)}(\omega)$  限制在  $\Omega_{T} := \{T < \infty\}$  上关于  $\Omega_{T} \cap G_{T}$  可测.

证明 易证 $\omega \mapsto T(\omega) \wedge t$ 是 $(\Omega, \mathcal{G}_t)$ 到 $([0, t], \mathcal{B}[0, t])$ 的可测映射, 故 $\omega \mapsto (T(\omega) \wedge t, \omega)$ 是 $(\Omega, \mathcal{G}_t)$ 到 $([0, t] \times \Omega, \mathcal{B}[0, t] \times \mathcal{G}_t)$ 的可测映射. 根据命题 2.1.19, 对任何 $t \geqslant 0$ 映射 $(s, \omega) \to X_s(\omega)$ 限定在 $[0, t] \times \Omega$ 上关于 $\sigma$ 代数 $\mathcal{B}[0, t] \times \mathcal{G}_t$ 和 $\mathcal{B}^d$ 可测. 因此复合 $\omega \mapsto (T(\omega) \wedge t, \omega) \mapsto X_{T(\omega) \wedge t}(\omega)$ 是 $(\Omega, \mathcal{G}_t)$ 到 $(\mathbb{R}^d, \mathcal{B}^d)$ 的可测映射. 这样对任意的 $B \in \mathcal{B}^d$ 有

$$
\{X _ {T} \in B \} \cap \Omega_ {T} \cap \{T \leqslant t \} = \{X _ {T \wedge t} \in B \} \cap \{T \leqslant t \} \in \mathscr {G} _ {t},
$$

故 $\{X_T\in B\} \cap \Omega_T\in \mathcal{G}_T$ ，即映射 $\omega \mapsto X_{T(\omega)}(\omega)$ 限制在 $\Omega_T$ 上关于 $\Omega_T\cap \mathcal{G}_T$ 可测.□

命题 2.1.21 设  $(X_{t})$  是关于流  $(\mathcal{G}_{t})$  适应的右连续过程, 则 X 到任何开集  $A \subseteq E$  的首达时  $\tau_{A} := \inf\{t \geqslant 0 : X_{t} \in A\}$  和击中时  $\tau_{A} := \inf\{t > 0 : X_{t} \in A\}$  重合且是  $(\mathcal{G}_{t+})$  的停时.

证明 因 $A$ 是开集, 显然有 $\tau_{A} = T_{A}$. $\mathbb{Q}$ 表示有理数集. 由于 $(X_{t})$ 右连续且关于流 $(\mathcal{G}_{t})$ 适应, 对任何 $t > 0$ 有

$$
\{\tau_ {A} <   t \} = \bigcup_ {s \in [ 0, t) \cap \mathbb {Q}} \{X _ {s} \in A \}.
$$

事实上, 假定 $\tau_{A} < t$, 必有某个 $s \in [\tau_{A}, t)$ 使得 $X_{s} \in A$. 而因 $(X_{t})$ 右连续, 有某个有理数 $r \in [s, t) \subseteq [0, t)$ 使 $X_{r} \in A$, 故上式左端是右端的子集. 相反的包含关系显然, 故上式成立. 显然上式右端属于 $\mathcal{G}_{t}$, 故得 $\{\tau_{A} < t\} \in \mathcal{G}_{t}$. 由命题2.1.15知 $\tau_{A}$ 是 $(\mathcal{G}_{t+})$ 的停时. $\square$

可以证明, 若流 $(\mathcal{G}_t)$ 满足通常条件, 则 $(\mathcal{G}_t)$ 循序可测过程 $(X_t)$ 对于任何集合 $A \in \mathcal{B}^d$ 的首达时 $\tau_A$ 和击中时 $T_A$ 都是 $(\mathcal{G}_t)$ 的停时; 如可参见 [38, p.186, 定理 3.2.13].

## 练习题

1. 设 $\{B_n\} \subseteq \mathcal{F}$ 是 $\Omega$ 的可数划分, 且对每个 $n \geqslant 1$ 有 $\mathbf{P}(B_n) > 0$. 令 $\xi$ 为可积随机变量. 证明 $\mathcal{G} := \sigma(\{B_n\})$ 由 $\{B_n\}$ 中的集合的所有可能的并构成 (规定零个集合的

并为空集)且

$$
\mathbf {E} (\xi | \mathcal {G}) = \sum_ {n = 1} ^ {\infty} 1 _ {B _ {n}} \mathbf {E} (\xi | B _ {n}).
$$

2. 证明对任何 $(\mathcal{F}_t)$ 的停时 $T$ 有 $\{T = \infty\} \in \mathcal{F}_{\infty}$.
3. 证明常数值随机变量 $T \equiv t$ 是停时, 且此时有 $\mathcal{F}_T = \mathcal{F}_t$.
4. 证明泊松过程 $(N_{t})$ 的第 $n$ 次跳跃时间 $S_{n}$ 是关于其自然流 $(\mathcal{F}_t^N)$ 的停时.
5. 直接证明左连续适应过程是循序可测的.

## 2.2 鞅、上鞅和下鞅

在本节中, 我们取 $I = \mathbb{Z}_{+}$ 或 $\mathbb{R}_{+}$. 考虑完备概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上给定的 $\sigma$ 代数流 $(\mathcal{F}_t : t \in I)$.

## 2.2.1 定义和基本性质

定义 2.2.1 设实数值过程 $(X_{t}: t \in I)$ 可积且关于流 $(\mathscr{F}_{t}: t \in I)$ 适应. 若对任何 $t \geqslant s \in I$ 都有 $\mathbf{E}(X_{t} | \mathscr{F}_{s}) = X_{s}$, 则称 $(X_{t})$ 为关于 $(\mathscr{F}_{t})$ 的鞅. 若这里的 “=” 替换为 “$\leqslant$” 或 “$\geqslant$”, 则对应地称 $(X_{t})$ 为关于 $(\mathscr{F}_{t})$ 的上鞅或下鞅. 在流 $(\mathscr{F}_{t})$ 明确的情况下, 简称 $(X_{t})$ 为鞅、上鞅或下鞅.

当 $I = \mathbb{Z}_{+}$ 时, 对应的鞅称为离散时间鞅或者鞅序列; 当 $I = \mathbb{R}_{+}$ 时, 对应的鞅称为连续时间鞅. 显然 $(X_{n}: n \geqslant 0)$ 是离散时间鞅当且仅当对任何 $n \geqslant 0$ 都有 $\mathbf{E}(X_{n+1}|\mathcal{F}_n) = X_n$. 由定义, 立刻得到下列简单性质:

命题 2.2.1 (1) 令 M 和  $M^{+}$  分别表示关于某个给定  $\sigma$  代数流的鞅和下鞅的全体, 那么 M 是一个线性空间, 而  $M^{+}$  是凸锥且对取大运算 V 封闭.

(2) 若 $(X_{t})$ 是 $(\mathcal{F}_{t})$ 下鞅, 则 $t \mapsto \mathbf{E}(X_{t})$ 递增. 另外, 下鞅 $(X_{t})$ 是鞅当且仅当 $t \mapsto \mathbf{E}(X_{t})$ 是常数.
(3) 若 $(X_{t})$ 是鞅, $\phi$ 是凸函数且每个 $\phi(X_{t})$ 可积, 则 $(\phi(X_{t}))$ 是下鞅. 因此 $(|X_{t}|)$ 是下鞅, 而若每个 $X_{t}$ 平方可积, 则 $(X_{t}^{2})$ 是下鞅.
(4) 若 $(X_{t})$ 是下鞅, $\phi$ 是递增凸函数且每个 $\phi(X_{t})$ 可积, 则 $(\phi(X_{t}))$ 也是下鞅. 因此 $(X_{t}^{+})$ 是下鞅.

例 2.2.1 设  $\{\xi_{n}: n \geqslant 1\}$  为独立同分布的随机变量序列, 且有  $\mathbf{P}(\xi_{n}=1)=p$  和  $\mathbf{P}(\xi_{n}=-1)=q$ , 其中  $p, q \geqslant 0$  且  $p+q=1$ . 任取整数值  $X_{0}=k$  并令  $X_{n}=X_{0}+\sum_{i=1}^{n}\xi_{i}$ $(n \geqslant 1)$ , 则  $(X_{n})$  为简单随机游动. 再令  $(\mathscr{F}_{n})$  为  $(X_{n})$  的自然流. 我们有

$$
\begin{array}{l} \mathbf {E} (X _ {n + 1} | \mathcal {F} _ {n}) = \mathbf {E} (X _ {n + 1} - X _ {n} | \mathcal {F} _ {n}) + \mathbf {E} (X _ {n} | \mathcal {F} _ {n}) \\ = \mathbf {E} (\xi_ {n + 1} | \mathcal {F} _ {n}) + X _ {n} = \mathbf {E} (\xi_ {n + 1}) + X _ {n} \\ = (p - q) + X _ {n}. \\ \end{array}
$$

当 $p = q$ 时, $(X_{n})$ 是对称的简单随机游动, 此时它是鞅. 当 $p \geqslant q$ 时, $(X_{n})$ 是下鞅; 当 $p \leqslant q$ 时, $(X_{n})$ 是上鞅. 简单随机游动可用来描述赌博中某个赌徒的赌资. 从概率平均的角度看, 鞅的情况对应于对双方公平的博弈.

例 2.2.2 设  $\sigma^{2} \geqslant 0$  和  $b \in R$  为常数, 而  $(B_{t}: t \geqslant 0)$  是以  $\sigma^{2}$  为参数的布朗运动. 称  $(B_{t} + bt : t \geqslant 0)$  为带漂移的布朗运动. 设  $E|B_{0}| < \infty$ , 则当  $b = 0 (\geqslant 0, \leqslant 0)$  时  $(B_{t} + bt : t \geqslant 0)$  是关于  $(B_{t} : t \geqslant 0)$  的自然流的鞅 (下鞅, 上鞅).

鞅、上鞅或下鞅的概念与流有关. 若 $X$ 关于大的适应流是鞅, 它关于小的适应流也是鞅. 显然, $X$ 是上鞅当且仅当 $-X$ 是下鞅, 而 $X$ 是鞅当且仅当它既是上鞅也是下鞅. 因此, 后面的结果只对上鞅或下鞅叙述.

命题 2.2.2 设可积过程  $(X_{t})$  关于  $(\mathcal{F}_{t})$  适应. 那么  $(X_{t})$  是关于流  $(\mathcal{F}_{t})$  的下鞅当且仅当对于  $s \leqslant t \in I$  和  $A \in F_{s}$  有  $\mathbf{E}(X_{s}; A) \leqslant \mathbf{E}(X_{t}; A)$ .

证明 由定理2.1.1知 $(X_{t})$ 关于流 $(\mathcal{F}_t)$ 是下鞅当且仅当对于任意 $s\leqslant t\in I$ 和$A\in \mathcal{F}_s$ 有 $\mathbf{E}(X_s;A)\leqslant \mathbf{E}[\mathbf{E}(X_t|\mathcal{F}_s);A] = \mathbf{E}(X_t;A)$ □

命题 2.2.3 如果  $(X_{t})$  是关于流  $(\mathcal{F}_{t})$  的下鞅, 它也是关于加强的流  $(\mathcal{F}_{t}^{*})$  的下鞅.

证明 因为 $(X_{t})$ 关于 $(\mathcal{F}_t)$ 适应, 它也关于 $(\mathcal{F}_t^*)$ 适应. 考虑 $s \leqslant t \in I$ 和 $B \in \mathcal{F}_s^*$. 根据命题2.1.14, 存在 $A \in \mathcal{F}_s$ 使得 $\mathbf{P}(A \triangle B) = 0$. 而由命题2.2.2有

$$
\mathbf {E} (X _ {s}; B) = \mathbf {E} (X _ {s}; A) \leqslant \mathbf {E} (X _ {t}; A) = \mathbf {E} (X _ {t}; B).
$$

再由命题 2.2.2 知  $(X_{t})$  是  $(\mathcal{F}_{t}^{*})$  下鞅. □

定理 2.2.4 (杜布分解) 若  $(X_{n})$  相对流  $(\mathcal{F}_{n})$  为下鞅, 则存在相对该流的鞅  $(Z_{n})$  和从原点出发的可料单增过程  $(A_{n})$ , 使得  $X_{n}=Z_{n}+A_{n}, n\geqslant0$ . 此外, 这样的分解是唯一的且

$$
A _ {n} = \sum_ {i = 1} ^ {n} \left[ \mathbf {E} (X _ {i} | \mathscr {F} _ {i - 1}) - X _ {i - 1} \right].
$$

证明 假设有 $(\mathcal{F}_n)$ 适应过程 $(Z_{n})$ 和从原点出发的可料过程 $(A_{n})$ 使得 $X_{n} = Z_{n} + A_{n}$. 对于 $n \geqslant 1$, 定义 $\mathcal{F}_{n-1}$ 可测随机变量 $\xi_{n} = A_{n} - A_{n-1}$. 注意 $A_{n} = \sum_{i=1}^{n} \xi_{i}$. 另

外

$$
\begin{array}{l} \xi_ {n} = \mathbf {E} (X _ {n} - Z _ {n} - X _ {n - 1} + Z _ {n - 1} | \mathcal {F} _ {n - 1}) \\ = \mathbf {E} (X _ {n} | \mathscr {F} _ {n - 1}) - \mathbf {E} (Z _ {n} | \mathscr {F} _ {n - 1}) - X _ {n - 1} + Z _ {n - 1}. \\ \end{array}
$$

所以 $(Z_{n})$ 是鞅当且仅当 $\xi_{n} = \mathbf{E}(X_{n}|\mathcal{F}_{n - 1}) - X_{n - 1}$ ($n\geqslant 1$), 而此时 $(X_{n})$ 为 $(\mathcal{F}_n)$ 的下鞅当且仅当 $(\xi_n)$ 为非负可料过程, 即 $(A_{n})$ 为从原点出发的单增可料过程. 这就证明了定理结论成立. □

例 2.2.3 设  $(S_{n}: n \geqslant 1)$  是从原点出发的一维对称简单随机游动. 根据定理 2.2.4 有下鞅分解  $|S_{n}| = M_{n} + A_{n}$ ，其中  $(A_{n})$  为从原点出发的可料单增过程且

$$
A _ {n} = \sum_ {i = 1} ^ {n} \left[ \mathbf {E} (| S _ {i} | | \mathcal {F} _ {i - 1}) - | S _ {i - 1} | \right].
$$

易知, 对  $i \geqslant 1$  有

$$
| S _ {i} | = \left\{ \begin{array}{l l} | S _ {i - 1} | + \xi_ {i}, & S _ {i - 1} > 0, \\ | S _ {i - 1} | - \xi_ {i}, & S _ {i - 1} <   0, \\ 1, & S _ {i - 1} = 0. \end{array} \right.
$$

因此

$$
\mathbf {E} (| S _ {i} | | \mathscr {F} _ {i - 1}) = \left\{ \begin{array}{l l} | S _ {i - 1} |, & S _ {i - 1} \neq 0, \\ 1, & S _ {i - 1} = 0. \end{array} \right.
$$

故有 $A_{n} = \mathrm{Card}\{i:1\leqslant i\leqslant n:S_{i - 1} = 0\}$ .由于

$$
\mathbf {P} (S _ {2 k - 1} = 0) = 0, \quad \mathbf {P} (S _ {2 k} = 0) = \binom{2 k}{k} \frac {1}{4 ^ {k}},
$$

不难计算出

$$
\mathbf {E} (| S _ {n} |) = \sum_ {i = 0} ^ {n - 1} \mathbf {P} (S _ {i} = 0) = \sum_ {i = 0} ^ {\lfloor (n - 1) / 2 \rfloor} \binom{2 k}{k} \frac {1}{4 ^ {k}}.
$$

中文的“鞅”为形声字. 这里“央”为聚拢之意, 而“革”指皮带, 联合起来本义是一头套在牛马颈部, 另一头掌握在驾驭者手里的皮带. 主要指双马双牛或多马多牛齐驱并驾时抓在驾驭者手里的牛马颈带. 英文词 martingale 原意是一种用来控制马头的皮带, 也指一类于 18 世纪流行于法国的投注策略, 其中最简单的一种为博弈而设计. 在此博弈中, 赌徒每局投掷一枚硬币, 若硬币正面朝上, 则赌徒赢得赌本; 若硬币反面朝上, 则赌徒输掉赌本. 概率论中的鞅的概念由莱维 (Paul Pierre Lévy) 提出, 而其基础理论则是杜布 (Joseph Leo Doob) 建立的.

## 2.2.2 杜布鞅

定义 2.2.2 设 Y 为实可积随机变量. 对于  $t \in I$  令  $X_{t} = \mathbf{E}(Y|\mathcal{F}_{t})$ , 则  $X = (X_{t}: t \in I)$  是一个关于  $(\mathcal{F}_{t})$  的鞅, 称为右闭鞅或杜布鞅.

命题 2.2.5 杜布鞅  $X = (X_{t} : t \in I)$  是一致可积的.

证明 设 $X_{t} = \mathbf{E}(Y|\mathcal{F}_{t})$ 由上面定义给出, 其中 $Y$ 为可积随机变量. 由延森 (Jensen) 不等式得 $|X_{t}| \leqslant \mathbf{E}(|Y||\mathcal{F}_{t})$. 根据定理 2.1.1, 对任意的 $\lambda > 0$ 有

$$
\mathbf {E} (| X _ {t} |; | X _ {t} | > \lambda) \leqslant \mathbf {E} [ \mathbf {E} (| Y | | \mathscr {F} _ {t}); | X _ {t} | > \lambda ] = \mathbf {E} (| Y |; | X _ {t} | > \lambda).
$$

再取 $n \geqslant 1$ 得

$$
\begin{array}{l} \mathbf {E} (| Y |; | X _ {t} | > \lambda) \leqslant \mathbf {E} (| Y |; | X _ {t} | > \lambda , | Y | > n) + n \mathbf {P} (| X _ {t} | > \lambda , | Y | \leqslant n) \\ \leqslant \mathbf {E} (| Y |; | Y | > n) + n \mathbf {P} (| X _ {t} | > \lambda), \\ \end{array}
$$

其中

$$
\mathbf {P} (| X _ {t} | > \lambda) \leqslant \frac {1}{\lambda} \mathbf {E} | X _ {t} | = \frac {1}{\lambda} \mathbf {E} [ | \mathbf {E} (Y | \mathscr {F} _ {t}) | ] \leqslant \frac {1}{\lambda} \mathbf {E} | Y |.
$$

所以

$$
\operatorname * {l i m s u p} _ {\lambda \to \infty} \sup _ {t \in I} \mathbf {E} (| X _ {t} |; | X _ {t} | > \lambda) \leqslant \mathbf {E} (| Y |; | Y | > n).
$$

由 $n \geqslant 1$ 的任意性知上式左边为零, 即 $X = (X_{t}: t \in I)$ 是一致可积的. $\square$

## 2.2.3 局部鞅

定义 2.2.3 关于流  $(\mathcal{F}_{t}: t \in I)$  适应的实值过程  $M = (M_{t}: t \in I)$  称为局部鞅，是指存在单增的停时列  $\{\tau_{k}\}$  满足  $\lim_{k \to \infty} \tau_{k} \stackrel{a.s.}{=} \infty$ ，且对任何  $k \geqslant 1$ ，停止过程  $M^{\tau_{k}} = (M_{t \wedge \tau_{k}}: t \in I)$  关于流  $(\mathcal{F}_{t}: t \in I)$  是鞅。此时  $\{\tau_{k}\}$  称为 M 的局部化序列。

显然, 鞅是局部鞅.

命题 2.2.6 可积的非负局部鞅是上鞅.

证明 设 $X = (X_{t}: t \in I)$ 是非负局部鞅, 而 $\{\tau_{k}\}$ 为相应的局部化序列. 对于任意 $t \geqslant r \in I$, 由条件数学期望的法图定理有

$$
\mathbf {E} (X _ {t} | \mathscr {F} _ {r}) \leqslant \operatorname * {l i m i n f} _ {k \to \infty} \mathbf {E} (X _ {t \wedge \tau_ {k}} | \mathscr {F} _ {r}) = \operatorname * {l i m i n f} _ {k \to \infty} X _ {r \wedge \tau_ {k}} = X _ {r}.
$$

所以 $X$ 是上鞅. $\square$

## 练习题

1. 设 $\alpha \geqslant 0$ 和 $\beta \in \mathbb{R}$ 为常数, 而 $(N_t : t \geqslant 0)$ 是以 $\alpha$ 为参数的泊松过程. 设 $\mathbf{E}(N_0) < \infty$. 证明当 $\beta = \alpha (\geqslant \alpha, \leqslant \alpha)$ 时 $(N_t - \beta t : t \geqslant 0)$ 是关于 $(N_t : t \geqslant 0)$ 的自然流的鞅 (上鞅, 下鞅).
2. 设 $\{\xi_n : n \geqslant 0\}$ 是独立随机变量序列且 $\mathbf{E}(\xi_n) = 1 (n \geqslant 0)$. 令 $(\mathscr{F}_n)$ 为 $(\xi_n)$ 的自然流, 再对 $n \geqslant 0$ 令 $X_n = \prod_{i=0}^{n} \xi_i$. 证明 $(X_n)$ 是关于 $(\mathscr{F}_n)$ 的鞅.
3. 设流 $(\mathcal{F}_t: t \in I)$ 和 $(\mathcal{G}_t: t \in I)$ 满足 $\mathcal{F}_t \subseteq \mathcal{G}_t$ ($t \in I$) 而实值过程 $(X_t: t \in I)$ 关于流 $(\mathcal{F}_t: t \in I)$ 适应. 证明: 若 $(X_t)$ 关于流 $(\mathcal{G}_t)$ 是下鞅, 则它关于流 $(\mathcal{F}_t)$ 是下鞅.
4. 设 $(X_{t}: t \geqslant 0)$ 和 $(Y_{t}: t \geqslant 0)$ 都是关于流 $(\mathcal{F}_t)_{t \geqslant 0}$ 的下鞅. 证明 $(X_{t} \vee Y_{t}: t \geqslant 0)$ 是关于 $(\mathcal{F}_t)_{t \geqslant 0}$ 的下鞅.
5. 设 $(X_{t}: t \geqslant 0)$ 和 $(Y_{t}: t \geqslant 0)$ 都是关于流 $(\mathcal{F}_t)_{t \geqslant 0}$ 的上鞅. 证明 $(X_{t} \wedge Y_{t}: t \geqslant 0)$ 是关于 $(\mathcal{F}_t)_{t \geqslant 0}$ 的上鞅.
6. 设 $(X_{t}: t \geqslant 0)$ 是关于流 $(\mathcal{F}_t)_{t \geqslant 0}$ 的非负平方可积下鞅, 而 $C$ 为常数. 证明 $(X_{t}^{2} \vee C: t \geqslant 0)$ 是关于 $(\mathcal{F}_t)_{t \geqslant 0}$ 的下鞅.

## 2.3 杜布停止定理

本节主要讨论离散时间下鞅, 即 $I = \mathbb{Z}_{+}$ 的情况. 设 $(\Omega, \mathcal{F}, \mathbf{P})$ 是完备的概率空间, 而 $(\mathcal{F}_n : n \geqslant 0)$ 是其上的离散时间 $\sigma$ 代数流. 随机过程 $(H_n : n \geqslant 0)$ 称为可料的, 是指 $H_0$ 是 $\mathcal{F}_0$ 可测的且对任意的 $n \geqslant 1$, 随机变量 $H_n$ 关于 $\mathcal{F}_{n-1}$ 可测.

## 2.3.1 下鞅的停止过程

设有实值适应过程 $X = (X_{n}:n\geqslant 0)$ 和可料过程 $H = (H_n:n\geqslant 0)$. 令 $(H\cdot X)_0 = H_0X_0$. 对 $n\geqslant 1$ 令

$$
(H \cdot X) _ {n} = (H \cdot X) _ {n - 1} + H _ {n} (X _ {n} - X _ {n - 1}). \tag {2.3.1}
$$

称 $\{(H\cdot X)_n:n\geqslant 0\}$ 为 $H$ 关于 $X$ 的离散积分.由上面递推公式得

$$
(H \cdot X) _ {n} = H _ {0} X _ {0} + \sum_ {i = 1} ^ {n} H _ {i} (X _ {i} - X _ {i - 1}), \quad n \geqslant 1. \tag {2.3.2}
$$

(为了在符号上区别乘积与随机积分, 我们写乘积时一般不用点.) 上式实际上是随机分析中的随机积分的离散时间形式.

命题 2.3.1 设  $H \cdot X$  可积. 若 X 是鞅, 则  $H \cdot X$  是鞅; 若 X 是下鞅且 H 非负, 则  $H \cdot X$  是下鞅.

证明 显然 $H \cdot X$ 是适应的. 对 $n \geqslant 1$ 我们有

$$
\begin{array}{l} \mathbf {E} [ (H \cdot X) _ {n} - (H \cdot X) _ {n - 1} | \mathcal {F} _ {n - 1} ] = \mathbf {E} (H _ {n} (X _ {n} - X _ {n - 1}) | \mathcal {F} _ {n - 1}) \\ = H _ {n} \mathbf {E} (X _ {n} - X _ {n - 1} | \mathscr {F} _ {n - 1}). \\ \end{array}
$$

因此 X 是鞅 (对应地, X 是下鞅且 H 非负) 蕴涵着  $H \cdot X$  是鞅 (对应地, 下鞅). □

给定停时 $\tau$, 令 $H_{n} = 1_{\{n \leqslant \tau\}} = 1 - 1_{\{\tau \leqslant n - 1\}}$. 注意 $H_{0} = 1$, 且 $H_{n}$ 关于 $\mathscr{F}_{n-1}$ 可测. 再利用 (2.3.2) 式得

$$
X _ {\tau \wedge n} = X _ {0} + \sum_ {i = 1} ^ {n \wedge \tau} (X _ {i} - X _ {i - 1}) = X _ {0} + \sum_ {i = 1} ^ {n} 1 _ {\{i \leqslant \tau \}} (X _ {i} - X _ {i - 1}) = (H \cdot X) _ {n}.
$$

显然, 每个 $(H \cdot X)_n$ 可积. 根据命题 2.3.1, 我们有

命题 2.3.2 若 X 是下鞅而  $\tau$  是停时, 则停止过程  $X^{\tau} = (X_{\tau \wedge n} : n \geqslant 0)$  也是下鞅.

## 2.3.2 杜布有界停止定理

若对任意的 $n$, 随机变量 $H_{n}$ 有界, 则称过程 $H = (H_{n}: n \geqslant 0)$ 是局部有界的. 不难证明, 如果 $X$ 可积, 且 $H$ 局部有界, 那么 $H \cdot X$ 是可积的. 下面的定理称为杜布有界停止定理, 是鞅论中非常本质的结果.

定理 2.3.3 设 X 为下鞅,  $\sigma$  和  $\tau$  是有界停时且  $\sigma \leqslant \tau$ , 那么  $X_{\sigma}$  和  $X_{\tau}$  是可积的且

$$
\mathbf {E} (X _ {\tau} | \mathscr {F} _ {\sigma}) \geqslant X _ {\sigma}.
$$

证明 取 $N$ 使得 $\tau \leqslant N$. 由命题2.3.2知 $X_{\sigma} = X_{N}^{\sigma}$ 和 $X_{\tau} = X_{N}^{\tau}$ 均可积. 根据定理2.1.1, 只需证明对任意的 $B \in \mathcal{F}_{\sigma}$ 有

$$
\mathbf {E} (X _ {\sigma}; B) \leqslant \mathbf {E} [ \mathbf {E} (X _ {\tau} | \mathscr {F} _ {\sigma}); B ] = \mathbf {E} (X _ {\tau}; B).
$$

以下分两步进行讨论:

(1) 设 $0 \leqslant \tau - \sigma \leqslant 1$. 此时, 我们可以写

$$
\mathbf {E} (X _ {\tau} - X _ {\sigma}; B) = \sum_ {n = 1} ^ {N} \mathbf {E} (X _ {\tau} - X _ {\sigma}; B \cap \{\sigma = n - 1 \} \cap \{\tau = n \})
$$

$$
= \sum_ {n = 1} ^ {N} \mathbf {E} (X _ {n} - X _ {n - 1}; B \cap \{\sigma = n - 1 \} \cap \{\tau = n \}).
$$

注意对任意的 $1 \leqslant n \leqslant N$ 有

$$
B \cap \{\sigma = n - 1 \} \cap \{\tau = n \} = B \cap \{\sigma = n - 1 \} \cap \{\tau > n - 1 \} \in \mathcal {F} _ {n - 1}.
$$

由下鞅性

$$
\begin{array}{l} \mathbf {E} (X _ {\tau} - X _ {\sigma}; B) = \sum_ {n = 1} ^ {N} \mathbf {E} \{\mathbf {E} [ (X _ {n} - X _ {n - 1}) 1 _ {B \cap \{\sigma = n - 1 \} \cap \{\tau = n \}} | \mathcal {F} _ {n - 1} ] \} \\ = \sum_ {n = 1} ^ {N} \mathbf {E} [ \mathbf {E} (X _ {n} - X _ {n - 1} | \mathscr {F} _ {n - 1}) 1 _ {B \cap \{\sigma = n - 1 \} \cap \{\tau = n \}} ] \geqslant 0. \\ \end{array}
$$

(2) 在一般情形, 令 $\tau_{n} = \tau \wedge (\sigma + n)$, 其中 $0 \leqslant n \leqslant N$, 则每个 $\tau_{n}$ 为停时且 $0 \leqslant \tau_{n} - \tau_{n-1} \leqslant 1$. 由于 $B \in \mathscr{F}_{\sigma} \subseteq \mathscr{F}_{\tau_{n}}$, 由上面证明的结论

$$
\mathbf {E} (X _ {\sigma}; B) = \mathbf {E} (X _ {\tau_ {0}}; B) \leqslant \mathbf {E} (X _ {\tau_ {1}}; B) \leqslant \dots \leqslant \mathbf {E} (X _ {\tau_ {N}}; B) = \mathbf {E} (X _ {\tau}; B).
$$

故得欲证结论. □

推论 2.3.4 设 X 为可积适应过程, 则 X 是鞅当且仅当对任何有界停时  $\sigma \leqslant \tau$  有  $\mathbf{E}(X_{\sigma}) = \mathbf{E}(X_{\tau})$ , 或等价地对任何有界停时  $\tau$  有  $\mathbf{E}(X_{\tau}) = \mathbf{E}(X_{0})$ .

证明 设 $X$ 为鞅. 由定理2.3.3, 对任何有界停时 $\sigma \leqslant \tau$ 有 $X_{\sigma} = \mathbf{E}(X_{\tau}|\mathcal{F}_{\sigma})$, 两端取期望得 $\mathbf{E}(X_{\sigma}) = \mathbf{E}(X_{\tau})$. 反之, 设对任何有界停时 $\sigma \leqslant \tau$ 有 $\mathbf{E}(X_{\sigma}) = \mathbf{E}(X_{\tau})$. 取 $N$ 使得 $\tau \leqslant N$. 对任何 $B \in \mathscr{F}_{\sigma} \subseteq \mathscr{F}_{\tau}$ 令

$$
\sigma_ {B} = \sigma 1 _ {B} + N 1 _ {B ^ {c}}, \quad \tau_ {B} = \tau 1 _ {B} + N 1 _ {B ^ {c}}.
$$

下面验证  $\sigma_{B}$  和  $\tau_{B}$  是停时. 事实上, 若 n < N, 则

$$
\{\sigma_ {B} \leqslant n \} = \{\sigma \leqslant n \} \cap B \in \mathscr {F} _ {n}, \quad \{\tau_ {B} \leqslant n \} = \{\tau \leqslant n \} \cap B \in \mathscr {F} _ {n};
$$

而若 $n \geqslant N$, 则 $\{\sigma_B \leqslant n\} = \{\tau_B \leqslant n\} = \Omega \in \mathscr{F}_n$. 因此, 由假定有 $\mathbf{E}(X_{\sigma_B}) = \mathbf{E}(X_{\tau_B})$, 或写为

$$
\mathbf {E} (X _ {\sigma}; B) + \mathbf {E} (X _ {N}; B ^ {c}) = \mathbf {E} (X _ {\tau}; B) + \mathbf {E} (X _ {N}; B ^ {c}).
$$

这推出

$$
\mathbf {E} (X _ {\sigma}; B) = \mathbf {E} (X _ {\tau}; B) = \mathbf {E} [ \mathbf {E} (X _ {\tau} 1 _ {B} | \mathcal {F} _ {\sigma}) ] = \mathbf {E} [ \mathbf {E} (X _ {\tau} | \mathcal {F} _ {\sigma}); B ].
$$

再由推论2.1.2得 $X_{\sigma} = \mathbf{E}(X_{\tau}|\mathcal{F}_{\sigma})$ .因而 $X$ 是鞅. □

若 $\{X_{n}: n \geqslant 0\}$ 是鞅且 $\tau$ 是有界停时, 则由推论2.3.4有 $\mathbf{E}(X_{\tau}) = \mathbf{E}(X_{0})$. 下面的定理说明这个等式对于某些无界停时也是正确的.

定理 2.3.5 设  $(X_{n}: n \geqslant 0)$  是鞅,  $\tau$  是停时. 如果 (1)  $\mathbf{P}(\tau < \infty) = 1$ ;

(2)  $P|X_{\tau}| < \infty$ ; (3)  $\lim_{n \to \infty} \mathbf{E}(X_{n}; \tau > n) = 0$ , 那么  $\mathbf{E}(X_{\tau}) = \mathbf{E}(X_{0})$ .

证明 利用有界停止定理, 有

$$
\mathbf {E} (X _ {0}) = \mathbf {E} (X _ {\tau \wedge n}) = \mathbf {E} (X _ {\tau}; \tau \leqslant n) + \mathbf {E} (X _ {n}; \tau > n) \rightarrow \mathbf {E} (X _ {\tau}) \quad (n \rightarrow \infty).
$$

这里最后的极限关系成立是由于条件 (1), (2), (3) 及控制收敛定理. □

例 2.3.1 我们在例 2.2.1 中提到过, 在赌博对局中, 鞅表达了一种公平性原则. 然而, 它只说明赌博的每一局是公平的, 其最后的结果仍然可能是不公平的. 考虑由从 0 出发的对称简单随机游动描述的赌博游戏. 赌徒开局时持有赌资为零. 如果他可以决定赌博的停止时间, 那么他可以规定自己在钱数达到 a > 0 后离开. 根据游动的常返性, 他总可实现该目标. 之所以会出现这种不公平的结果, 是因为赌徒可以无利息无限制地借款, 而且可以随意决定停止的时刻. 所以同一个具有无限赌资的赌徒进行赌博是不公平的. 此例还说明杜布停止定理对于一般的 (有限但无界) 停时未必成立.

## 2.3.3 非负上鞅的吸收性

定理 2.3.6 设 X 为非负上鞅. 令  $\sigma = \min\{k \geqslant 0 : X_{k} = 0\}$ ，那么对任意的  $n \geqslant 0$  有  $P\{\sigma \leqslant n, X_{n} > 0\} = 0$ .

证明 固定 $a > 0$, 并令 $\tau = \min \{k \geqslant \sigma : X_k \geqslant a\}$. 易证 $\sigma$ 和 $\tau$ 是停时, 而且 $\sigma \leqslant \tau$. 另外, 显然有 $X_{\sigma} = 0$ 和 $X_{\tau} \geqslant a$. 由定理2.3.3, 对任意的 $n \geqslant 0$ 有

$$
\begin{array}{l} 0 \geqslant \mathbf {E} (X _ {\tau \wedge n} - X _ {\sigma \wedge n}) \\ = \mathbf {E} (X _ {\tau} - X _ {\sigma}; \tau \leqslant n) + \mathbf {E} (X _ {n} - X _ {\sigma}; \sigma <   n <   \tau) + \mathbf {E} (X _ {n} - X _ {n}; \sigma \geqslant n) \\ \geqslant a \mathbf {P} (\tau \leqslant n) + \mathbf {E} (X _ {n}; \sigma <   n <   \tau) \\ \geqslant a \mathbf {P} (\tau \leqslant n). \\ \end{array}
$$

因此 $\mathbf{P}(\tau \leqslant n) = 0$。显然 $\{\sigma \leqslant n, X_n \geqslant a\} \subseteq \{\tau \leqslant n\}$，故 $\mathbf{P}(\sigma \leqslant n, X_n \geqslant a) = 0$。令 $a \to 0$ 即得所需结论。$\square$

上述定理说明非负上鞅在某时刻到达零点后会被该点吸收.

## 练习题

1. 设实值过程 $(X_{n}: n \geqslant 0)$ 关于流 $(\mathcal{F}_n: n \geqslant 0)$ 是可料的鞅. 证明对任何 $n \geqslant 1$ 有 $X_{n} \stackrel{\mathrm{a.s.}}{=} X_{0}$.

2. 设 $(X_{n}: n \geqslant 0)$ 是关于流 $(\mathcal{F}_n: n \geqslant 0)$ 的下鞅. 令 $X_{n}^{*} = \max_{0 \leqslant k \leqslant n} X_{k}$. 证明 $(X_{n}^{*}: n \geqslant 0)$ 是关于 $(\mathcal{F}_n)$ 的下鞅.
3. 设 $(X_{n}: n \geqslant 0)$ 是关于流 $(\mathcal{F}_n: n \geqslant 0)$ 的下鞅, 而 $\{\tau_n : n \geqslant 0\}$ 是单增的有界停时序列. 证明 $(X_{\tau_n})$ 是关于 $(\mathcal{F}_{\tau_n})$ 的下鞅.
4. 设 $(X_{n}: n \geqslant 0)$ 是鞅, 且对有限停时 $\tau$ 满足 $\mathbf{E}(\sup_{k \geqslant 0} |X_{\tau \wedge k}|) < \infty$. 证明 $\mathbf{E}[X_{\tau}] = \mathbf{E}[X_{0}]$.
5. 设 $(S_{n}: n \geqslant 0)$ 是从 $x \in \mathbb{Z}$ 出发的对称简单随机游动. 对 $y \in \mathbb{Z}$ 令 $\tau_{y} = \inf \{n \geqslant 0 : S_{n} = y\}$. 利用 $(S_{n}: n \geqslant 0)$ 的鞅性质证明: 若 $a, b \in \mathbb{Z}$ 满足 $a < x < b$, 则有

$$
\mathbf {P} (\tau_ {b} > \tau_ {a}) = \frac {b - x}{b - a}, \quad \mathbf {P} (\tau_ {a} > \tau_ {b}) = \frac {x - a}{b - a}.
$$

6. 设 $(S_{n}: n \geqslant 0)$ 是从原点出发的对称简单随机游动. 设 $a, b \in \mathbb{Z}$ 满足 $a < 0 < b$. 采用上题的记号, 求 $\tau = \tau_{a} \wedge \tau_{b}$ 的数学期望, 并证明 $\mathbf{E}(\tau_{a}) = \mathbf{E}(\tau_{b}) = \infty$.

提示: 易证  $(S_{n}^{2}-n:n\geqslant0)$  是鞅. 因  $\sup_{k\geqslant0}S_{\tau\wedge k}^{2}\leqslant a^{2}\vee b^{2}$ , 根据有界停止定理和上题的结论,

$$
\mathbf {E} (\tau) = \mathbf {E} (S _ {\tau} ^ {2}) = \frac {a ^ {2} b - a b ^ {2}}{b - a} = - a b.
$$

## 2.4 不等式和收敛定理

鞅、上鞅和下鞅的基本理论是美国数学家杜布建立的.关于它们的很多不等式在随机过程理论中起着重要的作用.本节就离散时间情况讨论这些不等式，并在此基础上证明下鞅的若干收敛定理.这里我们假定所讨论的过程和流定义在概率空间 $(\Omega,\mathscr{F},\mathbf{P})$ 上.

## 2.4.1 基本不等式

定理 2.4.1 设  $(X_{n}: n \geqslant 0)$  是下鞅. 则对任何  $\lambda > 0$  及整数  $n \geqslant 0$  有

$$
\lambda \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) \leqslant \mathbf {E} \Big (X _ {n}; \max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) \leqslant \mathbf {E} (X _ {n} ^ {+}) \tag {2.4.1}
$$

和

$$
\lambda \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} | X _ {k} | \geqslant \lambda \Big) \leqslant 2 \mathbf {E} (X _ {n} ^ {+}) - \mathbf {E} (X _ {0}). \tag {2.4.2}
$$

证明 令 $\tau = \inf \{k\geqslant 0:X_k\geqslant \lambda \}$ ，则 $\tau$ 是停时，所以

$$
\begin{array}{l} \mathbf {E} (X _ {n}) \geqslant \mathbf {E} (X _ {\tau \wedge n}) = \mathbf {E} \Big (X _ {\tau}; \max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) + \mathbf {E} \Big (X _ {n}; \max _ {0 \leqslant k \leqslant n} X _ {k} <   \lambda \Big) \\ \geqslant \lambda \mathbf {E} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) + \mathbf {E} \Big (X _ {n}; \max _ {0 \leqslant k \leqslant n} X _ {k} <   \lambda \Big). \\ \end{array}
$$

因此

$$
\lambda \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) \leqslant \mathbf {E} (X _ {n}) - \mathbf {E} \Big (X _ {n}; \max _ {0 \leqslant k \leqslant n} X _ {k} <   \lambda \Big),
$$

故得 (2.4.1) 式. 再令 $\sigma = \inf \{k \geqslant 0 : X_k \leqslant -\lambda\}$. 与上面类似地, 有

$$
\begin{array}{l} \mathbf {E} (X _ {0}) \leqslant \mathbf {E} (X _ {\sigma \wedge n}) = \mathbf {E} \Big (X _ {\sigma}; \min _ {0 \leqslant k \leqslant n} X _ {k} \leqslant - \lambda \Big) + \mathbf {E} \Big (X _ {n}; \min _ {0 \leqslant k \leqslant n} X _ {k} > - \lambda \Big) \\ \leqslant - \lambda \mathbf {P} \Big (\min _ {0 \leqslant k \leqslant n} X _ {k} \leqslant - \lambda \Big) + \mathbf {E} \Big (X _ {n}; \min _ {0 \leqslant k \leqslant n} X _ {k} > - \lambda \Big). \\ \end{array}
$$

因此

$$
\begin{array}{l} \lambda \mathbf {P} \Big (\min _ {0 \leqslant k \leqslant n} X _ {k} \leqslant - \lambda \Big) \leqslant \mathbf {E} \Big (X _ {n}; \min _ {0 \leqslant k \leqslant n} X _ {k} > - \lambda \Big) - \mathbf {E} (X _ {0}) \\ \leqslant \mathbf {E} (X _ {n} ^ {+}) - \mathbf {E} (X _ {0}). \\ \end{array}
$$

结合上式与 (2.4.1) 式即得 (2.4.2) 式. □

推论 2.4.2 设  $(X_{n}: n \geqslant 0)$  是非负上鞅, 则对任何  $\lambda > 0$  及整数  $n \geqslant 0$  有

$$
\lambda \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant \lambda \Big) = \lambda \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} | - X _ {k} | \geqslant \lambda \Big) \leqslant \mathbf {E} (X _ {0}).
$$

定理 2.4.3 设  $(X_{n}: n \geqslant 0)$  是鞅或非负下鞅, 则对任何  $\lambda > 0, p \geqslant 1$  及整数  $n \geqslant 0$  有

$$
\lambda^ {p} \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} | X _ {k} | \geqslant \lambda \Big) \leqslant \mathbf {E} (| X _ {n} | ^ {p}); \tag {2.4.3}
$$

而对任何 $p > 1$ 及整数 $n \geqslant 0$ 有

$$
\mathbf {E} \Big (\max _ {0 \leqslant k \leqslant n} | X _ {k} | ^ {p} \Big) \leqslant \Big (\frac {p}{p - 1} \Big) ^ {p} \mathbf {E} (| X _ {n} | ^ {p}). \tag {2.4.4}
$$

证明 不妨设 $\mathbf{E}[|X_n|^p] < \infty$. 此时, 由延森不等式易知 $(|X_k|^p : 0 \leqslant k \leqslant n)$ 为下鞅. 再由 (2.4.1) 式得 (2.4.3) 式. 令 $M_n = \max_{0 \leqslant k \leqslant n} |X_k|$. 对下鞅 $(|X_n| : n \geqslant 0)$ 应用 (2.4.1) 式有

$$
t \mathbf {E} (1 _ {\{M _ {n} \geqslant t \}}) = t \mathbf {P} (M _ {n} \geqslant t) \leqslant \mathbf {E} (| X _ {n} |; M _ {n} \geqslant t) = \mathbf {E} (| X _ {n} | 1 _ {\{M _ {n} \geqslant t \}}).
$$

令  $q = p/(p - 1)$ . 由上式及赫尔德 (Hölder) 不等式得到

$$
\begin{array}{l} \mathbf {E} (M _ {n} ^ {p}) = \mathbf {E} \bigg (\int_ {0} ^ {\infty} p t ^ {p - 1} 1 _ {\{t \leqslant M _ {n} \}} \mathrm{d} t \bigg) = p \int_ {0} ^ {\infty} t ^ {p - 1} \mathbf {E} (1 _ {\{t \leqslant M _ {n} \}}) \mathrm{d} t \\ \leqslant p \int_ {0} ^ {\infty} t ^ {p - 2} \mathbf {E} (| X _ {n} | 1 _ {\{t \leqslant M _ {n} \}}) \mathrm{d} t = p \mathbf {E} \bigg (| X _ {n} | \int_ {0} ^ {M _ {n}} t ^ {p - 2} \mathrm{d} t \bigg) \\ = \frac {p}{p - 1} \mathbf {E} (| X _ {n} | M _ {n} ^ {p - 1}) \leqslant q [ \mathbf {E} (| X _ {n} | ^ {p}) ] ^ {\frac {1}{p}} [ \mathbf {E} (M _ {n} ^ {(p - 1) q}) ] ^ {\frac {1}{q}} \\ = q [ \mathbf {E} (| X _ {n} | ^ {p}) ] ^ {\frac {1}{p}} [ \mathbf {E} (M _ {n} ^ {p}) ] ^ {\frac {1}{q}}, \\ \end{array}
$$

两边同除以  $\left[\mathbf{E}(M_{n}^{p})\right]^{\frac{1}{q}}$  即得 (2.4.4) 式. □

## 2.4.2 上穿不等式

下面证明另外一个非常重要的不等式. 考虑实值随机过程 $(X_{n}: n \geqslant 0)$. 对于给定的常数 $-\infty < a < b < \infty$, 我们定义 $\tau_{0} = 0$ 和

$$
\begin{array}{l} \tau_ {1} = \inf \{n \geqslant 0: X _ {n} \leqslant a \}, \\ \tau_ {2} = \inf \{n \geqslant \tau_ {1}: X _ {n} \geqslant b \}, \\ \tau_ {2 k + 1} = \inf \{n \geqslant \tau_ {2 k}: X _ {n} \leqslant a \}, \\ \tau_ {2 k + 2} = \inf \{n \geqslant \tau_ {2 k + 1}: X _ {n} \geqslant b \}, \\ \end{array}
$$

...

...

则 $\{\tau_n : n \geqslant 1\}$ 是一个严格单调上升的停时序列. 对 $N \geqslant 1$ 令

$$
U _ {N} ^ {X} [ a, b ] = \max \{k: \tau_ {2 k} \leqslant N \}.
$$

随机变量  $U_{N}^{X}[a,b]$  记录了过程 X 在时刻 0 到 N 之间上穿区间  $[a,b]$  的次数. 下面是著名的杜布上穿不等式.

定理 2.4.4 设  $(X_{n}: n \geqslant 0)$  是一个下鞅, 则对任何常数 a < b 和非负整数 N, 有

$$
\mathbf {E} \big \{U _ {N} ^ {X} [ a, b ] \big \} \leqslant \frac {1}{b - a} \mathbf {E} \big [ (X _ {N} - a) ^ {+} - (X _ {0} - a) ^ {+} \big ] \leqslant \frac {1}{b - a} \mathbf {E} \big | X _ {N} - a \big |.
$$

证明 令 $Y_{n} = (X_{n} - a)^{+}$, 显然 $(Y_{n})$ 也是一个下鞅. 自然地有 $U_{N}^{X}[a, b] = U_{N}^{Y}[0, b - a]$. 取 $k$ 使 $2k - 1 \geqslant N$, 那么 $\tau_{2k} \geqslant 2k - 1 \geqslant N$, 因此

$$
Y _ {N} - Y _ {0} = \sum_ {n = 1} ^ {2 k} (Y _ {\tau_ {n} \wedge N} - Y _ {\tau_ {n - 1} \wedge N})
$$

$$
\begin{array}{l} = \sum_ {n = 1} ^ {k} (Y _ {\tau_ {2 n} \wedge N} - Y _ {\tau_ {2 n - 1} \wedge N}) + \sum_ {n = 0} ^ {k - 1} (Y _ {\tau_ {2 n + 1} \wedge N} - Y _ {\tau_ {2 n} \wedge N}) \\ \geqslant (b - a) U _ {N} ^ {Y} [ 0, b - a ] + \sum_ {n = 0} ^ {k - 1} (Y _ {\tau_ {2 n + 1} \wedge N} - Y _ {\tau_ {2 n} \wedge N}). \\ \end{array}
$$

因为  $\tau_{2n+1} \geqslant \tau_{2n}$ ，由定理 2.3.3 得

$$
\begin{array}{l} \mathbf {E} (Y _ {N} - Y _ {0}) \geqslant (b - a) \mathbf {E} \big \{U _ {N} ^ {X} [ a, b ] \big \} + \sum_ {n = 0} ^ {k - 1} \big [ \mathbf {P} (Y _ {\tau_ {2 n + 1} \wedge N}) - \mathbf {P} (Y _ {\tau_ {2 n} \wedge N}) \big ] \\ \geqslant (b - a) \mathbf {E} \big \{U _ {N} ^ {X} [ a, b ] \big \}. \\ \end{array}
$$

此即为欲证不等式. □

## 2.4.3 向前收敛定理

利用上穿不等式, 可以证明下面的下鞅收敛定理.

定理 2.4.5 设  $(X_{n}: n \geqslant 0)$  是下鞅且  $K := \sup_{n \geqslant 0} P |X_{n}| < \infty$ ，则当  $n \to \infty$  时有  $X_{n} \stackrel{a.s.}{\rightarrow} X$ ，其中 X 是一个可积随机变量。另外，若  $(X_{n})$  是一致可积下鞅，则  $X_{n} \stackrel{L^{1}}{\rightarrow} X$ ；若  $(X_{n})$  是一致可积鞅，则还有  $X_{n} = \mathbf{E}(X|\mathscr{F}_{n})$ 。

证明 令 $X_{*} = \liminf_{n\to \infty}X_{n}$ 和 $X^{*} = \limsup_{n\to \infty}X_{n}$. $\mathbb{Q}$ 表示有理数集. 显然

$$
\{X _ {*} <   X ^ {*} \} = \bigcup_ {a <   b \in \mathbb {Q}} \{X _ {*} <   a <   b <   X ^ {*} \}.
$$

由上穿不等式

$$
\mathbf {E} \big \{U _ {N} ^ {X} [ a, b ] \big \} \leqslant \frac {1}{b - a} \mathbf {E} | X _ {N} - a | \leqslant \frac {K + | a |}{b - a}.
$$

由单调收敛定理 $\mathbf{E}\big\{\lim_{N\to \infty}U_N^X [a,b]\big\} < \infty$ .因此几乎必然 $\lim_{N\to \infty}U_N^X [a,b] < \infty$ .但是

$$
\{X _ {*} <   a <   b <   X ^ {*} \} \subseteq \Big \{\lim _ {N \to \infty} U _ {N} ^ {X} [ a, b ] = \infty \Big \},
$$

故 $\mathbf{P}\{X_{*} < a < b < X^{*}\} = 0$ ，推出几乎必然 $X^{*} = X_{*}$ .所以几乎必然存在有限或无限的极限 $X\coloneqq = \lim_{n\to \infty}X_n$ .由法图定理有

$$
\mathbf {E} | X | = \mathbf {E} \Big (\operatorname * {l i m i n f} _ {n \to \infty} | X _ {n} | \Big) \leqslant \operatorname * {l i m i n f} _ {n \to \infty} \mathbf {E} | X _ {n} | \leqslant K <   \infty ,
$$

故 $X$ 可积, 因而几乎必然有限. 如果 $\{X_{n}\}$ 是一致可积下鞅, 则由控制收敛定理有 $X_{n} \xrightarrow{L^{1}} X$. 若 $\{X_{n}\}$ 是一致可积鞅, 则有 $X_{n} \xrightarrow{L^{1}} X$ 且对 $k \geqslant n$ 和 $A \in \mathscr{F}_{n}$ 有

$$
\mathbf {E} (X _ {n} 1 _ {A}) = \mathbf {E} [ \mathbf {E} (X _ {k} | \mathcal {F} _ {n}) 1 _ {A} ] = \mathbf {E} (X _ {k} 1 _ {A}),
$$