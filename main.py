from orders_loader import load_orders_from_jsonl

if __name__ == "__main__":
    logs, marketplace_spending = load_orders_from_jsonl("./orders.jsonl")
    sorted_marketplace = dict(sorted(marketplace_spending.items(),
                                     key=lambda item: item[1],
                                     reverse=True))
    total_revenue = sum(sorted_marketplace.values())

    print(f'Total revenue: {total_revenue:.2f} EUR\n')
    print("Revenue by marketplace:")
    for m, c in marketplace_spending.items():
        print(f'{m}: {c} EUR')
    print("\n")
    print("suspicious orders:")
    for log in logs:
        print(log)
