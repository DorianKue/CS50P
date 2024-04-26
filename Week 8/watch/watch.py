import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Extracting the Youtube URL from HTML by searching for the src attribute containing a Youtube URL, making the "s" in "https", and the "www." optional. Then capturing the video id/link after then last "/" in a group.
    if matches := re.search(
        r"src=\"https?://(?:www\.)?youtube\.com/embed/([\w]+?)\"", s
    ):
        # Returning the video URL in the shorter more shareable form.
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
