# Module 08：半导体制造数据科学（Semiconductor Manufacturing Data Science）

模块优先级 `Branch` · 估算学时 40–60 h

## 定位

理解 Fab 数据结构，掌握工业预测、异常检测与工艺优化的典型方案。本模块是分支内容：只有选择 [Path C](../../learning-paths/path-c-semiconductor-industrial-ai.md) 时才升级为 P1。

## 章节

<!-- AUTO:chapters:start -->
<!-- 本区域由 scripts/sync_index.py 根据 curriculum.yaml 生成，请勿手工编辑 -->

| ID | 章节 | 优先级 | 先修 | 锚点 | 建设状态 | 学习状态 |
|---|---|---|---|---|---|---|
| M08.1 | 半导体制造数据<br>Semiconductor Manufacturing Data | Branch | — | — | Planned | Not Started |
| M08.2 | 过程监控<br>Process Monitoring | Branch | M02.4, M04.5 | — | Planned | Not Started |
| M08.3 | 良率与缺陷分析<br>Yield and Defect Analysis | Branch | M04.7, M05.5 | — | Planned | Not Started |
| M08.4 | 虚拟量测<br>Virtual Metrology | Branch | M03.5, M04.4 | — | Planned | Not Started |
| M08.5 | 可靠性与优化<br>Reliability and Optimization | Branch | M02.4, M03.6 | A5 | Planned | Not Started |

**各章范围**

- **M08.1 半导体制造数据**：Fab 工艺流程概览；Lot、Wafer、Die 层级数据；工艺、设备与传感器数据；可追溯性与数据质量。
- **M08.2 过程监控**：统计过程控制（SPC）与控制图；过程能力指数；故障检测与分类（FDC）；多变量过程监控（PCA-based、Hotelling T²）。
- **M08.3 良率与缺陷分析**：良率预测；晶圆图模式分类；缺陷图像分类；异常批次分析与根因归因。
- **M08.4 虚拟量测**：计量值预测；时序传感器特征工程；设备状态建模；模型漂移监测。
- **M08.5 可靠性与优化**：Weibull 分析；生存分析；退化趋势预测（与 PCM 保持特性、电阻漂移等可靠性问题相关）；因果推断基础（归属 M12.1）；DOE 与响应面（归属 M03.6）；贝叶斯优化（归属 M06.5）。

<!-- AUTO:chapters:end -->

讲义按即时建设原则逐章创建，最多领先学习进度两章；表中没有链接的章节尚未建设。

## 毕业标准

达到以下全部条件，才算完成本模块。每一条都对应具体的代码、测试或书面产出。

- 完成 Project 01（Semiconductor Data Analysis）；
- 能针对给定的工业场景写出包含数据、模型、评价与部署考虑的方案设计文档。

## 研究锚点

- **A5**：老化轨迹的时间序列分析：对数时间采样、漂移、变化点

各锚点的知识链条与推荐学习顺序见 [研究锚点说明](../../docs/research-anchors.md)。
