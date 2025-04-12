import cv2
import numpy as np
import time

def detect_eyes(frame, face_cascade, eye_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:  # If at least 2 eyes are detected
            # Sort eyes by x-coordinate (left to right)
            eyes = sorted(eyes, key=lambda x: x[0])
            
            # Get left and right eye coordinates
            left_eye = eyes[0]
            right_eye = eyes[1]
            
            # Draw rectangles around eyes
            cv2.rectangle(roi_color, (left_eye[0], left_eye[1]), 
                         (left_eye[0]+left_eye[2], left_eye[1]+left_eye[3]), 
                         (0, 255, 0), 2)
            cv2.rectangle(roi_color, (right_eye[0], right_eye[1]), 
                         (right_eye[0]+right_eye[2], right_eye[1]+right_eye[3]), 
                         (0, 255, 0), 2)
            
            # Calculate eye centers
            left_center = (x + left_eye[0] + left_eye[2]//2, y + left_eye[1] + left_eye[3]//2)
            right_center = (x + right_eye[0] + right_eye[2]//2, y + right_eye[1] + right_eye[3]//2)
            
            # Draw lines connecting eyes
            cv2.line(frame, left_center, right_center, (0, 255, 255), 2)
            
            # Calculate and display eye positions
            eye_distance = right_center[0] - left_center[0]
            eye_height = (left_center[1] + right_center[1]) / 2
            
            # Display coordinates
            cv2.putText(frame, f"Left Eye: [{left_center[0]}, {left_center[1]}]", 
                       (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f"Right Eye: [{right_center[0]}, {right_center[1]}]", 
                       (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f"Distance: [{eye_distance:.1f}]", 
                       (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f"Height: [{eye_height:.1f}]", 
                       (10, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    return frame

def main():
    # Load the cascades
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    # Set window properties
    cv2.namedWindow('Eye Tracking', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Eye Tracking', 800, 600)
    
    # Initialize FPS calculation variables
    prev_frame_time = 0
    new_frame_time = 0
    
    print("Eye Tracking Application Started")
    print("Press 'q' to quit")
    
    while True:
        # Read frame from webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from webcam")
            break
            
        # Process the frame
        frame = detect_eyes(frame, face_cascade, eye_cascade)
        
        # Calculate FPS
        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps)
        
        # Add FPS counter to frame
        cv2.putText(frame, f"FPS: {fps}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Show the frame
        cv2.imshow('Eye Tracking', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 