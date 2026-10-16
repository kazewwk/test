自然界中的有些现象, 在某些条件下必然发生, 我们称之为确定性现象. 例如, 每天太阳会从东方升起, 无支撑的重物会从高处落下, 等等. 还有很多现象, 在条件给定的情况下是否发生并不确定. 例如, 掷一枚均匀硬币, 观察落下后是正面朝上还是反面朝上, 掷之前我们不能确定将会出现哪种情况. 又如, 某处某个时刻的气温, 事先我们无法知道确切的结果, 只有到了那个时刻测量后才能够知道. 这种在给定条件下是否发生具有不确定性的现象称为随机现象.

在本章中, 我们首先对随机试验、古典概型、几何概型等做简单的介绍. 在此基础上, 引入概率空间的概念, 定义条件概率, 证明全概率公式和贝叶斯公式, 并给出事件和试验的独立性等性质的严格数学描述. 作为对上述内容的扩展, 我们还将介绍抽象测度的概念和基本性质. 这些构成后面各章的理论基础.

## 1.1 随机试验和事件

## 1.1.1 随机试验

对于随机现象的观测和分析构成随机试验, 其基本特征是可以在相同的条件下多次重复, 且所有可能发生的结果构成的集合是确定不变的. 随机试验在大量重复试验中会表现出规律性.

例 1.1.1 连续投掷一枚质地均匀的硬币, 每次的结果是不确定的, 出现正面和反面的可能性均为 1/2. 用  $S_{n}$  表示前 n 次投掷中出现正面的次数. 根据经验, 当 n 很大时, 比值  $S_{n}/n$  总是很接近于一次投掷中正面出现的可能性 1/2, 从而显现出规律性. 这个规律可以利用本课程后面将要学习的大数定律给出严格的数学解释.

例 1.1.2 英国生物统计学家高尔顿 (Galton) 设计的钉板装置是用来研究随机现象的统计规律的模型。钉板结构如图 1.1 所示, 木板上钉有多层铁钉, 每层相邻铁钉间的距离相同, 且上层每颗钉的水平位置恰好位于下层两颗钉的正中间。从入口处放进一个直径略小于两钉距离的玻璃圆球, 圆球每次碰到铁钉后以 1/2 的概率向左或向右滚下, 直到滚到底部的某个格子内为止。把大量的圆球不断从入口处放下。当球的数目很大时, 它们会在底部堆成中间高两边低的形状, 从而显现出规律性。这个规律可利用本课程后面将要证明的中心极限定理给出严格的数学解释。

为了准确地描述随机现象, 我们需要使用集合论的语言和记号. 我们知道, 集合是由一些元素构成的总体, 其元素的个数可以是有限的, 也可以是可数无限或不可数无限的. 有限集和可数无限集统称为可数集. 由一个集合 $A$ 中的部分或全部元素构成的另一个集合 $B$ 称为 $A$ 的子集. 不包含任何元素的集合称为空集, 记作 $\varnothing$. 我们规定空集是任何集合的子集.

![](images/page_17_image_2.jpg)

<details>
<summary>natural_image</summary>

Diagram of a triangular structure with vertical columns and scattered dots, no text or symbols present
</details>

图 1.1 高尔顿钉板试验

本课程假定读者熟悉关于集合的基本概念, 运算和记号. 例如 $A = B$, $A \subseteq B$, $A \supseteq B$, $A \cap B$, $A \cup B$, $A \setminus B$ 等. 如果有一个明确的基本集合 $\Omega$, 对于子集 $A \subseteq \Omega$, 我们称 $\Omega \setminus A$ 为 $A$ 的补集或余集, 并将其记作 $A^c$.

某个随机试验所有可能的结果构成的 (非空) 集合称为它的样本空间, 通常用大写希腊字母 $\Omega$ 表示. 称 $\Omega$ 中的元素为样本点, 用小写希腊字母 $\omega$ 表示. 我们关心的随机事件可以用 $\Omega$ 的某些子集来表示. 某个随机事件 $A \subseteq \Omega$ 的概率是区间 $[0,1]$ 中的一个数 $\mathbf{P}(A)$, 它给出 $A$ 发生的可能性大小的描述. 我们称样本空间 $\Omega$ 为必然事件并规定 $\mathbf{P}(\Omega) = 1$, 而称空集 $\varnothing$ 为不可能事件并规定 $\mathbf{P}(\varnothing) = 0$. 事件 $A$ 的余集 $A^c$ 也称为它的对立事件, 显然 $\mathbf{P}(A) + \mathbf{P}(A^c) = 1$.

假设在一个随机试验中, 我们关心的仅仅是事件 $A \subseteq \Omega$ 是否发生, 并且已知 $\mathbf{P}(A) = p$ 和 $\mathbf{P}(A^c) = 1 - p$, 其中 $0 \leqslant p \leqslant 1$. 这样的随机试验称为伯努利 (Bernoulli) 试验. 在伯努利试验中, 事件 $A$ 发生称为成功, 事件 $A^c$ 发生称为失败. 对于伯努利试验, 为了简单我们可以将样本空间取为 $\Omega = \{1,0\}$, 其中 1 表示 $A$ 发生, 而 0 表示 $A^c$ 发生.

例 1.1.3 掷一枚硬币, 用 1 表示结果正面朝上, 用 0 表示反面朝上. 则试验的样本空间为  $\Omega = \{1, 0\}$ . 显然, 这是一种伯努利试验. 若硬币质地均匀, 则有  $\mathbf{P}(\{1\}) = \mathbf{P}(\{0\}) = 1/2$ .

例 1.1.4 投掷骰子试验的样本空间为  $\Omega = \{1, 2, 3, 4, 5, 6\}$ . 在这个随机试验中, 我们感兴趣的事件包括  $A = \{6\}, B = \{2, 4, 6\}$  等. 若骰子质地均匀, 则每个点数出现的概率均为 1/6.

例 1.1.5 记录一台电话交换机在某个时段内收到的呼唤次数。这个试验的样本空间可取为  $\Omega = \{0, 1, 2, \cdots\}$ .

例 1.1.6 射手连续向某个目标射击, 直至命中为止, 考虑射击的总次数. 这个试验的样本空间为  $\Omega = \{1, 01, 001, 0001, \cdots\}$ .

例1.1.7 观察北京夏季某日的最低气温 $x$ 和最高气温 $y$ (单位: ${}^{\circ}\mathrm{C}$). 这个试验的样本空间可取为 $\Omega = \{(x, y) : 0 < x \leqslant y < 50\}$.

考虑以 $\Omega$ 为样本空间的随机试验. 在这个随机试验中, 随机事件之间的基本关系

可以用集合的关系及运算描述. 具体地说, 若 $A \subseteq \Omega$ 和 $B \subseteq \Omega$ 是两个事件, 则我们有

$A \cap B$  表示 A 和 B 同时发生;

$A \cup B$  表示 A 和 B 中至少有一个发生;

$A \setminus B$  表示 A 发生但 B 不发生;

$A \subseteq B$  表示 A 发生则 B 发生.

为简单起见, 我们经常写 $A \cap B$ 为 $AB$. 显然 $AB = \varnothing$ 当且仅当 $A$ 和 $B$ 不同时发生, 此时称 $A$ 和 $B$ 互不相容或互斥. 我们称 $A$ 和 $A^c := \Omega \setminus A$ 互为对立事件. 注意, 有些教科书将对立事件 $A^c$ 写为 $\bar{A}$.

