# Stage 01：数字电路与 Verilog

目标：建立数字电路与 CMOS 基础，能独立设计、仿真和解释基础 RTL。Track A 为数字 IC 设计，Track B 为 AI 芯片与 NPU 架构。资源名称、官方链接、使用范围及限制见 [学习资源](../resources/learning-resources.md)。

**课程主线**：以 MIT 6.004 Computation Structures 的官方课程材料为知识骨架，依据 [课程映射](../CURRICULUM_MAP.md) 选择当前主题的讲义、视频和可公开作业；先用正式课程建立概念并尝试官方习题，再用 HDLBits、GPT 解惑和自写 RTL 补充。MIT 6.002 仅按电路/CMOS 缺口配合学校课程穿插；它是较早的基础课程。课程缺少 Verilog 或 testbench 内容时用官方工具文档与 HDLBits 补齐，不把自拟练习称为官方作业。

**节奏**：当前反馈为每周约 6–8 小时，仅作估计，以大学课程和考试优先；以下周次是顺序建议，可跨周、暂停或合并，实际时间记录在周报。预计总计 49–74 小时，不含额外补课或反复修改。实际超过预估时拆分任务，不降低验收标准。初始计划中任务默认 `NOT_STARTED`、成果默认 `PLANNED`；当前状态以 [PROGRESS](../PROGRESS.md) 为唯一权威来源。`VERIFIED` 与 `INDEPENDENTLY_EXPLAINED` 需要分别留存证据，不能互相推断。任务的结果由学习者实际完成后记录。

## 入阶段诊断与调整

请先独立作答，再展开参考答案核对。每题记下用时与求助情况；不会时写出尝试，不猜测通过。

1. 将无符号二进制 `101101` 转成十进制和十六进制。
2. 用 8 位补码表示 −5；计算 −5 + 3 的 8 位二进制结果及其十进制值。
3. 写出两输入 XOR 的完整真值表。使用布尔代数或卡诺图化简 `F = (~A & B) | (A & B) | (A & C)`，并用真值表验证。
4. 某正边沿触发 D 寄存器采用**同步高有效复位**：每个上升沿若 `rst=1` 则 Q 置 0，否则 Q 取该沿 D。下表给出各上升沿前稳定的输入，请写出每个上升沿之后的 Q。第一次上升沿前的 Q 未知。

   | 上升沿序号 | 1 | 2 | 3 | 4 | 5 |
   |---|---:|---:|---:|---:|---:|
   | rst | 1 | 0 | 0 | 1 | 0 |
   | D | 1 | 0 | 1 | 0 | 1 |
   | Q（作答） |  |  |  |  |  |

5. 用 Verilog 写模块 `mux2`：输入 `a`、`b`、`sel` 均为 1 bit，输出 `y` 为 1 bit；`sel=0` 时 y=a，`sel=1` 时 y=b。列出全部测试输入、期望输出，并说明如何在仿真中自动发现错误。无法写出代码时可先写伪代码，标记缺口。

<details>
<summary>完成作答后展开参考答案</summary>

1. `101101₂ = 45₁₀ = 2D₁₆`。
2. −5 为 `11111011`，加 3 (`00000011`) 得 `11111110`，即 −2；此题没有第 9 位进位。若其他 8 位运算产生第 9 位进位，则按固定位宽约定丢弃。
3. XOR 真值表：00→0、01→1、10→1、11→0。由于 `(~A & B) | (A & B) = B`，故 `F = B | (A & C)`；依 `ABC=000,001,010,011,100,101,110,111` 排列，F 依次为 `0,0,1,1,0,1,1,1`。
4. 各沿后的 Q 依次为 `0, 0, 1, 0, 1`。同步复位只在上升沿生效。
5. 可使用 `assign y = sel ? b : a;`；穷举 a、b、sel 共 8 组，以独立期望表达式或真值表比较，错误时报告并使仿真失败。完整模块与自检测试应独立编写。

</details>

每类分别记录 0/1/2 分：0=无法独立作答或核心概念错误；1=有可用思路但结果或解释不完整；2=在不查资料、不依赖 AI 的情况下正确作答并解释，且用独立参考答案或仿真复核。评分不取总分抵消短板：每类 2 分视为已掌握、1 分为部分掌握、0 分为未掌握。部分及未掌握内容先执行对应补充任务并复测；已掌握内容可跳过重复练习，但须完成相应里程碑独立验收。记录题目、答案、判分依据、求助与复测日期；答案不充分时标记待判，不自动判满分。开始阶段时并不预设任何题已通过。

## 周次与里程碑

