# 上册 / 第二章 实数

原始 PDF 第 34–56 页。

## 第二章

## 实数

---

20

第二章 实数

数的发展过程可以从两个方面来看: 一个是它的历史发展过程, 另一个是它的逻辑发展过程.

不同的文化对数的认识过程有所区别. 大体上, 人们首先 (感性地) 认识了自然数, 然后认识整数、有理数、实数、复数, 并在有理数基础上建立实数理论, 在集合论基础上建立自然数理论.

逻辑上, 自然应该是先建立自然数理论, 再引入有理数, 并在此基础上建立实数理论, 并引入复数.

## 2.1 自然数公理

自然数是构造实数的基础,但从实数理论的历史发展过程来看,自然数理论晚于实数理论.这虽然有点意料之外,却在情理之中.

Peano $^{①}$ 于1889年发表了自然数公理.

(N) 自然数公理 满足以下性质的集合 $\mathbb{N}$ 称为自然数集:

(1) 0 属于 N;
(2) 每一个确定的自然数 n 都有唯一的后继  $n^{+}$ ;
(3) 没有以 0 为后继的自然数;
(4) 不同的自然数对应不同的后继, 即若 $m \neq n$, 则 $m^{+} \neq n^{+}$;
(5) 若 $E$ 是 $\mathbb{N}$ 的子集, 包含 0 及其每一个元素的后继, 则 $E$ 是 $\mathbb{N}$.

在自然数公理中, 只是涉及自然数的序而没有涉及四则运算. 这里 0 可以抽象地看作一个符号. 我们可以用别的记号, 比如 $\bar{n}$ 来代替 0. 自然, 我们也可以用 1 来代替 0.

有了自然数以后, 我们可以在其中定义加法. 对于 $m, n \in \mathbb{N}$, 定义

(1) $n+0=n;$
(2) $m + n^{+} = (m + n)^{+}$.

然后建立加法的性质, 再引入乘法, 把自然数集扩充为整数集、有理数集. 对此有兴趣的读者可以尝试自己完成这些工作.

易得有理数具有如下的稠密性: 对任何 $p, q \in \mathbb{Q}, p < q$, 存在有理数 $r$ 使得 $p < r < q$. 例如, 取 $r = \frac{p + q}{2}$ 即可.

进一步, 有理数还具有 Archimedes $^{②}$ 性: 设 p 为正有理数, 则对任何有理数 q, 存在自然数 n, 使得 np > q.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Peano, Giuseppe, 1858 年 8 月 27 日—1932 年 4 月 20 日, 意大利数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Archimedes, 公元前 287 年—前 212 年, 古希腊哲学家、数学家、物理学家、力学家.</span></small>

---

2.1 自然数公理

21

为证明这一结论, 不妨设 $q > 0$. 我们有正整数 $m_p, k_p$ 以及 $m_q, k_q$ 使得 $p = \frac{k_p}{m_p}$, $q = \frac{k_q}{m_q}$. 取 $n = m_p k_q + 1$ 即得 $np > q$.

基于自然数公理, 我们有如下常用的数学归纳法.

定理 2.1.1 设  $P_{0}, P_{1}, \cdots, P_{n}, \cdots$  是一列命题，满足

(1) $P_{0}$ 成立;
(2) 若对某个 $n \in \mathbb{N}$, $P_{n}$ 成立, 则 $P_{n+1}$ 成立,

则对任何  $n \in N, P_{n}$  成立.

证明 令

$$
E := \left\{n \in \mathbb {N} | P _ {n} \text {成立} \right\}.
$$

由 (1), $0 \in E$, 而由 (2), $n \in E$ 蕴涵 $n + 1 \in E$. 因此, 由自然数公理 (N), 得到 $E = \mathbb{N}$. 即对任何 $n \in \mathbb{N}, P_n$ 成立. $\square$

数学归纳法还有以下常用的形式.

定理 2.1.2 设  $m \in N$  给定,  $P_{m}, P_{m+1}, \cdots, P_{n}, \cdots$  是一列命题, 满足

(1) $P_{m}$ 成立;
(2) 对某个 $n \in \mathbb{N}, n \geqslant m$, 若 $P_{n}$ 成立, 则 $P_{n+1}$ 成立,

则对任何自然数  $n \geqslant m, P_{n}$  成立.

定理 2.1.3 设  $m \in N$  给定,  $P_{m}, P_{m+1}, \cdots, P_{n}, \cdots$  是一列命题, 满足

(1) $P_{m}$ 成立;
(2) 对某个  $n \in N, n \geqslant m$ ，若  $P_{m}, P_{m+1}, \cdots, P_{n}$  成立，则  $P_{n+1}$  成立，则对任何自然数  $n \geqslant m, P_{n}$  成立.

关于自然数的介绍, 可参看《陶哲轩实分析》[57] 第二章.

Peano 自然数公理对于集合论公理的建立起到了重要作用. von Neumann 则按以下方式 “无中生有” 地构造出了自然数:

$$
\begin{array}{l} 0 := \varnothing , \\ 1 := \{\varnothing \} = \{0 \}, \\ 2 := \{\varnothing , \{\varnothing \} \} = \{0, 1 \}, \\ 3 := \{\varnothing , \{\varnothing \}, \{\varnothing , \{\varnothing \} \} \} = \{0, 1, 2 \}, \\ 4 := \{\varnothing , \{\varnothing \}, \{\varnothing , \{\varnothing \} \}, \{\varnothing , \{\varnothing \}, \{\varnothing , \{\varnothing \} \} \} \} = \{0, 1, 2, 3 \}, \\ \cdots , \\ n + 1 := n \cup \{n \} = \{0, 1, 2, \dots , n \}, \\ \dots \\ \end{array}
$$

按照集合论公理, 以上的自然数都是合乎公理规则的集合. 因此, 这可以视为基于集合论公理构造出了自然数. 而完成了自然数的构造, 相当于证明了满足自然数公理的自然

---

22

第二章 实数

数确实是存在的. 而此项工作的完成, 则意味着我们不必再把 Peano 的自然数公理视为公理. 它更像是一个构造自然数的 “定制标准”. 类似地, 即将介绍的实数系公理也可以视为构造实数系的一个 “定制标准”.

## 2.2 实数系公理

什么是实数, Hilbert $^{①}$ 于 1899 年首次提出了实数公理系统. 这虽然是在建立实数理论的工作之后, 但相关要求是每一种实数理论都必须考虑的. 正如我们在前一节所指出的, 我们在课程中引用这一公理体系, 并非真的要把它们作为公理, 而是把它们视为构造实数系的一个 “定制标准”.

## 2.2.1 实数系公理

实数系公理有几种等价的形式, 我们采用以下形式.

设 $\mathbb{R}$ 是一个集合, 带有加法和乘法两种运算以及序关系:

加法 +:  $R \times R \rightarrow R, (x, y) \mapsto x + y;$

乘法 $\because \mathbb{R} \times \mathbb{R} \to \mathbb{R}, (x, y) \mapsto x \cdot y,$ 在不引起混淆的情况下，$x \cdot y$ 简记为 $xy$;

序关系 $\leqslant: x \leqslant y$ 也记作 $y \geqslant x$.

进一步, x < y (也记作 y > x) 表示  $x \leqslant y$  且  $x \neq y$ .

满足下列公理的系统 $(\mathbb{R}, +, \cdot, \leqslant)$ 称为实数系，简写为 $\mathbb{R}$，它的元素称为实数:

设 $x, y, z \in \mathbb{R}$.

(F) 域公理 ( $R, +, \cdot$ ) 是一个域, 即满足

(A1) 加法结合律  $(x+y)+z=x+(y+z)$ .

(A2) 加法交换律  $x + y = y + x$ .

(A3) 存在加法单位元 存在 $0 \in \mathbb{R}$, 称为加法单位元或零元, 满足: 对于任何 $x \in \mathbb{R}$, 成立 $x + 0 = x$.

(A4) 存在负元 对于任何 $x \in \mathbb{R}$, 存在一个元素 $y \in \mathbb{R}$ (记作 $-x$) 满足 $x + (-x) = 0$.

(M1) 乘法结合律  $(xy)z = x(yz)$ .

(M2) 乘法交换律 xy = yx.

(M3) 存在乘法单位元 存在非零元 $1 \in \mathbb{R}$, 称为乘法单位元, 满足: 对于任何 $x \in \mathbb{R}$, $1 \cdot x = x$.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Hilbert, David, 1862 年 1 月 23 日—1943 年 2 月 14 日, 德国数学家.</span></small>

---

2.2 实数系公理

23

(M4) 非零元存在逆元 若 $x \neq 0$, 则存在一个元素 $y \in \mathbb{R}$ (记作 $1 / x$ 或 $x^{-1}$) 满足 $x(1 / x) = 1$.

(AM) 乘法分配律 $x(y + z) = xy + xz$.

(O) 序公理

(O1) 反对称性 若 $x \leqslant y$ 与 $y \leqslant x$ 都成立, 则 $x = y$.

(O2) 传递性 若 $x \leqslant y$, 且 $y \leqslant z$, 则 $x \leqslant z$.

(O3) 全序性 关系式  $x \leqslant y, y \leqslant x$  中至少有一个成立.

(AO) 加法的保序性 若 $y \leqslant z$, 则 $x + y \leqslant x + z$.

(MO) 乘法的保序性 若  $x, y \geqslant 0$ ，则  $xy \geqslant 0$ .

(C) 连续公理

(C1) Archimedes 公理 给定 $y$ 与 $x > 0$, 则总可以把 $x$ 自己相加足够多的次数使得

$$
n x := \overbrace {x + x + \cdots + x} ^ {n \text {次}} > y.
$$

(C2) 完备公理 如果 $\widetilde{\mathbb{R}} \supseteq \mathbb{R}$ 且 $(\widetilde{\mathbb{R}}, +, \cdot, \leqslant)$ 满足前述公理 (F), (O), (C1), 则 $\widetilde{\mathbb{R}} = \mathbb{R}$.

注 2.2.1 条件 (A1)\~(A4) 表示 ( $\mathbb{R}, +$ ) 是一个 (可) 交换群, 又称 Abel $^{①}$ 群.

注 2.2.2 条件 (O1)\~(O2) 及自反性 “ $x \leqslant x$ ” 表示 ( $R, \leqslant$ ) 是一个偏序集，条件 (O1)\~(O3) 表示 ( $R, \leqslant$ ) 是一个全序集。易见 (O3) 蕴涵自反性。

