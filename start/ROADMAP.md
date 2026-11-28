# 路线图：从数字逻辑到自己的 NPU

> 这是整条路线的唯一总表。当前进度看 [STATE.md](STATE.md)，当前战役在 [campaigns/](campaigns/) 中。
> 战役结束时只改本页的"状态"列；路线调整由我本人决定，并在本页末尾的"变更记录"中写一行。

## 目标
用开源工具，自己走完一颗小 NPU 从规格到实现的全流程：**数字设计 → 片上总线与跨时钟域 → NPU 架构与 RTL → 验证（UVM / 形式化）→ 综合、后端与 FPGA 演示**。流程对标工业 NPU 课程，但全部成果都能公开，架构由我自己定。

## 三栏学习
| 栏 | 谁 | 内容 |
|---|---|---|
| **阅读** `Rxx` | 我自己，不和 AI 对话 | 每个战役一份主教材的章节（I1 Harris & Harris、I2 ZipCPU 教程、I3 Sze 等、I4 UVM Primer、I5 Kahng 等），不在多份资料之间切换；协议规范和工具手册只在任务中查阅；每篇附自测问题，不考核；读完告诉 Muse 记录 |
| **编程** `Pxx` | GPT 带我写 | RTL、testbench、参考模型由我写，GPT 只按提示梯度引导 |
| **动手** `Hxx` | Muse | 工具链、回归与 CI、形式化与综合的运行、后端流程、FPGA 烧写、整理报告；需要解读的部分由我写 |

**主线**：每个战役读一本主教材 → 编程 → 动手，三栏计入进度。**支线**：与主教材配套的现成实践课程，选做、不计入进度，读完对应章节后做。