随机试验可以在相同的条件下重复多次, 多次重复试验构成联合随机试验. 假设我们进行了 $n$ 次重复伯努利试验, 用 $S_{n}$ 表示事件 $A$ 在这 $n$ 次试验中发生的次数. 对于 $0 \leqslant k \leqslant n$, 显然 “$S_{n} = k$” 或者 “事件 $A$ 发生 $k$ 次” 是上述联合随机试验中的随机事件. 所以 $S_{n}$ 的取值具有随机性. 我们称 $F_{n}(A) := S_{n}/n$ 为 $A$ 发生的频率. 不难看出, 频率有如下性质:

(1) 非负性:  $F_{n}(A) \geqslant 0;$
(2) 规范性:  $F_{n}(\Omega)=1;$
(3) 可加性: 若 $AB = \varnothing$, 则 $F_{n}(A \cup B) = F_{n}(A) + F_{n}(B)$.

根据实践经验, 当 $n$ 很大时, $F_{n}(A)$ 会稳定在事件 $A$ 发生的概率附近, 这个性质称为频率稳定性.

## 1.1.2 古典概率模型

当样本空间有限时, 我们可以自然地基于可能性假设建立一个概率模型. 这是最早研究的概率模型, 在概率论的发展中占有重要的地位. 由于这类模型比较简单, 它们非常有助于初学者理解概率论中的一些概念.

定义 1.1.1 若某个随机试验的样本空间  $\Omega$  只包含有限个样本点, 且各样本点出现的概率相等, 则称这个随机试验为古典概率模型, 简称古典概型. 分别记  $\Omega$  和其子集 A 中所包含的样本点的个数为  $n(A)$  和  $n(\Omega)$ . 则事件 A 发生的概率为

$$
\mathbf {P} (A) = \frac {n (A)}{n (\Omega)}. \tag {1.1.1}
$$

根据上述定义, 对于古典概型计算事件 $A$ 的概率, 关键是求出 $\Omega$ 中样本点的总数和 $A$ 中样本点的个数. 为此通常需要利用排列组合的工具, 而且往往有一定的技巧性. 对于整数 $n \geqslant m \geqslant 1$, 我们用 $\mathrm{A}_n^m$ 表示从 $n$ 个取 $m$ 个的所有排列数, 用 $\mathrm{C}_n^m$ 或 $\binom{n}{m}$ 表示从 $n$ 个取 $m$ 个的所有组合数, 即

$$
\mathrm{A} _ {n} ^ {m} = n (n - 1) \dots (n - m + 1), \quad \mathrm{C} _ {n} ^ {m} = \binom{n}{m} = \frac {n !}{m ! (n - m) !}.
$$

例 1.1.8 将一枚质量均匀的硬币重复投掷两次, 求出现正、反面各一次的概率.

解 用 1 表示结果正面朝上, 0 表示反面朝上. 则试验的样本空间为

$$
\Omega = \{(1, 1), (1, 0), (0, 1), (0, 0) \}.
$$

它总共有 4 个样本点. 再记事件 { 正、反面各一次 } 为 B. 则 $B = \{(1,0),(0,1)\}$, 它有 2 个样本点. 按照古典概型的概率计算公式, 有 $\mathbf{P}(B) = 2/4 = 1/2$. □

例 1.1.9 从连续整数 0 至 9 中无放回地取 3 个数依次排列, 利用古典概型计算 3 个数构成 3 位偶数的概率.

解 样本空间 $\Omega$ 可取为 0 至 9 这 10 个数中任意 3 个的所有排列, 它包含 $A_{10}^{3}$ 个样本点. 用 $B$ 表示事件 $\{3$ 个数形成 3 位偶数 $\}$. 考虑到三位偶数的百位数不能够为 0, 事件 $B$ 发生可分为如下两种情况: (i) 第 3 个数为 0 而第 1 和第 2 个数为 $\{1,2,\cdots,9\}$ 这 9 个数中任意 2 个数的排列; (ii) 第 3 个数为 $\{2,4,6,8\}$ 中的某个数 $c$, 第 1 个数为 $\{1,2,\cdots,9\} \setminus \{c\}$ 这 8 个数中的某个数 $a$, 而第 2 个数为 $\{0,1,2,\cdots,9\} \setminus \{a,c\}$ 这 8 个数中的某个数 $b$. 根据这样的考虑, 我们有

$$
\mathbf {P} (B) = \frac {\mathrm{A} _ {9} ^ {2} + 4 \times 8 \times 8}{\mathrm{A} _ {1 0} ^ {3}} = \frac {9 \times 8 + 4 \times 8 \times 8}{1 0 \times 9 \times 8} = \frac {9 + 4 \times 8}{1 0 \times 9} = \frac {4 1}{9 0}.
$$

例 1.1.10 (生日问题) 假定一年为 365 天. 利用古典概型计算  $r (1 \leqslant r \leqslant 365)$  个人生日互不相同的概率.

解 记 $B = \{r$ 个人生日互不相同}. 则

$$
\mathbf {P} (B) = \frac {\mathrm{C} _ {3 6 5} ^ {r} \cdot r !}{3 6 5 ^ {r}}.
$$

特别地, 当 $r = 55$ 时, 可算得 $\mathbf{P}(B) = 0.01$. 这个概率很小, 直观上有些意外!

例 1.1.11 袋子中有 r 个红球和 b 个黑球. 现将球依次取出, 求  $R_{k}=\{ 第 k 次取到红球 \}$  的概率.

解 (1) 同色球可辨. 将球依次取出相当于把 $r + b$ 个不同的球进行排列. 这样 $\Omega$ 中样本点的个数为 $(r + b)!$. 事件 $R_{k}$ 发生也就是第 $k$ 位放红球, 有 $r$ 种方式, 而其余 $r + b - 1$ 个球在 $r + b - 1$ 个位置随意排列, 共有 $(r + b - 1)!$ 种排法. 故有

$$
\mathbf {P} (R _ {k}) = \frac {r \cdot (r + b - 1) !}{(r + b) !} = \frac {r}{r + b}.
$$

(2) 同色球不可辨. 将球依次取出相当于在 $r + b$ 个位置中挑选 $r$ 个位置放红球. 这样 $\Omega$ 中样本点个数为 $\mathrm{C}_{r + b}^{r}$. 第 $k$ 次取到红球相当于第 $k$ 个位置必须是红球, 而在余下的 $r + b - 1$ 个位置中挑 $r - 1$ 个位置放其余的红球. 故有 $\mathrm{C}_{r + b - 1}^{r - 1}$ 种放置方法. 所以

$$
\mathbf {P} (R _ {k}) = \frac {\mathrm{C} _ {r + b - 1} ^ {r - 1}}{\mathrm{C} _ {r + b} ^ {r}} = \frac {(r + b - 1) ! \cdot r ! \cdot b !}{(r + b) ! \cdot (r - 1) ! \cdot b !} = \frac {r}{r + b}.
$$

上例中用两种方法算出的概率 $\mathbf{P}(R_k)$ 相同, 且这个概率与 $k$ 无关. 这说明我们平时采用的抽签方式是公平的.

例 1.1.12 袋中有 r 个红球和 b 个黑球, 从中随机取出 n 个. 求取出的球中恰有 k 个红球的概率  $(k=0,1,2,\cdots,n)$ .

