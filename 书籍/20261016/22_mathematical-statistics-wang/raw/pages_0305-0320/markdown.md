- Cramér-von Mises (克拉默-冯·米泽斯) 统计量: $C_n = \int [F_n(x) - F_0(x)]^2 \mathrm{d}F_0(x)$.
- Anderson-Darling (安德森-达林) 统计量: $n \int w(x)[F_n(x) - F_0(x)]^2 \mathrm{d}F_0(x)$, 其中 $w(x) = [x(1 - x)]^{-1/2}$.

Kolmogorov-Smirnov 统计量度量了经验分布函数和总体分布的差异的最大值, Cramér-von Mises 检验统计量考虑经验分布函数和总体分布的差异在密度函数意义下的加权平均. Cramér-von Mises 检验统计量有下面的极限分布:

$$
n C _ {n} \xrightarrow {\mathrm{d}} \sum_ {j = 0} ^ {\infty} j ^ {- 2} \pi^ {- 2} \chi_ {1 j} ^ {2},
$$

其中  $\chi_{1j}^{2}$  独立同分布于  $\chi_{1}^{2}$  分布. Anderson-Darling 统计量采用更灵活的加权平均.

## 6.3.4 正态性检验

前面提到的  $\chi^{2}$  拟合优度检验和 Kolmogorov-Smirnov 检验方法等方法对于总体分布没有做特殊限制, 即其可适用于正态分布, 也可适用于其他分布类型. 正态分布在统计学中占有特殊地位. 许多统计推断方法都是基于正态总体的, 因此检验数据是否服从正态分布是很有意义的. 有必要针对数据是否服从正态分布给出特殊的检验方法. 本小节介绍另两种有更高检验功效的常用检验方法, 即 Shapiro-Wilk 的 W 检验和 D'Agostino 的 D 检验. 我国已把这两个方法列入了国家标准. 当样本量  $n \leqslant 50$  时, 用 W 检验; 当样本量 n > 50 时, 用 D 检验.

为了方便, 本小节始终假设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体为 F 的独立同分布样本, 现感兴趣的假设为

$$
H _ {0}: F (x) \in \left\{\varPhi \left(\frac {x - \mu}{\sigma}\right): \mu \in \mathbb {R}, \sigma > 0 \right\}.
$$

## 1. W 检验

W 检验是 S. Shapiro (夏皮罗) 和 M. Wilk (威尔克) 提出的, 参见 Shapiro et al. (1965). W 检验的检验统计量为

$$
W = \frac {\left(\sum_ {k = 1} ^ {[ n / 2 ]} a _ {k} (n) (X _ {(n + 1 - k)} - X _ {(k)})\right) ^ {2}}{\sum_ {i = 1} ^ {n} (X _ {(i)} - \bar {X}) ^ {2}},
$$

其中  $X_{(1)} \leqslant X_{(2)} \leqslant \cdots \leqslant X_{(n)}$  为次序统计量,  $\{a_{k}(n)\}$  是一组给定的与 n 有关的常数, 可查表求得. W 检验的拒绝域为

$$
\{W <   c \},
$$

其中临界值 $c$ 满足 $P(W < c|H_0) = \alpha$.

此检验的理由大致如下:

设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自  $N(\mu, \sigma^{2})$  的独立同分布样本，如记  $Y_{i} = \frac{X_{(i)} - \mu}{\sigma}, m_{i} = E(Y_{i}), \varepsilon_{i} = X_{(i)} - E[X_{(i)}]$ ，则知  $m_{i}$  是与  $\mu, \sigma$  无关的常数，且有

$$
X _ {(i)} = \mu + \sigma m _ {i} + \varepsilon_ {i}.
$$

由于当 n 较大时,  $X_{(i)} \approx E[X_{(i)}]$ , 因而  $\varepsilon_{i}$  较小. 于是 n 个点  $\{(X_{(i)}, m_{i}) : i = 1, 2, \cdots, n\}$  近似在一条直线上.

为区别这 n 个点是否在一条直线上, 可采用下面的  $R^{2}$  统计量:

$$
R ^ {2} = \left\{\frac {\sum_ {i = 1} ^ {n} [ X _ {(i)} - \bar {X} ] (m _ {i} - \bar {m})}{\sqrt {\sum_ {i = 1} ^ {n} [ X _ {(i)} - \bar {X} ] ^ {2} \sum_ {i = 1} ^ {n} (m _ {i} - \bar {m}) ^ {2}}} \right\} ^ {2}, \tag {6.3.6}
$$

其中  $\bar{m}=\sum_{i=1}^{n}m_{i}/n.$  当  $H_{0}$  成立时, 即  $X_{i}$  服从  $N(\mu,\sigma^{2})$  时, (6.3.6) 式的  $R^{2}$  应接近 1.
于是, 当  $R^{2}$  远离 1 时, 有理由拒绝  $H_{0}$ .

由于  $N(0,1)$  是对称分布, 故当  $H_{0}$  成立时,  $(Y_{1}, Y_{2}, \cdots, Y_{n})$  与  $(-Y_{1}, -Y_{2}, \cdots, -Y_{n})$  有相同的联合分布, 从而  $Y_{k}$  与  $-Y_{n+1-k}$  也有相同的分布, 故  $m_{k} = -m_{n+1-k}, \bar{m} = 0$ . 于是,

$$
R ^ {2} = \frac {\left(\sum_ {i = 1} ^ {n} X _ {(i)} m _ {i}\right) ^ {2}}{\sum_ {i = 1} ^ {n} (X _ {(i)} - \bar {X}) ^ {2} \sum_ {i = 1} ^ {n} m _ {i} ^ {2}} = \frac {\left(\sum_ {k = 1} ^ {[ n / 2 ]} m _ {n + 1 - k} (X _ {(n + 1 - k)} - X _ {(k)})\right) ^ {2}}{\sum_ {i = 1} ^ {n} (X _ {(i)} - \bar {X}) ^ {2} \sum_ {i = 1} ^ {n} m _ {i} ^ {2}}, \tag {6.3.7}
$$

如取

$$
a _ {k} (n) = \frac {m _ {n + 1 - k}}{\left(\sum_ {i = 1} ^ {n} m _ {i} ^ {2}\right) ^ {1 / 2}},
$$

则知 $W = R^2$

为理解 (6.3.7) 式, 定义

$$
Q ^ {2} = \sum_ {i = 1} ^ {n} (X _ {(i)} - \bar {X}) ^ {2}, \hat {\sigma} = \sum_ {i = 1} ^ {n} b _ {i} X _ {(i)}, b _ {i} = m _ {i} / \sum_ {i = 1} ^ {n} m _ {i} ^ {2},
$$

则 $R^2$ 可以重写成

$$
R ^ {2} = \sum_ {i = 1} ^ {n} m _ {i} ^ {2} \hat {\sigma} ^ {2} / Q ^ {2}.
$$

注意到, 无论样本是否正态, $Q^2$ 经修正后都可以成为 $\sigma^2$ 的一个 UE, 而分子 $\hat{\sigma}$ 是样本的线性函数, 且当 $H_0$ 成立时它是 $\sigma$ 的 UE, 于是 $\hat{\sigma}^2$ 也可成为 $\sigma^2$ 的一个估计. 这样, 在正态性假设下, 二者的差别不应很大. 这就是采用 $R^2$ 来检验正态性假设的一个直观解释. 为了扩大这个差异, Shapiro 和 Wilk 把上述的 $\hat{\sigma}$ 换为 $\sigma$ 的 BLUE

$$
\hat {\sigma} ^ {\prime} = \sum_ {i = 1} ^ {n} c _ {i} X _ {(i)}, \tag {6.3.8}
$$

就得到了 W 检验统计量.

## 2. D 检验

