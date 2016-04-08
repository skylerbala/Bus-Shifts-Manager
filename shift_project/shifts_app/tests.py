from django.test import TestCase
from datetime import datetime, date, time, timedelta
from django.utils.timezone import make_aware, get_default_timezone, utc
from django.db.models import Q
from shifts_app.run import Run
from shifts_app.shift import Shift
from shifts_app.shift_group import ShiftGroup

class RunTests(TestCase):

	def set_up(self):
		start_date = date.today()
		end_date =  start_date + timedelta(days=7)
		start_time = time(12,30)
		end_time =	time(13,30)

		start_datetime = make_aware(datetime.combine(start_date, start_time),utc)
		end_datetime = make_aware(datetime.combine(date.today(), end_time),utc)
		shift = Shift.objects.create(start_date= start_date, end_date= end_date)
		run = Run.objects.create(shift=shift, start_datetime=start_datetime, end_datetime=end_datetime)

		return (shift,run,start_datetime,end_datetime)
	
	def test_start_datetime(self):
		(shift,run,start_datetime,end_datetime) = self.set_up()
		self.assertEqual(run.start_date,start_datetime)

	def test_end_datetime(self):
		(shift,run,start_datetime,end_datetime) = self.set_up()
		self.assertEqual(run.end_datetime, end_datetime)

	def test_fk_to_shift(self):
		(shift,run,start_datetime,end_datetime) = self.set_up()
		self.assertEqual(run.shift,shift)

class ShiftTests(TestCase):

	def set_up(self,case_num):

		if case_num == 1:
			start_date = date.today()
			end_date =  start_date + timedelta(days=7)
			shift = Shift.objects.create(start_date = start_date)
			return (shift, start_date)

		if case_num == 2:
			start_date = date.today()
			end_date =  start_date + timedelta(days=7)
			start_time = time(12,30)
			end_time =	time(13,30)

			start_datetime = make_aware(datetime.combine(start_date, start_time),utc)
			end_datetime = make_aware(datetime.combine(date.today(), end_time),utc)
			shift = Shift.objects.create(start_date= start_date, end_date= end_date)
			run = Run.objects.create(shift=shift, start_datetime=start_datetime, end_datetime=end_datetime)
			return (shift, run)

		if case_num == 3:
			shift_range = 21
			num_weeks = shift_range / 7 # correct_num_runs
			start_date = date.today()
			end_date =  date.today() + timedelta(days=shift_range)
			cur_date = date.today()

			shift = Shift.objects.create(start_date = start_date, end_date = end_date)
			for i in range(0,num_weeks + 1):
				start_datetime = make_aware(datetime.combine(cur_date, time(12,30)), utc)
				end_datetime = make_aware(datetime.combine(cur_date, time(13,30)), utc)
				run = Run.objects.create(shift=shift, start_datetime=start_datetime, end_datetime=end_datetime)
				cur_date = cur_date + timedelta(days=7 * i)
			return (shift, num_weeks)

		if case_num == 4:
			start_date = date.today()
			end_date =  start_date + timedelta(days=7)
			shift = Shift.objects.create(start_date = start_date, end_date= end_date)
			return (shift, start_date, end_date)

	def test_reverse_to_run(self):
		case_num = 2
		(shift, run) = self.set_up(case_num)
		self.assertEqual(shift.run_related.filter(id=1), run)

	def test_create_single_shift(self):
		case_num = 1
		(shift, start_date) = self.set_up(case_num)
		self.assertEqual(shift.start_date, start_date)

	def test_create_recurring_shift(self):
		case_num = 3
		(shift, correct_num_runs) = self.set_up(case_num)
		num_runs = shift.run_related.count()
		self.assertEqual(num_runs, correct_num_runs)

	def test_start_date(self):
		case_num = 4
		(shift, start_date, end_date) = self.set_up(case_num)
		self.assertEqual(shift.start_date, start_date)

	def test_end_date(self):
		case_num = 4
		(shift, start_date, end_date) = self.set_up(case_num)
		self.assertEqual(shift.end_date)

# 	def test_gap(self):
		
		


# # 	def test_shiftgroup(self):

# # class ShiftGroupTests(TestCase):

# 	# def set_up(self):

# # 	def