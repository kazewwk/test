## A.1 可测集与单调类

给定可测空间 $(\Omega, \mathcal{F})$，即 $\mathcal{F}$ 为非空集 $\Omega$ 上的 $\sigma$ 代数，我们称 $\mathcal{F}$ 中的集合为可测集。为了深入讨论集合的可测性，我们需要引入集代数和单调类的概念。

## A.1.1 集代数

定义 A.1.1 设 $\mathcal{A}$ 是非空集 $\Omega$ 的子集类. 如果下面的性质成立:

(i) $\Omega \in \mathcal{A}$;
(ii) 若 $A \in \mathcal{A}$, 则 $A^c \in \mathcal{A}$;
(iii) 若 $A, B \in \mathscr{A}$, 则 $A \cup B \in \mathscr{A}$,

那么称 $\mathcal{A}$ 为 $\Omega$ 上的集代数.

下面的几个结论显然成立.

命题 A.1.1 非空集  $\Omega$  的子集类 A 是集代数的充要条件是定义 A.1.1 中的 (i), (ii) 和下面的性质成立: (iii)' 若  $A, B \in A$ , 则  $A \cap B \in A$ .

推论 A.1.2 集代数 A 具有下面的性质:(v) 若  $A_{1}, A_{2}, \cdots, A_{n} \in A$ ，则有  $\bigcup_{k=1}^{n} A_{k} \in A$  和  $\bigcap_{k=1}^{n} A_{k} \in A$ .

命题 A.1.3 非空集  $\Omega$  的子集类 A 是集代数的充要条件是定义 A.1.1 中的 (i) 和下面的性质成立: (vi) 若  $A, B \in A$ , 则  $A \setminus B \in A$ .

## A.1.2 单调类定理

定义 A.1.2 设 M 是非空集  $\Omega$  的子集类. 如果下面的性质成立:

(i) 若序列 $\{A_k\} \subseteq \mathcal{M}$ 单调不降, 则 $\bigcup_{k=1}^{\infty} A_k \in \mathcal{M}$;
(ii) 若序列 $\{A_k\} \subseteq \mathcal{M}$ 单调不增, 则 $\bigcap_{k=1}^{\infty} A_k \in \mathcal{M}$,

那么称 M 为  $\Omega$  上的单调类.

显然  $\sigma$  代数是单调类.

命题 A.1.4 若 F 既是集代数又是单调类, 则它是  $\sigma$  代数.

证明 只需证明 $\mathcal{F}$ 对可数并封闭. 设 $A_{1}, A_{2}, \cdots \in \mathcal{F}$. 由于 $\mathcal{F}$ 是集代数, 对任意 $n \geqslant 1$ 有 $B_{n} := \bigcup_{k=1}^{n} A_{k} \in \mathcal{F}$. 显然 $\{B_{n}\}$ 不降. 再因 $\mathcal{F}$ 是单调类, 有 $\bigcup_{k=1}^{\infty} A_{k} = \bigcup_{k=1}^{\infty} B_{k} \in \mathcal{F}$.

命题 A.1.5 设  $\{\mathcal{M}_{\alpha} : \alpha \in J\}$  是  $\Omega$  上的一族单调类, 其中 J 为指标集. 则  $\bigcap_{\alpha \in J} M_{\alpha}$  也是  $\Omega$  上的单调类.

证明 因为每个集类 $\mathcal{M}_{\alpha}$ 都满足定义A.1.2中的性质(i)和(ii)，易证 $\mathcal{M}$ 也满足这两个性质. □

给定 $\Omega$ 的子集类 $\mathcal{G}$, 令 $m(\mathcal{G}) = \cap \{\mathcal{M} : \mathcal{M}$ 为 $\Omega$ 上的单调类且 $\mathcal{M} \supseteq \mathcal{G}\}$. 由命题 A.1.5 知 $m(\mathcal{G})$ 是单调类, 称为由 $\mathcal{G}$ 生成的单调类. 它是 $\Omega$ 上的包含 $\mathcal{G}$ 的最小的单调类. 特别地, 若 $\mathcal{G}$ 本身就是单调类, 则 $\mathcal{G} = m(\mathcal{G})$. 以下固定 $\Omega$ 的集类 $\mathcal{A}$, 并对 $A \subseteq \Omega$ 记 $\mathcal{M}_A = \{B \subseteq \Omega : A \setminus B, B \setminus A \in m(\mathcal{A})\}$. 则对于 $A, B \subseteq \Omega$ 有 $B \in \mathcal{M}_A$ 当且仅当 $A \in \mathcal{M}_B$.

引理 A.1.6 若 A 是集代数, 则  $M_{A}$  是单调类.

证明 设 $\{B_k\} \subseteq \mathcal{M}_A$ 不降. 由 $\mathcal{M}_A$ 的定义, 对每个 $k \geqslant 1$ 有 $A \setminus B_k, B_k \setminus A \in m(\mathscr{A})$. 注意

$$
B _ {1} \setminus A \subseteq B _ {2} \setminus A \subseteq \dots \quad \text {和} \quad A \setminus B _ {1} \supseteq A \setminus B _ {2} \supseteq \dots .
$$

因 $m(\mathcal{A})$ 是单调类, 有

$$
A \setminus \left(\bigcup_ {k = 1} ^ {\infty} B _ {k}\right) = A \cap \left(\bigcap_ {k = 1} ^ {\infty} B _ {k} ^ {c}\right) = \bigcap_ {k = 1} ^ {\infty} (A \setminus B _ {k}) \in m (\mathscr {A})
$$

和

$$
\Big (\bigcup_ {k = 1} ^ {\infty} B _ {k} \Big) \setminus A = \Big (\bigcup_ {k = 1} ^ {\infty} B _ {k} \Big) \cap A ^ {c} = \bigcup_ {k = 1} ^ {\infty} (B _ {k} \setminus A) \in m (\mathscr {A}).
$$

这就证明了 $\bigcup_{k=1}^{\infty} B_k \in \mathcal{M}_A$. 类似地, 若 $\{B_k\} \subseteq \mathcal{M}_A$ 单调不增, 则 $\bigcap_{k=1}^{\infty} B_k \in \mathcal{M}_A$. 所以 $\mathcal{M}_A$ 是单调类. □

定理A.1.7（单调类定理） 设 $\mathcal{A}$ 为集代数. 则 $m(\mathcal{A}) = \sigma(\mathcal{A})$.