W 检验虽有效, 但可惜的是它只适用于容量 3—50 的样本, 其主要原因是, 对超过 50 的样本容量 n, 很难计算其分位数值. 为此, D'Agostino (1971) 提出了 D 检验.

由 W 统计量的定义不难看出, 如果不计常数因子, 它是正态分布的标准差  $\sigma$  的 BLUE 与样本标准差的比值的平方, 即关于  $\sigma$  的两个估计量的比值的平方. 由于 BLUE 的系数计算是繁杂的, 且随着样本量的增加, 这种繁杂在增加. 随着样本量的增加, 不得不放弃用 BLUE 来构造检验统计量. 因此, D'Agostino 建议, 在样本容量超过 50 时, 用  $i - \frac{n + 1}{2}$  来代替 BLUE (6.3.8) 式中的  $c_{i}$ , 即考虑用

$$
T = \sum_ {i = 1} ^ {n} \left(i - \frac {n + 1}{2}\right) X _ {(i)}
$$

作为 $\sigma$ 的一个线性无偏估计. 再考虑到 $n$ 的阶, 用统计量

$$
D _ {n} = \frac {\sum_ {i = 1} ^ {n} \left(i - \frac {n + 1}{2}\right) X _ {(i)}}{n ^ {3 / 2} \sqrt {\sum_ {i = 1} ^ {n} (X _ {i} - \bar {X}) ^ {2}}},
$$

作为正态性检验统计量, 且当它远离 1 时, 有理由拒绝正态性假设.

为求取其极限零分布, 可以证明, 当  $H_{0}$  成立时,

$$
E (D _ {n}) = 0. 2 8 2 0 9 4 7 9, \sqrt {\mathrm{Var} (D _ {n})} = 0. 0 2 9 9 8 5 9 8 / \sqrt {n},
$$

故采用如下的标准化随机变量

$$
Y _ {n} = \frac {\sqrt {n} (D _ {n} - 0 . 2 8 2 0 9 4 7 9)}{0 . 0 2 9 9 8 5 9 8}
$$

作为检验统计量, 且其拒绝域为

$$
\{Y _ {n} <   c _ {1} \} \cup \{Y _ {n} > c _ {2} \},
$$

其中 $c_{1} < c_{2}$

关于 D 检验的分位数现已有表可查.

## 6.4 独立性检验

当研究两个分类变量 A 和 B 之间是否独立时, 即考虑如下的假设:

$$
H _ {0}: \text {变量} A \text {与} B \text {独立}, \tag {6.4.1}
$$

此时, 常用的检验方法是使用列联表, 其为这两个变量交叉分类的频数分布表. 交叉分类的目的是将多个变量分组, 然后比较各组的分布状况, 以寻找变量间是否存在相关性等关系. 列联表的方法也可以检验多个分类变量之间是否独立.

按两个变量交叉分类的列联表称为二维列联表, 如例 6.3.4 中的色盲和性别是两个变量; 若按三个变量交叉分类, 所得的列联表称为三维列联表, 以此类推. 三维及以上的列联表称为 “多维列联表” 或 “高维列联表”. 列联表分析主要包括两个任务: 一是根据收集的样本数据, 产生二维或多维列联表; 二是在列联表的基础上, 通过检验统计量对变量间是否存在相关性进行检验.

一般的二维列联表数据如表 6.4.1 所示, 其中, 变量 A, B 分别有 r, s 个水平, 且以  $n_{ij}$  表示在 n 个样本中属于  $A_{i} \cap B_{j}$  的样本个数,  $n_{i.} = \sum_{j=1}^{s} n_{ij}$  和  $n_{.j} = \sum_{i=1}^{r} n_{ij}$  分别表示 A 取第 i 个水平和 B 取第 j 个水平的样本个数. 记

$$
p _ {i j} = P (X \in A _ {i} \cap B _ {j}), i = 1, 2, \dots , r, j = 1, 2, \dots , s,
$$

表 6.4.1 二维列联表数据

<table><tr><td rowspan="2">A</td><td colspan="4">B</td><td rowspan="2">总计</td></tr><tr><td> $B_1$ </td><td> $B_2$ </td><td>...</td><td> $B_s$ </td></tr><tr><td> $A_1$ </td><td> $n_{11}$ </td><td> $n_{12}$ </td><td>...</td><td> $n_{1s}$ </td><td> $n_{1.}$ </td></tr><tr><td> $A_2$ </td><td> $n_{21}$ </td><td> $n_{22}$ </td><td>...</td><td> $n_{2s}$ </td><td> $n_{2.}$ </td></tr><tr><td> $\vdots$ </td><td> $\vdots$ </td><td> $\vdots$ </td><td></td><td> $\vdots$ </td><td> $\vdots$ </td></tr><tr><td> $A_r$ </td><td> $n_{r1}$ </td><td> $n_{r2}$ </td><td>...</td><td> $n_{rs}$ </td><td> $n_{r.}$ </td></tr><tr><td>总计</td><td> $n_{.1}$ </td><td> $n_{.2}$ </td><td>...</td><td> $n_{.s}$ </td><td>n</td></tr></table>

则这 $n$ 个样本可以看成是来自多项分布 $X$ 的样本. 令

$$
p _ {i.} = P (X \in A _ {i}), i = 1, 2, \dots , r,
$$

$$
p _ {\cdot j} = P (X \in B _ {j}), j = 1, 2, \dots , s,
$$

则有

$$
p _ {i.} = \sum_ {j = 1} ^ {s} p _ {i j}, p _ {. j} = \sum_ {i = 1} ^ {r} p _ {i j}.
$$

另外, 还要注意到如下两个约束:

$$
\sum_ {i = 1} ^ {r} p _ {i.} = \sum_ {j = 1} ^ {s} p _ {. j} = 1. \tag {6.4.2}
$$

当 $H_0$ 成立时, 对于 $A$ 和 $B$ 这两个离散型随机变量, 应有 $p_{ij} = p_i \cdot p_j$. 于是, (6.4.1)式的零假设等价于如下假设:

$$
H _ {0}: p _ {i j} = p _ {i}. p _ {. j}, i = 1, 2, \dots , r, j = 1, 2, \dots , s. \tag {6.4.3}
$$

由于可以把上述列联表数据看作是多项分布的样本, 故可以用  $\chi^{2}$  拟合优度检验对其独立性假设 (6.4.3) 进行显著性检验. 由于  $p_{i}$ . 和  $p_{\cdot j}$  是未知的, 且有两个约束 (6.4.2), 故当  $H_{0}$  成立时共有  $r + s - 2$  个未知参数. 此时, 其未知参数的最大似然估计为

$$
\hat {p} _ {i \cdot} = \frac {n _ {i \cdot}}{n}, \hat {p} _ {\cdot j} = \frac {n _ {\cdot j}}{n}, i = 1, 2, \dots , r, j = 1, 2, \dots , s.
$$

于是, 对于二维列联表,  $\chi^{2}$  拟合优度检验统计量为

$$
\chi^ {2} = n \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} \frac {\left(n _ {i j} - \frac {n _ {i} . n _ {. j}}{n}\right) ^ {2}}{n _ {i} . n _ {. j}},
$$

且当  $H_{0}$  成立及  $n \rightarrow \infty$  时, 根据 (6.3.4) 式的结果, 有

$$
\chi^ {2} \xrightarrow {\mathrm{d}} \chi^ {2} (r s - r - s + 2 - 1) = \chi^ {2} ((r - 1) (s - 1)),
$$

于是, 此检验的近似水平为  $\alpha$  的检验拒绝域为

$$
\{\chi^ {2} \geqslant \chi_ {\alpha} ^ {2} ((r - 1) (s - 1)) \}.
$$

