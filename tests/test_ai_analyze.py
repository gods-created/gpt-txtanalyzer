from dotenv import load_dotenv
from unittest import IsolatedAsyncioTestCase
from services import AIAnalyze
from loguru import logger
from textwrap import dedent

class Tests(IsolatedAsyncioTestCase):
    def setUp(self):
        load_dotenv()
        self.text = dedent('''
            She was carrying some unsightly, unsettling yellow flowers. 
            I am uncertain of their name, but they are the first to appear in Moscow for some reason. 
            These flowers stood out distinctly against her black spring coat. She was carrying yellow flowers! 
            An unfavorable color. She turned from Tverskaya Street into an alley and then turned around. 
            Well, you know Tverskaya Street? Thousands of people were walking along Tverskaya, 
            but I swear she saw only me and looked not so much anxious as if in pain. 
            And I was struck not so much by her beauty as by the extraordinary, unprecedented loneliness in her eyes!
            Obeying this yellow sign, I also turned into the alley and followed in her footsteps.
            We walked silently along the crooked, boring alley, me on one side and her on the other. 
            And imagine, there was not a soul in the alley. 
            I was tormented because I felt I had to talk to her, and I was worried that 
            I wouldn't be able to say a word, and she would leave, and I would never see her again.
        ''').strip()

    async def test_ai_analyze(self):
        async with AIAnalyze() as obj:
            response = await obj.start(self.text)

        logger.debug(response)

        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        self.assertTrue(len(response) > 0)
        self.assertIn('tags', response)
        self.assertIn('sentiment', response)
        self.assertIsInstance(response['tags'], list)
        self.assertTrue(len(response['tags']) > 0)
        self.assertIsInstance(response['sentiment'], str)