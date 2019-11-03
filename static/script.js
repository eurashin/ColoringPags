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
var index = 0; 

function change_image(i) {
    var paths = JSON.parse(localStorage.getItem('paths'));
    var path = "/static/images/" + paths[i];
    $('#map').css("background-image", "url('" + path + "')");  
}

function swipe_left() {
    if(index >= 1) { // Can swipe left
        index--; 
        change_image(index); 
    }
}


function swipe_right() {
    if(index <= 8) { // Can swipe left
        index++; 
        change_image(index);
    }
}

function on_book_load(directory) {
    console.log(localStorage.getItem('paths'));

    // Display the first image
    change_image(0);
   
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
    
    console.log(url);
    img.src = url;
}


var createPDF = function(imgData, i) {
    doc.addImage(imgData, 'JPEG', 0,0 );

    console.log('added!');
    if(i == NUM_PAGES) {
        doc.save("download.pdf"); 
    }
}



function download_pages() {
    var paths = JSON.parse(localStorage.getItem("paths"));
   
    for(var i=0; i<NUM_PAGES+1; i++) {
        var url = "/static/images/" + paths[i] ;
        getImageFromUrl(url, i, createPDF);
    }
    
}

function make_coloring_book() {
    // Get the input form elements
    var link_string = $("#drive_link").val() ; 
    var start_string = $("#start").val() ; 
    var end_string = $("#end").val();

    var formData = new FormData();
    formData.append('link', link_string);
    formData.append('start', start_string);
    formData.append('end', end_string);


    $.ajax({
//        url: 'https://coloring-book-257804.appspot.com/generate_pages',
        url: 'http://localhost:8080/generate_pages',
        type: 'POST',
        data: formData,
        dataType: "json",
        success: function (data) {
            localStorage.clear();
            localStorage.setItem('paths', JSON.stringify(data.paths));
            //window.location.replace("https://coloring-book-257804.appspot.com/book");
            window.location.replace("http://localhost:8080/book");
        },
        cache: false,
        contentType: false,
        processData: false
    });
}


// [END gae_python37_log]
