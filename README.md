# IC-Design-Learning

A structured learning journey from digital circuits to my own NPU. 从数字逻辑、片上总线到自己设计的 NPU：跟着名校课程学理论，用开源工具亲手完成 RTL、验证和后端，每一步都有机器验收。

## 学习进度
<!-- progress:start -->
```
当前战役 I1 数字逻辑与 Verilog · 截止 2027-02-21
  理论线 ░░░░░░░░░░░░░░░░░░░░   0%  0/4 个任务通过 · 已用 0h / 计划 14.5h
  实践线 ░░░░░░░░░░░░░░░░░░░░   0%  0/5 个任务通过 · 已用 0h / 计划 21h
整条路线 I1 → I5
  ░░░░░░░░░░░░░░░░░░░░   0%  0/5 个战役完成
环境准备 0/1 就绪（与 Muse 协作，不计入学习进度）· 已用 0h
当前理论任务 I1-T01 入门诊断（寒假开始）
当前实践任务 I1-P01 第一个自检模块 mux2（依赖 I1-S01）
最近学习 2026-11-24
```
<!-- progress:end -->

## 我怎么开始学习
| 我想 | 对谁说 |
|---|---|
| 学理论（课程、习题；结束时自动归档） | GPT："开始理论学习" … "结束" |
| 做实践（RTL、验证、综合；结束时自动归档） | Muse："开始实践" … "结束" |
| 考核一个做完的理论任务 | Gemini："考核 <任务ID>" |
| 装环境、配工具 | Muse："准备环境" |
| 看整条路线 | [ROADMAP](start/ROADMAP.md)：I1 数字逻辑 → I2 总线与跨时钟域 → I3 NPU 设计 → I4 UVM 验证 → I5 后端与演示 |

## 学习过程
[journey/](journey/README.md)：时间线，理论线和实践线各自的日志、笔记和考核记录。

## 学习成果
<!-- results:start -->
| # | 做了什么 | 结论 | 在哪里 |
|---|---|---|---|
| E1 | 1×4 脉动阵列行（Verilog，AI 编写，我定规格） | 4 个定向用例通过；Yosys 通用综合 1859 个单元、227 个触发器 | [systolic-mac-1x4](https://github.com/lingquan11/systolic-mac-1x4) |
| E2 | 2×2 输出驻留阵列 SKY130 后端全流程（AI 执行） | 产出 GDS，DRC 0 违例、LVS 一致；布线后 setup −0.25 ns（10 ns 目标）未收敛 | [systolic2x2-asic-backend](https://github.com/lingquan11/systolic2x2-asic-backend) |
<!-- results:end -->

详见 [results/](results/README.md)。相关仓库：[cpp-matmul-performance](https://github.com/lingquan11/cpp-matmul-performance)（CPU 矩阵乘法）· [AI-Infra-Learning](https://github.com/lingquan11/AI-Infra-Learning)（CUDA 路线）