证明 显然 $\sigma(\mathcal{A})$ 是单调类, 故有 $\sigma(\mathcal{A}) \supseteq m(\mathcal{A})$. 为证 $m(\mathcal{A}) \supseteq \sigma(\mathcal{A})$, 只需证明 $m(\mathcal{A})$ 是 $\sigma$ 代数. 由单调类的定义, 为此只需证明对任何 $A, B \in m(\mathcal{A})$ 有 $A \setminus B, B \setminus A \in m(\mathcal{A})$. 当 $A \in \mathcal{A}$ 时, 因 $\mathcal{A}$ 是集代数, 对 $B \in \mathcal{A}$ 有 $A \setminus B, B \setminus A \in \mathcal{A}$, 故 $B \in \mathcal{M}_A$. 于是 $\mathcal{M}_A \supseteq \mathcal{A}$. 由引理 A.1.6 知 $\mathcal{M}_A$ 是单调类, 故 $\mathcal{M}_A \supseteq m(\mathcal{A})$. 这样, 当 $B \in m(\mathcal{A})$ 时有 $B \in \mathcal{M}_A$, 故 $A \in \mathcal{M}_B$. 于是 $\mathcal{M}_B \supseteq \mathcal{A}$. 再由引理 A.1.6 知 $\mathcal{M}_B$ 是单调类, 故 $\mathcal{M}_B \supseteq m(\mathcal{A})$. 后者说明当 $A \in m(\mathcal{A})$ 时有 $A \in \mathcal{M}_B$, 故 $A \setminus B, B \setminus A \in m(\mathcal{A})$. 这就证明了对任何 $A, B \in m(\mathcal{A})$ 有 $A \setminus B, B \setminus A \in m(\mathcal{A})$.

## A.1.3 邓肯类定理

定义 A.1.3 设 D 是非空集  $\Omega$  的子集类. 如果下面的性质成立:

(i) $\Omega \in \mathcal{D}$;
(ii) 若 $A, B \in \mathcal{D}$ 且 $A \subseteq B$, 则 $B \setminus A \in \mathcal{D}$;
(iii) 若序列  $\{A_{k}\} \subseteq D$  单调不降, 则  $\bigcup_{k=1}^{\infty} A_{k} \in D$ ,

那么称 $\mathcal{D}$ 为 $\Omega$ 上的邓肯 (Dynkin) 类.

给定 $\Omega$ 的子集类 $\mathcal{G}$, 令 $d(\mathcal{G}) = \cap \{\mathcal{D}: \mathcal{D}$ 为 $\Omega$ 上的邓肯类且 $\mathcal{D} \supseteq \mathcal{G}\}$. 则 $d(\mathcal{G})$ 是包含 $\mathcal{G}$ 的最小的邓肯类, 称为由 $\mathcal{G}$ 生成的邓肯类. 以下固定 $\Omega$ 的集类 $\mathcal{C}$, 并对 $A \subseteq \Omega$ 记 $\mathcal{D}_A = \{B \in d(\mathcal{C}): A \cap B \in d(\mathcal{C})\}$. 则对于 $A, B \in d(\mathcal{C})$ 有 $B \in \mathcal{D}_A$ 当且仅当 $A \in \mathcal{D}_B$.

引理A.1.8 设 $\mathcal{C}$ 对交运算封闭. 则对 $A \in d(\mathcal{C})$ 集类 $\mathcal{D}_A$ 是邓肯类.

证明 显然 $\Omega \in \mathcal{D}_A$，即定义 A.1.3 中的性质 (i) 成立。设 $B, C \in \mathcal{D}_A$ 且 $B \subseteq C$。根据 $\mathcal{D}_A$ 的定义，有 $B, C \in d(\mathcal{C})$ 且 $A \cap B, A \cap C \in d(\mathcal{C})$。因 $d(\mathcal{C})$ 是邓肯类，有 $C \setminus B \in d(\mathcal{C})$ 和 $A \cap (C \setminus B) = (A \cap C) \setminus (A \cap B) \in d(\mathcal{C})$，故 $C \setminus B \in \mathcal{D}_A$。因此定义 A.1.3 中的性质 (ii) 成立。再设 $\{B_k\} \subseteq \mathcal{D}_A$ 单调不降。根据 $\mathcal{D}_A$ 的定义，对每个 $k \geqslant 1$ 有 $B_k \in d(\mathcal{C})$ 且 $A \cap B_k \in d(\mathcal{C})$。因 $d(\mathcal{C})$ 是邓肯类，有 $\bigcup_{k} B_k \in d(\mathcal{C})$ 和 $A \cap \left(\bigcup_{k} B_k\right) = \bigcup_{k} (A \cap B_k) \in d(\mathcal{C})$，故 $\bigcup_{k} B_k \in \mathcal{D}_A$。因此定义 A.1.3 中的性质 (iii) 成立。

定理 A.1.9 (邓肯类定理) 设 C 对交运算封闭. 则  $d(\mathcal{C}) = \sigma(\mathcal{C})$ .

证明 因为 $\sigma(\mathcal{C})$ 是邓肯类, 所以有 $d(\mathcal{C}) \subseteq \sigma(\mathcal{C})$. 为证 $d(\mathcal{C}) \supseteq \sigma(\mathcal{C})$, 只需证明 $d(\mathcal{C})$ 是 $\sigma$ 代数. 由邓肯类的定义, 为此只需证明 $d(\mathcal{C})$ 对交运算封闭. 当 $A \in \mathcal{C}$ 时, 显然 $\mathcal{D}_A \supseteq \mathcal{C}$. 由引理 A.1.8 知 $\mathcal{D}_A$ 是邓肯类, 故 $\mathcal{D}_A \supseteq d(\mathcal{C})$. 这样, 当 $B \in d(\mathcal{C})$ 时有 $B \in \mathcal{D}_A$, 故 $A \in \mathcal{D}_B$. 于是 $\mathcal{D}_B \supseteq \mathcal{C}$. 再由引理 A.1.8 知 $\mathcal{D}_B$ 是邓肯类, 故 $\mathcal{D}_B \supseteq d(\mathcal{C})$. 后者说明当 $A \in d(\mathcal{C})$ 时有 $A \in \mathcal{D}_B$, 故 $A \cap B \in d(\mathcal{C})$. 这就证明了对任何 $A, B \in d(\mathcal{C})$ 都有 $A \cap B \in d(\mathcal{C})$, 即 $d(\mathcal{C})$ 对交运算封闭. □

在很多时候, 经常把定理 A.1.7 和定理 A.1.9 通称为单调类定理, 参见 [3, pp.496-497] 或 [13, pp.13-14].

## A.2 抽象测度的积分

固定一个 $\sigma$ 有限测度空间 $(\Omega, \mathcal{F}, \mu)$. 若 $f$ 为此空间上的实值可测函数, 我们写 $f \in \mathcal{F}$; 若 $f$ 为非负实值可测函数, 写 $f \in \mathcal{F}^{+}$. 本节将按照简单函数、非负可测函数、实值可测函数的顺序, 依次给出抽象测度积分的定义并讨论其若干基本性质.

## A.2.1 非负简单函数的积分

