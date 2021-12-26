import hashlib

from allauth.account.signals import user_signed_up, user_logged_in
from django.dispatch.dispatcher import receiver

from .models import Profile

@receiver(user_signed_up)
def social_login_fname_lname_profilepic(sociallogin, user, **kwargs):
    preferred_avatar_size_pixels=256

    picture_url = "http://www.gravatar.com/avatar/{0}?s={1}".format(
        hashlib.md5(user.email.encode('UTF-8')).hexdigest(),
        preferred_avatar_size_pixels
    )

    if sociallogin:
        # Extract first / last names from social nets and store on User record

        if sociallogin.account.provider == 'facebook':
            # f_name = sociallogin.account.extra_data['first_name']
            # l_name = sociallogin.account.extra_data['last_name']
            # if f_name:
                # user.first_name = f_name
            # if l_name:
                # user.last_name = l_name
                            #verified = sociallogin.account.extra_data['verified']
            picture_url = "http://graph.facebook.com/{0}/picture?width={1}&height={1}".format(
                sociallogin.account.uid, preferred_avatar_size_pixels)

        if sociallogin.account.provider == 'google':
            # f_name = sociallogin.account.extra_data['given_name']
            # l_name = sociallogin.account.extra_data['family_name']
            # if f_name:
                # user.first_name = f_name
            # if l_name:
                # user.last_name = l_name
            #verified = sociallogin.account.extra_data['verified_email']
            picture_url = sociallogin.account.extra_data['picture']

    user.save()
    profile = Profile(user=user, social_img=picture_url)
    profile.save() 
