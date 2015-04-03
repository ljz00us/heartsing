
from __future__ import print_function
import semantria
import uuid
import time

import heartsing


serializer = semantria.JsonSerializer()

semantria_key = "4240922d-eea6-4f59-ac8c-3a283f730894"
semantria_secret = "415af06b-1b0b-488b-80dd-19da1bef4f30"

initialTexts = [
    "Lisa - there's 2 Skinny cow coupons available $5 skinny cow ice cream coupons on special k boxes and Printable FPC from facebook - a teeny tiny cup of ice cream. I printed off 2 (1 from my account and 1 from dh's). I couldn't find them instore and i'm not going to walmart before the 19th. Oh well sounds like i'm not missing much ...lol",
    "In Lake Louise - a guided walk for the family with Great Divide Nature Tours rent a canoe on Lake Louise or Moraine Lake  go for a hike to the Lake Agnes Tea House. In between Lake Louise and Banff - visit Marble Canyon or Johnson Canyon or both for family friendly short walks. In Banff  a picnic at Johnson Lake rent a boat at Lake Minnewanka  hike up Tunnel Mountain  walk to the Bow Falls and the Fairmont Banff Springs Hotel  visit the Banff Park Museum. The \"must-do\" in Banff is a visit to the Banff Gondola and some time spent on Banff Avenue - think candy shops and ice cream.",
    "On this day in 1786 - In New York City  commercial ice cream was manufactured for the first time."
]

for text in initialTexts:
   doc = {"id": str(uuid.uuid4()).replace("-", ""), "text": text}

session = semantria.Session("key4240922d-eea6-4f59-ac8c-3a283f730894", "secret415af06b-1b0b-488b-80dd-19da1bef4f30", serializer, use_compression=True)
status = session.queueDocument(doc)

if status == 202:
    print("\"", doc["id"], "\" document queued successfully.", "\r\n")

length = len(initialTexts)
results = []I think

while len(results) < length):
   print("Retrieving your processed results...", "\r\n")
   time.sleep(2)
   # get processed documents
   status = session.getProcessedDocuments()
   results.extend(status)

for data in results:
   # print document sentiment score
   print("Document ", data["id"], " Sentiment score: ", data["sentiment_score"], "\r\n")

   # print document themes
   if "themes" in data:
      print("Document themes:", "\r\n")
      for theme in data["themes"]:
         print("     ", theme["title"], " (sentiment: ", theme["sentiment_score"], ")", "\r\n")

   # print document entities
   if "entities" in data:
      print("Entities:", "\r\n")
      for entity in data["entities"]:
         print("\t", entity["title"], " : ", entity["entity_type"]," (sentiment: ", entity["sentiment_score"], ")", "\r\n")

# from django.contrib.messages import constants as message
# import requests
# import re
# def analysis (text):
#     url = 'http://text-processing.com/api/sentiment/'
#     payload = {'text':text}
#     response = requests.post(url, data=payload)
#     return_string = response.content
#     numbers = re.findall('\d+(\.\d{1,5})', return_string)
#     neg_int = float(numbers[0])
#
#     # "neutral int" is another number returned by the API
#     # but is unused for this app
#     # neutral_int = float(numbers[1])
#     pos_int = float(numbers[2])
#
#     if pos_int > neg_int:
#         label = "POSITIVE"
#     else:
#         label = "NEGATIVE"
#
#     neg_int = str(int(neg_int*100)) + "%"
#     # neutral_int = str(int(neutral_int*100)) + "%"
#     pos_int = str(int(pos_int*100)) + "%"
#     analysis_results = {'neg_int':neg_int,'label':label, 'pos_int':pos_int}
#     print analysis_results
#     return analysis_results






