证明 (1) 设正项级数  $\sum_{k=1}^{+\infty}a_{k}$  收敛. 记  $a_{0}=0, S_{0}=0, \sum_{k=0}^{+\infty}a_{k}=S.$  由  $T_{n}=S-S_{n-1}$   $(n=1,2,\cdots)$ ，以及  $\{S_{n}\}$  单调上升趋于 S，知  $\{T_{n}\}$  单调下降趋于 0，即

$$
S = T _ {1} \geqslant T _ {2} \geqslant T _ {3} \geqslant \dots , \quad T _ {n} > 0, \quad T _ {n} \rightarrow 0 \quad (n \rightarrow + \infty).
$$

(i) 当 $\alpha \leqslant -1$ 时, 由 $T_{n} \to 0 (n \to +\infty)$ 知, 存在 $N > 0$, 当 $n > N$ 时, $T_{n} < 1$, 故 $\frac{1}{T_{n}^{1+\alpha}} \leqslant 1$. 因此有 $\frac{a_{n}}{T_{n}^{1+\alpha}} \leqslant a_{n}$, 由比较判别法知级数 $\sum_{n=1}^{+\infty} \frac{a_{n}}{T_{n}^{1+\alpha}}$ 收敛.

(ii) 当  $-1 < \alpha < 0, x \in [T_{n+1}, T_n]$  时, 考察广义积分  $\int_{0}^{S} \frac{dx}{x^{1+\alpha}}$  和级数  $\sum_{n=1}^{+\infty} \frac{a_n}{T_n^{1+\alpha}}$ , 注意到  $a_n = T_n - T_{n+1}, \int_{T_{n+1}}^{T_n} \frac{dx}{x^{1+\alpha}} = \frac{a_n}{\xi^{1+\alpha}} \geqslant \frac{a_n}{T_n^{1+\alpha}}$ , 其中  $\xi \in [T_{n+1}, T_n]$ , 知

$$
\sum_ {n = 1} ^ {+ \infty} \frac {a _ {n}}{T _ {n} ^ {1 + \alpha}} \leqslant \sum_ {n = 1} ^ {+ \infty} \int_ {T _ {n + 1}} ^ {T _ {n}} \frac {\mathrm{d} x}{x ^ {1 + \alpha}} \leqslant \int_ {0} ^ {S} \frac {\mathrm{d} x}{x ^ {1 + \alpha}} <   + \infty .
$$

因此, 级数  $\sum_{n=1}^{+\infty}\frac{a_{n}}{T_{n}^{1+\alpha}}$  收敛.

(iii) 当 $\alpha = 0$ 时, 我们用 Cauchy 准则证明级数 $\sum_{n=1}^{+\infty} \frac{a_n}{T_n}$ 发散. 事实上, 我们有

$$
\left| \frac {a _ {n + 1}}{T _ {n + 1}} + \frac {a _ {n + 2}}{T _ {n + 2}} + \dots + \frac {a _ {n + p}}{T _ {n + p}} \right| \geqslant \frac {1}{T _ {n + 1}} | a _ {n + 1} + a _ {n + 2} + \dots + a _ {n + p} | = 1 - \frac {T _ {n + p + 1}}{T _ {n + 1}}.
$$

不论取 $n$ 多么大, 都可以选取这样的 $p$, 使得 $\frac{T_{n+p+1}}{T_{n+1}} < \frac{1}{2}$, 因而

$$
\left| \frac {a _ {n + 1}}{T _ {n + 1}} + \frac {a _ {n + 2}}{T _ {n + 2}} + \dots + \frac {a _ {n + p}}{T _ {n + p}} \right| > \frac {1}{2}.
$$

从而原级数发散.

(iv) 当  $\alpha > 0$  时, 由

$$
\frac {a _ {n}}{T _ {n} ^ {1 + \alpha}} = \frac {a _ {n}}{T _ {n}} \cdot \frac {1}{T _ {n} ^ {\alpha}},
$$

和 $T_{n}\rightarrow 0$ $(n\to +\infty)$ ，知存在 $N > 0$ ，当 $n > N$ 时， $\frac{1}{T_n^\alpha}\geqslant 2,$ 从而有

$$
\frac {a _ {n}}{T _ {n} ^ {1 + \alpha}} \geqslant 2 \frac {a _ {n}}{T _ {n}}.
$$

根据比较判别法知, 原级数发散.

(2) 设正项级数 $\sum_{k=1}^{+\infty} a_k$ 发散, 这种情况下定理的证明思路和 (1) 完全类似, 可简述如下.

(i) 当 $\alpha > 0$ 时, 利用 Cauchy 积分判别法, 比较广义积分 $\int_{1}^{+\infty} \frac{\mathrm{d}x}{x^{1 + \alpha}}$ 和级数 $\sum_{n=1}^{+\infty} \frac{a_n}{S_n^{1 + \alpha}}$ 的大小. 由于

$$
\frac {a _ {n}}{S _ {n} ^ {1 + \alpha}} = \frac {S _ {n} - S _ {n - 1}}{S _ {n} ^ {1 + \alpha}} \leqslant \int_ {S _ {n - 1}} ^ {S _ {n}} \frac {\mathrm{d} x}{x ^ {1 + \alpha}} \quad (n = 2, 3, \dots),
$$

故

$$
\sum_ {n = 2} ^ {+ \infty} \frac {a _ {n}}{S _ {n} ^ {1 + \alpha}} \leqslant \int_ {a _ {1}} ^ {+ \infty} \frac {\mathrm{d} x}{x ^ {1 + \alpha}},
$$

而右端的无穷限积分当 $\alpha > 0$ 时收敛, 故 $\sum_{n=1}^{+\infty} \frac{a_n}{S_n^{1+\alpha}}$ 收敛.

(ii) 当 $\alpha = 0$ 时, 我们利用 Cauchy 准则证明级数 $\sum_{n=1}^{+\infty} \frac{a_n}{S_n}$ 发散. 为此, 考虑

$$
\left| \frac {a _ {n + 1}}{S _ {n + 1}} + \frac {a _ {n + 2}}{S _ {n + 2}} + \dots + \frac {a _ {n + p}}{S _ {n + p}} \right| \geqslant \frac {1}{S _ {n + p}} \left| a _ {n + 1} + a _ {n + 2} + \dots + a _ {n + p} \right| = 1 - \frac {S _ {n}}{S _ {n + p}}.
$$

不论取 $n$ 多么大, 都可以选取这样的 $p$, 使得 $\frac{S_n}{S_{n+p}} < \frac{1}{2}$, 因而

$$
\left| \frac {a _ {n + 1}}{S _ {n + 1}} + \frac {a _ {n + 2}}{S _ {n + 2}} + \dots + \frac {a _ {n + p}}{S _ {n + p}} \right| > \frac {1}{2}.
$$

故级数发散.

(iii) 当  $\alpha < 0$  时, 注意到

