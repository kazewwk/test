# 第四章 离散时间马氏链

原始 PDF 第 93–124 页。

90

第四章 离散时间马氏链

马氏链是状态空间可数且满足马氏性的随机过程. 在本章里, 我们讨论离散时间马氏链的基本性质, 包括马氏性、强马氏性、常返性、暂留性、周期性、过份函数、常返链的游程等. 目的是帮助读者形成对于马氏过程的初步的直观认识, 为深入学习抽象马氏过程的理论打下基础.

## 4.1 马氏性及等价形式

设 E 是一个可数集, 默认装备了由其所有子集构成的  $\sigma$  代数 E. 对任何整数  $n \geqslant 1$  用  $E^{n}$  表示 E 的 n 重乘积空间. 定义于概率空间  $(\Omega, \mathcal{G}, \mathbf{P})$ , 取值于 E 的随机变量族  $(X_{n}: n = 0, 1, 2, \cdots)$  构成一个离散时间离散状态的随机过程. 为简单起见, 也写此过程为  $(X_{n})$  或  $(X_{n}: n \geqslant 0)$ .

## 4.1.1 简单马氏性

考虑概率空间 $(\Omega, \mathcal{G}, \mathbf{P})$ 上的 $\sigma$ 代数流 $(\mathcal{G}_n : n \geqslant 0)$, 也就是递增的 $\sigma$ 代数序列. 假定随机过程 $X = (X_n : n \geqslant 0)$ 关于此流是适应的, 即对于任意的 $n \geqslant 0$ 随机变量 $X_n$ 关于 $\sigma$ 代数 $\mathcal{G}_n$ 可测. 换言之, 对于任何 $B \subseteq E$ 有

$$
X _ {n} ^ {- 1} (B) = \{X _ {n} \in B \} := \{\omega \in \Omega : X _ {n} (\omega) \in B \} \in \mathcal {G} _ {n}. \tag {4.1.1}
$$

对于  $n \geqslant 0$  令  $\mathscr{F}_{n} = \sigma(X_{0}, X_{1}, \cdots, X_{n})$  是所有形如

$$
(X _ {0}, X _ {1}, \dots , X _ {n}) ^ {- 1} (A) = \{(X _ {0}, X _ {1}, \dots , X _ {n}) \in A \}, \tag {4.1.2}
$$

的集合构成的  $\Omega$  的  $\sigma$  代数, 其中  $A \subseteq E^{n+1}$ . 则  $(\mathcal{F}_{n}: n \geqslant 0)$  是 X 的自然  $\sigma$  代数流.

定义 4.1.1 称随机过程 X 关于其适应流  $(\mathcal{G}_{n})$  具有马氏性或称它是关于该流的马氏链, 是指对于任意的  $n \geqslant 0, i, j \in E$  和  $G \in G_{n}$ , 当  $\mathbf{P}(G \cap \{X_{n} = i\}) > 0$  时有

$$
\mathbf {P} (X _ {n + 1} = j | G \cap \{X _ {n} = i \}) = \mathbf {P} (X _ {n + 1} = j | X _ {n} = i). \tag {4.1.3}
$$

为便于理解, 我们以 (4.1.3) 式作为简单马氏性的定义, 它只用到初等条件概率. 本书后面的讨论大都基于这种表达形式. 马氏性也可用给定 $\sigma$ 代数的条件期望和条件概率进行表达. 这就是下面的:

定理 4.1.1 过程 X 关于其适应流  $(\mathcal{G}_{n})$  具有马氏性 (4.1.3) 的充要条件是对任意的  $n \geqslant 0$  和  $j \in E$  有

$$
\mathbf {P} (X _ {n + 1} = j | \mathcal {G} _ {n}) = \mathbf {P} (X _ {n + 1} = j | X _ {n}). \tag {4.1.4}
$$

---

4.1 马氏性及等价形式

91

证明 首先, 根据给定 $\sigma$ 代数的条件期望和条件概率的定义, 等式 (4.1.4) 等价于对于任何 $G \in \mathcal{G}_n$ 有

$$
\mathbf {P} (\{X _ {n + 1} = j \} \cap G) = \mathbf {E} [ \mathbf {P} (X _ {n + 1} = j | X _ {n}) 1 _ {G} ]. \tag {4.1.5}
$$

