import pygame
import threading

class MusicPlayer:
    def __init__(self, music_file):
        self.music_file = music_file
        self.thread = None
        self.stop_event = threading.Event()

    def play_music(self):
        print("Initializing mixer")
        pygame.mixer.init()
        print(f"Loading music file: {self.music_file}")
        pygame.mixer.music.load(self.music_file)
        print("Starting music playback")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        # Wait for stop event to be set, allowing the thread to be interruptible
        while not self.stop_event.is_set():
            pygame.time.wait(100)  # Wait a bit, check again

        pygame.mixer.music.stop()  # Stop the music if stop_event is set

    def start(self):
        """Start music playback in a daemon thread."""
        if self.thread is None or not self.thread.is_alive():
            self.stop_event.clear()  # Ensure the stop event is cleared
            self.thread = threading.Thread(target=self.play_music, daemon=True)
            self.thread.start()

    def stop(self):
        """Stop music playback."""
        if self.thread is not None:
            self.stop_event.set()  # Signal the thread to stop
            self.thread.join()  # Wait for the thread to finish