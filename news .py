from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='d195a71f47ea415ba53cd187f57d4469')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          language='en',
                                          )

# /v2/everything
all_articles = newsapi.get_everything(q='Steve Smith',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_parameter='2018-03-24',
                                      to='2018-03-26',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
									  
sources = newsapi.get_sources()
article_list=all_articles['articles']
list=[]
for i in range(len(article_list)):
	des=article_list[i]
	list.append(des['description'])
	
#file=open('/home/dead/Desktop/pr/news.txt','w')
#for i in range(len(list)):
#	file.write(list[i])
	
#file.close()


