# I1-T02 组合逻辑与 Verilog

- **线**：理论 | **计划用时**：6h | **前置**：I1-T01 | **依赖环境**：无（HDLBits 在浏览器里做）
- **一句话目标**：理解组合电路和 Verilog 的建模方式，能解释一段 Verilog 综合后会变成什么硬件（实践线 I1-P02 据此动手）

## 材料（一手来源）
- ETH DDCA Spring 2026 L2、L3（组合逻辑）、L5（Verilog）讲义：https://safari.ethz.ch/ddca/spring2026/doku.php?id=schedule ；视频：https://www.youtube.com/playlist?list=PL5Q2soXY2Zi9Eo29LMgKVcaydS7V1zZW3
- Harris & Harris, *Digital Design and Computer Architecture: RISC-V Edition*，第 2 章（组合逻辑）、第 4 章（HDL）、第 5.2 节（加法器）
- HDLBits：https://hdlbits.01xz.net/wiki/Problem_sets
- 导读：R-I1-02、R-I1-03（做前），R-I1-04（卡住时），见 [reading-map](../../../reading-map.md)
- ETH Optional HW1（2025）及官方答案：https://safari.ethz.ch/ddca/spring2025/lib/exe/fetch.php?media=optional_hw1_2025.pdf 、https://safari.ethz.ch/ddca/spring2025/lib/exe/fetch.php?media=optional_hw1_2025_solution.pdf

## 步骤
1. 【me】看 L2、L3、L5，读教材对应章节（诊断中已满分的部分可以快速过）。
2. 【me】HDLBits：完成 Getting Started、Verilog Language（Basics、Vectors、Modules: Hierarchy、Procedures、More Verilog Features）和 Circuits → Combinational Logic（Basic Gates、Multiplexers、Arithmetic Circuits、Karnaugh Map to Circuit）。每节完成后截图，存入 `journey/theory/exercises/hdlbits/`。
3. 【me】**闭卷**做 ETH HW1 第 1–9 题，拍照存入 `journey/theory/exercises/ddca-hw/`，再对照官方答案逐题自评（0 / 1 / 2），错题写一行原因。

## 所有权
- `[me]`：HDLBits 作答、HW1 作答与自评
- GPT 只做讲解和提示（按提示梯度），不提供 HDLBits 和 HW1 的答案

## 机器验收（开工前写死，AI 不得修改）
- [ ] `journey/theory/exercises/hdlbits/` 中有第 2 步列出的全部小节的完成截图
- [ ] HW1 第 1–9 题的闭卷作答照片和逐题自评已入库

## 闭卷要点（Gemini 据此出题）
- 补码加法的溢出怎么判断？无符号进位和有符号溢出有什么区别？
- 组合 `always` 块中漏写一个分支会发生什么？怎样从代码上避免锁存器？
- `assign` 和 `always @(*)` 各适合写什么？组合逻辑里该用阻塞还是非阻塞赋值，为什么？
- 4 位行波进位加法器的关键路径经过哪些门？位宽翻倍后延迟怎么变？
- 现场题：给一个新的布尔函数，化简并写出 Verilog，再说明需要多少组测试才能穷举

## 卡住时
- HDLBits 某题超过 30 分钟：允许看讲义例子，不看题解；仍然不会就记下题号，第二天重做。
- 总用时超过 9h：HW1 只做第 6–9 题（MUX 和 Verilog），在日志中写明。
