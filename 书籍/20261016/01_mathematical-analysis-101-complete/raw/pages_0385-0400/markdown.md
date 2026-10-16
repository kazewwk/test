解 (1) 考虑级数通项

$$
a _ {n} = \frac {1}{(\ln n) ^ {\ln n}} = \frac {1}{\mathrm{e} ^ {\ln n \cdot \ln (\ln n)}} = \frac {1}{n ^ {\ln (\ln n)}},
$$

当 n 适当大（比如  $n > e^{e^{2}}$ ）时，有  $n^{\ln(\ln n)} > n^{2}$ ，从而有  $a_{n} < \frac{1}{n^{2}}$ 。取优级数  $b_{n} = \frac{1}{n^{2}}$ ，根据前面 p-级数敛散性的结论知  $\sum_{n=1}^{+\infty} b_{n} \in c$ ，从而级数  $\sum_{n=3}^{+\infty} a_{n} \in c$ 。

(2) 注意到显然存在自然数  $n_{0}$ ，当  $n > n_{0}$  时，成立下面的关系式:

$$
\frac {1}{(\ln n) ^ {\ln (\ln n)}} = \frac {1}{\mathrm{e} ^ {(\ln (\ln n)) ^ {2}}} > \frac {1}{\mathrm{e} ^ {\ln n}} = \frac {1}{n},
$$

取 $b_{n} = \frac{1}{n}$, 则由级数 $\sum_{n=1}^{+\infty} b_{n} \in d$, 得知原级数发散.

回到定理 11.2.3, 我们知道关系式 (11.2.1) 等价于不等式  $\frac{a_{n}}{b_{n}} \leqslant c (n > n_{0})$ . 另一方面, 由于一个级数改变其有限项的值并不改变其敛散性, 因此上述不等式只要当 n 充分大时成立即可. 因此我们有下面极限形式的判别法:

推论 11.2.4 (比较判别法的极限形式) 设  $\sum_{n=1}^{+\infty}a_{n}$  和  $\sum_{n=1}^{+\infty}b_{n}$  是两个正项级数, 如果

$$
\lim _ {n \to + \infty} \frac {a _ {n}}{b _ {n}} = \ell ,
$$

那么

(1) 若 $0 < \ell < +\infty$，则 $\sum_{n=1}^{+\infty} a_n$ 和 $\sum_{n=1}^{+\infty} b_n$ 同敛散.
(2) 若 $\ell = 0$, 则当 $\sum_{n=1}^{+\infty} b_n$ 收敛时, $\sum_{n=1}^{+\infty} a_n$ 也收敛.
(3) 若 $\ell = +\infty$，则当 $\sum_{n=1}^{+\infty} b_n$ 发散时，$\sum_{n=1}^{+\infty} a_n$ 也发散.

证明 (1) 设 $0 < \ell < +\infty$ ，则对 $\varepsilon = \frac{\ell}{2} > 0$ ，存在 $N$ ，当 $n > N$ 时，有

$$
\left| \frac {a _ {n}}{b _ {n}} - \ell \right| <   \frac {\ell}{2},
$$

即

$$
\frac {\ell}{2} b _ {n} <   a _ {n} <   \frac {3 \ell}{2} b _ {n}.
$$

故两级数同敛散.

(2) 若 $\ell = 0$, 则对 $\varepsilon = 1$, 存在 $N$, 当 $n > N$ 时, 有

$$
0 <   \frac {a _ {n}}{b _ {n}} <   1, \quad \text {即} \quad a _ {n} <   b _ {n}.
$$

故当 $\sum_{n=1}^{+\infty} b_n$ 收敛时, 有 $\sum_{n=1}^{+\infty} a_n$ 收敛.

(3) 本情形是情形 (2) 的对偶, 证明可类似给出.

例 11.2.5 试判断下列级数的敛散性:

(1) $\sum_{n=1}^{+\infty} \frac{n+1}{\sqrt{n^4+1}}$;

(2) $\sum_{n=1}^{+\infty} \frac{n+2}{\sqrt{n^5+1}};$

(3) $\sum_{n=1}^{+\infty}\left(\frac{1}{n}-\ln\left(1+\frac{1}{n}\right)\right).$

解 只要注意到 $n \to +\infty$ 时，

$$
\frac {n + 1}{\sqrt {n ^ {4} + 1}} \sim \frac {1}{n}, \quad \frac {n + 2}{\sqrt {n ^ {5} + 1}} \sim \frac {1}{\sqrt {n ^ {3}}}, \quad \lim _ {n \to + \infty} \left(\frac {1}{n} - \ln \left(1 + \frac {1}{n}\right)\right) / \frac {1}{n ^ {2}} = \frac {1}{2},
$$

则可得第一个级数发散, 第二和第三个级数收敛.

下面我们考虑定理 11.2.3 中关系式 (11.2.1) 和推论 11.2.4 中关系式的极限形式  $\lim_{n\to+\infty}\frac{a_n}{b_n}=\ell$  的一种特殊情况, 即, 考虑数列  $\left\{\frac{a_n}{b_n}\right\}$  单调下降的情况: 如果该数列单调下降, 由于其非负性, 则知其极限  $\ell$  必存在且为有限. 因此级数  $\sum_{n=1}^{+\infty}a_n$  和  $\sum_{n=1}^{+\infty}b_n$  要么同敛散  $(0<\ell<+\infty)$ , 要么后者的收敛蕴涵着前者的收敛  $(\ell=0)$ . 另一方面, 注意到

$$
\left\{\frac {a _ {n}}{b _ {n}} \right\} \text {单调下降} \quad \Longleftrightarrow \quad \frac {a _ {n + 1}}{b _ {n + 1}} \leqslant \frac {a _ {n}}{b _ {n}} \quad \Longleftrightarrow \quad \frac {a _ {n + 1}}{a _ {n}} \leqslant \frac {b _ {n + 1}}{b _ {n}}.
$$

这样, 我们得到下面一种非常实用的判别法:

定理 11.2.5 (比值型比较判别法的普通形式) 设  $\sum_{n=1}^{+\infty} a_{n}$  和  $\sum_{n=1}^{+\infty} b_{n}$  是两个正项级数, 如果存在自然数  $n_{0}$ , 使得当  $n > n_{0}$  时, 有

$$
\frac {a _ {n + 1}}{a _ {n}} \leqslant \frac {b _ {n + 1}}{b _ {n}}, \tag {11.2.2}
$$

