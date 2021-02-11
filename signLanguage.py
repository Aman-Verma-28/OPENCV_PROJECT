import cv2, keyboard
# import pyautogui
# def hit(key):
    # pyautogui.keyDown(key)
    # pyautogui.keyUp(key)

cap = cv2.VideoCapture(0)
# tracker = cv2.TrackerMOSSE_create()  # 30FPS, good accuracy
# tracker = cv2.TrackerCSRT_create() # 30FPS, high accuracy (g)
# tracker = cv2.TrackerBoosting_create() # 20FPS, more than average accuracy
# tracker = cv2.TrackerMIL_create() # bad FPS, very bad accuracy
# tracker = cv2.TrackerGOTURN_create() # dosen't work
# tracker = cv2.TrackerKCF_create() # 17FPS, above average accuracy
# tracker = cv2.TrackerTLD_create() # 8FPS, high accuracy
tracker = cv2.TrackerMedianFlow_create() # 40FPS, low accuracy   (g)

count = 0
reg, img = cap.read()
img = cv2.flip(img,1)
bbox = cv2.selectROI("Tracking", img, None)
tracker.init(img, bbox)
# img = cv2.flip(img, 1)

init_points = bbox
ix, iy, iw, ih = int(init_points[0]), int(init_points[1]), int(init_points[2]), int(init_points[3])
center_x = ix + int(iw/2)
center_y = iy + int(ih/2)
radius_Bound = 28
  

def get_direction(tracker_dot_x, tracker_dot_y):
    global count
    if tracker_dot_x < center_x + radius_Bound and tracker_dot_x > center_x - radius_Bound and tracker_dot_y < center_y + radius_Bound//2 and tracker_dot_y > center_y - radius_Bound//2:
        count = 0
    if count<1:
        if tracker_dot_y > (center_y + radius_Bound//2): 
            # print('down')
            keyboard.press_and_release('down')
            count+=1
        
        elif tracker_dot_y < (center_y - radius_Bound//2):
            # print('up')
            keyboard.press_and_release('up')
            count+=1
        
        elif tracker_dot_x > (center_x + radius_Bound):
            # print('right')
            keyboard.press_and_release('right')
            count+=1
        
        elif tracker_dot_x < (center_x - radius_Bound):
            # print('left')
            keyboard.press_and_release('left')
            count+=1

for i in range(1):
    while True:
        timer = cv2.getTickCount()
        ret, img = cap.read()

        img = cv2.flip(img, 1)

        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        tracker_dot_x = x + w//2
        tracker_dot_y = y + h//2
        # print(tracker_dot_x, tracker_dot_y)
        cv2.circle(img, (tracker_dot_x, tracker_dot_y), 6, (255, 0, 0), 2)
        
        cv2.circle(img, (center_x, center_y), radius_Bound, (255, 255, 0), 2)
        get_direction(tracker_dot_x, tracker_dot_y)
        success, bbox = tracker.update(img)


        
        fps = str(int(cv2.getTickFrequency() / (cv2.getTickCount() - timer)))
        # cv2.putText(img, fps, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('img', img)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()



