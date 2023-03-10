from unittest import TestCase
from xebia_email_signature.signature import (
    render_template,
    validate_html,
    add_office_details,
)


class Test(TestCase):
    def setUp(self) -> None:
        self.employee_details = {
            "full_name": "John Doe",
            "email": "john.doe@xebia.com",
            "phone": "+31 6 12 34 56 78",
            "job_role": "Consultant",
            "linkedin_url": "https://linkedin.com/user",
            "unit": "Xebia Cloud",
            "github_url": "https://github.com/user",
        }
        self.employee_details = add_office_details(self.employee_details)

    def test_official_template(self):
        rendered_output = render_template(self.employee_details, "signature.html.jinja")
        _ = validate_html(rendered_output)

    def test_unofficial_template(self):
        rendered_output = render_template(
            self.employee_details, "simple-signature.html.jinja"
        )
        _ = validate_html(rendered_output)
