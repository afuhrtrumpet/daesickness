import requests
import json
import praw

def parse(query):
	user_agent=("Medical reddit searcher"
			"github.com/afuhrtrumpet/codefest")
	r = praw.Reddit(user_agent=user_agent)
	results = []
	for submission in r.search(query=query, subreddit='medical'):
		resultItem = {}
		resultItem["title"] = submission.title
		resultItem["url"] = submission.short_link
		results.append(resultItem)
	return results
