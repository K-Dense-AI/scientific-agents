#!/usr/bin/env python3
"""Validate and repair CLAUDE.md -> AGENTS.md profile symlinks."""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path

EXPECTED_TARGET = "AGENTS.md"


@dataclass
class Summary:
    agents: int = 0
    claudes: int = 0
    missing: int = 0
    non_symlink: int = 0
    wrong_target: int = 0
    broken: int = 0
    fixed: int = 0
    agents_symlink: int = 0
    messages: list[str] = field(default_factory=list)

    @property
    def violations(self) -> int:
        return (
            self.missing
            + self.non_symlink
            + self.wrong_target
            + self.broken
            + self.agents_symlink
        )


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def iter_named_files(root: Path, filename: str) -> list[Path]:
    matches: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        filenames.sort()
        if filename in filenames:
            matches.append(Path(dirpath) / filename)
    return matches


def replace_with_expected_symlink(path: Path) -> None:
    path.unlink()
    path.symlink_to(EXPECTED_TARGET)


def validate_claude(path: Path, root: Path, summary: Summary, fix: bool) -> None:
    if not path.is_symlink():
        summary.non_symlink += 1
        summary.messages.append(f"non_symlink: {rel(path, root)}")
        return

    target = os.readlink(path)
    target_path = path.parent / target
    has_sibling_agents = (path.parent / EXPECTED_TARGET).exists()
    broken = not target_path.exists()
    wrong = target != EXPECTED_TARGET

    if fix and has_sibling_agents and (wrong or broken):
        replace_with_expected_symlink(path)
        summary.fixed += 1
        summary.messages.append(f"fixed: {rel(path, root)} -> {EXPECTED_TARGET}")
        return

    if wrong:
        summary.wrong_target += 1
        summary.messages.append(f"wrong_target: {rel(path, root)} -> {target}")
    if broken:
        summary.broken += 1
        summary.messages.append(f"broken: {rel(path, root)} -> {target}")


def validate(root: Path, fix: bool) -> Summary:
    summary = Summary()
    profiles = root / "scientific-agents"
    if not profiles.is_dir():
        summary.messages.append(f"missing_scan_root: {rel(profiles, root)}")
        return summary

    agents_paths = iter_named_files(profiles, "AGENTS.md")
    claude_paths = iter_named_files(profiles, "CLAUDE.md")
    summary.agents = len(agents_paths)
    summary.claudes = len(claude_paths)

    for agents_path in agents_paths:
        if agents_path.is_symlink():
            summary.agents_symlink += 1
            summary.messages.append(f"agents_symlink: {rel(agents_path, root)}")
            continue

        claude_path = agents_path.parent / "CLAUDE.md"
        if not claude_path.exists() and not claude_path.is_symlink():
            if fix:
                claude_path.symlink_to(EXPECTED_TARGET)
                summary.claudes += 1
                summary.fixed += 1
                summary.messages.append(f"fixed: {rel(claude_path, root)} -> {EXPECTED_TARGET}")
            else:
                summary.missing += 1
                summary.messages.append(f"missing: {rel(claude_path, root)}")

    for claude_path in claude_paths:
        validate_claude(claude_path, root, summary, fix)

    return summary


def print_summary(summary: Summary) -> None:
    for message in summary.messages:
        print(message)
    print(
        "summary "
        f"agents={summary.agents} "
        f"claudes={summary.claudes} "
        f"missing={summary.missing} "
        f"non_symlink={summary.non_symlink} "
        f"wrong_target={summary.wrong_target} "
        f"broken={summary.broken} "
        f"fixed={summary.fixed} "
        f"agents_symlink={summary.agents_symlink}"
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate scientific-agents CLAUDE.md symlinks."
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Create missing CLAUDE.md symlinks and repair broken or wrong symlinks.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository or fixture root containing scientific-agents/.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    root = args.root.resolve()
    summary = validate(root, args.fix)
    print_summary(summary)
    return 1 if summary.violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