$$
\frac {a _ {n}}{S _ {n} ^ {1 + \alpha}} = \frac {a _ {n}}{S _ {n}} \cdot S _ {n} ^ {- \alpha}.
$$

由 $S_{n}\rightarrow +\infty (n\to +\infty)$ 且 $\alpha < 0$ ，知，存在 $N > 0$ ，使得当 $n > N$ 时， $S_{n}^{-\alpha} > 2.$ 因此，当 $n > N$ 时， $\frac{a_n}{S_n^{1 + \alpha}} >2\frac{a_n}{S_n}$ 根据比较判别法知，原级数发散. □

作为 Abel-Dini 定理的一个具体案例, 有下面的结论:

例 11.2.15 (1) 若正项级数  $\sum_{n=1}^{+\infty}a_{n}$  收敛,

$$
b _ {n} = \sqrt {T _ {n}} - \sqrt {T _ {n + 1}} = \sqrt {\sum_ {k = n} ^ {+ \infty} a _ {k}} - \sqrt {\sum_ {k = n + 1} ^ {+ \infty} a _ {k}},
$$

则级数 $\sum_{n=1}^{+\infty} b_n$ 是收敛得比 $\sum_{n=1}^{+\infty} a_n$ 慢的收敛级数.

(2) 若正项级数  $\sum_{n=1}^{+\infty}a_{n}$  发散,

$$
c _ {n} = \sqrt {S _ {n + 1}} - \sqrt {S _ {n}} = \sqrt {\sum_ {k = 1} ^ {n + 1} a _ {k}} - \sqrt {\sum_ {k = 1} ^ {n} a _ {k}},
$$

则级数  $\sum_{n=1}^{+\infty}c_{n}$  是发散得比  $\sum_{n=1}^{+\infty}a_{n}$  慢的发散级数.

证明 例子中的级数相当于定理中 $\alpha = -\frac{1}{2}$ 的情况, 对于这种特殊情况, 可以用下面更直接的方法验证:

(1) $\sum_{k = 1}^{n}b_{k} = \sqrt{T_{1}} -\sqrt{T_{n + 1}} <   \sqrt{T_{1}} = \sqrt{\sum_{n = 1}^{+\infty}a_{n}},$

而且

$$
\frac {a _ {n}}{b _ {n}} = \frac {T _ {n} - T _ {n + 1}}{\sqrt {T _ {n}} - \sqrt {T _ {n + 1}}} = \sqrt {T _ {n}} + \sqrt {T _ {n + 1}} \rightarrow 0 \quad (n \rightarrow + \infty)
$$

结论 (2) 的证明完全类似于 (1) 的思路, 证略.

注11.2.9 前面我们讨论了以几何级数、 $p$-级数、 $\frac{1}{n\ln n}$ 为对标级数，得到的几种重要的判别方法，而Abel-Dini定理告诉我们:任何收敛级数都不可能作为万能的对标级数.换句话说，我们总能找到一些级数，它们的敛散性判别不能以给定的级数为对标级数.

## 习题 11.2

1. 举例说明, 当 $\lim_{n\to +\infty}\sqrt[n]{a_n} = 1$ 时, 正项级数 $\sum_{n=0}^{+\infty} a_n$ 既可能收敛也可能发散.

2. 设  $a_{1} \geqslant a_{2} \geqslant a_{3} \geqslant \cdots \geqslant 0$ . 证明: 若  $\sum_{n=1}^{+\infty} a_{n}$  收敛, 则  $\lim_{n \to +\infty} na_{n} = 0$ .

3. (1) 设 $\{a_{n}\}$ 单调递减趋于零, 级数 $\sum_{n=0}^{+\infty} a_{n}$ 发散, 证明: 级数 $\sum_{n=1}^{+\infty} \min \left\{a_{n}, \frac{1}{n}\right\}$ 也发散.

(2) 设  $\{a_{n}\}$  和  $\{b_{n}\}$  均单调递减趋于零，级数  $\sum_{n=0}^{+\infty}a_{n}$  和  $\sum_{n=0}^{+\infty}b_{n}$  均发散，问级数

$\sum_{n=0}^{+\infty}\min\{a_n,b_n\}$ 的敛散性如何？

4. 问是否存在收敛的正项级数, 使得它有无限多项满足条件 $a_{n_k} \geqslant \frac{1}{n_k}$?
5. 设正项级数  $\sum_{n=1}^{+\infty}\dot{a}_{n}$  收敛,  $\lim_{n\to+\infty}na_{n}=a$ . 证明: a=0.
6. 讨论以下级数的敛散性:

$$
\left(\frac {1}{2}\right) ^ {p} + \left(\frac {1 \times 3}{2 \times 4}\right) ^ {p} + \left(\frac {1 \times 3 \times 5}{2 \times 4 \times 6}\right) ^ {p} + \dots .
$$

7. 设  $\alpha > 0$  为一常数, 试研究下面数列当 n 趋于无穷时的阶:

$$
\left\{\frac {1}{1 + \alpha} \times \frac {2}{2 + \alpha} \times \dots \times \frac {n}{n + \alpha} \right\} _ {n = 1} ^ {+ \infty}.
$$

8. 研究级数  $\sum_{n=10}^{+\infty}\frac{1}{n^{p}(\ln n)^{q}(\ln\ln n)^{r}}$  的敛散性, 其中 p, q, r 为实数.
9. 设 $\{a_{n}\}_{n=1}^{+\infty}$ 是单调递减的正项数列, $\sum_{n=1}^{+\infty} a_{n}$ 发散. 证明: $\sum_{n=1}^{+\infty} a_{n} \mathrm{e}^{-\frac{a_{n}}{a_{n+1}}}$ 也发散.

10. 研究下列级数的敛散性:

(1) $\sum_{n=10}^{+\infty} \frac{1}{n^{1+\frac{1}{\ln \ln n}}}$;
(2) $\sum_{n=10}^{+\infty} \frac{1}{n^{1 + \frac{\ln \ln n}{\ln n}}}$;
(3) $\sum_{n=10}^{+\infty} \frac{1}{n^{1+2\frac{\ln \ln n}{\ln n}}}$;
(4) $\sum_{n=10}^{+\infty} \frac{1}{(\ln n)^{\ln n}}$;
(5) $\sum_{n=10}^{+\infty} \frac{1}{(\ln n)^{\ln \ln n}}$;
(6) $\sum_{n=10}^{+\infty} \frac{1}{(\ln \ln n)^{\ln n}}$;
(7) $\sum_{n=10}^{+\infty} \frac{1}{a^{\ln n}}, \quad a > 1;$
(8) $\sum_{n=1}^{+\infty} \frac{1}{n^{\sqrt[n]{n}}}.$

11. 判断下列级数的敛散性:

