import os
import pandas as pd

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def analyze_expenses(data):

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Amount",
            "Category",
            "Description",
            "Date"
        ]
    )

    prompt = f"""
    You are a financial advisor.

    Analyze the spending data below:

    {df.to_string()}

    Provide:

    1. Spending Summary
    2. Spending Patterns
    3. Areas of Concern
    4. Savings Recommendations
    5. Weekly Financial Action Plan

    Keep the response concise.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


def ask_finance_bot(
    data,
    question
):

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Amount",
            "Category",
            "Description",
            "Date"
        ]
    )

    prompt = f"""
    You are an AI Finance Assistant.

    Expense Records:

    {df.to_string()}

    User Question:

    {question}

    Answer clearly and practically.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text