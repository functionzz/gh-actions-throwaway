import os
import requests
from datetime import date

def main():
    # target_url = os.getenv("TARGET_URL")
    target_url = "https://pontoon.mozilla.org/static/revision.txt"

    try:
        response = requests.get(target_url, timeout=10)
        response.raise_for_status()

        commit = response.text
        print(f"Successfully fetched data for: {commit}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
            print("release=false", file=fh)
        return

# fetch commit sha

# get commit tag, check if it includes v20*

# if yes, end
# if no, tag commit with generated semver
# release with generated semver as the title.

    if commit.startswith("v20"):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
            print("release=false", file=fh)
        return


    version = "v" + date.today().strftime("%Y.%m.%d")


    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(commit)
        print(f"version={version}", file=fh)
        print("release=true", file=fh)

    print(version)
    return



if __name__ == "__main__":
    main()
