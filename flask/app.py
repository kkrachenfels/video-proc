from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

import moviepy.editor as mymovie
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip


app = Flask(__name__)
app._static_folder = 'static/'

app.config["UPLOAD_FOLDER"] = "data/"
app.config["AUDIO_FOLDER"] = "audio/"
app.config["DOWNLOAD_FOLDER"] = "downloads/"


def add_beeps(filename):
    test_list = [(1,3),(7,10),(11,18)]
    startaudio = app.config["AUDIO_FOLDER"] + "start.mp3"
    endaudio = app.config["AUDIO_FOLDER"] + "end.mp3"
    outputvideo = app.config["DOWNLOAD_FOLDER"] + filename
    videoclip = VideoFileClip(app.config["UPLOAD_FOLDER"] + filename)

    start, end = test_list[0]
    startaudioclip = mymovie.AudioFileClip(startaudio)
    endaudioclip = mymovie.AudioFileClip(endaudio)

    finalclip = videoclip.set_audio(CompositeAudioClip([videoclip.audio, startaudioclip.set_start(start), endaudioclip.set_start(end)]))

    for x in range(1,len(test_list)):
        start, end = test_list[x]
        finalclip = finalclip.set_audio(CompositeAudioClip([finalclip.audio, startaudioclip.set_start(start), endaudioclip.set_start(end)]))
    finalclip.write_videofile(outputvideo, fps=30, audio_codec="aac")

    #return outputvideo



@app.route('/', methods = ['GET', 'POST'])
def display_file():
    if request.method == 'POST':
    
        f = request.files['filename']
        stored_filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + stored_filename)

        return render_template('submitted.html', filename=stored_filename)

        #file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        #content = file.read()   
        
    else:
        return render_template('lumin.html')

@app.route('/<filename>')
def download_file(filename):
    add_beeps(filename)
    return send_from_directory(app.config["DOWNLOAD_FOLDER"], filename, as_attachment=True)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)


"""
'''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>

    '''
"""