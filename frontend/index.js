const fileInput = document.getElementById('file-input');
const submitBtn = document.getElementById('submit-btn');
const imageOutput = document.getElementById('image-output');

API_URL = 'http://127.0.0.1:5000/api'

submitBtn.addEventListener('click', async (event) => {
    // prevent the page from reloading
    event.preventDefault();

    // get the file and prepare it for sending
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    postImage(formData)
    
});


/**
 * Send the image to the API.
 * Then show the returned image in <img id="image-output"/> 
 */
function postImage(data) {
    fetch(`${API_URL}/predict`, {
        method: 'POST',
        body: data
    })
    .then(response => {
        response.text()
            .then((data) => {
                removeTmpMessage()

                const imageOutput = document.getElementById('image-output');
                imageOutput.src = `data:image/png;base64,${data}`;
            })
    })

}


/**
 * Remove the tempoary message "Predictions will be shown below".
 */
function removeTmpMessage() {
    const element = document.getElementById("tmp-message");
    element.remove();
}

/**
 * Display the date
 */ 
function displayCurrentDate() {
    const currentDate = new Date();
    const day = currentDate.getDate();
    const month = currentDate.getMonth() + 1;
    const year = currentDate.getFullYear();
    const dateString = `${day}/${month}/${year}`;
    
    document.getElementById('date').innerHTML = dateString
}

displayCurrentDate()