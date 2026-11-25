# I1-P02 第一个自检模块：`mux2`

- **栏**：编程 | **计划用时**：2h | **先读**：I1-R04（Verilog） | **依赖动手**：I1-H01（工具链就绪）
- **一句话目标**：走通"写 RTL → 写自检 testbench → 仿真 → lint → 错误注入 → 看波形"整条链路，以后每个模块都照这个流程做

## 材料
- Icarus Verilog 文档：https://steveicarus.github.io/iverilog/ ；Verilator `--lint-only` 说明：https://verilator.org/guide/latest/

## 步骤
1. 【me】写 `results/basics/mux2/mux2.v` 和 `results/basics/mux2/mux2_tb.v`：穷举 8 种输入，与独立写出的期望表比较，不一致时打印 FAIL 并 `$fatal`，全部一致时打印 PASS。
2. GPT 运行：用 Icarus 编译运行；用 `verilator --lint-only -Wall` 检查 `mux2.v`，警告要清零或写明原因。
3. 【me】错误注入：把 `mux2.v` 的选择条件改反，确认 testbench 报 FAIL；改回后再跑一次 PASS。
4. 【me】用 GTKWave 打开波形，截图存入 `results/basics/mux2/`。
5. 把 `mux2_tb` 加进 Muse 在 I1-H02 中建立的 `results/basics/run-all.sh`。

## 所有权
- `[me]`：`mux2.v`、`mux2_tb.v`、错误注入
- `[ai]`：无（回归脚本和 CI 由 Muse 在 I1-H02 中负责）

## 机器验收（开工前写死，AI 不得修改）
- [ ] `mux2_tb` 输出 PASS；错误注入那次输出 FAIL（两次的终端输出写进 `results/basics/mux2/README.md`）
- [ ] `verilator --lint-only -Wall` 对 `mux2.v` 无未说明的警告
- [ ] GTKWave 截图已入库
- [ ] `bash results/basics/run-all.sh` 包含本模块并在 CI 中通过（需要 I1-H02 完成）

## 卡住时
- 工具报错：回到 I1-H01 找 Muse 排查环境，不在这里硬调。
