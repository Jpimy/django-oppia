from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum, Count
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from oppia.models import Course
from summary.models import UserCourseSummary


@method_decorator(staff_member_required, name='dispatch')
class CompletionRates(TemplateView):

    def get(self, request):

        courses = Course.objects.filter(is_draft=False,
                                        is_archived=False).order_by('title')

        courses_list = []
        course_stats = list(UserCourseSummary.objects
                            .filter(course__in=courses)
                            .values('course')
                            .annotate(users=Count('user'),
                                      completed=Sum('badges_achieved')))

        for course in courses:
            obj = {}
            obj['course'] = course

            for stats in course_stats:
                if stats['course'] == course.id:
                    no_users = stats['users']
                    obj['enroled'] = no_users
                    if no_users > 0:
                        obj['completion'] = (float(stats['completed'])
                                             / float(no_users)) * 100
                    else:
                        obj['completion'] = 0
                    # remove the element to optimize next searches
                    course_stats.remove(stats)

            courses_list.append(obj)

        return render(request, 'reports/completion_rates.html',
                      {'courses_list': courses_list})