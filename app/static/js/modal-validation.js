var inputs = document.querySelectorAll('th[type="text"]');
var submitButton = document.getElementById('submit-table-{{ word.Id }}');

button.addEventListener('click', function () {
    const rowId = this.closest('tr').dataset.rowId;
    document.getElementById('selectedRowId').value = rowId;
});

inputs.forEach(function (input) {
    input.addEventListener('input', validateInput);
});

function validateInput() {
    var input1 = document.getElementById('term-field-').value;
    var input2 = document.getElementById('added-field-{{ word.Id }}').value;
    var input3 = document.getElementById('context-field-{{ word.Id }}').value;
    var input4 = document.getElementById('meaning-field-{{ word.Id }}').value;

    console.log(input1, input2, input3, input4)

    var isDisabled = (input1.trim() === '' || input2.trim() === '' || input3.trim() === '' || input4.trim() === '') ||
                     (!isValidInput(input1, 30) || !isValidInput(input2, 30) || !isValidInput(input3, 150) || !isValidInput(input4, 150));

    submitButton.disabled = isDisabled;
}

function isValidInput(input, maxLength) {
    var regex = /^[a-zA-Z 0-9-,.()'/"]+$/;
    return input.length <= maxLength && regex.test(input);
}