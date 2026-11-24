# IC-Design-Learning

A structured learning journey from digital circuits and RTL design to computer architecture and AI accelerators.

从数字逻辑、Verilog 到 RISC-V CPU、脉动阵列和开源 ASIC 后端：跟着名校公开课亲手写 RTL，用测试集和工具报告验收。

## 学习进度
<!-- progress:start -->
```
当前战役 I1 数字逻辑、Verilog 与单周期 RISC-V
  ░░░░░░░░░░░░░░░░░░░░   0%  0/7 个必做任务通过 · 已用 0h / 计划 56h · 截止 2027-02-21
整条路线 I1 → I5
  ░░░░░░░░░░░░░░░░░░░░   0%  0/5 个战役完成
当前任务 I1-T01 入门诊断 + 仿真工具链（寒假开始，等 AI-Infra-Learning 的 C1 收尾） · 最近学习 2026-11-23
```
<!-- progress:end -->

## 我怎么开始学习
在 Codex 中打开本仓库，说"开始学习"；学完说"结束"，Codex 自动归档并更新进度。流程见 [AGENTS.md](AGENTS.md)；路线见 [start/ROADMAP.md](start/ROADMAP.md)（I1 单周期 RISC-V → I2 流水线与 Cache → I3 脉动阵列 → I4 ASIC 后端 → I5 加速器）。

## 学习过程
[journey/](journey/README.md)：时间线、每次学习的日志、笔记、练习和考核记录。

## 学习成果
<!-- results:start -->
| # | 做了什么 | 结论 | 在哪里 |
|---|---|---|---|
| E1 | 1×4 脉动阵列行（Verilog，AI 编写，我定规格） | 4 个定向用例通过；Yosys 通用综合 1859 个单元、227 个触发器 | [systolic-mac-1x4](https://github.com/lingquan11/systolic-mac-1x4) |
| E2 | 2×2 输出驻留阵列 SKY130 后端全流程（AI 执行） | 产出 GDS，DRC 0 违例、LVS 一致；布线后 setup −0.25 ns（10 ns 目标）未收敛 | [systolic2x2-asic-backend](https://github.com/lingquan11/systolic2x2-asic-backend) |
<!-- results:end -->

详见 [results/](results/README.md)。

相关仓库：[cpp-matmul-performance](https://github.com/lingquan11/cpp-matmul-performance)（CPU 矩阵乘法）· [AI-Infra-Learning](https://github.com/lingquan11/AI-Infra-Learning)（CUDA 路线）