我们称 $(\Omega, \mathcal{F}, \mu)$ 上的某个实值可测函数为简单函数，是指它只有有限多可能的取值。用 $\mathcal{S}$ 表示所有简单函数构成的集合，用 $\mathcal{S}^{+}$ 表示所有非负简单函数构成的集合。显然，每个函数 $f \in \mathcal{S}^{+}$ 都可以表示为

$$
f (\omega) = \sum_ {i = 1} ^ {m} a _ {i} 1 _ {A _ {i}} (\omega), \quad \omega \in \Omega , \tag {A.2.1}
$$

其中 $a_1, a_2, \dots, a_m \in \mathbb{R}_+$ 而 $A_1, A_2, \dots, A_m \in \mathcal{F}$ 为 $\Omega$ 的有限划分, 即当 $i \neq j$ 时有 $A_i A_j = \varnothing$ 且 $\bigcup_{i=1}^{m} A_i = \Omega$. 上式意味着, 函数 $f$ 在集合 $A_i$ 上取 $a_i$ 值.

定义A.2.1 对于由(A.2.1)式给出的 $f\in \mathcal{S}^{+}$ ，我们定义其关于测度 $\mu$ 的积分为

$$
\mu (f) := \int_ {\Omega} f (\omega) \mu (\mathrm{d} \omega) = \sum_ {i = 1} ^ {m} a _ {i} \mu (A _ {i}). \tag {A.2.2}
$$

引理A.2.1 等式(A.2.2)右端的值与 $f\in \mathcal{S}^{+}$ 的形如(A.2.1)的表达式的选取无关.

证明 假设函数 $f \in \mathcal{S}^{+}$ 还可以表示为

$$
f (\omega) = \sum_ {j = 1} ^ {n} b _ {j} 1 _ {B _ {j}} (\omega), \quad \omega \in \Omega ,
$$

其中 $b_{1}, b_{2}, \cdots, b_{n} \in \mathbb{R}_{+}$ 而 $B_{1}, B_{2}, \cdots, B_{n} \in \mathcal{F}$ 为 $\Omega$ 的有限划分. 若 $A_{i}B_{j} \neq \varnothing$, 显然有 $a_{i} = b_{j}$. 由测度的可加性得

$$
\begin{array}{l} \sum_ {i = 1} ^ {m} a _ {i} \mu \left(A _ {i}\right) = \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} a _ {i} \mu \left(A _ {i} B _ {j}\right) \\ = \sum_ {j = 1} ^ {n} \sum_ {i = 1} ^ {m} b _ {j} \mu (A _ {i} B _ {j}) = \sum_ {j = 1} ^ {n} b _ {j} \mu (B _ {j}). \\ \end{array}
$$

所以 (A.2.2) 式右端的值与 $f \in \mathcal{S}^{+}$ 的表达式的选取无关.

命题 A.2.2 若 $f, g \in \mathcal{S}^{+}$ 满足 $f \stackrel{\mathrm{a.e.}}{=} g$, 则有 $\mu(f) = \mu(g)$.

证明 不妨设 $f \in \mathcal{S}^{+}$ 有表达式 (A.2.1), 而 $g$ 有表达式

$$
g (\omega) = \sum_ {j = 1} ^ {n} b _ {j} 1 _ {B _ {j}} (\omega), \quad \omega \in \Omega ,
$$

其中  $b_{1}, b_{2}, \cdots, b_{n} \in R_{+}$  而  $B_{1}, B_{2}, \cdots, B_{n} \in F$  为  $\Omega$  的有限划分，故 f, g 有表达式

$$
f (\omega) = \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} a _ {i} 1 _ {A _ {i} B _ {j}} (\omega), \quad g (\omega) = \sum_ {j = 1} ^ {n} \sum_ {i = 1} ^ {m} b _ {j} 1 _ {A _ {i} B _ {j}} (\omega).
$$

注意在集合 $A_{i}B_{j}$ 上有 $f = a_{i}$ 和 $g = b_{j}$. 由假设 $f \stackrel{\mathrm{a.e.}}{=} g$, 故当 $\mu(A_{i}B_{j}) \neq 0$ 必有 $a_{i} = b_{j}$. 基于上面的表达式, 应用引理 A.2.1 即知 $\mu(f) = \mu(g)$. □

命题 A.2.3 非负简单函数的积分具有如下性质:

(1) 对任意的 $A \in \mathcal{F}$ 有 $\mu(1_A) = \mu(A)$;
(2) 对任意的 $f \in \mathcal{S}^{+}$ 有 $\mu(f) \geqslant 0$;
(3) 对任意的 $a \geqslant 0$ 和 $f \in \mathcal{S}^{+}$ 有 $af \in \mathcal{S}^{+}$ 且 $\mu(af) = a\mu(f)$;
(4) 对任意的 $f, g \in \mathcal{S}^{+}$ 有 $f + g \in \mathcal{S}^{+}$ 且 $\mu(f + g) = \mu(f) + \mu(g)$;
(5) 若 $f, g \in \mathcal{S}^{+}$ 且 $f \leqslant g$, 则 $\mu(f) \leqslant \mu(g)$.

证明 性质 (1),(2),(3) 显然.

为证 (4), 设 $f \in \mathcal{S}^{+}$ 取值于有限集 $\{a_{1}, a_{2}, \cdots, a_{m}\} \subseteq \mathbb{R}_{+}$, 而 $g \in \mathcal{S}^{+}$ 取值于有限集 $\{b_{1}, b_{2}, \cdots, b_{n}\} \subseteq \mathbb{R}_{+}$. 则 $\{f = a_{i}, g = b_{j}\}, i = 1, 2, \cdots, m, j = 1, 2, \cdots, n$ 构成 $\Omega$ 的划分, 且

$$
f (\omega) + g (\omega) = \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} (a _ {i} + b _ {j}) 1 _ {\{f = a _ {i}, g = b _ {j} \}} (\omega).
$$

因此 $f + g\in \mathcal{S}^{+}$ 且有

$$
\begin{array}{l} \mu (f + g) = \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} (a _ {i} + b _ {j}) \mu (f = a _ {i}, g = b _ {j}) \\ = \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} a _ {i} \mu (f = a _ {i}, g = b _ {j}) + \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} b _ {j} \mu (f = a _ {i}, g = b _ {j}) \\ = \sum_ {i = 1} ^ {m} a _ {i} \mu (f = a _ {i}) + \sum_ {j = 1} ^ {n} b _ {j} \mu (g = b _ {j}) = \mu (f) + \mu (g). \\ \end{array}
$$

即性质 (4) 成立. 类似地, 可以证明性质 (5) 成立.

## A.2.2 非负可测函数的积分

定义A.2.2 对于非负可测函数 $f\in \mathcal{F}^{+}$ ，我们定义其相对于 $\mu$ 的积分为

$$
\mu (f) := \int_ {\Omega} f (\omega) \mu (\mathrm{d} \omega) = \sup \big \{\mu (g): g \in \mathscr {S} ^ {+}, g \leqslant f \big \}. \tag {A.2.3}
$$

