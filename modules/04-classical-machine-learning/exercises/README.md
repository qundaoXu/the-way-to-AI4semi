# Module 04 练习

这里的文件是**练习桩**：只有函数签名和 docstring，函数体是 `raise NotImplementedError`。把它换成你自己的实现。Agent 不会替你写这些文件，也不会在未经你同意时修改它们。

## 练习列表

| 章节 | 文件 | 需要实现 | 测试 |
|---|---|---|---|
| M04.2 线性模型 | [linear_regression.py](linear_regression.py) | `fit_ols`、`fit_ridge`、`ridge_loss_and_grad`、`soft_threshold`、`fit_lasso_cd` | [test_linear_regression.py](../tests/test_linear_regression.py) |
| M04.2 线性模型 | [logistic_regression.py](logistic_regression.py) | `sigmoid`、`logistic_loss_and_grad`、`fit_logistic_newton` | [test_logistic_regression.py](../tests/test_logistic_regression.py) |

建议顺序：`fit_ols` → `fit_ridge` → `ridge_loss_and_grad` → `soft_threshold` → `fit_lasso_cd` → `sigmoid` → `logistic_loss_and_grad` → `fit_logistic_newton`。

## 运行方式

```bash
make ex M=04                                                        # 本模块全部测试
uv run pytest modules/04-classical-machine-learning/tests -k ols    # 只跑名字含 ols 的测试
uv run pytest modules/04-classical-machine-learning/tests -x --pdb  # 第一个失败处进入调试器
```

`make ex` 会把结果写入 `progress/test-results.json`，学习网站首页据此显示最近一次测试结果。在 VS Code 的测试面板里也可以逐条运行和断点调试，面板默认检查 `exercises/`（由仓库根目录的 `.env` 决定）。

刚开始时全部测试都应该失败，错误是 `NotImplementedError`。每实现一个函数，对应的几条测试由红转绿。

## 提示规则

卡住时，按下面的顺序向 Agent 求助（TUTOR 模式），每次只要一级：

1. **方向提示**：该用哪个概念或讲义的哪一节；
2. **关键步骤**：推导或算法的骨架，不含代码；
3. **伪代码**。

只有你明确要求时，Agent 才给出完整解答。`solutions/` 里有参考解答，它的作用是证明测试本身可以通过；在自己的实现通过测试之前不要打开。

## 完成之后

1. 全部测试通过后，把学习状态改为 `Reviewed` 前，先做完讲义的自测题；
2. 用 `make status ID=M04.2 S=Reviewed` 更新状态，并在讲义 frontmatter 的 `evidence` 里记录证据（例如测试通过时的 commit）；
3. 再对照 `solutions/` 看参考解答与自己的实现有什么不同。
