from core import Mail
from core import Message
from core import jsonify
from core import app

#send tablet name, location and damage type in email
def DamagedReport(name, location, damage):
    with app.app_context():
        msg = Message(subject="Damaged Report!",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["zlatanjr08@gmail.com"], # replace with your email for testing
                      body="The following tablet {} from {} has been reported with a {} issue.".format(name, location, damage ))
        mail.send(msg)
    return jsonify({'message': 'Your message has been sent successfully'}), 200