# import smtplib
import datetime
import config
import time
import outlook


def main():
    mail = outlook.Outlook()
    mail.login(config.username, config.passwd)
    while True:
        try:
            mail.inbox()
        except:
            print("Connection down, reconnecting...")
            mail.login(config.username, config.passwd)
        print(datetime.datetime.now())
        if mail.hasUnread():
            print("Has Unread Mail")
            mail.unread()
            print("Subject: ")
            print(mail.mailsubject())
            print("Body: ")
            print(mail.mailbody())
            attach = mail.getAttachements()
            if attach is not None:
                print("Attachements: ")
                print(attach)
        else:
            print("No Unread Mail")
        time.sleep(1)


main()
