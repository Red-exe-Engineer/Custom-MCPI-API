# Custom-MPCI-API
A new block.py that has every block/item ID and some search functions to help you remember them all!

Github said I should add this.
Just put it in your MCPI API dorectory and import *

Examples:

from mcpi.data import *

print(searchAll(search="sign"))

print(searchBlock(search="stone"))

print(searchItem(search="clock"))

blockID = Block("Block of Gold")
itemID = Item("Arrow")

print([blockID, itemID])
