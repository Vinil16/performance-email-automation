
#  Performance Email Automation

This project automatically sends personalized performance summary emails to team managers based on employee feedback and sentiment analysis.

---

##  Features

-  AI-driven sentiment analysis using TextBlob
-  Smart summary generation based on feedback
-  Sends auto-generated emails to respective managers
-  Uses `.env` for securing email credentials

---

## Project Structure

```
├── emailer.py            # Main script to run
├── employees.csv         # Input CSV with employee data
├── .env                  # Secure file to store email credentials
└── README.md             # Project documentation
```

---

##  Requirements

- Python 3.x
- Required Libraries:
    ```bash
    pip install pandas textblob python-dotenv
    python -m textblob.download_corpora
    ```

---

##  Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Vinil16/performance-email-automation.git
    cd performance-email-automation
    ```

2. **Create a `.env` File in the Same Directory**

    ```env
    EMAIL=youremail@gmail.com
    PASSWORD=your-app-password
    ```
    > Use an [App Password](https://support.google.com/accounts/answer/185833?hl=en) for Gmail if 2FA is enabled.

3. **Add Employee Data in `employees.csv`**
    Example format:
    ```csv
    Name,Manager,Performance,Projects,LastFeedbackText,ManagerEmail
    Karthik Bulusu,vinil,Good,4,"Karthik shows good teamwork and often helps peers during crunch time.",vinilarava2004@gmail.com
    ```

4. **Run the Script**
    ```bash
    python emailer.py
    ```

---

##  How to Test

```bash
cd performance-email-automation
python emailer.py
```

Make sure `.env` and `employees.csv` are correctly filled before testing.


---

##  Sample Output

```
SUCCESS: Karthik Bulusu to vinilarava2004@gmail.com
SUCCESS: Suman Das to vinil_arava@srmap.edu.in
```


