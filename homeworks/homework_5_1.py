class BaseView:
    def render(self):
        print("Template render")

class LoggingMixin:
    def render(self):
        print("Log: start")
        super().render()
        print("Log: end")

class AuthRequiredMixin:
    def __init__(self, authed=True):
        self.authed = authed

    def render(self):
        if not self.authed:
            print("Access denied")
            return
        print("Auth OK")
        super().render()

class AdminPageView(LoggingMixin, AuthRequiredMixin, BaseView):
    def __init__(self, authed=True):
       super().__init__(authed)

    def render(self):
        print("Admin page render start")
        super().render()
        print("Admin page render end")

print(AdminPageView.__mro__)
print("=======================")
admin_page = AdminPageView(authed=True)
admin_page.render()
print("=======================")
admin_page = AdminPageView(authed=False)
admin_page.render()




