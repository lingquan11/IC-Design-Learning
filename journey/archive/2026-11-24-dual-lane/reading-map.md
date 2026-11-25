# 导读表

导师在进入任务、或讲到新概念之前，从这里挑**最多 2 篇**给我：理论线由 GPT 给，实践线由 Muse 给（规则见 `start/prompts/theory-tutor.md`、`practice-tutor.md`）。路线由战役和任务卡决定，导读只服务于当前任务。
读过的条目在各自日志的"做了什么"里写编号（如 `读 R-I1-05`），导师不再重复推荐。

**时机**：做前 = 动手前读，建立概念；卡住 = 遇到对应问题时读；做后 = 自己做完再读，用来对照。
**常用来源**：ETH DDCA Spring 2026（[课程表与讲义](https://safari.ethz.ch/ddca/spring2026/doku.php?id=schedule)，[视频](https://www.youtube.com/playlist?list=PL5Q2soXY2Zi9Eo29LMgKVcaydS7V1zZW3)，下表写"ETH Lx"）· Harris & Harris, *Digital Design and Computer Architecture: RISC-V Edition*（下表写"H&H"）· [HDLBits](https://hdlbits.01xz.net/wiki/Problem_sets) · 工具官方文档 · 论文与协议规范

## I1 数字逻辑与 Verilog（逐任务）
| 编号 | 任务 | 线 | 时机 | 来源与章节 | 读完要回答 | 时长 |
|---|---|---|---|---|---|---|
| R-I1-01 | T01 | 理论 | 卡住（数制题 < 2 分时） | ETH L1；H&H 1.4 数制 | n 位补码能表示的范围是多少？为什么补码加法不用区分正负？ | 40m |
| R-I1-02 | T02 | 理论 | 做前 | ETH L2、L3；H&H 第 2 章 | 卡诺图化简和布尔代数化简分别适合什么情况？什么是竞争冒险？ | 90m |
| R-I1-03 | T02 | 理论 | 做前 | ETH L5；H&H 第 4 章 | 结构化描述和行为描述有什么区别？一段 `assign` 综合后是什么电路？ | 90m |
| R-I1-04 | T02 / P03 | 理论 / 实践 | 卡住 | Cummings, *Nonblocking Assignments in Verilog Synthesis, Coding Styles That Kill!*（[SNUG 2000](http://www.sunburst-design.com/papers/CummingsSNUG2000SJ_NBA.pdf)）前 4 节 | 组合逻辑和时序逻辑分别该用哪种赋值？混用会出现什么仿真与综合不一致？ | 45m |
| R-I1-05 | T03 | 理论 | 做前 | ETH L4；H&H 3.2–3.4（锁存器与触发器、同步时序设计、有限状态机） | 锁存器和触发器的本质区别？Moore 与 Mealy 输出时序有何不同？ | 90m |
| R-I1-06 | T03 | 理论 | 做前 | ETH L6；H&H 3.5（时序逻辑的时序） | 建立时间和保持时间分别约束什么？怎样由关键路径算出最高时钟频率？ | 60m |
| R-I1-07 | T04 | 理论 | 做前 | H&H 5.2.6（乘法）；自己写的 `results/basics/mac-int8/README.md` | 两个 8 位有符号数相乘最多需要几位？累加 N 次后需要几位？你为什么选了现在的溢出策略？ | 40m |
| R-I1-08 | P01 | 实践 | 做前 | [Icarus Verilog 文档](https://steveicarus.github.io/iverilog/)（Getting Started）；[Verilator 文档](https://verilator.org/guide/latest/)（`--lint-only` 与警告说明） | `iverilog` 和 `vvp` 各做什么？Verilator 的 `WIDTH`、`UNUSED` 警告分别在提醒什么？ | 40m |
| R-I1-09 | P01 | 实践 | 做前 | ETH L6b（验证与测试） | 自检 testbench 由哪几部分组成？期望值为什么必须来自独立来源？ | 45m |
| R-I1-10 | P02 | 实践 | 做前 | ETH [实验 3 手册](https://safari.ethz.ch/ddca/spring2026/lib/exe/fetch.php?media=ddca_ss26_lab3_manual.pdf)；H&H 5.2.1（加法器） | 行波进位加法器的关键路径怎么走？参数化模块时 `parameter` 和 `generate` 各起什么作用？ | 45m |
| R-I1-11 | P04 | 实践 | 做前 | Jacob et al., *Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference*（[arXiv:1712.05877](https://arxiv.org/abs/1712.05877)）第 2 节 | INT8 推理里乘积为什么累加到 INT32？零点和缩放因子在 MAC 之外还是之内处理？ | 60m |
| R-I1-12 | P05 | 实践 | 做前 | [Yosys 综合示例](https://yosyshq.readthedocs.io/projects/yosys/en/latest/getting_started/example_synth.html) | `synth` 之后 `stat` 报告的单元数代表什么？为什么它不能直接说明时序？ | 30m |

## I2 片上总线与跨时钟域（任务卡展开时细化）
| 编号 | 线 | 时机 | 来源与章节 | 读完要回答 |
|---|---|---|---|---|
| R-I2-01 | 理论 | 做前 | Cummings, *Clock Domain Crossing (CDC) Design & Verification Techniques Using SystemVerilog*（[SNUG 2008](http://www.sunburst-design.com/papers/CummingsSNUG2008Boston_CDC.pdf)） | 亚稳态为什么不能消除只能降低概率？两级同步器适用于什么信号？ |
| R-I2-02 | 理论 / 实践 | 做前 | Cummings, *Simulation and Synthesis Techniques for Asynchronous FIFO Design*（[SNUG 2002](http://www.sunburst-design.com/papers/CummingsSNUG2002SJ_FIFO1.pdf)） | 指针为什么要用格雷码跨时钟域？满标志为什么要多一位？ |
| R-I2-03 | 理论 | 做前 | ARM AMBA APB 规范（IHI 0024）、AXI 规范（IHI 0022）中 AXI4-Lite 部分，在 developer.arm.com 下载 | APB 的 setup / access 两个阶段各做什么？AXI 的 valid / ready 握手有哪些不允许的行为？ |
| R-I2-04 | 实践 | 做前 | ZipCPU [AXI-Lite 形式化验证](https://zipcpu.com/formal/2018/12/28/axilite.html)；SymbiYosys 官方文档 | 怎样把协议规则写成断言？`assume` 和 `assert` 在形式化中分别约束谁？ |

## I3 NPU 设计（任务卡展开时细化）
| 编号 | 线 | 时机 | 来源与章节 | 读完要回答 |
|---|---|---|---|---|
| R-I3-01 | 理论 | 做前 | H. T. Kung, *Why Systolic Architectures?*（[DOI](https://doi.org/10.1109/MC.1982.1653825)）；ETH L18b | 脉动阵列靠什么减少访存？它适合什么样的计算？ |
| R-I3-02 | 理论 | 做前 | [Eyeriss 教程](https://eyeriss.mit.edu/2019_neurips_tutorial.pdf)（数据流部分）；[MIT 6.5930/1](https://csg.csail.mit.edu/6.5930/info.html) | 权重驻留、输出驻留、行驻留分别复用了哪类数据？ |
| R-I3-03 | 理论 | 做后 | TPU 论文（[arXiv:1704.04760](https://arxiv.org/abs/1704.04760)） | 你的 PE 阵列和 TPU 的矩阵单元在规模、数据流、存储上差在哪里？ |

## I4 验证（任务卡展开时细化）
| 编号 | 线 | 时机 | 来源与章节 | 读完要回答 |
|---|---|---|---|---|
| R-I4-01 | 理论 | 做前 | Chris Spear, *SystemVerilog for Verification*（类、随机约束、覆盖率章节） | 受约束随机测试比定向测试好在哪里？覆盖率 100% 说明了什么、没说明什么？ |
| R-I4-02 | 理论 / 实践 | 做前 | [Verification Academy UVM Cookbook](https://verificationacademy.com/cookbook/uvm-universal-verification-methodology)；[Antmicro Verilator + UVM 示例](https://github.com/antmicro/verilator-uvm-example)；[pyuvm](https://github.com/pyuvm/pyuvm) | agent、driver、monitor、scoreboard 各负责什么？sequence 和 test 怎样分工？ |

## I5 实现与演示（任务卡展开时细化）
| 编号 | 线 | 时机 | 来源与章节 | 读完要回答 |
|---|---|---|---|---|
| R-I5-01 | 理论 | 做前 | [Berkeley EECS 151/251A Fall 2025](https://inst.eecs.berkeley.edu/~eecs151/fa25/) 的 ASIC 讲义（综合、STA、布局布线） | 布线后时序为什么常比综合后差？插入流水级怎样修复 setup 违例？ |
| R-I5-02 | 实践 | 做前 | OpenROAD、LibreLane、SkyWater SKY130 官方文档；[Tiny Tapeout](https://tinytapeout.com/) | 从 RTL 到 GDS 每一步的输入和输出文件是什么？ |