解 令 $E_{k} = \{$ 摸出的球中恰有 $k$ 个红球 $\}$. 我们需要对取球的方式进行讨论.

(1) 无放回抽取. 此时

$$
\mathbf {P} (E _ {k}) = \frac {\mathrm{C} _ {r} ^ {k} \mathrm{C} _ {b} ^ {n - k}}{\mathrm{C} _ {r + b} ^ {n}}.
$$

(2) 有放回抽取. 此时

$$
\mathbf {P} (E _ {k}) = \frac {\mathrm{C} _ {n} ^ {k} r ^ {k} b ^ {n - k}}{(r + b) ^ {n}} = \mathrm{C} _ {n} ^ {k} \bigg (\frac {r}{r + b} \bigg) ^ {k} \bigg (\frac {b}{r + b} \bigg) ^ {n - k}.
$$

(请读者说明上述两种方式对应的样本空间, 并对计算的合理性作出解释.)

在古典概型中, 用 $\mathcal{F}$ 表示样本空间 $\Omega$ 的所有子集构成的集类. 则 (1.1.1) 式在 $\mathcal{F}$ 上定义了一个取值于 $[0,1]$ 的函数 $\mathbf{P}$, 它在 $A \in \mathcal{F}$ 的取值就是概率值 $\mathbf{P}(A)$. 不难看出, 该集函数具有如下基本性质:

(1) 非负性: 对于任何  $A \in F$  有  $\mathbf{P}(A) \geqslant 0;$
(2) 规范性:  $\mathbf{P}(\Omega)=1;$
(3) 有限可加性: 对任何两两不交的 $A_{1}, A_{2}, \cdots, A_{n} \in \mathcal{F}$ 有

$$
\mathbf {P} \left(\bigcup_ {i = 1} ^ {n} A _ {i}\right) = \sum_ {i = 1} ^ {n} \mathbf {P} (A _ {i}).
$$

## 1.1.3 几何概率模型

有时候, 我们需要考虑样本点的个数无限, 甚至不可数的随机试验, 其各个样本点的出现仍然具有某种 “等可能” 性. 此时我们无法像古典概型那样, 通过样本点个数的比值来定义随机事件的概率. 几何概型为我们提供了处理此类问题的常用的方法. 令 $\mathbb{R}^{d}$ 表示 $d (d \geqslant 1)$ 维欧几里得 (Euclid) 空间, 简称欧氏空间.

定义1.1.2 设随机试验的样本空间 $\Omega$ 是欧氏空间 $\mathbb{R}^d$ 的某个具有体积 $m(\Omega)$ 的子集, 且 $0 < m(\Omega) < \infty$. 若集合 $A \subseteq \Omega$ 具有体积 $m(A)$, 则规定 $A$ 的概率为

$$
\mathbf {P} (A) = \frac {m (A)}{m (\Omega)}. \tag {1.1.2}
$$

称这样的随机试验为几何概率模型, 简称几何概型.

例 1.1.13 向一个半径为 0.5 m 的圆形靶子投飞镖. 根据几何概型计算飞镖落入以靶心为中心、以 0.25 m 为半径的圆内的概率.

解 根据圆面积的计算公式, 事件 $A = \{\text{飞镖落入以靶心为中心、以 } 0.25 \mathrm{~m} \text{ 为半径的圆内}\}$ 的概率为

$$
\mathbf {P} (A) = \frac {\pi \cdot 0 . 2 5 ^ {2}}{\pi \cdot 0 . 5 ^ {2}} = \frac {1}{4}.
$$

在几何概型中, 用 $\mathcal{F}$ 表示样本空间 $\Omega$ 的所有可求体积的子集构成的集类. 则 (1.1.2) 式在集类 $\mathcal{F}$ 上定义了一个取值于 $[0,1]$ 的函数 $\mathbf{P}$, 它在 $A \in \mathcal{F}$ 的取值就是概率值 $\mathbf{P}(A)$. 直观上, 几何概率应该具有如下基本性质:

(1) 非负性: 对于任何  $A \in F$  有  $\mathbf{P}(A) \geqslant 0;$
(2) 规范性:  $\mathbf{P}(\Omega)=1;$
(3) 可数可加性: 对任何两两不交的  $A_{1}, A_{2}, \cdots, A_{n}, \cdots \in F$  有

$$
\mathbf {P} \left(\bigcup_ {i = 1} ^ {\infty} A _ {i}\right) = \sum_ {i = 1} ^ {\infty} \mathbf {P} (A _ {i}).
$$

根据实变函数论中的结论, 我们不能对欧氏空间 $\mathbb{R}^d$ 的所有子集合理地定义其体积; 参见 [22]. 所以 $\mathcal{F}$ 可能不包含 $\Omega$ 的所有子集.

例 1.1.14 设平面上布满间隔为 t 的平行线, 现向平面任意投放一根长为  $l(l < t)$  的针, 根据几何概型求事件  $E = \{ \text{针与某直线相交} \}$  的概率.

解 针的位置是由它的中点到最近直线的距离 $\rho$ 以及针和直线的夹角 $\theta$ 决定. 考虑到对称性, 我们可取样本空间为 $\Omega = \left\{(\rho, \theta): 0 \leqslant \rho \leqslant \frac{t}{2}, 0 \leqslant \theta \leqslant \frac{\pi}{2} \right\}$. 根据针与直线的几何位置, 有 $E = \left\{(\rho, \theta): 0 \leqslant \rho \leqslant \frac{l}{2} \sin \theta \right\}$, 如图1.2所示. 由此可得

$$
\mathbf {P} (E) = \frac {m (E)}{m (\varOmega)} = \left(\frac {\pi}{2} \cdot \frac {t}{2}\right) ^ {- 1} \int_ {0} ^ {\frac {\pi}{2}} \frac {l}{2} \sin \theta \mathrm{d} \theta = \frac {2 l}{\pi t}.
$$

![](images/page_21_image_15.jpg)

<details>
<summary>text_image</summary>

ρ
θ
t
</details>

(a)

![](images/page_21_image_17.jpg)

<details>
<summary>text_image</summary>

ρ
t/2
l/2 sin θ
E
O
π/2
θ
</details>

(b)

图1.2 布丰投针试验

上例中的随机试验称为布丰 (Buffon) 投针试验. 重复该试验 $n$ 次, 将事件 $E$ 发生

的次数记为 $S_{n}$ 次. 根据本课程后面证明的大数定律, 当 $n \to \infty$ 时, 在一定意义下有

$$
\frac {S _ {n}}{n} \rightarrow \mathbf {P} (E) = \frac {2 l}{\pi t}.
$$

因此, 当 $n$ 很大时, 我们有近似关系

$$
\frac {S _ {n}}{n} \approx \frac {2 l}{\pi t} \quad \text {或} \quad \pi \approx \frac {2 l n}{t S _ {n}}.
$$

上式给出了一种利用概率模型进行近似计算的方法, 这类方法称为蒙特卡罗 (Monte Carlo) 方法.

例 1.1.15 在单位圆上任作一弦, 求  $E = \{弦长大于 \sqrt{3}\}$  的概率.

解 本例题对于“任作一弦”的含义没有给出准确描述. 下面我们对其作出三种解读, 并分别给出问题的解答.

