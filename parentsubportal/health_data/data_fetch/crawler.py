from bs4 import BeautifulSoup
from ..models import PageLink
import re
import requests
from urllib.parse import urljoin, urlparse, urldefrag
import pdb
from posts.models import PDF
from django.core.files import File


headers = requests.utils.default_headers()
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'

def scrape(url, user):

    headers.update({'User-Agent': USER_AGENT})

    r = requests.get(url)

    raw_html = r.content

    content = BeautifulSoup(raw_html, 'html.parser')

    links = content.select('body a')

    visited_urls = []

    pdfs = []

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
            'content': get_content(child_content),
            'url': child_url
        }

        pdfs += get_pdfs(child_content, user)

        page_link = PageLink(**preview_dict)

        try:
            page_link.save()
        except:
            print('Error saving url', child_url)

    return pdfs


def get_title(link):
    """Attempt to get a title."""
    title = None
    if link.title is None:
        if link.find("h1") is not None:
            title = link.find("h1")
    elif link.title.string is not None:
        title = link.title.string

    return title

def get_pdfs(link, user):
    """Attempt to get pdf links from page"""
    pdf_links = link.find_all('a', href=re.compile(r'(.pdf)'))
    # clean the pdf link names
    url_list = []
    for el in pdf_links:
        url_list.append(el.get_text())

        """ Save the PDF from a URL """
        import requests
        #from django.core.files.base import ContentFile
        #response = requests.get(el['href'])
        #pdf = ContentFile(response.content) import urllib.request
        try:
            import urllib.request
            from django.core.files.uploadedfile import SimpleUploadedFile
            from urllib.parse import urlparse
            pdf_url = el['href']
            basename = urlparse(pdf_url).path.split('/')[-1]
            tmpfile, _ = urllib.request.urlretrieve(pdf_url)
            p = PDF(title=el.get_text(), content="This is a crawled PDF", author=user, pdf_file=SimpleUploadedFile(basename, open(tmpfile, "rb").read()), age_group="N/A")
            p.save()
        except:
            print("failed to scrape " + pdf_url)
        print(el['href'])
    return url_list

def get_description(link):
    """Attempt to get description."""
    description = ''
    if link.find("meta", property="og:description") is not None:
        description = link.find("meta", property="og:description").get('content')
    elif link.find("strong") is not None:
        description = link.find("strong").content
    elif link.find("p") is not None:
        description = link.find("p").content
    return description

def get_content(link):
    """Attempt to get content."""
    content = ''
    paragraphs = link.findAll('p', attrs={'class': None})
    for each in paragraphs:
        content += each.get_text()
    return content

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
