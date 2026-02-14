import time

def generate_bill():
    print("="*45)
    print("     🇮🇳  WELCOME TO PIZZA STORE   🇮🇳     ")
    print("="*45)
    time.sleep(0.5)

    bill = 0
    items = []

    # 1. Size Selection (Prices in Rupees)
    while True:
        print("\nAvailable Sizes: [S]mall: ₹199 | [M]edium: ₹399 | [L]arge: ₹599")
        size = input("Select Size (S/M/L): ").upper()
        if size == 'S':
            bill += 199
            items.append("Small Pizza Base    ₹199")
            break
        elif size == 'M':
            bill += 399
            items.append("Medium Pizza Base   ₹399")
            break
        elif size == 'L':
            bill += 599
            items.append("Large Pizza Base    ₹599")
            break
        else:
            print("❌ Invalid input! Please choose S, M, or L.")

    # 2. Local Toppings (Replacing Pepperoni)
    print("\n--- Customize Your Toppings ---")
    paneer = input("Add Peri-Peri Paneer? (₹50) [Y/N]: ").upper()
    if paneer == 'Y':
        bill += 50
        items.append("Peri-Peri Paneer    ₹50")

    capsicum = input("Add Extra Capsicum & Onion? (₹30) [Y/N]: ").upper()
    if capsicum == 'Y':
        bill += 30
        items.append("Veggie Delight Mix  ₹30")

    cheese = input("Extra Cheese Burst? (₹80) [Y/N]: ").upper()
    if cheese == 'Y':
        bill += 80
        items.append("Cheese Burst        ₹80")

    # 3. Tax Calculation (GST @ 5%)
    gst = bill * 0.05
    total_with_tax = bill + gst

    # 4. Final Professional Receipt
    print("\n" + "*"*40)
    print("          THE UNIQUE PIZZA MAKERS           ")
    print("          HINDUPUR, AP                ")
    print("*"*40)
    for item in items:
        print(item)
    print("-" * 40)
    print(f"Subtotal:           ₹{bill}")
    print(f"GST (5%):           ₹{gst:.2f}")
    print("-" * 40)
    print(f"TOTAL PAYABLE:      ₹{total_with_tax:.2f}")
    print("*" * 40)
    print("      Thank you! Visit Again!       ")
    print("="*45)

if __name__ == "__main__":
    generate_bill()