若  $\mu(f)<\infty,$  则称 f 可积.

命题 A.2.4 若  $f, g \in F^{+}$  满足  $f \leqslant g$  (a.e.), 则有  $\mu(f) \leqslant \mu(g)$ .

证明 根据 $\mu(f)$ 的定义, 存在序列 $\{f_n\} \in \mathscr{S}^+$ 满足 $f_n \leqslant f$ 且 $\mu(f_n) \uparrow \mu(f)$. 令 $g_n = f_n 1_{\{f \leqslant g\}}$. 显然 $\{g_n\} \in \mathscr{S}^+$. 因 $\{g_n \neq f_n\} \subseteq \{f > g\}$, 有 $\mu(\{g_n \neq f_n\}) \leqslant \mu(\{f > g\}) = 0$, 故 $f_n \stackrel{\text{a.e.}}{=} g_n$. 由命题 A.2.2 有 $\mu(f_n) = \mu(g_n)$. 另外, 对任何 $\omega \in \Omega$, 当 $f(\omega) > g(\omega)$ 时有 $g_n(\omega) = 0 \leqslant g(\omega)$, 而当 $f(\omega) \leqslant g(\omega)$ 时有 $g_n(\omega) = f_n(\omega) \leqslant f(\omega) = g(\omega)$,即在全空间 $\Omega$ 上有 $g_{n} \leqslant g$. 由定义 A.2.2 有 $\mu(g_{n}) \leqslant \mu(g)$, 进而 $\mu(f) = \lim_{n \to \infty} \mu(f_{n}) = \lim_{n \to \infty} \mu(g_{n}) \leqslant \mu(g)$.

推论A.2.5 若 $f, g \in \mathcal{F}^{+}$ 满足 $f \stackrel{\mathrm{a.e.}}{=} g$, 则有 $\mu(f) = \mu(g)$.

定理A.2.6 设 $f \in \mathcal{F}^{+}$. 则 $f \stackrel{\mathrm{a.e.}}{=} 0$ 当且仅当 $f$ 可积且 $\mu(f) = 0$.

证明 “$\Rightarrow$” 由推论 A.2.5 显然.

“$\Leftarrow$”假设 $\mu(f) = 0$. 对于 $k \geqslant 1$, 根据命题 A.2.4 有

$$
0 = \mu (f) \geqslant \mu (f 1 _ {\{f > 1 / k \}}) \geqslant \mu (k ^ {- 1} 1 _ {\{f > 1 / k \}}) \geqslant k ^ {- 1} \mu (f > 1 / k),
$$

故 $\mu (f > 1 / k) = 0$ .由测度的下连续性，得

$$
\mu (f > 0) = \mu \bigg (\bigcup_ {k = 1} ^ {\infty} \{f > 1 / k \} \bigg) = \lim _ {k \to \infty} \mu (f > 1 / k) = 0.
$$

定理 A.2.7（单调收敛定理）设  $f, f_{1}, f_{2}, \cdots \in F^{+}$  满足  $f_{n} \uparrow f$  (a.e.). 则有  $\mu(f_{n}) \uparrow \mu(f)$ .

证明 基于推论 A.2.5, 我们不妨假定在全空间 $\Omega$ 上 $\{f_n\} \subseteq \mathcal{F}^+$ 处处不降且 $f_n \to f$ 处处成立. 由定义 A.2.2 知 $\mu(f_n)$ 关于 $n \geqslant 1$ 不降且 $\mu(f_n) \leqslant \mu(f)$, 故 $\lim_{n \to \infty} \mu(f_n) \leqslant \mu(f)$. 另一方面, 取 $0 < a < 1$ 和 $g \in \mathcal{S}^+$ 满足 $g \leqslant f$. 令 $A_n = \{f_n \geqslant ag\}$. 则 $A_n^c = \{f_n < ag\}$. 对任何 $\omega \in \Omega$, 当 $f(\omega) = 0$ 时有 $ag(\omega) = 0$, 进而 $\omega \notin A_n^c$; 当 $f(\omega) > 0$ 时有 $ag(\omega) < f(\omega)$, 故当 $n$ 充分大时 $f_n(\omega) > ag(\omega)$, 进而 $\omega \notin A_n^c$. 这说明 $A_n^c \downarrow \varnothing$. 注意 $C := \max_{\omega \in \Omega} g(\omega) < \infty$. 因为 $g1_{A_n^c} \leqslant C1_{A_n^c}$, 根据命题 A.2.4 有

$$
0 \leqslant \mu (g 1 _ {A _ {n} ^ {c}}) \leqslant \mu (C 1 _ {A _ {n} ^ {c}}) = C \mu (A _ {n} ^ {c}) \rightarrow 0 \quad (n \rightarrow \infty), \tag {A.2.4}
$$

其中最后的极限是因为测度的上连续性. 再注意 $f_{n} \geqslant f_{n}1_{A_{n}} \geqslant ag1_{A_{n}}$, 故有

$$
\mu (f _ {n}) \geqslant \mu (f _ {n} 1 _ {A _ {n}}) \geqslant \mu (a g 1 _ {A _ {n}}) = a \mu (g 1 _ {A _ {n}}) = a \big [ \mu (g) - \mu (g 1 _ {A _ {n} ^ {c}}) \big ],
$$

其中的等号是基于命题A.2.3.在上式中依次令 $n\to \infty$ 和 $a\to 1,$ 并应用(A.2.4)式得$\mu (f)\geqslant \lim_{n\to \infty}\mu (f_n)\geqslant \mu (g),$ 再对 $g$ 取上确界得 $\mu (f)\geqslant \lim_{n\to \infty}\mu (f_n)\geqslant \mu (f).$ 故得欲证等式.

在关于可测函数的积分的讨论中, 经常会使用简单函数逼近一般可测函数的方法. 为了方便表述, 对于整数 $n \geqslant 1$, 令

$$
\phi_ {n} (x) = n 1 _ {\{x \geqslant n \}} + \sum_ {k = 1} ^ {n 2 ^ {n}} 2 ^ {- n} (k - 1) 1 _ {\{[ (k - 1) / 2 ^ {n}, k / 2 ^ {n}) \}} (x), \quad x \geqslant 0. \tag {A.2.5}
$$

显然, 对任意的 $x \geqslant 0$ 有 $\phi_n(x) \uparrow x$. 若 $f$ 为非负可测函数, 则 $f_n := \phi_n \circ f \in \mathcal{S}^+$ 且 $f_n \uparrow f$. 由单调收敛定理知 $\mu(f_n) \uparrow \mu(f)$. 所以 (A.2.3) 式相当于通过分割函数 $f$ 的值域来逼近积分 $\mu(f)$, 这与黎曼积分中通过分割函数的定义域来逼近积分的思想有本质的不同.

## A.2.3 实值可测函数的积分

