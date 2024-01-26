var inputs = document.querySelectorAll('input[type="text"]');
var submitButton = document.getElementById('submit-table-2');

inputs.forEach(function (input) {
    input.addEventListener('input', validateInput);
});

function validateInput() {
    var input1 = document.getElementById('form-field-1').value;
    var input2 = document.getElementById('form-field-2').value;
    var input3 = document.getElementById('form-field-3').value;
    var input4 = document.getElementById('form-field-4').value;

    var isValid1 = isValidInput(input1, 30);
    var isValid2 = isValidInput(input2, 30);
    var isValid3 = isValidInput(input3, 150);
    var isValid4 = isValidInput(input4, 150);

    var isDisabled = (input1.trim() === '' || input2.trim() === '' || input3.trim() === '' || input4.trim() === '') ||
                     (!isValid1 || !isValid2 || !isValid3 || !isValid4);

    submitButton.disabled = isDisabled;

    displayFeedback('feedback-added-add-1', isValid1, input1);
    displayFeedback('feedback-added-add-2', isValid2, input2);
    displayFeedback('feedback-added-add-3', isValid3, input3);
    displayFeedback('feedback-added-add-4', isValid4, input4);
}

function isValidInput(input, maxLength) {
    var regex = /^[a-zA-Z 0-9-,.()'/"]+$/;
    return input.length <= maxLength && regex.test(input);
}

function displayFeedback(feedbackId, isValid, inputValue) {
    var feedbackElement = document.getElementById(feedbackId);

    if (!isValid && inputValue.trim() !== '') {
        feedbackElement.innerHTML = 'Invalid input.';
        feedbackElement.style.color = '#fed136';
    } else {
        feedbackElement.innerHTML = '';
    }
}