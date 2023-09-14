def cleaner(url: str) -> str:
    for i in range(len(url) - 1, -1, -1):
        if url[i] == "/":
            url = url[i + 1:]
            break
        elif i == 0:
            raise AttributeError("Error! Not an url.")
        
    return url


if __name__ == "__main__":
    print(cleaner("https://i.4cdn.org/x/1693545450077124.jpg"))