注2.2.3 为方便起见, 用 $y \geqslant x$ 表示 $x \leqslant y$. 而 $x < y$ 表示 $x \leqslant y$ 且 $x \neq y$. 这样, 由序公理, 关系式 $x < y$, $x = y$, $y < x$ 中有且只有一个成立.

## 2.2.2 实数的基本性质

称满足域公理 (F) 与序公理 (O) 的系统为有序域. 关于实数四则运算的很多常用性质和不等式的都可以从公理 (F) 和 (O) 推导出来. 我们将它们的一部分留作习题.

对于 $x, y \in \mathbb{R}$ 记 $x - y := x + (-y)$. 当 $y \neq 0$ 时, 记 $x \cdot (1 / y)$ 为 $x / y$ 或 $\frac{x}{y}$. 定义 $x$ 的绝对值为

$$
| x | := \left\{ \begin{array}{l l} x, & x \geqslant 0, \\ - x, & x <   0. \end{array} \right.
$$

对于正整数 n, 定义它的阶乘  $n!$  为  $n \cdot (n-1) \cdots 2 \cdot 1$ . 定义偶数 2n 的双阶乘  $(2n)!!$  为  $(2n)(2n-2) \cdots 2$ , 定义奇数  $2n+1$  的双阶乘  $(2n+1)!!$  为  $(2n+1)(2n-1) \cdots 3 \cdot 1$ . 当 n=0 时,  $n!$  以及  $n!!$  定义为 1.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Abel, Niels Henrik, 1802 年 8 月 5 日—1829 年 4 月 6 日, 挪威数学家.</span></small>

---

24

第二章 实数

类似地, 可以定义三阶乘等.

对于自然数 n 以及  $0 \leqslant k \leqslant n$ ，记

$$
\mathrm{C} _ {n} ^ {k} := \frac {n !}{k ! (n - k) !}.
$$

则对于 $k \geqslant 0$ 以及 $n \geqslant k + 1$, 成立

$$
\mathrm{C} _ {n + 1} ^ {k + 1} = \mathrm{C} _ {n} ^ {k} + \mathrm{C} _ {n} ^ {k + 1}. \tag {2.2.1}
$$

对于整数  $n \geqslant m$ ，以及  $x_{m}, x_{m+1}, \cdots, x_{n} \in R$ ，引入求和符号

$$
\sum_ {k = m} ^ {n} x _ {k} := x _ {m} + x _ {m + 1} + \dots + x _ {n} \tag {2.2.2}
$$

和求积符号

$$
\prod_ {k = m} ^ {n} x _ {k} := x _ {m} x _ {m + 1} \dots x _ {n}. \tag {2.2.3}
$$

当 $n$ 为正整数时, $n$ 个 $x$ 的乘积记为 $x^n$. 进一步, 当 $x \neq 0$ 时, $x^0$ 定义为 $1, x^{-n}$ 定义为 $(x^{-1})^n$.

我们有以下重要结果.

命题 2.2.1 (三角不等式) $\left| {x + y}\right|  \leq  \left| x\right|  + \left| y\right|$ .

证明 上述不等式分情形讨论可得

(i) $x \geqslant 0, y \geqslant 0$. 则 $x + y \geqslant 0$. 从而 $|x + y| = x + y = |x| + |y|$.
(ii)  $x \geqslant 0, y \leqslant 0.$  则  $x + y = |x| - |y|$ .

若 $|x| - |y| \geqslant 0$，则 $|x + y| = |x| - |y| \leqslant |x| \leqslant |x| + |y|$.

若 $|x| - |y| < 0$，则 $|x + y| = |y| - |x| \leqslant |y| \leqslant |x| + |y|$.

(iii) $x \leqslant 0, y \leqslant 0$. 则由 (i), $|x + y| = |(-x) + (-y)| = |-x| + |-y| = |x| + |y|$.

(iv) $x \leqslant 0, y \geqslant 0$. 则由 (ii), $|x + y| = |y + x| \leqslant |y| + |x| = |x| + |y|$.

命题 2.2.2 (Newton $^{①}$  二项展开式) 对于正整数 n, 有

$$
(x + y) ^ {n} = \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} x ^ {k} y ^ {n - k}. \tag {2.2.4}
$$

证明 当 $n = 1$ 时, (2.2.4) 式成立. 进一步, 若对某个 $n \geqslant 1$, (2.2.4) 式成立, 则

$$
\begin{array}{l} (x + y) ^ {n + 1} = (x + y) (x + y) ^ {n} = (x + y) \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} x ^ {k} y ^ {n - k} \\ = \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} x ^ {k + 1} y ^ {n - k} + \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} x ^ {k} y ^ {n + 1 - k} \\ \end{array}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Newton, Isaac, 1643 年 1 月 4 日—1727 年 3 月 31 日, 英国物理学家、数学家.</span></small>

---

2.2 实数系公理

25

$$
\begin{array}{l} = x ^ {n + 1} + \sum_ {k = 1} ^ {n} (\mathrm{C} _ {n} ^ {k - 1} + \mathrm{C} _ {n} ^ {k}) x ^ {k} y ^ {n + 1 - k} + y ^ {n + 1} \\ = \mathrm{C} _ {n + 1} ^ {n + 1} x ^ {n + 1} + \sum_ {k = 1} ^ {n} \mathrm{C} _ {n + 1} ^ {k} x ^ {k} y ^ {n + 1 - k} + \mathrm{C} _ {n + 1} ^ {0} y ^ {n + 1} \\ = \sum_ {k = 0} ^ {n + 1} \mathrm{C} _ {n + 1} ^ {k} x ^ {k} y ^ {n + 1 - k}. \\ \end{array}
$$

于是, 由数学归纳法 (2.2.4) 式对任何自然数 n 成立.

展开式 (2.2.4) 中的系数称为二项式系数, 这些系数形成的三角称为杨辉 $^{①}$ 三角或贾宪 $^{②}$ 三角 $^{③}$ . 表中每个数字等于上一行左右两个数字之和:

![](../../raw/pages_0033-0048/images/page_39_image_5.jpg)

<details>
<summary>text_image</summary>

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
... ... ... ... ... ... ... ... ... ...
</details>

## 2.2.3 复数域

有很多问题在实数域内难以得到满意的结果. 我们需要复数域.

在  $R^{2}$  中引入加法和乘法:

$$
(x _ {1}, y _ {1}) + (x _ {2}, y _ {2}) := (x _ {1} + x _ {2}, y _ {1} + y _ {2}),
$$

$$
(x _ {1}, y _ {1}) \cdot (x _ {2}, y _ {2}) := (x _ {1} x _ {2} - y _ {1} y _ {2}, x _ {1} y _ {2} + x _ {2} y _ {1}).
$$

则可以验证 $(\mathbb{R}^2, +, \cdot)$ 构成一个域. 为了与通常的欧氏空间 $\mathbb{R}^2$ 区别开来, 我们把 $(\mathbb{R}^2, +, \cdot)$ 记为 $\mathbb{C}$, 称为复数域. 此时 $(1,0)$ 就是 $\mathbb{C}$ 的单位元. 若记 $i := (0,1)$, 则 $i^2 = (-1,0)$, 我们称 $i$ 为虚根单位. 此处及今后, 在复数域中, 直接用实数 $x$ 表示 $(x,0)$, 则 $\mathbb{C}$ 中的元素 $(x,y)$ 可以写为 $x + yi$, 称为复数, $x,y$ 分别称为 $x + yi$ 的实数部分和虚数部分, 简称实部和虚部, 记作 $x = \operatorname{Re}(x + yi), y = \operatorname{Im}(x + yi)$. 称 $|x + yi| := \sqrt{x^2 + y^2}$ 为 $x + yi$ 的

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 杨辉, 字谦光, 南宋钱塘 (今浙江杭州) 人, 约 1238 年—约 1298 年.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② 贾宪, 北宋人, 生平籍贯不详, 约活动在 11 世纪上半叶.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">③ 杨辉在 1261 年所著的《详解九章算法》一书中, 辑录了这一三角形数表, 称之为 “开方作法本源” 图, 并说明此表引自贾宪的《释锁算术》.</span></small>

---

26

第二章 实数

模或绝对值. 若 $y \neq 0$, 则 $x + yi$ 称为虚数, 而 $yi$ 称为纯虚数. 由于 $\mathrm{i}^2 = -1$, 因此, 不可能在 $\mathbb{C}$ 中引进序使之成为有序域.

## 2.2.4 广义实数系

时常, 引入广义实数系可以方便讨论. 广义实数系包含 $\mathbb{R}$ 中所有的元以及两个无穷大: 正无穷大 $+\infty$ 和负无穷大 $-\infty$. 规定

$$
- \infty <   x <   + \infty , \quad \forall x \in \mathbb {R}.
$$

对于广义实数系中的元素 $a < b$ ，记

$$
\begin{array}{l} (a, b) := \{x | a <   x <   b \}, \\ [ a, b ] := \{x | a \leqslant x \leqslant b \}, \\ [ a, b) := \{x | a \leqslant x <   b \}, \\ (a, b ] := \{x | a <   x \leqslant b \}. \\ \end{array}
$$

特别地, $(-\infty, +\infty)$ 即为 $\mathbb{R}$, 而 $[- \infty, +\infty]$ 即为广义实数系. 当这些集合不以 $-\infty$ 和 $+\infty$ 为元素时, 我们称之为区间. 其中, 当 $a, b$ 为实数时, 称为有界区间, 当 $a = -\infty$ 或 $b = +\infty$ 时称为无界区间.

进一步, 设 $a < b$ 为实数, 可把区间分为以下三类:

开区间: $(a,b),(a, + \infty),(-\infty ,b),(-\infty , + \infty)$

闭区间: $[a,b],[a, + \infty),(-\infty ,b],(-\infty , + \infty)$

半开半闭区间: $[a, b)$, $(a, b]$.

对于 $x, y, z \in \mathbb{R}, y > 0, z < 0,$ 规定

$$
\begin{array}{l} x + (+ \infty) = x - (- \infty) = + \infty , \\ x - (+ \infty) = x + (- \infty) = - \infty , \\ y \cdot (+ \infty) = z \cdot (- \infty) = + \infty , \\ y \cdot (- \infty) = z \cdot (+ \infty) = - \infty , \\ \end{array}
$$

