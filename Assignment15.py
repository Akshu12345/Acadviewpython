
# Ques1
import re
email="zuck26@facebook.com page33@google.com jeff42@amazon.com"
result=re.findall('[\w\d]{1,20}[\w]{1,20}[\w]{1,5}',email)
t1=(result[0:3])
t2=(result[3:6])
t3=(result[6:9])
s1=(tuple(t1))
s2=(tuple(t2))
s3=(tuple(t3))
l1=[]
l1.append(s1)
l1.append(s2)
l1.append(s3)
print(l1)


# Ques2
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better"
a=re.findall('[Bb][\w]{1,20}',text)
print(a)


# Qurs3
import re
sentence="A,very very;irregular_sentence"
output=re.sub("[,;_]"," ",sentence)
print(output)


# optional question
# Ques1
import re
tweet="Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
def clean_tweet(tweet):
    tweet=re.sub('RT|cc',' ',tweet)
    tweet=re.sub('http\S+\s*',' ',tweet)
    tweet=re.sub('@\S+',' ',tweet)
    tweet=re.sub('#\S+',' ',tweet)
    tweet=re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./;:<=>?@[\]^_{|}"""),' ',tweet)
    tweet=re.sub('\s+',' ',tweet)
    return tweet
print(clean_tweet(tweet))