(1) 考虑由其中点确定的弦. 取单位圆的内接正三角形及该三角形的内切圆, 如图 1.3(a) 所示. 不难算出, 三角形的边长为 $2\sin (\pi / 3) = \sqrt{3}$, 而小圆的半径为 $1/2$. 当且仅当弦的中点落在小圆内时, 弦的长度大于三角形的边长 $\sqrt{3}$. 单位圆盘的面积是 $\pi$, 而小圆盘的面积是 $\pi / 2^2$. 基于这样的解读, 我们可以取 $\Omega = \{\text{单位圆盘}\}$ 和 $E = \{\text{半径为} 1/2 \text{的同心圆盘}\}$. 这样得到

$$
\mathbf {P} (E) = \frac {\pi / 2 ^ {2}}{\pi} = \frac {1}{4}.
$$

![](images/page_22_image_11.jpg)

<details>
<summary>text_image</summary>

Geometric diagram showing a circle inscribed in a circle with intersecting triangles and diagonal lines, likely for a math problem or proof.
</details>

(a)

![](images/page_22_image_13.jpg)

<details>
<summary>text_image</summary>

Geometric diagram of a circle with inscribed triangle and internal segments, labeled with mathematical notation
</details>

(b)

![](images/page_22_image_15.jpg)

<details>
<summary>text_image</summary>

Geometric diagram of a circle with inscribed triangles and intersecting lines, likely for trigonometry or geometry problem solving.
</details>

(c)

图 1.3 贝特朗奇论

(2) 考虑一个端点固定的弦. 以该端点为一个顶点作单位圆的内接正三角形, 如图 1.3(b) 所示. 注意, 三角形交于该顶点的两条边与圆在此处的切线分别成 $60^{\circ}$ 角和 $120^{\circ}$ 角. 由此可知, 当弦与切线成的角度介于 $60^{\circ}$ 和 $120^{\circ}$ 之间时其长度大于三角形的边长 $\sqrt{3}$. 这样, 我们可以取 $\Omega = [0, 180]$ 和 $E = [60, 120]$. 于是有

$$
\mathbf {P} (E) = \frac {1 2 0 - 6 0}{1 8 0} = \frac {6 0}{1 8 0} = \frac {1}{3}.
$$

(3) 考虑与某个半径垂直的弦. 取单位圆的内接正三角形及与该三角形的一条边垂直的半径. 则该半径被三角形的边平分, 如图 1.3(c) 所示. 当且仅当弦的中点落在半径上三角形内时, 弦的长度大于三角形的边长 $\sqrt{3}$. 这样, 我们可以取 $\Omega = \{\text{半径上的所有点}\}$ 和 $E = \{\text{半径上到圆心距离小于} 1/2\text{的点}\}$. 于是有

$$
\mathbf {P} (E) = \frac {1}{2}.
$$

在上例中, 基于 “任作一弦” 的三种解读方式, 对于同一个问题得出了三种完全不同的答案, 这是概率论发展史上一个著名的例子, 称为贝特朗 (Bertrand) 奇论. 那么, 上述哪一个答案是正确的呢? 这个例子对我们有哪些启发呢? 请读者查阅相关资料, 认真思考一下.

## 1.1.4 概率公理化体系

古典概型和几何概型对概率论早期的发展起了重要作用. 但是这两种模型都基于对样本点的“等可能”假定, 而且古典概型只适用于有限样本空间, 这使它们的应用有很大的局限性. 由于对于“等可能”假定的不同解读, 几何概型在应用中会产生像贝特朗奇论那样的问题. 事实上, 当随机试验有不可数无穷多个可能的结果时, 有时很难客观地规定“等可能”确切的含义, 这反映出几何概型的逻辑基础是不够严密的.

到 19 世纪下半叶, 概率论的发展及其在物理学等学科中的应用已经突破了概率的古典定义, 但关于概率的一般定义却始终未能明确化和严格化. 这种情况严重阻碍了概率论的进一步发展和应用. 在 1900 年的世界数学家大会上, 希尔伯特提出了建立物理学、概率论等公理化体系的问题.

进入 20 世纪后, 抽象测度和积分理论逐步发展完善. 随着研究的深入, 人们发现事件的运算与集合的运算完全类似, 而概率与测度有相同的性质. 在这种背景下, 柯尔莫哥洛夫 (Andrey N. Kolmogorov) 在 1933 年出版了《概率论基础》一书, 他在书中给出了概率的测度论式的定义和严密的公理化体系. 该公理化体系以概率空间概念为基础, 首先对事件与概率的最基本性质和关系作出规定, 在此基础上导出概率的其他性质. 这些性质从客观实际中抽象出来, 既概括了古典概率和几何概率的基本特性, 又避免了各自的局限性和含混之处. 柯尔莫哥洛夫概率公理化体系是概率论发展史上一个重要的里程碑, 为现代概率论的发展打下了坚实的基础.

本教材后面将采用柯尔莫哥洛夫的公理化体系, 在此基础上系统地介绍概率论的基本知识.

## 练习题

1. 设 $A, B$ 和 $C$ 是三个事件. 用它们给出下列事件的表示:

(1) 至少有一个事件发生;

(2) 至少有两个事件发生;

(3) 所有事件都不发生;
(4) 至多一个事件发生;
(5) 至多两个事件发生;
(6) 恰有两个事件发生.

2. 从 0,1,2,3,4,5 中任取 4 个数排成一行. 求恰好构成四位偶数的概率.

3. 在桥牌游戏中四人各从 52 张纸牌中分得 13 张. 求 4 张 A 集中在一个人手里的概率.
4. 信封里有 8 把钥匙, 其中只有一把能打开房门, 现取出钥匙试开. 分有放回和无放回两种情形, 求 3 次以内能打开房门的概率.
5. 袋子里有 $m$ 个白球, $n$ 个黑球 $(m, n \geqslant 1)$.

(1) 从袋中随机取两个球, 求两球同色的概率;

(2) 从袋中随机取一个球, 记录颜色后放回, 从中再取一球, 求两次取的球同色的概率;

(3) 证明 (2) 的概率始终大于 (1) 的概率.

6. 在区间 $(0,1)$ 中随机地取出三个数, 以它们作为三条线段的长度. 求这些线段能连接成一个三角形的概率.
7. 在打好方格的白纸上投掷一枚直径为 1 的硬币. 问方格的边长至少应为多少才能使硬币与方格的边不交的概率小于 $1 / 100$.

## 1.2 可测空间和概率空间

柯尔莫哥洛夫的概率论公理化体系的基础是概率空间, 它给出了我们前面提到的样本空间、随机事件、概率等概念的严格数学定义.

## 1.2.1 可测空间

定义 1.2.1 设  $\Omega$  为非空集, 而 F 为  $\Omega$  的子集构成的集类. 如果

(i) $\Omega \in \mathcal{F}$;
(ii) 若 $A \in \mathcal{F}$, 则 $A^c \in \mathcal{F}$;
(iii) 若 $A, B \in \mathcal{F}$, 则 $A \cup B \in \mathcal{F}$,

那么称 $\mathcal{F}$ 为 $\Omega$ 上的集代数.

定义 1.2.2 称非空集  $\Omega$  的子集类 F 是  $\sigma$  代数, 是指定义 1.2.1 中的 (i), (ii) 和下面的性质成立: (iii)' 若  $A_{1}, A_{2}, \cdots \in F$ , 则  $\bigcup_{k=1}^{\infty} A_{k} \in F$ . 此时称  $(\Omega, \mathcal{F})$  为可测空间, 称 F 中的集合为可测集.

