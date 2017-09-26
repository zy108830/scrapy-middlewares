from fake_useragent import UserAgent


# [每个请求]都使用不同的UserAgent
class RandomUserAgentMiddleware(object):
    def __init__(self, crawler):
        self.ua = UserAgent()
        self.user_agent_type = crawler.settings['USER_AGENT_TYPE']

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.ua[self.user_agent_type])