那么

(1) 如果  $\sum_{n=1}^{+\infty}b_{n}\in c,$  则  $\sum_{n=1}^{+\infty}a_{n}\in c.$
(2) 如果  $\sum_{n=1}^{+\infty}a_{n}\in d,$  则  $\sum_{n=1}^{+\infty}b_{n}\in d.$

比值判别法有相应的极限形式, 但此时需要注意的是 (11.2.2) 中的不等号 $\leqslant$ 应该是严格不等号 $<$, 因为很容易看出若取 $a_{n} = \frac{1}{n}, b_{n} = \frac{1}{n^{2}}$, 则两个比值的极限相等, 但敛散性不同. 即有下面的结论:

推论 11.2.6 (比值型比较判别法的极限形式) 设  $\sum_{n=1}^{+\infty}a_{n}$  和  $\sum_{n=1}^{+\infty}b_{n}$  是两个正项级数, 如果

$$
\lim _ {n \to + \infty} \frac {a _ {n + 1}}{a _ {n}} <   \lim _ {n \to + \infty} \frac {b _ {n + 1}}{b _ {n}}, \tag {11.2.3}
$$

那么

(1) 若  $\sum_{n=1}^{+\infty}b_{n}\in c,$  则  $\sum_{n=1}^{+\infty}a_{n}\in c.$
(2) 若  $\sum_{n=1}^{+\infty}a_{n}\in d,$  则  $\sum_{n=1}^{+\infty}b_{n}\in d.$

有时候, 我们也可以将上述推论中的极限改成更一般的上、下极限形式, 结论仍然成立, 证明从略.

推论 11.2.7 (比值型比较判别法的上、下极限形式) 设  $\sum_{n=1}^{+\infty} a_{n}$  和  $\sum_{n=1}^{+\infty} b_{n}$  是两个正项级数, 如果

$$
\varlimsup_ {n \to + \infty} \frac {a _ {n + 1}}{a _ {n}} <   \varliminf_ {n \to + \infty} \frac {b _ {n + 1}}{b _ {n}}, \tag {11.2.4}
$$

那么

(1) 若  $\sum_{n=1}^{+\infty}b_{n}\in c,$  则  $\sum_{n=1}^{+\infty}a_{n}\in c.$
(2) 若  $\sum_{n=1}^{+\infty}a_{n}\in d,$  则  $\sum_{n=1}^{+\infty}b_{n}\in d.$

下面我们讨论定理11.2.5的具体应用，并给出几个实用的判别法.在具体应用定理11.2.5时，我们常把对标级数 $\sum_{n = 1}^{+\infty}b_n$ 选为几何级数 $\sum_{n = 1}^{+\infty}q^n (q > 0)$ 或者 $p$ -级数 $\sum_{n = 1}^{+\infty}\frac{1}{n^p}$ 下面我们就这两种情况分别给予讨论.

## 11.2.2 几何级数为对标级数

如果把对标级数 $\sum_{n=1}^{+\infty} b_n$ 选为几何级数 $\sum_{n=1}^{+\infty} q^n (q > 0)$, 然后把被讨论的级数 $\sum_{n=1}^{+\infty} a_n$ 与之比较, 可以得到一些非常实用的级数敛散性判别法. 而两个级数之间的大小比较, 常见的比较方式有下面两种:

(i) $\frac{a_{n + 1}}{a_n}$ 与 $\frac{b_{n + 1}}{b_n} = q$ 比较； (ii) $\sqrt[n]{a_n}$ 与 $\sqrt[n]{b_n} = q$ 比较. (11.2.5)

下面的 d'Alembert 比值判别法和 Cauchy 根值判别法就是根据情况 (i) 和 (ii) 的具体应用得到的.

我们先看 (11.2.5) 中情况 (i) 下的 d'Alembert 比值判别法.

