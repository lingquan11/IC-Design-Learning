# Stage 05：NPU 微架构

**目标**：将 AI 工作负载映射为计算、存储、数据搬运、调度协同的硬件系统，不能把 NPU 简化为矩阵乘法阵列。建议前置：Stage 01 的 RTL 和自检能力、Stage 02 的访存分析、Stage 03 的计算机体系结构和 Stage 04 的 GEMM/量化与工作负载分析。预计 **53–80 小时**，不含因诊断而安排的补课；按实际反馈调整细节，不按日期强制完成。资源的官方链接和使用限制见[学习资源](../resources/learning-resources.md)。

所有任务初始状态为 `NOT_STARTED`，计划中的成果为 `PLANNED`。下面的任务为后续细化基础，须在实际执行时冻结规格、时间和验收数据来源；仿真、模型和实际芯片结果不可混淆。

## 前置诊断

独立作答并保存题目、推导、证据及求助情况：①设 A 为 2×3、B 为 3×2，计算 C=AB 的输出维度及所需 MAC 数（只计矩阵乘法，不含额外偏置）；②解释寄存器、片上 buffer、外部存储的层次与带宽；③画出一个带使能和复位的有符号 MAC，说明乘法、累加位宽及溢出规则；④某工作负载的算术强度为 1 MAC/字节、峰值计算吞吐量为 16 MAC/周期、目标存储层级带宽为 8 字节/周期，求 Roofline 理论上界并说明假设。对于每项：正确且独立解释并经计算或仿真复核为“已掌握”；思路部分正确或需提示为“部分掌握”；无法完成或核心错误为“未掌握”。薄弱项回 Stage 01–04 对应任务补足并用同类新题复测；已掌握项允许跳过重复学习，不跳过里程碑验收。

<details>
<summary>作答后展开数值题参考答案</summary>

①输出为 2×2，需 12 次 MAC；④上界为 min(16, 1×8)=8 MAC/周期，只是给定模型和该存储层级下的上界，不是实测性能。

</details>

## 里程碑和初步任务

### M01 计算单元：S05-M01-T01 MAC 与 PE

- **Objective**：设计位宽和控制明确的 MAC、处理单元 PE。
- **Track**：A、B。
- **Prerequisites**：诊断通过；有符号运算、同步时序 RTL 与自检 testbench。
- **Learning Materials**：MIT 6.5930 Hardware Architecture for Deep Learning；MIT Eyeriss 教程；资源清单中的仿真器文档。
- **Actions**：定义数据格式、乘积与累加位宽、溢出、复位、使能和流水周期；分析 INT8/INT4 量化硬件中的符号扩展、累加位宽、缩放、舍入及饱和，明确哪些实际实现；实现 MAC 与封装 PE；以独立参考模型测试正负数、最大最小值、使能停顿、复位及溢出。
- **Estimated Hours**：12–18。
- **Deliverables**：规格、RTL、testbench、运行环境与实际结果。
- **Verification**：逐周期比较输入、预期及实际输出；注入错误确认测试有效。
- **Acceptance Criteria**：上述边界通过、输出周期与位宽符合规格；能独立推导一次累加并解释溢出语义，画出量化值到累加及重定标的路径并标记尚未实现部分。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### M02 数据流：S05-M02-T01 小规模脉动阵列与映射

- **Objective**：理解 PE 协作、数据复用和阵列利用率。
- **Track**：A、B。
- **Prerequisites**：M01；矩阵乘法正确性与时序波形分析。
- **Learning Materials**：MIT 6.5930；MIT Eyeriss 教程中的数据流和复用。
- **Actions**：为 2×2 PE 阵列定义输入倾斜、累加及输出时间；用手算绘制周期表；实现阵列并模拟矩阵乘法；比较 weight stationary、output stationary、row stationary 的数据停留和搬运，不假设三者都已实现。
- **Estimated Hours**：15–22。
- **Deliverables**：数据流图、逐周期表、RTL、测试及不同数据流比较。
- **Verification**：将多个小矩阵（含零、负数及边界）与独立软件结果逐元素对照，并检查周期表。
- **Acceptance Criteria**：测试结果和数据到达/输出周期均符合规格；用有依据的计数说明一个算例的有效 PE 周期与利用率；明确三种数据流比较的假设。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### M03 存储与搬运：S05-M03-T01 Buffer、DMA 和互连

- **Objective**：设计支撑阵列的存储与搬运方案。
- **Track**：A、B。
- **Prerequisites**：M02；存储层次与有限状态机。
- **Learning Materials**：MIT Eyeriss 教程；MIT 6.5930；Roofline 原论文。
- **Actions**：为选定矩阵分块画片外存储、SRAM/buffer、PE 和输出之间的数据路径；估算容量、读写次数及带宽；说明 DMA 事务、握手、数据移动与简化 NoC/互连职责；实现并自检一个小 buffer 或调度控制模块，将其与 M02 阵列集成为固定规模矩阵乘法加速器；规定启动、搬运、计算和完成顺序，DMA/NoC 可以用明确标记的接口模型代替实体实现。
- **Estimated Hours**：16–24。
- **Deliverables**：容量和带宽计算、存储及互连图、buffer 或控制模块及集成加速器 RTL、testbench、运行结果。
- **Verification**：用手算小例逐笔核对传输次数；仿真边界、读写冲突约定、满/空或地址边界以及复位；端到端比较完整矩阵计算与独立软件结果，检查启动、完成和数据搬运顺序。
- **Acceptance Criteria**：数据容量和流量可由任务形状复算；实现模块及集成的固定规模矩阵乘法测试通过，控制和数据搬运顺序与规格一致；明确未实现的 DMA 和 NoC 部分，不将示意设计标记为实物。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### M04 性能与能效：S05-M04-T01 系统建模

- **Objective**：结合计算、存储、数据流与调度分析系统瓶颈。
- **Track**：A、B。
- **Prerequisites**：M02、M03；Stage 04 工作负载及 Roofline 分析。
- **Learning Materials**：Roofline 原论文；MIT Eyeriss 教程；MIT 6.5930。
- **Actions**：对同一 GEMM 形状给出计算量、片上/片外流量、带宽与峰值吞吐假设；计算算术强度、模型上界和考虑阵列填充/排空的周期估计；对不同分块或数据流作敏感性比较；使用明确来源的单位能耗假设估算数据搬运及计算能耗。
- **Estimated Hours**：10–16。
- **Deliverables**：参数表、可复算模型、比较结果与限制说明。
- **Verification**：对最小实例手工核对次数和单位；与 M02 仿真的周期逐项比较，解释差异。
- **Acceptance Criteria**：算式、单位和数据来源完整；区分理论上界、模型估计、实测值；若缺少可信能耗参数，仅列公式与所需参数，不虚构结果。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

里程碑独立验收分别以各任务验收为最低要求：M01 独立说明数值格式与边界；M02 给出未经模板代写的新小矩阵周期表；M03 独立推导流量并指出未建模的系统部分；M04 独立解释计算瓶颈和带宽瓶颈随假设变化的条件。全部要求与证据通过后才将对应任务标为 `COMPLETED`；能力解释证据单独记录。