假设 (4.1.5) 式成立. 在该式中用 $G \cap \{X_{n} = i\}$ 替代 $G$ 得

$$
\begin{array}{l} \mathbf {P} (\{X _ {n + 1} = j \} \cap G \cap \{X _ {n} = i \}) = \mathbf {E} [ \mathbf {P} (X _ {n + 1} = j | X _ {n}) 1 _ {G \cap \{X _ {n} = i \}} ] \\ = \mathbf {E} [ \mathbf {P} (X _ {n + 1} = j | X _ {n} = i) 1 _ {G \cap \{X _ {n} = i \}} ] \\ = \mathbf {P} (G \cap \{X _ {n} = i \}) \mathbf {P} (X _ {n + 1} = j | X _ {n} = i). \\ \end{array}
$$

将上式两端同除以 $\mathbf{P}(G\cap \{X_n = i\})$ 即得(4.1.3)式.反之,假若 $X$ 满足(4.1.3)式,由可数可加性有

$$
\begin{array}{l} \mathbf {P} (\{X _ {n + 1} = j \} \cap G) = \sum_ {i \in E} \mathbf {P} (\{X _ {n + 1} = j \} \cap G \cap \{X _ {n} = i \}) \\ = \sum_ {i \in E} \mathbf {P} (G \cap \{X _ {n} = i \}) \mathbf {P} (X _ {n + 1} = j | G \cap \{X _ {n} = i \}) \\ = \sum_ {i \in E} \mathbf {P} (G \cap \{X _ {n} = i \}) \mathbf {P} (X _ {n + 1} = j | X _ {n} = i) \\ = \sum_ {i \in E} \mathbf {E} [ 1 _ {G \cap \{X _ {n} = i \}} \mathbf {P} (X _ {n + 1} = j | X _ {n} = i) ] \\ = \sum_ {i \in E} \mathbf {E} [ 1 _ {G \cap \{X _ {n} = i \}} \mathbf {P} (X _ {n + 1} = j | X _ {n}) ] \\ = \mathbf {E} [ 1 _ {G} \mathbf {P} (X _ {n + 1} = j | X _ {n}) ]. \\ \end{array}
$$

因此 (4.1.5) 式成立. □

显然, 若 $X$ 关于任何适应流 $(\mathcal{G}_n)$ 具有马氏性, 它关于自然流 $(\mathcal{F}_n)$ 具有马氏性. 后面若只是说 $X$ 是马氏链或说它具有马氏性而不指出具体的流, 则通常意味着该性质对于其自然流成立.

定理 4.1.2 过程 X 相对其自然流具有马氏性的充要条件是对于任意  $n \geqslant 0$  和  $\{i_{0}, i_{1}, \cdots, i_{n} = i, j\} \subseteq E$ ，当  $\mathbf{P}(X_{k} = i_{k} : 0 \leqslant k \leqslant n) > 0$  时有

$$
\mathbf {P} (X _ {n + 1} = j | X _ {k} = i _ {k}: 0 \leqslant k \leqslant n) = \mathbf {P} (X _ {n + 1} = j | X _ {n} = i). \tag {4.1.6}
$$

证明 假若 X 具有马氏性, 对于任何  $G \in F_{n}$ , 当  $\mathbf{P}(G \cap \{X_{n} = i\}) > 0$  时有 (4.1.3) 式成立, 从该式中取  $i = i_{n}$  和  $G = \{X_{k} = i_{k} : 0 \leqslant k \leqslant n\}$  即得 (4.1.6) 式. 反之, 假设对于任意的  $n \geqslant 0$  和  $\{i_{0}, i_{1}, \cdots, i_{n} = i, j\} \subseteq E$ , 当  $\mathbf{P}(X_{k} = i_{k} : 0 \leqslant k \leqslant n) > 0$  时有 (4.1.6) 式成立. 对于  $G \in F_{n}$ , 可取  $A \subseteq E^{n+1}$  使得

$$
G = \{(X _ {0}, X _ {1}, \dots , X _ {n}) \in A \} = \bigcup_ {(i _ {0}, i _ {1}, \dots , i _ {n}) \in A} \{X _ {k} = i _ {k}: 0 \leqslant k \leqslant n \}.
$$

---

92

第四章 离散时间马氏链

这样, 利用可数可加性和 (4.1.6) 式有

