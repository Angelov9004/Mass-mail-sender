import smtplib
from email.message import EmailMessage

def send_email(to_email):
    from_email = "your@email.com"
    password = "your_password"
    message = "Subject: Hello from your Python bot!\n\nThis is a test email sent from Python."

    try:
        server = smtplib.SMTP('smtp.mail.com', 25)
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message)
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {str(e)}")
    finally:
        try:
            server.quit()
        except UnboundLocalError:
            pass

def main():
    # Read email addresses from a txt file
    with open('email_database.txt', 'r') as file:
        emails = file.readlines()

    for email in emails:
        email = email.strip()  # Remove any leading/trailing whitespaces
        send_email(email)

if __name__ == "__main__":
    main()

