$$
\mathrm{i} \frac {\partial \Psi (\boldsymbol {r} , t)}{\partial t} = \hat {H} \Psi (\boldsymbol {r}, t) 。 \tag {25-1}
$$

波函数  $\Psi(t)$  的取值是复数， $\Psi(t)$  里包含了描述该自旋体系所需要的所有状态信息。在时刻 t，体系处在某个自旋状态的概率为  $\left|\Psi(t)\right|^{2}=\Psi^{*}(t)\Psi(t)$ ，其中 “\*” 表示复共轭（知识窗 25-1）。由于我们假设在自旋空间里总是存在这么一个自旋体系，概率密度在全空间的积分必然等于 1，此即归一化的要求:

$$
\int \Psi^ {*} (\boldsymbol {r}, t) \Psi (\boldsymbol {r}, t) \mathrm{d} \boldsymbol {r} = 1,
$$

其中 $r$ 代表自旋空间变量。既然波函数里包含了自旋体系的所有状态信息，那么如何将这些信息提取出来呢？这时我们就需要对波函数施加一个合适的算符。

在核磁实验中，施加的射频场大小相对于静磁场强度可以忽略，大多数情况下 $\hat{H}$ 可被视为不随时间变化，此时薛定谔方程可以简化为如下不含时的形式:

$$
\hat {H} \Psi (\boldsymbol {r}) = E \Psi (\boldsymbol {r}) _ {\circ}
$$

根据该方程，在对波函数施加了哈密顿算符后，我们可以提取出自旋体系的能量（或者说共振频率）。

在自旋体系的量子力学描述中，除了哈密顿算符，还有两个算符特别重要，即描述自旋角动量模平方的算符 $\hat{I}^2$ 和描述自旋角动量在 $z$ 方向（即静磁场方向）分量的算符 $\hat{I}_z$ 。显然，这两个算符均可以从波函数中提取出相应的观测量，即 $\hat{I}^2\Psi = I(I + 1)\Psi$ 以及 $\hat{I}_z\Psi = m\Psi$ [参见式（5-1）和式（5-2)]。

在上述几个例子中，算符作用在波函数上得到了该波函数和某个常数的乘积。具有这样特性的波函数被称为该算符的本征函数（eigenfunction），对应的状态则称作本征态（eigenstate），而得到的常数被称为本征值（eigenvalue）。哈密顿算符的本征值即为该量子体系的能级（energy level），而哈密顿算符的本征状态则称作该体系的定态（stationary state）或者能量本征态（energy eigenstate）。

## 知识窗25-1

## 波函数的概率解释

薛定谔受到德布罗意的波粒二象性的启发，在1926年正式发表了薛定谔方程。由于该方程与经典物理学的波动方程形似，因此薛定谔将方程中的 $\Psi$ 称为波函数。有意思的是，薛定谔本人最初对波函数的物理意义也不清楚。1926年夏天，玻恩第一次提出了波函数的概率解释，即 $\Psi$ 的模平方代表粒子处在某状态的概率。这一解释破除了经典物理学的决定论思想，诠释了量子力学的统计本性，成为量子力学的基本假设之一。除了对波函数的统计诠释，玻恩还与约尔当以及海森堡共同创建了矩阵力学，而矩阵力学和薛定谔的波动力学是量子力学的不同表述形式。1932年海森堡单独获得诺贝尔物理学奖，第二年去信给玻恩表示“问心有愧”，因为工作是由三人共同完成的。而玻恩本人直到1954年才与博特共享了诺贝尔物理学奖，此时他已年过七旬，所以这是一个名副其实的迟到的诺奖。

我们先考虑一种简单的情况，即体系里只有一个自旋量子数为 $1/2$ 的原子核。这种情形下，存在两个本征波函数，记作 $\Psi_{\alpha}$ 和 $\Psi_{\beta}$，对应的自旋磁量子数分别为 $1/2$ 和 $-1/2$。可以证明这两个本征波函数是正交的，即 $\int \Psi_{\alpha}^{*} \Psi_{\beta} \mathrm{d}\sigma = 0$，也就是说，自旋向上和自旋向下是截然分明的状态，没有重叠的部分。一般情形下，$1/2$ 自旋核的波函数可以表示为两个本征波函数的线性叠加:$\Psi = c_{\alpha} \Psi_{\alpha} + c_{\beta} \Psi_{\beta}$。假设对单个原子核的能量进行一次测量，如果该原子核处于某个能量本征态，那么每次测量总是得到该本征态对应的能量值；如果原子核处于两个本征态的叠加，那么单次测量得到的将是两个能级中的一个，处在 $\alpha$ 能级的概率是 $|c_{\alpha}|^2$，处在 $\beta$ 能级的概率是 $|c_{\beta}|^2$。如果是对宏观样品进行能量测量，那么测量值（或者说能量算符的期望值）是 $\langle H \rangle = \int \Psi^{*}(t) \hat{H} \Psi(t) \mathrm{d}\sigma = E_{\alpha} |c_{\alpha}|^2 + E_{\beta} |c_{\beta}|^2$，注意这里利用了 $\hat{H} \Psi_{\alpha} = E_{\alpha} \Psi_{\alpha}$ 和 $\hat{H} \Psi_{\beta} = E_{\beta} \Psi_{\beta}$。如果我们测量的不是能量，而是其它观测量 $Q$，那么只要把 $\hat{H}$ 替换为 $Q$ 对应的算符 $\hat{Q}$，上述处理方式同样适用。

上面讨论的本征值和本征函数很容易令人联想到线性代数里的本征值和本征向量，它们确实有内在联系。要建立这种联系，我们需要用本征波函数作为基底，对自旋体系的状态空间进行线性化。要达到这个目的，我们首先引入狄拉克符号（Dirac notation）来简化波函数的表示形式，即波函数 $\Psi$ 可以用 $|\Psi\rangle$ 表示，而其复共轭 $\Psi^{*}$ 可以用 $\langle \Psi|$ 表示，其中“$|\rangle$”称为右矢符号（ket），“$||$”称为左矢符号（bra）。使用狄拉克符号，一个1/2自旋核的波函数可以写成下面的形式:

$$
\mid \Psi \rangle = c _ {\alpha} \mid \alpha \rangle + c _ {\beta} \mid \beta \rangle ,
$$

其中 $|\alpha\rangle$ 和 $|\beta\rangle$ 分别代表 $\alpha$ 态和 $\beta$ 态的本征函数。

左矢和右矢的乘积则代表积分操作，例如 $\int \Psi_1^*\Psi_2\mathrm{d}\sigma = \langle \Psi_1|\Psi_2\rangle$ 。而观测量 $Q$ 的期望值可以写成 $\langle Q\rangle = \int \Psi^{*}(t)\hat{Q}\Psi (t)\mathrm{d}\sigma = \langle \Psi |\hat{Q} |\Psi \rangle$ 。以 $|\alpha \rangle$ 和 $|\beta \rangle$ 作为自旋空间的正交基，那么波函数就可以表示为列向量，而波函数的复共轭则用行向量表示，其中符号“†”代表对向量或者矩阵的共轭转置运算:

![](images/page_737_image_7.jpg)

<details>
<summary>text_image</summary>

y
u=[3/2]=3e_i+2e_j
e_j=[0/1]
O
x
e_i=[1/0]
</details>

图25-1 二维向量在平面直角坐标系中的表示方法

$$
\left\{ \begin{array}{l} | \alpha \rangle = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right], \quad | \beta \rangle = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right], \quad | \Psi \rangle = \left[ \begin{array}{c} c _ {\alpha} \\ c _ {\beta} \end{array} \right] _ {\circ} \\ \langle \alpha | = [ 1 \quad 0 ], \langle \beta | = [ 0 \quad 1 ], \langle \Psi | = [ c _ {\alpha} ^ {*} \quad c _ {\beta} ^ {*} ] = | \Psi \rangle^ {\dagger}. \end{array} \right.
$$

在与线性空间建立了联系后，一个波函数就可以类比为二维平面中的一个向量，而二维平面由两个正交基 $[1, 0]^{\mathrm{T}}$ 和 $[0, 1]^{\mathrm{T}}$ 来定义，分别是 $x$ 轴和 $y$ 轴的单位向量，如图25-1所示。

同理，归一化条件也可以用向量乘法来表达，即波函数所对应向量的模平方等于1:

