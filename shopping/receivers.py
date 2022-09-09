import datetime


def post_save_update_price_date_receiver(sender, instance=None, created=False, **kwargs):
    if not created:
        instance.price_date = datetime.datetime.now()
        instance.save()