进一步, 规定

$$
\begin{array}{l} \frac {1}{+ \infty} = \frac {1}{- \infty} = 0, \\ (+\infty) + (+ \infty) = (+ \infty) - (- \infty) = + \infty , \\ (- \infty) + (- \infty) = (- \infty) - (+ \infty) = - \infty , \\ \end{array}
$$

---

2.3 实数系的构造

27

$$
\begin{array}{l} (- \infty) \cdot (- \infty) = (+ \infty) \cdot (+ \infty) = + \infty , \\ (- \infty) \cdot (+ \infty) = (+ \infty) \cdot (- \infty) = - \infty . \\ \end{array}
$$

但是 $(+\infty) + (-\infty), (+\infty) - (+\infty), 0 \cdot (\pm \infty)$ 等无意义.

## 2.2.5 单调函数与周期函数

单调函数与周期函数是非常重要的两类函数. 首先, 定义单调函数如下:

定义 2.2.1 设有函数 $f: E \to \mathbb{R}$, 其中 $E$ 是 $\mathbb{R}$ 的非空子集①.

如果对任何 $x, y \in E, x < y$ 蕴涵 $f(x) \leqslant f(y)$，则称 $f$ 在 $E$ 上单调增加。若 $x < y$ 蕴涵 $f(x) < f(y)$，则称 $f$ 在 $E$ 上严格单调增加。

称 $f$ 在 $E$ 上（严格）单调减少是指 $-f$ 在 $E$ 上（严格）单调增加.

单调增加又称单调上升、单调递增, 简称单增, 单调减少又称单调下降、单调递减, 简称单减.

若 $f:\mathbb{R}\to \mathbb{R},T\neq 0$ 使得对任何 $x\in \mathbb{R}$ 成立 $f(x + T) = f(x)$ ，则称 $f$ 为以 $T$ 为周期的周期函数.

周期时常指正周期, 甚至所谓 “最小正周期”. 并非所有周期函数均有最小正周期. 例如任何非零有理数均为 Dirichlet $^{②}$ 函数 $D(\cdot):=\chi_{\mathbb{Q}}(\cdot)$ 的周期. 因此, Dirichlet 函数没有最小正周期.

## 2.3 实数系的构造

本节主要介绍用 Dedekind 分割建立实数系的方法.

## 第一次数学危机

首先, 简单回顾第一次数学危机的历史. 构造实数系的历史可追溯到古希腊的 Pythagoras $^{③}$ 学派的工作.

Pythagoras 学派信奉任何两个 (同类型的) 量都是 “可公度” 的. 以直线段的长度为例, 对于直线段 $\ell$ 与 $L$, 都存在直线段 $s$, 使得 $\ell, L$ 都是 $s$ 的整数倍, 比如说, 依次为 $m$ 倍和 $n$ 倍. 这样, 如果把 $\ell$ 的长度定义为 1 的话, $L$ 的长度就是分数 $\frac{n}{m}$. 按照这种方法, 就可以定义所有线段的长度.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 可在广义实数系中类似地定义单调性.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Dirichlet, Peter Gustav Lejeune, 1805 年 2 月 13 日—1859 年 5 月 5 日, 德国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">③ Pythagoras of Samos, 约公元前 580 年—约前 500 年, 古希腊数学家、哲学家.</span></small>

---

28

第二章 实数

然而, Pythagoras 学派的 Hippasus $^{①}$ 发现存在不可公度的线段. 具体地, 就是正五边形边长与对角线不可公度, 正直角三角形直角边与斜边不可公度 (参见文献 [43]). 前者相当于说方程 $x = \frac{1 - x}{x}$ 没有有理根. 后者相当于说 $x^{2} = 2$ 没有有理根 $^{②}$.

不可公度量的发现, 导致了数学史上的第一次数学危机. 为了解决不可公度性问题, Eudoxus $^{③}$ 建立了比例论.

对于两个同类的量, Eudoxus 定义其 “比例” 及大小关系. 例如,

$\frac{a}{b}=\frac{A}{B}$  定义为: 对于任何 (正) 整数 m, n, 以下三者有且只有一个成立:

(1) ma > nb 且 mA > nB;
(2) ma < nb 且 mA < nB;
(3) ma = nb 且 mA = nB.

而  $\frac{a}{b} > \frac{A}{B}$  定义为: 存在 (正) 整数 m, n 使得 ma > nb 且  $mA \neq nB$ .

这样, $a, b$ 可公度当且仅当存在 $m, n$ 使得 $\frac{m}{n} = \frac{a}{b}$. 否则, (正) 整数的比分成两个集合: $L = \left\{\frac{m}{n} \mid \frac{m}{n} < \frac{a}{b}\right\}$ 以及 $U = \left\{\frac{m}{n} \mid \frac{m}{n} > \frac{a}{b}\right\}$, 且可见 $L$ 中每一个比例都小于 $U$ 中每一个比例.

然而, 在 Eudoxus 的比例论中, 比例不是数. 对于第一次数学危机, 比例论给出的解决方案是不完备的.

## 实数系的构造 Dedekind 分割

Dedekind 把有理数分成两个集合 $L$ 和 $U$, 其中 $L$ 中每一个元素均小于 $U$ 中每一个元素, 其思想明显与 Eudoxus 的比例论有关. 这样的集合对 $(L, U)$ 称为分割. 通过在分割中引入序、加法和乘法, Dedekind 给出了实数系的构造.

需要指出的是, Dedekind 时代的数学家们对于实数的理解并不是那么清晰的. 事实上, Dedekind 本人并不认为是通过分割构造了无理数, 而是认为分割确定了无理数. 但 Weber $^{④}$ 已经认识到并告诉过 Dedekind, 无理数就是分割.

另一方面, 实数在有理数的基础上构造, 而有理数的基础是自然数. 在建立实数理论时, 对于自然数的认识主要还基于经验. 因此, 那时的实数理论, 本质上还没有做到真正的严密.

如今, 我们基于集合论, 构造出了自然数, 并在此基础上引入了有理数及四则运算, 并建立其性质. 而用 Dedekind 分割构造实数的论证过程 (以及构造实数的其他方法), 完全在集合论公理允许的范围内. 并且, 我们也能够证明满足实数系公理的实数系本质上是唯一的. 因此, 严密地建立实数理论, 已经圆满地完成了.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Hippasus of Metapontum, 约公元前 470 年, 古希腊数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② 目前还不能说它相当于说  $\sqrt{2}$  是无理数, 因为我们还没有定义什么是  $\sqrt{2}$ .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">③ Eudoxus of Cnidus, 约公元前 408 年—前 347 年, 古希腊天文学家、数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">④ Weber, Heinrich Martin, 1842 年 5 月 5 日—1913 年 5 月 17 日, 德国数学家.</span></small>

---

2.3 实数系的构造

29

以下我们来介绍利用 Dedekind 分割构造实数系的过程.

由于 $U = \mathbb{Q} \setminus L$ 完全由 $L$ 确定, 所以我们采用 Rudin$^{①}$《数学分析原理》$^{[52]}$ 中的做法, 只考虑 $L$.

在通常的教材中, 利用 Dedekind 分割来构造实数时, 定义加法和乘法时都会涉及 Dedekind 分割的定义. 在本小节中, 我们按文献 [43] 中的方法, 在上确界存在定理的基础上来定义加法、乘法以及证明相关性质. 利用这一方法, 可以容易地用小数构造实数 $^{②}$ .

现在, 我们来构造实数系.

I. 实数集 称满足条件

(D1)  $\alpha \neq \varnothing, \alpha \neq Q;$

(D2) 对于有理数 p, q, 若  $q \in \alpha$ , p < q, 则  $p \in \alpha$ ;

(D3) $\alpha$ 中没有最大元

的有理数集 $\mathbb{Q}$ 的子集 $\alpha$ 为Dedekind分割.

称 Dedekind 分割为实数, 全体实数记为 $\mathbb{R}$. 本节下文中小写英文字母 $k, m, n$ 表示整数, 其他的小写英文字母表示有理数, 小写希腊字母表示实数. 对于有理数 $p$, 定义 $p^{*} := \{q | q < p\}$.

若 $\mathbb{Q} \setminus \alpha$ 中没有最小元, 则称 $\alpha$ 为无理分割, 若 $\mathbb{Q} \setminus \alpha$ 中有最小元 $p$, 则易证 $\alpha = p^*$, 此时称 $\alpha$ 为有理分割. 另一方面, 对于任何有理数 $p$, 必有 $p^* \in \mathbb{R}$. 因此, 有理分割的全体为 $\mathbb{Q}^* = \{p^* | p \in \mathbb{Q}\}$.

例 2.3.1 (无理分割的存在性) 考虑  $\alpha := \{p | p \geqslant 0, p^{2} < 2\} \cup 0^{*}$ . 则易见 (D1) 和 (D2) 成立. 为验证 (D3), 考虑 p > 0 满足  $p^{2} < 2$ . 令  $r = \frac{2 - p^{2}}{2p + 2}$ , 则 0 < r < 1. 进而  $r < \frac{2 - p^{2}}{r + 2p}$ . 即  $(p + r)^{2} < 2$ . 这表明  $p + r \in \alpha$ . 说明  $\alpha$  中没有最大元, 因此,  $\alpha$  是分割.

另一方面, 由于任何有理数的平方都不等于 2, 因此, $\mathbb{Q} \setminus \alpha = \{p | p > 0, p^2 > 2\}$. 若 $p \in \mathbb{Q} \setminus \alpha$, 取 $r := \frac{p^2 - 2}{2p}$, 易见 $0 < r < p$ 且 $r < \frac{p^2 - 2 + r^2}{2p}$. 因此, $(p - r)^2 > 2$, 即 $p - r \in \mathbb{Q} \setminus \alpha$. 所以 $\mathbb{Q} \setminus \alpha$ 中没有最小元, 即 $\alpha$ 是无理分割.

II. 在 $\mathbb{R}$ 中定义序

1. 序的定义 定义  $\alpha \leqslant \beta$  为  $\alpha \subseteq \beta$ .

2. $\mathbb{Q}$ 与 $\mathbb{Q}^*$ 的序一致 显然有

$$
p ^ {*} \leqslant q ^ {*} \Longleftrightarrow p \leqslant q. \tag {2.3.1}
$$

