# TrelloJSON2CSV
Mangle the json export from Trello to a csv that preserves key data

## Background
I was trying to get contents of a Trello board into airtable - and the export options of Trello were kinda unsatisfying.
So I set down and quickly parsed key contents of the Trello cards to create a csv that preserved
- Name of the card
- All labels set
- The assigned users
- Description
- Due date and whether completed
- Comments given

This CSV can be imported into Tools like Excel, Google Sheets, Airtable.

## How to use
1. Go to Trello and go to "Show menu", "More", "Print and Export", "Export as json"
2. Open your terminal
3. Run the script and pipe the json as STDIN
4. Get the CSV

e.g.
`# Trello_json_to_csv.py < GxNlkD8k.json > export.csv`

## Adjustments
In case you want to create files with different delimiters, change `sep` to e.g. `;`or `\t`
At some point, a command line argument for that may be added ;)