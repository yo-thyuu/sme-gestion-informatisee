# main.py - Session 1


# === DATA === list + disc the value
order = {
    "id": "PO-001",
    "supplier": "Fournisseur A",
    "lines": [
        {
            "variant": "Stylo vert",
            "sku": "SV-001",
            "qty": 10
        }
    ]
}

# /// DISPLAY \\\ using a def function called show_order
def show_order(order):
    print(f"Commande: {order['id']} - Fournisseur: {order['supplier']}")
    for line in order['lines']:
        print(f" - {line['variant']} ({line['sku']}): {line['qty']} units")


# \\ RUN // call the def function to input it's value stored
# using a special variable call recognize by python
if __name__ == "__main__":
    print("=" * 40)
    print("Systeme de gestion - PROTOTYPE")
    print("=" * 40)
    show_order(order)