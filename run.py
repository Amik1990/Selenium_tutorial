from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.confirm_cookies()
    bot.change_currency()
    # bot.select_place_to_go("New York")


