import os
import requests
from datetime import date

def main():
    # target_url = os.getenv("TARGET_URL")
    target_url = "https://pontoon.mozilla.org/static/revision.txt"

    try:
        response = requests.get(target_url, timeout=10)
        response.raise_for_status()

        text = response.text
        print(f"Successfully fetched data for: {text}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
            print("release=false", file=fh)


    if text.startswith("v20"):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
            print("release=false", file=fh)


    version = "v" + date.today().strftime("%Y.%m.%d")


    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f"version={version}", file=fh)
        print("release=true", file=fh)



    print(version)



if __name__ == "__main__":
    main()
