print'\n\t\t\t---> Before starting, I will click your pic first.<----'

import cv2
# Camera 0 is the integrated web cam on my netbook
camera_port = 0
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)

# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
 temp = get_image()
print("\t\tTaking image...")
# Take the actual image we want to keep
camera_capture = get_image()
file = "/root/Desktop/test_image.jpg"
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)

# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)
import webbrowser
webbrowser.open('/root/Desktop/test_image.jpg')
print'\t\t\t\tDONE!!\n--- Now u can continue.'''

from steganography.steganography import Steganography
print'\n\t\t\t\t\t\t\t\t----Date and Time of Login:----'
from datetime import datetime
t=datetime.now()
print t.strftime("\t\t\t\t\t\t\t\t%d %B %Y , %r")

#Play Audio,Video

a=raw_input('Enter password:')
if a=='zibran@123':
    print'Password Verified!'
elif a!='zibran@123':
    print'Wrong Password!!\n\t\t Retry Again!'
    exit()
print'\n\t\t\t"Hello and Welcome to SpyChat"\n'
from final import spy,choose_member,add_status,add_friend,send_message,read_message,read_chat
# Choose user
while True:
    choice = raw_input("Do you continue as the default user(Y/N) :")
    if choice == 'Y' or choice == 'y':
        active = choose_member(choice)
        break
    elif choice == 'N' or choice == 'n':
        active = choose_member(choice)
        break
    else:
        print "Invalid input.Please re-enter "

print "\n\t\tWelcome %s %s\n" % (active.sal,active.name)

i=True
current_stat = None
while i:
    # Main menu of spy_chat
    scan = raw_input("\t\t1) Add a status update\n\t\t2) Add a friend\n\t\t3) Send a secret message\n"\
    "\t\t4) Read a secret message\n\t\t5) Read chats from a user\n\t\t6) Close application ")
    if scan == '1':
        print "Current account status :%s" % current_stat
        current_stat = add_status(active)
        print "Updated status: %s" % current_stat
    elif scan == '2':
        tot = add_friend(active)
        print "Total friend :%d" % tot
        for temp in active.friends:
            print "* %s" % temp.name
    elif scan == '3':
        s = send_message(active)
        if s != 0:
            print "Message saved"
    elif scan == '4':
        m = read_message(active)
        if m == 'SOS':
            print "You got an emergency message\n\tSOS!!!!SOS!!!SOS!!!!\n"
        elif m == 'SAVE ME':
            print "Code red message\n\tSAVE ME!!!!SAVE ME!!!!\n"
        elif m == 'OP':
            print "Call for operation\n\tTIME TO GOOOOO!!!!\n"
        elif m == 0:
            continue
        else:
            print "Message :%s" % m
    elif scan == '5':
        read_chat(active)
    elif scan == '6':
        print "Thanks for using My Spychat\n\t\t\tAprreciate the Hard Work!'"
        i=False
    else:
        print "Invalid input.Re-enter"








