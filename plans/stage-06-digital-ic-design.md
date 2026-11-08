# Stage 06：数字 IC 设计流程

**目标**：在功能验证基础上理解从 RTL 到开源教学物理实现的流程，并能解释 PPA、时序约束与结果边界。前置 Stage 01 的 RTL 和仿真、Stage 03 的数据通路，以及 Stage 05 的小模块项目；课程与本机环境允许时可提前学习概念，但本阶段项目按主线进行。预计 **52–84 小时**，实际以环境、PDK 和诊断结果调整；资源官方链接及限制见[学习资源](../resources/learning-resources.md)。

开源教学流程、工业 sign-off、真实流片是不同层次：完成开源布局布线或输出 GDS 不表示满足工业级签核、更不代表完成流片。功耗依赖库、活动率、角点和方法；缺数据时只说明缺口，不虚构数值。所有任务初始 `NOT_STARTED`，计划成果为 `PLANNED`。

## 前置诊断

独立作答并记录证据：①解释组合逻辑、寄存器、时钟和复位的 RTL 推断；②解释仿真、综合和静态时序分析分别检查什么；③给定 10 ns 时钟周期、1 ns 时钟到 Q、6 ns 组合路径、1 ns setup，在忽略其他因素下算 setup 裕量，并说明为何不能由此判断 hold；④执行既有小模块回归并识别一个失败。对每项分别标记：独立正确解释且经参考答案/运行复核为“已掌握”；需提示或不完整为“部分掌握”；无法回答或核心错误为“未掌握”。薄弱项返回 Stage 01/03/05 相关任务并以新题复测。

<details>
<summary>作答后展开数值题参考答案</summary>

第③题理想化 setup 裕量为 10−1−6−1=2 ns，仅在题设忽略其他因素的情况下成立；hold 需单独检查最短路径等条件。

</details>

## 里程碑和初步任务

### M01 验证与综合：S06-M01-T01 可复现 RTL 综合

- **Objective**：从已验证设计生成可检查的逻辑网表。
- **Track**：A。
- **Prerequisites**：前置诊断；Stage 01 或 05 的已有 RTL、testbench。
- **Learning Materials**：Yosys Synthesis starter；Icarus Verilog 或 Verilator 文档。
- **Actions**：选择既有小模块，冻结接口与测试；记录工具版本和输入；运行仿真回归；执行解析、综合、检查；保存网表及报告；区分通用综合与目标工艺映射。
- **Estimated Hours**：10–16。
- **Deliverables**：源代码引用、测试、脚本、日志、综合网表和环境说明。
- **Verification**：复跑功能测试、检查综合错误与警告；根据环境可用性对综合网表进行等价或门级功能检查，记录限制。
- **Acceptance Criteria**：脚本可重现，测试结果有证据，能解释 RTL 中寄存器和主要逻辑如何映射到网表；不能把综合成功当功能正确。
- **Status**：NOT_STARTED。

### M02 时序与映射：S06-M02-T01 标准单元映射与 STA

- **Objective**：理解约束、路径和 STA 报告。
- **Track**：A。
- **Prerequisites**：M01；时钟周期、setup、hold 与工艺库概念。
- **Learning Materials**：OpenROAD 文档；OpenLane 使用指南；Yosys 文档。
- **Actions**：选择可用教学工艺库及其角点，记录来源；对可实现的设计配置时钟、输入输出延迟等适用约束并标注假设；运行技术映射和 STA；识别关键路径、slack 和 setup/hold；调整一个约束或结构后复跑比较。
- **Estimated Hours**：12–20。
- **Deliverables**：约束文件、库及角点说明、映射网表、时序报告、差异解释。
- **Verification**：追踪报告中起点、终点、路径延迟与约束；用单一路径数据检查 slack 计算，并确认实际报告的假设。
- **Acceptance Criteria**：可解释至少一个真实 setup 报告和 hold 检查的状态；声明未约束路径、时钟不确定性等适用限制；无工具/库时记录阻塞，不编造报告。
- **Status**：NOT_STARTED。

### M03 物理实现：S06-M03-T01 教学 RTL-to-GDS 流程

- **Objective**：理解 floorplan 到布线的完整顺序和主要检查。
- **Track**：A。
- **Prerequisites**：M02；可用 OpenLane/OpenROAD 教学环境及合法可用 PDK。
- **Learning Materials**：OpenLane 使用指南；OpenROAD 文档；KLayout 基础手册。
- **Actions**：记录操作系统、工具版本、PDK 和约束；运行小模块 floorplanning、placement、clock tree synthesis、routing；检查版图及流程报告；记录 DRC/LVS 检查是否可用、使用规则和实际结果；归档 GDS 或流程实际生成物。
- **Estimated Hours**：20–32。
- **Deliverables**：环境与运行脚本、日志、布局文件、时序/面积报告、检查结果与失败说明。
- **Verification**：按日志逐阶段确认真实运行结果；用 KLayout 查看生成版图；检查 DRC/LVS 报告而非仅依据版图可打开。
- **Acceptance Criteria**：在可用环境中重现小设计的流程并解释各步骤；明确完成及失败/跳过的检查、PDK 和约束；不将教学结果称为工业 sign-off 或流片。环境不可用时标记 `BLOCKED` 并记录原因。
- **Status**：NOT_STARTED。

### M04 PPA：S06-M04-T01 面积、时序与功耗比较

- **Objective**：有依据地比较一个设计变化的 PPA 取舍。
- **Track**：A、B。
- **Prerequisites**：M02、M03；至少两个功能等价的可复现配置。
- **Learning Materials**：OpenROAD、OpenLane 报告文档；Yosys 文档。
- **Actions**：选择一个可解释的 RTL 或约束变化，控制库、角点、工具与工作负载；验证功能一致；记录面积、关键路径和可用的功耗估计方法；对比局限与变化原因。
- **Estimated Hours**：10–16。
- **Deliverables**：配置差异、两组真实报告、对比表、运行命令及结论。
- **Verification**：对两组设计运行相同功能测试；核对报告来源、单位和比较条件；功耗若有估计则说明活动率、模型和角点。
- **Acceptance Criteria**：面积与时序比较可追溯、可复算；只有具备合适工具、活动率和库时才报告功耗，否则标记未测并解释原因；不声称真实硅片 PPA。
- **Status**：NOT_STARTED。

里程碑的独立验收除各任务要求外：M01 能在新模块定位网表中的寄存器和逻辑；M02 在新报告中解释时钟、关键路径与 slack；M03 讲清 floorplan、placement、CTS、routing、DRC/LVS 的职责及实际覆盖；M04 解释比较条件及结论边界。证据应链接到实际产物；`VERIFIED` 和 `INDEPENDENTLY_EXPLAINED` 分别记录。
