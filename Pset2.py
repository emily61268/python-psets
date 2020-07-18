#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:34:02 2018

@author: emilybean612
"""

# Problem 1
balance = float(input("Balance: "))
annualInterestRate = float(input("Annual Interest Rate: "))
monthlyPaymentRate = float(input("Monthly Interest Rate: "))
monthInterestRate = (annualInterestRate)/12.0
month = 0

while month < 12:
    month += 1
    minMonthlyPayment = monthlyPaymentRate * balance
    monthlyub = balance - minMonthlyPayment
    balance = round(monthlyub + (monthInterestRate * monthlyub), 2)
    print("Month "+str(month)+" Remaining balance: "+str(balance))
print("Remaining balance: "+str(balance))





# Problem 2
balance = float(input("Balance: "))
annualInterestRate = float(input("Annual Interest Rate: "))
monthlyInterestRate = (annualInterestRate)/12.0
newBalance = balance
month = 0
minFixed = 0

while newBalance > 0:
    newBalance = balance
    minFixed += 0.01
    while month < 12:
        month += 1
        monthlyub = newBalance - minFixed
        newBalance = round(monthlyub + (monthlyInterestRate * monthlyub), 2)
    month = 0
print("Lowest Payment: "+str(round(minFixed, 2)))
    
    
    
    
# Problem 3 (Bisection Search)
balance = float(input("Balance: "))
annualInterestRate = float(input("Annual Interest Rate: "))
newBalance = balance
monthlyInterestRate = (annualInterestRate)/12.0
lowerBound = balance/12
upperBound = (balance * ((1 + monthlyInterestRate)**12))/12.0
epsilon = 0.05

while abs(balance) > epsilon:
    ans = (lowerBound + upperBound)/2.0
    balance = newBalance
    for i in range(12):
        balance = balance - ans + ((balance - ans) * monthlyInterestRate)
    if balance > epsilon:
        lowerBound = ans
    elif balance < -epsilon:
        upperBound = ans
    else:
        break
print("Lowest Payment: "+str(round(ans, 2)))





    
    
    
    