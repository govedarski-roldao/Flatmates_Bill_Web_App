from flask.views import MethodView
from wtforms import Form
from flask import Flask
from flask import render_template

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template("index.html")



class BillFormPage(MethodView):
    def get(self):
        return "I am the bull form page"


class Results(MethodView):
    def __init__(self):
        self.empty = ''


class BillForm(Form):
    def __init__(self):
        self.wow = ''


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill", view_func=BillFormPage.as_view("bill_form_page"))

app.run(debug=True)


#
# class Matter:
#     freezing_temperature = None
#     boiling_temperature = None
#
#     def __init__(self, temperature):
#         self.temperature = temperature
#
#     def state(self):
#         if self.temperature <= self.freezing_temperature:
#             return 'solid'
#         elif self.freezing_temperature < self.temperature < self.boiling_temperature:
#             return 'liquid'
#         else:
#             return 'gas'
#
#
# class Water(Matter):
#     freezing_temperature = 0
#     boiling_temperature = 100
#
#
# class Mercury(Matter):
#     freezing_temperature = -38.83
#     boiling_temperature = 356.7