$$
\begin{array}{l} \mathbf {P} (\{X _ {n + 1} = j \} \cap G \cap \{X _ {n} = i \}) \\ = \sum_ {(i _ {0}, i _ {1}, \dots , i _ {n}) \in A} \mathbf {P} (\{X _ {n + 1} = j \} \cap \{X _ {k} = i _ {k}: 0 \leqslant k \leqslant n \} \cap \{X _ {n} = i \}) \\ = \sum_ {(i _ {0}, i _ {1}, \dots , i _ {n}) \in A} 1 _ {\{i _ {n} = i \}} \mathbf {P} (\{X _ {n + 1} = j \} \cap \{X _ {k} = i _ {k}: 0 \leqslant k \leqslant n \}) \\ = \sum_ {(i _ {0}, i _ {1}, \dots , i _ {n}) \in A} 1 _ {\{i _ {n} = i \}} \mathbf {P} (X _ {k} = i _ {k}: 0 \leqslant k \leqslant n) \mathbf {P} (X _ {n + 1} = j | X _ {n} = i) \\ = \sum_ {(i _ {0}, i _ {1}, \dots , i _ {n}) \in A} \mathbf {P} (\{X _ {k} = i _ {k}: 0 \leqslant k \leqslant n \} \cap \{X _ {n} = i \}) \mathbf {P} (X _ {n + 1} = j | X _ {n} = i) \\ = \mathbf {P} (G \cap \{X _ {n} = i \}) \mathbf {P} (X _ {n + 1} = j | X _ {n} = i). \\ \end{array}
$$

因此 (4.1.3) 式成立, 即 $X$ 相对其自然流具有马氏性. $\square$

(4.1.3) 式和 (4.1.6) 式用初等概率的方式分别给出了 X 关于一般适应流和自然流的马氏性的表达形式。由此可以看出，马氏性直观上意味着，在已知过程的现在 (时刻 n) 和过去 (时刻  $0,1,\cdots,n-1$ ) 的状态的情况下，将来的运动情况只和现在的状态  $X_{n}$  有关，而和过去的状态无关。

定理 4.1.3 设  $(X_{n}: n \geqslant 0)$  是关于流  $(\mathcal{G}_{n}: n \geqslant 0)$  的马氏链。再设对  $k \geqslant 0$  和  $A \in G_{k}$  有  $\mathbf{P}(A) > 0$ ，则在条件概率  $\mathbf{P}_{A} := \mathbf{P}(\cdot | A)$  之下  $(X_{k+n}: n \geqslant 0)$  具有关于流  $(\mathcal{G}_{k+n}: n \geqslant 0)$  的马氏性。

证明 取 $n \geqslant 0$ 和 $G \in \mathcal{G}_{k+n}$. 注意 $A \cap G \in \mathcal{G}_{k+n}$. 根据 $(X_n)$ 关于流 $(\mathcal{G}_n)$ 的马氏性, 对于 $i, j \in E$ 有

$$
\begin{array}{l} \mathbf {P} _ {A} (X _ {k + n + 1} = j | G \cap \{X _ {k + n} = i \}) = \mathbf {P} (X _ {k + n + 1} = j | A \cap G \cap \{X _ {k + n} = i \}) \\ = \mathbf {P} (X _ {k + n + 1} = j | X _ {k + n} = i) \\ = \mathbf {P} (X _ {k + n + 1} = j | A \cap \{X _ {k + n} = i \}) \\ = \mathbf {P} _ {A} (X _ {k + n + 1} = j | X _ {k + n} = i). \\ \end{array}
$$

因此, 在 $\mathbf{P}_A$ 之下 $(X_{k + n})$ 关于流 $(\mathcal{G}_{k + n})$ 具有马氏性. □

例 4.1.1 设  $\{\xi_{n}: n \geqslant 1\}$  是取值于  $Z^{d}$  的独立随机变量序列. 令  $X_{0}$  为取值于  $Z^{d}$  且与  $\{\xi_{n}: n \geqslant 1\}$  独立的随机变量. 令

$$
X _ {n} = X _ {0} + \sum_ {i = 1} ^ {n} \xi_ {i}, \quad n \geqslant 1. \tag {4.1.7}
$$

显然, 对  $n \geqslant 0$  及  $\{i_{0}, i_{1}, \cdots, i_{n} = i, j\} \subseteq Z^{d}$  有

