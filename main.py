import webapp2
import random

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"
        lucky_number = random.randint(1,100)
        number_sentence = 'Your lucky number: ' + str(lucky_number)
        number_paragraph = "<p>" + number_sentence + "</p>"
        self.response.write(header + number_paragraph)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
