import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.db.models import Avg, Count, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from .models import Doctor
from django.contrib.auth.decorators import login_required
from app.models import*

@never_cache
def logout_view(request):
    logout(request)
    return redirect('login_view')
def navigation_header(request):
    return render(request,'navigation_header.html')
@login_required(login_url='login_view')
def user_view_rating(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    ratings = Rating.objects.filter(DOCTOR_ID=doctor).select_related('PATIENT_ID')

    if ratings.exists():
        avg_rating = round(sum(r.stars for r in ratings) / ratings.count(), 1)
        total_reviews = ratings.count()
    else:
        avg_rating = 0
        total_reviews = 0

    # Calculate star distribution
    star_counts = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
    for r in ratings:
        if r.stars in star_counts:
            star_counts[r.stars] += 1
            
    star_distribution = []
    for stars in range(5, 0, -1):
        count = star_counts[stars]
        percentage = (count / total_reviews * 100) if total_reviews > 0 else 0
        star_distribution.append({
            'stars': stars,
            'count': count,
            'percentage': percentage
        })

    return render(request, 'user_view_rating.html', {
        'doctor': doctor,
        'ratings': ratings,
        'avg_rating': avg_rating,
        'total_reviews': total_reviews,
        'star_distribution': star_distribution,
    })

def home(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='admin').exists():
            return redirect('admin_index')
        elif request.user.groups.filter(name='doctor').exists():
            return redirect('doctor_index')
        elif request.user.groups.filter(name='user').exists():
            return redirect('user_home')
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        regno = request.POST['reg_no']
        smc = request.POST['smc']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.save()

        group = Group.objects.get(name='doctor')
        user.groups.add(group)

        Doctor.objects.create(USER_ID=user, name=name, address=address, email=email, phone=phone, regno=regno,
                                status='pending', smc=smc)

        messages.success(request, 'Registration successfull')
        return redirect('login_view')

    return render(request,'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['user_id']=user.id

            if user.groups.filter(name='admin').exists():
                return redirect('admin_index')
            elif user.groups.filter(name='doctor').exists():
                doctor=Doctor.objects.get(USER_ID=user)
                request.session['doctor_id']=doctor.id

                if doctor.status=='approved':
                    return redirect('doctor_index')
                elif doctor.status=='rejected':
                    messages.success(request,'Your approval got rejected')
                    return redirect('login_view')
                else:
                    messages.success(request,'approval still pending')
                    return redirect('login_view')


            elif user.groups.filter(name='user').exists():
                user=User_profile.objects.get(USER_ID=user)
                request.session['user']=user.id
                return redirect('user_home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


@login_required(login_url='login_view')
def admin_home(request):
    return redirect('admin_index')

@login_required(login_url='login_view')
def admin_header(request):
    pending_doctors_count = Doctor.objects.exclude(status__iexact='approved').exclude(status__iexact='rejected').count()
    approved_doctors_count = Doctor.objects.filter(status__iexact='approved').count()
    open_complaints_count = Complaint.objects.filter(Q(Reply__isnull=True) | Q(Reply='')).count()

    return render(request,'admin_header.html', {
        'pending_doctors_count': pending_doctors_count,
        'approved_doctors_count': approved_doctors_count,
        'open_complaints_count': open_complaints_count,
    })

@login_required(login_url='login_view')
def verify_doctor(request):
    doctor=Doctor.objects.all().order_by('-id')
    return render(request,'verify_doctor.html',{'doctor':doctor})
@login_required(login_url='login_view')
def admin_approve_doctor(request,id):
    doctor=Doctor.objects.get(id=id)
    doctor.status="approved"
    doctor.save()
    messages.error(request,'approved successfully')
    return redirect('verify_doctor')

@login_required(login_url='login_view')
def admin_reject_doctor(request,id):
    doctor=Doctor.objects.get(id=id)
    doctor.status="rejected"
    doctor.save()
    messages.error(request,'rejected successfully')
    return redirect('verify_doctor')

from django.db.models import Count, Q, F, ExpressionWrapper, fields
from datetime import datetime, timedelta
from django.utils import timezone

@login_required(login_url='login_view')
def admin_index(request):
    # Get current date and calculate date ranges
    today = timezone.now().date()
    last_week = today - timedelta(days=7)
    start_of_month = today.replace(day=1)
    previous_month_start = (start_of_month - timedelta(days=1)).replace(day=1)
    previous_week_start = last_week - timedelta(days=7)

    def _time_ago(dt):
        if not dt:
            return ""

        now = timezone.now()
        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt, timezone.get_current_timezone())
        delta = now - dt

        seconds = int(delta.total_seconds())
        if seconds < 60:
            return "just now"

        minutes = seconds // 60
        if minutes < 60:
            return f"{minutes}m ago"

        hours = minutes // 60
        if hours < 24:
            return f"{hours}h ago"

        days = hours // 24
        return f"{days}d ago"
    
    # 1. Total Patients
    total_patients = User_profile.objects.count()
    new_patients_this_month = User_profile.objects.filter(
        USER_ID__date_joined__date__gte=start_of_month
    ).count()
    
    # Calculate patient growth percentage
    current_month_patients = User_profile.objects.filter(
        USER_ID__date_joined__date__gte=start_of_month
    ).count()
    
    previous_month_patients = User_profile.objects.filter(
        USER_ID__date_joined__date__gte=previous_month_start,
        USER_ID__date_joined__date__lt=start_of_month
    ).count()
    
    patient_growth = 0
    if previous_month_patients > 0:
        patient_growth = round(((current_month_patients - previous_month_patients) / previous_month_patients) * 100)
    elif current_month_patients > 0:
        patient_growth = 100  # Initial growth
    
    # 2. Active Doctors
    active_doctors = Doctor.objects.filter(status='approved').count()

    current_month_doctors = Doctor.objects.filter(
        status='approved',
        USER_ID__date_joined__date__gte=start_of_month,
    ).count()

    previous_month_doctors = Doctor.objects.filter(
        status='approved',
        USER_ID__date_joined__date__gte=previous_month_start,
        USER_ID__date_joined__date__lt=start_of_month,
    ).count()

    doctor_growth = 0
    if previous_month_doctors > 0:
        doctor_growth = round(((current_month_doctors - previous_month_doctors) / previous_month_doctors) * 100)
    
    # 3. Appointments
    total_appointments = Booking.objects.count()
    today_appointments = Booking.objects.filter(date__startswith=today.isoformat()).count()

    current_month_appointments = Booking.objects.filter(
        date__startswith=start_of_month.isoformat()[:7]
    ).count()
    previous_month_appointments = Booking.objects.filter(
        date__startswith=previous_month_start.isoformat()[:7]
    ).count()

    appointment_growth = 0
    if previous_month_appointments > 0:
        appointment_growth = round(
            ((current_month_appointments - previous_month_appointments) / previous_month_appointments) * 100
        )
    
    # 4. Skin Scans
    total_skin_scans = 0
    weekly_skin_scans = 0
    scan_growth = 0
    try:
        from app.models import SkinPredictionHistory
        total_skin_scans = SkinPredictionHistory.objects.count()
        weekly_skin_scans = SkinPredictionHistory.objects.filter(created_at__date__gte=last_week).count()

        previous_week_scans = SkinPredictionHistory.objects.filter(
            created_at__date__gte=previous_week_start,
            created_at__date__lt=last_week,
        ).count()

        if previous_week_scans > 0:
            scan_growth = round(((weekly_skin_scans - previous_week_scans) / previous_week_scans) * 100)
    except:
        pass

    pending_doctors = list(
        Doctor.objects.exclude(status__iexact='approved').exclude(status__iexact='rejected').order_by('-id')[:3]
    )
    for d in pending_doctors:
        d.initials = (d.name or '').strip()[:2].upper() if getattr(d, 'name', None) else 'DR'

    recent_complaints = list(Complaint.objects.select_related('USER_ID').order_by('-id')[:3])
    for c in recent_complaints:
        user_name = getattr(c.USER_ID, 'username', '') or ''
        c.initials = user_name.strip()[:2].upper() if user_name else 'US'
        c.is_resolved = bool((c.Reply or '').strip())

    pending_doctors_count = Doctor.objects.exclude(status__iexact='approved').exclude(status__iexact='rejected').count()
    approved_doctors_count = Doctor.objects.filter(status__iexact='approved').count()
    open_complaints_count = Complaint.objects.filter(Q(Reply__isnull=True) | Q(Reply='')).count()

    recent_activity = []

    latest_approved_doctor = Doctor.objects.filter(status__iexact='approved').select_related('USER_ID').order_by('-USER_ID__date_joined').first()
    if latest_approved_doctor and getattr(latest_approved_doctor, 'USER_ID', None) and getattr(latest_approved_doctor.USER_ID, 'date_joined', None):
        recent_activity.append({
            'tone': 'success',
            'icon': 'fa-user-check',
            'title': 'Doctor Approved',
            'description': f"{latest_approved_doctor.name} has been verified",
            'time': _time_ago(latest_approved_doctor.USER_ID.date_joined),
            'ts': latest_approved_doctor.USER_ID.date_joined,
        })

    latest_booking = Booking.objects.select_related('PATIENT_ID').order_by('-id').first()
    if latest_booking:
        recent_activity.append({
            'tone': 'info',
            'icon': 'fa-calendar-plus',
            'title': 'New Appointment',
            'description': 'A patient booked a consultation',
            'time': 'recent',
            'ts': timezone.now() - timedelta(minutes=5),
        })

    latest_complaint = Complaint.objects.select_related('USER_ID').order_by('-id').first()
    if latest_complaint:
        recent_activity.append({
            'tone': 'warning',
            'icon': 'fa-exclamation-triangle',
            'title': 'New Complaint',
            'description': (latest_complaint.Complaint_text or '').strip()[:60] or 'User reported an issue',
            'time': 'recent',
            'ts': timezone.now() - timedelta(minutes=10),
        })

    latest_scan_ts = None
    try:
        latest_prediction = SkinPredictionHistory.objects.order_by('-created_at').first()
        if latest_prediction and getattr(latest_prediction, 'created_at', None):
            latest_scan_ts = latest_prediction.created_at
            recent_activity.append({
                'tone': 'success',
                'icon': 'fa-microscope',
                'title': 'Scan Completed',
                'description': f"AI diagnosis generated: {latest_prediction.label}",
                'time': _time_ago(latest_prediction.created_at),
                'ts': latest_prediction.created_at,
            })
    except Exception:
        pass



    recent_activity = sorted(recent_activity, key=lambda x: x.get('ts') or timezone.now(), reverse=True)[:4]
    for item in recent_activity:
        if item.get('time') == 'recent':
            item['time'] = _time_ago(item.get('ts'))
    
    # Prepare context
    context = {
        'total_patients': total_patients,
        'active_doctors': active_doctors,
        'total_appointments': total_appointments,
        'today_appointments': today_appointments,
        'total_skin_scans': total_skin_scans,
        'weekly_skin_scans': weekly_skin_scans,
        'new_patients_this_month': new_patients_this_month,
        'patient_growth': patient_growth,
        'doctor_growth': doctor_growth,
        'appointment_growth': appointment_growth,
        'scan_growth': scan_growth,
        'new_doctors_this_month': current_month_doctors,
        'pending_doctors': pending_doctors,
        'recent_complaints': recent_complaints,
        'pending_doctors_count': pending_doctors_count,
        'approved_doctors_count': approved_doctors_count,
        'open_complaints_count': open_complaints_count,
        'notification_count': (pending_doctors_count + open_complaints_count),
        'recent_activity': recent_activity,
    }
    
    return render(request, 'admin_index.html', context)

def approved_doctors(request):
    doctor = Doctor.objects.filter(status='approved').order_by('-id')
    
    for d in doctor:
        ratings = Rating.objects.filter(DOCTOR_ID=d)
        if ratings.exists():
            d.avg_rating = round(sum(r.stars for r in ratings) / ratings.count(), 1)
            d.total_reviews = ratings.count()
        else:
            d.avg_rating = 0
            d.total_reviews = 0
            
    top_rated_count = 0
    for d in doctor:
        if d.avg_rating >= 4.5:
            top_rated_count += 1
            
    from django.utils import timezone
    current_month = timezone.now().month
    active_month_count = Doctor.objects.filter(status='approved', USER_ID__date_joined__month=current_month).count()

    context = {
        "doctor": doctor,
        "top_rated_count": top_rated_count,
        "active_month_count": active_month_count
    }
    return render(request,'approved_doctors.html', context)

@login_required(login_url='login_view')
def feedbacks(request):
    feedback = Feedback.objects.all().order_by('-Date')
    total_feedback_count = feedback.count()
    doctor_feedback_count = feedback.filter(DOCTOR_ID__isnull=False).count()
    patient_feedback_count = feedback.filter(PATIENT_ID__isnull=False).count()
    
    context = {
        'feedbacks': feedback,
        'total_feedback_count': total_feedback_count,
        'doctor_feedback_count': doctor_feedback_count,
        'patient_feedback_count': patient_feedback_count,
    }
    return render(request, 'feedbacks.html', context)

@login_required(login_url='login_view')
def users(request):
    user = User_profile.objects.all().order_by('-id')
    male_count = user.filter(gender='Male').count()
    female_count = user.filter(gender='Female').count()
    
    context = {
        'user': user,
        'male_count': male_count,
        'female_count': female_count,
    }
    return render(request, 'users.html', context)

@login_required(login_url='login_view')
def complaint(request):
    complaints = list(Complaint.objects.all().order_by('-Date'))
    pending_count = Complaint.objects.filter(Reply='pending').count()
    resolved_count = Complaint.objects.exclude(Reply='pending').count()
    
    for c in complaints:
        if hasattr(c.USER_ID, 'doctor'):
            c.complainant_name = c.USER_ID.doctor.name
            c.complainant_type = 'Doctor'
        elif hasattr(c.USER_ID, 'user_profile'):
            c.complainant_name = c.USER_ID.user_profile.name
            c.complainant_type = 'Patient'
        else:
            c.complainant_name = c.USER_ID.username
            c.complainant_type = 'User'

    context = {
        'complaints': complaints,
        'pending_count': pending_count,
        'resolved_count': resolved_count,
    }
    return render(request, 'complaint.html', context)

@login_required(login_url='login_view')
def admin_send_reply(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    if request.method == 'POST':
        complaint.Reply = request.POST['replyText']
        complaint.save()
        messages.success(request, 'Reply sent successfully')
        return redirect('complaint')

    return render(request, 'admin_sent_reply.html', {'complaint': complaint})


@login_required(login_url='login_view')
def doctor_index(request):
    today = timezone.now().date()

    doctor_id = request.session.get('doctor_id')
    if doctor_id:
        doctor = get_object_or_404(Doctor, id=doctor_id)
    else:
        doctor = get_object_or_404(Doctor, USER_ID=request.user)

    def _time_ago_from_date_str(date_str):
        if not date_str:
            return ""
        try:
            dt = timezone.datetime.fromisoformat(date_str)
            if timezone.is_naive(dt):
                dt = timezone.make_aware(dt, timezone.get_current_timezone())
        except Exception:
            return date_str

        delta_days = (timezone.now().date() - dt.date()).days
        if delta_days == 0:
            return "Today"
        if delta_days == 1:
            return "Yesterday"
        return f"{delta_days} days ago"

    def _format_time_parts(t):
        if not t:
            return "--:--", ""
        try:
            hhmm = str(t).strip()
            hour = int(hhmm.split(':')[0])
            minute = hhmm.split(':')[1] if ':' in hhmm else "00"
            period = "AM" if hour < 12 else "PM"
            hour12 = hour % 12
            if hour12 == 0:
                hour12 = 12
            return f"{hour12:02d}:{minute}", period
        except Exception:
            return str(t), ""

    today_bookings = Booking.objects.filter(
        shedule_id__DOCTOR_ID=doctor,
        date__startswith=today.isoformat(),
    ).select_related('PATIENT_ID', 'shedule_id').order_by('shedule_id__start_time')

    today_appointments = today_bookings.count()

    consultations = Booking.objects.filter(shedule_id__DOCTOR_ID=doctor).count()
    total_patients = Booking.objects.filter(shedule_id__DOCTOR_ID=doctor).values('PATIENT_ID').distinct().count()

    rating_qs = Rating.objects.filter(DOCTOR_ID=doctor)
    rating_agg = rating_qs.aggregate(avg=Avg('stars'), total=Count('id'))
    avg_rating = round((rating_agg.get('avg') or 0), 1)
    rating_count = rating_agg.get('total') or 0

    today_schedule = []
    for b in today_bookings[:6]:
        hour, period = _format_time_parts(getattr(b.shedule_id, 'start_time', None))
        patient_name = getattr(b.PATIENT_ID, 'name', None) or getattr(b.PATIENT_ID, 'email', None) or 'Patient'
        today_schedule.append({
            'time_hour': hour,
            'time_period': period,
            'patient_name': patient_name,
            'kind': 'Consultation',
            'icon': 'fa-stethoscope',
        })

    recent_patients = []
    recent_bookings = Booking.objects.filter(shedule_id__DOCTOR_ID=doctor).select_related('PATIENT_ID').order_by('-id')[:12]
    seen_patient_ids = set()
    for b in recent_bookings:
        pid = getattr(b.PATIENT_ID, 'id', None)
        if not pid or pid in seen_patient_ids:
            continue
        seen_patient_ids.add(pid)

        patient_name = getattr(b.PATIENT_ID, 'name', None) or getattr(b.PATIENT_ID, 'email', None) or 'Patient'
        initials = (patient_name.strip()[:2].upper() if patient_name else 'PT')

        is_new = Booking.objects.filter(shedule_id__DOCTOR_ID=doctor, PATIENT_ID=b.PATIENT_ID).count() == 1
        recent_patients.append({
            'initials': initials,
            'name': patient_name,
            'when': _time_ago_from_date_str(getattr(b, 'date', None)),
            'status': 'New Patient' if is_new else 'Follow-up',
            'status_class': 'new' if is_new else 'followup',
        })
        if len(recent_patients) >= 4:
            break

    return render(request,'doctor_index.html', {
        'Doctor': doctor,
        'today_appointments': today_appointments,
        'total_patients': total_patients,
        'consultations': consultations,
        'rating': avg_rating,
        'rating_count': rating_count,
        'today_schedule': today_schedule,
        'recent_patients': recent_patients,
    })
@login_required(login_url='login_view')
@never_cache
def doctor_profile(request):
    doctor = Doctor.objects.get(id=request.session['doctor_id'])
    
    # Calculate dynamic stats
    consultations = Booking.objects.filter(shedule_id__DOCTOR_ID=doctor).count()
    total_patients = Booking.objects.filter(shedule_id__DOCTOR_ID=doctor).values('PATIENT_ID').distinct().count()
    
    rating_qs = Rating.objects.filter(DOCTOR_ID=doctor)
    rating_agg = rating_qs.aggregate(avg=Avg('stars'))
    avg_rating = round((rating_agg.get('avg') or 0), 1)
    
    context = {
        'doctor': doctor,
        'total_patients': total_patients,
        'consultations': consultations,
        'rating': avg_rating,
        'experience': 8, # This could also be dynamic if there's a field for joining date
    }
    return render(request, 'doctor_profile.html', context)

@login_required(login_url='login_view')
def doctor_profile_edit(request):
    doctor_id = request.session.get('doctor_id')
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.phone = request.POST.get('phone')
        doctor.email = request.POST.get('email')
        doctor.address = request.POST.get('address')
        # Registration number and SMC are not editable once verified
        doctor.save()
        messages.success(request, "Your profile has been updated successfully!")
        return redirect('doctor_profile')

    return render(request, 'doctor_profile_edit.html', {'doctor': doctor})

@login_required(login_url='login_view')
def manage_schedule(request):
    schedule=Doctor_schedule.objects.filter(DOCTOR_ID=request.session['doctor_id']).order_by('-id')
    doctor=Doctor.objects.get(id=request.session['doctor_id'])
    if request.method == 'POST':
        date_str = request.POST['date']
        start_time_str = request.POST['start_time']
        end_time_str = request.POST['end_time']
        fees=request.POST['fees']
        max_patients = request.POST.get('max_patients', 20)

        # Parse inputs
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_time_obj = datetime.strptime(start_time_str, '%H:%M').time()
            end_time_obj = datetime.strptime(end_time_str, '%H:%M').time()
        except ValueError:
            messages.error(request, "Invalid date or time format.")
            return redirect('manage_schedule')

        # Validation Logic
        now = datetime.now()
        today = now.date()
        current_time = now.time()

        if date_obj < today:
            messages.error(request, "Cannot add schedule for a past date!")
        elif date_obj == today and start_time_obj < current_time:
            messages.error(request, "Cannot add schedule for a past time!")
        elif end_time_obj <= start_time_obj:
            messages.error(request, "End time must be after start time!")
        else:
            # Check for Overlap
            overlap = Doctor_schedule.objects.filter(
                DOCTOR_ID=doctor,
                date=date_str,
                start_time=start_time_str,
                end_time=end_time_str
            ).exists()

            if overlap:
                messages.error(request, "Schedule overlaps with an existing slot!")
            else:
                Doctor_schedule.objects.create(
                    start_time=start_time_str,
                    end_time=end_time_str,
                    fees=fees,
                    date=date_str,
                    DOCTOR_ID=doctor,
                    max_patients=max_patients
                )
                messages.success(request, "Schedule added successfully!")

    # Convert string fields to datetime objects for template rendering
    for s in schedule:
        try:
            if isinstance(s.date, str):
                s.date = datetime.strptime(s.date, '%Y-%m-%d').date()
            if isinstance(s.start_time, str):
                # Handle potentially different time formats if legacy data exists
                try:
                    s.start_time = datetime.strptime(s.start_time, '%H:%M').time()
                except ValueError:
                    s.start_time = datetime.strptime(s.start_time, '%H:%M:%S').time()
            if isinstance(s.end_time, str):
                try:
                    s.end_time = datetime.strptime(s.end_time, '%H:%M').time()
                except ValueError:
                    s.end_time = datetime.strptime(s.end_time, '%H:%M:%S').time()
        except (ValueError, TypeError):
            # If parsing fails, keep original strings (or handle gracefully)
            pass

    return render(request,'manage_schedule.html',{'schedule':schedule})


@login_required(login_url='login_view')
def view_appoinment(request):
    doctor=Doctor.objects.get(USER_ID=request.user)
    bookings=Booking.objects.filter(shedule_id__DOCTOR_ID=doctor).order_by('-id')
    
    pending_count = bookings.filter(status='pending').count()
    approved_count = bookings.filter(status='approved').count()
    paid_count = bookings.filter(status='paid').count()
    
    context = {
        'doctor': doctor,
        'bookings': bookings,
        'pending_count': pending_count,
        'approved_count': approved_count,
        'paid_count': paid_count
    }

    return render(request,'view_appoinment.html', context)



@login_required(login_url='login_view')
def doctor_approved_booking(request,id):
    booking=Booking.objects.get(id=id)
    booking.status="approved"
    booking.save()
    return redirect('view_appoinment')


@login_required(login_url='login_view')
def doctor_rejected_booking(request,id):
    booking=Booking.objects.get(id=id)
    booking.status="rejected"
    booking.save()
    return redirect('view_appoinment')

@login_required(login_url='login_view')
def chat(request):
    return render(request,'chat.html')
from django.utils import timezone

@login_required(login_url='login_view')
def doctor_complaint(request):
    if request.method == 'POST':
        complaint_text = request.POST.get('complaint_text')

        if complaint_text:
            date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

            Complaint.objects.create(
                USER_ID=request.user,
                Complaint_text=complaint_text,
                Reply='pending',
                Date=date
            )

    complaints = Complaint.objects.filter(USER_ID=request.user)

    return render(request, 'doctor_complaint.html', {
        'complaints': complaints
    })

@login_required(login_url='login_view')
def user_home(request):
    try:
        from django.utils import timezone
        today = timezone.now().date().isoformat()
        
        # Global stats
        patient_count = User_profile.objects.count()
        doctor_count = Doctor.objects.filter(status='approved').count()
        
        context = {
            'patient_count': patient_count,
            'doctor_count': doctor_count,
        }
        
        # User specific data
        if request.user.is_authenticated:
            try:
                # Personal info
                user_profile = User_profile.objects.get(USER_ID=request.user)
                context['user_name'] = user_profile.name.split()[0] if user_profile.name else request.user.username
                
                # Upcoming appointments (approved and future date)
                upcoming_appointments = Booking.objects.filter(
                    PATIENT_ID__USER_ID=request.user,
                    status='approved',
                    date__gte=today
                ).select_related('shedule_id__DOCTOR_ID').order_by('date')[:2]
                context['upcoming_appointments'] = upcoming_appointments
                
                # Recent scans
                recent_scans = SkinPredictionHistory.objects.filter(
                    USER_ID=request.user
                ).order_by('-created_at')[:3]
                context['recent_scans'] = recent_scans
                
            except User_profile.DoesNotExist:
                context['user_name'] = request.user.username
                
        return render(request, 'user_home.html', context)
    except Exception as e:
        print(f"Error in user_home: {e}")
        return render(request, 'user_home.html')
def view_doctors(request):
    doctor = Doctor.objects.filter(status='approved').order_by('-id').annotate(
        avg_rating=Avg('rating__stars'),
        review_count=Count('rating'),
    )

    ratings_summary = Rating.objects.filter(DOCTOR_ID__status='approved').aggregate(
        avg_rating=Avg('stars'),
        total_reviews=Count('id'),
    )

    return render(request,'view_doctors.html',{
        'doctor': doctor,
        'overall_avg_rating': ratings_summary.get('avg_rating') or 0,
        'total_reviews': ratings_summary.get('total_reviews') or 0,
    })
def user_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        age = request.POST['age']
        gender = request.POST['gender']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST.get('confirm_password')

        # Validation logic
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('user_register')

        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long')
            return redirect('user_register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('user_register')

        if User_profile.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('user_register')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        try:
            group = Group.objects.get(name='user')
        except Group.DoesNotExist:
            group = Group.objects.create(name='user')
            
        user.groups.add(group)

        User_profile.objects.create(
            USER_ID=user, 
            name=name, 
            address=address, 
            email=email, 
            phone=phone, 
            age=age,
            gender=gender
        )

        messages.success(request, 'Registration Successful')
        return redirect('login_view')
    return render(request, 'user_register.html')

@login_required(login_url='login_view')
def user_complaint(request):
    if request.method == 'POST':
        complaint_text = request.POST.get('complaint_text')

        if complaint_text:
            date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

            Complaint.objects.create(
                USER_ID=request.user,
                Complaint_text=complaint_text,
                Reply='pending',
                Date=date
            )

    complaints = Complaint.objects.filter(USER_ID=request.user)

    return render(request,'user_complaint.html',{'complaints':complaints})

@login_required(login_url='login_view')
@never_cache
def user_profile(request):
    user = User_profile.objects.get(id=request.session['user'])
    
    # Calculate dynamic statistics
    bookings_count = Booking.objects.filter(PATIENT_ID=user).count()
    completed_count = Booking.objects.filter(PATIENT_ID=user, status='paid').count()
    pending_count = Booking.objects.filter(PATIENT_ID=user, status__in=['Pending', 'Approved']).count()
    
    return render(request, 'user_profile.html', {
        'user': user,
        'bookings_count': bookings_count,
        'completed_count': completed_count,
        'pending_count': pending_count
    })

@login_required(login_url='login_view')
def user_profile_edit(request):
    user_id = request.session.get('user')
    user_profile = get_object_or_404(User_profile, id=user_id)
    
    if request.method == 'POST':
        # Update UserProfile
        user_profile.name = request.POST.get('name')
        user_profile.phone = request.POST.get('phone')
        user_profile.email = request.POST.get('email')
        user_profile.address = request.POST.get('address')
        user_profile.age = request.POST.get('age')
        user_profile.gender = request.POST.get('gender')
        user_profile.save()
        
        # Sync with User account
        auth_user = user_profile.USER_ID
        auth_user.email = user_profile.email
        auth_user.save()
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('user_profile')
        
    return render(request, 'user_profile_edit.html', {'user': user_profile})



@login_required(login_url='login_view')
def doctor_feedback(request):
    doctor = None

    doctor_id = request.session.get('doctor_id')
    if doctor_id:
        doctor = Doctor.objects.filter(id=doctor_id).first()

    if doctor is None:
        doctor = Doctor.objects.filter(USER_ID=request.user).first()

    if doctor is None:
        messages.error(request, 'Doctor profile not found for this account.')
        return redirect('login_view')

    if request.method == 'POST':
        feedback_text= request.POST.get('feedback_text')

        if feedback_text:
            date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

            Feedback.objects.create(
                DOCTOR_ID=doctor,
                Feedback_text = feedback_text,
                Date=date
            )

    feedbacks = Feedback.objects.filter(DOCTOR_ID=doctor)


    return render(request,'doctor_feedback.html',{'feedbacks':feedbacks, 'Doctor': doctor})
# def user_feedback(request):
#     user = request.session['user']
#     print('hi',user)
#     id = User_profile.objects.get(USER_ID=user)
#     print(id)
#     if request.method == 'POST':
#         feedback_text= request.POST.get('feedback_text')
#         if feedback_text:
#             date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
#
#             Feedback.objects.create(
#                 PATIENT_ID=id,
#                 Feedback_text = feedback_text,
#                 Date=date
#             )
#
#     feedbacks = Feedback.objects.filter(PATIENT_ID=id)
#
#
#     return render(request,'user_feedback.html',{'feedbacks':feedbacks})

@login_required(login_url='login_view')
def user_feedback(request):
    user_profile_id = request.session['user']  # this is User_profile.id

    # Get the correct profile
    user_profile = User_profile.objects.get(id=user_profile_id)

    if request.method == 'POST':
        feedback_text = request.POST.get('feedback_text')

        if feedback_text:
            date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

            Feedback.objects.create(
                PATIENT_ID=user_profile,
                Feedback_text=feedback_text,
                Date=date
            )

    feedbacks = Feedback.objects.filter(PATIENT_ID=user_profile)

    return render(request, 'user_feedback.html', {'feedbacks': feedbacks})

@login_required(login_url='login_view')
def view_schedule(request, id):
    user_id = request.session.get("user_id")
    patient = User_profile.objects.get(USER_ID=user_id)

    doctor_schedule = Doctor_schedule.objects.filter(DOCTOR_ID=id).order_by('-id')
    
    # Calculate status for each schedule
    today = datetime.today().date()
    
    for schedule in doctor_schedule:
        # Check if date is in past
        try:
            schedule_date = datetime.strptime(schedule.date, '%Y-%m-%d').date()
            schedule.is_past = schedule_date < today
        except ValueError:
            schedule.is_past = False
            
        # Check if full
        current_bookings = Booking.objects.filter(shedule_id=schedule).count()
        schedule.is_full = current_bookings >= schedule.max_patients

    user_bookings = Booking.objects.filter(PATIENT_ID=patient)
    booked_ids = user_bookings.values_list('shedule_id_id', flat=True)

    return render(request, "view_schedule.html", {
        "doctor_schedule": doctor_schedule,
        "booked_ids": booked_ids
    })


@login_required(login_url='login_view')
def user_chat(request):
    return render(request,"user_chat.html")



from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime

@login_required(login_url='login_view')
def book_appointment(request, id):
    user_id = request.session.get('user_id')
    patient = User_profile.objects.get(USER_ID=user_id)
    schedule = get_object_or_404(Doctor_schedule, id=id)

    if request.method == "POST":
        # Check if date is in past
        try:
            today = datetime.today().date()
            schedule_date = datetime.strptime(schedule.date, '%Y-%m-%d').date()
            if schedule_date < today:
                messages.error(request, "Cannot book appointment for a past date.")
                return redirect('view_schedule', id=schedule.DOCTOR_ID.id)
        except ValueError:
            pass

        # Check if already booked
        if Booking.objects.filter(PATIENT_ID=patient, shedule_id=schedule).exists():
            messages.error(request, "You have already booked this slot.")
            return redirect('view_schedule', id=schedule.DOCTOR_ID.id)

        # Token Logic
        current_tokens = Booking.objects.filter(shedule_id=schedule).count()
        if current_tokens >= schedule.max_patients:
            messages.error(request, "This slot is full. Please choose another time.")
            return redirect('view_schedule', id=schedule.DOCTOR_ID.id)
        
        token_number = current_tokens + 1

        Booking.objects.create(
            PATIENT_ID=patient,
            shedule_id=schedule,
            date=datetime.today().strftime('%Y-%m-%d'),
            status="pending",
            token_number=token_number
        )
        
        messages.success(request, f"Appointment Booked! Your Token Number is {token_number}")
        return redirect('view_schedule', id=schedule.DOCTOR_ID.id)

    doctor_schedule = Doctor_schedule.objects.filter(DOCTOR_ID=schedule.DOCTOR_ID)
    
    # Re-calculate status for render (same logic as view_schedule)
    today = datetime.today().date()
    for sch in doctor_schedule:
        try:
            sch_date = datetime.strptime(sch.date, '%Y-%m-%d').date()
            sch.is_past = sch_date < today
        except ValueError:
            sch.is_past = False
        
        current = Booking.objects.filter(shedule_id=sch).count()
        sch.is_full = current >= sch.max_patients

    # Get booked IDs for this user to pass to template
    user_bookings = Booking.objects.filter(PATIENT_ID=patient)
    booked_ids = user_bookings.values_list('shedule_id_id', flat=True)

    return render(request, "view_schedule.html", {
        "doctor_schedule": doctor_schedule,
        "booked_ids": booked_ids
    })


@login_required(login_url='login_view')
def view_bookings(request):
    try:
        # Get user profile
        patient = User_profile.objects.get(USER_ID=request.user)
        
        # Get all bookings for this patient
        bookings = Booking.objects.filter(PATIENT_ID=patient).select_related(
            "shedule_id", 
            "shedule_id__DOCTOR_ID__USER_ID"
        ).order_by('-id')

        # Calculate stats
        pending_count = bookings.filter(status='pending').count()
        approved_count = bookings.filter(status='approved').count()
        paid_count = bookings.filter(status='paid').count()

        # Add extra info like unread messages
        for b in bookings:
            b.unread_count = Chat.objects.filter(
                SENDER_ID=b.shedule_id.DOCTOR_ID.USER_ID,
                RECIEVER_ID=request.user, 
                is_read=False
            ).count()

        return render(request, "view_bookings.html", {
            "bookings": bookings,
            "pending_count": pending_count,
            "approved_count": approved_count,
            "paid_count": paid_count,
        })
    except User_profile.DoesNotExist:
        # Handle case where user profile doesn't exist
        return render(request, "view_bookings.html", {
            "bookings": [],
            "pending_count": 0,
            "approved_count": 0,
            "paid_count": 0,
        })

import razorpay
from django.conf import settings
from razorpay.errors import SignatureVerificationError

from .models import Booking, Payment

razorpay_client = razorpay.Client(auth=(
    settings.RAZORPAY_KEY_ID,
    settings.RAZORPAY_KEY_SECRET
))


@login_required(login_url='login_view')
def pay_now(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    schedule = booking.shedule_id
    amount = float(schedule.fees)
    amount_paise = int(amount * 100)

    order_data = {
        "amount": amount_paise,
        "currency": "INR",
        "payment_capture": 1,
        "receipt": f"booking_{booking.id}"
    }

    razorpay_order = razorpay_client.order.create(order_data)
    razorpay_order_id = razorpay_order["id"]

    context = {
        "booking": booking,
        "razorpay_order_id": razorpay_order_id,
        "razorpay_merchant_key": settings.RAZORPAY_KEY_ID,
        "amount": amount,
        "amount_paise": amount_paise,
        "callback_url": "/payment/callback/"
    }

    return render(request, "payment.html", context)



@login_required(login_url='login_view')
def payment_callback(request):
    if request.method == "POST":
        payment_id = request.POST.get("razorpay_payment_id")
        order_id = request.POST.get("razorpay_order_id")
        signature = request.POST.get("razorpay_signature")
        booking_id = request.POST.get("booking_id")

        booking = get_object_or_404(Booking, id=booking_id)
        schedule = booking.shedule_id
        amount = str(schedule.fees)

        try:

            razorpay_client.utility.verify_payment_signature({
                "razorpay_payment_id": payment_id,
                "razorpay_order_id": order_id,
                "razorpay_signature": signature
            })

            Payment.objects.create(
                PAYMENT_ID=payment_id,
                BOOKING_ID=booking,
                amount=amount,
                payment_date=str(timezone.now().date()),
                status="success"
            )

            booking.status = "paid"
            booking.save()

            messages.success(request, "Payment successful!")
            return redirect("view_bookings")

        except SignatureVerificationError:
            messages.error(request, "Payment verification failed! Invalid signature.")
            return redirect("view_bookings")
        except Exception as e:
            messages.error(request, f"Payment failed: {str(e)}")
            return redirect("view_bookings")





from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
from django.utils import timezone

from django.contrib.auth.models import User
from .models import Chat


@login_required(login_url='login_view')
def chat_page(request, id):
    chat_partner = User.objects.get(id=id)
    logged_user = request.user

    return render(request, "chat.html", {
        "chat_partner": chat_partner,
        "user_obj": logged_user
    })



@csrf_exempt
@login_required(login_url='login_view')
def load_chat(request):
    if request.method == "POST":
        data = json.loads(request.body)

        user1 = int(data.get("user1"))
        user2 = int(data.get("user2"))

        chats = Chat.objects.filter(
            Q(SENDER_ID=user1, RECIEVER_ID=user2) |
            Q(SENDER_ID=user2, RECIEVER_ID=user1)
        ).order_by("id")

        msg_list = []
        for c in chats:
            msg_list.append({
                "id": c.id,
                "from": c.SENDER_ID_id,
                "message": c.message,
                "timestamp": c.timestamp
            })

        return JsonResponse({"status": "ok", "messages": msg_list})

    return JsonResponse({"status": "error"})



@csrf_exempt
@login_required(login_url='login_view')
def send_chat(request):
    data = json.loads(request.body.decode("utf-8"))

    sender = int(data.get("sender"))
    receiver = int(data.get("receiver"))
    msg = data.get("message")

    time_now = timezone.now().strftime("%Y-%m-%d %H:%M")

    chat = Chat.objects.create(
        SENDER_ID_id=sender,
        RECIEVER_ID_id=receiver,
        message=msg,
        timestamp=time_now,
    )

    return JsonResponse({"status": "ok", "msg_id": chat.id})


@login_required(login_url='login_view')
def add_rating(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    patient = request.user.user_profile
    
    # Handle legacy duplicate ratings if they exist
    existing_ratings = Rating.objects.filter(DOCTOR_ID=doctor, PATIENT_ID=patient).order_by('-date')
    existing_rating = existing_ratings.first()

    if request.method == "POST":
        stars = int(request.POST.get("stars"))
        review = request.POST.get("review")
        timestamp = timezone.now().strftime("%Y-%m-%d %H:%M")

        # If duplicates exist, clean them up and use the first one
        if existing_ratings.count() > 1:
            # Delete all except the most recent one
            ids_to_keep = [existing_rating.id]
            Rating.objects.filter(DOCTOR_ID=doctor, PATIENT_ID=patient).exclude(id__in=ids_to_keep).delete()

        # Now perform the update or create
        Rating.objects.update_or_create(
            DOCTOR_ID=doctor,
            PATIENT_ID=patient,
            defaults={
                'stars': stars,
                'review': review,
                'date': timestamp
            }
        )

        return redirect('user_view_rating', doctor_id=doctor.id)

    return render(request, "add_rating.html", {
        "doctor": doctor,
        "existing_rating": existing_rating
    })



@login_required(login_url='login_view')
def view_rating(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    ratings = Rating.objects.filter(DOCTOR_ID=doctor)

    if ratings.exists():
        avg_rating = round(sum(r.stars for r in ratings) / ratings.count(), 1)
        total_reviews = ratings.count()
    else:
        avg_rating = 0
        total_reviews = 0

    # Calculate star distribution
    star_counts = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
    for r in ratings:
        if r.stars in star_counts:
            star_counts[r.stars] += 1
            
    star_distribution = []
    for stars in range(5, 0, -1):
        count = star_counts[stars]
        percentage = (count / total_reviews * 100) if total_reviews > 0 else 0
        star_distribution.append({
            'stars': stars,
            'count': count,
            'percentage': percentage
        })

    five_star_count = star_counts[5]

    return render(request, "view_rating.html", {
        "doctor": doctor,
        "ratings": ratings,
        "avg_rating": avg_rating,
        "total_reviews": total_reviews,
        "star_distribution": star_distribution,
        "five_star_count": five_star_count,
    })


#///////////////////CHAT////////////////////////////////////////////////////////////////////////////////////

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, Doctor_schedule, Booking

@login_required(login_url='login_view')
def doctor_paid_patients(request):
    doctor_id = request.session.get('doctor_id')

    if not doctor_id:
        return redirect('login_view')

    doctor = Doctor.objects.get(id=doctor_id)

    schedules = Doctor_schedule.objects.filter(DOCTOR_ID=doctor)

    bookings = Booking.objects.filter(
        shedule_id__in=schedules,
        status__iexact='paid'
    ).select_related('PATIENT_ID__USER_ID')

    active_chats_count = 0
    for b in bookings:
        b.unread_count = Chat.objects.filter(
            SENDER_ID=b.PATIENT_ID.USER_ID, 
            RECIEVER_ID=doctor.USER_ID, 
            is_read=False
        ).count()
        if b.unread_count > 0:
            active_chats_count += 1

    total_patients = bookings.count()
    total_revenue = bookings.aggregate(Sum('shedule_id__fees'))['shedule_id__fees__sum'] or 0

    context = {
        'bookings': bookings,
        'total_patients': total_patients,
        'active_chats': active_chats_count,
        'total_revenue': total_revenue
    }

    return render(request, 'doctor_paid_patients.html', context)

@login_required(login_url='login_view')
def new_doctor_chat(request, patient_user_id):
    sender = request.user
    receiver = User.objects.get(id=patient_user_id)

    if request.method == "POST":
        message = request.POST.get("message")
        image = request.FILES.get("image")

        Chat.objects.create(
            SENDER_ID=sender,
            RECIEVER_ID=receiver,
            message=message,
            image=image,
            timestamp=timezone.now().strftime("%Y-%m-%d %H:%M")
        )
        return redirect('new_doctor_chat', patient_user_id=patient_user_id)

    # Mark incoming messages as read
    Chat.objects.filter(SENDER_ID=receiver, RECIEVER_ID=sender, is_read=False).update(is_read=True)

    chats = Chat.objects.filter(
        SENDER_ID__in=[sender, receiver],
        RECIEVER_ID__in=[sender, receiver]
    ).order_by('id')

    return render(request, 'doctor_chat_popup.html', {
        'chats': chats,
        'receiver': receiver
    })


@login_required(login_url='login_view')
def user_doctor_chat_list(request):
    user = request.user

    paid_bookings = Booking.objects.filter(
        PATIENT_ID__USER_ID=user,
        status__iexact='paid'
    ).select_related('shedule_id__DOCTOR_ID')

    doctors = Doctor.objects.filter(
        id__in=paid_bookings.values_list(
            'shedule_id__DOCTOR_ID__id',
            flat=True
        )
    ).select_related('USER_ID').distinct()

    return render(request, 'user_doctor_chat_list.html', {
        'doctors': doctors
    })


@login_required(login_url='login_view')
def user_doctor_chat(request, doctor_user_id):
    sender = request.user
    receiver = User.objects.get(id=doctor_user_id)

    if request.method == "POST":
        msg = request.POST.get('message')
        image = request.FILES.get("image")

        Chat.objects.create(
            SENDER_ID=sender,
            RECIEVER_ID=receiver,
            message=msg,
            image=image,
            timestamp=timezone.now().strftime("%Y-%m-%d %H:%M")
        )
        return redirect('user_doctor_chat', doctor_user_id)

    # Mark incoming messages as read
    Chat.objects.filter(SENDER_ID=receiver, RECIEVER_ID=sender, is_read=False).update(is_read=True)

    chats = Chat.objects.filter(
        SENDER_ID__in=[sender, receiver],
        RECIEVER_ID__in=[sender, receiver]
    ).order_by('id')

    return render(request, 'user_doctor_chat_popup.html', {
        'chats': chats,
        'receiver': receiver
    })


#////////////////////////////DISEASE PREDICTION////////////////////////////////////////////////////////////////////////
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import default_storage
import os
from . import skintest


def get_disease_info(label):
    disease_db = {
        'BA-cellulitis': {
            'title': 'Cellulitis (Bacterial skin infection)',
            'overview': 'Cellulitis is a bacterial infection of the deeper layers of the skin. It often causes redness, swelling, warmth, and pain in the affected area and can spread quickly.',
            'symptoms': [
                'Redness that may expand',
                'Swelling and warmth',
                'Tenderness or pain',
                'Fever or chills (sometimes)',
            ],
            'remedies': [
                'Keep the affected area clean and dry',
                'Rest and elevate the affected limb if possible',
                'Avoid scratching or rubbing the area',
                'Mark the edge of redness to monitor spreading',
            ],
            'precautions': [
                'Cellulitis often needs prescription antibiotics',
                'Seek urgent care if redness spreads rapidly, you have fever, severe pain, or diabetes/immunosuppression',
            ],
        },
        'BA-impetigo': {
            'title': 'Impetigo (Bacterial skin infection)',
            'overview': 'Impetigo is a contagious bacterial infection common in children. It typically causes honey-colored crusts or blisters, often around the nose and mouth.',
            'symptoms': [
                'Red sores or blisters that can break open',
                'Honey-colored crusts',
                'Itching',
            ],
            'remedies': [
                'Gently wash with mild soap and water',
                'Keep nails short to reduce skin damage from scratching',
                'Do not share towels/razors; wash clothing and bedding',
            ],
            'precautions': [
                'Impetigo usually needs medical treatment (topical or oral antibiotics)',
                'Avoid close contact until treated; it spreads easily',
            ],
        },
        'FU-athlete-foot': {
            'title': "Athlete's Foot (Fungal infection)",
            'overview': "Athlete's foot is a fungal infection that commonly affects the skin between the toes. It can cause itching, scaling, and cracking and may recur if feet stay moist.",
            'symptoms': [
                'Itching or burning between toes',
                'Scaling, peeling, or cracked skin',
                'Redness or blisters',
            ],
            'remedies': [
                'Keep feet clean and dry, especially between toes',
                'Change socks daily (more often if sweaty)',
                'Use breathable shoes; rotate shoes to let them dry',
                'Avoid walking barefoot in public showers/pools',
            ],
            'precautions': [
                'If symptoms persist or worsen, consult a doctor/pharmacist for antifungal treatment advice',
                'Treat early to prevent spread to nails or other body areas',
            ],
        },
        'FU-nail-fungus': {
            'title': 'Nail Fungus (Onychomycosis)',
            'overview': 'Nail fungus is a common infection that can cause thickened, discolored, brittle nails. It often requires weeks to months of treatment and can recur.',
            'symptoms': [
                'Thickened nail',
                'White/yellow/brown discoloration',
                'Brittle, crumbly, or ragged nail edges',
                'Nail lifting from nail bed (sometimes)',
            ],
            'remedies': [
                'Keep nails trimmed and clean',
                'Keep feet dry and change socks daily',
                'Disinfect nail tools and avoid sharing them',
                'Wear breathable footwear and use antifungal powder if needed',
            ],
            'precautions': [
                'Nail fungus often needs prolonged treatment; consult a dermatologist for best options',
                'Seek care sooner if you have diabetes, pain, swelling, or skin breaks around the nail',
            ],
        },
        'Uncertain': {
            'title': 'Uncertain Result / Likely Healthy',
            'overview': 'The AI is not confident enough to provide a specific diagnosis. This usually means the skin appears healthy, or the image quality is not sufficient for a clear analysis.',
            'symptoms': [
                'No significant abnormalities detected',
                'Image may be blurry or poorly lit',
                'Area may not match known disease patterns'
            ],
            'remedies': [
                'Ensure the skin is clean and dry',
                'Retake the photo with better lighting and focus',
                'Monitor the area for any changes in color, size, or sensation'
            ],
            'precautions': [
                'AI results are preliminary and not a substitute for professional medical advice.',
                'If you have persistent symptoms, pain, or concerns, please consult a dermatologist regardless of the AI result.'
            ],
        },
    }
    return disease_db.get(
        label,
        {
            'title': label,
            'overview': 'No additional details are available for this label yet.',
            'symptoms': [],
            'remedies': [],
            'precautions': ['Please consult a dermatologist for an accurate diagnosis: AI results are preliminary.'],
        },
    )


@login_required(login_url='login_view')
def skin_prediction(request):
    context = {}

    history = SkinPredictionHistory.objects.filter(USER_ID=request.user).order_by('-created_at')[:10]
    for item in history:
        item.image_url = settings.MEDIA_URL + item.image_path
    context['history'] = history

    if request.method == "POST":
        try:
            image_file = request.FILES.get("image")

            if not image_file:
                context["error"] = "Please upload an image"
                return render(request, "skin_predict.html", context)

            file_path = default_storage.save(
                "uploads/" + image_file.name, image_file
            )
            abs_path = os.path.join(settings.MEDIA_ROOT, file_path)

            img_tensor = skintest.load_and_preprocess(abs_path)
            raw_label, confidence = skintest.predict(img_tensor)

            # --- Safeguard: Confidence Threshold ---
            THRESHOLD = 0.85  # 85% confidence required (Raised from 70% based on user photo testing)
            if confidence < THRESHOLD:
                label = 'Uncertain'
            else:
                label = raw_label

            context["label"] = label
            context["confidence"] = round(confidence * 100, 2)
            context["image_url"] = settings.MEDIA_URL + file_path
            context["disease_info"] = get_disease_info(label)
            context["is_uncertain"] = (label == 'Uncertain')

            SkinPredictionHistory.objects.create(
                USER_ID=request.user,
                image_path=file_path,
                label=label,
                confidence=round(confidence * 100, 2),
            )

        except Exception as e:
            context["error"] = str(e)

    return render(request, "skin_predict.html", context)

# //////////// CHATBOT ////////////////////////////////////////////////////////
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import google.generativeai as genai

# ---------------- GEMINI CONFIG ----------------
genai.configure(api_key=settings.GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- GEMINI TEXT CHAT ----------------
def generate_gemini_text(message):
    """
    Generate skin-disease related response using Gemini API.
    """
    try:
        prompt = f"""
        You are a SKIN DISEASE CHATBOT.
        Provide general information only.
        Do NOT prescribe medicines.
        Suggest consulting a dermatologist.

        Question: {message}
        """
        response = gemini_model.generate_content(prompt)
        text = response.text if hasattr(response, "text") else "I could not understand."
        return text.replace("*", " ").strip()

    except Exception as e:
        print("Gemini API Error:", e)
        return "I could not process your request."


# ---------------- DJANGO VIEW ----------------
@login_required(login_url='login_view')
@csrf_exempt
def skin_chatbot(request):
    if request.method == "GET":
        history = SkinChatMessage.objects.filter(USER_ID=request.user).order_by('created_at')
        return render(request, "skin_chatbot.html", {'history': history})

    if request.method == "POST":
        try:
            message = request.POST.get("message", "").strip()

            if not message:
                return JsonResponse({"response": "Please enter a description of your skin problem."})

            SkinChatMessage.objects.create(USER_ID=request.user, role='user', message=message)

            reply = generate_gemini_text(message)
            SkinChatMessage.objects.create(USER_ID=request.user, role='bot', message=reply)

            return JsonResponse({"response": reply})

        except Exception as e:
            print("Error:", e)
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Method not allowed"}, status=405)
