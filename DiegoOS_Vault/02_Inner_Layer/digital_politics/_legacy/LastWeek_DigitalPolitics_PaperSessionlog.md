---
id: session_log_2026_06_02_repo_and_automation_setup
title: "Session Log: Repo Setup, Terminal Config & Lit Review Automation Protocol"
date: 2026-06-02
tags:
  - workflow
  - setup
  - together_ai
  - obsidian
  - compol_project
author: Diego Polanco
status: in_progress
---

# 🚀 Session Log: Repo Setup & Automation Protocol (June 2, 2026)

## 📋 Executive Summary
Successfully transitioned from a scattered project structure to a unified, reproducible repository. Configured a robust, cost-optimized terminal AI workflow using Together.ai (bypassing hardcoded CLI limitations) and drafted the Python automation pipeline for systematic literature review extraction into Obsidian.

---

## ✅ Completed Milestones

### 1. Repository Unification & Structure
- **Root Directory**: `C:\ReposGitHub\COMPOL_DigitalCapitalism`
- **Structure Locked**:
  - `vault/` (Obsidian vault with `00_Inbox`, `10_Literature`, `20_Project_Notes`, `30_Drafts`)
  - `data/raw` & `data/processed`
  - `literature/pdfs` & `literature/pdf_manifest.csv`
  - `src/notebooklm`, `src/analysis`, `src/utils`
  - `output/figures`, `output/tables`, `output/drafts`
  - `legacy_repo/` (Read-only reference)
- **Configuration Files**: Generated `.gitignore` (excluding large data, Obsidian workspace conflicts), `requirements.txt`, `pyproject.toml`, and `.env`.

### 2. Manifest Curation
- Updated `literature/pdf_manifest.csv` to include an `include_in_review` boolean column.
- **Excluded**: Administrative files (`FrontMatter`, `TableContents`, `EditorsContributors`, `BackMatter`, `Index`) and misplaced files (`LICHT_2022...pdf`).
- **Included**: All substantive chapters from the Fuchs & Chandler (2019) edited volume and the core empirical literature.

### 3. Terminal AI Configuration (Together.ai)
- **Problem**: The default `qwen` CLI was hardcoded to Alibaba DashScope and ignoring local JSON edits.
- **Solution**: Successfully used the internal `/auth` and `/model` commands to override the provider settings.
- **Current Config**:
  - **Base URL**: `https://api.together.ai/v1`
  - **Model**: `meta-llama/Llama-3.3-70B-Instruct-Turbo` (Best cost/performance for academic reasoning)
  - **Alternative Models Available**: `Qwen/Qwen2.5-72B-Instruct`, `Qwen/Qwen3.5-9B` (for cheap batch processing), `deepseek-ai/DeepSeek-V3`.

### 4. Automation Scripts Drafted
- **`src/utils/qwen_cli.py`**: A flexible terminal wrapper that accepts `--model` and `--system` flags, pulling credentials securely from `.env`.
- **`src/notebooklm/extract_literature.py`**: A robust pipeline that:
  1. Reads the curated `pdf_manifest.csv`.
  2. Extracts text from the first 5 pages of each PDF (to control token costs and focus on abstracts/intros).
  3. Sends the snippet to Together.ai with a strict academic prompt.
  4. Outputs a perfectly formatted Markdown file with YAML frontmatter directly into `vault/10_Literature/`.

### 5. Literature Assessment (Fuchs & Chandler, 2019)
- Analyzed the Introduction and Table of Contents.
- **Key Theoretical Hooks Identified**: "Big Data capitalism", "algorithmic knowledge", "digital labour" (unpaid user data generation), and the tension between "digital optimism" (participatory democracy) and "digital pessimism" (surveillance/exploitation).
- **Target Chapters for Extraction**: Gerbaudo (Platform Party), Dean (Communicative Capitalism), Fuchs (Beyond Big Data, Karl Marx in the Age of Big Data), and Chandler (Correlational Machine).

---

## ⏳ Pending Next Steps

- [ ] **Review Legacy Scripts**: Analyze the Python scripts in `C:\ReposGitHub\Financialization_LandRent\05_scripts` to extract any unique `notebooklmpy` logic or best practices to merge into `extract_literature.py`.
- [ ] **Vault Note Systematization**: Review pending notes in `vault/20_Project_Notes/` (Introduction, Conceptual Framework, Analytical Framework, Data Methods) to align the extraction prompt with specific research gaps.
- [ ] **Question Registry Cross-Reference**: Map the existing registry of research questions to ensure the automated literature notes explicitly answer or address them.
- [ ] **Test Run**: Execute `python src/notebooklm/extract_literature.py --model "Qwen/Qwen3.5-9B"` on a small batch (2-3 PDFs) to verify the Obsidian Markdown output format before running the full manifest.

---

## 💡 Key Learnings & Pro Tips
- **CLI Hardcoding**: Proprietary AI CLIs often aggressively overwrite local config files. Using internal CLI commands (`/auth`) combined with file read-only locks, or simply building a custom Python wrapper, is the most reliable long-term solution.
- **Token Economics**: Limiting PDF extraction to the first 5 pages (~12,000 characters) is highly effective for capturing the core argument, methodology, and key concepts without burning credits on appendices or dense literature reviews that the LLM can summarize from the intro alone.
- **Model Routing**: Use `Qwen/Qwen3.5-9B` for high-volume, simple extraction tasks, and escalate to `Llama-3.3-70B-Instruct-Turbo` or `Qwen3.5-397B` only for complex theoretical synthesis or cross-referencing.

---
> [!INFO] Metadata
> **Next Action**: Upload/paste the code from `Financialization_LandRent\05_scripts` to finalize the automation protocol.