#  Performance email automation

##  Overview
This Python-based tool automates the generation and sending of personalized performance insight emails to managers. It leverages AI (TextBlob) for sentiment analysis of manager feedback and formats summaries into human-friendly emails.

---

##  Features
-  **AI Sentiment Analysis**: Automatically classifies feedback as Positive, Neutral, or Negative.
-  **Email Automation**: Sends personalized, professional summaries directly to each manager.
-  **Performance Insights**: Generates context-aware summaries based on feedback and project data.

---

## Project Structure
| File | Description |
|------|-------------|
| `employees.csv` | Input data containing employee details and feedback |
| `emailer.py` | Main script for analysis and email distribution |
| `.env` | (Not tracked) Stores email credentials securely |
| `.gitignore` | Ensures `.env` and other sensitive files are ignored |
| `README.md` | Documentation (this file) |

---

##  Setup & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/Vinil16/performance-email-automation.git
cd performance-email-automation
