# I1-T02 组合逻辑与 Verilog 基础

- **线**：必做 | **计划用时**：10h | **前置**：I1-T01
- **一句话目标**：能用 Verilog 写出正确的组合电路，并能解释它综合后会变成什么硬件

## 材料（一手来源）
- ETH DDCA Spring 2026 L2、L3（组合逻辑）、L5（Verilog）、L6b（验证与测试）讲义：https://safari.ethz.ch/ddca/spring2026/doku.php?id=schedule ；视频：https://www.youtube.com/playlist?list=PL5Q2soXY2Zi9Eo29LMgKVcaydS7V1zZW3
- Harris & Harris, *Digital Design and Computer Architecture: RISC-V Edition*，第 2 章（组合逻辑）、第 4 章（HDL）、第 5.2 节（加法器）
- HDLBits：https://hdlbits.01xz.net/wiki/Problem_sets
- ETH 实验 3 手册（组合电路 Verilog）：https://safari.ethz.ch/ddca/spring2026/lib/exe/fetch.php?media=ddca_ss26_lab3_manual.pdf
- ETH Optional HW1（2025）及官方答案：https://safari.ethz.ch/ddca/spring2025/lib/exe/fetch.php?media=optional_hw1_2025.pdf 、https://safari.ethz.ch/ddca/spring2025/lib/exe/fetch.php?media=optional_hw1_2025_solution.pdf

## 步骤
1. 【me】看 L2、L3、L5，读教材对应章节。
2. 【me】HDLBits：完成 Getting Started、Verilog Language（Basics、Vectors、Modules: Hierarchy、Procedures、More Verilog Features）和 Circuits → Combinational Logic（Basic Gates、Multiplexers、Arithmetic Circuits、Karnaugh Map to Circuit）。每节完成后截图进度，存入 `journey/exercises/hdlbits/`。
3. 【me】按 ETH 实验 3 的要求写组合电路，用仿真代替上板。在 `results/basics/` 中至少完成：4 位行波进位加法器（由全加器例化）、参数化位宽的 N 选 1 多路选择器。每个都配穷举（或 ≥ 1000 组随机）的自检 testbench，并做一次错误注入。
4. 【me】**闭卷**做 ETH HW1 第 1–9 题（逻辑完备性、布尔代数、组合逻辑设计、晶体管级电路、MUX、Verilog I–III），拍照存入 `journey/exercises/ddca-hw/`，再对照官方答案逐题自评（0/1/2），错题写一行原因。

## 所有权
- `[me]`：全部 RTL、testbench、HDLBits 作答、HW1 作答
- `[ai]`：只做讲解和提示（按提示梯度），不提供 HDLBits 答案

## 机器验收（开工前写死，AI 不得修改）
- [ ] `journey/exercises/hdlbits/` 中有第 2 步列出的全部小节的完成截图
- [ ] `results/basics/` 中加法器和多路选择器的 testbench 都输出 PASS，并 `verilator --lint-only -Wall` 无未说明的警告
- [ ] 两个模块各有一次错误注入记录（FAIL 的终端输出）
- [ ] HW1 第 1–9 题的闭卷作答照片和逐题自评已入库

## 闭卷要点
- 补码加法的溢出怎么判断？无符号进位和有符号溢出有什么区别？
- 在组合 `always` 块中漏写一个分支会发生什么？怎样从代码上避免锁存器？
- `assign` 和 `always @(*)` 各适合写什么？阻塞赋值和非阻塞赋值在组合逻辑里该用哪个，为什么？
- 4 位行波进位加法器的关键路径经过哪些门？位宽翻倍后延迟怎么变？
- 现场题：考官给一个新的布尔函数，要求化简并写出 Verilog，再说明需要多少组测试才能穷举

## 卡住时
- HDLBits 某题超过 30 分钟：允许看讲义例子，但不看题解；仍然不会就在 `journey/exercises/hdlbits/` 记下题号，第二天重做。
- 总用时超过 15h：HW1 只做第 6–9 题（MUX 和 Verilog），在 log 中写明。
