import praw

def parse(query):
	user_agent = ("Medical reddit searcher"
			"github.com/afuhrtrumpet/codefest")
	r = praw.Reddit(user_agent=user_agent)
	results = []
	for submission in r.search(query=query, subreddit='medical'):
		result_item = {}
		result_item["title"] = submission.title
		result_item["url"] = submission.short_link
		results.append(result_item)
	reddit_item = {'title':'Reddit', 'site_url': 'http://www.reddit.com', 'icon_url': '', 'results': results}
	return reddit_item
