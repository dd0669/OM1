import requests
import time
import sys

# 設定目標：以太幣
COIN_ID = "ethereum"
CURRENCY = "usd"
# 設定一個心中的「底價」，跌破這個就要叫
ALERT_PRICE = 3000 

def get_crypto_price():
    """ 感知層 (Perception): 去網路上抓價格 """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={COIN_ID}&vs_currencies={CURRENCY}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        return data[COIN_ID][CURRENCY]
    except Exception as e:
        print(f"❌ Network Error: {e}")
        return None

def brain_process(price):
    """ 大腦層 (Brain): 判斷價格好壞 """
    if price is None:
        return "SLEEP", "Cannot fetch data"

    if price < ALERT_PRICE:
        return "PANIC", f"📉 ALERT! Price dropped to ${price}!"
    else:
        return "HAPPY", f"📈 All good. Price is ${price}."

def run_agent():
    print(f"🤖 Crypto Watchdog initialized. Monitoring {COIN_ID}...")
    print(f"🎯 Threshold: ${ALERT_PRICE}")
    print("------------------------------------------------")

    # 模擬機器人的無限迴圈 (按 Ctrl+C 停止)
    try:
        while True:
            # 1. Sense (感知)
            current_price = get_crypto_price()

            # 2. Think (思考)
            mood, message = brain_process(current_price)

            # 3. Act (行動)
            if mood == "PANIC":
                print(f"🚨 [ACTION] Barking loud: {message}")
            elif mood == "HAPPY":
                print(f"✅ [ACTION] Wagging tail: {message}")
            else:
                print(f"💤 [ACTION] Sleeping...")

            # 休息 10 秒避免被 API 封鎖
            time.sleep(10)

    except KeyboardInterrupt:
        print("\n👋 Agent shutdown.")

if __name__ == "__main__":
    run_agent()