定理 11.2.8 (d'Alembert 比值判别法的普通形式) 设  $\sum_{n=1}^{+\infty} a_{n}$  为一正项级数.

(1) 如果存在自然数 $n_0$, 使得当 $n > n_0$ 时, 有 $\frac{a_{n+1}}{a_n} \leqslant q < 1$, 则级数 $\sum_{n=1}^{+\infty} a_n$ 收敛.
(2) 如果对于充分大的 n, 有  $\frac{a_{n+1}}{a_{n}} \geqslant 1$ , 则级数  $\sum_{n=1}^{+\infty} a_{n}$  发散.

例 11.2.6 设 a > 0, 试讨论级数  $\sum_{n=1}^{+\infty} n! \left(\frac{a}{n}\right)^{n}$  的敛散性.

解 因为

$$
\frac {a _ {n + 1}}{a _ {n}} = \frac {a}{\left(1 + \frac {1}{n}\right) ^ {n}} \rightarrow \frac {a}{\mathrm{e}} \quad (n \rightarrow + \infty).
$$

我们在几何级数通项 $b_{n} = q^{n}$ 中取 $q = \frac{a}{\mathrm{e}}$ ，则有:当 $0 < a < \mathrm{e}$ 时，原级数收敛；当 $a > \mathrm{e}$ 时，原级数发散.

当 $a = \mathrm{e}$ 时，注意到

$$
\frac {a _ {n + 1}}{a _ {n}} = \frac {\mathrm{e}}{\left(1 + \frac {1}{n}\right) ^ {n}} \geqslant 1,
$$

此时通项不趋于0,故级数也发散.

由于通项的前有限项不影响级数的敛散性, 因此, 在应用 d'Alembert 比值判别法定理 11.2.8 时, 直接考虑比值  $\frac{a_{n+1}}{a_{n}}$  的极限往往更方便. 具体来说, 有

推论 11.2.9 (d'Alembert 比值判别法的极限形式) 设  $\sum_{n=1}^{+\infty}a_{n}$  为一正项级数, 且

$$
\lim _ {n \to + \infty} \frac {a _ {n + 1}}{a _ {n}} = q. \tag {11.2.6}
$$

(1) 如果 q < 1, 则级数  $\sum_{n=1}^{+\infty} a_{n}$  收敛.
(2) 如果 q > 1，则级数  $\sum_{n=1}^{+\infty} a_{n}$  发散.

而当 $q = 1$ 时, 是级数收敛和发散的临界值, 一般来说级数 $\sum_{n=1}^{+\infty} a_n$ 的敛散性需要用其他方法做进一步讨论.

更一般地, 如果 (11.2.6) 式中的极限不存在, 那么代之以考虑它的上、下极限更方便, 即

推论 11.2.10 (d'Alembert 比值判别法的上、下极限形式) 设  $\sum_{n=1}^{+\infty} a_{n}$  为正项级数.

(1) 如果  $\varlimsup_{n\to+\infty}\frac{a_{n+1}}{a_n}=\overline{q}<1$  ，则级数  $\sum_{n=1}^{+\infty}a_n$  收敛.
(2) 如果  $\lim_{n\to+\infty}\frac{a_{n+1}}{a_n}=q>1$ ，则级数  $\sum_{n=1}^{+\infty}a_n$  发散.

证明 (1) 取实数 $\varepsilon > 0$ 满足 $\overline{q} + \varepsilon < 1$, 则存在 $N_{1} > 0$, 使得 $n > N_{1}$ 时, $\frac{a_{n+1}}{a_{n}} < \overline{q} + \varepsilon$. 因此有

$$
a _ {n + 1} = \frac {a _ {n + 1}}{a _ {n}} \frac {a _ {n}}{a _ {n - 1}} \dots \frac {a _ {N _ {1} + 1}}{a _ {N _ {1}}} \cdot a _ {N _ {1}} <   (\bar {q} + \varepsilon) ^ {n} (\bar {q} + \varepsilon) ^ {- N _ {1}} a _ {N _ {1}} = c (\bar {q} + \varepsilon) ^ {n},
$$

其中 $c = a_{N_1}(\bar{q} +\varepsilon)^{-N_1}$ .由于几何级数 $\sum_{n = 1}^{+\infty}(\bar{q} +\varepsilon)^n$ 收敛，得证

(2) 类似 (1) 的证明, 只要取实数 $\varepsilon > 0$ 满足 $q - \varepsilon > 1$, 可证 (2), 证略.

例 11.2.7 设 a 为一给定实数,  $a_{n}=\frac{2^{n}}{1+a^{2^{n}}}$   $n=0,1,\cdots$ . 试判断级数

$$
\sum_ {n = 0} ^ {+ \infty} a _ {n} = \frac {1}{1 + a} + \frac {2}{1 + a ^ {2}} + \frac {4}{1 + a ^ {4}} + \dots
$$

的敛散性.

解 考虑

$$
\frac {a _ {n + 1}}{a _ {n}} = 2 \frac {1 + a ^ {2 ^ {n}}}{1 + a ^ {2 ^ {n + 1}}}.
$$

当 $|a|>1$ 时,

$$
\frac {a _ {n + 1}}{a _ {n}} = 2 \frac {1 + a ^ {2 ^ {n}}}{1 + a ^ {2 ^ {n + 1}}} = 2 \frac {1 + a ^ {- 2 ^ {n}}}{a ^ {2 ^ {n}} + a ^ {- 2 ^ {n}}} \rightarrow 0 \quad (n \rightarrow + \infty).
$$

所以由 d'Alembert 比值判别法知所给级数收敛.

当  $|a| \leqslant 1$  时, 级数通项不趋于 0, 级数发散.

![](images/page_388_image_20.jpg)

注11.2.2 在推论11.2.10中, 如果 $\underline{q} = \overline{q} = 1$, 那么比值判别法也不能给出敛散的结论, 需要另寻他法. 比如对于调和级数 $\sum_{n=1}^{+\infty} \frac{1}{n}$, d'Alembert比值判别法不是一个有效的方法.

注11.2.3 如果在推论11.2.10中 $\varlimsup_{n\to +\infty}\frac{a_{n + 1}}{a_n} = \overline{q} >1$ ，我们得不出发散的结论；类似地，如果 $\lim_{n\to +\infty}\frac{a_{n + 1}}{a_n} = \underline{q} < 1$ ，我们也得不出收敛的结论.参见后面的例11.2.11.事实上，我们很容易通过构造性方法来解释这点:

任取一个收敛的正项级数 $\sum_{n=1}^{+\infty} a_n$, 令

$$
\tilde {a} _ {2 n + 1} = a _ {2 n + 1}, \qquad \tilde {a} _ {2 n} = \min \left\{\frac {1}{2} a _ {2 n}, \frac {1}{2} a _ {2 n + 1} \right\},
$$

则显然级数  $\sum_{n=1}^{+\infty}\tilde{a}_{n}$  收敛, 但  $\varlimsup_{n\to+\infty}\frac{\tilde{a}_{n+1}}{\tilde{a}_{n}}\geqslant2.$

我们再来讨论 (11.2.5) 中情况 (ii) 下的 Cauchy 根值判别法. 即, 在定理 11.2.3 中, 我们仍然选取几何级数 $b_{n} = q^{n}$ ($q > 0$) 作为参照比较的级数, 但现在不是通过考虑相邻两项的比值, 而是直接比较 $a_{n}$ 与 $q^{n}$ 的大小. 基于显然的不等式关系

$$
a _ {n} \leqslant q ^ {n} \quad \Longleftrightarrow \quad \sqrt [ n ]{a _ {n}} \leqslant q,
$$

我们可得下面的根值判别法.

## 定理 11.2.11 (Cauchy 根值判别法的普通形式)

设 $\sum_{n=1}^{+\infty} a_n$ 为一正项级数.

(1) 如果存在自然数 $n_0$, 使得当 $n > n_0$ 时, 有

$$
\sqrt [ n ]{a _ {n}} \leqslant q <   1, \tag {11.2.7}
$$

则级数  $\sum_{n=1}^{+\infty}a_{n}$  收敛.

(2) 如果存在无穷多个 $n$, 使得

$$
\sqrt [ n ]{a _ {n}} \geqslant 1, \tag {11.2.8}
$$

则级数  $\sum_{n=1}^{+\infty}a_{n}$  发散.

注 11.2.4 在断定级数  $\sum_{n=1}^{+\infty}a_{n}$  收敛时, 我们要求对所有充分大的 n, 都满足 (11.2.7) 式; 而在断定级数  $\sum_{n=1}^{+\infty}a_{n}$  发散时, 我们只需要存在无穷多项满足 (11.2.8) 式即可, 因为这足以破坏通项趋于 0 的必要条件了.

Cauchy 根值判别法也有相应的极限形式:

推论 11.2.12 (Cauchy 根值判别法的极限形式) 设  $\sum_{n=1}^{+\infty}a_{n}$  为一正项级数, 且

$$
\lim _ {n \to + \infty} \sqrt [ n ]{a _ {n}} = q.
$$

(1) 如果 q < 1, 则级数  $\sum_{n=1}^{+\infty} a_{n}$  收敛.
(2) 如果 q > 1 则级数  $\sum_{n=1}^{+\infty} a_{n}$  发散.

当根值列  $\left\{\sqrt[n]{a_{n}}\right\}$  的极限不存在时, 可以通过讨论相应的上极限来判定级数的敛散性.

推论 11.2.13 (Cauchy 根值判别法的上极限形式) 设  $\sum_{n=1}^{+\infty} a_{n}$  为一正项级数, 且

$$
\varlimsup_ {n \to + \infty} \sqrt [ n ]{a _ {n}} = q.
$$

(1) 如果 q < 1, 则级数  $\sum_{n=1}^{+\infty} a_{n}$  收敛.
(2) 如果 q > 1 则级数  $\sum_{n=1}^{+\infty} a_{n}$  发散.

推论 11.2.12 和推论 11.2.13 的证明完全类似于推论 11.2.10 的证明, 我们留给读者完成.

注11.2.5 当用上、下极限值来判别级数的敛散性时，与d'Alembert比值判别法不同之处在于，Cauchy根值判别法只需要考虑上极限即可:这是因为如果存在子列 $\{a_{n_k}\}$，$n_k\sqrt{a_{n_k}} \geqslant 1$，则 $a_{n_k} \geqslant 1$，从而通项 $\{a_n\}$ 有一子列不趋于0，故级数 $\sum_{n=1}^{+\infty} a_n$ 必然发散。而如果上极限 $\bar{q} < 1$，则通项趋于0的速度比几何级数 $\bar{q}^n$ 趋于0的速度还要快，从而级数收敛。所以，根值判别法只需考虑上极限即可。

注 11.2.6 在上述推论中, 如果 q = 1, 类似于比值判别法, 根值判别法也不能给出敛散的结论, 需要另寻他法. 比如对于 p-级数, Cauchy 根值判别法并不是一个有效的方法, 因为对于  $p = \{1, 2\}$ , 都有

$$
\lim _ {n \to + \infty} \sqrt [ n ]{\frac {1}{n ^ {p}}} = 1,
$$

但是 p 的两个不同值对应的级数敛散性刚好不同.

例 11.2.8 判断级数  $\sum_{n=1}^{+\infty}\frac{1}{2^{n}}\left(1+\frac{1}{n}\right)^{n^{2}}$  的敛散性.

解 因为

$$
\lim _ {n \to + \infty} \sqrt [ n ]{a _ {n}} = \lim _ {n \to + \infty} \frac {1}{2} \left(1 + \frac {1}{n}\right) ^ {n} = \frac {\mathrm{e}}{2} > 1,
$$

所以由 Cauchy 根值判别法知所给级数发散.

例 11.2.9 设  $a_{2n-1}=\frac{1}{2^{n}}, a_{2n}=\frac{1}{3^{n}}$ ，试讨论级数  $\sum_{n=1}^{+\infty}a_{n}$  的敛散性.

解 由于

$$
\varlimsup_ {n \to + \infty} \sqrt [ n ]{a _ {n}} = \frac {1}{\sqrt {2}} <   1,
$$

故由 Cauchy 根值判别法知所给级数收敛.

例 11.2.10 设 a > 0, 试讨论级数  $\sum_{n=1}^{+\infty}\frac{a^{n}}{1+a^{2n}}$  的敛散性.

解 当 a=1 时, 级数通项  $a_{n}=\frac{1}{2}\nrightarrow0$ , 故原级数发散.

当 $0 < a \neq 1$ 时，

$$
\lim _ {n \to + \infty} \sqrt [ n ]{a _ {n}} = \lim _ {n \to + \infty} \frac {a}{\sqrt [ n ]{1 + a ^ {2 n}}} = \left\{ \begin{array}{l l} a <   1, & a <   1, \\ \frac {1}{a} <   1, & a > 1, \end{array} \right.
$$

所以, 当  $a \neq 1$  时, 原级数收敛.

![](images/page_391_image_15.jpg)

<details>
<summary>natural_image</summary>

Blank white image with a dark blue horizontal bar at the top (no text or symbols)
</details>

注11.2.7 从理论上来说, 凡是能用 d'Alembert 判别法来判别敛散性的级数, 由 Cauchy 判别法也一定可以判别其敛散性, 而反过来则不一定. 这是基于以下事实: 对正项级数 $\sum_{n=1}^{+\infty} a_n (a_n > 0)$, 总成立以下不等式:

$$
\varliminf_ {n \to + \infty} \frac {a _ {n + 1}}{a _ {n}} \leqslant \varliminf_ {n \to + \infty} \sqrt [ n ]{a _ {n}} \leqslant \varlimsup_ {n \to + \infty} \sqrt [ n ]{a _ {n}} \leqslant \varlimsup_ {n \to + \infty} \frac {a _ {n + 1}}{a _ {n}}. \tag {11.2.9}
$$

我们给出 (11.2.9) 式的一个证明, 只考虑最右边的不等式, 最左边的不等式可以类似给出.

不妨设 $\lim_{n\to +\infty}\frac{a_{n + 1}}{a_n} = L < +\infty$ ，则对任何 $\varepsilon >0$ ，存在 $N\geqslant 1$ 使得当 $n\geqslant N$ 时有$\frac{a_{n + 1}}{a_n}\leqslant L + \varepsilon .$ 从而对任何 $n\geqslant N,$ 成立

$$
a _ {n} \leqslant a _ {N} \cdot (L + \varepsilon) ^ {n - N}.
$$

因此，

$$
\varlimsup_ {n \to + \infty} \sqrt [ n ]{a _ {n}} \leqslant L + \varepsilon .
$$

由 $\varepsilon > 0$ 的任意性得到 $\lim_{n \to +\infty} \sqrt[n]{a_n} \leqslant L$.

例11.2.11 试分别讨论以

(1) $u_{n} = \frac{2 + (-1)^{n}}{2^{n}},$

(2) $v_{n}=\left(\frac{2+(-1)^{n}}{4}\right)^{n}\quad n=1,2,\cdots$

为通项的级数的敛散性.

解 因为

(1) $\varlimsup_{n\to +\infty}\sqrt[n]{u_n} = \frac{1}{2} < 1,$ (2) $\varlimsup_{n\to +\infty}\sqrt[n]{v_n} = \frac{3}{4} < 1,$

所以根据 Cauchy 根值判别法知这两个级数均收敛. 但是如果在本例中应用比值判别法, 则分别有

(1) $\frac{u_{2n}}{u_{2n - 1}} = \frac{1}{2} \cdot \frac{2 + (-1)^{2n}}{2 + (-1)^{2n - 1}} = \frac{3}{2},$

$$
\frac {u _ {2 n + 1}}{u _ {2 n}} = \frac {1}{2} \cdot \frac {2 + (- 1) ^ {2 n + 1}}{2 + (- 1) ^ {2 n}} = \frac {1}{6}.
$$

所以有

$$
\varlimsup_ {n \to + \infty} \frac {u _ {n + 1}}{u _ {n}} = \frac {3}{2}, \quad \varliminf_ {n \to + \infty} \frac {u _ {n + 1}}{u _ {n}} = \frac {1}{6}.
$$

可以看出, d'Alembert 判别法失效.

(2) $\frac{v_{2n}}{v_{2n - 1}} = \frac{1}{4}\cdot \frac{(2 + (-1)^{2n})^{2n}}{(2 + (-1)^{2n - 1})^{2n - 1}} = \frac{1}{4}\cdot 3^{2n},$

$$
\frac {v _ {2 n + 1}}{v _ {2 n}} = \frac {1}{4} \cdot \frac {(2 + (- 1) ^ {2 n + 1}) ^ {2 n + 1}}{(2 + (- 1) ^ {2 n}) ^ {2 n}} = \frac {1}{4} \cdot \frac {1}{3 ^ {2 n}}.
$$

所以有

$$
\varlimsup_ {n \to + \infty} \frac {v _ {n + 1}}{v _ {n}} = + \infty , \quad \varliminf_ {n \to + \infty} \frac {v _ {n + 1}}{v _ {n}} = 0.
$$

同样, d'Alembert 判别法也不能给出敛散性的结论.

需要注意的是, 虽然 Cauchy 根值判别法的适用范围比 d'Alembert 判别法要广泛一些, 但在具体问题中, 还是要充分考虑通项的具体表达形式选取适合的判别法, 而不是一味使用单一方法. 比如形如例 11.2.6 的级数或者以 $a_{n} = n!n^{-n}$ 为通项的级数的敛散性, 用 d'Alembert 比值判别法就要比 Cauchy 根值判别法来得方便.

## 11.2.3 $p$-级数为对标级数

在上面的讨论中我们是基于把 $b_{n}$ 选为几何级数 $q^{n}$ 作为对标级数, 然后具体应用, 得到了 d'Alembert 判别法和 Cauchy 判别法, 这两种判别法都存在一种临界状态 $(q = 1)$.

比如在讨论 $p$-级数敛散性时, 两种方法也都不再有效. 下面, 我们再介绍一些其他的判别方法. 为此, 我们选 $b_{n} = \frac{1}{n^{p}}$, 即选 $p$-级数 $\sum_{n=1}^{+\infty} \frac{1}{n^{p}}$ 作为对标级数, 那么, 我们可得到下面的 Raabe 判别法.

定理 11.2.14 (Raabe 判别法的普通形式) 设  $\sum_{n=1}^{+\infty} a_{n}$  为一正项级数.

(1) 如果存在 $r > 1, N > 1$, 使得当 $n > N$ 时, 有 $n\left(\frac{a_n}{a_{n+1}} - 1\right) \geqslant r$, 则级数 $\sum_{n=1}^{+\infty} a_n$ 收敛.

(2) 如果存在 $N > 1$, 使得当 $n > N$ 时, 有

$$
n \left(\frac {a _ {n}}{a _ {n + 1}} - 1\right) \leqslant 1,
$$

则级数  $\sum_{n=1}^{+\infty}a_{n}$  发散.

定理 11.2.15 (Raabe 判别法的极限形式) 设  $\sum_{n=1}^{+\infty}a_{n}$  为一正项级数, 有

$$
\lim _ {n \to + \infty} n \left(\frac {a _ {n}}{a _ {n + 1}} - 1\right) = r,
$$

其中  $r \in [-\infty, +\infty]$ .

(1) 如果 r > 1, 则级数  $\sum_{n=1}^{+\infty} a_{n}$  收敛.
(2) 如果 r < 1, 则级数  $\sum_{n=1}^{+\infty} a_{n}$  发散.
(3) 如果 r = 1，则级数  $\sum_{n=1}^{+\infty} a_{n}$  可能收敛也可能发散.

我们只给出 Raabe 判别法极限形式的证明, 普通形式 Raabe 定理的证明读者可以自行补充. 在给出定理的逻辑验证之前, 我们来分析一下定理中的关系式在说些什么. 因为一旦明白了结论由来的心路过程, 逻辑证明就成为水到渠成的事了.

我们选取 $p$-级数 $b_{n} = \frac{1}{n^{p}}$ 作为比较判别法中的对标级数. 这样, 一方面我们有

$$
\frac {b _ {n}}{b _ {n + 1}} = \frac {(n + 1) ^ {p}}{n ^ {p}} = \left(1 + \frac {1}{n}\right) ^ {p} \cong 1 + \frac {p}{n} \qquad (n \gg 1).
$$

另一方面, 定理中的假设蕴涵着下面的关系式成立:

$$
\lim _ {n \to + \infty} n \left(\frac {a _ {n}}{a _ {n + 1}} - 1\right) = r \quad \Longleftrightarrow \quad \frac {a _ {n}}{a _ {n + 1}} \cong 1 + \frac {r}{n} \quad (n \gg 1).
$$

可以看出,两个级数通项的比值已经具备了完全相同的表达形式.

为了应用比较判别法, 需要建立 $\frac{a_n}{a_{n+1}}$ 和 $\frac{b_n}{b_{n+1}}$ 之间的大小关系. 具体来说, 如果我们希望级数 $\sum_{n=1}^{+\infty} a_n$ 收敛, 则需要一个收敛的 $p$-级数 $\sum_{n=1}^{+\infty} \frac{1}{n^p}$, 并且有关系式 $\frac{a_n}{a_{n+1}} \geqslant \frac{b_n}{b_{n+1}}$. 这等价于 $p > 1$ 且成立关系式

$$
1 + \frac {r}{n} \cong \frac {a _ {n}}{a _ {n + 1}} \geqslant \frac {b _ {n}}{b _ {n + 1}} \cong 1 + \frac {p}{n} \quad (n \gg 1). \tag {11.2.10}
$$

至此, 情况就非常清楚了: 当定理中的极限值 $r > 1$ 时, 级数 $\sum_{n=1}^{+\infty} a_n$ 的收敛与否取决于在保证关系式 (11.2.10) 成立的条件下, 是否还有余地选取 $p > 1$. 而这一点是显然的, 因为对任意的 $r > 1$, 都有足够多的实数 $p$ 加塞到 1 和 $r$ 之间. 事实上, 我们甚至可以做到: 对于任意实数 $r > 1$, 存在实数 $p$ 和 $q$ 满足 $1 < p < q < r$, 至于在 $p$ 和 $r$ 之间插入一个实数 $q$, 是给逻辑证明中的 $\varepsilon$ 留余地的. 类似的分析表明, 如果定理中的 $r < 1$, 则只要选取 $b_n$ 为调和级数 $(p = 1)$, 即可证明原级数发散了.

证明 (1) 由假设 $\lim_{n\to +\infty}n\left(\frac{a_n}{a_{n + 1}} -1\right) = r > 1,$ 取 $q,1 < q < r,$ 则存在自然数$N_{1}$ ，当 $n\geqslant N_1$ 时，有

$$
\frac {a _ {n}}{a _ {n + 1}} > 1 + \frac {q}{n}.
$$

再取 $p, 1 < p < q < r$. 考虑极限

$$
\lim _ {n \to + \infty} \frac {\left(1 + \frac {1}{n}\right) ^ {p} - 1}{\frac {q}{n}} = \lim _ {x \to 0} \frac {(1 + x) ^ {p} - 1}{q x} = \frac {p}{q} <   1.
$$

因此, 存在 $N_{2} > 0$, 当 $n \geqslant N_{2}$ 时, 有

$$
\left(1 + \frac {1}{n}\right) ^ {p} \leqslant 1 + \frac {q}{n}.
$$

所以, 当 $n > \max \{N_1, N_2\}$ 时, 有

$$
\frac {a _ {n}}{a _ {n + 1}} > 1 + \frac {q}{n} \geqslant \left(1 + \frac {1}{n}\right) ^ {p} = \frac {\frac {1}{n ^ {p}}}{\frac {1}{(n + 1) ^ {p}}} = \frac {b _ {n}}{b _ {n + 1}}.
$$

注意到以 $b_{n}$ 为通项的 $p$-级数当 $p > 1$ 时是收敛的, 故由比较判别法知 $\sum_{n=1}^{+\infty} a_{n}$ 收敛.

(2) 如果  $\lim_{n\to+\infty}n\left(\frac{a_n}{a_{n+1}}-1\right)=r<1,$  取 r<q<1, 则存在 N>0, 当 n>N 时,

$$
\frac {a _ {n}}{a _ {n + 1}} <   1 + \frac {q}{n} <   1 + \frac {1}{n} = \frac {\frac {1}{n}}{\frac {1}{n + 1}} = \frac {b _ {n}}{b _ {n + 1}}.
$$

注意到以  $b_{n}=\frac{1}{n}$  为通项的调和级数是发散的, 故由比较判别法知  $\sum_{n=1}^{+\infty}a_{n}$  发散. ☐

例 11.2.12 试讨论下列级数的敛散性:

(1) $\sum_{n=1}^{+\infty} \frac{(2n-1)!!}{(2n)!!}$;

(2) $\sum_{n=1}^{+\infty}\left(\frac{(2n-1)!!}{(2n)!!}\right)^{3}$.

解 记 $u_{n} = \frac{(2n - 1)!!}{(2n)!!}, v_{n} = \left(\frac{(2n - 1)!!}{(2n)!!}\right)^{3}$. 则有

$$
\lim _ {n \to + \infty} \frac {u _ {n + 1}}{u _ {n}} = 1, \quad \lim _ {n \to + \infty} \frac {v _ {n + 1}}{v _ {n}} = 1.
$$

利用Stirling公式 $n! \sim \left(\frac{n}{\mathrm{e}}\right)^n \sqrt{2\pi n}$, 可以证明

$$
\lim _ {n \to + \infty} \sqrt [ n ]{u _ {n}} = 1, \quad \lim _ {n \to + \infty} \sqrt [ n ]{v _ {n}} = 1.
$$

这说明无论用 d'Alembert 比值判别法还是 Cauchy 根值判别法, 都不能确定这两个级数的敛散性.

现在我们用 Raabe 判别法来讨论. 由于

$$
n \left(\frac {u _ {n}}{u _ {n + 1}} - 1\right) = n \left(\frac {2 n + 2}{2 n + 1} - 1\right)\rightarrow \frac {1}{2} \quad (n \rightarrow + \infty),
$$

根据 Raabe 判别法知, 级数 (1) 发散.

同理，

$$
n \left(\frac {v _ {n}}{v _ {n + 1}} - 1\right) = n \left(\left(\frac {2 n + 2}{2 n + 1}\right) ^ {3} - 1\right) = n \cdot \frac {1 2 n ^ {2} + 1 8 n + 7}{(2 n + 1) ^ {3}} \rightarrow \frac {3}{2} \quad (n \rightarrow + \infty),
$$

根据 Raabe 判别法知, 级数 (2) 收敛.

![](images/page_395_image_19.jpg)

注 11.2.8 类似于注 11.2.7, 可以证明凡是能用 d'Alembert 比值判别法给出敛散答案的级数, 都可以用 Raabe 判别法回答, 所以后者是前者的一个加强版. 尽管如此, Raabe 判别法也有一个临界状态, 即定理 11.2.15 中 r = 1时, Raabe 判别法也将无效, 还需另寻他法. 比如, 级数 $\sum_{n=1}^{+\infty} \left( \frac{(2n-1)!!}{(2n)!!} \right)^{2}$ 和 $\sum_{n=2}^{+\infty} \frac{1}{n \ln^{\alpha} n}$ 的敛散性用 Raabe 判别法都无法给出.

当定理 11.2.15 中的极限不存在时, 可以考虑相应的上、下极限, 即有下面更一般的 Raabe 判别法. 读者可以给出相应的证明.

定理 11.2.16 (Raabe 判别法) 设  $\sum_{n=1}^{+\infty}a_{n}$  为一正项级数.

(1) 如果  $\lim_{n\to+\infty}n\left(\frac{a_n}{a_{n+1}}-1\right)=r>1$ ，则级数  $\sum_{n=1}^{+\infty}a_n$  收敛.
(2) 如果  $\lim_{n\to+\infty}n\left(\frac{a_n}{a_{n+1}}-1\right)=\tilde{r}<1$  ，则级数  $\sum_{n=1}^{+\infty}a_n$  发散.

## 11.2.4 其他的对标级数

前面我们把几何级数作为对标级数, 得到了 d'Alembert $^{①}$  比值判别法和 Cauchy 根值判别法. 然后又把 p-级数作为对标级数, 得到了 Raabe $^{②}$  判别法. 我们还看到, Raabe 判别法虽然判别的范围比根值判别法和比值判别法要广泛一些, 但仍然有临界状态, 即判别法失效的情况. 事实上, 后面我们将证明, 对于任何一个收敛的级数, 都可以构造出一个比它收敛得还慢的收敛级数. 因此除非像 Cauchy 准则或者像正项级数部分和序列的有界性这样的充要条件, 任何充分性的判别法都有其解决不了的情况. 换句话说, 任何一个充分性判别法, 都有其局限性, 都只能解决若干类而非全部级数的敛散问题. 尽管如此, 建立一些比 Raabe 更精细的判别法还是很值得的.

事实上, 如果我们选

$$
b _ {n} = \frac {1}{n \ln^ {p} n}, \quad b _ {n} = \frac {1}{n \ln n (\ln \ln n) ^ {p}}, \quad b _ {n} = \frac {1}{n \ln n \ln \ln n (\ln \ln \ln n) ^ {p}}, \quad \dots
$$

作为对标级数的通项, 则可以得到更多的判别法, 比如 Gauss 或 Bertrand 判别法. 这个细化过程是无穷尽的, 不再赘述.

将前面基本的比较法应用到具体的场景, 得到诸多的判别法, 由于大多没有明显的思想上的不同, 因此我们把诸如 Bertrand $^{③}$ 判别法、Gauss 判别法、Kummer $^{④}$ 判别法等, 都放到后面的习题里, 供读者熟悉一下技术手法. 需要指出的是, Kummer 判别法的思想是来自正项级数收敛的充要条件是其部分和数列有上界, 与这里的比较判别法没有太多直接的联系 (参见《美国数学月刊》102 卷 (1995) 817-818 页中的历史观点).

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">① d'Alembert, Jean le Rond, 1717 年 11 月 17 日—1783 年 10 月 29 日, 法国数学家、哲学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">② Raabe, Joseph Ludwig, 1801 年 5 月 15 日—1859 年 1 月 22 日, 瑞士数学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">③ Bertrand, Joseph Louis François, 1822 年 3 月 11 日—1900 年 4 月 5 日, 法国数学家、经济学家.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">④ Kummer, Ernst Eduard, 1810 年 1 月 29 日—1893 年 5 月 14 日, 德国数学家.</span></small>

## 11.2.5 Cauchy 积分判别法

不难看出, 对于形如

$$
\sum_ {n = 3} ^ {+ \infty} \frac {1}{n ^ {p}}, \quad \sum_ {n = 3} ^ {+ \infty} \frac {1}{n ^ {p} \ln^ {q} n}, \quad \sum_ {n = 3} ^ {+ \infty} \frac {1}{n ^ {p} \ln^ {q} n \ln^ {r} \ln n}
$$

的级数, 用前面的比值判别法、根值判别法, 甚至 Raabe 判别法, 都很难确定它们的敛散性. 但这些级数有一个共同的特点, 就是通项为正, 单调下降趋于 0. 对于这类级数, 我们有下面的 Cauchy 积分判别法. 具体说来, 假设 $\{a_{n}\}$ 是一个单调下降趋于 0 的数列, 我们可以任取一个定义在 $[1, +\infty)$ 上的单调下降的连续函数 $f(x)$, 使得 $f(n) = a_{n}$. 从广义积分的基本性质可以看出

$$
\sum_ {n = 2} ^ {+ \infty} a _ {n} \leqslant \int_ {1} ^ {+ \infty} f (x) \mathrm{d} x \leqslant \sum_ {n = 1} ^ {+ \infty} a _ {n}.
$$

因此, 下面的定理成立.

定理 11.2.17 设函数  $f(x)$  在  $[1, +\infty)$  上单调下降，则级数  $\sum_{n=1}^{+\infty} f(n)$  与无穷限广义积分  $\int_{1}^{+\infty} f(x) dx$  同敛散.

证明 对任一自然数 $n$, 当 $n \leqslant x \leqslant n + 1$ 时, 有

$$
f (n + 1) \leqslant f (x) \leqslant f (n).
$$

所以有

$$
a _ {n + 1} = \int_ {n} ^ {n + 1} f (n + 1) \mathrm{d} x \leqslant \int_ {n} ^ {n + 1} f (x) \mathrm{d} x \leqslant \int_ {n} ^ {n + 1} f (n) \mathrm{d} x = a _ {n}.
$$

因此有

$$
\sum_ {n = 2} ^ {+ \infty} a _ {n} \leqslant \int_ {1} ^ {+ \infty} f (x) \mathrm{d} x \leqslant \sum_ {n = 1} ^ {+ \infty} a _ {n}.
$$

故定理结论成立.

例 11.2.13 试讨论下列级数的敛散性:

(1) $\sum_{n=3}^{+\infty} \frac{1}{n^p}$;

(2) $\sum_{n=3}^{+\infty} \frac{1}{n^p \ln^n n}$;

(3) $\sum_{n=3}^{+\infty} \frac{1}{n^p \ln^q n \ln^r \ln n}$.

解 (1) 选取 $f(x) = \frac{1}{x^p}, x \geqslant 1$. 根据定理 11.2.17 可知广义积分 $\int_{1}^{+\infty} f(x) \mathrm{d}x$ 的敛散性如下: 当 $p \leqslant 1$ 时, 广义积分发散; 当 $p > 1$ 时, 广义积分收敛. 因此, 相应 $p$-级数的敛散性亦然.

(2) 选取 $f(x) = \frac{1}{x^p \ln^q x}$, $x \geqslant a > 1$, 一方面, 我们知道广义积分 $\int_{a}^{+\infty} f(x) \mathrm{d}x$ 的敛散性如下:

(i) 当 p < 1 时, 积分发散;
(ii) 当  $p=1, q \leqslant 1$  时, 积分发散; 当 p = 1, q > 1 时, 积分收敛;
(iii) 当 p > 1 时, 积分收敛.

另一方面, 根据定理 11.2.17, 可知相应级数的敛散性与上面 p, q 的取值相对应.

(3) 可类似讨论, 级数的敛散性如下:
(i) 当 p < 1 时, 级数发散;
(ii) 当 p = 1, q < 1 时, 级数发散;
(iii) 当 p = 1, q > 1 时, 级数收敛;
(iv) 当  $p=1, q=1, r \leqslant 1$  时, 级数发散; 当  $p=1, q=1, r > 1$  时, 级数收敛;
(v) 当 p > 1 时, 级数收敛.

选取适当的不等式放缩, 有时候可以利用 Cauchy 积分判别法, 非常方便地判定通项级别很靠近 $\frac{1}{n^{1 + a_n}} (a_n \to 0, n \to +\infty)$ 的级数的敛散性.

例 11.2.14 证明: 级数  $\sum_{n=1}^{+\infty}\frac{1}{n^{1+\frac{1}{n}}}$  发散.

证明 根据 Cauchy 积分判别法, 考虑广义积分

$$
\int_ {1} ^ {+ \infty} \frac {1}{x ^ {1 + \frac {1}{x}}} \mathrm{d} x = \int_ {0} ^ {+ \infty} \frac {1}{\mathrm{e} ^ {t \mathrm{e} ^ {- t}}} \mathrm{d} t > \int_ {0} ^ {+ \infty} \frac {1}{\mathrm{e} ^ {t / t}} \mathrm{d} t = + \infty ,
$$

其中第一个等式是由变换  $x = e^{t}$  得到.

## 11.2.6 级数敛散的快慢 Abel-Dini 定理

前面我们已经看到, 凡是用几何级数做比较可以判断出收敛性的级数一定也可以用 $p$-级数加以比较来判断出敛散性. 事实上, 对于任何 $q \in [0,1)$, 以及 $p \in \mathbb{R}$, 均有 $\lim_{n \to +\infty} \frac{q^n}{1/n^p} = 0$. 而对于 $q > 1$, 有 $\lim_{n \to +\infty} \frac{q^n}{1/n^p} = +\infty$. 上面的事实可以表示为: 任何一个收敛的 $p$-级数都比任何一个收敛的正项几何级数要收敛得“更慢”, 而任何一个发散的 $p$-级数要比任何一个发散的正项几何级数发散得“更慢”. 同理, $\sum_{n=2}^{+\infty} \frac{1}{n \ln n}$ 是比所有发散的 $p$-级数发散得“更慢”的发散级数, 而 $\sum_{n=2}^{+\infty} \frac{1}{n \ln^2 n}$ 是比所有收敛的 $p$-级数收敛得“更慢”的收敛级数. 当然, 我们也可以用敛散得“更快”来描述, 比如收敛的正项几何级数总是比收敛的 $p$-级数收敛得“更快”. 注意, 并非任意两个级数敛散的速度都可以比较的.

这里关于级数敛散得快慢的定义必须要加以明确了, 否则, 比如级数 $\sum_{n=1}^{+\infty} a_n$ 收敛时, 则级数 $\sum_{n=1}^{+\infty} 2a_n$ 也收敛, 我们能说后者比前者收敛得快或者慢吗? 而且, 比较这两个级数敛散的快慢似乎不是我们感兴趣的话题. 我们给出下面级数敛散快慢的定义. 除非另外说明, 我们这里讨论的级数均指严格正项级数.

定义 11.2.2 设  $\sum_{n=1}^{+\infty}a_{n}$  和  $\sum_{n=1}^{+\infty}b_{n}$  是两个给定的正项级数.

(1) 若两者均收敛, 且 $a_{n} = o(b_{n})$, 则称 $\sum_{n=1}^{+\infty} b_{n}$ 比 $\sum_{n=1}^{+\infty} a_{n}$ 收敛得慢, 或称 $\sum_{n=1}^{+\infty} a_{n}$ 比 $\sum_{n=1}^{+\infty} b_{n}$ 收敛得快.
(2) 若两者均发散, 且 $b_{n} = o(a_{n})$, 则称 $\sum_{n=1}^{+\infty} b_{n}$ 比 $\sum_{n=1}^{+\infty} a_{n}$ 发散得慢, 或称 $\sum_{n=1}^{+\infty} a_{n}$ 比 $\sum_{n=1}^{+\infty} b_{n}$ 发散得快.

关于正项级数敛散性的快慢, 下面结论成立:

定理 11.2.18 (du Bois-Reymond 定理) (1) 对任一收敛的正项级数, 都存在比它收敛得更慢的正项级数.

(2) 对任一发散的正项级数, 都存在比它发散得更慢的正项级数.

定理 11.2.18 可以通过下面 Abel-Dini 定理的构造性证明来完成。为此, 我们介绍下面的 Abel-Dini 定理:

定理 11.2.19 (Abel-Dini 定理) (1) 设正项级数 $\sum_{k=1}^{+\infty} a_k$ 收敛. 则级数 $\sum_{n=1}^{+\infty} \frac{a_n}{T_n^{1+\alpha}}$ 收敛的充要条件是 $\alpha < 0$, 其中 $T_n$ 为级数 $\sum_{k=1}^{+\infty} a_k$ 的第 $n$ 个余式和, 即 $T_n = a_n + a_{n+1} + \cdots$.

(2) 设正项级数  $\sum_{k=1}^{+\infty}a_{k}$  发散. 则  $\sum_{n=1}^{+\infty}\frac{a_{n}}{S_{n}^{1+\alpha}}$  收敛的充要条件是  $\alpha>0$ , 其中  $S_{n}$  为级数  $\sum_{k=1}^{+\infty}a_{k}$  的第 n 个部分和, 即  $S_{n}=a_{1}+a_{2}+\cdots+a_{n}$ .