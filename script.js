
document.getElementById('deployForm').addEventListener('submit', function (e) {
    e.preventDefault();  // Prevent form from submitting the traditional way

    const botCode = document.getElementById('bot_code').files[0];
    const requirementsFile = document.getElementById('requirements').files[0];

    // Create FormData to send files
    const formData = new FormData();
    formData.append('bot_code', botCode);
    formData.append('requirements', requirementsFile);

    // Send the files to the Flask API
    fetch('http://localhost:5000/deploy', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('statusMessage').innerText = 'Bot deployed successfully!';
    })
    .catch(error => {
        document.getElementById('statusMessage').innerText = 'Error deploying bot.';
    });
});
    