(1) $\sum_{n=1}^{+\infty} \frac{1}{\sqrt{n + n^2}}$;
(2) $\sum_{n=1}^{+\infty} 2^n \sin \frac{\pi}{3n}$;
(3) $\sum_{n=1}^{+\infty}\left(1 - \cos\frac{1}{n}\right)$;
(4) $\sum_{n=1}^{+\infty} \frac{1}{n} \tan \frac{1}{n}$;
(5) $\sum_{n=1}^{+\infty} \frac{1}{\sqrt{n^3 + 1}}$;
(6) $\sum_{n=1}^{+\infty} \frac{\ln n}{n^p}$.

12. 判断下列级数的敛散性:

(1) $\sum_{n=1}^{+\infty} \frac{(2n-1)!!}{n!}$;

(2) $\sum_{n=1}^{+\infty} \frac{n!}{n^n}$;

(3) $\sum_{n=1}^{+\infty} \frac{n^2}{2^n}$;

(4) $\sum_{n=1}^{+\infty}\left(\sqrt[n]{a-1}\right)^{p}(a>1)$;

(5) $\sum_{n=1}^{+\infty}\left(1-n\sin\frac{1}{n}\right)^p$;

(6) $\sum_{n=1}^{+\infty}\left(\frac{n}{2n+1}\right)^{n}$.

13. 设 $a_{n} > 0, \sum_{n=1}^{+\infty} a_{n}$ 收敛. 证明:

(1) $\sum_{n=1}^{+\infty}a_{n}^{1-\frac{1}{kn+1}}$ 收敛, 其中 k>0.

(2) 若 $b_{n}$ 满足 $b_{n} \ln n \to 0 (n \to +\infty)$, 证明: $\sum_{n=1}^{+\infty} a_{n}^{1 - b_{n}}$ 收敛.

14. 证明: $\sum_{n=2}^{+\infty} \frac{1}{n^{1+\frac{1}{\ln n}}}$ 发散, $\sum_{n=2}^{+\infty} \frac{1}{n^{1+\frac{1}{\sqrt{\ln n}}}}$ 收敛, $\sum_{n=1}^{+\infty} \frac{1}{n^{1+|\sin n|}}$ 发散.

15. 证明: 调和级数中去掉所有的合数项, 剩下的质数的倒数和仍然发散, 即, 设 $p_1, p_2, \cdots$ 为由质数形成的单调上升数列. 证明: 级数 $\sum_{n=1}^{+\infty} \frac{1}{p_n}$ 发散.

16. 证明: 调和级数中去掉所有含有数字 9 的项, 剩下的和收敛, 即, 设 $A$ 是自然数集合的子集

$$
A = \{n \in \mathbb {N} _ {+} \mid n \text {的十进制表示中不含数字} 9 \},
$$

则级数  $\sum_{n\in A}\frac{1}{n}$  收敛;

17. 证明: (1) 设 $A$ 是自然数集合的子集

$$
A = \{n \in \mathbb {N} _ {+} \mid n \text {的十进制表示中不含字串} 9 9 \},
$$

则级数  $\sum_{n\in A}\frac{1}{n}$  收敛.

(2) 设 $\alpha$ 是一个由给定的数字组成的字串, 比如 $\alpha = 123456789$, $A$ 是自然数集合的子集

$$
A = \{n \in \mathbb {N} _ {+} \mid n \text {的十进制表示中不含字串} \alpha \},
$$

则级数  $\sum_{n\in A}\frac{1}{n}$  收敛.

18. 考虑级数 $\sum_{n=1}^{+\infty} \frac{(n-1)!n!4^n}{(2n)!\sqrt{n}}$ 和 $\sum_{n=1}^{+\infty} \frac{n!(n+1)!4^{n+1}}{(2n+2)!\sqrt{n+1}}$, 可以看出后者通项是前者通项向左平移一位后得到的级数, 因此两者应该有相同的敛散性. 但如果利用 Raabe判别法的普通形式, 可以得到对前者判别法失效而后者发散. 试通过此例分析并证明 Raabe 判别法有下面的推论:

设  $\sum_{n=1}^{+\infty}a_{n}$  为正项级数. 若存在  $\ell>0$ , 当 n 充分大时, 有  $(n-\ell)\left(\frac{a_{n}}{a_{n+1}}-1\right)\leqslant1$ ,
则级数  $\sum_{n=1}^{+\infty}a_{n}$  发散.

19. 设 $\sum_{n=1}^{+\infty} a_n$ 为正项级数, 常数 $\lambda > 0$. 记

$$
r _ {n, 1} = \ln (\lambda n) \left(\frac {a _ {n}}{a _ {2 n}} - 2\right), \quad r _ {n, 2} = \ln (\lambda n) \left(\frac {a _ {n}}{a _ {2 n + 1}} - 2\right),
$$

$$
\bar {r} = \max \left\{\varlimsup_ {n \to + \infty} r _ {n, 1}, \varlimsup_ {n \to + \infty} r _ {n, 2} \right\}, \quad \underline {{r}} = \min \left\{\varliminf_ {n \to + \infty} r _ {n, 1}, \varliminf_ {n \to + \infty} r _ {n, 2} \right\}.
$$

证明:

(1) 当  $\underline{r} > 2 \ln 2$  时, 级数  $\sum_{n=1}^{+\infty} a_{n}$  收敛.
(2) 当  $\bar{r} < 2 \ln 2$  时, 级数  $\sum_{n=1}^{+\infty} a_{n}$  发散.
(3) 当  $\underline{r} \leqslant 2 \ln 2 \leqslant \bar{r}$  时, 判别法失效.

20. 试给出无穷限积分相应的 Abel-Dini 定理.

21. 设 $a_{n} > 0, \sum_{n=1}^{+\infty} a_{n}$ 收敛. 证明: 级数 $\sum_{n=1}^{+\infty} H_{n}, \quad \sum_{n=1}^{+\infty} A_{n}$ 和 $\sum_{n=1}^{+\infty} G_{n}$ 均收敛, 其中

$$
H _ {n} = \frac {1}{\frac {1}{a _ {1}} + \frac {1}{a _ {2}} + \cdots + \frac {1}{a _ {n}}}, \quad A _ {n} = \frac {1}{n} (a _ {1} + a _ {2} + \dots + a _ {n}), \quad G _ {n} = \sqrt [ n ]{a _ {1} a _ {2} \cdots a _ {n}}.
$$

22. 证明: 不可能存在严格正项数列 $\{a_{n}\}$ 使得级数 $\sum_{n=1}^{+\infty} a_{n}$ 与 $\sum_{n=1}^{+\infty} \frac{1}{n^{2} a_{n}}$ 同时收敛.
23. 设 $\alpha > 0$, 证明: 存在严格正项数列 $\{a_{n}\}$ 使得级数 $\sum_{n=1}^{+\infty} a_{n}$ 与 $\sum_{n=1}^{+\infty} \frac{1}{n^{2 + \alpha} a_{n}}$ 同时收敛.
24. 设 $\alpha > 0$, 证明: 存在严格正项数列 $\{a_{n}\}$ 使得级数 $\sum_{n=1}^{+\infty} a_{n}$ 与 $\sum_{n=2}^{+\infty} \frac{1}{n^{2} (\ln^{2 + \alpha} n) a_{n}}$ 同时收敛.
25. 设严格正项级数  $\sum_{n=1}^{+\infty} a_{n}$  收敛,  $\alpha > 0$ , 问下面哪些级数有可能收敛, 哪些级数一

