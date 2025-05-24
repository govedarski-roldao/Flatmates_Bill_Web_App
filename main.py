from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, IntegerField
from flask import Flask
from flask import render_template, request
from flatmates_bill import flat


app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html", billform=bill_form)


class ResultsPage(MethodView):
    def post(self):
        #Form and amounts
        billform = BillForm(request.form)
        amount = float(billform.amount.data)
        period = billform.period.data
        the_bill = flat.Bill(amount, period)
        #First Person
        name1 = billform.name1.data
        days_in_house1 = float(billform.days_in_house1.data)
        flatmate1 = flat.Flatmate(name1, days_in_house1)
        #Second Person
        name2 = billform.name2.data
        days_in_house2 = float(billform.days_in_house2.data)
        flatmate2 = flat.Flatmate(name2, days_in_house2)
        to_pay = flat.Flatmate.pays(flatmate1, the_bill, flatmate2)
        amount1 = flatmate1.pays(the_bill,flatmate2)
        amount2 = flatmate2.pays(the_bill, flatmate1)
        return render_template("results.html", name1=name1,amount1=amount1,name2=name2,amount2=amount2)


class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")
    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in the house: ")
    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in the house: ")
    button = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill", view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/results", view_func=ResultsPage.as_view("results"))

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