对于例 6.3.4 中的数据, 由于 r = s = 2, n = 1000,  $\chi^{2} = 27.4 > 6.64 = \chi_{0.01}^{2}(1)$ , 故有理由拒绝  $H_{0}$ , 即认为色盲与性别之间存在着显著性的相关关系.

注 6.4.1 当分类指标为连续型变量时, 仍然可以先用前面的离散化方法对变量离散后, 再用  $\chi^{2}$  拟合优度检验对二者的独立性进行检验.

可以将上述结果推广到多维的情况. 下面考虑三维列联表的独立性检验问题. 假设一个观测包含三个指标: A, B, C, 且分别有 r, s, t 个水平. 记  $n_{ijk}(i = 1, 2, \cdots, r, j = 1, 2, \cdots, s, k = 1, 2, \cdots, t)$  表示在 n 个样本中属于  $A_i \cap B_j \cap C_k$  的样本个数;  $n_{i..}(i = 1, 2, \cdots, r)$  表示在 n 个样本中属于  $A_i$  的样本个数,  $n_{\cdot j.(j = 1, 2, \cdots, s)}$  表示在 n 个样本中属于  $B_j$  的样本个数,  $n_{\cdot k}(k = 1, 2, \cdots, t)$  表示在 n 个样本中属于  $C_k$  的样本个数, 即

$$
n _ {i..} = \sum_ {j = 1} ^ {s} \sum_ {k = 1} ^ {t} n _ {i j k}, \quad n _ {. j.} = \sum_ {i = 1} ^ {r} \sum_ {k = 1} ^ {t} n _ {i j k}, \quad n _ {.. k} = \sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} n _ {i j k}.
$$

令  $n_{ij}.(i=1,2,\cdots,r,j=1,2,\cdots,s)$  表示在 n 个样本中属于  $A_{i}\cap B_{j}$  的样本个数， $n_{i\cdot k}(i=1,2,\cdots,r,k=1,2,\cdots,t)$  表示在 n 个样本中属于  $A_{i}\cap C_{k}$  的样本个数， $n_{\cdot jk}(j=1,2,\cdots,s,k=1,2,\cdots,t)$  表示在 n 个样本中属于  $B_{j}\cap C_{k}$  的样本个数，即

$$
n _ {i j.} = \sum_ {k = 1} ^ {t} n _ {i j k}, \quad n _ {i \cdot k} = \sum_ {j = 1} ^ {s} n _ {i j k}, \quad n _ {\cdot j k} = \sum_ {i = 1} ^ {r} n _ {i j k}.
$$

分别对 $n_{i..}, n_{.j..}, n_{..k}, n_{ij..}, n_{i.k}, n_{.jk}$ 和 $n_{ijk}$ 除以样本总数 $n$, 得到相应的概率 $p_{i..}, p_{.j..}, p_{..k}, p_{ij..}, p_{i.k}, p_{.jk}$ 和 $p_{ijk}$ 等概率值. 从而, 有

$$
\sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} \sum_ {k = 1} ^ {t} p _ {i j k} = 1, \quad \sum_ {i = 1} ^ {r} p _ {i..} = 1, \quad \sum_ {j = 1} ^ {s} p _ {\cdot j.} = 1, \quad \sum_ {k = 1} ^ {t} p _ {\cdot .. k} = 1,
$$

$$
\sum_ {i = 1} ^ {r} \sum_ {j = 1} ^ {s} p _ {i j.} = 1, \sum_ {i = 1} ^ {r} \sum_ {k = 1} ^ {t} p _ {i \cdot k} = 1, \sum_ {j = 1} ^ {s} \sum_ {k = 1} ^ {t} p _ {\cdot j k} = 1.
$$

此时感兴趣的假设可能有三类:

\- 三个指标相互独立, 即检验

$$
H _ {0}: \quad p _ {i j k} = p _ {i..} p _ {\cdot j}. p _ {\cdot k}. \tag {6.4.4}
$$

\- 部分独立性检验, 即检验某个分组变量独立于其他分组变量. 例如, 指标 A 与指标 B、C 之间独立, 即检验

$$
H _ {0}: \quad p _ {i j k} = p _ {i..} p _ {\cdot j k}. \tag {6.4.5}
$$

类似地, 可检验  $H_{0}$ :  $p_{ijk} = p_{\cdot j}$ .  $p_{i\cdot k}$  或  $H_{0}$ :  $p_{ijk} = p_{\cdot k}$ .  $p_{ij\cdot}$

\- 条件独立性检验, 即检验其中两个变量在第三个变量的每一水平上独立. 例如, 给定指标 $C$ 下, 指标 $A$ 与 $B$ 独立, 即检验

$$
H _ {0}: \quad p _ {i j k} = p _ {i \cdot k} p _ {\cdot j k} / p _ {\cdot \cdot k}. \tag {6.4.6}
$$

对于这三个检验, 可以用似然比检验方法.

对于三个指标相互独立的检验问题 (6.4.4), 似然比统计量为

$$
\Lambda_ {1} = \frac { \prod_ {i = 1} ^ {r} \prod_ {j = 1} ^ {s} \prod_ {k = 1} ^ {t} \left(\frac {n _ {i . .}}{n}\right) ^ {n _ {i . .}} \left(\frac {n _ {. j .}}{n}\right) ^ {n _ {. j .}} \left(\frac {n _ {. . k}}{n}\right) ^ {n _ {. . k}}}{ \prod_ {i = 1} ^ {r} \prod_ {j = 1} ^ {s} \prod_ {k = 1} ^ {t} \left(\frac {n _ {i j k}}{n}\right) ^ {n _ {i j k}}},
$$

且当 $H_0$ 成立及 $n\to \infty$ 时，有

$$
- 2 \ln \varLambda_ {1} \stackrel {\mathrm{d}} {\rightarrow} \chi^ {2} (r s t - 1 - (r - 1) - (s - 1) - (t - 1)).
$$

对于部分独立性检验问题 (6.4.5), 似然比统计量为

$$
\Lambda_ {2} = \frac { \prod_ {i = 1} ^ {r} \prod_ {j = 1} ^ {s} \prod_ {k = 1} ^ {t} \left(\frac {n _ {i . .}}{n}\right) ^ {n _ {i . .}} \left(\frac {n _ {. j k}}{n}\right) ^ {n _ {. j k}}}{ \prod_ {i = 1} ^ {r} \prod_ {j = 1} ^ {s} \prod_ {k = 1} ^ {t} \left(\frac {n _ {i j k}}{n}\right) ^ {n _ {i j k}}},
$$

且当 $H_0$ 成立及 $n\to \infty$ 时，有

$$
- 2 \ln \varLambda_ {2} \xrightarrow {\mathrm{d}} \chi^ {2} (r s t - 1 - (r - 1) - (s t - 1)).
$$

对于条件独立性检验问题 (6.4.6), 可以得到此时的似然比统计量为

$$
\Lambda_ {3} = \frac { \prod_ {i = 1} ^ {r} \prod_ {j = 1} ^ {s} \prod_ {k = 1} ^ {t} \left(\frac {n _ {i \cdot k} n _ {\cdot j k}}{n n _ {\cdot \cdot k}}\right) ^ {n _ {i j k}}}{ \prod_ {i = 1} ^ {r} \prod_ {j = 1} ^ {s} \prod_ {k = 1} ^ {t} \left(\frac {n _ {i j k}}{n}\right) ^ {n _ {i j k}}},
$$

且当 $H_0$ 成立及 $n\to \infty$ 时，有

$$
- 2 \ln \varLambda_ {3} \xrightarrow {\mathrm{d}} \chi^ {2} (t (r - 1) (s - 1)).
$$

需要指出的是, 也可以把三维列联表合并为一个二维列联表来处理. 不过, 这种处理会损失掉许多信息. 因此, 在一些情形下, 合并的列联表中认为变量之间是独立的, 但在三维列联表的检验中是不独立的.

