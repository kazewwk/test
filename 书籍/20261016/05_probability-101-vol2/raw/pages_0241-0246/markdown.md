(此步的严格论证需要更多工作, 这里从略, 详见 [22, pp.221-222].) 特别地, 对 $(X_{t}^{x}: t \geqslant 0)$ 应用 (9.3.25) 式得

$$
\mathbf {P} (X _ {r + t} ^ {x} \in A) = \mathbf {E} [ \mathbf {P} (X _ {r + t} ^ {x} \in A | \mathcal {F} _ {r}) ] = \mathbf {E} [ P _ {t} (X _ {r} ^ {x}, A) ],
$$

即有

$$
P _ {r + t} (x, A) = \int_ {\mathbb {R}} P _ {r} (x, \mathrm{d} y) P _ {t} (y, A), \quad A \in \mathscr {B}.
$$

所以 $(P_t)_{t\geqslant 0}$ 构成 $(\mathbb{R},\mathcal{B})$ 上的马氏转移半群, 而 (9.3.25) 式说明 $(X_{t}:t\geqslant 0)$ 满足相对于流 $(\mathcal{F}_t)$ 以 $(P_t)_{t\geqslant 0}$ 为转移半群的马氏性. 利用 (9.3.23)式, 与定理8.2.12的证明类似地可以推出强马氏性成立. □

通常称连续的强马氏过程为扩散过程. 根据定理 9.3.7, 随机微分方程 (9.3.3) 的解  $(X_{t}: t \geqslant 0)$  相对于流  $(\mathcal{F}_{t})$  是具有转移半群  $(P_{t})_{t \geqslant 0}$  的扩散过程. 分别称  $\sigma$  和 b 为  $(X_{t}: t \geqslant 0)$  的扩散系数和漂移系数.

命题 9.3.8 若  $\sigma$  和 b 是有界的利普希茨函数, 则  $(P_{t})_{t\geqslant0}$  是费勒半群.

证明 因 (9.3.23) 式对于一切有界连续函数 $f$ 成立, 只需证明当 $f \in C_0(\mathbb{R})$ 时有 $P_t f \in C_0(\mathbb{R})$. 根据 (9.3.3) 式有

$$
\begin{array}{l} \mathbf {E} [ (X _ {t} ^ {x} - x) ^ {2} ] \leqslant 2 \mathbf {E} \Bigg \{\left[ \int_ {0} ^ {t} \sigma (X _ {s} ^ {x}) \mathrm{d} B _ {s} \right] ^ {2} \Bigg \} + 2 \mathbf {E} \Bigg \{\left[ \int_ {0} ^ {t} b (X _ {s} ^ {x}) \mathrm{d} s \right] ^ {2} \Bigg \} \\ \leqslant 2 \mathbf {E} \Big [ \int_ {0} ^ {t} \sigma (X _ {s} ^ {x}) ^ {2} \mathrm{d} s \Big ] + 2 t \mathbf {E} \Big [ \int_ {0} ^ {t} b (X _ {s} ^ {x}) ^ {2} \mathrm{d} s \Big ] \\ \leqslant 2 t \big (\| \sigma \| ^ {2} + t \| b \| ^ {2} \big). \\ \end{array}
$$

根据上式和马尔可夫不等式,

$$
\lim _ {r \to \infty} \sup _ {x \in \mathbb {R}} \mathbf {P} \big (| X _ {t} ^ {x} - x | > r \big) = 0.
$$

对于 $r > 0$ 有

$$
\mathbf {E} [ f (X _ {t} ^ {x}) ] \leqslant \mathbf {E} \big [ f (X _ {t} ^ {x}) 1 _ {\{| X _ {t} ^ {x} - x | \leqslant r \}} \big ] + \| f \| \mathbf {P} \big (| X _ {t} ^ {x} - x | > r \big).
$$

由上式和有界收敛定理得