定发散?

$$
\sum_ {n = 1} ^ {+ \infty} \frac {1}{n ^ {2} a _ {n}}; \quad \sum_ {n = 2} ^ {+ \infty} \frac {1}{(n ^ {2} \ln^ {2} n) a _ {n}}; \quad \sum_ {n = 1} ^ {+ \infty} \frac {1}{n ^ {2 + \alpha} a _ {n}}; \quad \sum_ {n = 2} ^ {+ \infty} \frac {1}{(n ^ {2} \ln^ {2 + \alpha} n) a _ {n}}.
$$

26. 证明: (1) 设正项数列 $\{a_{n}\}$ 单调下降, 则

$$
\lim _ {n \to + \infty} a _ {n} = 0 \Longleftrightarrow \sum_ {n = 1} ^ {+ \infty} \left(1 - \frac {a _ {n + 1}}{a _ {n}}\right) \mathrm{发散}.
$$

(2) 设正项数列 $\{a_{n}\}$ 单调上升, 则 $\{a_{n}\}$ 与 $\sum_{n=1}^{+\infty}\left(1 - \frac{a_n}{a_{n+1}}\right)$ 同敛散, 即 $\{a_{n}\}$ 有上界时, 该级数收敛, 无上界时发散.

(3) 设 $\{S_n\}$ 为正项级数 $\Sigma a_{n}$ 的部分和数列, 则 $\sum_{n=1}^{+\infty} a_{n}$ 与 $\sum_{n=1}^{+\infty} \frac{a_{n}}{S_{n}}$ 同敛散.

27. (Gauss 判别法) 证明: 设 $\sum_{n=1}^{+\infty} a_n$ 为一正项级数. 存在常数 $r, p > 0$ 使得

$$
\frac {a _ {n}}{a _ {n + 1}} = \frac {1}{r} + \frac {p}{n} + O \left(\frac {1}{n ^ {2}}\right).
$$

(1) 若 r < 1, 则级数  $\sum_{n=1}^{+\infty} a_{n}$  收敛, 与 p 的值无关.
(2) 若 r > 1, 则级数  $\sum_{n=1}^{+\infty} a_{n}$  发散, 与 p 的值无关.
(3) 若 r = 1, 则级数的收敛性与 p 的值有关.
(i) 当 p > 1 时, 级数  $\sum_{n=1}^{+\infty} a_{n}$  收敛.
(ii) 当  $p \leqslant 1$  时, 级数  $\sum_{n=1}^{+\infty} a_{n}$  发散.

28. 试讨论下面几何级数的敛散性, 其中 $\alpha, \beta, \gamma, x$ 均为正数:

$$
F (\alpha , \beta , \gamma , x) = 1 + \sum_ {n = 1} ^ {+ \infty} \frac {\alpha (\alpha + 1) \cdots (\alpha + n - 1) \beta (\beta + 1) \cdots (\beta + n - 1)}{n ! \gamma (\gamma + 1) \cdots (\gamma + n - 1)} x ^ {n}.
$$

29. 设 $\Sigma a_{n}$ 是一个发散的正项级数, 考虑以下级数的敛散性:

(1) $\Sigma \frac{a_n}{1 + a_n}$;

(2) $\Sigma \frac{a_n}{1 + n^2 a_n}$;

(3) $\Sigma \frac{a_n}{1 + a_n^2}$;

(4) $\Sigma \frac{a_n}{1 + na_n}$.

## 11.3 任意项级数

所谓任意项级数, 也称一般项级数, 是指其通项可正可负的级数. 任意项级数的敛散性也是通过部分和序列极限的存在性来定义的, 但一般来说, 它们敛散性的判定要比正项级数敛散性的判定困难得多. 尽管如此, 其中有一类所谓的绝对收敛的级数, 其收敛性可以通过正项级数收敛性判别法得到. 而且一般来说, 绝对收敛的级数具有较好的代数性质. 为此, 我们先引入定义:

定义11.3.1 若级数 $\sum_{n=1}^{+\infty}|a_n|$ 收敛, 则称级数 $\sum_{n=1}^{+\infty}a_n$ 绝对收敛.

若级数  $\sum_{n=1}^{+\infty}a_{n}$  收敛, 而  $\sum_{n=1}^{+\infty}|a_{n}|$  发散, 则称级数  $\sum_{n=1}^{+\infty}a_{n}$  条件收敛.

需要注意的是收敛、条件收敛和绝对收敛是三个概念, 当我们泛泛地说一个级数收敛时, 通常是指该级数已经收敛了, 但它是条件收敛还是绝对收敛并不明确. 绝对收敛的级数一定不是条件收敛的, 反之, 条件收敛的级数也一定不是绝对收敛的.

下面的结论在讨论任意项级数时格外重要.

定理 11.3.1 绝对收敛的级数一定收敛.

证明 由 Cauchy 准则及不等式 $|a_{n+1} + \cdots + a_{n+p}| \leqslant |a_{n+1}| + \cdots + |a_{n+p}|$ 可得. □

根据定理 11.3.1, 要讨论一个任意项级数的敛散性, 通常可按以下步骤来判断. 一是看通项是否趋于零, 若通项趋于零, 则看它是否绝对收敛, 因为这时我们可以应用前面正项级数的各种判别法; 如果级数绝对收敛, 自然也就收敛. 如果不然, 则需要更细腻的判别方法, 而这正是我们本节讨论的重点.

例 11.3.1 容易证明级数  $\sum_{n=1}^{+\infty}\frac{(-1)^{n}}{n^{2}}$  和  $\sum_{n=1}^{+\infty}\frac{\sin^{3}n}{n\sqrt{n}}$  均收敛, 这是因为两者均绝对收敛.

## 11.3.1 交错级数的敛散性

在任意项级数中, 有一类特殊的任意项级数, 即所谓的交错级数. 形如  $\sum_{n=1}^{+\infty}(-1)^{n+1}a_{n}$ , 其中  $a_{n}>0\ (n=1,2,\cdots)$ , 的级数称为交错级数. 交错级数最显著的特点是其通项正负交错出现. 我们先给出关于交错级数的 Leibniz 定理:

定理 11.3.2 (Leibniz 交错判别法) 设数列 $\{a_{n}\}$ 是单调且趋于零的, 则级数 $\sum_{n=1}^{+\infty}(-1)^{n+1}a_{n}$ 收敛.

证明 不妨设 $a_{n}$ 单调递减趋于零, 从而必有 $a_{n} > 0$. 我们考虑该级数的部分和数列的子列 $\{S_{2n}\}$ 和 $\{S_{2n+1}\}$:

一方面, 我们有

