var dataTable = $('#table-database-shifts').DataTable({
  "scrollY": "500px",
  "scrollCollapse": true,
  "paging": false,
});

$('.dataTables_length').addClass('bs-select');

// ADD SHIFT FORM VALIDATION
$.validator.addMethod('timeBounds', (value, element) => {
  let endtime = value
  let starttime = $(element).parent().prev()[0].children[1].value
  return (starttime < endtime) ? true: false
}, 'Your error message!');

$('#shift-add-form').validate({
  rules: {
    start_datetime: {
      required: true,
    },
    end_datetime: {
      required: true,
      timeBounds: true,
    },
    start_datetime_run_0: {
      required: true,
    },
    end_datetime_run_0: {
      required: true,
      timeBounds: true,
    },
    start_datetime_run_1: {
      required: true,
    },
    end_datetime_run_1: {
      required: true,
      timeBounds: true,
    },
    start_datetime_run_2: {
      required: true,
    },
    end_datetime_run_2: {
      required: true,
      timeBounds: true,
    },
    start_datetime_run_3: {
      required: true,
    },
    end_datetime_run_3: {
      required: true,
      timeBounds: true,
    },
    start_datetime_run_4: {
      required: true,
    },
    end_datetime_run_4: {
      required: true,
      timeBounds: true,
    },
    start_datetime_run_5: {
      required: true,
    },
    end_datetime_run_5: {
      required: true,
      timeBounds: true,
    },
    start_datetime_run_6: {
      required: true,
    },
    end_datetime_run_6: {
      required: true,
      timeBounds: true,
    },
    start_datetime_run_7: {
      required: true,
    },
    end_datetime_run_7: {
      required: true,
      timeBounds: true,
    },
    start_datetime_run_8: {
      required: true,
      timeBounds: true,
    },
    end_datetime_run_8: {
      required: true,
      timeBounds: true,
    },
    start_datetime_run_9: {
      required: true,
    },
    end_datetime_run_9: {
      required: true,
      timeBounds: true,
    },
  },
  messages: {
    start_datetime: {
      required: 'Datetime input required',
      },
      end_datetime: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
      start_datetime_run_0: {
      required: 'Datetime input required',
      },
      end_datetime_run_0: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
      start_datetime_run_1: {
      required: 'Datetime input required',
      },
      end_datetime_run_1: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
      start_datetime_run_2: {
      required: 'Datetime input required',
      },
      end_datetime_run_2: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
      start_datetime_run_3: {
      required: 'Datetime input required',
      },
      end_datetime_run_3: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
      start_datetime_run_4: {
      required: 'Datetime input required',
      },
      end_datetime_run_4: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
      start_datetime_run_5: {
      required: 'Datetime input required',
      },
      end_datetime_run_5: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
      start_datetime_run_6: {
      required: 'Datetime input required',
      },
      end_datetime_run_6: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
      start_datetime_run_7: {
      required: 'Datetime input required',
      },
      end_datetime_run_7: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
      start_datetime_run_8: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
      end_datetime_run_8: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
      start_datetime_run_9: {
      required: 'Datetime input required',
      },
      end_datetime_run_9: {
      required: 'Datetime input required',
      timeBounds: "Time bounds error; Can't have an end datetime earlier than a start datetime",
      },
  },
  invalidHandler: (event, validator) => {

  },
  submitHandler: (form) => {
    data = $(form).serializeArray()
    shiftStart = data[1].value
    shiftEnd = data[2].value
    if (data[3].value == null) {
      shiftEmployee = 'Open'
    }
    else {
      shiftEmployee = data[3].value
    }
    
    shiftRuns = ''
    for (let i = 7; i < data.length; i+=3) {
      if  (i == (data.length - 1)) {
        shiftRuns += data[i].value
      }
      else {
        shiftRuns += data[i].value + ', '
      }
    }
    let message = '<strong>Confirm the following information is correct.</strong><br>'
    message += 'Start Datetime: ' + shiftStart + '<br>End Datetime: ' + shiftEnd + '<br>Runs: ' + shiftRuns
    bootbox.confirm(message, () => {
      $.ajax({
        data: $(form).serialize(), // get the form data
        type: $(form).attr('method'), // GET or POST
        url: $(form).attr('action'), // the file to call
        success: (response) => { // on success..Z
          var clone = $('#table-database-shifts').find('tr').clone(true)[1]
          let dataTags = $(clone).children('td')
          dataTags[0].textContent = response.shiftID
          dataTags[1].textContent = response.coverage
          dataTags[2].textContent = response.lines
          dataTags[3].textContent = response.date
          dataTags[4].textContent = response.day
          dataTags[5].textContent = response.startTime
          dataTags[6].textContent = response.endTime
          dataTable.row.add(clone).draw()

        },
      });
    })
  }
});