定义A.2.3 对于一般的实值可测函数 $f \in \mathcal{F}$, 定义非负可测函数 $f^{+} = f1_{\{f > 0\}}$ 和 $f^{-} = -f1_{\{f < 0\}}$. 注意 $f = f^{+} - f^{-}$. 若 $\mu(f^{+}) < \infty$ 或 $\mu(f^{-}) < \infty$, 则称 $f$ 关于 $\mu$ 的积分存在, 并称

$$
\mu (f) := \int_ {\Omega} f (\omega) \mu (\mathrm{d} \omega) = \mu (f ^ {+}) - \mu (f ^ {-})
$$

为 $f$ 关于测度 $\mu$ 的积分; 否则称 $f$ 关于 $\mu$ 的积分不存在. 如果

$$
\mu (| f |) = \mu (f ^ {+}) + \mu (f ^ {-}) <   \infty ,
$$

我们就称 f 关于测度  $\mu$  可积.

由上面的定义, 显然实值可测函数 $f \in \mathcal{F}$ 与其绝对值 $|f| \in \mathcal{F}$ 的可积性等价. 特别地, 有界可测函数关于有限测度可积.

定理 A.2.8 实值可测函数的积分具有如下性质:

(1) 设 $f, g \in \mathcal{F}$ 满足 $f = g$ (a.e.). 若 $f, g$ 之一的积分存在, 则二者的积分都存在且 $\mu(f) = \mu(g)$;
(2) 若 $f, g \in \mathcal{F}$ 的积分存在且有 $f \leqslant g$ (a.e.), 则 $\mu(f) \leqslant \mu(g)$;
(3) 设 $a \in \mathbb{R}$. 若 $f \in \mathcal{F}$ 的积分存在, 则 $af$ 的积分存在且 $\mu(af) = a\mu(f)$;
(4) 若 $f, g \in \mathcal{F}$ 均可积, 则 $f + g$ 可积且有 $\mu(f + g) = \mu(f) + \mu(g)$.

证明 性质 (1), (2), (3) 显然.

(4) 首先考虑 $f, g \in \mathcal{F}^{+}$ 的情况. 令 $\phi_{n}$ 是 (A.2.5) 式定义的函数. 则有 $f_{n} = \phi_{n} \circ f \in \mathcal{S}^{+}$ 和 $g_{n} = \phi_{n} \circ g \in \mathcal{S}^{+}$. 注意 $f_{n} \uparrow f$ 和 $g_{n} \uparrow g$, 因而 $f_{n} + g_{n} \uparrow f + g$. 根据命题 A.2.3 和单调收敛定理有

$$
\mu (f + g) = \lim _ {n \to \infty} \mu (f _ {n} + g _ {n}) = \lim _ {n \to \infty} \left[ \mu (f _ {n}) + \mu (g _ {n}) \right] = \mu (f) + \mu (g).
$$

对于一般情况 $f, g \in \mathcal{F}$, 由关系

$$
(f + g) ^ {+} - (f + g) ^ {-} = f + g = f ^ {+} - f ^ {-} + g ^ {+} - g ^ {-},
$$

有

$$
(f + g) ^ {+} + f ^ {-} + g ^ {-} = (f + g) ^ {-} + f ^ {+} + g ^ {+},
$$

进而

$$
\mu \big ((f + g) ^ {+} \big) + \mu (f ^ {-}) + \mu (g ^ {-}) = \mu \big ((f + g) ^ {-} \big) + \mu (f ^ {+}) + \mu (g ^ {+}).
$$

移项并适当合并即得欲证等式.

□

## A.2.4 控制收敛定理

前面证明的单调收敛定理与下面的法图定理和控制收敛定理构成了抽象积分理论中的三个基本收敛定理, 在该理论中扮演着关键角色.

定理 A.2.9 (法图定理) 对于任何  $f_{1}, f_{2}, \cdots \in F^{+}$  有

$$
\mu \big (\liminf _ {n \to \infty} f _ {n} \big) \leqslant \liminf _ {n \to \infty} \mu (f _ {n}).
$$

证明 令 $g_{n} = \inf_{k\geqslant n}f_{k}$ .则有 $0\leqslant g_n\leqslant f_n$ 和 $g_{n}\uparrow \liminf_{n\to \infty}f_{n}$ .利用单调收敛定理，

$$
\mu \big (\operatorname * {l i m   i n f} _ {n \to \infty} f _ {n} \big) = \mu \big (\lim _ {n \to \infty} g _ {n} \big) = \lim _ {n \to \infty} \mu (g _ {n}) \leqslant \operatorname * {l i m   i n f} _ {n \to \infty} \mu (f _ {n}).
$$

定理 A.2.10（控制收敛定理）设  $f, f_{1}, f_{2}, \cdots \in F$  满足  $f_{n} \rightarrow f$  (a.e.). 若有可积函数 g 使得  $|f_{n}| \leqslant g$  (a.e.),  $n = 1, 2, \cdots$ ，则有  $\mu(f_{n}) \rightarrow \mu(f)$ .

证明 基于定理 A.2.8(1), 不妨假定  $\lim_{n\to\infty}f_n=f$  和  $|f_n|\leqslant g, n=1,2,\cdots$  处处成立. 注意到  $g+f_{n}$  和  $g-f_{n}$  都是非负可测函数, 利用法图定理, 我们有

$$
\begin{array}{l} \mu (g) + \mu (f) = \mu (g + f) = \mu \big (\operatorname * {l i m i n f} _ {n \to \infty} (g + f _ {n}) \big) \\ \leqslant \liminf _ {n \to \infty} \mu (g + f _ {n}) = \mu (g) + \liminf _ {n \to \infty} \mu (f _ {n}) \\ \end{array}
$$

和

$$
\begin{array}{l} \mu (g) - \mu (f) = \mu (g - f) = \mu \big (\liminf _ {n \to \infty} (g - f _ {n}) \big) \\ \leqslant \operatorname * {l i m i n f} _ {n \to \infty} \mu (g - f _ {n}) = \mu (g) - \operatorname * {l i m s u p} _ {n \to \infty} \mu (f _ {n}). \\ \end{array}
$$

综合上面二式得

$$
\mu (f) \leqslant \operatorname * {l i m   i n f} _ {n \to \infty} \mu (f _ {n}) \leqslant \operatorname * {l i m   s u p} _ {n \to \infty} \mu (f _ {n}) \leqslant \mu (f),
$$

故得  $\lim_{n\to\infty}\mu(f_n)=\mu(f).$

上面的控制收敛定理的条件可以弱化. 称 $(\Omega, \mathcal{F})$ 上的可测函数序列 $\{f_n\}$ 相对于 $\mu$ 是一致可积的, 是指当 $c \to \infty$ 时有

$$
\sup _ {n \geqslant 1} \mu \big (| f _ {n} | 1 _ {\{| f _ {n} | \geqslant c \}} \big) \to 0.
$$

