from itertools import islice
from youtube_comment_downloader import *
import csv
import random

downloader = YoutubeCommentDownloader()
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=69qKUoGhoQo', sort_by=SORT_BY_POPULAR)

# collect 2000
mostpop = []
firstsample = 2000
for comment in islice(comments, firstsample):
    mostpop.append(comment)
print("2000 collected")

# randomly select 500
randomsample = random.sample(mostpop, 500)
print("500 rand collected")

with open("scrapped_data.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for comment in randomsample:
        commentext = comment['text'].replace(",", "")
        commentime = comment['time']
        eachrow = [commentext, commentime]
        csv_writer.writerow(eachrow)
