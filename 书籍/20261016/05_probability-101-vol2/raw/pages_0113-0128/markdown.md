常返类互通类 $H_{n}$ 都是闭集, 即若链从某个 $H_{n}$ 中出发, 则它会永远留在该类中并跑遍 $H_{n}$ 中的所有状态. 若链从暂留类 $U$ 中出发, 则它可能永远在 $U$ 中运动, 也可能会进入某个常返类并留在该类中.

为了表述方便, 不妨写  $E = \{i_{1}, i_{2}, \cdots\}$ . 则将状态按互通等价关系进行排列后, 有分解  $E = U \cup H_{1} \cup H_{2} \cup \cdots$ . 相应地, 可以将转移矩阵 P 写为如下形式:

$$
U H _ {1} H _ {2} \dots H _ {n} \dots
$$

$$
P = \begin{array}{c} U \\ H _ {1} \\ H _ {2} \\ \vdots \\ H _ {n} \\ \vdots \end{array} \left( \begin{array}{c c c c c c} Q & B _ {1} & B _ {2} & \dots & B _ {n} & \dots \\ 0 & P _ {1} & 0 & \dots & 0 & \dots \\ 0 & 0 & P _ {2} & \dots & 0 & \dots \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & P _ {n} & \dots \\ \vdots & \vdots & \vdots & & \vdots \end{array} \right). \tag {4.3.9}
$$

这里 $Q, B_{n}, P_{n}$ 和 0 代表子矩阵, 其中 0 的元素均为零, 而 $Q$ 和 $P_{n}$ 为方阵. 注意 $P_{n}$ 也是转移矩阵, 它描述马氏链在常返互通类 $H_{n}$ 中的运动情况.

特别地, 若 $P$ 是不可约的, 则状态空间 $E$ 只包含暂留互通类或一个常返互通类.

例 4.3.3 设 $X = (X_{n}: n \geqslant 0)$ 为 $\mathbb{Z}$ 上的简单随机游动, 且有 $\mathbf{P}(X_{n+1} - X_{n} = 1) = p$ 和 $\mathbf{P}(X_{n+1} - X_{n} = -1) = q$, 其中 $p, q > 0$ 满足 $p + q = 1$. 对于 $a \in \mathbb{Z}$ 定义 $\tau_{a} = \inf \{n \geqslant 0 : X_{n} = a\}$ 和 $X_{n}^{a} = X_{n \wedge \tau_{a}}$. 则 $X^{a} = (X_{n}^{a}: n \geqslant 0)$ 为在 $a$ 被吸收的简单随机游动, 其转移矩阵 $P^{a} = (p_{ij}^{a}: i, j \in \mathbb{Z})$ 可表示为

$$
p _ {i j} ^ {a} = p 1 _ {\{a \neq i = j - 1 \}} + q 1 _ {\{a \neq i = j + 1 \}} + 1 _ {\{a = i = j \}}.
$$

易知 $X^{a}$ 有暂留类 $U = \mathbb{Z} \setminus \{a\}$ 和唯一的常返互通类 $H = \{a\}$. 显然 $(- \infty, a], \{a\}$ 和 $[a, \infty)$ 都是 $X^{a}$ 的闭集.

例 4.3.4 设 $X = (X_{n}: n \geqslant 0)$ 为例 4.3.3 中的简单随机游动. 对 $a < b \in \mathbb{Z}$ 记 $\tau = \inf \{n \geqslant 0 : X_{n} = a \text{ 或 } b\}$. 再令 $Y_{n} = X_{n \wedge \tau}$, 则 $Y = (Y_{n}: n \geqslant 0)$ 仍然是 $\mathbb{Z}$ 上的马氏链. 特别地, 若 $\mathbf{P}(a \leqslant X_{0} \leqslant b) = 1$, 则 $Y$ 是 $[a, b]$ 上的马氏链, 称为该区间上的吸收边界简单随机游动, 其转移矩阵 $P^{a, b} = (p_{ij}^{a, b}: i, j \in \mathbb{Z})$ 可表示为

$$
p _ {i j} ^ {a, b} = p 1 _ {\{i > a, j = i + 1 \leqslant b \}} + q 1 _ {\{i <   b, j = i - 1 \geqslant a \}} + 1 _ {\{i = j = a \}} + 1 _ {\{i = j = b \}}.
$$

此时 $Y$ 的暂留类为整数开区间 $U = (a, b)$. 它有两个常返类, 即 $H_{1} = \{a\}$ 和 $H_{2} = \{b\}$.

## 4.3.4 周期性

定义 4.3.4 对于 $i \in E$, 若集合 $\{n \geqslant 1 : p_{ii}(n) > 0\}$ 非空, 就称它的最大公约数 $d$ 为 $i$ 的周期. 当 $d \geqslant 2$ 时称 $i$ 是周期的; 当 $d = 1$ 时称 $i$ 是非周期的. 若 $E$ 中的所有状态都是非周期的, 则称 X 或 P 是非周期的.

根据上面的定义, 若状态 $i \in E$ 有周期 $d \geqslant 1$, 则从此状态出发的链只能在时间集 $\{kd : k \geqslant 0\}$ 回访该状态, 而对于该集合之外的时刻 $n \geqslant 1$ 都有 $p_{ii}(n) = 0$.

定理 4.3.11 若  $i \in E$  以 d 为周期, 则存在  $k_{i} \geqslant 1$ , 使当  $k \geqslant k_{i}$  时有  $p_{ii}(kd) > 0$ .

证明 将非空集  $\{n\geqslant1:p_{ii}(n)>0\}$  记为  $\{n_{1},n_{2},\cdots\}$ . 令  $d_{m}$  为  $\{n_{1},n_{2},\cdots,n_{m}\}$  的最大公约数. 显然, 当  $m\to\infty$  时递降地  $d_{m}\to d$ . 故存在充分大的  $m\geqslant1$  使  $d_{m}=d$ , 亦即 d 为  $\{n_{1},n_{2},\cdots,n_{m}\}$  的最大公约数. 由数论中的结果, 存在  $k_{i}\geqslant1$  使当  $k\geqslant k_{i}$  时有  $kd=t_{1}n_{1}+t_{2}n_{2}+\cdots+t_{m}n_{m}$ , 其中  $t_{1},t_{2}\cdots,t_{m}\geqslant0$  为整数. 因而

$$
p _ {i i} (k d) \geqslant \prod_ {r = 1} ^ {m} p _ {i i} (t _ {r} n _ {r}) \geqslant \prod_ {r = 1} ^ {m} p _ {i i} (n _ {r}) ^ {t _ {r}}.
$$

于是有 $p_{ii}(kd) > 0$ □

定理 4.3.12 同一互通类中的状态有相同的周期.

证明 设 $i, j \in E$ 互通, 并设 $i$ 以 $d$ 为周期, 而 $j$ 以 $t$ 为周期. 由定理4.3.11, 存在 $k_j \geqslant 1$ 使当 $k \geqslant k_j$ 时, 有 $p_{jj}(kt) > 0$. 取 $m, n \geqslant 1$ 使 $p_{ij}(m)p_{ji}(n) > 0$. 这样, 当 $k \geqslant k_j$ 时有

$$
p _ {i i} (m + n + k t) \geqslant p _ {i j} (m) p _ {j j} (k t) p _ {j i} (n) > 0.
$$

因为 i 以 d 为周期, 所以必存在  $r_{2} > r_{1} \geqslant 1$  使

$$
m + n + k _ {j} t = r _ {1} d, m + n + (k _ {j} + 1) t = r _ {2} d.
$$

将两式相减得 $t = (r_2 - r_1)d$. 同理知存在 $l_2 > l_1 \geqslant 1$ 使 $d = (l_2 - l_1)t$. 因此必然有 $r_2 - r_1 = l_2 - l_1 = 1$, 即 $t = d$. $\square$

定理 4.3.13 设 P 不可约且有周期  $d \geqslant 1$ ，则对任何  $i, j \in E$  存在唯一的  $0 \leqslant t_{ij} < d$  使得  $p_{ij}(n) > 0$  蕴涵  $n = kd + t_{ij}$ ，其中  $k \geqslant 0$ .

