#!/usr/bin/env python3

import pandas as pd
import os
import sys


def generate_summary(portfolio_file):
    """Read the portfolio CSV and generate a summary report."""
    # Check if portfolio file exists
    if not os.path.exists(portfolio_file):
        print(f"Error: Portfolio file '{portfolio_file}' not found.", file=sys.stderr)
        sys.exit(1)
    
    # Read the CSV file
    df = pd.read_csv(portfolio_file)
    
    # Check if DataFrame is empty
    if df.empty:
        print("Portfolio is empty. No data to summarize.")
        return
    
    # Calculate Total Value
    total_portfolio_value = df['card_market_value'].sum()
    
    # Find Most Valuable Card
    most_valuable_card = df.loc[df['card_market_value'].idxmax()]
    
    # Print Report
    print("\n" + "="*50)
    print("PORTFOLIO SUMMARY")
    print("="*50)
    print(f"\nTotal Portfolio Value: ${total_portfolio_value:,.2f}")
    print(f"\nMost Valuable Card:")
    print(f"  Name: {most_valuable_card['card_name']}")
    print(f"  ID: {most_valuable_card['card_id']}")
    print(f"  Value: ${most_valuable_card['card_market_value']:,.2f}")
    print("\n" + "="*50 + "\n")


def main():
    """Run the production report."""
    generate_summary('card_portfolio.csv')


def test():
    """Run the test report."""
    generate_summary('test_card_portfolio.csv')


if __name__ == "__main__":
    test()
