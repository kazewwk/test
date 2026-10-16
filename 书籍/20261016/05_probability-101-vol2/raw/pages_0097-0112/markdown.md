$j_{3},\cdots,X_{n+k+1}=j_{k+1}\}$ . 根据归纳假设, 有

$$
\mathbf {P} (H | G \cap \{X _ {n} = i \} \cap \{X _ {n + 1} = j _ {1} \}) = \mathbf {P} (H | \{X _ {n} = i \} \cap \{X _ {n + 1} = j _ {1} \}).
$$

事实上, 此式两端都等于  $\mathbf{P}(H|X_{n+1}=j_{1})$ . 根据乘法公式, 并利用 (4.1.3) 式和上式得

$$
\begin{array}{l} \mathbf {P} (\{X _ {n + 1} = j _ {1} \} \cap H | G \cap \{X _ {n} = i \}) \\ = \mathbf {P} (X _ {n + 1} = j _ {1} | G \cap \{X _ {n} = i \}) \mathbf {P} (H | G \cap \{X _ {n} = i \} \cap \{X _ {n + 1} = j _ {1} \}) \\ = \mathbf {P} (X _ {n + 1} = j _ {1} | X _ {n} = i) \mathbf {P} (H | \{X _ {n} = i \} \cap \{X _ {n + 1} = j _ {1} \}) \\ = \mathbf {P} (\{X _ {n + 1} = j _ {1} \} \cap H | X _ {n} = i), \\ \end{array}
$$

即把 $k$ 换作 $k + 1$ 后 (4.1.8) 式仍然成立. 根据数学归纳法, 这就证明了 (4.1.8) 式对任意的 $n \geqslant 0$ 和 $k \geqslant 1$ 成立. $\square$

定理 4.1.5 记  $\mathcal{F}^{n} = \sigma(X_{n}, X_{n+1}, \cdots)$ ，则过程 X 关于流  $(\mathcal{G}_{n})$  具有马氏性 (4.1.3) 的充要条件是对于任意的  $n \geqslant 0, k \geqslant 1, i \in E, G \in G_{n}$  和  $F \in F^{n}$  有

$$
\mathbf {P} (F | G \cap \{X _ {n} = i \}) = \mathbf {P} (F | X _ {n} = i). \tag {4.1.9}
$$

证明 若 (4.1.9) 式成立, 取 $F = \{X_{n+1} = j\}$ 即知 (4.1.3) 式成立. 反之, 假设 $X$ 具有马氏性 (4.1.3). 令 $\mathcal{M}$ 是使 (4.1.9) 式成立的所有事件 $F \in \mathscr{F}^n$ 构成的集类. 显然 $\mathcal{M}$ 是一个单调类. 由定理 4.1.4 知 $X$ 满足性质 (4.1.8). 对整数 $k \geqslant 0$, 记 $\mathscr{F}_k^n = \sigma(X_n, X_{n+1}, \cdots, X_{n+k})$. 则对于形如 $F = \{X_n = j_0, X_{n+1} = j_1, \cdots, X_{n+k} = j_k\} \in \mathscr{F}_k^n$ 的事件, 当 $j_0 \neq i$ 时 (4.1.9) 式两端皆为零, 故该式成立; 而当 $j_0 = i$ 时由 (4.1.8) 式知 (4.1.9) 式成立. 对一般的 $F \in \mathscr{F}_k^n$, 存在 $A \subseteq E^{n+1}$ 使得 $F = \{(X_n, X_{n+1}, \cdots, X_{n+k}) \in A\}$. 利用条件概率的可数可加性有

$$
\begin{array}{l} \mathbf {P} (F | G \cap \{X _ {n} = i \}) \\ = \sum_ {(j _ {0}, j _ {1}, \dots , j _ {k}) \in A} \mathbf {P} (X _ {n} = j _ {0}, X _ {n + 1} = j _ {1}, \dots , X _ {n + k} = j _ {k} | G \cap \{X _ {n} = i \}) \\ = \sum_ {(j _ {0}, j _ {1}, \dots , j _ {k}) \in A} \mathbf {P} (X _ {n} = j _ {0}, X _ {n + 1} = j _ {1}, \dots , X _ {n + k} = j _ {k} | X _ {n} = i) \\ = \mathbf {P} (F | X _ {n} = i). \\ \end{array}
$$

所以 (4.1.9) 式对任意的 $F \in \mathcal{F}_k^n$ 成立, 即有 $\mathcal{M} \supseteq \bigcup_k \mathcal{F}_k^n$. 注意 $\bigcup_k \mathcal{F}_k^n$ 是集代数. 根据单调类定理有 $\mathcal{M} \supseteq m\left(\bigcup_k \mathcal{F}_k^n\right) = \sigma\left(\bigcup_k \mathcal{F}_k^n\right) = \mathcal{F}^n$, 即 (4.1.9) 式对一切 $F \in \mathcal{F}^n$ 成立. □

定理 4.1.6 过程 X 满足关于流  $(\mathcal{G}_{n})$  的马氏性 (4.1.3) 的充要条件是对任意的  $n \geqslant 0, k \geqslant 1, i \in E, G \in \mathcal{G}_{n}$  和  $F \in F^{n}$  有

$$
\mathbf {P} (G \cap F | X _ {n} = i) = \mathbf {P} (G | X _ {n} = i) \mathbf {P} (F | X _ {n} = i). \tag {4.1.10}
$$

证明 假设 $X$ 满足关于流 $(\mathcal{G}_n)$ 的马氏性 (4.1.3). 根据定理 4.1.5 它满足 (4.1.9) 式, 因而由乘法公式得

$$
\begin{array}{l} \mathbf {P} (G \cap F | X _ {n} = i) = \mathbf {P} (G | X _ {n} = i) \mathbf {P} (F | G \cap \{X _ {n} = i \}) \\ = \mathbf {P} (G | X _ {n} = i) \mathbf {P} (F | X _ {n} = i), \\ \end{array}
$$

即 (4.1.10) 式成立. 反之, 假设 (4.1.10) 式成立. 在该式中用 $G \cap \{X_{n} = i\}$ 替代 $G$ 得

$$
\mathbf {P} (G \cap \{X _ {n} = i \} \cap F | X _ {n} = i) = \mathbf {P} (G \cap \{X _ {n} = i \} | X _ {n} = i) \mathbf {P} (F | X _ {n} = i).
$$

将上式两端同乘以  $\mathbf{P}(X_{n}=i)$  得

$$
\mathbf {P} (G \cap \{X _ {n} = i \} \cap F) = \mathbf {P} (G \cap \{X _ {n} = i \}) \mathbf {P} (F | X _ {n} = i).
$$

两端同除以 $\mathbf{P}(G\cap \{X_n = i\})$ 即得(4.1.9)式.根据定理4.1.5知马氏性(4.1.3)成立.□

推论 4.1.7 过程 X 相对其自然流具有马氏性的充要条件是对于任意的  $n \geqslant 0$  和  $i \in E$ ，在条件概率  $\mathbf{P}(\cdot | X_n = i)$  之下  $\{X_0, X_1, \cdots, X_n\}$  和  $\{X_n, X_{n+1}, \cdots\}$  独立.

定理 4.1.6 和推论 4.1.7 说明, 过程 X 的马氏性 (4.1.6) 等价于给定当前的状态  $X_{n}$  其过去和将来的运动情况是彼此独立的.

## 练习题

1. 设概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 上的事件 $C \in \mathcal{F}$ 满足 $\mathbf{P}(C) > 0$. 定义 $\mathcal{F}$ 上的条件概率 $\mathbf{P}_C = \mathbf{P}(\cdot | C)$. 证明: 若 $A, B \in \mathcal{F}$ 且 $\mathbf{P}(B \cap C) > 0$, 则 $\mathbf{P}_C(A|B) = \mathbf{P}(A|B \cap C)$.
2. 设 $(X_{n}: n \geqslant 0)$ 是一维对称简单随机游动, 即有 $\mathbf{P}(X_{n} - X_{n-1} = \pm 1) = 1/2$. 证明 $(|X_{n}|: n \geqslant 0)$ 是以 $\mathbb{Z}_{+}$为状态空间的马氏链.
3. 设 $(X_{n}: n \geqslant 0)$ 是以 $E$ 为状态空间的马氏链, 而 $\phi: E \to F$ 是单射. 证明 $\{\phi(X_{n}): n \geqslant 0\}$ 是以 $\phi(E) := \{\phi(x): x \in E\} \subseteq F$ 为状态空间的马氏链.
4. 设 $(X_{n}: n \geqslant 0)$ 和 $(Y_{n}: n \geqslant 0)$ 分别是状态空间 $E$ 和 $F$ 上的马氏链, 且它们相互独立. 证明 $\{(X_{n}, Y_{n}): n \geqslant 0\}$ 是 $E \times F$ 上的马氏链.
5. 在上题的条件下, 证明 $(X_{n}: n \geqslant 0)$ 是关于 $\{(X_{n}, Y_{n}): n \geqslant 0\}$ 的自然流的马氏链.
6. 令 $\mu_0 = \{\mu_0(j): j \geqslant 0\}$ 为 $\mathbb{Z}_+$ 上的概率分布. 对于 $n \geqslant 1$ 递推地定义

