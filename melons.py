"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract class for all melon orders.""" 
    
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False 
        self.order_type = order_type
        self.tax = tax
       

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas melon":
            christmas_melons = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        
        # if qty is less than ten melons =$3 +international_order
        if self.qty < 10 and self.order_type == 'international':
                total = total + 3

        return total

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    def __init__(self, species, qty):
        super().__init__(species, qty, order_type, tax)   


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order with the US government."""
    
    def __init__(self, species, qty):
        super().__init__(species, qty, "government", 0.00)
        self.passed_inspection = False


    def mark_inspection(self, passed):
        """Record the fact that an inspection has passed."""

        self.passed_inspection = True