3. 全序性 (O1)\~(O3) 显然, (O1)\~(O2) 成立. 下证 (O3) 成立.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Rudin, Walter, 1921 年 5 月 2 日—2010 年 5 月 20 日, 美国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② 利用小数构造实数比想象的要困难一些, 参见第 34 页.</span></small>

---

30

第二章 实数

若 $\alpha \leqslant \beta$ 不成立, 即 $\alpha \nsubseteq \beta$, 则存在 $p \in \alpha \setminus \beta$. 由分割定义中的条件 (D2), 这意味着对任何 $q \in \beta$ 成立 $q < p$, 进而得到 $q \in \alpha$. 从而 $\beta \subseteq \alpha$, 即 $\beta \leqslant \alpha$ 成立. 因此 (O3) 成立.

4. 有理分割的稠密性 易见有理分割在 $\mathbb{R}$ 中有如下引理中的稠密性.

引理 2.3.1 若  $\alpha < \beta,$  则有 p 使得  $\alpha < p^{*} < \beta.$

证明 首先, 有 $p_0 \in \beta \setminus \alpha$. 进而又有 $p > p_0$ 使得 $p \in \beta$. 此时, $\alpha \leqslant p_0^* < p^* < \beta$. □进一步, 我们有

引理2.3.2 设 $\alpha \in \mathbb{R}, r > 0$。则存在 $p$ 使得 $p^* < \alpha < (p + r)^*$。进一步，若 $\alpha > q^*$，则可取到 $p \geqslant q$ 使得 $p^* < \alpha < (p + r)^*$。

证明 取 $p_0 \in \alpha$, 以及 $q \notin \alpha$, 记 $p_k = p_0 + \frac{kr}{2} (k = 1, 2, \dots)$. 由 Archimedes 性, 存在正整数 $n$ 使得 $p_n > q$. 从而 $p_n \notin \alpha$. 设 $m$ 为使得 $p_m \notin \alpha$ 成立的最小的整数. 取 $p = p_{m-1}$, 则有 $p^* < \alpha \leqslant \left(p + \frac{r}{2}\right)^* < (p + r)^*$. 进一步, 当 $\alpha > q^*$ 时, 若上面取到的 $p < q$, 则用 $q$ 代替 $p$ 即得结论.

5. 上确界存在定理 对于 $E \subset \mathbb{R}$, 若 $\beta \in \mathbb{R}$ 满足

$$
\alpha \leqslant \beta (\alpha \geqslant \beta), \quad \forall \alpha \in E, \tag {2.3.2}
$$

则称 $\beta$ 为 $E$ 的上界 (下界), $E$ 为上有界集 (下有界集). 如果存在 $\gamma \in \mathbb{R}$ 满足

(1)  $\gamma$  是 E 的上界 (下界);

(2) 若  $\sigma$  是 E 的上界 (下界), 则  $\gamma \leqslant \sigma (\gamma \geqslant \sigma)$ ,

则称 $\gamma$ 为 $E$ 的最小上界或上确界 (最大下界或下确界), 记作 $\sup E (\inf E)$. 若 $\gamma \in E$ 且 $\gamma$ 是 $E$ 的上界 (下界), 则称 $\gamma$ 为 $E$ 的最大值 (最小值), 记作 $\max E (\min E)$. 易见 $E$ 的上确界或最大值 (下确界或最小值) 存在的话, 是唯一的. 而 $E$ 的最大值 (最小值) 就是属于 $E$ 的上确界 (下确界). 为方便起见, 时常记 $\max \{\alpha, \beta\}$ 和 $\min \{\alpha, \beta\}$ 为 $\alpha \vee \beta$ 和 $\alpha \wedge \beta$.

我们有下面非常重要的上确界存在定理:

定理 2.3.3 R 中任何非空上有界集均有上确界.

证明 设 $E \subset \mathbb{R}$ 是一非空上有界集, 设 $\gamma$ 为 $E$ 的一个上界. 令 $\beta := \bigcup_{\alpha \in E} \alpha$. 我们来证明 $\beta$ 是一个分割.

(i) 首先, 由 $E$ 非空得到 $\beta \neq \varnothing$. 进一步, 由于 $\gamma \neq \mathbb{Q}$, 因此存在 $p \notin \gamma$. 于是对任何 $q \in \alpha \in E$, 必有 $q < p$. 因此, $p \notin \beta$. 所以 $\beta \neq \mathbb{Q}$.

(ii) 若 $q \in \beta, p < q$, 则有 $\alpha \in E$ 使得 $q \in \alpha$, 从而由 $\alpha$ 是分割得到 $p \in \alpha \subseteq \beta$.

(iii) 若 $p \in \beta$, 则存在 $\alpha \in E$ 使得 $p \in \alpha$. 从而有 $q > p$ 使得 $q \in \alpha$. 进而 $q \in \beta$. 因此, $\beta$ 中没有最大元.

这就证明了  $\beta$  是一个分割.

---

2.3 实数系的构造

31

接下来, 易见 $\beta$ 是 $E$ 的一个上界. 而如果 $\sigma$ 是 $E$ 的另一个上界, 则 $\forall \alpha \in E$ 有 $\alpha \subseteq \sigma$, 从而 $\beta = \bigcup_{\alpha \in E} \alpha \subseteq \sigma$. 这就是说 $\beta$ 是 $E$ 的上确界. □

6. 实数表示成有理分割集的上确界 利用有理分割的稠密性, 立即可得

$$
\alpha = \sup \left\{p ^ {*} \mid p ^ {*} <   \alpha \right\} = \sup \left\{p ^ {*} \mid p ^ {*} \leqslant \alpha \right\}. \tag {2.3.3}
$$

如若不然, 则必有 $\beta \equiv \sup \left\{p^{*} | p^{*} < \alpha \right\} < \alpha$. 由有理分割的稠密性, 存在 $q$ 使得 $\beta < q^{*} < \alpha$. 所以 $q^{*} \in \left\{p^{*} | p^{*} < \alpha \right\}$. 这又得到 $\beta \geqslant q^{*}$. 得到矛盾. 因此, (2.3.3) 式成立.

## Ⅲ. 在 $\mathbb{R}$ 中定义加法

1. 加法的定义 定义 $\alpha +\beta := \sup E_{\alpha ,\beta}$ ，其中

$$
E _ {\alpha , \beta} := \left\{(p + q) ^ {*} \mid p ^ {*} \leqslant \alpha \text {且} q ^ {*} \leqslant \beta \right\}. \tag {2.3.4}
$$

由有理分割的稠密性, $E_{\alpha, \beta}$ 非空, 且有 $p, q$ 使得 $p^{*} > \alpha$ 以及 $q^{*} > \beta$. 此时易证 $(p + q)^{*}$ 是 $E_{\alpha, \beta}$ 的上界. 因此, 由上确界存在定理, $\alpha + \beta$ 是合理定义的.

2. $\mathbb{Q}$ 与 $\mathbb{Q}^*$ 中加法的一致性 易见 $(p + q)^{*}$ 是 $E_{p^{*},q^{*}}$ 的最大值. 因此 $(p + q)^{*} = p^{*} + q^{*}$.

3. 加法交换律 (A2) 成立  $\alpha + \beta = \beta + \alpha$ . 这是因为  $E_{\alpha, \beta} = E_{\beta, \alpha}$ .

4. 加法零元 (A3) 成立 $\alpha + 0^{*} = \alpha$. 易见 $E_{\alpha,0^{*}} = \{p^{*} | p^{*} \leqslant \alpha\}$. 于是由 (2.3.3) 式即得 $\alpha + 0^{*} = \alpha$.

5. 加法的保序性 (AO) 若 $\alpha \leqslant \beta$, 则 $\alpha + \gamma \leqslant \beta + \gamma$. 这是因为此时有 $E_{\alpha, \gamma} \subseteq E_{\beta, \gamma}$.

推论 2.3.4 若对任何 s > 0, 成立  $\alpha \leqslant \beta + s^{*}$ , 则  $\alpha \leqslant \beta$ .

证明 若结论不真, 则 $\alpha > \beta$. 从而存在 $p, q$ 使得 $\beta < q^{*} < p^{*} < \alpha$. 因此, $\beta + (p - q)^{*} \leqslant q^{*} + (p - q)^{*} = p^{*} < \alpha$. 得到矛盾.

6. 加法结合律 (A1) 成立 $\alpha + (\beta + \gamma) = (\alpha + \beta) + \gamma$. 这是因为, 对任何 $s > 0$, 由引理2.3.2, 有 $p, q, r$ 使得

$$
p ^ {*} <   \alpha <   (p + s) ^ {*}, \quad q ^ {*} <   \beta <   (q + s) ^ {*}, \quad r ^ {*} <   \gamma <   (r + s) ^ {*}. \tag {2.3.5}
$$

于是

$$
\alpha + (\beta + \gamma) \leqslant p ^ {*} + q ^ {*} + r ^ {*} + (3 s) ^ {*} \leqslant ((\alpha + \beta) + \gamma) + (3 s) ^ {*},
$$

$$
(\alpha + \beta) + \gamma \leqslant p ^ {*} + q ^ {*} + r ^ {*} + (3 s) ^ {*} \leqslant (\alpha + (\beta + \gamma)) + (3 s) ^ {*}.
$$

由推论2.3.4以及反对称性得到 $\alpha +(\beta +\gamma) = (\alpha +\beta) + \gamma .$

7. Archimedes 性 (C1) 设 $\alpha > 0^{*}, \beta \in \mathbb{R}$. 有正整数 $n$ 使得 $n\alpha > \beta$. 具体地, 可取 $p, q$ 满足 $0^{*} < p^{*} < \alpha$ 及 $q^{*} > \beta$. 由 $\mathbb{Q}$ 中的 Archimedes 性, 存在正整数 $n$ 使得 $np > q$. 从而 $n\alpha \geqslant np^{*} = (np)^{*} > q^{*} > \beta$.

---

32

第二章 实数

8. 负元 (A4) 对于 $\alpha \in \mathbb{R}$, 存在 $\alpha$ 的负元. 具体地, 令 $E := \{\gamma | \gamma + \alpha \leqslant 0^*\}$. 任取 $s > 0$, 有 $p$ 使得 $p^* < \alpha < (p + s)^*$. 于是, $\alpha + (-p - s)^* \leqslant 0^*$. 因此 $(-p - s)^* \in E$. 而对任何 $\gamma \in E$, 我们有 $\gamma + p^* \leqslant \gamma + \alpha \leqslant 0^*$. 从而 $\gamma \leqslant (-p)^*$. 这样 $\beta := \sup E$ 是合理定义的, 且 $(-p - s)^* \leqslant \beta \leqslant (-p)^*$. 我们有

