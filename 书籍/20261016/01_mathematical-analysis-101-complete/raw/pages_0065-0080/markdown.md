(2) 由收敛数列的有界性, 存在常数 $M > 0$ 使得对任何 $n \geqslant 1$, 都有 $|a_{n}| \leqslant M$. 于是, $\forall \varepsilon > 0$, 存在 $N \geqslant 1$, 使得当 $n \geqslant N$ 时, 有

$$
\(| a _ {n} - A | <   \varepsilon , \quad | b _ {n} - B | <   \varepsilon . \tag {3.1.13}
$$

从而

$$
\begin{array}{l} \left| a _ {n} b _ {n} - A B \right| = \left| a _ {n} \left(b _ {n} - B\right) + B \left(a _ {n} - A\right) \right| \\ \leqslant \left| a _ {n} \right| \left| b _ {n} - B \right| + | B | \left| a _ {n} - A \right| \\ \leqslant M \varepsilon + | B | \varepsilon = (M + | B |) \varepsilon . \tag {3.1.14} \\ \end{array}
$$

因此， $\lim_{n\to +\infty}(a_nb_n) = AB.$

(3) 由 (2), 只需对 $a_{n} \equiv 1$ 的情形加以证明. 由 (1), 不妨设 $B > 0$. 由定理 3.1.1, 有 $N \geqslant 1$ 使得当 $n \geqslant N$ 时, 有 $b_{n} \geqslant \frac{B}{2}$. 此时,

$$
\left| \frac {1}{b _ {n}} - \frac {1}{B} \right| = \frac {| b _ {n} - B |}{b _ {n} B} \leqslant \frac {2}{B ^ {2}} | b _ {n} - B |. \tag {3.1.15}
$$

因此, 由 (1) 和夹逼准则即得 $\lim_{n\to +\infty}\frac{1}{b_n} = \frac{1}{B}$.

在定理3.1.3(3)中， $\{b_n\}$ 不一定恒不为零.但由保号性，存在 $n\geqslant m$ 时，$|b_n| > 0.$ 因此，定理中考虑的数列本质上是数列 $\left\{\frac{a_n}{b_n}\right\}_{m}^{\infty}$

而在 (3.1.14) 式中, 不等式的右端是 $(M + |B|)\varepsilon$ 而不是 $\varepsilon$, 其中 $M + |B|$ 是一个与 $\varepsilon$ 无关的常数 (没有特别要求 $M + |B|$ 为正数). 相较于我们刻意使得 (3.1.12) 式的右端为 $\varepsilon$, 并在 (3.1.11) 式中, 为避免分母为零而采用 $1 + |\alpha| + |\beta|$ 代替 $|\alpha| + |\beta|$, 这无疑更为方便.

例3.1.6 计算 $\lim_{n\to +\infty}\frac{5n^3 - 65n^2 + 2n - 17}{3n^3 + 4n^2 + 4n - 3}.$

解 运用极限四则运算的性质, 我们有

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {5 n ^ {3} - 6 5 n ^ {2} + 2 n - 1 7}{3 n ^ {3} + 4 n ^ {2} + 4 n - 3} = \lim _ {n \to + \infty} \frac {5 - \frac {6 5}{n} + \frac {2}{n ^ {2}} - \frac {1 7}{n ^ {3}}}{3 + \frac {4}{n} + \frac {4}{n ^ {2}} - \frac {3}{n ^ {3}}} \\ = \frac {5 - \lim _ {n \rightarrow + \infty} \frac {6 5}{n} + \lim _ {n \rightarrow + \infty} \frac {2}{n ^ {2}} - \lim _ {n \rightarrow + \infty} \frac {1 7}{n ^ {3}}}{3 + \lim _ {n \rightarrow + \infty} \frac {4}{n} + \lim _ {n \rightarrow + \infty} \frac {4}{n ^ {2}} - \lim _ {n \rightarrow + \infty} \frac {3}{n ^ {3}}} \\ = \frac {5 - 6 5 \cdot 0 + 2 \cdot 0 - 1 7 \cdot 0}{3 + 4 \cdot 0 + 4 \cdot 0 - 3 \cdot 0} = \frac {5}{3}. \tag {3.1.16} \\ \end{array}
$$

上面的计算过程以及书写方式太过详细, 对于书写和阅读都是一种负担. 一般说来, 对

于初学者, 如下写法就足够详细了:

$$
\lim _ {n \to + \infty} \frac {5 n ^ {3} - 6 5 n ^ {2} + 2 n - 1 7}{3 n ^ {3} + 4 n ^ {2} + 4 n - 3} = \lim _ {n \to + \infty} \frac {5 - \frac {6 5}{n} + \frac {2}{n ^ {2}} - \frac {1 7}{n ^ {3}}}{3 + \frac {4}{n} + \frac {4}{n ^ {2}} - \frac {3}{n ^ {3}}} = \frac {5}{3}.
$$

以后, 对于如此简单的极限, 可直接写出答案:

$$
\lim _ {n \to + \infty} \frac {5 n ^ {3} - 6 5 n ^ {2} + 2 n - 1 7}{3 n ^ {3} + 4 n ^ {2} + 4 n - 3} = \frac {5}{3}.
$$

由定理 3.1.3(1) 的结论直接可得, 任何有限个数列 “和的极限等于极限的和”. 但这一结论不能推广到无限和. 尤其要注意不能推广到形式上有限个, 实质上为无限个数列的和.

例 3.1.7 计算  $\lim_{n\to+\infty}\left(\frac{1}{n^{2}}+\frac{2}{n^{2}}+\cdots+\frac{n}{n^{2}}\right)$ .

解 如果利用“和的极限等于极限的和”得到

$$
\begin{array}{l} \lim _ {n \to + \infty} \left(\frac {1}{n ^ {2}} + \frac {2}{n ^ {2}} + \dots + \frac {n}{n ^ {2}}\right) \\ = \lim _ {n \to + \infty} \frac {1}{n ^ {2}} + \lim _ {n \to + \infty} \frac {2}{n ^ {2}} + \dots + \lim _ {n \to + \infty} \frac {n}{n ^ {2}} \\ = 0 + 0 + \dots + 0 = 0. \\ \end{array}
$$

则论证过程以及结论都是错误的. 这是因为这里和式的项数 $n$ 随着 $n$ 的增大而增大, 并没有一个上限. 以下是正确的推导过程:

$$
\begin{array}{l} \lim _ {n \to + \infty} \left(\frac {1}{n ^ {2}} + \frac {2}{n ^ {2}} + \dots + \frac {n}{n ^ {2}}\right) = \lim _ {n \to + \infty} \frac {1 + 2 + \cdots + n}{n ^ {2}} \\ = \lim _ {n \to + \infty} \frac {n (n + 1)}{2 n ^ {2}} = \frac {1}{2}. \\ \end{array}
$$

通常我们不能像例 3.1.7 那样得到和的表达式. 此时, 可通过适当的放大和缩小, 最后利用夹逼准则得到极限. 如何恰到好处地进行 “放缩”(估计), 是最能体现分析这门学科的基本技巧和思想的地方.

例3.1.8 求 $\lim_{n\to +\infty}\left(\frac{n}{n^2 + 1} +\frac{n - 1}{n^2 + 2} +\dots +\frac{1}{n^2 + n}\right)$

解 我们有

$$
\frac {n + (n - 1) + \cdots + 1}{n ^ {2} + n} \leqslant \frac {n}{n ^ {2} + 1} + \frac {n - 1}{n ^ {2} + 2} + \dots + \frac {1}{n ^ {2} + n} \leqslant \frac {n + (n - 1) + \cdots + 1}{n ^ {2}}.
$$

同例3.1.7, 可得

$$
\lim _ {n \to + \infty} \frac {n + (n - 1) + \cdots + 1}{n ^ {2} + n} = \lim _ {n \to + \infty} \frac {n + (n - 1) + \cdots + 1}{n ^ {2}} = \frac {1}{2}.
$$

于是，由夹逼准则，得到

$$
\lim _ {n \to + \infty} \left(\frac {n}{n ^ {2} + 1} + \frac {n - 1}{n ^ {2} + 2} + \dots + \frac {1}{n ^ {2} + n}\right) = \frac {1}{2}.
$$

## 习题3.1

1. 用定义证明 $\lim_{n\to +\infty}\frac{3n^3 + 4n^2 - 100}{2n^3 - 9n - 11} = \frac{3}{2}$.

2. 用定义证明 $\lim_{n\to +\infty}\lg \left(1 + \frac{1}{n}\right) = 0.$

3. 证明: $\lim_{n\to +\infty}a_n = 0$ 的充要条件是存在单调下降且无正下界的正数列 $\{\omega_n\}$ 使得 $\forall n\geqslant 1$ 有 $|a_{n}|\leqslant \omega_{n}$.

4. 计算极限  $\lim_{n\to+\infty}\frac{2\sqrt[n]{n}+\sqrt[n]{100}}{3\sqrt[n]{n}-1}$ .

5. 计算极限  $\lim_{n\to+\infty}\left(\frac{3\lg^{3}n+2\lg n+1}{2\lg^{2}n+\lg n}-\frac{6\lg^{3}n+5\lg^{2}n+3\lg n+1}{4\lg^{2}n-\lg n+2}\right)$ .

6. 计算极限  $\lim_{n\to+\infty}\left(\left(1+\frac{1}{n}\right)^{n}+\left(2+\frac{3}{n}\right)^{n}+\left(3+\frac{5}{n}\right)^{n}\right)^{\frac{1}{n}}$

7. 设  $0 \leqslant p \leqslant k - 1$ ，求: $\lim_{n \to +\infty} \frac{C_{kn}^{p} + C_{kn}^{p+k} + \cdots + C_{kn}^{p+(n-1)k}}{2^{kn}}$ .

## 3.2 无穷大量 无穷小量 Stolz 公式

易见 $\lim_{n\to +\infty}a_n = A$ 等价于 $\lim_{n\to +\infty}|a_n - A| = 0.$ 结合夹逼准则, 在证明 $\lim_{n\to +\infty}a_n = A$ 时时常寻求如下不等式:

$$
\left| a _ {n} - b _ {n} \right| \leqslant c _ {n}, \quad \forall n \gg 1,
$$

其中 $\lim_{n\to +\infty}b_n = A,\lim_{n\to +\infty}c_n = 0.$ 因此，极限为零的数列是需要特别关注的数列.类似地，也需要特别关注极限为无穷的数列.具体地，我们给出如下定义:

定义 3.2.1 考虑实数列  $\{a_{n}\}$ .

(1) 若  $\lim_{n\to+\infty}a_{n}=0$ ，则称  $\{a_{n}\}$  为无穷小量；

(2) 若对任何 $M > 0$, 存在 $N \geqslant 1$, 使得当 $n \geqslant N$ 时有 $a_{n} > M$, 则称 $\{a_{n}\}$ 为正无穷大量, 记作 $\lim_{n \to +\infty} a_{n} = +\infty$, 或 $a_{n} \to +\infty (n \to +\infty)$, 或

$$
a _ {n} \rightarrow + \infty , \qquad \text {当} n \rightarrow + \infty \text {时};
$$

(3) 若 $\{-a_{n}\}$ 是正无穷大量, 则称 $\{a_{n}\}$ 为负无穷大量, 记作 $\lim_{n\to +\infty}a_n = -\infty$, 或 $a_{n}\rightarrow -\infty (n\rightarrow +\infty)$, 或

$$
a _ {n} \rightarrow - \infty , \qquad \text {当} n \rightarrow + \infty \text {时};
$$

(4) 若  $\{|a_{n}|\}$  为正无穷大量, 则称  $\{a_{n}\}$  为无穷大量, 记作  $\lim_{n\to+\infty}a_{n}=\infty$ , 或  $a_{n}\to\infty(n\to+\infty)$ , 或

$$
a _ {n} \to \infty , \qquad \text {当} n \to + \infty \text {时}.
$$

当 $\lim_{n\to +\infty}a_n = +\infty (-\infty$ 或 $\infty)$ 时，可称 $\{a_{n}\}$ 的极限为 $+\infty (-\infty$ 或 $\infty)$. 此时，$\{a_{n}\}$ 是发散的，仍然称 $\{a_{n}\}$ 的极限不存在. 但当 $\lim_{n\to +\infty}a_n = +\infty$ 或 $-\infty$ 时，可称 $\{a_{n}\}$ 在广义实数系中的极限存在或收敛.

在极限的讨论中, 引入如下记号可以带来很大的方便.

定义 3.2.2 考虑实数列  $\{a_{n}\}$  和  $\{b_{n}\}$ . 设有  $N \geqslant 1$  使得当  $n \geqslant N$  时  $b_{n} \neq 0$ .

(1) 若  $\lim_{n\to+\infty}\frac{a_{n}}{b_{n}}=0,$  则记

$$
a _ {n} = o (b _ {n}), \qquad {\text {当}} n \to + \infty \text {时}.
$$

此时, 若 $\{a_{n}\}$ 与 $\{b_{n}\}$ 均为无穷小量, 则称 $\{a_{n}\}$ 是 $\{b_{n}\}$ 的高阶无穷小量, 称 $\{b_{n}\}$ 是 $\{a_{n}\}$ 的低阶无穷小量; 若 $\{a_{n}\}$ 与 $\{b_{n}\}$ 均为无穷大量, 则称 $\{a_{n}\}$ 是 $\{b_{n}\}$ 的低阶无穷大量, 称 $\{b_{n}\}$ 是 $\{a_{n}\}$ 的高阶无穷大量.

(2) 若  $\left\{\frac{a_{n}}{b_{n}}\right\}_{N}^{\infty}$  有界, 则记

$$
a _ {n} = O (b _ {n}), \qquad \text {当} n \to + \infty \text {时}.
$$

(3) 若 $\lim_{n\to +\infty}\frac{a_n}{b_n} = 1$ ，则称 $\{a_n\}$ 与 $\{b_n\}$ 等价，记作

$$
a _ {n} \sim b _ {n}, \qquad \text {当} n \to + \infty \text {时}.
$$

若 $\lim_{n\to +\infty}\frac{a_n}{b_n}$ 存在且不等于零, 则称 $\{a_n\}$ 与 $\{b_n\}$ 同阶.

等价和同阶主要用于 $\{a_{n}\}$ 与 $\{b_n\}$ 均为无穷大量或均为无穷小量的情形.

利用上述记号, 无穷小量可以记作 $o(1)$, 有界量可以记作 $O(1)$.

对于等价量, 利用极限的四则运算, 易见有以下结果.

定理 3.2.1 设  $\{a_{n}\}, \{b_{n}\}$  与  $\{x_{n}\}$  为实数列. 又  $\lim_{n\to+\infty}\frac{a_{n}}{b_{n}}=1,\ell$  是有限数、 $+\infty,-\infty$  或  $\infty$ .

(1) 若  $\lim_{n\to+\infty}a_{n}x_{n}=\ell,$  则  $\lim_{n\to+\infty}b_{n}x_{n}=\ell;$

(2) 若  $\lim_{n\to+\infty}\frac{x_{n}}{a_{n}}=\ell,$  则  $\lim_{n\to+\infty}\frac{x_{n}}{b_{n}}=\ell.$

证明 定理的证明是简单的. 具体地, 我们有

(1) $\lim_{n\to +\infty}b_nx_n = \lim_{n\to +\infty}(a_nx_n)\cdot \lim_{n\to +\infty}\frac{b_n}{a_n} = \ell \cdot 1 = \ell .$
(2) $\lim_{n\to +\infty}\frac{x_n}{b_n} = \lim_{n\to +\infty}\frac{x_n}{a_n}\cdot \lim_{n\to +\infty}\frac{a_n}{b_n} = \ell \cdot 1 = \ell .$

我们给出上述证明过程, 主要是希望读者在具体使用这一定理时, 心里也有这样一个证明过程.

例3.2.1 由于 $\lim_{n\to +\infty}\frac{(n + 1)^{-1}}{n^{-1}} = 1,$ 因此

$$
\lim _ {n \to + \infty} \frac {n ^ {- 1} - (n + 1) ^ {- 1}}{n ^ {- 2}} = \lim _ {n \to + \infty} \frac {n ^ {- 1} - n ^ {- 1}}{n ^ {- 2}} = 0.
$$

自然, 上述推导过程是错误的. 如果写成

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {n ^ {- 1} - (n + 1) ^ {- 1}}{n ^ {- 2}} = \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 2}} - \lim _ {n \to + \infty} \frac {(n + 1) ^ {- 1}}{n ^ {- 2}} \\ = \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 2}} - \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 2}} = 0, \\ \end{array}
$$

