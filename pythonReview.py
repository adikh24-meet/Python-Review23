def create_youtube_video(title,discription,hashtag):
	youtube = {"title":title,"discription":discription,"likes":0,"dislikes":0,"comments":{},"hashtag":hashtag}
	return youtube


def like(youtube):
	if "likes" in youtube:
		youtube["likes"]+=1
	return youtube

def dislike(youtube):
	if "dislikes" in youtube:
		youtube["likes"]+=1
	return youtube

def add_comment(youtube,username,comment_text):
	youtube["comments"]={username:comment_text}
	return youtube

def similarity_to_video(youtube1,youtube2):
	count=0
	list1 = youtube1["hashtag"]
	list2 = youtube2["hashtag"]
	for i in range(5):
		for hash in list1:
			if hash == list2[i]:
				count+=1
	print(count,"/ 5")

youtubevid1 = create_youtube_video("ta3arof","hello guys how are you?",["fun","cute","funny","cat","animal"])
youtubevid2 = create_youtube_video("ta3arof","hello guys how are you?",["fun","cute","funny","dog","animal"])


for i in range(495):
	like(youtubevid1)

add_comment(youtubevid1,"adi","you nawartoo paris")

print(youtubevid1)

similarity_to_video(youtubevid1,youtubevid2)