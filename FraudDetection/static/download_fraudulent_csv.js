function downloadCsv() {
    var form = document.createElement('form');
    form.action = '/download-csv';
    form.method = 'POST';
    document.body.appendChild(form);
    form.submit();
}