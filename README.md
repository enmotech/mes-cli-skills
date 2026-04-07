# mes-cli-skills

AI agent skills for `mes-cli` — the command-line interface for the MES platform.

This repository is automatically synced from the `skills/` directory of `mes-cli` on every release.

## Available Skills

### `mes-cli-terminal`

Converts natural language (Chinese or English) into precise `mes` CLI commands.

**Use when you want to:**
- Login, switch accounts, or check auth status
- Report hours, query timesheets, review statistics
- Create or manage service requests (work orders)
- Query or update plans, articles, contracts
- Query dashboards or manage weekly reports
- Parse MES support URLs into structured data

**Supports:**
- Non-interactive mode — all commands are fully parameterized, no prompts
- Write-operation safety — previews commands before execution, supports `--dry-run`
- Windows → WSL cross-environment encoding handling
- Structured JSON output with key field extraction

## Usage

These skills are designed for use with any AI agents that support skills.

## Releases

Skills are versioned together with `mes-cli`.
