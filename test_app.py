from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text = True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('TESTING HOMEPAGE ROUTE', html)
            ...


    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            ...
            response = client.post("/api/new-game")
            json_response = response.get_json()

            # Checks whether game id is a string
            self.assertTrue(isinstance(json_response["gameId"], str))

            # Checks whether board is a list
            self.assertTrue(isinstance(json_response["board"], list))

            # Checks whether game id is in the games dict
            self.assertIn(json_response["gameId"], games)


    def test_score_word(self):
        """Test if word is valid"""

        with self.client as client:
            ...
            # make a post request to /api/new-game
            # get the response body as json using .get_json()
            # find that game in the dictionary of games (imported from app.py above)

            # manually change the game board's rows so they are not random

            # test to see that a valid word on the altered board returns {'result': 'ok'}
            # test to see that a valid word not on the altered board returns {'result': 'not-on-board'}
            # test to see that an invalid word returns {'result': 'not-word'}