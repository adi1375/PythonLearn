def calculate_finances(monthly_income:float,tax_rate:float,currency:str) -> None:
    monthly_tax : float = monthly_income * (tax_rate/100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary : float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax
    
    print('---------------------------------------')    
    print(f'Monthly and Yearly Finance:')
    print('---------------------------------------')
    print(f'Monthly Income: {currency}{monthly_income:,.2f}')
    print(f'Tax Rate: {tax_rate:,.0f}%')
    print(f'Monthly Tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly Net Income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly Salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly Tax Paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly Net Income: {currency}{yearly_net_income:,.2f}')
    print('---------------------------------------')

def calculate_monthly_expenses(monthly_income:float,tax_rate:float,monthly_rent: float, monthly_food_expenses: float, currency: str) -> None:
    monthly_tax : float = monthly_income * (tax_rate/100)
    monthly_net_income: float = monthly_income - monthly_tax
    total_monthly_expenses: float = monthly_rent + monthly_food_expenses
    income_left_over_per_month: float = monthly_net_income - total_monthly_expenses
     
    print(f'Monthly Expenses: ')
    print('---------------------------------------')
    print(f'Monthly Net income: {currency}{monthly_net_income:,.2f}')
    print(f'Monthly Rent: {currency}{monthly_rent:,.2f}')
    print(f'Monthly Food Expenses: {currency}{monthly_food_expenses:,.2f}')
    print(f'Total Monthly Expense: {currency}{total_monthly_expenses:,.2f}')
    print(f'Monthly Income Left Over: {currency}{income_left_over_per_month:,.2f}')
    print('---------------------------------------')

def get_float_input(msg: str,min_val=None) -> float:
    while True:
        try:
            value = float(input(msg))
            if min_val is not None and value < min_val:
                print(f"Input can't be less than {min_val}. Please enater a valid number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main() -> None:

    monthly_income : float = get_float_input("Enter your monthly salary: ",min_val = 0)
    tax_rate : float = get_float_input("Enter your tax rate (%): ",min_val=0)
    monthly_rent: float = get_float_input("Enter your monthly rent: ",min_val=0)
    monthly_food_expenses = get_float_input("Enter your monthly food expenses: ",min_val=0)
        
    
    calculate_finances(monthly_income,tax_rate,currency='$')
    calculate_monthly_expenses(monthly_income,tax_rate,monthly_rent,monthly_food_expenses,currency='$')
    
if __name__ == '__main__':
    main() 