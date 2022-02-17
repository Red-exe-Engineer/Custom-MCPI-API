# MCPI-Data Documentation

## Data dictionaries
- `mcpi.data.Block`/`blocks`: A list of all blocks and IDs
- `mcpi.data.Item`/`items`: A list of all items and IDs


## Search functions

- `mcpi.data.searchBlock(search: str = "", printName: bool = False) -> dict:` Searches a block in the blocks list
- `mcpi.data.searchItem(search: str = "", printName: bool = False) -> dict:` Searches an item in the items list.
- `mcpi.data.searchAll(search: str = "", printName: bool = False) -> dict:` Searches a query in both: Items and blocks 
- `main():` Interactive search shell