命题 1.2.1 非空集  $\Omega$  的子集类 F 是  $\sigma$  代数的充要条件是定义 1.2.1 中的 (i), (ii) 和下面的性质成立: (iii) 若  $A_{1}, A_{2}, \cdots \in F$ , 则  $\bigcap_{k=1}^{\infty} A_{k} \in F$ .

证明 只需证明, 在性质 (i) 和 (ii) 成立的情况下, 性质 (iii)' 和 (iii)'' 等价. 设性质 (i) 和 (ii) 成立. 由 $\bigcap_{k=1}^{\infty} A_k = \left(\bigcup_{k=1}^{\infty} A_k^c\right)^c$ 知 (iii)' $\Rightarrow$ (iii)''; 而由 $\bigcup_{k=1}^{\infty} A_k = \left(\bigcap_{k=1}^{\infty} A_k^c\right)^c$ 知 (iii)" $\Rightarrow$ (iii)'.\) □

例 1.2.1 令  $\Omega$  为非空集. 则  $\Omega$  的所有子集构成的集类  $F_{\infty}$  是  $\Omega$  上的  $\sigma$  代数, 且它在  $\Omega$  的所有  $\sigma$  代数中是最大的. 特别地, 若  $\Omega$  是包含 n 个元素的有限集, 则  $F_{\infty}$  中共有  $2^{n}$  个子集.

例 1.2.2 令  $\Omega$  为非空集. 易知  $F_{0} := \{\varnothing, \Omega\}$  是  $\Omega$  上的集代数和  $\sigma$  代数, 且它在  $\Omega$  的所有集代数和  $\sigma$  代数中是最小的.

例 1.2.3 令  $\Omega$  为非空集, 而 A 为  $\Omega$  的非空真子集. 则  $F := \{\varnothing, A, A^{c}, \Omega\}$  是  $\Omega$  的集代数和  $\sigma$  代数, 且它在  $\Omega$  的所有包含 A 的集代数和  $\sigma$  代数中是最小的.

例 1.2.4 令  $\Omega=\{1,2,3\}$  和  $A=\{1,2\}$ . 定义  $F=\{\varnothing,A,A^{c},\Omega\}$ . 则单点集  $\{1\}$  不属于 F. 所以  $\Omega$  上的集代数和  $\sigma$  代数未必包含其所有子集.

例 1.2.5 设  $(\Omega, \mathcal{F})$  为可测空间. 给定非空集  $E \in F$  记  $E = \{E \cap A : A \in F\}$ . 易证 E 是 E 上的  $\sigma$  代数, 故  $(E, \mathcal{E})$  是可测空间. 注意  $E \subseteq F$ .

命题 1.2.2 设  $\{\mathcal{F}_{\alpha} : \alpha \in I\}$  是  $\Omega$  上的一族  $\sigma$  代数, 其中 I 为指标集. 则  $F := \bigcap_{\alpha \in I} F_{\alpha}$  也是  $\Omega$  上的  $\sigma$  代数.

证明 因为每个集类 $\mathcal{F}_{\alpha}$ 都满足定义1.2.1中的性质(i)，(ii)和定义1.2.2中的性质(iii)'，易证 $\mathcal{F}$ 也满足这些性质. □

给定非空集 $\Omega$ 的子集类 $\mathcal{G}$, 令

$$
\sigma (\mathcal {G}) = \cap \{\mathcal {F}: \mathcal {F} \text {为} \Omega \text {上的} \sigma \text {代数且} \mathcal {F} \supseteq \mathcal {G} \}.
$$

由命题1.2.2知 $\sigma (\mathcal{G})$ 是 $\sigma$ 代数, 我们称之为由 $\mathcal{G}$ 生成的 $\sigma$ 代数. 它是 $\Omega$ 上的包含 $\mathcal{G}$ 的最小的 $\sigma$ 代数. 特别地, 若 $\mathcal{G}$ 是 $\sigma$ 代数, 则 $\mathcal{G} = \sigma (\mathcal{G})$.

如果  $\Omega$  的可数个子集  $B_{1}, B_{2}, \cdots$  两两不交且满足  $\bigcup_{n=1}^{\infty} B_{n} = \Omega$ ，我们就称之为  $\Omega$  的一个可数划分.

例 1.2.6 设  $G := \{B_{1}, B_{2}, \cdots\}$  是  $\Omega$  的可数划分. 则  $\sigma(\mathcal{G})$  是由 G 中的集合的所有可能的并构成的集类 (规定零个集合的并为空集).

命题1.2.3 设 $\mathcal{E}$ 和 $\mathcal{G}$ 是 $\Omega$ 上的集类且 $\mathcal{E} \subseteq \mathcal{G}$. 则 $\sigma(\mathcal{E}) \subseteq \sigma(\mathcal{G})$.

证明 因为 $\mathcal{E} \subseteq \mathcal{G}$, 所以

$\{\mathcal{F}:\mathcal{F}$ 为 $\Omega$ 上的 $\sigma$ 代数且 $\mathcal{F}\supseteq \mathcal{E}\} \supseteq \{\mathcal{F}:\mathcal{F}$ 为 $\Omega$ 上的 $\sigma$ 代数且 $\mathcal{F}\supseteq \mathcal{G}\}$, 故知 $\sigma (\mathcal{E})\subseteq \sigma (\mathcal{G})$.

定义1.2.3 令 $\mathcal{O}^d$ 为 $d$ 维欧氏空间 $\mathbb{R}^d$ 的所有开集构成的集类。我们称 $\mathcal{B}^d := \sigma(\mathcal{O}^d)$ 为 $\mathbb{R}^d$ 的博雷尔 (Borel) $\sigma$ 代数，称 $\mathcal{B}^d$ 中的集合为博雷尔可测集，简称博雷尔集。称 $(\mathbb{R}^d, \mathcal{B}^d)$ 为欧氏可测空间或博雷尔可测空间。

命题 1.2.4 令  $S^{d}$  是  $R^{d}$  上所有形如  $(a,b]=(a_{1},b_{1}]\times(a_{2},b_{2}]\times\cdots\times(a_{d},b_{d}]$  的左开右闭区间构成的集类. 则  $\mathcal{B}^{d}=\sigma(\mathcal{S}^{d})$ .

证明 由于 $(a, b) = (a_1, b_1) \times (a_2, b_2) \times \cdots \times (a_d, b_d) \in \mathcal{O}^d \subseteq \sigma(\mathcal{O}^d) = \mathcal{B}^d$，而 $\mathcal{B}^d$ 对于可数交运算封闭，故有

$$
(a, b ] = \bigcap_ {k = 1} ^ {\infty} (a _ {1}, b _ {1} + 1 / k) \times (a _ {2}, b _ {2} + 1 / k) \times \dots \times (a _ {d}, b _ {d} + 1 / k) \in \mathcal {B} ^ {d},
$$

因而 $\mathcal{S}^d\subseteq \mathcal{B}^d$ .由命题1.2.3有 $\sigma (\mathcal{S}^d)\subseteq \sigma (\mathcal{B}^d) = \mathcal{B}^d$ .另一方面，因为 $\mathcal{O}^d$ 中的每个开集都可写为至多可数个形如 $(a,b]$ 的区间的并，而 $\sigma (\mathcal{S}^d)$ 作为 $\sigma$ 代数对于可数并运算封闭，所以 $\sigma (\mathcal{S}^d)\supseteq \mathcal{O}^d$ .再由命题1.2.3有 $\sigma (\mathcal{S}^d)\supseteq \sigma (\mathcal{O}^d) = \mathcal{B}^d$ .综上得

