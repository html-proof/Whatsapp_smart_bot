from pywhatkit import sendwhats_image,sendwhatmsg,sendwhatmsg_instantly,open_web,sendwhatmsg_to_group,sendwhatmsg_to_group_instantly
from  time import sleep

def num():
    print("\n Whatsapp Bot Chat \n ")
    sleep(5)
    print("1. Send Whatsapp_image \n2. Sent Message to WhatsApp time_set \n3. Sent Instantly Message \n4. Open Whatsapp Web \n5. Sent message to Whatsapp Group \n6. Sent Message to Whatsapp group instantly")

    choice =int(input("input the choice :"))

    if choice ==1:
        try:
            phone_number =str(input("input the number :"))
            img_path =input("input the path of image :")
            caption =input("input the caption :")
            wait_time =int(input("input the time :"))
            sendwhats_image(receiver=phone_number,img_path=img_path,caption=caption,wait_time=wait_time,tab_close=False,close_time=3)
        except ValueError:
            print("sleep length must be non-negative")
        except FileNotFoundError:
            print("File is not found ")
    if choice ==2:
        try:

            phone_number = str(input("input the number :"))
            message = input("input the message :")
            time_hour = int(input("input the Hour to sent message :"))
            time_min = int(input("input the min to sent message :"))
            sendwhatmsg(phone_no=phone_number, message=message, time_hour=time_hour, time_min=time_min, wait_time=15,
                            tab_close=False, close_time=3)
        except:
            pass
    if choice ==3:
        try:
            phone_number = str(input("input the number :"))
            message = input("input the message :")
            sendwhatmsg_instantly(phone_no=phone_number,message=message,wait_time=15,tab_close=False,close_time=3)
        except:
            pass
    if choice ==4:
        try:
            open_web()
        except:
            pass
    if choice ==5:
        try:
            group_id =input("input the group-id :")
            message =input("input the message :")
            time_hour = int(input("input the Hour to sent message :"))
            time_min = int(input("input the min to sent message :"))
            sendwhatmsg_to_group(group_id=group_id,message=message,time_hour=time_hour,time_min=time_min,wait_time=15,tab_close=False,close_time=3)
        except :
            pass
    if choice ==6:
        try:
            group_id = input("input the group-id :")
            message = input("input the message :")
            sendwhatmsg_to_group_instantly(group_id=group_id,message=message,wait_time=15,tab_close=False,close_time=3)
        except:
            pass





num()