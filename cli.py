import argparse
from bot.orders import place_order
from bot.validators import validate_input
import logging
from bot.logging_config import setup_logging
import logging
setup_logging()

print("🚀 Script Started")  # DEBUG LINE

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

print("✅ Inputs received:", args)  # DEBUG LINE

error = validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

if error:
    print("❌ Error:", error)
else:
    print("📡 Placing Order...")
    
    response = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("📦 Response:", response)
    logging.info(response)