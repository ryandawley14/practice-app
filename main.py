from app.config import load_config
from app.invoices import calculate_invoice_total
from app.legacy_batch import run_batch

if __name__ == "__main__":
    cfg = load_config("config.yaml")
    items = [{"price": 120.0, "qty": 3}, {"price": 80.0, "qty": 2}]
    print(calculate_invoice_total(items, cfg["tax_rate"], cfg["discount_threshold"], cfg["discount_rate"]))
    run_batch("sample_export.txt", "out.csv")