特别地, 不难看出对任何  $\alpha > 1$  有

$$
\mu (| f _ {n} | 1 _ {\{| f _ {n} | \geqslant c \}}) \leqslant c ^ {1 - \alpha} \mu (| f _ {n} | ^ {\alpha} 1 _ {\{| f _ {n} | \geqslant c \}}) \leqslant c ^ {1 - \alpha} \mu (| f _ {n} | ^ {\alpha}).
$$

因此, 若 $\sup_{n\geqslant 1}\mu (|f_n|^{\alpha}) < \infty$ ，则 $\{f_n\}$ 是一致可积的.

定理 A.2.11 (控制收敛定理) 设  $f, f_{1}, f_{2}, \cdots \in F$  满足  $f_{n} \rightarrow f$  (a.e.). 若序列  $\{f_{n}\}$  一致可积, 则  $\mu(f_{n}) \rightarrow \mu(f)$ .

证明 由一致可积性, 对任意的 $\varepsilon > 0$ 当 $c > 0$ 充分大时有

$$
\sup _ {n \geqslant 1} \mu \big (f _ {n} 1 _ {\{f _ {n} <   - c \}} \big) \geqslant - \sup _ {n \geqslant 1} \mu \big (| f _ {n} | 1 _ {\{| f _ {n} | > c \}} \big) \geqslant - \varepsilon .
$$

因此有

$$
\mu (f _ {n}) = \mu \big (f _ {n} 1 _ {\{f _ {n} \geqslant - c \}} \big) + \mu \big (f _ {n} 1 _ {\{f _ {n} <   - c \}} \big) \geqslant \mu \big (f _ {n} 1 _ {\{f _ {n} \geqslant - c \}} \big) - \varepsilon .
$$

对 $f_{n}1_{\{f_{n}\geqslant -c\}}$ 应用法图定理可得

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mu \big (f _ {n} 1 _ {\{f _ {n} \geqslant - c \}} \big) \geqslant \mu \Big (\operatorname * {l i m i n f} _ {n \to \infty} f _ {n} 1 _ {\{f _ {n} \geqslant - c \}} \Big) \geqslant \mu \Big (\operatorname * {l i m i n f} _ {n \to \infty} f _ {n} \Big).
$$

因此有

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mu (f _ {n}) \geqslant \mu \Big (\operatorname * {l i m i n f} _ {n \to \infty} f _ {n} \Big) - \varepsilon .
$$

再由 $\varepsilon > 0$ 的任意性得

$$
\operatorname * {l i m i n f} _ {n \to \infty} \mu (f _ {n}) \geqslant \mu \Big (\operatorname * {l i m i n f} _ {n \to \infty} f _ {n} \Big).
$$

类似地, 可得

$$
\operatorname * {l i m s u p} _ {n \to \infty} \mu (f _ {n}) \leqslant \mu \Big (\operatorname * {l i m s u p} _ {n \to \infty} f _ {n} \Big).
$$

因为 $\lim_{n\to \infty}f_n = f$ (a.e.), 以上二式右边的积分都等于 $\mu (f)$. 故欲证结果成立.

例A.2.1 取 $\Omega = (0,1)$ 和 $\mathcal{F} = (0,1) \cap \mathcal{B}$, 令 $\mu$ 为 $(\Omega, \mathcal{F})$ 上的勒贝格测度. 则 $(\Omega, \mathcal{F}, \mu)$ 为概率空间. 对 $n \geqslant 1$, 令 $f_n = n1_{(0,1/n]}$. 显然 $\lim_{n \to \infty} f_n = 0$ 在 $\Omega$ 上处处成立. 但是

$$
\lim _ {n \to \infty} \int_ {\Omega} f _ {n} (\omega) \mu (\mathrm{d} \omega) = 1 \neq 0.
$$

这说明极限与积分次序的交换并不是无条件成立的.

## A.2.5 与斯蒂尔切斯积分的联系

令 $\mu$ 为欧氏可测空间 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的局部有限测度, 而 $G$ 为它的一个分布函数.

定理A.2.12 若 $\mathbb{R}^d$ 上的局部有界的博雷尔可测函数 $f$ 相对于 $\mu$ 几乎处处连续, 则它在任何有界区间 $[a, b] \subseteq \mathbb{R}^d$ 上相对于 $G$ 斯蒂尔切斯可积且

$$
\int_ {a} ^ {b} f (x) \mathrm{d} G (x) = \int_ {\mathbb {R} ^ {d}} f (x) 1 _ {(a, b ]} (x) \mu (\mathrm{d} x). \tag {A.2.6}
$$

证明 为表述简单, 我们只考虑 $d = 1$ 的情况. 根据假设, 存在 $N \in \mathcal{B}$ 满足 $\mu(N) = 0$ 且 $f$ 在 $N^{c} := \mathbb{R} \setminus N$ 中每点处连续. 对任何整数 $k \geqslant 1$, 取 $[a, b]$ 的分割点 $a = x_{k,0} < x_{k,1} < \cdots < x_{k,n_{k}} = b$ 满足

$$
\delta_ {k} := \max _ {1 \leqslant i \leqslant n _ {k}} (x _ {k, i} - x _ {k, i - 1}) \to 0, \quad k \to \infty .
$$

任取 $t_{k,i}\in [x_{k,i - 1},x_{k,i}],1\leqslant i\leqslant n_k.$ 定义 $\mathbb{R}$ 上的阶梯函数

$$
f _ {k} (x) = \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) 1 _ {(x _ {k, i - 1}, x _ {k, i} ]} (x). \tag {A.2.7}
$$

注意 $f_{k}$ 是简单函数, 故有

$$
\begin{array}{l} \int_ {(a, b ]} f _ {k} (x) \mu (\mathrm{d} x) = \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) \mu (x _ {k, i - 1}, x _ {k, i} ] \\ = \sum_ {i = 1} ^ {n _ {k}} f (t _ {k, i}) [ G (x _ {k, i}) - G (x _ {k, i - 1}) ] =: \sigma_ {k} (f, G; a, b). \\ \end{array}
$$

因为 $\lim_{k\to \infty}\delta_k = 0$ 且 $f$ 在 $[a,b]\setminus N$ 中的每一点处连续，由(A.2.7)式得

$$
\lim _ {k \to \infty} f _ {k} (x) = f 1 _ {(a, b ]} (x), \quad x \in [ a, b ] \setminus N,
$$

故相对于测度 $\mu$ 有 $\lim_{k\to \infty}f_k = f1_{(a,b]} = f1_{[a,b]}$ (a.e.). 应用控制收敛定理得

$$
\lim _ {k \to \infty} \sigma_ {k} (f, G; a, b) = \lim _ {k \to \infty} \int_ {\mathbb {R} ^ {d}} f _ {k} (x) 1 _ {(a, b ]} (x) \mu (\mathrm{d} x) = \int_ {\mathbb {R} ^ {d}} f (x) 1 _ {(a, b ]} (x) \mu (\mathrm{d} x).
$$