$$
\alpha + \beta \leqslant (p + s) ^ {*} + (- p) ^ {*} = s ^ {*},
$$

$$
0 = p ^ {*} + (- p - s) ^ {*} + s ^ {*} \leqslant \alpha + \beta + s ^ {*}.
$$

由推论2.3.4以及反对称性得到 $\alpha +\beta = 0^{*}$

## IV. 在 $\mathbb{R}$ 中定义乘法

1. 乘法的定义 对于 $\alpha, \beta > 0^{*}$, 定义 $\alpha \beta := \sup M_{\alpha, \beta}$, 其中

$$
M _ {\alpha , \beta} := \left\{\left(p q\right) ^ {*} \mid 0 ^ {*} <   p ^ {*} \leqslant \alpha , 0 ^ {*} <   q ^ {*} \leqslant \beta \right\}. \tag {2.3.6}
$$

易见 $M_{\alpha, \beta}$ 非空有上界. 从而 $\alpha \beta$ 是合理定义的.

对于其他情形, 补充定义

$$
\alpha \beta := \left\{ \begin{array}{l l} 0 ^ {*}, & \alpha = 0 ^ {*} \text {或} \beta = 0 ^ {*}, \\ - ((- \alpha) \beta), & \alpha <   0 ^ {*}, \beta > 0 ^ {*}, \\ - (\alpha (- \beta)), & \alpha > 0 ^ {*}, \beta <   0 ^ {*}, \\ (- \alpha) (- \beta), & \alpha <   0 ^ {*}, \beta <   0 ^ {*}. \end{array} \right. \tag {2.3.7}
$$

2. $\mathbb{Q}$ 与 $\mathbb{Q}^*$ 中乘法的一致性 当 $p, q > 0$ 时, 易见 $(pq)^*$ 是 $M_{p^*, q^*}$ 的最大值. 因此

$$
(p q) ^ {*} = p ^ {*} q ^ {*}. \tag {2.3.8}
$$

结合 (2.3.7) 式可见 (2.3.8) 式对任何有理数 $p, q$ 成立.

3. 乘法交换律 (M2) 成立 $\alpha \beta = \beta \alpha$. 若 $\alpha, \beta > 0^*$, 则 $M_{\alpha, \beta} = M_{\beta, \alpha}$, 从而结论成立. 一般情形的结果结合 (2.3.7) 式得到.
4. 乘法单位元 (M3) 成立 $\alpha \cdot 1^{*} = \alpha$. 若 $\alpha > 0^{*}$, 易见 $M_{\alpha,1^{*}} = \{p^{*} | 0^{*} < p^{*} \leqslant \alpha\}$. 于是由 (2.3.3) 式可得 $\alpha \cdot 1^{*} = \alpha$. 一般情形的结果结合 (2.3.7) 式得到.
5. 乘法保序性 (MO) 若 $\alpha, \beta \geqslant 0^{*}$, 则 $\alpha \beta \geqslant 0^{*}$. 这可由定义立即得到.

进一步, 若 $\alpha > 0^{*}, \beta \geqslant \gamma > 0^{*}$, 则 $M_{\alpha, \gamma} \subseteq M_{\alpha, \beta}$, 从而 $\alpha \beta \geqslant \alpha \gamma$.

6. 分配率 (AM) 成立 $\alpha (\beta +\gamma) = \alpha \beta +\alpha \gamma$ . 若记 $\delta = -(\beta +\gamma)$ ，则 $\beta +\gamma +\delta = 0^{*}$ 由乘法定义，即要证明

$$
\alpha \beta + \alpha \gamma + \alpha \delta = 0 ^ {*}. \tag {2.3.9}
$$

若 $\alpha, \beta, \gamma, \delta$ 之一为 $0^{*}$, 则直接从乘法定义可见 (2.3.9) 式成立. 因此, 我们只需考虑 $\alpha, \beta, \gamma, \delta$ 全不为 $0^{*}$ 的情形. 进一步, 只需考虑 $\alpha, \beta, \gamma > 0^{*}$ 的情形. 取 $u^{*} > \alpha, \beta, \gamma$.

---

2.3 实数系的构造

33

则对任何 $0 < s < u$ ，由引理2.3.2，有 $p, q, r \geqslant 0$ 满足(2.3.5)式. 易见

$$
(p + s) (q + r + 2 s) \leqslant p (q + r) + 6 u s.
$$

上式结合保序性立即得到

$$
\begin{array}{l} \alpha (\beta + \gamma) \leqslant p ^ {*} q ^ {*} + p ^ {*} r ^ {*} + (6 u s) ^ {*} \leqslant \alpha \beta + \alpha \gamma + (6 u s) ^ {*}, \\ \alpha \beta + \alpha \gamma \leqslant p ^ {*} (q ^ {*} + r ^ {*}) + (6 u s) ^ {*} \leqslant \alpha (\beta + \gamma) + (6 u s) ^ {*}. \\ \end{array}
$$

由推论2.3.4以及反对称性得到 $\alpha (\beta +\gamma) = \alpha \beta +\alpha \gamma$ 即(2.3.9)式成立

7. 乘法结合律 (M1) 成立乘法结合律 $\alpha (\beta \gamma) = (\alpha \beta)\gamma$. 为此, 只需对 $\alpha, \beta, \gamma > 0^{*}$ 的情形加以证明. 取 $u^{*} > \alpha, \beta, \gamma$. 对任何 $0 < s < u$, 有 $p, q, r \geqslant 0$ 满足 (2.3.5) 式. 此时

$$
(p + s) (q + s) (r + s) \leqslant p q r + 7 u ^ {2} s.
$$

上式结合保序性立即得到

$$
\begin{array}{l} \alpha (\beta \gamma) \leqslant (p ^ {*} q ^ {*}) r ^ {*} + (7 u ^ {2} s) ^ {*} \leqslant (\alpha \beta) \gamma + (7 u ^ {2} s) ^ {*}, \\ (\alpha \beta) \gamma \leqslant p ^ {*} (q ^ {*} r ^ {*}) + (7 u ^ {2} s) ^ {*} \leqslant \alpha (\beta \gamma) + (7 u ^ {2} s) ^ {*}. \\ \end{array}
$$

由推论2.3.4以及反对称性得到 $\alpha (\beta \gamma) = (\alpha \beta)\gamma$

8. 逆元 (M4) 对于 $\alpha \neq 0^{*}$, 存在 $\alpha$ 的逆元. 首先, 设 $\alpha > 0^{*}$, 我们有 $r$ 使得 $0^{*} < r^{*} < \alpha$. 考虑 $E := \{\gamma | 0^{*} < \gamma \alpha \leqslant 1^{*}\}$. 任取 $s > 0$. 由引理2.3.2, 有 $p \geqslant r$ 使得 $p^{*} < \alpha < (p + s)^{*}$. 从而由乘法保序性可得 $0^{*} < \alpha \left(\frac{1}{p + s}\right)^{*} \leqslant 1^{*}$, 因此, $\left(\frac{1}{p + s}\right)^{*} \in E$.

另一方面, 对任何 $\gamma \in E$, 我们有 $\gamma p^{*} \leqslant \gamma \alpha \leqslant 1^{*}$. 因此, $\gamma \leqslant \left(\frac{1}{p}\right)^{*}$. 这样 $\beta := \sup E$ 存在且 $\left(\frac{1}{p + s}\right)^{*} \leqslant \beta \leqslant \left(\frac{1}{p}\right)^{*}$. 进而

$$
\begin{array}{l} \alpha \beta \leqslant (p + s) ^ {*} \left(\frac {1}{p}\right) ^ {*} \leqslant 1 ^ {*} + \left(\frac {s}{r}\right) ^ {*}, \\ 1 ^ {*} = p ^ {*} \left(\frac {1}{p + s}\right) ^ {*} + \left(\frac {s}{p + s}\right) ^ {*} \leqslant \alpha \beta + \left(\frac {s}{r}\right) ^ {*}. \\ \end{array}
$$

由推论2.3.4以及反对称性得到 $\alpha \beta = 1^{*}$

若 $\alpha < 0^{*}$. 则 $-\frac{1}{(-\alpha)}$ 为 $\alpha$ 的逆元.

V. 完备性 (C2) 设 $\widetilde{\mathbb{R}} \supseteq \mathbb{R}$ 且 $(\widetilde{\mathbb{R}}, +, \cdot, \leqslant)$ 满足 (F), (O) 以及 (C1). 我们要证 $\widetilde{\mathbb{R}} = \mathbb{R}$.

首先, 我们来说明 $\mathbb{R}$ 的零元 $0^{*}$ 和单位元 $1^{*}$ 就是 $\widetilde{\mathbb{R}}$ 的零元 $\tilde{\theta}$ 和单位元 $\tilde{I}$. 为此, 设 $0^{*}$ 在 $\widetilde{\mathbb{R}}$ 中的负元为 $\tilde{\gamma}$. 则

$$
\tilde {\theta} = 0 ^ {*} + \tilde {\gamma} = (0 ^ {*} + 0 ^ {*}) + \tilde {\gamma} = 0 ^ {*} + (0 ^ {*} + \tilde {\gamma}) = 0 ^ {*} + \tilde {\theta} = 0 ^ {*}.
$$

---

34

第二章 实数

因此, $0^{*}$ 就是 $\widetilde{\mathbb{R}}$ 的零元. 特别地, $1^{*}$ 不是 $\widetilde{\mathbb{R}}$ 的零元, 从而它在 $\widetilde{\mathbb{R}}$ 中有逆元 $\tilde{\beta}$. 类似地, 我们有

$$
\tilde {I} = \tilde {\beta} \cdot 1 ^ {*} = \tilde {\beta} \cdot (1 ^ {*} \cdot 1 ^ {*}) = (\tilde {\beta} \cdot 1 ^ {*}) \cdot 1 ^ {*} = \tilde {I} \cdot 1 ^ {*} = 1 ^ {*}.
$$

即  $1^{*}$  是  $\widetilde{R}$  的单位元.

任取 $\tilde{\sigma} \in \widetilde{\mathbb{R}}$. 由 (C1), 存在正整数 $n$ 使得 $n^{*} > \tilde{\sigma}$ 以及 $n^{*} > -\tilde{\sigma}$. 因此, $\tilde{\sigma} > -n^{*}$.

现在令 $E := \{\alpha \in \mathbb{R} | \alpha \leqslant \tilde{\sigma}\}$. 则 $E$ 是 $\mathbb{R}$ 中的非空上有界集. 因此, 它在 $\mathbb{R}$ 中有上确界 $\beta = \sup_{\mathbb{R}} E$.

如果 $\tilde{\sigma} >\beta$ ，则 $\tilde{\sigma} -\beta >0^{*}$ .由(C1)，存在正整数 $m$ 使得 $m(\tilde{\sigma} -\beta) > 1^{*} = m\cdot \left(\frac{1}{m}\right)^{*}$ 于是，由(MO)易得 $\tilde{\sigma} -\beta \geqslant \left(\frac{1}{m}\right)^{*}$ .即 $\tilde{\sigma}\geqslant \left(\frac{1}{m}\right)^{*} + \beta .$ 所以 $\left(\frac{1}{m}\right)^{*} + \beta \in E.$ 这与 $\beta$ 为 $E$ 在 $\mathbb{R}$ 中的上确界矛盾.

类似地, 如果 $\tilde{\sigma} < \beta$, 则 $\beta - \tilde{\sigma} > 0^{*}$. 由 (C1), 存在正整数 $m$ 使得 $m(\beta - \tilde{\sigma}) > 1^{*}$. 这蕴涵了对任何 $\gamma \in E$, 成立 $\beta - \left(\frac{1}{m}\right)^{*} \geqslant \tilde{\sigma} \geqslant \gamma$. 同样与 $\beta$ 的定义矛盾.

因此, $\tilde{\sigma} = \beta$. 这就证明了 $\tilde{\mathbb{R}} = \mathbb{R}$, 即 (C2) 成立.

至此, 我们完成了实数系的构造. 接下来, 有理数的称呼将用于称呼有理分割, 而将无理分割称为无理数.

等价于上确界存在定理, 我们有下确界存在定理:

定理 2.3.5 R 中任何非空下有界集均有下确界.

若非空集 $E$ 无上界, 则记 $\sup E = +\infty$, 若 $E$ 无下界, 则记 $\inf E = -\infty$. 易见, 对于非空集 $E, F$, 我们有

$$
\inf E \leqslant \sup E, \tag {2.3.10}
$$

以及

$$
E \subseteq F \Longrightarrow \inf F \leqslant \inf E, \quad \sup E \leqslant \sup F. \tag {2.3.11}
$$

另一方面, 通常规定 $\sup \varnothing = -\infty, \inf \varnothing = +\infty$. 我们看到对于空集, (2.3.10) 式不成立. 构造实数系的其他典型方法

Weierstrass $^{①}$ 很早就认识到, 要使分析具备牢靠的基础, 必须建立严格的实数理论. 他于 1857 年开始讲授解析函数论等课程, 总要在第一阶段花很多时间阐明他关于实数的理论. 稍后, Méray $^{②}$, Cantor, Dedekind 以及 Heine $^{③}$ 分别于 1869, 1871, 1872, 1872 年各自独立地给出了无理数的定义, 建立了严格的实数理论.

历史上, Wallis $^{④}$ 于 1696 年将有理数与无限循环小数等同, 而 Stolz $^{⑤}$ 则于 1886 年提出将十进制无限非循环小数作为无理数的定义, 但未建立起一个满意的实数理论. 如今, 人们知道在小

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Weierstrass, Karl Theodor Wilhelm, 1815 年 10 月 31 日—1897 年 2 月 19 日, 德国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Méray, Hugues Charles Robert, 1835 年 11 月 12 日—1911 年 2 月 2 日, 法国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">③ Heine, Heinrich Eduard, 1821 年 3 月 16 日—1881 年 10 月 21 日, 德国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">④ Wallis, John, 1616 年 11 月 23 日—1703 年 10 月 28 日, 英国数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">⑤ Stolz, Otto, 1842 年 7 月 3 日—1905 年 11 月 23 日, 奥地利数学家.</span></small>

---

2.4 实数系一些概念的回顾

35

数中先引入序, 在此基础上建立上确界定理, 再来定义加法和乘法, 同样不难用小数来构造实数. 只是这一构造过程不如人们所期望的那么简捷. 有兴趣的读者也可以对本节用 Dedekind 分割构造实数的过程略加改写, 就可以得到用小数构造实数的过程.

从有理数扩充到实数, 以 Weierstrass, Dedekind 和 Cantor 的工作最具代表性. 关于它们的简单介绍, 读者可以参见文献 [41, 43].

## 实数系的唯一性

人们用多种方法建立了实数系, 那么不同的方法会不会构造出本质上不同的实数系来呢? 很幸运, 回答是否定的. 事实上, 若用其他方法建立了一个实数系 $(\mathbb{R}^{*}, \oplus, \otimes, \preceq)$, 即它满足实数系公理 (F), (O) 和 (C), 则 $(\mathbb{R}^{*}, \oplus, \otimes, \preceq)$ 必然与之前构造的实数系 $(\mathbb{R}, +, \cdot, \leqslant)$ 序同构. 即存在一个双射 $T: \mathbb{R} \to \mathbb{R}^{*}$ 使得

(1)  $\forall x, y \in R, T(x + y) = T(x) \oplus T(y)$  成立;
(2)  $\forall x, y \in R, T(x \cdot y) = T(x) \otimes T(y)$  成立;
(3) 若 $x \in \mathbb{R}, x \geqslant 0$, 则 $T(x) \geqslant \theta$, 这里 $\theta$ 表示 $\mathbb{R}^*$ 中的零元.

由上述性质, 可以看到 $\mathbb{R}$ 中元素之间的四则运算、序关系与对应的元素在 $\mathbb{R}^*$ 中的四则运算、序关系完全一样. 而实数的其他即将引入的运算都是在序和四则运算的基础上引入的. 所以可以把 $\mathbb{R}$ 和 $\mathbb{R}^*$ 看作是一样的. 这样的 $T$ 称为“序同构”.

有兴趣的读者可参见文献[41,43].

## 2.4 实数系一些概念的回顾

基于已经建立的实数理论, 我们对实数的 $p$ 进制表示、算术几何不等式、基本初等函数的定义等作一个回顾.

## 实数的十进制表示

对于实数 $x$, 称 $[x] := \max \{n \in \mathbb{Z} | n \leqslant x\}$ 为 $x$ 的整数部分, 称 $\{x\} := x - [x]$ 为 $x$ 的小数部分. 请读者说明它们定义的合理性.

接下来, 我们来引入十进制小数.

首先, 对于实数 $x \geqslant 0$, 令 $m := [x]$, 以及对于整数 $k \geqslant 1$, 称

$$
a _ {k} := [ 1 0 ^ {k} x ] - 1 0 \cdot [ 1 0 ^ {k - 1} x ]
$$

为 x 的十进制小数的第 k 位小数. 此时,  $a_{k}$  取值于  $0,1,2,\cdots,9$ , 且成立

$$
x = \sup _ {k \geqslant 1} \left(m + \frac {a _ {1}}{1 0} + \frac {a _ {2}}{1 0 ^ {2}} + \dots + \frac {a _ {k}}{1 0 ^ {k}}\right). \tag {2.4.1}
$$

我们记 $x = m.a_{1}a_{2}\dots a_{k}\dots$ ，并称之为 $x$ 的十进制表示.而称 $-m.a_1a_2\dots a_k\dots$ 为 $-x$ 的十进制表示.

---

36

第二章 实数

一般地, 若对某个 $k \geqslant 1$, 当 $j \geqslant k$ 时, 总有 $a_{j} = 0$, 则简记 $m.a_{1}a_{2} \cdots a_{k} \cdots$ 为 $m.a_{1}a_{2} \cdots a_{k-1}$. 相应实数称为有限小数.

若存在正整数 $n$, 以及某个 $k \geqslant 1$, 使得当 $j \geqslant k$ 时成立 $a_{j+n} = a_j$, 则记 $m.a_1a_2 \cdots a_k \cdots = m.a_1 \cdots a_{k-1}\dot{a}_k\dot{a}_{k+1} \cdots\dot{a}_{k+n-1}$ 并称 $a_k a_{k+1} \cdots a_{k+n-1}$ 为 (长为 $n$ 的) 循环节.

另一方面, 对于非负实数 $m$ 以及取值于 $0,1,2,\cdots,9$ 的 $a_1,a_2,\cdots,m.a_1a_2\cdots a_k\cdots$ 是否给出了一个实数? 按上确界存在定理, 不难看到, 可由 (2.4.1) 式给出一个实数. 问题是这一实数的小数表示是否就是 $m.a_1a_2\cdots a_k\cdots$?

容易证明, 当且仅当 9 不是 $m.a_{1}a_{2}\cdots a_{k}\cdots$ 的循环节时, 回答是肯定的.

但时常, 当 $m.a_{1}a_{2}\cdots a_{k}\cdots$ 以9为循环节时, 我们认为它就是按(2.4.1)式得到的实数. 这样, $0.\dot{9}=1$. 而有限小数都会有两个不同的表示, 一个是有限小数的形式, 另一个是以9为循环节的形式. 这在讨论中需要引起注意.

## 实数的 $p$ 进制表示

同样, 对于整数 $p \geqslant 2$, 可以定义实数的 $p$ 进制表示.

考虑 $x \geqslant 0$. 若 $x \leqslant 1$, 令 $N \equiv N_x := 0$. 若 $x > 1$, 由二项展开式, 对于 $n = [x] + 1$, 可得 $p^n \geqslant (p - 1 + 1)^n \geqslant n > x$. 因此, 注意到 $p^0 = 1 < x$, 此时可定义 $N \equiv N_x$ 为使得 $p^n \geqslant x$ 的最小整数 $n$. 即 $N$ 满足 $p^{N-1} < x \leqslant p^N$. 对于整数 $k \leqslant N$, 定义①

$$
a _ {k} := [ p ^ {- k} x ] - p \cdot [ p ^ {- k - 1} x ].
$$

则

$$
x = \sup _ {- \infty <   m \leqslant N} \sum_ {k = m} ^ {N} a _ {k} p ^ {k} = \sup _ {m \geqslant 1} \Big (\sum_ {k = 0} ^ {N} a _ {k} p ^ {k} + \sum_ {j = 1} ^ {m} \frac {a _ {- j}}{p ^ {j}} \Big). \tag {2.4.2}
$$

我们记 $x = a_{N}a_{N - 1}\dots a_{0}.a_{-1}a_{-2}\dots a_{-k}\dots_{p}$ ，并称之为 $x$ 的 $p$ 进制表示.而称 $x = -a_{N}a_{N - 1}\dots a_{0}.a_{-1}a_{-2}\dots a_{-k}\dots_{p}$ 为 $-x$ 的 $p$ 进制表示.

由于我们熟悉十进制表示. 当 p > 10 时, 采用上述表述方法, 就需要引入新的字符表示  $10, 11, \cdots, p - 1$ . 自然很不方便. 今后, 我们可以把 (2.4.2) 式中的 x 表示成无穷级数

$$
x = \sum_ {k = - \infty} ^ {N} a _ {k} p ^ {k} = \sum_ {k = 0} ^ {N} a _ {k} p ^ {k} + \sum_ {j = 1} ^ {\infty} \frac {a _ {- j}}{p ^ {j}}. \tag {2.4.3}
$$

对于 $p$ 进制数, 同样可以定义循环节. 时常, 若循环节为 $p - 1$, 则按 (2.4.2) 式来定义该数.

不难看到, $p$ 进制下的有限小数不见得是十进制下的有限小数. 反之亦然. 但 $p$ 进制下的有限小数或无限循环小数一定也是十进制下的有限小数或无限小数, 反之亦然. 事实上, 对任何整数 $p \geqslant 2$, $p$ 进制下的有限小数和无限循环小数的全体就是所有有理数.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 上面定义实数的十进制表示, 也应该如此处理整数部分.</span></small>

---

2.4 实数系一些概念的回顾

37

## $n$ 次方根

有了上确界存在定理, 我们可以定义 n 次方根.

定理 2.4.1 设 a > 0 ，而 n 为正整数，则方程  $x^{n} = a$  有唯一的正解.

证明 由于 $t > s > 0$ 蕴涵 $t^n > s^n$, 因此, 方程 $x^n = a$ 的正解若存在, 必然唯一.

现考虑集合  $E_{a} := \{y | y > 0, y^{n} \leqslant a\}$ .

取 $s = \frac{a}{1 + a}$, 则 $0 < s < 1$, 从而 $s^n < s < a$, 即 $s \in E_a$, 因此 $E_a$ 非空. 另一方面, $(1 + a)^n \geqslant 1 + a > a$, 因此 $1 + a$ 是 $E_a$ 的一个上界. 这样, $x := \sup E_a$ 存在且 $\frac{a}{1 + a} \leqslant x \leqslant 1 + a$. 下证 $x^n = a$.

若 $x^n < a$ ，取 $\varepsilon = \frac{a - x^n}{(2 + a)^n}$ ，则 $\varepsilon \in (0,1)$ ，从而

$$
(x + \varepsilon) ^ {n} = \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} \varepsilon^ {k} x ^ {n - k} \leqslant x ^ {n} + \varepsilon \sum_ {k = 1} ^ {n} \mathrm{C} _ {n} ^ {k} x ^ {k} <   x ^ {n} + \varepsilon (2 + a) ^ {n} = a.
$$

