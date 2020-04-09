from bs4 import BeautifulSoup
from ..models import PageLink
import requests
from urllib.parse import urljoin, urlparse, urldefrag
import pdb


headers = requests.utils.default_headers()
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'

def scrape(url):

    headers.update({'User-Agent': USER_AGENT})

    r = requests.get(url)

    raw_html = r.content

    content = BeautifulSoup(raw_html, 'html.parser')

    links = content.select('body a')

    visited_urls = []

    for link in links:
        child_url = get_parsed_url(
            link.get('href'), url)

        if not child_url:
            continue

        if child_url in visited_urls:
            continue

        query = PageLink.objects.filter(
            url=child_url)

        if len(query) > 0:
            continue

        visited_urls.append(child_url)


        r2 = requests.get(child_url, headers=headers)

        child_html = r2.content

        child_content = BeautifulSoup(child_html, 'html.parser')

        print(child_url)
        preview_dict = {
            'name': link.text,
            'title': get_title(child_content),
            'description': get_description(child_content),
            'source': get_site_name(child_content, url),
            'url': child_url
        }

        page_link = PageLink(**preview_dict)

        try:
            page_link.save()
        except:
            print('Error saving url', child_url)


def get_title(link):
    """Attempt to get a title."""
    title = None
    if link.title is None:
        if link.find("h1") is not None:
            title = link.find("h1")
    elif link.title.string is not None:
        title = link.title.string

    return title


def get_description(link):
    """Attempt to get description."""
    description = ''
    if link.find("meta", property="og:description") is not None:
        description = link.find("meta", property="og:description").get('content')
    elif link.find("p") is not None:
        description = link.find("p").content
    return description


def get_site_name(link, url):
    """Attempt to get the site's base name."""
    sitename = ''
    if link.find("meta", property="og:site_name") is not None:
        sitename = link.find("meta", property="og:site_name").get('content')
    else:
        sitename = url.split('//')[1]
        name = sitename.split('/')[0]
        name = sitename.rsplit('.')[1]
        return name
    return sitename

def get_parsed_url(url, domain):
    """
    Checks whether url is a valid URL.
    """
    url_parser = urlparse(url)
    domain_parser = urlparse(domain)

    parsed_url = None

    if url_parser.netloc == domain_parser.netloc:
        parsed_url = urljoin(domain, url_parser.path)
        parsed_url = urldefrag(parsed_url)[0]

    elif url_parser.scheme == '':
        parsed_url = urljoin(domain, url_parser.path)
        parsed_url = urldefrag(parsed_url)[0]
    elif url_parser.netloc != domain:
        parsed_url = None

    return parsed_url