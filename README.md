# AI-Powered People Insight Emailer

## 📌 Overview
This Python script reads employee performance data and manager feedback, analyzes the sentiment using AI (TextBlob), and sends templated emails to managers with personalized insights.

## 🔍 Features
- AI-based sentiment analysis (Positive/Neutral/Negative)
- Dynamic performance summaries
- Automated email distribution using templated content

## 📁 Files
- `employees.csv`: Input data file
- `emailer.py`: Main script
- `README.md`: This file

## ✅ How to Run
1. Install dependencies:
   pip install pandas textblob
   python -m textblob.download_corpora

2. Run the script:
   python emailer.py

## 🚀 Future Enhancements
- Use OpenAI/Gemini to generate smarter summaries
- Add dashboard view of team performance trends