因此 $f$ 在区间 $[a, b]$ 上 $G$ 可积且 (A.2.6) 式成立.

推论A.2.13 若 $\mathbb{R}^d$ 上的局部有界的博雷尔可测函数 $f$ 相对于 $\mu$ 几乎处处连续, 则它在 $\mathbb{R}$ 上的 $G$ 积分为

$$
\int_ {- \infty} ^ {\infty} f (x) \mathrm{d} G (x) = \int_ {\mathbb {R} ^ {d}} f (x) \mu (\mathrm{d} x). \tag {A.2.8}
$$

该等式的含义是只要等号两边有一边的积分存在, 则另一边的积分也存在且二者相等.

定理 A.2.12 和推论 A.2.13 中关于函数 f 博雷尔可测的假定并不是必需的. 事实上, 由于 f 相对于勒贝格测度几乎处处连续, 可以证明它与一个博雷尔可测函数几乎处处重合, 且 (A.2.6) 式和 (A.2.8) 式仍然成立.

## A.2.6 概率空间上的积分

前面讨论的测度空间上的积分当然也适用于概率空间. 由此可以给出基于测度积分的数学期望的定义.

定义 A.2.4 设  $(\Omega, \mathcal{F}, \mathbf{P})$  为概率空间. 如果此空间上的随机变量  $\xi$  作为可测函数的积分存在, 我们就称该积分为  $\xi$  的数学期望, 并记作  $\mathbf{E}\xi$  或  $\mathbf{E}(\xi)$ , 即

$$
\mathbf {E} \xi = \int_ {\Omega} \xi (\omega) \mathbf {P} (\mathrm{d} \omega). \tag {A.2.9}
$$

若 $\mathbf{E}|\xi| < \infty$，则称 $\xi$ 是可积的。

定理A.2.14 设 $\xi$ 是 $d$ 维随机变量, 而 $\mu_{\xi}$ 是 $\xi$ 在 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的分布. 则对 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的任何可测函数 $f$ 有

$$
\mathbf {E} f (\xi) = \int_ {\mathbb {R} ^ {d}} f (x) \mu_ {\xi} (\mathrm{d} x). \tag {A.2.10}
$$

该等式的含义是只要等号两边有一边存在, 则另一边也存在且二者相等.

证明 首先, 考虑 $f$ 为 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的非负简单函数的情况. 假设它有表达式

$$
f (x) = \sum_ {k = 1} ^ {n} b _ {k} 1 _ {B _ {k}} (x), \quad x \in \mathbb {R} ^ {d},
$$

其中 $b_{1}, b_{2}, \cdots, b_{n} \in \mathbb{R}_{+}$ 而 $B_{1}, B_{2}, \cdots, B_{n} \in \mathcal{B}^{d}$ 为 $\mathbb{R}^{d}$ 的有限划分. 这样

$$
f (\xi (\omega)) = \sum_ {k = 1} ^ {n} b _ {k} 1 _ {B _ {k}} (\xi (\omega)) = \sum_ {k = 1} ^ {n} b _ {k} 1 _ {\xi^ {- 1} (B _ {k})} (\omega), \quad \omega \in \varOmega ,
$$

其中  $\xi^{-1}(B_{1}),\xi^{-1}(B_{2}),\cdots,\xi^{-1}(B_{n})\in\mathcal{F}$  为  $\Omega$  的有限划分. 所以  $f(\xi)$  为  $(\Omega,\mathcal{F})$  上的非负简单函数. 根据数学期望的定义有

$$
\mathbf {E} f (\xi) = \sum_ {k = 1} ^ {n} b _ {k} \mathbf {P} (\xi^ {- 1} (B _ {k})) = \sum_ {k = 1} ^ {n} b _ {k} \mu_ {\xi} (B _ {k}) = \int_ {\mathbb {R} ^ {d}} f (x) \mu_ {\xi} (\mathrm{d} x).
$$

其次, 考虑 $f$ 为 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的非负可测函数的情况. 令 $\phi_n$ 是 (A.2.5) 式定义的函数. 则 $f_n := \phi_n \circ f$ 为 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的简单函数且 $f_n \uparrow f$. 根据前面证明的结果和单调收敛定理有

$$
\mathbf {E} f (\xi) = \lim _ {n \to \infty} \mathbf {E} f _ {n} (\xi) = \lim _ {n \to \infty} \int_ {\mathbb {R} ^ {d}} f _ {n} (x) \mu_ {\xi} (\mathrm{d} x) = \int_ {\mathbb {R} ^ {d}} f (x) \mu_ {\xi} (\mathrm{d} x).
$$

最后, 当 $f$ 为 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的一般可测函数时, 分别考虑其正部和负部对应的积分即得欲证等式. □

由定理 A.2.14 和推论 A.2.13 可以看出, 在很多情况下定义 A.2.4 与本书正文中给出的数学期望的定义是吻合的. 这里的定义拓宽了可积函数的范围.

## 参考文献

[1] CHEN L H Y, GOLDSTEIN L, SHAO Q M. Normal Approximation by Stein's Method. Berlin: Springer, 2011.
[2] CHEN M F. From Markov Chains to Non-Equilibrium Particle Systems. 2nd ed. Singapore: World Sci., 2004.
[3] ETHIER S N, KURTZ T G. Markov Processes: Characterization and Convergence. New York: John Wiley & Sons, 1986.
[4] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第一卷. 杨弢亮, 叶彦谦, 译. 北京: 高等教育出版社, 2006.
[5] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第二卷. 徐献瑜, 冷生明, 梁文骐, 译. 北京: 高等教育出版社, 2006.
[6] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第三卷. 路见可, 余家荣, 吴亲仁, 译. 北京: 高等教育出版社, 2006.
[7] FELLER W. An Introduction to Probability Theory and its Applications: Vol. 1. 3rd ed. New York: John Wiley & Sons, 1968.
[8] FELLER W. An Introduction to Probability Theory and its Applications: Vol. 2. 2nd ed. New York: John Wiley & Sons, 1971.
[9] GRIMMETT G, WELSH D. Probability: An Introduction. 2nd ed. Oxford: Oxford Univ. Press, 2014.
[10] HEWITT E, STROMBERG K. Real and Abstract Analysis. Berlin: Springer, 1965.
[11] KALLENBERG O. Foundations of Modern Probability. 3rd ed. Switzerland: Springer, 2021.
[12] LE GALL J -F. Brownian Motions, Martingales and Stochastic Calculus. Switzerland: Springer, 2016.
[13] LE GALL, J -F. Measure Theory, Probability, and Stochastic Processes. Switzerland: Springer, 2022.
[14] LIGGETT M. Interacting Particle Systems. Berlin: Springer, 1985.
[15] ROSE S M. Introduction to Probability Models. 13th ed. London: Academic Press, 2019.
[16] TALAGRAND M. Spin Glasses: A Challenge for Mathematicians. Berlin: Springer-Verlag, 2003.
[17] TALAGRAND M. The Parisi formula. Ann. Math., 2006, 163: 221-263.
[18] 王梓坤. 概率论基础及其应用. 3 版. 北京: 北京师范大学出版社, 2007.
[19] 严加安. 测度论讲义. 3 版. 北京: 科学出版社, 2021.
[20] 严士健, 刘秀芳. 测度与概率. 2 版. 北京: 北京师范大学出版社, 2003.
[21] 应坚刚, 何萍. 概率论. 2 版. 上海: 复旦大学出版社, 2016.
[22] 周民强. 实变函数论. 2 版. 北京: 北京大学出版社, 2008.

