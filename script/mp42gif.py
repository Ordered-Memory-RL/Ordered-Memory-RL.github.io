import imageio
import argparse
import os
import tqdm
import cv2 as cv

parser = argparse.ArgumentParser('From mp4 to gif')
parser.add_argument('mp4')
parser.add_argument('--subsample', type=int, default=1, help='whether or not to subsample frames')
args = parser.parse_args()

cap = cv.VideoCapture(args.mp4)
if not cap.isOpened():
    print("Cannot open video")
    exit()

frames = []
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is Tru
    if not ret:
        break
    # Our operations on the
    # frame come here
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frames.append(frame)
cap.release()
cv.destroyAllWindows()
print('Producing GIF...')
gif_path = os.path.join('.', os.path.basename(args.mp4).replace('mp4', 'gif'))
with imageio.get_writer(gif_path, mode='I', duration=0.1) as writer:
    for frame in tqdm.tqdm(frames[::args.subsample]):
        writer.append_data(frame)

