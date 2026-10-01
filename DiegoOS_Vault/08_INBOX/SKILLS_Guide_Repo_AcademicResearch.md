---
tags:
  - academic-workflow
  - AI-agents
  - obsidian
  - qwen
  - together-ai
  - terminal
created: 2026-06-07
status: active-guide
---
# 🎓 Workflow: Academic Research Skills via Antigravity, Codex & Together AI

## 1. Architectural Overview
This workflow utilizes the `Imbad0202/academic-research-skills` repository not as an IDE plugin, but as a **terminal-native orchestration framework**. 

*   **The Brain (LLM):** Qwen (via Together AI API) provides the high-parameter reasoning required for complex macroeconomic theory and historical data reconstruction.
*   **The Orchestrators (Agent Managers):** **Google Antigravity CLI** and **OpenAI Codex CLI** manage the agents. Antigravity natively supports "Agent Skills" (the exact structure of this repo), allowing parallel multi-agent execution.
*   **The Truth Layer (Verification):** Local Python scripts handle deterministic tasks (CrossRef/OpenAlex citation verification, data formatting) to ensure zero hallucination in bibliographies.
*   **The Knowledge Graph (Obsidian):** Your Obsidian vault acts as the physical manifestation of the repo’s "Material Passport," serving as the central state-tracker that the agents read from and write to via the GitHub repo.

---

## 2. Environment & API Configuration

Since we are bypassing local model hosting and using Together AI, we must configure the Agent Managers to route their OpenAI-compatible requests to Together's Qwen endpoints.

### A. Install Dependencies
Ensure you have the Agent Managers and Python requirements installed globally or in your virtual environment:
```bash
# Install Agent Managers (if not already installed)
npm install -g @openai/codex-cli
npm install -g @anthropic-ai/claude-code # Or the specific Antigravity installer
# Note: Antigravity CLI is typically installed via Google's official toolchain or brew.

# Clone the skills repo
git clone https://github.com/Imbad0202/academic-research-skills.git
cd academic-research-skills
pip install -r requirements-dev.txt # Installs citation verification scripts
```


### B. Configure Together AI Routing

Set the following environment variables in your `~/.zshrc` or `~/.bashrc`. Both Codex and Antigravity respect standard OpenAI-compatible environment variables for custom routing:

```bash
export TOGETHER_API_KEY="your_together_api_key_here"
export OPENAI_API_KEY="$TOGETHER_API_KEY"
export OPENAI_BASE_URL="https://api.together.xyz/v1"
export DEFAULT_MODEL="Qwen/Qwen2.5-72B-Instruct-Turbo" # Or your preferred Qwen variant
```


## 3. Obsidian & GitHub Integration (The Material Passport)

The repository relies on a "Material Passport" to prevent agents from losing context during long research sessions. We will map this directly to your Obsidian vault.

1. **Initialize the Vault as a Git Repo:** Ensure your Obsidian vault is tracked in GitHub.
2. **Create the Passport Note:** Create a new note in Obsidian named `000_MATERIAL_PASSPORT.md`.
3. **Link the Skills:** In your Obsidian settings (or via a local symlink), map the `academic-research-skills/` directory into your vault so you can visually read the `SKILL.md` files alongside your research notes.

**How it works:** When you start a session, the agents will read `000_MATERIAL_PASSPORT.md` to understand the current state of your paper (e.g., "Stage 2: Literature Review on Chilean Inequality"). As they work, they will append their findings to this note, which you can visually review in Obsidian's Graph View or Reading Mode.

---

## 4. Execution Workflows

### Phase 1: Initialization & Strategy (Using Antigravity CLI)

Antigravity is ideal for the initial setup because it excels at managing multiple parallel agents (e.g., one for literature, one for methodology).

1. Open your terminal in your Obsidian vault directory.
2. Load the `academic-pipeline` skill. Antigravity allows you to specify custom skill directories:
    
```bash
antigravity --skill-dir ./academic-research-skills/academic-pipeline
```

1. **Prompt:** _"Initialize the Material Passport. I am starting a paper on [Topic, e.g., Stock-Flow Consistent Approaches to Capital Stocks in Chile]. Read the 000_MATERIAL_PASSPORT.md file, set up the project structure, and deploy the deep-research and academic-paper agents."_
2. Antigravity will spawn sub-agents. They will populate your Obsidian vault with outline notes and strategy documents.

