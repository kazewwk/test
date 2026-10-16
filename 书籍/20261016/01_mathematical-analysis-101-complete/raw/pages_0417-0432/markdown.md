$\sum_{n=1}^{+\infty}\frac{\sin nx}{n^{\alpha}}$ 条件收敛.

## 习题 11.3

1. 讨论下列级数的敛散性:

(1) $\sum_{n=1}^{+\infty} \frac{(-1)^{[\sqrt{n}]}}{\sqrt{n}}$;

(2) $\sum_{n=2}^{+\infty} \frac{(-1)^{[\sqrt{n}]}}{n}$;

(3) $\sum_{n=2}^{+\infty} \frac{(-1)^n}{\sqrt{n} + (-1)^n}$;

(4) $\sum_{n=2}^{+\infty} \frac{(-1)^{[\sqrt{n}]}}{\sqrt{n+(-1)^n}};$

(5) $\sum_{n=2}^{+\infty} \frac{(-1)^n}{\sqrt{n} + (-1)^{\lceil \sqrt{n} \rceil}};$

(6) $\sum_{n=2}^{+\infty} \frac{(-1)^{[\sqrt{n}]}}{\sqrt{n+(-1)^{[\sqrt{n}]]}}.$

2. 若对任一趋于 0 的序列 $\{x_{n}\}$, 级数 $\sum_{n=1}^{+\infty} a_{n} x_{n}$ 均收敛, 证明: 级数 $\sum_{n=1}^{+\infty} |a_{n}|$ 收敛.

3. 证明:对于任意满足 $\sum_{n=1}^{+\infty} a_n^2 = +\infty$ 的数列 $\{a_n\}$，都存在数列 $\{b_n\}$ 满足 $\sum_{n=1}^{+\infty} b_n^2 < +\infty$，但 $\sum_{n=1}^{+\infty} a_n b_n = +\infty$.

4. 设序列 $\{a_{n}\}$ 单调且 $\lim_{n\to +\infty}a_n = 0.$ 证明:

(1) 若级数  $\sum_{n=1}^{+\infty}a_{n}$  收敛, 则级数  $\sum_{n=1}^{+\infty}a_{n}\sin nx$  和  $\sum_{n=1}^{+\infty}a_{n}\cos nx$  对一切 x 均绝对收敛.

(2) 若级数  $\sum_{n=1}^{+\infty}a_{n}$  发散, 则级数  $\sum_{n=1}^{+\infty}a_{n}\sin nx$  和  $\sum_{n=1}^{+\infty}a_{n}\cos nx$  对一切 x 均条件收敛.

5. 设 $\sum_{n=1}^{+\infty} a_n$ 是一个条件收敛的级数, 其前 $n$ 项部分和 $S_n$ 具有分解 $S_n = S_n^+ + S_n^-$, 其中 $S_n^+$ 与 $S_n^-$ 分别为正项之和与负项之和. 证明极限 $\lim_{n \to +\infty} \frac{S_n^+}{S_n^-}$ 存在并求之.

6. 设 $b_{n} > 0, \lim_{n\to +\infty} n\left(\frac{b_{n}}{b_{n+1}} - 1\right) > 0.$ 证明: $\sum_{n=1}^{+\infty} (-1)^{n} b_{n}$ 收敛.

7. 设 $m$ 是一给定的自然数, 数列 $\{a_{n}\}$ 单调趋于零, 试讨论级数 $\sum_{n=1}^{+\infty} a_{n} \sin \frac{n^{2}}{2m+1} \pi$ 的敛散性.

8. 如果 $\sum_{n=1}^{+\infty}\left|a_n - a_{n+1}\right| < +\infty$, 那么级数 $\sum_{n=1}^{+\infty}a_n$ 称为是有界变差的. 证明: 级数

$\sum_{n=1}^{+\infty} a_n$ 是有界变差的充要条件是对任意收敛级数 $\sum_{n=1}^{+\infty} b_n$, 都有 $\sum_{n=1}^{+\infty} a_n b_n$ 收敛.

9. 设 m 为自然数. 证明: 级数  $\sum_{n=1}^{+\infty}\frac{|\sin n^{m}|}{n}$  发散.

10. 证明: 级数 $\sum_{n=1}^{+\infty} \frac{\sin n^2}{n}$ 条件收敛.

## 11.4 绝对收敛级数与条件收敛级数的代数性质

级数考虑的是可数无穷多个实数的求和, 可以看成是有限个实数和的推广. 当级数收敛时, 我们可以理解为给定的无穷多个实数是可以求和的. 由于无限求和是通过极限来实现的, 因此有限个实数间代数运算的某些性质在取极限过程中可能不再被继承. 本节我们将重点讨论级数运算过程中结合律、交换律和分配律是否成立的问题 (简称 “三律”). 换句话说, 我们感兴趣于在什么情况下, 对于无穷次运算这三律仍然成立, 以及如果这三律不能成立, 又会出现什么样的现象. 一个可以高度概况的充分条件就是绝对收敛的级数继承代数运算的三律. 下面我们详细解释这句话的具体含义.

## 11.4.1 级数运算的结合律

所谓级数的结合律, 就是我们通常所说的级数的加括号或去括号, 是指对于给定的级数 $\sum_{n=1}^{+\infty} a_n$, 在保持级数通项位置次序不变的前提下, 对其若干项加括号, 得到级数

$$
(a _ {1} + \dots + a _ {n _ {1}}) + (a _ {n _ {1} + 1} + \dots + a _ {n _ {2}}) + \dots + (a _ {n _ {k} + 1} + \dots + a _ {n _ {k + 1}}) + \dots = \sum_ {k = 1} ^ {+ \infty} \tilde {a} _ {k},
$$

其中  $\tilde{a}_{k}=a_{n_{k-1}+1}+\cdots+a_{n_{k}}, n_{0}=0, k=1,2,\cdots,$  即  $\tilde{a}_{k}$  是原级数的第 k 个括号内的项之和. 级数  $\sum_{k=1}^{+\infty}\tilde{a}_{k}$  称为原级数加括号后得到的级数.

对于级数的加括号运算, 有下面重要的结论: 收敛级数任意添加括号不会改变级数的收敛性, 也不改变级数的和. 具体来说, 即

定理 11.4.1 (加括号法则) 设级数 $\sum_{n=1}^{+\infty} a_n$ 收敛, 则加括号后的级数仍然收敛, 并且与原级数有相等的和.

证明 设原级数的部分和序列为  $A_{1}, A_{2}, \cdots$ ，加括号后的级数的部分和序列为  $\tilde{A}_{1}, \tilde{A}_{2}, \cdots$ 。则显然有

$$
\tilde {A} _ {1} = A _ {n _ {1}}, \quad \tilde {A} _ {2} = A _ {n _ {2}}, \dots
$$

即 $\{\tilde{A}_k\}$ 是数列 $\{A_n\}$ 的子列. 因此, 当 $\{A_n\}$ 收敛时, 其子列 $\{\tilde{A}_k\}$ 必收敛且收敛于同一个值. □

注 11.4.1 (1) 对于发散的级数, 上述结论不成立, 即发散级数加括号后有可能收敛, 比如典型的反例是级数 $1 - 1 + 1 - 1 + \cdots$. 由于该级数通项不趋于 0 , 故发散. 但每两项加一个括号, 得到的新级数是收敛的. 当然, 如果加括号后的级数发散, 原级数必然发散.

