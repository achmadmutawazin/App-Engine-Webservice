import webapp2

class ReverseHandler(webapp2.RequestHandler):
    def get(self):
        string = self.request.get('string')
        reversed_string = string[::-1]
        self.response.write(f"The reverse of '{string}' is '{reversed_string}'")

app = webapp2.WSGIApplication([
    ('/reverse', ReverseHandler)
], debug=True)
