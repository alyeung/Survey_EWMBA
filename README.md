# EWMBA: Managing People in a Global Context Survey

This repository contains the survey design, research questions, and Prolific deployment configuration for our global business study on **AI Adoption and Psychological Safety**.

---

## Repository Contents & File Guide

This workspace contains all the research design, deployment scripts, and reference files for the study:

### Research & Planning Docs
*   **[survey_questions_plan.md](survey_questions_plan.md):** Defines the academic survey questions across four core research tracks inspired by your EWMBA cases:
    1.  *Track 1:* AI Adoption & Psychological Safety (our core focus).
    2.  *Track 2:* Culturally-Aligned Incentives (Juhudi/Hofstede).
    3.  *Track 3:* Unconscious Bias & Discretionary Compensation (Fivetran).
    4.  *Track 4:* Hiring for Learnability vs. Technical Skills (Infosys/InfoBeans).
*   **[Managing People in Global Context.md](Managing%20People%20in%20Global%20Context.md):** Detailed notes mapping EWMBA course concepts, case studies, and reading references that form the academic foundation of the research tracks.
*   **[prolific_survey_demo.md](prolific_survey_demo.md):** A clean participant-facing preview of how the survey questions render for respondents.

### Deployment & Integration Guides
*   **[workspace_steps_summary.md](workspace_steps_summary.md):** A simplified, step-by-step summary checklist of all actions taken to set up, secure, and validate your active survey.
*   **[ai_survey_plan.md](ai_survey_plan.md):** A step-by-step guide outlining how the study is registered and executed on the Prolific platform.
*   **[free_survey_plan.md](free_survey_plan.md):** A guide to running zero-cost integration tests using Prolific's developer sandbox.

### Automation Scripts & Configs
*   **[ai-adoption-survey.yaml](ai-adoption-survey.yaml):** The study configuration file defining target demographics, budget constraints, and redirection loops.
*   **[create_or_update_study.py](create_or_update_study.py):** A dynamic Python script that reads the YAML file, checks if a draft study is already present on Prolific, and edits/patches it (PATCH) instead of creating duplicates.

---

## Research Focus: "AI Adoption" & Psychological Safety

This study investigates how top-down corporate mandates to adopt Generative AI tools (ChatGPT, Claude, etc.) impact employee job security, psychological safety, and team status dynamics across global organizations.

We compare:
1.  **Status Shift Dynamics:** How power shifts from experienced senior managers to younger, tech-savvy junior employees.
2.  **Universal vs. Customized Mandates:** The effectiveness of strict company-wide mandates vs. decentralized, unit-specific adoption paths.
3.  **Psychological Insecurity:** Employees' willingness to admit difficulties using AI tools without fear of looking incompetent.

---

## How to Run the Study

1.  **Configure API Authentication:**
    Ensure your token is set locally or in your Prolific config file (`~/.config/prolific-oss/prolific.yaml`).
2.  **Create the Draft Study:**
    Run the following command using the Prolific CLI:
    ```bash
    prolific study create -t ai-adoption-survey.yaml
    ```
3.  **Publish the Study (with funding):**
    ```bash
    prolific study create -t ai-adoption-survey.yaml --publish
    ```
