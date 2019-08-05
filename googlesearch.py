#! python3
# -*- coding: utf-8 -*

# Libs
from googleapiclient.discovery import build

class Google:

	def google_search(self,search_term, api_key, cse_id, **kwargs):
		service = build("customsearch", "v1", developerKey=api_key)
		res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
		return res

	def search(self,text):
		output = {}
		my_api_key = "your key"
		my_cse_id = "your key"
		
		result = self.__class__.google_search(self,str(text), my_api_key, my_cse_id)
		items = result.get("items")
		
		for link in items:
			output[link.get("title")] = link.get("link")

		return output