# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:37:57 2016

@author: meemee
"""
from historical import query, query_compare
from latest import latest_prices
from comp_search import search, compare
from news import get_articles
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def lookup():
    query = {}
    if request.method == 'POST':
        fromdate=request.form['from-date']
        todate=request.form['to-date']
        keyword=request.form['keyword']
        query = {'fromdate': fromdate, 'todate': todate, 'keyword': keyword}
        start = query.get('fromdate')
        end = query.get('todate')
        company = query.get('keyword')
        return redirect(url_for('get_price', start=start, end = end, company=company))
    return render_template('home.html')

@app.route('/<string:company>+from<string:start>to<string:end>')
def get_price(company,start,end):
    asx = search(company)
    cc = str(asx[0])
    cn = str(asx[1] + " ")
    sec = str(asx[2])
    markc = str(asx[3])

    late = latest_prices(cc)
    qu = query(cc, start, end)
    com = compare(sec)
    c1 = str(com[0])
    cm1 = str(com[1])
    c2 = str(com[2])
    cm2 = str(com[3])
    c3 = str(com[4])
    cm3 = str(com[5])

    comparison = query_compare(cc, com)
    articles = get_articles(cc)
    #articles = [{'Date': '2016-10-20', 'URL': 'http://www.smh.com.au/business/banking-and-finance/apras-wayne-byres-wont-use-the-b-word-in-housing-debate-20161019-gs6eqx.html', 'Body': 'Australia\'s powerful banking regulator has declined to enter into the debate over whether Sydney faces a housing bubble, saying the "B-word" simplifies what is a more "nuanced" issue.\n\nWayne Byres, chair of the Australian Prudential Regulation Authority, was on Thursday asked by Greens senator Peter ...', 'Title': "APRA's Wayne Byres won't use the 'B word' in housing debate"}, {'Date': '2016-10-19', 'URL': 'http://www.smh.com.au/business/8ateight/8eight-gloves-off-again-for-the-third-scorched-earth-debate-20161019-gs6b8s.html', 'Body': "The local share market is set to lift at the open as Wall Street heads for a second day of gains. Meanwhile the Aussie dollar gained ground against the greenback overnight.\n\nGloves off again for the third 'scorched earth' debate\n\n1. Whitehouse race: The gloves come off for third and final time, with ...", 'Title': "8@eight: Gloves off again for the third 'scorched earth' debate"}, {'Date': '2016-10-19', 'URL': 'http://www.smh.com.au/business/banking-and-finance/mortgage-price-war-could-threaten-bank-dividends-says-jpmorgan-20161018-gs5gss.html', 'Body': "A resurgence in fierce price competition between Australia's big banks could pose a threat to the industry's prized dividends, after a crunch in home loan profitability, new research says.\n\nBorrowers have been the winners from a lift in competition between banks this year, which has resulted in ...", 'Title': 'Mortgage price war could threaten bank dividends, says JPMorgan'}, {'Date': '2016-10-18', 'URL': 'http://www.smh.com.au/business/8ateight/8eight-markets-hold-breath-on-chinese-data-dump-20161018-gs5cdc.html', 'Body': 'The local share market is set to rise off the back of a rally on Wall Street, while traders will today be focused on a data dump from China on the state of its economy.\n\nStrong Chinese GDP figures could see the Aussie dollar push back against the greenback.\n\n1. Politics: In the last 12 hours our the ...', 'Title': '8@eight: Markets hold breath on Chinese data dump '}, {'Date': '2016-10-18', 'URL': 'http://www.smh.com.au/business/banking-and-finance/cba-ceo-ian-narev-says-strong-bank-profits-are-critical-amid-volatility-20161016-gs3sck.html', 'Body': 'Commonwealth Bank of Australia chief executive Ian Narev says the application of monetary policy by global central banks has created "endemic volatility" in financial markets that makes it even more important for Australia\'s banks to maintain strong profits in order to buttress the economy from ...', 'Title': "CBA CEO Ian Narev says strong bank profits are 'critical' amid volatility"}, {'Date': '2016-09-09', 'URL': 'http://www.smh.com.au/business/markets-live/markets-live-20160908-grcdr8.html', 'Body': "Australian shares closed down for the fourth week in a row after the European Central Bank failed to extend its monetary stimulus program and investors piled out of the big banks.\n\nSort posts by Newest Oldest 4:42pm on 9 Sep 2016\n\nThat's it for Markets Live for today.\n\nThanks for reading and have a ...", 'Title': 'Markets Live: Draghi drags on ASX'}, {'Date': '2016-09-08', 'URL': 'http://www.smh.com.au/business/the-economy/rbas-glenn-stevens-admits-sydney-house-prices-give-me-some-discomfort-20160908-grbtg5.html', 'Body': 'Reserve Bank governor Glenn Stevens has conceded that he has "some discomfort\' about rising Sydney house prices, but argued that these concerns need to be weighed up against the need to stimulate economic activity.\n\nIn his final annual interview with The Australian Financial Review, the outgoing ...', 'Title': "RBA governor on house prices: 'it certainly gives me some discomfort'"}, {'Date': '2016-10-20', 'URL': 'http://www.smh.com.au/business/banking-and-finance/apras-wayne-byres-wont-use-the-b-word-in-housing-debate-20161019-gs6eqx.html', 'Body': 'Australia\'s powerful banking regulator has declined to enter into the debate over whether Sydney faces a housing bubble, saying the "B-word" simplifies what is a more "nuanced" issue.\n\nWayne Byres, chair of the Australian Prudential Regulation Authority, was on Thursday asked by Greens senator Peter ...', 'Title': "APRA's Wayne Byres won't use the 'B word' in housing debate"}, {'Date': '2016-10-19', 'URL': 'http://www.smh.com.au/business/8ateight/8eight-gloves-off-again-for-the-third-scorched-earth-debate-20161019-gs6b8s.html', 'Body': "The local share market is set to lift at the open as Wall Street heads for a second day of gains. Meanwhile the Aussie dollar gained ground against the greenback overnight.\n\nGloves off again for the third 'scorched earth' debate\n\n1. Whitehouse race: The gloves come off for third and final time, with ...", 'Title': "8@eight: Gloves off again for the third 'scorched earth' debate"}, {'Date': '2016-10-19', 'URL': 'http://www.smh.com.au/business/banking-and-finance/mortgage-price-war-could-threaten-bank-dividends-says-jpmorgan-20161018-gs5gss.html', 'Body': "A resurgence in fierce price competition between Australia's big banks could pose a threat to the industry's prized dividends, after a crunch in home loan profitability, new research says.\n\nBorrowers have been the winners from a lift in competition between banks this year, which has resulted in ...", 'Title': 'Mortgage price war could threaten bank dividends, says JPMorgan'}, {'Date': '2016-10-18', 'URL': 'http://www.smh.com.au/business/8ateight/8eight-markets-hold-breath-on-chinese-data-dump-20161018-gs5cdc.html', 'Body': 'The local share market is set to rise off the back of a rally on Wall Street, while traders will today be focused on a data dump from China on the state of its economy.\n\nStrong Chinese GDP figures could see the Aussie dollar push back against the greenback.\n\n1. Politics: In the last 12 hours our the ...', 'Title': '8@eight: Markets hold breath on Chinese data dump '}, {'Date': '2016-10-18', 'URL': 'http://www.smh.com.au/business/banking-and-finance/cba-ceo-ian-narev-says-strong-bank-profits-are-critical-amid-volatility-20161016-gs3sck.html', 'Body': 'Commonwealth Bank of Australia chief executive Ian Narev says the application of monetary policy by global central banks has created "endemic volatility" in financial markets that makes it even more important for Australia\'s banks to maintain strong profits in order to buttress the economy from ...', 'Title': "CBA CEO Ian Narev says strong bank profits are 'critical' amid volatility"}, {'Date': '2016-09-09', 'URL': 'http://www.smh.com.au/business/markets-live/markets-live-20160908-grcdr8.html', 'Body': "Australian shares closed down for the fourth week in a row after the European Central Bank failed to extend its monetary stimulus program and investors piled out of the big banks.\n\nSort posts by Newest Oldest 4:42pm on 9 Sep 2016\n\nThat's it for Markets Live for today.\n\nThanks for reading and have a ...", 'Title': 'Markets Live: Draghi drags on ASX'}, {'Date': '2016-09-08', 'URL': 'http://www.smh.com.au/business/the-economy/rbas-glenn-stevens-admits-sydney-house-prices-give-me-some-discomfort-20160908-grbtg5.html', 'Body': 'Reserve Bank governor Glenn Stevens has conceded that he has "some discomfort\' about rising Sydney house prices, but argued that these concerns need to be weighed up against the need to stimulate economic activity.\n\nIn his final annual interview with The Australian Financial Review, the outgoing ...', 'Title': "RBA governor on house prices: 'it certainly gives me some discomfort'"}]
    return render_template('news.html', cc=cc, cn=cn, sec=sec,markc=markc,c1=c1, c2=c2, c3=c3,
                           cm1=cm1, cm2=cm2, cm3=cm3, comparison = comparison, late=late, qu=qu, articles=articles)

if __name__ == "__main__":
    app.run(debug = True)
