import cv2
import mediapipe as mp
import pyautogui as pi

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
w,h = pi.size()
print(w,h)
while True:
    _ , frame = cam.read()
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x= int(landmark.x * frame_w)
            y= int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(255,0,0))
            if id == 1:
                screen_x= int (landmark.x * w)*2
                screen_y= int(landmark.y *h)
                pi.moveTo(screen_x,screen_y)
    
    cv2.imshow('mouse',frame)
    cv2.waitKey(1)