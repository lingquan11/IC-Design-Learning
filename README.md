# IC-Design-Learning

A structured learning journey from digital circuits to my own NPU. 从数字逻辑、片上总线到自己设计的 NPU：读教材和经典论文学理论，用开源工具亲手完成 RTL、验证和后端，每一步都有机器验收。

## 学习进度
<!-- progress:start -->
```
当前战役 I1 数字逻辑与 Verilog · 截止 2027-02-21
  阅读 ░░░░░░░░░░░░░░░░░░░░   0%  0/8 项完成 · 已用 0h / 计划 15h
  编程 ░░░░░░░░░░░░░░░░░░░░   0%  0/6 项完成 · 已用 0h / 计划 23.5h
  动手 ░░░░░░░░░░░░░░░░░░░░   0%  0/3 项完成 · 已用 0h / 计划 3.5h
整条路线 I1 → I5
  ░░░░░░░░░░░░░░░░░░░░   0%  0/5 个战役完成
当前阅读 I1-R01 Harris & Harris 第 1 章（可以提前读）
当前编程任务 I1-P01 HDLBits：Verilog 语法与组合逻辑（寒假开始）
当前动手任务 I1-H01 OSS CAD Suite + cocotb（可以提前做）
最近学习 2026-11-25
```
<!-- progress:end -->

## 我怎么开始学习
| 我想 | 怎么做 |
|---|---|
| 学理论 | 自己读当前阅读任务的长文（不和 AI 对话，不考核）；读完对 Muse 说"读完 <R编号>" |
| 写代码（RTL、testbench、HDLBits） | GPT："开始写代码" … "结束"（结束时自动归档） |
| 装环境、跑仿真 / 综合 / 后端 | Muse："准备环境" 或 "做 <H任务ID>" |
| 看整条路线 | [ROADMAP](start/ROADMAP.md)：I1 数字逻辑 → I2 总线与跨时钟域 → I3 NPU 设计 → I4 UVM 验证 → I5 后端与演示 |

## 学习过程
[journey/](journey/README.md)：时间线、编程日志、动手与阅读日志、笔记。

## 学习成果
<!-- results:start -->
| # | 做了什么 | 结论 | 在哪里 |
|---|---|---|---|
| E1 | 1×4 脉动阵列行（Verilog，AI 编写，我定规格） | 4 个定向用例通过；Yosys 通用综合 1859 个单元、227 个触发器 | [systolic-mac-1x4](https://github.com/lingquan11/systolic-mac-1x4) |
| E2 | 2×2 输出驻留阵列 SKY130 后端全流程（AI 执行） | 产出 GDS，DRC 0 违例、LVS 一致；布线后 setup −0.25 ns（10 ns 目标）未收敛 | [systolic2x2-asic-backend](https://github.com/lingquan11/systolic2x2-asic-backend) |
<!-- results:end -->

详见 [results/](results/README.md)。相关仓库：[cpp-matmul-performance](https://github.com/lingquan11/cpp-matmul-performance)（CPU 矩阵乘法）· [AI-Infra-Learning](https://github.com/lingquan11/AI-Infra-Learning)（CUDA 路线） · 工作流：[learning-workflow](https://github.com/lingquan11/learning-workflow)（三个仓库共用的规则、提示词和进度脚本）
