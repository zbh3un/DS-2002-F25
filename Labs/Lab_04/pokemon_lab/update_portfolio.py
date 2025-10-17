#!/usr/bin/env python3

import pandas as pd
import json
import os
import sys


def _load_lookup_data(lookup_dir):
    """Load and process JSON card lookup data from the lookup directory."""
    all_lookup_df = []
    
    # Loop through all JSON files in the lookup directory
    for filename in os.listdir(lookup_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(lookup_dir, filename)
            
            # Load JSON data
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            # Flatten JSON into DataFrame
            df = pd.json_normalize(data['data'])
            
            # Price Calculation: prioritize holofoil, then normal, fill missing with 0.0
            df['card_market_value'] = df.get('tcgplayer.prices.holofoil.market', 0.0).fillna(
                df.get('tcgplayer.prices.normal.market', 0.0)
            ).fillna(0.0)
            
            # Rename columns
            df = df.rename(columns={
                'id': 'card_id',
                'name': 'card_name',
                'number': 'card_number',
                'set.id': 'set_id',
                'set.name': 'set_name'
            })
            
            # Define required columns
            required_cols = ['card_id', 'card_name', 'card_number', 'set_id', 'set_name', 'card_market_value']
            
            # Append copy of the DataFrame
            all_lookup_df.append(df[required_cols].copy())
    
    # Concatenate all DataFrames
    lookup_df = pd.concat(all_lookup_df, ignore_index=True)
    
    # Clean duplicates: sort by value and keep first (highest)
    lookup_df = lookup_df.sort_values('card_market_value', ascending=False).drop_duplicates(subset=['card_id'], keep='first')
    
    return lookup_df


def _load_inventory_data(inventory_dir):
    """Load and process CSV inventory data from the inventory directory."""
    inventory_data = []
    
    # Loop through all CSV files in the inventory directory
    for filename in os.listdir(inventory_dir):
        if filename.endswith('.csv'):
            filepath = os.path.join(inventory_dir, filename)
            df = pd.read_csv(filepath)
            inventory_data.append(df)
    
    # Check if inventory_data is empty
    if not inventory_data:
        return pd.DataFrame()
    
    # Concatenate all DataFrames
    inventory_df = pd.concat(inventory_data, ignore_index=True)
    
    # Create unified key: card_id
    inventory_df['card_id'] = inventory_df['set_id'].astype(str) + '-' + inventory_df['card_number'].astype(str)
    
    return inventory_df


def update_portfolio(inventory_dir, lookup_dir, output_file):
    """Main ETL function to merge inventory and lookup data, then output portfolio CSV."""
    # Load data using helper functions
    lookup_df = _load_lookup_data(lookup_dir)
    inventory_df = _load_inventory_data(inventory_dir)
    
    # Handle empty inventory
    if inventory_df.empty:
        print("Error: No inventory data found.", file=sys.stderr)
        # Create empty portfolio CSV with headers
        empty_df = pd.DataFrame(columns=['card_name', 'card_id', 'set_name', 'card_market_value', 'index'])
        empty_df.to_csv(output_file, index=False)
        return
    
    # Data Merge: join inventory with lookup data on card_id
    portfolio_df = pd.merge(
        inventory_df,
        lookup_df[['card_id', 'set_name', 'card_market_value']],
        on='card_id',
        how='left'
    )
    
    # Final Cleaning
    portfolio_df['card_market_value'] = portfolio_df['card_market_value'].fillna(0.0)
    portfolio_df['set_name'] = portfolio_df['set_name'].fillna('NOT_FOUND')
    
    # Index Creation: create location index
    portfolio_df['index'] = (
        portfolio_df['binder_name'].astype(str) + '-' +
        portfolio_df['page_number'].astype(str) + '-' +
        portfolio_df['slot_number'].astype(str)
    )
    
    # Define final columns
    final_cols = ['card_name', 'card_id', 'set_name', 'card_market_value', 'index']
    
    # Write to CSV
    portfolio_df[final_cols].to_csv(output_file, index=False)
    
    print(f"Portfolio successfully updated and saved to {output_file}")


def main():
    """Run the production pipeline."""
    update_portfolio('./card_inventory/', './card_set_lookup/', 'card_portfolio.csv')


def test():
    """Run the test pipeline."""
    update_portfolio('./card_inventory_test/', './card_set_lookup_test/', 'test_card_portfolio.csv')


if __name__ == "__main__":
    print("Running in Test Mode...", file=sys.stderr)
    test()