### Phase 2: Drafting & The Socratic Method (Using Codex CLI)

Codex CLI is highly autonomous and excellent at executing the strict "Sprint Contracts" defined in the repo's `academic-paper` skill.

1. Navigate to the specific chapter folder in your vault.
2. Load the drafting skill:

```bash
codex --custom-instructions "$(cat ../academic-research-skills/academic-paper/SKILL.md)"
```
    
3. **Prompt:** _"Execute 'Mode: Draft'. Review the Material Passport. Draft Section 2 based on the notes in this folder. Adhere strictly to the Anti-Leakage Protocol: use ONLY the provided data on Chilean economic history. Do not use your internal training data for macroeconomic statistics. Insert [CITATION_NEEDED] placeholders where appropriate."_
4. Codex will write the draft directly into a Markdown file in your Obsidian vault. You can watch it write in real-time via your terminal or switch to Obsidian to read along.

### Phase 3: Deterministic Verification (Python Scripts)

**Never trust the LLM's bibliography.** This is where your local Python scripts come in. The repo includes scripts like `scripts/crossref_verify.py` and `scripts/openalex_search.py`.

1. Once Codex finishes drafting, extract the `[CITATION_NEEDED]` placeholders or the raw reference list it generated.
2. Run the verification scripts locally in your terminal:
        
    ```bash
    python scripts/crossref_verify.py --input draft_section_2.md --output verified_references.json
    ```
        
1. The script will query the real CrossRef/Semantic Scholar APIs. It will return a JSON file flagging any "ghost" citations that Qwen hallucinated.
2. Feed the verified JSON back into the agent to update the Markdown file with real DOI links.

### Phase 4: The "Devil’s Advocate" Review (Using Antigravity)

Before finalizing, use Antigravity to run the `academic-paper-reviewer` skill.

1. Load the reviewer skill:

``` bash
antigravity --skill-dir ./academic-research-skills/academic-paper-reviewer
```


1. **Prompt:** _"Activate the Devil's Advocate agent. Read the completed draft in this folder. Pre-commit to the Sprint Contract scoring criteria. Ruthlessly critique the heterodox macroeconomic assumptions and the network analysis methodology. Output the review to 001_PEER_REVIEW.md."_
2. Open `001_PEER_REVIEW.md` in Obsidian to read the critique, then use Codex to systematically address the reviewer's points in the main draft.

## 5. Pro-Tips for Heterodox Economics Research

- **Style Calibration:** Since you publish in both English and Spanish, gather 3 of your past papers (PDFs) and place them in an `obsidian_vault/reference_style/` folder. Use the repo's `style_calibration_protocol.md` to force Qwen (via Together AI) to analyze your specific sentence structures and citation habits before it begins drafting.
- **Data Grounding:** When working with reconstructed capital stocks, create a `data_dictionary.md` in your Obsidian vault. Explicitly instruct the agents: _"You are strictly forbidden from estimating missing values in the capital stock data. If a value is missing in data_dictionary.md, output [DATA_MISSING] and halt."_
- **Context Window Management:** Qwen via Together AI has a massive context window, but the `academic-pipeline` skill is designed to chunk work. Rely on the "Material Passport" to pass context between sessions rather than feeding the entire paper into a single prompt.



***

### Why this specific stack is incredibly powerful for you:
1.  **Antigravity CLI** was explicitly designed by Google to manage "Agent Skills" and orchestrate multiple local agents in parallel. It is the spiritual successor to the exact environment the `academic-research-skills` repo was trying to emulate, but with native terminal support.
2.  **Obsidian** solves the "state-tracking" problem. Instead of the AI trying to remember what it did in a hidden JSON file, the "Material Passport" is a visible Markdown note in your vault. You maintain total visual control over the research graph.
3.  **Together AI + Qwen** gives you the 72B+ parameter reasoning required for complex economic theory, without the $2000 hardware requirement of running it locally, while keeping your data entirely within your own terminal and GitHub ecosystem.

--- 

# Website  of the Repo

https://github.com/Imbad0202/academic-research-skills/