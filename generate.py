# -*- coding: utf-8 -*-
import json
import urllib3
from datetime import datetime

articlesUrl = 'https://taketoday.cn/api/articles/popular'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) GitHubREADME/85.0.4183.102 Safari/537.36'
}


def addIntro(file):
    ret = ''''''
    file.write(ret)


def addProjectStats(file):
    text = '''
### GitHub统计
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=TAKETODAY"/>
</p>

> '''
    text += datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file.write(text)


def addBlog(file):
    http = urllib3.PoolManager(num_pools=1, headers=headers)
    response = http.request('GET', articlesUrl)
    file.write("\n### 我的博客\n")

    articles = json.loads(response.data)

    for article in articles:
        file.write(
            '- [%s](https://taketoday.cn/articles/%s)\n' % (article['title'], article['id'])
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
