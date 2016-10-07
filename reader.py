__author__ = 'Andy'

import csv
import re

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
Internet
Advertising and Promotion
"""

dictionary = {}

def readcsv2(filename):
	reader = csv.DictReader(open(filename))
	print sum([float(row['Amount'].replace(',', '') or 0) for row in reader])

def readcsv(filename):
	reader = csv.DictReader(open(filename))
	# new comment type, add to sum array
	for row in reader:
		#if not empty string
		if row['Category']:
			row['Debit'] = row['Debit'].replace(',', '') or 0.
			row['Credit'] = row['Credit'].replace(',', '') or 0.
			#if category isn't in dict, init
			if row['Category']in dictionary:
				try:
					dictionary[row['Category']] += -float(row['Debit']) + float(row['Credit'])
				except ValueError:
					print str(row['Debit']) + "+=this is wrong? debit"
					print str(row['Credit']) + "+=this is wrong? credit"
			#else add to it
			else:
				try:
					dictionary[row['Category']] = -float(row['Debit']) + float(row['Credit'])
				except ValueError:
					print str(row['Debit']) + "=this is wrong? debit"
					print str(row['Credit']) + "=this is wrong? credit"
	print dictionary
	print sum(dictionary.values())

# readcsv2("August.csv")
readcsv("September.csv")

