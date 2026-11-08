# Stage 07：完整 AI 加速器项目

目标：整合计算、存储、数据搬运、控制、验证和实现流程，完成分层验收的加速器项目。前置为 Stage 01–06 的对应验收，重点复用 Stage 05 已有阵列和模块；缺口先补，不另建重复项目。资源与工具见[资源表](../resources/learning-resources.md)。每个任务初始 `NOT_STARTED`，成果初始 `PLANNED`，实际实现、验证与独立解释证据分别记录。真实芯片流片不是本阶段或任何层次完成的必要条件。

预计 MVP 30–46 小时、Intermediate 30–48 小时、Advanced 60–100 小时；合计约 120–194 小时，不含先修补课和环境故障排查。按实际课业负荷拆分；每层达标即可独立记录，不以前一层通过推定后一层通过。高级层可按诊断和实际需求分批实现，但完整验收保留以下全部能力范围。

## 入阶段诊断

独立完成并记录用时、求助和证据：对 A、B 均为 2×2、元素为有符号 8 位、输出以足够宽累加器保存的矩阵乘法，①画出输入、输出、控制、buffer、MAC 与存储之间的接口，写清复位及完成条件；②计算乘加次数及在单 MAC 每周期完成一次且无额外开销的理想下界；③列出至少三类边界测试与预期；④解释 RTL 功能仿真通过为何不能证明 STA 和 PPA 通过。逐项独立正确且可解释/复核为已掌握，需提示或不完整为部分掌握，无法完成或核心错误为未掌握；薄弱处回相应阶段补足，并用同类新题复测，不以看过材料判定。

<details><summary>作答后查看核对点</summary>

结果是 2×2，共 8 次 MAC；在题设理想条件下至少 8 周期，仅为计算下界。完整系统还需考虑装载、控制、排空和输出。测试可包括正负值、全零、极值与累加溢出规则、复位中断及握手边界；具体预期必须以规格计算。功能仿真与工艺库、时钟约束、路径时序和功耗模型是不同证据。
</details>

## M01：MVP

里程碑独立验收：规定输入输出及位宽；RTL 对声明的矩阵规模以独立参考模型完成常规、边界、复位和完成信号验证；从干净环境按命令重跑并独立解释数据流和覆盖局限。交付需求、架构图、微架构、RTL、testbench、仿真记录和 README；没有报告的综合与 PPA 留在计划中。

### S07-M01-T01：需求与最小架构

- **Objective**：定义可实现且可验证的矩阵乘法加速器 MVP。
- **Track**：A、B。
- **Prerequisites**：Stage 05 的 MAC、数据流和参考模型；上述诊断。
- **Learning Materials**：MIT 6.5930、Eyeriss 教程和本仓库项目模板。
- **Actions**：盘点 Stage 05 既有实现；选定矩阵规模、输入输出协议、数值格式、复位、溢出和完成条件；画系统架构与逐周期数据流；建立测试计划及手算例子。
- **Estimated Hours**：8–12。
- **Deliverables**：需求、架构图、微架构说明、测试计划及已有模块映射。
- **Verification**：用手算样例检查接口和数值约定，并逐条对应测试用例。
- **Acceptance Criteria**：每条功能要求均可检查，输入范围和不支持事项明确，独立解释数据流。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S07-M01-T02：RTL、自检与交付

- **Objective**：完成符合规格的最小实现及验证闭环。
- **Track**：A、B。
- **Prerequisites**：T01；阶段 01、05 的 RTL 和 testbench。
- **Learning Materials**：Icarus Verilog 文档、现有 RTL 与项目模板。
- **Actions**：复用或修改既有模块；实现数据路径和控制；编写独立参考模型、自检 testbench 和运行脚本；覆盖常规、边界、复位及完成行为；留存代码版本、环境、波形、结果与贡献说明。
- **Estimated Hours**：22–34。
- **Deliverables**：RTL、参考模型、测试、脚本、实际仿真记录、README 和 MVP 总结。
- **Verification**：按运行说明从干净构建执行回归，逐元素比较；临时注入错误验证测试能报错，再恢复并重跑。
- **Acceptance Criteria**：声明范围的测试均通过且可复现；能独立解释设计与测试盲区；未验证内容不标 VERIFIED。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

## M02：Intermediate

里程碑独立验收：多种支持的矩阵尺寸、Buffer 与数据流控制通过回归；周期模型与仿真比较且解释偏差；在记录工具、库与约束的前提下提供综合报告和可获得的 PPA。若没有可信功耗模型或活动数据，功耗标记不可得，不能虚构。