$$
\sigma (\mathcal {S} ^ {d}) = \mathcal {B} ^ {d}.
$$

事实上, 易证 $\mathcal{B}^d$ 也可以由 $\mathbb{R}^d$ 中的开区间, 或闭区间, 或左闭右开区间生成. 为简化记号, 我们后面将写写 $\mathcal{O} = \mathcal{O}^1$, $\mathcal{C} = \mathcal{C}^1$ 和 $\mathcal{B} = \mathcal{B}^1$.

## 1.2.2 测度及其基本性质

定义 1.2.4 设  $(\Omega, \mathcal{F})$  是可测空间, 而  $\mu$  为定义在  $\sigma$  代数 F 上取值于  $[0, \infty]$  的函数. 我们称  $\mu$  为一个测度, 是指  $\mu(\varnothing) = 0$  且下面的可数可加性或  $\sigma$  可加性成立: 对任何两两不交的集合列  $\{A_{1}, A_{2}, \cdots\} \subseteq F$  有

$$
\mu \left(\bigcup_ {k = 1} ^ {\infty} A _ {k}\right) = \sum_ {k = 1} ^ {\infty} \mu (A _ {k}).
$$

此时, 若存在两两不交的集合列 $\{\Omega_1, \Omega_2, \cdots\} \subseteq \mathcal{F}$ 使得 $\bigcup_{k=1}^{\infty} \Omega_k = \Omega$ 且对每个 $k \geqslant 1$ 有 $\mu(\Omega_k) < \infty$, 则称 $\mu$ 为 $\sigma$ 有限测度. 特别地, 若 $\mu(\Omega) < \infty$, 则称 $\mu$ 为有限测度; 而若 $\mu(\Omega) = 1$, 则称 $\mu$ 为概率测度或概率.

在可数可加性中取  $A_{n+1}=A_{n+2}=\cdots=\varnothing$ ，我们得到有限可加性:对任何两两不交的  $A_{1}, A_{2}, \cdots, A_{n} \in F$  有

$$
\mu \left(\bigcup_ {k = 1} ^ {n} A _ {k}\right) = \sum_ {k = 1} ^ {n} \mu (A _ {k}). \tag {1.2.1}
$$

进而容易证明测度  $\mu$  的如下性质:

- 单调性: 若 $A, B \in \mathcal{F}$ 且有 $A \subseteq B$, 则 $\mu(A) \leqslant \mu(B)$;
- 可减性: 若 $A, B \in \mathcal{F}$ 且有 $A \subseteq B$ 和 $\mu(A) < \infty$, 则 $\mu(B \setminus A) = \mu(B) - \mu(A)$.

例 1.2.7 对于  $\omega \in \Omega$  和  $A \in F$ ，当  $\omega \in A$  时令  $\delta_{\omega}(A) = 1$ ，当  $\omega \in A^{c}$  时令  $\delta_{\omega}(A) = 0$ 。显然  $\delta_{\omega}$  是  $(\Omega, \mathcal{F})$  上的概率测度。称  $\delta_{\omega}$  为集中于  $\omega \in \Omega$  的单点概率测度或狄拉克 (Dirac) 测度。

例 1.2.8 设  $\mu$  是可测空间  $(\Omega, \mathcal{F})$  上的  $\sigma$  有限测度, 而  $E \in F$  为非空集. 对于  $A \in F$  令  $\mu_{E}(A) = \mu(E \cap A)$ . 则  $\mu_{E}$  也是  $(\Omega, \mathcal{F})$  上的  $\sigma$  有限测度. 称  $\mu_{E}$  为  $\mu$  在 E 上的限制. 我们也经常将  $\mu_{E}$  视为  $(E, \mathcal{E})$  上的测度, 其中 E 如例 1.2.5 给出.

例 1.2.9 设  $(\Omega, \mathcal{F})$  和  $(E, \mathcal{E})$  如例 1.2.5 给出. 再设  $\nu$  是  $(E, \mathcal{E})$  上的  $\sigma$  有限测度. 对于  $A \in F$  令  $\mu(A) = \nu(E \cap A)$ . 则  $\mu$  是  $(\Omega, \mathcal{F})$  上的  $\sigma$  有限测度.

为简单起见, 下面假定  $\mu$  是可测空间  $(\Omega, \mathcal{F})$  上的有限测度.

定理 1.2.5（次可加性） 对任何  $A_{1}, A_{2}, \cdots \in F$  有

$$
\mu \Big (\bigcup_ {n = 1} ^ {\infty} A _ {n} \Big) \leqslant \sum_ {n = 1} ^ {\infty} \mu (A _ {n}).
$$

证明 定义 $B_{1} = A_{1}$ 和 $B_{n} = A_{1}^{c}A_{2}^{c}\dots A_{n - 1}^{c}A_{n}(n\geqslant 2)$. 易证 $B_{1},B_{2},\dots \in \mathcal{F}$ 两两不交且 $\bigcup_{n = 1}^{\infty}A_n = \bigcup_{n = 1}^{\infty}B_n$ .由可数可加性和单调性得

$$
\mu \Big (\bigcup_ {n = 1} ^ {\infty} A _ {n} \Big) = \mu \Big (\bigcup_ {n = 1} ^ {\infty} B _ {n} \Big) = \sum_ {n = 1} ^ {\infty} \mu (B _ {n}).
$$

因 $\mu(B_n) \leqslant \mu(A_n)$, 故得欲证不等式.

定理1.2.6（两集合的加法定理） 对于任何 $A, B \in \mathcal{F}$ 有

$$
\mu (A \cup B) = \mu (A) + \mu (B) - \mu (A \cap B). \tag {1.2.2}
$$

证明 注意 $A \cup B = A \cup (B \setminus A)$, 其中 $A, B \setminus A \in \mathcal{F}$ 不交. 由测度的有限可加性,

$$
\mu (A \cup B) = \mu (A \cup (B \setminus A)) = \mu (A) + \mu (B \setminus A).
$$

再由可减性得

$$
\mu (B \setminus A) = \mu (B \setminus (A \cap B)) = \mu (B) - \mu (A \cap B),
$$

从而 (1.2.2) 式成立.

定理 1.2.7 (推广的加法定理) 对于任何  $A_{1}, A_{2}, \cdots, A_{n} \in \mathcal{F} (n \geqslant 2)$ ，有

$$
\mu \Big (\bigcup_ {k = 1} ^ {n} A _ {k} \Big) = \sum_ {1 \leqslant i \leqslant n} \mu (A _ {i}) - \sum_ {1 \leqslant i <   j \leqslant n} \mu (A _ {i} A _ {j}) +
$$

$$
\sum_ {1 \leqslant i <   j <   k \leqslant n} \mu (A _ {i} A _ {j} A _ {k}) + \dots + (- 1) ^ {n - 1} \mu (A _ {1} A _ {2} \dots A _ {n}). \tag {1.2.3}
$$

证明 利用数学归纳法证明. 由定理1.2.6知(1.2.3)式对2个集合的情况成立. 现设该等式对 $n$ 个集合的情况成立. 由(1.2.2)式得

