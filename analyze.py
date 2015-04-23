
from django.contrib.messages import constants as message
import requests
import re
from heartsing import show_posts

# test_sample = input("Please enter the text you'd like to analyze:")
#
# def analysis (test_sample):
#     url = 'http://text-processing.com/api/sentiment/'
#     payload = {'text':test_sample}
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





