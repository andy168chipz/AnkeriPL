__author__ = 'Andy'

import csv
"""
Categories as follows:


Income
Bookkeeping
Rent - retail
Rent - storage
Cash Wage
Food Cost
Tax
Payroll
Lawyer James
POS Fees
Meal & Entertainment
Office Supplies
Refund
Transfer to Savings
One Time
Ice Cream
Transfer from Savings
Credit Card Payment
Bank Fee
"""

def readcsv(filename):
	reader = csv.DictReader(open(filename))
