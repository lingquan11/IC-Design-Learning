# 学习资源目录

按任务需要选用，不要求通读或重复完成大学课程。公开页面和内容范围于 2026-11-08 通过检索原始页面核对；“免费、注册”指所列公开材料，证书、教材、在线作业和第三方视频可能另有条件。标注“待核实”的条件须在实际使用时确认；外部链接可变，失效时记录并寻找原发布者的新地址。学习记录引用来源，不直接复制受版权限制的材料。

## 主要课程与参考资料

| 名称与官方链接 | 阶段及推荐范围 / 用途 | 推荐理由 | 免费 | 注册 | 注意事项 |
|---|---|---|---|---|---|
| [MIT 6.004 Computation Structures（2009）](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2009/) | S01 选 MOS、逻辑门、组合/时序电路、FSM；S03 再选处理器部分 | 从器件到数字系统，配题目 | 公开课资料免费 | 浏览无需 | 旧课程，使用教学 ISA；不等同于 RISC-V，也不要求全修 |
| [MIT 6.002 Circuits and Electronics（2007）](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) | 模拟支线：按学校课程补电阻网络、MOS、RC、基本放大器和频率响应 | 含电路、器件与习题 | 公开课资料免费 | 浏览无需 | 旧版基础课，不代表现代 IC 完整教材；指定纸质教材可能需购买 |
| [HDLBits](https://hdlbits.01xz.net/wiki/Main_Page) | S01 按缺口选择门电路、组合、触发器、FSM 和 testbench 题 | 小题有仿真反馈，便于诊断 | 是 | 练习无需；跨浏览器保存进度需账户 | 判题通过只覆盖站点测试；仍要自己设计本地测试 |
| [IEEE SSCS The Beauty of Circuits](https://sscs.ieee.org/education/sscs-video-series/the-beauty-of-circuits/) | S01 模拟/CMOS 直觉补充；按问题选视频 | 电路直观解释 | 页面公开；视频具体条件待核实 | 页面无需；视频平台条件待核实 | 非必修整套课程，不替代电路分析和练习 |
| [MIT 18.06 Linear Algebra（2010）](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) | 数学支线：仅对诊断出的矩阵乘法、线性方程和向量空间缺口补学 | 与矩阵计算、数据映射直接相关 | 公开课资料免费 | 浏览无需 | 先以本校课程为主；指定教材可能另购 |
| [CMU CS:APP Labs](https://csapp.cs.cmu.edu/2e/labs.html) | S02 看 Performance Lab 与 Cache Lab；S03 缓存模拟 | 从可执行实验理解局部性 | 公开自学材料免费 | 浏览无需 | 页面为旧版；Cache Lab 是转置而非 GEMM，要求 64 位 x86 和 Valgrind，实际环境先核对 |
| [Roofline 原论文](https://people.eecs.berkeley.edu/~kubitron/courses/cs252/handouts/papers/RooflineVyNoYellow.pdf) | S02、S04–05：算术强度、带宽和吞吐上界 | 统一描述计算与访存瓶颈 | 公开 PDF 免费 | 浏览无需 | 模型是上界而非实测，须说明流量层级、峰值和测量方法 |
| [RISC-V RV32I 官方规范](https://docs.riscv.org/reference/isa/v20240411/unpriv/rv32.html) | S03：寄存器、指令编码、算术、访存和分支 | ISA 一手依据 | 是 | 无需 | 教学 CPU 若只实现指令子集，应明确列出支持及不支持项，不能称完整兼容 |
| [Stanford CS231n 卷积笔记](https://cs231n.github.io/convolutional-networks/) | S04：卷积尺寸、参数共享、乘加量估算 | 图文直观，适合手算 | 页面免费 | 浏览无需 | 页面部分最佳实践带有历史时间背景；只作为基础概念参考 |
| [Attention Is All You Need 原论文](https://arxiv.org/abs/1706.03762) | S04：选择注意力公式、注意力头及 Transformer 结构，拆解前向计算 | Attention 和 Transformer 的原始论文 | 公开摘要及 PDF 免费 | 无需 | 原始编码器—解码器架构是历史基线，不代表所有现代模型；先掌握矩阵维度 |
| [NumPy `matmul` 文档](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) | S04：矩阵维度、广播和数值对照 | API 与边界定义权威 | 是 | 无需 | 后端可能调用优化库；不把库性能归因于个人实现 |
| [MIT 6.5940 TinyML and Efficient AI Computing](https://hanlab.mit.edu/course) | S04–05：按需选 DNN、量化、Transformer 和高效推理 | 连接模型计算与部署 | 公开页面及链接材料免费；全部作业权限待核实 | 浏览页面无需；Canvas 等待核实 | 内容按学期更新；先补矩阵和基础机器学习 |
| [MIT 6.5930 Hardware Architecture for Deep Learning](https://csg.csail.mit.edu/6.5930/info.html) | S05：加速器、建模与算法硬件协同 | 课程明确覆盖硬件与系统分析 | 公开课程信息免费；完整课件/视频待核实 | 公开页面无需；课程平台待核实 | 有体系结构和机器学习前置要求，不假定全部课堂资源公开 |
| [MIT Eyeriss 深度学习高效计算教程](https://eyeriss.mit.edu/2019_neurips_tutorial.pdf) | S05：数据搬运、复用、row-stationary 和能效 | 作者原始教程，连接工作负载与硬件 | 公开 PDF 免费 | 无需 | 2019 年资料及特定架构案例，不把 NPU 简化为阵列 |
| [Berkeley Gemmini 项目](https://github.com/ucb-bar/gemmini) | S05–07：阅读架构说明中的脉动阵列、scratchpad、DMA、控制器及系统连接 | 展示计算、存储与搬运的完整协同 | 仓库和文档公开免费 | 浏览无需 | 高级参考，基于 Chisel/Chipyard；先读架构图即可，不强制搭建完整工具链，复用时检查许可证和版本 |

## 按需使用的工具文档

| 名称与官方链接 | 阶段及推荐范围 / 用途 | 推荐理由 | 免费 | 注册 | 注意事项 |
|---|---|---|---|---|---|
| [Pro Git 官方在线书](https://git-scm.com/book/en/v2) | 按需学习仓库、提交、分支及历史 | 形成可追溯的代码和记录 | 在线免费 | 无需 | 本地练习与远程推送不同；推送前遵循用户授权 |
| [Icarus Verilog 入门](https://steveicarus.github.io/iverilog/usage/getting_started.html) | S01：用 `iverilog` 编译、`vvp` 运行 testbench | 本地仿真入门路径 | 文档免费；工具开源 | 无需 | 具体 SystemVerilog 特性支持因版本而异；编译成功不等于功能正确 |
| [GTKWave 文档](https://gtkwave.github.io/gtkwave/) | S01：查看仿真导出的波形 | 排查时序错误 | 文档免费；工具开源 | 无需 | 波形辅助定位，不替代自检与预期结果比对 |
| [Verilator 安装指南](https://verilator.org/guide/latest/install.html) | S01 后期及后续项目：lint、仿真和回归 | 提供另一套实用验证工具 | 文档免费；工具开源 | 无需 | 按操作系统及具体项目需要选择；记录版本 |
| [Yosys Synthesis starter](https://yosyshq.readthedocs.io/projects/yosys/en/latest/getting_started/example_synth.html) | S06：综合步骤、读取网表 | 可观察 RTL 到网表的转换 | 文档免费；工具开源 | 无需 | 示例针对 iCE40 FPGA；结果不能直接当作 ASIC PPA |
| [SymbiYosys 文档](https://symbiyosys.readthedocs.io/en/latest/) | 前置仿真与断言掌握后，按需学习有限范围形式验证 | 开源 Yosys 形式验证前端 | 文档免费；工具开源 | 无需 | 证明结论取决于属性、约束、验证范围和工具配置 |
| [OpenROAD 文档](https://openroad.readthedocs.io/en/latest/main/README.html) | S06：查询布局、时钟树、布线及工具模块 | 物理实现工具原始说明 | 文档免费；工具开源 | 无需 | 实践结果受 PDK、约束及配置影响，不能自动视作工业 sign-off |
| [OpenSTA 静态时序分析](https://openroad.readthedocs.io/en/latest/main/src/sta/README.html) | S06：读取网表、时钟及约束，理解 setup/hold 路径报告 | 静态时序工具官方说明 | 文档免费；工具开源 | 无需 | 结果依赖时钟、时序库、寄生参数及约束；缺失信息时不可声称签核通过 |
| [OpenLane 使用指南](https://openlane2.readthedocs.io/en/latest/usage/index.html) | S06–07：PDK、时序、布局布线和报告 | 开源物理实现流程 | 文档免费；工具开源 | 无需 | 计算资源和 PDK 条款需核对；[官方说明默认流程为等待硅验证的 beta](https://openlane2.readthedocs.io/en/stable/reference/flows.html)，教学结果不等于工业 sign-off 或实际流片 |
| [KLayout 基础手册](https://www.klayout.de/doc/manual/basic.html) | S06–07：打开并检查布局层次 | 布局可视化与测量 | 文档免费 | 无需 | 能查看版图不代表 DRC/LVS 已通过；检查所用 PDK 规则 |

资源选用与完成状态应记录在对应任务或周报中；本清单只表示资料经过检索，不表示任何课程、工具或能力已经完成。
