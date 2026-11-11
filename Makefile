# 常用命令入口。详见 docs/getting-started.md 与 PROJECT_BLUEPRINT.md 第 11.4 节。
UV  ?= uv
RUN := $(UV) run
PY  := $(RUN) python

.DEFAULT_GOAL := help
.PHONY: help setup check ex nb sync test-src preview site status

help:
	@echo "make setup                         创建环境，安装 semiai 与 dev 依赖"
	@echo "make check                         ruff + 参考解答测试 + 仓库一致性 + 索引检查"
	@echo "make ex M=04                       用自己的练习实现运行模块 04 的测试"
	@echo "make sync                          重新生成索引（CURRICULUM.md、进度清单等）"
	@echo "make test-src                      运行公共包 semiai 的测试"
	@echo "make preview                       启动本地学习网站，保存即刷新"
	@echo "make site                          完整渲染学习网站"
	@echo "make status ID=M04.2 S=Practicing  修改某章的学习状态并同步索引"

setup:
	@command -v quarto >/dev/null || echo "提示：未找到 Quarto CLI，make preview / make site 需要它，见 docs/getting-started.md"
	$(UV) sync
	$(RUN) pre-commit install

check:
	$(RUN) ruff check .
	LEARN_TARGET=solutions $(RUN) pytest -q
	$(PY) scripts/check_repo.py
	$(PY) scripts/sync_index.py --check

ex:
	@test -n "$(M)" || { echo "用法：make ex M=04"; exit 2; }
	-LEARN_TARGET=exercises $(RUN) pytest modules/$(M)-*/tests --results-json progress/test-results.json
	@$(PY) scripts/sync_index.py --touch-dashboard

# 实例讲解 notebook 带输出提交；改动 notebook 代码后用它重新执行并保存输出。
nb:
	@test -n "$(M)" || { echo "用法：make nb M=01"; exit 2; }
	$(RUN) jupyter nbconvert --to notebook --execute --inplace \
		--ExecutePreprocessor.timeout=600 --ExecutePreprocessor.kernel_name=python3 \
		modules/$(M)-*/notebooks/*.ipynb

sync:
	$(PY) scripts/sync_index.py --touch-dashboard

test-src:
	$(RUN) pytest -q tests

preview:
	$(RUN) quarto preview

site:
	$(RUN) quarto render

status:
	@test -n "$(ID)" -a -n "$(S)" || { echo '用法：make status ID=M04.2 S=Practicing（状态含空格时加引号，如 S="Not Started"）'; exit 2; }
	$(PY) scripts/sync_index.py --set-status "$(ID)" "$(S)" --touch-dashboard