同样也是错误的. 第一个等式后的两个极限不存在, 因此不能用四则运算中 “和的极限等于极限的和”. 而最后一个等式的左边事实上是  $(+\infty)-(+\infty)$ , 它是没有意义的, 自然这一步也是错的.

再者, 如果写

$$
\lim _ {n \to + \infty} \frac {n ^ {- 1} + (n + 1) ^ {- 1}}{n ^ {- 1}} = \lim _ {n \to + \infty} \frac {n ^ {- 1} + n ^ {- 1}}{n ^ {- 1}} = 2,
$$

虽然结论是正确的,但过程的准确性就有疑问.自然,如下的过程是正确的:

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {n ^ {- 1} + (n + 1) ^ {- 1}}{n ^ {- 1}} = \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 1}} + \lim _ {n \to + \infty} \frac {(n + 1) ^ {- 1}}{n ^ {- 1}} \\ = \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 1}} + \lim _ {n \to + \infty} \frac {n ^ {- 1}}{n ^ {- 1}} = 1 + 1 = 2. \\ \end{array}
$$

这里我们刻意写了较完整的计算步骤. 事实上, 只要写出关键的第一步, 其后的两步可以省略.

另一方面, 我们有

定理 3.2.2 设实数列 $\{a_{n}\}$ 与 $\{b_{n}\}$ 分别为无穷小量与有界量, 则 $\{a_{n}b_{n}\}$ 为无穷小量.

