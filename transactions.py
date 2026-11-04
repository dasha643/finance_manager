def add_transaction(transactions, transaction_type, amount, category, description):
    """додає нову транзакцію до списку"""
    if transaction_type not in ["income", "expense"]:
        raise ValueError("тип транзакції має бути income або expense")
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("сума має бути додатнім")
    if not category or not str(category).strip():
        raise ValueError("категорія не має бути порожньою")
    if not description or not str(description).strip():
        raise ValueError("опис не має бути порожнім")

    new_id = 1 if not transactions else transactions[-1]["id"] + 1

    transaction = {
        "id": new_id,
        "type": transaction_type,
        "amount": amount,
        "category": category.strip(),
        "description": description.strip()
    }

    transactions.append(transaction)
    return transaction


def show_transaction(transactions):
    """виводить усі транзакції у табличці"""
    if not transactions:
        print("список порожній")
        return

    print(f"{'ID'} | {'Type'} | {'Amount'} | {'Category'} | {'Description'}")
    for t in transactions:
        print(f"{t['id']} | {t['type']} | {t['amount']} | {t['category']} | {t['description']}")


def filter_by_category(transactions, category):
    """фільтрує та виводить транзакцію за категорією"""
    category_lower = category.strip().lower()
    filtered = [t for t in transactions if t["category"].lower() == category_lower]

    if not filtered:
        print("транзакцію у категорії не знайдено")
    else:
        print("відфільтровані транзакції для категорії")
        print(f"{'ID'} | {'Type'} | {'Amount'} | {'Category'} | {'Description'}")
        for t in filtered:
            print(f"{t['id']} | {t['type']} | {t['amount']} | {t['category']} | {t['description']}")
        return filtered
