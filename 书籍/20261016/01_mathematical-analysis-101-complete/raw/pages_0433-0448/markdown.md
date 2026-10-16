对任意正整数 N > 1, 取所有不超过 N 的素数  $p_{1} = 2, p_{2} = 3, \cdots, p_{k} \leqslant N$ ，将其分别代入上述展开式并做这 k 个级数的乘积，这样可得到一个形式级数，该级数包含了所有如下形式的项: $\frac{1}{2^{n_{1}s}} \cdot \frac{1}{3^{n_{2}s}} \cdots \frac{1}{p_{k}^{n_{k}s}}$ ，其中  $n_{1}, \cdots, n_{k}$  为非负整数，且对指定的  $n_{1}, \cdots, n_{k}$ ，该形式的项只出现一次。由整数的因子分解定理，任一正整数 n < N 都存在唯一因式分解  $n = 2^{n_{1}} \cdot 3^{n_{2}} \cdots p_{k}^{n_{k}}$ 。注意到  $N \to +\infty \Leftrightarrow k \to +\infty$ ，故得

$$
0 <   \sum_ {n = 1} ^ {+ \infty} \frac {1}{n ^ {s}} - \prod_ {i = 1} ^ {k} \left(1 - \frac {1}{p _ {i} ^ {s}}\right) ^ {- 1} <   \sum_ {n > N} \frac {1}{n ^ {s}} \rightarrow 0 (N \rightarrow + \infty).
$$

例 11.5.4 (Euler 定理) 设  $\{p_{n}\}$  是由所有素数所组成的数列. 证明:无穷乘积  $\prod_{n=1}^{+\infty}\left(1-\frac{1}{p_{n}}\right)^{-1}$  和级数  $\sum_{n=1}^{+\infty}\frac{1}{p_{n}}$  均发散.

证明 取正整数 N > 1, 记所有不超过 N 的素数为  $\{p_{1}, p_{2}, \cdots, p_{k}\}$  ( $p_{1} = 2, p_{2} = 3, \cdots, p_{k} \leqslant N$ ), 则有

$$
\prod_ {i = 1} ^ {k} \left(1 - \frac {1}{p _ {i}}\right) ^ {- 1} \geqslant \sum_ {n = 1} ^ {N} \frac {1}{n},
$$

故

$$
\prod_ {n = 1} ^ {+ \infty} \left(1 - \frac {1}{p _ {n}}\right) ^ {- 1} = + \infty ,
$$

所以原无穷乘积发散. 又从上式可得

$$
\sum_ {n = 1} ^ {+ \infty} \ln \left(1 - \frac {1}{p _ {n}}\right) = - \infty ,
$$

注意到 $\ln (1 - x)\sim -x(x\to 0)$ ，可得 $\sum_{n = 1}^{+\infty}\frac{1}{p_n} = +\infty .$

注 11.5.1 (1) 由上面例子的结论, 我们可以证明素数一定有无穷多. 事实上, 假如不然, 设  $P_{N}$  是最大素数, 则对任意的 s > 1 有

$$
\frac {1}{\zeta (s)} = \prod_ {n = 1} ^ {N} \left(1 - \frac {1}{p _ {n} ^ {s}}\right).
$$

注意等式右端仅有有限项相乘, 因此, 在上式两端取 $s \to 1^{+}$ 的极限, 得

$$
\prod_ {n = 1} ^ {N} \left(1 - \frac {1}{p _ {n} ^ {s}}\right)\rightarrow \prod_ {n = 1} ^ {N} \left(1 - \frac {1}{p _ {n}}\right) > 0 \quad (s \rightarrow 1 ^ {+}).
$$

但是另一方面， $\lim_{s\to1^{+}}\frac{1}{\zeta(s)}=0,$  矛盾.

(2) 比较例 11.5.4 中的结论  $\sum_{n=1}^{+\infty}\frac{1}{p_{n}} = +\infty$  与级数  $\sum_{n=1}^{+\infty}\frac{1}{n^{2}} = \frac{\pi^{2}}{6}$ ，可以看出在所有正整数中，素数并不稀少，甚至比平方数还要“多”.

## 习题 11.5

1. (Cauchy 准则) 证明: 无穷乘积 $\prod_{n=1}^{+\infty} a_n$ 收敛当且仅当对任意的 $\varepsilon > 0$, 存在 $N > 0$, 使得对任意的 $n \geqslant N$, 任意的 $p \geqslant 0$, 都有

$$
\left| a _ {n} a _ {n + 1} \dots a _ {n + p} - 1 \right| <   \varepsilon .
$$

2. 证明下列等式:

(1) $\prod_{n=2}^{+\infty} \frac{n^3 - 1}{n^3 + 1} = \frac{2}{3}$;

(2) $\prod_{n=2}^{+\infty}\left(1 - \frac{2}{n(n+1)}\right) = \frac{1}{3};$

(3) $\prod_{n=0}^{+\infty}\left(1 + \left(\frac{1}{2}\right)^n\right) = 2.$

3. 试用 Wallis 公式证明:

(1) $\prod_{n=1}^{+\infty}\left(1 - \frac{1}{4n^2}\right) = \frac{2}{\pi};$

(2) $\prod_{n=1}^{+\infty}\left(1 - \frac{1}{(2n+1)^2}\right) = \frac{\pi}{4}.$

4. 讨论下列无穷乘积的敛散性:

(1) $\prod_{n=1}^{+\infty} \frac{1}{n}$;

(2) $\prod_{n=1}^{+\infty} \frac{(n+1)^2}{n(n+2)}$;

(3) $\prod_{n=1}^{+\infty}\sqrt{1 + \frac{1}{n}}.$

5. 讨论下列无穷乘积的敛散性:

(1) $\prod_{n=1}^{+\infty} \frac{n}{\sqrt{n^2 + 1}}$;

(2) $\prod_{n=2}^{+\infty}\left(\frac{n^2-1}{n^2+1}\right)^p$, $p$ 为任意实数;

(3) $\prod_{n=1}^{+\infty}\sqrt{\ln(n+x)-\ln n}, x \neq 0, -1, -2, \cdots.$

6. 证明: 若级数 $\sum_{n=1}^{+\infty} a_n^2 < +\infty$, 则 $\prod_{n=1}^{+\infty} \cos a_n$ 收敛.

7. 能否由  $\prod_{n=1}^{+\infty} p_{n} \prod_{n=1}^{+\infty} q_{n}$  的敛散性, 得出下列乘积的敛散性?

