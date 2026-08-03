#!/usr/bin/env python3
"""validate_skill.py — deterministic read-only validator for the
product-experience-reviewer Skill.

Standard library only.

Usage:
  python3 scripts/validate_skill.py [--root <skill_root>] [--report <report.md>]

Exit codes:
  0 — PASS
  1 — FAIL (skill structure or content)
  2 — FAIL (report contract)

The Core copy under
    <skill_root>/product-experience-reviewer/references/PRODUCT_EXPERIENCE_REVIEWER_CORE.md
is treated as the authoritative copy of the Core that this Skill ships.
Run mode --report additionally validates a generated review report for the
required sections.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


SKILL_NAME = "product-experience-reviewer"
EXPECTED_CORE_SHA256 = "041a475d8cbc3404ed1e6df66c52377aecfcd631721d18a0ec9de59783f2b676"

REQUIRED_TOP_LEVEL = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "PROJECT_STATUS.md",
    "TODO.md",
    "DECISIONS.md",
    "docs/ARCHITECTURE.md",
    ".github/workflows/validate.yml",
    ".gitattributes",
    "product-experience-reviewer/SKILL.md",
    "product-experience-reviewer/agents/openai.yaml",
    "product-experience-reviewer/references/PRODUCT_EXPERIENCE_REVIEWER_CORE.md",
    "product-experience-reviewer/references/AI_PRODUCT_TASTE_OVERLAY.md",
    "product-experience-reviewer/scripts/validate_skill.py",
    "product-experience-reviewer/templates/project-profile.md",
    "product-experience-reviewer/templates/blind-brief.md",
    "product-experience-reviewer/templates/frozen-output.md",
    "product-experience-reviewer/templates/candidate-identity.md",
    "product-experience-reviewer/templates/full-review.md",
    "product-experience-reviewer/templates/focused-retest.md",
    "product-experience-reviewer/templates/issue-contract.md",
    "product-experience-reviewer/templates/evidence-manifest.md",
    "product-experience-reviewer/templates/developer-fix-contract.md",
    "product-experience-reviewer/templates/runtime-journey.md",
]

REQUIRED_FRONTMATTER_FIELDS = {"name", "description"}

# Forbidden in distributable Skill files (would force a fail). These are
# loaded from REPO secrets patterns but only checked when --strict-secrets
# is passed; default mode checks only obvious high-risk markers.
OBVIOUS_SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),                       # AWS access key id
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),                   # GitHub PAT (new format)
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),           # GitHub PAT (fine-grained)
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),           # Slack token
    re.compile(r"AIza[0-9A-Za-z\-_]{35}"),                # Google API key
    re.compile(r"sk-[A-Za-z0-9]{20,}"),                    # OpenAI / many LLM keys
]

# These absolute paths are forbidden in shipped Skill files (Core mirror,
# templates, references). They are allowed only in the task receipts under
# tasks/<date>-<task>/**.
TASK_RECEIPT_ALLOW_PREFIXES = ("tasks/", ".git/")
PRIVATE_PATH_PATTERNS = [
    re.compile(r"/" + r"Users/[A-Za-z0-9._-]+/"),
    re.compile(r"/" + r"private/tmp/[^/]+/"),  # owner-only tmp worktrees
    re.compile(r"/" + r"home/[A-Za-z0-9._-]+/"),
]


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Minimal YAML frontmatter parser (key: value). Does not handle nested
    YAML on purpose; the validator only needs scalar key/value pairs."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    block = text[4:end]
    out: dict[str, str] = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            return None
        k, v = line.split(":", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def collect_markdown_links(text: str) -> list[str]:
    """Return relative paths used in markdown links/images (best-effort)."""
    out: list[str] = []
    for m in re.finditer(r"\]\(([^)]+)\)", text):
        target = m.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        out.append(target.split("#", 1)[0].split("?", 1)[0])
    return out


def collect_inline_paths(text: str) -> list[str]:
    """Return Skill-owned relative paths written as inline code."""
    return [
        m.group(1)
        for m in re.finditer(
            r"`((?:templates|references|scripts|agents)/[^`]+)`", text
        )
    ]


def check_skill(root: Path) -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED_TOP_LEVEL:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")

    sk = root / "product-experience-reviewer" / "SKILL.md"
    if sk.is_file():
        text = sk.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append("SKILL.md frontmatter missing or unparsable")
        else:
            for k in REQUIRED_FRONTMATTER_FIELDS:
                if k not in fm:
                    errors.append(f"SKILL.md frontmatter missing field: {k}")
            if fm.get("name") != SKILL_NAME:
                errors.append(
                    f"SKILL.md frontmatter name must equal '{SKILL_NAME}', got {fm.get('name')!r}"
                )
        for link in collect_markdown_links(text) + collect_inline_paths(text):
            if link.startswith(("templates/", "references/", "scripts/", "agents/")):
                if not (sk.parent / link).exists():
                    errors.append(f"SKILL.md references missing file: {link}")

    # Core presence + non-empty
    core = root / "product-experience-reviewer" / "references" / "PRODUCT_EXPERIENCE_REVIEWER_CORE.md"
    if core.is_file():
        ctext = core.read_text(encoding="utf-8")
        if "PRODUCT_EXPERIENCE_REVIEWER_CORE" not in ctext:
            errors.append("Core copy does not self-identify as PRODUCT_EXPERIENCE_REVIEWER_CORE")
        if "Human Owner Gate" not in ctext:
            errors.append("Core copy missing 'Human Owner Gate' section")
        actual_core_sha = sha256_file(core)
        if actual_core_sha != EXPECTED_CORE_SHA256:
            errors.append(
                "Core SHA-256 mismatch: "
                f"expected {EXPECTED_CORE_SHA256}, got {actual_core_sha}"
            )

    # Overlay presence + non-empty + non-overriding Core
    overlay = root / "product-experience-reviewer" / "references" / "AI_PRODUCT_TASTE_OVERLAY.md"
    if overlay.is_file():
        otext = overlay.read_text(encoding="utf-8")
        if "AI_PRODUCT_TASTE_OVERLAY" not in otext:
            errors.append("Overlay copy does not self-identify")
        if "Core" not in otext:
            errors.append("Overlay must reference the Core")
        if "不覆盖" not in otext and "不得覆盖" not in otext and "do not override" not in otext.lower():
            errors.append("Overlay must explicitly disclaim overriding the Core")

    # Agent YAML parse
    ay = root / "product-experience-reviewer" / "agents" / "openai.yaml"
    if ay.is_file():
        atext = ay.read_text(encoding="utf-8")
        if "display_name" not in atext:
            errors.append("agents/openai.yaml missing display_name")
        if "default_prompt" not in atext:
            errors.append("agents/openai.yaml missing default_prompt")

    # Templates presence + minimal anchor
    templates = root / "product-experience-reviewer" / "templates"
    if templates.is_dir():
        for t in templates.glob("*.md"):
            ttext = t.read_text(encoding="utf-8")
            if not ttext.strip():
                errors.append(f"template is empty: {t.name}")

    # Secret / private-path scan in distributable Skill files (not receipts).
    scan_root = root
    if scan_root.exists():
        for f in scan_root.rglob("*"):
            if not f.is_file():
                continue
            rel = str(f.relative_to(root))
            if any(rel.startswith(p) for p in TASK_RECEIPT_ALLOW_PREFIXES):
                continue
            try:
                data = f.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for pat in OBVIOUS_SECRET_PATTERNS:
                if pat.search(data):
                    errors.append(f"obvious secret pattern matched in {rel} (rule: {pat.pattern})")
            for pat in PRIVATE_PATH_PATTERNS:
                m = pat.search(data)
                if m:
                    errors.append(
                        f"private absolute path in distributable file {rel}: {m.group(0)}"
                    )

    return errors


def check_report(report: Path, expected_core_sha: str | None) -> list[str]:
    errors: list[str] = []
    text = report.read_text(encoding="utf-8")
    required_sections = [
        "Owner Decision Brief",
        "Product Experience Verdict",
        "Release Evidence Verdict",
        "Prototype Concept Verdict",
        "Prototype-to-Runtime Parity",
        "Issue",
        "Evidence",
        "Human Owner Gate",
    ]
    for s in required_sections:
        if s not in text:
            errors.append(f"report missing required section: {s}")
    if "HUMAN_OWNER_GATE" not in text and "P0" not in text:
        errors.append("report missing P0 / HUMAN_OWNER_GATE signal")
    if expected_core_sha:
        m = re.search(r"core[_-]?sha256\s*[:=]\s*([0-9a-fA-F]{64})", text)
        if not m:
            errors.append("report does not pin Core SHA-256")
        elif m.group(1).lower() != expected_core_sha.lower():
            errors.append("report pinned Core SHA-256 does not match Skill's Core copy")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=".", help="Skill repo root")
    ap.add_argument("--report", help="Optional review report to validate")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    errors = check_skill(root)
    if errors:
        print("FAIL — skill structure / content errors:")
        for e in errors:
            print(f"  - {e}")
        if any("secret pattern" in e or "private absolute path" in e for e in errors):
            return 4
        if any("Core SHA-256 mismatch" in e for e in errors):
            return 3
        return 1

    core = root / "product-experience-reviewer" / "references" / "PRODUCT_EXPERIENCE_REVIEWER_CORE.md"
    core_sha = sha256_file(core) if core.is_file() else None
    if core_sha:
        print(f"core_sha256={core_sha}")

    if args.report:
        report_path = Path(args.report)
        if not report_path.is_file():
            print(f"FAIL — report not found: {args.report}")
            return 2
        rerrs = check_report(report_path, core_sha)
        if rerrs:
            print("FAIL — report contract errors:")
            for e in rerrs:
                print(f"  - {e}")
            return 2
        print(f"report_ok={args.report}")

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
