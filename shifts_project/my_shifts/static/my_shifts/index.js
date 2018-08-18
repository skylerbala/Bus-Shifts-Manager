var dataTableMyShifts = $('#table-database-my-shifts').DataTable({
  "scrollY": "500px",
  "scrollCollapse": true,
  "paging": false,
});

$('.dataTables_length').addClass('bs-select');

// MARKET POST
$('.market-post-button').on('click', function (ev) {
  ev.stopPropagation();
});

$('.market-post-form').submit((e) => {
  e.preventDefault()

  let message = ''
  let form = e.target
  let action = ''
  
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
      },
      cancel: {
        label: 'No',
        className: 'btn-danger',
      }
    },
    callback: (result) => {
      if (result) {
        $.ajax({
          data: $(form).serialize(), // get the form data
          type: $(form).attr('method'), // GET or POST
          url: $(form).attr('data-post-url'), // the file to call
          success: (response) => { // on success..
            dataTableMyShifts.row($(form).parents('tr')[0]).remove().draw()
          }
        });
      }
    }
  });
})

$('.fb-share-button').on('click', function (ev) {
  ev.stopPropagation();
});













/*

// MARKET POST
$('.market-post-button').on('click', function (ev) {
  ev.stopPropagation();
});

$('.market-post-form').submit((e) => {
  e.preventDefault()

  let message = ''
  let form = e.target
  let action = ''
  
  if ($(form).find('button')[0].textContent.trim() == 'Post') {
    action = $(form).attr('data-post-url');
    message = '<strong>Are you sure you want to POST the following shift?</strong><br>'
  }
  else {
    action = $(form).attr('data-cancel-url');
    message = '<strong>Are you sure you want to REMOVE the following shift from the shift market?</strong><br>'
  }
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
      },
      cancel: {
        label: 'No',
        className: 'btn-danger',
      }
    },
    callback: (result) => {
      if (result) {
        $.ajax({
          data: $(form).serialize(), // get the form data
          type: $(form).attr('method'), // GET or POST
          url: action, // the file to call
          success: (response) => { // on success..
            console.log(response)
            if (response['shift-filled']) {
      
            }
            if (action == $(form).attr('data-post-url')) {
              $(form).find('button')[0].textContent = 'Cancel'
            }
            else {
              $(form).find('button')[0].textContent = 'Post'
            }
          }
        });
      }
    }
  });
})

$('.fb-share-button').on('click', function (ev) {
  ev.stopPropagation();
});


*/