from django.test import TestCase
from datetime import datetime, date, time, timedelta
from django.utils.timezone import make_aware, get_default_timezone, utc
from django.db.models import Q
from shifts_app.run import Run
from shifts_app.shift import Shift
from shifts_app.shift_group import ShiftGroup

class RunTests(TestCase):
	#pass in a run that spans overnight but with a shift that spans 25-27 
	#so long as the resulting runs in the shift don't overlap then it's valid

	#all other checks need to be expecting only one output

	def set_up(self, case_num):

		if case_num == 1:
			shift_start_date = date(2016,4,12)
			shift_end_date = date(2016,4,13)
			shift_start_time = time(11,00)
			shift_end_time = time(15,00)
			shift_start_datetime = make_aware(datetime.combine(shift_start_date, shift_start_time), utc)
			shift_end_datetime = make_aware(datetime.combine(shift_end_date, shift_end_time),utc)

			run_times_list = [
					{'start_time':time(11,00), 'end_time': time(12,00)}, 
					{'start_time':time(12,00), 'end_time':time(13,00)},
					{'start_time':time(13,00), 'end_time':time(14,00)},
					{'start_time':time(14,00), 'end_time':time(15,00)}
			]
				
			for key in run_times_list:
				run_start_datetime = make_aware(datetime.combine(shift_start_date,key['start_time']),utc)
				run_end_datetime = 	make_aware(datetime.combine(shift_start_date, key['end_time']), utc)

			shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
			run = Run.objects.create(shift = shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
			run_info = [run_start_datetime, run_end_datetime, shift]

			return (run, run_info)
		
		if case_num == 2:
			shift_start_date = date(2016,4,12)
			shift_end_date = date(2016,4,14)
			shift_start_time = time(00,00)
			shift_end_time = time(1,00)
			shift_start_datetime = make_aware(datetime.combine(shift_start_date, shift_start_time), utc)
			shift_end_datetime = make_aware(datetime.combine(shift_end_date,shift_end_time),utc)
			runs = []

			run_times_list = [
					{'start_time':time(11,00), 'end_time':time(0,00)}, 
					{'start_time':time(00,00), 'end_time':time(1,00)},
					{'start_time':time(1,00), 'end_time':time(2,00)},
					{'start_time':time(2,00), 'end_time':time(3,00)},
					{'start_time':time(3,00), 'end_time':time(4,00)},
					{'start_time':time(4,00), 'end_time':time(5,00)},
			]
			
			shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
			dummy_shift = Shift.objects.create(start_datetime = shift_start_datetime, end_datetime = shift_end_datetime)

			for key in run_times_list:
				run_start_datetime = make_aware(datetime.combine(shift_start_date,key['start_time']),utc)
				run_end_datetime = 	make_aware(datetime.combine(shift_start_date, key['end_time']), utc)
				run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)

			return (runs, shift)

	def test_start_datetime(self):
		case_num = 1
		(run, run_info) = self.set_up(case_num)

		self.assertEqual(run.start_datetime, run_info[0])

	def test_end_datetime(self):
		case_num = 1
		(run, run_info) = self.set_up(case_num)
		self.assertEqual(run.end_datetime, run_info[1])

	def test_fk_to_shift(self):
		case_num = 1
		(run, run_info) = self.set_up(case_num)
		self.assertEqual(run.shift, run_info[2])

	def test_twenty_four_hour_run(self):
		case_num = 2
		overlap = False
		#check that the number of runs in runs is equal to the number of runs in shift
		#check that the consecutive runs in shift don't overlap
		#assert whether or not overlap is false