$$
\mu_ {n} (0) = \mu_ {n - 1} ^ {* 2} (0) + \mu_ {n - 1} ^ {* 2} (1), \mu_ {n} (j) = \mu_ {n - 1} ^ {* 2} (j + 1), \quad j \geqslant 1,
$$

其中 $\mu_{n - 1}^{*2}$ 表示 $\mu_{n - 1}$ 的二重卷积. 用 $F_{n - 1}$ 表示 $\mu_{n - 1}$ 的分布函数, 再记

$$
F _ {n - 1} ^ {- 1} (y) = \inf \{x \geqslant 0: y \leqslant F _ {n - 1} (x) \}, \quad 0 \leqslant y \leqslant 1.
$$

序列 $(\mu_{n}:n\geqslant 0)$ 称为德里达-勒托(Derrida-Retaux)模型.设 $X_0$ 是取值于 $\mathbb{Z}_{+}$ 的随机变量且有分布 $\mu_0$ ，而 $\{U_n:n\geqslant 1\}$ 是与之独立的独立同分布随机变量且服从(0,1)上的均匀分布.对于 $n\geqslant 1$ 递推地定义

$$
X _ {n} = 0 \vee [ X _ {n - 1} + F _ {n - 1} ^ {- 1} (U _ {n}) - 1 ].
$$

证明 $(X_{n}:n\geqslant0)$ 是以 $Z_{+}$ 为状态空间的马氏链,且 $X_{n}$ 服从分布 $\mu_{n}$.

## 4.2 转移矩阵

利用转移矩阵可以定义一种马氏链, 它的马氏性比前面讨论的简单马氏性略强. 本节中我们讨论由转移矩阵定义的马氏性、强马氏性以及它们的若干基本性质.

## 4.2.1 有转移矩阵的马氏链

定义 4.2.1 称 E 上的矩阵  $P = (p(i, j) : i, j \in E)$  为一个转移矩阵, 是指它有下面的性质:

(1) 对任何  $i, j \in E$ ，有  $p(i, j) \geqslant 0;$
(2) 对任何 $i \in E$, 有 $\sum_{j \in E} p(i, j) = 1$.

给定一个转移矩阵 $P$, 令 $P^0 = I$. 利用矩阵乘积, 对 $n \geqslant 1$ 可以归纳地定义 $P^n = PP^{n-1}$. 不难证明 $P^n := (p_n(i,j): i, j \in E)$ 也是一个转移矩阵. 为了书写方便, 后面可能将 $p(i,j)$ 和 $p_n(i,j)$ 分别写为 $p_{ij}$ 和 $p_{ij}(n)$.

定义 4.2.2 设 P 是可数状态空间 E 上的转移矩阵. 称 E 上的过程  $X = (X_{n} : n \geqslant 0)$  是关于其适应流  $(\mathcal{G}_{n})$  有转移矩阵 P 的马氏链, 是指对任意的  $n \geqslant 0, i, j \in E$  和  $G \in G_{n}$  有

$$
\mathbf {P} (X _ {n + 1} = j | G \cap \{X _ {n} = i \}) = p (i, j). \tag {4.2.1}
$$

等式 (4.2.1) 表达的性质称为有转移矩阵 $P$ 的马氏性.

如果 $X$ 满足以 $P$ 为转移矩阵的马氏性 (4.2.1), 显然它满足马氏性 (4.1.3). 所以由转移矩阵定义的马氏性 (4.2.1) 比普通马氏性 (4.1.3) 要强.

在定义 4.2.2 的情况下, 令  $\mu(i)=\mathbf{P}(X_{0}=i)$ , 称  $\mu=(\mu(i):i\in E)$  为 X 的初始分布. 特别地, 若  $\mathbf{P}(X_{0}=i)=1$ , 则称 X 是从 i 出发的. 如果 (4.2.1) 式对于 X 的自然流  $(\mathcal{F}_{n})$  成立, 就简单地称 X 为以 P 为转移矩阵的马氏链.

与定理 4.1.1 和定理 4.1.2 的证明类似, 我们可以得到如下的:

定理 4.2.1 过程 X 关于流  $(\mathcal{G}_{n})$  是以 P 为转移矩阵的马氏链的充要条件是对任意的  $n \geqslant 0$  和  $j \in E$  有

$$
\mathbf {P} (X _ {n + 1} = j | \mathcal {G} _ {n}) = p (X _ {n}, j). \tag {4.2.2}
$$

定理 4.2.2 过程 X 相对其自然流是以 P 为转移矩阵的马氏链的充要条件是对于任意的  $n \geqslant 0$  和  $\{i_{0}, i_{1}, \cdots, i_{n} = i, j\} \subseteq E$  有

$$
\mathbf {P} (X _ {n + 1} = j | X _ {k} = i _ {k}: 0 \leqslant k \leqslant n) = p (i, j). \tag {4.2.3}
$$

例 4.2.1 设  $\{\xi_{n}: n \geqslant 1\}$  为取值于  $Z^{d}$  的独立同分布随机变量. 令  $(X_{n}: n \geqslant 0)$  是由 (4.1.7) 式定义的 d 维随机游动. 记  $p_{k} = \mathbf{P}(\xi_{n} = k), k \in \mathbb{Z}^{d}$ , 则对任意的  $n \geqslant 0$  以及  $\{i_{0}, i_{1}, \cdots, i_{n} = i, j\} \subseteq Z^{d}$  有

$$
\mathbf {P} (X _ {n + 1} = j | X _ {k} = i _ {k}: 0 \leqslant k \leqslant n) = \mathbf {P} (\xi_ {n + 1} = j - i) = p _ {j - i}.
$$

所以 $(X_{n}:n\geqslant 0)$ 是以 $\mathbb{Z}^d$ 为状态空间、以 $P\coloneqq (p_{j - i}:i,j\in \mathbb{Z}^d)$ 为转移矩阵的马氏链.任取 $k\in \mathbb{Z}^d$ ，易知 $(X_{n} + k:n\geqslant 0)$ 也是有转移矩阵 $P$ 的随机游动.该性质称为随机游动的平移不变性.

例 4.2.2 在上例中假定  $\mathbf{P}(\xi_{n}=1)=p$  和  $\mathbf{P}(\xi_{n}=-1)=q$ ，其中  $p,q\geqslant0$  且  $p+q=1$ 。则  $X=(X_{n}:n\geqslant0)$  是一维简单随机游动，其转移矩阵  $P=(p(i,j):i,j\in\mathbb{Z})$  可表示为  $p(i,j)=p1_{\{j=i+1\}}+q1_{\{j=i-1\}}$ 。

例 4.2.3 依次做标号为  $1,2,\cdots$  的系列试验, 其中第 i 号试验成功的概率为  $q_{i}(0 \leqslant q_{i} \leqslant 1)$ . 若第 i 号试验成功, 则接着进行第  $i+1$  号试验; 否则下一步从第 1 号试验重新开始. 用  $X_{n}$  表示第 n 次试验的标号, 则  $X = (X_{n} : n \geqslant 0)$  是状态空间  $E := \{1, 2, \cdots\}$  上的马氏链且有转移矩阵  $P = (p_{ij} : i, j \in E)$ , 其中  $p_{ij} = q_{i} 1_{\{j=i+1\}} + (1 - q_{i}) 1_{\{j=0\}}$ .

## 4.2.2 有限维分布性质

