# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:36:05 2016

@author: meemee
"""
from eventregistry import *
import datetime
now = datetime.datetime.now()
past = now - datetime.timedelta(days = 50)
start = past.strftime("%Y-%m-%d")
end = now.strftime("%Y-%m-%d")

ssplit = start.split("-")
s_y = int(ssplit[0])
s_m = int(ssplit[1])
s_d = int(ssplit[2])
start = datetime.date(s_y, s_m, s_d)

esplit = end.split("-")
e_y = int(esplit[0])
e_m = int(esplit[1])
e_d = int(esplit[2])
end = datetime.date(e_y, e_m, e_d)


er = EventRegistry()
q = QueryArticles()

def get_articles(company_code):
    error = "No recent articles found for this company in the last 50 days"
    empty = {'error': 'No results match the criteria'}
    news = []
    news_list = []
    q.setDateLimit(start, end)
    q.addConcept(er.getConceptUri("Finance", lang = "eng"))
    comp = company_code.split(".")
    key = str(comp[0])
    q.addKeyword(key)

    q.addNewsSource(er.getNewsSourceUri("www.smh.com.au"))
    q.addRequestedResult(RequestArticlesInfo(count = 10,
                                             returnInfo = ReturnInfo(articleInfo = ArticleInfoFlags(duplicateList = False, title = True))))

    data = er.execQuery(q)
    news.append(data)               
    if data != empty:
        news.append(data)  
        for item in news:
            new = item.get('articles',{}).get('results', {})
            for article in new:
                if article.get('lang') == ('eng'):
                    date = article.get('date')
                    dsplit = date.split("-")
                    d_y = int(dsplit[0])
                    d_m = int(dsplit[1])
                    d_d = int(dsplit[2])
                    dd = datetime.date(d_y, d_m, d_d)
                    url = article.get('url')
                    title = article.get('title')
                    body = article.get('body')
                    parsart = {
                        "Date": dd.strftime("%Y-%m-%d"),
                        "URL": str(url),
                        "Title":str(title),
                        "Body": str(body)
                    }
                    news_list.append(parsart)
        return news_list
    else:
        return error
