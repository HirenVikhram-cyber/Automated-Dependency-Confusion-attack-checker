#!/bin/bash

# Define the file containing URLs
url_file="scripterout2.txt"

# Define the file containing words to match
word_file="non_existent_packages2.txt"

# Loop through each URL in the url_file
while IFS= read -r url; do
    # Curl the URL and store the output in a variable
    output=$(curl -s "$url")

    # Loop through each word in the word_file
    while IFS= read -r word; do
        # Check if the output contains the word
        if [[ $output =~ $word ]]; then
            echo "URL: $url, Matched Word: $word"
        fi
    done < "$word_file"
done < "$url_file"