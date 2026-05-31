import streamlit as st
import pandas as pd
import plotly.express as px

from datetime import datetime

from database import (
    create_table,
    add_expense,
    get_expenses
)

from chatbot import (
    analyze_expenses,
    ask_finance_bot
)

# Setup

st.set_page_config(
    page_title="AI Finance Assistant",
    page_icon="💰",
    layout="wide"
)

create_table()

# Header

st.title("💰 AI Finance Assistant")

st.write(
    """
    Track your expenses and receive
    AI-powered financial insights.
    """
)

# Sidebar

st.sidebar.header(
    "Add New Expense"
)

amount = st.sidebar.number_input(
    "Amount",
    min_value=0.0
)

category = st.sidebar.selectbox(
    "Category",
    [
        "Food",
        "Transport",
        "Shopping",
        "Bills",
        "Education",
        "Entertainment",
        "Other"
    ]
)

description = st.sidebar.text_input(
    "Description"
)

if st.sidebar.button(
    "Save Expense"
):

    add_expense(
        amount,
        category,
        description,
        datetime.now().strftime(
            "%Y-%m-%d"
        )
    )

    st.sidebar.success(
        "Expense Saved!"
    )

# Load Data

expenses = get_expenses()

if expenses:

    df = pd.DataFrame(
        expenses,
        columns=[
            "ID",
            "Amount",
            "Category",
            "Description",
            "Date"
        ]
    )

    # Dashboard

    st.subheader(
        "📊 Dashboard"
    )

    col1, col2, col3 = st.columns(3)

    total_spending = df[
        "Amount"
    ].sum()

    total_transactions = len(df)

    avg_spending = df[
        "Amount"
    ].mean()

    col1.metric(
        "Total Spending",
        f"₦{total_spending:,.0f}"
    )

    col2.metric(
        "Transactions",
        total_transactions
    )

    col3.metric(
        "Average Spending",
        f"₦{avg_spending:,.0f}"
    )

    st.divider()

    # Expense Table

    st.subheader(
        "📋 Expense History"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    # Spending Chart

    st.subheader(
        "📈 Spending by Category"
    )

    category_chart = (
        df.groupby(
            "Category"
        )["Amount"]
        .sum()
        .reset_index()
    )

    bar_chart = px.bar(
        category_chart,
        x="Category",
        y="Amount",
        title="Spending by Category"
    )

    st.plotly_chart(
        bar_chart,
        use_container_width=True
    )

    # Pie Chart

    st.subheader(
        "🥧 Expense Distribution"
    )

    pie_chart = px.pie(
        category_chart,
        names="Category",
        values="Amount"
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

    # Summary

    st.subheader(
        "💡 Spending Summary"
    )

    highest_category = (
        category_chart
        .sort_values(
            "Amount",
            ascending=False
        )
        .iloc[0]
    )

    st.success(
        f"""
        Highest spending category:
        {highest_category['Category']}
        (₦{highest_category['Amount']:,.0f})
        """
    )

    st.divider()

    # AI Analysis

    st.subheader(
        "🤖 AI Financial Insights"
    )

    if st.button(
        "Analyze Spending"
    ):

        with st.spinner(
            "Analyzing..."
        ):

            insights = analyze_expenses(
                expenses
            )

            st.write(
                insights
            )

    st.divider()

    # Chatbot

    st.subheader(
        "💬 Ask Your Finance Assistant"
    )

    question = st.text_input(
        "Ask a question"
    )

    if st.button(
        "Ask AI"
    ):

        answer = ask_finance_bot(
            expenses,
            question
        )

        st.write(answer)

else:

    st.info(
        """
        No expenses recorded yet.

        Add your first expense
        from the sidebar.
        """
    )