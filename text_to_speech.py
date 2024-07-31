from gtts import gTTS
import pygame
import os
import tempfile

def text_to_speech(text, language=['en', 'fr']):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')as fp:
        tts=gTTS(text=text, lang=language)
        tts.save(fp.name)
        fp_name=fp.name


    pygame.mixer.init()
    pygame.mixer.music.load(fp_name)    
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)



    pygame.mixer.music.stop() 
    os.unlink(fp_name)    