// ADD SHIFT POST
$('#shift-add-form').submit((e) => {
  e.preventDefault()
  $('#shift-add-form').valid()
});

$('[data-toggle="datepicker"]').datetimepicker({
  format:'m/d/Y H:i',
  mask: true,
  todayButton: true,
});

$('#id_number_of_runs').change(() => {
    var selector = document.getElementById('id_number_of_runs');
    var choice = selector[selector.selectedIndex].value;
    var myNode = document.getElementById("id_run_forms");
    while (myNode.firstChild) {
        myNode.removeChild(myNode.firstChild);
    }
    let run_forms = document.querySelector('#id_run_forms');
    for (let i = 0; i < choice; i++) {
        let form = document.querySelector('#shift-form-og');
        form = form.cloneNode(true);
        form.querySelector('#form-title').textContent = 'Run ' + (i+1);
        form.querySelector('#id_start_datetime').name = 'start_datetime_run_' + i;
        form.querySelector('#id_end_datetime').name = 'end_datetime_run_' + i;
        form.querySelector('#id_start_datetime').value = '';
        form.querySelector('#id_end_datetime').value = '';

        form.querySelector('#id_start_datetime').setAttribute("data-toggle", "datepicker" + i);
        form.querySelector('#id_end_datetime').setAttribute("data-toggle", "datepicker" + i);
        function genCharArray(charA, charZ) {
            var a = ['---------'], i = charA.charCodeAt(0), j = charZ.charCodeAt(0);
            for (; i <= j; ++i) {
                a.push(String.fromCharCode(i));
            }
            return a;
        }
        let alphabet = genCharArray('A', 'Z')

        let label = document.createElement('label');
        label.for = 'id_line_select'
        label.textContent = 'Line:   '
        
        let selectEl = document.createElement('select');
        selectEl.id = 'id_line_select'
        selectEl.name = 'run_line' + i

        let container = document.createElement('div');
        container.append(label, selectEl)

        let optionList = selectEl.options;
  
        alphabet.forEach(option =>
          optionList.add(
            new Option(option, option)
          )
        );

        form.appendChild(container);
        

        form.querySelector('#id_start_datetime').id = 'id_start_datetime_run_' + i;
        form.querySelector('#id_end_datetime').id = 'id_end_datetime_run_' + i;

        run_forms.appendChild(form);

        var datepickerName = 'datepicker' + i;
        $('[data-toggle="' + datepickerName + '"]').datetimepicker({
          format:'m/d/Y H:i',
          mask: true,
          todayButton: true,
        });
    }
});









$('.market-shift-delete').click((e) => {
  e.preventDefault()

  let message = '<strong>Are you sure you want to delete the following shift?</strong><br>'
  let form = e.target;
  
  data = $(form).parent().parent().siblings()
  console.log(data)
  lines = data[2].textContent
  date = data[3].textContent
  day = data[4].textContent
  starttime = data[5].textContent
  endtime = data[6].textContent

  message += 'Start Time: ' + starttime + '<br>End Time: ' + endtime + '<br>Day: ' + day + '<br>Date: ' + date + '<br>Lines: ' + lines;

  bootbox.confirm({
    size: 'large',
    title: 'Shift Delete',
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
            dataTable.row($(form).parents('tr')).remove().draw()
            $('#bootbox-button-alert')[0].textContent = 'Shift Deleted'
            $('#bootbox-button-alert').show(700, () => {
              $('#bootbox-button-alert').fadeOut(3000)
            })
          }
        });
      }
    }
  });
})


