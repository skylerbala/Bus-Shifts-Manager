from shifts_app.run import Run
from shifts_app.shift import Shift
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime


def main():
	start_datetime = make_aware(datetime.datetime(2016,5,1), get_default_timezone())
	end_datetime = make_aware(datetime.datetime(2016,5,3), get_default_timezone())

	run_times_list = [
				{'start_time':datetime.time(11,30), 'end_time':datetime.time(12,30)},
				{'start_time':datetime.time(12,30), 'end_time':datetime.time(13,30)},
				{'start_time':datetime.time(13,30), 'end_time':datetime.time(14,30)},
				{'start_time':datetime.time(14,30), 'end_time':datetime.time(19,30)},
				{'start_time':datetime.time(19,30), 'end_time':datetime.time(1,30)},
				{'start_time':datetime.time(1,30), 'end_time':datetime.time(13,30)},
			]


	shift = Shift.objects.create_shift(start_datetime, end_datetime, run_times_list)



main()