$$
S _ {2 (n + 1)} - S _ {2 n} = a _ {2 n + 1} - a _ {2 n + 2} \geqslant 0,
$$

即  $\{S_{2n}\}$  单调上升. 另一方面,

$$
\begin{array}{l} S _ {2 n} = a _ {1} - a _ {2} + a _ {3} - \dots - a _ {2 n - 2} + a _ {2 n - 1} - a _ {2 n} \\ = a _ {1} - (a _ {2} - a _ {3}) - \dots - (a _ {2 n - 2} - a _ {2 n - 1}) - a _ {2 n} \\ \leqslant a _ {1}, \\ \end{array}
$$

所以  $\{S_{2n}\}$  有上界, 故  $\{S_{2n}\}$  有极限  $\ell_{1}$ .

同理, 一方面, 我们有

$$
S _ {2 n + 3} - S _ {2 n + 1} = a _ {2 n + 3} - a _ {2 n + 2} \leqslant 0,
$$

即  $\{S_{2n+1}\}$  单调下降. 另一方面,

$$
\begin{array}{l} S _ {2 n + 1} = a _ {1} - a _ {2} + \dots + a _ {2 n - 1} - a _ {2 n} + a _ {2 n + 1} \\ = (a _ {1} - a _ {2}) + \dots + (a _ {2 n - 1} - a _ {2 n}) + a _ {2 n + 1} \\ \geqslant a _ {2 n + 1}, \\ \end{array}
$$

所以  $\{S_{2n+1}\}$  有下界, 故  $\{S_{2n+1}\}$  有极限  $\ell_{2}$ . 由于

$$
S _ {2 n + 1} - S _ {2 n} = a _ {2 n + 1} \rightarrow 0 \quad (n \rightarrow + \infty),
$$

所以  $\ell_{1}=\ell_{2}$ . 因此级数的部分和数列  $\{S_{n}\}$  收敛, 故原级数收敛.

例 11.3.2 我们知道级数

$$
\sum_ {n = 1} ^ {+ \infty} \frac {1}{n}, \quad \sum_ {n = 1} ^ {+ \infty} \frac {1}{\sqrt {n}}, \quad \sum_ {n = 2} ^ {+ \infty} \frac {1}{\ln n}, \quad \sum_ {n = 3} ^ {+ \infty} \frac {1}{\ln \ln n}
$$

均发散, 但根据 Leibniz 交错判别法知它们对应的交错级数

$$
\sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n}}{n}, \quad \sum_ {n = 1} ^ {+ \infty} \frac {(- 1) ^ {n}}{\sqrt {n}}, \quad \sum_ {n = 2} ^ {+ \infty} \frac {(- 1) ^ {n}}{\ln n}, \quad \sum_ {n = 3} ^ {+ \infty} \frac {(- 1) ^ {n}}{\ln \ln n}
$$

均收敛, 即这四个级数均为条件收敛级数.

从这些例子可以得到某种直观认识: 即使交错级数通项趋于零的速度远比正项级数通项趋于零的速度慢, 仍然有可能收敛.

注 11.3.1 如果交错级数通项趋于零, 但不单调, 则结论不成立. 比如级数

$$
1 - \frac {1}{2} + \frac {1}{3 ^ {2}} - \frac {1}{4} + \frac {1}{5 ^ {2}} - \frac {1}{6} + \frac {1}{7 ^ {2}} - \dots
$$

是交错级数, 通项趋于 0, 但发散.

事实上, 此例很容易一般化: 选两个正项级数, 级数 $\sum_{n=1}^{+\infty} a_n$ 收敛, 级数 $\sum_{n=1}^{+\infty} b_n$ 通项趋于 0 但发散, 则交错级数 $a_1 - b_1 + a_2 - b_2 + \cdots$ 通项趋于 0 且一定发散.

例11.3.3 试讨论交错级数 $\sum_{n=2}^{+\infty} \frac{(-1)^n}{\sqrt{n} + (-1)^n}$ 的敛散性.

解 记 $a_{n} = \frac{(-1)^{n}}{\sqrt{n}}, b_{n} = \frac{(-1)^{n}}{\sqrt{n} + (-1)^{n}}, c_{n} := a_{n} - b_{n} = \frac{1}{n + (-1)^{n}\sqrt{n}}$, 可以看出级数 $\sum_{n=2}^{+\infty} c_{n}$ 发散. 注意到级数 $\sum_{n=2}^{+\infty} a_{n}$ 收敛, 知原级数 $\sum_{n=2}^{+\infty} b_{n}$ 发散.

注意到当  $n \rightarrow +\infty$  时,  $a_{n}$  与  $b_{n}$  是等价无穷小, 但以它们为通项的交错级数的敛散性完全不同, 因此本例告诉我们, 在讨论任意项级数敛散性时, 利用等价无穷小代换判断敛散性需要格外小心!

## 11.3.2 Abel 变换、Abel 判别法和 Dirichlet 判别法

在讨论广义积分收敛时, 我们曾经介绍过 Abel 判别法和 Dirichlet 判别法 (简称 A-D 判别法), 这是两个针对形如 $\int_{I} f(x) g(x) \mathrm{d}x$ (其中 $I$ 可以是无穷限区间或者是有界闭区间时 $f(x) g(x)$ 有瑕点) 的广义积分敛散性的判别法. 类似于广义积分, 在考虑形如 $\sum_{n=1}^{+\infty} a_n b_n$ 的任意项级数敛散性时, 也有相应的 A-D 判别法.

A-D 判别法是分析学中两种基本的技术手法, 有着广泛的应用. 事实上, 在后续章节内容中, 我们还会多次遇到这两种判别法. A-D 判别法虽然是两种不同的表现形式, 但它们本质上遵循着同一种基本思想. 具体来说, 就是在研究形如 $\sum_{n=1}^{+\infty} a_n b_n$ 或 $\int_I f(x) g(x) \mathrm{d}x$ 的敛散性时, 两个因子乘积的效果决定了它们的敛散性: 因此, 如果两因子是强强搭配, 则级数或广义积分可以收敛, 甚至绝对收敛; 但如果是强弱搭配, 则需要考虑两者间的协调问题. 形象地说, 当一个因子条件较强, 另一因子条件则可以适当放宽. 反之亦然, 此时仍有可能收敛或条件收敛; 当两者条件都比较弱时, 一般来说需要考虑两者间特殊的搭配, 此时也许能得到某种弱形式下的性质.

A-D 判别法均源于 Abel 变换, 后者逐渐演变成一种基本手法和思想. Abel 变换朴素的改变求和方式的直观做法对 Lebesgue 积分的诞生等诸多领域都有直接的影响. 在前面定积分章节证明积分第二中值定理时, 也有不少参考书中将 Abel 变换的手法应用到相应的 Riemann 和上. 下面我们再简单介绍一下 Abel 变换.

## 1. Abel 变换

定理 11.3.3 (Abel 变换) 设  $a_{1}, a_{2}, \cdots, a_{n}$  和  $b_{1}, b_{2}, \cdots, b_{n}$  为两组给定的实数，则有

