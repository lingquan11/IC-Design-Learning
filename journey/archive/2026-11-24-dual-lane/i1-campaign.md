# 战役 I1：数字逻辑与 Verilog

- **周期**：2027-01-18 → 2027-02-21（寒假，按校历调整；截止日确定后不延期）
- **预算**：每周 7–8h，合计 35–40h（理论 14.5h + 实践 21h），另有环境任务约 1h（与 Muse 协作）
- **唯一交付物**：`results/basics/`：自己写的组合 / 时序模块和 INT8 MAC 单元，每个都有自检 testbench，一条命令跑完全部回归
- **前置**：AI-Infra-Learning 的 C1 已收尾（2027-01-10）

## 统一约定
- 仿真：Icarus Verilog（`iverilog -g2012`）或 Verilator；波形用 GTKWave。每个模块都有**自检 testbench**：期望值来自独立来源（手算表或 Python 参考模型），不一致时打印 FAIL 并以非零码退出
- 每个 testbench 做一次**错误注入**：故意改坏一处 RTL，确认测试报 FAIL，再改回来
- 理论线的习题照片、HDLBits 截图放 `journey/theory/exercises/`；实践代码放 `results/basics/`

## 理论线（GPT 教学与归档，Gemini 考核；状态：未开始 / 进行中 / 待考官 / 通过）
| ID | 任务 | 计划用时 | 验收要点（展开任务卡时不得弱于此） | 状态 |
|---|---|---:|---|---|
| I1-T01 | 入门诊断 | 1h | 见 [theory/t01-diagnostic.md](theory/t01-diagnostic.md) | 未开始 |
| I1-T02 | 组合逻辑与 Verilog | 6h | 见 [theory/t02-combinational-verilog.md](theory/t02-combinational-verilog.md) | 未开始 |
| I1-T03 | 时序逻辑与有限状态机 | 6h | 看完 ETH L4、L6（时序逻辑、时序与验证）并读教材第 3 章；HDLBits Sequential Logic 的 Latches and Flip-Flops、Counters、Shift Registers、Finite State Machines 四节完成截图；ETH HW1 第 10–13 题闭卷完成并对照官方答案自评；闭卷要点：建立 / 保持时间、同步与异步复位、Moore 与 Mealy | 未开始 |
| I1-T04 | 设计答辩：INT8 MAC 单元 | 1.5h | Gemini 读 `results/basics/mac-int8/README.md` 和代码，追问位宽选择、溢出策略、流水级与关键路径、测试是否充分 | 未开始 |

## 实践线（Muse 协助与归档，只做机器验收；状态：未开始 / 进行中 / 通过）
| ID | 任务 | 计划用时 | 验收要点 | 前置理论 | 依赖环境 | 状态 |
|---|---|---:|---|---|---|---|
| I1-P01 | 第一个自检模块：`mux2` | 2h | 见 [practice/p01-first-module.md](practice/p01-first-module.md) | 无 | I1-S01 | 未开始 |
| I1-P02 | 组合模块：加法器与参数化多路选择器 | 4h | 见 [practice/p02-combinational-modules.md](practice/p02-combinational-modules.md) | I1-T02 | I1-S01 | 未开始 |
| I1-P03 | 时序模块：计数器、移位寄存器与 FSM | 5h | 计数器（带使能和同步复位）、移位寄存器、一个 FSM（参照 ETH 实验 4）各有自检 testbench，覆盖复位和全部状态转移；错误注入记录 | I1-T03 | I1-S01 | 未开始 |
| I1-P04 | INT8 MAC 单元（I3 PE 的前身） | 8h | 先写 ≤ 1 页 spec（接口、位宽、溢出或饱和策略、时序）；有符号 INT8 乘、INT32 累加，带清零和使能；Python 参考模型生成 ≥ 1000 组随机输入加边界值（含 −128 × −128、累加溢出），自检 0 失败；错误注入记录 | I1-T02、I1-T03 | I1-S01 | 未开始 |
| I1-P05 | 收尾 | 2h | `results/basics/README.md` ≤ 30 行（模块清单、测试数、边界）；`make test` 或一个脚本跑完全部回归；Yosys 通用综合 MAC 单元并记录单元数；打 tag `i1-v1.0` | — | I1-S01 | 未开始 |

## 环境准备（与 Muse 协作，按 [setup.md](../../prompts/setup.md)；状态：未开始 / 进行中 / 就绪）
| ID | 内容 | 验收命令 / 要点 | 被哪些任务依赖 | 状态 |
|---|---|---|---|---|
| I1-S01 | WSL2 中安装 OSS CAD Suite（Icarus Verilog、Verilator、Yosys、SymbiYosys、GTKWave）和 Python 3 + cocotb；仓库 CI 能跑仿真 | 见 [s01-hdl-toolchain.md](s01-hdl-toolchain.md) | I1-P01 起 | 未开始 |

## 加分线（两条线的必做任务都通过后才碰）
| ID | 任务 | 计划用时 |
|---|---|---:|
| I1-B01 | HDLBits 验证练习：Verification: Reading Simulations、Writing Testbenches | 3h |
| I1-B02 | 用 cocotb 重写 MAC 单元的 testbench，与 Verilog 版对比 | 3h |
| I1-B03 | 上板：如果有 FPGA 开发板，把 MAC 单元接按键和数码管跑起来 | 4h |

## 砍线顺序
1. I1-B03
2. I1-B02
3. I1-B01
4. （仍然超时）I1-P05 跳过 Yosys 综合，在 README 中写明

## 收尾定义
截止日：两条线的必做任务都通过 → 打 `i1-v1.0` → 由实践线归档更新 ROADMAP 和时间线 → 回到 AI-Infra-Learning 的 C2。
有必做项没有完成：在 `results/basics/README.md` 的"边界"一节写明，同样收尾。
