from playwright.sync_api import Page, expect

# Tests for your routes go here
# def test_get_albums(page, test_web_address, db_connection): 
#     db_connection.seed("seeds/music_web_app.sql")
#     page.goto(f"http://{test_web_address}/albums")

#     div_tags = page.locator("div")

#     expect(div_tags).to_have_text([
#         "title: Death Magnetic \nReleased: 2008",
#         "title: Rocket Ride \nReleased: 2006",
#         "title: King of Fools \nReleased: 2004"
#     ])

def test_get_albums_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/albums/2")

    div_tags = page.locator("p")

    expect(div_tags).to_have_text([
        "Released: 2006 Artist: 2"
    ])

def test_album_specific_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text='Rocket Ride'")

    h1_tag = page.locator("h1")
    p = page.locator("p")
    expect(h1_tag).to_have_text("Album: Rocket Ride")
    expect(p).to_have_text("Released: 2006 Artist: 2")

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
