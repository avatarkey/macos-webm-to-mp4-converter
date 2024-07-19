import os
import subprocess

def convert_webm_to_mp4(input_file, output_file):
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libx264',
        '-crf', '23',
        '-c:a', 'aac',
        '-q:a', '100',
        output_file
    ]
    
    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"Successfully converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_file}: {e}")

def main():
    current_dir = os.getcwd()
    
    for filename in os.listdir(current_dir):
        if filename.endswith('.webm'):
            input_file = os.path.join(current_dir, filename)
            output_file = os.path.join(current_dir, f"{os.path.splitext(filename)[0]}.mp4")
            convert_webm_to_mp4(input_file, output_file)

if __name__ == "__main__":
    main()