| 战役 | 主线主教材 | 支线实践课程 |
|---|---|---|
| I1 | Harris & Harris 第 1–5 章 | [HDLBits](https://hdlbits.01xz.net/wiki/Problem_sets)：组合、时序、验证练习 |
| I2 | ZipCPU 博客：跨时钟域、异步 FIFO、形式化、AXI-Lite | [ZipCPU 入门教程](https://zipcpu.com/tutorial/)：10 课设计练习与[形式化教程](https://zipcpu.com/tutorial/formal.html) |
| I3 | Sze 等, *Efficient Processing of Deep Neural Networks* | 无：编程任务本身就是从零写 PE 阵列 |
| I4 | Salemi, *The UVM Primer* | 无：照书中配套代码逐章改写即可 |
| I5 | Kahng 等, *VLSI Physical Design* | [Tiny Tapeout](https://tinytapeout.com/)：用开源流程把小设计真正流片（可选） |

## 衔接
- 寒假前在其他仓库：cpp-matmul 的 C0，之后接 [ai-infra-plan](https://github.com/lingquan11/ai-infra-plan)（代码放在 [AI-Infra-Learning](https://github.com/lingquan11/AI-Infra-Learning)）；本仓库从寒假开始，之后与 ai-infra-plan 按学期课表交替
- 已有成果 E1（1×4 脉动阵列行）、E2（2×2 阵列 SKY130 后端）由 AI 执行，I3、I5 中由我亲手重做

## 战役总表
| ID | 战役 | 窗口 | 预算 | 唯一交付物 | 必做验收摘要 | 状态 |
|---|---|---|---:|---|---|---|
| I1 | 数字逻辑与 Verilog | 2027-01-18 → 2027-02-21（寒假，按校历调整） | 35–40h | `results/basics/`：组合 / 时序模块 + INT8 MAC 单元 | 读完 Harris & Harris 第 1–4 章与第 5 章相关两节；每个模块自检 testbench + 错误注入；INT8 MAC 与 Python 参考模型随机回归 0 失败 | 未开始 |
| I2 | 片上总线与跨时钟域 | 寒假后，约 4 周 | 35–45h | `results/bus-and-cdc/` | 异步 FIFO 双时钟随机测试 + SymbiYosys 证明空满性质；APB / AXI4-Lite 协议性质形式化证明通过 | 未开始 |
| I3 | NPU 设计：LeNet INT8 加速器 | 约 6–8 周 | 60–80h | `results/npu/` | 自己写的 spec 与参考模型；PE 阵列与卷积 / 池化 / 全连接数据通路；MNIST 测试图片端到端仿真与参考模型逐字节一致 | 未开始 |
| I4 | 验证：SystemVerilog / UVM | 约 5–6 周 | 45–60h | `results/npu/verif/` | UVM 环境先验证 I2 的 APB 和 FIFO，再验证 NPU 顶层；功能覆盖率报告；回归接入 CI | 未开始 |
| I5 | 实现与演示 | 约 4–5 周 | 35–45h | `results/implementation/` | PE 阵列在 SKY130 上 RTL 到 GDS，setup 收敛、DRC / LVS 干净；NPU 在 FPGA 上识别 MNIST（无开发板时用综合后仿真代替） | 未开始 |

合计约 215–275h。只有 I1 排在寒假；I2–I5 的窗口在寒假后看课表再定。

---

## I1 数字逻辑与 Verilog
- **阅读**（主教材 Harris & Harris）：[*Digital Design and Computer Architecture: RISC-V Edition*](https://shop.elsevier.com/books/digital-design-and-computer-architecture-risc-v-edition/harris/978-0-12-820064-3)（[作者课件](https://pages.hmc.edu/harris/class/e85/old/fall24/)）第 1–4 章与第 5 章的算术电路、时序构件两节
- **支线**：[HDLBits](https://hdlbits.01xz.net/wiki/Problem_sets) 的组合、时序与验证练习
- **编程**：第一个自检模块 → 组合模块 → 时序模块与 FSM → **INT8 MAC 单元**（I3 PE 的前身）
- **动手**：OSS CAD Suite 工具链 → 回归脚本与 CI → Yosys 综合与收尾

## I2 片上总线与跨时钟域
- **阅读**（主教材 ZipCPU 博客，同一作者）：[Some Simple Clock-Domain Crossing Solutions](https://zipcpu.com/blog/2017/10/20/cdc.html) → [Crossing clock domains with an Asynchronous FIFO](https://zipcpu.com/blog/2018/07/06/afifo.html) → [Getting started with formal verification](https://zipcpu.com/blog/2017/10/19/formal-intro.html) → [Building an AXI-Lite slave the easy way](https://zipcpu.com/blog/2020/03/08/easyaxil.html)。ARM [APB（IHI 0024）](https://developer.arm.com/documentation/ihi0024/latest/)与 [AXI（IHI 0022）](https://developer.arm.com/documentation/ihi0022/latest/)规范在编程任务中查阅
- **支线**：[ZipCPU 入门教程](https://zipcpu.com/tutorial/)（第 7 课同步器、第 10 课 FIFO 与配套形式化练习）
- **编程**：同步 FIFO → 异步 FIFO（格雷码 + 两级同步 + 断言）→ APB 从设备寄存器堆 → AXI4-Lite 从设备（握手性质）
- **动手**：SymbiYosys 环境；运行形式化证明与双时钟随机仿真；CI

## I3 NPU 设计：LeNet INT8 加速器
- **阅读**（主教材 Sze 等）：Sze, Chen, Yang, Emer, [*Efficient Processing of Deep Neural Networks*](https://doi.org/10.1007/978-3-031-01766-7)（2020）的 DNN 概述、评价指标、核心计算、加速器设计（数据流与脉动阵列，含 TPU 案例）和降低精度几章；买不到书时用作者的同名综述 [arXiv:1703.09039](https://arxiv.org/abs/1703.09039) 代替
- **编程**：spec + Python INT8 参考模型 → PE 与脉动阵列（亲手重写 [systolic-mac-1x4](https://github.com/lingquan11/systolic-mac-1x4)，只作参照）→ 卷积 / 池化 / 全连接数据通路 → 片上缓存与 APB 配置（复用 I2）→ 顶层集成
- **动手**：用 PyTorch 训练 LeNet 并导出 INT8 权重与测试向量；MNIST 端到端仿真；综合面积与频率报告

## I4 验证：SystemVerilog / UVM
- **阅读**（主教材 UVM Primer）：Ray Salemi, *The UVM Primer* 全书（从 SystemVerilog 面向对象到完整 UVM 环境；[作者的配套代码](https://github.com/raysalemi/uvmprimer)按章节对照）
- **编程**：为 I2 的 APB 和 FIFO 写 agent、driver、monitor、scoreboard、sequence，再扩展到 NPU 顶层；功能覆盖率
- **动手**：Verilator + UVM（参照 [Antmicro 示例](https://github.com/antmicro/verilator-uvm-example)）或 cocotb + [pyuvm](https://github.com/pyuvm/pyuvm) 的环境；回归与覆盖率报告接入 CI

## I5 实现与演示
- **阅读**（主教材 Kahng 等）：Kahng, Lienig, Markov, Hu, [*VLSI Physical Design: From Graph Partitioning to Timing Closure*](https://doi.org/10.1007/978-3-030-96415-3)（第 2 版）的布局、时钟树、布线、时序收敛几章
- **支线**：[Tiny Tapeout](https://tinytapeout.com/)（可选，真实流片）
- **编程**：为 PE 阵列插入流水级修复 setup；FPGA 顶层封装
- **动手**：SKY130 后端全流程（亲手重做 [systolic2x2-asic-backend](https://github.com/lingquan11/systolic2x2-asic-backend)）、DRC / LVS；FPGA 烧写与演示（工具手册：[OpenROAD](https://openroad.readthedocs.io/en/latest/)、[LibreLane](https://librelane.readthedocs.io/en/latest/)、[SkyWater SKY130](https://skywater-pdk.readthedocs.io/en/main/)）

---

## 变更记录
- 2026-11-23：由七阶段体系改写为 I1–I5（CPU 优先），原版见 `journey/archive/`。
- 2026-11-24：改为 NPU 方向与理论 / 实践双线。
- 2026-11-25：改为三栏学习：理论改为自己读长文、不和 AI 对话、不考核；编程（含 HDLBits）由 GPT 带写；动手（工具链、形式化与综合运行、后端、FPGA）由 Muse 负责。双线版本见 [journey/archive/2026-11-24-dual-lane/](../journey/archive/2026-11-24-dual-lane/)。
- 2026-11-25：阅读改为"一个战役一份主教材"：I1 只用 Harris & Harris（去掉 Cummings 与 Jacob 两篇），I2 用 ZipCPU 博客，I3 用 Sze 等的书，I4 用 UVM Primer，I5 用 Kahng 等的书。
- 2026-11-25：加上支线：每个战役配一门现成实践课程（I1 HDLBits、I2 ZipCPU 入门教程、I5 Tiny Tapeout），选做、不计入进度；HDLBits 从编程任务移到支线。
