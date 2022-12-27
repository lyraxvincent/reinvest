"""investment calculators"""
from typing import Tuple

def investment_calculator(monthly_contribution: int,
                          n_years: int,
                          annual_percentage_return: int = 10,
                          starting_amount: int = 0) -> float:
    """
    Calculate amount in investments after n_years

    Arguments:
        monthly_contribution -- amount to be contriuted every month

        n_years -- number of years for contribution

        annual_percentage_return -- % annual return

    Keyword Arguments:
        starting_amount -- amount currently in the contribution pool/account (default: {0})

    Returns:
        total investment amount after the specified years
    """

    yearly_contribution = monthly_contribution * 12

    total_amount = starting_amount

    for _ in range(n_years):
        amount = yearly_contribution + ((yearly_contribution + total_amount) * (annual_percentage_return/100))
        total_amount += amount

    return total_amount


def trading_calculator(initial_capital: int,
                       starting_share_price: float,
                       average_share_price: float,
                       trading_difference: float,
                       n_months: int,
                       trading_frequency: int) ->  Tuple[float, float]:
    """
    Calculate amount in trading account after n_months, trading n times a month on a share price difference eg. 1 bob
    (selling at 1 bob higher and buying at 1 bob lower selling price)

    Arguments:
        initial_capital -- amount invested initially

        starting_share_price -- first buying price per share

        average_share_price -- average price per share

        trading_difference -- share price difference to take advantage of

        n_months -- number of months

        trading_frequency -- no. of times traded in a month

    Assumption: the average price per share does not change so much so we use the same price for all transactions

    Returns:
        Total amount in trading account after n_months
    """

    # to be updated when profit made buys extra shares
    total_shares = initial_capital / starting_share_price

    for _ in range(n_months):

        monthly_profit = (trading_difference * trading_frequency) * total_shares

        # profit back to shares
        total_shares += (monthly_profit / average_share_price)

    return total_shares, total_shares*average_share_price