所以 $x + \varepsilon \in E_a$ ，与 $x$ 为 $E_{a}$ 的上确界矛盾.

若 $x^n > a$. 取 $\varepsilon = \frac{x^n - a}{(2 + a)^n}$, 则 $0 < \varepsilon < 1$ 且 $x - \varepsilon > 0$. 进一步,

$$
(x - \varepsilon) ^ {n} = \sum_ {k = 0} ^ {n} \mathrm{C} _ {n} ^ {k} (- \varepsilon) ^ {k} x ^ {n - k} \geqslant x ^ {n} - \varepsilon \sum_ {k = 1} ^ {n} \mathrm{C} _ {n} ^ {k} x ^ {k} > x ^ {n} - \varepsilon (2 + a) ^ {n} = a.
$$

因此, $x - \varepsilon$ 是 $E_{a}$ 的一个上界, 与 $x$ 为 $E_{a}$ 的上确界矛盾.

这就证明了 $x^n = a$.

定义 2.4.1 设  $a \geqslant 0$ ，对于正整数  $n \geqslant 2$ ，称方程  $x^{n} = a$  的唯一非负实根为 a 的 n 次方根，记作  $a^{\frac{1}{n}}$  或  $\sqrt[n]{a}$ 。 $\sqrt[2]{a}$  简记为  $\sqrt{a}$ 。

