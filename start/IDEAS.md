# IDEAS（停车场：想到就记一行，战役结束再看）

来自 2026-11-08 七阶段体系中的支线（原文在 `journey/archive/plans/supporting-tracks.md`）：
- 模拟电路基础：MIT 6.002，按 I4 中遇到的 CMOS 与时序问题再补
- 等价检查：用开源工具亲手做一次（对应 systolic2x2 中 AI 做过的部分），I5 时考虑
- 数学：线性代数与概率，按 I3 的量化和性能模型需要再补

与其他仓库的交叉：
- cpp-matmul 归档的 OS/WS/IS 数据流访存账本 → I3 的数据流分析可以直接复用
- ai-infra-plan 第 14 周的 GPU 分块 GEMM → 与 I3 的脉动阵列做数据复用对照

## CPU 支线（可选，原 I1 / I2，计划见 `journey/archive/i1-campaign-2026-11-23-cpu-first.md`）
- 单周期 RV32I（ETH DDCA L7–L10，Harris & Harris 第 6–7 章），用 riscv-tests `rv32ui` 回归
- 5 级流水线与 Cache（ETH DDCA L11–L13、L21–L23，Berkeley CS 152）