定理 4.2.3 过程 X 满足关于流  $(\mathcal{G}_{n})$  以 P 为转移矩阵的马氏性 (4.2.1) 的充要条件是对于对任意的  $n \geqslant 0, G \in G_{n}$  和  $\{i, j_{1}, j_{2}, \cdots, j_{k}\} \subseteq E$  有

$$
\mathbf {P} (H | G \cap \{X _ {n} = i \}) = p (i, j _ {1}) p (j _ {1}, j _ {2}) \dots p (j _ {k - 2}, j _ {k - 1}) p (j _ {k - 1}, j _ {k}), \tag {4.2.4}
$$

其中  $H=\{X_{n+1}=j_{1},X_{n+2}=j_{2},\cdots,X_{n+k}=j_{k}\}$ .

证明 显然 (4.2.1) 式是 (4.2.4) 式的特殊形式, 故条件的充分性是显然的. 反之, 设 $X$ 满足关于流 $(\mathcal{G}_n)$ 以 $P$ 为转移矩阵的马氏性 (4.2.1), 则 (4.2.4) 式对 $k = 1$ 成立. 假设该式对某个 $k \geqslant 1$ 成立, 并取 $j_{k+1} \in E$. 由 (4.2.1) 式有

$$
\begin{array}{l} \mathbf {P} (X _ {n + k + 1} = j _ {k + 1} | G \cap \{X _ {n} = i \} \cap H) \\ = \mathbf {P} (X _ {n + k + 1} = j _ {k + 1} | G \cap \{X _ {n} = i \} \cap \{X _ {n + 1} = j _ {1}, X _ {n + 2} = j _ {2}, \dots , X _ {n + k} = j _ {k} \}) \\ = \mathbf {P} (X _ {n + k + 1} = j _ {k + 1} | G \cap \{X _ {n} = i, X _ {n + 2} = j _ {2}, \dots , X _ {n + k - 1} = j _ {k - 1} \} \cap \{X _ {n + k} = j _ {k} \}) \\ = p (j _ {k}, j _ {k + 1}). \\ \end{array}
$$

根据乘法公式, 并利用上式和归纳假设有

$$
\begin{array}{l} \mathbf {P} (G \cap \{X _ {n} = i \} \cap H \cap \{X _ {n + k + 1} = j _ {k + 1} \}) \\ = \mathbf {P} (G \cap \{X _ {n} = i \} \cap H) \mathbf {P} (X _ {n + k + 1} = j _ {k + 1} | G \cap \{X _ {n} = i \} \cap H) \\ = \mathbf {P} (G \cap \{X _ {n} = i \}) \mathbf {P} (H | G \cap \{X _ {n} = i \}) p (j _ {k}, j _ {k + 1}) \\ = \mathbf {P} (G \cap \{X _ {n} = i \}) p (i, j _ {1}) p (j _ {1}, j _ {2}) \dots p (j _ {k - 1}, j _ {k}) p (j _ {k}, j _ {k + 1}). \\ \end{array}
$$

所以

$$
\begin{array}{l} \mathbf {P} (H \cap \{X _ {n + k + 1} = j _ {k + 1} \} | G \cap \{X _ {n} = i \}) \\ = p (i, j _ {1}) p (j _ {1}, j _ {2}) \dots p (j _ {k - 1}, j _ {k}) p (j _ {k}, j _ {k + 1}). \\ \end{array}
$$

即把 $k$ 换为 $k + 1$ 后(4.2.4)式仍然成立.根据数学归纳法即得欲证结果. $\square$

推论 4.2.4 过程 X 满足关于流  $(\mathcal{G}_{n})$  以 P 为转移矩阵的马氏性 (4.2.1) 的充要条件是对任意的  $n \geqslant 0, k \geqslant 1, G \in G_{n}$  和  $i, j \in E$  有

$$
\mathbf {P} (X _ {n + k} = j | G \cap \{X _ {n} = i \}) = p _ {k} (i, j). \tag {4.2.5}
$$

证明 假设 $X$ 具有马氏性 (4.2.1). 简记 $H_{j_1, j_2, \dots, j_{k-1}} = \{X_{n+1} = j_1, X_{n+2} = j_2, \dots, X_{n+k-1} = j_{k-1}\}$. 根据定理 4.2.3, 我们有

$$
\begin{array}{l} \mathbf {P} (X _ {n + k} = j | G \cap \{X _ {n} = i \}) \\ = \sum_ {j _ {1}, j _ {2}, \dots , j _ {k - 1} \in E} \mathbf {P} (H _ {j _ {1}, j _ {2}, \dots , j _ {k - 1}} \cap \{X _ {n + k} = j \} | G \cap \{X _ {n} = i \}) \\ = \sum_ {j _ {1}, j _ {2}, \dots , j _ {k - 1} \in E} p (i, j _ {1}) p (j _ {1}, j _ {2}) \dots p (j _ {k - 1}, j) = p _ {k} (i, j). \\ \end{array}
$$

所以 (4.2.5) 式成立. 反之, 若 (4.2.5) 式成立, 取 $k = 1$ 即得 (4.2.1) 式, 故 $X$ 具有马氏性. $\square$

对照 (4.2.1) 式和 (4.2.5) 式, 若 $X$ 是关于流 $(\mathcal{G}_n)$ 以 $P$ 为转移矩阵的马氏链, 我们自然地称 $P^k := (p_k(i,j): i, j \in E)$ 为 $X$ 的 $k$ 步转移矩阵.

定理 4.2.5 过程 X 相对其自然流是以 P 为转移矩阵的马氏链且有初始分布  $\mu = (\mu(i) : i \in E)$  的充要条件是对于任意的  $n \geqslant 0$  和  $\{i_{0}, i_{1}, \cdots, i_{n}\} \subseteq E$  有

$$
\mathbf {P} (X _ {k} = i _ {k}: 0 \leqslant k \leqslant n) = \mu (i _ {0}) p (i _ {0}, i _ {1}) \dots p (i _ {n - 1}, i _ {n}). \tag {4.2.6}
$$

证明 假设 $X$ 为以 $P$ 为转移矩阵、以 $(\mu(i):i\in E)$ 为初始分布的马氏链. 由定理4.2.3知(4.2.4)式成立. 特别地, 取 $n = 0$ 和 $G = \Omega$ 有

$$
\mathbf {P} (X _ {k} = i _ {k}: 1 \leqslant k \leqslant n | X _ {0} = i _ {0}) = p (i _ {0}, i _ {1}) \dots p (i _ {n - 1}, i _ {n}).
$$

再由乘法公式即得 (4.2.6) 式. 反之, 假设性质 (4.2.6) 成立. 显然 $X_0$ 有分布 $(\mu(i): i \in E)$ 且

$$
\mathbf {P} (\{X _ {k} = i _ {k}: 0 \leqslant k \leqslant n \} \cap \{X _ {n + 1} = j \}) = \mu (i _ {0}) p (i _ {0}, i _ {1}) \dots p (i _ {n - 1}, i _ {n}) p (i _ {n}, j).
$$

将上式两端分别除以 (4.2.6) 式的两端即得 (4.2.3) 式. 再由定理 4.2.2 知 $X$ 是以 $P$ 为转移矩阵的马氏链. $\square$

推论 4.2.6 若以 P 为转移矩阵的马氏链 X 有初始分布  $\mu$ ，则对于任意的  $n \geqslant 0$  随机变量  $X_{n}$  有分布  $\mu P^{n}$ .

## 4.2.3 强马氏性

首先回忆关于停时的概念. 设  $(\mathcal{G}_{n}: n \geqslant 0)$  为概率空间  $(\Omega, \mathcal{G}, \mathbf{P})$  上的离散时间流. 称映射  $\tau: \Omega \to \{0, 1, 2, \cdots, \infty\}$  为关于该流的停时, 是指对任何整数  $n \geqslant 0$  都有  $\{\tau \leqslant n\} \in \mathcal{G}_{n}$ . 注意  $\tau$  是  $(\mathcal{G}_{n})$  的停时当且仅当对任意的  $n \geqslant 0$  都有  $\{\tau = n\} \in \mathcal{G}_{n}$ .

