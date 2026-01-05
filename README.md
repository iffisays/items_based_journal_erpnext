# Items Based Journal

Add Item selection to Journal Entry with auto account population in ERPNext.

## Features

- **Item field in Journal Entry**: Select items directly in journal entry rows
- **Auto-fill Account**: Automatically populates account based on item's default journal account
- **Default Journal Account**: New field in Item master to set the default account for journal entries
- **Item-wise Reports**:
  - Item-wise Journal Entries
  - Item Ledger (with running balance)

## Installation

```bash
# Get the app (use --skip-assets as this app has no frontend assets)
bench get-app https://github.com/iffisays/items_based_journal_erpnext --skip-assets

# Install on your site
bench --site your-site install-app items_based_journal

# Run migrate to sync fixtures
bench --site your-site migrate

# Clear cache
bench --site your-site clear-cache
```

## Usage

1. Go to Item → Set "Default Journal Account" field
2. In Journal Entry, select Item in the first column of the accounts table
3. Account will auto-fill based on the item's default journal account

## Reports

- **Item-wise Journal Entries**: View all journal entries by item with filters for date range and company
- **Item Ledger**: View running balance for a specific item across all journal entries

## License

MIT