$$
\langle \Psi | \Psi \rangle = \left[ \begin{array}{l l} c _ {\alpha} ^ {*} & c _ {\beta} ^ {*} \end{array} \right] \left[ \begin{array}{l} c _ {\alpha} \\ c _ {\beta} \end{array} \right] = | c _ {\alpha} | ^ {2} + | c _ {\beta} | ^ {2} = 1 _ {\circ}
$$

## (2) 自旋算符的矩阵表示

当把波函数用向量表示后，很自然地，对波函数做某种运算的算符就可以用矩阵来表示。对于一个1/2自旋核来说，算符就表示为一个 $2\times2$ 的矩阵。算符的本征值和本征函数对应着矩阵的本征值和本征向量。我们可以通过两个本征向量—— $|\alpha\rangle$ 和 $|\beta\rangle$，以列向量和行向量相乘的形式人为地定义下面四种算符:

$$
\left\{ \begin{array}{l} | \alpha \rangle \langle \alpha | = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] [ 1 \quad 0 ] = \left[ \begin{array}{c c} 1 \times 1 & 1 \times 0 \\ 0 \times 1 & 0 \times 0 \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \end{array} \right] \equiv \hat {I} ^ {\alpha}, \\ | \alpha \rangle \langle \beta | = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right] [ 0 \quad 1 ] = \left[ \begin{array}{c c} 1 \times 0 & 1 \times 1 \\ 0 \times 0 & 0 \times 1 \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right] \equiv \hat {I} ^ {+}, \\ | \beta \rangle \langle \alpha | = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] [ 1 \quad 0 ] = \left[ \begin{array}{c c} 0 \times 1 & 0 \times 0 \\ 1 \times 1 & 1 \times 0 \end{array} \right] = \left[ \begin{array}{c c} 0 & 0 \\ 1 & 0 \end{array} \right] \equiv \hat {I} ^ {-}, \\ | \beta \rangle \langle \beta | = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] [ 0 \quad 1 ] = \left[ \begin{array}{c c} 0 \times 0 & 0 \times 1 \\ 1 \times 0 & 1 \times 1 \end{array} \right] = \left[ \begin{array}{c c} 0 & 0 \\ 0 & 1 \end{array} \right] \equiv \hat {I} ^ {\beta}. \end{array} \right.
$$

我们先考察 $\hat{I}^{\alpha}$ 和 $\hat{I}^{\beta}$，将这两个算符分别作用于本征函数 $|\alpha\rangle$ 和 $|\beta\rangle$:

