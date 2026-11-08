# 七阶段路线

七阶段主线顺序固定；课程映射见 [CURRICULUM_MAP](CURRICULUM_MAP.md)，正式大学课程提供知识骨架，导师解释和工程任务按需补充。支线按当前课程及任务需要插入，先完成入阶段诊断，再修复缺口。任务的真实前置满足时，可在主线之外适量复盘已有矩阵项目或提前接触综合概念；这不等于跳过阶段验收，也不改变主线顺序。阶段和里程碑的任务、工时及验收以各计划为准，不以日历强制推进。当前可用时间约每周 6–8 小时，考试周降低投入；估时超出时拆分任务，不降低验收标准。后续阶段工时均为低置信度初估，按实际反馈校准。

| 阶段 | 路线和主要里程碑 | 能力轨道 | 前置与预计投入（估算） |
|---|---|---|---|
| [01 数字电路与 Verilog](plans/stage-01-digital-circuits.md) | 数制与组合逻辑 → CMOS 和基础 RTL → 时序 → FSM → 4-bit ALU | A | 入阶段诊断；约 49–74 小时 |
| [02 C++ 矩阵乘法优化](plans/stage-02-matrix-optimization.md) | 盘点现有项目 → 正确性 → 计时与局部性 → 分块、SIMD 与分析 | B | 01；C++、矩阵和实验基础诊断；已有证据可减少重复 |
| [03 计算机组成与体系结构](plans/stage-03-computer-architecture.md) | ISA、数据通路 → 流水线 → Cache → RISC-V 子集 CPU | A、B | 01–02 的 RTL、验证与访存基础 |
| [04 AI 算法与计算特征](plans/stage-04-ai-algorithms.md) | GEMM → 卷积 → Attention/Transformer → 量化与屋顶线 | B | 02–03；线代与 Python |
| [05 NPU 微架构](plans/stage-05-npu-microarchitecture.md) | MAC/PE → 阵列与数据流 → 存储、搬运和调度 → 建模 | A、B | 01、03–04 |
| [06 数字 IC 设计流程](plans/stage-06-digital-ic-design.md) | 综合与网表 → STA → 布局布线 → 有条件的 PPA 分析 | A | 01、05；工具与计算资源检查 |
| [07 完整 AI 加速器](plans/stage-07-ai-accelerator.md) | MVP → Intermediate → Advanced，各自独立验收 | A、B | 01–06；真实流片非必要 |

轨道 A 是数字 IC 设计：RTL、验证、综合、STA、物理设计与 PPA。轨道 B 是 AI 芯片架构：性能、体系结构、算法计算、数据流与建模。两者在阶段 07 汇合。[数学、模拟电路、验证及工具支线](plans/supporting-tracks.md) 随任务按需学习，不另设主阶段。

## 阶段成果与独立验收

| 阶段 | 目标成果 | 进入下一阶段前的验收摘要 |
|---|---|---|
| 01 | 基础门电路、加法器、计数器、移位寄存器、FSM、4-bit ALU 和 testbench | 独立解释组合/时序、时钟复位；RTL 自检和独立验收通过，能说明覆盖限制 |
| 02 | 复用现有矩阵乘法项目，补足正确性、分块、基准与实验报告 | 能独立解释算法、局部性与测试设计，真实数据和贡献来源可追溯 |
| 03 | 数据通路、有限指令子集 CPU、流水线实践、Cache 模拟器 | 可追踪指令与冒险，依据独立测试解释处理与缓存行为，明确 ISA 子集 |
| 04 | GEMM、卷积、Attention/Transformer、精度和流量分析 | 独立推导算量、形状及访存假设，参考小样例核验，区分模型与实测 |
| 05 | MAC、PE、小阵列、Buffer、数据流及性能模型 | 独立解释数据流、搬运与调度，计算模型与功能验证可复查 |
| 06 | 已验证设计的综合、时序及教学物理实现和 PPA 报告 | 指出工具、工艺、约束及报告边界，说明教学流程与工业签核/真实流片的区别 |
| 07 | 分层 AI 加速器：需求、架构、RTL、测试、报告与总结 | MVP、Intermediate、Advanced 各按阶段文件独立验收，记录范围及未覆盖项，真实流片非必要 |

从 [真实进度](PROGRESS.md) 找当前任务，从对应阶段文件查动作和验收；每周使用 [复盘模板](templates/weekly-log-template.md)。学习材料集中在 [资源清单](resources/learning-resources.md)。
