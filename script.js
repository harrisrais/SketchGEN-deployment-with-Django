document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const fileInput = document.getElementById('file');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Redirect to sketch.html with the sketch URL as a query parameter
            window.location.href = 'Sketch.html?SketchUrl=' + encodeURIComponent(data.SketchUrl);
        } else {
            alert('Failed to process the image.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