$$
\begin{array}{l} \left\{ \begin{array}{l} \hat {I} ^ {\alpha} | \alpha \rangle = | \alpha \rangle \langle \alpha | \cdot | \alpha \rangle = | \alpha \rangle \\ \hat {I} ^ {\alpha} | \beta \rangle = | \alpha \rangle \langle \alpha | \cdot | \beta \rangle = 0 \end{array} , \right. \\ \left\{ \begin{array}{l} \hat {I} ^ {\beta} | \alpha \rangle = | \beta \rangle \langle \beta | \cdot | \alpha \rangle = 0 \\ \hat {I} ^ {\beta} | \beta \rangle = | \beta \rangle \langle \beta | \cdot | \beta \rangle = | \beta \rangle^ {\circ} \end{array} \right. \\ \end{array}
$$

由此可见，$\hat{I}^{\alpha}$ 的本征函数为 $|\alpha\rangle$，$\hat{I}^{\alpha}$ 从 $|\alpha\rangle$ 提取出的信息为 1（即 $100\%$），从 $|\beta\rangle$ 提取出的信息为 0（即 $0\%$）；$\hat{I}^{\beta}$ 的本征函数为 $|\beta\rangle$，$\hat{I}^{\beta}$ 从 $|\alpha\rangle$ 提取出的信息为 0（即 $0\%$），从 $|\beta\rangle$ 提取出的信息为 1（即 $100\%$）。因此，$\hat{I}^{\alpha}$ 算符代表 $\alpha$ 态，$\hat{I}^{\beta}$ 算符代表 $\beta$ 态，如图 25-2 所示。这两个算符合称为投影算符（projection operator）。

我们再考察 $\hat{I}^{+}$ 和 $\hat{I}^{-}$，同样将它们分别作用于 $|\alpha\rangle$ 和 $|\beta\rangle$:

$$
\begin{array}{l} \left\{ \begin{array}{l} \hat {I} ^ {+} | \alpha \rangle = | \alpha \rangle \langle \beta | \cdot | \alpha \rangle = 0 \\ \hat {I} ^ {+} | \beta \rangle = | \alpha \rangle \langle \beta | \cdot | \beta \rangle = | \alpha \rangle , \end{array} \right. \\ \left\{ \begin{array}{l} \hat {I} ^ {-} | \alpha \rangle = | \beta \rangle \langle \alpha | \cdot | \alpha \rangle = | \beta \rangle \\ \hat {I} ^ {-} | \beta \rangle = | \beta \rangle \langle \alpha | \cdot | \beta \rangle = 0 \end{array} \right. 。 \\ \end{array}
$$

由此可见，$\hat{I}^{+}$会把 $\beta$ 态转化为 $\alpha$ 态，而 $\hat{I}^{-}$会把 $\alpha$ 态转化为 $\beta$ 态。从 $\beta$ 态到 $\alpha$ 态，磁量子数升高一个单位，因此 $\hat{I}^{+}$称作升算符（raising operator）；从 $\alpha$ 态到 $\beta$ 态，磁量子数降低一个单位，因此 $\hat{I}^{-}$称作降算符（lowering operator）。$\hat{I}^{+}$代表从高能级向低能级的跃迁，而 $\hat{I}^{-}$代表从低能级向高能级的跃迁，如图25-3所示。

$\hat{I}^{\alpha}$ 、 $\hat{I}^{\beta}$ 、 $\hat{I}^{+}$ 和 $\hat{I}^{-}$ 这四个算符矩阵彼此正交，构成了一个完备的算符空间。它们的非零元分别占据了 $2\times 2$ 的方阵的四个位置。根据四个算符的物理意义可知，方阵的主对角元代表着分布在两个能级上原子核的丰度（population），副对角元代表着能级跃迁导致的相位相干性（coherence），即核磁信号:

$$
\left[ \begin{array}{c c} \hat {I} ^ {\alpha} & \hat {I} ^ {+} \\ \hat {I} ^ {-} & \hat {I} ^ {\beta} \end{array} \right] \circ
$$

![](images/page_738_image_12.jpg)

图 25-2 算符 $\hat{I}^{\alpha}$ 和 $\hat{I}^{\beta}$ 在能级图上的表现形式

![](images/page_738_image_14.jpg)

<details>
<summary>chemical</summary>

Energy level diagrams showing electron transitions labeled Eα and Eβ with spin states i⁺ and i⁻
</details>

图 25-3 算符 $\hat{I}^{+}$ 和 $\hat{I}^{-}$ 在能级图上的表现形式

算符矩阵还可以用在笛卡尔坐标系中，这在分析核磁实验时往往更为方便。下面我们从 $\hat{I}^{\alpha}$ 、 $\hat{I}^{\beta}$ 、 $\hat{I}^{+}$ 和 $\hat{I}^{-}$ 四个算符出发来推导笛卡尔坐标系中的四个算符。首先把 $\hat{I}^{\alpha}$ 和 $\hat{I}^{\beta}$ 进行重新组合。$\hat{I}^{\alpha} + \hat{I}^{\beta}$ 代表两个能级上丰度之和，值总是为1（即 $100\%$），可以用单位矩阵 $\hat{E}$ 表示，那么有 $(\hat{I}^{\alpha} + \hat{I}^{\beta}) / 2 = \hat{E} / 2$。$\hat{I}^{\alpha} - \hat{I}^{\beta}$ 代表处于 $\alpha$ 态和 $\beta$ 态的原子核的丰度之差，所以 $(\hat{I}^{\alpha} - \hat{I}^{\beta}) / 2$ 表示 $\alpha$ 态的丰度高于 $50\%$ 的部分或者 $\beta$ 态丰度低于 $50\%$ 的部分。根据核磁共振的矢量模型，这个值与静磁场激发出的宏观磁化矢量成正比，我们把它记作 $\hat{I}_z$。由此，我们得到了两个新的算符，$\hat{E} / 2$ 和 $\hat{I}_z$。通过矩阵的加减运算可以得到 $\hat{E} / 2$ 和 $\hat{I}_z$ 的矩阵形式:

$$
\left\{ \begin{array}{l} \frac {\hat {I} ^ {\alpha} + \hat {I} ^ {\beta}}{2} = \left(\left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 1 \end{array} \right]\right) / 2 = \frac {1}{2} \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \equiv \frac {1}{2} \hat {E}, \\ \frac {\hat {I} ^ {\alpha} - \hat {I} ^ {\beta}}{2} = \left(\left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \end{array} \right] - \left[ \begin{array}{c c} 0 & 0 \\ 0 & 1 \end{array} \right]\right) / 2 = \frac {1}{2} \left[ \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right] \equiv \hat {I} _ {z _ {\circ}} \end{array} \right.
$$

接着我们对 $\hat{I}^{+}$ 和 $\hat{I}^{-}$ 进行重新组合。 $\hat{I}^{+}$ 代表着从高能级到低能级的跃迁，对应正的频率，即逆时针转动； $\hat{I}^{-}$ 代表着从低能级到高能级的跃迁，对应负的频率，即顺时针转动。正向和反向的转动组合起来能得到简谐振动，如图25-4所示。

图 25-4 两个沿相反方向转动的矢量可以合成为一个简谐振动的矢量

（A）如果两个转动矢量的初始位置都在正 $x$ 轴，那么得到的是在 $x$ 轴上的简谐振动。（B）如果两个转动矢量的初始位置都在正 $y$ 轴，那么得到的是在 $y$ 轴上的简谐振动。

![](images/page_739_image_7.jpg)

由此，我们就得到了 $\hat{I}_{x}$ 和 $\hat{I}_{y}$ :

$$
\left\{ \begin{array}{l} \frac {\hat {I} ^ {+} + \hat {I} ^ {-}}{2} = \left(\left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 1 & 0 \end{array} \right]\right) / 2 = \frac {1}{2} \left[ \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right] \equiv \hat {I} _ {x}, \\ \frac {\hat {I} ^ {+} - \hat {I} ^ {-}}{2 \mathrm{i}} = \left(\left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right] - \left[ \begin{array}{c c} 0 & 0 \\ 1 & 0 \end{array} \right]\right) / 2 \mathrm{i} = \frac {1}{2 \mathrm{i}} \left[ \begin{array}{c c} 0 & 1 \\ - 1 & 0 \end{array} \right] \equiv \hat {I} _ {y ^ {\circ}} \end{array} \right.
$$

其中，$\hat{I}_y$ 项的分母多了一个 $\mathrm{i}$ 。这一点不难理解，因为沿 $x$ 轴的简谐振动和沿 $y$

轴的简谐振动只有在相位差为 $90^{\circ}$ 时才能合成为转动，即 $\hat{I}^{+} = \hat{I}_{x} + \mathrm{i}\hat{I}_{y},\hat{I}^{-} = \hat{I}_{x} - \mathrm{i}\hat{I}_{y}$ ，而虚数i就代表 $90^{\circ}$ 相移。

这四个笛卡尔坐标系算符同样构成了一个完备的算符空间。它们在能级图上对应的表示见图25-5。

当体系中有两个自旋核时，算符的矩阵形式拓展为 $4 \times 4$ ，可以由两个大小为 $2 \times 2$ 的算符矩阵进行外积获得。

![](images/page_739_image_14.jpg)

<details>
<summary>text_image</summary>

Eβ
½E
îz
îx
îy
Eu
</details>

图 25-5 笛卡尔坐标系下的四个算符在能级图上的表现形式  $\hat{E}/2$  和  $\hat{I}_{z}$  代表自旋在两个能级上丰度的极化状态，其中空心圆圈表示丰度低于平均值，实心圆表示丰度高于平均值，没有圆圈代表丰度为平均值（即 50%）。 $\hat{I}_{x}$  和  $\hat{I}_{y}$  代表向上跃迁和向下跃迁的混合态，其中  $\hat{I}_{y}$  的虚线表示  $90^{\circ}$  的相移。

我们以 $I$ 和 $S$ 分别代表第一个和第二个自旋核。基于笛卡尔坐标系下的四个基算符 $\hat{E} / 2$ 、 $\hat{I}_z$ 、 $\hat{I}_x$ 和 $\hat{I}_y$ ，可以得到如下16个双自旋体系的标准化基算符\*: $\hat{E} / 2$ 、 $\hat{S}_z$ 、 $\hat{S}_x$ 、 $\hat{S}_y$ 、 $\hat{I}_z$ 、 $2\hat{I}_z\hat{S}_z$ 、 $2\hat{I}_z\hat{S}_x$ 、 $2\hat{I}_z\hat{S}_y$ 、 $\hat{I}_x$ 、 $2\hat{I}_x\hat{S}_z$ 、 $2\hat{I}_x\hat{S}_x$ 、 $2\hat{I}_x\hat{S}_y$ 、 $\hat{I}_y$ 、 $2\hat{I}_y\hat{S}_z$ 、 $2\hat{I}_y\hat{S}_x$ 、 $2\hat{I}_y\hat{S}_y$ 。例如，$2\hat{I}_z\hat{S}_y$ 和 $\hat{I}_z$ 可以按照如下的方法获得:

$$
2 \hat {I} _ {z} \hat {S} _ {y} = 2 \times \frac {1}{2} \left[ \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right] \textcircled {\times} \frac {1}{2} \left[ \begin{array}{c c} 1 & - \mathrm{i} \\ \mathrm{i} & 0 \end{array} \right] = \frac {1}{2} \left[ \begin{array}{c c c c} 0 & - \mathrm{i} & 0 & 0 \\ \mathrm{i} & 0 & 0 & 0 \\ 0 & 0 & 0 & \mathrm{i} \\ 0 & 0 & - \mathrm{i} & 0 \end{array} \right],
$$

$$
\hat {I} _ {z} = \hat {I} _ {z} \otimes \hat {E} = \frac {1}{2} \left[ \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right] \otimes \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] = \frac {1}{2} \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & - 1 & 0 \\ 0 & 0 & 0 & - 1 \end{array} \right] 。
$$

类似地，$\hat{I}^{\alpha}$、$\hat{I}^{\beta}$、$\hat{I}^{+}$和$\hat{I}^{-}$这四个基算符也可以生成16个双自旋体系的基算符，此处不再赘述。

和单自旋体系类似，双自旋体系的基算符也可以用能级图来展示，图25-6给出了部分算符的能级示意图。注意 $\hat{S}_z = \hat{E}\hat{S}_z = (\hat{I}^\alpha +\hat{I}^\beta)\hat{S}_z$ ， $2\hat{I}_z\hat{S}_z = \frac{(\hat{I}^\alpha - \hat{I}^\beta)(\hat{S}^\alpha - \hat{S}^\beta)}{2} = \frac{1}{2} (\hat{I}^\alpha \hat{S}^\alpha -\hat{I}^\alpha \hat{S}^\beta -\hat{I}^\beta \hat{S}^\alpha +\hat{I}^\beta \hat{S}^\beta)$ 。而像 $2\hat{I}_y\hat{S}_x$ 这样的算符，也是进行类似的展开后再绘制能级示意图。

综上所述，单自旋体系存在4种基算符，而双自旋体系存在16种基算符。无论是单自旋还是双自旋体系，其任意一个状态都可以表示为相应基算符的线性叠加，或者说表示为相应能级示意图的线性叠加。而后者正是自旋算符的物理图像。

## （3）核磁共振的哈密顿算符和密度矩阵

如前文所述，在核磁共振中最重要的算符是哈密顿算符。哈密顿算符可以用上面

![](images/page_740_image_10.jpg)

图 25-6 部分双自旋体系的算符在能级图上的表现形式

$\hat{S}_z$ 和 $2\hat{I}_z\hat{S}_z$ 代表自旋的极化状态，其中空心圆圈表示丰度低于平均值，实心圆表示丰度高于平均值。$\hat{I}^{+}$、$\hat{S}_y$、$\hat{I}^{-}\hat{S}^{\beta}$ 和 $\hat{I}^{+}\hat{S}^{-}$ 代表能级间的跃迁。

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* 部分算符前的系数2是出于归一化的要求。</span></small>

