from flask import Flask, render_template, request
import pyktok as pyk
import os
import re
import time

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/cotact')
def contact():
    return render_template('cotact.html')

@app.route('/privacy')
def privacy_policy():
    return render_template('privacy.html')

@app.route('/termsandconditions')
def terms_conditions():
    return render_template('termsandconditions.html')

@app.route('/download', methods=['POST'])
def download():
    message = None  # Initialize message variable

    if request.method == 'POST':
        url = request.form['url']  # TikTok video URL

        # Specify the user's Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

        # Extract video title or ID from the URL
        video_title = re.search(r'video/(\d+)', url)
        if video_title:
            video_title = video_title.group(1)
        else:
            video_title = 'video'  # Default name if extraction fails

        # Set the output file path in the Downloads folder
        output_file = os.path.join(downloads_folder, f"{video_title}.mp4")

        try:
            # Temporarily change the working directory to the Downloads folder
            original_cwd = os.getcwd()  # Store the original working directory
            os.chdir(downloads_folder)  # Change to Downloads folder

            # Specify the browser (assuming 'pyk.specify_browser' exists)
            pyk.specify_browser('firefox')

            # Simulate download with progress (you can replace this with the actual download code)
            for i in range(10):  # Simulate download steps
                time.sleep(0.5)  # Simulate time delay per step

            # Download the TikTok video by passing the URL
            pyk.save_tiktok(url, True)

            # Change back to the original working directory
            os.chdir(original_cwd)

            # Set the success message
            message = "Video successfully downloaded!"

        except Exception as e:
            # Ensure we return to the original working directory even in case of error
            os.chdir(original_cwd)
            message = f"An error occurred: {e}"

    return render_template('homepage.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