## 实数指数幂

在 $n$ 次方根的基础上, 对于正数 $a$ 以及有理数 $q$, 我们可以定义 $a^q$ 并建立相应的性质. 另外, 也可以对某些特殊的 $q$, 当 $a = 0$ 或 $a < 0$ 时, 定义 $a^q$.

进一步, 可以定义实数指数幂与对数并建立相关性质. 具体细节参见本节习题 9\~15.

以上过程较为烦琐. 今后, 我们还将利用极限来定义实数指数幂与对数 (参见第五章第 5 节).

## 三角函数与反三角函数

我们称幂函数、指数函数、对数函数、三角函数与反三角函数为基本初等函数. 要从分析上严格地定义三角函数及反三角函数, 一般有三个途径: 利用定积分、利用微分方程以及利用极限或级数. 有兴趣的读者可参见文献 [43]. 在第五章第 5 节, 我们介绍如何用极限或级数来定义三角函数.

## 算术几何平均不等式

接下来, 建立如下的算术几何平均不等式.

---

38

第二章 实数

命题 2.4.2 设  $n \geqslant 2, a_{1}, a_{2}, \cdots, a_{n} \geqslant 0$ ，则

$$
\sqrt [ n ]{\prod_ {k = 1} ^ {n} a _ {k}} \leqslant \frac {1}{n} \sum_ {k = 1} ^ {n} a _ {k}. \tag {2.4.4}
$$

且等号成立当且仅当  $a_{1}=a_{2}=\cdots=a_{n}$ .

不等式左端称为  $a_{1}, a_{2}, \cdots, a_{n}$  的几何平均，右端称为  $a_{1}, a_{2}, \cdots, a_{n}$  的算术平均.

证明 我们分三步加以证明.

(i) $n = 2$ 的情形. 设 $a_1, a_2 \geqslant 0$, 则

$$
a _ {1} - 2 \sqrt {a _ {1} a _ {2}} + a _ {2} = (\sqrt {a _ {1}} - \sqrt {a _ {2}}) ^ {2} \geqslant 0.
$$

从而 (2.4.4) 式成立, 且等号成立当且仅当 $a_1 = a_2$.

(ii)  $n = 2^{k} \quad (k \geqslant 1)$  的情形. 设对某个  $k \geqslant 1$ , 当  $n = 2^{k}$  时命题 2.4.2 成立. 记  $m = 2^{k}$ . 则对于  $a_{1}, a_{2}, \cdots, a_{2m} \geqslant 0$ , 我们有

$$
\sqrt [ 2 m ]{\prod_ {j = 1} ^ {2 m} a _ {j}} = \sqrt [ m ]{\prod_ {j = 1} ^ {m} \sqrt {a _ {j} a _ {m + j}}} \leqslant \frac {1}{m} \sum_ {j = 1} ^ {m} \sqrt {a _ {j} a _ {m + j}},
$$

且等号成立当且仅当  $a_{1}a_{m+1}=a_{2}a_{m+2}=\cdots=a_{m}a_{2m}$ . 由 (i),

$$
\frac {1}{m} \sum_ {j = 1} ^ {m} \sqrt {a _ {j} a _ {m + j}} \leqslant \frac {1}{2 m} \sum_ {j = 1} ^ {2 m} a _ {j},
$$

且等号成立当且仅当 $a_1 = a_{m + 1},a_2 = a_{m + 2},\dots ,a_m = a_{2m}$ 都成立.总之，

$$
\sqrt [ 2 m ]{\prod_ {j = 1} ^ {2 m} a _ {j}} \leqslant \frac {1}{2 m} \sum_ {j = 1} ^ {2 m} a _ {j},
$$

且等号成立当且仅当  $a_{1}=a_{2}=\cdots=a_{2m}$ . 即命题 2.4.2 当  $n=2^{k+1}$  时也成立.

结合 (i), 由数学归纳法得到对任何 $k \geqslant 1$, 命题2.4.2当 $n = 2^k$ 时成立.

(iii)  $n \geqslant 2$  的一般情形. 一般地, 对于  $n \geqslant 2$ , 有  $k \geqslant 1$  使得  $2^{k} \leqslant n < 2^{k+1}$ . 记  $m = 2^{k}$ , 由 (ii), 不妨设 m < n < 2m. 对于  $a_{1}, a_{2}, \cdots, a_{n} \geqslant 0$ , 令  $A = \frac{1}{n} \sum_{j=1}^{n} a_{j}$ . 当 A = 0 时,  $a_{1} = a_{2} = \cdots = a_{n} = 0$ , 命题自然成立. 下设 A > 0. 令  $a_{n+1} = a_{n+2} = \cdots = a_{2m} = A$ , 我们有

$$
\sqrt [ n ]{\prod_ {j = 1} ^ {n} a _ {j}} = \frac {1}{A ^ {\frac {2 m - n}{n}}} \left[ \left(\prod_ {j = 1} ^ {2 m} a _ {j}\right) ^ {\frac {1}{2 m}} \right] ^ {\frac {2 m}{n}} \leqslant \frac {1}{A ^ {\frac {2 m - n}{n}}} \left(\frac {1}{2 m} \sum_ {j = 1} ^ {2 m} a _ {j}\right) ^ {\frac {2 m}{n}} = A,
$$

---

习题2

39

且等号成立当且仅当  $a_{1}=a_{2}=\cdots=a_{n}=A$ . 这就证明了命题.

## Young 不等式

我们来把算术几何平均不等式推广为 Young $^{①}$ 不等式. 若 $1 \leqslant p, q \leqslant +\infty$ 满足 $\frac{1}{p} + \frac{1}{q} = 1$, 则称 p, q 为对偶数.