## 6.5 U 统计量与秩检验

U 统计量 (U-statistic) 是一类特定的、具有对称性的统计量, 它是由 Hoeffding (1948) 引进的一种非参数统计量, 是样本均值的推广. U 统计量在非参数估计和非参数检验中都有重要应用, 其名称中的 “U” 为无偏 (unbiased) 之意. 本节将介绍 U 统计量的性质及其应用. 此外, 本节还介绍秩和检验等非参数检验.

## 6.5.1 U 统计量

先看下面的可靠性统计中的一个例子.

例6.5.1 对于某种电子元器件的寿命 $X$ ，在参数统计中，常设 $X$ 服从某类特殊的参数分布，例如指数分布、Weibull分布，或对数正态分布等；在非参数统计中，往往仅假设 $X$ 服从非负值连续分布 $F(x)$. 如果对任意的 $s > 0, t > 0$, 都有 $P(X > s + t | X > t) < P(X > s)$, 则称该元器件老化; 若有 $P(X > s + t | X > t) = P(X > s)$, 则称该元器件无老化. 在可靠性统计中, 一个重要的检验问题如下:

$$
H _ {0}: \text {元器件无老化} \leftrightarrow H _ {1}: \text {元器件老化}. \tag {6.5.1}
$$

令生存函数 $\bar{F}(x) = 1 - F(x)$, 则 $P(X > s + t | X > t) = P(X > s)$ 等价于 $\bar{F}(s + t) = \bar{F}(s) \cdot \bar{F}(t)$, $P(X > s + t | X > t) < P(X > s)$ 等价于 $\bar{F}(s + t) < \bar{F}(s) \cdot \bar{F}(t)$. 令

$$
\omega = \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} [ \bar {F} (s) \cdot \bar {F} (t) - \bar {F} (s + t) ] \mathrm{d} F (s) \mathrm{d} F (t).
$$

则检验问题 (6.5.1) 可简化为关于参数  $\omega$  的检验问题

$$
H _ {0}: \omega = 0 \quad \leftrightarrow \quad H _ {1}: \omega > 0.
$$

设 $X_{1}, X_{2}, X_{3}$ 是该元器件的寿命试验的三次随机试验结果，即独立同分布于 $F(x)$. 因为

$$
\int_ {0} ^ {\infty} \int_ {0} ^ {\infty} \bar {F} (s) \cdot \bar {F} (t) \mathrm{d} F (s) \mathrm{d} F (t) = \int_ {0} ^ {1} \int_ {0} ^ {1} (1 - u) \cdot (1 - v) \mathrm{d} u \mathrm{d} v = \frac {1}{4},
$$

$$
\begin{array}{l} \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} \bar {F} (s + t) \mathrm{d} F (s) \mathrm{d} F (t) = \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} P (X _ {1} > x _ {2} + x _ {3}) \mathrm{d} F (x _ {2}) \mathrm{d} F (x _ {3}) \\ = P (X _ {1} > X _ {2} + X _ {3}), \\ \end{array}
$$

所以 $\omega = \frac{1}{4} - P(X_1 > X_2 + X_3)$. 若令 $\theta = P(X_1 > X_2 + X_3)$, 则检验问题 (6.5.1) 可进一步简化为关于参数 $\theta$ 的检验问题

$$
H _ {0}: \theta = \frac {1}{4} \leftrightarrow H _ {1}: \theta <   \frac {1}{4}.
$$

因此, 一个非参数检验问题也可以简化为关于某个参数的检验问题.

为了寻求检验统计量, 首先要估计  $\theta$ . 一种自然的想法是寻找  $\theta$  的无偏估计. 根据两点分布的性质, 可知