对于 $(\mathcal{G}_n)$ 的停时 $\tau$, 我们将 $\mathcal{G}_{\infty} := \sigma \left( \bigcup_{n=0}^{\infty} \mathcal{G}_n \right)$ 中对所有 $n \geqslant 0$ 满足 $A \cap \{\tau \leqslant n\} \in \mathcal{G}_n$ 的集合 $A$ 的全体记为 $\mathcal{G}_{\tau}$, 则 $\mathcal{G}_{\tau}$ 是一个 $\sigma$ 代数, 而且 $\tau$ 关于 $\mathcal{G}_{\tau}$ 可测. 另外, 显然 $A \in \mathcal{G}_{\tau}$ 当且仅当对任意的 $n \geqslant 0$ 有 $A \cap \{\tau = n\} \in \mathcal{G}_n$.

若过程 $X = (X_{n}:n\geqslant 0)$ 关于流 $(\mathcal{G}_n)$ 适应, 而 $\tau$ 是 $(\mathcal{G}_n)$ 的停时, 则映射 $\omega \mapsto X_{\tau (\omega)}(\omega)$ 限制在 $\{\tau < \infty \}$ 上关于 $\{\tau < \infty \} \cap \mathcal{G}_{\tau}$ 可测. 事实上, 对任意的 $n\geqslant 0$ 和$i\in E$ 有

$$
\{\tau <   \infty \} \cap \{X _ {\tau} = i \} \cap \{\tau = n \} = \{X _ {n} = i \} \cap \{\tau = n \} \in \mathcal {G} _ {n},
$$

进而  $\{\tau < \infty\} \cap \{X_{\tau} = i\} \in \mathcal{G}_{\tau}.$

定理 4.2.7 设  $(X_{n})$  为关于流  $(\mathcal{G}_{n})$  以 P 为转移矩阵的马氏链, 而  $\tau$  是  $(\mathcal{G}_{n})$  的停时, 则对于任意的  $G \in G_{\tau}$  和  $\{i, j_{1}, j_{2}, \cdots, j_{k}\} \subseteq E$  有

$$
\mathbf {P} (H | G \cap \{\tau <   \infty , X _ {\tau} = i \}) = p (i, j _ {1}) p (j _ {1}, j _ {2}) \dots p (j _ {k - 1}, j _ {k}), \tag {4.2.7}
$$

其中  $H=\{X_{\tau+1}=j_{1},X_{\tau+2}=j_{2},\cdots,X_{\tau+k}=j_{k}\}$ .

证明 记  $H_{n}=\{X_{n+1}=j_{1},X_{n+2}=j_{2},\cdots,X_{n+k}=j_{k}\}$ . 根据  $\sigma$  可加性, 并对  $G\cap\{\tau=n\}\in\mathcal{G}_{n}$  应用定理 4.2.3 得

$$
\begin{array}{l} \mathbf {P} (G \cap \{\tau <   \infty , X _ {\tau} = i \} \cap H) \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (G \cap \{\tau = n, X _ {n} = i \} \cap H _ {n}) \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (G \cap \{\tau = n, X _ {n} = i \}) \mathbf {P} (H _ {n} | G \cap \{\tau = n \} \cap \{X _ {n} = i \}) \\ = \sum_ {n = 0} ^ {\infty} \mathbf {P} (G \cap \{\tau = n, X _ {\tau} = i \}) p (i, j _ {1}) p (j _ {1}, j _ {2}) \dots p (j _ {k - 1}, j _ {k}) \\ = \mathbf {P} (G \cap \{\tau <   \infty , X _ {\tau} = i \}) p (i, j _ {1}) p (j _ {1}, j _ {2}) \dots p (j _ {k - 1}, j _ {k}). \\ \end{array}
$$

将上式两端同除以 $\mathbf{P}(G\cap \{\tau <  \infty ,X_{\tau} = i\})$ 即知(4.2.7)式成立.□

推论 4.2.8 设  $(X_{n})$  为关于流  $(\mathcal{G}_{n})$  以 P 为转移矩阵的马氏链, 而  $\tau$  是  $(\mathcal{G}_{n})$  的停时, 则对于任意的  $k \geqslant 1, G \in G_{\tau}$  和  $i, j \in E$  有

$$
\mathbf {P} (X _ {\tau + k} = j | G \cap \{\tau <   \infty , X _ {\tau} = i \}) = p _ {k} (i, j). \tag {4.2.8}
$$

等式 (4.2.7) 和 (4.2.8) 都是 (4.2.1) 式的推论, 但在形式上它们又都是 (4.2.1) 式的加强. 我们称 (4.2.7) 式或 (4.2.8) 式为 $X$ 关于流 $(\mathcal{G}_n)$ 以 $P$ 为转移矩阵的强马氏性. 所以, 对于离散时间离散状态随机过程, 马氏性和强马氏性是等价的.

定理 4.2.9 设  $(X_{n})$  为关于流  $(\mathcal{G}_{n})$  以 P 为转移矩阵的马氏链, 而  $\tau$  是  $(\mathcal{G}_{n})$  的停时. 记  $\mathcal{F}^{\tau} = \sigma(X_{\tau}, X_{\tau+1}, \cdots)$ , 则对于任意的  $i \in E, G \in G_{\tau}$  和  $F \in F^{\tau}$  有

$$
\mathbf {P} (F | G \cap \{\tau <   \infty , X _ {\tau} = i \}) = \mathbf {P} (F | \tau <   \infty , X _ {\tau} = i). \tag {4.2.9}
$$

证明 根据定理 4.2.7 易知 (4.2.9) 式对于 $F = \{X_{\tau+1} = j_1, X_{\tau+2} = j_2, \cdots, X_{\tau+k} = j_k\}$ 成立. 对于整数 $k \geqslant 0$, 记 $\mathscr{F}_k^\tau = \sigma(X_\tau, X_{\tau+1}, \cdots, X_{\tau+k})$. 分别考虑 $j_0 \neq i$ 和 $j_0 = i$ 两种情况, 知 (4.2.9) 式对形如 $F = \{X_\tau = j_0, X_{\tau+1} = j_1, \cdots, X_{\tau+k} = j_k\} \in \mathscr{F}_k^\tau$ 的事件也成立. 对于一般的 $F \in \mathscr{F}_k^\tau$, 存在 $A \subseteq E^{k+1}$ 使 $F = \{(X_\tau, X_{\tau+1}, \cdots, X_{\tau+k}) \in A\}$. 利用条件概率的可数可加性可知此时 (4.2.9) 式仍然成立. 这就证明了 (4.2.9) 式对一切 $F \in \bigcup_k \mathscr{F}_k^\tau$ 成立. 注意 $\bigcup_k \mathscr{F}_k^\tau$ 是集代数且 $\mathscr{F}^\tau = \sigma\left(\bigcup_k \mathscr{F}_k^\tau\right)$. 再应用单调类定理即知该式对一切 $F \in \mathscr{F}^\tau$ 成立. □

基于上面的结论, 与定理 4.1.3 和定理 4.1.6 的证明类似, 我们有如下的:

定理 4.2.10 设  $(X_{n}: n \geqslant 0)$  是关于流  $(\mathcal{G}_{n}: n \geqslant 0)$  以 P 为转移矩阵的马氏链. 再设  $\tau$  为  $(\mathcal{G}_{n})$  的停时并取  $A \in G_{\tau}$ . 则在条件概率  $\mathbf{P}_{A} := \mathbf{P}(\cdot | A \cap \{\tau < \infty\})$  之下  $(X_{\tau+n}: n \geqslant 0)$  具有关于流  $(\mathcal{G}_{\tau+n}: n \geqslant 0)$  以 P 为转移矩阵的马氏性.

定理 4.2.11 设  $(X_{n})$  为关于流  $(\mathcal{G}_{n})$  以 P 为转移矩阵的马氏链, 而  $\tau$  是  $(\mathcal{G}_{n})$  的停时, 则对于任意的  $i \in E, G \in G_{\tau}$  和  $F \in F^{\tau}$  有

$$
\mathbf {P} (G \cap F | \tau <   \infty , X _ {\tau} = i) = \mathbf {P} (G | \tau <   \infty , X _ {\tau} = i) \mathbf {P} (F | \tau <   \infty , X _ {\tau} = i).
$$

推论 4.2.12 设  $(X_{n})$  为关于流  $(\mathcal{G}_{n})$  以 P 为转移矩阵的马氏链, 而  $\tau$  是  $(\mathcal{G}_{n})$  的停时, 则对任意的  $i \in E$ , 在条件概率  $\mathbf{P}(\cdot|\tau < \infty, X_{\tau} = i)$  之下  $(X_{n \wedge \tau}: n \geqslant 0)$  和  $(X_{\tau+n}: n \geqslant 0)$  是独立的.

