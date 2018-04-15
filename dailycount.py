import sys

ytcrawl_path = '/home/kumar/sem/NLP/YTCrawl'

sys.path.append(ytcrawl_path)

from crawler import Crawler

c = Crawler()

c._crawl_delay_time = 1

#print c.single_crawl("1yOksQv1ho0")

c.batch_crawl("incomplete_1.txt", "/home/kumar/sem/NLP/daily_count")