$$
\sum_ {i = 1} ^ {n} a _ {i} b _ {i} = \sum_ {i = 1} ^ {n - 1} \left(a _ {i} - a _ {i + 1}\right) B _ {i} + a _ {n} B _ {n}, \tag {11.3.1}
$$

其中  $B_{i}=b_{1}+b_{2}+\cdots+b_{i},\quad i=1,2,\cdots,n.$

证法1 为方便起见, 记 $B_{0} = 0$. 由 $b_{i} = B_{i} - B_{i-1}$, 于是有

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} a _ {i} b _ {i} = \sum_ {i = 1} ^ {n} a _ {i} (B _ {i} - B _ {i - 1}) = \sum_ {i = 1} ^ {n} a _ {i} B _ {i} - \sum_ {i = 1} ^ {n} a _ {i} B _ {i - 1} \\ = \sum_ {i = 1} ^ {n} a _ {i} B _ {i} - \sum_ {i = 0} ^ {n - 1} a _ {i + 1} B _ {i} = \sum_ {i = 1} ^ {n - 1} (a _ {i} - a _ {i + 1}) B _ {i} + a _ {n} B _ {n}. \\ \end{array}
$$

Abel 变换的正确性可以通过逻辑直接验证, 然后它的几何直观性更值得体会和思考. 图 11.1 是 Abel 变换的一个示意图 (为方便起见, 我们假设  $a_{1} > a_{2} > \cdots > a_{n} > 0$ ,  $b_{i} > 0$ . 这些假设丝毫不影响 Abel 变换的基本思想).

可以看出, Abel 变换 (11.3.1) 的两端恰恰对应的是计算图中阴影部分面积的两种模式.

证法 2 我们给出 Abel 变换的一种代数处理: 分别把  $a_{1}, a_{2}, \cdots, a_{n}$  和  $b_{1}, b_{2}, \cdots, b_{n}$  看成两个 n 维向量,

$$
\boldsymbol {\alpha} _ {0} = (a _ {1}, a _ {2}, \dots , a _ {n}), \quad \boldsymbol {\beta} _ {0} = (b _ {1}, b _ {2}, \dots , b _ {n}).
$$

则方程 (11.3.1) 的左端即为 $\alpha_0$ 和 $\beta_0$ 的内积, 即

$$
\sum_ {i = 1} ^ {n} a _ {i} b _ {i} = (\boldsymbol {\alpha} _ {0}, \boldsymbol {\beta} _ {0}).
$$

任取一个 $n \times n$ 非奇异矩阵 $\pmb{M}$, 记 $\pmb{M}^{-1}$ 为其逆. 则有

$$
\left(\boldsymbol {\alpha} _ {0}, \boldsymbol {\beta} _ {0}\right) = \left(\boldsymbol {\alpha} _ {0} \boldsymbol {M}, \boldsymbol {\beta} _ {0} (\boldsymbol {M} ^ {- 1}) ^ {\mathrm{T}}\right) = \left(\boldsymbol {\alpha} _ {1}, \boldsymbol {\beta} _ {1}\right),
$$

其中 $\alpha_{1} = \alpha_{0}M, \beta_{1} = \beta_{0}(M^{-1})^{\mathrm{T}}, (M^{-1})^{\mathrm{T}}$ 是 $M^{-1}$ 的转置.

![](images/page_411_chart_2.jpg)

<details>
<summary>bar</summary>

| Interval | Value |
| --- | --- |
| 1 | a1 |
| 2 | a2 |
| 3 | a3 |
| 4 | a4 |
| 5 | a5 |
</details>

(a) Abel 变换示意图，等式 (11.3.1) 左端

![](images/page_411_chart_4.jpg)

<details>
<summary>area</summary>

| Level | Difference \((\Delta a_k)\) |
| --- | --- |
| B_1 | \(\Delta a_1\) |
| B_2 | \(\Delta a_2\) |
| B_3 | \(\Delta a_3\) |
| B_4 | \(\Delta a_4\) |
| B_5 | a_5 |
</details>

(b) Abel 变换示意图，等式 (11.3.1) 右端

图11.1

直接验证, 选取下面的矩阵 M, 即可得到经典的 Abel 变换 (11.3.1).

$$
M = \left( \begin{array}{c c c c c} 1 & 0 & 0 & \dots & 0 \\ - 1 & 1 & 0 & \dots & 0 \\ 0 & - 1 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & - 1 & 1 \end{array} \right), \quad M ^ {- 1} = \left( \begin{array}{c c c c c} 1 & 0 & 0 & \dots & 0 \\ 1 & 1 & 0 & \dots & 0 \\ 1 & 1 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 1 & 1 & 1 & 1 & 1 \end{array} \right).
$$

事实上, 可以看出 (注意, 我们已约定  $a_{n+1}=0$ ):

$$
\begin{array}{l} \boldsymbol {\alpha} _ {1} = \boldsymbol {\alpha} _ {0} \boldsymbol {M} = (a _ {1} - a _ {2}, a _ {2} - a _ {3}, \dots , a _ {n - 1} - a _ {n}, a _ {n}) \\ = (\Delta a _ {1}, \Delta a _ {2}, \dots , \Delta a _ {n}). \\ \boldsymbol {\beta} _ {1} = \boldsymbol {\beta} _ {0} (\boldsymbol {M} ^ {- 1}) ^ {\mathrm{T}} = (b _ {1}, b _ {1} + b _ {2}, \dots , b _ {1} + \dots + b _ {n}) \\ = (B _ {1}, B _ {2}, \dots , B _ {n}). \\ \end{array}
$$

$$
\begin{array}{l} \boldsymbol {\beta} _ {1} = \boldsymbol {\beta} _ {0} (\boldsymbol {M} ^ {- 1}) ^ {\mathrm{T}} = (b _ {1}, b _ {1} + b _ {2}, \dots , b _ {1} + \dots + b _ {n}) \\ = (B _ {1}, B _ {2}, \dots , B _ {n}). \\ \end{array}
$$

从而 $(\alpha_{1},\beta_{1})$ 刚好给出了关系式(11.3.1)的右端.

![](images/page_411_image_13.jpg)

上述证明给我们提供了一种更灵活和方便的代数手法, 是进一步深刻理解 Abel 变换的新的角度. 可以看到, 由于矩阵 M 的选取具有极大的自由度, 因此, 我们可以很容易通过选取 M 而将经典的 Abel 变换推广到非常一般的场景. 另外, 这一手法还为我们引入二阶、三阶等高阶 Abel 变换提供了可能.

比如我们可以很自然地引入二阶 Abel 变换:

$$
\left(\boldsymbol {\alpha} _ {0}, \boldsymbol {\beta} _ {0}\right) = \left(\boldsymbol {\alpha} _ {0} \boldsymbol {M} ^ {2}, \boldsymbol {\beta} _ {0} (\boldsymbol {M} ^ {- 2}) ^ {\mathrm{T}}\right) = \left(\boldsymbol {\alpha} _ {2}, \boldsymbol {\beta} _ {2}\right),
$$

