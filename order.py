from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(frozen=True)
class Order:
    """
    Représente une commande immuable avec validation
    et conversion de montants.
    """
    id: str
    marketplace: str
    country: str
    amount_cents: int
    created_at: datetime

    @property
    def amount_euros(self) -> Decimal:
        """Convertit le montant de centimes en euros avec précision Decimal."""
        return Decimal(str(self.amount_cents)) / Decimal('100')
