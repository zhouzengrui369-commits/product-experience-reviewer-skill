# Blind Brief Template (Stage A input)

> 给 Blind User Reviewer 的**唯一**信息包。
> 任何产品定位 / PRD / 路线图 / 历史报告 **不得出现**。
> 主评审官也不得在交付本包之后修改它。

---

## Brief Header

```yaml
review_mode: <FIRST_INSTALL | FULL_EXPERIENCE_REVIEW | EXPLORATORY_PRODUCT_REVIEW | FOCUSED_RETEST | RELEASE_CANDIDATE_REVIEW>
project: <project>
reviewer_role: <target user identity>
task_one_line: <single real task>
candidate_entry: <URL | path | app id>
safety_boundary:
  - <what the reviewer may not access>
  - <what data must remain synthetic>
isolation_status: <BLIND_TEST | PRIMED_COGNITIVE_WALKTHROUGH>
```

## Identity

> 1–3 句话描述 Reviewer 扮演的用户。**不包含**产品定位、版本号、
> Roadmap、上一轮报告编号。

## Candidate Entry

> 进入候选产品的入口。仅可包含：
> - URL 或路径；
> - 必要的测试账号说明（**不**包含任何凭据）；
> - 一项安全操作边界；
> - 一项不泄露产品答案的目标用户任务。

## Single Real Task

> 一句话真实任务。**不得**暗示产品应当如何回答。

## Safety Boundary

- 不得访问的资源；
- 不得上传 / 写入的真实数据；
- 出现意外副作用时的中止条件；
- 凭据 / API key / 私人笔记的处理规则。

## Output Contract (frozen-output.md)

> Reviewer 完成后必须按 `templates/frozen-output.md` 输出冻结结果，
> **不得**事后修改。

— end of blind brief —