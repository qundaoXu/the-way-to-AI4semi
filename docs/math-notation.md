# 数学符号约定

全仓库的讲义统一使用下面的符号。某章确实需要偏离时（例如沿用某篇论文的记号），在该章开头说明。新符号在第一次有章节用到时补充到这里。

## 通用

| 对象 | 记法 | 示例 |
|---|---|---|
| 标量 | 斜体小写或大写 | $n$、$\alpha$、$E$ |
| 向量 | 粗体小写，默认列向量 | $\mathbf{x}$、$\mathbf{w}$ |
| 矩阵 | 斜体大写 | $X$、$A$、$\Sigma$ |
| 高阶张量 | 无衬线大写 | $\mathsf{T}$ |
| 集合、空间 | 花体或黑板体 | $\mathcal{D}$、$\mathbb{R}^d$ |
| 第 $i$ 个样本 | 下标 $i$ | $\mathbf{x}_i$、$y_i$ |
| 向量的第 $j$ 个分量 | 下标 $j$，不加粗 | $w_j$、$x_{ij}$ |
| 估计量 | 加帽 | $\hat{\mathbf{w}}$、$\hat{y}$ |
| 均值 | 加横线 | $\bar{y}$ |
| 迭代步 | 圆括号上标 | $\mathbf{w}^{(t)}$ |

## 线性代数

| 记法 | 含义 |
|---|---|
| $A^\top$、$A^{-1}$、$A^{+}$ | 转置、逆、Moore–Penrose 伪逆 |
| $I$、$\mathbf{0}$、$\mathbf{1}$ | 单位矩阵、零向量、全 1 向量 |
| $\lVert\mathbf{x}\rVert$ | 欧氏范数（$\ell_2$）；其他范数写明下标，如 $\lVert\mathbf{x}\rVert_1$ |
| $\lVert A\rVert_F$、$\lVert A\rVert_2$ | Frobenius 范数、谱范数 |
| $\operatorname{tr}$、$\det$、$\operatorname{rank}$、$\operatorname{diag}$ | 迹、行列式、秩、对角矩阵 |
| $\operatorname{col}(A)$ | 列空间 |
| $\kappa(A)$ | 条件数（默认 2-范数） |
| $A = U\Sigma V^\top$ | SVD；奇异值 $\sigma_1 \ge \sigma_2 \ge \dots$，左右奇异向量 $\mathbf{u}_i$、$\mathbf{v}_i$ |
| $A \succeq 0$、$A \succ 0$ | 半正定、正定 |

## 微积分

| 记法 | 含义 |
|---|---|
| $\nabla_{\mathbf{w}} J$ | 梯度，与 $\mathbf{w}$ 同形状的列向量 |
| $\nabla^2_{\mathbf{w}} J$ | Hessian |
| $\dfrac{\partial \mathbf{f}}{\partial \mathbf{x}}$ | Jacobian，分子布局：第 $i$ 行第 $j$ 列为 $\partial f_i / \partial x_j$ |
| $df=\operatorname{tr}((\nabla_X f)^\top dX)$ | 以 Frobenius 内积定义矩阵梯度，$\nabla_X f$ 与 $X$ 同形状 |

## 群表示与随机过程

| 记法 | 含义 |
|---|---|
| $R\in\mathrm{SO}(3)$ | 主动旋转，列向量 $\mathbf r'=R\mathbf r$；代码行存储对应 `r @ R.T` |
| $D_l(R)$、$\mathbf Y_l$ | 固定阶数的旋转表示与球谐块；具体实基顺序在 M02.7 明示 |
| $P$、$\boldsymbol\pi$ | Markov 转移矩阵与平稳行分布，$\boldsymbol\pi P=\boldsymbol\pi$；与投影矩阵按语境区分 |
| $W_t$、$dW_t$ | 标准 Wiener 过程及其增量，增量方差为时间间隔 |

## 概率与统计

