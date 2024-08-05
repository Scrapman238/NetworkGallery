from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import ffmpeg
import socket
from PIL import Image, ExifTags

app = Flask(__name__)

# Set maximum file size (10 GB)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 * 1024  # 10 GB in bytes

# Configure number of files to be processed
MAX_FILE_COUNT = 10000

# Function to get the local IP address
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))  # Connect to a remote server (Google DNS)
        ip_address = s.getsockname()[0]
    except Exception as e:
        ip_address = '127.0.0.1'  # Fallback to localhost if unable to determine
    finally:
        s.close()
    return ip_address

# Automatically determine the device's IP address
ip_host_address = get_ip_address()

# Paths for media uploads
UPLOAD_FOLDER_IMAGES = 'static/images'
UPLOAD_FOLDER_VIDEOS = 'static/videos'
LOW_QUALITY_FOLDER = 'static/images/low_quality'
app.config['UPLOAD_FOLDER_IMAGES'] = UPLOAD_FOLDER_IMAGES
app.config['UPLOAD_FOLDER_VIDEOS'] = UPLOAD_FOLDER_VIDEOS
app.config['LOW_QUALITY_FOLDER'] = LOW_QUALITY_FOLDER

# Ensure low quality folder exists
os.makedirs(LOW_QUALITY_FOLDER, exist_ok=True)

@app.route('/')
def index():
    image_filenames = [f for f in os.listdir(UPLOAD_FOLDER_IMAGES) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    video_filenames = [os.path.splitext(f)[0] for f in os.listdir(UPLOAD_FOLDER_VIDEOS) if f.endswith(('.mp4', '.avi', '.mov'))]

    image_data = []
    for image in image_filenames:
        base_filename, _ = os.path.splitext(image)
        video_exists = base_filename in video_filenames
        image_data.append({
            'image': image,
            'video_exists': video_exists,
            'base_filename': base_filename
        })

    return render_template('index.html', image_data=image_data, ip_address=ip_host_address)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'media' not in request.files:
            return redirect(url_for('index'))

        files = request.files.getlist('media')
        
        if len(files) > MAX_FILE_COUNT:
            return "Error: Too many files. Maximum allowed is 10,000.", 400
        
        for file in files:
            if file.filename == '':
                continue

            filename = file.filename
            file_extension = filename.rsplit('.', 1)[-1].lower()
            
            if file_extension in ('png', 'jpg', 'jpeg', 'gif'):
                file_path = os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], filename)
                file.save(file_path)
                
                # Generate lower quality image
                low_quality_path = os.path.join(app.config['LOW_QUALITY_FOLDER'], filename)
                generate_low_quality_image(file_path, low_quality_path)
            
            elif file_extension in ('mp4', 'webm', 'ogg'):
                video_path = os.path.join(app.config['UPLOAD_FOLDER_VIDEOS'], filename)
                file.save(video_path)
                
                # Extract the first frame and save it as a PNG image
                image_filename = f"{os.path.splitext(filename)[0]}.png"
                image_path = os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], image_filename)
                extract_first_frame(video_path, image_path)
                
                # Generate lower quality image
                low_quality_path = os.path.join(app.config['LOW_QUALITY_FOLDER'], image_filename)
                generate_low_quality_image(image_path, low_quality_path)
        
        return redirect(url_for('index'))
    
    # If GET request, show upload page
    return render_template('upload.html', ip_address=ip_host_address)

@app.route('/low_quality/<filename>')
def low_quality_image(filename):
    low_quality_path = os.path.join(app.config['LOW_QUALITY_FOLDER'], filename)
    original_path = os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], filename)
    
    if not os.path.exists(low_quality_path):
        generate_low_quality_image(original_path, low_quality_path)
    
    return send_from_directory(app.config['LOW_QUALITY_FOLDER'], filename)

def extract_first_frame(video_path, output_image_path):
    try:
        # Use ffmpeg to extract the first frame
        ffmpeg.input(video_path, ss=0).output(output_image_path, vframes=1).run()
    except Exception as e:
        print(f"An error occurred while extracting the frame: {e}")

def generate_low_quality_image(input_image_path, output_image_path):
    try:
        with Image.open(input_image_path) as img:
            # Handle EXIF orientation tag to correct image orientation
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break

            exif = img._getexif()
            if exif is not None:
                orientation = exif.get(orientation)
                if orientation == 3:
                    img = img.rotate(180, expand=True)
                elif orientation == 6:
                    img = img.rotate(270, expand=True)
                elif orientation == 8:
                    img = img.rotate(90, expand=True)

            img.thumbnail((1280, 720))  # Resize image to fit within 720p bounds
            img.save(output_image_path)
    except Exception as e:
        print(f"An error occurred while generating a low quality image: {e}")

if __name__ == '__main__':
    app.run(host=ip_host_address, port=80, debug=True)