例3.2.2 由于 $\lim_{n\to +\infty}\frac{1}{n} = 0,\{\sin n\}$ 有界,因此，由定理3.2.2可得 $\lim_{n\to +\infty}\frac{\sin n}{n} =$ 0.但我们不能写

$$
\lim _ {n \to + \infty} \frac {\sin n}{n} = \lim _ {n \to + \infty} \frac {1}{n} \cdot \lim _ {n \to + \infty} \sin n = 0 \cdot \lim _ {n \to + \infty} \sin n = 0.
$$

这是因为 (可以证明) $\lim_{n\to +\infty}\sin n$ 不存在.

在处理商的极限时, 时常需要面对分子、分母同时为无穷小量或无穷大量的情形, 我们称之为 $\frac{0}{0}$ 型或 $\frac{\infty}{\infty}$ 型的不定式. 对此, 一个有效的工具是以下的 Stolz-Cesàro$^{①}$ 定理$^{②}$.

定理3.2.3 设 $\{x_{n}\}$ 和 $\{y_{n}\}$ 是两个实数列, 若

(1) $\{y_{n}\}$ 严格单调增加;
(2) $\lim_{n\to +\infty}y_n = +\infty;$
(3) $\lim_{n\to +\infty}\frac{x_{n + 1} - x_n}{y_{n + 1} - y_n} = \ell$ ，其中 $\ell$ 可以是有限数、 $+\infty$ 或 $-\infty ,$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Cesàro, Ernesto, 1859 年 3 月 12 日—1906 年 9 月 12 日, 意大利数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Stolz-Cesàro 定理习惯上称为 Stolz 定理, 也常称为 Stolz 公式.</span></small>

则

$$
\lim _ {n \to + \infty} \frac {x _ {n}}{y _ {n}} = \ell . \tag {3.2.1}
$$

证明 我们仅就 $\ell$ 为有限数的情形加以证明. 其余情形类似可证.

由(2)，存在 $N_{1}\geqslant 1$ 使得当 $n\geqslant N_1$ 时，有 $y_{n} > 0$

$\forall\varepsilon\in(0,1)$ ，由(3)，存在 $N_{2}\geqslant N_{1}$ 使得当 $n\geqslant N_{2}$ 时，有

$$
\ell - \varepsilon <   \frac {x _ {n + 1} - x _ {n}}{y _ {n + 1} - y _ {n}} <   \ell + \varepsilon .
$$

即

$$
(\ell - \varepsilon) (y _ {n + 1} - y _ {n}) <   x _ {n + 1} - x _ {n} <   (\ell + \varepsilon) (y _ {n + 1} - y _ {n}).
$$

进而有

$$
(\ell - \varepsilon) \sum_ {k = N _ {2}} ^ {n - 1} \left(y _ {k + 1} - y _ {k}\right) <   \sum_ {k = N _ {2}} ^ {n - 1} \left(x _ {k + 1} - x _ {k}\right) <   (\ell + \varepsilon) \sum_ {k = N _ {2}} ^ {n - 1} \left(y _ {k + 1} - y _ {k}\right), \quad \forall n > N _ {2}.
$$

即

$$
(\ell - \varepsilon) (y _ {n} - y _ {N _ {2}}) <   x _ {n} - x _ {N _ {2}} <   (\ell + \varepsilon) (y _ {n} - y _ {N _ {2}}), \quad \forall n > N _ {2}.
$$

整理得到

