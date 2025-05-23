# main.py

from bank_ops import create_account,transfer_money,view_last_5_transactions,view_full_history,show_menu,deposit_money,withdraw_money,view_balance
(
    show_menu,
    create_account,
    view_balance,
    deposit_money,
    withdraw_money,
    transfer_money,
    view_last_5_transactions,
    view_full_history
)

account = None

while True:
    show_menu()
    choice = input("Choose an option (1-8): ")
    if choice == '1':
        if account is None:
            account = create_account()
        else:
            print("Account already exists.")
    elif choice in ['2', '3', '4', '5', '6', '7']:
        if account is None:
            print("No account found. Please create one first.")
        elif choice == '2':
            view_balance(account)
        elif choice == '3':
            deposit_money(account)
        elif choice == '4':
            withdraw_money(account)
        elif choice == '5':
            transfer_money(account)
        elif choice == '6':
            view_last_5_transactions(account)
        elif choice == '7':
            view_full_history(account)
    elif choice == '8':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
