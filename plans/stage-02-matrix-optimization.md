# Stage 02：C++ 矩阵乘法优化

目标：从软件计算出发理解计算效率、内存访问和数据复用，为 NPU 架构打基础。主线位于 Stage 01 之后；先修为 C++ 基础、矩阵乘法和基本复杂度。任务预计合计 26–44 小时，诊断另约 30–45 分钟；既有成果经核验可减少重复时间。课业优先，时间超预估时拆分任务，不降低验收标准。Track B 为主。学习资源名称见[资源目录](../resources/learning-resources.md)。

既有项目 [cpp-matmul-performance](https://github.com/lingquan11/cpp-matmul-performance) 应优先盘点、复用和补缺，不复制另建已有代码。本计划未宣称其成果已由学习者独立完成或已在本次运行中验证。任务状态使用 NOT_STARTED / IN_PROGRESS / BLOCKED / COMPLETED；成果状态单独使用 PLANNED / IMPLEMENTED / VERIFIED / INDEPENDENTLY_EXPLAINED，并须各有证据。以下任务初始均为 NOT_STARTED，成果初始为 PLANNED。

## 阶段前诊断

建议用 30–45 分钟独立完成以下题目，先不看答案、不用 AI，记录答案、耗时和运行证据；之后再展开核对。时间不是硬门槛，避免为赶时间牺牲正确性。

1. **矩阵与维度：** 给定 A = `[[1, 2, 3], [4, 0, -1]]`，B = `[[2, 1], [0, -1], [3, 2]]`，手算 AB 的每个元素及输出维度，说明为什么可以相乘。
2. **算法与复杂度：** 写出计算 `C[M][N] = A[M][K] × B[K][N]` 的三重循环伪代码，给出时间复杂度及输出矩阵所占空间复杂度。
3. **局部性与测量：** 假设 C++ 二维矩阵按行连续存储，比较 `i-j-k` 循环中 B 的访问与 `i-k-j` 中 B 的访问；列出两个可能干扰计时的因素。只解释访问顺序，不必猜测特定机器的具体性能。
4. **独立编程：** 用熟悉的 C++ 写出兼容非方阵的乘法函数，以第 1 题数据为输入；编译运行并记录命令、实际输出；说明如何处理不兼容维度。

<details>
<summary>完成作答后展开核对答案与分项判定</summary>

1. A 是 2×3，B 是 3×2；内侧维度相同，所以结果为 2×2：`[[11, 5], [5, 2]]`。四个元素和维度、约束均正确为已掌握；方法基本正确但有算术或维度遗漏为部分掌握；无法建立乘法过程为未掌握。
2. 外层遍历 `i`、中层遍历 `j`，对每个输出将 `sum` 初始化为 0，再对 `k` 累加 `A[i][k] * B[k][j]` 后写入 `C[i][j]`。时间复杂度为 O(MNK)，输出空间为 O(MN)，不含输出的额外空间可为 O(1)。循环、初始化、边界及复杂度均正确为已掌握；大体正确但有遗漏为部分掌握；不能写出有效过程为未掌握。
3. `i-j-k` 在内层变化 k，访问 B 的同一列、跨行跳跃；`i-k-j` 在内层变化 j，访问 B 的同一行、地址连续。计时可能受预热、编译优化、后台进程、计时粒度或数据初始化影响。正确说明两种访问和至少两个因素为已掌握；仅解释一部分为部分掌握；无法解释为未掌握。连续访问并不保证任意平台都更快。
4. 实际输出与第 1 题一致，且索引适用于非方阵、明确拒绝或处理不兼容维度，才可判已掌握；程序可运行但存在可定位的边界或设计遗漏为部分掌握；不能独立完成或运行错误为未掌握。

</details>

逐项记录“已掌握 / 部分掌握 / 未掌握”和依据。诊断中已掌握的内容可快速通过相应学习内容，但保留必要的项目验收；薄弱项先补齐。看过课程、自评熟悉或他人代写不能作为已掌握的证据。

## M01：盘点、正确实现与测试

里程碑验收：已有项目的功能、来源与证据完成映射；选定实现对兼容非方阵及边界输入通过可复现正确性测试，错误输入按文档处理。

### S02-M01-T01：盘点现有矩阵乘法项目

- Objective：识别可复用成果、证据和真实缺口。
- Track：B。Prerequisites：Git 仓库浏览、C++ 基础。
- Learning Materials：已有 cpp-matmul-performance 项目及 Pro Git 官方在线书。
- Actions：检查 README、src、tests、benchmarks、experiments 和 notes；记录各实现的代码来源、测试覆盖、运行方法、数据及当前状态；与后续任务逐一映射，仅为缺口安排补充。
- Estimated Hours：2–4。
- Deliverables：带文件链接和证据的盘点表、缺口与后续任务映射。
- Verification：检查来源与报告原文；有条件时按记录复现，未运行的明确写未复现。
- Acceptance Criteria：每项成果和贡献都能追溯到具体证据；不重复创建已有实现；未核验内容不标 VERIFIED，也不凭 AI 生成内容标自主完成。
- Status：NOT_STARTED。

### S02-M01-T02：建立或复核基准矩阵乘法

- Objective：获得可读、正确、接口明确的基准实现。
- Track：B。Prerequisites：T01、C++ 容器、矩阵乘法及维度约束。
- Learning Materials：已有项目、MIT 18.06 Linear Algebra。
- Actions：优先复核现有实现；确定数据布局与接口；仅在缺失时补充 M×K 与 K×N 的基准乘法；明确维度不兼容如何处理。
- Estimated Hours：3–5。
- Deliverables：已有代码链接或必要补充、构建和运行说明。
- Verification：手算小矩阵及一个非方阵，与程序结果比较。
- Acceptance Criteria：结果正确；独立解释索引、维度约束和 O(MNK) 计算量。
- Status：NOT_STARTED。

### S02-M01-T03：复核并补齐正确性测试

- Objective：为优化提供可靠正确性基线。
- Track：B。Prerequisites：T02、浮点运算基础。
- Learning Materials：已有项目测试与所用测试工具文档。
- Actions：盘点现有测试，补齐零矩阵、单位矩阵、非方阵、不可乘维度及固定种子输入；与独立可信参考比较，说明浮点绝对及相对容差。
- Estimated Hours：3–5。
- Deliverables：测试代码或现有测试链接、命令和运行结果。
- Verification：执行全部测试；可在临时副本中人为引入索引错误，确认测试能够发现。
- Acceptance Criteria：列出的有效输入通过；非法维度按设计处理；记录容差与环境，测试失败时不标已验证。
- Status：NOT_STARTED。

## M02：可信基准与访存分析

里程碑验收：同一环境、编译配置和输入下测量可重复，报告正确性、耗时与方法限制。

### S02-M02-T01：构建或复核性能基准

- Objective：建立可复现测量方法。
- Track：B。Prerequisites：M01、计时与编译基础。
- Learning Materials：已有 benchmarks 和实验记录、CMU CS:APP Labs。
- Actions：检查并优先复用已有基准；记录 CPU、操作系统、编译器与参数、输入和随机种子；预热、重复测量，排除初始化与输出开销，保存原始数据、统计中位数和波动，防止结果被优化掉。
- Estimated Hours：4–6。
- Deliverables：基准代码链接或补充、命令、环境及原始结果。
- Verification：重复执行两轮并核查单位、输入、正确性和波动。
- Acceptance Criteria：按说明可复现；保留多次原始测量，能解释噪声；若用 2MNK 计算 GFLOP/s，明确这一运算计数约定。
- Status：NOT_STARTED。

### S02-M02-T02：分析循环顺序与数据局部性

- Objective：联系访存模式与性能。
- Track：B。Prerequisites：T01、数组布局、Cache 基础。
- Learning Materials：CMU CS:APP Labs、已有 experiments。
- Actions：绘制循环访问顺序；检查已有等价循环变体，缺失时补充；先测正确性，再比较小、中、大及非方阵输入。
- Estimated Hours：3–5。
- Deliverables：代码或链接、访问示意、原始结果与分析。
- Verification：变体通过同一测试集，使用 T01 的基准流程。
- Acceptance Criteria：基于连续访问、复用与尺寸解释观察，同时区分推测与测得结果；没有硬件计数器证据时不断言 Cache miss 的具体变化。
- Status：NOT_STARTED。

## M03：分块、SIMD 与实验报告

里程碑验收：同一测试框架下比较已有或补充的策略；真实结果支持结论，未观察到加速也可以完成。

### S02-M03-T01：复核分块矩阵乘法

- Objective：理解分块与数据复用。
- Track：B。Prerequisites：M02、循环边界。
- Learning Materials：已有项目分块实现、CMU CS:APP Labs。
- Actions：审查已有分块实现与实验，仅补未覆盖缺口；处理尺寸不能整除块大小；选至少三个块大小测试，解释容量限制。
- Estimated Hours：4–7。
- Deliverables：已有实现链接或补充、边界测试与实验数据。
- Verification：对比基准，包含多个非整除尺寸。
- Acceptance Criteria：所有测试满足声明容差；解释块大小与平台的影响；不要求一定比基准快。
- Status：NOT_STARTED。

### S02-M03-T02：调查 SIMD 与计算瓶颈

- Objective：认识编译器向量化、吞吐和带宽限制。
- Track：B。Prerequisites：M02、T01 与编译器基础。
- Learning Materials：已有项目 SIMD 相关代码、Roofline 原论文、所用编译器官方向量化文档。
- Actions：检查现有 SIMD 实现和测试的最新状态；查看向量化报告；选择一种可用策略实验；估算运算量与数据访问量，声明存储层级和复用假设。
- Estimated Hours：4–7。
- Deliverables：实现链接、编译器报告、命令、实验数据与估算过程。
- Verification：先运行正确性测试，再重复基准；独立复算一个例子。
- Acceptance Criteria：有证据说明 SIMD 是否生效；解释估算假设与局限，不把估计带宽当作硬件实测值。
- Status：NOT_STARTED。

### S02-M03-T03：撰写可复现实验报告

- Objective：形成可审阅的工程记录。
- Track：B。Prerequisites：T01–T02。
- Learning Materials：已有项目 notes、Roofline 原论文及本仓库项目模板。
- Actions：汇总问题、方法、环境、输入、正确性、原始数据、统计和限制；说明个人贡献、参考来源及 AI 辅助情况；区分历史记录与本次运行。
- Estimated Hours：3–5。
- Deliverables：报告、原始数据引用、复现入口。
- Verification：从干净构建按说明复现至少一组结果。
- Acceptance Criteria：数据和贡献可追溯，结论不超出证据；能独立解释优化为何可能有效及何时可能失效。
- Status：NOT_STARTED。

## 阶段验收与下一步

完成各里程碑并能独立实现或解释基准乘法、复杂度、缓存和数据局部性；能设计可信测试并用真实数据分析计算与访存关系。实际证据记录至 [PROGRESS.md](../PROGRESS.md) 和项目本身，再根据缺口进入 Stage 03；不将已有历史记录直接视为本次独立验收通过。