$$
\begin{array}{l} \mu \left(\bigcup_ {k = 1} ^ {n + 1} A _ {k}\right) = \mu \left(\bigcup_ {k = 1} ^ {n} A _ {k}\right) + \mu (A _ {n + 1}) - \mu \left(A _ {n + 1} \cap \bigcup_ {k = 1} ^ {n} A _ {k}\right) \\ = \mu \Big (\bigcup_ {k = 1} ^ {n} A _ {k} \Big) + \mu (A _ {n + 1}) - \mu \Big (\bigcup_ {k = 1} ^ {n} A _ {n + 1} A _ {k} \Big). \tag {1.2.4} \\ \end{array}
$$

利用归纳假设, 上式右端第 1 项可以表示为 (1.2.3) 式, 而第 3 项可以表示为

$$
\begin{array}{l} \mu \bigg (\bigcup_ {k = 1} ^ {n} A _ {n + 1} A _ {k} \bigg) = \sum_ {1 \leqslant i \leqslant n} \mu (A _ {n + 1} A _ {i}) - \sum_ {1 \leqslant i <   j \leqslant n} \mu (A _ {i} A _ {j} A _ {n + 1}) + \\ \sum_ {1 \leqslant i <   j <   k \leqslant n} \mu (A _ {i} A _ {j} A _ {k} A _ {n + 1}) + \dots + (- 1) ^ {n - 1} \mu (A _ {1} A _ {2} \dots A _ {n} A _ {n + 1}). \\ \end{array}
$$

将上述表示代入 (1.2.4) 式知 (1.2.3) 式对 $n + 1$ 个集合的情况成立。由此即得欲证结果。

定理 1.2.8（下连续性）。若  $\{A_{n}\} \subseteq F$  为不降集合序列，则

$$
\mu \left(\bigcup_ {n = 1} ^ {\infty} A _ {n}\right) = \lim _ {n \to \infty} \mu (A _ {n}).
$$

证明 令 $A_0 = \varnothing$ 和 $B_n = A_n \setminus A_{n-1}, n \geqslant 1$. 则 $B_1, B_2, \cdots \in \mathscr{F}$ 两两不交且 $\bigcup_{n=1}^{\infty} A_n = \bigcup_{n=1}^{\infty} B_n$. 利用可数可加性得

$$
\begin{array}{l} \mu \left(\bigcup_ {n = 1} ^ {\infty} A _ {n}\right) = \mu \left(\bigcup_ {n = 1} ^ {\infty} B _ {n}\right) = \sum_ {n = 1} ^ {\infty} \mu (B _ {n}) \\ = \sum_ {n = 1} ^ {\infty} [ \mu (A _ {n}) - \mu (A _ {n - 1}) ] \\ = \lim _ {k \to \infty} \sum_ {n = 1} ^ {k} [ \mu (A _ {n}) - \mu (A _ {n - 1}) ]. \\ \end{array}
$$

因  $\mu(A_{0})=\mu(\varnothing)=0,$  故得欲证等式.

定理 1.2.9（上连续性） 若  $\{A_{n}\} \subseteq F$  为不增集合序列，则

$$
\mu \left(\bigcap_ {n = 1} ^ {\infty} A _ {n}\right) = \lim _ {n \to \infty} \mu (A _ {n}).
$$

证明 注意 $A_1^c, A_2^c, \dots \in \mathscr{F}$ 且 $A_1^c \subseteq A_2^c \subseteq \dots$. 根据 $\mu$ 的下连续性及可减性有

$$
\mu \left(\bigcup_ {n = 1} ^ {\infty} A _ {n} ^ {c}\right) = \lim _ {n \to \infty} \mu (A _ {n} ^ {c}) = \mu (\varOmega) - \lim _ {n \to \infty} \mu (A _ {n}).
$$

再次利用可减性得

$$
\mu \left(\bigcap_ {n = 1} ^ {\infty} A _ {n}\right) = \mu \left(\varOmega \setminus \left(\bigcap_ {n = 1} ^ {\infty} A _ {n}\right) ^ {c}\right) = \mu (\varOmega) - \mu \left(\bigcup_ {n = 1} ^ {\infty} A _ {n} ^ {c}\right).
$$

综合以上二式即得欲证等式.

定义1.2.5 称博雷尔可测空间 $(\mathbb{R}^d, \mathcal{B}^d)$ 上的测度 $\mu$ 为博雷尔测度. 如果对于任何有界区间 $[a, b] \subseteq \mathbb{R}^d$ 都有 $\mu[a, b] = \mu([a, b]) < \infty$, 那么称该测度是局部有限的.

显然, 局部有限测度是  $\sigma$  有限的.

例 1.2.10 根据实变函数中的结论, 存在博雷尔  $\sigma$  代数  $B^{d}$  上的唯一的测度  $\lambda$ , 使得对任何区间  $(a,b]=(a_{1},b_{1}]\times(a_{2},b_{2}]\times\cdots\times(a_{d},b_{d}]\in\mathcal{S}^{d})$  有

$$
\lambda (a, b ] = (b _ {1} - a _ {1}) (b _ {2} - a _ {2}) \dots (b _ {d} - a _ {d}), \quad a _ {i} \leqslant b _ {i} \in \mathbb {R}, i = 1, 2, \dots , d.
$$

我们称 $\lambda$ 为 $\mathbb{R}^d$ 上的勒贝格 (Lebesgue) 测度. 勒贝格测度是反映欧几里得空间中子集的长度、面积或者体积的严格数学概念. 显然, 勒贝格测度是局部有限的. 对于勒贝格测度存在性的证明感兴趣的读者, 可以参考实分析方面的著作, 例如 [22] 等.

## 1.2.3 概率空间的概念

定义1.2.6 给定可测空间 $(\Omega, \mathcal{F})$ 和 $\mathcal{F}$ 上的概率测度 $\mathbf{P}$, 我们称 $(\Omega, \mathcal{F}, \mathbf{P})$ 为概率空间, 其中 $\Omega$ 称为样本空间, 而 $\mathcal{F}$ 称为事件域. 事件域 $\mathcal{F}$ 中的集合称为随机事件, 简称事件. 对于事件 $A \in \mathcal{F}$, 称 $\mathbf{P}(A)$ 为 $A$ 的概率.

概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$ 是描述随机试验的数学模型。这里样本空间 $\Omega$ 表示所有可能的结果的集合。令 $A \in \mathcal{F}$ 为一个事件。假设试验的结果是某个 $\omega \in \Omega$。若 $\omega \in A$，则表示 $A$ 在试验中发生了，否则表示 $A$ 在试验中没有发生。概率测度 $\mathbf{P}$ 给出了事件域 $\mathcal{F}$ 中所有事件的概率。注意有 $\mathbf{P}(\Omega) = 1$ 和 $\mathbf{P}(\varnothing) = 0$。我们分别称 $\Omega$ 和 $\varnothing$ 为必然事件和不可能事件。

给定概率空间 $(\Omega, \mathcal{F}, \mathbf{P})$，我们称 $A \subseteq \Omega$ 为 $\mathbf{P}$ 零集，是指存在 $N \in \mathcal{F}$ 满足 $N \supseteq A$ 且 $\mathbf{P}(N) = 0$。称 $(\Omega, \mathcal{F}, \mathbf{P})$ 是完备概率空间，是指 $\mathcal{F}$ 包含一切 $\mathbf{P}$ 零集。

