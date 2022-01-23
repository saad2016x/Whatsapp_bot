from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
   
    if 'السلام عليكم' in incoming_msg:

        msg.body('وعليكم السلام                 ')

        msg.body('       حياك الله في متجرنا!             ')

        msg.body('      تفضل كيف اقدر اخدمك ؟ ')
        responded = True
    if 'كيف حالك' in incoming_msg:
        msg.body('الحمدلله اخباركك !')

        responded = True
    if 'احتاج' in incoming_msg:
        msg.body('اذا ممكن تفيدنا بمعلوماتك للتواصل معك لاحقا !        ')

        msg.body('      الاسم ,         '  )

        msg.body(        '      رقم التواصل , ' )

        msg.body(         '     وقت التواصل المناسب  ')
        responded = True
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'قطط' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('اتمنى منك كتابة الخدمة المطلوبة ليتم التواصل معك !')
    return str(resp)


if __name__ == '__main__':
    app.run()