$(document).ready(function() {
  $('th.sortable').click(function() {
    var table = $(this).parents('table').eq(0);
    var rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()));
    var sortArrow = $(this).find('.sort-arrow');
    $('th span.sort-arrow').not(sortArrow).removeClass('asc desc').html('');
    sortArrow.toggleClass('asc desc');
    if (sortArrow.hasClass('asc')) {
      sortArrow.html('&#9650;');
      rows = rows.reverse();
    } else {
      sortArrow.html('&#9660;');
    }
    for (var i = 0; i < rows.length; i++) {
      table.append(rows[i]);
    }
  });
});


  function comparer(index) {
    return function(a, b) {
      var valA = getCellValue(a, index)
      var valB = getCellValue(b, index)
      return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.localeCompare(valB)
    }
  }
function getCellValue(row, index) {
  return $(row).children('td').eq(index).text()
}
