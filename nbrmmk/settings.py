BOT_NAME = 'nbrmmk'

SPIDER_MODULES = ['nbrmmk.spiders']
NEWSPIDER_MODULE = 'nbrmmk.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'nbrmmk.pipelines.NbrmmkPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