(2) 可以构造更复杂的反例: 存在通项趋于 0 的发散级数, 使得适当加括号后收敛. 只不过对这样的级数, 添加的括号一定具有如下特点: 对任意的自然数 $N$, 一定存在一个括号, 其括号内的项数大于 $N$. 而且也一定存在这样的括号, 其括号内的所有项不可能同号.
(3) 对于正项级数或不变号级数, 定理的逆命题也成立. 这是基于如下事实: 不变号级数的部分和数列是单调的, 而单调数列如果存在一个子列收敛, 则原数列也必定收敛并且有与子列相同的极限.

下面我们对注 11.4.1 中涉及的问题做进一步的讨论. 注中第 (1) 条告诉我们, 如果一个级数本身就是通过加括号得到的, 那么一般来说, 我们是不能去括号的. 换句话说, 去括号有可能使得收敛级数变成发散级数. 但我们有下面的定理, 这个定理也部分回答了注中第 (2) 条的问题.

定理 11.4.2 (去括号法则 1) 设  $\lim_{n\to+\infty}a_n = 0$ ，如果  $\sum_{n=1}^{+\infty}a_n$  加括号后的级数  $\sum_{n=1}^{+\infty}\tilde{a}_n$  收敛，且所有括号长度有一致的上界 N (即括号内的项数一致有界)，则去掉括号后的原级数  $\sum_{n=1}^{+\infty}a_n$  也一定收敛，且和不变.

在给出严格的逻辑证明之前, 我们看看这定理在说什么. 为了证明级数 $\sum_{n=1}^{+\infty} a_n$ 收敛, 可以考察其部分和的 Cauchy 列, 即当 $n \gg 1$ 时, $\forall p > 0$, 是否有 $|a_{n+1} + \cdots + a_{n+p}|$ 充分小. 这点还是比较显然的, 事实上, 这 $p$ 个项可以分成三部分: 第一部分是前头的若干项, 它们没有构成一个完整的括号, 这些项充其量只有 $N$ 项, 由于 $\lim_{n \to +\infty} a_n = 0$, 故这些项之和可以做到充分小. 第二部分是中间的 (大部分) 项, 它们形成若干个完整的括号, 从而对应着级数 $\sum_{n=1}^{+\infty} \tilde{a}_n$ 中的若干项, 这些项的估计恰好满足该级数部分和序列的 Cauchy 准则, 因此也可以做到充分小. 同理, 第三部分是最后的若干项, 它们也没有构成一个完整的括号, 这些项充其量不超过 $N$, 所以也可以做到充分小. 因此, 这 $p$ 个项之和, 只要 $n$ 充分大, 在定理条件假设下, 是可以任意小的.

证明 由于 $\tilde{a}_k = a_{n_{k-1}+1} + a_{n_{k-1}+2} + \cdots + a_{n_k}, |n_k - n_{k-1}| \leqslant N, k = 1, 2, \cdots,$ 根据假设, 级数 $\sum_{n=1}^{+\infty} \tilde{a}_n$ 的部分和数列 $\{\tilde{S}_k\}$ 收敛到 $\tilde{S}$, 于是 $\forall \varepsilon > 0, k \gg 1$ 时, $\forall p > 0$, 有

$$
\begin{array}{l} | \tilde {S} _ {k + p} - \tilde {S} _ {k} | = | \tilde {a} _ {k + 1} + \dots + \tilde {a} _ {k + p} | \\ = \left| \left(a _ {n _ {k} + 1} + \dots + a _ {n _ {k + 1}}\right) + \dots + \left(a _ {n _ {k + p - 1} + 1} + \dots + a _ {n _ {k + p}}\right) \right| \\ <   \varepsilon . \tag {11.4.1} \\ \end{array}
$$

记 $S_{n}$ 为级数 $\sum_{n=1}^{+\infty} a_{n}$ 的部分和. 则数列 $\{\tilde{S}_{k}\}$ 是数列 $\{S_{n}\}$ 的一个子列. 我们往证数列 $\{S_{n}\}$ 也收敛, 且收敛到 $\tilde{S}$. 为此, 考虑

$$
| S _ {n} - \tilde {S} _ {k} | = | S _ {n} - S _ {n _ {k}} | = | \mathrm{第一部分} | + | \mathrm{第二部分} | + | \mathrm{第三部分} |, \tag {11.4.2}
$$

其中第一部分和第三部分是级数 $\sum_{n = 1}^{+\infty}a_n$ 中还不够形成一个完整括号的项，因此

$$
| \text {第一部分} | \leqslant N \cdot \max _ {n _ {k} + 1 <   m \leqslant n _ {k + 1}} \{| a _ {m} | \}.
$$

由于 $\lim_{n\to +\infty}a_n = 0$ ，因此，只要 $n\gg 1,k\gg 1$ ，第一部分就可以小于 $\varepsilon$

同理, 第三部分也可以小于 $\varepsilon$.

第二部分是由级数 $\sum_{n=1}^{+\infty} a_n$ 中若干个完整的括号构成, 即它们是 $\sum_{n=1}^{+\infty} \tilde{a}_n$ 中若干项. 因此, 只要 $n \gg 1, k \gg 1$, 则根据 (11.4.1) 式知这一部分也可以小于 $\varepsilon$. 从而根据 Cauchy 准则以及 (11.4.2) 式, 我们不但证明了级数 $\sum_{n=1}^{+\infty} a_n$ 收敛, 还证明了它与级数 $\sum_{n=1}^{+\infty} \tilde{a}_n$ 有相同的和.

关于级数的去括号, 还有下面的定理成立.

定理 11.4.3 (去括号法则 2) 设级数 $\sum_{n=1}^{+\infty} \tilde{a}_{n}$ 是由级数 $\sum_{n=1}^{+\infty} a_{n}$ 加括号后而得, 其中 $\tilde{a}_{n}$ 是原级数的第 $n$ 个括号内的项. 假定对每个 $n$, $\tilde{a}_{n}$ 中的各项都具有相同的符号, 则 $\sum_{n=1}^{+\infty} a_{n}$ 与级数 $\sum_{n=1}^{+\infty} \tilde{a}_{n}$ 有相同的敛散性, 并且当级数收敛时, 两者有相同的和.

我们给出这个定理证明的要点分析. 技术细节读者可参考定理 11.4.2 加以补充.

首先若  $\sum_{n=1}^{+\infty}a_{n}$  收敛, 则根据定理 11.4.1 知级数  $\sum_{n=1}^{+\infty}\tilde{a}_{n}$  也收敛. 相反方向的结论, 证明思路非常类似于定理 11.4.2 的证明过程, 我们只需估计当  $n \gg 1$  时,  $\forall p > 0$ , 是否有  $|a_{n+1} + \cdots + a_{n+p}|$  充分小. 将此和式分成三部分: 第一部分是前面还没有形成一个完整  $\tilde{a}_{n}$  的若干项, 第二部分是中间形成完整  $\tilde{a}_{n}$  的项, 第三部分还是没有形成一个完整  $\tilde{a}_{n}$  的项. 显然有

