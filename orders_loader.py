import json
from datetime import datetime
from order import Order
from order_validator import validate_order


def parse_datetime(value: str) -> datetime:
    """Convertit une chaîne ISO 8601 (avec 'Z' pour UTC) en objet datetime."""
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_orders_from_jsonl(filepath: str) -> tuple[list, dict]:
    """
    Charge et valide les commandes depuis un fichier JSONL.

    Lit un fichier JSONL ligne par ligne, crée des objets Order et les valide.
    Les erreurs de parsing JSON ou de champs sont capturées et loggées.

    Args:
        filepath: Chemin vers le fichier JSONL contenant les commandes

    Returns:
        Tuple contenant :
            - logs (list): Liste des messages d'erreur de validation
            - marketplace_spending (dict): Dictionnaire
            {marketplace: montant_total_en_euros}

    Raises:
        Aucune exception n'est levée,
        toutes les erreurs sont capturées et ajoutées aux logs

    """
    logs = []
    marketplace_spending = {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                order = Order(
                    id=data["id"],
                    marketplace=data["marketplace"],
                    country=data["country"],
                    amount_cents=data["amount_cents"],
                    created_at=parse_datetime(data["created_at"]),
                )
                logs, marketplace_spending = validate_order(
                    order, logs, marketplace_spending
                )
    except json.JSONDecodeError as e:
        logs.append(f"Invalid JSON: {e}")
    except KeyError as e:
        logs.append(f"Missing required field: {e}")
    return logs, marketplace_spending
