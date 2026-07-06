# EWMBA: Managing People in a Global Context Survey

This repository contains the survey design, research questions, and Prolific deployment configuration for our global business study on **AI Adoption and Psychological Safety**.

---

## 📁 Repository Contents

*   **[survey_questions_plan.md](survey_questions_plan.md):** The complete set of academic survey questions covering all four tracks:
    1.  *Track 1:* AI Adoption & Psychological Safety (our core focus)
    2.  *Track 2:* Culturally-Aligned Incentives
    3.  *Track 3:* Unconscious Bias & Discretionary Compensation
    4.  *Track 4:* Hiring for Learnability vs. Technical Skills
*   **[ai_survey_plan.md](ai_survey_plan.md):** The step-by-step action plan to deploy and run the AI survey on the Prolific platform.
*   **[ai-adoption-survey.yaml](ai-adoption-survey.yaml):** The Prolific CLI configuration file used to programmatically register and structure the study.
*   **[hackathon_plan.md](hackathon_plan.md):** The overall strategy blueprint mapping out how MBA students and developers collaborate to rapidly validate ideas during a hackathon.

---

## 🤖 Research Focus: "AI Adoption" & Psychological Safety

This study investigates how top-down corporate mandates to adopt Generative AI tools (ChatGPT, Claude, etc.) impact employee job security, psychological safety, and team status dynamics across global organizations.

We compare:
1.  **Status Shift Dynamics:** How power shifts from experienced senior managers to younger, tech-savvy junior employees.
2.  **Universal vs. Customized Mandates:** The effectiveness of strict company-wide mandates vs. decentralized, unit-specific adoption paths.
3.  **Psychological Insecurity:** Employees' willingness to admit difficulties using AI tools without fear of looking incompetent.

---

## 🚀 How to Run the Study

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