$$
\prod_ {n = 1} ^ {+ \infty} (p _ {n} + q _ {n}); \quad \prod_ {n = 1} ^ {+ \infty} p _ {n} q _ {n}; \quad \prod_ {n = 1} ^ {+ \infty} \frac {p _ {n}}{q _ {n}}.
$$

8. 设

$$
a _ {n} = \left\{ \begin{array}{l l} - \frac {1}{\sqrt {k}}, & n = 2 k - 1, \\ \frac {1}{k} + \frac {1}{k} + \frac {1}{k \sqrt {k}}, & n = 2 k, \end{array} \right.
$$

证明: $\sum_{n=1}^{+\infty} a_n, \sum_{n=1}^{+\infty} a_n^2$ 都发散, 但 $\prod_{n=1}^{+\infty} (1 + a_n)$ 收敛.

9. 证明:

$$
\prod_ {n = 1} ^ {+ \infty} \frac {1}{\mathrm{e}} \left(1 + \frac {1}{n}\right) ^ {n} = 0,
$$

并由此证明:

$$
\lim _ {n \to \infty} \frac {n ^ {n}}{n !} \mathrm{e} ^ {- n} = 0.
$$

10. 设 $|a_{n}| < \frac{\pi}{4}$，级数 $\sum_{n=1}^{+\infty} a_{n}$ 绝对收敛. 证明: 无穷乘积

$$
\prod_ {n = 1} ^ {+ \infty} \tan \left(\frac {\pi}{4} + a _ {n}\right)
$$

收敛.

## 第十二章

## 函数序列与函数项级数

上一章我们讨论了数项级数的敛散性及其在收敛时级数的基本性质, 本章我们将重点研究函数项级数, 即通项均为函数的无穷求和问题. 显然, 在函数项级数通项中, 如果固定自变量, 那么函数项级数即为常数项级数. 此时判别常数项级数敛散性的所有方法都可以用于函数项级数的敛散判别. 这种固定一点然后考虑函数项级数收敛的情形称之为函数项级数的 “点态” 收敛. 在上一章学习了数项级数敛散性之后, 函数项级数的重点将不再是点态收敛问题, 而更侧重于每一项作为一个函数来看它们的 “整体” 收敛问题. 换句话说, 点态收敛是进一步研究函数项级数性质的入门级假设: 只有在点态收敛假设下, 函数项级数才能定义出一个和函数, 而我们更感兴趣的则是和函数能否继承通项中逐个函数的性质.

作为本章的主要内容之一, 我们将系统回答函数项级数求和时的 “三观问题”: 我们知道在有限个函数求和时, 逐个函数的连续性、可微性和可积性都能传承到和函数上. 一个自然的问题是对无穷多个函数求和时, 这三个基本性质是否还能得以传承? 我们给出了一个高度概括的充分条件: 粗略说来就是, 对于一致收敛的级数, 初等数学中有限个函数求和时的三观传承性可以推广到无穷多个函数求和时的情形 $^{①}$ .

本章的研究对象主要有两种表现形式:函数序列（简称函数列）和函数项级数，因为它们之间存在众多的结构相似和内容平行之特点，所以在技术细节处理上，一般来说，我们只详细讨论一种情况，另一种情况“同理可证”了.

## 12.1 函数列与函数项级数的基本问题

## 12.1.1 逐点收敛与一致收敛

本章的重点研究对象是函数列的极限函数和函数项级数的和函数. 前者是说各项都是 $x$ 的函数组成的函数列

$$
f _ {1} (x), f _ {2} (x), \dots , f _ {n} (x), \dots \tag {12.1.1}
$$

后者是说以 $x$ 的函数为通项构成的函数项级数

$$
\sum_ {n = 1} ^ {+ \infty} u _ {n} (x). \tag {12.1.2}
$$

这里, 我们默认式中涉及的所有函数具有共同的定义域. 为此, 我们假设函数列中的所有函数 $f_{n}(x)$, 或者函数项级数中的所有函数 $u_{n}(x)$, 均在集合 $I$ 上有定义. 称使得函数列 (12.1.1) 或函数项级数 (12.1.2) 收敛的 $x$ 的全体为函数列 (12.1.1) 或函数项级数 (12.1.2) 的收敛域. 在收敛域内, 函数列收敛于极限函数, 函数项级数收敛于和函数.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 可微性的继承需要把“一致收敛”的充分性条件加在导函数为通项的函数项级数上.</span></small>

从前面数项级数章节我们知道, 对级数  $\sum_{n=1}^{+\infty}a_{n}$  的研究和对数列  $\{S_{n}\}$  的研究本质上是相同的. 因为两者可以相互转换: 由级数可诱导出相应的部分和数列  $\{S_{n}\}$ , 而由后者  $\{S_{n}\}$  可以构造相应的数项级数  $\sum_{n=1}^{+\infty}(S_{n}-S_{n-1})$ . 完全类似, 函数列与函数项级数之间也存在着上述转换关系. 基于此, 我们在本章的讨论中, 将以函数列为重点, 阐明基本思想、介绍典型手法、陈述主要结论, 然后将其主体结构复述到相应的函数项级数中, 而省略了某些细节证明. $^{①}$

定义 12.1.1 定义在集合 I 上的函数列  $f_{1}(x), f_{2}(x), \cdots, f_{n}(x), \cdots$ ，如果  $x_{0} \in I$ ，数列  $\{f_{n}(x_{0})\}$  极限存在（且为有限），则称  $x_{0}$  为该函数列的收敛点.

使得函数列收敛的点的全体  $E \subseteq I$  称为该函数列的收敛域.

可以完全平行地给出函数项级数的收敛点和收敛域.

例 12.1.1 不难验证下列结论:

级数  $\sum_{n=1}^{+\infty}\frac{x^{n}}{n!}$  的收敛域为 R.

级数  $\sum_{n=1}^{+\infty}e^{nx}$  的收敛域为  $(-\infty,0)$ .

函数列  $\{x^{n}\}$  的收敛域为  $(-1,1]$ .

级数  $\sum_{n=1}^{+\infty} n! x^{n}$  的收敛域为  $\{0\}$ .

级数  $\sum_{n=1}^{+\infty}e^{nx^{2}}$  的收敛域为空集  $\varnothing$ .

当然, 并非每个函数列或函数项级数的收敛域都能给出, 比如函数列 $\{n\sin (n!\pi x)\}$ 的收敛域就很难给出一个完整的刻画. 读者可以尝试一下, 该函数列的收敛域既包含 $\mathbb{R}$ 中的稠密子集 $\mathbb{Q}$, 也包含形如 $r + 2ke(r \in \mathbb{Q}, k \in \mathbb{Z})$ 的点, 但却不包含形如 $r + (2k + 1)e$ 或形如 $\frac{e}{2}$ 的点, 至于是否包含诸如 $\sqrt{2}, \sqrt{3}, \pi, \cdots$ 的点, 则需要进一步单独讨论.

显然, 对收敛域 $E$ 中的每一点 $x_0$, 函数列 (函数项级数) 的收敛性和数列 (常数项级数) 的收敛性没有区别. 记此数列在点 $x_0$ 处的极限为 $f(x_0)$, 以示与 $x_0$ 的关系. 那么可以看出, 在收敛域 $E$ 上, 存在函数 $f(x)$ 使得 $\forall x \in E, f_n(x) \to f(x)(n \to +\infty)$. 函数 $f(x)$ 称为给定函数列的极限函数.

上述对收敛域 $E$ 上每一指定点收敛的方式通常称为函数列的逐点收敛（又称点点收敛或点态收敛). 逐点收敛是得以讨论极限函数的基本假设.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① 偶尔我们也会倒过来讨论:详细研究函数项级数，“同理可证”函数列.</span></small>

