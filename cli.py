import logging
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logging

# Setup logging
setup_logging()

print("🚀 Trading Bot Started")

# 🔹 Interactive CLI Menu
def get_user_input():
    print("\n📊 Trading Bot Menu")

    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()

    side = input("Enter side (BUY/SELL): ").upper()
    while side not in ["BUY", "SELL"]:
        print("❌ Invalid input! Please enter BUY or SELL")
        side = input("Enter side (BUY/SELL): ").upper()

    order_type = input("Enter order type (MARKET/LIMIT): ").upper()
    while order_type not in ["MARKET", "LIMIT"]:
        print("❌ Invalid type! Please enter MARKET or LIMIT")
        order_type = input("Enter order type (MARKET/LIMIT): ").upper()

    # Quantity input with validation
    while True:
        try:
            quantity = float(input("Enter quantity: "))
            if quantity <= 0:
                print("❌ Quantity must be greater than 0")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number")

    price = None
    if order_type == "LIMIT":
        while True:
            try:
                price = float(input("Enter price: "))
                if price <= 0:
                    print("❌ Price must be greater than 0")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid number")

    return symbol, side, order_type, quantity, price


# 🔹 Get user input
symbol, side, order_type, quantity, price = get_user_input()

print("\n✅ Inputs received:")
print(f"Symbol: {symbol}, Side: {side}, Type: {order_type}, Quantity: {quantity}, Price: {price}")

# 🔹 Validate input
error = validate_input(symbol, side, order_type, quantity, price)

if error:
    print("❌ Error:", error)
    logging.error(f"Validation Error: {error}")
else:
    print("\n📡 Placing Order...")

    try:
        response = place_order(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\n📦 Order Response:")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Price:", response.get("price"))

        logging.info(f"Order Response: {response}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print("\n❌ Failed to place order:", str(e))
        logging.error(f"Order Error: {str(e)}")