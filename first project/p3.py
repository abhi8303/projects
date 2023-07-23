import instaloader
loader=instaloader.Instaloader()
user_name=input("user_id ")
print("downloading")
loader.download_profile(user_name,profile_pic_only=True)
print("downloaded_completed")