证明 设对 $n \geqslant 1$ 有 $p_{ij}(n) > 0$. 令 $t_{ij} = n (\bmod d)$, 则 $0 \leqslant t_{ij} < d$ 且有 $k \geqslant 0$ 使 $n = kd + t_{ij}$. 假设还有 $m \geqslant 1$ 使得 $p_{ij}(m) > 0$. 因 $P$ 不可约, 有 $l \geqslant 1$ 使得 $p_{ji}(l) > 0$, 从而

$$
p _ {i i} (n + l) \geqslant p _ {i j} (n) p _ {j i} (l) > 0, p _ {i i} (m + l) \geqslant p _ {i j} (m) p _ {j i} (l) > 0.
$$

由周期的定义知 $d$ 整除 $n + l$ 和 $m + l$. 因此 $d$ 整除 $n - m$, 故定理结论成立. $\square$

定理 4.3.14 设 P 不可约且有周期  $d \geqslant 1$ . 令  $i, j \in E$  而  $0 \leqslant t_{ij} < d$  由定理 4.3.13 给出, 则存在  $k_{ij} \geqslant 1$  使当  $k \geqslant k_{ij}$  时有  $p_{ij}(kd + t_{ij}) > 0$ .

证明 因 $P$ 不可约, 有 $n_0 \geqslant 1$ 使 $p_{ij}(n_0) > 0$. 由定理4.3.13有 $k_0 \geqslant 0$ 使 $n_0 = k_0d + t_{ij}$. 再由定理4.3.11有 $k_j \geqslant 1$, 使当 $k \geqslant k_j$ 时有 $p_{jj}(kd) > 0$. 令 $k_{ij} = k_0 + k_j$, 则对 $k \geqslant k_{ij}$ 有 $k - k_0 \geqslant k_j$, 故 $p_{ij}(kd + t_{ij}) \geqslant p_{ij}(n_0)p_{jj}((k - k_0)d) > 0$. $\square$

考虑 $E$ 上的以 $d \geqslant 1$ 为周期的不可约转移矩阵 $P$. 取定初始状态 $i \in E$. 对于 $0 \leqslant k < d$ 令

$C_{k}=\{j\in E:$ 对充分大的 n 从 i 出发的链在时刻 $nd+k$ 以正概率到 j\}.

由定理 4.3.13 和定理 4.3.14 可知  $\{C_{0}, C_{1}, \cdots, C_{d-1}\}$  是 E 的一个有限分割, 而且链从  $C_{r}$  中的状态可以而且只可以经过  $s - r \pmod{d}$  步到达  $C_{s}$  中的状态. 特别地, 从  $C_{0}$  中的状态出发的链会一直按照下面的顺序做循环运动:

$$
C _ {0} \rightarrow C _ {1} \rightarrow \dots \rightarrow C _ {d - 1} \rightarrow C _ {0} \rightarrow C _ {1} \rightarrow \dots . \tag {4.3.10}
$$

我们称  $E = C_{0} \cup C_{1} \cup \cdots \cup C_{d-1}$  为转移矩阵 P 的周期环分解. 不难证明, 除分解集  $C_{0}, C_{1}, \cdots, C_{d-1}$  的标号可能有变化外, 该分解并不依赖于初始状态  $i \in E$  的选择. 而且, 选择  $C_{0}$  中的任何一点作为初始状态, 所得到分解集的标号完全相同.

## \*4.3.5 过份函数

在本小节中, 我们将利用过份函数给出常返性的一个充要条件. 考虑状态空间 $E$ 上的马氏链 $X = (X_{n}: n \geqslant 0)$, 设其转移矩阵为 $P = (p_{ij}: i, j \in E)$.

定义 4.3.5 设 f 是定义在 E 上的非负函数, 可以取值  $\infty$ . 如果

$$
\sum_ {j \in E} p _ {i j} f (j) \leqslant f (i), \quad i \in E,
$$

就称 $f$ 是 $X$ 或 $P$ 的过份函数. 这里约定 $0 \cdot \infty = 0$. 若把 $f$ 视为由它的值排成的列向量, 则上式可简写为矩阵形式 $Pf \leqslant f$. 特别地, 如果 $Pf = f$, 我们称 $f$ 是一个调和函数.

定理 4.3.15 设 P 不可约, 则 P 是常返的当且仅当它的所有过份函数均为常数.

证明 假设 $P$ 常返而 $f$ 为它的过份函数. 假若存在 $j \in E$ 使得 $f(j) = \infty$, 由不可约性对于 $i \in E$ 存在 $n_0 \geqslant 0$ 使 $p_{ij}(n_0) > 0$, 故

$$
f (i) \geqslant \sum_ {k \in E} p _ {i k} (n _ {0}) f (k) = \infty ,
$$

即 $f \equiv \infty$. 因此, 只需考虑 $f$ 有限的情况. 记 $X$ 的自然流为 $(\mathcal{F}_n : n \geqslant 0)$. 对于 $x \in E$ 有

$$
\mathbf {E} (f (X _ {n + 1}) | X _ {n} = x) = \sum_ {k \in E} p (x, k) f (k) \leqslant f (x).
$$

应用马氏性得

$$
\mathbf {E} (f (X _ {n + 1}) | \mathcal {F} _ {n}) = \mathbf {E} (f (X _ {n + 1}) | X _ {n}) \leqslant f (X _ {n}).
$$

所以 $\{f(X_n): n \geqslant 0\}$ 是非负上鞅, 故几乎必然存在极限 $\lim_{n \to \infty} f(X_n) = Z$。另一方面, 由于 $P$ 常返不可约, 对任何 $j, k \in E$ 有

$\mathbf{P}(X_n = j$ 对无限个 $n\geqslant 1$ 成立) $= \mathbf{P}(X_{n} = k$ 对无限个 $n\geqslant 1$ 成立) $= 1$

因此

$$
\begin{array}{l} \mathbf {P} (f (X _ {n}) = f (j) \text {对无限个} n \geqslant 1 \text {成立}) \\ = \mathbf {P} \left(f \left(X _ {n}\right) = f (k) \text {对无限个} n \geqslant 1 \text {成立}\right) = 1, \\ \end{array}
$$

可见 $\mathbf{P}(f(k) = f(j) = Z) = 1$。故必有 $f \equiv$ 常数。反之，假设 $P$ 是暂留的，下证它有非常数的过份函数。固定 $j \in E$ 并定义首达时 $\tau = \inf \{n \geqslant 0 : X_n = j\}$ 和击中时 $T = \inf \{n \geqslant 1 : X_n = j\}$。根据全概率公式有

$$
\mathbf {P} _ {i} (T <   \infty) = \sum_ {k \in E} p _ {i k} \mathbf {P} _ {i} (T <   \infty | X _ {1} = k) = \sum_ {k \in E} p _ {i k} \mathbf {P} _ {k} (\tau <   \infty). \tag {4.3.11}
$$

注意 $\mathbf{P}_i(T < \infty) \leqslant \mathbf{P}_i(\tau < \infty)$. 所以, 上式说明

