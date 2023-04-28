import requests
import time

def main():
    url = input("Please enter the website URL to monitor: ")
    interval = int(input("Please enter the time interval between checks (in seconds): "))

    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{url} is up and running.")
            else:
                print(f"{url} is down. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{url} is down. Error: {e}")

        time.sleep(interval)

if __name__ == "__main__":
    main()