$$
\psi (X _ {1}, X _ {2}, X _ {3}) = \left\{ \begin{array}{l l} 1, & X _ {1} > X _ {2} + X _ {3}, \\ 0, & X _ {1} \leqslant X _ {2} + X _ {3} \end{array} \right.
$$

是 $\theta$ 的一个无偏估计. 考虑到样本中各个分量的地位是相同的, 故定义对称函数

$$
\phi (X _ {1}, X _ {2}, X _ {3}) = \frac {\sum \psi (X _ {i _ {1}} , X _ {i _ {2}} , X _ {i _ {3}})}{3 !},
$$

它也是 $\theta$ 的一个无偏估计, 其中 $(i_1, i_2, i_3)$ 是 (1,2,3) 的一个置换, $\sum$ 表示对所有这种置换求和. $\psi(X_1, X_2, X_3)$ 和 $\phi(X_1, X_2, X_3)$ 都是 $\theta$ 的无偏估计, 但 $\phi(X_1, X_2, X_3)$ 的方差不会比  $\psi(X_{1},X_{2},X_{3})$  的方差大. 进一步地, 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体分布  $F(x)$  的独立同分布样本,

$$
U (X _ {1}, X _ {2}, \dots , X _ {n}) = \frac {\sum \phi (X _ {i _ {1}} , X _ {i _ {2}} , X _ {i _ {3}})}{\mathrm{C} _ {n} ^ {3}},
$$

其中  $1 \leqslant i_{1} < i_{2} < i_{3} \leqslant n, \sum$  表示对所有组合  $(i_{1}, i_{2}, i_{3})$  求和. 则  $U(X_{1}, X_{2}, \cdots, X_{n})$  仍是  $\theta$  的一个无偏估计, 其方差不比  $\phi(X_{1}, X_{2}, X_{3})$  的方差大. 由于  $H_{1}$  为真时,  $\theta$  的值比较小, 因此当  $U(X_{1}, X_{2}, \cdots, X_{n}) \leqslant c$  时拒绝原假设, 认为元器件老化. 这里临界值 c 由统计量  $U(X_{1}, X_{2}, \cdots, X_{n})$  的分布决定.

在例 6.5.1 中, 统计量  $U(X_{1}, X_{2}, \cdots, X_{n})$  是待估参数  $\theta$  特殊的无偏估计. 称其为 U 统计量. 若能得到该统计量的分布或极限分布, 则可解决检验问题 (6.5.1). 下面给出 U 统计量的定义.

定义 6.5.1 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自总体分布  $F(x)$  的独立同分布样本, 其中未知总体 F 来自非参数族 F. 设对称函数  $\phi(X_{1}, X_{2}, \cdots, X_{m})$  是待估参数  $\theta = T(F)$  的一个无偏估计, 其中  $m \leqslant n$ , 且对任意  $F \in F$ , 有  $E\left[\left|\phi(X_{1}, X_{2}, \cdots, X_{m})\right|\right] < \infty$ . 称  $\theta$  的一个对称无偏估计

$$
U _ {n} = \frac {1}{\mathrm{C} _ {n} ^ {m}} \sum_ {c} \phi (X _ {i _ {1}}, X _ {i _ {2}}, \dots , X _ {i _ {m}})
$$

为具有 m 阶核  $\phi$  的 U 统计量. 这里,  $\sum_{c}$  表示对全部  $C_{n}^{m}$  个有不同元素的  $\{i_{1}, i_{2}, \cdots, i_{m}\} \subset \{1, 2, \cdots, n\}$  求和.

令  $\theta = E[\phi(X_{1}, X_{2}, \cdots, X_{m})]$ . 基于核函数  $\phi(X_{1}, X_{2}, \cdots, X_{m})$ ，定义

$$
\phi_ {k} (x _ {1}, x _ {2}, \dots , x _ {k}) = E [ \phi (x _ {1}, \dots , x _ {k}, X _ {k + 1}, \dots , X _ {m}) ], 0 \leqslant k \leqslant m,
$$

则  $\phi_{0}=E[\phi(X_{1},X_{2},\cdots,X_{m})]$ ， $\phi_{m}=E[\phi(x_{1},x_{2},\cdots,x_{m})]$ ，且对于任意 k，我们有  $E[\phi_{k}(X_{1},X_{2},\cdots,X_{k})]=\theta$ 。记  $\phi_{k}$  的方差为  $\sigma_{k}^{2}=\mathrm{Var}[\phi_{k}(X_{1},X_{2},\cdots,X_{k})]$ ，则  $\sigma_{0}^{2}=0$ ， $\sigma_{m}^{2}=\mathrm{Var}[\phi_{m}(X_{1},X_{2},\cdots,X_{m})]$ 。由条件方差分解，有  $0=\sigma_{0}^{2}\leqslant\sigma_{1}^{2}\leqslant\cdots\leqslant\sigma_{m}^{2}$ 。

定理 6.5.1 U 统计量有以下性质:

(1) 数学期望  $E(U_{m}) = E[\phi(X_{1}, X_{2}, \cdots, X_{m})] = \theta.$
(2) 方差

$$
\mathrm{Var} (U _ {n}) = \frac {1}{\mathrm{C} _ {n} ^ {m}} \sum_ {k = 1} ^ {m} \mathrm{C} _ {m} ^ {k} \mathrm{C} _ {n - m} ^ {m - k} \sigma_ {k} ^ {2},
$$

特别地, 当 $\sigma_{m}^{2}<\infty$ 时, $\mathrm{Var}(U_{k})=\frac{m^{2}}{n}\cdot\sigma_{1}^{2}+O(n^{-2}).$

(3) 渐近正态性. 当  $\sigma_{m}^{2}<\infty$  且  $\sigma_{1}^{2}>0$  时,

$$
\sqrt {n} (U _ {n} - \theta) \xrightarrow {\mathrm{d}} N (0, m ^ {2} \sigma_ {1} ^ {2}).
$$

证明 数学期望可由 U 统计量的定义以及期望的可加性得到. 下面, 计算 U 统计量的方差. 根据  $\sigma_{k}^{2}$  的定义, 对于  $U_{n}$  的方差计算中每一个小单元,

$$
\mathrm{Cov} (\phi (X _ {i _ {1}}, X _ {i _ {2}}, \dots , X _ {i _ {m}}), \phi (X _ {j _ {1}}, X _ {j _ {2}}, \dots , X _ {j _ {m}})) = \sigma_ {k} ^ {2},
$$

其中  $i_{1}, i_{2}, \cdots, i_{m}$  和  $j_{1}, j_{2}, \cdots, j_{m}$  为  $X_{1}, X_{2}, \cdots, X_{n}$  中选出的 m 个元素，k 为  $i_{1}, i_{2}, \cdots, i_{m}$  和  $j_{1}, j_{2}, \cdots, j_{m}$  中相同的对数. 则

$$
\begin{array}{l} \mathrm{Var} (U _ {n}) \\ = \operatorname{Var} \left[ \frac {1}{\mathrm{C} _ {n} ^ {m}} \sum_ {1 \leqslant i _ {1} <   i _ {2} <   \dots <   i _ {m} \leqslant n} \phi (X _ {i _ {1}}, X _ {i _ {2}}, \dots , X _ {i _ {m}}) \right] \\ = \frac {1}{\left(\mathrm{C} _ {n} ^ {m}\right) ^ {2}} \sum_ {i _ {1} <   i _ {2} <   \dots <   i _ {m}} \sum_ {j _ {1} <   j _ {2} <   \dots <   j _ {m}} \operatorname{Cov} \left(\phi \left(X _ {i _ {1}}, X _ {i _ {2}}, \dots , X _ {i _ {m}}\right), \phi \left(X _ {j _ {1}}, X _ {j _ {2}}, \dots , X _ {j _ {m}}\right)\right) \\ = \frac {1}{\mathrm{C} _ {n} ^ {m}} \sum_ {j _ {1} <   j _ {2} <   \dots <   j _ {m}} \operatorname{Cov} \left(\phi (X _ {1}, X _ {2}, \dots , X _ {m}), \phi (X _ {j _ {1}}, X _ {j _ {2}}, \dots , X _ {j _ {m}})\right) \\ = \frac {1}{\mathrm{C} _ {n} ^ {m}} \sum_ {k = 1} ^ {m} \mathrm{C} _ {m} ^ {k} \mathrm{C} _ {n - m} ^ {m - k} \sigma_ {k} ^ {2}. \\ \end{array}
$$

由此可知, 当  $\sigma_{m}^{2}<\infty$  时,  $\mathrm{Var}(U_{k})=\frac{m^{2}}{n}\cdot\sigma_{1}^{2}+O(n^{-2})$ . 下面来证明渐近正态性. 由于  $\phi_{1}(X_{1}),\phi_{1}(X_{2}),\cdots,\phi_{1}(X_{n})$  是独立同分布于均值为  $\theta$ , 方差为  $\sigma_{1}^{2}(\sigma_{1}^{2}\in(0,\infty))$  的分布, 若令  $U_{n}^{*}=\frac{1}{n}\sum_{i=1}^{n}\phi_{1}(X_{i})$ , 则根据中心极限定理,

$$
\sqrt {n} (U _ {n} ^ {*} - \theta) \xrightarrow {\mathrm{d}} N (0, \sigma_ {1} ^ {2}).
$$

再令

$$
T _ {n} = \sqrt {n} (U _ {n} - \theta) - m \sqrt {n} (U _ {n} ^ {*} - \theta),
$$

则可证 $E(T_{n}) = 0$ ，且

$$
\begin{array}{l} \mathrm{Var} (T _ {n}) = n \mathrm{Var} (U _ {n}) + m ^ {2} n \mathrm{Var} (U _ {n} ^ {*}) - 2 m n \mathrm{Cov} (U _ {n}, U _ {n} ^ {*}) \\ = \frac {n}{\mathrm{C} _ {n} ^ {m}} \sum_ {k = 1} ^ {m} \mathrm{C} _ {m} ^ {k} \mathrm{C} _ {n - m} ^ {m - k} \sigma_ {k} ^ {2} + m ^ {2} \sigma_ {1} ^ {2} - 2 m ^ {2} \sigma_ {1} ^ {2} \\ = m ^ {2} \sigma_ {1} ^ {2} (1 + o (1)) - m ^ {2} \sigma_ {1} ^ {2} \\ = o (1). \\ \end{array}
$$

由 Markov 不等式, 有 $T_{n} \stackrel{\mathrm{p}}{\rightarrow} 0$, 因此, 由 Slutsky 定理, 可知

$$
\sqrt {n} (U _ {n} - \theta) \xrightarrow {\mathrm{d}} N (0, m ^ {2} \sigma_ {1} ^ {2}).
$$

根据定理 6.5.1 的渐近正态性, 可知 U 统计量具有相合性. 进一步地, 可以构造 U 统计量来做一些非参数检验.

例 6.5.2 设总体 X 的分布函数为  $F(x - \theta)$ ，其中  $F(x)$  是关于原点对称的连续型分布，具体形式未知。考虑检验问题

$$
H _ {0}: \theta = 0 \quad \leftrightarrow \quad H _ {1}: \theta > 0,
$$

即检验对称分布的对称中心在原点, 还是在原点的右边. 设  $X_{1}, X_{2}, \cdots, X_{n}$  是来自总体 X 的一个样本. 当原假设  $H_{0}: \theta = 0$  成立时,  $P(X_{1} + X_{2} > 0) = 0.5$ ; 当备择假设  $H_{1}: \theta > 0$  成立时,  $P(X_{1} + X_{2} > 0) > 0.5$ . 令  $\omega = P(X_{1} + X_{2} > 0)$ , 则上述检验问题可简化为关于参数  $\omega$  的检验问题,

$$
H _ {0}: \omega = 0. 5 \leftrightarrow H _ {1}: \omega > 0. 5.
$$

根据两点分布的性质，

$$
\phi (X _ {1}, X _ {2}) = \left\{ \begin{array}{l l} 1, & X _ {1} + X _ {2} > 0, \\ 0, & X _ {1} + X _ {2} \leqslant 0 \end{array} \right.
$$

是  $\omega$  的一个无偏估计. 由对称函数  $\phi(X_{1}, X_{2})$  可构造 U 统计量,

$$
U = U (X _ {1}, X _ {2}, \dots , X _ {n}) = \frac {\sum \phi (X _ {i _ {1}} , X _ {i _ {2}})}{\mathrm{C} _ {n} ^ {2}},
$$

其中 $1 \leqslant i_1 < i_2 \leqslant n$, $\sum$ 表示对所有组合 $(i_1, i_2)$ 求和. 根据定理 6.5.1 可知, $U$ 也是 $\omega$ 的一个无偏估计. 由于在备择假设成立时, $\omega$ 的值较大, 则当 $U(X_1, X_2, \cdots, X_n) \geqslant c$ 时, 拒绝原假设. 具体的 $c$ 由下面的方式确定. 由于 $m = 2$, 当 $H_0$ 为真时, $E[U(X_1, X_2, \cdots, X_n)] = 0.5$, 且 $\phi_1(x_1) = F(x_1), \sigma_1^2 = \frac{1}{12}, \phi_2(x_1, x_2) = \phi(x_1, x_2), \sigma_2^2 = \frac{1}{4}$. 则

$$
\mathrm{Var} [ U (X _ {1}, X _ {2}, \dots , X _ {n}) ] = \frac {2 n - 1}{6 n (n - 1)} = \frac {1}{3 n} + O (n ^ {- 2}),
$$

在原假设成立时, $\sqrt{n} \cdot \left(U - \frac{1}{2}\right) \xrightarrow{\mathrm{d}} N\left(0, \frac{1}{3}\right), n \to \infty$. 因此, 在大样本场合下检验问题的拒绝域为

$$
U \geqslant \frac {1}{2} + \sqrt {\frac {1}{3 n}} \cdot u _ {\alpha},
$$

其中  $u_{\alpha}$  是标准正态分布的上  $\alpha$  分位数.

前面的单样本的 U 统计量可以推广至两样本的情形.考虑两个相互独立的总体，其分布分别为 F 和 G，关心的参数  $\theta = \theta(F, G)$ .类似地，设  $X_{1}, X_{2}, \cdots, X_{n_{1}}$ ，和  $Y_{1}, Y_{2}, \cdots, Y_{n_{2}}$  是分别来自 F 和 G 的随机样本.设  $\phi(X, Y)$  为  $\theta$  的无偏估计.在  $X_{1}, X_{2}, \cdots, X_{n_{1}}$  给定时， $\phi(X_{1}, X_{2}, \cdots, X_{n_{1}}, Y_{1}, Y_{2}, \cdots, Y_{n_{2}})$  为  $Y_{1}, Y_{2}, \cdots, Y_{n_{2}}$  的对称函数, 而在  $Y_{1}, Y_{2}, \cdots, Y_{n_{2}}$  给定时,  $\phi(X_{1}, X_{2}, \cdots, X_{n_{1}}, Y_{1}, Y_{2}, \cdots, Y_{n_{2}})$  为  $X_{1}, X_{2}, \cdots, X_{n_{1}}$  的对称函数. 令

$$
U _ {n _ {1}, n _ {2}} = \frac {1}{\mathrm{C} _ {n _ {1}} ^ {m _ {1}}} \frac {1}{\mathrm{C} _ {n _ {2}} ^ {m _ {2}}} \sum_ {i _ {1} <   i _ {2} <   \dots <   i _ {m _ {1}}} \sum_ {j _ {1} <   j _ {2} <   \dots <   j _ {m _ {2}}} \phi (X _ {i _ {1}}, X _ {i _ {2}}, \dots , X _ {i _ {m _ {1}}}, Y _ {j _ {1}}, Y _ {j _ {2}}, \dots , Y _ {j _ {m _ {2}}}),
$$

则称  $U_{n_{1},n_{2}}$  是以  $\phi(X_{1},X_{2},\cdots,X_{m_{1}},Y_{1},Y_{2},\cdots,Y_{m_{2}})$  为核的两样本 U 统计量. 这里的对称化, 使得所有  $X_{i}$  地位是一样的, 所有  $Y_{j}$  地位是一样的, 但是两者不一定可以交换. 类似地, 也可以定义:

$$
\sigma_ {i j} ^ {2} = \mathrm{Cov} \left(\phi (X _ {1}, \dots , X _ {i}, X _ {i + 1}, \dots , X _ {m _ {1}}, Y _ {1}, \dots , Y _ {j}, Y _ {j + 1}, \dots , Y _ {m _ {2}}\right),
$$

$$
\phi (X _ {1}, \dots , X _ {i}, X _ {i + 1} ^ {*}, \dots , X _ {m _ {1}} ^ {*}, Y _ {1}, \dots , Y _ {j}, Y _ {j + 1} ^ {*}, \dots , Y _ {m _ {2}} ^ {*})).
$$

这里  $X_{1},\cdots,X_{i},X_{i+1},\cdots,X_{m_{1}},X_{i+1}^{*},\cdots,X_{m_{1}}^{*}$  是来自总体分布 F 的独立同分布样本， $Y_{1},\cdots,Y_{j},Y_{j+1},\cdots,Y_{m_{2}},Y_{j+1}^{*},\cdots,Y_{m_{2}}^{*}$  是来自总体分布 G 的独立同分布样本. 类似于一元的情形, 有下面的结论.

定理6.5.2 两样本U统计量 $U_{n_1,n_2}$ 的数学期望为 $E(U_{n_1,n_2}) = \theta$，其方差

$$
\mathrm{Var} (U _ {n _ {1}, n _ {2}}) = \sum_ {k = 0} ^ {m _ {1}} \sum_ {l = 0} ^ {m _ {2}} \frac {\mathrm{C} _ {m _ {1}} ^ {k} \mathrm{C} _ {n _ {1} - m _ {1}} ^ {m _ {1} - k}}{\mathrm{C} _ {n _ {1}} ^ {m _ {1}}} \frac {\mathrm{C} _ {m _ {2}} ^ {l} \mathrm{C} _ {n _ {2} - m _ {2}} ^ {m _ {2} - l}}{\mathrm{C} _ {n _ {2}} ^ {m _ {2}}} \sigma_ {k l} ^ {2}.
$$

进一步地, 若 $\sigma_{m_1m_2}^2 < \infty$, $n_1 + n_2 \to \infty$ 且 $n_1 / (n_1 + n_2) \to p \in (0,1)$, 则

$$
\sqrt {n _ {1} + n _ {2}} (U _ {n _ {1}, n _ {2}} - \theta) \xrightarrow {\mathrm{d}} N (0, \sigma^ {2}), \quad \sigma^ {2} = \frac {m _ {1} ^ {2}}{p} \sigma_ {1 0} ^ {2} + \frac {m _ {2} ^ {2}}{p} \sigma_ {0 1} ^ {2}.
$$

## 6.5.2 秩检验

除了 U 统计量检验方法外, 秩检验方法也是非常重要的非参数检验方法. Wilcoxon (1945) 提出秩和检验方法之后, 秩和检验和其他秩方法逐渐受到人们的重视. 秩和检验方法不考虑总体的参数和总体的分布类型, 而是对样本所代表的总体的分布和分布位置进行假设检验, 其在应用上有很大的意义. 秩检验方法是建立在秩与秩统计量基础上的非参数方法.

例 6.5.3 对于某生物实验中的对照实验, 设  $(X_{1}, Y_{1}), (X_{2}, Y_{2}), \cdots, (X_{n}, Y_{n})$ , 其中  $X_{1}, X_{2}, \cdots, X_{n}, Y_{1}, Y_{2}, \cdots, Y_{n}$  分别是实验组和对照组的结果. 假设实验组服从连续分布  $F(x)$ , 对照组的分布为  $F(x - \theta)$ . 设  $Z_{i} = Y_{i} - X_{i}$ , 则  $Z_{i}$  的分布是对称的连续分布, 对称点为  $\theta$ . 现关心实验效果  $\theta$  是否为 0, 即检验

$$
H _ {0}: \theta = 0 \quad \leftrightarrow \quad H _ {1}: \theta \neq 0.
$$

若原假设  $H_{0}:\theta=0$  成立, 则  $Z_{i}$  的取值中应接近一半的值大于 0, 一半的值小于 0; 若大部分  $Z_{i}$  的取值大于 (或小于) 0, 则可以拒绝原假设. 令  $\phi_{i}=I(Z_{i}>0)$ ,

$$
S ^ {+} = \sum_ {i = 1} ^ {n} \phi_ {i} = \# \{Z _ {i} > 0, i = 1, 2, \dots , n \}
$$

其中记号 # 表示计数. 原假设  $H_{0}$  成立时,  $\phi_{i} \sim B(1,0.5)$ , 则  $S^{+} \sim B(n,0.5)$ . 于是当  $S^{+}$  比较小或比较大时拒绝原假设, 认为  $\theta \neq 0$ . 检验临界值分别为  $B_{1-\alpha/2}(n,0.5)$  和  $B_{\alpha/2}(n,0.5)$ ,  $\alpha$  为检验水平.

在例 6.5.3 中, 所用的检验方法称为符号检验. 然而, 符号检验仅仅使用样本是正数还是负数的信息, 而没有使用样本数据值大小的信息. 为了更有效地解决对称中心  $\theta$  是否等于 0 的检验问题, 不仅应用正负号信息, 还应该使用其数值大小的信息. Wilcoxon (威尔科克森) 提出的秩和检验方法可改进符号检验方法. 为此, 下面首先介绍秩与秩统计量.

定义 6.5.2 设  $X_{1}, X_{2}, \cdots, X_{n}$  为来自连续型分布 F 的独立同分布样本，得到次序统计量  $X_{(1)} < X_{(2)} < \cdots < X_{(n)}$ . 若  $X_{i} = X_{(R_{i})}$ ，则称  $X_{i} (i = 1, 2, \cdots, n)$  在  $X_{1}, X_{2}, \cdots, X_{n}$  中的秩为  $R_{i}$ ，简称  $X_{i}$  的秩为  $R_{i}, R_{i} = 1, 2, \cdots, n$ .  $R = (R_{1}, R_{2}, \cdots, R_{n})$  以及 R 的任意可测函数称为秩统计量. 基于秩统计量的检验方法为秩检验.

由于随机样本  $X_{1}, X_{2}, \cdots, X_{n}$  来自连续型分布 F，从而以概率 1 保证，样本  $X_{1}, X_{2}, \cdots, X_{n}$  互不相等。R 为离散型随机变量，它取 n! 个值，且取  $1, 2, \cdots, n$  的任意一排列  $(r_{1}, r_{2}, \cdots, r_{n})$  的概率都是 1/n！，即 R 服从均匀分布。因此，秩统计量的分布和总体分布 F 没有关系。对于单个秩统计量  $R_{i}$ ，有

$$
R _ {i} = \sum_ {k = 1} ^ {n} I (X _ {k} \leqslant X _ {i}), i = 1, 2, \dots , n.
$$

由于 R 服从均匀分布, 单个的秩  $R_{i}(i=1,2,\cdots,n)$  也服从均匀分布:

$$
P (R _ {i} = r) = 1 / n, r = 1, 2, \dots , n,
$$

且 $R_{i}$ 和 $R_{j}(i\neq j)$ 的联合分布也是均匀分布:

$$
P (R _ {i} = r _ {1}, R _ {j} = r _ {2}) = \frac {1}{n (n - 1)}, r _ {1} \neq r _ {2}.
$$

从而, 可得 $E(R_i) = \frac{n + 1}{2}$, $\operatorname{Var}(R_i) = \frac{n^2 - 1}{12}$, $\operatorname{Cov}(R_i, R_j) = -\frac{n + 1}{12}$.

定义 6.5.3 对于随机样本  $X_{1}, X_{2}, \cdots, X_{n}$ ，设  $R_{i}^{+}$  为  $|X_{i}|$  在  $|X_{1}|, |X_{2}|, \cdots, |X_{n}|$  中的秩， $\phi_{i} = I(X_{i} > 0)$ ，则称

$$
R ^ {+} = \left(\phi_ {1} R _ {1} ^ {+}, \phi_ {2} R _ {2} ^ {+}, \dots , \phi_ {n} R _ {n} ^ {+}\right)
$$

为 $(X_{1},X_{2},\cdots,X_{n})$ 的符号秩,称

$$
W ^ {+} = \sum_ {i = 1} ^ {n} \phi_ {i} R _ {i} ^ {+}
$$

为符号秩和统计量.

由于符号秩涉及符号, 对于不同的分布 $F, \phi$ 取 0 或者 1 的情况完全不同, 因此一般的符号秩统计量应该与 $F$ 密切相关. 特别地, 若 $F$ 连续且关于 0 对称, 可以证明, $\phi_1, |X_1|, \phi_2, |X_2|, \cdots, \phi_n, |X_n|$ 相互独立, 且 $P(\phi_i = 0) = P(\phi_i = 1) = 1/2$. 应用符号秩和统计量可以做一些非参数检验. 例如, 在例 6.5.3 中, 记 $R_i$ 为 $Z_i$ 的秩, 则可以考虑符号秩和统计量:

$$
W _ {n} ^ {+} = \sum_ {i = 1} ^ {n} \phi_ {i} R _ {i}.
$$

当 $W_{n}^{+}$ 偏大或偏小时, 都可以拒绝原假设 $H_{0}$. 为了求检验的 $p$ 值和检验的临界值, 下面研究原假设 $H_{0}: \theta = 0$ 成立, 即总体的分布关于原点 0 对称时, 符号秩和检验统计量 $W_{n}^{+}$ 的分布的性质.

$W_{n}^{+}$ 服从离散型分布, 它可能取  $0,1,2,\cdots,\frac{n(n+1)}{2}$  各个值. 令  $t_{n,d}$  表示从  $1,2,\cdots,n$  这 n 个数字中任取若干个数, 其和恰为 d 的取法种数, 其中  $d=0,1,2,\cdots,\frac{n(n+1)}{2}$ . 则在总体 X 的分布是关于原点 0 对称的连续型分布时,  $R_{1}, R_{2}, \cdots, R_{n}$  给定后  $W_{n}^{+}=d$  的条件概率为

$$
\begin{array}{l} P (W _ {n} ^ {+} = d | R _ {1}, R _ {2}, \dots , R _ {n}) = P \bigg (\sum_ {i = 1} ^ {n} \phi_ {i} R _ {i} = d \bigg | R _ {1}, R _ {2}, \dots , R _ {n} \bigg) \\ = t _ {n, d} / 2 ^ {n}, \quad d = 0, 1, 2, \dots , \frac {n (n + 1)}{2}. \\ \end{array}
$$

这个条件概率和  $R_{1}, R_{2}, \cdots, R_{n}$  没有关系. 这说明在  $R_{1}, R_{2}, \cdots, R_{n}$  给定后  $W_{n}^{+} = d$  的条件概率就是  $W_{n}^{+} = d$  的概率. 由此, 对于检验水平  $\alpha$ , 即可得检验临界值.

例 6.5.3 中的配对问题可以推广至更一般的情形. 设  $X_{1}, X_{2}, \cdots, X_{m}$  为来自总体  $F(x)$  的独立同分布样本,  $Y_{1}, Y_{2}, \cdots, Y_{n}$  为来自总体  $G(x)$  的独立同分布样本, 且两总体相互独立. 令  $\gamma = P(X < Y)$ , 感兴趣的问题是检验

$$
\gamma = \frac {1}{2} \leftrightarrow \gamma \neq \frac {1}{2}. \tag {6.5.2}
$$

当  $F(x)$  为连续型对称分布且  $G(x)=F(x-\theta)$  时, 该检验问题也等价于检验

$$
\theta = 0 \quad \leftrightarrow \quad \theta \neq 0, \tag {6.5.3}
$$

其假设两个分布的类型相同, 而对称点可能不同. 若把  $X_{i}$  对应的秩相加:

$$
W _ {n} = \sum_ {k = 1} ^ {m} R _ {k}, \tag {6.5.4}
$$

其中 $(R_{1}, R_{2}, \cdots, R_{m+n})$ 为样本 $(X_{1}, X_{2}, \cdots, X_{m}, Y_{1}, Y_{2}, \cdots, Y_{n})$ 的秩统计量，则当 $\gamma$ 太大或者太小时，有理由认为 $W_{n}$ 很大或者很小。这里把 $X_{i}$ 对应的秩相加，等价地，也可以考虑把 $Y_{j}$ 对应的秩相加。从而，可以通过统计量 $W_{n}$ 来检验两总体是否相同。这种检验方法即为 Wilcoxon 秩和检验方法，称 (6.5.4) 式为 Wilcoxon 秩和统计量。拒绝域为

$$
\left\{W _ {n} \leqslant W _ {1 - \alpha / 2} (m, n) \quad \text {或} \quad W _ {n} \geqslant W _ {\alpha / 2} (m, n) \right\}.
$$

具体的临界值可参见现成的分布表. 实际上, 可以证明 $W_{n}$ 的分布关于 $\frac{1}{2} m(m + n + 1)$ 是对称的, 且 $E(W_{n}) = \frac{m(m + n + 1)}{2}, \operatorname{Var}(W_{n}) = \frac{mn(m + n + 1)}{12}$. 在样本容量较大时,

$$
W ^ {*} = \frac {W _ {n} - \frac {m (m + n + 1)}{2}}{\sqrt {\frac {m n (m + n + 1)}{1 2}}} \stackrel {\cdot} {\sim} N (0, 1). \tag {6.5.5}
$$

在 m, n 都大于等于 20 时, 近似效果已很好.

对于检验问题 (6.5.2), 也可以从 U 统计量的角度, 构造参数  $\gamma = P(X < Y)$  的 U 统计量:

$$
U _ {n} = \frac {1}{m n} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} I \left(X _ {i} <   Y _ {j}\right).
$$

这里核函数为  $\phi(x,y)=I(x<y)$ . 则根据上一小节的内容, 可得

$$
\sigma_ {1 1} ^ {2} = \mathrm{Var} [ I (X <   Y) ] = P (X <   Y) [ 1 - P (X <   Y) ] = \gamma (1 - \gamma) <   \infty ,
$$

$$
\sigma_ {0 1} ^ {2} = \mathrm{Cov} \left(I (X <   Y), I \left(X <   Y _ {1}\right)\right) = \int \left[ 1 - G (x) \right] ^ {2} \mathrm{d} F (x) - \gamma^ {2},
$$

$$
\sigma_ {1 0} ^ {2} = \mathrm{Cov} \left(I (X <   Y), I \left(X _ {1} <   Y\right)\right) = \int F (x) ^ {2} \mathrm{d} G (x) - \gamma^ {2}.
$$

当  $m+n\to\infty$  且  $m/(m+n)\to p\in(0,1)$  时，由定理 6.5.2 中两样本 U 统计量的渐近结果，有

$$
\sqrt {m + n} \left(U _ {n} - \gamma\right) \xrightarrow {\mathrm{d}} N \left(0, \sigma^ {2}\right), \sigma^ {2} = \frac {1}{p} \sigma_ {1 0} ^ {2} + \frac {1}{1 - p} \sigma_ {0 1} ^ {2}.
$$

若再用一次U统计量的方法，可以构造出 $\sigma^2$ 的相合估计 $\hat{\sigma}^2$ .由Slutsky定理，可得

$$
\frac {\sqrt {m + n} (U _ {n} - \gamma)}{\hat {\sigma} ^ {2}} \xrightarrow {\mathrm{d}} N (0, 1). \tag {6.5.6}
$$

从而, 得到检验的接受域: $A = \left\{u_{\alpha / 2} \leqslant \frac{\sqrt{m + n}(U_n - 1/2)}{\hat{\sigma}^2} \leqslant u_{1 - \alpha / 2}\right\}$. 若对于检验问题 (6.5.3), 当原假设成立时, 两个分布相同, 则可以直接计算出 $\sigma^2$, 代入即可. 这种方法即为 Mann-Whitney (曼-惠特尼) 检验方法.

此外, 还可以通过 U 统计量的工具得到秩和检验统计量 (6.5.4) 的极限分布. 对于秩统计量, 有

$$
R _ {i} = \sum_ {k = 1} ^ {m} I \left(X _ {k} \leqslant X _ {i}\right) + \sum_ {j = 1} ^ {n} I \left(Y _ {j} \leqslant X _ {i}\right), \quad i = 1, 2, \dots , m.
$$

则

$$
\begin{array}{l} W _ {n} = \sum_ {i = 1} ^ {m} R _ {i} = \sum_ {i = 1} ^ {m} \left(\sum_ {k = 1} ^ {m} I \left(X _ {k} \leqslant X _ {i}\right) + \sum_ {j = 1} ^ {n} I \left(Y _ {j} \leqslant X _ {i}\right)\right) \\ = \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} I \left(X _ {i} \leqslant X _ {j}\right) + \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} I \left(Y _ {j} \leqslant X _ {i}\right) \\ = \frac {m (m + 1)}{2} + m n - \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {n} I \left(X _ {i} <   Y _ {j}\right). \\ \end{array}
$$

