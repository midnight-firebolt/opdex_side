from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from docui.models import MedicineSchedule , Appointment
from django.http import HttpResponse 

def view (request) :
    medicine_schedules = MedicineSchedule.objects.all()
    if request.method == 'POST':
        # Process form data here
        form_data = request.POST  # Access form data
        # Do something with form_data
        print(form_data)
        pat_id = form_data.get('patient_id')
        print (pat_id)
        medicine_schedules = MedicineSchedule.objects.all()
        print(medicine_schedules.values_list('id', flat=True))
        context = {
            'pat_id' : pat_id, 
            'medicine_schedules' : medicine_schedules
        }
        return render(request, 'medsSchedule.html', context)
    else:
        return render(request, 'askForID.html')