介绍的基算符来表示，常用的哈密顿算符包括自由进动（free precession）、脉冲和J耦合等类型，如表25-1所示。

表 25-1 核磁共振中常用的哈密顿算符

| 算符类型 | 算符表示形式 |
| --- | --- |
| 自由进动(化学位移) | $\hat{H}_{\text{Zeeman}} = \omega_0 \hat{I}_z$(实验室坐标系)$= \Omega_0 \hat{I}_z$(旋转坐标系) |
| 脉冲 | $\hat{H}_{\text{pulse}} = \omega_1 \hat{I}_x (x\text{-pulse})$或 $\omega_1 \hat{I}_y (y\text{-pulse})$ |
| J耦合 | $\hat{H}_J = 2\pi J \hat{I}_z \hat{S}_z$(弱耦合近似) |

上面介绍的算符是用于描述单个分子中自旋体系的状态，实际的核磁样品里含有大量的分子。而核磁实验操纵和检测的是宏观磁化矢量，是全体分子中某个磁矩的宏观平均。单个分子中某个自旋核的微观磁矩总是与它的自旋角动量成正比，例如 $\mu_z\propto \hat{I}_z$ 、 $\mu_x\propto \hat{I}_x$ （参见5.2.2节）。假设单个自旋核的波函数可以表示为 $[c_{\alpha},c_{\beta}]^{\mathrm{T}}$ ，那么我们可以定义这样一个算符来表示该自旋核的状态:

$$
\mid \Psi \rangle \langle \Psi \mid = \left[ \begin{array}{c} c _ {\alpha} \\ c _ {\beta} \end{array} \right] [ c _ {\alpha} ^ {*} \quad c _ {\beta} ^ {*} ] = \left[ \begin{array}{c c} c _ {\alpha} c _ {\alpha} ^ {*} & c _ {\alpha} c _ {\beta} ^ {*} \\ c _ {\beta} c _ {\alpha} ^ {*} & c _ {\beta} c _ {\beta} ^ {*} \end{array} \right] 。
$$

对核磁样品的测量相当于对样品中所有感兴趣的自旋核所对应的算符取了系综平均（ensemble average），由此我们就得到了密度算符，其矩阵形式如下:

$$
\hat {\rho} = \overline {{| \psi \rangle \langle \psi |}} = \left[ \begin{array}{c c} \overline {{c _ {\alpha} c _ {\alpha} ^ {*}}} & \overline {{c _ {\alpha} c _ {\beta} ^ {*}}} \\ \overline {{c _ {\beta} c _ {\alpha} ^ {*}}} & \overline {{c _ {\beta} c _ {\beta} ^ {*}}} \end{array} \right] 。
$$

以单自旋体系为例（双自旋体系也可类似处理），在采用笛卡尔坐标系下的基算符时，密度矩阵可以写成

$$
\hat {\rho} (t) = a _ {\mathrm{E}} \hat {E} + a _ {x} (t) \hat {I} _ {x} + a _ {y} (t) \hat {I} _ {y} + a _ {z} (t) \hat {I} _ {z}, \tag {25-2}
$$

其中， $a_{\mathrm{E}}$ 对应体系里自旋核的总数，是一个不随时间变化的常数，我们不需要关心。$a_{x}$ 、 $a_{y}$ 、 $a_{z}$ 对应宏观磁化矢量的三个分量，即

$$
M _ {x} \propto a _ {x} (t), M _ {y} \propto a _ {y} (t), M _ {z} \propto a _ {z} (t) 。
$$

在得到某个自旋状态的密度矩阵 $\hat{\rho}$ 后，观测量 $Q$ 的期望值可以通过如下公式计算:

$$
\langle Q \rangle = \mathrm{tr} \{\hat {\rho} \hat {Q} \} = \mathrm{tr} \{\hat {Q} \hat {\rho} \},
$$

其中，tr代表矩阵的迹。在下个小节，我们将讨论在核磁实验中密度矩阵如何随时间演化。

## 25.1.2 核磁实验的脉冲序列

在运行核磁实验的时候，我们首先把核磁样品加载到磁体中央的探头线圈中，然后施加核磁脉冲序列（pulse sequence），最后检测探头线圈中产生的核磁信号。核磁脉冲序列是核磁实验的灵魂，由一系列受到精确控制的脉冲（pulse）和时间延迟（delay）组成，很多核磁实验的脉冲序列还会包含梯度场（gradient field）。在核磁实验开始前，样品里的自旋体系处于平衡状态，外加磁场在样品中激发出宏观磁化矢量 $M_{z}$，根据式（25-2），其对应的密度矩阵是 $\hat{\rho}(0) = \hat{I}_{z}$。因此核磁实验本质上就是从密度矩阵 $\hat{I}_{z}$ 出发，经过脉冲序列的演化后得到可测量的新的密度矩阵。

那么密度矩阵如何在脉冲序列的作用下演化呢？在知识窗5-2中，我们从牛顿运动方程推导出了经典力学框架下描述核磁共振现象的布洛赫方程。类似地，我们也可以从含时的薛定谔方程[式（25-1）]出发推导出量子力学框架下描述核磁共振现象的刘维尔-冯·诺依曼方程（Liouville-von Neumann equation）:

$$
\frac {\mathrm{d}}{\mathrm{d} t} \hat {\rho} = - \mathrm{i} [ \hat {H}, \hat {\rho} ] _ {\circ}
$$

方程里出现的中括号代表算符的对易运算，其定义为

$$
[ \hat {A}, \hat {B} ] = \hat {A} \hat {B} - \hat {B} \hat {A} _ {\circ}
$$

这个微分方程的解是

$$
\hat {\rho} (t) = \mathrm{e} ^ {- \mathrm{i} \hat {H} t} \hat {\rho} (0) \mathrm{e} ^ {\mathrm{i} \hat {H} t},
$$

其中 $\hat{H}$ 是核磁脉冲序列运行过程中作用于自旋体系的哈密顿算符（表25-1）。这个公式的形式是 $\hat{\rho}(0)$ 被夹在两个互逆的指数算符中间，因此又称为三明治公式（sandwich formula）。在计算密度矩阵的演化时，需要把脉冲序列按脉冲和时间延迟分割成多个时间区域，各区域中 $\hat{H}$ 保持不变。在每个区域运用刘维尔-冯·诺依曼方程，即可从始态密度算符推导出终态密度算符。这样从 $\hat{\rho}(0) = \hat{I}_z$ 出发，依次运用该方程，即可获得核磁脉冲结束时待测核磁信号的密度算符。

最后，我们以HSQC实验为例，简要分析其脉冲序列（图25-7）。该脉冲序列可以分为三段:从（1）到（2），宏观磁化矢量从自旋核H传递到N；从（2）到（3），磁化矢量在 ${}^{15}\mathrm{N}$ 上进行时长为 $t_1$ 的演化；从（3）到（4），磁化矢量从自旋核N传递到H。最后在 $t_2$ 上采集FID。下面我们对这三个阶段逐一进行说明。

从（1）到（2）:

初始状态的密度矩阵算符是 $H_{z}$，经过第一个 $90^{\circ}$ 脉冲后变成 $-H_{y}$。在随后的 $2\tau_{1}$ 的时间中，由于两个同时施加的 $180^{\circ}$ 脉冲的存在，无须考虑化学位移的演化，在J耦合哈密顿量的作用下算符转化为 $2H_{x}N_{z}$。最后，两个同时施加的 $90^{\circ}$ 脉冲使得算符变为 $2H_{z}N_{y}$。在该算符中，H保持在 $z$ 轴而N转到 $xy$ 平面做进动，因此 $2H_{z}N_{y}$ 和 $N_{y}$

![](images/page_742_image_13.jpg)

<details>
<summary>text_image</summary>

H
τ₁ τ₁ y
τ₂ τ₂ t₂
N
(1) (2) (3) (4)
t₁
</details>

图 25-7 NH-HSQC 的脉冲序列

窄竖条代表 $90^{\circ}$ 脉冲，宽竖条代表 $180^{\circ}$ 脉冲，浅蓝色实心横条代表去耦脉冲。时长$\tau_{1}$ 和 $\tau_{2}$ 均被设置为 $1 / (4J)$ 其中 $J$ 为 ${}^{1}\mathrm{H}$ 和 ${}^{15}\mathrm{N}$ 之间的J耦合常数。

一样都代表转移到 N 上的磁化矢量。