因此, $W_{n} = \frac{m(m + 1)}{2} + mn(1 - U_{n})$. 由 $U_{n}$ 的极限分布 (6.5.6), 可得

$$
\sqrt {m + n} \left(1 + \frac {m + 1}{2 n} - \frac {1}{m n} W _ {n} - \gamma\right) \xrightarrow {\mathrm{d}} N (0, \sigma^ {2}).
$$

这即是经典的 Wilcoxon 两样本秩和检验.

例 6.5.4 在某小学随机采集 12 岁男童和女童各 10 名的头发样品, 检测发样中钙含量 (单位:  $\mu g/g$ ), 数据见表 6.5.1. 检验男童与女童头发中钙含量有无差异?

首先对男童和女童的数据进行正态性检验. 经检验, 在检验水平 0.05 下, 认为这两组数据都不符合正态分布. 因此, 下面考虑用非参数检验中的秩和检验方法. 把这 20 个数据放在一起得到相应的秩, 见表 6.5.1, 从而得到男童的秩和为 $W_1 = 77$, 选其作为 Wilcoxon 秩和检验统计量 $W$. 在原假设 $H_0$ 成立的情况下, $W$ 的均值和方差分别为

$$
E (W) = \frac {m (m + n + 1)}{2} = 1 0 5, \mathrm{Var} (W) = \frac {m n (m + n + 1)}{1 2} = 1 7 5.
$$

根据 (6.5.5) 式, 男童的秩和 $W = 77$ 与 $E(W)$ 之差的绝对值约为标准差的 2 倍: $(77 - 105) / 13.229 = -2.117$, 因此, 在检验水平 $\alpha = 0.05$ 下, 认为两组数据是有差异的.