| 周次 | Task | 预计小时 |
|---|---|---:|
| 1 | S01-M01-T01、T02：诊断和数制 | 4–7 |
| 2 | S01-M01-T03：布尔代数、组合逻辑与锁存器 | 4–6 |
| 3 | S01-M02-T01：电路和 CMOS | 4–6 |
| 4 | S01-M02-T02：门电路 RTL、SystemVerilog 与仿真 | 4–6 |
| 5 | S01-M02-T03：参数化多路选择器和加法器 | 5–7 |
| 6 | S01-M03-T01：触发器、时钟与复位 | 3–5 |
| 7 | S01-M03-T02：计数器 | 4–6 |
| 8 | S01-M03-T03：移位寄存器与时序 | 4–6 |
| 9 | S01-M04-T01：有限状态机 | 4–6 |
| 10 | S01-M04-T02：状态机验证 | 4–6 |
| 11 | S01-M05-T01：4-bit ALU | 5–7 |
| 12 | S01-M05-T02：回归与独立验收 | 4–6 |

表中周次是建议顺序而非任务开始限制：第 1 周在不影响诊断独立性的前提下，若仿真器可用，提前试运行 S01-M02-T02 的最小门电路示例；第 2 周学习组合逻辑时完成同任务中的一个门电路自检。第 4 周继续完成其余门电路、波形和 SystemVerilog，避免重复计时，49–74 小时是原任务估时合计，不因拆分另加。环境未就绪时先完成课程材料，记录障碍并稍后补做，不以示例运行代替独立任务验收。

- **M01 数制和组合逻辑**：不查资料完成数制与补码题和布尔化简题，用完整真值表验证化简结果，并解释组合逻辑；错题先修复。
- **M02 CMOS 和组合 RTL**：独立解释 CMOS 反相器，独立实现并穷举测试指定的多路选择器与 4-bit 加法器。
- **M03 时序逻辑**：根据输入、时钟、复位波形准确画出寄存器输出；独立实现验证计数器，区分 setup、hold 与周期约束。
- **M04 有限状态机**：根据新的文字需求画状态图并独立实现；验证复位、主要转移、连续输入及非法状态恢复。
- **M05 4-bit ALU**：明确操作与位宽后穷举测试所有声明的操作及输入，并独立说明 RTL、测试覆盖及局限。各里程碑通过须有解题或设计过程、验证结果和独立验收记录；有编程任务时还须保留代码和测试。

## M01 数制和组合逻辑

### S01-M01-T01 入阶段诊断

- **Objective**：确定真实起点，识别需修复的知识。
- **Track**：A、B。
- **Prerequisites**：无。
- **Learning Materials**：MIT 6.004 数字逻辑；HDLBits 入门；见资源清单。
- **Actions**：按上方诊断完成题目；记录时间、求助、错误；按每类评分并决定补充任务。
- **Estimated Hours**：2–3。
- **Deliverables**：题目、答案、评分依据及调整记录。
- **Verification**：使用独立答案复核；代码可运行时记录命令和结果。
- **Acceptance Criteria**：每类均有证据、状态和必要的补救措施，不会的内容明确留空或记录尝试。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S01-M01-T02 数制与编码

- **Objective**：掌握数字表示与固定位宽运算。
- **Track**：A、B。
- **Prerequisites**：T01。
- **Learning Materials**：MIT 6.004 数字表示；HDLBits 基础练习。
- **Actions**：练习二进制、十六进制互转；表示无符号数和有符号补码；计算固定位宽加减及溢出。
- **Estimated Hours**：2–4。
- **Deliverables**：至少六道覆盖转换、补码、溢出的练习及订正。
- **Verification**：手算，并用脚本或独立计算器复核。
- **Acceptance Criteria**：独立完成转换、补码、溢出各一题；解释截断与溢出的区别，错误题重新独立完成。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S01-M01-T03 布尔代数与组合逻辑

- **Objective**：从需求推导和化简组合电路。
- **Track**：A。
- **Prerequisites**：T02。
- **Learning Materials**：MIT 6.004 数字逻辑；HDLBits 组合逻辑。
- **Actions**：列真值表；用布尔恒等式和卡诺图化简；画门级电路；完成编码器或比较器练习；分析门控 D 锁存器在使能有效和无效时的行为，比较电平敏感锁存器与边沿触发器。
- **Estimated Hours**：4–6。
- **Deliverables**：真值表、化简过程、门级图、锁存器行为分析与独立验收题。
- **Verification**：比较所有输入组合的化简前后结果。
- **Acceptance Criteria**：所有输入一致，能说明无关项及其使用前提；能根据使能和输入变化预测锁存器输出，并解释其与触发器的区别。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

## M02 CMOS 和组合 RTL

### S01-M02-T01 基础电路与 CMOS