从（2）到（3）:

在此过程中由于N上未施加 $180^{\circ}$ 脉冲，因此 $2H_{z}N_{y}$ 将在N上进行化学位移的演化，而J耦合的演化无须考虑。算符经演化变成 $2H_{z}N_{y}\cos \Omega_{\mathrm{N}}t_{1}$，此时我们称算符带上了 ${}^{15}\mathrm{N}$ 化学位移的标签。

从（3）到（4）:

这是第一阶段的逆过程，算符 $2H_{z}N_{y}$ 演化为 $H_{x}$，再加上前一阶段添加的 ${}^{15}\mathrm{N}$ 化学位移的标签，在（4）这个时间点密度矩阵算符成为 $H_{x}\cos \Omega_{\mathrm{N}}t_{1}$。

最后就是FID的采集，即 $H_{x}$ 在 $xy$ 平面进动，为算符进一步带上了 ${}^{1}\mathrm{H}$ 化学位移的标签。由于在此阶段对N进行去耦，可忽略J耦合的影响。由此我们就同时测量到了N上的共振频率和H上的共振频率。

蛋白质的所有NH基团在脉冲序列的作用下同时完成上述过程，最终我们就得到了二维HSQC谱。

## 25.1.3 核磁共振的弛豫和构象动态研究

生物大分子在溶液中广泛存在从皮秒到秒以及更慢时间尺度的构象动态（知识窗25-2）。构象的动态性与生物大分子的功能息息相关，例如酶的催化、配体的识别、折叠与去折叠、别构调控、生物大分子机器的装配等。与X射线晶体衍射和冷冻电镜方法相比，核磁共振方法在研究生物大分子构象动态方面有显著的优势，在各个

## 知识窗25-2

## 蛋白质构象动态的早期研究

物理学家费曼（Richard Feynman，1918—1988）曾经说过，生命所做的一切都可以通过原子的抖动（jiggling）和摇摆（wiggling）来理解。生物大分子的功能不仅由其结构决定，也与其构象动态息息相关。在20世纪中叶蛋白质晶体结构解析方法建立后的一段时期，蛋白质分子被描绘成具有比较刚性的静态结构。到了70年代，蛋白质内在的动态性通过计算和实验方法的发展被逐步揭示出来。在计算层面，卡普拉斯（Martin Karplus，1930—2024）和合作者在1977年首次将分子动力学模拟应用在蛋白质上。该模拟以包含58个氨基酸残基的BPTI蛋白为对象，尽管使用的力场比较粗糙，在真空中进行，且时长也仅仅只有9.2皮秒，但这一开创性的工作改变了我们对于蛋白质结构相对刚性的看法。在实验层面，核磁波谱学家在同一时期通过检测BPTI蛋白和溶菌酶上芳香残基侧链亚氨基的'H谱峰，发现这些芳香环存在翻转运动。由于芳香环常常位于蛋白质的疏水核心，这些结果表明蛋白质分子很可能广泛存在着内部运动。此后，随着同位素标记方法和多维核磁谱的出现，以及脉冲序列和硬件的不断进步，核磁共振技术在生物大分子构象动态研究中发挥了关键作用，并且通过与分子动力学模拟的深度融合，为这一领域的研究提供了强有力的工具。

![](images/page_744_image_2.jpg)

<details>
<summary>text_image</summary>

蛋白质的运动
芳香环翻转
甲基旋转 侧链摆动 二硫键反转
环区快速摆动 环区慢速摆动 化学反应动力学
化学键振动 整体翻转 局部折叠/去折叠 整体折叠/去折叠
10^-12 10^-9 10^-6 10^-3 10^0 10^3
运动的时间尺度/s
自旋弛豫（R₁, R₂, NOE） 弛豫弥散和化学交换饱和转移 ZZ-交换谱 实时 NMR
残余偶极耦合(RDC) 氢气交换
</details>

核磁共振方法

时间尺度上都有相应的核磁方法来测量（图 25-8）。

这里我们重点介绍两类这样的方法，一类是自旋弛豫方法（spin relaxation）（参见5.3.1节），另一类是基于构象交换的测量方法。前者通过对 $R_{1}$ 、 $R_{2}$ 、NOE等自旋弛豫速率的测量，可以探测皮秒到纳秒时间范围的构象动态。后者可以检测微秒到秒时间范围的构象转换，尤其是丰度低、寿命短的瞬态构象，其中包括弛豫弥散（relaxation dispersion, RD）、化学交换饱和转移（chemical exchange saturation transfer, CEST）以及ZZ-交换谱（ZZ-exchange spectroscopy）等方法。仍以前文中提到的蛋白激酶为例。酶的催化功能与其结构上的柔性息息相关，而自旋弛豫方法可以揭示该蛋白质中各个残基内部运动的幅度和快慢，有助于我们深入理解其功能。此外，蛋白激酶在生理条

件下有时候存在一个或多个低丰度构象。某些疾病相关突变或者配体结合通过改变酶蛋白在多种构象间的平衡来调控其生理功能，因此通过弛豫弥散等方法对这些低丰度构象进行原子分辨率的测量具有重要的生物学意义。

## (1) 自旋弛豫方法

$^{15}$ N 的  $R_{1}/R_{2}/NOE$  是在蛋白质中应用最为普遍的自旋弛豫方法。要理解这种方法，我们需要先解释自旋弛豫是如何与蛋白质的运动产生关联的。我们以一个包含 76 个氨基酸残基的泛素蛋白为例，这个蛋白质在水溶液中的运动过程可以通过分子动力学模拟来获得（图 25-9）。对于这类折叠得很好的蛋白质来说，存在两种运动:一种是在水溶液里随机的整体翻转运动（overall tumbling），另一种是分子的内部运动（internal motion）。在两种运动的作用下，蛋白质的每个 N—H 键都在不停地做重定向运动（reorientation）。自旋弛豫方法的目的就是获取每个 N—H 键重定向运动的幅度和快慢。

分子运动与自旋弛豫速率有密切关系。弛豫过程实际上是自旋体系从非平衡态回到平衡态的过程。在这个过程中，除了外加的静磁场，原子核还会感受到分子运动所导致的附加磁场的波动。这种附加磁场的来源主要有两个:一个是空间上邻近的自旋核对所测原子核的偶极相互作用（dipolar interaction），即邻近核发出的磁场作用在测量核上（图25-10A）；另一个是化学位移各向异性（chemical shift anisotropy，CSA），即测量核周围电子分布对静磁场的屏蔽作用（图25-10B）。这两种作用都受到分子运动的调制，因此产生的附加磁场也随着分子运动而产生波动。这种附加磁场的波动包含了不同的频率分量，有些频率分量正好与 $^{15}$ N所在自旋体系中的能级差匹配，因此能够帮助自旋体系更快地回复到平衡态。换句话说，分子运动导致了附加磁场的波动，而这种波动包含的某些频率分量对弛豫速率产生了贡献。所以，通过分析测量到的弛豫速率，我们就可以推导出分子的运动情况。

图25-8 核磁共振可以在原子分辨率上表征生物大分子跨越十多个数量级时间尺度的运动这里以蛋白质分子为例，时间轴上方是蛋白质在各个时间尺度上的运动，下方是适用的核磁共振技术。

![](images/page_744_image_11.jpg)

<details>
<summary>natural_image</summary>

3D ribbon diagram of a protein structure with alpha helices and beta sheets (no text or labels)
</details>

图25-9 泛素蛋白分子动力学模拟的快照三维构象上展示的是主链上每个NH基团，蓝色小球代表N原子，红色小棍代表N—H键。

图25-10 受运动调制的附加磁场产生的两种机制（A）附近原子核对所测核通过偶极相互作用施加的局部磁场。（B）化学位移各向异性作用，即测量核周边电子分布（这里以芳香环的离域电子为例）对外加静磁场的屏蔽作用。

![](images/page_745_image_3.jpg)

