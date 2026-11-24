# I1-S01 环境：HDL 工具链（与 Muse 协作）

- **类型**：环境任务（按 `start/prompts/setup.md`，只做机器验收） | **预计**：1h | **被依赖**：I1-P01 起的全部实践任务
- **可以提前做**：不必等到寒假；AI-Infra 的 C1-S01 已经装好 WSL2 的话，这里直接复用

## 官方文档
- OSS CAD Suite（YosysHQ 的二进制发行版，包含 Icarus Verilog、Verilator、Yosys、SymbiYosys、GTKWave 等）：https://github.com/YosysHQ/oss-cad-suite-build
- cocotb 安装说明：https://docs.cocotb.org/en/stable/install.html

## 步骤
1. WSL2（Ubuntu 24.04）中下载并解压 OSS CAD Suite，把 `bin/` 加入 `PATH`（或用 apt 安装 `iverilog verilator gtkwave yosys`，版本以能满足 I2 的 SymbiYosys 为准）。
2. Python 3 虚拟环境中安装 cocotb（I1 只验证能导入，I4 才正式使用）。
3. 让 GTKWave 能在 Windows 上显示（WSLg 或导出 VCD 后在 Windows 端打开）。
4. 仓库 CI（`.github/workflows/check.yml`）增加一个安装 Icarus Verilog 的步骤，为 I1-P01 的 `run-all.sh` 做准备。

## 机器验收
- [ ] `iverilog -V`、`verilator --version`、`yosys -V`、`sby --help`（或 `sby -h`）、`python -c "import cocotb; print(cocotb.__version__)"` 的输出写进 `results/hw/environment.md`
- [ ] 一个最小的 Verilog 模块（Muse 可以直接写）能用 Icarus 仿真、能用 Yosys 综合
- [ ] GTKWave 能打开一个 VCD 文件（截图）

## 卡住时
- OSS CAD Suite 在 WSL 中有问题：改用 apt 安装的 Icarus、Verilator、Yosys，SymbiYosys 留到 I2 的环境任务中再装，在 `environment.md` 中写明。