## 名词索引

G 积分 92, 97, 99

G 可积 92, 97, 99

$L^r$ 基本列 163

$L^r$ 柯西列 163

$L^r$ 收敛 163

P 零集 15

$\sigma$ 代数 10

$\sigma$ 可加性 12

$\sigma$ 有限测度 12

d 维正态分布 153

n 维乘积概率空间 32

r 阶平均收敛 163

0-1 律 160

## A

爱德华兹-安德森模型 80

## B

贝特朗奇论 9

贝叶斯公式 22

必然事件 3,15

边缘分布 65,66

边缘分布函数 65, 67

边缘分布列 68

边缘分布密度 68,70

标准差 113

标准化随机变量 116

标准正态分布 56

博雷尔-坎泰利引理 159

博雷尔 $\sigma$ 代数 12

博雷尔测度 15

博雷尔函数 38

博雷尔集 12

博雷尔可测集 12

博雷尔可测空间 12

伯恩斯坦多项式 179

伯努利分布 45

伯努利概率空间 15

伯努利试验 3

补集 3

不降函数的广义逆 59

不可能事件 3,15

不可数无限集 2

不相关 115

布丰投针试验 7

## C

测度 12

测度的限制 13

成功 3

| 乘法公式 | 20 |
| --- | --- |
| 乘积σ代数 | 28, 31 |
| 乘积概率测度 | 29, 31, 32 |
| 乘积概率空间 | 29, 31, 32 |
| 乘积可测空间 | 28 |
| 乘积样本空间 | 28, 31 |

D

| (弱)大数定律 | 176 |
| --- | --- |
| 单边切比雪夫不等式 | 179 |
| 单点概率测度 | 13 |
| 单调类 | 210 |
| 单调类定理 | 211, 212 |
| 单调收敛定理 | 109, 215 |
| 导数 | 134 |
| 邓肯类 | 212 |
| 邓肯类定理 | 212 |
| 狄拉克测度 | 13 |
| 第n次成功的时间 | 47 |
| 棣莫弗-拉普拉斯中心极限定理 | 186 |
| 独立事件 | 25, 27, 28 |
| 独立事件类 | 26, 28 |
| 独立随机变量 | 75, 79 |
| 独立性检验 | 200, 204 |
| 对立事件 | 3, 4 |
| 多元特征函数 | 147 |
| 多重卷积 | 149 |

E

| 二维正态分布 | 72 |
| --- | --- |
| 二项分布 | 45 |

F

| 法图定理 | 109, 217 |
| --- | --- |

| 反温度 | 80 |
| --- | --- |
| 反演公式 | 144 |
| 方差 | 113 |
| 非退化随机变量 | 43 |
| 费勒条件 | 194 |
| 分布 | 42 |
| 分布函数 | 40, 42, 64 |
| 分布函数的实现 | 58 |
| 分布列 | 44 |
| 分布密度 | 44 |
| 分部积分公式 | 101 |
| 符号测度 | 100 |
| 复平面 | 134 |
| 傅里叶变换 | 134 |
| 负部 | 93 |
| 负二项分布 | 48 |

G

| 伽马分布 | 56 |
| --- | --- |
| 伽马函数 | 55 |
| 概率 | 3, 12, 15 |
| 概率测度 | 12 |
| 概率分布 | 42 |
| 概率分布函数 | 40 |
| 概率空间 | 15 |
| 高斯分布 | 56 |
| 共轭数 | 134 |
| 古典概率空间 | 16 |
| 古典概率模型 | 4 |
| 古典概型 | 4 |

H

| 赫尔德不等式 | 119 |
| --- | --- |
| 黑利第二定理 | 170 |

黑利第一定理 169

后验概率 24

互不相容事件 4

互斥事件 4

J

| 基本列 | 162 |
| --- | --- |
| 积分 | 100, 213, 214, 216 |
| 积分存在 | 216 |
| 吉布斯态 | 80 |
| 集代数 | 10, 210 |
| 集合 | 2 |
| 集类生成的σ代数 | 11 |
| 几何分布 | 46 |
| 几何分布的无记忆性 | 47 |
| 几何概率空间 | 16 |
| 几何概率模型 | 6 |
| 几何概型 | 6 |
| 几乎必然成立 | 42 |
| 几乎必然收敛 | 158 |
| 几乎必然相等 | 43 |
| 几乎处处成立 | 40 |
| 几乎处处相等 | 40 |
| 加西亚极大不等式 | 182 |
| 简单函数 | 213 |
| 简单随机游动 | 79 |
| 解析函数 | 134 |
| 居里-外斯模型 | 80 |
| 局部有限测度 | 15 |
| 具有吸收态 | 80 |
| 卷积 | 149 |
| 卷积公式 | 85, 149 |
| 绝对连续 | 98 |
| 绝对连续型 | 41, 53, 65, 69, 70 |
| 绝对值 | 134 |

均匀分布 魏函数合70

均值 101

K

| 卡方独立性检验 | 204 |
| --- | --- |
| 卡方分布 | 83 |
| 卡方分布的自由度 | 83 |
| 卡方检验 | 204 |
| 柯西-施瓦茨不等式 | 113 |
| 柯西分布 | 82 |
| 柯西列 | 162 |
| 可测函数 | 38 |
| 可测集 | 10, 210 |
| 可测空间 | 10 |
| 可测映射 | 37 |
| 可积 | 101, 135, 214, 216, 220 |
| 可数概率空间 | 16 |
| 可数划分 | 11 |
| 可数集 | 2 |
| 可数可加性 | 12 |
| 可数无穷次伯努利试验 | 32 |
| 可数无穷维乘积概率空间 | 32 |
| 可数无限集 | 2 |
| 空集 | 2 |
| 控制收敛定理 | 109, 217, 218 |

L

| 拉普拉斯变换 | 150 |
| --- | --- |
| 莱维连续性定理 | 172 |
| 勒贝格测度 | 15 |
| 离散型 | 41, 65, 67 |
| 离散型随机变量 | 44 |
| 李亚普诺夫中心极限定理 | 198 |
| 联合分布 | 66 |