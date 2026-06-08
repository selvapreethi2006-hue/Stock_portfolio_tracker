# Stock Portfolio Tracker
# Hardcoded stock prices (symbol: price per share)
STOCK_PRICES = {
    "AAPL": 180.0,   # Apple
    "TSLA": 250.0,   # Tesla
    "GOOGL": 140.0,  # Google
    "AMZN": 130.0,   # Amazon
    "MSFT": 330.0    # Microsoft
}

def get_portfolio_from_user():
    """Interactively ask user for stock symbols and quantities."""
    portfolio = []  # list of tuples (symbol, quantity)
    print("\n=== Stock Portfolio Tracker ===")
    print("Enter stock symbols (e.g., AAPL, TSLA) and quantity.")
    print(f"Supported symbols: {', '.join(STOCK_PRICES.keys())}")
    print("Type 'done' when finished.\n")

    while True:
        symbol = input("Stock symbol (or 'done'): ").strip().upper()
        if symbol == 'DONE':
            break
        if symbol not in STOCK_PRICES:
            print(f"❌ '{symbol}' not found in price list. Please try again.")
            continue
        
        # Quantity input
        try:
            qty = int(input(f"Quantity of {symbol}: "))
            if qty <= 0:
                print("⚠️ Quantity must be positive. Please re-enter.")
                continue
        except ValueError:
            print("⚠️ Invalid number. Please enter an integer quantity.")
            continue
        
        portfolio.append((symbol, qty))
        print(f"✅ Added {qty} shares of {symbol}.\n")
    
    return portfolio

def calculate_total_value(portfolio):
    """Compute total investment value based on hardcoded prices."""
    total = 0.0
    details = []
    for symbol, qty in portfolio:
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        details.append((symbol, qty, price, value))
    return total, details

def save_to_file(portfolio, total, details, filename):
    """Save portfolio and total to a file (supports .txt or .csv)."""
    if filename.lower().endswith('.csv'):
        # CSV format
        with open(filename, 'w') as f:
            f.write("Symbol,Quantity,Price per Share,Total Value\n")
            for sym, qty, price, val in details:
                f.write(f"{sym},{qty},{price:.2f},{val:.2f}\n")
            f.write(f"\nGRAND TOTAL,{total:.2f}\n")
        print(f"✅ Portfolio saved to {filename} (CSV format).")
    else:
        # Default: plain text
        with open(filename, 'w') as f:
            f.write("STOCK PORTFOLIO SUMMARY\n")
            f.write("=======================\n")
            for sym, qty, price, val in details:
                f.write(f"{sym}: {qty} shares @ ${price:.2f} = ${val:.2f}\n")
            f.write("=======================\n")
            f.write(f"TOTAL INVESTMENT VALUE: ${total:.2f}\n")
        print(f"✅ Portfolio saved to {filename} (TXT format).")

def main():
    portfolio = get_portfolio_from_user()
    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return
    
    total_value, details = calculate_total_value(portfolio)
    
    # Display results
    print("\n=== Portfolio Summary ===")
    for sym, qty, price, val in details:
        print(f"{sym}: {qty} shares @ ${price:.2f} = ${val:.2f}")
    print(f"\n💰 TOTAL INVESTMENT: ${total_value:.2f}\n")
    
    # Optional file saving
    save_choice = input("Do you want to save the result to a file? (y/n): ").strip().lower()
    if save_choice == 'y':
        filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ").strip()
        if not filename:
            filename = "portfolio.txt"
        save_to_file(portfolio, total_value, details, filename)

if __name__ == "__main__":
    main()