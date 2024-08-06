# Scrapy��Ŀ�������ļ�

BOT_NAME = 'temp'

SPIDER_MODULES = ['temp.spiders']
NEWSPIDER_MODULE = 'temp.spiders'

# ����robots.txt����
ROBOTSTXT_OBEY = True

# ����Scrapyͬʱ�������󲢷���������Ĭ��Ϊ16��
# CONCURRENT_REQUESTS = 32

# Ϊͬһ��վ�����������ӳ٣�Ĭ��Ϊ0��
# �ο���https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# �����ӳ�����ֻ��Ӧ��������һ����
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# ����cookies��Ĭ�����ã�
# COOKIES_ENABLED = False

# ����Telnet����̨��Ĭ�����ã�
# TELNETCONSOLE_ENABLED = False

# ����Ĭ������ͷ:
# DEFAULT_REQUEST_HEADERS = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en',
# }

# ���û����Spider�м��
# �ο���https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'temp.middlewares.TempSpiderMiddleware': 543,
# }

# ���û����Downloader�м��
# �ο���https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'temp.middlewares.TempDownloaderMiddleware': 543,
# }

# ���û������չ
# �ο���https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# ����Item����ܵ�
# �ο���https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'temp.pipelines.TempPipeline': 300,
# }

# ���ò������Զ�������չ��Ĭ�Ͻ��ã�
# �ο���https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# ��ʼ�����ӳ�
# AUTOTHROTTLE_START_DELAY = 5
# �ڸ��ӳ���������õ���������ӳ�
# AUTOTHROTTLE_MAX_DELAY = 60
# ScrapyӦͬʱ���͵�ÿ��Զ�̷�������ƽ��������
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# ������ʾ����ÿ�����յ�����Ӧ�Ľ���ͳ����Ϣ��
# AUTOTHROTTLE_DEBUG = False

# ���ò�����HTTP���棨Ĭ�Ͻ��ã�
# �ο���https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# ����Ĭ��ֵ�����õ������Ա�֤δ��������
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'
