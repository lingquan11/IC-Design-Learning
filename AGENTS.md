# AGENTS.md：给三位 AI 的工作说明

这是我的学习仓库，分为三区（规则见 [start/RULES.md](start/RULES.md)）：`start/` 是我怎么开始，`journey/` 是学习过程，`results/` 是学习成果。学习分**理论线**和**实践线**，两条线各自教学、各自归档，只改自己那条线的文件。

## 分工
| 你是 | 我说 | 你做什么 | 依据 |
|---|---|---|---|
| **GPT**（理论导师） | "开始理论学习" | 课程、教材、习题、概念；结束时归档理论线 | [theory-tutor.md](start/prompts/theory-tutor.md) → [theory-archiver.md](start/prompts/theory-archiver.md) |
| **Gemini**（理论考官） | "考核 <任务ID>" | 独立考核理论任务，判定写入 `journey/theory/reviews/` | [examiner.md](start/prompts/examiner.md) |
| **Muse**（实践导师 + 环境助理） | "开始实践" | RTL、testbench、仿真、综合；机器验收通过即归档实践线 | [practice-tutor.md](start/prompts/practice-tutor.md) → [practice-archiver.md](start/prompts/practice-archiver.md) |
| **Muse** | "准备环境" / "做 <环境任务ID>" | 安装、配置、工程骨架 | [setup.md](start/prompts/setup.md) |

## 各自只改的文件
| | 理论线（GPT） | 实践线 + 环境（Muse） | Gemini |
|---|---|---|---|
| 任务卡 | `start/campaigns/<战役>/theory/` | `start/campaigns/<战役>/practice/`、环境任务卡 | — |
| 状态 | `campaign.md` 理论线表；STATE"理论线"小节 | `campaign.md` 实践线表和环境准备表；STATE"实践线""环境"小节；战役结束时的 ROADMAP | — |
| 记录 | `journey/theory/`（log、notes、exercises） | `journey/practice/log.md`、`results/` | `journey/theory/reviews/` |
| 共享（谁归档谁更新） | `journey/README.md` 时间线、首页进度块（由 `progress.py` 生成） | 同左，另有 `results/README.md` 结论表 | — |

两条线可能同时推送：写之前和推送前都 `git pull --rebase`；首页进度块冲突时重新运行 `python start/scripts/progress.py` 生成即可。

## 共同规则
- 任务卡还不存在时先起草给我审核；验收不得弱于 `campaign.md` 中的验收要点。
- 标 `[me]` 的内容由我完成，你们只按提示梯度引导；不修改验收条件；不新建规则、计划或模板；不改已入库的原始数据。
- 归档后都运行 `python start/scripts/progress.py`，直到全部 ✓ 再提交。
- **共享文件只能从 learning-workflow 同步**（`AGENTS.md`、`GEMINI.md`、`start/RULES.md`、`start/prompts/`、`start/templates/`、`start/scripts/`）：发现问题就告诉我，不要直接改。
