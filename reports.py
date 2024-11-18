import smtplib
from email.mime.text import MIMEText

# Function to send email
def send_email(subject, body, recipient_email, sender_email, sender_password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Email sent successfully!")

# Example usage
if __name__ == "__main__":
    SUBJECT = "Daily Competitor Report"
    BODY = "GitHub Activity: XYZ\nJobs Posted: ABC\nApp Reviews: DEF\nPricing Changes: GHI"
    RECIPIENT_EMAIL = "recipient@example.com"
    SENDER_EMAIL = "your-email@gmail.com"
    SENDER_PASSWORD = "your-email-password"

    send_email(SUBJECT, BODY, RECIPIENT_EMAIL, SENDER_EMAIL, SENDER_PASSWORD)
