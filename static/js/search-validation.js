var searchInput = document.getElementById('myInput');
var searchButton = document.getElementById('submit-table-2');

searchInput.addEventListener('input', validateSearchInput);

function validateSearchInput() {
    var searchTerm = searchInput.value.trim();
    searchButton.disabled = searchTerm === '' || !isValidInput(searchTerm, 30);
}

function isValidInput(input, maxLength) {
    var regex = /^[a-zA-Z 0-9-,.()'/"]+$/;
    return input.length <= maxLength && regex.test(input);
}

function submitSearch() {
    console.log('Search submitted!');
}