$$
\operatorname * {l i m s u p} _ {| x | \to \infty} \mathbf {E} [ f (X _ {t} ^ {x}) ] \leqslant \| f \| \sup _ {x \in \mathbb {R}} \mathbf {P} \big (| X _ {t} ^ {x} - x | > r \big).
$$

再由 r > 0 的任意性,

$$
\lim _ {| x | \to \infty} P _ {t} f (x) = \lim _ {| x | \to \infty} \mathbf {E} [ f (X _ {t} ^ {x}) ] = 0.
$$

因此有 $P_{t}f\in C_{0}(\mathbb{R})$ □

## \*9.3.4 柯西初值问题

设 $(X_{t}:t\geqslant 0)$ 是由随机微分方程(9.3.3)定义的的扩散过程.这里假定扩散系数$\sigma$ 和漂移系数 $b$ 都是有界利普希茨函数.令 $C_b^2 (\mathbb{R})$ 是 $\mathbb{R}$ 上二次连续可微且其本身和前两阶导数均有界的函数全体构成的集合.对于 $f\in C_b^2 (\mathbb{R})$ 写

$$
L f (x) = \frac {1}{2} \sigma^ {2} (x) \partial_ {x x} f (x) + b (x) \partial_ {x} f (x), \quad x \in \mathbb {R}. \tag {9.3.26}
$$

根据 (9.3.3) 式和伊藤公式,

$$
f (X _ {t}) = f (X _ {0}) + \int_ {0} ^ {t} f ^ {\prime} (X _ {s}) \sigma (X _ {s}) \mathrm{d} B _ {s} + \int_ {0} ^ {t} L f (X _ {s}) \mathrm{d} s.
$$

令 $X_0 = x$ 并对上式取期望得

$$
P _ {t} f (x) = f (x) + \int_ {0} ^ {t} P _ {s} L f (x) \mathrm{d} s.
$$

对 $t \geqslant 0$ 求导数, 并应用控制收敛定理得

$$
\partial_ {t} P _ {t} f (x) = P _ {t} L f (x), \quad x \in \mathbb {R}. \tag {9.3.27}
$$

给定 $[0, \infty) \times \mathbb{R}$ 上的函数 $u = u(t, x)$, 我们写 $u \in C^{1,2}([0, \infty) \times \mathbb{R})$, 是指该函数有连续的导数 $\partial_t u$, $\partial_x u$ 和 $\partial_{xx} u$ 且函数 $|u| + |\partial_t u| + |\partial_x u| + |\partial_{xx} u|$ 在 $[0, \infty) \times \mathbb{R}$ 上有界. 对于函数 $u \in C^{1,2}([0, \infty) \times \mathbb{R})$, 考虑抛物型偏微分方程:

$$
\partial_ {t} u (t, x) = L u (t, x), \quad t \geqslant 0, x \in \mathbb {R}. \tag {9.3.28}
$$

显然 (9.3.28) 式是例 8.1.4 中的热方程 (8.1.10) 的推广. 求解 (9.3.28) 式满足初值条件 $u(0, \cdot) = f$ 的解的问题称为柯西问题.

对于 (9.3.1) 式的解 $(X_{t}: t \geqslant 0)$ 和 $[0, t] \times \mathbb{R}$ 上的函数 $(r, x) \mapsto u(t - r, x)$ 应用伊藤公式得

$$
\begin{array}{l} u (t - r, X _ {r}) = u (t, X _ {0}) + \int_ {0} ^ {r} \partial_ {x} u (t - s, X _ {s}) \sigma (X _ {s}) \mathrm{d} B _ {s} + \\ \int_ {0} ^ {r} \partial_ {x} u (t - s, X _ {s}) b (X _ {s}) \mathrm{d} s - \int_ {0} ^ {r} \partial_ {t} u (t - s, X _ {s}) \mathrm{d} s + \\ \frac {1}{2} \int_ {0} ^ {r} \partial_ {x x} u (t - s, X _ {s}) \sigma (X _ {s}) ^ {2} \mathrm{d} s \\ = u (t, X _ {0}) + \int_ {0} ^ {r} \partial_ {x} u (t - s, X _ {s}) \sigma (X _ {s}) \mathrm{d} B _ {s}. \\ \end{array}
$$

