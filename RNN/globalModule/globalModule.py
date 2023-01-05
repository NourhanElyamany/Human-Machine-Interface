import numpy as np
import os
import mediapipe as mp
import cv2

dataPath = "../Data/"
gesturesDataPath = os.path.join(f'{dataPath}/Gestures')
modelPath = os.path.join(f'../Models/')
log_dir = os.path.join('../Logs')

actions = np.array(['right click', 'left click'])
noSequences = 30
sequenceLen = 30

mpHolistics = mp.solutions.holistic
mpDrawing = mp.solutions.drawing_utils


def mediapipeDetection(img, model):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img.flags.writeable = False
    results = model.process(img)
    img.flags.writeable = True
    return results

def getKeyPoints(result):
    face = np.array([[res.x, res.y, res.z] for res in result.face_landmarks.landmark]).flatten() if result.face_landmarks else np.zeros(1404)
    leftHandLandMarks = np.array([[res.x, res.y, res.z] for res in result.left_hand_landmarks.landmark]).flatten() if result.left_hand_landmarks else np.zeros(21*3)
    rightHandLandMarks = np.array([[res.x, res.y, res.z] for res in result.right_hand_landmarks.landmark]).flatten() if result.right_hand_landmarks else np.zeros(21*3)
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in result.pose_landmarks.landmark]).flatten()if result.pose_landmarks else np.zeros(132)
    return np.concatenate([face, leftHandLandMarks, rightHandLandMarks, pose])

def drawLandmarks(img, results):
    mpDrawing.draw_landmarks(img, results.face_landmarks, mpHolistics.FACEMESH_TESSELATION)
    mpDrawing.draw_landmarks(img, results.pose_landmarks, mpHolistics.POSE_CONNECTIONS)
    mpDrawing.draw_landmarks(img, results.left_hand_landmarks, mpHolistics.HAND_CONNECTIONS)
    mpDrawing.draw_landmarks(img, results.right_hand_landmarks, mpHolistics.HAND_CONNECTIONS)
   