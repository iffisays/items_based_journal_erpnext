# Items Based Journal

Add Item selection to Journal Entry with auto account population in ERPNext.

## Features

- **Item field in Journal Entry**: Select items directly in journal entry rows
- **Auto-fill Account**: Automatically populates account based on item"s default journal account
- **Default Journal Account**: New field in Item master to set the default account for journal entries
- **Item-wise Reports**: 
  - Item-wise Journal Entries
  - Item Ledger (with running balance)

## Installation

```bash
bench get-app https://github.com/iffisays/items_based_journal
bench --site your-site install-app items_based_journal
```

## Usage

1. Go to Item → Set "Default Journal Account"
2. In Journal Entry, select Item in the first column
3. Account will auto-fill based on the item"s default journal account

## License

MIT
