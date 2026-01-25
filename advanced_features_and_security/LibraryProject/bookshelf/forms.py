from django import forms


class BookSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        max_length=100,
        strip=True,
        help_text="Search by title or author",
    )