$$
- \varepsilon - (\ell - \varepsilon) \frac {y _ {N _ {2}}}{y _ {n}} + \frac {x _ {N _ {2}}}{y _ {n}} <   \frac {x _ {n}}{y _ {n}} - \ell <   \varepsilon - (\ell + \varepsilon) \frac {y _ {N _ {2}}}{y _ {n}} + \frac {x _ {N _ {2}}}{y _ {n}}, \quad \forall n > N _ {2}. \tag {3.2.2}
$$

再次由条件 (2), 可得存在  $N \geqslant N_{2}$  使得当  $n \geqslant N$  时, 有

$$
\frac {\big (| \ell | + \varepsilon \big) | y _ {N _ {2}} | + | x _ {N _ {2}} |}{y _ {n}} <   \varepsilon .
$$

结合 (3.2.2) 式得到

$$
\left| \frac {x _ {n}}{y _ {n}} - \ell \right| <   2 \varepsilon , \quad \forall n \geqslant N.
$$

从而由极限定义知 (3.2.1) 式成立.

由于定理条件没有要求 $\{x_{n}\}$ 趋于无穷, 因此, 这一类型的 $\frac{x_n}{y_n}$ 称为 $\frac{*}{\infty}$ 型的不定式. 由 Stolz 定理, 可得如下推论.

推论 3.2.4 设有实数列  $\{x_{n}\}$ .

(1) 若  $\lim_{n\to+\infty}(x_{n+1}-x_n)=\ell,$  则  $\lim_{n\to+\infty}\frac{x_n}{n}=\ell,$  其中  $\ell$  可以是有限数、 $+\infty$  或  $-\infty;$
(2) 若  $\lim_{n\to+\infty}x_n=\ell,$  则  $\lim_{n\to+\infty}\frac{x_1+x_2+\cdots+x_n}{n}=\ell,$  其中  $\ell$  可以是有限数、 $+\infty$  或  $-\infty;$
(3) 若 $\{x_{n}\}$ 为正数列, 且 $\lim_{n\to +\infty}\frac{x_{n + 1}}{x_n} = \ell$, 则 $\lim_{n\to +\infty}\sqrt[n]{x_n} = \ell$, 其中 $\ell$ 可以是有限数或 $+\infty$.

易见, (1) 和 (2) 本质上是一样的. 严格说来, 目前 (3) 还不能由 Stolz 定理直接得到. 它需要结合指数函数与对数函数的连续性得到. 但我们可以仿照定理 3.2.3 的证明直接证明 (3).

例 3.2.3 设 k 为自然数, 计算  $\lim_{n\to+\infty}\frac{1^{k}+2^{k}+\cdots+n^{k}}{n^{k+1}}$ .

解 由 Stolz 定理, 我们有

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {1 ^ {k} + 2 ^ {k} + \cdots + n ^ {k}}{n ^ {k + 1}} = \lim _ {n \to + \infty} \frac {(n + 1) ^ {k}}{(n + 1) ^ {k + 1} - n ^ {k + 1}} \\ = \lim _ {n \to + \infty} \frac {n ^ {k}}{\mathrm{C} _ {k + 1} ^ {1} n ^ {k} + \mathrm{C} _ {k + 1} ^ {2} n ^ {k - 1} + \cdots + \mathrm{C} _ {k + 1} ^ {k} n + \mathrm{C} _ {k + 1} ^ {k + 1}} \\ = \frac {1}{k + 1}. \\ \end{array}
$$

结合定理 2.4.4 以及夹逼准则, 让我们有可能处理 k 不为整数时的极限. 我们把它留作习题.

例3.2.4 设 $k$ 为自然数， $\lim_{n\to +\infty}a_n = a.$ 证明:

$$
\lim _ {n \to + \infty} \frac {n ^ {k} a _ {1} + (n - 1) ^ {k} a _ {2} + \cdots + a _ {n}}{n ^ {k + 1}} = \frac {a}{k + 1}. \tag {3.2.3}
$$

证明 本例是上例的推广. 由上例的结果, 若 $a_{n} \equiv a$, 则结论成立. 鉴此, 令 $\alpha_{n} = a_{n} - a$, 则问题化为在条件 $\lim_{n \to +\infty} \alpha_{n} = 0$ 下证明

$$
\lim _ {n \to + \infty} \frac {n ^ {k} \alpha_ {1} + (n - 1) ^ {k} \alpha_ {2} + \cdots + \alpha_ {n}}{n ^ {k + 1}} = 0. \tag {3.2.4}
$$

这相当于说, 不妨设 a = 0.

我们有

$$
\left| \frac {n ^ {k} \alpha_ {1} + (n - 1) ^ {k} \alpha_ {2} + \cdots + \alpha_ {n}}{n ^ {k + 1}} \right| \leqslant \frac {| \alpha_ {1} | + | \alpha_ {2} | + \cdots + | \alpha_ {n} |}{n}, \quad n \geqslant 1.
$$

于是结合 Stolz 公式与夹逼准则得到 (3.2.4) 式. 结论得证.

易见在证明 (3.2.4) 式的过程中, 对于变量的缩放, 要比直接证明 (3.2.3) 式放得开手脚. 在下例中, 把问题化为证明某个数列的极限为零起到了重要作用.

例3.2.5 设数列 $\{2x_{n + 1} + x_n\}$ 收敛. 证明: $\{x_{n}\}$ 也收敛.

证明 不妨设 $\{2x_{n + 1} + x_n\}$ 收敛到零. 此时 $\lim_{n\to +\infty}(-1)^n (2x_{n + 1} + x_n) = 0.$ 我们有

$$
\begin{array}{l} \lim _ {n \to + \infty} (- 1) ^ {n} x _ {n} = \lim _ {n \to + \infty} \frac {(- 2) ^ {n} x _ {n}}{2 ^ {n}} \\ = \lim _ {n \to + \infty} \frac {(- 2) ^ {n + 1} x _ {n + 1} - (- 2) ^ {n} x _ {n}}{2 ^ {n + 1} - 2 ^ {n}} \\ \end{array}
$$

$$
= \lim _ {n \to + \infty} (- 1) ^ {n + 1} (2 x _ {n + 1} + x _ {n}) = 0.
$$

因此, $\{x_{n}\}$ 收敛于零.

在上面的论证中, 如果不设  $\{2x_{n+1} + x_{n}\}$  收敛到零, 则在 Stolz 公式的运用中就会遇到麻烦. 读者也可以利用反证法证明例 3.2.5 的结论.

对于分子、分母都是无穷小量的情形, 即  $\frac{0}{0}$  型的不定式, 有如下类似的结果 (同样称之为 Stolz 定理):

定理3.2.5 设有实数列 $\{x_{n}\}$ 和 $\{y_{n}\}$, 若

(1) $\{y_{n}\}$ 严格单调减少;
(2) $\lim_{n\to +\infty}x_n = \lim_{n\to +\infty}y_n = 0;$
(3) $\lim_{n\to +\infty}\frac{x_n - x_{n + 1}}{y_n - y_{n + 1}} = \ell$ ，其中 $\ell$ 可以是有限数、 $+\infty$ 或 $-\infty ,$

则