根据推论 4.2.12, 在当前的状态  $X_{\tau}$  给定的条件下 X 在过去和将来的运动情况是相互独立的, 注意这里所说的 “当前” 是由停时  $\tau$  代表的随机时刻.

令  $\tau_{a}=\inf\{n\geqslant0:X_{n}=a\}$  是以 P 为转移矩阵的马氏链 X 到  $a\in E$  的首达时.
易证  $X^{a}=(X_{n\wedge\tau_{a}}:n\geqslant0)$  也是马氏链, 且有转移矩阵  $P^{a}=(p^{a}(i,j):i,j\in E)$ , 其中

$$
p ^ {a} (i, j) = p (i, j) 1 _ {\{a \neq i \}} + 1 _ {\{a = i = j \}}. \tag {4.2.10}
$$

称 $X^{a}$ 为在 $a$ 被吸收的马氏链或在 $a$ 停止的马氏链.根据定理4.2.10，在条件概率 $\mathbf{P}(\cdot |\tau_a < \infty)$ 之下 $Y^{a} := (X_{\tau_a + n}: n \geqslant 0)$ 是从 $a$ 出发以 $P$ 为转移矩阵的马氏链.特别地，当 $\mathbf{P}(\tau_a < \infty) = 1$ 时 $Y^{a}$ 在原概率之下是从 $a$ 出发以 $P$ 为转移矩阵的马氏链.

## 4.2.4 随机游动的反射原理

令 $X = (X_{n}: n \geqslant 0)$ 是由 (1.2.1) 式或 (4.1.7)式定义的 $d$ 维随机游动, 其中 $\{\xi_{n}: n \geqslant 1\}$ 是取值于 $\mathbb{Z}^{d}$ 的独立同分布随机变量. 记 $p_{k} = \mathbf{P}(\xi_{n} = k), k \in \mathbb{Z}^{d}$. 我们知道 $X$ 是以 $\mathbb{Z}^{d}$ 为状态空间、以 $P := (p_{j-i}: i, j \in \mathbb{Z}^{d})$ 为转移矩阵的马氏链. 易证 $-X = (-X_{n}: n \geqslant 0)$ 是以 $\mathbb{Z}^{d}$ 为状态空间、以 $Q := (p_{i-j}: i, j \in \mathbb{Z}^{d})$ 为转移矩阵的马氏链. 特别地, 若 $X$ 是对称的, 则有 $P = Q$.

定理 4.2.13 (反射原理) 设  $X = (X_{n} : n \geqslant 0)$  是从原点 0 出发的一维对称简单随机游动. 则对任何整数  $x \in Z_{+}$ ，有

$$
\mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant x \Big) = \mathbf {P} (X _ {n} \geqslant x) + \mathbf {P} (X _ {n} > x), \tag {4.2.11}
$$

进而有

$$
2 \mathbf {P} (X _ {n} > x) \leqslant \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant x \Big) \leqslant 2 \mathbf {P} (X _ {n} \geqslant x). \tag {4.2.12}
$$

证明 记 $M_{n} = \max_{0\leqslant k\leqslant n}X_{k}$ ，再令 $\tau = \inf \{n\geqslant 0:X_n = x\}$ ，则

$$
\begin{array}{l} \mathbf {P} (M _ {n} \geqslant x) = \mathbf {P} (M _ {n} \geqslant x, X _ {n} \geqslant x) + \mathbf {P} (M _ {n} \geqslant x, X _ {n} <   x) \\ = \mathbf {P} (X _ {n} \geqslant x) + \mathbf {P} (\tau \leqslant n, X _ {n} <   x). \\ \end{array}
$$

根据强马氏性, 在条件概率

$$
\mathbf {P} (\cdot | \tau = k) = \mathbf {P} (\cdot | \tau = k, X _ {k} = x) = \mathbf {P} (\cdot | \{\tau = k, X _ {k} = x \} \cap \{\tau <   \infty \})
$$

之下 $(X_{k+n}:n\geqslant0)$ 是从x出发的对称简单随机游动,故

$$
\begin{array}{l} \mathbf {P} (\tau \leqslant n, X _ {n} <   x) = \sum_ {k = 0} ^ {n} \mathbf {P} (\tau = k, X _ {k} = x, X _ {n} <   x) \\ = \sum_ {k = 0} ^ {n} \mathbf {P} (\tau = k, X _ {k} = x) \mathbf {P} (X _ {n} <   x | \tau = k, X _ {k} = x) \\ = \sum_ {k = 0} ^ {n} \mathbf {P} (\tau = k, X _ {k} = x) \mathbf {P} (X _ {n} > x | \tau = k, X _ {k} = x) \\ = \sum_ {k = 0} ^ {n} \mathbf {P} (\tau = k, X _ {k} = x, X _ {n} > x) \\ = \mathbf {P} (\tau \leqslant n, X _ {n} > x) = \mathbf {P} (X _ {n} > x), \\ \end{array}
$$

其中第 3 个等号成立是由于对称性. 所以 (4.2.11) 式成立. □

推论 4.2.14 设  $X = (X_{n} : n \geqslant 0)$  是从 0 出发的一维对称简单随机游动, 则对任何整数  $x \in Z_{+}$ , 有

$$
2 \mathbf {P} (0 <   X _ {n} <   x) \leqslant \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} <   x \Big) \leqslant 2 \mathbf {P} (0 \leqslant X _ {n} \leqslant x). \tag {4.2.13}
$$

证明 由于 $\mathbf{P}(X_n > 0) \leqslant 1/2$, 利用 (4.2.12) 式有

$$
\begin{array}{l} \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} <   x \Big) = 1 - \mathbf {P} \Big (\max _ {0 \leqslant k \leqslant n} X _ {k} \geqslant x \Big) \\ \geqslant 2 \mathbf {P} (X _ {n} > 0) - 2 \mathbf {P} (X _ {n} \geqslant x). \\ \end{array}
$$

故 (4.2.13) 式中的第一个不等号成立. 类似地, 由 $\mathbf{P}(X_n \geqslant 0) \geqslant 1/2$ 可证第二个不等号成立. $\square$

## 练习题

1. 设 $(X_{n}: n \geqslant 0)$ 是转移矩阵为 $P$ 的马氏链. 固定整数 $d \geqslant 1$, 并令 $Y_{n} = X_{nd}$. 证明: $(Y_{n}: n \geqslant 0)$ 是转移矩阵为 $P^{d}$ 的马氏链.
2. 令 $(X_{n}: n \geqslant 0)$ 是状态空间 $E$ 上的以 $P = (p_{ij})$ 为转移矩阵的马氏链. 证明 $\{(X_{n}, X_{n+1}): n \geqslant 0\}$ 是 $E^{2}$ 上的马氏链, 并给出其转移矩阵 $Q = (q_{(i,j),(k,l)})$.

简答: 欲求转移概率为

