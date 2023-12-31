import cv2

cap = cv2.VideoCapture(1);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True: 
      ret, frame = cap.read()

      try:
          cv2.imshow('frame', frame)
          out.write(frame)

      except:
          print ('ERROR - Not writting to file')
          gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          cv2.imshow('frame', gray)

      if cv2.waitKey(1) & 0xFF == ord('q'):
          break

cap.release()
out.release()
cv2.destroyAllWindows()
del(cap)