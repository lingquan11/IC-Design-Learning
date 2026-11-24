# Stage 03：计算机组成原理与体系结构

目标是理解指令执行、数据通路、流水线和存储层次；以小型教学设计建立可检验的模型。Track A 为数字 IC，Track B 为 AI 芯片与架构。预计 **41–61 小时**，不含针对诊断缺口的额外补课；不设强制完成日期，先保障学校课程。预计时间须按实际情况调整，超时则拆解任务，不降低验收要求。

**前置**：Stage 01 的组合与时序 RTL、状态机、自检仿真；Stage 02 的矩阵访存与基准实验基础。未达到时先修复对应缺口。资源名称及访问限制见[资源清单](../resources/learning-resources.md)。允许复用 Stage 01 已验证 ALU 和 Stage 02 访存证据，先核对接口、许可和覆盖范围，不重复创建项目。

**知识范围**：ISA 与指令编码、寄存器/PC、ALU、数据通路与控制器、取指到写回、单周期实现、流水线、数据/控制冒险及转发与暂停、Cache 和存储层次、总线与互连、并行与性能、RISC-V。具体任务随前一阶段实际结果迭代，维持七阶段顺序。

## 入阶段诊断与调整

不查资料先尝试：①用自己的话区分 ISA、微架构，并写出 `add x3,x1,x2` 对寄存器的变化；②给定寄存器 `x1=5, x2=7`，解释该指令所需数据通路及执行后 `x3`；③紧跟 `add x4,x3,x1`，解释依赖、两种解决方式；④对 4 行直接映射 Cache（块大小 1 字），从空缓存依次访问字地址 `0,4,0`，列出命中/缺失。逐项记录题设、解法、求助及复核依据：独立正确且解释完整为“已掌握”，有思路但有错误或不完整为“部分掌握”，无法完成为“未掌握”；先补缺并复测，已掌握可跳过重复学习，但里程碑的独立验收不能免除。完成作答后再查看下方核对点，并对照 RISC-V 规范与 Cache 映射规则。

<details><summary>诊断核对点（作答后展开）</summary>

① ISA 是软硬件约定的指令与可见状态，微架构是实现该约定的内部组织；该指令写入 `x3=x1+x2`。② `x3=12`，数据由寄存器堆送入 ALU，结果写回。③ 存在对 `x3` 的 RAW 依赖，可通过转发或暂停解决，具体时机取决于实现。④ 地址均映射同一行，三次均缺失。

</details>

## 里程碑与独立验收

| 里程碑 | 成果与独立验收 |
|---|---|
| M01 前置诊断 | 四项均记录证据、分级和补救；未知不得写成已掌握 |
| M02 指令与单周期数据通路 | 独立跟踪一条未练过的算术和访存指令，给出 PC、控制和寄存器变化并对照模型 |
| M03 流水线 | 对新指令序列标出冒险；说明或实现转发/暂停和分支处理并逐周期核对 |
| M04 Cache 和系统性能 | 手算新地址序列与模拟器逐项一致；解释总线/带宽及测量局限 |
| M05 教学 RISC-V CPU | 明确支持的指令子集，运行涵盖算术、访存和分支的自检程序；不声称完整 ISA 合规 |

### S03-M01-T01 前置诊断与缺口清单

- **Objective**：识别 ISA、数据通路、冒险与 Cache 的起点。
- **Track**：A、B。
- **Prerequisites**：Stage 01–02 的相应成果。
- **Learning Materials**：MIT 6.004；RISC-V RV32I 官方规范；CMU CS:APP Labs。
- **Actions**：完成上述四题；逐项与独立资料核对；为每个缺口指定补充、复测及记录日期。
- **Estimated Hours**：3–4。
- **Deliverables**：原始题解、分级、核对依据和补救清单。
- **Verification**：逐项核对，而非以总分抵消缺口。
- **Acceptance Criteria**：四项均有判定或明确待判、复测方式；不把看过资料当掌握。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S03-M02-T01 ISA 与单周期数据通路

- **Objective**：解释指令如何由硬件执行。
- **Track**：A、B。
- **Prerequisites**：T01 诊断与必要补救；Stage 01 ALU。
- **Learning Materials**：MIT 6.004 CPU 部分；RISC-V RV32I 官方规范。
- **Actions**：确定少量算术、load/store 和分支指令；画寄存器堆、PC、ALU、控制器及内存数据通路；列指令控制表；先复用既有 ALU，制作单周期数据通路模型或 RTL，并为选定指令写自检测试。
- **Estimated Hours**：8–12。
- **Deliverables**：指令子集、数据通路图、控制表、模型或 RTL、测试及运行记录。
- **Verification**：用手算指令轨迹逐步核对模型状态；覆盖正负立即数、零寄存器及基本访存。
- **Acceptance Criteria**：声明指令的状态变化与参考轨迹一致；独立解释每条指令的控制与数据流，明确未实现部分。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S03-M03-T01 流水线与冒险

- **Objective**：分析指令重叠及其正确性代价。
- **Track**：A、B。
- **Prerequisites**：M02；时序逻辑与寄存器。
- **Learning Materials**：MIT 6.004 流水线部分；RISC-V RV32I 规范。
- **Actions**：将数据通路划分流水级；画独立、数据依赖、分支序列的逐周期表；给出转发、暂停、冲刷规则；用简单模型或 RTL 实现并记录可观测的状态变化。
- **Estimated Hours**：10–15。
- **Deliverables**：流水级图、冒险表、规则、模型或 RTL 与测试。
- **Verification**：比较逐周期表与实际执行，覆盖依赖、load-use、分支及复位。
- **Acceptance Criteria**：声明范围内最终状态与顺序参考一致；能解释暂停、转发和控制冒险的代价及未覆盖情形。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S03-M04-T01 Cache 模拟与系统性能

- **Objective**：把访存映射到缓存与系统带宽。
- **Track**：B。
- **Prerequisites**：Stage 02 局部性；M01 诊断中的地址与 Cache。
- **Learning Materials**：CMU CS:APP Cache Lab；Roofline 原论文。
- **Actions**：定义块大小、组数、相联度和替换规则；先手算短访问轨迹，再编写 Cache 模拟器；对连续与跨步访问做对照；画 CPU、缓存、内存和总线示意并讨论并行度与带宽限制。
- **Estimated Hours**：8–12。
- **Deliverables**：配置、访问轨迹、手算、模拟器、测试与局限说明。
- **Verification**：至少覆盖冷缺失、命中、冲突和替换，逐访问对比手算。
- **Acceptance Criteria**：声明配置下的命中/缺失序列一致；区分模拟结果与真实硬件计数器测量。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S03-M05-T01 简单 RISC-V 子集 CPU

- **Objective**：整合数据通路、控制与功能验证。
- **Track**：A、B。
- **Prerequisites**：M02–M04；自检 testbench。
- **Learning Materials**：RISC-V RV32I 官方规范；MIT 6.004；Icarus Verilog 文档。
- **Actions**：明确支持的指令及异常/内存假设；复用前述数据通路或流水线，完成教学子集 CPU；写小程序与独立预期寄存器/内存轨迹；测试依赖、复位、边界和分支；记录互连模型与性能限制。
- **Estimated Hours**：12–18。
- **Deliverables**：规格、RTL、测试程序、testbench、运行命令、结果和覆盖缺口。
- **Verification**：逐步对照预期状态，失败报告输入、周期、期望与实际；修改后运行回归。
- **Acceptance Criteria**：已声明指令及边界测试通过，能够独立解释一段新程序；清楚说明不支持的指令、异常和不构成完整 RISC-V 一致性验证的范围。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。
