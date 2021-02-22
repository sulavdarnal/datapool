#!/usr/bin/env python
# coding: utf-8

# Hacker News Data Analysis Project
# In this project we will analyze what kind of posts
# receives more comments on average and does certain time
# make any difference

# In[7]:


import csv

f = open('hacker_news.csv')
hn = list(csv.reader(f))
hn[:5]


# In[8]:


headers = hn[0]
hn = hn[1:]
print(headers)
print(hn[:5])


# In[9]:


ask_posts = []
show_posts = []
other_posts = []

for post in hn:
    title = post[1]
    if title.lower().startswith('ask hn'):
        ask_posts.append(post)
    elif title.lower().startswith('show hn'):
        show_posts.append(post)
    else:
        other_posts.append(post)
        
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))
        

        
    


# In[10]:


total_ask_comments = 0

for post in ask_posts:
    total_ask_comments += int(post[4])

avg_ask_comments = total_ask_comments / len(ask_posts)

print(avg_ask_comments)


# In[12]:


total_show_comments = 0

for post in show_posts:
    total_show_comments += int(post[4])
    
avg_show_comments = total_show_comments / len(show_posts)

print(avg_show_comments)


# from the above findings, we see that on average ask posts receives more comments than show posts.

# In[14]:


import datetime as dt

result_list = []

for post in ask_posts:
      result_list.append(
        [post[6], int(post[4])]
    )
    
counts_by_hour = {}
comments_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for each_row in result_list:
    date = each_row[0]
    comment = each_row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1
    


# In[15]:


avg_by_hour = []

for hr in comments_by_hour:
    avg_by_hour.append([hr, comments_by_hour[hr] / counts_by_hour[hr]])

avg_by_hour


# In[17]:


swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
    
swap_avg_by_hour
    


# In[18]:


sorted_swap = sorted(swap_avg_by_hour, reverse=True)
sorted_swap


# In[19]:


print("Top 5 Hours for 'Ask HN' Comments")
for avg, hr in sorted_swap[:5]:
    print(
        "{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(hr, "%H").strftime("%H:%M"),avg
        )
    )


# The hour that receives the most comments per post on average is 15:00, with an average of 38.59 comments per post. There's about a 60% increase in the number of comments between the hours with the highest and second highest average number of comments.
# 
# To conclude, ask posts received more comments on average than show posts and ask posts created between 15:00 and 16:00 (3:00 pm est - 4:00 pm est) received the most comments on average.
# 
