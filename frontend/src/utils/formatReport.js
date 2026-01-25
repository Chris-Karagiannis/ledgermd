export function formatReport() {
    // Make table look nice
    const tables = document.querySelectorAll("table")

    tables.forEach(table => {
        table.classList.add("table", "border", "table-hover")
    });
}