# I1-H02 回归脚本与 CI

- **栏**：动手（Muse，按 `start/prompts/hands-on.md`） | **计划用时**：1h | **先读**：无 | **被依赖**：I1-P01 起的每个模块
- **一句话目标**：一条命令跑完所有 testbench，CI 每次提交自动跑，我和 GPT 只专注写模块

## 步骤
1. 写 `results/basics/run-all.sh`：自动发现 `results/basics/*/` 下的 `*_tb.v`，用 Icarus 编译运行；任何一个输出 FAIL 或非零退出，整体返回非零；最后打印通过数 / 总数。
2. 在 `.github/workflows/check.yml` 中安装 Icarus Verilog 并运行 `run-all.sh`（保留原有的 `progress.py --check` 步骤）。
3. 用一个临时的必然失败的 testbench 验证脚本确实会让 CI 变红，验证后删掉。

## 机器验收（开工前写死，AI 不得修改）
- [ ] 本地 `bash results/basics/run-all.sh` 能运行（还没有模块时打印 0/0 并返回 0）
- [ ] 必然失败的 testbench 让 CI 变红过一次（截图或运行链接写进 `journey/hands-on-log.md`）
- [ ] 删除临时 testbench 后 CI 为绿色

## 卡住时
- CI 中安装 Icarus 失败：改用 `apt-get install -y iverilog`，在任务卡下方注明。
