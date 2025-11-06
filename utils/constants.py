

POSE_THRESHOLDS = [45.0, 45.0, 45.0]  # yaw, pitch, roll limits
FACE_CONF_THRESHOLD = 0.5
MAX_DISAPPEARED = 20  # frames before an ID is removed
MAX_DISTANCE = 50  # max pixel distance to match same ID
lpfid_map = {}   
LPFID_TTL = 10 * 60 
next_lpfid = 1

data_base_dir = "ByteTracker_data"
model_dir = 'models'
faces_dir = 'faces'
videos_dir = 'videos'

output_dir = 'output'
all_detection_json = "all_detections.json"

pose_model = model_dir + "/head-pose-estimation-adas-0001.xml"
face_model = model_dir + "/yolov12n-face.pt"
video = videos_dir + "/input_video.mp4"

save_once_in_count = 50
save_once_in_step = 1