#remember to change the api.py and the endpoints.py from manuel cortez pull request

from twython import Twython


class Twitter:
    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
        try:
            self.twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
        except:
            raise Exception("twitter could not authenticate these tokens!")

    def get_user_object(self,screen_name):
        try:
            user = self.twitter.show_user(screen_name = screen_name)
            print("got the user object..")
            return user
        except:
            raise Exception("user with this screen_name doesnt exist!")

    def send_DM(self,screen_name,message):
        user = self.get_user_object(screen_name)
        recipient_id = user['id']
        event_data = {
            "event": {
                "type": "message_create",
                "message_create": {
                    "target": {
                        "recipient_id": recipient_id
                    },
                    "message_data": {
                        "text": message
                    }
                }
            }
        }
        try:
            event = self.twitter.send_direct_message(**event_data)
            print("message sent..")
            return event
        except:
            raise Exception("could not DM this person!")

    def follow(self,to_follow):
        try:
            event = self.twitter.create_friendship(screen_name = to_follow)
            print("followed the user "+to_follow)
            return event
        except:
            raise Exception("could not follow this person!")

    def unfollow(self,to_unfollow):
        try:
            event = self.twitter.destroy_friendship(screen_name = to_unfollow)
            print("unfollowed the user "+to_unfollow)
            return event
        except:
            raise Exception("could not follow this person!")





if __name__ == "__main__":
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    twitter = Twitter(consumer_key,consumer_secret,access_token,access_token_secret)

    #for getting user object
    # user = twitter.get_user_object(recipient_screen_name)
    # print("the user is",user)

    #for sending DM
    # recipient_screen_name = input("enter the user you want to send to!\n")
    # message = input("type your message you want to send\n")
    # event = twitter.send_DM(recipient_screen_name,message)

    #for following a user
    # e = twitter.follow("")
    # print("done....",e)
    
    #for unfollowing a user
    to_unfollow = ""
    e = twitter.unfollow(to_unfollow)
    print("you successfully unfollowed user:",to_unfollow)
    print("unfollow event is ",e)



