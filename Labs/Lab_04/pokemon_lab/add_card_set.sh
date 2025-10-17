#!/bin/bash

# Prompt user for Set ID
read -p "Enter the TCG Card Set ID (e.g., base1, base4): " SET_ID

# Check if SET_ID is empty
if [ -z "$SET_ID" ]; then
    echo "Error: Set ID cannot be empty." >&2
    exit 1
fi

# Inform user we're fetching data
echo "Fetching card data for set: $SET_ID"

# Call the Pokemon TCG API and save to card_set_lookup directory
curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID" -o "card_set_lookup/$SET_ID.json"

echo "Card data saved to card_set_lookup/$SET_ID.json"
