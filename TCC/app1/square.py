import webapp2

class SquareHandler(webapp2.RequestHandler):
    def get(self):
        number = float(self.request.get('number'))
        square = number * number
        self.response.write(f"The square of {number} is {square}")

app = webapp2.WSGIApplication([
    ('/square', SquareHandler)
], debug=True)
