import pygame
import os
from sys import exit


def main():
    pygame.init()

    # Get the base path (absolute path to the runner_game directory)
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Paths to the assets within the runner_game directory
    font_path = os.path.join(base_path, "font", "Pixeltype.ttf")
    test_font = pygame.font.Font(font_path, 50)

    # Initialize screen, clock, and music
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption(" 🏃 The Runner 🏃")
    clock = pygame.time.Clock()

    # Path to the music file
    music_path = os.path.join(base_path, "..", "audio", "music.wav")
    music = pygame.mixer.Sound(music_path)
    music.play(loops=1)

    # Paths to the graphics
    sky_surface = pygame.image.load(
        os.path.join(base_path, "graphics", "sky.png")
    ).convert()
    ground_surface = pygame.image.load(
        os.path.join(base_path, "graphics", "ground.png")
    ).convert()
    snail_surf = pygame.image.load(
        os.path.join(base_path, "graphics", "snail", "snail1.png")
    ).convert_alpha()
    player_surf = pygame.image.load(
        os.path.join(base_path, "graphics", "player", "player_walk_1.png")
    ).convert_alpha()
    player_surf2 = pygame.image.load(
        os.path.join(base_path, "graphics", "player", "player_walk_2.png")
    ).convert_alpha()
    game_over = pygame.image.load(
        os.path.join(base_path, "graphics", "game_over.jpg")
    ).convert()

    # Game variables
    player_run = [player_surf, player_surf2]
    player_rect = player_surf.get_rect(midbottom=(100, 300))
    player_gravity = 0
    game_active = True
    start_time = 0
    snail_rect = snail_surf.get_rect(midbottom=(800, 300))

    def display_score():
        current_time = int(pygame.time.get_ticks() / 1000) - start_time
        score_surf = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
        score_rect = score_surf.get_rect(center=(400, 50))
        screen.blit(score_surf, score_rect)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                        player_gravity = -20
            else:
                if event.type == pygame.KEYDOWN:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            screen.blit(sky_surface, (0, 0))
            screen.blit(ground_surface, (0, 300))
            display_score()

            snail_rect.x -= 6
            if snail_rect.right <= 0:
                snail_rect.left = 800
            screen.blit(snail_surf, snail_rect)

            player_gravity += 1
            player_rect.y += player_gravity
            if player_rect.bottom >= 300:
                player_rect.bottom = 300
            screen.blit(player_surf, player_rect)

            if snail_rect.colliderect(player_rect):
                game_active = False
        else:
            screen.fill((100, 150, 220))
            screen.blit(game_over, (90, 35))

        pygame.display.update()
        clock.tick(40)


if __name__ == "__main__":
    main()
