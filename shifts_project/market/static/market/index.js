var dataTableMarket = $('#table-database-market').DataTable({
  "scrollY": "500px",
  "scrollCollapse": true,
  "paging": false,
});

$('.dataTables_length').addClass('bs-select');

// MARKET POST
$('.market-post-button').on('click', function (ev) {
  ev.stopPropagation();
});

$('.market-shift-cover').click((e) => {
  e.preventDefault()

  let message = '<strong>Are you sure you want to COVER the following shift from the shift market?</strong><br>'
  let form = e.target;
  
  data = $(form).parent().parent().siblings()
  lines = data[2].textContent
  date = data[3].textContent
  day = data[4].textContent
  starttime = data[5].textContent
  endtime = data[6].textContent

  message += 'Start Time: ' + starttime + '<br>End Time: ' + endtime + '<br>Day: ' + day + '<br>Date: ' + date + '<br>Lines: ' + lines;

  bootbox.confirm({
    size: 'large',
    title: 'Shift Post',
    message: message,
    buttons: {
      confirm: {
        label: 'Yes',
        className: 'btn-success',
        callback: () => {
          
        }
      },
      cancel: {
        label: 'No',
        className: 'btn-danger',
      }
    },
    callback: (result) => {
      if (result) {
        $.ajax({
          data: '',
          type: 'POST', // GET or POST
          url: $(form).attr('href'), // the file to call
          success: (response) => { // on success..
            dataTableMarket.row($(form).parents('tr')).remove().draw()
            $('#bootbox-button-alert')[0].textContent = 'Shift Covered'
            $('#bootbox-button-alert').show(700, () => {
              $('#bootbox-button-alert').fadeOut(3000)
            })
          }
        });
      }
    }
  });
})

$('.fb-share-button').on('click', function (ev) {
  ev.stopPropagation();
});

