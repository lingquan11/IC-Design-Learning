# 战役 I1：数字逻辑与 Verilog

- **周期**：2027-01-18 → 2027-02-21（寒假，按校历调整；截止日确定后不延期）
- **预算**：每周约 7h，合计约 34.5h（阅读 13h + 编程 18h + 动手 3.5h）；支线另计
- **唯一交付物**：`results/basics/`：自己写的组合 / 时序模块和 INT8 MAC 单元，每个都有自检 testbench，一条命令跑完全部回归
- **主线**：读 Harris & Harris → 编程 P01–P04（mux2 → 组合模块 → 时序模块与 FSM → INT8 MAC）→ 动手 H01–H03（三张表，计入进度）
- **支线**（选做，不计入进度）：[HDLBits](https://hdlbits.01xz.net/wiki/Problem_sets)，在线 Verilog 题库，浏览器里写、即时判题，按主线读到的章节做
- **主教材**：Harris & Harris, [*Digital Design and Computer Architecture: RISC-V Edition*](https://shop.elsevier.com/books/digital-design-and-computer-architecture-risc-v-edition/harris/978-0-12-820064-3)；阅读表全部出自它（作者课件只作辅助）
- **统一约定**：每个模块都有**自检 testbench**（期望值来自独立来源：手算表或 Python 参考模型，不一致时打印 FAIL 并以非零码退出）；每个 testbench 做一次**错误注入**；教材示例用 SystemVerilog（`logic`、`always_ff`、`always_comb`），HDLBits 和本仓库用 Verilog-2005（`wire` / `reg`、`always @(posedge clk)`、`always @(*)`），读到时自己对应
- **推荐顺序**：R01 → R02 → R03 →（支线 S01）→ H01 → H02 → P01 → R04 → P02 → R05 → R06 →（支线 S02）→ P03 → P04 → H03

## 阅读（我自己读，不和 AI 对话；读完对 Muse 说"读完 <ID>"；状态：未读 / 在读 / 读完）
| ID | 长文 | 读哪些部分 | 预计用时 | 读完应该能回答（自测，不考核） | 状态 |
|---|---|---|---:|---|---|
| I1-R01 | Harris & Harris, [*Digital Design and Computer Architecture: RISC-V Edition*](https://shop.elsevier.com/books/digital-design-and-computer-architecture-risc-v-edition/harris/978-0-12-820064-3)；作者课件 [第 1 章](https://pages.hmc.edu/harris/class/e85/old/fall24/DDCArv_Ch1.pdf) | 第 1 章 From Zero to One：数制、补码、逻辑门、CMOS 晶体管 | 2.5h | n 位补码的表示范围？CMOS 反相器怎样工作？什么是噪声容限？ | 未读 |
| I1-R02 | [Harris & Harris](https://shop.elsevier.com/books/digital-design-and-computer-architecture-risc-v-edition/harris/978-0-12-820064-3)（同上）；作者课件 [第 2 章](https://pages.hmc.edu/harris/class/e85/old/fall24/DDCArv_Ch2.pdf) | 第 2 章 Combinational Logic Design | 3h | 卡诺图怎样化简？多路选择器和译码器怎样搭？什么是竞争冒险和关键路径？ | 未读 |
| I1-R03 | [Harris & Harris](https://shop.elsevier.com/books/digital-design-and-computer-architecture-risc-v-edition/harris/978-0-12-820064-3)（同上）；作者课件 [第 4 章](https://pages.hmc.edu/harris/class/e85/old/fall24/DDCArv_Ch4.pdf) | 第 4 章前半：Introduction、Combinational Logic、Structural Modeling、Data Types、Parameterized Modules、Testbenches 几节（跳过 VHDL；时序相关几节留给 R06） | 1.5h | 行为描述和结构化描述的区别？`assign` 和模块实例化分别对应什么硬件？testbench 的期望值为什么要来自独立来源？ | 未读 |
| I1-R04 | [Harris & Harris](https://shop.elsevier.com/books/digital-design-and-computer-architecture-risc-v-edition/harris/978-0-12-820064-3)（同上）；作者课件 [第 5 章](https://pages.hmc.edu/harris/class/e85/old/fall24/DDCArv_Ch5.pdf) | 第 5 章 Arithmetic Circuits 一节：加法器、减法器、比较器、ALU、移位器、乘法器 | 1.5h | 行波进位和超前进位的延迟差别？两个 8 位有符号数相乘需要几位？ | 未读 |
| I1-R05 | [Harris & Harris](https://shop.elsevier.com/books/digital-design-and-computer-architecture-risc-v-edition/harris/978-0-12-820064-3)（同上）；作者课件 [第 3 章](https://pages.hmc.edu/harris/class/e85/old/fall24/DDCArv_Ch3.pdf) | 第 3 章 Sequential Logic Design | 3h | 锁存器和触发器有何不同？Moore 与 Mealy 的输出时序？建立 / 保持时间怎样决定最高频率？ | 未读 |
| I1-R06 | [Harris & Harris](https://shop.elsevier.com/books/digital-design-and-computer-architecture-risc-v-edition/harris/978-0-12-820064-3)（同上）；作者课件 [第 4 章](https://pages.hmc.edu/harris/class/e85/old/fall24/DDCArv_Ch4.pdf)、[第 5 章](https://pages.hmc.edu/harris/class/e85/old/fall24/DDCArv_Ch5.pdf) | 第 4 章后半：Sequential Logic、More Combinational Logic、Finite State Machines 几节；第 5 章 Sequential Building Blocks 一节（计数器、移位寄存器） | 1.5h | `always @(*)` 综合后是什么？怎样避免意外的锁存器？FSM 为什么拆成状态寄存器、次态逻辑、输出逻辑三段？时序逻辑为什么用非阻塞赋值、组合逻辑为什么用阻塞赋值？ | 未读 |

章节按标题找，不按小节编号：不同版本（RISC-V / ARM / MIPS）第 1–5 章内容相同，但小节编号可能不同。

## 编程（GPT 带写，只看机器验收；状态：未开始 / 进行中 / 通过）
| ID | 任务 | 计划用时 | 验收要点（展开任务卡时不得弱于此） | 先读 | 依赖动手 | 状态 |
|---|---|---:|---|---|---|---|
| I1-P01 | 第一个自检模块：`mux2` | 2h | 见 [p01-first-module.md](p01-first-module.md) | I1-R03 | I1-H01、H02 | 未开始 |
| I1-P02 | 组合模块：4 位加法器与参数化多路选择器 | 4h | 加法器穷举 512 种输入；N 选 1 多路选择器测两组参数、每组 ≥ 1000 组随机输入；各一次错误注入；`verilator --lint-only -Wall` 无未说明的警告 | I1-R03、R04 | I1-H01 | 未开始 |
| I1-P03 | 时序模块：计数器、移位寄存器与 FSM | 4h | 带使能和同步复位的计数器、移位寄存器、一个 FSM，自检覆盖复位和全部状态转移；错误注入 | I1-R05、R06 | I1-H01 | 未开始 |
| I1-P04 | INT8 MAC 单元（I3 PE 的前身） | 8h | 先写 ≤ 1 页 spec（接口、位宽、溢出或饱和策略、时序）；有符号 INT8 乘、INT32 累加（神经网络 INT8 推理的标准做法：乘积累加到 32 位，避免溢出），带清零和使能；Python 参考模型 ≥ 1000 组随机输入加边界值（含 −128 × −128、累加溢出），0 失败；错误注入 | I1-R04 | I1-H01 | 未开始 |

## 动手（Muse 负责，只看机器验收；状态：未开始 / 进行中 / 完成）
| ID | 任务 | 计划用时 | 验收要点 | 先读 | 状态 |
|---|---|---:|---|---|---|
| I1-H01 | 环境：OSS CAD Suite + cocotb | 1h | 见 [h01-hdl-toolchain.md](h01-hdl-toolchain.md) | — | 未开始 |
| I1-H02 | 回归脚本与 CI | 1h | 见 [h02-regression-ci.md](h02-regression-ci.md) | — | 未开始 |
| I1-H03 | 综合与收尾 | 1.5h | Yosys 综合 MAC 单元并记录单元数；GTKWave 截图；`results/basics/README.md` ≤ 30 行（模块清单、测试数、边界）；打 tag `i1-v1.0`；ROADMAP 中 I1 改为完成 | — | 未开始 |

## 支线（现成实践课程，选做，不计入进度；做完对 Muse 说"做完 <ID>"；状态：未开始 / 完成）
| ID | 实践课程 | 做哪些 | 配合主线（读完 / 做完之后） | 预计用时 | 状态 |
|---|---|---|---|---:|---|
| I1-S01 | [HDLBits](https://hdlbits.01xz.net/wiki/Problem_sets) | Getting Started；Verilog Language 的 Basics、Vectors、Modules: Hierarchy、More Verilog Features；Circuits → Combinational Logic 的 Basic Gates、Multiplexers、Karnaugh Map to Circuit、Arithmetic Circuits（最后一节等读完 R04） | I1-R03 | 2.5h | 未开始 |
| I1-S02 | HDLBits（同上） | Verilog Language 的 Procedures；Circuits → Sequential Logic 的 Latches and Flip-Flops、Counters、Shift Registers、Finite State Machines | I1-R06 | 3h | 未开始 |
| I1-S03 | HDLBits（同上） | Verification 的 Reading Simulations、Writing Testbenches | I1-P01 | 2h | 未开始 |

某题超过 30 分钟就回看 Harris & Harris 对应的例子，不看题解；想留档就把截图和错题存到 `journey/exercises/hdlbits/`。

## 加分（必做全部完成后才碰）
| ID | 任务 | 计划用时 |
|---|---|---:|
| I1-B01 | 用 cocotb 重写 MAC 单元的 testbench，与 Verilog 版对比 | 3h |

## 砍线顺序
1. I1-B01
2. （仍然超时）I1-P02 只做加法器，参数化多路选择器移到加分

## 收尾定义
截止日：三栏必做全部完成 → 打 `i1-v1.0` → Muse 更新 ROADMAP 和时间线 → 回到 ai-infra-plan。没完成的必做项在 `results/basics/README.md` 的"边界"中写明，同样收尾。
