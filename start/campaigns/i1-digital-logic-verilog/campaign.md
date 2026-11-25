# 战役 I1：数字逻辑与 Verilog

- **周期**：2027-01-18 → 2027-02-21（寒假，按校历调整；截止日确定后不延期）
- **预算**：每周约 8.5h，合计约 41.5h（阅读 14.5h + 编程 23.5h + 动手 3.5h）
- **唯一交付物**：`results/basics/`：自己写的组合 / 时序模块和 INT8 MAC 单元，每个都有自检 testbench，一条命令跑完全部回归
- **统一约定**：每个模块都有**自检 testbench**（期望值来自独立来源：手算表或 Python 参考模型，不一致时打印 FAIL 并以非零码退出）；每个 testbench 做一次**错误注入**

## 阅读（我自己读，不和 AI 对话；读完对 Muse 说"读完 <ID>"；状态：未读 / 在读 / 读完）
| ID | 长文 | 读哪些部分 | 预计用时 | 读完应该能回答（自测，不考核） | 状态 |
|---|---|---|---:|---|---|
| I1-R01 | Harris & Harris, *Digital Design and Computer Architecture: RISC-V Edition* | 第 1 章：数制、补码、逻辑门、CMOS 晶体管 | 2.5h | n 位补码的表示范围？CMOS 反相器怎样工作？什么是噪声容限？ | 未读 |
| I1-R02 | 同上 | 第 2 章：组合逻辑设计 | 3h | 卡诺图怎样化简？多路选择器和译码器怎样搭？什么是竞争冒险和关键路径？ | 未读 |
| I1-R03 | 同上 | 第 3 章：时序逻辑设计 | 3h | 锁存器和触发器有何不同？Moore 与 Mealy 的输出时序？建立 / 保持时间怎样决定最高频率？ | 未读 |
| I1-R04 | 同上 | 第 4 章：硬件描述语言（只读 Verilog / SystemVerilog 部分） | 2.5h | 结构化描述和行为描述的区别？一段 `always @(*)` 综合后是什么？怎样避免意外的锁存器？ | 未读 |
| I1-R05 | 同上 | 5.1–5.2：算术电路（加法器、移位器、乘法器） | 1.5h | 行波进位和超前进位的延迟差别？两个 8 位有符号数相乘需要几位？ | 未读 |
| I1-R06 | Cummings, *Nonblocking Assignments in Verilog Synthesis, Coding Styles That Kill!*（[SNUG 2000](http://www.sunburst-design.com/papers/CummingsSNUG2000SJ_NBA.pdf)） | 全文 | 1h | 组合逻辑和时序逻辑分别该用哪种赋值？混用会造成什么仿真与综合不一致？ | 未读 |
| I1-R07 | Jacob et al., *Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference*（[arXiv:1712.05877](https://arxiv.org/abs/1712.05877)） | 第 1–2 节 | 1h | INT8 推理为什么把乘积累加到 INT32？零点和缩放因子在 MAC 之内还是之外处理？ | 未读 |

## 编程（GPT 带写，只看机器验收；状态：未开始 / 进行中 / 通过）
| ID | 任务 | 计划用时 | 验收要点（展开任务卡时不得弱于此） | 先读 | 依赖动手 | 状态 |
|---|---|---:|---|---|---|---|
| I1-P01 | HDLBits：Verilog 语法与组合逻辑 | 3h | 见 [p01-hdlbits-combinational.md](p01-hdlbits-combinational.md) | I1-R02、R04 | — | 未开始 |
| I1-P02 | 第一个自检模块：`mux2` | 2h | 见 [p02-first-module.md](p02-first-module.md) | I1-R04 | I1-H01 | 未开始 |
| I1-P03 | 组合模块：4 位加法器与参数化多路选择器 | 4h | 加法器穷举 512 种输入；N 选 1 多路选择器测两组参数、每组 ≥ 1000 组随机输入；各一次错误注入；`verilator --lint-only -Wall` 无未说明的警告 | I1-R02、R05 | I1-H01 | 未开始 |
| I1-P04 | HDLBits：时序逻辑 | 2.5h | Sequential Logic 的 Latches and Flip-Flops、Counters、Shift Registers、Finite State Machines 四节完成截图 | I1-R03、R06 | — | 未开始 |
| I1-P05 | 时序模块：计数器、移位寄存器与 FSM | 4h | 带使能和同步复位的计数器、移位寄存器、一个 FSM，自检覆盖复位和全部状态转移；错误注入 | I1-R03、R06 | I1-H01 | 未开始 |
| I1-P06 | INT8 MAC 单元（I3 PE 的前身） | 8h | 先写 ≤ 1 页 spec（接口、位宽、溢出或饱和策略、时序）；有符号 INT8 乘、INT32 累加，带清零和使能；Python 参考模型 ≥ 1000 组随机输入加边界值（含 −128 × −128、累加溢出），0 失败；错误注入 | I1-R05、R07 | I1-H01 | 未开始 |

## 动手（Muse 负责，只看机器验收；状态：未开始 / 进行中 / 完成）
| ID | 任务 | 计划用时 | 验收要点 | 先读 | 状态 |
|---|---|---:|---|---|---|
| I1-H01 | 环境：OSS CAD Suite + cocotb | 1h | 见 [h01-hdl-toolchain.md](h01-hdl-toolchain.md) | — | 未开始 |
| I1-H02 | 回归脚本与 CI | 1h | 见 [h02-regression-ci.md](h02-regression-ci.md) | — | 未开始 |
| I1-H03 | 综合与收尾 | 1.5h | Yosys 综合 MAC 单元并记录单元数；GTKWave 截图；`results/basics/README.md` ≤ 30 行（模块清单、测试数、边界）；打 tag `i1-v1.0`；ROADMAP 中 I1 改为完成 | — | 未开始 |

## 加分（必做全部完成后才碰）
| ID | 任务 | 计划用时 |
|---|---|---:|
| I1-B01 | HDLBits 验证练习：Reading Simulations、Writing Testbenches | 3h |
| I1-B02 | 用 cocotb 重写 MAC 单元的 testbench，与 Verilog 版对比 | 3h |

## 砍线顺序
1. I1-B02
2. I1-B01
3. （仍然超时）I1-P04 只做 Counters 和 Finite State Machines 两节

## 收尾定义
截止日：三栏必做全部完成 → 打 `i1-v1.0` → Muse 更新 ROADMAP 和时间线 → 回到 AI-Infra-Learning 的 C2。没完成的必做项在 `results/basics/README.md` 的"边界"中写明，同样收尾。
