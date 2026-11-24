# 战役 I1：数字逻辑、Verilog 与单周期 RISC-V

- **周期**：2027-01-18 → 2027-02-21（寒假，按校历调整；截止日确定后不延期）
- **预算**：每周 12–15h，合计 60–75h；必做线计划 56h
- **唯一交付物**：`results/rv32i-single-cycle/`：自己写的单周期 RV32I CPU，一条命令跑完对应的 riscv-tests 并输出通过数
- **前置**：AI-Infra-Learning 的 C1 已收尾（2027-01-10）

## 统一约定（所有任务共用）
- 仿真：Icarus Verilog（`iverilog -g2012`）或 Verilator；波形用 GTKWave。每个模块都有**自检 testbench**：期望值来自独立来源（手算表、Python 参考模型），不一致时打印 FAIL 并以非零码退出
- 每个 testbench 要做一次**错误注入**：故意改坏一处 RTL，确认测试会报 FAIL，再改回来
- 代码目录：练习级小模块放 `results/basics/`，CPU 放 `results/rv32i-single-cycle/`；HDLBits 截图和笔记放 `journey/exercises/hdlbits/`
- 官方习题（ETH Optional HW）先闭卷做，拍照存入 `journey/exercises/ddca-hw/`，再对照官方答案自评

## 必做线（状态：未开始 / 进行中 / 待考官 / 通过）
| ID | 任务 | 计划用时 | 验收要点（展开任务卡时不得弱于此） | 状态 |
|---|---|---:|---|---|
| I1-T01 | 入门诊断 + 仿真工具链 | 3h | 见 [t01-diagnostic-and-toolchain.md](t01-diagnostic-and-toolchain.md) | 未开始 |
| I1-T02 | 组合逻辑与 Verilog 基础 | 10h | 见 [t02-combinational-verilog.md](t02-combinational-verilog.md) | 未开始 |
| I1-T03 | 时序逻辑与有限状态机 | 10h | HDLBits Sequential Logic 的 Latches and Flip-Flops、Counters、Shift Registers、Finite State Machines 四节全部通过（截图）；自己写的计数器和一个 FSM（参照 ETH 实验 4）带自检 testbench，覆盖复位和全部状态转移；ETH HW1 第 10–13 题闭卷完成并自评 | 未开始 |
| I1-T04 | ALU 与寄存器堆 | 8h | ALU 覆盖 RV32I 需要的全部运算；Python 参考模型生成 ≥ 1000 组随机向量加边界值，自检 testbench 0 失败；寄存器堆 2 读 1 写、x0 恒为 0；错误注入有记录 | 未开始 |
| I1-T05 | 单周期 RV32I 数据通路与控制 | 14h | 支持 RV32I 除 `ecall`/`ebreak`/`fence`/CSR 之外的指令（清单入库）；控制信号表入库；两个手写汇编程序（如求和、斐波那契）在仿真中得到预期的寄存器和内存值；ETH HW2 第 9 题闭卷完成并自评 | 未开始 |
| I1-T06 | riscv-tests 回归 | 8h | `[ai]` 提供最小测试环境（把通过/失败写到固定地址）和运行脚本；所支持指令对应的 `rv32ui-p-*` 测试全部通过（清单入库）；一条命令输出汇总；故意改坏一条指令时对应测试报 FAIL | 未开始 |
| I1-T07 | 收尾 | 3h | `results/rv32i-single-cycle/README.md`（≤ 30 行：结构图、支持指令、测试通过数、边界）；Yosys 通用综合跑一次并记录单元数（不讨论时序）；打 tag `i1-v1.0`；不考官 | 未开始 |

I1-T03 到 I1-T07 的任务卡在前一张通过后再展开（见 [RULES.md](../../RULES.md) §2）。

## 加分线（必做线全部通过后才碰）
| ID | 任务 | 计划用时 |
|---|---|---:|
| I1-B01 | 5 级流水线雏形（先不处理冒险，为 I2 打底） | 8h |
| I1-B02 | HDLBits 的两节验证练习：Verification: Reading Simulations、Writing Testbenches | 3h |
| I1-B03 | 上板：如果有 FPGA 开发板，把 CPU 跑在板子上 | 4h |

## 砍线顺序
1. I1-B03
2. I1-B02
3. I1-B01
4. （仍然超时）I1-T07 跳过 Yosys 综合，在 README 中写明

## 收尾定义
截止日：必做线全部通过 → 打 `i1-v1.0` → 按归档流程更新 ROADMAP 和时间线 → 回到 AI-Infra-Learning 的 C2。
有必做项没有完成：在 README 的"边界"一节写明，同样收尾。
