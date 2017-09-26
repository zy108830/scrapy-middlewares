from PIL import Image
from io import BytesIO
from scrapy.http import HtmlResponse
import time


# 对爬取页面进行截屏
# spider中需定义screenshots_width，screenshots_height，screenshots_dir，browser
class ScreenshotsMiddleware(object):
    def process_request(self, request, spider):
        screenshots = request.meta.get('screenshots', False)
        if screenshots:
            width = spider.screenshots_width
            height = spider.screenshots_height
            screenshots_path = spider.screenshots_dir + '/' + (str)(time.time()) + '.png'
            screen = spider.browser.get_screenshot_as_png()
            box = (0, 0, width, height)
            im = Image.open(BytesIO(screen))
            region = im.crop(box)
            region.save(screenshots_path, 'PNG', optimize=True, quality=60)
            request.meta['screenshots_path'] = screenshots_path
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8",
                                request=request)
