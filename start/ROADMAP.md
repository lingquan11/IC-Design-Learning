# 路线图：从数字逻辑到自己的 NPU

> 这是整条路线的唯一总表。当前进度看 [STATE.md](STATE.md)，当前战役在 [campaigns/](campaigns/) 中。
> 战役结束时只改本页的"状态"列；路线调整由我本人决定，并在本页末尾的"变更记录"中写一行。

## 目标
用开源工具，自己走完一颗小 NPU 从规格到实现的全流程：**数字设计 → 片上总线与跨时钟域 → NPU 架构与 RTL → 验证（UVM / 形式化）→ 综合、后端与 FPGA 演示**。流程对标工业 NPU 课程，但全部成果都能公开，架构由我自己定。

## 三栏学习
| 栏 | 谁 | 内容 |
|---|---|---|
| **阅读** `Rxx` | 我自己，不和 AI 对话 | 教材、经典论文、协议规范、作者本人的长文；每篇附自测问题，不考核；读完告诉 Muse 记录 |
| **编程** `Pxx` | GPT 带我写 | RTL、testbench、参考模型由我写，GPT 只按提示梯度引导；HDLBits 练习也在这一栏 |
| **动手** `Hxx` | Muse | 工具链、回归与 CI、形式化与综合的运行、后端流程、FPGA 烧写、整理报告；需要解读的部分由我写 |

## 衔接
- 寒假前在其他仓库：cpp-matmul 的 C0、AI-Infra-Learning 的 C1（CUDA SGEMM）；本仓库从寒假开始，之后与 AI-Infra 的 C2–C5 按学期课表交替
- 已有成果 E1（1×4 脉动阵列行）、E2（2×2 阵列 SKY130 后端）由 AI 执行，I3、I5 中由我亲手重做

## 战役总表
| ID | 战役 | 窗口 | 预算 | 唯一交付物 | 必做验收摘要 | 状态 |
|---|---|---|---:|---|---|---|
| I1 | 数字逻辑与 Verilog | 2027-01-18 → 2027-02-21（寒假，按校历调整） | 40–45h | `results/basics/`：组合 / 时序模块 + INT8 MAC 单元 | 读完 Harris & Harris 第 1–4 章与第 5 章相关两节；每个模块自检 testbench + 错误注入；INT8 MAC 与 Python 参考模型随机回归 0 失败 | 未开始 |
| I2 | 片上总线与跨时钟域 | 寒假后，约 4 周 | 35–45h | `results/bus-and-cdc/` | 异步 FIFO 双时钟随机测试 + SymbiYosys 证明空满性质；APB / AXI4-Lite 协议性质形式化证明通过 | 未开始 |
| I3 | NPU 设计：LeNet INT8 加速器 | 约 6–8 周 | 60–80h | `results/npu/` | 自己写的 spec 与参考模型；PE 阵列与卷积 / 池化 / 全连接数据通路；MNIST 测试图片端到端仿真与参考模型逐字节一致 | 未开始 |
| I4 | 验证：SystemVerilog / UVM | 约 5–6 周 | 45–60h | `results/npu/verif/` | UVM 环境先验证 I2 的 APB 和 FIFO，再验证 NPU 顶层；功能覆盖率报告；回归接入 CI | 未开始 |
| I5 | 实现与演示 | 约 4–5 周 | 35–45h | `results/implementation/` | PE 阵列在 SKY130 上 RTL 到 GDS，setup 收敛、DRC / LVS 干净；NPU 在 FPGA 上识别 MNIST（无开发板时用综合后仿真代替） | 未开始 |

合计约 215–275h。只有 I1 排在寒假；I2–I5 的窗口在寒假后看课表再定。

---

