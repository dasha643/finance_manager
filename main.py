from transactions import (
    add_transaction,
    show_transaction,
    filter_by_category
)
from statistics import (
    calculate_income,
    calculate_expenses,
    calculate_balance
)

def main():
    transactions = []

    try:
        add_transaction(transactions, "income", 15000, "salary", "monthly salary")
        add_transaction(transactions, "expense", 25000, "food", "groceries")
    except ValueError:
        pass

    while True:
        print("\n========== FINANCE MANAGER ==========")
        print("\n1. додати дохід")
        print("2. додати витрату")
        print("3. переглянути всі транзакції")
        print("4. показати загальний дохід")
        print("5. показати загальні витрати")
        print("6. показати поточний баланс")
        print("7. фільтрація за категорією")
        print("0. вихід\n")

        choice = input("оберіть дію").strip()

        if choice == "1":
            try:
                amount = float(input("введіть суму доходу "))
                category = input("введіть категорію ")
                description = input("введіть опис: ")
                add_transaction(transactions, "income", amount, category, description)
                print("дохід додано")
            except ValueError as e:
                print(f"помилка {e}")

        elif choice == "2":
            try:
                amount = float(input("введіть суму витрати "))
                category = input("введіть категорію ")
                description = input("введіть опис ")
                add_transaction(transactions, "expense", amount, category, description)
                print("витрату додано")
            except ValueError as e:
                print(f"помилка {e}")

        elif choice == "3":
            show_transaction(transactions)

        elif choice == "4":
            income = calculate_income(transactions)
            print(f"\nзагальний дохід {income}")

        elif choice == "5":
            expenses = calculate_expenses(transactions)
            print(f"\nзагальні витрати {expenses}")

        elif choice == "6":
            balance = calculate_balance(transactions)
            print(f"\nпоточний баланс {balance}")

        elif choice == "7":
            category = input("введіть категорію для фільтрації ")
            filter_by_category(transactions, category)

        elif choice == "0":
            print("\nвихід з програми")
            break
        else:
            print("\nнеправильний вибір. оберіть пункт від 0 до 7")

if __name__ == "__main__":
    main()