| 记法 | 含义 |
|---|---|
| $p(x)$、$p(x \mid y)$ | 概率密度或质量函数、条件分布 |
| $\mathbb{E}[\cdot]$、$\operatorname{Var}[\cdot]$、$\operatorname{Cov}[\cdot,\cdot]$ | 期望、方差、协方差 |
| $\mathcal{N}(\boldsymbol{\mu}, \Sigma)$ | 高斯分布 |
| $x \sim p$ | $x$ 服从分布 $p$ |
| $\mathrm{KL}(p \,\Vert\, q)$、$H(p)$ | KL 散度、熵 |
| $\varepsilon$ | 噪声 |
| $\sigma^2$ | 噪声方差。与奇异值 $\sigma_i$ 同时出现时，奇异值总带下标 |

## 机器学习

| 记法 | 含义 |
|---|---|
| $n$、$d$ | 样本数、特征维数 |
| $X \in \mathbb{R}^{n \times d}$ | 设计矩阵，每行一个样本 |
| $\mathbf{y} \in \mathbb{R}^n$ | 目标 |
| $\mathbf{w}$、$b$ | 权重（系数）、截距 |
| $\boldsymbol{\theta}$ | 一般模型的全部参数 |
| $J$、$\mathcal{L}$ | 目标函数、损失函数 |
| $\alpha$、$\lambda$ | 正则化强度。两者并用时：$\alpha$ 沿用 scikit-learn 的约定，$\lambda$ 用于按样本平均的目标函数 |
| $\eta$ | 学习率（GLM 一节中 $\eta$ 表示线性预测子，上下文会说明） |
| $\sigma(\cdot)$ | sigmoid 函数 |
| $k(\mathbf{x}, \mathbf{x}')$、$K$ | 核函数、核矩阵 |

## 原子模拟

| 记法 | 含义 | 单位（默认） |
|---|---|---|
| $N$ | 原子数 | — |
| $\mathbf{r}_i$、$\mathbf{r}_{ij} = \mathbf{r}_j - \mathbf{r}_i$ | 原子位置、相对位矢 | Å |
| $Z_i$ | 原子种类 | — |
| $E$、$E_i$ | 总能量、原子能量 | eV |
| $\mathbf{F}_i = -\nabla_{\mathbf{r}_i} E$ | 力 | eV/Å |
| $\boldsymbol{\sigma}$ | 应力张量。只在原子模拟语境下使用，避免与 sigmoid 混淆 | eV/Å³ |
| $r_c$ | 截断半径 | Å |
| $k_B$、$T$ | Boltzmann 常数、温度 | eV/K、K |

代码中涉及物理量时，在 docstring 里写明单位。

## 神经网络与能量导数

| 记法 | 含义与约定 |
|---|---|
| $H^{(l)}$、$Z^{(l)}$、$W^{(l)}$ | MLP 行样本表示、预激活与权重；讲义 NumPy 权重为 in×out，PyTorch Linear 存储 out×in |
| $\Delta^{(l)}$ | 损失对该层预激活的梯度，与 batch×通道形状一致 |
| $Jv$、$J^\top u$ | JVP、VJP；Jacobian 仍使用输出×输入的分子布局 |
| $\epsilon_{ab}$、$V_0$ | 无量纲仿射形变与参考体积；M05.2 取行坐标 $R(\epsilon)=R_0(I+\epsilon)^\top$ |
| $\sigma_{ab}=V_0^{-1}\partial E/\partial\epsilon_{ab}$ | 本仓库示例的能量应变应力约定，不含动能；比较软件时核对符号、体积与剪切因子 |
| $h_t$、$c_t$ | 递推隐藏状态与 LSTM cell 状态；时间用下标，网络层用上标 |

M05.2 的 LJ 实例明确使用约化单位 $\varepsilon=\sigma=m=1$，与全站默认 eV/Å 单位区分。该章的 $\varepsilon$ 用于 LJ 能量尺度，形变用 $\boldsymbol\epsilon$，含义在段落中说明。
