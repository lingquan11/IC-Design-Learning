# 学习成果

<!-- results:start -->
| # | 做了什么 | 结论 | 在哪里 |
|---|---|---|---|
| E1 | 1×4 脉动阵列行（Verilog，AI 编写，我定规格） | 4 个定向用例通过；Yosys 通用综合 1859 个单元、227 个触发器 | [systolic-mac-1x4](https://github.com/lingquan11/systolic-mac-1x4) |
| E2 | 2×2 输出驻留阵列 SKY130 后端全流程（AI 执行） | 产出 GDS，DRC 0 违例、LVS 一致；布线后 setup −0.25 ns（10 ns 目标）未收敛 | [systolic2x2-asic-backend](https://github.com/lingquan11/systolic2x2-asic-backend) |
<!-- results:end -->

E1、E2 我还没有亲手重做，计划在 I3、I5 中完成。数字来自两个仓库各自的 README。

计划目录：

| 目录 | 内容 | 战役 |
|---|---|---|
| `basics/` | 组合与时序模块、INT8 MAC 单元 | I1 |
| `bus-and-cdc/` | 同步 / 异步 FIFO、APB、AXI4-Lite 从设备（含形式化证明） | I2 |
| `npu/` | LeNet INT8 加速器：spec、Python 参考模型、RTL | I3 |
| `npu/verif/` | UVM 验证环境与覆盖率 | I4 |
| `implementation/` | SKY130 后端与 FPGA 演示 | I5 |
