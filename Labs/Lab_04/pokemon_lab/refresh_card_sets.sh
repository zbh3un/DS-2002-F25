#!/bin/bash

# Inform user we're refreshing all card sets
echo "Refreshing all card sets in card_set_lookup/"

# Loop through all JSON files in card_set_lookup/
for FILE in card_set_lookup/*.json; do
    # Extract the set ID from the filename
    SET_ID=$(basename "$FILE" .json)
    
    # Inform user we're updating this set
    echo "Updating set: $SET_ID"
    
    # Call the Pokemon TCG API and save to the file
    curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID" -o "$FILE"
    
    # Inform user the data was written
    echo "Data written to $FILE"
done

# Let user know all sets have been refreshed
echo "All card sets have been refreshed."
