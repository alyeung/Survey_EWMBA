# 💸 Zero-Cost Survey Action Plan

Since your workspace balance is currently `0.00 GBP`, you can still successfully test your integration and collect global data for free. Here are the two pathways to execute your survey without spending money:

---

## 💻 Path 1: The Prolific Developer Sandbox (For Integration Testing)
* **Goal:** Verify that your CLI configuration, survey redirect links, and completion codes work correctly before launching to paid participants.
* **Cost:** **$0.00** (Draft creation and test runs on Prolific are completely free).

### Step 1: Create a Test Participant
Before you can run a free test study, you must create a "Test Participant" in your workspace.
You can run this using a curl request in your terminal:
```bash
curl -X POST https://api.prolific.com/api/v1/researchers/participants/ \
  -H "Authorization: Token YOUR_PROLIFIC_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"email": "test-participant@example.com"}'
```

### Step 2: Create a Draft Study
Write a simple YAML file called `draft-study.yaml`. Note that we **do not** use the `--publish` flag here:
```yaml
name: "Draft Usability Study"
internal_name: "Draft_Val_Test"
description: "Draft study for testing."
external_study_url: "https://yourteam.typeform.com/to/surveyid?participant={{%PROLIFIC_PID%}}"
prolific_id_option: url_parameters
completion_code: "VAL_DONE_2026"
completion_option: code
total_available_places: 1
estimated_completion_time: 2
reward: 50 # (Doesn't charge you since it remains a draft)
device_compatibility:
  - desktop
  - mobile
```
Create the draft using the CLI:
```bash
# This creates a draft study and prints its ID (e.g., 64395e9c2332b8a59a65d51e)
prolific study create -t draft-study.yaml
```

### Step 3: Run the Free Test Preview
Once you have the Study ID returned from the previous step, run:
```bash
prolific study test <STUDY_ID>
```
* **Output:** The CLI will generate a special test URL.
* **Action:** Paste this URL into your browser. It will simulate a participant clicking your study, direct you to your survey, pass a mock participant ID, and test the redirect back to the completion code page—all for free!

---

## 👥 Path 2: The "Global MBA Cohort" Crowd (For Free Response Collection)
* **Goal:** Collect real data from a global audience by leveraging your international classmates as proxies.
* **Cost:** **$0.00**

Since you are in a global MBA program, your classmates represent a highly diverse, multilingual, and cross-cultural cohort. You can run one of the survey tracks from the `survey_questions_plan.md` using this method:

### 1. Survey Creation (Free Tier)
Set up a free survey on **Typeform** (max 10 responses/month free) or **Google Forms** (unlimited free responses).
* **Tip:** Google Forms is recommended for hackathons because it is completely free and automatically exports responses to Google Sheets for real-time charts.

### 2. Tailor for Global Contexts
In your survey, add a mandatory demographic question:
* *"Which country did you spend the majority of your working career in?"* (This allows you to filter and segment your classmate responses into US, Europe, Asia, etc. during your analysis).

### 3. Share & Trade Responses
During the hackathon, distribute your Google Form link:
* In your class Slack/WhatsApp groups.
* Pitch it as: *"Quick 2-minute survey on global workplace incentives for our hackathon project. Happy to fill out yours in return!"*

### 4. Create your Slides
Once you get 15-20 responses, create charts showing:
* **Perception discrepancy:** Do classmates from Asian contexts view incentives differently than those from US/European contexts?
* **Presenter Slide:** *"We surveyed 20 future global business leaders representing 8 nationalities."*