那么，从分子运动出发该如何定量磁场波动在各个频率上的成分呢？我们先考虑偶极相互作用。对于 $^{15}\mathrm{N}$ 来说，由于紧邻的 $\mathbf{H}^{\mathrm{N}}$ 与它距离最近且旋磁比也最大，所以$^{15}\mathrm{N}$ 受到的偶极相互作用绝大多数来自 $\mathbf{H}^{\mathrm{N}}$ 。然后是 $^{15}\mathrm{N}$ 的化学位移各向异性作用。人们经过测量发现，化学位移各向异性效应最大的方向与N—H键的方向大体上是重合的。综合上述两方面的因素，N—H键的重定向运动主导了 $^{15}\mathrm{N}$ 所感受到的磁场波动。由此可见， $^{15}\mathrm{N}$ 的弛豫速率与分子运动的关系比较简单，易于进行定量分析，而且NH-HSQC谱图性质优良，因此 $^{15}\mathrm{N}$ 的自旋弛豫测量获得了广泛的应用。

下面以泛素蛋白为例来解释如何在分子运动与弛豫速率之间建立定量关系。我们首先讨论如何从泛素蛋白的分子动力学模拟轨迹计算自旋弛豫速率。在此基础上，我们才可以讨论如何从测量的自旋弛豫速率获得每个N—H键重定向运动的参数。

N—H键重定向运动可以通过自相关函数（autocorrelation function）来定量描述。对于一个随时间随机波动的信号，我们可以计算该信号与其自身沿时间轴平移 $\tau$ 之后的相关系数，而该相关系数对 $\tau$ 的函数就是自相关函数。在 $\tau = 0$ 时，两个信号完全相同，相关系数为1；当 $\tau$ 逐渐增大时，相关系数逐渐衰减，衰减的快慢反映了随机波动的快慢（图25-11）。

图25-11 自相关函数（A）随时间快速波动的信号（左）和对应的自相关函数（右）。（B）随时间慢速波动的信号（左）和对应的自相关函数（右）。

![](images/page_745_image_9.jpg)

## 知识窗25-3

## N—H 键重定向运动的自相关函数

从分子动力学模拟出发，我们可以提取每一个 N—H 键随时间变化的轨迹，如图 25-12 所示。将这一轨迹序列平移后与其自身按下面的公式计算相关系数:

$$
C (\tau) = \left\langle P _ {2} (\boldsymbol {u} (0) \cdot \boldsymbol {u} (\tau)) \right\rangle_ {\circ}
$$

其中 $P_{2}(x) = (3x^{2} - 1) / 2$ ，是二阶勒让德函数； $\pmb {u}(0)$ 和$u(\tau)$  分别为两条轨迹的重叠部分中来自原始轨迹和来自平移  $\tau$  时间后轨迹的 NH 单位矢量。得到的随时间衰减的自相关函数可以分解为一个或多个指数衰减项  $a_{i}e^{-t/\tau_{i}}$  的加和，其中  $a_{i}$  代表第 i 个运动组分的幅度， $\tau_{i}$  代表该运动组分的特征时间。

![](images/page_746_image_8.jpg)

<details>
<summary>text_image</summary>

τ₁
τ₂
</details>

图25-12 自相关函数的计算

分子动力学模拟轨迹中提取出的某个NH矢量的时间序列（第1行），以及将该矢量序列沿时间轴滑移 $\tau_{1}$ 和 $\tau_{2}$ 之后的序列（第2、3行）。

如前所述，对于泛素这类有固定三维结构的蛋白质来说，其分子内运动与蛋白质在溶液中的整体翻转运动可以被清楚地分开，并且前者被后者所调制。此时蛋白质每个N—H键的自相关函数（知识窗25-3）都是描述内部运动的自相关函数与描述整体翻转运动的自相关函数的乘积:

$$
C (t) = C _ {\mathrm{I}} (t) C _ {0} (t) \text {。}
$$

我们假定蛋白质的整体翻转是各向同性的 $^{*}$ ，其特征时间记作 $\tau_{m}$ ，那么 $C_{0}(t)=\mathrm{e}^{-t/\tau_{m}}$ 。更重要的部分是 $C_{1}(t)$ ，因为内部运动与蛋白质功能更相关。要从分子动力学轨迹得到 $C_{1}(t)$ ，我们需要把轨迹里的每个构象都转到与初始构象相同的朝向，这样就消除了整体翻转运动。如果对泛素蛋白在 $\alpha$ 螺旋、连接环和无序尾部这三个区域里各选择一个氨基酸残基的N—H键，分别代表刚性、有一定柔性和非常有柔性这三种情况，计算得到的 $C_{1}(t)$ 如图25-13所示。

这三个残基的内部运动自相关函数经过衰减后都出现了一个平台区。残基越有柔性，N—H键空间朝向的分布越分散，平台值越低。我们把平台区的高度定义为序参数（order parameter），用 $S^2$ 表示，取值范围是 $0\sim 1$ ，0代表完全无序，1代表完全刚性。位于平台区之前的衰减曲线可以分解成一个或多个指数衰减项，每个衰减项的特征时间记作  $\tau_{i}^{\prime}$ ，因此  $C_{1}(t)=a_{1}\mathrm{e}^{-t/\tau_{1}^{\prime}}+a_{2}\mathrm{e}^{-t/\tau_{2}^{\prime}}+\cdots+S^{2}$ ，其中  $a_{1}+a_{2}+\cdots+S^{2}=1$ 。而完整的自相关函数可以写成:

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* 整体形状大体上是球形的蛋白质都符合这种情况。</span></small>

![](images/page_747_chart_2.jpg)

<details>
<summary>scatter_3d</summary>

| Time (ns) | C(t) |
| --- | --- |
| 0 | ~0.92 |
| 500 | ~0.92 |
</details>

![](images/page_747_chart_3.jpg)

<details>
<summary>line</summary>

| 时间/ns | C(t) |
| --- | --- |
| 0 | ~0.75 |
| 100 | ~0.65 |
| 200 | ~0.65 |
| 300 | ~0.64 |
| 400 | ~0.63 |
| 500 | ~0.62 |
</details>

![](images/page_747_chart_4.jpg)

<details>
<summary>line</summary>

| 时间 (ns) | C(t) |
| --- | --- |
| 0 | ~0.15 |
| 100 | ~0.05 |
| 200 | ~0.05 |
| 300 | ~0.05 |
| 400 | ~0.05 |
| 500 | ~0.05 |
</details>

图25-13 泛素蛋白分子动力学模拟中A28、T9和G76的N—H键内部运动对应的自相关函数三个残基分别处在 $\alpha$ 螺旋、连接环和无序尾部，在蛋白质三维结构中用红色标出。每个子图还展示了N—H键中氢原子在以氮原子为中心的球面上的散点分布图。

$$
C (t) = (a _ {1} \mathrm{e} ^ {- t / \tau_ {1} ^ {\prime}} + a _ {2} \mathrm{e} ^ {- t / \tau_ {2} ^ {\prime}} + \dots + S ^ {2}) \mathrm{e} ^ {- t / \tau_ {\mathrm{m}}} = \sum_ {i} a _ {i} \mathrm{e} ^ {- t / \tau_ {i}}
$$

