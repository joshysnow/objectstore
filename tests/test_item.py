#!/usr/bin/env python3
from objectstore import Item

class TestItem:

    def test_item_constructor_succeeds(self):
        item = Item(0, 'Pappa', 1)
        assert item.id == 0
        assert item.name == 'Pappa'
        assert item.colours == 1
