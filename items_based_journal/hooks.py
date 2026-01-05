app_name = "items_based_journal"
app_title = "Items Based Journal"
app_publisher = "iffisays"
app_description = "Add Item selection to Journal Entry with auto account population"
app_email = "iffisays@gmail.com"
app_license = "MIT"
app_version = "1.0.0"

# Fixtures - these will be installed when the app is installed
fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            ["name", "in", [
                "Item-default_journal_account",
                "Journal Entry Account-custom_item"
            ]]
        ]
    },
    {
        "dt": "Client Script",
        "filters": [
            ["name", "=", "JE Item to Account Auto-Fill"]
        ]
    },
    {
        "dt": "Report",
        "filters": [
            ["name", "in", [
                "Item-wise Journal Entries",
                "Item Ledger"
            ]]
        ]
    }
]

# Required apps
required_apps = ["frappe", "erpnext"]