其中 $\tau_{i} = \frac{1}{1 / \tau_{i}' + 1 / \tau_{\mathrm{m}}}$，代表内部运动组分 $\tau_{i}'$ 被 $\tau_{\mathrm{m}}$ 调制后的结果。注意，在上式中 $S^2$ 对应的那一项可以看作幅度为 $S^2$，特征时间为无穷大的内部运动组分，因此调制后的特征时间为 $\tau_{\mathrm{m}}$。

接下来我们需要从自相关函数中获得不同频率下的分量，方法是施加傅里叶变换然后取实部，得到的函数称为谱密度函数（spectral density function）:

$$
J (\omega) = \mathrm{Re} \left(\frac {1}{5} \int_ {- \infty} ^ {\infty} \sum_ {i} a _ {i} \mathrm{e} ^ {- t / \tau_ {i}} \cdot \mathrm{e} ^ {- i \omega t} \mathrm{d} t\right) = \frac {2}{5} \sum_ {i} \frac {a _ {i} \tau_ {i}}{1 + \omega^ {2} \tau_ {i} ^ {2}}
$$

$^{15}$ N 的纵向弛豫速率  $R_{1}$  、横向弛豫速率  $R_{2}$  以及  ${}^{15}$ N 和  ${}^{1}$ H 之间的交叉弛豫速率  $\sigma_{NH}$  是由  $J(\omega)$  在不同频率分量的线性加和来决定的  $^{*}$ ，反映了分子运动导致的局部磁场波动中特定频率分量对弛豫速率所产生的贡献（知识窗 25-4）。

从自旋弛豫速率的公式出发，我们可以绘出三种自旋弛豫速率对N—H键重定向特征时间的依赖曲线（图25-14）。由图中可见， $R_{1}$ 对纳秒尺度（0.1 ns到十几纳秒）的运动比较敏感， $R_{2}$ 对慢速运动（慢于十几纳秒）很敏感，而NOE对快速运动（几百皮秒）比较敏感。生物大分子的分子量越大，在水溶液中的整体翻转运动就越慢，因而每个化学键的重定向运动也越慢，进而导致 $R_{2}$ 比较大，谱峰展宽明显。这就解释了我们在5.3.1节中提到的分子量大小对核磁测量的限制。

到目前为止，我们可以从分子动力学模拟轨迹出发，提取出每个N—H键重定向运动的特征参数，然后计算出自旋弛豫速率 $R_{1}$ 、 $R_{2}$ 和NOE。那么如果我们已经通过实验得到了这三组自旋弛豫速率，如何才能从中提取出关于NH重定向运动的特征参数呢？这时我们需要做无模型（model-free）分析（也称作Lipari-Szabo分析）。

无模型分析方法的前提条件是分子的整体翻转运动与内部运动之间有比较清晰

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* 在 $R_{2}$ 表达式中有一项 $R_{ex}$ 代表化学交换的贡献，将在下文中讨论。</span></small>

## 知识窗25-4

## $^{15}$ N 自旋弛豫速率的公式

自旋弛豫速率  $R_{1}$ 、 $R_{2}$  和 NOE 可以表达为下面的公式:

$$
\left\{ \begin{array}{l} R _ {1} = \frac {d ^ {2}}{4} \left[ J (\omega_ {\mathrm{H}} - \omega_ {\mathrm{N}}) + 3 J (\omega_ {\mathrm{N}}) + 6 J (\omega_ {\mathrm{H}} + \omega_ {\mathrm{N}}) \right] + C ^ {2} J (\omega_ {\mathrm{N}}), \\ R _ {2} = \frac {d ^ {2}}{8} \left[ 4 J (0) + J (\omega_ {\mathrm{H}} - \omega_ {\mathrm{N}}) + 3 J (\omega_ {\mathrm{N}}) + 6 J (\omega_ {\mathrm{H}}) + 6 J (\omega_ {\mathrm{H}} + \omega_ {\mathrm{N}}) \right] + \frac {C ^ {2}}{6} \left[ 4 J (0) + 3 J (\omega_ {\mathrm{N}}) \right] + R _ {\mathrm{ex}} 。 \\ \sigma_ {\mathrm{NH}} = \frac {d ^ {2}}{4} \left[ 6 J (\omega_ {\mathrm{H}} + \omega_ {\mathrm{N}}) - J (\omega_ {\mathrm{H}} - \omega_ {\mathrm{N}}) \right] 。 \end{array} \right.
$$

其中， $c = \Delta_{\mathrm{N}} / \sqrt{3}$ ， $d = \mu_0\hbar \gamma_{\mathrm{H}}\gamma_{\mathrm{N}} / (4\pi r_{\mathrm{HN}}^3)$ ，分别是偶极相互作用和化学位移各向异性所对应的常数； $\Delta_{\mathrm{N}}$ 是以 $\mathrm{Hz}$ 为单位的 $^{15}\mathrm{N}$ 化学位移各向异性值， $\mu_0$ 为真空磁导率； $\omega_{\mathrm{H}}$ 和 $\omega_{\mathrm{N}}$ 分别为 ${}^{1}\mathrm{H}$ 和 $^{15}\mathrm{N}$ 的拉莫尔频率。实验测量的NOE值与 $\sigma_{\mathrm{NH}}$ 有如下关系:

$$
\mathrm{NOE} = 1 + \frac {\gamma_ {\mathrm{H}}}{\gamma_ {\mathrm{N}}} \cdot \frac {\sigma_ {\mathrm{NH}}}{R _ {1}} 。
$$

![](images/page_748_image_8.jpg)

图25-14 $^{15}\mathrm{N}R_{1}$ 、 $R_{2}$ 和NOE对N—H键重定向运动特征时间的依赖曲线橙线和蓝线分别对应600MHz核磁仪和1GHz核磁仪下的模拟结果。

的界限，通常折叠得比较好的生物大分子都满足这个条件。该方法假定每个残基的内部运动只有一个主要成分 $^{*}$ 。以 ${}^{15}N$ 自旋弛豫实验为例，内部运动可由每个N—H键各自的内部运动的特征时间来代表。同时，所有的N—H键都要经历共同的整体翻转，同样可以由一个单独的整体翻转特征时间来代表。从自旋弛豫的实验数据出发，我们不仅可以得到蛋白质分子整体翻转的特征时间，更重要的是可以获得每个残基内部运动的序参数和特征时间，后两者分别反映了残基的空间动态性和时间动态性（知识窗25-5）。

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* 对蛋白质的大多数残基位点，该假定都是成立的。少数位点的内部运动存在两种或更多的主要成分，此时需要用拓展的无模型方法来处理。</span></small>

## 知识窗25-5

## 无模型分析方法

假设蛋白质某个残基 N—H 键的内部运动特征时间为  $\tau_{e}$ ，并且整体翻转运动是各向同性的，特征时间记作  $\tau_{m}$ ，那么自相关函数可以写为

$$
C (t) = C _ {\mathrm{I}} (t) C _ {\mathrm{O}} (t) = [ (1 - S ^ {2}) \mathrm{e} ^ {- t / \tau_ {\mathrm{e}}} + S ^ {2} ] \mathrm{e} ^ {- t / \tau_ {\mathrm{m}}},
$$

相应的谱密度函数为

$$
J (\omega) = \frac {2}{5} \bigg [ S ^ {2} \frac {\tau_ {\mathrm{m}}}{1 + \omega^ {2} \tau_ {\mathrm{m}} ^ {2}} + (1 - S ^ {2}) \frac {\tau}{1 + \omega^ {2} \tau^ {2}} \bigg ],
$$

其中 $\tau = (1 / \tau_{\mathrm{m}} + 1 / \tau_{\mathrm{e}})^{-1}$，是内部运动受整体翻转调制后的

约化特征时间。

如果  ${}^{15}N$  自旋弛豫实验一共测到了 n 个残基的数据，那么已知的弛豫速率一共有 3n 个，未知的则有 n 个  $S^{2}$ 、n 个  $\tau_{e}$ 、1 个  $\tau_{m}$ ，共计  $2n+1$  个参数。由此我们就可以利用自旋弛豫速率的公式（知识窗 25-4）拟合出整体翻转特征时间  $\tau_{m}$  以及每个残基的  $S^{2}$  和  $\tau_{e}$ ，其中  $S^{2}$  反映每个残基在空间上的动态性，而  $\tau_{e}$  反映每个残基在时间上的动态性。

![](images/page_749_image_11.jpg)

<details>
<summary>text_image</summary>

基态 ← → 激发态
95% 5%
</details>

图25-15 在基态和激发态之间转换的RNA分子

在两个状态之间碱基对发生了滑移，构象交换发生在微秒到毫秒的时间尺度内。

## (2) 弛豫弥散方法

生物大分子在溶液中除了有丰度很高、自由能最低的基态（ground state，GS）构象外，还存在着高自由能构象状态，称为激发态（excited state，ES）或者瞬态（transient state）。激发态构象由于丰度低、寿命短，难以用其它生物物理手段来表征其结构，因此有时也被称作不可见状态（invisible state）。核磁共振的弛豫弥散方法是检测激发态构象并表征其结构的强有力工具。

假定有一个核酸分子在基态和激发态之间互相转换，如果构象交换发生在微秒到毫秒时间尺度内，就适合应用弛豫弥散方法。值得注意的是，微秒到毫秒是一个非常重要的时间范围，大多数重要的生物学过程都发生在这个范围内。由于两个构象有所区别，总有一些原子核在两个构象中的化学位移有差别。我们可以用一

个两态模型来表示在两种化学位移之间切换的原子核（图25-15）。

弛豫弥散方法包括 CPMG（Carr-Purcell-Meiboom-Gill）和  $R_{1\rho}$  这两种实验。在 5.4.4 节中我们解释了中速化学交换会导致谱峰展宽（或者说  $R_{2}$  的增大），而微秒到毫秒的时间尺度通常就处于中速交换的范围。这种谱峰展宽效应也是该方法的名称中“弥散”两字的由来。为了获取化学交换的信息，我们需要用某种方法对交换产生的谱峰展宽效应进行调制，CPMG 和  $R_{1\rho}$  采用的是基于自旋回波（spin echo）的方法。假设样品中的待测原子核有的处于基态，有的处于激发态，然后我们让这些原子核经历一个自旋回波脉冲序列，那么只要在这段时间内没有发生化学交换，这些原子核由于化学位移不同所产生的分散效应将被完全消除（图 25-16A）。CPMG 方法使用由一系列等距排列的  $180^{\circ}$  脉冲组成的脉冲队列（图 25-16B）。而  $R_{1\rho}$  方法使用一段连续的长脉冲，实际上相当于多个  $180^{\circ}$  脉冲头尾相连（图 25-16C），因此与 CPMG 本质上是一样的。

$180^{\circ}$ 脉冲队列对谱峰展宽有抑制作用，脉冲越密集，抑制作用越显著（图25-17A、B）。当测量不同脉冲队列频率下的 $R_{2}$ 弛豫速率（$R_{2,\mathrm{eff}} = R_2 + R_{\mathrm{ex}}$），会得到一条逐渐衰减的曲线（图25-17C）。对这样的曲线进行拟合，就能获得激发态的丰度 $p_{\mathrm{B}}$、正向反

(A)

![](images/page_750_image_4.jpg)

(B)

![](images/page_750_chart_6.jpg)

<details>
<summary>bar</summary>

| Category | Value |
| --- | --- |
| 1 | \(\pi\) |
| 2 | \(\pi\) |
| 3 | \(\pi\) |
| 4 | \(\pi\) |
| 5 | \(\pi\) |
| 6 | \(\pi\) |
| 7 | \(\pi\) |
</details>

(C)

![](images/page_750_image_8.jpg)

<details>
<summary>text_image</summary>

R₁ρ
</details>

![](images/page_750_image_9.jpg)

<details>
<summary>natural_image</summary>

Blue gradient vertical stripes on white background (no text or symbols)
</details>

图25-16 CPMG和 $R_{1p}$ （A）自旋回波可以消除由于化学位移不同而产生的分散效应。用两个速度不同的人代表化学位移不同的两种状态。在时间零点，两人同时出发；经过 $\tau$ 时间，两人拉开差距；然后 $180^{\circ}(\pi)$ 脉冲令两人同时折返，再经过$\tau$ 时间，两人同时回到起点。（B）CPMG方法应用了一系列等距排布的 $180^{\circ}$ 脉冲。（C） $R_{1p}$ 方法应用一段连续的长脉冲，可以等效为多个$180^{\circ}$ 脉冲头尾相连。

(A)

![](images/page_750_chart_12.jpg)

<details>
<summary>scatter</summary>

| Series | X (range) | Y (range) |
| --- | --- | --- |
| Blue | 0.1~0.9 | 0.1~0.9 |
| Orange | 0.2~0.8 | 0.2~0.9 |
</details>

(B)

![](images/page_750_chart_14.jpg)

<details>
<summary>bubble</summary>

| Series | X (range) | Y (range) |
| --- | --- | --- |
| Blue | ~0.1 ~0.9 | ~0.2 ~0.9 |
| Orange | ~0.1 ~0.9 | ~0.2 ~0.9 |
| Red | ~0.1 ~0.9 | 0~0.3 |
</details>

(C)

![](images/page_750_chart_16.jpg)

<details>
<summary>line</summary>

| 脉冲队列频率/Hz | P2,\(eff/s^{-1}\) |
| --- | --- |
| ~50 | ~13.4 |
| ~80 | ~10.6 |
| ~120 | ~7.4 |
| ~150 | ~6.1 |
| ~190 | ~4.5 |
| ~220 | ~4.1 |
| ~250 | ~3.7 |
| ~280 | ~3.3 |
| ~350 | ~2.6 |
| ~420 | ~2.5 |
| ~520 | ~2.1 |
| ~620 | ~2.2 |
| ~700 | ~2.2 |
| ~800 | ~2.3 |
| ~900 | ~2.2 |
| 1000 | ~2.1 |
</details>

图25-17 CPMG脉冲队列可以抑制化学交换导致的谱峰展宽

（A）低频的脉冲队列对谱峰展宽的抑制效果较小。（B）高频的脉冲队

列对谱峰展宽的抑制效果显著。（C）当存在化学交换导致的谱峰展宽效应时，测量不同脉冲队列频率下的表观 $R_{2}$ （即 $R_{2,\mathrm{eff}}$），可以得到一条衰减的曲线。增大脉冲队列频率会让 $R_{2,\mathrm{eff}}$ 逐渐接近 $R_{2}$。

(A)

![](images/page_751_chart_3.jpg)

<details>
<summary>scatter</summary>

| Category | 1H (ppm) | 15N (ppm) |
| --- | --- | --- |
| U167^ES | ~13.8 | ~160.5 |
| U167^GS | ~11.9 | ~157.5 |
</details>

图25-18 化学交换饱和转移的原理

GS代表基态，ES代表激发态。假设U167的基态谱峰位于左边谱图中的上方虚线圆圈处，而不可见的激发态谱峰位于下方虚线圆圈处，

(B)

![](images/page_751_image_7.jpg)

<details>
<summary>chemical</summary>

DNA double-stranded structure with base pairing and molecular weight shifts
</details>

激发态: 3%

(C)

![](images/page_751_chart_10.jpg)

<details>
<summary>line</summary>

| 15N上饱和照射的位置 (ppm) | U167GS谱峰的相对强度 |
| --- | --- |
| 165 | ~1.0 |
| 160 | ~0.9 |
| 155 | ~0.4 |
| 150 | ~0.2 |
| 145 | ~0.1 |
</details>

那么当 $B_{1}$ 扫描到U167激发态谱峰的频率时，将导致U167基态谱峰峰高的降低。

应速率 $k_{1}$ 、逆向反应速率 $k_{-1}$ 以及激发态与基态的化学位移差值 ${}^{*}\Delta \omega = \omega_{\mathrm{ES}} - \omega_{\mathrm{GS}}$ 。其中$\Delta \omega$ 的信息尤为重要，因为从中我们可以得到激发态的化学位移，进而获得激发态的构象信息。

## (3) 化学交换饱和转移

CPMG对化学交换（ $k_{\mathrm{ex}}$ ）的检测范围是 $50\sim 5000~\mathrm{s}^{-1}$ ，而 $R_{1\rho}$ 的检测范围是$50\sim 100000\mathrm{s}^{-1}$ 。对于构象交换更慢的过程，可以采用化学交换饱和转移实验，其测量

范围是 $20\sim 300\mathrm{s}^{-1}$ 。该方法把很弱的连续波脉冲施加到样品上\*\*，在不同的脉冲频率下测量基态谱峰的强度。由于饱和现象，当扫描到基态谱峰的频率时会出现基态谱峰峰高的严重下降。如果存在激发态，那么当扫描到激发态谱峰的频率时，激发态信号的饱和效应会被化学交换带到基态，因此基态谱峰也会出现峰高的降低，从而实现对激发态的检测（图25-18）。

## (4) ZZ- 交换谱

如果构象交换脱离了微秒到毫秒的时间范围，达到上百毫秒到秒，这时适用的方法是ZZ-交换谱。这个时间尺度下，谱图上会同时出现代表两种状态的谱峰以及两个谱峰相交处由于交换产生的较弱的交叉峰（图25-19）。ZZ-交换谱要求激发态达到较高的丰度，如果

![](images/page_751_chart_18.jpg)

<details>
<summary>contour</summary>

| Feature | X-axis (ppm) | Y-axis (ppm) |
| --- | --- | --- |
| Central Cluster | -166~-162 | -166~-162 |
| Left Cluster | -162~-160 | -162~-160 |
| Right Cluster | -166~-164 | -166~-164 |
</details>

图25-19 ZZ-交换谱的示例

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\* 对 CPMG 方法，得到的是化学位移差值的绝对值，因此通常需要在两台不同场强的核磁仪上采集数据以确定该值的正负号。而 $R_{1\rho}$ 方法则没有这个问题。</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\*\* 使用强度很弱的脉冲是因为脉冲越弱，在频域上的激发范围越窄，有利于它对频率的精细扫描。</span></small>