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
var doc; 
var NUM_PAGES = 9; 

function on_book_load(directory) {
    console.log(localStorage.getItem('paths'));
    doc = new jsPDF();
}


var getImageFromUrl = function(url, page, callback) {
    var img = new Image();

    img.onError = function() {
        alert('Cannot load image: "'+url+'"');
    };

    img.onload = function() {
        callback(img, page);
    };

    img.src = url;
}


var createPDF = function(imgData, i) {
    if(i > 0) {
        doc.addPage();
    }

    doc.addImage(imgData, 'JPEG', 0,0 );

    console.log('added!');
    if(i == NUM_PAGES) {
        doc.save("download.pdf"); 
    }
}



function download_pages() {
    var paths = JSON.parse(localStorage.getItem("paths"));
   
    for(var i=0; i<paths.length; i++) {
        var url = "/static/" + paths[i] ;
        getImageFromUrl(url, i, createPDF);
    }
    
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
        url: 'https://coloring-book-257804.appspot.com/generate_pages',
        type: 'POST',
        data: formData,
        dataType: "json",
        success: function (data) {
            localStorage.setItem('paths', JSON.stringify(data.paths));
            window.location.replace("https://coloring-book-257804.appspot.com/book");
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
