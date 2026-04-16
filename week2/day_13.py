import asyncio

async def get_restaurant_menu(restaurant_id):
    print(f"Loading Menu For {restaurant_id}...")
    await asyncio.sleep(1)
    return {"restaurant": restaurant_id, "items": ["Burger", "Pizza"]}


async def get_user_location(user_id):
    print(f"Getting Location for user {user_id}...")
    await asyncio.sleep(0.5)
    return {"lat": 11.0168, "lng": 76.9558}


async def get_delivery_partners():
    print("Finding Delivery partners...")
    await asyncio.sleep(0.8)
    return ["Partner 1", "Partner 2"]

async def load_swiggy_home(user_id, restaurant_id):
    menu, location, partners = await asyncio.gather(
        get_restaurant_menu(restaurant_id),
        get_user_location(user_id),
        get_delivery_partners()
    )
    print(f"\nPage loaded!")
    print(f"Menu: {menu['items']}")
    print(f"Location: {location}")
    print(f"Partners: {partners}")

asyncio.run(load_swiggy_home(1, 102))

