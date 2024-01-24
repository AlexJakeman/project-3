function deleteTerm(id) {
    if (confirm("Are you sure you want to delete this term?")) {
        // Manually set the form action and submit it
        const form = document.getElementById(`deleteForm${id}`);
        form.action = `/delete/${id}`;
        form.submit();
    }
}