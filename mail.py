from app import mail


#send tablet name, location and damage type in email
def DamagedReport(damage):
    with app.app_context():
        msg = Message(subject="Damaged Report!",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["zlatanjr08@gmail.com"], # replace with your email for testing
                      body="The following tablet {} from {} has been reported with a {} issue.".format(tabletname, location, damage ))
        mail.send(msg)