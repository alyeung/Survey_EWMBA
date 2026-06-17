# Survey Research Plan: Managing People in a Global Context

Based on your course notes, here is a structured survey plan. These survey tracks are designed to gather real-world data from global participants on Prolific to validate or challenge the key concepts from your class cases (Rakuten, Infosys, InfoBeans, Juhudi, and Fivetran).

---

## 🤖 Track 1: "AI-nization" & Psychological Safety (The AI Mandate)
* **Core Hypothesis:** Top-down corporate mandates to use Generative AI ("AI-nization") disrupt internal power dynamics (shifting status from senior leaders to tech-savvy juniors) and create psychological insecurity, which can be mitigated by custom, unit-specific adoption tracks.
* **Target Audience on Prolific:** Corporate and knowledge-work professionals globally who are experiencing AI tool adoption or mandates in their workplace.

### Suggested Survey Questions:
1. **[Multiple Choice]** How does a company-wide mandate or pressure to use Generative AI tools (e.g. ChatGPT, Claude, Copilot) in your daily tasks affect your psychological comfort and job security?
   * *Options:* Significantly increases anxiety & insecurity / Slightly increases insecurity / Has no effect / Increases my confidence & job safety.
2. **[Likert Scale]** "I feel comfortable admitting to my manager or team when I struggle to use or prompt AI tools, without fear of looking incompetent."
   * *Options:* Strongly Agree / Agree / Neutral / Disagree / Strongly Disagree.
3. **[Multiple Choice]** How has the rise of Generative AI affected the status dynamics and power balance in your team?
   * *Options:* Shifted power to younger, tech-savvy junior employees / Strengthened the position of senior leaders / Had no noticeable impact on power dynamics.
4. **[Multiple Choice]** Which implementation strategy do you believe is most effective for adopting AI in a global organization?
   * *Options:* A universal mandate (everyone uses the same tools) / Customized adoption tracks (different business units or regions select and customize their own AI tools) / Voluntary adoption (no guidelines or requirements).
5. **[Open-Ended]** Describe a scenario where you felt pressured to use AI to complete a task, but felt it was either unnecessary, counter-productive, or made you feel anxious about your role value. (Note: in the live Prolific survey, this was converted to a multiple-choice question on Coercion & Pressure to support API rules).
6. **[Multiple Choice]** Which of the following training formats do you find most effective for learning how to use and integrate Generative AI tools (e.g., ChatGPT, Claude) into your daily workflows?
   * *Options:* Hands-on, Interactive Workshops (live group sessions) / 1-on-1 Mentorship or Coaching (personalized guidance) / Self-Paced Tutorials & Online Videos (interactive online courses) / Formal Classroom Classes / Peer-Led Learning Communities / On-the-job Trial and Error.

---

## 💰 Track 2: Culturally-Aligned Incentives (Juhudi & Hofstede Case)
* **Core Hypothesis:** Employees in collectivist cultures respond more favorably to team-level bonuses and non-monetary rewards (e.g., career development, flexibility) than those in individualist cultures, who prefer discretionary individual cash bonuses.
* **Target Audience on Prolific:** A cross-cultural comparison group:
  * Group A (Individualist): United States, United Kingdom.
  * Group B (Collectivist/Relationship-focused): India, Mexico, Kenya.

### Suggested Survey Questions:
1. **[Ranking]** Please rank the following rewards in order of what motivates you the most to perform at your best:
   * *Items:* Individual cash bonus / Team-level cash bonus / Additional paid time off / Sponsored career training / Flexible remote-work options / Public recognition.
2. **[Likert Scale]** "If my team works together on a project, it is fairer to divide the bonus equally among everyone than to reward individuals based on personal performance."
   * *Options:* Strongly Agree / Agree / Neutral / Disagree / Strongly Disagree.
3. **[Multiple Choice]** How do you view discretionary bonuses (decided subjectively by your manager) compared to formula-based bonuses (determined by strict metrics)?
   * *Options:* Prefer discretionary (allows manager to see soft efforts) / Prefer formula-based (fairer and avoids favoritism) / Neutral.
4. **[Open-Ended]** What is the most meaningful non-monetary incentive you have ever received from an employer, and why did it motivate you?

---

## ⚖️ Track 3: Unconscious Bias & Discretionary Compensation (Ryan Hammond/Fivetran Case)
* **Core Hypothesis:** Discretionary compensation systems (like negotiating individual stock options/equity) introduce significant gender and social bias compared to standardized, formula-driven reward models.
* **Target Audience on Prolific:** Tech and corporate professionals across multiple countries.

### Suggested Survey Questions:
1. **[Likert Scale]** "I believe my company's process for awarding equity/stock options is transparent and free of managerial bias."
   * *Options:* Strongly Agree / Agree / Neutral / Disagree / Strongly Disagree.
2. **[Multiple Choice]** Which system do you believe results in the fairest pay outcomes for diverse employees?
   * *Options:* Fixed formulaic pay with zero negotiation / Discretionary pay with room to negotiate / Peer-reviewed performance ratings.
3. **[Likert Scale]** "I have had to prove I can perform at a higher level *before* receiving a promotion/raise, rather than being promoted on potential."
   * *Options:* Strongly Agree / Agree / Neutral / Disagree / Strongly Disagree.
4. **[Open-Ended]** Have you ever negotiated your equity or bonus compensation? If so, did you feel the process was transparent and fair?

---

## 🎓 Track 4: Hiring for "Learnability" vs. Technical Skills (Infosys & InfoBeans Case)
* **Core Hypothesis:** Recruiting from regional, non-elite schools based on "learnability" and core values (general skills) yields higher retention and organizational loyalty than targeting elite engineering schools for immediate technical skills.
* **Target Audience on Prolific:** Early-career professionals and recent graduates (Ages 18–26) in India or Eastern Europe.

### Suggested Survey Questions:
1. **[Multiple Choice]** When choosing a graduate job, which of the following is most important to you?
   * *Options:* Highest starting salary / Comprehensive learning and development program / Prestige of the company brand / Geographic proximity to home / Work-life balance.
2. **[Likert Scale]** "I feel a strong sense of loyalty to the first company that hired and invested in training me, even if a competitor offers slightly more pay."
   * *Options:* Strongly Agree / Agree / Neutral / Disagree / Strongly Disagree.
3. **[Multiple Choice]** How would you rate your university's preparation for your actual job compared to the on-the-job training provided by your employer?
   * *Options:* University did 80% of the prep / Employer training did 80% of the prep / 50-50 split.
4. **[Open-Ended]** What specific skill (technical or communication) do you wish your employer had trained you on during your onboarding?

---

## 📋 Hackathon Action Plan: Running Your Survey

1. **Pick One Track:** Select the track that most directly supports your class project's final presentation argument.
2. **Setup the Survey Tool:** Build the survey in a free tool like Typeform, Google Forms, or Qualtrics. Ensure you pass the Prolific ID in the URL:
   * e.g., `https://yourteam.typeform.com/to/surveyid?participant={{%PROLIFIC_PID%}}`
3. **Draft the CLI Config:** In your workspace, use the template to create a targeted yaml file matching your choice (e.g., using `study-with-select-filters.json` to filter by country or industry).
4. **Launch and Analyze:**
   ```bash
   prolific study create -t your-survey.yaml --publish
   ```
5. **Get Results:** Wait 30 minutes, download the submissions, and analyze the response trends to create charts for your slides.
