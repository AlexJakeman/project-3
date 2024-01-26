var submitButtons = document.querySelectorAll('[id^="submit-table-"]');

submitButtons.forEach(function (submitButton) {
    var wordId = submitButton.id.split('-')[2]; // Extract wordId from the submit button's ID

    var inputs = document.querySelectorAll('[id^="added-field-' + wordId + '"], [id^="term-field-' + wordId + '"], [id^="context-field-' + wordId + '"], [id^="meaning-field-' + wordId + '"]');

    inputs.forEach(function (input) {
        var feedback = createFeedbackElement(input);
        input.parentNode.appendChild(feedback);

        input.addEventListener('input', function () {
            validateInput(wordId);
        });
    });

    function validateInput(wordId) {
        var input1 = document.getElementById('added-field-' + wordId).value;
        var input2 = document.getElementById('term-field-' + wordId).value;
        var input3 = document.getElementById('context-field-' + wordId).value;
        var input4 = document.getElementById('meaning-field-' + wordId).value;

        updateFeedback('added-field-' + wordId, !isValidInput(input1, 30));
        updateFeedback('term-field-' + wordId, !isValidInput(input2, 30));
        updateFeedback('context-field-' + wordId, !isValidInput(input3, 150));
        updateFeedback('meaning-field-' + wordId, !isValidInput(input4, 150));

        var isDisabled = (input1.trim() === '' || input2.trim() === '' || input3.trim() === '' || input4.trim() === '') ||
            !isValidInput(input1, 30) || !isValidInput(input2, 30) || !isValidInput(input3, 150) || !isValidInput(input4, 150);

        submitButton.disabled = isDisabled;
    }

    function createFeedbackElement(input) {
        var feedbackId = 'feedback-' + input.id;
        var existingFeedback = document.getElementById(feedbackId);

        if (existingFeedback) {
            return existingFeedback;
        }

        var feedback = document.createElement('div');
        feedback.id = feedbackId;
        feedback.className = 'feedback';
        return feedback;
    }

    function updateFeedback(inputId, isInvalid) {
        var feedbackId = 'feedback-' + inputId;
        var feedback = document.getElementById(feedbackId);

        if (!feedback) {
            feedback = createFeedbackElement(document.getElementById(inputId));
            input.parentNode.appendChild(feedback);
        }

        feedback.textContent = isInvalid ? 'Invalid input' : '';
    }
});

function isValidInput(input, maxLength) {
    var regex = /^[a-zA-Z 0-9-,.()'/"]+$/;
    return input.length <= maxLength && regex.test(input);
}