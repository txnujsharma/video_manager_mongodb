from pymongo import MongoClient
from bson import ObjectId


client = MongoClient(
    "mongodb+srv://AddYours:AddYours@cluster0.yl1ar41.mongodb.net/yashhsharma199?retryWrites=true&w=majority",
    tlsAllowInvalidCertificates=True
)



print(client)
db = client["yashhsharma199"]
video_collection = db["videos"]
 



def list_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_videos(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube manager App")
        print("1. list all videos")
        print("2. add a new video")
        print("3. update a video")
        print("4. delete a video")
        print("5. exit the app")
        choice = input("enter your choice: ")

        if choice == '1':
            list_video()

        elif choice == '2':
            name = input("enter the video name: ")
            time = input("enter the video time: ")
            add_videos(name, time)

        elif choice == '3':
            video_id = input("enter the video if of the video you wanna update: ")
            new_name = input("enter the updated video name: ")
            new_time = input("enter the updated video time: ")
            update_video(video_id, new_name, new_time)
        
        elif choice == '4':
            video_id = input("enter the video if of the video you wanna delete: ")
            
            delete_video(video_id)

        elif choice == '5':
            break

        else:
            print("invalid choice")

        
if __name__ == "__main__":
    main()
