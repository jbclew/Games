# Import tkinter
from tkinter import *
from tkinter import ttk


class LoanCalculator:

    def __init__(self):
        window = Tk()  # Create a window
        window.geometry("550x500")
        window.title("Home Loan Payment Calculator")  # Set title
        # create the input boxes.
        Label(window, text="Annual Interest Rate (%)", font=("Courier", 14)).grid(row=1, column=1, sticky=W)
        Label(window, text="Number of Years", font=("Courier", 14)).grid(row=2, column=1, sticky=W)
        Label(window, text="House Price", font=("Courier", 14)).grid(row=3, column=1, sticky=W)
        Label(window, text="Down Payment", font=("Courier", 14)).grid(row=4, column=1, sticky=W)
        Label(window, text="Credit Score", font=("Courier", 14)).grid(row=5, column=1, sticky=W)
        Label(window, text="PMI Coverage", font=("Courier", 14)).grid(row=6, column=1, sticky=W)
        Label(window, text="Maintenance Costs", font=("Courier", 14)).grid(row=7, column=1, sticky=W)
        Label(window, text="Property Tax Rate (%)", font=("Courier", 14)).grid(row=8, column=1, sticky=W)
        Label(window, text="Monthly Insurance", font=("Courier", 14)).grid(row=9, column=1, sticky=W)
        Label(window, text="PMI Payment", font=("Courier", 14)).grid(row=10, column=1, sticky=W)
        Label(window, text="Mortgage Payment", font=("Courier", 14)).grid(row=11, column=1, sticky=W)
        Label(window, text="Maintenance", font=("Courier", 14)).grid(row=12, column=1, sticky=W)
        Label(window, text="Taxes", font=("Courier", 14)).grid(row=13, column=1, sticky=W)
        Label(window, text="Total Monthly Payment", font=("Courier", 14, 'bold')).grid(row=14, column=1, sticky=W)

        # for taking inputs
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)

        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=2, column=2)

        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)

        self.downPayment = StringVar()
        Entry(window, textvariable=self.downPayment, justify=RIGHT).grid(row=4, column=2)

        # drop-down choices for credit score and coverage choices
        credit_choices = ['760+', '720-759', '680-719', '620-679', 'Below 620']

        coverage_choices = [['35%', '30%', '25%', '18%'], ['35%', '30%', '25%', '18%', '16%'],
                            ['30%', '25%', '17%', '12%'],
                            ['25%', '17%', '12%', '6%'], ['N/A']]

        credit = ttk.Combobox(window, width=20, value=(credit_choices))
        credit.grid(row=5, column=2, columnspan=1, padx=10, pady=2, sticky='w')

        self.cov_select = ttk.Combobox(window, width=20)
        self.cov_select.grid(row=6, column=2, columnspan=1, padx=10, pady=2, sticky='w')

        # following method will link credit and coverage selection drop-downs as combo box.
        # This allows the correct coverage choices to display depending on credit chosen.
        def callback(eventObject):
            abc = eventObject.widget.get()
            car = credit.get()
            index = credit_choices.index(car)
            self.cov_select.config(values=coverage_choices[index])

        self.cov_select.bind('<Button-1>', callback)
        # Define the maintenance costs as a percentage of the house value.
        maint_choices = ['0%', '1%', '2%', '3%', '4%']
        self.maintain = ttk.Combobox(window, width=20, value=(maint_choices))
        self.maintain.grid(row=7, column=2, columnspan=1, padx=10, pady=2, sticky='w')

        self.taxesVar = StringVar()
        Entry(window, textvariable=self.taxesVar, justify=RIGHT).grid(row=8, column=2)

        self.insuranceMonth = StringVar()
        Entry(window, textvariable=self.insuranceMonth, justify=RIGHT).grid(row=9, column=2)

        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar).grid(row=10, column=2, sticky=E)

        self.pmiPaymentVar = StringVar()
        lblPMIPayment = Label(window, textvariable=self.pmiPaymentVar).grid(row=11, column=2, sticky=E)

        self.maintainVar = StringVar()
        lblmaintainPayment = Label(window, textvariable=self.maintainVar).grid(row=12, column=2, sticky=E)

        self.taxPay = StringVar()
        lbltaxPayment = Label(window, textvariable=self.taxPay).grid(row=13, column=2, sticky=E)

        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable=
        self.totalPaymentVar, font=("Courier", 14, 'bold')).grid(row=14, column=2, sticky=E)

        # create the button
        btComputePayment = Button(window, text="Compute Payment", font=("Courier", 14),
                                  command=self.computePayment).grid(row=16, column=2, sticky=E)
        window.mainloop()  # Create an event loop

    # compute the total payment.
    def computePayment(self):
        loan_amount = float(self.loanAmountVar.get()) - float(self.downPayment.get())
        monthlyPayment = self.getMonthlyPayment(
            loan_amount, float(self.annualInterestRateVar.get()), int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        ltv = (float(self.loanAmountVar.get()) - float(self.downPayment.get())) / float(self.loanAmountVar.get())
        # Change the coverage from string to float then ignore PMI if credit score too low.
        cov_string_to_float = self.cov_select.get()
        if cov_string_to_float == 'N/A':
            coverage_perc = 'n/a'
        else:
            coverage_perc = float(cov_string_to_float[:-1]) / 100
        if ltv <= .80:
            coverage_perc = 0
        if coverage_perc == 'n/a':
            self.pmiPaymentVar.set('N/A for credit score')
            monthly_pmi = 0
        else:
            annual_cost = (float(self.loanAmountVar.get()) - float(self.downPayment.get())) * (coverage_perc / 100.0)
            monthly_pmi = annual_cost / 12.0
            self.pmiPaymentVar.set(format(monthly_pmi, '10.2f'))
        tax_rate = float(self.taxesVar.get()) / 100
        taxes = (loan_amount * tax_rate) / 12
        insurance = float(self.insuranceMonth.get())
        # get maintenance value and covert to float
        maint = self.maintain.get()
        maintstr = maint[:-1]
        maint_factor = float(maintstr) / 100
        maintain_cost = (float(self.loanAmountVar.get()) * maint_factor) / 12
        # Display Taxes, Insurance, Maintenance costs.
        self.maintainVar.set(format(maintain_cost, '10.2f'))
        self.taxPay.set(format(taxes, '10.2f'))
        total = monthlyPayment + monthly_pmi + taxes + insurance + maintain_cost
        self.totalPaymentVar.set(format(total, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        # compute the monthly payment.
        payments = float(numberOfYears) * 12
        interestRate = float(monthlyInterestRate) / 100 / 12
        mortgagePayment = loanAmount * (interestRate * (1 + interestRate)
                                        ** payments) / ((1 + interestRate) ** payments - 1)

        return mortgagePayment

# call the class to run the program.
LoanCalculator()