$$
\lim _ {n \to + \infty} \frac {x _ {n}}{y _ {n}} = \ell . \tag {3.2.5}
$$

证明 定理的证明与定理3.2.3的证明是完全类似的.这里我们对 $\ell = +\infty$ 的情形加以证明.其余情形类似可证.

首先, 由 (1) 和 (2), 易见 $\{y_{n}\}$ 是正数列.

$\forall M>0,$  由(3), 存在  $N\geqslant1$  使得当  $n\geqslant N$  时, 有

$$
\frac {x _ {n} - x _ {n + 1}}{y _ {n} - y _ {n + 1}} > M.
$$

即

$$
x _ {n} - x _ {n + 1} > M \Big (y _ {n} - y _ {n + 1} \Big), \qquad n \geqslant N.
$$

进而, 对任何  $m > n \geqslant N$ , 有

$$
x _ {n} - x _ {m + 1} > M \Big (y _ {n} - y _ {m + 1} \Big).
$$

在上式中令 $m\to +\infty$ 得到

$$
x _ {n} \geqslant M y _ {n}, \quad \forall n \geqslant N.
$$

即

$$
\frac {x _ {n}}{y _ {n}} \geqslant M, \quad \forall n \geqslant N.
$$

这就证明了  $\lim_{n\to+\infty}\frac{x_{n}}{y_{n}}=+\infty.$

例 3.2.6 设 k 为正整数, 计算

$$
\lim _ {n \to + \infty} \frac {(n + 1) ^ {- k - 1} + (n + 2) ^ {- k - 1} + \cdots + (2 n) ^ {- k - 1}}{n ^ {- k}}.
$$

解 要使用定理 3.2.5, 需要证明分子趋于零. 易见,

$$
0 \leqslant (n + 1) ^ {- k - 1} + (n + 2) ^ {- k - 1} + \dots + (2 n) ^ {- k - 1} \leqslant (n + 1) ^ {- k}.
$$

于是, 由夹逼准则得到

$$
\lim _ {n \to + \infty} \left((n + 1) ^ {- k - 1} + (n + 2) ^ {- k - 1} + \dots + (2 n) ^ {- k - 1}\right) = 0.
$$

这样, 由定理 3.2.5 得到

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {(n + 1) ^ {- k - 1} + (n + 2) ^ {- k - 1} + \cdots + (2 n) ^ {- k - 1}}{n ^ {- k}}. \\ = \lim _ {n \to + \infty} \frac {(n + 1) ^ {- k - 1} - (2 n + 1) ^ {- k - 1} - (2 n + 2) ^ {- k - 1}}{n ^ {- k} - (n + 1) ^ {- k}} \\ = \lim _ {n \to + \infty} \left(1 - \left(2 - \frac {1}{n + 1}\right) ^ {- k - 1} - 2 ^ {- k - 1}\right) \lim _ {n \to + \infty} \frac {1}{(n + 1) \left(\left(1 + \frac {1}{n}\right) ^ {k} - 1\right)} \\ = \frac {1 - 2 ^ {- k}}{k}. \\ \end{array}
$$

例3.2.7 设 $\ell \in \mathbb{R}$, 数列 $\{2x_{n} - x_{n + 1}\}$ 收敛于 $\ell$, 且 $\lim_{n\to +\infty}2^{-n}x_n = 0$. 证明: $\{x_{n}\}$ 也收敛于 $\ell$.

证明 由 Stolz 公式, 有

$$
\begin{array}{l} \lim _ {n \to + \infty} x _ {n} = \lim _ {n \to + \infty} \frac {2 ^ {- n} x _ {n}}{2 ^ {- n}} \\ = \lim _ {n \to + \infty} \frac {2 ^ {- n} x _ {n} - 2 ^ {- (n + 1)} x _ {n + 1}}{2 ^ {- n} - 2 ^ {- (n + 1)}} = \lim _ {n \to + \infty} (2 x _ {n} - x _ {n + 1}) = \ell . \\ \end{array}
$$

## 习题 3.2

1. 计算  $\lim_{n\to+\infty}\frac{n^{-1}-(n+1)^{-1}}{n^{-2}}$ .

2. 证明: $\lim_{n\to +\infty}\sin n$ 不存在.

3. $\{a_{n}\}$ 的极限为 $L$ 当且仅当 $\{a_{2n}\}$ 与 $\{a_{2n + 1}\}$ 的极限为 $L$, 其中 $L$ 为有限数、 $+\infty, -\infty$ 或 $\infty$.

4. 设  $\alpha > 0$ , 计算  $\lim_{n \to +\infty} \frac{1 + 2^{\alpha} + \cdots + n^{\alpha}}{n^{\alpha+1}}$ .

5. 若  $\alpha \in (-1,0)$ ，则极限  $\lim_{n\to+\infty}\frac{1+2^{\alpha}+\cdots+n^{\alpha}}{n^{\alpha+1}}$  是否存在？请说明理由。若存在，请进一步计算该极限。

6. 若  $\alpha < -1$ ，则极限  $\lim_{n\to+\infty}\frac{(n+1)^{\alpha}+(n+2)^{\alpha}+\cdots+(n+n)^{\alpha}}{n^{\alpha+1}}$  是否存在？请说明理由。若存在，请进一步计算该极限。

7. 证明定理3.2.3与定理3.2.5的未证部分.

8. 设  $x_{1}=a, x_{2}=b, x_{n+2}=\frac{1}{2}(x_{n}+x_{n+1})$  ( $n=1,2,\cdots$ ). 试证明  $\{x_{n}\}$  收敛, 并求其极限.

(提示: 计算数列的通项公式, 或利用例 3.2.5.)

9. 设  $\{x_{n}\}$  满足  $\lim_{n\to+\infty}x_{n}\sum_{k=1}^{n}x_{k}^{2}=1$ . 证明:  $\lim_{n\to+\infty}\sqrt[3]{3n}x_{n}=1$ .

10. 设 a 和 d 是给定的正数. 对于  $n = 1, 2, 3, \cdots$ , 由等差数列  $a, a + d, \cdots, a + (n - 1)d$  形成算术平均  $A_{n}$  和几何平均  $G_{n}$ , 试求  $\lim_{n \to +\infty} \frac{G_{n}}{A_{n}}$ .

11. 令 $a_{n,k} = \frac{k}{n - k + 1} (n \geqslant k \geqslant 1)$. 证明:

(1) 对于固定的  $k \geqslant 1, \{a_{n,k}\}$  是无穷小量;

(2) $A_{n}:=\prod_{k=1}^{n}a_{n,k}$ 不是无穷小量.

12. 设 $E \subseteq \mathbb{R}$ 为非空集. 证明: 存在 $E$ 中点列 $\{x_k\}$ 使得 $\lim_{k \to +\infty} x_k = \sup E$, 这里 $\sup E$ 可以是 $+\infty$.

注: 对于 $f: D \to \mathbb{R}$, 满足 $\lim_{k \to +\infty} f(x_k) = \sup_{x \in D} f(x) (\inf_{x \in D} f(x))$ 的 $D$ 中的点列 $\{x_k\}$ 称为 $f$ 在 $D$ 上的极大化序列 (极小化序列).

13. (Toeplitz $^{①}$ 定理) 设有无穷三角矩阵 $(t_{nm})_{n\geqslant m}$ :

