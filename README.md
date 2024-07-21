# WEBM to MP4 Converter

   A simple GUI application to convert WEBM files to MP4 format using Python and FFmpeg.

   ## Prerequisites

   - Python 3.6 or higher
   - FFmpeg
   - PyQt6

   ## Installation

   1. Clone this repository:
      ```
      git clone https://github.com/yourusername/webm-to-mp4-converter.git
      cd webm-to-mp4-converter
      ```

   2. Create a virtual environment and activate it:
      ```
      python3 -m venv venv
      source venv/bin/activate
      ```

   3. Install the required packages:
      ```
      pip install PyQt6
      ```

   4. Install FFmpeg:
      - On macOS with Homebrew: `brew install ffmpeg`
      - On other systems, please refer to the [FFmpeg download page](https://ffmpeg.org/download.html)

   ## Usage

   1. Ensure you're in the project directory and your virtual environment is activated.

   2. Run the launcher script:
      ```
      ./launch_converter.command
      ```
      Or double-click `launch_converter.command` in Finder.

   3. Drag and drop WEBM files onto the application window to convert them to MP4.

   ## Contributing

   Contributions are welcome! Please feel free to submit a Pull Request.

   ## License

   This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.