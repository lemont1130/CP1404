"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

incomes = []
def main():
    """Display income report for incomes over a given number of months."""
    how_many_months = int(input("How many months? "))
    count_total_income(how_many_months)
def count_total_income(how_many_months):
    for month in range(1, how_many_months + 1):
        income = float(input("Enter income for month{}: ".format(month)))
        incomes.append(income)
    total=0
    print("\nIncome Report\n-------------")
    for month in range(1, how_many_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month,income,total))

main()
