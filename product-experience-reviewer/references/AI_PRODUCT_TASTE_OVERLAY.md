---
title: AI Product Taste Overlay
document_id: AI_PRODUCT_TASTE_OVERLAY
additive_to: PRODUCT_EXPERIENCE_REVIEWER_CORE
version: 1.0.0
status: pilot-baseline
effective_date: 2026-08-03
language: zh-CN
---

# AI Product Taste Overlay

> 本文件**仅追加**产品品味维度。它不覆盖、不弱化、不替换
> `PRODUCT_EXPERIENCE_REVIEWER_CORE.md` 中的任何方法、证据纪律或裁决。
> 任何与 Core 冲突的解读，**以 Core 为准**。

适用范围：

- KnowMe / 灵犀；
- Copilot App；
- 灵犀演示 / Lingxi Presentation；
- AOG AI 知识库；
- 后续纳入 KnowMe 生态的 AI 产品。

---

## 0. 与 Core 的关系

- 本 Overlay 的权威性低于项目 Profile 与 Core。冲突顺序为：
  `项目 Profile → Core → 本 Overlay`。
- 不得借助 Overlay 引入会降低证据门槛、放宽 P0 触发条件或改变四类
  裁决集合的“品味”主张。
- 任何品味打分不得代替 Core §13 的问题分级；P0 仍然一票否决。

---

## 1. 品味不是装饰，是产品决策

产品品味是评审 AI 产品时的一类独立判断维度。它关注：

- 用户是否在 **30 秒内** 感受到产品的核心承诺；
- 关键交互是否让人 **愿意再点一次**，而不是 “能用但不想用”；
- AI 输出是否真正 **融入工作流**，而不是悬浮在外的聊天框；
- 文案、视觉、节奏是否传达出 **一致的产品人格**。

它**不**关心：

- 代码是否“优雅”；
- 模型是否最新；
- 功能数量；
- 营销话术；
- 任何不能用 30 秒演示回答“为什么更好”的维度。

---

## 2. 品味评估的硬约束

- 品味打分 1–5 分，规则与 Core §12 完全一致；
- 品味必须挂在 Runtime 上；原型 / fixture / mock 不得计入 Runtime 总分；
- 品味不得让 P0 通过；任一 P0 存在时，任何高品味评分都不得抬高裁决；
- “品味不错”必须绑定可截图 / 可录屏的真实交互，不得只凭主观判断；
- AI 评审官不得声称代表真实人类的情感认同；品味由事实证据支撑。

---

## 3. 核心品味维度（Core 上叠加项，不替换）

下列维度与项目 Profile 维度**叠加**使用。删除任何一项都需要 Owner
明确批准，并在 Profile 中记录。

### D1. 首屏承诺密度（First-screen promise density）

用户在没有任何操作前能否读出 “这是什么、为谁、下一步是什么”。
评判关键：是否把三件事 **同时** 显式暴露给用户，而不是藏在二级页面。

证据要求：首屏截图 + 30 秒无操作录屏。

### D2. 关键交互的可触发感（Action affordance）

主要 CTA 是否 **一眼可点**，且不依赖颜色 / 位置 / 提示符单一通道。
评判关键：键盘可达、屏读可达、不依赖鼠标悬停。

证据要求：键盘路径 + 焦点轨迹截图。

### D3. AI 输出与工作流的融合度（AI in the workflow）

AI 输出是否 **直接进入** 用户的下一步工作对象（笔记 / Todo / 日程 /
计划 / MOC），还是停留在 “聊天回复” 中。

证据要求：转化路径录屏 + 转化后的对象截图。

### D4. 诚实密度（Honesty density）

失败 / 未知 / 部分可用的状态是否被诚实暴露，而不是涂成绿色成功。
评判关键：`UNKNOWN` / `OUT_OF_CURRENT_SCOPE` / `AMBIGUOUS_SCOPE` 是否
有视觉上的真实身份，不被伪装。

证据要求：失败态 + 不确定态并排截图。

### D5. 产品人格一致性（Persona consistency）

文案、节奏、视觉密度、错误信息是否 **像同一个产品在说话**。
评判关键：跨页面 / 跨错误的语气与措辞是否一致。

证据要求：跨页面对比截图 + 错误信息采样。

### D6. 持续使用阻力预测（Predicted continued-use friction）

把 “长期使用意愿” 显式改写为 “预测持续使用阻力”。
评判关键：完成核心任务后，用户是否愿意再回来，而不是 “能用完就关”。

证据要求：完成核心任务后的 30 秒观察 + 引导回流入口截图。

---

## 4. 品味 P0 / P1 / P2

品味等级是 Core §13 的**子集**，不是平行体系：

- **品味 P0**：核心承诺在 30 秒内被产品 **反向** 表达（用户感受到 “这不是
  我以为的产品”），或 AI 输出对用户造成可见的人格 / 价值冲突。
- **品味 P1**：核心交互存在但用户无法感受到；D3 失败但功能在；
  诚实密度被伪装但未达 P0。
- **品味 P2**：节奏、文案、视觉层级一致性缺陷。
- **品味 P3**：微调，不影响当前核心承诺。

品味 P0 / P1 必须使用 Core §14 的 issue-contract 模板，不允许简写。

---

## 5. 评审流程中的 Overlay 触发点

1. **Owner Decision Brief**：在 Core §16 之后，叠加一行 “核心品味维度总
   分 / 6” 与 “最高品味项 / 最低品味项”。
2. **Runtime 评分**：与 Profile 维度 **并列**，不替换。
3. **四类裁决**：不增加新裁决，但 **D3 失败必须把 Product Experience
   Verdict 限制为 `READY_WITH_MANDATORY_FIXES` 或更严**，无论其他维度
   多亮。
4. **Human Owner Gate**：Core §17 不变；Overlay 不替 Owner 决策。

---

## 6. 禁止项

- ❌ 用品味掩盖 P0；
- ❌ 用 “整体有品味” 抵消 “关键交互失败”；
- ❌ 在 Overlay 中放宽 Core §10 的证据纪律；
- ❌ 在 Overlay 中引入 “印象分”、“个人偏好”、“美学直觉” 之类无证据
  通道；
- ❌ 把品味打分当作放行 MVP / Phase 1 / Release 的独立依据。

---

## 7. 版本与同步

- 本 Overlay 的升级规则与 Core §21.4 完全一致；
- 项目仓库可镜像 `docs/acceptance/AI_PRODUCT_TASTE_OVERLAY.md`，但不得
  在项目仓库内修改；
- Profile 必须记录引用的 Overlay 版本；
- 报告必须记录本轮使用的 Overlay 版本。

— end of overlay —
