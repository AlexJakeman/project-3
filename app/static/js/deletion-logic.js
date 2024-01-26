document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.delete-btn');
    const deleteForm = document.getElementById('deleteForm');
    const modalDeleteBtn = document.querySelector('.delete-modal-btn');

    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const rowId = this.closest('tr').dataset.rowId;
            document.getElementById('selectedRowId').value = rowId;
            deleteForm.action = "/delete_term/" + rowId;
        });
    });

    modalDeleteBtn.addEventListener('click', function () {
    });
});