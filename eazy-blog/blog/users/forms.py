from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label= (""),
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                        'placeholder': 'Username',
                                        'required': 'true',
                                        "autocomplete":"off",
        }),

    )
    first_name = forms.CharField(max_length=60,
        label= (""),
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                    'type': 'text',
                                    'placeholder': 'First name',
                                    "autocomplete":"off",
                                    'required': 'true',
        }),
    )
    last_name = forms.CharField(max_length=60,
        label= (""),
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                    'type': 'text',
                                    'placeholder': 'Last name',
                                    'required': 'true',
                                    "autocomplete":"off",
        }),
    )

    email = forms.CharField( max_length=255,
        label= (""),
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                    'type': 'email',
                                    'placeholder': 'Email address',
                                    'required': 'true',
                                    "autocomplete":"off",
        }),
    )

    password1 = forms.RegexField( label=(""), max_length=30, regex=r"^[\w.@+-]+$",
    help_text=("Required. 30 characters or fewer. Letters, digits and "
                "@/./+/-/_ only."),
    error_messages={
        'invalid': ("This value may contain only letters, numbers and "
                     "@/./+/-/_ characters.")},
    widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg',
                                      'type': 'password',
                                        'required': 'true',
                                        'placeholder': 'Password',
                                        "autocomplete":"off",
    }),
    )

    password2 = forms.RegexField( label=(""), max_length=30, regex=r"^[\w.@+-]+$",
    help_text=("Required. 30 characters or fewer. Letters, digits and "
                "@/./+/-/_ only."),
    error_messages={
        'invalid': ("This value may contain only letters, numbers and "
                     "@/./+/-/_ characters.")},
    widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg',
                                    'type': 'password',
                                    'required': 'true',
                                    'placeholder': 'Confirm your password',
                                    "autocomplete":"off",
                                    
    }),
    )

    class Meta:
        model = User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class LogInForm(AuthenticationForm):
    username = forms.CharField(label=(""),
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Username',
            'required': 'true',
            "autocomplete":"off",
        })
    )
    password = forms.CharField(label=(""),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Password',
            'required': 'true',
            "autocomplete":"off",
        })
    )