$$
f (i) := \mathbf {P} _ {i} (\tau <   \infty) = \left\{ \begin{array}{l l} 1, & i = j, \\ f _ {i j} ^ {*}, & i \neq j \end{array} \right. \tag {4.3.12}
$$

定义了 $P$ 的一个有界过份函数 $f$. 此函数不是常数. 否则对任何 $k \in E$ 有 $f(k) = \mathbf{P}_k(\tau < \infty) = 1$. 再由 (4.3.11) 式知 $f_{jj}^* = \mathbf{P}_j(T < \infty) = 1$. 这与 $P$ 是暂留的假设矛盾. $\square$

推论 4.3.16 设 P 不可约, 并取  $j \in E$ . 则 P 是暂留的当且仅当方程组

$$
y _ {i} = \sum_ {k \in E} p _ {i k} y _ {k}, \quad i \in E \setminus \{j \} \tag {4.3.13}
$$

有非常数的有界解  $\{y_{i}: i \in E\}$ .

证明 沿用定理4.3.15的证明中的记号. 设 $P$ 是暂留的. 注意对 $k \neq j$ 有 $\mathbf{P}_k (T < \infty) = \mathbf{P}_k (\tau < \infty)$. 所以由(4.3.12)式定义的函数 $f$ 就给出(4.3.13)式的一个非常数的有界解. 反之, 假若 (4.3.13) 式有非常数有界解 $\{y_{i}: i \in E\}$, 因常函数是该方程组的解, 我们可假定 $\{y_{i}: i \in E\}$ 由非负数构成. 令

$$
a = y _ {j} - \sum_ {k \in E} p _ {j k} y _ {k}. \tag {4.3.14}
$$

利用 (4.3.13) 式和 (4.3.14) 式有

$$
\begin{array}{l} \sum_ {k \in E} p _ {j k} (2) y _ {k} = \sum_ {k \in E} \sum_ {i \neq j} p _ {j i} p _ {i k} y _ {k} + \sum_ {k \in E} p _ {j j} p _ {j k} y _ {k} \\ = \sum_ {i \neq j} p _ {j i} y _ {i} + p _ {j j} (y _ {j} - a) \\ = \sum_ {i \in E} p _ {j i} y _ {i} - a p _ {j j} = y _ {j} - a - a p _ {j j}. \\ \end{array}
$$

比较此式和 (4.3.14) 式不难看出, 重复上面的运算可得

$$
\sum_ {k \in E} p _ {j k} (n) y _ {k} = y _ {j} - a \sum_ {m = 0} ^ {n - 1} p _ {j j} (m).
$$

因此有

$$
c := \sup _ {k \in E} y _ {k} \geqslant y _ {j} - a \sum_ {m = 0} ^ {n - 1} p _ {j j} (m).
$$

假若 $a < 0$, 则由上式有 $\sum_{m=1}^{\infty} p_{jj}(m) < \infty$, 故 $j$ 为暂留态, 再由不可约性知 $P$ 是暂留的. 而若 $a \geqslant 0$, 由 (4.3.13) 式和 (4.3.14) 式知 $f(i) = y_i$ 定义了 $P$ 的一个非常值的过份函数, 再由定理 4.3.15 知 $P$ 是暂留的. □

## 练习题

1. 设 $(X_{n}: n \geqslant 0)$ 是状态空间 $E$ 上的不可约马氏链. 证明该链是常返的 (或暂留的) 当且仅当对任意的 $i \in E$ 有

$$
\mathbf {P} \bigg (\bigcap_ {n = 1} ^ {\infty} \bigcup_ {k = n} ^ {\infty} \{X _ {k} = i \} \bigg) = 1 (\text {或} 0).
$$

提示: 令  $\tau_{i}=\inf\{n\geqslant0:X_{n}=i\}$  并应用推论 4.3.2 和强马氏性.

2. 证明: 状态空间 E 有限的马氏链至少有一个常返态.

提示: 对 $k \in E$ 有 $\sum_{i \in E} p_{ki}^{*} = \infty$. 因 $E$ 是有限集, 必有 $i \in E$ 使 $p_{ki}^{*} = \infty$. 再应用推论 4.3.5.

3. 设状态空间 $E$ 上的马氏链 $X$ 有一个吸收态 $i \in E$, 且从任何其他状态都可达 $i$. 证明除点 $i$ 外 $E$ 中其他的点都是暂留的.
4. 设 $(X_{n}: n \geqslant 0)$ 是状态空间 $\mathbb{Z}$ 上的马氏链. 证明它是暂留的当且仅当对任何初始分布都有 $\lim_{n \to \infty} |X_{n}| \stackrel{\text{a.s.}}{=} \infty$.

提示: 若对任何初始分布都有 $\lim_{n\to \infty}|X_n|^{\text{a.s.}} = \infty$, 则对任何 $i\in E$ 等式 (4.3.4) 左边的概率为 0, 故 $(X_{n}:n\geqslant 0)$ 是暂留的. 反之, 设 $(X_{n}:n\geqslant 0)$ 是暂留的, 则对任何 $i\in E$ 等式 (4.3.4) 左边的概率为 0. 令 $\tau = \inf \{n\geqslant 0:X_n = i\}$. 利用强马氏性和推论 4.3.2 得

$$
\begin{array}{l} \mathbf {P} \bigg (\bigcap_ {n = 1} ^ {\infty} \bigcup_ {k = n} ^ {\infty} \{X _ {k} = i \} \bigg) = \mathbf {P} \bigg (\{\tau <   \infty , X _ {\tau} = i \} \cap \bigg (\bigcap_ {n = 1} ^ {\infty} \bigcup_ {k = n} ^ {\infty} \{X _ {\tau + k} = i \} \bigg) \bigg) \\ = \mathbf {P} (\tau <   \infty , X _ {\tau} = i) \mathbf {P} _ {i} \bigg (\bigcap_ {n = 1} ^ {\infty} \bigcup_ {k = n} ^ {\infty} \{X _ {k} = i \} \bigg) = 0. \\ \end{array}
$$

5. 令 $\{a_k\}$ 为 $\mathbb{Z}_+$ $= \{0,1,2,\dots\}$ 上的概率分布列, 满足 $a_0 > 0$ 和 $\mu := \sum_{k=1}^{\infty} ka_k > 1$. 定义 $\mathbb{Z}_+$ 上转移矩阵 $P$ 如下:

$$
p _ {i j} = \left\{ \begin{array}{l l} a _ {j}, & i = 0, \\ a _ {j - i + 1}, & i \geqslant 1 \text {且} j \geqslant i - 1, \\ 0, & \text {其他.} \end{array} \right.
$$

证明 P 是暂留的.

提示: 注意 P 是不可约的. 令  $f(z)=\sum_{k=0}^{\infty}a_{k}z^{k}$  为  $\{a_{k}\}$  的母函数. 由 f 的凸性, 存在唯一的  $c\in(0,1)$  使  $c=f(c)$ , 故对  $i\geqslant1$  有

$$
c ^ {i} = \sum_ {k = 0} ^ {\infty} a _ {k} c ^ {k + i - 1} = \sum_ {j = i - 1} ^ {\infty} a _ {j - i + 1} c ^ {j} = \sum_ {j = 0} ^ {\infty} p _ {i j} c ^ {j}.
$$

## 4.4 马氏链的游程

本节对马氏链的游程进行简单的讨论, 并给出反射游动的一个简单构造. 在此基础上, 讨论如何对常返简单游动进行拆解, 得到两个独立的反射游动.

## 4.4.1 游程的独立性

令 $X = \{X(n):n\geqslant 0\}$ 是定义在某个概率空间 $(\Omega ,\mathcal{F},\mathbf{P})$ 上的以 $E$ 为状态空间、以 $P = (p(i,j):i,j\in E)$ 为转移矩阵的马氏链.取定两个不同的状态 $a,b\in \mathbb{Z}$ .令$\tau_0 = 0$ 并对 $k\geqslant 1$ 递推地定义

$$
\sigma_ {k} = \inf \{n \geqslant \tau_ {k - 1}: X (n) = b \}, \tau_ {k} = \inf \{n > \sigma_ {k}: X (n) = a \}. \tag {4.4.1}
$$

则 $\sigma_{k}$ 和 $\tau_{k}$ 都是停时. 令

$$
e _ {k} = \{X ((\sigma_ {k} + n) \land \tau_ {k}): n \geqslant 0 \}, \varepsilon_ {k} = \{X ((\tau_ {k} + n) \land \sigma_ {k + 1}): n \geqslant 0 \}. \tag {4.4.2}
$$

再记 $\phi_0 = \{X(n\wedge \sigma_1):n\geqslant 0\}$. 当 $\sigma_{k} < \infty$ 时, 称 $e_k$ 为 $X$ 的第 $k$ 个由 $b$ 到 $a$ 的游程. 注意当 $\sigma_{k} = \infty$ 时 $e_k$ 为空集. 显然, 若 $\tau_{1} < \infty$, 则 $\varepsilon_{1}$ 是过程 $\{X(\tau_1 + n):n\geqslant 0\}$ 的第 1 个由 $a$ 到 $b$ 的游程, 但它未必是 $X$ 的第 1 个由 $a$ 到 $b$ 的游程, 因为后者可能包含在 $\phi_0$ 中. 特别地, 若 $X$ 是不可约常返链, 则 (4.4.1) 式和 (4.4.2) 式中定义的所有停时都是有限的.

根据强马氏性, 在条件概率 $\mathbf{P}(\cdot|\sigma_k < \infty)$ 之下 $\{X(\sigma_k + n): n \geqslant 0\}$ 是从 $b$ 出发以 $P$ 为转移矩阵的马氏链. 因此, 在上述条件概率之下 $e_k$ 是从 $b$ 出发在 $a$ 停止的马氏链, 其转移矩阵 $P^a = (p^a(i,j): i, j \in E)$ 可表示为

$$
p ^ {a} (i, j) = p (i, j) 1 _ {\{i \neq a \}} + 1 _ {\{i = a = j \}}.
$$

类似地, 在条件概率  $\mathbf{P}(\cdot|\tau_{k}<\infty)$  之下  $\varepsilon_{k}$  是从 a 出发在 b 停止的马氏链, 其转移矩阵  $P^{b}=(p^{b}(i,j):i,j\in E)$  可表示为

$$
p ^ {b} (i, j) = p (i, j) 1 _ {\{i \neq b \}} + 1 _ {\{i = b = j \}}.
$$

我们称  $k (\geqslant 2)$  个随机过程  $\xi_{1} = (\xi_{1}(n) : n \geqslant 0), \xi_{2} = (\xi_{2}(n) : n \geqslant 0), \cdots, \xi_{k} = (\xi_{k}(n) : n \geqslant 0)$  独立，是指对任意的  $n \geqslant 0$ ，随机向量  $(\xi_{1}(0), \xi_{1}(1), \cdots, \xi_{1}(n)), (\xi_{2}(0), \xi_{2}(1), \cdots, \xi_{2}(n)), \cdots, (\xi_{k}(0), \xi_{k}(1), \cdots, \xi_{k}(n))$  独立。称可数个随机过程  $\xi_{1}, \xi_{2}, \cdots$  独立，是指对任意的  $k \geqslant 2$ ，有限随机过程组  $\xi_{1}, \xi_{2}, \cdots, \xi_{k}$  独立。

定理 4.4.1 设  $X = \{X(n) : n \geqslant 0\}$  是不可约常返马氏链. 则如上定义的  $\phi_{0}, e_{k}, \varepsilon_{k}, k \geqslant 1$  为独立的随机过程, 且其中  $\phi_{0}$  是以  $P^{b}$  为转移矩阵的马氏链,  $e_{k}, k \geqslant 1$  是从 b 出发以  $P^{a}$  为转移矩阵的马氏链, 而  $\varepsilon_{k}, k \geqslant 1$  是从 a 出发以  $P^{b}$  为转移矩阵的马氏链.

证明 显然 $\phi_0$ 是以 $P^b$ 为转移矩阵的马氏链. 根据强马氏性, 在条件概率 $\mathbf{P}(\cdot|\sigma_k < \infty) = \mathbf{P}(\cdot|\sigma_k < \infty, X_{\sigma_k} = b)$ 之下 $\{X(\sigma_k + n): n \geqslant 0\}$ 是从 $b$ 出发以 $P$ 为转移矩阵的马氏链且与 $\{X(n \wedge \sigma_k): n \geqslant 0\}$ 独立. 类似地, 对 $k \geqslant 1$ 在条件概率 $\mathbf{P}(\cdot|\tau_k < \infty) =$ $\mathbf{P}(\cdot|\tau_k < \infty, X_{\tau_k} = a)$ 之下 $\{X(\tau_k + n): n \geqslant 0\}$ 是从 $a$ 出发以 $P$ 为转移矩阵的马氏链且与 $\{X(n \wedge \tau_k): n \geqslant 0\}$ 独立. 由 $X$ 的不可约性和常返性, 有

$$
\mathbf {P} (\sigma_ {k} <   \infty , X _ {\sigma_ {k}} = b) = \mathbf {P} (\tau_ {k} <   \infty , X _ {\tau_ {k}} = a) = 1.
$$

所以, 对 $k \geqslant 1$ 在原概率 $\mathbf{P}$ 之下 $\{X(\sigma_k + n): n \geqslant 0\}$ 是从 $b$ 出发以 $P$ 为转移矩阵的马氏链且与 $\{X(n \wedge \sigma_k): n \geqslant 0\}$ 独立, 而 $\{X(\tau_k + n): n \geqslant 0\}$ 是从 $a$ 出发以 $P$ 为转移矩阵的马氏链且与 $\{X(n \wedge \tau_k): n \geqslant 0\}$ 独立. 由此可知 $e_k, k \geqslant 1$ 是从 $b$ 出发以 $P^a$ 为转移矩阵的马氏链, 而 $\varepsilon_k, k \geqslant 1$ 是从 $a$ 出发以 $P^b$ 为转移矩阵的马氏链. 再注意 $\{\phi_0, e_1, \varepsilon_1, \cdots, e_{k-1}, \varepsilon_{k-1}\}$ 由 $\{X(n \wedge \sigma_k): n \geqslant 0\}$ 决定, 而 $\{e_k, \varepsilon_k, e_{k+1}, \varepsilon_{k+1}, \cdots\}$ 由 $\{X(\sigma_k + n): n \geqslant 0\}$ 决定, 故 $\{\phi_0, e_1, \varepsilon_1, \cdots, e_{k-1}, \varepsilon_{k-1}\}$ 和 $\{e_k, \varepsilon_k, e_{k+1}, \varepsilon_{k+1}, \cdots\}$ 独立. 同理 $\{\phi_0, e_1, \varepsilon_1, \cdots, e_{k-1}, \varepsilon_{k-1}, e_k\}$ 和 $\{\varepsilon_k, e_{k+1}, \varepsilon_{k+1}, \cdots\}$ 独立. 由此易证 $\phi_0, e_1, \varepsilon_1, e_2, \varepsilon_2, \cdots$ 的独立性. □

## 4.4.2 反射简单随机游动

设 $p, q \geqslant 0$ 满足 $p + q = 1$. 我们知道, 一维简单随机游动的转移矩阵 $P = (p(i, j): i, j \in \mathbb{Z})$ 可以表示为

$$
p (i, j) = p 1 _ {\{j = i + 1 \}} + q 1 _ {\{j = i - 1 \}}. \tag {4.4.3}
$$

对于 $a \in \mathbb{Z}$, 称以 $\mathbb{Z}_{a+} := \mathbb{Z} \cap [a, \infty)$ 为状态空间的马氏链为反射简单随机游动, 是指它有转移矩阵 $Q_{+}^{a} = (q_{+}^{a}(i, j): i, j \in \mathbb{Z}_{a+})$, 其中

$$
q _ {+} ^ {a} (i, j) = p 1 _ {\{a <   i = j - 1 \}} + q 1 _ {\{a <   i = j + 1 \}} + 1 _ {\{a = i = j - 1 \}}. \tag {4.4.4}
$$

称以  $\mathbb{Z}_{a-} := \mathbb{Z} \cap (-\infty, a]$  为状态空间的马氏链为反射简单随机游动, 是指它有转移矩阵  $Q_{-}^{a} = (q_{-}^{a}(i, j) : i, j \in \mathbb{Z}_{a+})$ , 其中

$$
q _ {-} ^ {a} (i, j) = p 1 _ {\{a > i = j - 1 \}} + q 1 _ {\{a > i = j + 1 \}} + 1 _ {\{a = i = j + 1 \}}. \tag {4.4.5}
$$

对于 $a < b \in \mathbb{Z}$, 称以 $\mathbb{Z}_{a,b} := \mathbb{Z} \cap [a, b]$ 为状态空间的马氏链是反射简单随机游动, 是指它有转移矩阵 $Q^{a,b} = (q^{a,b}(i,j): i, j \in \mathbb{Z}_{a,b})$, 其中

$$
q ^ {a, b} (i, j) = p 1 _ {\{i > a, j = i + 1 \leqslant b \}} + q 1 _ {\{i <   b, j = i - 1 \geqslant a \}} + 1 _ {\{i = a, j = i + 1 \}} + 1 _ {\{i = b, j = b - 1 \}}. \tag {4.4.6}
$$

例 4.4.1 令  $(X_{n}: n \geqslant 0)$  是一维对称简单随机游动. 不难证明  $(|X_{n}|: n \geqslant 0)$  是  $Z_{+}$ 上的反射随机游动, 而  $(-|X_{n}|: n \geqslant 0)$  是  $Z_{-}$ 上的反射随机游动.

注意, 在 $a \in \mathbb{Z}$ 被吸收的简单游动的转移矩阵 $P^a = (p^a(i,j):i,j \in \mathbb{Z})$ 可以表示为

$$
p ^ {a} (i, j) = p 1 _ {\{a \neq i = j - 1 \}} + q 1 _ {\{a \neq i = j + 1 \}} + 1 _ {\{a = i = j \}}. \tag {4.4.7}
$$

定理 4.4.2 设 $e_k, k \geqslant 1$ 是一列独立的从 $a + 1$ 出发且在 $a$ 被吸收的简单游动，其转移矩阵 $P^a$ 由 (4.4.7) 式给出。记 $S_1 = 0$，并对 $k \geqslant 2$ 记 $S_k = \sum_{i=1}^{k-1} (\zeta_i + 1)$，其中 $\zeta_i = \inf\{n \geqslant 0 : e_i(n) = a\}$。再令

$$
W _ {n} = e _ {k} (n - S _ {k}), \quad S _ {k} \leqslant n <   S _ {k + 1}, \tag {4.4.8}
$$

则 $W = (W_{n}:n\geqslant 0)$ 是 $\mathbb{Z}_{a + }$ 上的从 $a + 1$ 出发的反射简单随机游动.

证明 令 $(\mathscr{F}_n)$ 是 $W$ 是的自然流. 令 $T_1 = 0$, 并对 $k \geqslant 2$ 令 $T_k = S_k - 1$. 显然有 $S_k = \inf\{n \geqslant T_k : W_n = a + 1\}$ 和 $T_k = \inf\{n \geqslant S_{k-1} : W_n = a\}$. 据此易证 $S_k$ 和 $T_k$ 都是 $(\mathscr{F}_n)$ 的停时. 注意 $S_k$ 和 $T_k$ 都只依赖于 $e_1, e_2, \cdots, e_{k-1}$. 给定 $i_0, i_1, \cdots, i_n \in \mathbb{Z}_{a+}$, 记 $G_n = \{W_r = i_k : 0 \leqslant r \leqslant n\}$. 再任取 $j \in \mathbb{Z}_{a+}$. 对于 $k \geqslant 1$ 和 $0 \leqslant r \leqslant n$, 利用 $e_1, e_2, \cdots, e_k$ 的独立性和马氏性有

$$
\begin{array}{l} \mathbf {P} (\{S _ {k} = r, T _ {k + 1} > n \} \cap G _ {n} \cap \{W _ {n + 1} = j \}) \\ = \mathbf {P} (\{S _ {k} = r \} \cap \{\zeta_ {k} > n - r \} \cap G _ {r - 1} \cap \{e _ {k} (0) = i _ {r}, \dots , \\ e _ {k} (n - r) = i _ {n} \} \cap \{e _ {k} (n - r + 1) = j \}\left. \right) \\ = \mathbf {P} (\{S _ {k} = r \} \cap G _ {r - 1} \cap \{e _ {k} (0) = i _ {r}, \dots , e _ {k} (n - r) = i _ {n} \} \cap \\ \{\zeta_ {k} > n - r \} \cap \{e _ {k} (n - r + 1) = j \}\left. \right) \\ = \mathbf {P} (\{S _ {k} = r \} \cap G _ {r - 1}) \mathbf {P} (\{e _ {k} (0) = i _ {r}, \dots , e _ {k} (n - r) = i _ {n} \} \cap \\ \{\zeta_ {k} > n - r \} \cap \{e _ {k} (n - r + 1) = j \}\left. \right) \\ = \mathbf {P} (\{S _ {k} = r \} \cap G _ {r - 1}) \mathbf {P} (\{e _ {k} (0) = i _ {r}, \dots , e _ {k} (n - r) = i _ {n} \} \cap \\ \{\zeta_ {k} > n - r \}) p ^ {a} (i _ {n}, j) \\ = \mathbf {P} (\{S _ {k} = r \} \cap G _ {r - 1} \cap \{e _ {k} (0) = i _ {r}, \dots , e _ {k} (n - r) = i _ {n} \} \cap \\ \{\zeta_ {k} > n - r \}) q _ {+} ^ {a} (i _ {n}, j) \\ = \mathbf {P} (\{S _ {k} = r, T _ {k + 1} > n \} \cap G _ {n}) q _ {+} ^ {a} (i _ {n}, j). \\ \end{array}
$$

类似地，

$$
\begin{array}{l} \mathbf {P} (\{S _ {k} = r, T _ {k + 1} = n \} \cap G _ {n} \cap \{W _ {n + 1} = j \}) \\ = \mathbf {P} (\{S _ {k} = r \} \cap \{\zeta_ {k} = n - r \} \cap G _ {r - 1} \cap \{e _ {k} (0) = i _ {r}, \dots , \\ e _ {k} (n - r) = i _ {n} \} \cap \{e _ {k + 1} (0) = j \}) \\ = \mathbf {P} (\{S _ {k} = r \} \cap G _ {r - 1} \cap \{e _ {k} (0) = i _ {r}, \dots , e _ {k} (n - r) = i _ {n} \} \cap \\ \{\zeta_ {k} = n - r \} \cap \{e _ {k + 1} (0) = j \}) 1 _ {\{i _ {n} = a, j = a + 1 \}} \\ = \mathbf {P} (\{S _ {k} = r \} \cap G _ {r - 1} \cap \{e _ {k} (0) = i _ {r}, \dots , e _ {k} (n - r) = i _ {n} \} \cap \\ \end{array}
$$

$$
\begin{array}{l} \{\zeta_ {k} = n - r \}) 1 _ {\{i _ {n} = a, j = a + 1 \}} q _ {+} ^ {a} (i _ {n}, j) \\ = \mathbf {P} (\{S _ {k} = r, T _ {k + 1} = n \} \cap G _ {n}) q _ {+} ^ {a} (i _ {n}, j). \\ \end{array}
$$

将上面两式相加得

$$
\begin{array}{l} \mathbf {P} (\{S _ {k} = r, n \leqslant T _ {k + 1} \} \cap G _ {n} \cap \{W _ {n + 1} = j \}) \\ = \mathbf {P} (\{S _ {k} = r, n \leqslant T _ {k + 1} \} \cap G _ {n}) q _ {+} ^ {a} (i _ {n}, j). \\ \end{array}
$$

对 $0 \leqslant r \leqslant n$ 求和有

$$
\begin{array}{l} \mathbf {P} (\{S _ {k} \leqslant n \leqslant T _ {k + 1} \} \cap G _ {n} \cap \{W _ {n + 1} = j \}) \\ = \mathbf {P} (\{S _ {k} \leqslant n \leqslant T _ {k + 1} \} \cap G _ {n}) q _ {+} ^ {a} (i _ {n}, j), \\ \end{array}
$$

再对 $k \geqslant 1$ 求和得

$$
\mathbf {P} (G _ {n} \cap \{W _ {n + 1} = j \}) = \mathbf {P} (G _ {n}) q _ {+} ^ {a} (i _ {n}, j),
$$

故有

$$
\mathbf {P} (W _ {n + 1} = j | G _ {n}) = q _ {+} ^ {a} (i _ {n}, j).
$$

所以 $W$ 是 $\mathbb{Z}_{a+}$ 上的反射简单随机游动. $\square$

在定理 4.4.2 中, 当 p > 1/2 时对  $k \geqslant 2$  可能以严格正的概率有  $S_{k} = \infty$ . 当  $p \leqslant 1/2$  时, 对一切  $k \geqslant 1$  有  $S_{k} < \infty$ . 显然, 当  $S_{k} < \infty$  时  $e_{k}$  就是 W 的第 k 个从  $a + 1$  到 a 的游程. 也就是说, 将可数个相互独立的从  $a + 1$  到 a 的游程首尾相接, 就得到一个  $Z_{a+}$  上的从  $a + 1$  出发的反射简单随机游动. 基于定理 4.4.2, 可以容易地构造出  $Z_{a+}$  上的从任何状态出发的反射游动. 对此我们有:

推论 4.4.3 设  $\phi_{0}=\{\phi_{0}(n):n\geqslant0\}$  是从  $\phi_{0}(0)\geqslant a+1$  出发在  $a+1$  被吸收的简单游动且与 (4.4.8) 式定义的游动  $W=(W_{n}:n\geqslant0)$  独立. 对  $k\geqslant1$  令  $\sigma_{k}=\zeta_{0}+S_{k}$ ，其中  $\zeta_{0}=\inf\{n\geqslant0:\phi_{0}(n)=a+1\}$ . 再令

$$
X _ {n} = \left\{ \begin{array}{l l} \phi_ {0} (n), & 0 \leqslant n <   \zeta_ {0}, \\ W _ {n - \sigma_ {k}}, & \sigma_ {k} \leqslant n <   \sigma_ {k + 1}, \end{array} \right.
$$

则  $X=(X_{n}:n\geqslant0)$  是  $Z_{a+}$  上的反射简单随机游动.

与定理 4.4.2 和推论 4.4.3 类似, 可以构造出  $Z_{a-}$  上的反射简单随机游动.

## 4.4.3 常返游动的拆解

取定 $a \in \mathbb{Z}$. 设 $W = \{W(n) : n \geqslant 0\}$ 为 $\mathbb{Z}$ 上的对称简单随机游动且满足 $W(0) \geqslant a$. 考虑非负不降过程 $H^{+} = \{H_{n}^{+} : n \geqslant 0\}$ 和 $H^{+} = \{H_{n}^{-} : n \geqslant 0\}$, 其中

$$
H _ {n} ^ {+} = \sum_ {k = 0} ^ {n} 1 _ {\{W (k) \geqslant a \}}, H _ {n} ^ {-} = \sum_ {k = 0} ^ {n} 1 _ {\{W (k) \leqslant a + 1 \}}. \tag {4.4.9}
$$

由于 $W$ 不可约且常返, 当 $n \to \infty$ 时有 $H_{n}^{+} \to \infty$ 和 $H_{n}^{-} \to \infty$. 对于 $k \geqslant 0$ 令

$$
\eta_ {k} ^ {+} = \inf \{n \geqslant 0: H _ {n} ^ {+} > k \}, \eta_ {k} ^ {-} = \inf \{n \geqslant 0: H _ {n} ^ {-} > k \}, \tag {4.4.10}
$$

则 $\eta^{+} = (\eta_{k}^{+}:k\geqslant 0)$ 和 $\eta^{-} = (\eta_{k}^{-}:k\geqslant 0)$ 也是非负不降过程. 下面的定理从 $W$ 中拆解出了两个独立的反射游动.

定理 4.4.4 过程  $W^{+}=\{W(\eta_{k}^{+}):k\geqslant0\}$  和  $W^{-}=\{W(\eta_{k}^{-}):k\geqslant0\}$  分别是  $Z_{a+}=Z\cap[a,\infty)$  上和  $\mathbb{Z}_{(a+1)-}=\mathbb{Z}\cap(-\infty,a+1]$  上的反射简单游动且二者相互独立.

证明 对于过程 $X = W$ 和水平 $a, b = a + 1$ 可以像 (4.4.1) 式中那样定义停时 $\sigma_k$, $\tau_k, k \geqslant 0$, 并像 (4.4.2) 式中那样定义游程 $e_k, \varepsilon_k, k \geqslant 0$. 再令 $\phi_0 = \{W(n \wedge \sigma_1): n \geqslant 0\}$. 注意 $W^+$ 是将 $\phi_0, e_k, k \geqslant 0$ 首尾相接得到的过程, 而 $W^-$ 是将 $\varepsilon_k, k \geqslant 0$ 首尾相接得到的过程. 应用推论 4.4.3 易知 $W^+$ 是 $\mathbb{Z}_{a+}$ 上的反射简单游动, 同理 $W^-$ 是 $\mathbb{Z}_{(a+1)-}$ 上的反射简单游动. 再由定理 4.4.1 知 $\phi_0, e_k, k \geqslant 0$ 与 $\varepsilon_k, k \geqslant 0$ 独立. 所以 $W^+$ 和 $W^-$ 独立. $\square$

对于非对称的简单游动, 也可以给出类似于定理 4.4.4 的拆解. 为了保证常返性, 下面考虑反射游动. 任取 $c < a \in \mathbb{Z}$. 设 $W = \{W(n): n \geqslant 0\}$ 为 $\mathbb{Z}_{c+} = \mathbb{Z} \cap [c, \infty)$ 上的反射简单随机游动, 其转移矩阵由 (4.4.4) 式给出, 其中 $a = c$ 而 $0 < p \leqslant q < 1$. 此时, 仍可像 (4.4.9) 式和 (4.4.10) 式那样定义 $H^{\pm}$ 和 $\eta^{\pm}$. 与前面的证明类似地, 可以得到下面的:

定理 4.4.5 在上述情况下, 过程  $W^{+} = \{W(\eta_{k}^{+}) : k \geqslant 0\}$  和  $W^{-} = \{W(\eta_{k}^{-}) : k \geqslant 0\}$  分别是  $Z_{a+} = Z \cap [a, \infty)$  上和  $Z_{c,a+1} = Z \cap [c, a+1]$  上的反射简单游动且二者相互独立.

## 练习题

1. 证明由 (4.4.1) 式定义的每个 $\sigma_{k}$ 和 $\tau_{k}$ 是 $(\mathcal{F}_n)$ 的停时.

提示: 令 $(\mathcal{F}_n)$ 是 $X$ 的自然流. 注意, 对于 $k \geqslant 1$ 和 $n \geqslant 0$, 有 $\sigma_k \leqslant n$ 当且仅当存在 $0 \leqslant i_1 < j_1 \leqslant i_2 < j_2 < \cdots \leqslant i_{k-1} < j_{k-1} \leqslant i_k \leqslant n$, 使得

$$
X _ {i _ {1}} = X _ {i _ {2}} = \dots = X _ {i _ {k - 1}} = X _ {i _ {k}} = b, X _ {j _ {1}} = X _ {j _ {2}} = \dots = X _ {j _ {k - 1}} = a.
$$

所以 $\{\sigma_k\leqslant n\} \in \mathcal{F}_n$ .类似地有 $\{\tau_k\leqslant n\} \in \mathcal{F}_n$

2. 求从 1 出发的一维简单随机游动的第一个由 1 到 0 的游程 $e = \{e(n) : n \geqslant 0\}$ 的高度 $\sup_{n \geqslant 0} e(n)$ 的分布.

3. 证明: 当 $0 < p \leqslant q$ 时具有转移矩阵 $Q_{+}^{a}$ 的反射随机游动是常返的; 当 $p \geqslant q > 0$ 时具有转移矩阵 $Q_{-}^{a}$ 的反射随机游动是常返的.

4. 给出推论 4.4.3 的直接证明.

提示: 参考定理 4.4.2 的证明.

5. 给出 $\mathbb{Z}_{+} \times \mathbb{Z}$ 上的以 $\{0\} \times \mathbb{Z}$ 为反射面的简单对称随机游动的定义, 并给出该游动的构造.

提示: 利用定理 4.4.2 和推论 4.4.3 的结论.

本章讨论马氏链的遍历理论, 包括平稳链、不变测度、弱遍历定理、遍历定理和转移矩阵的遍历性. 在形式上, 马氏链的遍历定理通常是指它的转移概率或轨道按时间平均的极限定理, 前者称为弱遍历定理, 后者称为强遍历定理.

## 5.1 可逆性与对称性

马氏链的不变测度就是在它的转移矩阵作用下保持不变的测度. 以不变概率测度为初始分布的马氏链是一个平稳过程, 即其有限维分布具有时间上的推移不变性. 可逆性是指过程的分布性质在时间逆转下的不变性, 即将时间反转后过程的有限维分布保持不变. 对称性是可逆性的推广. 可逆过程和对称过程具有许多特殊性质, 非常便于处理.

## 5.1.1 平稳链和可逆链

考虑定义于概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的具有可数状态空间 $E$ 和转移矩阵 $P = (p_{ij}: i, j \in E)$ 的马氏链 $X = (X_n : n \geqslant 0)$.

定义 5.1.1 称 E 上的概率测度  $\pi = (\pi_{i} : i \in E)$  为 X 或 P 的平稳分布, 是指

$$
\sum_ {i \in E} \pi_ {i} p _ {i j} = \pi_ {j}, \quad j \in E. \tag {5.1.1}
$$

称  $\pi$  为 X 或 P 的可逆分布, 是指

$$
\pi_ {i} p _ {i j} = \pi_ {j} p _ {j i}, \quad i, j \in E. \tag {5.1.2}
$$

显然, 若  $\pi$  是 X 的可逆分布, 则它一定是 X 的平稳分布.

定义 5.1.2 称马氏链 X 为平稳的, 是指  $X_{n}$  的概率分布不依赖于时间  $n \geqslant 0$ . 根据 X 的马氏性, 这意味着对任意的  $n \geqslant 0$  和  $k \geqslant 0$  下面的随机向量具有相同的概率分布:

$$
(X _ {0}, X _ {1}, \dots , X _ {k}), \quad (X _ {n}, X _ {n + 1}, \dots , X _ {n + k}).
$$

命题 5.1.1 以  $\pi = (\pi_{i} : i \in E)$  为初始分布且有转移矩阵 P 的马氏链 X 是平稳的当且仅当  $\pi$  是 P 的平稳分布.

证明 设 $X$ 是以 $\pi$ 为初始分布的马氏链. 根据马氏性有

$$
\mathbf {P} (X _ {1} = j) = \sum_ {i \in E} \mathbf {P} (X _ {0} = i) \mathbf {P} (X _ {1} = j | X _ {0} = i) = \sum_ {i \in E} \pi_ {i} p _ {i j},
$$

所以 $X_{1}$ 服从分布 $\pi$ 当且仅当 (5.1.1) 式成立.利用马氏性和数学归纳法可得命题结论.$\square$

定义 5.1.3 称马氏链 X 是可逆的, 是指对任何  $n \geqslant 0$  下面的随机向量具有相同的概率分布:

$$
(X _ {0}, X _ {1}, \dots , X _ {n - 1}, X _ {n}), \quad (X _ {n}, X _ {n - 1}, \dots , X _ {1}, X _ {0}),
$$

命题 5.1.2 以  $\pi = (\pi_{i} : i \in E)$  为初始分布且有转移矩阵 P 的马氏链 X 是可逆的当且仅当  $\pi$  是 P 的可逆分布.

证明 如果 $X$ 可逆, 那么对任意的 $i, j \in E$ 我们有

$$
\pi_ {i} p _ {i j} = \mathbf {P} (X _ {0} = i, X _ {1} = j) = \mathbf {P} (X _ {1} = i, X _ {0} = j) = \pi_ {j} p _ {j i},
$$

即 (5.1.2) 式成立. 反之, 假设 (5.1.2) 式成立. 则对  $n \geqslant 0$  和  $\{i_{0}, i_{1}, \cdots, i_{n}\} \subseteq E$  有

$$
\begin{array}{l} \mathbf {P} (X _ {0} = i _ {0}, X _ {1} = i _ {1}, \dots , X _ {n - 1} = i _ {n - 1}, X _ {n} = i _ {n}) \\ = \pi_ {i _ {0}} p _ {i _ {0} i _ {1}} p _ {i _ {1} i _ {2}} \dots p _ {i _ {n - 2} i _ {n - 1}} p _ {i _ {n - 1} i _ {n}} \\ = p _ {i _ {1} i _ {0}} \pi_ {i _ {1}} p _ {i _ {1} i _ {2}} \dots p _ {i _ {n - 2} i _ {n - 1}} p _ {i _ {n - 1} i _ {n}} \\ = p _ {i _ {1} i _ {0}} p _ {i _ {2} i _ {1}} \pi_ {i _ {2}} \dots p _ {i _ {n - 2} i _ {n - 1}} p _ {i _ {n - 1} i _ {n}} \\ = \dots \\ = p _ {i _ {1} i _ {0}} p _ {i _ {2} i _ {1}} \dots p _ {i _ {n - 1} i _ {n - 2}} p _ {i _ {n} i _ {n - 1}} \pi_ {i _ {n}} \\ = \pi_ {i _ {n}} p _ {i _ {n} i _ {n - 1}} p _ {i _ {n - 1} i _ {n - 2}} \dots p _ {i _ {2} i _ {1}} p _ {i _ {1} i _ {0}} \\ = \mathbf {P} (X _ {0} = i _ {n}, X _ {1} = i _ {n - 1}, \dots , X _ {n - 1} = i _ {1}, X _ {n} = i _ {0}). \\ \end{array}
$$

这说明 $X$ 是可逆的. $\square$

可逆马氏链必然是平稳的. 物理学中称满足 (5.1.2) 式的过程 $(X_{n}: n \geqslant 0)$ 是细致平衡的, 意为对任意一对状态 $\{i, j\} \subseteq E$, 过程从 $i$ 运动到 $j$ 的概率与从 $j$ 运动到 $i$ 的概率相同. 此时, 对给定的 $n \geqslant 1$ 令 $Y_{k} = X_{n-k}$, 则 $(Y_{k}: 0 \leqslant k \leqslant n)$ 也是以 $P$ 为转移矩阵的平稳马氏链.

定义 5.1.4 对 $n \geqslant 1$ 写 $P^n = (p_{ij}^n : i, j \in E)$. 称 $P$ 是遍历的, 是指存在 $E$ 上的概率分布 $\pi = (\pi_i : i \in E)$ 使得

$$
\lim _ {n \to \infty} p _ {i j} ^ {n} = \pi_ {j}, \quad i, j \in E. \tag {5.1.3}
$$

命题 5.1.3 若 P 是遍历转移矩阵且  $\pi$  由 (5.1.3) 式确给出, 则  $\pi$  是 P 的唯一的平稳分布.

证明 根据 (5.1.3) 式和法图定理有

$$
\pi_ {j} = \lim _ {n \to \infty} p _ {i j} ^ {n} = \lim _ {n \to \infty} \sum_ {k \in E} p _ {i k} ^ {n - 1} p _ {k j} \geqslant \sum_ {k \in E} \pi_ {k} p _ {k j}.
$$

将上式对 $j \in E$ 求和, 易见两端均为 1 , 故这里只能成立等号. 所以 $\pi$ 是 $P$ 的平稳分布. 假设 $\mu = (\mu_i : i \in E)$ 也是 $P$ 的平稳分布. 根据控制收敛定理有

$$
\mu_ {j} = \lim _ {n \to \infty} \sum_ {k \in E} \mu_ {k} p _ {k j} ^ {n} = \sum_ {k \in E} \mu_ {k} \pi_ {j} = \pi_ {j}.
$$

这说明 $\pi$ 是 $P$ 的唯一的平稳分布. $\square$

## 5.1.2 对称测度

作为平稳分布和可逆分布的推广, 我们引入不变测度和对称测度的概念如下:

定义 5.1.5 称 E 上的  $\sigma$  有限测度  $\mu = (\mu_{i} : i \in E)$  是 X 或 P 的不变测度, 是指

$$
\sum_ {i \in E} \mu_ {i} p _ {i j} = \mu_ {j}, \quad j \in E. \tag {5.1.4}
$$

称  $\mu$  是 X 或 P 的对称测度, 是指

$$
\mu_ {i} p _ {i j} = \mu_ {j} p _ {j i}, \quad i, j \in E. \tag {5.1.5}
$$

命题 5.1.4 转移矩阵 P 关于测度  $\mu$  是对称的当且仅当有

$$
\mu_ {i} p _ {i j} (n) = \mu_ {j} p _ {j i} (n), \quad n \geqslant 0, i, j \in E. \tag {5.1.6}
$$

证明 若 (5.1.6) 式成立, 显然 $P$ 关于测度 $\mu$ 对称. 反之, 若 $P$ 关于 $\mu$ 是对称的, 则 (5.1.6) 式对于 $n = 1$ 成立. 假若 (5.1.6) 式对于某个 $n \geqslant 1$ 成立, 则有

$$
\begin{array}{l} \mu_ {i} p _ {i j} (n + 1) = \sum_ {k \in E} \mu_ {i} p _ {i k} (n) p _ {k j} = \sum_ {k \in E} p _ {k i} (n) \mu_ {k} p _ {k j} \\ = \sum_ {k \in E} p _ {k i} (n) p _ {j k} \mu_ {j} = \mu_ {j} p _ {j i} (n + 1). \\ \end{array}
$$

由数学归纳法知 (5.1.6) 式对于所有 $n \geqslant 1$ 成立. $\square$

例 5.1.1 对于每个  $i \in Z$  取常数  $p_{i}, q_{i} > 0$  满足  $p_{i} + q_{i} = 1$ . 定义 Z 上的转移矩阵  $P = (p_{ij} : i, j \in \mathbb{Z})$  如下:

$$
p _ {i j} = p _ {i} 1 _ {\{j = i + 1 \}} + q _ {i} 1 _ {\{j = i - 1 \}}, \quad i, j \in \mathbb {Z}.
$$

以 $P$ 为转移矩阵的马氏链也称为生灭过程. 令

$$
\mu_ {0} = 1, \quad \mu_ {i} = \prod_ {k = 0} ^ {i - 1} \frac {p _ {k}}{q _ {k + 1}} (i > 0), \quad \mu_ {i} = \prod_ {k = i + 1} ^ {0} \frac {q _ {k}}{p _ {k - 1}} (i <   0),
$$

则当 $|i - j| \geqslant 2$ 时有 $\mu_i p_{ij} = \mu_j p_{ji} = 0$. 当 $|i - j| = 1$ 时, 利用上式易证 $\mu_i p_{ij} = \mu_j p_{ji}$. 所以 $\mu$ 是 $P$ 的对称测度.

例5.1.2 设有 $m(\geqslant 1)$ 个粒子被放置到一个容器中, 容器被挡板分为左右两侧. 每过一个时间单位从 $m$ 个粒子中等概率地随机选择一个, 将它移到容器的另外一侧. 用 $X_{n}$ 表示第 $n$ 次操作完成后容器左侧粒子的个数, 则 $X = (X_{n}: n \geqslant 0)$ 是整数区间 $E := [0, m]$ 上的马氏链, 其转移矩阵 $P = (p_{ij}: 0 \leqslant i, j \leqslant m)$ 可表示为

$$
p _ {i j} = \Big (\frac {i}{m} \Big) 1 _ {\{j = i - 1 \}} + \Big (1 - \frac {i}{m} \Big) 1 _ {\{j = i + 1 \}}.
$$

易证 $X$ 不可约, 以2为周期且有平稳分布 $\pi = (\pi_i:0\leqslant i\leqslant m)$, 其中 $\pi_j = 2^{-m}\mathrm{C}_m^i$. 此外, 对任何 $1\leqslant i\leqslant m$ 有 $\pi_{i}p_{i,i - 1} = \pi_{i - 1}p_{i - 1,i}$. 由命题5.1.2知 $\pi$ 是 $X$ 的可逆分布. 该马氏链称为埃伦菲斯特(Ehrenfest)模型, 是为研究气体分子的扩散行为而设计的简化模型.

## 5.1.3 对称测度的判别法

马氏链的对称测度一定是不变测度, 且比不变测度更容易处理. 事实上, 对称测度总可以用转移矩阵的元素给出显式表示, 而不变测度通常很难做到这点. 下面的定理属于柯尔莫哥洛夫, 它提供了一个非常有用的对称性判别法, 同时给出了对称测度的表示.

定理 5.1.5 不可约转移矩阵  $P = (p_{ij} : i, j \in E)$  有非零的对称测度当且仅当对状态空间中任意的环路  $i_{1} \rightarrow i_{2} \rightarrow \cdots \rightarrow i_{r} \rightarrow i_{1}$  有等式

$$
p _ {i _ {1} i _ {2}} p _ {i _ {2} i _ {3}} \dots p _ {i _ {r - 1} i _ {r}} p _ {i _ {r} i _ {1}} = p _ {i _ {1} i _ {r}} p _ {i _ {r} i _ {r - 1}} \dots p _ {i _ {3} i _ {2}} p _ {i _ {2} i _ {1}}. \tag {5.1.7}
$$

此时, 可以定义非零对称测度  $\mu = (\mu_{i} : i \in E)$  如下: 取状态  $i_{0} \in E$  并令  $\mu_{i_{0}} = 1$ ; 对于  $i \neq i_{0} \in E$  取  $\{i_{1}, i_{2}, \cdots, i_{n}\} \subseteq E$  满足  $p_{i_{0}i_{1}} p_{i_{1}i_{2}} \cdots p_{i_{n-1}i_{n}} p_{i_{n}i} > 0$ , 再令

$$
\mu_ {i} = \frac {p _ {i _ {0} i _ {1}} p _ {i _ {1} i _ {2}} \cdots p _ {i _ {n - 1} i _ {n}} p _ {i _ {n} i}}{p _ {i i _ {n}} p _ {i _ {n} i _ {n - 1}} \cdots p _ {i _ {2} i _ {1}} p _ {i _ {1} i _ {0}}} = \prod_ {k = 0} ^ {n} \frac {p _ {i _ {k} i _ {k + 1}}}{p _ {i _ {k + 1} i _ {k}}}, \tag {5.1.8}
$$

其中  $i_{n+1}=i$ . 上式右边的值与  $\{i_{1},i_{2},\cdots,i_{n}\}$  的选择无关, 且分子和分母均严格正.

证明 假设 $\mu$ 是 $P$ 的非零的对称测度. 由命题5.1.4, 对 $n \geqslant 0$ 和 $i, j \in E$ 有 $\mu_{i} p_{ij}(n) = \mu_{j} p_{ji}(n)$. 因 $P$ 是不可约的, 若 $\mu_{i_0} > 0$, 对 $i_0 \neq j \in E$ 可取 $n \geqslant 1$ 使得 $p_{i_0j}(n) > 0$, 从而 $\mu_{j} p_{ji_0}(n) = \mu_{i_0} p_{i_0j}(n) > 0$. 由此可见 $\mu_j > 0$ 对所有 $j \in E$ 成立. 对任意的环路 $i_1 \to i_2 \to \dots \to i_r \to i_1$ 有

$$
\begin{array}{l} \mu_ {i _ {1}} p _ {i _ {1} i _ {2}} p _ {i _ {2} i _ {3}} \dots p _ {i _ {r - 1} i _ {r}} p _ {i _ {r} i _ {1}} = p _ {i _ {2} i _ {1}} \mu_ {i _ {2}} p _ {i _ {2} i _ {3}} \dots p _ {i _ {r - 1} i _ {r}} p _ i _ {r} i _ {1} \\ = \dots = p _ {i _ {2} i _ {1}} p _ {i _ {3} i _ {2}} \dots p _ {i _ {r} i _ {r - 1}} p _ {i _ {1} i _ {r}} \mu_ i _ {1} \\ = \mu_ {i _ {1}} p _ {i _ {1} i _ {r}} p _ {i _ {r} i _ {r - 1}} \dots p _ {i _ {3} i _ {2}} p _ {i _ {2} i _ {1}}. \\ \end{array}
$$

由于  $\mu_{i_{1}}>0$ ，上式等价于 (5.1.7) 式。反之，假设 (5.1.7) 式对所有环路成立。我们证明 (5.1.8) 式定义了非零对称测度  $\mu$ 。先证该式中分子和分母均不为零。取  $\{l_{1}, l_{2}, \cdots, l_{r}\} \subseteq$