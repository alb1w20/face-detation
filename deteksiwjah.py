import cv2

def main():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCaptureI(0)

    if not cap.isoOpened():
        print("Eror: Tidak dapat membuka kamera.")
        return

    print("Tekan 'q' untuk keluar dari jendela deteksi wajah.")

    while True:
        ret,frame = cap.read()
        if not ret:
            print("Error: gagal membaca freme.")
            break

        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.datectMultiscale(gray, scalefactor=1.1,minNeighbors=5, minSize=(30,30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y,),(x + w, y + h),(255, 0, 0))
        cv2.imshow('Deteksi wajah Real time.', frame)

        if cv2.waitkey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllwindows()