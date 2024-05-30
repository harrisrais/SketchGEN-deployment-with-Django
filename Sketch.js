window.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const sketchUrl = params.get('sketchUrl');
    if (sketchUrl) {
        const sketchResultDiv = document.getElementById('sketchResult');
        const img = document.createElement('img');
        img.src = sketchUrl;
        img.alt = 'Sketch';
        img.className = 'img-fluid';
        sketchResultDiv.appendChild(img);
    } else {
        alert('No sketch found.');
    }
});