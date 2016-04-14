from django.test import TestCase
from datetime import datetime, date, time, timedelta
from django.utils.timezone import make_aware, get_default_timezone, utc
from django.db.models import Q
from shifts_app.run import Run
from shifts_app.shift import Shift
from shifts_app.shift_group import ShiftGroup
from shifts_app.test_functions import TestGrouping, ShiftCreation

class RunTests(TestCase):
	#pass in a run that spans overnight but with a shift that spans 25-27 
	#so long as the resulting runs in the shift don't overlap then it's valid

	#all other checks need to be expecting only one output

	def set_up(self):
		#run_times_list  = list of dicts
		
		shift_start_date = date(2016,4,12)
		shift_end_date = date(2016,4,13)
		# 	shift_start_time = time(11,00)
		#	shift_end_time = time(15,00)

		run_times_list = [
					{time(11,00): time(12,00)}, 
					{time(12,00): time(13,00)},
					{time(13,00):  time(14,00)},
					{time(14,00):  time(15,00)}
			]
		
		for key in run_times_list[0]:
			run_start_datetime = make_aware(datetime.combine(shift_start_date,key),utc)
			run_end_datetime = 	make_aware(datetime.combine(shift_start_date, run_times_list[0][key]), utc)

		shift = Shift.objects.create_shift(shift_start_date, shift_end_date, run_times_list)
		run = Run.objects.create(shift = shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
		run_info = [run_start_datetime, run_end_datetime, shift]

		return (run, run_info)
	
	def test_start_datetime(self):
		(run, run_info) = self.set_up()

		self.assertEqual(run.start_datetime, run_info[0])

	def test_end_datetime(self):
		(run, run_info) = self.set_up()
		self.assertEqual(run.end_datetime, run_info[1])

	def test_fk_to_shift(self):
		(run, run_info) = self.set_up()
		self.assertEqual(run.shift, run_info[2])

class ShiftTests(TestCase):

	def set_up(self,case_num):

		shift_start_date = date(2016,4,12)
		shift_end_date = date(2016,4,13)
		shift_start_time = time(11,00)
		shift_end_time = time(15,00)
		shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
		shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)
		shift_info = [shift_start_datetime, shift_end_datetime]
		total_dur = shift_start_datetime - shift_end_datetime
		runs = []
		run_times_list = [
				{time(11,00): time(12,00)}, 
				{time(12,00): time(13,00)},
				{time(13,00):  time(14,00)},
				{time(14,00):  time(15,00)}
		]
		
		shift = Shift.objects.create_shift(shift_start_date, shift_end_date, run_times_list) # can create_shift generate the run times list from the start_datetime and end_datetime

		for i in range(0,5):
			for key in run_times_list[i]:
				run_start_datetime = make_aware(datetime.combine(shift_start_date,key),utc)
				run_end_datetime = 	make_aware(datetime.combine(shift_start_date, run_times_list[i][key]), utc)
				run = Run.objects.create(shift = shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)

			runs.append(run)
			# print "run:%s\n" %(run)

		if case_num == 1:
			return (shift, shift_info)
		
		if case_num == 2:
			return (shift, runs[0])
		
		if case_num == 3:
			num_expected_runs = total_dur / timedelta(hours=1)
			# print "num_expected_runs: %d\n" %(num_expected_runs) 
			return (shift,runs, num_expected_runs)

	def test_shift_creation_start_datetime(self):
		case_num = 1
		(shift, shift_info) = self.set_up(case_num)
		self.assertEqual(shift.start_datetime, shift_info.shift_start_datetime)

	def test_shift_creation_end_datetime(self):
		case_num = 1
		(shift, shift_info) = self.set_up(case_num)
		self.assertEqual(shift.end_datetime.time, shift_info.shift_end_datetime)
	
	def test_reverse_to_run(self):
		case_num = 2
		(shift, run) = self.set_up(case_num)
		shift_run = shift.runs_related.get(id=1)
		self.assertEqual(shift_run, run)

	def test_num_shift_runs(self):
		case_num = 3
		(shift, runs, num_expected_runs) = self.set_up(case_num)
		num_shift_runs = shift.runs_related.count()
		self.assertEqual(num_shift_runs, num_expected_runs)

	def test_shift_first_run(self):
		case_num = 3
		(shift, runs, num_expected_runs) = self.set_up(case_num)
		num_shift_runs = shift.runs_related.count()
		shift_first_run = shift.runs_related.get(id=1)
		expected_first_run = runs[0]
		self.assertEqual(shift_first_run, expected_first_run)

	def test_shift_last_run(self):
		case_num = 3
		(shift, runs, num_expected_runs) = self.set_up(case_num)
		num_shift_runs = shift.runs_related.count()
		shift_last_run = shift.runs_related.get(id=num_shift_runs)
		expected_final_run = runs[len(runs)]
		self.assertEqual(shift_last_run, expected_final_run)
		
# # 	def test_shiftgroup(self):

# # class ShiftGroupTests(TestCase):

# 	# def set_up(self):

# # 	def

# def test_create_recurring_shift(self):
	# 	case_num = 3
	# 	(shift, correct_num_runs) = self.set_up(case_num)
	# 	num_runs = shift.run_related.count()
	# 	self.assertEqual(num_runs, correct_num_runs)