$$
\mathbf {P} (X _ {n + 1} = j | X _ {n} = i) = \mathbf {P} (X _ {n + 1} = j | X _ {k} = i _ {k}: 0 \leqslant k \leqslant n)
$$

---

4.1 马氏性及等价形式

93

$$
= \mathbf {P} (\xi_ {n + 1} = j - i).
$$

所以 $(X_{n}:n\geqslant 0)$ 是以 $\mathbb{Z}^d$ 为状态空间的马氏链.特别地,若随机变量序列 $\{\xi_n:n\geqslant 1\}$ 具有相同的分布,则 $(X_{n}:n\geqslant 0)$ 就是前面讨论过的 $d$ 维随机游动.在一般情况下,有些文献中也称 $(X_{n}:n\geqslant 0)$ 为(非时齐)随机游动.

例 4.1.2 设  $(\eta_{n}: n \geqslant 1)$  是取值于  $Z_{+}$  的独立随机变量序列. 令  $Y_{0} = 0$  并对  $n \geqslant 1$  依次定义  $Y_{n+1} = (Y_{n} - 1) \vee 0 + \eta_{n+1}$ . 则  $(Y_{n}: n \geqslant 0)$  是以  $Z_{+}$  为状态空间的马氏链. 对任何  $n \geqslant 0$  及  $i, j \in Z_{+}$  有

