# I1-P02 组合模块：加法器与参数化多路选择器

- **线**：实践 | **计划用时**：4h | **前置理论**：I1-T02（组合逻辑与 Verilog） | **依赖环境**：I1-S01
- **一句话目标**：用层次化和参数化写出可复用的组合模块，并用穷举或大量随机测试证明它们是对的

## 材料
- ETH 实验 3 手册（组合电路 Verilog，这里用仿真代替上板）：https://safari.ethz.ch/ddca/spring2026/lib/exe/fetch.php?media=ddca_ss26_lab3_manual.pdf
- Harris & Harris 第 5.2 节（加法器）
- 导读：R-I1-10（做前），见 [reading-map](../../../reading-map.md)

## 步骤
1. 【me】`results/basics/adder4/`：全加器 → 由 4 个全加器例化出 4 位行波进位加法器（带进位输入和输出）。自检 testbench 穷举全部 512 种输入，期望值用 testbench 中独立的整数加法计算。
2. 【me】`results/basics/muxn/`：参数化位宽 `W`、输入个数 `N` 的 N 选 1 多路选择器。testbench 至少测两组参数（如 `W=8, N=4` 和 `W=1, N=8`），每组 ≥ 1000 组随机输入。
3. 【me】两个模块各做一次错误注入。
4. Muse 执行：`verilator --lint-only -Wall`；把两个 testbench 加进 `run-all.sh`。

## 所有权
- `[me]`：全部 RTL 和 testbench
- `[ai]`：只做讲解和提示（按提示梯度），以及把测试加进 `run-all.sh`

## 机器验收（开工前写死，AI 不得修改）
- [ ] 两个模块的 testbench 都输出 PASS，`verilator --lint-only -Wall` 无未说明的警告
- [ ] 两个模块各有一次错误注入记录（FAIL 的终端输出写进各自的 README）
- [ ] `bash results/basics/run-all.sh` 在 CI 中通过

## 卡住时
- 参数化写不出来：先写固定的 4 选 1，再改成参数化。
- 超过 6h：多路选择器只测一组参数，在 README 的"边界"中写明。
