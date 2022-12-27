"""tests for src/reinvest/calculators.py"""

from reinvest import investment_calculator, trading_calculator
import numpy as np


def test_investment_calculator():

    assert investment_calculator(
        starting_amount=0,
        monthly_contribution=100000,
        n_years=5,
        annual_percentage_return=10
    ) == 8058732


def test_trading_calculator():

    res1 =  trading_calculator(
        initial_capital=350000,
        starting_share_price=30,
        average_share_price=30,
        trading_difference=1,
        n_months=24,
        trading_frequency=4
    )

    res2 =  trading_calculator(
        initial_capital=350000,
        starting_share_price=30,
        average_share_price=30,
        trading_difference=1,
        n_months=24,
        trading_frequency=6
    )

    assert np.allclose(res1[0], 235250.57)
    assert np.allclose(res1[1], 7057517.12)

    assert np.allclose(res2[0], 927463.22)
    assert np.allclose(res2[1], 27823896.52)