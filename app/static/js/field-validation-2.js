var inputs = document.querySelectorAll('th[type="text"]');
var submitButton = document.getElementById('submit-table-2');

inputs.forEach(function (input) {
    input.addEventListener('input', validateInput);
});

function validateInput() {
    var input1 = document.getElementById('form-field-5').value;
    var input2 = document.getElementById('form-field-6').value;
    var input3 = document.getElementById('form-field-7').value;
    var input4 = document.getElementById('form-field-8').value;

    var isDisabled = (input1.trim() === '' || input2.trim() === '' || input3.trim() === '' || input4.trim() === '') ||
                     (!isValidInput(input1, 30) || !isValidInput(input2, 30) || !isValidInput(input3, 150) || !isValidInput(input4, 150));

    submitButton.disabled = isDisabled;
}

function isValidInput(input, maxLength) {
    var regex = /^[a-zA-Z 0-9-,.()'/"]+$/;
    return input.length <= maxLength && regex.test(input);
}