所以 $\{u(t - r, X_r) : r \in [0, t]\}$ 是有界的 $(\mathcal{F}_t)$ 鞅.特别地，上式对 (9.3.1) 式的满足 $X_0^x = x$ 的唯一解 $(X_t^x : t \geqslant 0)$ 成立.再令 $r = t$ 并取期望得

$$
u (t, x) = P _ {t} f (x) = \mathbf {E} [ f (X _ {t} ^ {x}) ]. \tag {9.3.29}
$$

这就给出了 (9.3.28) 式的柯西问题的解的一个概率表示. 事实上, 在 $b, \sigma$ 和 $f$ 满足适当正则条件的情况下, 由 (9.3.29) 式定义的函数 $u$ 是 (9.3.28) 式的初值问题的唯一解, 参见 [19, p.227, 定理 24.1]. 关于随机微分方程和扩散过程的更为深入的讨论, 还可以参考 [20, 22, 29, 38] 等.

## 练习题

1. 令 $(X_{t})$ 为由(9.3.17)式定义的奥恩斯坦-乌伦贝克过程.

(1) 证明 $(X_{t})$ 是朗之万方程 (9.3.18) 的解;
(2) 给出  $(X_{t})$  的转移半群  $(P_{t})$ ;
(3) 证明 $(P_{t})$ 是费勒半群; (4) 证明: 若 $b > 0$, 则 $X_{t}$ 的分布弱收敛到正态分布 $N(0, \sigma^{2} / 2b)$.
2. 证明由 (9.3.20) 式给出的过程 $(S_{t})$ 是 (9.3.19) 式的解.
3. 利用关于正态分布的积分给出由 (9.3.20) 式定义的几何布朗运动 $(S_{t})$ 的转移半群 $(P_{t})$ 的表示并证明 $(P_{t})$ 是费勒半群.
4. 令 $g \in C_b^2(\mathbb{R})$ 而 $L$ 是由 (9.3.26) 式定义的微分算子. 再设 $[0, \infty) \times \mathbb{R}$ 上的函数 $v = v(t, x)$ 有连续的导数 $\partial_t v, \partial_x v$ 和 $\partial_{xx} v$ 且函数 $|v| + |\partial_t v| + |\partial_x v| + |\partial_{xx} v|$ 在 $[0, \infty) \times \mathbb{R}$ 上有界. 证明: 若 $v$ 满足偏微分方程

$$
\partial_ {t} v (t, x) = L v (t, x) + g (x) v (t, x),
$$

则它可以表示为

$$
v (t, x) = \mathbf {E} \Big [ v (0, X _ {t} ^ {x}) \exp \Big \{\int_ {0} ^ {t} g (X _ {s} ^ {x}) \mathrm{d} s \Big \} \Big ].
$$

提示: 参见 [19, p.230, 定理 24.2].

## 参考文献

