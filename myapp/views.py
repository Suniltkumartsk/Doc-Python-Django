from django.shortcuts import render, redirect
from .models import Userdata, Doctorinfo, Registerinfo
from django.contrib import messages
import hashlib


# ── helpers ──────────────────────────────────────────────────────────────────

def hash_password(password):
    """Simple SHA-256 hash. Use django.contrib.auth in production."""
    return hashlib.sha256(password.encode()).hexdigest()


def login_required_custom(view_func):
    """Decorator: redirect to login if user session is missing."""
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user'):
            messages.error(request, "Please login to continue.")
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


# ── public views ─────────────────────────────────────────────────────────────

def index(request):
    return render(request, 'index.html')


def login_page(request):
    if request.session.get('user'):
        return redirect('home')

    if request.method == "POST":
        email_id = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if not email_id or not password:
            messages.error(request, "Email and password are required.")
            return render(request, 'login.html')

        hashed = hash_password(password)
        user = Userdata.objects.filter(email=email_id, password=hashed).first()

        if user:
            request.session['user'] = email_id
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login.html')


def signup_page(request):
    if request.session.get('user'):
        return redirect('home')

    if request.method == "POST":
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if not email or not password:
            messages.error(request, "All fields are required.")
        elif Userdata.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif len(password) < 6:
            messages.error(request, "Password must be at least 6 characters.")
        else:
            Userdata.objects.create(email=email, password=hash_password(password))
            messages.success(request, "Account created! Please login.")
            return redirect('login')

    return render(request, 'signup.html')


def logout_view(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('login')


# ── protected views ───────────────────────────────────────────────────────────

@login_required_custom
def home(request):
    doctors = Doctorinfo.objects.all()
    return render(request, 'home.html', {'doctors': doctors})


@login_required_custom
def register(request):
    doctors = Doctorinfo.objects.all()

    if request.method == "POST":
        doc_name = request.POST.get('doc_name', '').strip()
        p_name = request.POST.get('p_name', '').strip()
        p_age = request.POST.get('p_age', '').strip()
        p_date = request.POST.get('p_date', '').strip()
        gender = request.POST.get('gender', '').strip()
        contact = request.POST.get('contact', '').strip()
        problem = request.POST.get('problem', '').strip()

        # Basic validation
        errors = []
        if not all([doc_name, p_name, p_age, p_date, gender, contact, problem]):
            errors.append("All fields are required.")
        if contact and (not contact.isdigit() or len(contact) < 10 or len(contact) > 15):
            errors.append("Enter a valid contact number (10–15 digits).")
        if p_age and (not p_age.isdigit() or int(p_age) <= 0 or int(p_age) > 120):
            errors.append("Enter a valid age.")

        if errors:
            for e in errors:
                messages.error(request, e)
            return render(request, 'register.html', {'doctors': doctors})

        user_id = request.session.get('user_id')
        user = Userdata.objects.filter(id=user_id).first()

        Registerinfo.objects.create(
            user=user,
            doc_name=doc_name,
            p_name=p_name,
            p_age=int(p_age),
            p_date=p_date,
            gender=gender,
            contact=contact,
            problem=problem,
        )
        return render(request, 'success.html')

    return render(request, 'register.html', {'doctors': doctors})


@login_required_custom
def my_appointments(request):
    user_id = request.session.get('user_id')
    appointments = Registerinfo.objects.filter(user_id=user_id).order_by('-created_at')
    return render(request, 'appointments.html', {'appointments': appointments})