例 1.2.11 考虑关于事件  $A \subseteq \Omega$  的伯努利试验. 令  $F = \{\varnothing, A, A^{c}, \Omega\}$ . 设成功概率为  $\mathbf{P}(A) = p$ , 其中  $0 \leqslant p \leqslant 1$ , 故有

$$
\mathbf {P} (\varnothing) = 0, \mathbf {P} (\varOmega) = 1, \mathbf {P} (A) = p, \mathbf {P} (A ^ {c}) = 1 - p.
$$

我们称 $(\Omega, \mathcal{F}, \mathbf{P})$ 为伯努利概率空间.

例 1.2.12 (古典概率空间) 设  $\Omega$  为有限集. 令 F 为  $\Omega$  的所有子集构成的  $\sigma$  代数. 用  $n(A)$  表示集合  $A \in F$  中元素的个数, 并令

$$
\mathbf {P} (A) = \frac {n (A)}{n (\varOmega)}.
$$

则 $(\Omega, \mathcal{F}, \mathbf{P})$ 构成一个概率空间, 称为古典概率空间.

例 1.2.13 (可数概率空间) 设  $\Omega = \{\omega_{i} : i \in I\}$  为非空可数集, 其中 I 为其指标集. 令 F 为  $\Omega$  的所有子集构成的  $\sigma$  代数. 取非负实数  $p_{i}, i \in I$  满足  $\sum_{i \in I} p_{i} = 1$ . 对于  $A = \{\omega_{i} : i \in J\} \in F$ , 其中  $J \subseteq I$ , 令

$$
\mathbf {P} (A) = \sum_ {i \in J} p _ {i}.
$$

则 $(\Omega, \mathcal{F}, \mathbf{P})$ 为一个概率空间, 称为可数概率空间. 特别地, 若 $\Omega$ 为有限集, 则称 $(\Omega, \mathcal{F}, \mathbf{P})$ 为有限概率空间. 古典概率空间是典型的有限概率空间.

例1.2.14 设 $\Omega \in \mathcal{B}^d$ 满足 $0 < \lambda (\Omega) < \infty$. 令 $\mathcal{F} = \Omega \cap \mathcal{B}^d$. 对 $A \in \mathcal{F}$ 定义

$$
\mathbf {P} (A) = \frac {\lambda (A)}{\lambda (\varOmega)}.
$$

则 $(\Omega, \mathcal{F}, \mathbf{P})$ 构成一个概率空间, 称为几何概率空间.

将事件域定义为一个 $\sigma$ 代数为事件和概率的运算提供了很大的便利. 给定一列事件序列 $\{A_{n}\} \subseteq \mathcal{F}$, 分别称

$$
\operatorname * {l i m s u p} _ {n \to \infty} A _ {n} := \bigcap_ {n = 1} ^ {\infty} \bigcup_ {k = n} ^ {\infty} A _ {k}, \quad \operatorname * {l i m i n f} _ {n \to \infty} A _ {n} := \bigcup_ {n = 1} ^ {\infty} \bigcap_ {k = n} ^ {\infty} A _ {k} \tag {1.2.5}
$$

为  $\{A_{n}\}$  的上极限和下极限. 容易证明如下性质:

- $\omega \in \limsup_{n\to \infty}A_n$ 当且仅当有无穷多个 $k\geqslant 1$ 使得 $\omega \in A_k$;
- $\omega \in \liminf_{n\to \infty}A_n$ 当且仅当有某个 $n\geqslant 1$ 使当 $k\geqslant n$ 时有 $\omega \in A_k$.

上述性质可以解释为: 事件  $\limsup_{n\to\infty}A_n$  发生表示事件序列  $A_1, A_2, \cdots$  中有无穷多个事件发生, 而事件  $\liminf_{n\to\infty}A_n$  发生表示有某个  $n \geqslant 1$  使得事件  $A_n, A_{n+1}, A_{n+2}, \cdots$  都发生. 由此易知

$$
\operatorname * {l i m s u p} _ {n \to \infty} A _ {n} \supseteq \operatorname * {l i m i n f} _ {n \to \infty} A _ {n}.
$$

为简单起见, 若事件序列 $\{A_{n}\}$ 单调不降, 我们写 $A_{n} \uparrow \bigcup_{n} A_{n}$; 而若 $\{A_{n}\}$ 单调不增, 写 $A_{n} \downarrow \bigcap_{n} A_{n}$.

例1.2.15 取 $\Omega = \{\text{全体非负整数}\}$. 对 $n \geqslant 1$ 令 $A_{2n} = \{\text{全体非负偶数}\}$ 和 $A_{2n-1} = \{\text{全体非负奇数}\}$, 则有

$$
\operatorname * {l i m s u p} _ {n \to \infty} A _ {n} = \bigcap_ {k = 1} ^ {\infty} \bigcup_ {n = k} ^ {\infty} A _ {n} = \varOmega , \quad \operatorname * {l i m i n f} _ {n \to \infty} A _ {n} = \bigcup_ {k = 1} ^ {\infty} \bigcap_ {n = k} ^ {\infty} A _ {n} = \varnothing.
$$

## 1.2.4 概率的计算

在概率空间的定义中, 我们将概率视为一种具有若干特殊性质的集函数. 这体现了数学学科的整体性, 使概率论的发展可以更有效地利用其他数学分支的方法和工具. 下面给出了几个利用概率的一般性质进行概率计算的例子.

例 1.2.16 假设 n 对夫妇任意在一排 2n 个椅子上就座. 求有夫妇不相邻的概率.

解 记 $A = \{\text{有夫妇不相邻}\}$. 显然 $A^c = \{\text{所有夫妇都相邻}\}$ 的概率比较容易计算:

$$
\mathbf {P} (A ^ {c}) = \frac {n ! \cdot 2 ^ {n}}{(2 n) !} = \frac {1}{(2 n - 1) ! !}.
$$

从而 $\mathbf{P}(A) = 1 - \frac{1}{(2n - 1)!!}$.

例 1.2.17 (布丰投针试验的续) 向画满间隔为 t 的平行直线的桌面上任投一直径为 l (l < t) 的半圆形纸片 (图 1.4). 求纸片与某直线相交的概率.

解 (1) 记 $E = \{\text{半圆形纸片与某直线相交}\}$. 设想把半圆形纸片拼成一个完整的圆形纸片. 再令 $F = \{\text{新的半圆形纸片与某直线相交}\}$. 则有 $E \cup F = \{\text{直径为} l\text{的圆形与某直线相交}\}$. 因 $l < t$, 我们有

$$
\begin{array}{l} E \cap F = \{\text {两半圆分界线与某直线相交} \} \\ = \{\text {长为} l \text {的线段与某直线相交} \}. \\ \end{array}
$$

由关于布丰投针问题的结果得 $\mathbf{P}(E\cap F) = 2l / \pi t.$

![](images/page_31_image_14.jpg)

<details>
<summary>text_image</summary>

1/18 (1-)(0=)
=(n8)9 - 1 = (n8)
乘法公有个 x: (n8)
</details>

图1.4 布丰投针试验

(2) 因 $E \cup F = \{\text{直径为 } l \text{ 的圆形纸片与平行线相交}\}$, 只要考虑圆心与最近平行线的距离和半径的关系. 取样本空间 $\Omega = [0, t/2]$. 则 $E \cup F = \{r \in \Omega : r \leqslant l/2\}$, 故 $\mathbf{P}(E \cup F) = l/t$.