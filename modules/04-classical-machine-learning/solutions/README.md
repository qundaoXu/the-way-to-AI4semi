# Module 04 参考解答

**在自己的实现通过测试之前，不要打开这个目录里的 `.py` 文件。**

参考解答由 Agent 编写，作用只有一个：证明 `tests/` 里的测试是正确且可以通过的。`make check` 和 CI 以 `LEARN_TARGET=solutions` 运行全部测试来验证这一点。它们不进入学习网站。

自己的实现通过之后，再回来对照：参考解答未必是唯一或最好的写法，值得比较的是数值稳定性的处理、边界情况和复杂度。

```bash
LEARN_TARGET=solutions uv run pytest modules/04-classical-machine-learning/tests
```