### S07-M02-T01：Buffer 与可配置数据流

- **Objective**：扩展存储控制及多种矩阵规模。
- **Track**：A、B。
- **Prerequisites**：M01 验收；Stage 05 buffer、握手和数据搬运。
- **Learning Materials**：Eyeriss 教程、Gemmini 架构文档及原项目规格。
- **Actions**：定义容量、分块、输入输出协议与支持的尺寸；实现或复用 Buffer 和控制；覆盖非整除尺寸、复位、背压（若接口支持）及地址边界。
- **Estimated Hours**：16–26。
- **Deliverables**：修订规格、RTL、控制图、测试计划和实际回归结果。
- **Verification**：对多个尺寸与独立模型比较并检查存储地址和协议。
- **Acceptance Criteria**：所有声明支持的输入及边界测试通过；限制、未支持协议和测试缺口明确。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S07-M02-T02：性能模型与综合报告

- **Objective**：把周期估算与开源实现结果联系起来。
- **Track**：A、B。
- **Prerequisites**：T01；Stage 06 综合与时序基础。
- **Learning Materials**：Roofline 原论文、Yosys、OpenSTA 和 OpenLane 官方文档。
- **Actions**：按计算、加载、输出、填充/排空与可能重叠建立周期模型；记录仿真周期并分析差异；针对已验证版本综合，记录工具版本、库、约束、网表及面积/时序报告；有条件时依据活动数据估算功耗。
- **Estimated Hours**：14–22。
- **Deliverables**：模型、仿真与模型对照、综合脚本及报告、PPA 分析和项目总结。
- **Verification**：对至少两种尺寸手算复核与回归；检查约束有效，报告对应同一版本及配置。
- **Acceptance Criteria**：模型假设和偏差可解释，报告可追溯且不把教学结果称为工业 sign-off；缺失功耗如实标注。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

## M03：Advanced

里程碑独立验收：在明确约定的项目范围内，量化、更复杂 AI 工作负载、片上存储管理、调度优化和 SoC 集成均须有规格、可运行实现和对应验证证据。每项可限定为可完成的子集，但不得仅靠示意图或模型冒充实现；误差标准在实验前定义。可以分批推进并记录部分成果，仍有上述项目未实现或未通过时，Advanced 保持未完成。

### S07-M03-T01：量化与工作负载扩展

- **Objective**：在更复杂 AI 工作负载上实现并评估量化计算与误差。
- **Track**：A、B。
- **Prerequisites**：M02 验收；Stage 04 量化与 Stage 05 数值格式。
- **Learning Materials**：MIT 6.5940、NumPy 文档与既有参考模型。
- **Actions**：选择 INT8 或 INT4 量化，并选择一个超出基础矩阵乘法的 AI 工作负载及其可完成子集；定义缩放、舍入、饱和、累加和误差阈值；实现并与高精度参考比较；记录数据分布和误差。
- **Estimated Hours**：25–40。
- **Deliverables**：数值规格、实现、输入及参考模型、测试数据和误差报告。
- **Verification**：覆盖极值、零和典型值；按声明规则逐项比较并记录误差。
- **Acceptance Criteria**：声明范围内满足事先设定的误差或精确整数规则；如未满足，保留失败和修复记录，不宣称通过。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S07-M03-T02：存储管理、调度与 SoC 集成

- **Objective**：验证片上存储管理、调度优化和 SoC 集成的可实现子集。
- **Track**：A、B。
- **Prerequisites**：T01；Stage 05 搬运、Stage 03 互连。
- **Learning Materials**：Gemmini 系统架构、MIT 6.5930 与所选协议的官方文档。
- **Actions**：分别限定片上存储管理、调度优化与 SoC 接口的范围和协议；实现这三部分的可验证子集并测试；比较调度或存储调整前后的周期、数据搬运和适用条件。
- **Estimated Hours**：35–60。
- **Deliverables**：接口及调度说明、实现、测试、实际对照数据、最终 README 与项目总结。
- **Verification**：在相同输入和计数口径下测试功能及边界，对照原始版本；记录环境和数据来源。
- **Acceptance Criteria**：三个方面的声明子集均有可运行实现且测试通过、可复现，对照结果支持结论；无提升也可如实验收。任何方面未实现时保留为计划且不得将本任务或高级层标为完成。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。