$$
q _ {(i, j), (k, l)} = \left\{ \begin{array}{l l} 0, & j \neq k, \\ p _ {j l}, & j = k. \end{array} \right.
$$

3. 设 $(X_{n}: n \geqslant 0)$ 和 $(Y_{n}: n \geqslant 0)$ 是空间 $E$ 上的相互独立的马氏链, 且分别有转移矩阵 $(p_{ij}: i, j \in E)$ 和 $(q_{ij}: i, j \in E)$. 证明 $\{(X_{n}, Y_{n}): n \geqslant 0\}$ 是乘积空间 $E^{2} := E \times E$ 上的马氏链, 并给出其转移矩阵.

4. 在上题的情况下, 令 $(\mathcal{G}_n : n \geqslant 0)$ 是 $\{(X_n, Y_n) : n \geqslant 0\}$ 的自然流.

(1) 证明 $(X_{n}: n \geqslant 0)$ 是关于流 $(\mathcal{G}_n: n \geqslant 0)$ 以 $(p_{ij}: i, j \in E)$ 为转移矩阵的马氏链;
(2) 在什么条件下 $(\mathcal{G}_n: n \geqslant 0)$ 也是 $(X_n: n \geqslant 0)$ 的自然流？

5. 设 $(X_{n})$ 是一维对称简单随机游动. 令 $\tau_{a} = \inf \{n \geqslant 0 : X_{n} = a\}$ 为点 $a \in \mathbb{Z}$ 的首达时.

(1) 证明 $(X_{\tau_a + n}:n\geqslant 0)$ 也是一维对称简单随机游动;
(2) 证明 $(X_{n\wedge \tau_a}:n\geqslant 0)$ 是 $\mathbb{Z}$ 上的马氏链并给出其转移矩阵;
(3) 证明 $(X_{n\wedge \tau}:n\geqslant 0)$ 和 $(X_{\tau_a + n}:n\geqslant 0)$ 独立.

6. 设 $(X_{n})$ 为从原点出发的一维对称简单随机游动. 证明 $(|X_{n}|: n \geqslant 0)$ 是 $\mathbb{Z}_{+}$ 上的马氏链, 并给出其转移矩阵.

## 4.3 状态的分类

考虑一个以 $E$ 为状态空间、以 $P = (p_{ij}: i, j \in E)$ 为转移矩阵的马氏链 $X = (X_n : n \geqslant 0)$. 令 $P^n = (p_{ij}(n): i, j \in E)$ 为 $X$ 的 $n$ 步转移矩阵. 为方便起见, 我们写 $\mathbf{P}_i = \mathbf{P}(\cdot | X_0 = i)$, 并用 $\mathbf{E}_i$ 表示对应的数学期望. 对于 $i, j \in E$ 和 $n \geqslant 1$ 令

$$
f _ {i j} (n) = \mathbf {P} _ {i} (X _ {n} = j, X _ {k} \neq j: 0 <   k <   n), \tag {4.3.1}
$$

它是从 $i$ 出发的链在时刻 $n$ 首达 $j$ 的概率. 容易看出, 对任何 $n \geqslant 1$ 有 $f_{ij}(n) \leqslant p_{ij}(n)$ 且

$$
p _ {i j} (n) = \mathbf {P} _ {i} (X _ {n} = j) = \sum_ {k = 1} ^ {n} f _ {i j} (k) p _ {j j} (n - k). \tag {4.3.2}
$$

再令

$$
f _ {i j} ^ {*} = \sum_ {n = 1} ^ {\infty} f _ {i j} (n), \quad p _ {i j} ^ {*} = \sum_ {n = 0} ^ {\infty} p _ {i j} (n), \tag {4.3.3}
$$

其中后者可能为无穷. 定义 $j \in E$ 的击中时

$$
T _ {j} = \inf \{n \geqslant 1: X _ {n} = j \}.
$$

显然有  $f_{ij}^{*} = \mathbf{P}_{i}(T_{j} < \infty)$ .

## 4.3.1 常返态和暂留态

定义 4.3.1 称状态  $i \in E$  为常返的, 是指  $f_{ii}^{*} = \mathbf{P}_{i}(T_{i} < \infty) = 1$ ; 称该状态为正常返的, 是指它是常返的且

$$
\mathbf {E} _ {i} (T _ {i}) = \sum_ {n = 1} ^ {\infty} n f _ {i i} (n) <   \infty .
$$

常返但非正常返的状态称为零常返的. 非常返的状态也称为暂留的.

定理 4.3.1 令  $S_{0}=0,$  并对  $k\geqslant1$  递归地定义  $S_{k}=\min\{n>S_{k-1}:X_{n}=i\}$ ,
则状态  $i \in E$  常返 (或暂留) 当且仅当

$$
\mathbf {P} _ {i} (S _ {k} <   \infty \text {对所有} k \geqslant 0 \text {成立}) = 1 (\text {或} 0).
$$

证明 注意  $\{S_{0}, S_{1}, S_{2}, \cdots\}$  是递增的停时列. 对于  $k \geqslant 1$ , 在集合  $\{S_{k} < \infty\}$  上几乎必然有  $X_{S_{k}} = i$ . 由定理 4.2.10, 在  $\mathbf{P}_{i}(\cdot | S_{k} < \infty) = \mathbf{P}_{i}(\cdot | S_{k} < \infty, X_{S_{k}} = i)$  之下  $(X_{S_{k} + n} : n \geqslant 0)$  是从 i 出发且以 P 为转移矩阵的马氏链, 从而

$$
\mathbf {P} _ {i} (S _ {k + 1} <   \infty | S _ {k} <   \infty) = \mathbf {P} _ {i} (S _ {1} <   \infty) = \mathbf {P} _ {i} (T _ {i} <   \infty) = f _ {i i} ^ {*}.
$$

由乘法公式和上式得

$$
\begin{array}{l} \mathbf {P} _ {i} (S _ {k} <   \infty) = \mathbf {P} _ {i} (S _ {k - 1} <   \infty , S _ {k} <   \infty) \\ = \mathbf {P} _ {i} (S _ {k - 1} <   \infty) \mathbf {P} _ {i} (S _ {k} <   \infty | S _ {k - 1} <   \infty) \\ = \mathbf {P} _ {i} (S _ {k - 1} <   \infty) f _ {i i} ^ {*} = \dots = (f _ {i i} ^ {*}) ^ {k}. \\ \end{array}
$$

再利用概率测度的上连续性有

$$
\mathbf {P} _ {i} \Big (\bigcap_ {k = 1} ^ {\infty} \{S _ {k} <   \infty \} \Big) = \lim _ {k \to \infty} \mathbf {P} _ {i} (S _ {k} <   \infty) = \lim _ {k \to \infty} (f _ {i i} ^ {*}) ^ {k}.
$$

故得欲证结论. □

推论 4.3.2 状态  $i \in E$  常返 (或暂留) 当且仅当

$$
\mathbf {P} _ {i} \bigg (\bigcap_ {n = 1} ^ {\infty} \bigcup_ {k = n} ^ {\infty} \{X _ {k} = i \} \bigg) = 1 (\text {或} 0). \tag {4.3.4}
$$

定理 4.3.1 和推论 4.3.2 说明  $i \in E$  常返意味着从该状态出发的链以概率 1 返回无限次, 而  $i \in E$  暂留则意味着从该状态出发的链以概率 1 至多返回有限次.

定理 4.3.3 设  $i \in E$  为常返态. 记  $\tau_{k} = S_{k} - S_{k-1}$ ，则在  $P_{i}$  之下  $\{\tau_{k} : k = 1, 2, \cdots\}$  为独立同分布随机变量序列.

证明 根据定理 4.2.10, 对任意 $k \geqslant 1$, 在 $\mathbf{P}_i(\cdot|S_k < \infty) = \mathbf{P}_i(\cdot|S_k < \infty, X_{S_k} = i)$ 之下 $(X_{S_k+n}: n \geqslant 0)$ 是从 $i$ 出发以 $P$ 为转移矩阵的马氏链, 且与 $(X_{n \wedge S_k}: n \geqslant 0)$ 独立. 由定理 4.3.1 有 $\mathbf{P}_i(S_k < \infty) = \mathbf{P}_i(S_k < \infty, X_{S_k} = i) = 1$, 故

$$
\mathbf {P} _ {i} = \mathbf {P} _ {i} (\cdot | S _ {k} <   \infty) = \mathbf {P} _ {i} (\cdot | S _ {k} <   \infty , X _ {S _ {k}} = i).
$$

因此在  $\mathbf{P}_{i}$  之下  $(X_{S_{k+n}}:n\geqslant0)$  是从 i 出发以 P 为转移矩阵的马氏链, 且与  $(X_{n\wedge S_{k}}:n\geqslant0)$  独立. 注意  $\tau_{k+1}$  是  $(X_{S_{k+n}}:n\geqslant0)$  对 i 的击中时. 所以, 在  $P_{i}$  之下  $\tau_{1},\tau_{2},\cdots$  是同分布的随机变量. 因为  $\tau_{1},\tau_{2},\cdots,\tau_{k}$  由  $(X_{n\wedge S_{k}}:n\geqslant0)$  决定, 而  $\tau_{k+1}$  由  $(X_{S_{k+n}}:n\geqslant0)$  决定. 所以在  $P_{i}$  之下  $\{\tau_{1},\tau_{2},\cdots,\tau_{k}\}$  与  $\tau_{k+1}$  独立. 再由  $k\geqslant1$  的任意性, 易知在  $P_{i}$  之下  $\tau_{1},\tau_{2},\cdots$  是相互独立的. □

我们知道, 任何有界数列由其母函数唯一决定. 为方便后面的讨论, 对 $i, j \in E$ 定义数列 $\{f_{ij}(n): n \geqslant 1\}$ 和 $\{p_{ij}(n): n \geqslant 0\}$ 的母函数

$$
F _ {i j} ^ {*} (z) = \sum_ {n = 1} ^ {\infty} f _ {i j} (n) z ^ {n}, \quad P _ {i j} ^ {*} (z) = \sum_ {n = 0} ^ {\infty} p _ {i j} (n) z ^ {n}. \tag {4.3.5}
$$

这里不妨限定 $|z| < 1$. 由 (4.3.2) 式有

$$
\begin{array}{l} P _ {i j} ^ {*} (z) = \delta_ {i j} + \sum_ {n = 1} ^ {\infty} \sum_ {k = 1} ^ {n} f _ {i j} (k) p _ {j j} (n - k) z ^ {n} \\ = \delta_ {i j} + \sum_ {k = 1} ^ {\infty} \sum_ {n = k} ^ {\infty} f _ {i j} (k) z ^ {k} p _ {j j} (n - k) z ^ {n - k} \\ = \delta_ {i j} + \sum_ {k = 1} ^ {\infty} \sum_ {n = 0} ^ {\infty} f _ {i j} (k) z ^ {k} p _ {j j} (n) z ^ {n}, \\ \end{array}
$$

其中 $\delta_{ij} = 1_{\{i = j\}}$ .故得

$$
P _ {i j} ^ {*} (z) = \delta_ {i j} + F _ {i j} ^ {*} (z) P _ {j j} ^ {*} (z), \quad | z | <   1. \tag {4.3.6}
$$

定理 4.3.4 状态  $i \in E$  是暂留的当且仅当

$$
p _ {i i} ^ {*} = \sum_ {n = 0} ^ {\infty} p _ {i i} (n) <   \infty .
$$

而且, 此时有 $p_{ii}^{*} = (1 - f_{ii}^{*})^{-1}$.

证明 注意 $p_{ii}^{*} = \lim_{z\uparrow 1}P_{ii}^{*}(z)$ 和 $f_{ii}^{*} = \lim_{z\uparrow 1}F_{ii}^{*}(z)$. 由 (4.3.6) 式得

$$
[ 1 - F _ {i i} ^ {*} (z) ] P _ {i i} ^ {*} (z) = 1, \quad | z | <   1. \tag {4.3.7}
$$

在上式两边令 $z \uparrow 1$ 知 $f_{ii}^{*} < 1$ 当且仅当 $p_{ii}^{*} < \infty$, 且此时有 $p_{ii}^{*} = (1 - f_{ii}^{*})^{-1}$. □

推论 4.3.5 状态  $i \in E$  是暂留的当且仅当对每个  $k \in E$  有

$$
p _ {k i} ^ {*} = \sum_ {n = 0} ^ {\infty} p _ {k i} (n) <   \infty .
$$

证明 若 $i \in E$ 是暂留的, 由定理4.3.4有 $p_{ii}^{*} < \infty$. 因为 $f_{ki}^{*} \leqslant 1$, 由(4.3.2)式得

$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} p _ {k i} (n) = \sum_ {n = 1} ^ {\infty} \sum_ {m = 1} ^ {n} f _ {k i} (m) p _ {i i} (n - m) \\ = \sum_ {m = 1} ^ {\infty} \sum_ {n = m} ^ {\infty} f _ {k i} (m) p _ {i i} (n - m) \\ = \sum_ {m = 1} ^ {\infty} \sum_ {n = 0} ^ {\infty} f _ {k i} (m) p _ {i i} (n) = f _ {k i} ^ {*} p _ {i i} ^ {*} <   \infty . \\ \end{array}
$$

