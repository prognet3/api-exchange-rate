import requests
import schedule
import time
from win10toast import ToastNotifier


def api_exchange_rates():
    url = "https://api.accessban.com/v1/data/sana/json"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_api = response.json()
    value_sana = response_api["sana"]
    value_data = value_sana["data"]
    toast = ToastNotifier()
    fileforlog = open("C:/Users/a_zamanpour/Desktop/log.txt", "a+", encoding="utf-8")
    for i in range(len(value_data)):
        print("{:<20},{:^20},{:>20}".format(value_data[i]["title"], value_data[i]["p"], value_data[i]["updated_at"]))
        fileforlog.write("{} , {} , {}".format(value_data[i]["title"], value_data[i]["p"], value_data[i]["updated_at"]))
        fileforlog.write('\n')
    print('\n')
    toast.show_toast("Dollar", str(value_data[0]["p"]))


schedule.every(10).seconds.do(api_exchange_rates)
while True:
    schedule.run_pending()
    time.sleep(1)

