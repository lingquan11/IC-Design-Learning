# I1-T01 入门诊断 + 仿真工具链

- **线**：必做 | **计划用时**：3h | **前置**：无
- **一句话目标**：知道自己从哪里起步；在 WSL2 里写出第一个带自检的 Verilog 模块，确认整条仿真链路能用

## 材料（一手来源）
- Icarus Verilog 文档：https://steveicarus.github.io/iverilog/
- Verilator 文档：https://verilator.org/guide/latest/
- ETH DDCA L5 讲义（HDL 与 Verilog）：https://safari.ethz.ch/ddca/spring2026/lib/exe/fetch.php?media=onur-ddca-2026-lecture5-hdl-verilog-afterlecture.pdf

## 步骤
1. 【me】**先闭卷做诊断**（下面 5 题），每题记下用时和是否求助，写进 `journey/notes/i1-diagnostic.md`。做完再展开参考答案自评。
2. 【me】在 WSL2 中安装 Icarus Verilog、Verilator、GTKWave（Ubuntu：`sudo apt install iverilog verilator gtkwave`），记录版本。
3. 【me】写 `results/basics/mux2.v` 和 `results/basics/mux2_tb.v`：穷举 8 种输入，与独立的期望表比较，不一致时打印 FAIL 并 `$fatal`，全部一致时打印 PASS。
4. 【me】用 Icarus 编译运行；用 `verilator --lint-only -Wall` 检查 `mux2.v`，警告要清零或说明原因。
5. 【me】错误注入：把 `mux2.v` 中的选择条件改反，确认 testbench 报 FAIL；改回后再跑一次 PASS。
6. 【me】用 GTKWave 打开波形，截一张图存入 `journey/notes/`。

### 诊断题（闭卷）
1. 将无符号二进制 `101101` 转成十进制和十六进制。
2. 用 8 位补码表示 −5；计算 −5 + 3 的 8 位二进制结果及其十进制值。
3. 写出两输入 XOR 的完整真值表。化简 `F = (~A & B) | (A & B) | (A & C)`，并用真值表验证。
4. 正边沿触发的 D 寄存器采用同步高有效复位。各上升沿前的输入如下，写出每个上升沿之后的 Q（第一次上升沿前 Q 未知）。

   | 上升沿 | 1 | 2 | 3 | 4 | 5 |
   |---|---:|---:|---:|---:|---:|
   | rst | 1 | 0 | 0 | 1 | 0 |
   | D | 1 | 0 | 1 | 0 | 1 |

5. 用 Verilog 写 `mux2`（`sel=0` 时 `y=a`，`sel=1` 时 `y=b`），列出全部测试输入和期望输出，并说明仿真中怎样自动发现错误。

<details>
<summary>做完后再展开参考答案</summary>

1. `101101₂ = 45₁₀ = 2D₁₆`
2. −5 = `11111011`；加 3 得 `11111110`，即 −2
3. XOR：00→0、01→1、10→1、11→0。`(~A & B) | (A & B) = B`，所以 `F = B | (A & C)`；按 ABC = 000…111，F = 0,0,1,1,0,1,1,1
4. Q 依次为 0, 0, 1, 0, 1（同步复位只在上升沿生效）
5. `assign y = sel ? b : a;`；穷举 8 组，与独立期望比较，不一致时报错并让仿真失败

</details>

**自评**：每题 0/1/2 分（0 = 不会或核心错误；1 = 思路对但不完整；2 = 闭卷做对且能解释）。得 0 或 1 的题，在 STATE 的"未解决的问题"中记下，T02/T03 会覆盖。

## 所有权
- `[me]`：诊断作答、`mux2.v`、`mux2_tb.v`
- `[ai]`：工具安装报错排查（只给建议，命令由我执行）

## 机器验收（开工前写死，AI 不得修改）
- [ ] `journey/notes/i1-diagnostic.md` 有 5 题的作答、用时、自评分数
- [ ] `iverilog -V` 和 `verilator --version` 的输出已贴进上述笔记
- [ ] `mux2_tb` 输出 PASS；错误注入那次输出 FAIL（两次的终端输出都贴进笔记）
- [ ] `verilator --lint-only -Wall` 对 `mux2.v` 无未说明的警告
- [ ] GTKWave 截图已入库

## 闭卷要点
- 不考官（诊断本身就是自评）。

## 卡住时
- 工具装不上：先用 Icarus 完成第 3–5 步，Verilator 留到 T04 之前补上，在 log 中写明。