$$
| a _ {n + 1} + \dots + a _ {n + p} | \leqslant | \text {第一部分} | + | \text {第二部分} | + | \text {第三部分} |.
$$

首先第二部分可以对级数 $\sum_{n=1}^{+\infty} \tilde{a}_n$ 应用 Cauchy 准则, 因此可以得到它的估计. 即, 如果级数收敛, 则可以使得第二部分充分小.

对于第一部分, 我们在它的首项前面补充若干项, 使得成为一个完整的括号, 即成为某一项  $\tilde{a}_{m}$ . 由于括号内的项具有相同的正负性, 因此,

$$
| \mathrm{第一部分} | \leqslant | \mathrm{对应的一个完整的括号} | = | \tilde {a} _ {m} |,
$$

其中 $\tilde{a}_m$ 是级数 $\sum_{n=1}^{+\infty} \tilde{a}_n$ 中的一项. 因此, 只要该级数收敛, 通项就必然趋于 0 , 所以这一项可以做到充分小.

同理, 对于第三部分, 可以类似讨论.

## 11.4.2 级数运算的交换律

我们知道, 有限个实数的加法满足交换律, 即被加项可以任意交换求和次序而不影响其和. 但是, 当无限多个数相加, 即级数求和时, 一般说来, 如果任意交换求和次序的话, 有可能改变原级数的敛散性, 而且即使收敛, 其和也有可能改变. 由于显然如果只交换级数中有限多项的次序, 则既不改变级数的收敛性, 也不会改变它的和, 因此, 除非特别声明, 当说交换级数的求和次序时, 我们默认是指改变无穷多项的求和次序.

我们首先定义正整数集 $N_{+}$ 的重排:

集合 $\mathbb{N}_{+}$ 的一个重排是指 $\mathbb{N}_{+}$ 到 $\mathbb{N}_{+}$ 的一个一一对应, 记此对应关系为 $\varphi(n), n \in \mathbb{N}_{+}$. 在上下文清楚时, 我们也简称“重排 $\varphi(n)$”“重排 $\psi(n)$”等.

级数的重排可以通过 $\mathbb{N}_{+}$ 的重排来刻画: 称级数 $\sum_{n=1}^{+\infty} b_{n}$ 是级数 $\sum_{n=1}^{+\infty} a_{n}$ 的一个重排, 是指存在 $\mathbb{N}_{+}$ 的一个重排 $\varphi(n)$, 使得 $b_{n} = a_{\varphi(n)}$. 即 $\sum_{n=1}^{+\infty} b_{n} = \sum_{n=1}^{+\infty} a_{\varphi(n)}$.

我们看到, 重排 $\varphi(n)$ 的效果是把原来位于 $n$ 处的项“搬”到了位置 $\varphi(n)$. 因此, 我们可以很形象地通过 $|\varphi(n) - n|$ 的大小确定位置 $n$ 处的项被搬动的远近. 如果存在实数 $M > 0$ ，使得对任意的 $n\in \mathbb{N}_{+}$ ，都有 $|\varphi (n) - n| < M$ ，则称 $\varphi (n)$ 是一个有界重排

级数重排的直观理解就是原来级数中的每一项都搬家了(原地不动称之为“平凡搬家”),而有界重排则是指级数的每一项被搬到了离“老家”最远不超过M的“新家”.关于有界重排,成立下面有趣的结论:

定理 11.4.4（有界重排法则） 级数的有界重排既不改变其敛散性，在收敛的情况下也不改变其和.

