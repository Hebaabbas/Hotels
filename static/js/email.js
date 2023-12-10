// Function to send an email using the emailjs service
function sendMail(){
    // Gathering data from the form inputs
    var templateParams = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value,
    }
    // Sending the email with the specified service and template IDs, and the parameters from the form
    emailjs.send('service_u77afju', 'template_mageqwt', templateParams, "rbSvDk825LGhLJpd6")
        .then(function(response) {
            // Handling successful email submission
           console.log('Success', response.status, response.text);
        }, function(error) {
            // Handling errors during email submission
           console.log('Failure', error);
        });
    }