# 七阶段课程映射

课程主线提供知识结构；GPT 辅导理解，实践及独立验收检验能力。优先按官方讲义/视频、教材、习题、实验的可用内容学习；无公开资料时明确记录缺口，用标注为补充的材料替代，不冒充官方作业。每次只选择与当前任务相关的一小段。表中材料入口和公开范围按 2026-11-08 的官方页面核查；页面链接存在不保证视频、课程账户、全部附件可用，访问受限时报告具体限制，不猜测。课程多为历史学期，不声称最新；学校课程和考试要求优先。

## Stage 01 — 数字电路与 Verilog

- **Primary Course**：[MIT 6.004 Computation Structures，Spring 2017](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/)。官方目录涵盖信息表示、数字抽象、CMOS、组合与时序逻辑、FSM；非 Verilog 完整课程。
- **官方讲义、视频和习题**：当前入门从 [1 Basics of Information](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/) 开始，依次使用 [1.1 注释讲义](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/c1s1/)、[1.2 视频](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/c1s2/) 和 [1.3 Worksheet](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c1/c1s3/)。章节 2–6 的对应入口见课程目录；具体作答范围由诊断决定。
- **官方实验**：[MIT 6.004 Spring 2009 Labs](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/pages/labs/) 和 [Tools](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/pages/tools/) 作为补充，属于不同学期旧版；老 Java 工具的现代系统可运行性未核实，不保证线上评分服务仍运行。2017 版与 2009 版不要混写为同一套作业。
- **Supporting Courses**：[MIT 6.002](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) 补电路；[HDLBits](https://hdlbits.01xz.net/wiki/Main_Page) 补 Verilog；[IEEE The Beauty of Circuits](https://sscs.ieee.org/education/sscs-video-series/the-beauty-of-circuits/) 作直觉补充。视频平台可访问性待实际检查。
- **推荐范围**：先独立做 S01-M01-T01 诊断；针对缺口学习课程第 1–6 个主题，结合本校课堂进度。HDL 和 testbench 由补充资料与项目覆盖。
- **GPT 辅导**：解释信息表示、CMOS 和时序术语，引导解官方 worksheet，不直接代答；核对证据和独立解释。
- **工程实践**：门电路、加法器、计数器、移位寄存器、FSM、4-bit ALU 和自检仿真，详见 [Stage 01](plans/stage-01-digital-circuits.md)。
- **课程考核标准**：独立解释所学主题并完成对应官方可得题目；官方评分服务不可用时保留题目、答案、核对依据和未覆盖项；工程验收依阶段计划。未做不视为通过。

## Stage 02 — C++ 矩阵乘法优化

- **Primary Course**：[CMU 15-213 Introduction to Computer Systems，2018 课程表](https://www.cs.cmu.edu/afs/cs/academic/class/15213-m18/www/schedule.html)，选 memory hierarchy、cache 和 code optimization；其基础为系统性能，不是专门 C++ GEMM 课程。
- **讲义 / 视频**：课程表提供 PDF 和视频链接（部分录制于 2015 年），实际播放权限待核实；按主题取用。
- **作业 / 实验**：[CS:APP 自学实验](https://csapp.cs.cmu.edu/2e/labs.html)，Cache Lab 可学习缓存模拟与转置；和课程表不是同一版本，下载、环境及权限应核对。不是官方 GEMM 作业。官方作业入口见课程表；在线提交账户可用性未核实。
- **Supporting Courses**：[MIT 18.06 线性代数](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)；[Roofline 原论文](https://people.eecs.berkeley.edu/~kubitron/courses/cs252/handouts/papers/RooflineVyNoYellow.pdf)。
- **推荐范围 / GPT 辅导**：依据诊断及现有项目查漏补缺；解释访存、缓存和基准设计，不把耗时变化当作缓存事件的直接测量。
- **工程实践**：先审阅并复用 [现有矩阵项目](https://github.com/lingquan11/cpp-matmul-performance) 的实现、测试与实验，按 [Stage 02](plans/stage-02-matrix-optimization.md) 补缺。
- **课程考核标准**：独立解读局部性并完成所选官方可得练习；以项目的正确性、可复现数据和独立解释验收补充 GEMM 能力。

## Stage 03 — 计算机体系结构

- **Primary Course**：[Berkeley CS 152/252A Computer Architecture and Engineering，Spring 2026](https://inst.eecs.berkeley.edu/~cs152/sp26/)，为特定旧学期而非当前课程保证。
- **讲义 / 视频**：官方课程表列 slides 和 recording；部分链接指向 Google Drive 或课程平台，公开权限逐项待核实。
- **作业 / 实验**：课程表列出 homework、讨论题及答案；[Labs](https://inst.eecs.berkeley.edu/~cs152/sp26/lab/) 公开列出实验，平台、运行环境与附件权限待实际确认。
- **Supporting Courses**：[MIT 6.004 2017](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) 中处理器、缓存、流水线主题；[RISC-V RV32I 官方规范](https://docs.riscv.org/reference/isa/v20240411/unpriv/rv32.html)。
- **推荐范围 / GPT 辅导**：从 ISA、数据通路、流水线与缓存中选择与当前里程碑匹配的讲义，逐周期分析冒险；声明教学 CPU 的 ISA 子集。
- **工程实践**：复用 ALU，完成简单 CPU、流水线和 Cache 模拟器；见 [Stage 03](plans/stage-03-computer-architecture.md)。
- **课程考核标准**：独立完成所选官方练习和指令跟踪；CPU 测试、状态、局限和可复现命令是工程验收的额外证据。

## Stage 04 — AI 算法与计算特征

- **Primary Course**：[MIT 6.S191 Introduction to Deep Learning](https://ocw.mit.edu/courses/6-s191-introduction-to-deep-learning-january-iap-2020/)，官方 OCW 指向课程在线发布网站，页面会更新；进入时记录所用具体学期。
- **讲义 / 视频**：OCW 将其列为视频课程并链接 [课程在线发布页](https://introtodeeplearning.com/)；2026 页面列有 slides 和视频链接，具体视频播放权限待实际核实。
- **作业 / 实验**：2026 在线页列有软件实验及代码链接；具体代码能否在本机运行和在线评分的权限未逐项核实，不能假定可提交。
- **Supporting Courses**：[MIT 6.5940](https://hanlab.mit.edu/course) 用于量化与高效计算；[Stanford CS231n 卷积笔记](https://cs231n.github.io/convolutional-networks/)、[NumPy matmul 文档](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) 用于计算核对。
- **推荐范围 / GPT 辅导**：先补线代和网络计算基础，再按所用课程版本寻找卷积、Attention 和 Transformer；量化、FLOPs/字节和 Roofline 用支持材料补足，不能假称都由主课程覆盖。
- **工程实践**：手算并用 NumPy 对照 GEMM、卷积与注意力，分析精度和访存；见 [Stage 04](plans/stage-04-ai-algorithms.md)。
- **课程考核标准**：完成所选官方可得练习并解释张量形状；对额外计算量、误差和数据量推导单独验收。

## Stage 05 — NPU 微架构

- **Primary Course**：[MIT 6.5930/1 Hardware Architecture for Deep Learning，Spring 2026](https://csg.csail.mit.edu/6.5930/info.html)。
- **讲义**：[课程大纲](https://csg.csail.mit.edu/6.5930/syllabus.html) 列阅读和部分讲义链接，逐项公开程度待核实；课程页面指出可能调整。
- **视频**：该学期大纲明确表示课堂不录制，不能假定有该版授课视频。
- **作业 / 实验**：课程信息列出实验及设计项目，但页面描述的实验数量存在不一致；具体题目、代码及 Canvas 权限待进入时核实。
- **Supporting Courses**：[MIT Eyeriss 原始教程](https://eyeriss.mit.edu/2019_neurips_tutorial.pdf)、[Roofline](https://people.eecs.berkeley.edu/~kubitron/courses/cs252/handouts/papers/RooflineVyNoYellow.pdf)。
- **推荐范围 / GPT 辅导**：按课程内容学习映射、数据流、复用、存储与系统模型；先检查体系结构与 AI 前置知识，指出课程可用材料的缺口。
- **工程实践**：MAC、PE、阵列、buffer、搬运和性能模型，见 [Stage 05](plans/stage-05-npu-microarchitecture.md)。
- **课程考核标准**：独立解释工作负载到架构的映射并完成可得官方练习；RTL、存储和性能结论另以可复现证据验收。

## Stage 06 — 数字 IC 设计流程

- **Primary Course**：[MIT 6.374 Analysis and Design of Digital Integrated Circuits，Fall 2003](https://ocw.mit.edu/courses/6-374-analysis-and-design-of-digital-integrated-circuits-fall-2003/)。这门研究生课程侧重 CMOS 数字电路，不完整覆盖现代 RTL-to-GDS 流程，须用官方工具资料补足。
- **讲义 / 作业 / 实验**：官方 [Lecture Notes](https://ocw.mit.edu/courses/6-374-analysis-and-design-of-digital-integrated-circuits-fall-2003/pages/lecture-notes/)、[Assignments](https://ocw.mit.edu/courses/6-374-analysis-and-design-of-digital-integrated-circuits-fall-2003/pages/assignments/) 和 [Projects](https://ocw.mit.edu/courses/6-374-analysis-and-design-of-digital-integrated-circuits-fall-2003/pages/projects/) 页面可访问；旧版商业工具或项目材料的可运行性和完整访问待核实。
- **视频**：课程页面未列公开授课视频，是否有其他官方版本待核实，不编造。
- **Supporting Courses / 文档**：[Yosys](https://yosyshq.readthedocs.io/projects/yosys/en/latest/getting_started/example_synth.html)、[OpenSTA](https://github.com/The-OpenROAD-Project/OpenSTA)、[OpenLane](https://openlane2.readthedocs.io/en/latest/usage/index.html)、[KLayout](https://www.klayout.de/doc/manual/basic.html) 补充综合、时序和物理流程。
- **推荐范围 / GPT 辅导**：依据课程和前置选 CMOS、时序、功耗；解释工艺、约束、报告假设和教学流程局限。
- **工程实践**：以已有已验证 RTL 完成综合、时序和可用的开源物理流程；见 [Stage 06](plans/stage-06-digital-ic-design.md)。
- **课程考核标准**：所选官方练习独立通过；工程证据包含环境、PDK、脚本、约束及报告。教学实现不等于工业 sign-off 或真实流片。

## Stage 07 — 完整 AI 加速器项目

- **Primary Course**：[MIT 6.5930/1 Hardware Architecture for Deep Learning](https://csg.csail.mit.edu/6.5930/info.html)，延续 Stage 05 的系统分析和课程设计项目，不要求重复学习已验收内容。
- **讲义 / 视频 / 作业 / 实验**：参照 Stage 05 的同一课程入口和访问限制；官方页面描述开放式项目，但项目具体说明及线上服务的可用性待核实；Spring 2026 不录制课堂。
- **Supporting Courses / 文档**：Stage 01 的 MIT 6.004、Stage 06 的开源流程，以及 [Berkeley Gemmini 项目](https://github.com/ucb-bar/gemmini) 系统架构参考；不得把外部项目实现当作个人成果。
- **推荐范围 / GPT 辅导**：从已有能力和真实成果出发确定项目规格；逐层追问数值、接口、验证、存储和可复现性；不要重复安排课程中已通过的部分。
- **工程实践**：MVP、Intermediate、Advanced，见 [Stage 07](plans/stage-07-ai-accelerator.md)；明确个人、AI 和参考贡献。
- **课程考核标准**：所选可得官方项目要求仅作课程参考，仓库实际分层验收须有独立项目证据；没有官方评分不声称取得课程成绩。流片非必要。

## 材料缺失与变更

当官方视频、讲义、作业、实验任一不可访问，记录访问日期、失败项、原因（已知时）及替代官方/可靠材料；不要将自拟题标为官方。短期更换材料时保留同一阶段与学习目标；重大路线或主课程改变应说明影响并由学习者确认。当前进度只在 [PROGRESS.md](PROGRESS.md) 维护。
