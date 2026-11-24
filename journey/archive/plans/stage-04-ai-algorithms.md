# Stage 04：AI 算法与计算特征

目标是理解主要 AI 工作负载的前向计算，估算运算和数据访问，并分析硬件需求。Track B 为 AI 芯片与 NPU 架构，必要时联系 Track A。预计 **33–50 小时**，额外补课和调试另计；不设强制日期，大学课程优先。随实际掌握情况拆分任务，不降低验收。

**前置**：Stage 02 的矩阵乘法、复杂度与访存；Stage 03 的存储层次与性能；大学线代中的矩阵维度及 Python/NumPy 基础。缺口先补、复测；已有 C++ 矩阵项目和课程练习可复用，不重复造项目。[资源清单](../resources/learning-resources.md)列出官方链接与限制。

**知识范围**：矩阵与 GEMM、CNN 和卷积、Transformer、Attention、Softmax、激活函数、量化及 INT8/INT4、FLOPs、带宽与数据复用、Roofline。工作量和访存均须注明数据类型、计算口径与存储层级，不把理论估算写成实测。

## 入阶段诊断与调整

不查资料尝试：①`A` 为 2×3、`B` 为 3×4，求 `AB` 的形状与乘加次数；②输入 5×5、卷积核 3×3、步长 1、无填充且单通道，求输出形状；③对 Q 为 2×4、K 为 3×4、V 为 3×5，写出 `QKᵀ` 和 `softmax(QKᵀ)V` 的形状；④解释 8 位与 4 位理想原始存储及量化误差的区别。逐项记录原题、推导、求助和复核依据；独立正确并解释为已掌握，部分正确为部分掌握，无法完成为未掌握。弱项先按相关任务补充并复测，已掌握可跳过重复练习但仍须通过独立验收。作答后再展开核对点并核对原始资料。

<details><summary>诊断核对点（作答后展开）</summary>

① 输出 2×4，每个输出有 3 次乘加，共 24 次 MAC；若 1 MAC 计作 2 FLOPs，则按此约定为 48 FLOPs。② 输出 3×3。③ 两个结果分别为 2×3、2×5。④ 理想存储分别为每元素 8、4 bit，低位宽可表示等级更少，误差与数值范围、scale 和舍入等规则有关；实际还需考虑打包与元数据开销。

</details>

## 里程碑与独立验收

| 里程碑 | 成果与独立验收 |
|---|---|
| M01 诊断 | 四类均有证据、分级与必要补救 |
| M02 GEMM | 对新矩阵尺寸手算形状、乘加与理想访问量，并用独立脚本核对 |
| M03 CNN | 对新卷积配置推算输出维度、乘加及参数量，并与 NumPy 参考一致 |
| M04 Transformer | 给出指定输入的 Attention 维度和一次数值结果，解释 Softmax 与激活 |
| M05 量化与瓶颈 | 使用真实计算结果比较误差与理论存储，并在明确假设下判断计算/带宽上界 |

### S04-M01-T01 前置知识诊断

- **Objective**：定位矩阵、卷积、Attention、数值精度的起点。
- **Track**：B。
- **Prerequisites**：Stage 02–03；线代和 Python 基础。
- **Learning Materials**：MIT 18.06；NumPy `matmul`；Stanford CS231n；Transformer 原论文。
- **Actions**：完成上述四题；独立核对形状、运算次数和误差解释；按项记录分级、资料与补救。
- **Estimated Hours**：3–5。
- **Deliverables**：原始作答、判分依据及复测计划。
- **Verification**：手算与独立脚本或资料交叉核对。
- **Acceptance Criteria**：四类均有明确状态、证据与必要补救，不能以其他题正确抵消缺口。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S04-M02-T01 GEMM 参考计算与复杂度

- **Objective**：连接矩阵运算、计算量和访存。
- **Track**：B。
- **Prerequisites**：T01 与必要补救；矩阵乘法。
- **Learning Materials**：NumPy `matmul`；MIT 18.06；Roofline 原论文。
- **Actions**：为 `M×K` 乘 `K×N` 推导输出尺寸、MAC 数及 FLOPs 口径；估算理想输入/输出字节数并注明是否含读写 C；用 NumPy 验证小矩阵及非方阵；与现有 Stage 02 项目的访问模式联系。
- **Estimated Hours**：6–9。
- **Deliverables**：推导、计算脚本、小矩阵结果及内存模型假设。
- **Verification**：手算非方阵与脚本逐元素比较，检查维度和计数。
- **Acceptance Criteria**：能对新尺寸独立给出 MAC、约定的 FLOPs 与指定层级下的理想流量，说明理想流量不等于实测。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S04-M03-T01 CNN 卷积与激活

- **Objective**：分析卷积工作负载及数据复用。
- **Track**：B。
- **Prerequisites**：M02；Python 数组索引。
- **Learning Materials**：Stanford CS231n 卷积笔记；NumPy 文档。
- **Actions**：定义批量、通道、卷积核、步长和填充；推导输出尺寸、权重数及 MAC；用 NumPy 实现单层小卷积与 ReLU；用手算边界及多通道样例验证；说明输入和权重的复用。
- **Estimated Hours**：7–10。
- **Deliverables**：维度和 MAC 推导、参考脚本、测试输入输出与复用说明。
- **Verification**：至少覆盖非零填充、步长和多通道中的两种条件，逐元素对照独立预期。
- **Acceptance Criteria**：声明条件下输出形状和数值匹配；能解释卷积与矩阵计算的关系及计算假设。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S04-M04-T01 Attention 与 Transformer 前向计算

- **Objective**：理解注意力的张量形状及计算开销。
- **Track**：B。
- **Prerequisites**：M02；指数和矩阵运算。
- **Learning Materials**：Attention Is All You Need；MIT 6.5940；NumPy `matmul`。
- **Actions**：拆解 Q/K/V 投影、缩放点积、Softmax、多头拼接、输出投影及前馈层；标注尺寸；用 NumPy 对小输入逐步计算；估算序列长度变化对 Attention 矩阵的影响，说明非线性激活作用。
- **Estimated Hours**：9–14。
- **Deliverables**：前向流程与形状表、参考脚本、手算样例、计算与流量估算。
- **Verification**：检查 Softmax 每行和及数值稳定性；与独立手算对照小样例；说明是否包含 mask、bias 和其他模块。
- **Acceptance Criteria**：新输入尺寸下能独立推导各关键形状、计算量及二次增长的假设；参考结果与手算在声明容差内一致。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S04-M05-T01 INT8/INT4 量化与 Roofline

- **Objective**：分析精度、存储和计算/带宽瓶颈之间的关系。
- **Track**：A、B。
- **Prerequisites**：M02–M04；Stage 02 性能测量。
- **Learning Materials**：Roofline 原论文；MIT 6.5940 量化材料；NumPy 文档。
- **Actions**：明确对称或非对称量化、scale、zero-point、舍入、饱和及累加位宽；对同一组实际小矩阵分别量化 INT8/INT4 并反量化，与浮点参考比较误差；列理想存储和元数据开销；选定峰值算力、带宽与访存层级，计算算术强度和理论上界。
- **Estimated Hours**：8–12。
- **Deliverables**：量化脚本、输入与输出、误差数据、存储计算、Roofline 假设及结论。
- **Verification**：手算一个量化及饱和边界并核对脚本；检查单位与两种瓶颈上界。
- **Acceptance Criteria**：能独立解释误差、累加位宽和数据复用的影响；区分理论估算、测量数据和适用范围，不声称低比特必然带来实测加速。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。
