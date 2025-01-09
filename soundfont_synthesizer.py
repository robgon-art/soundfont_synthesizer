import pygame
import fluidsynth

# Initialize PyGame
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
BLUE = (0, 0, 255)
WHITE_KEY_WIDTH = 60
WHITE_KEY_HEIGHT = 200
BLACK_KEY_WIDTH = 40
BLACK_KEY_HEIGHT = 120

# Initialize FluidSynth
sf = fluidsynth.Synth()
sf.start(driver="dsound")  # Use "dsound" for Windows

# Load the SoundFont
soundfont_path = "Dore Mark's NY S&S Model B-v5.2.sf2"  # Replace with your SoundFont file path
sfid = sf.sfload(soundfont_path)
if sfid == -1:
    raise RuntimeError(f"Failed to load SoundFont: {soundfont_path}")

# Select the first preset of the SoundFont on channel 0
sf.program_select(0, sfid, 0, 0)

# Map keyboard keys to MIDI notes
KEY_TO_NOTE = {
    pygame.K_a: 60,  # Middle C
    pygame.K_w: 61,  # C#
    pygame.K_s: 62,  # D
    pygame.K_e: 63,  # D#
    pygame.K_d: 64,  # E
    pygame.K_f: 65,  # F
    pygame.K_t: 66,  # F#
    pygame.K_g: 67,  # G
    pygame.K_y: 68,  # G#
    pygame.K_h: 69,  # A
    pygame.K_u: 70,  # A#
    pygame.K_j: 71,  # B
    pygame.K_k: 72,  # High C
}

# Create a screen for capturing events
screen_width = WHITE_KEY_WIDTH * 8  # Adjusted for 8 white keys
screen_height = WHITE_KEY_HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Soundfont Synthesizer")

# Font for key labels
font = pygame.font.SysFont(None, 24)

# Function to draw the keyboard
def draw_keyboard(active_notes):
    screen.fill(GRAY)
    
    # Draw white keys
    white_keys = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K']
    for i, key in enumerate(white_keys):
        x = i * WHITE_KEY_WIDTH
        rect = pygame.Rect(x, 0, WHITE_KEY_WIDTH, WHITE_KEY_HEIGHT)
        note = KEY_TO_NOTE.get(getattr(pygame, f'K_{key.lower()}'))
        if note in active_notes:
            pygame.draw.rect(screen, BLUE, rect)
        else:
            pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)
        label = font.render(key, True, BLACK)
        screen.blit(label, (x + WHITE_KEY_WIDTH // 2 - label.get_width() // 2, WHITE_KEY_HEIGHT - 30))
    
    # Draw black keys
    black_keys = ['W', 'E', 'T', 'Y', 'U']
    black_key_positions = [1, 2, 4, 5, 6]
    for i, (key, pos) in enumerate(zip(black_keys, black_key_positions)):
        x = pos * WHITE_KEY_WIDTH - BLACK_KEY_WIDTH // 2
        rect = pygame.Rect(x, 0, BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT)
        note = KEY_TO_NOTE.get(getattr(pygame, f'K_{key.lower()}'))
        if note in active_notes:
            pygame.draw.rect(screen, BLUE, rect)
        else:
            pygame.draw.rect(screen, BLACK, rect)
        label = font.render(key, True, WHITE)
        screen.blit(label, (x + BLACK_KEY_WIDTH // 2 - label.get_width() // 2, BLACK_KEY_HEIGHT - 30))

    pygame.display.flip()

# Main loop
running = True
active_notes = set()

while running:
    draw_keyboard(active_notes)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press
        elif event.type == pygame.KEYDOWN:
            note = KEY_TO_NOTE.get(event.key)
            if note and note not in active_notes:
                sf.noteon(0, note, 127)  # Channel 0, Note, Velocity
                active_notes.add(note)

        # Key release
        elif event.type == pygame.KEYUP:
            note = KEY_TO_NOTE.get(event.key)
            if note and note in active_notes:
                sf.noteoff(0, note)  # Channel 0, Note
                active_notes.remove(note)

sf.delete()  # Clean up the synthesizer
pygame.quit()
