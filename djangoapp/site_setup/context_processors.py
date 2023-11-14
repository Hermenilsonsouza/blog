from site_setup.models import SiteSetup

def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()

    print(setup)

    return {
        'site_setup': setup
    }


