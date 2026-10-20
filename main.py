# main.py - Session 1


# === DATA === list + disc the value
# 00 - showing the order
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


# ||| RECEPTION ||| return value inside the function - in the list take the first item
# 01 - classify accepted vs damaged from thw received goods

def recieve_goods(order_line, recieved_qty, damaged_qty):
    """Recevoir des marchandises et classifier / receive goods and classify"""
    accepted_qty = recieved_qty - damaged_qty

    receipt = {
        "id": "GR-001", #always assign the keys to it's value in dict
        "order": order_line["sku"],
        "variant_recu": order_line["variant"],
        "quantite_recue": recieved_qty,
        "accepte": accepted_qty,
        "endommage": damaged_qty,
    }
    # \n is for new line (breathing room)
    print(f"\n--- Réception {receipt['id']} ---")
    print(f"Variante recue: {receipt['variant_recu']}")
    print(f"Quantite recue: {recieved_qty}")
    print(f"Endommage: {damaged_qty}")
    print(f"Accepte: {accepted_qty}")

    # give back the aimed value
    return receipt

# \\ RUN // call the def function to input the  value stored
# using a special variable call recognize by python
if __name__ == "__main__":
    print("=" * 40)
    print("Systeme de gestion - PROTOTYPE")
    print("=" * 40)

    #make the order
    show_order(order)

    #the order sent : 8 received / 1 damaged
    receipt = recieve_goods(order["lines"][0], recieved_qty = 8, damaged_qty = 1)