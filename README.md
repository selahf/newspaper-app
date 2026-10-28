# Tutoring App

Welcome to the Tutoring App!

**Purpose:** This application was created to display tutoring hours in
the "Fish Bowl" located in the Computer Science Department of the
University of Montana.

## Superuser Credentials

During development, you may need to create a new superuser locally to be able to
use it. Here are the credentials I entered; feel free to use them (it is not a
username or password I use for anything else).

**Username:** abc
**Email:** selahf@gmail.com
**Password:** abc

This is my personal email address, so if you need me to authenticate anything, let
me know on Discord right away and I will get to it as soon as possible.

## Test Users

Similarly, I created a test user. Again, you may have to set these up locally if you
want to use them for development and testing. Once again, feel free to use my credentials
or choose your own.

**Username:** user1
**Age:** 20
**Password:** webappdev1

**Username:** user2
**Email Address:** user2@example.com
**Age:** 21
**Password:** webappdev2

Remember that test users cannot login to the admin page because they are not superusers.

## Requirements

This application must:
- Display all tutoring hours by all TAs
- Include a way for TAs to sign up
    - This should include which classes they would like to tutor for
- Include a database of hour, day, and TA
- Allow TAs to add hours that they are available
    - The link to add hours should only be available when signed in as a TA
- Include clickable TAs from the homepage
    - Upon selection, you should be directed to a TA detail page
- TA detail pages with information about the TA (classes they tutor for)

## Chapters

For this assignment, we are expected to use material from Chapters 9-11.

### Chapter 9: Newspaper Project

The content from this chapter will be added by **Carter.**

This chapter is complete when:
- The Django project has been set up
- The GitHub repository has been set up and connected
- A custom user model is created
    - `django_project/settings.py` is updated
    - A new `CustomUser` model is added
    - New forms for `UserCreationForm` and `UserChangeForm` are added
    - `accounts/admin.py` is updated
- A superuser is created and all parts are checked
- Tests are implemented
- Changes are committed to GitHub

### Chapter 10

The content from this chapter will be added by **Selah.**

This chapter is complete when:
- A `templates` directory has been created
- `django_project/settings.py` is updated
- New templates are created
    - `templates/base.html`
    - `templates/home.html`
    - `templates/registration/login.html`
    - `templates/registration/signup.html`
- URL routes are configured
- Logic for the signup form is implemented
- `home.html` is updated
- Admin accounts versus user accounts are tested
- User fields are configured
- Tests are implemented
- Changes are committed

### Chapter 11

The content from this chapter will be added by **Caden.**

This chapter is complete when:
- A `pages` app is added
- `django_project/settings.py` is updated
- `urls.py` and `pages/urls.py` are updated
- `TemplateView` is used in `views.py`
- Tests are implemented
- Bootstrap CSS and Javascript Bundle links are added to `base.html`
- A navigation bar is added to the page
- Styling of buttons is complete
- Django source code is downloaded
- Django Crispy Forms is implemented
    - It is installed
    - `django_project/settings.py` is updated
    - `signup.html` is updated
    - `login.html` is updated
- `requirements.txt` is updated
- Changes are committed

## Authors

This application was developed by:
- Selah
- Carter
- Caden