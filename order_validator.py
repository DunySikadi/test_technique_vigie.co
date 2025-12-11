from order import Order


def validate_order(data: Order, logs: list, marketplace_spending: dict):
    """
    Valide une commande et met à jour les logs et les dépenses par marketplace.
    Args:
        order: La commande à valider
        logs: Liste des logs d'erreur
        marketplace_spending: Dictionnaire des dépenses par marketplace
    Returns:
        Tuple contenant (logs mis à jour, marketplace_spending mis à jour)
    """
    has_error = False
    if data.amount_cents < 0:
        logs.append(f'- {data.id}: negative amount ({data.amount_cents})')
        has_error = True
    if not data.marketplace:
        logs.append(f'- {data.id}: empty marketplace')
        has_error = True
    if not has_error:
        if data.marketplace not in marketplace_spending:
            marketplace_spending[data.marketplace] = data.amount_euros
        else:
            marketplace_spending[data.marketplace] += data.amount_euros
    return logs, marketplace_spending
