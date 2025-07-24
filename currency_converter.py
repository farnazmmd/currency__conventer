import requests

def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data["rates"]

def convert_currency(amount,from_currency, to_currency, rates):
    try:
        rate = rates[to_currency] / rates[from_currency]
        return amount * rate
    except KeyError:
        return None
    

def main():
    rates = get_exchange_rates()
    print("simple currency conventer: ")
    print("enter 'exit' for exit.")

    while True:
        from_cur = input("از چه ارزی میخوای تبدیل کنی؟ مثلا USD").upper()
        if from_cur == 'EXIT':
            break
        to_cur = input("به چه ارزی تبدیل بشه؟ مثلا EUR").upper()
        amount = input("مقدار چقدره؟")

        try:
            amount = float(amount)
            result = convert_currency(amount, from_cur, to_cur, rates)
            if result:
                print(f"{amount} {from_cur} = {result:.2f} {to_cur}")
            else:
                print("ارز وارد شده نامعتبر هست")
        except ValueError:
            print("لطفا عدد معتبر وارد کن")

main()
