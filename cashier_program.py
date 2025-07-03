# Start Project at: 07-02-2025 9:50:00 AM Wednesday
# Making a cashier program using python programming language

list_cashier = []
list_topup = []

class Cashier:
    def __init__(self, name_cashier, id_cashier):
        self.name_cashier = name_cashier
        self.id_cashier = id_cashier
        list_cashier.append((self.name_cashier, self.id_cashier))

    def __str__(self):
        return f"Name: {self.name_cashier} | ID: {self.id_cashier} added."
    
    def print_cashier():
        for index, cashier in list_cashier:
            print(index + ". ", cashier)
while True:

    print("""Welcome to Cashier Program by Transmart
    1. Add Cashier Information
    2. List of Cashier Information
    3. List of Top-up Value 
    4. Transaction Process
    5. Exit
    """)
    user_choice = int(input("Choose the right number do you want to take action: "))
    c = Cashier()
    if user_choice == 1:
        while True: 
            cashier_name = str(input("Input cashier name: "))
            cashier_id = str(input("Input cashier ID: "))
            cashier_info = c(cashier_name, cashier_id)

            print(cashier_info)
            cont_cashier = str(input("Do you want to insert another information (y/n)?: "))
            if cont_cashier.lower() == 'y':
                print("\n")
                continue
            elif cont_cashier.lower() == 'n':
                print("\n")
                break
            else:
                print(f"Your input ({cont_cashier}) is unorganized in this program. Please insert the right option!")
                print("\n")
                break

    if user_choice == 2:
        cashier = c(self.name_cashier, self.id_cashier)
        print(cashier.print_cashier())

    if user_choice == 3:
        while True:
            print("""List of Top-up Value:
            1. Liburan Sekolah
            2. Promo Pelajar
            3. Diskon Traveloka
            4. Promo Gila-Gilaan
            """)
            choose_promo = int(input("Choose one option on that list: "))
            if choose_promo == 1:
                print("""List of Top-up Value Liburan Sekolah:
                1. Paket 1: Rp. 75,000.00 (bonus 100%: Rp. 150,000.00)
                2. Paket 2: Rp. 100,000.00 (bonus 110%: Rp. 220,000.00)
                3. Paket 3: Rp. 250.000.00 (bonus 130%: Rp. 650,000.00)
                4. Paket 4: Rp. 500.000.00 (bonus 200%: Rp. 1,500,000.00)
                """)
                promo1_choice = int(input("Choose one option on that list: "))
                if promo1_choice == 1:
                    price_promo1 = 75000
                elif promo1_choice == 2:
                    price_promo1 = 100000
                elif promo1_choice == 3:
                    price_promo1 = 250000
                elif promo1_choice == 4:
                    price_promo1 = 500000
                else:
                    print(f"Your input ({promo1_choice}) is unorganized in this program. Please insert the right option!")
                    break

            elif choose_promo == 2:
                print("""List of Top-up Value Promo Pelajar:
                1. Pelajar SD: Rp. 100,000.00 (bonus 110%: Rp. 220,000.00)
                2. Pelajar SMP: Rp. 150,000.00 (bonus 120%: Rp. 330,000.00)
                3. Pelajar SMA: Rp. 200,000.00 (bonus 150%: Rp. 500,000.00)
                """)
                promo2_choice = int(input("Choose one option on that list: "))
                if promo2_choice == 1:
                    price_promo2 = 100000
                elif promo2_choice == 2:
                    price_promo2 = 150000
                elif promo2_choice == 3:
                    price_promo2 = 200000
                else:
                    print(f"Your input ({promo2_choice}) is unorganized in this program. Please insert the right option!")
                    break
            elif choose_promo == 4:
                print("""List of Top-up Value Promo Gila-Gilaan:
                """)
            elif choose_promo == 5:
                print("Thank you for using this program, i hope better today than before! Kamsahamnida~")
                break
            else:
                print(f"Your input ({promo2_choice}) is unorganized in this program. Please insert the right option!")
                continue