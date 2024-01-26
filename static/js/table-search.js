function submitSearch() {
    myFunction();
}

function resetTable() {
    var table = document.getElementById("myTable");
    var tr = table.getElementsByTagName("tr");

    for (var i = 0; i < tr.length; i++) {
        tr[i].style.display = "";
    }

    document.getElementById("myInput").value = "";
}

function myFunction() {
    var input, filter, table, tr, th, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");

    var matchingIndices = [];

    if (filter === "") {
        for (i = 0; i < tr.length; i++) {
            tr[i].style.display = "";
        }
    } else {
        for (i = 0; i < tr.length; i++) {
            th = tr[i].getElementsByTagName("th")[1];
            if (th) {
                txtValue = th.textContent || th.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    matchingIndices.push(i);
                }
            }
        }

        for (i = 0; i < tr.length; i++) {
            tr[i].style.display = "none";
        }

        if (matchingIndices.length > 0) {
            for (i = 0; i < matchingIndices.length; i++) {
                tr[matchingIndices[i]].style.display = "";
                for (var j = matchingIndices[i] + 1; j <= matchingIndices[i] + 5 && j < tr.length; j++) {
                    tr[j].style.display = "";
                }
            }
        } else {
            alert("No results found");
        }
    }
}