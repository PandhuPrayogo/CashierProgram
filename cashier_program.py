# Start Project at: 07-02-2025 9:50:00 AM Wednesday
# Making a cashier program using python programming language

from datetime import datetime

# Saving data of cashier with tupples format
list_cashier = []
# Saving data of topup with tupples format
list_topup = []

# Blueprint of cashier (save information of cashier, return, and print list of cashier)
class Cashier:
    # Function to save information of cashier
    def __init__(self, name_cashier, id_cashier):
        self.name_cashier = name_cashier
        self.id_cashier = id_cashier
        list_cashier.append((self.name_cashier, self.id_cashier))

    # Function to give feedback after user input an information of cashier
    def __str__(self):
        return f"Name: {self.name_cashier} | ID: {self.id_cashier} added."
    
    # Function to print list of cashier
    def print_cashier():
        # When user haven't input the cashier information
        if not list_cashier:
            print("No cashier added yet.")
        else:
            for i, (n_cashier, id_cashier) in enumerate(list_cashier, start=1):
                print(f"{i}. Cashier name: {n_cashier}          |           Cashier ID: {id_cashier}")

# Function to print cash receipt
def transaction_process():
    # Initialize the date with the right time
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    # When user haven't input the top up amount
    if not list_topup:
        print("No top-up available.\n")
    else:
        print(f"""CASH RECEIPT
Adresss: Transmart MX Malang, Jl. Veteran No.8 lantai F4, Penanggungan, Kec. Klojen, Kota Malang, Jawa Timur 65113
======================================================================================================================
        """)
        for i, (p_topup, n_topup) in enumerate(list_topup, start=1): # Looping through the list of top up
            print(f"{i}. Price: {p_topup}              |                    ID: {n_topup}")
        t_topup = sum(sum_topup[0] for sum_topup in list_topup) # Sum of total top up
        print(f"Amount: Rp. {t_topup}")
        print(f"Time: {timestamp}\n")

