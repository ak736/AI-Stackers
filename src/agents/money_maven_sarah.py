import json
import os
import time

# Define the path to Sarah's "database"
TRANSFERS_PATH = os.path.join(
    'assets', 'sarah', 'json', 'savings_transfers.json')


def setup_auto_transfer(amount: float, frequency: str) -> dict:
    """
    Simulates setting up an auto-transfer by writing to Sarah's JSON file.
    """
    print(
        f"💰 Money Maven Sarah: Setting up a {frequency} transfer of ${amount}...")

    new_transfer = {
        "transfer_id": f"TRN{int(time.time())}",
        "amount": amount,
        "frequency": frequency,
        "start_date": time.strftime("%Y-%m-%d"),
        "status": "active"
    }

    try:
        # This assumes the file already exists and contains a list
        with open(TRANSFERS_PATH, 'r+') as f:
            transfers = json.load(f)
            transfers.append(new_transfer)
            f.seek(0)
            f.truncate()
            json.dump(transfers, f, indent=4)

        print(
            f"✅ Money Maven Sarah: Success! Auto-transfer is active. ID: {new_transfer['transfer_id']}")
        return new_transfer

    except Exception as e:
        print(f"❌ ERROR: Sarah failed to write to her transfers file. {e}")
        return {"status": "failed"}
