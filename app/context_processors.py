from .models import Doctor, Complaint, Chat
from django.db.models import Q

def admin_sidebar_stats(request):
    """
    Context processor to provide dynamic counts for the admin sidebar.
    """
    if request.user.is_authenticated:
        # We assume if the user is visiting admin URLs or is a superuser they might need these stats
        # but to be safe and efficient, we only calculate them if the template actually needs them
        # or if it's a small overhead.
        
        pending_doctors_count = Doctor.objects.exclude(status__iexact='approved').exclude(status__iexact='rejected').count()
        approved_doctors_count = Doctor.objects.filter(status__iexact='approved').count()
        rejected_doctors_count = Doctor.objects.filter(status__iexact='rejected').count()
        open_complaints_count = Complaint.objects.filter(Q(Reply__isnull=True) | Q(Reply='')).count()
        
        return {
            'pending_doctors_count': pending_doctors_count,
            'approved_doctors_count': approved_doctors_count,
            'rejected_doctors_count': rejected_doctors_count,
            'open_complaints_count': open_complaints_count,
        }
    return {}

def chat_notifications(request):
    if not request.user.is_authenticated:
        return {}
    
    unread_count = Chat.objects.filter(RECIEVER_ID=request.user, is_read=False).count()
    return {'unread_count': unread_count}