## I1 数字逻辑与 Verilog
- **阅读**：Harris & Harris, *Digital Design and Computer Architecture: RISC-V Edition* 第 1–4 章与第 5 章的算术电路、时序构件两节；Cummings, *Nonblocking Assignments in Verilog Synthesis, Coding Styles That Kill!*（[SNUG 2000](http://www.sunburst-design.com/papers/CummingsSNUG2000SJ_NBA.pdf)）；Jacob et al., *Integer-Arithmetic-Only Inference*（[arXiv:1712.05877](https://arxiv.org/abs/1712.05877)）第 1–2 节
- **编程**：HDLBits 组合 → 第一个自检模块 → 组合模块 → HDLBits always 与时序 → 时序模块与 FSM → **INT8 MAC 单元**（I3 PE 的前身）
- **动手**：OSS CAD Suite 工具链 → 回归脚本与 CI → Yosys 综合与收尾

## I2 片上总线与跨时钟域
- **阅读**（按此顺序）：Cummings, *Clock Domain Crossing (CDC) Design & Verification Techniques Using SystemVerilog*（[SNUG 2008](http://www.sunburst-design.com/papers/CummingsSNUG2008Boston_CDC.pdf)）；Cummings, *Simulation and Synthesis Techniques for Asynchronous FIFO Design*（[SNUG 2002](http://www.sunburst-design.com/papers/CummingsSNUG2002SJ_FIFO1.pdf)）；ZipCPU, [Getting started with formal verification](https://zipcpu.com/blog/2017/10/19/formal-intro.html)（异步 FIFO 的断言要用）；ARM AMBA APB 规范（IHI 0024）与 AXI 规范（IHI 0022）的 AXI4-Lite 部分（developer.arm.com 下载）；ZipCPU, [AXI-Lite 形式化验证](https://zipcpu.com/formal/2018/12/28/axilite.html)
- **编程**：同步 FIFO → 异步 FIFO（格雷码 + 两级同步 + 断言）→ APB 从设备寄存器堆 → AXI4-Lite 从设备（握手性质）
- **动手**：SymbiYosys 环境；运行形式化证明与双时钟随机仿真；CI

## I3 NPU 设计：LeNet INT8 加速器
- **阅读**：H. T. Kung, *Why Systolic Architectures?*（IEEE Computer 1982，[DOI](https://doi.org/10.1109/MC.1982.1653825)）；Sze et al., *Efficient Processing of Deep Neural Networks: A Tutorial and Survey*（[arXiv:1703.09039](https://arxiv.org/abs/1703.09039)）；Jouppi et al., *In-Datacenter Performance Analysis of a Tensor Processing Unit*（[arXiv:1704.04760](https://arxiv.org/abs/1704.04760)）
- **编程**：spec + Python INT8 参考模型 → PE 与脉动阵列（亲手重写 [systolic-mac-1x4](https://github.com/lingquan11/systolic-mac-1x4)，只作参照）→ 卷积 / 池化 / 全连接数据通路 → 片上缓存与 APB 配置（复用 I2）→ 顶层集成
- **动手**：用 PyTorch 训练 LeNet 并导出 INT8 权重与测试向量；MNIST 端到端仿真；综合面积与频率报告

## I4 验证：SystemVerilog / UVM
- **阅读**：Spear & Tumbush, *SystemVerilog for Verification*（类、随机约束、覆盖率相关章节）；Ray Salemi, *The UVM Primer*；Siemens [Verification Academy UVM Cookbook](https://verificationacademy.com/cookbook/uvm-universal-verification-methodology)（按需）
- **编程**：为 I2 的 APB 和 FIFO 写 agent、driver、monitor、scoreboard、sequence，再扩展到 NPU 顶层；功能覆盖率
- **动手**：Verilator + UVM（参照 [Antmicro 示例](https://github.com/antmicro/verilator-uvm-example)）或 cocotb + [pyuvm](https://github.com/pyuvm/pyuvm) 的环境；回归与覆盖率报告接入 CI

## I5 实现与演示
- **阅读**：Kahng et al., *VLSI Physical Design: From Graph Partitioning to Timing Closure*（布局、时钟树、布线、时序收敛章节）；OpenROAD、LibreLane、SkyWater SKY130 官方文档中的流程说明
- **编程**：为 PE 阵列插入流水级修复 setup；FPGA 顶层封装
- **动手**：SKY130 后端全流程（亲手重做 [systolic2x2-asic-backend](https://github.com/lingquan11/systolic2x2-asic-backend)）、DRC / LVS；FPGA 烧写与演示；可选提交 [Tiny Tapeout](https://tinytapeout.com/)

---

## 变更记录
- 2026-11-23：由七阶段体系改写为 I1–I5（CPU 优先），原版见 `journey/archive/`。
- 2026-11-24：改为 NPU 方向与理论 / 实践双线。
- 2026-11-25：改为三栏学习：理论改为自己读长文、不和 AI 对话、不考核；编程（含 HDLBits）由 GPT 带写；动手（工具链、形式化与综合运行、后端、FPGA）由 Muse 负责。双线版本见 [journey/archive/2026-11-24-dual-lane/](../journey/archive/2026-11-24-dual-lane/)。
