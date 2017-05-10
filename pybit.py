#!/usr/bin/env python

import fitbit
from tethig.vault import consumer_key, consumer_secret, access_token, refresh_token, user_id
from datetime import date
from dateutil.relativedelta import relativedelta

authd_client = fitbit.Fitbit(consumer_key, consumer_secret, access_token=access_token, refresh_token=refresh_token)
authd_client.sleep()

with open("heartdata.json", "w") as outfile:
    for i in range(7):
        start_date = date(2017, 5, 1) + relativedelta(days=+i)
        base_date = start_date.strftime('%Y-%m-%d')
        heart_data = authd_client.intraday_time_series(resource='activities/heart', base_date=base_date, detail_level='1sec')
        print(heart_data, file = outfile)


# fitbit_stats = authd_client._COLLECTION_RESOURCE(user_id=user_id, resource='activities', date='2017-05-05')
# date.today
