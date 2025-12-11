import unittest
from decimal import Decimal
from orders_loader import load_orders_from_jsonl


class OrdersLoaderTest(unittest.TestCase):
    """Tests pour le chargement et le traitement des commandes."""

    TEST_FILE = "order_test.jsonl"

    def setUp(self):
        """Préparation avant chaque test."""
        self.processed_logs, self.marketplace_expenses = (
            load_orders_from_jsonl(self.TEST_FILE)
        )

    def test_logs_contain_negative_amount_entry(self):
        """Vérifie que les logs contiennent
        l'entrée pour un montant négatif."""
        expected_log_entry = "- o3: negative amount (-500)"
        self.assertIn(expected_log_entry, self.processed_logs)

    def test_logs_contain_empty_marketplace_entry(self):
        """Vérifie que les logs contiennent
        l'entrée pour un marketplace vide."""
        expected_log_entry = "- o2: empty marketplace"
        self.assertIn(expected_log_entry, self.processed_logs)

    def test_total_marketplace_spending_correct(self):
        """Vérifie que le total des dépenses par marketplace est correct."""
        actual_total = sum(self.marketplace_expenses.values())
        expected_total = Decimal("25.99")

        self.assertEqual(
            actual_total,
            expected_total,
            f"Le total des dépenses ({actual_total})"
            f"ne correspond pas au montant attendu ({expected_total})"
        )

    def test_marketplace_expenses_structure(self):
        """Vérifie que les dépenses par
        marketplace ont la structure attendue."""
        self.assertIsInstance(
            self.marketplace_expenses,
            dict,
            "Les dépenses devraient être un dictionnaire"
            )

        # Vérifie que toutes les valeurs sont des Decimal
        for marketplace, amount in self.marketplace_expenses.items():
            self.assertIsInstance(
                amount,
                Decimal,
                f'Le montant pour {marketplace} devrait être un Decimal'
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
