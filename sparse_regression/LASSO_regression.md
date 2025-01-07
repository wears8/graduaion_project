## 1. 普通最小二乘法（OLS）的求解

在普通最小二乘法中，目标是最小化残差平方和：
$$
\min_{\beta} \left\| y - X\beta \right\|_2^2
$$
其中：
- $y$ 是因变量（目标变量）。
- $X$ 是自变量（特征矩阵）。
- $\beta$ 是回归系数。

OLS 的解析解为：
$$
\beta = (X^T X)^{-1} X^T y
$$
（假设 $X^T X$ 是可逆的）。

---

## 2. LASSO 回归的求解

LASSO 回归的目标函数在 OLS 的基础上添加了 $\ell_1$ 正则化项：
$$
\min_{\beta} \left\| y - X\beta \right\|_2^2 + \lambda \left\| \beta \right\|_1
$$
其中：
- $\left\| y - X\beta \right\|_2^2$ 是残差平方和（与 OLS 相同）。
- $\left\| \beta \right\|_1 = \sum_{j=1}^p |\beta_j|$ 是 $\ell_1$ 正则化项。
- $\lambda$ 是正则化参数，控制正则化的强度。

由于 $\ell_1$ 正则化项的存在，LASSO 回归的目标函数**不可导**，因此无法直接使用 OLS 的解析解。取而代之的是，LASSO 回归通常使用以下方法求解：

---

## 3. LASSO 回归的求解方法

### 坐标下降法（Coordinate Descent）
坐标下降法是 LASSO 回归最常用的求解方法。其基本思想是：
1. 每次只优化一个系数 $\beta_j$，而固定其他系数。
2. 通过迭代更新每个系数，直到收敛。

对于每个系数 $\beta_j$，更新公式为：
$$
\beta_j = \frac{S\left( \sum_{i=1}^n x_{ij}(y_i - \hat{y}_i^{(-j)}), \lambda \right)}{\sum_{i=1}^n x_{ij}^2}
$$
其中：
- $\hat{y}_i^{(-j)}$ 是不包括 $\beta_j$ 的预测值。
- $S(\cdot, \lambda)$ 是软阈值函数：
  $$
  S(z, \lambda) = \text{sign}(z) \cdot \max(|z| - \lambda, 0)
  $$

### 最小角回归（LARS）
LARS 是一种专门用于求解 LASSO 回归的高效算法。它通过逐步增加变量来选择模型，并在每一步中选择与当前残差最相关的变量。

---

## 4. LASSO 回归与 OLS 的区别

| 特性                | OLS                              | LASSO                            |
|---------------------|----------------------------------|----------------------------------|
| **目标函数**         | $\min_{\beta} \left\| y - X\beta \right\|_2^2$ | $\min_{\beta} \left\| y - X\beta \right\|_2^2 + \lambda \left\| \beta \right\|_1$ |
| **正则化项**         | 无                               | $\ell_1$ 正则化项              |
| **变量选择**         | 无                               | 通过 $\ell_1$ 正则化实现变量选择 |
| **稀疏性**           | 无                               | 生成稀疏模型                     |
| **求解方法**         | 解析解（矩阵求逆）               | 迭代算法（如坐标下降法、LARS）   |
| **适用场景**         | 低维数据                         | 高维数据、多重共线性问题         |