# 📋 EWMBA Study Workspace: Steps Completed & Next Steps

This document provides a comprehensive, high-level summary of the steps completed in your workspace and the action items remaining to deploy your **AI-nization and Psychological Safety** survey within your budget.

---

## 🛠️ Part 1: Steps Completed in this Workspace

### 1. Repository Setup & Git Version Control
*   **Action:** Git was initialized in the workspace directory.
*   **Result:** The code was connected to the GitHub repository [Survey_EWMBA](https://github.com/alyeung/Survey_EWMBA) on branch `main`.
*   **Files Tracked:**
    *   [README.md](file:///Users/allanyeung/Documents/June%2017%20prolific/README.md) - Homepage explaining the EWMBA study focus.
    *   [survey_questions_plan.md](file:///Users/allanyeung/Documents/June%2017%20prolific/survey_questions_plan.md) - Class notes survey questions.
    *   [ai_survey_plan.md](file:///Users/allanyeung/Documents/June%2017%20prolific/ai_survey_plan.md) - Original deployment steps (Google Forms track).
    *   [prolific_survey_demo.md](file:///Users/allanyeung/Documents/June%2017%20prolific/prolific_survey_demo.md) - Visual mock survey interface for class demo.
    *   [ai-nization-survey.yaml](file:///Users/allanyeung/Documents/June%2017%20prolific/ai-nization-survey.yaml) - Prolific CLI study configuration.

### 2. Formulated Survey Questions from Class Notes
*   **Action:** Extracted core themes from class discussion notes ([Managing People in Global Context.md](file:///Users/allanyeung/Documents/June%2017%20prolific/Managing%20People%20in%20Global%20Context.md)) such as "Englishnization" at Rakuten, customized vs. universal mandates, status shift dynamics, and psychological safety.
*   **Result:** Created [survey_questions_plan.md](file:///Users/allanyeung/Documents/June%2017%20prolific/survey_questions_plan.md) defining 4 study tracks.

### 3. Migrated to Native Prolific Survey Builder (Fixing 404s)
*   **Action:** Removed reliance on external redirect URLs (Google Forms / Typeform) and switched to Prolific's native Survey Builder to avoid 404 issues.
*   **Constraints Handled:** Adjusted the open-ended question (Q5) to a multiple-choice question because Prolific's native survey API currently only supports `single` (single-select) and `multiple` (multi-select) questions (free-text inputs are rejected by the API).
*   **Result:** Successfully created a native Prolific survey.
    *   **Native Survey ID:** `6a33219cffd7624bc7caf738`
    *   **Public Survey Demo UI:** Committed a readable representation of the participant experience to [prolific_survey_demo.md](file:///Users/allanyeung/Documents/June%2017%20prolific/prolific_survey_demo.md) for class presentations.

### 4. Configured Study YAML with Filters & Budget
*   **Action:** Created and edited [ai-nization-survey.yaml](file:///Users/allanyeung/Documents/June%2017%20prolific/ai-nization-survey.yaml) to target knowledge workers in the US, UK, and Australia.
*   **Targeting Filters Added:**
    *   **Country:** United Kingdom, United States, and Australia.
    *   **Employment Status:** Full-Time and Part-Time workers.
*   **Budget Optimization:**
    *   Estimated Completion Time: 3 minutes.
    *   Reward: $0.50 USD / £0.40 GBP per participant.
    *   Total Places: capped at **56 places** to ensure the total cost remains strictly under **$50.00 USD** (approx. £40.00 GBP, accounting for fees).

### 5. Created Draft Study on Prolific
*   **Action:** Executed API requests via the Prolific CLI to create the study in Draft mode.
    *   **Draft Study ID:** `6a331dff05850bc0afd54ffc`
    *   **Workspace ID:** `6a331d437473ed5c6b3b0623`
    *   **Project ID:** `6a331d437473ed5c6b3b0627`
*   **Result:** The study configuration is fully linked to the native survey and ready for preview.

### 6. Secured Credentials
*   **Action:** Scanned code base and redacted the old revoked Prolific API token (`GXBtYQ...`) from all documentation files and Git commits. Cleaned up untracked local guides ([free_survey_plan.md](file:///Users/allanyeung/Documents/June%2017%20prolific/free_survey_plan.md)).

---

## 🚀 Part 2: Next Steps to Complete the Study Launch

To get the study fully live and gather real participant data, follow these steps:

### Step 1: Change Workspace Billing Address (Optional, for USD billing)
Prolific billing default to British Pounds (GBP) and applies UK VAT unless your workspace is set to a US address.
1.  Log in to [Prolific Researcher Portal](https://app.prolific.com/).
2.  Go to **Workspace Settings** -> **Organisation**.
3.  Enter a US billing address (e.g., your UC Berkeley address). This will convert the currency settings of the workspace to USD.

### Step 2: Add Funds
1.  In the Prolific Researcher Portal, navigate to the **Finance** tab of the workspace.
2.  Click **Top Up** and add **$50.00 USD** to the wallet using a credit/debit card.

### Step 3: Run the Free Preview Test
Before publishing, simulate a free participant test:
1.  Open the study draft in your browser:  
    [https://app.prolific.com/researcher/studies/6a331dff05850bc0afd54ffc](https://app.prolific.com/researcher/studies/6a331dff05850bc0afd54ffc)
2.  Click **Preview** (or run `prolific study test 6a331dff05850bc0afd54ffc` in your CLI) to generate a test link.
3.  Navigate through the 5 multiple-choice questions to confirm the participant flow and ensure that it redirects correctly to the final screen with the completion code `AI_VAL_2026`.

### Step 4: Publish the Study
Once tested and funded:
1.  On the web dashboard, click **Publish**.
2.  *Alternative CLI command:*
    ```bash
    prolific study create -t ai-nization-survey.yaml --publish
    ```

### Step 5: Monitor & Export Submissions
Monitor active completions in real time:
```bash
# List studies and check completion count
prolific study list

# View and download participant submissions
prolific submission list --study-id 6a331dff05850bc0afd54ffc
```
Once completed, download the CSV data file directly from the Prolific dashboard to generate charts for your final class presentation.
