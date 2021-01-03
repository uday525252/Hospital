from django.shortcuts import render
from testapp.models import Doctor,Patient,Appointment

from django.core.paginator import Paginator
from testapp.forms import DoctorForm,PatientForm
from django.views.generic import CreateView

# Create your views here.
def home_view(request):
    return render(request,"home.html")

def doctor_read_view(request):
    doc_list=Doctor.objects.all()
    paginator=Paginator(doc_list,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    name=request.GET.get('name')
    if name!='' and name is not None:
        page_obj=doc_list.filter(doctor_name__contains=name)


    my_dict={'page_obj':page_obj}
    return render(request,"docread.html",my_dict)





class doctor_form_view(CreateView):
    model=Doctor
    #fields="__all__"
    template_name="docform.html"
    form_class=DoctorForm



def patient_read_view(request):
    pat_list=Patient.objects.all()
    my_dict={'pat_list':pat_list}
    return render(request,"patread.html",my_dict)



class patient_form_view(CreateView):
    model=Patient
    template_name="patform.html"
    form_class=PatientForm



def appointment_read_view(request):
    if request.method=='POST':
        order_amount = 500
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {'Shipping address': 'Bommanahalli, Bangalore'}
        client=razorpay.Client(auth=('rzp_test_o31MiTDgxL3CmL','lTaH0rrWG7cMmVKjF2GnTrDZ'))
        payment=client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
#internally razorpay will create an order_id
    app_list=Appointment.objects.all()
    my_dict={'app_list':app_list}
    return render(request,"app.html",my_dict)
