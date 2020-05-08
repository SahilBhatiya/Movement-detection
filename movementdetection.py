import cv2, time

video  = cv2.VideoCapture(0)

first_frame = None

a = 0

while True:
    a = a+1
    check, frame = video.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    store = (frame)
    gray = cv2.GaussianBlur(gray,(21 , 21), 0)
    if(first_frame is None):
        first_frame = gray
        continue

    if(a % 2500 == 0):
        print(a)
        first_frame = gray
        continue


    delta_frame = cv2.absdiff(first_frame, gray)

    changed_frame = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]

    changed_frame = cv2.dilate(changed_frame, None, iterations=4)


    (cnts,_)  = cv2.findContours(changed_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for contour in cnts:
        if cv2.contourArea(contour) < 1500:
            continue

        cv2.imwrite("caught\\cap"+str(a)+".jpg", store)
        print("capture at ", str(a))

    # cv2.imshow("capturing", gray)
    # cv2.imshow("diffenrence", delta_frame)
    # cv2.imshow("in black and white", changed_frame)







    key = cv2.waitKey(1)


    if(key == ord('q')):
        break


video.release()
cv2.destroyAllWindows()
