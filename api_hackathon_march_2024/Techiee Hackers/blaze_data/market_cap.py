import requests

from dotenv import load_dotenv
load_dotenv()
import os
API_KEY =os.getenv("BLAZEAI_API_KEY")

def get_market_cap(chain, start_date, end_date):

    url = "https://dashboard.withblaze.app/api/chain-insights/market_cap"


    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }


    payload = {
        "chain": chain,
        "start_date": start_date,
        "end_date": end_date
    }

    try:

        response = requests.get(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes


        token_prices = response.json()
        return {"status": "success", "data": token_prices}

    except requests.exceptions.RequestException as e:
        error_message = f"Error fetching token prices: {e}"
        print(error_message)
        return {"status": "error", "message": error_message}


def get_marketcap_data(chain,start_date,end_date):


    response = get_market_cap(chain, start_date, end_date)
    if response["status"] == "success":
        market_cap= response["data"]
        market_cap_dict = {price['date']: price['market_cap'] for price in  market_cap}
        print("Token Prices Dictionary:")
        print( market_cap_dict)

        return  market_cap_dict
    else:
        print("Failed to fetch token prices.")


