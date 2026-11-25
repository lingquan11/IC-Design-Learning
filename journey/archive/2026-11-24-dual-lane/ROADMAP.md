# 路线图：从数字逻辑到自己的 NPU

> 这是整条路线的唯一总表。当前进度看 [STATE.md](STATE.md)，当前战役在 [campaigns/](campaigns/) 中。
> 战役结束时只改本页的"状态"列；路线调整由我本人决定，并在本页末尾的"变更记录"中写一行。

## 目标
用开源工具，自己走完一颗小 NPU 从规格到实现的全流程：**数字设计 → 片上总线与跨时钟域 → NPU 架构与 RTL → 验证（UVM / 形式化）→ 综合、后端与 FPGA 演示**。流程对标工业 NPU 课程（数字设计、NPU 模块、SV/UVM 验证、后端），但全部成果都能公开，架构由我自己定。

## 双线学习
| 线 | 导师 | 归档 | 考核 | 内容 |
|---|---|---|---|---|
| **理论线**（`Txx`） | GPT | GPT | Gemini 独立考核 | 名校课程、教材、协议规范、习题、设计答辩 |
| **实践线**（`Pxx`） | Muse | Muse | 只看机器验收 | spec、RTL、testbench、形式化、综合、后端 |
| **环境任务**（`Sxx`） | Muse | Muse | 只看机器验收 | 工具安装和工程骨架，可以提前做 |

每个战役两条线并行：理论任务讲清"为什么"，实践任务把它做出来；实践任务卡写明依赖的理论任务。每个战役的最后一个理论任务是**设计答辩**：Gemini 读我的实践成果，追问设计选择。

## 衔接
- 寒假前在其他仓库：cpp-matmul 的 C0（CPU 访存与分块）、AI-Infra-Learning 的 C1（CUDA SGEMM）
- 本仓库从寒假开始；之后与 AI-Infra-Learning 的 C2–C5 按学期课表交替
- 已有成果 E1（1×4 脉动阵列行）、E2（2×2 阵列 SKY130 后端）由 AI 执行，I3、I5 中由我亲手重做

