# 📋 EWMBA Study: Simplified Setup Steps

Here is the simplified list of actions taken to set up your **AI Adoption and Psychological Safety** survey:

---

## 🛠️ Completed Steps

1.  **Set Up Token (Authentication)**
    *   Configured the Prolific API token in the CLI configuration file (`~/.config/prolific-oss/prolific.yaml`).
    *   Ensured all credentials are safe and excluded from the public code repository.

2.  **Configured Survey Questions**
    *   Designed 9 multiple-choice questions (including 1 attention check) on AI mandates, status shifts, psychological safety, job role, and organizational seniority.
    *   Created the survey directly in **Qualtrics** using the Qualtrics API (Survey ID: `SV_cCIqbC4QNOAzqNU`), linked to your Berkeley account.

3.  **Configured Demographics & Budget**
    *   Created the study configuration file ([ai-adoption-survey.yaml](ai-adoption-survey.yaml)).
    *   **Demographics:** Targeted **full-time** workers living in the **United States (US)** aged **22 to 55** who work in the **Information Technology** or **STEM** sectors.
    *   **Budget:** Capped the reward at **$0.50** per participant and the total slots at **70 places** to keep the total cost strictly under **$50.00 USD** (70 places * $0.50 reward + 42.8% fee = $49.99).

4.  **Created Draft Study**
    *   Registered the study draft on Prolific's system, linking to your Qualtrics survey with URL parameter tracking for IDs (Study ID: `6a4b443fd87a847024e788c8`).

5.  **Committed to GitHub**
    *   Connected the workspace to the GitHub repository [Survey_EWMBA](https://github.com/alyeung/Survey_EWMBA) and pushed all configuration and documentation files to the `main` branch.

---

## 🚀 Next Steps to Launch

1.  **Top Up:** Add **$50.00 USD** to your Prolific workspace wallet.
2.  **Preview:** Click **Preview** on your Prolific Study Dashboard (at `https://app.prolific.com/researcher/studies/[STUDY_ID]`) to test the participant flow.
3.  **Publish:** Click **Publish** on the web dashboard to start collecting data from the 70 US tech/STEM participants.

---

## 💡 How Prolific Pricing Works & Fluctuates

Your budget is capped at **$50.00 USD**. To prevent unexpected pricing increases:

1.  **Estimated vs. Actual Completion Time (Underpaying Studies):**
    *   If participants take longer to complete the survey than the estimated 3 minutes, Prolific will flag it as underpaying.
    *   You will be required to issue retroactive adjustments, which could push the total cost over $50.00. 
    *   *Tip:* Keep the questions clear and concise to ensure participants finish within the 3-minute target.
2.  **Platform Fees:** 
    *   Prolific adds a fee of **42.8%** (corporate) or **33.3%** (academic/non-profit) on top of the participant rewards. 
3.  **VAT & Currency:**
    *   UK/EU billing adds **20% VAT** on the service fee portion. Setting a US billing address (e.g. UC Berkeley) avoids this.
