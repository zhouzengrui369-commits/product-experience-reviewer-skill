# Project Profile Template

> 路径约定（可被项目覆盖）：
> `docs/acceptance/PRODUCT_EXPERIENCE_PROFILE.md`
> 镜像 Core：`docs/acceptance/PRODUCT_EXPERIENCE_REVIEWER_CORE.md`
> 引用版本必须在文件 frontmatter 中固定。

---

## Frontmatter

```yaml
---
title: <Project> Product Experience Profile
document_id: <PROJECT>_PRODUCT_EXPERIENCE_PROFILE
referenced_core: PRODUCT_EXPERIENCE_REVIEWER_CORE
referenced_core_version: 1.0.0
referenced_overlay: AI_PRODUCT_TASTE_OVERLAY  # optional
referenced_overlay_version: 1.0.0            # optional
status: pilot-baseline
effective_date: YYYY-MM-DD
---
```

---

## 1. 核心产品承诺

> 用一段不超过 120 字的话写清楚：**这个产品是什么、为谁、解决什么
> 真实困境**。
> 不得写 “提供一站式 AI 解决方案” 这类无承诺口号。
> 不得引入 Profile 中没承诺的能力。

## 2. 目标用户视角

> 给出 1 个 Blind User Reviewer 必须扮演的具体角色。包含：
> - 身份（职业 / 阶段）；
> - 拥有的资料 / 笔记 / 决策类型（不暴露具体答案）；
> - 真实任务（不暴露预期答案）；
> - 安全边界（不得访问的真实数据 / 系统）。

## 3. 项目专项用户旅程

> 把 Core §11 的 8 类骨架映射到本项目。
> 每条旅程至少包含：
> - 旅程名（C1, C2, …）；
> - 入口 / 触发；
> - 期望用户感受到的状态；
> - 失败 / 边界；
> - 是否在当前 Release Scope 内。

## 4. 项目专项评分维度

> Core §12 维度之外，本项目**额外**关注的维度。
> 维度必须可引用证据、可截图、可演示。
> 引用 Overlay 时，必须明确叠加 D1–D6 中使用哪些。

## 5. 项目专项阻塞条件

> 在 Core §15.1 / §15.2 之外，**只增不减**的领域专属阻塞：
> `BLOCKED_<DOMAIN>_<REASON>`。
> 每条必须给出：触发条件、影响范围、解除条件。

## 6. Owner Human Gate

> Core §17 要求 10 分钟脚本。本节必须给出 **本项目** 的脚本步骤
> （导入什么资料 / 提什么问题 / 检查什么来源 / 如何转化为下一步行动
> / 退出生效条件）。
> AI 输出固定为 `HUMAN_OWNER_GATE_REQUIRED`。

## 7. 报告路径

> 必须遵循 Core §20：
> `reports/product-review/YYYY-MM-DD-<project>-product-experience-review.md`
> `reports/product-review/YYYY-MM-DD-<project>-focused-retest.md`
> `reports/product-review/YYYY-MM-DD-<project>/evidence/`

## 8. 启动指令（本轮）

```text
本轮模式：FOCUSED_RETEST 或 FULL_EXPERIENCE_REVIEW
本轮候选：<branch / commit / package / deployment>
本轮优先问题：<issue ids>
```

— end of profile template —