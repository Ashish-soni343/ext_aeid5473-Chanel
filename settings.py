# Scrapy settings for chanel project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'chanel'

SPIDER_MODULES = ['chanel.spiders']
NEWSPIDER_MODULE = 'chanel.spiders'
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
# }


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'chanel (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 20

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
# SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'
# REACTOR_THREADPOOL_MAXSIZE = 20
LOG_LEVEL = 'INFO'
RETRY_ENABLED = True
DOWNLOAD_TIMEOUT = 999999999
REDIRECT_ENABLED = True
# AJAXCRAWL_ENABLED = True
# CONCURRENT_REQUESTS_PER_DOMAIN = 200
COOKIES_ENABLED = True
# COOKIES_DEBUG = True
# HTTPCACHE_ENABLED = True
# HTTPERROR_ALLOW_ALL = True


# REDIRECT_MAX_TIMES = 20
# handle_httpstatus_list =  [301]

# DNS_RESOLVER = 'scrapy.resolver.CachingThreadedResolver'
DUPEFILTER_CLASS = "scrapy.dupefilters.BaseDupeFilter"