[1] ATHREYA K B, NEY P E. Branching Processes. Berlin: Springer, 1972.
[2] BIENAYMÉ I J. De la loi de multiplication et de la durée des familles. Soc. Philomat. Paris Extraits, 1845, 5: 37-39.
[3] BOVIER A. Gaussian Processes on Trees: From Spin Glasses to Branching Brownian Motion. Cambridge: Cambridge Univ. Press, 2017.
[4] CHEN M F. From Markov Chains to Non-Equilibrium Particle Systems. 2nd ed. Singapore: World Sci., 2004.
[5] CHEN M F. Eigenvalues, inequalities, and Ergodic Theory. London: Springer, 2005.
[6] 陈木法, 毛永华. 随机过程导论. 北京: 高等教育出版社, 2007.
[7] CONWAY J B. A Course in Functional Analysis. New York: Springer, 1990.
[8] CHUNG, K L. Lectures from Markov Processes to Brownian Motion. New York: Springer, 1982.
[9] DUQUESNE T, LE GALL J F. Random Trees, Lévy Processes and Spatial Branching Processes. Astérisque, 2002, 281.
[10] ETHIER S N, KURTZ T G. Markov Processes: Characterization and Convergence. New York: John Wiley & Sons, 1986.
[11] EINSTEIN, A. Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung von in ruhenden Flüssigkeiten suspendierten Teilchen (On the movement of small particles suspended in stationary liquids required by the molecular-kinetic theory of heat). Annalen der Physik, 1905, 322(8): 549-560.
[12] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第一卷. 杨弢亮, 叶彦谦, 译. 北京: 高等教育出版社, 2006.
[13] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第二卷. 徐献瑜, 冷生明, 梁文骐, 译. 北京: 高等教育出版社, 2006.
[14] 菲赫金哥尔茨. 微积分学教程 (第 8 版): 第三卷. 路见可, 余家荣, 吴亲仁, 译. 北京: 高等教育出版社, 2006.
[15] GALTON F, WATSON H W. On the probability of the extinction of families. J. Anthropol. Inst. Great Britain and Ireland, 1874, 4, 138-144.
[16] GRIMMETT G, WELSH D. Probability: An Introduction. 2nd ed. Oxford: Oxford Univ. Press, 2014.
[17] HEWITT E, STROMBERG K. Real and Abstract Analysis. Berlin: Springer, 1965.
[18] 侯振挺. Q 过程的唯一性准则. 长沙: 湖南科学技术出版社, 1982.
[19] 黄志远. 随机分析学基础. 2 版. 北京: 科学出版社, 2001.
[20] IKEDA N, WATANABE S. Stochastic Differential Equations and Diffusion Processes. 2nd ed. Amsterdam: North-Holland, Tokyo: Kodansha, 1989.
[21] LAMBERTON D, LAPEYRE B. Introduction to Stochastic Calculus Applied to Finance. 2nd ed. Boca Raton: Chapman and Hall/CRC, 2008.
[22] LE GALL J -F. Brownian Motions, Martingales and Stochastic Calculus. Switzerland: Springer, 2016.
[23] LE GALL J -F. Measure Theory, Probability, and Stochastic Processes. Switzerland: Springer, 2022.
[24] LI Z H. Measure-Valued Branching Markov Processes. 2nd ed. Berlin: Springer, 2022.
[25] LIGGETT M. Interacting Particle Systems. Berlin: Springer, 1985.
[26] LINDGREN, G. Stationary Stochastic Processes: Theory and Applications. Boca Raton: CRC Press, 2013.
[27] PARDOUX E. Probabilistic Models of Population Evolution: Scaling Limits, Genealogies and Interactions. Switzerland: Springer, 2016.
[28] 钱敏平, 龚光鲁. 随机过程论. 2 版. 北京: 北京大学出版社, 1997.
[29] 任佳刚. 随机过程教程. 北京: 科学出版社, 2022.
[30] ROSE S M. Introduction to Probability Models. 12th ed. London: Academic Press, 2019.
[31] SATO K. Lévy Processes and Infinitely Divisible Distributions. Cambridge: Cambridge Univ. Press, 1999.
[32] SHI Z. Branching random walks. In: Ecole d'Eté de Probabilités de Saint-Flour Lecture Notes Math. 2151. Cham: Springer, 2015.
[33] SHIRYAEV A N. Probability. New York: Springer, 1996.
[34] WANG F Y. Functional Inequalities, Markov Semigroups and Spectral Theory. Beijing: Science Press, 2005.
[35] 王梓坤, 杨向群. 生灭过程与马尔可夫链. 北京: 科学出版社, 2005.
[36] WIENER N. Differential space. J. Math. Phys., 1923, 2, 131-174.
[37] 严士健, 刘秀芳. 测度与概率. 2 版. 北京: 北京师范大学出版社, 2003.
[38] 应坚刚. 随机过程基础. 3 版. 上海: 复旦大学出版社, 2024.