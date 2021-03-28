# from requests_html import HTMLSession
# session = HTMLSession()
# def scrape_from_quora(query,url = 'https://www.quora.com/search?q='):
#     url+=query
#     r = session.get(url)
#     r.html.render(sleep=1, keep_page=True, scrolldown=1, timeout=60)
#     ans=[]
#     a_tags = r.html.find('div.puppeteer_test_question_title')
#     for tag in a_tags:
#         try:
#             ans.append(tag.text)
#         except:
#             pass
#     return ans
# output=scrape_from_quora(input())
# print(output)

from requests_html import HTMLSession
session = HTMLSession()
def scrape_from_quora(query,url = 'https://www.quora.com/search/?q='):
    url+=query
    r = session.get(url)
    r.html.render(sleep=1, keep_page=True, scrolldown=1, timeout=60)
    a_tags = r.html.find('div.puppeteer_test_question_title')
    a_tags = [a.text for a in a_tags]
    print(a_tags)

 

output=scrape_from_quora(input())