故得

$$
p _ {k i} ^ {*} = \delta_ {k i} + \sum_ {n = 1} ^ {\infty} p _ {k i} (n) = \delta_ {k i} + f _ {k i} ^ {*} p _ {i i} ^ {*} <   \infty .
$$

反之, 若对每个 $k \in E$ 有 $p_{ki}^{*} < \infty$, 则 $p_{ii}^{*} < \infty$. 由定理4.3.4知 $i \in E$ 是暂留的. $\square$

推论 4.3.6 若状态  $i \in E$  是暂留的, 则对每个  $k \in E$  有  $\lim_{n \to \infty} p_{ki}(n) = 0$ .

定义 4.3.2 若 E 中的所有状态都是常返的, 则称 X 或 P 是常返的. 若 E 中的所有状态都是暂留的, 则称 X 或 P 是暂留的.

## 4.3.2 随机游动的常返性

例 4.3.1 注意由原点出发的 d 维对称简单随机游动 X 只能在偶数步以严格正概率返回原点. 根据斯特林 (Stirling) 公式: 当  $n \rightarrow \infty$  时,

$$
n! \sim \sqrt {2 \pi n} \Bigl (\frac {n}{\mathrm{e}} \Bigr) ^ {n}.
$$

由此得

$$
\frac {(2 n) !}{(n !) ^ {2}} \sim \frac {\sqrt {4 \pi n} \left(\frac {2 n}{\mathrm{e}}\right) ^ {2 n}}{2 \pi n \left(\frac {n}{\mathrm{e}}\right) ^ {2 n}} = \frac {2 ^ {2 n}}{\sqrt {\pi n}}. \tag {4.3.8}
$$

根据例 1.2.2 的结论, 当 d = 1 时,

$$
p _ {0 0} (2 n) = \frac {1}{2 ^ {2 n}} \frac {(2 n) !}{(n !) ^ {2}} \sim \frac {1}{\sqrt {\pi n}};
$$

当 $d = 2$ 时，

$$
p _ {0 0} (2 n) = \frac {1}{4 ^ {2 n}} \bigg (\frac {(2 n) !}{(n !) ^ {2}} \bigg) ^ {2} \sim \frac {1}{\pi n}.
$$

所以当 $d \leqslant 2$ 时 $X$ 常返. 根据例1.2.2, 当 $d = 3$ 时有

$$
p _ {0 0} (2 n) = \frac {1}{2 ^ {2 n}} \frac {(2 n) !}{(n !) ^ {2}} \sum_ {i + j + k = n} \left(\frac {1}{3 ^ {n}} \frac {n !}{i ! j ! k !}\right) ^ {2}.
$$

这里最后括号里的量在 $i = j = k$ 或临近处达到其最大值, 且在 $i + j + k = n$ 条件下求和为1. 根据斯特林公式有

$$
\begin{array}{l} \sum_ {i + j + k = n} \left(\frac {1}{3 ^ {n}} \frac {n !}{i ! j ! k !}\right) ^ {2} \leqslant \max _ {i + j + k = n} \left(\frac {1}{3 ^ {n}} \frac {n !}{i ! j ! k !}\right) \\ \sim \frac {1}{3 ^ {n}} \frac {\sqrt {2 \pi n} \left(\frac {n}{\mathrm{e}}\right) ^ {n}}{\left(\frac {2 \pi n}{3}\right) ^ {3 / 2} \left(\frac {n}{3 \mathrm{e}}\right) ^ {n}} = O \left(\frac {1}{n}\right). \\ \end{array}
$$

再利用 (4.3.8) 式得到

$$
p _ {0 0} (2 n) \leqslant \frac {1}{2 ^ {2 n}} \frac {(2 n) !}{(n !) ^ {2}} O \Big (\frac {1}{n} \Big) = \frac {1}{2 ^ {2 n}} \frac {2 ^ {2 n}}{\sqrt {\pi n}} O \Big (\frac {1}{n} \Big) = O \Big (\frac {1}{n ^ {3 / 2}} \Big).
$$

所以 3 维对称简单随机游动是暂留的. 类似地可以证明, 当  $d \geqslant 4$  时 d 维对称简单随机游动也是暂留的.

例 4.3.2 设 p, q > 0 满足  $p + q = 1$ . 考虑一维简单随机游动的转移矩阵  $P = (p_{ij} : i, j \in \mathbb{Z})$ , 其中  $p_{ij} = p1_{\{j=i+1\}} + q1_{\{j=i-1\}}$ . 注意从原点出发的游动在奇数步返回原点的概率是零, 而在其以严格正概率返回的 2n 步中必定有 n 步向左而另外 n 步向右. 所以

$$
p _ {0 0} (2 n) = \binom {2 n} {n} p ^ {n} q ^ {n}, \quad n \geqslant 0.
$$