其中  $\alpha_{2}=\alpha_{0}M^{2},\beta_{2}=\beta_{0}(M^{-2})^{\mathrm{T}}.$

$$
M ^ {2} = \left( \begin{array}{c c c c c c} 1 & 0 & 0 & \dots & 0 & 0 \\ - 2 & 1 & 0 & \dots & 0 & 0 \\ 1 & - 2 & 1 & \dots & 0 & 0 \\ 0 & 1 & - 2 & \dots & 0 & 0 \\ \vdots & \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 1 & 0 \\ 0 & 0 & 0 & \dots & - 2 & 1 \end{array} \right),
$$

$$
M ^ {- 2} = \left( \begin{array}{c c c c c} 1 & 0 & 0 & \dots & 0 \\ 2 & 1 & 0 & \dots & 0 \\ 3 & 2 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ n & n - 1 & n - 2 & \dots & 1 \end{array} \right).
$$

可以看出, 内积 $(\alpha_{2}, \beta_{2})$ 刚好给出了等式 (11.3.1) 中的右端.

## 2. Abel 判别法和 Dirichlet 判别法

由 Abel 变换, 易得如下判别法.

定理 11.3.4 (Abel 判别法、Dirichlet 判别法) 设级数  $\sum_{n=1}^{+\infty} a_{n}$  的部分和  $\{S_{n}\}$

有界, 数列 $\{b_n\}$ 单调有界. 则下面两条件之一满足时, 必有级数 $\sum_{n=1}^{+\infty} a_n b_n$ 收敛.

(1) (Abel 判别法) 如果 $\{S_n\}$ 收敛, 则 $\sum_{n=1}^{+\infty} a_n b_n$ 收敛.
(2) (Dirichlet 判别法) 如果 $\{b_n\}$ 收敛到零, 则 $\sum_{n=1}^{+\infty} a_n b_n$ 收敛.

证明 由 Abel 变换, 对于  $m > n \geqslant 1$ ,

$$
\sum_ {k = n + 1} ^ {m} a _ {k} b _ {k} = (S _ {m} - S _ {n}) b _ {m} + \sum_ {k = n + 1} ^ {m - 1} (S _ {k} - S _ {n}) (b _ {k} - b _ {k + 1}).
$$

故当 $\{b_n\}$ 单调时, 对于 $m > n \geqslant N \geqslant 1$, 有

$$
\begin{array}{l} \left| \sum_ {k = n + 1} ^ {m} a _ {k} b _ {k} \right| \leqslant \left(| b _ {m} | + \sum_ {k = n + 1} ^ {m - 1} | b _ {k} - b _ {k + 1} |\right) \sup _ {k, j \geqslant N} | S _ {k} - S _ {j} | \\ \leqslant \left(| b _ {m} | + | b _ {n + 1} - b _ {m} |\right) \sup _ {k, j \geqslant N} | S _ {k} - S _ {j} | \tag {11.3.2} \\ \leqslant 3 \sup _ {k \geqslant N} \left| b _ {k} \right| \cdot \sup _ {k, j \geqslant N} \left| S _ {k} - S _ {j} \right|. \\ \end{array}
$$

根据假设, 由 $\{S_n\}, \{b_n\}$ 的有界性, 无论是 $\{S_n\}$ 收敛还是 $\{b_n\}$ 收敛到 0, 均可推得

$$
\lim _ {N \to + \infty} \sup _ {m, n \geqslant N} \left| \sum_ {k = n + 1} ^ {m} a _ {k} b _ {k} \right| = 0.
$$

从而由 Cauchy 准则,  $\sum_{n=1}^{+\infty}a_{n}b_{n}$  收敛.

![](images/page_413_image_7.jpg)

可以看出关于交错级数的 Leibniz 定理 11.3.2 是 A-D 判别法的直接推论, 这只要取 $a_{n} = (-1)^{n}$ 即可. 事实上, 我们还可以有更一般的结论, 为此, 先引入一个类似于周期函数的概念:

定义11.3.2 无穷数列 $\{\lambda_n\}$ 称为周期数列, 是指存在自然数 $k$, 以及某 $n_0$, 使得 $\lambda_{n+k} = \lambda_n (n \geqslant n_0)$ 成立, 满足此性质的最小正整数 $k$ 称为该数列的周期.

$$
A := \lambda_ {n _ {0} + 1} + \lambda_ {n _ {0} + 2} + \dots + \lambda_ {n _ {0} + k}
$$

称为周期数列的周期值.

例 11.3.4 (1) 数列  $\{(-1)^{n}\}$  是一个周期为 2, 周期值为 0 的周期数列.

(2) 数列  $1, \frac{1}{2}, -2, 1, \frac{1}{2}, -2, 1, \frac{1}{2}, -2, \cdots$  是一个周期为 3，周期值为  $-\frac{1}{2}$  的周期数列。经典的 Leibniz 判别法可以重述如下:

Leibniz 定理:设  $\{a_{n}\}$  是一个周期为 2，周期值为 0 的数列， $\{b_{n}\}$  是单调且趋于零的数列，则级数  $\sum_{n=1}^{+\infty}a_{n}b_{n}$  收敛.

推论 11.3.5 (Leibniz 判别法的推广) 设数列  $\{b_{n}\}$  单调且趋于零,  $\{a_{n}\}$  是一个周期为 k, 周期值为 A 的数列.

(1) 如果 A = 0，则级数  $\sum_{n=1}^{+\infty} a_{n} b_{n}$  收敛.
(2) 如果 $A \neq 0$, 则级数 $\sum_{n=1}^{+\infty} a_n b_n$ 与 $\sum_{n=1}^{+\infty} b_n$ 同敛散.

证明 (1) 若 $A = 0$, 则显然级数 $\sum_{n=1}^{+\infty} a_n$ 的部分和总是有界的, 此时根据 Dirichlet 判别法知结论成立.

(2) 若 $A \neq 0$, 则一方面数列 $\{\tilde{a}_n\}$, $\tilde{a}_n = a_n - \frac{A}{k}$, 是一个周期为 $k$, 周期值为 0 的数列, 因此, 根据 (1), 知级数 $\sum_{n=1}^{+\infty} \tilde{a}_nb_n$ 收敛, 记其和为 $\tilde{S}$. 另一方面, 若记

$$
S _ {n} = \sum_ {i = 1} ^ {n} a _ {i} b _ {i}, \qquad B _ {n} = \sum_ {i = 1} ^ {n} b _ {i}, \qquad \tilde {S} _ {n} = \sum_ {i = 1} ^ {n} \tilde {a} _ {i} b _ {i},
$$

则有

$$
\tilde {S} _ {n} = \sum_ {i = 1} ^ {n} \left(a _ {i} - \frac {A}{k}\right) b _ {i} = S _ {n} - \frac {A}{k} B _ {n} \rightarrow \tilde {S} \quad (n \rightarrow + \infty),
$$