$$
\mathbf {P} (Y _ {n + 1} = j | Y _ {n} = i) = \left\{ \begin{array}{l l} \mathbf {P} (\eta_ {n + 1} = j), & i = 0, \\ \mathbf {P} (\eta_ {n + 1} = j - i + 1), & i \geqslant 1. \end{array} \right.
$$

该链描述了某个服务系统的排队人数随时间的变化情况.

例 4.1.3 某产品专营电商每日的销售量为取值于  $Z_{+}$  的独立随机变量. 该电商仓库进货规则是: 取定  $1 \leqslant m < M \in Z_{+}$ , 若营业结束时库存量未达到 m 件, 则当晚将货量补充到 M; 若库存量达到 m 件, 则无需补货. 分别用  $\xi_{n}$  和  $Z_{n}$  表示第 n 天的销售量和补货前的库存量. 设  $Z_{0} = 0$ . 注意

$$
Z _ {n + 1} = \left\{ \begin{array}{l l} (M - \xi_ {n + 1}) _ {+}, & Z _ {n} <   m, \\ (Z _ {n} - \xi_ {n + 1}) _ {+}, & Z _ {n} \geqslant m. \end{array} \right.
$$

易证 $(Z_{n}:n\geqslant0)$ 是以 $Z_{+}$ 为状态空间的马氏链.

## 4.1.2 条件独立性

本小节给出马氏性的另外几种等价形式. 我们将会看到, 由 (4.1.3) 式定义的马氏性实际上等价于某种条件独立性, 这从另外一个角度给出了马氏性的解释. 为了简化叙述, 我们约定: 在遇到古典条件概率时, 只需考虑作为条件的事件的概率非零的情况.

定理 4.1.4 过程 X 关于流  $(\mathcal{G}_{n})$  具有马氏性 (4.1.3) 的充要条件是对于任意的  $n \geqslant 0, k \geqslant 1, \{i, j_{1}, j_{2}, \cdots, j_{k}\} \subseteq E$  和  $G \in G_{n}$  有

$$
\begin{array}{l} \mathbf {P} (X _ {n + 1} = j _ {1}, X _ {n + 2} = j _ {2}, \dots , X _ {n + k} = j _ {k} | G \cap \{X _ {n} = i \}) \\ = \mathbf {P} (X _ {n + 1} = j _ {1}, X _ {n + 2} = j _ {2}, \dots , X _ {n + k} = j _ {k} | X _ {n} = i). \tag {4.1.8} \\ \end{array}
$$

证明 若 (4.1.8) 式成立, 取 $k = 1$ 即知 (4.1.3) 式成立. 反之, 假设 (4.1.3) 式成立, 下面用数学归纳法证明 (4.1.8) 式成立. 显然该式对 $k = 1$ 和任意 $n \geqslant 0$ 成立. 现假设 (4.1.8) 式对某个 $k \geqslant 1$ 和任意 $n \geqslant 0$ 成立. 对于 $j_{k+1} \in E$, 记 $H = \{X_{n+2} = j_2, X_{n+3} =$

---

94

第四章 离散时间马氏链

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

---

4.1 马氏性及等价形式

95

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

---

96

第四章 离散时间马氏链

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

---

4.2 转移矩阵

97

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

---

98

第四章 离散时间马氏链

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

---

4.2 转移矩阵

99

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

---

100

第四章 离散时间马氏链

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

---

4.2 转移矩阵

101

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

---

102

第四章 离散时间马氏链

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

---

4.3 状态的分类

103

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

---

104

第四章 离散时间马氏链

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

---

4.3 状态的分类

105

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

---

106

第四章 离散时间马氏链

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

---

4.3 状态的分类

107

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

---

108

第四章 离散时间马氏链

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

---

4.3 状态的分类

109

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

---

110

第四章 离散时间马氏链

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

定义 4.3.4 对于 $i \in E$, 若集合 $\{n \geqslant 1 : p_{ii}(n) > 0\}$ 非空, 就称它的最大公约数 $d$ 为 $i$ 的周期. 当 $d \geqslant 2$ 时称 $i$ 是周期的; 当 $d = 1$ 时称 $i$ 是非周期的. 若 $E$ 中的所有

---

4.3 状态的分类

111

状态都是非周期的, 则称 X 或 P 是非周期的.

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

---

112

第四章 离散时间马氏链

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

---

4.3 状态的分类

113

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

证明 沿用定理4.3.15的证明中的记号. 设 $P$ 是暂留的. 注意对 $k \neq j$ 有 $\mathbf{P}_k (T < \infty) = \mathbf{P}_k (\tau < \infty)$. 所以由(4.3.12)式定义的函数 $f$ 就给出(4.3.13)式的一个非常数的

---

114

第四章 离散时间马氏链

有界解. 反之, 假若 (4.3.13) 式有非常数有界解 $\{y_{i}: i \in E\}$, 因常函数是该方程组的解, 我们可假定 $\{y_{i}: i \in E\}$ 由非负数构成. 令

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

---

4.4 马氏链的游程

115

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

---

116

第四章 离散时间马氏链

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

证明 显然 $\phi_0$ 是以 $P^b$ 为转移矩阵的马氏链. 根据强马氏性, 在条件概率 $\mathbf{P}(\cdot|\sigma_k < \infty) = \mathbf{P}(\cdot|\sigma_k < \infty, X_{\sigma_k} = b)$ 之下 $\{X(\sigma_k + n): n \geqslant 0\}$ 是从 $b$ 出发以 $P$ 为转移矩阵的马氏链且与 $\{X(n \wedge \sigma_k): n \geqslant 0\}$ 独立. 类似地, 对 $k \geqslant 1$ 在条件概率 $\mathbf{P}(\cdot|\tau_k < \infty) =$

---

4.4 马氏链的游程

117

$\mathbf{P}(\cdot|\tau_k < \infty, X_{\tau_k} = a)$ 之下 $\{X(\tau_k + n): n \geqslant 0\}$ 是从 $a$ 出发以 $P$ 为转移矩阵的马氏链且与 $\{X(n \wedge \tau_k): n \geqslant 0\}$ 独立. 由 $X$ 的不可约性和常返性, 有

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

---

118

第四章 离散时间马氏链

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

---

4.4 马氏链的游程

119

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

---

120

第四章 离散时间马氏链

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

---

4.4 马氏链的游程

121

2. 求从 1 出发的一维简单随机游动的第一个由 1 到 0 的游程 $e = \{e(n) : n \geqslant 0\}$ 的高度 $\sup_{n \geqslant 0} e(n)$ 的分布.

3. 证明: 当 $0 < p \leqslant q$ 时具有转移矩阵 $Q_{+}^{a}$ 的反射随机游动是常返的; 当 $p \geqslant q > 0$ 时具有转移矩阵 $Q_{-}^{a}$ 的反射随机游动是常返的.

4. 给出推论 4.4.3 的直接证明.

提示: 参考定理 4.4.2 的证明.

5. 给出 $\mathbb{Z}_{+} \times \mathbb{Z}$ 上的以 $\{0\} \times \mathbb{Z}$ 为反射面的简单对称随机游动的定义, 并给出该游动的构造.

提示: 利用定理 4.4.2 和推论 4.4.3 的结论.
