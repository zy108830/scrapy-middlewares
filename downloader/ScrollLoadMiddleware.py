from selenium.webdriver.support import ui
from scrapy.http import HtmlResponse
import os


# 针对下拉加载的内容进行自动化滚动爬取
# spider中需定义browser，scroll_timeout
class ScrollLoadMiddleware(object):
    def process_request(self, request, spider):
        scroll_load = request.meta.get('scroll_load', False)
        if scroll_load:
            spider.browser.get(request.url)
            content = open(os.path.dirname(__file__) + '/js/scroll.js').read()
            spider.browser.execute_script(content)
            try:
                wait = ui.WebDriverWait(spider.browser, spider.scroll_timeout)
                wait.until(
                    lambda browser: browser.find_element_by_tag_name('body').get_attribute('has_more') is not None)
            except Exception as e:
                html = spider.browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
                return HtmlResponse(url=spider.browser.current_url, body=html, encoding="utf-8",
                                    request=request)