$$
\left( \begin{array}{c c c c} t _ {1 1} & & & \\ t _ {2 1} & t _ {2 2} & & \\ t _ {3 1} & t _ {3 2} & t _ {3 3} & \\ \vdots & \vdots & \vdots & \ddots \end{array} \right)
$$

满足下列条件:

(i) 每一列元趋于零, 即  $\lim_{n\to+\infty}t_{nm}=0;$

(ii) 各行元素的绝对值之和有界, 即  $\forall n \in N_{+}$ ,

$$
| t _ {n 1} | + | t _ {n 2} | + \dots + | t _ {n n} | \leqslant K <   + \infty .
$$

记  $y_{n}=t_{n1}x_{1}+t_{n2}x_{2}+\cdots+t_{nn}x_{n}$ . 证明:

(1) 若  $\lim_{n\to+\infty}x_{n}=0$ ，则  $\lim_{n\to+\infty}y_{n}=0$ .
(2) 记  $T_{n}=t_{n1}+t_{n2}+\cdots+t_{nn}$ . 若  $\lim_{n\to+\infty}T_{n}=1$ , 且  $\lim_{n\to+\infty}x_{n}=a$  有限, 则  $\lim_{n\to+\infty}y_{n}=a$ .

14. 试考察 Stolz 定理和 Toeplitz 定理的关系.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Toeplitz, Otto, 1881 年 8 月 1 日—1940 年 2 月 15 日, 德国数学家.</span></small>

## 3.3 实数系基本定理

本节介绍实数系 $\mathbb{R}$ 中的基本定理, 这些定理在分析中有着重要的地位, 其中很多基本定理可以推广到高维情形乃至更抽象的情形.

首先, 我们重述确界存在定理, 即定理 2.3.3 和定理 2.3.5 如下:

定理 3.3.1 (1) R 中任何非空上有界集有上确界;

(2) $\mathbb{R}$ 中任何非空下有界集有下确界.

## 3.3.1 单调收敛定理

由确界存在定理, 立即导出如下的单调收敛定理.

定理 3.3.2 R 中单调有界数列都有极限.

证明 设 $\{a_{n}\}$ 是 $\mathbb{R}$ 中的单调有界数列. 不妨设 $\{a_{n}\}$ 单调增加. 令 $A = \sup_{n\geqslant 1}a_n$. 则 $\forall \varepsilon >0$, 由上确界的定义, 存在 $N\geqslant 1$ 使得 $a_{N} > A - \varepsilon$. 于是由 $\{a_{n}\}$ 单增, 当 $n\geqslant N$ 时, 有 $A - \varepsilon < a_N\leqslant a_n\leqslant A$.

这样, 由极限定义得到 $\lim_{n\to +\infty}a_n = A$, 即 $\{a_n\}$ 有极限.

注意, 数列的极限为无穷不能够说成数列 “有极限”.

另一方面, 若 $\{a_{n}\}$ 单调增加, 则总有 $\lim_{n\to +\infty}a_n = \sup_{n\geqslant 1}a_n$. 同样地, 若 $\{a_{n}\}$ 单调减少, 则有 $\lim_{n\to +\infty}a_n = \inf_{n\geqslant 1}a_n$. 无论哪种情形, 我们都可以说, $\lim_{n\to +\infty}a_n$ 在广义实数系中存在.

例 3.3.1 设  $x_{0}>0, x_{n+1}=\sqrt{2+x_{n}} (n\geqslant0)$ . 证明  $\{x_{n}\}$  收敛并求极限.

证明 易见  $\{x_{n}\}$  是正数列. 进一步, 由递推公式,

$$
x _ {n + 1} - x _ {n} = \sqrt {2 + x _ {n}} - x _ {n} = \frac {(2 - x _ {n}) (1 + x _ {n})}{\sqrt {2 + x _ {n}} + x _ {n}}, \quad \forall n \geqslant 0. \tag {3.3.1}
$$

若 $x_0 \geqslant 2$，则利用递推式归纳可得 $x_n \geqslant 2 (\forall n \geqslant 0)$。进而，利用 (3.3.1) 式归纳可得 $\{x_n\}$ 单调减少。

若 $0 < x_0 < 2$, 归纳可得 $x_n < 2 (\forall n \geqslant 0)$. 进而, 利用 (3.3.1) 式归纳可得 $\{x_n\}$ 单调增加.

总之, $\{x_{n}\}$ 单调有界, 因此有极限, 设极限为 $L$. 则 $L \geqslant 0$. 将递推式平方后, 两端求极限得到 $L^{2} = 2 + L$. 结合 $L \geqslant 0$ 得到 $L = 2$. 即 $\lim_{n \to +\infty} x_{n} = 2$.

例3.3.2 设 $x_0 > 0, x_{n+1} = 2 + \frac{1}{x_n} (n \geqslant 0)$. 证明 $\{x_n\}$ 收敛并求极限.

证明 利用递推公式归纳可证

$$
x _ {n} > 2, \quad \forall n \geqslant 1.
$$

进而

$$
2 <   x _ {n} <   2 + \frac {1}{2}, \quad \forall n \geqslant 2.
$$

进一步, 由递推公式可得,

$$
\begin{array}{l} x _ {n + 2} - x _ {n} = \frac {1}{x _ {n + 1}} - \frac {1}{x _ {n - 1}} = - \frac {x _ {n + 1} - x _ {n - 1}}{x _ {n + 1} x _ {n - 1}} \\ = \frac {x _ {n} - x _ {n - 2}}{x _ {n + 1} x _ {n - 1} x _ {n} x _ {n - 2}}, \quad \forall n \geqslant 2. \tag {3.3.2} \\ \end{array}
$$

这表明 $x_{n + 2} - x_n$ 与 $x_{n} - x_{n - 2}$ 同时为正、或同时为负、或同时为零.由此可见 $\{x_{2n}\}$ 与$\{x_{2n + 1}\}$ 都是单调有界数列，从而都收敛.设它们的极限依次为 $L$ 与 $\ell$ .则 $L,\ell \in \left[2,\frac{5}{2}\right]$

$$
L = 2 + \frac {1}{\ell}, \quad \ell = 2 + \frac {1}{L}.
$$

解得 $L = \ell = 1 + \sqrt{2}$. 即 $\{x_{2n}\}$ 与 $\{x_{2n+1}\}$ 均收敛到同一极限. 因此, $\{x_n\}$ 收敛, 且 $\lim_{n\to +\infty}x_n = 1 + \sqrt{2}$. □

例3.3.3 设 $x_0 \in (0,1)$, $x_{n+1} = x_n - x_n^3$ ($n \geqslant 0$). 证明: $\lim_{n \to +\infty} \sqrt{n} x_n = \frac{\sqrt{2}}{2}$.

证明 归纳可证 $\{x_{n}\}$ 为单调下降的正数列，从而收敛.设其极限为 $L$ ，则 $L = L - L^{3}$ .从而 $L = 0$ 即 $\lim_{n\to +\infty}x_n = 0.$ 于是

$$
\lim _ {n \to + \infty} \frac {x _ {n + 1}}{x _ {n}} = \lim _ {n \to + \infty} \left(1 - x _ {n} ^ {2}\right) = 1.
$$

