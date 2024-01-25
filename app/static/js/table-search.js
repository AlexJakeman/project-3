    function submitSearch() {
        myFunction(); // Call the search function when the button is clicked
    }

    function resetTable() {
        var table = document.getElementById("myTable");
        var tr = table.getElementsByTagName("tr");

        // Show all rows
        for (var i = 0; i < tr.length; i++) {
            tr[i].style.display = "";
        }

        // Clear the search input
        document.getElementById("myInput").value = "";
    }

    function myFunction() {
        var input, filter, table, tr, th, i, txtValue;
        input = document.getElementById("myInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("myTable");
        tr = table.getElementsByTagName("tr");

        // Array to store indices of matching <th> elements
        var matchingIndices = [];

        if (filter === "") {
            // If the filter is empty, show all rows
            for (i = 0; i < tr.length; i++) {
                tr[i].style.display = "";
            }
        } else {
            for (i = 0; i < tr.length; i++) {
                th = tr[i].getElementsByTagName("th")[1];
                if (th) {
                    txtValue = th.textContent || th.innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {
                        // If the <th> is found, store its index
                        matchingIndices.push(i);
                    }
                }
            }

            // Hide all rows by default
            for (i = 0; i < tr.length; i++) {
                tr[i].style.display = "none";
            }

            if (matchingIndices.length > 0) {
                // Show rows corresponding to matching <th> elements
                for (i = 0; i < matchingIndices.length; i++) {
                    tr[matchingIndices[i]].style.display = "";
                    // Show the next 5 rows following the matching <th>
                    for (var j = matchingIndices[i] + 1; j <= matchingIndices[i] + 5 && j < tr.length; j++) {
                        tr[j].style.display = "";
                    }
                }
            }
        }
    }