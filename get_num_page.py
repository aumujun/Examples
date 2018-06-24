from pyquery import PyQuery as pq

result = []
base_url = 'http://quotes.toscrape.com'
urls = [base_url]


def get_article(url):
    doc = pq(url)
    for i in range(len(doc('.text'))):
        result.append(doc('.text').eq(i).text())


def get_next_page(url):
    try:
        doc = pq(url)
        url = base_url + doc('.pager .next a').attr('href')
        urls.append(url)
        if url:
            get_next_page(url)
            return url
    except Exception:
        return


if __name__ == '__main__':
    get_next_page(base_url)
    for url in urls:
        get_article(url)
    print(len(result))