因此  $\{S_{n}\}$  与  $\{B_{n}\}$  同敛散.

例 11.3.5 (1) 数列 1,2,-3,1,2,-3, $\cdots$ 是一个周期为 3，周期值为 0 的数列，数列 $\{a_{n}\}$ 单调趋于 0，故级数 $\sum_{n=0}^{+\infty}(a_{3n+1}+2a_{3n+2}-3a_{3n+3})$ 收敛.

(2) 数列 1, 2, -2, 1, 2, -2, … 是一个周期为 3，周期值为 1 的数列，设  $\{a_{n}\}$  为单调趋于 0 的数列，则级数  $\sum_{n=0}^{+\infty}(a_{3n+1} + 2a_{3n+2} - 2a_{3n+3})$  与级数  $\sum_{n=1}^{+\infty}a_{n}$  同敛散.

读者可能已经注意到该推论在连续型框架下的相似表述了. 换句话说, 在讨论定积分 (广义积分) 时, 我们也有类似的结论, 而且在实际应用中, 经常遇到被积函数中含有 $\sin x, \cos x, \sin^2 x$ 等因子的场景. 在那里, 我们经常利用这些因子函数的周期性以及一个周期上的周期值是否为 0 这些性质.

作为例子, 我们仅列举下面的结果形成对比. 证明细节略.

例 11.3.6 设  $f(x)$  在  $[0, +\infty)$  上单调趋于 0,  $g(x)$  为  $(-\infty, +\infty)$  内的周期为 T 的连续函数.

(1) 若  $\int_{0}^{T} g(x) \, dx = 0$ ，则  $\int_{0}^{+\infty} f(x)g(x) \, dx$  收敛；
(2) 若  $\int_{0}^{T} g(x) \, dx \neq 0$ ，则  $\int_{0}^{+\infty} f(x) \, dx$  收敛的充要条件是  $\int_{0}^{+\infty} f(x) g(x) \, dx$  收敛.
作为特例，有下面的结论:

例 11.3.7 下面两个广义积分的结论成立:

$$
\int_ {1} ^ {+ \infty} {\frac {\sin x}{x}}   \mathrm{d} x   \text {收敛}; \qquad \int_ {1} ^ {+ \infty} {\frac {\sin^ {2} x}{x}}   \mathrm{d} x   \text {发散}.
$$

这是因为  $\sin x$  与  $\sin^{2}x$  均作为周期函数, 前者在一个周期上的积分为零, 而后者非零, 同时又有当  $x \to +\infty$  时,  $\frac{1}{x}$  单调下降趋于零.

下面我们也对 Abel 和 Dirichlet 判别法给出一些推广. 为此, 对级数 $\sum_{n=1}^{+\infty} a_n b_n$ 的部

分和作 Abel 变换, 当  $n \geqslant 2$  时, 有

$$
\sum_ {k = 1} ^ {n} a _ {k} b _ {k} = S _ {n} b _ {n} - \sum_ {k = 1} ^ {n - 1} S _ {k} \big (b _ {k + 1} - b _ {k} \big).
$$

注意到在定理 11.3.4 中, 只要数列 $\{a_{n}\}, \{b_{n}\}$ 满足 Abel 判别法的条件或 Dirichlet 判别法的条件之一, 都有 $\{S_{n}b_{n}\}$ 收敛. 另一方面, 由于 $\{S_{n}\}$ 的有界性和 $\{b_{n}\}$ 的单调有界性, 上式右端第二项成立

$$
\sum_ {k = 1} ^ {n} | S _ {k} \big (b _ {k + 1} - b _ {k} \big) | \leqslant M \sum_ {k = 1} ^ {n} | b _ {k + 1} - b _ {k} | = M | b _ {n + 1} - b _ {1} | \rightarrow | b - b _ {1} | M,
$$

其中 $b$ 为 $\{b_n\}$ 的极限, 所以级数 $\sum_{k=1}^{+\infty} S_k (b_{k+1} - b_k)$ 总是绝对收敛, 从而 $\sum_{n=1}^{+\infty} a_n b_n$ 收敛. 故我们有下面推广的 Abel 和 Dirichlet 判别法:

定理 11.3.6 设级数  $\sum_{n=1}^{+\infty}a_{n}$  的部分和有界, 数列  $\{b_{n}\}$  有界且级数  $\sum_{n=1}^{+\infty}(b_{n}-b_{n+1})$  绝对收敛.

(1) (Abel 判别法的推广) 若级数  $\sum_{n=1}^{+\infty}a_{n}$  收敛, 则级数  $\sum_{n=1}^{+\infty}a_{n}b_{n}$  收敛.
(2) (Dirichlet 判别法的推广) 若 $\{b_n\}$ 收敛到零, 则级数 $\sum_{n=1}^{+\infty} a_n b_n$ 收敛.

例 11.3.8 讨论  $\sum_{n=1}^{+\infty}\frac{\sin nx}{n^{\alpha}}$  的敛散性.

解 一方面, 显然只需考虑 $x \in [0, 2\pi)$, 另一方面, 当 $x = 0, \pi$ 时级数绝对收敛. 因此, 以下只考虑 $x \in (0, \pi) \cup (\pi, 2\pi)$.

(1)  $\alpha \leqslant 0$ : 此时不难证明通项不趋于零, 因此级数发散.
(2)  $\alpha > 1$ : 此时易见级数绝对收敛.
(3) $0 < \alpha \leqslant 1$: 此时,

$$
2 \sin \frac {x}{2} \sum_ {k = 1} ^ {n} \sin k x = \sum_ {k = 1} ^ {n} \left(\cos \frac {(2 k - 1) x}{2} - \cos \frac {(2 k + 1) x}{2}\right) = \cos \frac {x}{2} - \cos \frac {(2 n + 1) x}{2}.
$$

因此， $\left|\sum_{k=1}^{n}\sin kx\right|\leqslant\frac{1}{\left|\sin\frac{x}{2}\right|}$ ，即级数 $\sum_{n=1}^{+\infty}\sin nx$ 的部分和有界，由Dirichlet判别法知，原级数收敛。另一方面，

$$
\sum_ {n = 1} ^ {+ \infty} \left| \frac {\sin n x}{n ^ {\alpha}} \right| \geqslant \sum_ {n = 1} ^ {+ \infty} \frac {\sin^ {2} n x}{n ^ {\alpha}} = \sum_ {n = 1} ^ {+ \infty} \frac {1 - \cos 2 n x}{2 n ^ {\alpha}}.
$$

类似地可证 $\sum_{n=1}^{+\infty} \frac{\cos 2nx}{n^{\alpha}}$ 收敛, 由于 $\sum_{n=1}^{+\infty} \frac{1}{n^{\alpha}}$ 发散, 因此 $\sum_{n=1}^{+\infty} \left| \frac{\sin nx}{n^{\alpha}} \right|$ 发散. 所以原级数