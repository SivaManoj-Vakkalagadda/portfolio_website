
# # Create your views here.
# from django.shortcuts import render

# def index(request):
#     # Data to pass in for all sections
#     data = {
#         'profile': {
#             "image": "images/profile.jpg",
#             "text_lines": [
#                 {"bold": True, "content": "Siva Manoj"},
#                 {"bold": False, "content": "A passionate fullstack developer with expertise in Python and Django."},
#                 {"bold": False, "content": "Loves coding, solving problems, and open source."}
#             ]
#         },
#         'intro_text': "Hi, this is Mr. Volt, a developer with a strong passion for creating efficient and elegant software solutions.",
#         'coding_profiles': [
#             {"image": "images/leetcode.png", "name": "LeetCode",  "url": "https://leetcode.com/username"},
#             {"image": "images/codeforces.png", "name": "Codeforces", "url": "https://codeforces.com/profile/username"},
#             {"image": "images/github.png", "name": "GitHub", "url": "https://github.com/username"},
#         ],
#         'skills': [
#             {"image": "images/skill_js.png", "name": "C++", "category": "Programming Language"},
#             {"image": "images/skill_js.png", "name": "C", "category": "Programming Language"},
#             {"image": "images/skill_python.png", "name": "Python", "category": "Programming Language"},
#             {"image": "images/skill_js.png", "name": "JavaScript", "category": "Programming Language"},
#             {"image": "images/skill_js.png", "name": "HTML", "category": "Programming Language"},
#             {"image": "images/skill_js.png", "name": "CSS", "category": "Programming Language"},
#             # Add more skills here...
#         ],
#         'projects': [
#             {
#                 "title": "Portfolio Website",
#                 "desc": "Personal website to showcase portfolio and skills",
#                 "tech": "Django, HTML, CSS, JavaScript",
#                 "url": "https://github.com/username/portfolio",
#             },
#             {
#                 "title": "Blog Platform",
#                 "desc": "A full-featured blogging platform",
#                 "tech": "Django, SQLite, Bootstrap",
#                 "url": "https://github.com/username/blog-platform",
#             },
#             {
#                 "title": "Mess App",
#                 "desc": "A full-featured blogging platform",
#                 "tech": "Django, SQLite, Bootstrap",
#                 "url": "https://github.com/username/blog-platform",
#             },
#             # Add more projects here...
#         ],
#         'contact': {
#             "phone": "91 8919 376709",
#             "email": "vakkalagadda.siva.23031@iitgoa.ac.in",
#             "instagram": "https://instagram.com/username",
#             "twitter": "https://twitter.com/username",
#             "linkedin": "https://linkedin.com/in/username",
#         }
#     }
#     return render(request, "index.html", data)

from django.shortcuts import render, get_object_or_404
from .models import Profile, CodingProfile, Skill, Project, ContactInfo

def index(request):
    # Assume there is only one Profile instance
    profile = Profile.objects.first()

    coding_profiles = CodingProfile.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    contact = ContactInfo.objects.first()

    # Prepare data structure compatible with template

    # For profile text lines, you can split description and extra_info into lines
    text_lines = []
    if profile:
        # First line bold = name
        text_lines.append({"bold": True, "content": profile.name})
        if profile.description:
            text_lines.append({"bold": False, "content": profile.description})
        if profile.extra_info:
            # Split by newline to paragraphs
            for para in profile.extra_info.split('\n'):
                if para.strip():
                    text_lines.append({"bold": False, "content": para.strip()})

    context = {
        'profile': {
            'image': profile.image.url if profile and profile.image else '',
            'text_lines': text_lines
        },
        'intro_text': "I am a third-year undergraduate student at the Indian Institute of Technology Goa with a strong interest in the field of Machine Learning. I am passionate about exploring intelligent systems and applying data-driven approaches to solve real-world problems.",
        'coding_profiles': coding_profiles,
        'skills': skills,
        'projects': projects,
        'contact': contact,
    }
    return render(request, "index.html", context)