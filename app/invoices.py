def calculate_invoice_total(items, tax_rate, discount_threshold, discount_rate):
    subtotal = 0
    for item in items:
        subtotal = subtotal + item["price"] * item["qty"]
    total = subtotal + subtotal * tax_rate
    if subtotal > discount_threshold:
        total = total - total * discount_rate
    return round(total, 2)