而由 Stolz 公式,

$$
\begin{array}{l} \lim _ {n \to + \infty} \frac {x _ {n} ^ {- 2}}{n} = \lim _ {n \to + \infty} (x _ {n + 1} ^ {- 2} - x _ {n} ^ {- 2}) = \lim _ {n \to + \infty} \frac {x _ {n} ^ {2} - x _ {n + 1} ^ {2}}{x _ {n + 1} ^ {2} x _ {n} ^ {2}} \\ = \lim _ {n \to + \infty} \frac {x _ {n} ^ {4} (2 - x _ {n} ^ {2})}{x _ {n} ^ {4} (1 - x _ {n} ^ {2}) ^ {2}} = 2. \\ \end{array}
$$

即 $\lim_{n\to +\infty}nx_n^2 = \frac{1}{2}$ .最后，由

$$
\left| \sqrt {n} x _ {n} - \frac {\sqrt {2}}{2} \right| = \left| \frac {n x _ {n} ^ {2} - \frac {1}{2}}{\sqrt {n} x _ {n} + \frac {\sqrt {2}}{2}} \right| \leqslant \sqrt {2} \left| n x _ {n} ^ {2} - \frac {1}{2} \right|
$$

与夹逼准则得到 $\lim_{n\to +\infty}\sqrt{n} x_n = \frac{\sqrt{2}}{2}$ 今后，利用 $\sqrt{x}$ 的连续性与 $\lim_{n\to +\infty}nx_n^2 = \frac{1}{2}$ 以及$\{x_n\}$ 为正数列，可直接得到上述结论. □

## 3.3.2 e 的定义

人们发现, 用形为 $\left(1 + \frac{1}{10^n}\right)^{10^n}$ 或 $\left(1 - \frac{1}{10^n}\right)^{10^n}$ 这样的数字作底数, 制作对数表就比较简单. 而 $n$ 取得越大, 则对数表可达到的精度越大.

进一步, 人们发现数列 $\left\{\left(1 + \frac{1}{n}\right)^n\right\}$ 有极限, Euler① 将该极限记为 e. 在现代数学中, e 和圆周率 $\pi$ 时常出现在各种场合, 成为最重要的两个常数.

定理 3.3.3 数列  $\left\{\left(1+\frac{1}{n}\right)^{n}\right\}$  严格单增且有界, 从而收敛.

证明 我们用两种方法给出证明.

证法 1 对任何  $n \geqslant 1$ ，利用算术几何平均不等式，

$$
\left(1 + \frac {1}{n}\right) ^ {n} = \left(1 + \frac {1}{n}\right) ^ {n} \cdot 1 <   \left(\frac {n \left(1 + \frac {1}{n}\right) + 1}{n + 1}\right) ^ {n + 1} = \left(1 + \frac {1}{n + 1}\right) ^ {n + 1}, \tag {3.3.3}
$$

$$
\left(1 + \frac {1}{n}\right) ^ {n + 1} = \frac {1}{\left(\frac {n}{n + 1}\right) ^ {n + 1} \cdot 1} > \frac {1}{\left(\frac {(n + 1) \frac {n}{n + 1} + 1}{n + 2}\right) ^ {n + 2}} = \left(1 + \frac {1}{n + 1}\right) ^ {n + 2}. \tag {3.3.4}
$$

因此, $\left\{\left(1+\frac{1}{n}\right)^{n}\right\}$ 严格单增而 $\left\{\left(1+\frac{1}{n}\right)^{n+1}\right\}$ 严格单减.

从而

$$
2 = (1 + 1) ^ {1} \leqslant \left(1 + \frac {1}{n}\right) ^ {n} <   \left(1 + \frac {1}{n}\right) ^ {n + 1} \leqslant (1 + 1) ^ {2} = 4.
$$

于是, 又得到  $\left\{\left(1+\frac{1}{n}\right)^{n}\right\}$  有界, 从而收敛.

证法 2 对任何  $n \geqslant 1$ ，利用二项展开式，我们有

$$
\left(1 + \frac {1}{n}\right) ^ {n} = 1 + 1 + \frac {1}{2 !} \left(1 - \frac {1}{n}\right) + \dots + \frac {1}{n !} \prod_ {k = 1} ^ {n - 1} \left(1 - \frac {k}{n}\right). \tag {3.3.5}
$$

直接与  $\left(1+\frac{1}{n+1}\right)^{n+1}$  的展开式

$$
1 + 1 + \frac {1}{2 !} \left(1 - \frac {1}{n + 1}\right) + \dots + \frac {1}{n !} \prod_ {k = 1} ^ {n - 1} \left(1 - \frac {k}{n + 1}\right) + \frac {1}{(n + 1) !} \prod_ {k = 1} ^ {n} \left(1 - \frac {k}{n + 1}\right)
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Euler, Leonhard, 1707 年 4 月 15 日—1783 年 9 月 18 日, 瑞士数学家、自然科学家.</span></small>

比较, 即得 $\left\{\left(1 + \frac{1}{n}\right)^n\right\}$ 严格单增. 另一方面, 由 (3.3.5) 式还可以得到

$$
2 \leqslant \left(1 + \frac {1}{n}\right) ^ {n} \leqslant \sum_ {k = 0} ^ {n} \frac {1}{k !} <   2 + \sum_ {k = 2} ^ {\infty} \frac {1}{2 ^ {k - 1}} = 3.
$$

因此, $\left\{\left(1+\frac{1}{n}\right)^{n}\right\}$ 有界,从而收敛.

利用定理3.3.3证明中得到的 $\left\{\left(1 + \frac{1}{n}\right)^n\right\}$ 严格单增以及 $\left\{\left(1 + \frac{1}{n}\right)^{n + 1}\right\}$ 严格单减,可得

$$
\left(1 + \frac {1}{n}\right) ^ {n} <   \mathrm{e} <   \left(1 + \frac {1}{n}\right) ^ {n + 1}, \qquad \forall n \geqslant 1.
$$

两端取对数得到

$$
n \ln \left(1 + \frac {1}{n}\right) <   1 <   (n + 1) \ln \left(1 + \frac {1}{n}\right), \qquad \forall n \geqslant 1.
$$

即

$$
\frac {1}{n + 1} <   \ln \left(1 + \frac {1}{n}\right) <   \frac {1}{n}, \quad \forall n \geqslant 1. \tag {3.3.6}
$$

于是又有

$$
\lim _ {n \to + \infty} n \ln \left(1 + \frac {1}{n}\right) = 1. \tag {3.3.7}
$$

另一方面, 利用定理 3.3.3 证明中的 (3.3.5) 式, 对于固定的 $m \geqslant 2$, 当 $n \geqslant m$ 时, 有

$$
1 + 1 + \frac {1}{2 !} \left(1 - \frac {1}{n}\right) + \dots + \frac {1}{m !} \prod_ {k = 1} ^ {m - 1} \left(1 - \frac {k}{n}\right) \leqslant \left(1 + \frac {1}{n}\right) ^ {n} \leqslant \sum_ {k = 0} ^ {\infty} \frac {1}{k !}.
$$

在上式中令 $n\to +\infty$ 得到