# Main Program
while True:
    print("""Welcome to Cashier Program by Transstudio Mini Malang
    1. Add Cashier Information
    2. List of Cashier Information
    3. List of Top-up Value 
    4. Transaction Process
    5. Exit
    """)
    user_choice = int(input("Choose the right number do you want to take action: "))
    if user_choice == 1:
        while True: 
            cashier_name = str(input("Input cashier name: "))
            cashier_id = str(input("Input cashier ID: "))
            cashier_info = Cashier(cashier_name, cashier_id)

            print(cashier_info)
            cont_cashier = str(input("Do you want to insert another information (y/n)?: "))
            if cont_cashier.lower() == 'y':
                print("\n")
                continue
            elif cont_cashier.lower() == 'n':
                print("\n")
                break
            else:
                print(f"Please insert the right option!")
                print("\n")
                break

    elif user_choice == 2:
        print(Cashier.print_cashier())

    elif user_choice == 3:
        while True:
            print("""List of Top-up Value:
            1. Liburan Sekolah
            2. Promo Pelajar
            3. Diskon TravelokaBanjir Saldo
            4. Exit
            """)
            choose_promo = int(input("Choose one option on that list: "))
            if choose_promo == 1:
                print("""List of Top-up Value Liburan Sekolah:
                1. Paket 1: Rp. 75,000.00 (bonus 100%: Rp. 150,000.00)
                2. Paket 2: Rp. 100,000.00 (bonus 110%: Rp. 220,000.00)
                3. Paket 3: Rp. 250.000.00 (bonus 130%: Rp. 650,000.00)
                4. Paket 4: Rp. 500.000.00 (bonus 200%: Rp. 1,500,000.00)
                5. Exit
                """)
                promo1_choice = int(input("Choose one option on that list: "))
                if promo1_choice == 1:
                    price1_promo1 = 75000
                    textprice1_promo1 = "Paket 1"
                    list_topup.append((price1_promo1, textprice1_promo1))
                    print(f"Paket 1 added.")
                elif promo1_choice == 2:
                    price2_promo1 = 100000
                    textprice2_promo1 = "Paket 2"
                    list_topup.append((price2_promo1, textprice2_promo1))
                    print(f"Paket 2 added.")
                elif promo1_choice == 3:
                    price3_promo1 = 250000
                    textprice3_promo1 = "Paket 3"
                    list_topup.append((price3_promo1, textprice3_promo1))
                    print(f"Paket 3 added.")
                elif promo1_choice == 4:
                    price4_promo1 = 500000
                    textprice4_promo1 = "Paket 4"
                    list_topup.append((price4_promo1, textprice4_promo1))
                    print(f"Paket 4 added.")
                elif promo1_choice == 5:
                    break
                else:
                    print(f"Please insert the right option!")
                    continue

            elif choose_promo == 2:
                print("""List of Top-up Value Promo Pelajar:
                1. Pelajar SD: Rp. 100,000.00 (bonus 110%: Rp. 220,000.00)
                2. Pelajar SMP: Rp. 150,000.00 (bonus 120%: Rp. 330,000.00)
                3. Pelajar SMA: Rp. 200,000.00 (bonus 150%: Rp. 500,000.00)
                4. Exit
                """)
                promo2_choice = int(input("Choose one option on that list: "))
                if promo2_choice == 1:
                    price1_promo2 = 100000
                    textprice1_promo2 = "Pelajar SD"
                    list_topup.append((price1_promo2, textprice1_promo2))
                    print(f"Pelajar SD added.")
                elif promo2_choice == 2:
                    price2_promo2 = 150000
                    textprice2_promo2 = "Pelajar SMP"
                    list_topup.append((price2_promo2, textprice2_promo2))
                    print(f"Pelajar SMP added.")
                elif promo2_choice == 3:
                    price3_promo2 = 200000
                    textprice3_promo2 = "Pelajar SMA"
                    list_topup.append((price3_promo2, textprice3_promo2))
                    print(f"Pelajar SMA added.")
                elif promo2_choice == 4:
                    break
                else:
                    print(f"Please insert the right option!")
                    continue
            
            elif choose_promo == 3:
                print("""List of Top-up Value Promo Banjir Saldo:
                1. Combo 1: Rp. 200,000.00 (bonus 50%: Rp. 100,000.00)
                2. Combo 2: Rp. 250,000.00 (bonus 100%: Rp. 500,000.00)
                3. Combo 3: Rp. 300,000.00 (bonus 120%: Rp. 660,000.00)
                4. Combo 4: Rp. 500,000.00 (bonus 150%: Rp. 1,500,000.00)
                5. Exit
                """)
                promo3_choice = int(input("Choose one option on that list: "))
                if promo3_choice == 1:
                    price1_promo3 = 200000
                    textprice1_promo3 = "Combo 1"
                    list_topup.append((price1_promo3, textprice1_promo3))
                    print(f"Combo 1 added.")
                elif promo3_choice == 2:
                    price2_promo3 = 250000
                    textprice2_promo3 = "Combo 2"
                    list_topup.append((price2_promo3, textprice2_promo3))
                    print(f"Combo 2 added.")
                elif promo3_choice == 3:
                    price3_promo3 = 300000
                    textprice3_promo3 = "Combo 3"
                    list_topup.append((price3_promo3, textprice3_promo3))
                    print(f"Combo 3 added.")
                elif promo3_choice == 4:
                    price4_promo3 = 500000
                    textprice4_promo3 = "Combo 4"
                    list_topup.append((price4_promo3, textprice4_promo3))
                    print(f"Combo 4 added.")
                elif promo3_choice == 5:
                    break
                else:
                    print(f"Please insert the right option!")
                    continue

            elif choose_promo == 4:
                print("If you want to print the tax please choose option number 4 for transaction process\n")
                break

            else:
                print(f"Please insert the right option!")
                continue

    elif user_choice == 4:
        transaction_process()
    
    elif user_choice == 5:
        print("Thankyou for using this program, please rate my first project to learn data analyst and machine learning using python programming language! note: Thx -Yunzi Tech 2025")

    else:
        print(f"Please insert the right option!")
    
# Project 01: Yunzi Tech - @PandhuPrayogo