定理 2.4.3 设 $p,q \in  \left( {1, + \infty }\right)$ 为对偶数. 则对任何 $a,b > 0$ ,有 ${}^{\text{②}}$

$$
a b \leqslant \frac {1}{p} a ^ {p} + \frac {1}{q} b ^ {q}. \tag {2.4.5}
$$

证明 令 $A = \frac{a}{(ab)^{\frac{1}{p}}}$. 则 $\frac{b}{(ab)^{\frac{1}{q}}} = \frac{1}{A}$. 因此, (2.4.5) 式等价于

$$
1 \leqslant \frac {1}{p} A ^ {p} + \frac {1}{q} \frac {1}{A ^ {q}}. \tag {2.4.6}
$$

不妨设 $A \geqslant 1$. 任取 $m > p$. 令 $k = \left[\frac{m}{p}\right] + 1$. 则 $\frac{1}{p} \leqslant \frac{k}{m} \leqslant \frac{1}{p} + \frac{1}{m}, \frac{1}{q} \geqslant \frac{m - k}{m}$. 从而利用算术几何平均不等式, 可得

$$
\begin{array}{l} \frac {1}{m} A ^ {p} + \frac {1}{p} A ^ {p} + \frac {1}{q} \frac {1}{A ^ {q}} \geqslant \frac {k}{m} A ^ {\frac {m}{k}} + \frac {m - k}{m} \frac {1}{A ^ {\frac {m}{m - k}}} \\ \geqslant \left(\left(A ^ {\frac {m}{k}}\right) ^ {k} \left(\frac {1}{A ^ {\frac {m}{m - k}}}\right) ^ {m - k}\right) ^ {\frac {1}{m}} = 1. \\ \end{array}
$$

由 m > p 的任意性即得 (2.4.6) 式. 定理得证.

利用 Young 不等式易得如下定理.

定理 2.4.4 设  $x \geqslant 0$ ，则

$$
(1 + x) ^ {\alpha} - 1 \leqslant \alpha x, \quad \forall \alpha \in (0, 1 ], x \geqslant 0. \tag {2.4.7}
$$

$$
(1 + x) ^ {\alpha} - 1 \geqslant \alpha x, \quad \forall \alpha \geqslant 1, x \geqslant 0. \tag {2.4.8}
$$

$$
(1 + x) ^ {\alpha} - 1 \geqslant \frac {\alpha x}{1 + x}, \quad \forall \alpha \geqslant 0, x \geqslant 0. \tag {2.4.9}
$$

进一步，以上三个不等式是等价的.

## 习题2

1. 证明: 对任何整数 $p \geqslant 2, p$ 进制下的有限小数和无限循环小数的全体就是所有有理数.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Young, William Henry, 1863 年 10 月 20 日—1942 年 7 月 7 日, 英国数学家. Young, Grace Chisholm, 1868 年 3 月 15 日—1944 年 3 月 29 日, 英国数学家. 两者为夫妻, 合作进行数学研究.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② 今后可以证明 (2.4.5) 式中, 等号成立当且仅当 $a = b^{q - 1}$.</span></small>

---

40

第二章 实数

2. Rudin 在其《数学分析原理》 $^{[52]}$  一书中使用了变换  $q = p + \frac{2 - p^{2}}{p + 2} = \frac{2 + 2p}{p + 2}$ . 验证:

(1) 若 p > 0, 且  $p^{2} < 2$ , 则 q > p 且  $q^{2} < 2$ ;
(2) 若 p > 0, 且  $p^{2} > 2$ , 则 0 < q < p 且  $q^{2} > 2$ .

3. 试求使变换 $q = p + \frac{2 - p^2}{ap + b}$ 具有习题 2 中性质 (1)\~(2) 的所有有理数对 $(a, b)$.
4. 证明无理数在实数集中的稠密性: 对任何 $x \in \mathbb{R}$, 以及 $\varepsilon > 0$, 存在无理数 $y$ 使得 $|y - x| < \varepsilon$.
5. 设 $a > 0$, 而 $n$ 为正整数. 证明: $\min \{a, 1\} \leqslant a^{\frac{1}{n}} \leqslant \max \{a, 1\}$.
6. 设  $n \geqslant 2, \alpha_{1}, \alpha_{2}, \cdots, \alpha_{n} \geqslant 0$ ，满足  $\alpha_{1} + \alpha_{2} + \cdots + \alpha_{n} = 1$ 。证明:对于  $x_{1}, x_{2}, \cdots, x_{n} > 0$ ，有  $x_{1}^{\alpha_{1}} x_{2}^{\alpha_{2}} \cdots x_{n}^{\alpha_{n}} \leqslant \alpha_{1} x_{1} + \alpha_{2} x_{2} + \cdots + \alpha_{n} x_{n}$ 。
7. 证明定理 2.4.4.
8. 设 $I$ 是一个非空指标集, 对 $I$ 中每一个元 $\alpha$, 都对应两个实数 $x_{\alpha}$ 以及 $y_{\alpha}$. 我们习惯将 $\sup \{x_{\alpha} | \alpha \in I\}$ 和 $\inf \{x_{\alpha} | \alpha \in I\}$ 写成 $\sup_{\alpha \in I} x_{\alpha}$ 和 $\inf_{\alpha \in I} x_{\alpha}$. 证明: 在广义实数系中,

(1) $\inf_{\alpha \in I}(-x_{\alpha}) = -\sup_{\alpha \in I}x_{\alpha};$

(2) 对以下所列的每一个不等式:

$$
\begin{array}{l} \inf _ {\alpha \in I} x _ {\alpha} + \inf _ {\alpha \in I} y _ {\alpha} \leqslant \inf _ {\alpha \in I} (x _ {\alpha} + y _ {\alpha}) \leqslant \sup _ {\alpha \in I} x _ {\alpha} + \inf _ {\alpha \in I} y _ {\alpha} \\ \leqslant \sup _ {\alpha \in I} (x _ {\alpha} + y _ {\alpha}) \leqslant \sup _ {\alpha \in I} x _ {\alpha} + \sup _ {\alpha \in I} y _ {\alpha}, \\ \end{array}
$$

若其两端在广义实数系中都有意义, 则该不等式成立;

(3) 若 $x_{\alpha} > 0 (\forall \alpha \in I)$, 并在此种情形规定 $\frac{1}{0} = +\infty$, 我们有

$$
\sup _ {\alpha \in I} \frac {1}{x _ {\alpha}} = \frac {1}{\inf _ {\alpha \in I} x _ {\alpha}};
$$

(4) 设  $x_{\alpha} > 0, y_{\alpha} > 0 (\forall \alpha \in I)$ . 对以下所列的每一个不等式:

$$
\begin{array}{l} \inf _ {\alpha \in I} x _ {\alpha} \inf _ {\alpha \in I} y _ {\alpha} \leqslant \inf _ {\alpha \in I} (x _ {\alpha} y _ {\alpha}) \leqslant \sup _ {\alpha \in I} x _ {\alpha} \inf _ {\alpha \in I} y _ {\alpha}, \\ \leqslant \sup _ {\alpha \in I} (x _ {\alpha} y _ {\alpha}) \leqslant \sup _ {\alpha \in I} x _ {\alpha} \sup _ {\alpha \in I} y _ {\alpha}, \\ \end{array}
$$

若其两端在广义实数系中都有意义, 则该不等式成立.

9. 对于 $a > 0$ 以及有理数 $\frac{m}{n}$, 其中 $m, n$ 为既约整数, $n > 0$. 当 $m \neq 1$ 时, 定义

$$
a ^ {\frac {m}{n}} := \left(a ^ {m}\right) ^ {\frac {1}{n}}.
$$

自然, 当 $m = 1$ 时, 上式也成立. 进一步, 当 $n = 2k + 1$ 为奇数时, 定义

$$
\left(- a\right) ^ {\frac {m}{2 k + 1}} := \left(- 1\right) ^ {m} a ^ {\frac {m}{2 k + 1}}.
$$

---

习题2

41

下设 $a, b > 0$，且 $p, q$ 为有理数，证明:

(1) $(a^p)^q = a^{pq}$;

(2) $a^p a^q = a^{p + q}$;

(3) $a^p b^p = (ab)^p$;

(4) 若 a > 1, p > 0, 则  $a^{p} > 1$ ;

(5) 若 a > 1, 则  $a^{p}$  关于  $p \in Q$  严格单增;

(6) 设 $a > 1$, 对于任何 $b \in \mathbb{R}$, $\sup \{a^p | p < b\} = \inf \{a^p | p > b\}$ 成立.

10. 设  $a \geqslant 1$ ，且 b 为无理数，定义

$$
a ^ {b} := \sup \left\{a ^ {p} | p \leqslant b \right\}.
$$

证明: 当 b 为有理数时上式也成立.

进一步, 当 0 < a < 1 时, 定义  $a^{b} = (a^{-1})^{-b}$ .

11. 设 $a, b > 0$, 且 $x, y \in \mathbb{R}$, 证明:

(1) $(a^x)^y = a^{xy}$;
(2) $a^{x}a^{y}=a^{x+y};$
(3) $a^x b^x = (ab)^x$;

(4) 若 a > 1, x > 0, 则  $a^{x} > 1$ ;

(5) 若 a > 1, 则  $a^{x}$  关于  $x \in R$  严格单增;

(6) 若 0 < a < 1, 则  $a^{x}$  关于  $x \in R$  严格单减.

12. 设 $a > 0, a \neq 1, b > 0$, 证明有唯一的实数 $x$ 满足 $a^x = b$. 该实数称为以 $a$ 为底以 $b$ 为真数的对数. 记作 $\log_a b$. 在底 $a$ 明确的情况下, 可以简写为 $\log b$. $\log_{10} b$ 记作 $\lg b$, 称为常用对数, $\log_e b$ 记作 $\ln b$, 称为自然对数, 其中常数 $e$ 在3.3.2小节定义.

13. 设 $a, b, x > 0, a \neq 1, b \neq 1$. 证明: $\log_a x = \frac{\log_b x}{\log_b a}$.

14. 证明: 当 $a > 1$ 时, $\log_a x$ 关于 $x > 0$ 严格单增; 当 $0 < a < 1$ 时, $\log_a x$ 关于 $x > 0$ 严格单减.

15. 设 $a, x, y > 0, a \neq 1$, 证明: $\log_a(xy) = \log_a x + \log_a y$.
