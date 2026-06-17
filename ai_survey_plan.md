# Action Plan: AI-nization Survey Deployment

This plan outlines the exact steps, configurations, and commands needed to set up and test your **AI-nization & Psychological Safety** survey for free.

---

## 📅 Timeline & Workflow (1 Hour)

```
[00-15 Min] Set up Google Form  --->  [15-30 Min] Write YAML Config  --->  [30-45 Min] Run Free CLI Test Run
```

* **Business/MBA Leads:** Create the Google Form with the questions and write down the final URL.
* **Developer:** Save the YAML file, configure the CLI with the default profile (`akyeung@gmail.com`), and run the test script.

---

## 🛠️ Step 1: Create the Google Form (MBA Leads)

1. Go to [Google Forms](https://docs.google.com/forms/) and create a new blank form.
2. Add the **5 questions** defined in **Track 1** of [survey_questions_plan.md](file:///Users/allanyeung/Documents/June%2017%20prolific/survey_questions_plan.md).
3. **Crucial:** To track which responses correspond to which participant IDs (without asking for their real names):
   * Add a short-answer question: *"Please enter your Prolific ID:"*
   * Alternatively, Google Forms can accept URL pre-fills, but asking them to copy-paste their ID is the easiest no-code method.
4. In the settings, change the confirmation message (shown after they hit submit) to show the completion code:
   * *"Thank you for your response! Your completion code is: **AI_VAL_2026**"*
5. Click **Send** and copy the public view link (e.g. `https://docs.google.com/forms/d/e/.../viewform`).

---

## 💻 Step 2: Create the CLI Study Configuration (Developer)

Create a file named `ai-nization-survey.yaml` in your workspace `/Users/allanyeung/Documents/June 17 prolific/ai-nization-survey.yaml` with the following content:

```yaml
name: "AI-nization and Psychological Safety in Global Workplaces"
internal_name: "AI_nization_Survey"
description: "Please answer a 3-minute survey about how Generative AI tools (ChatGPT, Claude, etc.) affect your day-to-day job security and psychological safety."
# Replace this with your actual Google Form URL
external_study_url: "https://docs.google.com/forms/d/e/1FAIpQLSfpX_REPLACE_WITH_YOUR_ID/viewform"
prolific_id_option: question # We ask for their ID in a question
completion_code: "AI_VAL_2026"
completion_option: code
total_available_places: 5
estimated_completion_time: 3
reward: 50 # Reward in cents/pence (50 pence / $0.65 approx per person)
device_compatibility:
  - desktop
  - tablet
  - mobile
```

---

## 🚀 Step 3: Run the Free CLI Test Run (Developer)

To execute a free simulation using your default profile (`akyeung@gmail.com`):

### 1. Create a Test Participant (Run once in Terminal)
```bash
curl -X POST https://api.prolific.com/api/v1/researchers/participants/ \
  -H "Authorization: Token YOUR_PROLIFIC_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"email": "allan+test@gmail.com"}'
```

### 2. Create the Draft Study
```bash
# This creates the study in draft mode (free) and prints the study ID
prolific study create -t ai-nization-survey.yaml
```

### 3. Generate Free Test Link
Replace `<STUDY_ID>` with the ID printed from the previous command:
```bash
prolific study test <STUDY_ID>
```
* Copy the resulting URL into your browser to test the full survey path from start to finish.

---

## 📊 Step 4: Live Launch & Data Collection

Once you add funds online to your personal account (`akyeung@gmail.com`):

1. **Publish the study:**
   ```bash
   prolific study create -t ai-nization-survey.yaml --publish
   ```
2. **Monitor Submissions:**
   Check completion progress and get submission data:
   ```bash
   prolific study list
   ```
3. **Analyze Results:**
   Open Google Forms -> **Responses** -> **Link to Sheets** to get your data in Excel format for your presentation slides.