根据泰勒展式, 当  $|x| < 1$  时有

$$
\begin{array}{l} (1 - x) ^ {- 1 / 2} = 1 + \sum_ {n = 1} ^ {\infty} \frac {\left(- \frac {1}{2}\right) \left(- \frac {3}{2}\right) \cdots \left(- \frac {2 n - 1}{2}\right)}{n !} (- x) ^ {n} \\ = 1 + \sum_ {n = 1} ^ {\infty} \frac {(2 n - 1) ! !}{2 ^ {n} n !} x ^ {n} = 1 + \sum_ {n = 1} ^ {\infty} \frac {(2 n) ! ! (2 n - 1) ! !}{2 ^ {n} n ! (2 n) ! !} x ^ {n} \\ = 1 + \sum_ {n = 1} ^ {\infty} \frac {(2 n) !}{n ! n !} \left(\frac {x}{4}\right) ^ {n} = 1 + \sum_ {n = 1} ^ {\infty} \binom {2 n} {n} \left(\frac {x}{4}\right) ^ {n}. \\ \end{array}
$$

故当 $4pqz^{2} < 1$ 时有

$$
P _ {0 0} ^ {*} (z) = \sum_ {n = 0} ^ {\infty} \binom {2 n} {n} p ^ {n} q ^ {n} z ^ {2 n} = \frac {1}{\sqrt {1 - 4 p q z ^ {2}}}.
$$

再利用 (4.3.6) 式得

$$
F _ {0 0} ^ {*} (z) = \sum_ {n = 1} ^ {\infty} f _ {0 0} (n) z ^ {n} = 1 - P _ {0 0} ^ {*} (z) ^ {- 1} = 1 - \sqrt {1 - 4 p q z ^ {2}},
$$

从而

$$
\mathbf {P} _ {0} (T _ {0} <   \infty) = \sum_ {n = 1} ^ {\infty} f _ {0 0} (n) = F ^ {*} (1 -) = 1 - \sqrt {1 - 4 p q}.
$$

由此易知, 一维简单随机游动常返当且仅当它是对称的, 即 $p = q = 1 / 2$. 在这种情况下, 不难看出

$$
\mathbf {E} _ {0} (T _ {0}) = \sum_ {n = 0} ^ {\infty} n f _ {0 0} (n) = \frac {\mathrm{d}}{\mathrm{d} z} F _ {0 0} ^ {*} (1 -) = \infty .
$$

所以一维对称简单随机游动是零常返的.

## 4.3.3 闭集与状态分类

定义 4.3.3 称马氏链 X 或其转移矩阵 P 自  $i \in E$  可达  $j \in E$ ，是指存在  $n \geqslant 0$  使得  $p_{ij}(n) > 0$ ，此时写  $i \rightsquigarrow j$ 。称  $K \subseteq E$  为闭集，是指对一切  $i \in K$  和  $j \in K^{c}$  自 i 都不可达 j。称  $i \in E$  与  $j \in E$  互通，是指  $i \rightsquigarrow j$  且  $j \rightsquigarrow i$ ，此时写  $i \rightsquigarrow j$ 。若 E 中的任何两个状态都互通，则称 X 或 P 是不可约的。

若 $K \subseteq E$ 为闭集, 则 $(p_{ij}: i, j \in K)$ 是 $K$ 上的一个转移矩阵. 在这种情况下, 从 $K$ 中出发的链永远在该闭集中运动, 且以 $(p_{ij}: i, j \in K)$ 为转移矩阵. 另外, 显然 $X$ 是不可约的当且仅当没有 $E$ 的真子集是它的闭集.

命题 4.3.7 设  $i, j \in E$  且  $i \neq j$ ，则马氏链 X 自 i 可达 j 当且仅当存在 E 中的路径  $i = i_{0} \rightarrow i_{1} \rightarrow \cdots \rightarrow i_{n} = j$  满足  $p_{i_{0}i_{1}} p_{i_{1}i_{2}} \cdots p_{i_{n-1}i_{n}} > 0$ .

证明 由可达性的定义可知, 链 X 自 i 可达 j 的充要条件是存在  $n \geqslant 1$  使得

$$
p _ {i j} (n) = \sum_ {i _ {1} \in E} \sum_ {i _ {2} \in E} \dots \sum_ {i _ {n - 1} \in E} p _ {i i _ {1}} p _ {i _ {1} i _ {2}} \dots p _ {i _ {n - 1} j} > 0.
$$

上式成立当且仅当存在路径  $i = i_{0} \rightarrow i_{1} \rightarrow \cdots \rightarrow i_{n} = j$  满足  $p_{i_{0}i_{1}}p_{i_{1}i_{2}}\cdots p_{i_{n-1}i_{n}} > 0.$  □

命题 4.3.8 互通关系是 E 中的一个等价关系.

证明 显然互通关系是自反的和对称的. 若 $i \rightsquigarrow j$ 且 $j \rightsquigarrow k$, 则存在 $m, n \geqslant 0$, 使得 $p_{ij}(m)p_{jk}(n) > 0$. 于是

$$
p _ {i k} (m + n) = \sum_ {l \in E} p _ {i l} (m) p _ {l k} (n) \geqslant p _ {i j} (m) p _ {j k} (n) > 0.
$$

也就是说 $i \rightsquigarrow k$. 可见可达关系是传递的, 因而互通关系也是传递的. $\square$

由命题 4.3.8 可见, 我们可以把 E 按互通关系分类, 使同类中的状态都互通, 而不同类中的状态不互通.

定理 4.3.9 每个互通类都是闭集且同一个互通类中的状态有相同的常返或暂留性.

证明 显然, 每个互通类都是闭集. 假定 $i, j \in E$ 互通. 于是存在 $m, n \geqslant 0$ 使 $p_{ij}(m)p_{ji}(n) > 0$. 再注意

$$
\begin{array}{l} p _ {j j} ^ {*} \geqslant \sum_ {k = 0} ^ {\infty} p _ {j j} (k + m + n) = \sum_ {k = 0} ^ {\infty} \sum_ {p, q \in E} p _ {j p} (n) p _ {p q} (k) p _ {q j} (m) \\ \geqslant \sum_ {k = 0} ^ {\infty} p _ {j i} (n) p _ {i i} (k) p _ {i j} (m) = p _ {j i} (n) p _ {i j} (m) p _ {i i} ^ {*}, \\ \end{array}
$$

故 $p_{ii}^{*} = \infty$ 蕴涵 $p_{jj}^{*} = \infty$. 利用定理4.3.4知当 $i$ 常返时 $j$ 也常返. 再由对称性知当 $j$ 常返时 $i$ 也常返. $\square$

定理 4.3.10 设  $i \in E$  常返且  $i \rightsquigarrow j \in E$ ，则  $i \rightsquigarrow j$  且  $f_{ij}^{*} = f_{ji}^{*} = 1$ .

证明 因为 $i \rightsquigarrow j$, 存在 $n_0 \geqslant 0$ 使得 $p_{ij}(n_0) > 0$. 因 $i$ 常返, 利用定理4.3.1和马氏性有

$$
\begin{array}{l} 0 = \mathbf {P} _ {i} (X _ {n _ {0} + k} \neq i: k \geqslant 1) \\ \geqslant \mathbf {P} _ {i} (X _ {n _ {0}} = j, X _ {n _ {0} + k} \neq i: k \geqslant 1) \\ = p _ {i j} (n _ {0}) \mathbf {P} _ {i} (X _ {n _ {0} + k} \neq i: k \geqslant 1 | X _ {n _ {0}} = j) \\ = p _ {i j} (n _ {0}) (1 - f _ {j i} ^ {*}). \\ \end{array}
$$

所以

$$
f _ {j i} ^ {*} = \sum_ {k = 1} ^ {\infty} f _ {j i} (k) = 1,
$$

故存在 $k \geqslant 1$ 使 $0 < f_{ji}(k) \leqslant p_{ji}(k)$, 即 $j \rightsquigarrow i$. 这就证明了 $i \rightsquigarrow j$. 由定理4.3.9知 $j$ 也常返. 再由前面推导知 $f_{ij}^{*} = 1$. $\square$

根据上面的结论, 不难对 E 中的状态和 X 的运动情况作出如下分析: 将全部暂留态构成的集合记为 U, 再将所有常返态分解为至多可数个互通类  $H_{1}, H_{2}, \cdots$  这里每个