class ShiftTests(TestCase):

	def set_up(self,case_num):

		shift_start_date = date(2016,4,12)
		shift_end_date = date(2016,4,13)
		shift_start_time = time(11,00)
		shift_end_time = time(15,00)
		shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
		shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)
		shift_info = [shift_start_datetime, shift_end_datetime]
		total_dur = abs(shift_start_datetime.hour - shift_end_datetime.hour)
		runs = []
		run_times_list = [
				{'start_time':time(11,00), 'end_time': time(12,00)}, 
				{'start_time':time(12,00),'end_time':time(13,00)},
				{'start_time':time(13,00), 'end_time':time(14,00)},
				{'start_time':time(14,00), 'end_time':time(15,00)}
		]
		
		shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
		dummy_shift = Shift.objects.create(start_datetime = shift_start_datetime, end_datetime = shift_end_datetime)

		for key in run_times_list:
			run_start_datetime = make_aware(datetime.combine(shift_start_date, key['start_time']),utc)
			run_end_datetime = 	make_aware(datetime.combine(shift_start_date, key['end_time']), utc)
			run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
			runs.append(run)

		if case_num == 1:
			shift_start_date = date(2016,4,12)
			shift_end_date = date(2016,4,12)
			shift_start_time = time(11,00)
			shift_end_time = time(15,00)

			shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
			shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)

			shift_info = [shift_start_datetime, shift_end_datetime]
			run_times_list = [
					{'start_time':time(11,00), 'end_time': time(12,00)}
			]
			shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
			return (shift, shift_info)
		
		if case_num == 2:
			shift_start_date = date(2016,4,12)
			shift_end_date = date(2016,4,12)
			shift_start_time = time(11,00)
			shift_end_time = time(15,00)

			shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
			shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)

			shift_info = [shift_start_datetime, shift_end_datetime]
			run_times_list = [
					{'start_time': time(11,00), 'end_time': time(12,00)}
			]
			
			shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
			dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
			run = Run.objects.create(shift = dummy_shift, start_datetime = shift_start_datetime, end_datetime = shift_end_datetime)
			return (shift, run)
		
		if case_num == 3:
			shift_start_date = date(2016,4,12)
			shift_end_date = date(2016,4,12)
			shift_start_time = time(11,00)
			shift_end_time = time(15,00)

			shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
			shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)

			shift_info = [shift_start_datetime, shift_end_datetime]
			run_times_list = [
				{'start_time':time(11,00), 'end_time': time(12,00)}, 
				{'start_time':time(12,00),'end_time':time(13,00)},
				{'start_time':time(13,00), 'end_time':time(14,00)},
				{'start_time':time(14,00), 'end_time':time(15,00)}
			]
			
			shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
			dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
			run = Run.objects.create(shift = dummy_shift, start_datetime = shift_start_datetime, end_datetime = shift_end_datetime)
			return (shift,runs, total_dur)

		# if case_num == 4:

		# if case_num == 5:

		# if case_num == 6:

	def test_shift_creation_start_datetime(self):
		case_num = 1
		(shift, shift_info) = self.set_up(case_num)
		self.assertEqual(shift.start_datetime, shift_info[0])

	def test_shift_creation_end_datetime(self):
		case_num = 1
		(shift, shift_info) = self.set_up(case_num)
		self.assertEqual(shift.end_datetime, shift_info[1])
	
	def test_reverse_to_run(self):
		case_num = 2
		(shift, run) = self.set_up(case_num)
		shift_run = shift.runs_related.first()
		self.assertEqual(shift_run.start_datetime, run.start_datetime)

	def test_num_shift_runs(self):
		case_num = 3
		(shift, runs, num_expected_runs) = self.set_up(case_num)
		num_shift_runs = shift.runs_related.count()
		self.assertEqual(num_shift_runs, num_expected_runs)

	def test_shift_first_run(self):
		case_num = 3
		(shift, runs, num_expected_runs) = self.set_up(case_num)
		num_shift_runs = shift.runs_related.count()
		shift_first_run = shift.runs_related.first()
		expected_first_run = runs[0]
		self.assertEqual(shift_first_run.start_datetime, expected_first_run.start_datetime)

	def test_shift_last_run(self):
		case_num = 3
		(shift, runs, num_expected_runs) = self.set_up(case_num)
		num_shift_runs = shift.runs_related.count()
		shift_last_run = shift.runs_related.last()
		expected_final_run = runs[len(runs) - 1]
		self.assertEqual(shift_last_run.start_datetime, expected_final_run.start_datetime)
	
	# def test_single_day_one_run(self):

	# def test_single_day_two_runs(self):
	# 	case_num = 4

	# def test_single_day_three_runs(self):

	# def test_two_day_one_run(self):

	# def test_two_day_two_non_midnight(self):

	# def test_two_day_three_middle_midnight(self):

	# def test_three_day_three_non_midnight(self):

	# def test_three_day_two_run_midnight(self):

	# def test_three_day_three_run_first_last_midnight(self):