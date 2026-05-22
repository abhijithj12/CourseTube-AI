def url_validation(url):
    return (
        url.startswith("https://www.youtube.com/watch")
        or url.startswith("https://youtu.be/")
    )