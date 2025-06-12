import pandas as pd
from textblob import TextBlob
from email.message import EmailMessage
import smtplib
import time
import os
from dotenv import load_dotenv

# Base directory (path where this script is located)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load environment variables from .env file in same directory
load_dotenv(os.path.join(BASE_DIR, ".env"))
sender_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Sentiment Analysis Function
def analyze_sentiment(text):
    blob = TextBlob(text)
    return "Positive" if blob.sentiment.polarity > 0.1 else "Negative" if blob.sentiment.polarity < -0.1 else "Neutral"

# Load CSV using absolute path and add Sentiment column
csv_path = os.path.join(BASE_DIR, "employees.csv")
df = pd.read_csv(csv_path)
df["Sentiment"] = df["LastFeedbackText"].apply(analyze_sentiment)

# Email Body Generator
def create_email_body(row):
    summary = {
        "Positive": f"{row['Name']} is performing exceptionally well and continues to exceed expectations.",
        "Negative": f"{row['Name']} may benefit from support to improve performance and meet goals.",
        "Neutral": f"{row['Name']}'s performance is steady. Monitoring further progress is suggested."
    }[row["Sentiment"]]

    return f"""
Hi {row['Manager']},

I hope you're doing well. Based on the performance data for this month, here’s a brief insight about your team member, {row['Name']}:

Performance Overview  
{summary}

Your Last Feedback  
"{row['LastFeedbackText']}"

Projects Completed: {row['Projects']}

Please feel free to add any additional feedback or appreciation as needed. Consistent support and timely recognition go a long way in team growth.

Best regards,  
Analytics Bot
"""

# Send personalized emails
for _, row in df.iterrows():
    msg = EmailMessage()
    msg["Subject"] = f"Performance Summary for {row['Name']} ({int(time.time())})"
    msg["From"] = sender_email
    msg["To"] = row["ManagerEmail"].strip().lower()
    msg.set_content(create_email_body(row))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)
            print(f"✅ SUCCESS: {row['Name']} to {row['ManagerEmail']}")
    except Exception as e:
        print(f"❌ FAILED: {row['Name']} to {row['ManagerEmail']} - {e}")
