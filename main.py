"""functions runner"""

from reinvest import investment_calculator, trading_calculator


if __name__ == "__main__":

    investment = True
    trading = True

    if investment:

        starting_amnt = 0
        monthly_amount = 100000
        years = 5

        amnt = investment_calculator(starting_amount=starting_amnt,
                                     monthly_contribution=monthly_amount,
                                     n_years=years,
                                     annual_percentage_return=10)

        print(f"Total amount in investments after {years} years: {amnt:,.2f}")

    if trading:

        capital = 350000
        start_price = 30
        avg_price = 30
        diff = 1
        months = 24
        freq = 4

        shares, value = trading_calculator(initial_capital=capital,
                                           starting_share_price=start_price,
                                           average_share_price=avg_price,
                                           trading_difference=diff,
                                           n_months=months,
                                           trading_frequency=freq)

        print(f"Total shares after {months} months: {shares:,.2f}, value: {value:,.2f}")
