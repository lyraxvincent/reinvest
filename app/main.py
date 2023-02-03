import streamlit as st
from reinvest import investment_calculator, trading_calculator

st.set_page_config(layout="wide")


with st.container():

    st.markdown("**:blue[Investment Calculator]**")
    st.caption("❓ Calculate amount in investments after n years ")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        STARTING_AMOUNT = st.number_input(label="Starting Amount", value=0)
    with col2:
        MONTHLY_CONTRIBUTION = st.number_input(label="Monthly Contribution", value=100)
    with col3:
        N_YEARS = st.number_input(label="Number of Years", value=5)
    with col4:
        ANNUAL_RETURN = st.number_input(label="Annual Percentage Return", value=10)


    res = investment_calculator(
        monthly_contribution=MONTHLY_CONTRIBUTION,
        starting_amount=STARTING_AMOUNT,
        n_years=N_YEARS,
        annual_percentage_return=ANNUAL_RETURN
    )

    st.caption(f"### Total invested amount after {N_YEARS} years: **:green[{res:,.2f}]**", )

st.markdown("-----")

with st.container():

    st.markdown("**:blue[Trading calculator]**")
    st.caption("❓ Calculate amount in trading account after n months, trading\
               n times a month on a price difference eg. $1")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        INITIAL_CAPITAL = st.number_input(label="Initial Capital", value=0)
        STARTING_SHARE_PRICE = st.number_input(label="Starting Share Price", value=1)
        AVERAGE_SHARE_PRICE = st.number_input(label="Average Share Price", value=1)
        TRADING_DIFF = st.number_input(label="Trading Difference", value=1.0, step=.1)
        N_MONTHS = st.number_input(label="Number of Months", value=12)
        TRADING_FREQUENCY = st.number_input(label="No. of Trades to be Closed per Month", value=4)
        BROKERAGE_FESS =st.number_input(label="Brokerage fees (%)", value=0.0, step=.1)

    n_shares, value = trading_calculator(
        initial_capital=INITIAL_CAPITAL,
        starting_share_price=STARTING_SHARE_PRICE,
        average_share_price=AVERAGE_SHARE_PRICE,
        trading_difference=TRADING_DIFF,
        n_months=N_MONTHS,
        trading_frequency=TRADING_FREQUENCY,
        brokerage_fees=BROKERAGE_FESS
    )

    with col2:

        for l in range(13):
            st.write(" ")
        st.caption(f"### Total shares after {N_MONTHS} months: **:green[{n_shares:,.2f}]**\
                   \n### Value in KShs: **:green[{value:,.2f}]**")