证明 设级数 $\sum_{n=1}^{+\infty} a_n$ 收敛, $\varphi(n)$ 是 $\mathbb{N}_+$ 的一个有界重排. 我们证明级数 $\sum_{n=1}^{+\infty} a_{\varphi(n)}$ 收敛, 并且和不变. 事实上, 设对任意的 $n$, 有 $|\varphi(n) - n| \leqslant M$, 其中 $M$ 是一个正整数. 因为 $\sum_{n=1}^{+\infty} a_n$ 收敛, 所以有 $\lim_{n \to +\infty} a_n = 0$, 从而有 $\lim_{n \to +\infty} \sum_{i=-M}^{M} |a_{n+i}| = 0$. 设 $\{S_n\}$ 和 $\{S_n'\}$ 分别为级数 $\sum_{n=1}^{+\infty} a_n$ 和 $\sum_{n=1}^{+\infty} a_{\varphi(n)}$ 的部分和数列. 则有 $|S_n - S_n'| \leqslant \sum_{i=-M}^{M} |a_{n+i}| \to 0 (n \to +\infty)$. 因此 $\lim_{n \to +\infty} S_n = \lim_{n \to +\infty} S_n'$.

同理, 若  $\sum_{n=1}^{+\infty}a_{\varphi(n)}$  收敛, 则通过考虑有界重排  $\varphi^{-1}(n)$  可知级数  $\sum_{n=1}^{+\infty}a_{n}$  收敛.

反之, 如果级数 $\sum_{n=1}^{+\infty} a_n$ 发散, 则其有界重排 $\sum_{n=1}^{+\infty} a_{\varphi(n)}$ 也必然发散. 因若不然, 根据上述论证, 经过有界重排 $\varphi^{-1}(n)$ 后的级数 $\sum_{n=1}^{+\infty} a_n$ 仍收敛, 与假设矛盾. □

绝对收敛级数的重排成立下面的重要结论, 无须有界性假设.

定理 11.4.5 绝对收敛级数的任意重排仍绝对收敛, 且其和不变.

证明 设 $\sum_{n=1}^{+\infty} a_n$ 绝对收敛, $\sum_{n=1}^{+\infty} a_{\varphi(n)}$ 是它的一个重排.

对于 $n \geqslant 1$, 令 $N_{n}$ 为使得 $\{k|1 \leqslant k \leqslant N\} \subseteq E_{n} := \{\varphi(k)|1 \leqslant k \leqslant n\}$ 的最大的 $N$, 若 $1 \notin E_{n}$, 规定 $N_{n}$ 为零. 根据重排的定义, 可得 $\lim_{n \to +\infty} N_{n} = +\infty$.

我们有

$$
\left| \sum_ {k = 1} ^ {n} a _ {\varphi (k)} - \sum_ {k = 1} ^ {N _ {n}} a _ {k} \right| \leqslant \sum_ {k = N _ {n} + 1} ^ {+ \infty} | a _ {k} |.
$$

于是由 $\sum_{n=1}^{+\infty} a_n$ 的绝对收敛性得到

$$
\lim _ {n \to + \infty} \sum_ {k = 1} ^ {n} a _ {\varphi (k)} = \lim _ {n \to + \infty} \sum_ {k = 1} ^ {N _ {n}} a _ {k}.
$$

即 $\sum_{n=1}^{+\infty} a_{\varphi(n)}$ 收敛且和为 $\sum_{n=1}^{+\infty} a_n$.

同理, $\sum_{n=1}^{+\infty}|a_{\varphi(n)}|$ 收敛到 $\sum_{n=1}^{+\infty}|a_n|$. 即重排级数 $\sum_{n=1}^{+\infty}a_{\varphi(n)}$ 绝对收敛, 且和不变. $\square$

条件收敛级数的重排就没有上述定理中那么强的结论了, 当然我们也可以说条件收敛级数的重排可以产生更为丰富的现象. 具体来说, 条件收敛的级数, 重排有可能改变其敛散性, 而且即使在收敛的情况下, 重排后的级数的和通常也很 “脆弱”, 严重依赖于重排的方式.

我们先讨论一下条件收敛的级数的基本性质:

命题 11.4.6 设级数  $\sum_{n=1}^{+\infty}a_{n}$  条件收敛, 则其正、负项部分构成的级数均发散: 即

$$
\sum_ {n = 1} ^ {+ \infty} a _ {n} ^ {+} = \sum_ {n = 1} ^ {+ \infty} a _ {n} ^ {-} = + \infty ,
$$

其中

$$
a _ {n} ^ {+} = \left\{ \begin{array}{l l} a _ {n}, & a _ {n} \geqslant 0, \\ 0, & a _ {n} <   0, \end{array} \right. \quad a _ {n} ^ {-} = \left\{ \begin{array}{l l} 0, & a _ {n} \geqslant 0, \\ - a _ {n}, & a _ {n} <   0. \end{array} \right.
$$

证明 注意到 $a_{n}^{\pm} = \frac{1}{2} (|a_{n}| \pm a_{n}) \geqslant 0$，以及 $\sum_{n=1}^{+\infty} a_{n} \in c, \sum_{n=1}^{+\infty} |a_{n}| \in d,$ 故 $\sum_{n=1}^{+\infty} a_{n}^{\pm}$ 均发散到 $+\infty$.

定理 11.4.7 (Riemann 重排定理) 设  $\sum_{n=1}^{+\infty} a_{n}$  条件收敛, 则该级数经重排后可以

(1) 收敛到事先给定的任何实数  $\mu$ .
(2) 发散到  $\pm\infty$ ，或者使部分和数列的上、下极限收敛到事先给定的任意两个不同的实数.

下面我们只给出 (1) 的证明, (2) 的证明思路完全类似. 首先我们捋一下证明思路: 对于任意给定的实数 $\mu$ (不妨假设 $\mu > 0$), 我们依序选取级数中的正项, 对其求和, 因为正项部分和发散到 $+\infty$, 所以加到适当的时候必有正项部分和大于 $\mu$. 一旦其和大于 $\mu$, 我们就开始按负项的出场顺序依次加上负项, 由于负项部分和发散到 $-\infty$, 故加到适当时候, 上述之和必定不再大于 $\mu$. 一旦其和不大于 $\mu$, 我们就再从上次停止的正项处添加下一个正项, 直到其和再次大于 $\mu$, 将此过程一直进行下去, 使得其和围绕着 $\mu$ 上下振荡. 因为原级数收敛, 所以通项趋于零, 因此偏离 $\mu$ 的振幅趋于零, 即如此构造的正负相间的部分和序列极限为 $\mu$. 显然这是原级数的一个重排. 下面我们给出严格的证明.

证明 设 $\{a_{n}\}$ 中第 $k$ 个非负数为 $b_{k}$, 第 $j$ 个负数为 $-c_{j}$. 则

$$
\lim _ {n \to + \infty} b _ {n} = \lim _ {n \to + \infty} c _ {n} = 0, \tag {11.4.3}
$$

$$
\sum_ {n = 1} ^ {+ \infty} b _ {n} = \sum_ {n = 1} ^ {+ \infty} c _ {n} = + \infty . \tag {11.4.4}
$$

对于任意实数  $\mu\in\mathbb{R}$  (不妨  $\mu\geqslant0$ ), 取  $a_{n_{1}}$  为  $b_{1}$ . 若已经选定  $a_{n_{1}},a_{n_{2}},\cdots,a_{n_{m}}$   $(m\geqslant1)$ , 记  $S_{m}:=\sum_{j=1}^{m}a_{n_{j}}$ .

(i) 当  $S_{m} \geqslant \mu$  时, 选数列  $\{-c_{n}\}$  中未被取走的元素中的第一个为  $a_{n_{m+1}}$ .
(ii) 当  $S_{m} < \mu$  时, 选数列  $\{b_{n}\}$  中未被取走的元素中的第一个为  $a_{n_{m+1}}$ .

由于 (11.4.4) 式, $a_{n_k}$ 不可能一直在 $\{b_n\}$ 中选, 或一直在 $\{-c_n\}$ 中选. 因此, $\sum_{k=1}^{+\infty} a_{n_k}$ 为 $\sum_{n=1}^{+\infty} a_n$ 的重排.

进一步, 设 $N_{m}$ 是使得 $\{S_{k} | N \leqslant k \leqslant m\}$ 与 $(-\infty, \mu)$ 和 $[\mu, +\infty)$ 的交均非空的最大的 $N$ (这样的 $N$ 不存在时, $N_{m} := 1$), 则 $\lim_{m \to +\infty} N_{m} = +\infty$. 易见当 $k > m$ 时, 成立

$$
- \inf _ {j \geqslant N _ {m}} a _ {n _ {j}} ^ {-} \leqslant S _ {k} - \mu \leqslant \sup _ {j \geqslant N _ {m}} a _ {n _ {j}} ^ {+}.
$$

由此即得  $\sum_{k=1}^{+\infty}a_{n_{k}}$  收敛到  $\mu$ .

![](images/page_423_image_10.jpg)

例 11.4.1 构造条件收敛级数  $\sum_{n=1}^{+\infty}\frac{(-1)^{n+1}}{n}$  的一个重排, 使得重排后的级数收敛到  $\frac{3}{2}\ln2$ .

解 注意到

$$
1 + \frac {1}{2} + \dots + \frac {1}{n} = \ln n + \gamma + \varepsilon_ {n}, \tag {11.4.5}
$$

其中  $\gamma$  是 Euler 常数,  $\varepsilon_{n} \rightarrow 0 (n \rightarrow +\infty)$ . 考虑如下重排级数:

$$
1 + \frac {1}{3} - \frac {1}{2} + \frac {1}{5} + \frac {1}{7} - \frac {1}{4} + \dots + \frac {1}{4 n - 3} + \frac {1}{4 n - 1} - \frac {1}{2 n} + \dots , \tag {11.4.6}
$$

记此级数的部分和为 $\tilde{S}_n$ .则

$$
\begin{array}{l} \tilde {S} _ {3 n} = \sum_ {k = 1} ^ {n} \left(\frac {1}{4 k - 3} + \frac {1}{4 k - 1} - \frac {1}{2 k}\right) \\ = \sum_ {k = 1} ^ {4 n} \frac {1}{k} - \sum_ {k = 1} ^ {n} \left(\frac {1}{4 k - 2} + \frac {1}{4 k} + \frac {1}{2 k}\right) \\ = \sum_ {k = 1} ^ {4 n} \frac {1}{k} - \frac {1}{2} \left(\sum_ {k = 1} ^ {2 n} \frac {1}{k} - \frac {1}{2} \sum_ {k = 1} ^ {n} \frac {1}{k}\right) - \frac {3}{4} \sum_ {k = 1} ^ {n} \frac {1}{k}. \\ \end{array}
$$

将关系式 (11.4.5) 代入到上面表达式中, 可得

$$
\tilde {S} _ {3 n} \rightarrow \frac {3}{2} \ln 2 \qquad (n \rightarrow + \infty).
$$

又因为

$$
\tilde {S} _ {3 n + 1} = \tilde {S} _ {3 n} + \frac {1}{4 n + 1} \rightarrow \frac {3}{2} \ln 2 \quad (n \rightarrow + \infty),
$$

$$
\tilde {S} _ {3 n + 2} = \tilde {S} _ {3 n + 1} + \frac {1}{4 n + 3} \rightarrow \frac {3}{2} \ln 2 \quad (n \rightarrow + \infty),
$$

所以重排后的级数收敛到给定的值  $\frac{3}{2}\ln2$ .

![](images/page_424_image_6.jpg)

注 11.4.2 此例中的重排级数 (11.4.6) 初看起来有点神奇, 其实它的构造过程本质上就是定理 11.4.7 证明过程的具体实现. 另外, 收敛于给定实数  $\mu$  的重排显然不是唯一的.

## 11.4.3 级数运算的分配律

我们知道两个有限和 $\sum_{n=1}^{N} a_n$ 和 $\sum_{n=1}^{M} b_n$ 的乘积满足加法和乘法的分配律, 其值等于一切可能的形如 $a_i b_j$ 的项的和

$$
\left(\sum_{n = 1}^{N}a_{n}\right)\cdot \left(\sum_{n = 1}^{M}b_{n}\right) = \sum_{\substack{1\leqslant i\leqslant N\\ 1\leqslant j\leqslant M}}a_{i}b_{j}.
$$

同时, 我们也知道收敛级数对于实数  $\lambda$  的分配律也成立:

$$
\lambda \cdot \left(\sum_ {n = 1} ^ {+ \infty} a _ {n}\right) = \sum_ {n = 1} ^ {+ \infty} \lambda \cdot a _ {n}.
$$

由这两点, 进一步可得

$$
(b_{1} + b_{2} + \dots +b_{N})\cdot \sum a_{n} = \sum_{\substack{1\leqslant n <   + \infty \\ 1\leqslant i\leqslant N}}a_{n}b_{i}.
$$

一个自然的问题是如果两个无穷级数相乘, 是否也有分配律成立. 下面我们给出一些讨论.

首先可以看出, 两个级数 $\sum_{n=1}^{+\infty} a_n$ 和 $\sum_{n=1}^{+\infty} b_n$ 形式上的分配律给出了所有形如 $a_i b_j$ 的项, 把这些项排成一个无穷阶矩阵的形式

$$
\left( \begin{array}{c c c c c} a _ {1} b _ {1} & a _ {1} b _ {2} & \dots & a _ {1} b _ {n} & \dots \\ a _ {2} b _ {1} & a _ {2} b _ {2} & \dots & a _ {2} b _ {n} & \dots \\ \vdots & \vdots & & \vdots \\ a _ {n} b _ {1} & a _ {n} b _ {2} & \dots & a _ {n} b _ {n} & \dots \\ \vdots & \vdots & & \vdots \end{array} \right).
$$

我们感兴趣的是这些项相加时的敛散性, 以及收敛时其和与求和次序的依赖关系.

把这矩阵中的无穷多个元素排序然后相加, 显然有无穷多种排序方式. 常用的排序方式包括正方形法和对角线法.

正方形排序法是指如下求和方式:记 $\sum_{n=1}^{+\infty} a_n$ 和 $\sum_{n=1}^{+\infty} b_n$ 的乘积为 $\sum_{n=1}^{+\infty} d_n$，其中

$$
\begin{array}{l} d _ {n} = a _ {1} b _ {n} + a _ {2} b _ {n} + \dots + a _ {n} b _ {n} + a _ {n} b _ {n - 1} + \dots + a _ {n} b _ {1} \\ = \sum_ {k = 1} ^ {n - 1} a _ {k} b _ {n} + \sum_ {k = 1} ^ {n - 1} b _ {k} a _ {n} + a _ {n} b _ {n}, \quad n = 1, 2, \dots . \\ \end{array}
$$

可以看出, $d_{n}$ 相当于在无穷矩阵中, 把元素 $a_{n}b_{n}$ 所在行的左边的所有元素与所在列的上方的所有元素加起来得到的和. 而部分和 $D_{n} = d_{1} + d_{2} + \dots + d_{n}$ 相当于在无穷矩阵中把元素 $a_{n}b_{n}$ 处左上角的 $n^{2}$ 个元素加起来.

分别记 $\sum_{n=1}^{+\infty} a_n, \sum_{n=1}^{+\infty} b_n$ 和 $\sum_{n=1}^{+\infty} d_n$ 的部分和分别为 $A_n, B_n$ 和 $D_n$, 则有 $D_n = A_n \cdot B_n$. 因此, 当 $\sum_{n=1}^{+\infty} a_n$ 与 $\sum_{n=1}^{+\infty} b_n$ 都收敛时, $\sum_{n=1}^{+\infty} d_n$ 也收敛, 且

$$
\sum_ {n = 1} ^ {+ \infty} d _ {n} = \left(\sum_ {n = 1} ^ {+ \infty} a _ {n}\right) \left(\sum_ {n = 1} ^ {+ \infty} b _ {n}\right). \tag {11.4.7}
$$

对角线排序法源于 Cauchy 研究幂级数乘法时产生的一种自然的求和方式. 考虑两个幂级数  $\sum_{n=0}^{+\infty} u_{n} x^{n}$  和  $\sum_{n=0}^{+\infty} v_{n} x^{n}$  的乘积, 形式上有

$$
\sum_ {n = 0} ^ {+ \infty} u _ {n} x ^ {n} \cdot \sum_ {n = 0} ^ {+ \infty} v _ {n} x ^ {n} = \sum_ {n = 0} ^ {+ \infty} w _ {n} x ^ {n}, \quad \text {其中} \quad w _ {n} = \sum_ {k = 0} ^ {n} u _ {k} v _ {n - k}, \quad n = 0, 1, 2, \dots .
$$

我们称幂级数  $\sum_{n=0}^{+\infty}w_{n}x^{n}$  为幂级数  $\sum_{n=0}^{+\infty}u_{n}x^{n}$  和  $\sum_{n=0}^{+\infty}v_{n}x^{n}$  的 Cauchy 乘积. 基于此, 更一般地, 对于级数  $\sum_{n=1}^{+\infty}a_{n}$  和  $\sum_{n=1}^{+\infty}b_{n}$ , 我们定义  $\sum_{n=1}^{+\infty}c_{n}$  为它们的 Cauchy 乘积级数, 其中  $c_{n}=a_{1}b_{n}+a_{2}b_{n-1}+\cdots+a_{n}b_{1}, n=1,2,\cdots$ .

可以看出, Cauchy 乘积级数的通项 $c_{n}$ 刚好是无穷矩阵中, 从右上角 $a_{1}b_{n}$ 到左下角 $a_{n}b_{1}$ 第 $n$ 个对角线上的 $n$ 个元素之和.

关于级数的分配律, 下面的定理成立:

定理 11.4.8 (Cauchy 定理) 设级数 $\sum_{n=1}^{+\infty} a_n$ 与 $\sum_{n=1}^{+\infty} b_n$ 均绝对收敛, 则其乘积矩阵中所有元素所构成的任何级数也绝对收敛, 并且它的和为 $\left(\sum_{n=1}^{+\infty} a_n\right)\left(\sum_{n=1}^{+\infty} b_n\right)$.

证明 设 $\sum_{n=1}^{+\infty} a_{k_n} b_{j_n}$ 是上面无穷矩阵中元素的某种次序的求和, 该级数的第 $n$ 项 $a_{k_n} b_{j_n}$ 为矩阵中的某一元素. 记

$$
M _ {n} = \max _ {1 \leqslant i \leqslant n} \{k _ {i}, j _ {i} \},
$$

则显然 $\sum_{i=1}^{n}|a_{k_i}b_{j_i}|$ 表示无穷矩阵中若干个元素取绝对值之后的和, 它应该不超过此矩阵中下标最大元素 $a_{M_n}b_{M_n}$ 左上角 $M_n^2$ 个元素取绝对值之后的和. 即

$$
\sum_ {i = 1} ^ {n} | a _ {k _ {i}} b _ {j _ {i}} | \leqslant \sum_ {k = 1} ^ {M _ {n}} | a _ {k} | \cdot \sum_ {j = 1} ^ {M _ {n}} | b _ {j} | \leqslant \sum_ {k = 1} ^ {+ \infty} | a _ {k} | \cdot \sum_ {j = 1} ^ {+ \infty} | b _ {j} |.
$$

因此级数 $\sum_{i=1}^{+\infty}\left|a_{k_i}b_{j_i}\right|$ 绝对收敛. 故根据定理 11.4.5, 它的任何一个重排也绝对收敛并且和不变. 从前面的讨论可知, 当我们取特殊的正方形排序法时, (11.4.7) 式成立, 因此定理得证. □

例 11.4.2 级数  $\sum_{n=0}^{+\infty}\frac{x^{n}}{n!}$  对任意实数 x 均绝对收敛, 因此, 将这样的两个级数  $\sum_{n=0}^{+\infty}\frac{x^{n}}{n!}$  和  $\sum_{n=0}^{+\infty}\frac{y^{n}}{n!}$  相乘, 然后取 Cauchy 乘积级数可得

$$
\left(\sum_ {n = 0} ^ {+ \infty} \frac {x ^ {n}}{n !}\right) \cdot \left(\sum_ {m = 0} ^ {+ \infty} \frac {y ^ {m}}{m !}\right) = \sum_ {\ell = 0} ^ {+ \infty} \left(\sum_ {k = 0} ^ {\ell} \frac {x ^ {k} y ^ {\ell - k}}{k ! (\ell - k) !}\right) = \sum_ {\ell = 0} ^ {+ \infty} \frac {(x + y) ^ {\ell}}{\ell !}.
$$

因此, 我们得到

$$
\mathrm{e} ^ {x + y} = \mathrm{e} ^ {x} \cdot \mathrm{e} ^ {y}.
$$

如果在定理 11.4.8 中条件减弱为两个级数中只有一个级数绝对收敛, 另一个收敛, 那么一般来说, 我们得不到定理 11.4.8 那么强的结论, 但可以得到某些特殊排序求和时的收敛, 比如 Cauchy 乘积级数收敛. 事实上, 我们有下面的 Mertens $^{①}$ 定理, 为此, 我们先证明一个引理:

引理 11.4.9 若  $\lim_{n\to+\infty}\beta_{n}=0,\sum_{n=1}^{+\infty}a_{n}$  绝对收敛, 设  $\gamma_{n}=a_{1}\beta_{n}+a_{2}\beta_{n-1}+\cdots+a_{n}\beta_{1}$ ，则  $\lim_{n\to+\infty}\gamma_{n}=0$ .

证明 事实上, 由 $\lim_{n\to +\infty}\beta_n = 0$ 知该数列有界, 即存在 $M > 0$ 使得对所有的 $n$, $|\beta_n| \leqslant M$, 而且 $\forall \varepsilon > 0$, $\exists N_1 > 0$ 当 $n > N_1$ 时, $|\beta_n| < \varepsilon$.

又由级数  $\sum_{n=1}^{+\infty}|a_{n}|$  收敛, 记其和为  $\tilde{A}$ , 知  $\tilde{A}<+\infty$ , 且  $\exists N_{2}>0$ , 使得  $n>N_{2}$  时,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Mertens, Franciszek, 1840 年 3 月 20 日—1927 年 3 月 5 日, 波兰—奥地利数学家.</span></small>

$$
| a _ {n + 1} | + | a _ {n + 2} | + \dots + | a _ {n + p} | <   \varepsilon , \quad \forall p > 0.
$$

现在取 $n > N_{1} + N_{2}$ ，则有 $n - N_{2} > N_{1}$ ，且

$$
\begin{array}{l} \left| \gamma_ {n} \right| = \left| a _ {1} \beta_ {n} + a _ {2} \beta_ {n - 1} + \dots + a _ {n} \beta_ {1} \right| \\ \leqslant (| a _ {1} | | \beta_ {n} | + \dots + | a _ {N _ {2} + 1} | | \beta_ {n - N _ {2}} |) + (| a _ {N _ {2} + 2} | | \beta_ {n - N _ {2} - 1} | + \dots + | a _ {n} | | \beta_ {1} |) \\ \leqslant (| a _ {1} | + \dots + | a _ {N _ {2} + 1} |) \varepsilon + M (| a _ {N _ {2} + 2} | + \dots + | a _ {n} |) \\ \leqslant (\tilde {A} + M) \varepsilon . \\ \end{array}
$$

定理 11.4.10 (Mertens 定理) 设级数  $\sum_{n=1}^{+\infty} a_{n}$  绝对收敛, 其和为 A,  $\sum_{n=1}^{+\infty} b_{n}$  收

敛, 其和为 $B$. 则 Cauchy 乘积级数 $\sum_{n=1}^{+\infty} c_n$ 收敛, 且其和为 $AB$, 其中

$$
c _ {n} = a _ {1} b _ {n} + a _ {2} b _ {n - 1} + \dots + a _ {n} b _ {1}.
$$

证明 设

$$
A _ {n} = \sum_ {k = 1} ^ {n} a _ {k}, \quad B _ {n} = \sum_ {k = 1} ^ {n} b _ {k}, \quad C _ {n} = \sum_ {k = 1} ^ {n} c _ {k}.
$$

则有

$$
\lim _ {n \to + \infty} A _ {n} = A, \quad \lim _ {n \to + \infty} B _ {n} = B.
$$

令 $\beta_{n} = B - \sum_{k = 1}^{n}b_{k}$ ，显然有 $\lim_{n\to +\infty}\beta_n = 0.$ 考虑

$$
C _ {n} = \sum_ {k = 1} ^ {n} c _ {k} = a _ {1} b _ {1} + (a _ {1} b _ {2} + a _ {2} b _ {1}) + \dots + (a _ {1} b _ {n} + \dots + a _ {n} b _ {1}),
$$

将等式右端重新组合可得

$$
C _ {n} = a _ {1} B _ {n} + a _ {2} B _ {n - 1} + \dots + a _ {n} B _ {1}. \tag {11.4.8}
$$

因此, 有

$$
\begin{array}{l} C _ {n} = a _ {1} (B - \beta_ {n}) + a _ {2} (B - \beta_ {n - 1}) + \dots + a _ {n} (B - \beta_ {1}) \\ = (a _ {1} + a _ {2} + \dots + a _ {n}) B - (a _ {1} \beta_ {n} + a _ {2} \beta_ {n - 1} + \dots + a _ {n} \beta_ {1}) \\ \rightarrow A B - 0 = A B \quad (n \rightarrow + \infty). \\ \end{array}
$$

其中, 最后一步我们利用了引理 11.4.9, 定理得证.

注11.4.3 定理11.4.10中的条件“ $\sum_{n = 1}^{+\infty}a_n$ 绝对收敛， $\sum_{n = 1}^{+\infty}b_n$ 收敛”是保证Cauchy乘积级数收敛的充分而非必要条件.

事实上, 存在两个条件收敛的级数, 它们的 Cauchy 乘积级数绝对收敛. 下面我们仅给出结论, 其证明需要一点幂级数的基本知识, 我们放到例 13.5.9 中给出.

例 11.4.3 存在两个条件收敛的级数, 它们的 Cauchy 乘积级数绝对收敛.

我们需要强调指出, 一般情况下 Mertens 定理 11.4.10 的条件也很难再减弱了, 换句话说, 两个均条件收敛的级数已经不能保证其 Cauchy 乘积级数的收敛性了.

例 11.4.4 存在两个条件收敛的级数, 其 Cauchy 乘积级数发散.

解 考虑通项为  $a_{n}=\frac{(-1)^{n}}{\sqrt{n+1}}\quad(n=0,1,\cdots)$  的级数, 可以证明其自身相乘的 Cauchy 乘积级数  $\sum_{n=0}^{+\infty}c_{n}$  发散, 其中  $c_{n}=\sum_{k=0}^{n}a_{k}a_{n-k}$ . 这是因为

$$
| c _ {n} | = \sum_ {k = 0} ^ {n} \frac {1}{\sqrt {(n - k + 1) (k + 1)}} \geqslant \sum_ {k = 0} ^ {n} \frac {1}{\frac {n + 2}{2}} = \frac {2 (n + 1)}{n + 2} \geqslant 1,
$$

故 $\sum_{n=0}^{+\infty} c_n$ 发散. 这里我们应用了不等式 $\sqrt{a(b-a)} \leqslant \frac{b}{2}$, 其中 $b \geqslant a > 0$.

该例表明, 两个条件收敛的级数其 Cauchy 乘积级数有可能不收敛, 但是一个有意思的结论是, 假如其 Cauchy 乘积级数收敛, 那么它的值一定等于两个条件级数和的乘积, 即

定理 11.4.11 (Abel 定理) 设  $\sum_{n=1}^{+\infty}a_{n}=A$  和  $\sum_{n=1}^{+\infty}b_{n}=B$  均为收敛级数, 如果

它们的 Cauchy 乘积级数  $\sum_{n=1}^{+\infty}c_{n}=C$  也收敛, 其中  $c_{n}=a_{1}b_{n}+a_{2}b_{n-1}+\cdots+a_{n}b_{1}$ , 则必成立

$$
C = A B.
$$

证明 我们将用到数列极限的两个经典结论, 此处证略: 如果

$$
\lim _ {n \to + \infty} \alpha_ {n} = \alpha , \quad \lim _ {n \to + \infty} \beta_ {n} = \beta,
$$

则

$$
\lim _ {n \to + \infty} \frac {\alpha_ {1} + \alpha_ {2} + \cdots + \alpha_ {n}}{n} = \alpha . \tag {11.4.9}
$$

$$
\lim _ {n \to + \infty} \frac {\alpha_ {1} \beta_ {n} + \alpha_ {2} \beta_ {n - 1} + \cdots + \alpha_ {n} \beta_ {1}}{n} = \alpha \beta . \tag {11.4.10}
$$

记级数 $\sum_{n=1}^{+\infty} a_n, \sum_{n=1}^{+\infty} b_n$ 和 $\sum_{n=1}^{+\infty} c_n$ 的第 $n$ 个部分和分别为 $A_n, B_n$ 和 $C_n$, 则由关系式 (11.4.8) 得

$$
\sum_ {n = 1} ^ {N} C _ {n} = A _ {1} B _ {N} + \dots + A _ {N} B _ {1}.
$$

这等价于

$$
\frac {1}{N} \sum_ {n = 1} ^ {N} C _ {n} = \frac {A _ {1} B _ {N} + \cdots + A _ {N} B _ {1}}{N}.
$$

上式两端取 $N\to +\infty$ 的极限，再注意到结论(11.4.9)式和(11.4.10)式，可得 $C = AB$ □

最后我们举例说明另一类极端, 算是从另一个角度理解相关内容: 类似于两个发散级数的和有可能收敛一样, 两个发散级数的 Cauchy 乘积级数也有可能收敛. 读者可以验证下面两个发散级数的 Cauchy 乘积级数收敛.

$$
\sum a _ {n} = 1 - 1 + 1 - 1 + \dots , \quad \sum b _ {n} = 1 + \left(2 + \frac {1}{2}\right) + \left(2 ^ {2} + \frac {1}{2 ^ {2}}\right) + \left(2 ^ {3} + \frac {1}{2 ^ {3}}\right) + \dots .
$$

## 习题11.4

1. 问是否存在这样的级数: 通项趋于零, 加括号时收敛, 去括号后发散? 如果不存在, 给出证明; 如果存在, 试构造一个.
2. 证明: 如果两个通项不恒为零的正项级数, 一个收敛一个发散, 则两者的 Cauchy 乘积级数必然发散.
3. 试构造两个级数  $\sum_{n=1}^{+\infty}a_{n}$  和  $\sum_{n=1}^{+\infty}b_{n}$ ，其一绝对收敛，另一个条件收敛，但正方形乘积求和的级数  $\sum_{n=1}^{+\infty}d_{n}$  发散，其中  $d_{n}=a_{1}b_{n}+a_{2}b_{n}+\cdots+a_{n}b_{n}+a_{n}b_{n-1}+\cdots+a_{n}b_{1}$ .
4. (Hölder 不等式) 设 $p > 1$, $\frac{1}{p} + \frac{1}{q} = 1$, $\sum_{k=1}^{+\infty}|x_k|^p$ 和 $\sum_{k=1}^{+\infty}|y_k|^q$ 均收敛, 证明: $\sum_{k=1}^{+\infty}|x_k y_k|$ 也收敛, 且

$$
\sum_ {k = 1} ^ {+ \infty} | x _ {k} y _ {k} | \leqslant \left(\sum_ {k = 1} ^ {+ \infty} | x _ {k} | ^ {p}\right) ^ {\frac {1}{p}} \left(\sum_ {k = 1} ^ {+ \infty} | y _ {k} | ^ {q}\right) ^ {\frac {1}{q}}.
$$

5. (Minkowski 不等式) 设 $p > 1$, $\sum_{k=1}^{+\infty}|x_k|^p$ 和 $\sum_{k=1}^{+\infty}|y_k|^p$ 均收敛, 证明:

$$
\left(\sum_ {k = 1} ^ {+ \infty} | x _ {k} + y _ {k} | ^ {p}\right) ^ {\frac {1}{p}} \leqslant \left(\sum_ {k = 1} ^ {+ \infty} | x _ {k} | ^ {p}\right) ^ {\frac {1}{p}} + \left(\sum_ {k = 1} ^ {+ \infty} | y _ {k} | ^ {p}\right) ^ {\frac {1}{p}}.
$$

6. 设 $1 \leqslant p < +\infty$, 定义

$$
\ell_ {p} := \left\{(a _ {1}, a _ {2}, \dots) \Bigg | \sum_ {n = 1} ^ {+ \infty} | a _ {n} | ^ {p} <   + \infty \right\},
$$

$\ell_{+\infty}:=\{(a_{1},a_{2},\cdots)\mid \sup |a_{i}| < + \infty \}$ 是所有有界数列构成的集合.

证明:(1) 在通常的数列加法和数乘意义下，对所有的 $1 \leqslant p \leqslant +\infty$ ，集合 $\ell_p$ 形成一个线性空间.

(2) 如果 p < q, 证明:  $\ell_{p} \subsetneq \ell_{q}$ .

## 11.5 无穷乘积

本节我们简要讨论一下无穷多个实数相乘的问题.

给定实数列 $\{a_{n}\}$, 形式乘积

$$
a _ {1} \cdot a _ {2} \dots a _ {n} \dots
$$

为由数列 $\{a_{n}\}$ 定义的无穷乘积. 记

$$
T _ {n} = \prod_ {k = 1} ^ {n} a _ {k}, \quad n = 1, 2, \dots ,
$$

称之为该数列的第 $n$ 个部分积, $a_{n}$ 称为无穷乘积的通项. 由于乘法的一个显著特点是只要有一个因子为0, 则乘积为0, 因此给定序列中我们默认所有项非零.

定义 11.5.1 设  $\{a_{n}\}$  是一个给定数列, 如果其部分积数列  $\{T_{n}\}$  极限  $\lim_{n\to+\infty}T_{n}=a$  存在有限且非零, 则称无穷乘积  $\prod_{n=1}^{+\infty}a_{n}$  收敛. 并记为  $\prod_{n=1}^{+\infty}a_{n}=a$ . 否则, 如果极限不存在, 或者存在但等于零, 则称无穷乘积发散.

例11.5.1 证明:无穷乘积 $\prod_{n=2}^{+\infty}\left(1 - \frac{1}{n^2}\right)$ 是收敛的.

证明 直接计算, 有

$$
T _ {n} = \prod_ {k = 2} ^ {n} \left(1 - \frac {1}{k ^ {2}}\right) = \prod_ {k = 2} ^ {n} \left(1 - \frac {1}{k}\right)\left(1 + \frac {1}{k}\right) = \frac {1}{2} \cdot \frac {n + 1}{n} \rightarrow \frac {1}{2} \quad (n \rightarrow + \infty).\quad \square
$$

定理 11.5.1 无穷乘积  $\prod_{n=1}^{+\infty}a_{n}$  收敛的必要条件是  $\lim_{n\to+\infty}a_{n}=1$ .

证明 证明可以由

$$
a _ {n} = \frac {T _ {n}}{T _ {n - 1}} \rightarrow \frac {a}{a} = 1 \quad (n \rightarrow + \infty)
$$

得到.

由此定理可知, 对于收敛的无穷乘积, $\forall \varepsilon > 0$, 当 $n$ 充分大时, 有 $0 < 1 - \varepsilon < a_n < 1 + \varepsilon$. 又由于改变前面有限多项 (不能变为 0), 不改变无穷乘积的收敛性, 因此我们不妨假设无穷乘积的通项均为正数. 这样, 可以把无穷乘积的形式改写为 $\prod_{n=1}^{+\infty}(1 + a_n)$. 随之而来的结论是: 若无穷乘积 $\prod_{n=1}^{+\infty}(1 + a_n)$ 收敛, 则必有 $\lim_{n\to +\infty}a_n = 0$.

定理 11.5.2 设 $a_{n} > -1$, 无穷乘积 $\prod_{n=1}^{+\infty}(1 + a_{n})$ 收敛的充要条件是无穷级数 $\sum_{n=1}^{+\infty}\ln(1 + a_{n})$ 收敛. 如果分别收敛到 $T$ 和 $S$, 那么 $T = \mathrm{e}^{S}$.

证明 只要注意到定理中的无穷乘积的部分积 $T_{n}$ 和无穷级数的部分和 $S_{n}$ 之间成立关系 $T_{n} = \mathrm{e}^{S_{n}}$ 即得结论. □

定理 11.5.3 (1) 若存在某  $n_{0} > 0$  使得  $n > n_{0}$  时, 有  $a_{n} > 0$  (或  $a_{n} < 0$ ), 则无穷乘积  $\prod_{n=1}^{+\infty}(1 + a_{n})$  与无穷级数  $\sum_{n=1}^{+\infty}a_{n}$  同敛散.

(2) 如果级数  $\sum_{n=1}^{+\infty}a_{n}$  和  $\sum_{n=1}^{+\infty}a_{n}^{2}$  均收敛, 则无穷乘积  $\prod_{n=1}^{+\infty}(1+a_{n})$  也收敛.

证明 (1) 只要注意到 $\lim_{n\to +\infty}\frac{\ln(1 + a_n)}{a_n} = 1$ 可知级数 $\sum_{n=1}^{+\infty}\ln(1 + a_n)$ 与 $\sum_{n=1}^{+\infty}a_n$ 同敛散.

(2) 注意到 $a_{n} \neq 0$ 时, $\lim_{n \to +\infty} \frac{a_{n} - \ln(1 + a_{n})}{a_{n}^{2}} = \frac{1}{2}$ 以及定理11.5.2即可.

例11.5.2 计算无穷乘积 $\prod_{n=1}^{+\infty} \cos \frac{x}{2^n}, x \neq 0$.

解 注意到 $T_{n} = \prod_{k=1}^{n} \cos \frac{x}{2^{k}} = \frac{\sin x}{2^{n} \sin \frac{x}{2^{n}}} \rightarrow \frac{\sin x}{x} (n \rightarrow +\infty)$. 可得 $\prod_{n=1}^{+\infty} \cos \frac{x}{2^{n}} = \frac{\sin x}{x}$. 特别地, 取 $x = \frac{\pi}{2}$, 成立下面的等式:

$$
\frac {2}{\pi} = \sqrt {\frac {1}{2}} \cdot \sqrt {\frac {1}{2} + \frac {1}{2} \sqrt {\frac {1}{2}}} \cdot \sqrt {\frac {1}{2} + \frac {1}{2} \sqrt {\frac {1}{2} + \frac {1}{2} \sqrt {\frac {1}{2}}}} \dots .
$$

例 11.5.3 (Riemann- $\zeta$ 函数的 Euler 乘积形式) 设 $\zeta(s)=\sum_{n=1}^{+\infty}\frac{1}{n^{s}},\{p_{n}\}$ 是全体素数组成的数列. 证明:

$$
\zeta (s) = \prod_ {n = 1} ^ {+ \infty} \left(1 - \frac {1}{p _ {n} ^ {s}}\right) ^ {- 1}.
$$

证明 根据级数敛散性判别法知函数 $\zeta(s)$ 在 $s > 1$ 时有定义. 设 $s > 1, p$ 为素数, 则有如下展开式:

$$
\left(1 - \frac {1}{p ^ {s}}\right) ^ {- 1} = 1 + \frac {1}{p ^ {s}} + \dots + \frac {1}{p ^ {n s}} + \dots .
$$