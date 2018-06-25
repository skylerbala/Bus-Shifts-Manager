from shifts_app.shift import Shift
from django.utils.timezone import utc, make_aware, get_default_timezone
import datetime


def main():
	start_datetime = make_aware(datetime.datetime(2018,6,8,10,0), get_default_timezone())
	end_datetime = make_aware(datetime.datetime(2018,6,8,11,0), get_default_timezone())

	run_times_list = [
				{'start_time':datetime.time(8,9), 'end_time':datetime.time(9,10)},
			]


	shift = Shift.objects.create_shift(start_datetime, end_datetime, run_times_list)



main()