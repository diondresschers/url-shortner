from urlshort import create_app

def test_shorten(client): # the `client` is the browser.
    response = client.get('/') # the / is the url
    assert b'Shorten' in response.data # Look for the text `Shorten` in the localhost:5000/ webbrowser.

