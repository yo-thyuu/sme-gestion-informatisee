# main.py - Session 1


# === DATA === list + dict
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

# /// DISPLAY \\\
def show_order(order):
    print(f"Commande: {order['id']} - Fournisseur: {order['supplier']}")
    for line in order['lines']:
        print(f" - {line['variant']} ({line['sku']}): {line['qty']} units")


# ||| RECEPTION |||
# 01 - classify accepted vs damaged from the received goods

def receive_goods(order_line, received_qty, damaged_qty, receipt_id="GR-001"):
    """Recevoir des marchandises et classifier / receive goods and classify"""
    accepted_qty = received_qty - damaged_qty

    receipt = {
       "id": receipt_id,
        "ordered_sku": order_line["sku"],
        "sku": order_line["sku"],
        "variant": order_line["variant"],
        "received_qty": received_qty,
        "accepted_qty":accepted_qty,
        "damaged_qty": damaged_qty,
    }
    # \n is for new line (breathing room)
    print(f"\n--- Receipt: {receipt['id']} ---")
    print(f"Variant: {receipt['variant']}")
    print(f"Received: {receipt['received_qty']}")
    print(f"Damaged: {receipt['damaged_qty']}")
    print(f"Accepted: {receipt['accepted_qty']}")

    # give back the aimed value
    return receipt

# \\ RUN //
# using a special variable call recognize by python
if __name__ == "__main__":
    print("=" * 40)
    print("Systeme de gestion - PROTOTYPE")
    print("=" * 40)

    #make the order
    show_order(order)

    #the order sent : 8 received / 1 damaged
    receipt = receive_goods(
        order["lines"][0],
        received_qty= 8,
        damaged_qty = 1
    )