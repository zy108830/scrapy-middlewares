from scrapy.http import HtmlResponse
import time


# 针对需要动态渲染的页面，延迟获取页面dom
# 需要设置spider的browser
class DelayMiddleware(object):
    def process_request(self, request, spider):
        delay = request.meta.get('delay', False)
        if delay:
            delay_time = request.meta.get('delay_time', 5)
            spider.browser.get(request.url)
            time.sleep(delay_time)
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8",
                                request=request)
