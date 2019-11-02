/**
 * Copyright 2018, Google LLC
 * Licensed under the Apache License, Version 2.0 (the `License`);
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an `AS IS` BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 
// [START gae_python37_log]
var file; 

function on_book_load(directory) {
    console.log(localStorage.getItem('paths'));
}


var getImageFromUrl = function(url, callback) {
    var img = new Image();

    img.onError = function() {
        alert('Cannot load image: "'+url+'"');
    };

    img.onload = function() {
        callback(img);
    };

    img.src = url;
}


var createPDF = function(imgData) {
    var doc = new jsPDF();

    doc.addImage(imgData, 'JPEG', 10, 10, 50, 50, 'monkey');
    doc.addImage('monkey', 70, 10, 100, 120); // use the cached 'monkey' image, JPEG is optional regardless

    doc.output('datauri');
}


function download_pages() {
    var pdf = new jsPDF();

    var paths = JSON.parse(localStorage.getItem("paths"));
   
    for(var i=0; i<paths.length; i++) {
        base_image = new Image();
        base_image.onload = function(){
            // Create an html canvas element
            var canvas = document.createElement('CANVAS');
            // Create a 2d context
            var ctx = canvas.getContext('2d');
            // Resize the canavas to the image dimensions
            canvas.height = this.height;
            canvas.width = this.width;
            // Draw the image to a canvas
            ctx.drawImage(this, 0, 0);
            // Convert the canvas to a data url
            var dataURL = canvas.toDataURL("image/jpeg", 1.0);
            pdf.addImage(base_image, 'JPEG', 0, 0);
            canvas = null;
        }
        base_image.src = "/static/" + paths[i] ;
    }
     
    pdf.save("download.pdf"); 
}

function make_coloring_book() {
    // Get the input form elements
    var start_string = $("#start").val() ; 
    var end_string = $("#end").val();

    var formData = new FormData();
    formData.append('file', file);
    formData.append('start', start_string);
    formData.append('end', end_string);


    $.ajax({
        url: 'http://localhost:8080/generate_pages',
        type: 'POST',
        data: formData,
        dataType: "json",
        success: function (data) {
            localStorage.setItem('paths', JSON.stringify(data.paths));
            window.location.replace("http://localhost:8080/book");
        },
        cache: false,
        contentType: false,
        processData: false
    });
}

function upload_file(files) {
    files = files; 
    if(files.length == 0) {
        console.log("empty!"); 
    }
    else {
        file = files[0];    
    }
}
// [END gae_python37_log]