例 12.1.2 函数列  $\{f_{n}(x)\}$ ,  $f_{n}(x)=x^{n}$ ，在其收敛域的子集区间 [0,1] 上逐点收敛到极限函数

$$
f (x) = \left\{ \begin{array}{l l} 0, & 0 \leqslant x <   1, \\ 1, & x = 1. \end{array} \right.
$$

注意, 函数列中的每一项均为连续函数, 但极限函数有间断点, 即

$$
\lim _ {x \to x _ {0}} \lim _ {n \to + \infty} f _ {n} (x) \neq \lim _ {n \to + \infty} \lim _ {x \to x _ {0}} f _ {n} (x). \tag {12.1.3}
$$

例 12.1.3 函数列  $\{f_{n}(x)\}$ ,  $f_{n}(x)=\frac{x^{n+1}}{n+1}\ (n=1,2,\cdots)$ ，在 [0,1] 上逐点收敛到极限函数  $f(x)\equiv0$ 。可以看出，其相应的导函数列  $\{f_{n}^{\prime}(x)\}$ ,  $f_{n}^{\prime}(x)=x^{n}$ ，虽然逐点收敛到极限函数

$$
g (x) = \left\{ \begin{array}{l l} 0, & 0 \leqslant x <   1, \\ 1, & x = 1, \end{array} \right.
$$

但此极限函数在 $x = 1$ 处并不可导 (单侧导数), 当然也谈不上等于极限函数 $f(x)$ 的导函数 $f'(x)$ 了, 即

$$
\lim _ {n \to + \infty} \frac {\mathrm{d}}{\mathrm{d} x} f _ {n} (x) \neq \frac {\mathrm{d}}{\mathrm{d} x} \Big (\lim _ {n \to + \infty} f _ {n} (x) \Big) = 0, \tag {12.1.4}
$$

这里左端项在 x = 1 处没有定义.

例12.1.4 函数列 $\{f_n(x)\}$, $f_n(x) = nx(1 - x^2)^n$, 在 $[0,1]$ 上逐点收敛到极限函数 $f(x) \equiv 0$. 考察 $f_n(x)$ 的积分

$$
\int_ {0} ^ {1} f _ {n} (x) \mathrm{d} x = \frac {n}{2 (n + 1)} \rightarrow \frac {1}{2} \quad (n \rightarrow + \infty).
$$

注意到极限函数 $f(x)$ 的积分 $\int_0^1 f(x)\mathrm{d}x = 0,$ 即

$$
\int_ {0} ^ {1} \lim _ {n \to + \infty} f _ {n} (x) \mathrm{d} x \neq \lim _ {n \to + \infty} \int_ {0} ^ {1} f _ {n} (x) \mathrm{d} x. \tag {12.1.5}
$$

从这些例子可以看出, 虽然给定的函数列都逐点收敛, 但函数列中每个函数具有的若干重要的分析性质并不能传递给极限函数. 而到底能否把每个函数的性质传递给极限函数, 我们是通过把极限函数计算出来再加以验证的. 这种做法虽然具有其本质性, 但显然也给我们带来极大的不便, 因为一般来说求出极限函数可能并不比证明其存在性容易.

如何不必求出极限函数的具体表达而又能保证重要的分析性质得以传承到极限函数, 是分析中的一个基本问题. 进一步的分析发现, 函数列的点态收敛有点太弱, 不足以保证性质的传承. 这是因为对于不同的收敛点, 由于收敛速度可能有快有慢, 收敛的步调不一致, 从而导致某些点 “掉队” 了. 为了克服这个问题, 我们引入下面的一致收敛概念.

定义12.1.2 设 $E \subseteq \mathbb{R}$. 称函数列 $\{f_n\}$ 在 $E$ 上一致收敛到 $f$, 是指对任何 $\varepsilon > 0$, 存在 $N \geqslant 1$, 使得当 $n \geqslant N$ 时, 对任何 $x \in E$ 成立 $\left|f_n(x) - f(x)\right| < \varepsilon$. 记为 $f_n(x) \Rightarrow f(x) (n \to +\infty)(x \in E)$. 也简称为 $\{f_n(x)\}$ 关于 $x \in E$ 一致收敛.

完全类似, 我们称函数项级数 $\sum_{n=1}^{+\infty} u_n(x)$ 在 $E$ 上一致收敛到函数 $S(x)$, 是指它的部分和组成的函数列 $\{S_n(x)\}$ 在 $E$ 上一致收敛到 $S(x)$, 记为 $\sum_{n=1}^{+\infty} u_n(x) \Rightarrow S(x) (x \in E)$.

显然, 一致收敛蕴涵着逐点收敛, 并且一致收敛的极限函数等同于点态收敛的极限函数. 一致性强调的是定义中的 $N$ 仅与 $\varepsilon$ 有关, 与 $x$ 在 $E$ 中的位置无关.

我们只对集合 $E$ 为无限集的情形感兴趣, 因为有限集的情形是平凡的.

容易看出, 函数列 $\{f_n\}$ 在 $E$ 上一致收敛到 $f$ 当且仅当

$$
\lim _ {n \to + \infty} \sup _ {x \in E} \left| f _ {n} (x) - f (x) \right| = 0,
$$

即

$$
\varlimsup_ {n \to + \infty} \sup _ {x \in E} \left| f _ {n} (x) - f (x) \right| = 0.
$$

所以下面的 Cauchy 准则成立.

定理 12.1.1 (Cauchy 准则) 函数列  $\{f_{n}\}$  在 E 上一致收敛当且仅当对任何  $\varepsilon > 0$ ，存在  $N \geqslant 1$ ，使得当  $m, n \geqslant N$  时，对任何  $x \in E$  成立  $\left|f_{m}(x) - f_{n}(x)\right| < \varepsilon$ 。即

$$
\lim _ {m, n \to + \infty} \sup _ {x \in E} \left| f _ {m} (x) - f _ {n} (x) \right| = 0,
$$

即

$$
\varlimsup_ {m, n \to + \infty} \sup _ {x \in E} \left| f _ {m} (x) - f _ {n} (x) \right| = 0.
$$

函数项级数一致收敛的 Cauchy 准则, 只需将定理中的函数列  $\{f_{n}\}$  改为函数项级数的部分和序列  $\{S_{n}(x)\}$  即可.

Cauchy 准则的最大特点之一是无须知道极限函数的具体表述, 它的优点在于保证了极限函数的存在性. 当然, 也可以理解为该准则的一个缺憾: 不能给出极限函数的描述.

例12.1.5 证明:函数列 $\{f_n(x)\}$, $f_n(x) = \frac{D(x)}{n}$, $D(x)$ 是Dirichlet函数, 在 $\mathbb{R}$ 上一致收敛到极限函数 $f(x) = 0$.

证明 事实上, 我们可以利用下面的不等式证明函数列的一致收敛性而不必考虑极限函数 $f$ 的具体形式. 对于任意的 $n > m \geqslant 1$,

$$
| f _ {n} (x) - f _ {m} (x) | \leqslant \frac {1}{m}.
$$

例 12.1.6 试研究例 12.1.2 中的函数列  $\{x^{n}\}$  在 [0,1] 上的一致收敛性.

解 我们知道该函数列的极限函数为

$$
f (x) = \left\{ \begin{array}{l l} 0, & x \in [ 0, 1), \\ 1, & x = 1. \end{array} \right.
$$

而当 $n\to +\infty$ 时，

$$
\sup _ {x \in [ 0, 1 ]} \left| x ^ {n} - f (x) \right| = \sup _ {x \in [ 0, 1)} | x ^ {n} | = 1 \not \to 0.
$$

因此, 函数列非一致收敛.

例 12.1.7 试讨论例 12.1.4 中的函数列  $\{nx(1-x^{2})^{n}\}$  的一致收敛性.

解 注意到

$$
\sup _ {x \in [ 0, 1 ]} \left| n x (1 - x ^ {2}) ^ {n} \right| \geqslant \frac {n}{\sqrt {2 n + 1}} \frac {(2 n) ^ {n}}{(2 n + 1) ^ {n}} \rightarrow + \infty \neq 0 \quad (n \rightarrow + \infty),
$$

故所给函数列在 $[0,1]$ 上非一致收敛.

我们对上面例子中的函数列 $\{x^n\}$ 做一些更细致的分析. 可以看出, $\forall \varepsilon > 0$, 对于每个固定的点 $x_0 \in E$, 都可以找到一个 $N = N(x_0)$, 使得当 $n > N$ 时, 有 $|f_n(x_0) - f(x_0)| = x_0^n < \varepsilon$. 但是, 对于不同的 $x_0$, 使得 $x_0^n < \varepsilon$ 成立的最小的 $N$ 可能有很大的区别. 比如, 令 $\varepsilon = \frac{1}{10^{100}}$, 则在 $x_0 = \frac{1}{10^{10}}$ 处, 只要取 $N_0 = 10$ 即可; 在 $x_1 = \frac{1}{10^5}$ 处, 可以取 $N_1 = 20$; 而在 $x_2 = \frac{1}{10}$ 处, 则需要取 $N_2 = 100$. 换句话说, 对任意的 $\varepsilon, 0 < \varepsilon < 1$, 以及对任意给定的 $N$, 都可以找到 $\tilde{x} \in [0,1)$, 使得 $\tilde{x}^N > \varepsilon$, 比如, 这只要取 $\tilde{x} = ^2\sqrt[N]{\varepsilon}$ 即可. 又如, 在函数列 $\{x^n\}$ 中, 对于函数 $x^n$, 对应取点列 $\left\{1 - \frac{1}{n}\right\}$, 则 $f_n\left(1 - \frac{1}{n}\right) \to \frac{1}{\mathrm{e}} (n \to +\infty)$; 如果取点列 $\left\{1 - \frac{1}{n^2}\right\}$, 则 $f_n\left(1 - \frac{1}{n^2}\right) \to 1 (n \to +\infty)$. 在函数列 $\{nx(1 - x^2)^n\}$ 中取点列 $\left\{\frac{1}{\sqrt{2n+1}}\right\}$, 则 $f_n(x_n) \to +\infty (n \to +\infty)$.

这种在不同点, 虽然收敛, 但收敛的速度呈现参差不齐以至于最终导致极限函数的性质呈现 “断崖式” 改变的现象, 恰好是由于不一致收敛造成的. 换言之, 如果不一致收敛, 则难以保证关系式 (12.1.3), (12.1.4) 和 (12.1.5) 中的等号成立.

下面我们再讨论几个关于一致收敛的例子. 注意, 为了考察其一致收敛性, 代之以计算定理 12.1.1 的上确界, 往往给出上确界的估计会更方便些, 但这通常需要对是否一致收敛有个预判, 从而来确定不等式估计是放大还是缩小.

例12.1.8 考察函数列 $\{x(1 - x)^n\}$, $\{nx(1 - x)^n\}$, $\left\{nx(1 - x)^{n^2}\right\}$ 在[0,1]区间上的一致收敛性.

解 容易证明, 这三个函数列的极限函数均为零函数. 注意到当 $n \to +\infty$ 时, 有

$$
\sup _ {x \in [ 0, 1 ]} \left| x (1 - x) ^ {n} \right| \leqslant \frac {1}{n + 1} \Big (1 - \frac {1}{n + 1} \Big) ^ {n} \to 0,
$$

$$
\sup _ {x \in [ 0, 1 ]} \left| n x (1 - x) ^ {n} \right| \geqslant \left(1 - \frac {1}{n}\right) ^ {n} \rightarrow \mathrm{e} ^ {- 1} \neq 0,
$$

$$
\sup _ {x \in [ 0, 1 ]} \left| n x (1 - x) ^ {n ^ {2}} \right| \leqslant \frac {n}{1 + n ^ {2}} \rightarrow 0.
$$

因此, $\{x(1 - x)^n\}$ 和 $\left\{nx(1 - x)^{n^2}\right\}$ 在[0,1]上一致收敛, 而 $\{nx(1 - x)^n\}$ 在[0,1]上非一致收敛. □

例 12.1.9 分别考察函数项级数  $\sum_{n=1}^{+\infty} n(1-x)x^{n^{2}}$  和  $\sum_{n=1}^{+\infty} n(1-x)x^{n^{3}}$  在 [0,1) 上的一致收敛性.

解 记 $u_{n}(x) = n(1 - x)x^{n^{2}}$，则易知当 $x = \frac{n^2}{1 + n^2}$ 时 $u_{n}(x)$ 在 $[0,1)$ 上取最大值.

$$
\sup _ {x \in [ 0, 1)} \left| u _ {n} (x) \right| \geqslant \frac {n}{n ^ {2} + 1} \left(\frac {n ^ {2}}{n ^ {2} + 1}\right) ^ {n ^ {2}} = \frac {1}{n} \cdot \left(1 - \frac {1}{n ^ {2} + 1}\right) ^ {n ^ {2} + 1} \sim \frac {1}{n \mathrm{e}} \quad (n \rightarrow + \infty).
$$

因此, $\sum_{n=1}^{+\infty}n(1-x)x^{n^{2}}$  在 [0,1) 上非一致收敛.

完全类似, 记  $v_{n}(x)=n(1-x)x^{n^{3}}$ , 有相应的估计

$$
\sup _ {x \in [ 0, 1)} | v _ {n} (x) | \leqslant \frac {n}{n ^ {3} + 1} \left(\frac {n ^ {3}}{n ^ {3} + 1}\right) ^ {n ^ {3}} = \frac {1}{n ^ {2}} \cdot \left(1 - \frac {1}{n ^ {3} + 1}\right) ^ {n ^ {3} + 1} = O \left(\frac {1}{n ^ {2}}\right) \quad (n \rightarrow + \infty).
$$

因此, $\sum_{n=1}^{+\infty}n(1-x)x^{n^{3}}$ 在[0,1)上一致收敛.

例 12.1.10 设  $\{f_{n}\}$  在 [0,1] 上点态收敛,  $f_{n}$  可微, 且  $|f_{n}^{\prime}| \leqslant M < +\infty$ . 试证:  $\{f_{n}\}$  在 [0,1] 上一致收敛.

证明 对于 $m, n \geqslant 1$, 任取 $k \geqslant 2$, 令 $x_{j} = \frac{j}{k}$, 则对任何 $j$,

$$
\begin{array}{l} \left| f _ {m} (x) - f _ {n} (x) \right| \leqslant \left| f _ {m} (x) - f _ {m} \left(x _ {j}\right) \right| + \left| f _ {n} \left(x _ {j}\right) - f _ {n} (x) \right| + \left| f _ {m} \left(x _ {j}\right) - f _ {n} \left(x _ {j}\right) \right| \\ \leqslant 2 M \left| x - x _ {j} \right| + \sum_ {i = 0} ^ {k} \left| f _ {m} (x _ {i}) - f _ {n} (x _ {i}) \right|. \\ \end{array}
$$

从而, 取 j 使得  $\left|x-x_{j}\right|\leqslant\frac{1}{k}$  可得

$$
\sup _ {x \in [ 0, 1 ]} | f _ {m} (x) - f _ {n} (x) | \leqslant \frac {2 M}{k} + \sum_ {i = 0} ^ {k} \left| f _ {m} (x _ {i}) - f _ {n} (x _ {i}) \right|.
$$

因此，

$$
\varlimsup_{\substack{m\to +\infty \\ n\to +\infty}}\sup_{x\in [0,1]}|f_{m}(x) - f_{n}(x)|\leqslant \frac{2M}{k}.
$$

令 $k\to +\infty$ 得到

$$
\varlimsup_{\substack{m\to +\infty \\ n\to +\infty}}\sup_{x\in [0,1]}|f_{m}(x) - f_{n}(x)|\leqslant 0.
$$

即得  $\{f_{n}\}$  在  $[0,1]$  上一致收敛.

从上述例子的证明过程不难看出下面的结论成立:设  $\{f_{n}\}$  在闭区间  $[a,b]$  上逐点收敛， $f_{n}(n=1,2,\cdots)$  均 Lipschitz 连续，且有一致的 Lipschitz 常数，则  $\{f_{n}\}$  在  $[a,b]$  上一致收敛.

由于函数的很多基本性质比如连续可微等都是局部性的, 我们再通过一个例子来引出一个基本概念.

例12.1.11 试研究函数列 $\left\{\frac{1}{nx}\right\}$ 在 $(0, +\infty)$ 内的一致收敛性.

解 $\forall x_0 \in (0, +\infty)$，该函数列的极限均为零，所以极限函数为零函数。但因为当 $n \to +\infty$ 时，

$$
\sup _ {x \in (0, + \infty)} \left| \frac {1}{n x} \right| = + \infty \not \to 0,
$$

所以函数列在 $(0, +\infty)$ 内不是一致收敛的.

另一方面, 对任何 $[a, b] \subseteq (0, +\infty)$, 显然当 $n \to +\infty$ 时,

$$
\sup _ {x \in E} \left| \frac {1}{n x} \right| \leqslant \sup _ {x \in [ a, b ]} \left| \frac {1}{n x} \right| = \frac {1}{n a} \rightarrow 0.
$$

因此, 函数列 $\left\{\frac{1}{nx}\right\}$ 在任何 $[a, b] \subseteq (0, +\infty)$ 上一致收敛. 一般来说, 当函数列在所考虑集合的紧子集上一致收敛时, 我们称之为内闭一致收敛. 本例是说 $\left\{\frac{1}{nx}\right\}$ 在 $(0, +\infty)$ 中内闭一致收敛.

定义 12.1.3 设函数列  $\{f_{n}(x)\}$  或函数项级数  $\sum_{n=1}^{+\infty} u_{n}(x)$  在区间 I 上有定义, 若对任何闭区间  $[a, b] \subseteq I$ ,  $\{f_{n}(x)\}$  或  $\sum_{n=1}^{+\infty} u_{n}(x)$  在  $[a, b]$  上一致收敛, 则称该函数列或函数项级数在 I 上内闭一致收敛.

如果函数列 $\{f_n(x)\}$ 或函数项级数 $\sum_{n=1}^{+\infty} u_n(x)$ 在 $x_0$ 的一个邻域内一致收敛, 则称其为局部一致收敛.

定义 12.1.3 中的区间 I 通常是开区间或半开半闭区间, 因为对闭区间而言, 内闭的定义是平凡的.

“内闭”是分析中处理开集上定义的研究对象时常用的手法, 通过此区间上的 “内闭” 子集上的性质来分析整个集合上的性质. 比如内闭有界、内闭一致收敛, 等等.

不难证明, 对于开区间 $I$ 而言, 内闭一致收敛等价于局部一致收敛. 但内闭一致收敛并不等价于开区间上的一致收敛, 比如 $\{x^n\}$ 在 $(0,1)$ 上是内闭一致收敛的, 但并非一致收敛; 又如函数 $f(x) = \frac{1}{x}$ 在 $(0,1)$ 上内闭有界, 但它并非有界.

朴素说来, 函数列 $\{f_n(x)\}$ 内闭一致收敛到 $f(x)$, 是对任意给定的闭区间, $\forall \varepsilon > 0$, 存在 $N$, 当 $n > N$ 时, $|f_n(x) - f(x)| \leqslant \varepsilon$, 这里的 $N$ 与 $x$ 在闭区间里的位置无关, 但通常与所选的闭区间有关. 比如考察 $\{x^n\}$ 在 $(0,1)$ 上的收敛情况, 一旦 $\delta_1, \delta_2$ 选定, 则在 $[\delta_1, 1 - \delta_2] \subseteq (0,1)$ 内函数列一致收敛, 但比如当 $\delta_1, \delta_2$ 越来越小时, 对应的 $N$ 可能就越来越大, 以至于在 $(0,1)$ 上时, 对于给定的 $\varepsilon > 0$, 无论 $N$ 选得多么大, 都不可能适合所有的闭区间.

## 12.1.2 极限函数的基本问题

本章我们关心的中心问题是:如果函数列中每个函数都具有性质 $P$，且函数列收敛，那么它们的极限函数是否也具有性质 $P$？其中性质 $P$ 主要包括:连续性、可微性以及可积性。如果极限函数仍然具有性质 $P$，我们称该函数列对性质 $P$ 具有传承性，简称性质 $P$ 具有传承性。具体说来，本章我们主要讨论下面三个方面的问题:

(1) 连续性: 如果函数列 $\{f_n\}$ 中的每个函数 $f_n(x)$ 均在 $x_0$ 处连续, 其极限函数 $f$ 是否也在 $x_0$ 也连续? 即是否有 $\lim_{x \to x_0} f(x) = f(x_0)$. 这相当于是否成立

$$
\lim _ {x \to x _ {0}} \lim _ {n \to + \infty} f _ {n} (x) = \lim _ {n \to + \infty} \lim _ {x \to x _ {0}} f _ {n} (x)?
$$

(2) 可微性: 如果函数列 $\{f_n\}$ 中的每个函数均可导, 其极限函数 $f$ 是否也可导, 且

$$
\frac {\mathrm{d}}{\mathrm{d} x} \Big (\lim _ {n \to + \infty} f _ {n} (x) \Big) = \lim _ {n \to + \infty} \frac {\mathrm{d}}{\mathrm{d} x} f _ {n} (x)?
$$

(3) 可积性: 如果函数列  $\{f_{n}\}$  中的每个函数均在  $[a, b]$  上可积, 其极限函数 f 是否也可积, 且成立

$$
\int_ {a} ^ {b} \lim _ {n \to + \infty} f _ {n} (x) \mathrm{d} x = \lim _ {n \to + \infty} \int_ {a} ^ {b} f _ {n} (x) \mathrm{d} x?
$$

## 习题12.1

1. 考虑下列级数,试找出尽可能多的使级数收敛的点:

(1) $\sum_{n=1}^{+\infty}\sin(n!x)$;

(2) $\sum_{n=1}^{+\infty} (\sin(n!x) - \sin((n-1)!x))$.

2. 求下列函数项级数的收敛点集:

(1) $\sum_{n=1}^{+\infty} \frac{n-1}{n+1} \left( \frac{x}{3x+1} \right)^n$;

(2) $\sum_{n=1}^{+\infty} n\mathrm{e}^{-nx}$;

(3) $\sum_{n=1}^{+\infty}\left(\frac{x(x+n)}{n}\right)^n$;

(4) $\sum_{n=1}^{+\infty} \frac{x^n}{1 + x^{2n}}$;

(5) $\sum_{n=1}^{+\infty} \frac{n + x}{n^{n + x}}$;

(6) $\sum_{n=1}^{+\infty} \frac{a^n x^n}{a^n + x^n}, a > 0;$

(7) $\sum_{n=1}^{+\infty} \frac{\ln(1 + x^n)}{n^n}, x > 0;$

(8) $\sum_{n=1}^{+\infty} (\sqrt[n]{n}-1)^{x}, x > 0.$

3. 设函数项级数  $\sum_{n=1}^{+\infty} u_{n}(x)$  在有界区间  $[a, b]$  上收敛于  $S(x)$ ，如果  $u_{n}(x)$  ( $n = 1, 2, \cdots$ ) 都是  $[a, b]$  上的非负连续函数，证明: $S(x)$  必在  $[a, b]$  上取到最小值。进一步问: $S(x)$  是否一定能取到最大值？

4. 把上题中的有界闭区间  $[a, b]$  换成开区间  $(a, b)$  或无穷区间, 结论是否成立?

5. 在区间 $[0,1]$ 上递归地定义函数列 $\{f_n\}$ 如下:

$$
f _ {1} (x) \equiv 1, \quad f _ {n + 1} (x) = \sqrt {x f _ {n} (x)}, \quad n \geqslant 1.
$$

证明: $\{f_{n}\}$  一致收敛到 [0,1] 上的一个连续函数.

6. 设 $a > 0, f_{1}(x)$ 为 $[0, a]$ 上的可积函数, 递归地定义函数列 $\{f_{n}\}$ 如下:

$$
f _ {n + 1} (x) = \int_ {0} ^ {x} f _ {n} (t)   \mathrm{d} t, \quad n \geqslant 1.
$$

证明: $\{f_n\}$ 一致收敛到0.

7. 设  $\{f_{n}(x)\}$  在 I 中一致收敛到  $f(x)$ . 如果对  $n=1,2,\cdots,f_{n}(x)$  均在 I 中一致连续, 证明:  $f(x)$  也在 I 中一致连续.

8. (1) 设 $\{f_n(x)\}$ 在 $I$ 中一致收敛到 $f(x)$. 如果 $g(x)$ 是 $I$ 中的有界函数, 证明: $\{f_n(x)g(x)\}$ 在 $I$ 中一致收敛到 $f(x)g(x)$.

(2) 问是否存在满足如下条件的例子: $\{f_{n}(x)\}$  在某区间 I 中收敛但不一致收敛， $g(x)$  是 I 中非零的有界函数， $\{f_{n}(x)g(x)\}$  在 I 中一致收敛到  $f(x)g(x)$ ?

9. 设 $f_{n}(x)$ 为 $[a, b]$ 中的连续函数列. 如果 $\{f_{n}(x)\}$ 一致收敛到正函数 $f(x)$, 证明: 存在 $N$, 当 $n > N$ 时 $f_{n}(x)$ 也是正函数, 且 $\left\{\frac{1}{f_{n}(x)}\right\}$ 一致收敛到 $\frac{1}{f(x)}$. 如果把闭区间 $[a, b]$ 换成开区间 $(a, b)$, 结论还成立吗?

10. 设  $\{f_{n}(x)\},\{g_{n}(x)\}$  和  $\{h_{n}(x)\}$  是定义在 I 中的函数, 且

$$
f _ {n} (x) \leqslant g _ {n} (x) \leqslant h _ {n} (x), \quad x \in I.
$$

如果 $\{f_n(x)\}$ 和 $\{h_n(x)\}$ 一致收敛到 $f(x)$, 证明: $\{g_n(x)\}$ 也一致收敛到 $f(x)$.

## 12.2 一致收敛的判别法则

本节我们给出函数序列一致收敛的几个常用的判别法则. 除了前面讨论过的可以利用定义以及 Cauchy 准则定理 12.1.1 外, 下面几个定理也是非常基本和重要的. 这些法则与上一章数项级数中的法则, 在表述上有高度的相似性, 比如 Weierstrass 判别法可以与正项级数的比较定理类比, Abel 判别法和 Dirichlet 判别法与数项级数的情形也完全类似.

利用 Cauchy 准则易得如下的 Weierstrass 判别法, 又称 M-判别法或优势级数判别法, 证明省略.

## 定理 12.2.1 (Weierstrass 判别法, M-判别法)

设 $E \subseteq \mathbb{R}, \forall x \in E, |u_n(x)| \leqslant$

$M_{n}$, 而数项级数 $\sum_{n=1}^{+\infty} M_{n}$ 收敛, 则 $\sum_{n=1}^{+\infty} u_{n}(x)$ 关于 $x \in E$ 一致收敛.

上述定理可以推广到如下情形.

## 定理12.2.2

设 $E \subseteq \mathbb{R}, \forall x \in E, |u_n(x)| \leqslant M_n(x)$, 而函数项级数 $\sum_{n=1}M_n(x)$ 关

于 $x \in E$ 一致收敛, 则 $\sum_{n=1}^{+\infty} u_n(x)$ 亦然.

例 12.2.1 设级数  $\sum_{n=1}^{+\infty}a_{n}$  绝对收敛, 则函数项级数  $\sum_{n=1}^{+\infty}a_{n}\sin nx$  和  $\sum_{n=1}^{+\infty}a_{n}\cos nx$  在任何集合  $E \subseteq R$  上均一致收敛.

注 12.2.1 Weierstrass 判别法给出的结论是函数项级数的绝对一致收敛, 绝对一致收敛的内涵可以字面理解, 它是一个比一致收敛还要强的收敛. 因此, 如果讨论条件收敛级数的一致收敛性, 则通常需要下面更精细的判别法.

利用 Abel 变换, 采用完全类似于 (11.3.2) 的不等式估计模式, 容易得到下面的关于一致收敛性的 Abel 判别法和 Dirichlet 判别法, 证略.

## 定理 12.2.3 (Abel 判别法)

设函数项级数  $\sum_{n=1}^{+\infty}u_{n}(x)$  在  $E\subseteq R$  上一致收敛,

函数列 $\{v_{n}(x)\}$ 对于每个取定的 $x\in E$ 关于 $n$ 单调且在 $E$ 上一致有界，则函数项级数 $\sum_{n = 1}^{+\infty}u_n(x)v_n(x)$ 在 $E$ 上一致收敛.

## 定理 12.2.4 (Dirichlet 判别法)

设函数项级数 $\sum_{n=1}^{+\infty} u_n(x)$ 的部分和

$$
U _ {n} (x) = \sum_ {k = 1} ^ {n} u _ {k} (x)
$$

组成的函数列 $\{U_n(x)\}$ 在 $E \subseteq \mathbb{R}$ 上一致有界, 函数列 $\{v_n(x)\}$ 对于每个取定的 $x \in E$ 关于 $n$ 单调且在 $E$ 上一致收敛到 0 , 则函数项级数 $\sum_{n=1}^{+\infty} u_n(x) v_n(x)$ 在 $E$ 上一致收敛.

例 12.2.2 证明: 级数 $\sum_{n=1}^{+\infty} \frac{\cos nx}{n}$ 和 $\sum_{n=1}^{+\infty} \frac{\sin nx}{n}$ 在 $(0, 2\pi)$ 内闭一致收敛, 即 $\forall \delta, 0 < \delta < \pi$, 级数在 $[\delta, 2\pi - \delta]$ 上一致收敛, 但级数在 $(0, 2\pi)$ 内并非一致收敛.

证明 令 $a_{n}(x) = \cos nx, b_{n}(x) = \frac{1}{n}$, 则 $b_{n}(x)$ 单调递减趋于0，而且

$$
\left| \sum_ {k = 1} ^ {n} \cos k x \right| \leqslant \frac {1}{\sin \frac {x}{2}}.
$$

因为 $x \in [\delta, 2\pi - \delta]$, 所以 $\sin \frac{x}{2} \geqslant \sin \frac{\delta}{2}$, 因而有

$$
\left| \sum_ {k = 1} ^ {n} \cos k x \right| \leqslant \frac {1}{\sin \frac {\delta}{2}}.
$$

即 $\sum_{k=1}^{n} \cos kx$ 在 $[\delta, 2\pi - \delta]$ 上一致有界. 根据 Dirichlet 判别法知原级数在 $[\delta, 2\pi - \delta]$ 上一致收敛. 同理, 级数 $\sum_{n=1}^{+\infty} \frac{\sin nx}{n}$ 在 $[\delta, 2\pi - \delta]$ 上也一致收敛.

为了证明  $\sum_{n=1}^{+\infty}\frac{\sin nx}{n}$  在  $(0,2\pi)$  内不一致收敛, 取  $x_{m}=\frac{\pi}{4m}$ , 则

$$
| S _ {2 m} - S _ {m} | = \left| \frac {\sin \frac {(m + 1) \pi}{4 m}}{m + 1} + \dots + \frac {\sin \frac {\pi}{2}}{2 m} \right| \geqslant m \cdot \frac {\sin \frac {\pi}{4}}{2 m} = \frac {1}{2 \sqrt {2}}.
$$

由 Cauchy 准则知此收敛是逐点收敛但不是一致收敛. 级数 $\sum_{n=1}^{+\infty} \frac{\cos nx}{n}$ 的情形可类似证明.

另外, 不难证明, 这两个级数在 $(0, \pi)$ 上都不是绝对收敛的, 这说明一致收敛的级数未必绝对收敛. 当然, 从例12.1.9可知绝对收敛也不等同于一致收敛. □

类似于定理 11.3.6, 我们也可以将 Abel 判别法与 Dirichlet 判别法推广为如下定理.

定理 12.2.5 设函数项级数  $\sum_{n=1}^{+\infty} u_{n}(x)$  在  $E \subseteq R$  上一致收敛,  $\sum_{n=1}^{+\infty} |v_{n}(x) - v_{n+1}(x)|$  的部分和在 E 上一致有界. 则  $\sum_{n=1}^{+\infty} u_{n}(x) v_{n}(x)$  在 E 上一致收敛.

定理 12.2.6 设函数项级数  $\sum_{n=1}^{+\infty} u_{n}(x)$  和  $\sum_{n=1}^{+\infty} |v_{n}(x) - v_{n+1}(x)|$  的部分和均在

$E \subseteq \mathbb{R}$ 上一致有界, $\{v_n(x)\}$ 在 $E$ 上一致收敛到 0 , 则 $\sum_{n=1}^{+\infty} u_n(x) v_n(x)$ 在 $E$ 上一致收敛. 对于函数列的一致收敛性, 也有相应的 Abel 判别法和 Dirichlet 判别法, 不再赘述.

## 习题 12.2

1. 判断下列函数项级数的一致收敛性:

(1) $\sum_{n=1}^{+\infty} n\mathrm{e}^{-nx}, \quad x > 0;$

(2) $\sum_{n=1}^{+\infty} \frac{\sin x \sin nx}{\sqrt{n+x}}, \quad x \geqslant 0;$

(3) $\sum_{n=1}^{+\infty} \frac{1}{(1 + nx)^2}, \quad x \in \mathbb{R}$;

(4) $\sum_{n=1}^{+\infty} \frac{nx}{1 + n^5 x^2}, \quad x \in \mathbb{R}$.

2. 研究下面函数列在指定区间上的一致收敛性:

(1) $f_{n}(x) = \frac{1}{1 + nx}$:

(i) x > 0;

(ii)

$0 < x_{0} < x < +\infty.$

(2) $f_{n}(x) = \frac{x^{n}}{1 + x^{n}}:$

(i) $0 < x \leqslant x_0 < 1$;

(ii) $0.9 \leqslant x \leqslant 1.1$.

3. 若 $f_{n}(x)$ 在 $[a, b]$ 上连续, 且 $\{f_{n}(x)\}$ 在 $(a, b)$ 上一致收敛, 证明其在 $[a, b]$ 上一致收敛.

4. 设  $\{x_{n}\}$  是 R 中给定的无穷数列, 证明: 存在 R 上的单调函数  $y = f(x)$ , 使得  $f(x)$  恰在  $x_{n} (n = 1, 2, \cdots)$  处有第一类间断, 且跳跃值  $f(x_{n}^{+}) - f(x_{n}^{-})$  等于给定的实数  $a_{n}$ , 其中  $\sum_{n=1}^{+\infty}|a_{n}| < +\infty$ .

5. 设 $\sum_{n=1}^{+\infty} u_n(x)$ 在 $[a, b]$ 上收敛, $u_n(x)$ 可导且 $\sum_{n=1}^{+\infty} u_n'(x)$ 的部分和 $\{S_n'(x)\}$ 在 $[a, b]$ 上一致有界, 证明: $\sum_{n=1}^{+\infty} u_n(x)$ 在 $[a, b]$ 上一致收敛.

6. 若级数 $\sum_{n=1}^{+\infty} a_n$ 收敛, 证明: 级数 $\sum_{n=1}^{+\infty} a_n e^{-nx}$ 在 $0 \leqslant x < +\infty$ 上一致收敛.

7. 设 $\{f_n(x)\}$ 是定义在 $[a, b] \setminus \{x_0\}$ 的函数列，其中 $x_0 \in [a, b]$. 如果 $f_n(x) \Rightarrow f(x) (x \in [a, b] \setminus \{x_0\})$，并且对每个 $n \geqslant 1$ 有 $\lim_{x \to x_0} f_n(x) = c_n$. 证明:$\lim_{n \to +\infty} c_n$ 存在并且有 $\lim_{x \to x_0} f(x) = \lim_{n \to +\infty} c_n$.

8. 证明: 级数 $\sum_{n=1}^{+\infty}(-1)^{n}\frac{1}{n+x}$ 在 $(0,+\infty)$ 上一致收敛但并不绝对逐点收敛.

9. 研究下面级数在指定区间上的一致收敛性:

(1) $\sum_{n=1}^{+\infty} \frac{1}{(x+n)(x+n+1)}, \quad 0 < x < +\infty;$

(2) $\sum_{n=1}^{+\infty} \frac{\sin\left(n + \frac{1}{2}\right)x}{n^4 + x^4}, -\infty < x < +\infty;$