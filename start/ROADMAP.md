# 路线图：从数字逻辑到 AI 加速器

> 这是整条路线的唯一总表。当前进度看 [STATE.md](STATE.md)，当前战役在 [campaigns/](campaigns/) 中。
> 战役结束时只改本页的"状态"列；路线调整须由我本人决定，并在本页末尾的"变更记录"中写一行。

## 原则
1. **权威课程 → 亲手实现 → 机器验收**：知识主线用名校公开课和教材；RTL 由我自己写（`[me]`）；验收看自检 testbench、官方测试集和工具报告。
2. **战役制**：每个战役 4–5 周，一个公开交付物，分必做线和加分线，到期收尾（见 [RULES.md](RULES.md)）。
3. **补上"AI 代做"的部分**：已有的两个成果仓库（1×4 脉动阵列行、2×2 阵列 SKY130 后端）由 AI 执行，I3、I4 要求我亲手重做并能逐步解释。

## 衔接
- 寒假前在其他仓库：[cpp-matmul-performance](https://github.com/lingquan11/cpp-matmul-performance) 的 C0（CPU 访存与分块），[AI-Infra-Learning](https://github.com/lingquan11/AI-Infra-Learning) 的 C1（CUDA SGEMM）
- 本仓库从寒假开始；之后与 AI-Infra-Learning 的 C2–C4 按学期课表交替安排

## 工具基线（I1-T01 实测核对）
- WSL2（Ubuntu 24.04）；Icarus Verilog、Verilator、GTKWave；RISC-V GCC 交叉工具链（`riscv64-unknown-elf-gcc`，用 `-march=rv32i`）
- 后端（I4）：OpenROAD / LibreLane、Magic、Netgen、KLayout、SKY130 PDK

## 战役总表

| ID | 战役 | 窗口 | 预算 | 唯一交付物 | 必做验收摘要 | 状态 |
|---|---|---|---:|---|---|---|
| I1 | 数字逻辑、Verilog 与单周期 RISC-V | 2027-01-18 → 2027-02-21（寒假，按校历调整） | 60–75h | `results/rv32i-single-cycle/` | 入门诊断；HDLBits 组合与时序章节；ALU 与寄存器堆随机回归；单周期 RV32I（不含 CSR/ecall/fence）通过对应的 riscv-tests `rv32ui` 测试 | 未开始 |
| I2 | 流水线 CPU 与 Cache | 寒假后，暂定 4–5 周 | 40–55h | `results/rv32i-pipeline/` | 5 级流水，转发、暂停、冲刷正确，`rv32ui` 回归仍全部通过；Cache 模拟器的命中率实验 | 未开始 |
| I3 | NPU 微架构：脉动阵列与数据流 | 暂定 4–5 周 | 40–55h | `results/systolic-array/` | 亲手重写并扩展 1×4 阵列行 → 参数化 N×N，输出驻留与权重驻留两种数据流，随机向量回归；访存账本与 PE 利用率模型 | 未开始 |
| I4 | 开源 ASIC 后端：亲手重跑 | 暂定 4 周 | 35–45h | `results/asic-flow/` | 亲手把 I3 阵列从 RTL 跑到 GDS（SKY130）；加流水级后 setup 收敛；DRC/LVS 干净；能逐步解释每个阶段 | 未开始 |
| I5 | AI 加速器 MVP | I4 之后再定 | — | — | 根据 I1–I4 的结果再写 | 未开始 |

合计约 175–230h（I5 除外）。只有 I1 排在寒假；I2–I4 的窗口看到下学期课表后再定。

---

## I1 数字逻辑、Verilog 与单周期 RISC-V
- **要回答的问题**：一条指令是怎样由门电路、寄存器和控制信号执行完的？
- **主课程**：ETH Zürich *Digital Design and Computer Architecture*（Onur Mutlu），[Spring 2026 课程页](https://safari.ethz.ch/ddca/spring2026/)：L1–L6b（数字逻辑、Verilog、时序与验证）、L7–L10（ISA 与微架构）；视频见 [Spring 2025 讲座列表](https://www.youtube.com/playlist?list=PL5Q2soXY2Zi9Eo29LMgKVcaydS7V1zZW3)
- **教材**：Harris & Harris, *Digital Design and Computer Architecture: RISC-V Edition*（第 1–5 章；第 6 章；第 7.1–7.3 节单周期处理器）
- **官方练习**：ETH DDCA [Spring 2025 Optional HW](https://safari.ethz.ch/ddca/spring2025/doku.php?id=homeworks) 1（布尔代数、组合逻辑、Verilog、FSM）、HW2 第 9 题（单周期数据通路），均有官方答案；[ETH 实验 3–6](https://safari.ethz.ch/ddca/spring2026/doku.php?id=labs)（原为 FPGA 实验，这里用仿真完成）
- **Verilog 练习**：[HDLBits](https://hdlbits.01xz.net/wiki/Main_Page)
- **验收测试集**：[riscv-tests](https://github.com/riscv-software-src/riscv-tests) 的 `isa/rv32ui`；规范：[RISC-V RV32I](https://docs.riscv.org/reference/isa/v20240411/unpriv/rv32.html)
- **说明**：ETH 课程的实验用 MIPS，本路线改用 RISC-V（与教材 RISC-V 版、riscv-tests 和后续 I2 对齐），概念完全对应
- **主要风险**：riscv-tests 默认通过 `ecall`/CSR 报告结果，单周期 CPU 不支持 → 由 `[ai]` 提供最小测试环境（把通过/失败写到固定地址）

## I2 流水线 CPU 与 Cache
- **要回答的问题**：流水线怎样在保持正确性的前提下提高吞吐？Cache 怎样把访存延迟藏起来？
- **锚点**：ETH DDCA L11–L13（多周期、流水线、精确异常）、L21–L23（存储层次与 Cache）；Harris & Harris 第 7.5 节、第 8 章；ETH Optional HW2 第 10–12 题（流水线）、HW5（存储）；选读 [Berkeley CS 152 Spring 2026](https://inst.eecs.berkeley.edu/~cs152/sp26/)

## I3 NPU 微架构：脉动阵列与数据流
- **要回答的问题**：同一个矩阵乘法，不同数据流怎样决定数据复用和 PE 利用率？
- **锚点**：ETH DDCA L18b（Systolic Array Architectures）；H. T. Kung, *Why Systolic Architectures?*（IEEE Computer 1982，[DOI](https://doi.org/10.1109/MC.1982.1653825)）；[MIT 6.5930/1](https://csg.csail.mit.edu/6.5930/info.html) 与 [Eyeriss 教程](https://eyeriss.mit.edu/2019_neurips_tutorial.pdf)；TPU 论文（[arXiv:1704.04760](https://arxiv.org/abs/1704.04760)）
- **起点**：[systolic-mac-1x4](https://github.com/lingquan11/systolic-mac-1x4)（AI 编写，只作参照，不复制）

## I4 开源 ASIC 后端：亲手重跑
- **要回答的问题**：从 RTL 到 GDS 每一步在做什么？时序为什么不收敛，怎样从结构上修？
- **锚点**：[Berkeley EECS 151/251A Fall 2025](https://inst.eecs.berkeley.edu/~eecs151/fa25/) 的 ASIC 部分讲义；OpenROAD、LibreLane、SkyWater SKY130 PDK 官方文档
- **起点**：[systolic2x2-asic-backend](https://github.com/lingquan11/systolic2x2-asic-backend)（AI 执行，布线后 setup −0.25 ns 未收敛），这次要我自己跑、自己解释，并加流水级解决

---

## 变更记录
- 2026-11-23：由 2026-11-08 的七阶段体系（见 [journey/archive/](../journey/archive/)）改写为战役制。对应关系：Stage 01 → I1；Stage 02 → 已由 cpp-matmul 的 C0 覆盖；Stage 03 → I1（单周期）+ I2；Stage 04 → 已由 AI-Infra-Learning 的 C1–C3 覆盖；Stage 05 → I3；Stage 06 → I4；Stage 07 → I5。主课程由 MIT 6.004（2017，非 Verilog）改为 ETH DDCA（Verilog，2026 年仍在开课，有完整视频和带答案的习题）。数学、模拟电路、验证方法学等支线移入 [IDEAS.md](IDEAS.md)。
