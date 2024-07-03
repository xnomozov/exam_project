from jet.dashboard.modules import DashboardModule
from django.utils.translation import gettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


class MyCustomDashboardModule(DashboardModule):
    # Customize your dashboard module here
    title = 'My Custom Dashboard Module'
    template = 'path_to_custom_template.html'
    # Add more customization options as needed


