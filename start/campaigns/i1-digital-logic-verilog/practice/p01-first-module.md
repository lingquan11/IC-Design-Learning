# I1-P01 第一个自检模块：`mux2`

- **线**：实践 | **计划用时**：2h | **前置理论**：无（诊断第 5 题已经想过） | **依赖环境**：I1-S01
- **一句话目标**：走通"写 RTL → 写自检 testbench → 仿真 → lint → 错误注入 → 看波形"整条链路，以后每个模块都照这个流程做

## 步骤
1. 【me】写 `results/basics/mux2/mux2.v` 和 `results/basics/mux2/mux2_tb.v`：穷举 8 种输入，与独立写出的期望表比较，不一致时打印 FAIL 并 `$fatal`，全部一致时打印 PASS。
2. Muse 执行：用 Icarus 编译运行；用 `verilator --lint-only -Wall` 检查 `mux2.v`，警告要清零或写明原因。
3. 【me】错误注入：把 `mux2.v` 的选择条件改反，确认 testbench 报 FAIL；改回后再跑一次 PASS。
4. 【me】用 GTKWave 打开波形，截图存入 `results/basics/mux2/`。
5. 【ai】写一个 `results/basics/run-all.sh`（以后每个模块的 testbench 都加进去），并让仓库 CI 运行它。

## 所有权
- `[me]`：`mux2.v`、`mux2_tb.v`、错误注入
- `[ai]`：`run-all.sh`、CI 配置

## 机器验收（开工前写死，AI 不得修改）
- [ ] `mux2_tb` 输出 PASS；错误注入那次输出 FAIL（两次的终端输出写进 `results/basics/mux2/README.md`）
- [ ] `verilator --lint-only -Wall` 对 `mux2.v` 无未说明的警告
- [ ] GTKWave 截图已入库
- [ ] `bash results/basics/run-all.sh` 在 CI 中通过

## 卡住时
- 工具报错：回到 I1-S01，和 Muse 一起排查环境，不在这里硬调。
