def create_youtube_video(title,discription):
	youtube = {"title":title,"discription":discription,"likes":0,"dislikes":0,"comments":{}}
	return youtube


def like(youtube):
	if "likes" in youtube:
		youtube[likes]+=1
	return youtube

def dislike(youtube):
	if "dislikes" in youtube:
		youtube[likes]+=1
	return youtube

def add_comment(youtube,username,comment_text):
	youtube[comments]={username:comment_text}
	return youtube

youtubevid = create_youtube_video("ta3arof","hello guys how are you?")
print (youtubevid)