- **Objective**：理解 CMOS 逻辑的基础物理背景。
- **Track**：A。
- **Prerequisites**：M01；必要时补 KCL、KVL 和电阻网络。
- **Learning Materials**：MIT 6.002 电路、MOS/CMOS 相关部分；IEEE The Beauty of Circuits。
- **Actions**：计算一个电阻或 RC 电路；在长沟道增强型 NMOS 简化模型下，以源极为参考并假设 VDS≥0，利用 VGS、VDS 和阈值区分截止、线性区和饱和区，说明开关简化模型的适用范围与局限；画 CMOS 反相器并分析高低输入下导通路径；说明传播延迟、静态和动态功耗、噪声容限。
- **Estimated Hours**：4–6。
- **Deliverables**：电路计算、反相器图、概念说明和疑点。
- **Verification**：对照材料核对计算与导通关系。
- **Acceptance Criteria**：根据给定 NMOS 电压及阈值判断截止（VGS<Vth）、线性区（VGS>Vth 且 VDS<VGS−Vth）或饱和区（VGS>Vth 且 VDS≥VGS−Vth）并说明模型假设；边界按所用课程模型处理；独立解释反相器两种稳态和切换，定性说明负载电容与活动频率对动态功耗和延迟的影响；不声称完成精确器件建模。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S01-M02-T02 门电路 RTL 与仿真

- **Objective**：建立模块、端口和可重复仿真的最小闭环。
- **Track**：A。
- **Prerequisites**：M01；命令行基础。
- **Learning Materials**：HDLBits 入门；Icarus Verilog 官方文档。
- **Actions**：可在第 1 周先尝试运行官方工具入门示例，第 2 周随组合逻辑尝试一个门电路；确认仿真器可用；编写 NOT、AND、XOR 模块及自检 testbench；运行仿真，查看至少一个波形；用基础 SystemVerilog 的 `logic` 和 `always_comb` 改写一个组合模块，确认仿真器的 SystemVerilog 模式及命令行选项。第 4 周完成余下内容。
- **Estimated Hours**：4–6。
- **Deliverables**：RTL、testbench、工具版本、运行命令、实际结果和波形说明。
- **Verification**：穷举各模块输入；临时引入逻辑错误，确认测试报错后恢复并重跑。
- **Acceptance Criteria**：全部输入符合真值表；故障能被检出；能解释端口、组合赋值、`logic`、`always_comb` 及测试结果，且记录 SystemVerilog 模式运行命令。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S01-M02-T03 多路选择器与加法器

- **Objective**：实现组合数据通路，建立边界测试习惯。
- **Track**：A。
- **Prerequisites**：T02。
- **Learning Materials**：MIT 6.004 组合模块；HDLBits 多路选择器和加法器。
- **Actions**：使用参数定义数据位宽，实现 2:1 多路选择器，并实现 4-bit 加法器；写独立预期值；对多路选择器至少两个位宽（例如 1 和 2）和 4-bit 加法器穷举输入；检查组合赋值完整性。
- **Estimated Hours**：5–7。
- **Deliverables**：RTL、自检 testbench、运行命令、实际结果及说明。
- **Verification**：对所有输入比较输出与参考结果；临时修改逻辑确认测试可检出，恢复后重跑。
- **Acceptance Criteria**：两个参数位宽的选择器与 4-bit 加法器穷举比较均无错误；能解释参数、进位和位宽。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

## M03 时序逻辑

### S01-M03-T01 触发器、时钟与复位

- **Objective**：区分组合和时序逻辑。
- **Track**：A。
- **Prerequisites**：M02。
- **Learning Materials**：MIT 6.004 时序逻辑；HDLBits 触发器。
- **Actions**：手画给定输入下 D 触发器波形；实现同步复位寄存器；比较异步复位；学习非阻塞赋值的时序语义。
- **Estimated Hours**：3–5。
- **Deliverables**：手算波形、RTL、testbench 和仿真记录。
- **Verification**：对照仿真，覆盖复位有效、释放及时钟边沿。
- **Acceptance Criteria**：逐边沿预测与仿真一致；能说明同步和异步复位的触发差异。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S01-M03-T02 计数器

- **Objective**：独立构建带使能的时序电路。
- **Track**：A。
- **Prerequisites**：T01。
- **Learning Materials**：HDLBits 计数器；仿真器官方文档。
- **Actions**：定义位宽、方向、使能、复位和回绕；实现计数器与自检 testbench；测试暂停、回绕与复位并检查波形。
- **Estimated Hours**：4–6。
- **Deliverables**：规格、RTL、测试、工具版本及实际运行记录。
- **Verification**：逐周期比较参考计数值。
- **Acceptance Criteria**：复位、使能、暂停和最大值回绕符合规格；失败信息包含周期、期望和实际值。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S01-M03-T03 移位寄存器与时序基础

