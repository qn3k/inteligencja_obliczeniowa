import cv2
import json
from ultralytics import YOLO


model = YOLO('yolov8n.pt')
img_path = 'office_yolo.png'
img = cv2.imread(img_path)
results = model(img)[0]
print("IMG:", img)

def save_detections_to_json(dets, filename, conf_thres, model):
    output = []
    for b in dets.boxes:
        if b.conf < conf_thres:
            continue
        
        cls_id = int(b.cls)
        cls_name = model.names[cls_id]
        
        conf = float(b.conf)
        x1, y1, x2, y2 = map(float, b.xyxy[0])
        
        output.append({
            'class_id': cls_id,
            'class_name': cls_name,
            'confidence': conf,
            'bbox_xyxy': [x1, y1, x2, y2]
        })
    
    with open(filename, 'w') as f:
        json.dump(output, f, indent=4)


for th in [0.1, 0.3, 0.5, 0.7]:
    save_detections_to_json(results, f'image_det_{th}.json', th, model)

for b in results.boxes:
    x1, y1, x2, y2 = map(int, b.xyxy[0])
    cls_id = int(b.cls)
    conf = float(b.conf)
    if conf < 0.3:
        continue
    cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
    cv2.putText(img, f"{model.names[cls_id]} {conf:.2f}", (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

cv2.imwrite('office_yolo_boxes_0.3.png', img)

video_path = 'office_yolo.mp4'
cap = cv2.VideoCapture(video_path)
frame_index = 0

all_frames = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break
    res = model(frame)[0]
    detections = []
    for b in res.boxes:
        cls_id = int(b.cls)
        conf = float(b.conf)
        x1, y1, x2, y2 = map(float, b.xyxy[0])
        if conf < 0.3:
            continue
        detections.append({
            'class_id': cls_id,
            'confidence': conf,
            'bbox_xyxy': [x1, y1, x2, y2]
        })
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
        cv2.putText(frame, f"{model.names[cls_id]} {conf:.2f}", (int(x1), int(y1)-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    all_frames[frame_index] = detections
    frame_index += 1
    cv2.imwrite(f'video_frame_{frame_index}_0.3.png', frame)

cap.release()

with open('video_detections_0.3.json', 'w') as f:
    json.dump(all_frames, f, indent=4)

stats = {}
for frame, dets in all_frames.items():
    for d in dets:
        cls_id = d['class_id']
        stats[cls_id] = stats.get(cls_id, 0) + 1

with open('video_stats.json', 'w') as f:
    json.dump(stats, f, indent=4)