$$
\sum_ {k = 0} ^ {m} \frac {1}{k !} \leqslant \mathrm{e} \leqslant \sum_ {k = 0} ^ {\infty} \frac {1}{k !}.
$$

再在上式中令 $m\to +\infty$ 即得

$$
\mathrm{e} = \sum_ {k = 0} ^ {\infty} \frac {1}{k !}. \tag {3.3.8}
$$

而利用 (3.3.8) 式, 可得对任何正整数 $m$, 有

$$
0 <   \mathrm{e} - \sum_ {k = 0} ^ {m} \frac {1}{k !} <   \frac {1}{(m + 1) !} \sum_ {k = m + 1} ^ {\infty} \frac {1}{(m + 1) ^ {k - m - 1}} = \frac {1}{m \cdot m !}.
$$

因此，

$$
0 <   m! \Big (\mathrm{e} - \sum_ {k = 0} ^ {m} \frac {1}{k !} \Big) <   \frac {1}{m}.
$$

这表明对任何正整数 $m, m! \mathrm{e}$ 的小数部分总不等于0. 因此, $\mathrm{e}$ 是一个无理数

下例中的常数 $\gamma$ 称为 Euler 常数, $\gamma \approx 0.5772$, 但人们至今还不知道 $\gamma$ 是否为无理数.

例 3.3.4 对于  $n \geqslant 1$ , 考虑

$$
a _ {n} = 1 + \frac {1}{2} + \dots + \frac {1}{n} - \ln n, \quad b _ {n} = 1 + \frac {1}{2} + \dots + \frac {1}{n} - \ln (n + 1).
$$

证明: $\{a_{n}\}$ 和 $\{b_{n}\}$ 均收敛, 且收敛到同一极限. 该极限称为 Euler 常数, 记为 $\gamma$.

证明 对于任何 $n \geqslant 1$, 由 (3.3.6) 式, 我们有

$$
\begin{array}{l} a _ {n + 1} - a _ {n} = \frac {1}{n + 1} - \ln (n + 1) + \ln n = \frac {1}{n + 1} - \ln \left(1 + \frac {1}{n}\right) <   0, \\ b _ {n + 1} - b _ {n} = \frac {1}{n + 1} - \ln (n + 2) + \ln (n + 1) = \frac {1}{n + 1} - \ln \left(1 + \frac {1}{n + 1}\right) > 0. \\ \end{array}
$$

因此， $\{a_{n}\}$  严格单减而  $\{b_{n}\}$  严格单增。另一方面，注意到  $a_{n}>b_{n}(n\geqslant1)$ ，可得

$$
b _ {1} \leqslant b _ {n} <   a _ {n} \leqslant a _ {1}, \quad \forall n \geqslant 1.
$$

即得 $\{a_{n}\}$ 与 $\{b_n\}$ 均单调有界, 从而有极限. 结合 $a_{n+1} = \frac{1}{n+1} + b_{n} (n \geqslant 1)$, 得到它们的极限相同. □

## 3.3.3 闭区间套定理

由单调收敛定理, 或直接利用确界存在定理, 容易得到如下的 Cauchy $^{①}$ -Cantor 闭区间套定理.

定理3.3.4 设 $\{[a_n, b_n]\}$ 是一列闭区间，满足

(1) 对任何 $n \geqslant 1$, $[a_{n+1}, b_{n+1}] \subseteq [a_n, b_n]$;
(2) $\lim_{n\to +\infty}(b_n - a_n) = 0,$

则  $\{[a_{n},b_{n}]\}$  有唯一的公共点.

证明 没有特别说明时, 定理中的 $a_{n}, b_{n}$ 是实数, 且 $a_{n} < b_{n} (n \geqslant 1)$. 因此, 由条件 (1), $\{a_{n}\}$ 单调增加, 且以 $a_{1}$ 为下界, $b_{1}$ 为上界. 因此 $\{a_{n}\}$ 是单调增加的有界数列. 设它的极限 $\xi$. 则由条件 (2),

$$
\lim _ {n \to + \infty} b _ {n} = \lim _ {n \to + \infty} a _ {n} + \lim _ {n \to + \infty} (b _ {n} - a _ {n}) = \xi .
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① Cauchy, Augustin-Louis, 1789 年 8 月 21 日—1857 年 5 月 23 日, 法国数学家.</span></small>

另一方面, 任取 $m \geqslant 1$, 当 $n \geqslant m$ 时,

$$
a _ {m} \leqslant a _ {n} <   b _ {n} \leqslant b _ {m}.
$$

令 $n\to +\infty$ 得到

$$
a _ {m} \leqslant \xi \leqslant b _ {m}.
$$

即  $\xi$  是  $\{[a_{n}, b_{n}]\}$  的公共点.

另一方面, 若  $\eta$  也是  $\{[a_{n}, b_{n}]\}$  的公共点. 即对任何  $m \geqslant 1$ ,

$$
a _ {m} \leqslant \eta \leqslant b _ {m}.
$$

则由夹逼准则得到 $\eta = \xi$. 这表明 $\{[a_n, b_n]\}$ 只有唯一一个公共点 $\xi$.

![](images/page_79_image_10.jpg)

注3.3.1 定理3.3.4的结论相当于说， $\bigcap_{n = 1}^{\infty}[a_n,b_n] = \{\xi \}$ .若去掉定理的条件(2)，则可证

$$
\bigcap_ {n = 1} ^ {\infty} [ a _ {n}, b _ {n} ] = \left\{x \Big | \lim _ {n \to + \infty} a _ {n} \leqslant x \leqslant \lim _ {n \to + \infty} b _ {n} \right\}.
$$

特别地， $\bigcap_{n = 1}^{\infty}[a_n,b_n]\neq \varnothing$

但有界闭区间改为无界闭区间后,区间套的交集可能为空.例如

$$
\bigcap_ {n = 1} ^ {\infty} [ n, + \infty) = \varnothing.
$$

## 3.3.4 $\mathbb{R}$ 中的基本概念

为进一步的讨论, 我们引入 $\mathbb{R}$ 中的一些基本概念. 对于 $E \subseteq \mathbb{R}$, 用 $\mathscr{C}E$ 表示集合 $\mathbb{R} \setminus E$.

定义 3.3.1 设  $E \subseteq R$ .

(1) 若存在 $\delta > 0$ 使得 $(x_0 - \delta, x_0 + \delta) \subset E$, 则称 $x_0$ 为 $E$ 的内点. $E$ 的内点全体称为 $E$ 的内部, 记作 $E^\circ$.

若  $x_{0}$  是集合 V 的内点, 则称 V 为  $x_{0}$  的邻域.

(2) 若 $x_0$ 是 $\mathcal{C}E$ 的内点, 则称 $x_0$ 为 $E$ 的外点. 这等价于存在 $\delta > 0$ 使得 $(x_0 - \delta, x_0 + \delta) \cap E = \varnothing$. 外点全体称为外部.
(3) 若 $x_0$ 既不是 $E$ 的内点又不是 $E$ 的外点, 则称 $x_0$ 为 $E$ 的边界点. 这等价于: $\forall \delta > 0$, $(x_0 - \delta, x_0 + \delta)$ 内既有 $E$ 中的点, 又有不属于 $E$ 的点. 边界点全体称为边界, 记作 $\partial E$.