- **Objective**：理解逐周期数据传播与基础时序约束。
- **Track**：A。
- **Prerequisites**：T02。
- **Learning Materials**：MIT 6.004 时序逻辑；HDLBits 移位寄存器。
- **Actions**：实现串行输入移位寄存器，定义位序和方向；验证复位及连续输入；用给定的时钟到 Q、组合延迟和 setup 数值计算最小时钟周期，说明 hold 需单独检查。
- **Estimated Hours**：4–6。
- **Deliverables**：RTL、testbench、逐周期预期表及计算过程。
- **Verification**：自检仿真与手算交叉核对。
- **Acceptance Criteria**：位序和逐周期输出正确；说明 setup、hold 和周期约束的区别，且不将练习等同物理时序签核。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

## M04 有限状态机

### S01-M04-T01 FSM 规格与实现

- **Objective**：把文字需求转为状态机。
- **Track**：A。
- **Prerequisites**：M03。
- **Learning Materials**：MIT 6.004 状态机；HDLBits FSM。
- **Actions**：选择序列检测器，明确是否允许重叠；列状态和转移表、绘状态图；实现状态寄存器、次态和输出逻辑；定义默认状态。
- **Estimated Hours**：4–6。
- **Deliverables**：规格、状态图、转移表、RTL 与仿真记录。
- **Verification**：手工追踪至少两组输入并与仿真波形比较。
- **Acceptance Criteria**：状态图、转移表和实现一致，明确复位状态及输出时机，组合赋值完整。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S01-M04-T02 FSM 自检与边界

- **Objective**：针对状态与转移设计验证。
- **Track**：A。
- **Prerequisites**：T01。
- **Learning Materials**：HDLBits FSM 练习；仿真器官方文档。
- **Actions**：建立独立参考序列或模型；测试匹配、不匹配、连续与重叠输入、中途复位；设计非法状态恢复检查并记录方法和限制。
- **Estimated Hours**：4–6。
- **Deliverables**：测试计划、自检 testbench、实际结果和未覆盖项。
- **Verification**：依据状态转移表逐项记录执行及通过状态。
- **Acceptance Criteria**：主要转移与边界有可复现证据，能够说明未被测试证明的内容。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

## M05 4-bit ALU

### S01-M05-T01 ALU 规格与实现

- **Objective**：综合运用组合 RTL 和模块化设计。
- **Track**：A、B。
- **Prerequisites**：M02、M04；固定宽度算术。
- **Learning Materials**：HDLBits 组合逻辑；MIT 6.004 数据通路。
- **Actions**：定义至少加、减、按位与、按位或；说明操作码、截断、零标志及进位/借位约定；绘数据通路；实现 RTL 与初步测试。
- **Estimated Hours**：5–7。
- **Deliverables**：规格、数据通路图、RTL、自检 testbench。
- **Verification**：每个操作检查普通值、全零、全一和相关算术边界。
- **Acceptance Criteria**：实现符合预先写明的位宽与标志约定；所有操作码和默认分支行为明确。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

### S01-M05-T02 ALU 穷举回归与阶段验收

- **Objective**：验证声明的输入范围并检验独立理解。
- **Track**：A、B。
- **Prerequisites**：T01。
- **Learning Materials**：ALU 规格与 testbench；HDLBits 相关习题。
- **Actions**：用独立参考模型遍历所有声明的操作及 4-bit 输入组合；记录命令、工具版本和失败数量；修复问题并重跑；脱离生成代码独立解释实现，完成一道新的组合或时序小题。
- **Estimated Hours**：4–6。
- **Deliverables**：参考模型、回归脚本、实际结果、阶段总结与独立验收记录。
- **Verification**：逐项比较 DUT 和参考模型；临时注入错误确认测试失败，恢复并重跑。
- **Acceptance Criteria**：声明操作和全部输入组合比较无误；测试具有非零失败退出状态或等价明确失败标记；独立说明规格、实现、测试及限制。`VERIFIED` 和 `INDEPENDENTLY_EXPLAINED` 分别记录证据。
- **Status**：查看 [PROGRESS](../PROGRESS.md)；未列出具体进展的任务按 NOT_STARTED 处理。

## 验证与学习记录

每个重要 RTL 项目记录测试目标、测试输入、边界条件、预期和实际结果、测试状态、工具版本、运行命令、失败情况和尚未覆盖的范围。功能编译成功不是正确性证据。记录独立完成、AI 辅助或参考来源；AI 参与不能标作完全自主完成。每周依据实际成果填写 [周报模板](../templates/weekly-log-template.md)，完成里程碑时使用 [里程碑模板](../templates/milestone-template.md)。仿真与基础自检从本阶段开始；断言、覆盖率、形式验证和回归逐步引入，以具体项目需要为准。

记录按实际价值分层：小练习保留解答或代码、自检结果和简短错误说明即可；里程碑保留规格、独立验收、测试与复现方法；性能实验和重要项目再保存完整环境、原始数据、方法和局限。周报可简短填写，实际进度只维护在 PROGRESS，不给每个小练习强制写完整报告。
