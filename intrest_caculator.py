# Intrest_month = float(input('Enter the number of month'))
# Loan_amount = float(input('Enter amount of loan' ))
# Intrest_rate = float(input('Enter rate of loan' ))

# total_intrest =Loan_amount * Intrest_rate *Intrest_month  / 100

# Intrest_amount =  Loan_amount + total_intrest
# print(f'your interest is {total_intrest}')
# print(f'your interest amount is {Intrest_amount}')

# Intrest_month = float(input('Enter the number of month'))
# Loan_amount = float(input('Enter amount of loan' ))
# Intrest_rate = float(input('Enter rate of loan' ))

# def  total_intrest(a,b,c):
#     return a*b*c/100
# interest_amount = total_intrest(Intrest_month,Loan_amount,Intrest_rate)

# print(f'your interest is {interest_amount}')




def check_loan_eligibility(age, annual_income, credit_score):

    new_age = age if 21 <= age <= 61 else None
    new_annual_income = annual_income if annual_income >= 20000 else None
    new_credit_score = credit_score if credit_score >= 600 else None

    if new_age and new_annual_income and new_credit_score:
        credits_check = "Eligible for credit loan"
    else:
        credits_check = "Not eligible for credit"
    return credits_check


credits_check = check_loan_eligibility(25, 35000, 720)
print(f"Credit check status: {credits_check}")