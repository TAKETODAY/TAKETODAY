# -*- coding: utf-8 -*-
import json
import pytz
import urllib3
from datetime import datetime

articlesUrl = 'https://taketoday.cn/api/articles?size=8'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) GitHubREADME/85.0.4183.102 Safari/537.36'
}


def addIntro(file):
    ret = ''''''
    file.write(ret)


def addProjectStats(file):
    text = '''
### GitHub 统计
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=TAKETODAY"/>
</p>

> '''
    text += datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    text += '''
    
<a title="Hits" target="_blank" href="https://github.com/TAKETODAY/TAKETODAY">
    <img src="https://hits.b3log.org/TAKETODAY/TAKETODAY.svg">
</a>
'''
    file.write(text)


def addBlog(file):
    http = urllib3.PoolManager(num_pools=1, headers=headers)
    response = http.request('GET', articlesUrl)
    file.write("\n### 我的博客\n")

    res = json.loads(response.data)
    articles = res['data']

    for article in articles:
        file.write(
            '- [%s](https://taketoday.cn/articles/%s)\n' % (article['title'], article['uri'])
        )

    file.write('\n[查看更多](https://taketoday.cn)\n')


if __name__ == '__main__':
    file = open('README.md', 'w+', encoding="utf-8")
    addIntro(file)
    file.write('<table align="center"><tr>\n')
    file.write('<td valign="top" width="50%">\n')

    addBlog(file)

    file.write('\n</td>\n')
    file.write('<td valign="top" width="50%">\n')

    addProjectStats(file)

    file.write('\n</td>\n')
    file.write('</tr></table>\n')
    file.close()