## 工具基线（I1-S01 实测核对）
- WSL2（Ubuntu 24.04）；[OSS CAD Suite](https://github.com/YosysHQ/oss-cad-suite-build)（Icarus Verilog、Verilator、Yosys、SymbiYosys、GTKWave）；Python 3 + cocotb
- I4：最新版 Verilator + Accellera UVM（或 cocotb + pyuvm）；I5：OpenROAD / LibreLane、Magic、Netgen、KLayout、SKY130 PDK

## 战役总表
| ID | 战役 | 窗口 | 预算 | 唯一交付物 | 必做验收摘要 | 状态 |
|---|---|---|---:|---|---|---|
| I1 | 数字逻辑与 Verilog | 2027-01-18 → 2027-02-21（寒假，按校历调整） | 35–40h | `results/basics/`：组合 / 时序模块 + INT8 MAC 单元 | 每个模块自检 testbench + 错误注入；INT8 MAC 与 Python 参考模型随机回归 0 失败；理论线通过 Gemini 考核 | 未开始 |
| I2 | 片上总线与跨时钟域 | 寒假后，约 4 周 | 35–45h | `results/bus-and-cdc/`：同步 / 异步 FIFO、APB 从设备、AXI4-Lite 从设备 | 异步 FIFO 双时钟随机测试 + SymbiYosys 证明空满标志性质；APB / AXI4-Lite 协议性质形式化证明通过 | 未开始 |
| I3 | NPU 设计：LeNet INT8 加速器 | 约 6–8 周 | 60–80h | `results/npu/`：spec、Python 参考模型、RTL | 自己写的 spec 与参考模型；PE 阵列与卷积 / 池化 / 全连接数据通路；MNIST 测试图片端到端仿真结果与参考模型逐字节一致 | 未开始 |
| I4 | 验证：SystemVerilog / UVM / 形式化 | 约 5–6 周 | 45–60h | `results/npu/verif/`：UVM 验证环境与覆盖率报告 | UVM 环境（agent、scoreboard、sequence）先验证 I2 的 APB 和 FIFO，再验证 NPU 顶层；功能覆盖率报告；回归接入 CI | 未开始 |
| I5 | 实现与演示 | 约 4–5 周 | 35–45h | `results/implementation/`：综合 / 后端报告 + 演示 | NPU 的 PE 阵列在 SKY130 上从 RTL 到 GDS，setup 收敛、DRC / LVS 干净；NPU 在 FPGA 上识别 MNIST（无开发板时用综合后仿真代替）；可选 Tiny Tapeout | 未开始 |

合计约 210–270h。只有 I1 排在寒假；I2–I5 的窗口在寒假后看课表再定。

---

## I1 数字逻辑与 Verilog
- **要回答的问题**：组合和时序电路怎样用 Verilog 描述？怎样证明自己写的模块是对的？
- **理论主线**：ETH Zürich *Digital Design and Computer Architecture*（Onur Mutlu），[Spring 2026 课程页](https://safari.ethz.ch/ddca/spring2026/)，L1–L6b；教材 Harris & Harris, *Digital Design and Computer Architecture: RISC-V Edition* 第 1–5 章；[HDLBits](https://hdlbits.01xz.net/wiki/Main_Page)；ETH Optional HW1（有官方答案）
- **实践**：第一个自检模块 → 组合模块 → 时序模块与 FSM → **INT8 MAC 单元**（I3 PE 的前身，用 Python 参考模型做随机回归）

## I2 片上总线与跨时钟域
- **要回答的问题**：两个时钟域之间怎样安全地传数据？总线握手怎样保证不丢、不重？
- **理论主线**：Cummings, *Simulation and Synthesis Techniques for Asynchronous FIFO Design*（[SNUG 2002](http://www.sunburst-design.com/papers/CummingsSNUG2002SJ_FIFO1.pdf)）；ARM AMBA APB 规范（IHI 0024）与 AXI 规范（IHI 0022），在 developer.arm.com 下载；ZipCPU 的 [AXI-Lite 形式化验证](https://zipcpu.com/formal/2018/12/28/axilite.html)；SymbiYosys 官方文档
- **实践**：同步 FIFO → 异步 FIFO（格雷码 + 两级同步 + 形式化）→ APB 从设备寄存器堆 → AXI4-Lite 从设备（形式化证明握手性质）

## I3 NPU 设计：LeNet INT8 加速器
- **要回答的问题**：同一个卷积，数据流怎样决定数据复用和 PE 利用率？INT8 量化引入了多少误差？
- **理论主线**：ETH DDCA L18b（Systolic Array Architectures）；H. T. Kung, *Why Systolic Architectures?*（IEEE Computer 1982，[DOI](https://doi.org/10.1109/MC.1982.1653825)）；[MIT 6.5930/1](https://csg.csail.mit.edu/6.5930/info.html) 与 [Eyeriss 教程](https://eyeriss.mit.edu/2019_neurips_tutorial.pdf)；TPU 论文（[arXiv:1704.04760](https://arxiv.org/abs/1704.04760)）
- **实践**：spec + PyTorch 训练 LeNet 并量化为 INT8 的参考模型 → PE 与脉动阵列（亲手重写 [systolic-mac-1x4](https://github.com/lingquan11/systolic-mac-1x4)，只作参照）→ 卷积 / 池化 / 全连接数据通路 → 片上缓存与 APB 配置（复用 I2）→ 顶层集成与 MNIST 端到端仿真

## I4 验证：SystemVerilog / UVM / 形式化
- **要回答的问题**：怎样系统地证明一个设计"足够对"？覆盖率说明了什么、没说明什么？
- **理论主线**：Chris Spear, *SystemVerilog for Verification*；Siemens [Verification Academy UVM Cookbook](https://verificationacademy.com/cookbook/uvm-universal-verification-methodology)
- **实践**：Verilator + UVM（参照 [Antmicro 示例](https://github.com/antmicro/verilator-uvm-example)）或 cocotb + [pyuvm](https://github.com/pyuvm/pyuvm)：先为 I2 的 APB 和 FIFO 搭 agent、scoreboard、sequence，再扩展到 NPU 顶层；功能覆盖率；CI 回归

## I5 实现与演示
- **要回答的问题**：从 RTL 到 GDS 每一步在做什么？时序不收敛时怎样从结构上修？
- **理论主线**：[Berkeley EECS 151/251A Fall 2025](https://inst.eecs.berkeley.edu/~eecs151/fa25/) 的 ASIC 部分；OpenROAD、LibreLane、SkyWater SKY130 官方文档
- **实践**：PE 阵列的 SKY130 后端（亲手重做 [systolic2x2-asic-backend](https://github.com/lingquan11/systolic2x2-asic-backend)，加流水级解决 setup 未收敛）→ FPGA 演示 → 可选：子模块提交 [Tiny Tapeout](https://tinytapeout.com/)

---

## 变更记录
- 2026-11-23：由七阶段体系改写为 I1–I5（CPU 优先），原版见 [journey/archive/roadmap-2026-11-23-cpu-first.md](../journey/archive/roadmap-2026-11-23-cpu-first.md)。
- 2026-11-24：改为 NPU 方向并采用理论 / 实践双线：路线对标工业 NPU 课程（总线与跨时钟域、NPU 模块、UVM 验证、后端），全部用开源工具；单周期 RV32I、流水线与 Cache 移入 [IDEAS.md](IDEAS.md) 作为可选的 CPU 支线；I1 由 56h 减为 35–40h，以 INT8 MAC 单元收尾，衔接 I3。
