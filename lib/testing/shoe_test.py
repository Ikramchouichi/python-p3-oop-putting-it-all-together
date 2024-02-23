import pytest
from shoe import Shoe

class TestShoe:
    def test_has_brand_and_size(self):
        """has the brand and size passed to __init__, and values can be set to new instance."""
        shoe = Shoe("Adidas", 9, "White")
        assert shoe.brand == "Adidas"
        assert shoe.size == 9
        assert shoe.color == "White"

    def test_requires_int_size(self):
        """prints 'size must be an integer' if size is not an integer."""
        # This is a conceptual test; actual implementation may vary based on how you handle non-integer sizes
        with pytest.raises(ValueError):
            Shoe("Adidas", "not an integer", "White")

    def test_can_cobble(self):
        """says that the shoe has been repaired."""
        shoe = Shoe("Adidas", 9, "White")
        shoe.cobble()
        assert shoe.condition == "New"

    def test_cobble_makes_new(self):
        """creates an attribute on the instance called 'condition' and set equal to 'New' after repair."""
        shoe = Shoe("Adidas", 9, "White")
        shoe.cobble()
        assert shoe.condition == "New"
