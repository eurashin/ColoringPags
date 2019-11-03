# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]
import datetime
import tools
from flask import Flask, render_template, request, jsonify
import datetime
from find.imageSearch import imageSearch
from pagify.pagify1 import pagify
from PIL import Image
import io


app = Flask(__name__)

def serve_pil_image(pil_img):
    img_io = io.StringIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
                   datetime.datetime(2018, 1, 2, 10, 30, 0),
                   datetime.datetime(2018, 1, 3, 11, 0, 0),
                   ]

    return render_template('index.html', times=dummy_times)

@app.route('/book/')
def download():
    return render_template('book.html')


@app.route('/generate_pages', methods=['POST'])
def generate():
    # Read the data
    file_string = request.values.get('link')
    start_date = request.values.get('start')
    end_date = request.values.get('end')

    # Find the locations!
    location_data = tools.parse_location_data('static/history.json')
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    locations = tools.extract_time_period(location_data, start, end)
  
    # Retrieve the photos
    if( isinstance(locations, list)): 
        # Return failed status
        return('failed')
    else: 
        paths = imageSearch(locations)
        images = pagify(paths)
       
#        counter = 0
#        for image in images: 
#            cv2.imwrite('' + 'colorme' + str(counter) + ".jpg" ,image)
#            counter = counter + 1
        
    return(jsonify(paths = images))


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
#    app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='https://coloring-book-257804.appspot.com/', debug=True)
# [START gae_python37_render_template]
